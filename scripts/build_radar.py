"""Converte registros Markdown do Radar em artefatos estáticos públicos."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path


SCHEMA_VERSION = "1.0"
RECORD = re.compile(
    r"^### (?P<date>\d{4}-\d{2}-\d{2}) (?P<time>\d{2}:\d{2}) BRT — (?P<title>.+)$",
    re.MULTILINE,
)
LINK = re.compile(r"\[([^\]]+)\]\((https?://[^)]+)\)")
RELATION = re.compile(r"\[\[([^\]]+)\]\]")
TAG = re.compile(r"#([\w-]+)")


def _bullet_value(block: str, name: str) -> str | None:
    match = re.search(rf"^- {re.escape(name)}:\s*(.+)$", block, re.MULTILINE)
    return match.group(1).strip() if match else None


def _item_id(url: str) -> str:
    return "radar-" + hashlib.sha256(url.encode("utf-8")).hexdigest()[:16]


def parse_document(document: str) -> dict:
    """Retorna registros válidos e os blocos que exigem revisão manual."""
    items = []
    quarantine = []
    matches = list(RECORD.finditer(document))
    for index, match in enumerate(matches):
        block_end = matches[index + 1].start() if index + 1 < len(matches) else len(document)
        block = document[match.start() : block_end]
        title = match.group("title").strip()
        source = _bullet_value(block, "Fonte")
        if title.lower() in {"sem_novidade", "nenhuma novidade de alto sinal"}:
            continue
        source_link = LINK.search(source or "")
        if not source_link:
            quarantine.append({"title": title, "reason": "missing_source_url"})
            continue
        tags = _bullet_value(block, "Tags") or ""
        relations = _bullet_value(block, "Relações") or ""
        items.append(
            {
                "id": _item_id(source_link.group(2)),
                "edition_at": f"{match.group('date')}T{match.group('time')}:00-03:00",
                "edition_date": match.group("date"),
                "title": title,
                "source": source_link.group(1),
                "url": source_link.group(2),
                "published": _bullet_value(block, "Publicado") or "não informado",
                "why_it_matters": _bullet_value(block, "Por que importa") or "não informado",
                "tags": TAG.findall(tags),
                "relations": RELATION.findall(relations),
                "confidence": _bullet_value(block, "Confiança") or "não informada",
            }
        )
    return {"items": items, "quarantine": quarantine}


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
    ET.SubElement(channel, "link").text = "./"
    for item in items:
        entry = ET.SubElement(channel, "item")
        ET.SubElement(entry, "title").text = item["title"]
        ET.SubElement(entry, "link").text = item["url"]
        ET.SubElement(entry, "guid", isPermaLink="false").text = item["id"]
        ET.SubElement(entry, "description").text = item["why_it_matters"]
        ET.SubElement(entry, "pubDate").text = item["edition_at"]
        ET.SubElement(entry, "category").text = ", ".join(item["tags"])
    return root


def build_artifacts(report: dict, output_dir: Path) -> None:
    """Escreve todos os artefatos em um diretório já validado pelo chamador."""
    items = sorted(report["items"], key=lambda item: item["edition_at"], reverse=True)
    radar_dir = output_dir / "v1" / "radar"
    grouped = defaultdict(list)
    for item in items:
        grouped[item["edition_date"]].append(item)

    canonical = {"schema_version": SCHEMA_VERSION, "items": items}
    _write_json(radar_dir / "radar-canonico.json", canonical)
    for edition_date, edition_items in grouped.items():
        _write_json(
            radar_dir / "editions" / f"{edition_date}.json",
            {"schema_version": SCHEMA_VERSION, "edition_date": edition_date, "items": edition_items},
        )

    latest_date = max(grouped, default=None)
    latest_items = grouped[latest_date] if latest_date else []
    _write_json(
        radar_dir / "latest.json",
        {"schema_version": SCHEMA_VERSION, "edition_date": latest_date, "items": latest_items},
    )
    rss_path = radar_dir / "feed.xml"
    ET.ElementTree(_rss(items[:50])).write(rss_path, encoding="utf-8", xml_declaration=True)

    files = sorted(path for path in radar_dir.rglob("*") if path.is_file())
    _write_json(
        radar_dir / "manifest.json",
        {
            "schema_version": SCHEMA_VERSION,
            "item_count": len(items),
            "edition_count": len(grouped),
            "quarantine_count": len(report["quarantine"]),
            "files": {str(path.relative_to(output_dir)): _file_hash(path) for path in files},
        },
    )
    _write_json(radar_dir / "quarantine.json", {"items": report["quarantine"]})


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("--output", type=Path, default=Path("public"))
    args = parser.parse_args()
    report = parse_document(args.source.read_text())
    build_artifacts(report, args.output)
    print(f"{len(report['items'])} itens; {len(report['quarantine'])} em quarentena")


if __name__ == "__main__":
    main()
