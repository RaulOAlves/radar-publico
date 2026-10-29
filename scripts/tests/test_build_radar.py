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
- Resumo: Primeiro parágrafo factual sobre o lançamento.

  Segundo parágrafo com contexto, sem copiar a fonte.
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
        self.assertEqual(
            "Primeiro parágrafo factual sobre o lançamento.\n\nSegundo parágrafo com contexto, sem copiar a fonte.",
            item["summary"],
        )
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
        self.assertEqual("publicado", latest["status"])
        self.assertEqual(1, manifest["item_count"])
        self.assertEqual("rss", rss.getroot().tag)
        self.assertEqual("https://radar-publico-opal.vercel.app", rss.findtext("./channel/link"))
        self.assertTrue(rss.findtext("./channel/item/pubDate").endswith("-0300"))
        self.assertEqual(
            "Primeiro parágrafo factual sobre o lançamento.\n\nSegundo parágrafo com contexto, sem copiar a fonte.",
            rss.findtext("./channel/item/description"),
        )
        self.assertIn("v1/radar/quarantine.json", manifest["files"])

    def test_same_input_produces_same_item_id(self):
        first = parse_document(DOCUMENT)["items"][0]["id"]
        second = parse_document(DOCUMENT)["items"][0]["id"]

        self.assertEqual(first, second)

    def test_legacy_item_uses_impact_as_summary_fallback(self):
        legacy = DOCUMENT.replace(
            "- Resumo: Primeiro parágrafo factual sobre o lançamento.\n\n  Segundo parágrafo com contexto, sem copiar a fonte.\n",
            "",
        )

        item = parse_document(legacy)["items"][0]

        self.assertEqual(item["why_it_matters"], item["summary"])

    def test_newest_empty_edition_is_published_explicitly(self):
        report = parse_document(
            DOCUMENT
            + "\n### 2026-10-30 07:35 BRT — Nenhuma novidade de alto sinal\n"
        )
        with tempfile.TemporaryDirectory() as temporary_directory:
            output_dir = Path(temporary_directory)
            build_artifacts(report, output_dir)
            latest = json.loads((output_dir / "v1/radar/latest.json").read_text())

        self.assertEqual("2026-10-30", latest["edition_date"])
        self.assertEqual("sem_novidade", latest["status"])
        self.assertEqual([], latest["items"])

    def test_strict_build_keeps_last_good_artifacts_on_quarantine(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            output_dir = Path(temporary_directory)
            build_artifacts(parse_document(DOCUMENT), output_dir)
            previous = (output_dir / "v1/radar/latest.json").read_bytes()

            invalid = parse_document(
                "## Registros\n\n### 2026-10-30 07:35 BRT — Sem URL\n\n- Fonte: sem link\n"
            )
            with self.assertRaisesRegex(ValueError, "quarentena"):
                build_artifacts(invalid, output_dir, fail_on_quarantine=True)

            self.assertEqual(previous, (output_dir / "v1/radar/latest.json").read_bytes())


if __name__ == "__main__":
    unittest.main()
