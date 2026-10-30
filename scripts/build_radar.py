"""Converte registros Markdown do Radar em artefatos estáticos públicos."""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import shutil
import tempfile
import xml.etree.ElementTree as ET
from collections import defaultdict
from datetime import datetime, timedelta
from email.utils import format_datetime
from pathlib import Path
from urllib.parse import urlparse


SCHEMA_VERSION = "1.0"
SITE_URL = "https://radar-publico-opal.vercel.app"
FEED_URL = f"{SITE_URL}/v1/radar/feed.xml"
FEED_TITLE = "Radar IA, GeoIA e Setores"
ATOM_NS = "http://www.w3.org/2005/Atom"
CONTENT_NS = "http://purl.org/rss/1.0/modules/content/"
ET.register_namespace("atom", ATOM_NS)
ET.register_namespace("content", CONTENT_NS)
METHODOLOGY = {
    "version": "1",
    "summary": "Edição diária com seleção editorial de novidades de alto sinal, deduplicação e fontes rastreáveis.",
}
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


def _suffix_id(url: str, discriminator: str) -> str:
    return "radar-" + hashlib.sha256(f"{url}\n{discriminator}".encode("utf-8")).hexdigest()[:16]


def _unique_ids(items: list[dict]) -> list[dict]:
    """Garante ids únicos. A matéria mais antiga de cada URL mantém o id original (guid estável)."""
    seen: set[str] = set()
    ids: dict[int, str] = {}
    for position in sorted(range(len(items)), key=lambda i: (items[i]["edition_at"], items[i]["title"])):
        item = items[position]
        candidate = item["id"]
        if candidate in seen:
            candidate = _suffix_id(item["url"], item["title"])
        if candidate in seen:
            candidate = _suffix_id(item["url"], f"{item['title']}\n{item['edition_at']}")
        seen.add(candidate)
        ids[position] = candidate
    return [{**item, "id": ids[position]} for position, item in enumerate(items)]


def _public_item(item: dict) -> dict:
    """Remove campos internos (relações com projetos) dos arquivos públicos."""
    return {key: value for key, value in item.items() if key != "relations"}


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
                "source_meta": {"domain": urlparse(source_link.group(2)).hostname or ""},
                "url": source_link.group(2),
                "published": _bullet_value(block, "Publicado") or "não informado",
                "summary": _bullet_value(block, "Resumo") or impact,
                "why_it_matters": impact,
                "tags": TAG.findall(tags),
                "relations": RELATION.findall(relations),
                "confidence": _bullet_value(block, "Confiança") or "não informada",
            }
        )
    return {"items": _unique_ids(items), "quarantine": quarantine, "empty_editions": empty_editions}


