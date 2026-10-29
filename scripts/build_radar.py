"""Converte registros Markdown do Radar em artefatos estáticos públicos."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import tempfile
import xml.etree.ElementTree as ET
from collections import defaultdict
from datetime import datetime
from email.utils import format_datetime
from pathlib import Path


SCHEMA_VERSION = "1.0"
SITE_URL = "https://radar-publico-opal.vercel.app"
RECORD = re.compile(
    r"^### (?P<date>\d{4}-\d{2}-\d{2}) (?P<time>\d{2}:\d{2}) BRT — (?P<title>.+)$",
    re.MULTILINE,
)
LINK = re.compile(r"\[([^\]]+)\]\((https?://[^)]+)\)")
RELATION = re.compile(r"\[\[([^\]]+)\]\]")
TAG = re.compile(r"#([\w-]+)")


def _bullet_value(block: str, name: str) -> str | None:
    prefix = f"- {name}:"
    lines = block.splitlines()
    for index, line in enumerate(lines):
        if not line.startswith(prefix):
            continue
        value = [line.removeprefix(prefix).strip()]
        for continuation in lines[index + 1 :]:
            if continuation.startswith("- "):
                break
            value.append(continuation.strip())
        return "\n".join(value).strip()
    return None


def _item_id(url: str) -> str:
    return "radar-" + hashlib.sha256(url.encode("utf-8")).hexdigest()[:16]


def parse_document(document: str) -> dict:
    """Retorna registros válidos e os blocos que exigem revisão manual."""
    items = []
    quarantine = []
    empty_editions = []
    matches = list(RECORD.finditer(document))
    for index, match in enumerate(matches):
        block_end = matches[index + 1].start() if index + 1 < len(matches) else len(document)
        block = document[match.start() : block_end]
        title = match.group("title").strip()
        source = _bullet_value(block, "Fonte")
        if title.lower() in {"sem_novidade", "nenhuma novidade de alto sinal"}:
            empty_editions.append(
                {
                    "edition_date": match.group("date"),
                    "edition_at": f"{match.group('date')}T{match.group('time')}:00-03:00",
                }
            )
            continue
        source_link = LINK.search(source or "")
        if not source_link:
            quarantine.append({"title": title, "reason": "missing_source_url"})
            continue
        tags = _bullet_value(block, "Tags") or ""
        relations = _bullet_value(block, "Relações") or ""
        impact = _bullet_value(block, "Por que importa") or "não informado"
        items.append(
            {
                "id": _item_id(source_link.group(2)),
                "edition_at": f"{match.group('date')}T{match.group('time')}:00-03:00",
                "edition_date": match.group("date"),
                "title": title,
                "source": source_link.group(1),
                "url": source_link.group(2),
                "published": _bullet_value(block, "Publicado") or "não informado",
                "summary": _bullet_value(block, "Resumo") or impact,
                "why_it_matters": impact,
                "tags": TAG.findall(tags),
                "relations": RELATION.findall(relations),
                "confidence": _bullet_value(block, "Confiança") or "não informada",
            }
        )
    return {"items": items, "quarantine": quarantine, "empty_editions": empty_editions}


def _write_json(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n")


def _file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _rss(items: list[dict]) -> ET.Element:
    root = ET.Element("rss", version="2.0")
    channel = ET.SubElement(root, "channel")
    ET.SubElement(channel, "title").text = "Radar IA, GeoIA e Setores"
    ET.SubElement(channel, "description").text = "Radar técnico público"
    ET.SubElement(channel, "link").text = SITE_URL
    for item in items:
        entry = ET.SubElement(channel, "item")
        ET.SubElement(entry, "title").text = item["title"]
        ET.SubElement(entry, "link").text = item["url"]
        ET.SubElement(entry, "guid", isPermaLink="false").text = item["id"]
        ET.SubElement(entry, "description").text = item["summary"]
        ET.SubElement(entry, "pubDate").text = format_datetime(
            datetime.fromisoformat(item["edition_at"])
        )
        ET.SubElement(entry, "category").text = ", ".join(item["tags"])
    return root


def _build_radar_dir(report: dict, radar_dir: Path) -> None:
    items = sorted(report["items"], key=lambda item: item["edition_at"], reverse=True)
    grouped = defaultdict(list)
    for item in items:
        grouped[item["edition_date"]].append(item)

    edition_dates = set(grouped)
    empty_dates = {edition["edition_date"] for edition in report["empty_editions"]}
    edition_dates.update(empty_dates)

    canonical = {"schema_version": SCHEMA_VERSION, "items": items}
    _write_json(radar_dir / "radar-canonico.json", canonical)
    for edition_date in sorted(edition_dates):
        edition_items = grouped[edition_date]
        _write_json(
            radar_dir / "editions" / f"{edition_date}.json",
            {
                "schema_version": SCHEMA_VERSION,
                "edition_date": edition_date,
                "status": "publicado" if edition_items else "sem_novidade",
                "items": edition_items,
            },
        )

    latest_date = max(edition_dates, default=None)
    latest_items = grouped[latest_date] if latest_date else []
    _write_json(
        radar_dir / "latest.json",
        {
            "schema_version": SCHEMA_VERSION,
            "edition_date": latest_date,
            "status": "publicado" if latest_items else "sem_novidade",
            "items": latest_items,
        },
    )
    rss_path = radar_dir / "feed.xml"
    ET.ElementTree(_rss(items[:50])).write(rss_path, encoding="utf-8", xml_declaration=True)

    _write_json(radar_dir / "quarantine.json", {"items": report["quarantine"]})
    files = sorted(path for path in radar_dir.rglob("*") if path.is_file())
    _write_json(
        radar_dir / "manifest.json",
        {
            "schema_version": SCHEMA_VERSION,
            "item_count": len(items),
            "edition_count": len(edition_dates),
            "quarantine_count": len(report["quarantine"]),
            "files": {
                str(Path("v1/radar") / path.relative_to(radar_dir)): _file_hash(path)
                for path in files
            },
        },
    )


def build_artifacts(report: dict, output_dir: Path, fail_on_quarantine: bool = False) -> None:
    """Gera em staging e substitui o radar somente depois de validá-lo."""
    if fail_on_quarantine and report["quarantine"]:
        raise ValueError("quarentena não vazia; publicação cancelada")
    radar_parent = output_dir / "v1"
    radar_parent.mkdir(parents=True, exist_ok=True)
    target = radar_parent / "radar"
    with tempfile.TemporaryDirectory(dir=radar_parent, prefix=".radar-staging-") as temporary_directory:
        staging = Path(temporary_directory) / "radar"
        _build_radar_dir(report, staging)
        for path in staging.rglob("*.json"):
            json.loads(path.read_text())
        ET.parse(staging / "feed.xml")

        backup = radar_parent / ".radar-previous"
        if backup.exists():
            shutil.rmtree(backup)
        if target.exists():
            target.replace(backup)
        staging.replace(target)
        if backup.exists():
            shutil.rmtree(backup)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("--output", type=Path, default=Path("public"))
    parser.add_argument("--fail-on-quarantine", action="store_true")
    args = parser.parse_args()
    report = parse_document(args.source.read_text())
    build_artifacts(report, args.output, args.fail_on_quarantine)
    print(f"{len(report['items'])} itens; {len(report['quarantine'])} em quarentena")


if __name__ == "__main__":
    main()
