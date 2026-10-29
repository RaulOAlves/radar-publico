import json
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SCRIPTS_DIR))

from build_radar import build_artifacts, parse_document


DOCUMENT = """# Radar IA, GeoIA e Setores

> Base relacional de notícias para projetos. Atualizado: 2026-10-29 07:35 (BRT).

## Registros

### 2026-10-29 07:35 BRT — Lançamento do Radar

- Fonte: [Fonte Oficial](https://example.com/noticia?a=1&b=2)
- Publicado: 2026-10-28 22:10 BRT
- Por que importa: Uma mudança verificável para agentes e GIS.
- Tags: #openai #geoia
- Relações: [[Projeto Exemplo]], [[Outro Projeto]]
- Confiança: alta
"""


class RadarBuildTests(unittest.TestCase):
    def test_parse_current_record_into_canonical_item(self):
        report = parse_document(DOCUMENT)

        self.assertEqual([], report["quarantine"])
        self.assertEqual(1, len(report["items"]))
        item = report["items"][0]
        self.assertEqual("Lançamento do Radar", item["title"])
        self.assertEqual("https://example.com/noticia?a=1&b=2", item["url"])
        self.assertEqual(["openai", "geoia"], item["tags"])
        self.assertEqual(["Projeto Exemplo", "Outro Projeto"], item["relations"])
        self.assertEqual("alta", item["confidence"])
        self.assertTrue(item["id"].startswith("radar-"))

    def test_malformed_record_is_quarantined_not_silently_dropped(self):
        report = parse_document(
            "## Registros\n\n### 2026-10-29 07:35 BRT — Sem URL\n\n- Fonte: Fonte sem link\n"
        )

        self.assertEqual([], report["items"])
        self.assertEqual("missing_source_url", report["quarantine"][0]["reason"])

    def test_no_high_signal_entry_is_a_valid_empty_edition(self):
        report = parse_document(
            "## Registros\n\n### 2026-10-29 07:35 BRT — Nenhuma novidade de alto sinal\n"
        )

        self.assertEqual([], report["items"])
        self.assertEqual([], report["quarantine"])

    def test_builds_latest_archive_rss_and_manifest(self):
        report = parse_document(DOCUMENT)
        with tempfile.TemporaryDirectory() as temporary_directory:
            output_dir = Path(temporary_directory)
            build_artifacts(report, output_dir)

            latest = json.loads((output_dir / "v1/radar/latest.json").read_text())
            archive = json.loads(
                (output_dir / "v1/radar/editions/2026-10-29.json").read_text()
            )
            manifest = json.loads((output_dir / "v1/radar/manifest.json").read_text())
            rss = ET.parse(output_dir / "v1/radar/feed.xml")

        self.assertEqual("1.0", latest["schema_version"])
        self.assertEqual(["Lançamento do Radar"], [item["title"] for item in latest["items"]])
        self.assertEqual(latest["items"], archive["items"])
        self.assertEqual(1, manifest["item_count"])
        self.assertEqual("rss", rss.getroot().tag)

    def test_same_input_produces_same_item_id(self):
        first = parse_document(DOCUMENT)["items"][0]["id"]
        second = parse_document(DOCUMENT)["items"][0]["id"]

        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