def _write_json(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n")


def _file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


INLINE_CODE = re.compile(r"`([^`]+)`")


def _plain_text(value: str) -> str:
    return value.replace("`", "")


def _html_text(value: str) -> str:
    return INLINE_CODE.sub(r"<code>\1</code>", html.escape(value, quote=False))


PUBLISHED = re.compile(r"^(\d{4})-(\d{2})-(\d{2})(?:[ T](\d{2}:\d{2}))?")
UNKNOWN_VALUES = {"não informado", "não informada"}


def _published_label(text: str) -> str | None:
    """Data (e hora, quando existe) de Publicado, sem as ressalvas em texto livre."""
    match = PUBLISHED.match(text.strip())
    if not match:
        return None
    year, month, day, time = match.groups()
    return f"{day}/{month}/{year}" + (f" {time}" if time else "")


def _metadata_line(item: dict) -> str | None:
    parts = []
    confidence = item.get("confidence", "")
    if confidence and confidence not in UNKNOWN_VALUES:
        parts.append(f"Confiança: {confidence}")
    published = _published_label(item.get("published", ""))
    if published:
        parts.append(f"Publicado: {published}")
    if item.get("tags"):
        parts.append("Tags: " + ", ".join(item["tags"]))
    if not parts:
        return None
    return "<p><small>" + html.escape(" · ".join(parts), quote=False) + "</small></p>"


def _content_html(item: dict) -> str:
    parts = [f"<p>{_html_text(paragraph)}</p>" for paragraph in item["summary"].split("\n\n") if paragraph.strip()]
    if item.get("why_it_matters"):
        parts.append(f"<p><strong>Por que importa:</strong> {_html_text(item['why_it_matters'])}</p>")
    link = html.escape(item["url"], quote=True)
    parts.append(f'<p>Fonte: <a href="{link}">{html.escape(item["source"], quote=False)}</a></p>')
    metadata = _metadata_line(item)
    if metadata:
        parts.append(metadata)
    return "\n".join(parts)


def _staggered_dates(items: list[dict]) -> list[str]:
    """pubDate por item: horário da edição + segundos que preservam a ordem editorial (1º = mais recente)."""
    sizes = defaultdict(int)
    for item in items:
        sizes[item["edition_at"]] += 1
    seen = defaultdict(int)
    dates = []
    for item in items:
        seen[item["edition_at"]] += 1
        offset = sizes[item["edition_at"]] - seen[item["edition_at"]]
        dates.append(format_datetime(datetime.fromisoformat(item["edition_at"]) + timedelta(seconds=offset)))
    return dates


def _rfc822(edition_at: str) -> str:
    return format_datetime(datetime.fromisoformat(edition_at))


def _rss(items: list[dict]) -> ET.Element:
    root = ET.Element("rss", version="2.0")
    channel = ET.SubElement(root, "channel")
    ET.SubElement(channel, "title").text = FEED_TITLE
    ET.SubElement(channel, "description").text = (
        "Radar técnico público de IA, GeoIA e setores, com seleção editorial diária e fontes rastreáveis."
    )
    ET.SubElement(channel, "link").text = SITE_URL
    ET.SubElement(channel, f"{{{ATOM_NS}}}link", href=FEED_URL, rel="self", type="application/rss+xml")
    ET.SubElement(channel, "language").text = "pt-BR"
    if items:
        newest = max(items, key=lambda item: datetime.fromisoformat(item["edition_at"]))
        ET.SubElement(channel, "lastBuildDate").text = _rfc822(newest["edition_at"])
    image = ET.SubElement(channel, "image")
    ET.SubElement(image, "url").text = f"{SITE_URL}/icon.png"
    ET.SubElement(image, "title").text = FEED_TITLE
    ET.SubElement(image, "link").text = SITE_URL
    for item, pub_date in zip(items, _staggered_dates(items)):
        entry = ET.SubElement(channel, "item")
        ET.SubElement(entry, "title").text = item["title"]
        ET.SubElement(entry, "link").text = item["url"]
        ET.SubElement(entry, "guid", isPermaLink="false").text = item["id"]
        ET.SubElement(entry, "description").text = _plain_text(item["summary"])
        ET.SubElement(entry, f"{{{CONTENT_NS}}}encoded").text = _content_html(item)
        ET.SubElement(entry, "pubDate").text = pub_date
        for tag in item["tags"]:
            ET.SubElement(entry, "category").text = tag
    return root


def _metrics(items: list[dict]) -> dict:
    return {
        "signals": len(items),
        "sources": len({item["source_meta"]["domain"] for item in items}),
        "high_confidence": sum(item["confidence"] == "alta" for item in items),
    }


def _edition_payload(edition_date: str | None, items: list[dict], generated_at: str | None) -> dict:
    return {
        "schema_version": SCHEMA_VERSION,
        "edition_id": f"radar-{generated_at}" if generated_at else None,
        "edition_date": edition_date,
        "generated_at": generated_at,
        "status": "publicado" if items else "sem_novidade",
        "metrics": _metrics(items),
        "methodology": METHODOLOGY,
        "items": items,
    }


def _build_radar_dir(report: dict, radar_dir: Path) -> None:
    items = sorted(
        (_public_item(item) for item in report["items"]),
        key=lambda item: item["edition_at"],
        reverse=True,
    )
    grouped = defaultdict(list)
    for item in items:
        grouped[item["edition_date"]].append(item)

    edition_dates = set(grouped)
    empty_editions = {
        edition["edition_date"]: edition["edition_at"] for edition in report["empty_editions"]
    }
    empty_dates = set(empty_editions)
    edition_dates.update(empty_dates)

    canonical = {"schema_version": SCHEMA_VERSION, "items": items}
    _write_json(radar_dir / "radar-canonico.json", canonical)
    for edition_date in sorted(edition_dates):
        edition_items = grouped[edition_date]
        generated_at = max(
            [item["edition_at"] for item in edition_items]
            + ([empty_editions[edition_date]] if edition_date in empty_editions else [])
        )
        _write_json(
            radar_dir / "editions" / f"{edition_date}.json",
            _edition_payload(edition_date, edition_items, generated_at),
        )

    latest_date = max(edition_dates, default=None)
    latest_items = grouped[latest_date] if latest_date else []
    latest_generated_at = None
    if latest_date:
        latest_generated_at = max(
            [item["edition_at"] for item in latest_items]
            + ([empty_editions[latest_date]] if latest_date in empty_editions else [])
        )
    _write_json(
        radar_dir / "latest.json",
        _edition_payload(latest_date, latest_items, latest_generated_at),
    )
    kindle_items = items[:50]
    kindle_date = kindle_items[0]["edition_date"] if kindle_items else latest_date
    kindle_generated_at = kindle_items[0]["edition_at"] if kindle_items else latest_generated_at
    kindle = _edition_payload(kindle_date, kindle_items, kindle_generated_at)
    kindle["scope"] = "ultimas_50_publicacoes"
    _write_json(radar_dir / "kindle.json", kindle)
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
