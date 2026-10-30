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
        self.assertEqual("radar-2026-10-29T07:35:00-03:00", latest["edition_id"])
        self.assertEqual("2026-10-29T07:35:00-03:00", latest["generated_at"])
        self.assertEqual({"signals": 1, "sources": 1, "high_confidence": 1}, latest["metrics"])
        self.assertEqual("1", latest["methodology"]["version"])
        self.assertIn("alto sinal", latest["methodology"]["summary"])
        self.assertEqual("example.com", latest["items"][0]["source_meta"]["domain"])
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

    def _feed(self, document: str = DOCUMENT):
        report = parse_document(document)
        with tempfile.TemporaryDirectory() as temporary_directory:
            output_dir = Path(temporary_directory)
            build_artifacts(report, output_dir)
            path = output_dir / "v1/radar/feed.xml"
            return ET.parse(path).getroot(), path.read_text(encoding="utf-8")

    def test_feed_declares_correct_namespaces_and_channel_metadata(self):
        root, raw = self._feed()

        self.assertIn('xmlns:atom="http://www.w3.org/2005/Atom"', raw)
        self.assertIn('xmlns:content="http://purl.org/rss/1.0/modules/content/"', raw)
        self.assertEqual("pt-BR", root.findtext("./channel/language"))
        self.assertTrue(root.findtext("./channel/lastBuildDate").endswith("-0300"))
        self_link = root.find("./channel/{http://www.w3.org/2005/Atom}link")
        self.assertEqual("self", self_link.get("rel"))
        self.assertEqual("application/rss+xml", self_link.get("type"))
        self.assertEqual(
            "https://radar-publico-opal.vercel.app/v1/radar/feed.xml", self_link.get("href")
        )

    def test_feed_emits_one_category_per_tag(self):
        root, _ = self._feed()

        categories = [c.text for c in root.findall("./channel/item/category")]
        self.assertEqual(["openai", "geoia"], categories)

    def test_feed_description_is_plain_text_without_markdown_backticks(self):
        document = DOCUMENT.replace(
            "Primeiro parágrafo factual sobre o lançamento.",
            "Lança `codex queue --resume` & `doctor`.",
        )
        root, _ = self._feed(document)

        description = root.findtext("./channel/item/description")
        self.assertNotIn("`", description)
        self.assertIn("codex queue --resume", description)

    def test_feed_content_encoded_has_html_summary_impact_and_source(self):
        document = DOCUMENT.replace(
            "Primeiro parágrafo factual sobre o lançamento.",
            "Lança `codex doctor` & <b>cru</b>.",
        )
        root, _ = self._feed(document)

        html = root.findtext("./channel/item/{http://purl.org/rss/1.0/modules/content/}encoded")
        self.assertIn("<p>Lança <code>codex doctor</code> &amp; &lt;b&gt;cru&lt;/b&gt;.</p>", html)
        self.assertIn("<p>Segundo parágrafo com contexto, sem copiar a fonte.</p>", html)
        self.assertIn("Por que importa", html)
        self.assertIn("Uma mudança verificável para agentes e GIS.", html)
        self.assertIn('<a href="https://example.com/noticia?a=1&amp;b=2">', html)

    def test_feed_does_not_expose_internal_relations(self):
        _, raw = self._feed()

        self.assertNotIn("Projeto Exemplo", raw)
        self.assertNotIn("Outro Projeto", raw)

    def _two_records_same_url(self, newest_first: bool) -> str:
        old = DOCUMENT.replace("2026-10-29 07:35", "2026-10-28 07:35").replace(
            "Lançamento do Radar", "Primeira matéria da página"
        )
        new = DOCUMENT.replace("Lançamento do Radar", "Segunda matéria da página")
        records = [new, old] if newest_first else [old, new]
        return records[0] + "\n" + records[1].split("## Registros\n", 1)[1]

    def test_items_sharing_a_url_get_distinct_ids_and_oldest_keeps_original(self):
        single = parse_document(DOCUMENT)["items"][0]["id"]

        for newest_first in (True, False):
            items = parse_document(self._two_records_same_url(newest_first))["items"]
            by_title = {item["title"]: item["id"] for item in items}

            self.assertEqual(2, len(set(by_title.values())), "ids devem ser únicos")
            self.assertEqual(single, by_title["Primeira matéria da página"])
            self.assertNotEqual(single, by_title["Segunda matéria da página"])

    def test_distinct_ids_do_not_depend_on_document_order(self):
        a = {i["title"]: i["id"] for i in parse_document(self._two_records_same_url(True))["items"]}
        b = {i["title"]: i["id"] for i in parse_document(self._two_records_same_url(False))["items"]}

        self.assertEqual(a, b)

    def test_feed_guids_are_unique_when_urls_repeat(self):
        root, _ = self._feed(self._two_records_same_url(True))

        guids = [g.text for g in root.findall("./channel/item/guid")]
        self.assertEqual(len(guids), len(set(guids)))

    def test_public_json_files_do_not_expose_relations(self):
        report = parse_document(DOCUMENT)
        with tempfile.TemporaryDirectory() as temporary_directory:
            output_dir = Path(temporary_directory)
            build_artifacts(report, output_dir)
            for path in (output_dir / "v1/radar").rglob("*.json"):
                text = path.read_text(encoding="utf-8")
                self.assertNotIn("Projeto Exemplo", text, path.name)
                self.assertNotIn('"relations"', text, path.name)

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
        self.assertEqual("radar-2026-10-30T07:35:00-03:00", latest["edition_id"])
        self.assertEqual("2026-10-30T07:35:00-03:00", latest["generated_at"])
        self.assertEqual({"signals": 0, "sources": 0, "high_confidence": 0}, latest["metrics"])

    def test_metrics_count_unique_domains_and_high_confidence_items(self):
        report = parse_document(
            DOCUMENT
            + """
### 2026-10-29 07:35 BRT — Segundo sinal

- Fonte: [Outra página oficial](https://example.com/segundo)
- Publicado: 2026-10-28
- Por que importa: Segundo sinal da edição.
- Tags: #geoia
- Confiança: média

### 2026-10-29 07:35 BRT — Terceiro sinal

- Fonte: [Nova fonte](https://news.example.org/terceiro)
- Publicado: 2026-10-28
- Por que importa: Terceiro sinal da edição.
- Tags: #geoia
- Confiança: alta
"""
        )
        with tempfile.TemporaryDirectory() as temporary_directory:
            output_dir = Path(temporary_directory)
            build_artifacts(report, output_dir)
            latest = json.loads((output_dir / "v1/radar/latest.json").read_text())

        self.assertEqual({"signals": 3, "sources": 2, "high_confidence": 2}, latest["metrics"])

    def test_empty_document_keeps_latest_contract(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            output_dir = Path(temporary_directory)
            build_artifacts(parse_document("# Radar sem registros\n"), output_dir)
            latest = json.loads((output_dir / "v1/radar/latest.json").read_text())

        self.assertIsNone(latest["edition_id"])
        self.assertIsNone(latest["generated_at"])
        self.assertEqual({"signals": 0, "sources": 0, "high_confidence": 0}, latest["metrics"])
        self.assertEqual("1", latest["methodology"]["version"])

    def test_kindle_feed_keeps_only_the_50_most_recent_items(self):
        records = []
        for index in range(51):
            records.append(
                f"""### 2026-10-30 07:{index:02d} BRT — Sinal {index}

- Fonte: [Fonte {index}](https://example.com/{index})
- Publicado: 2026-10-30
- Por que importa: Contexto {index}.
- Tags: #radar
- Confiança: alta
"""
            )
        with tempfile.TemporaryDirectory() as temporary_directory:
            output_dir = Path(temporary_directory)
            build_artifacts(parse_document("\n".join(records)), output_dir)
            kindle = json.loads((output_dir / "v1/radar/kindle.json").read_text())
            canonical = json.loads((output_dir / "v1/radar/radar-canonico.json").read_text())
            manifest = json.loads((output_dir / "v1/radar/manifest.json").read_text())

        self.assertEqual("1.0", kindle["schema_version"])
        self.assertEqual(50, len(kindle["items"]))
        self.assertEqual(50, kindle["metrics"]["signals"])
        self.assertEqual("Sinal 50", kindle["items"][0]["title"])
        self.assertEqual("Sinal 1", kindle["items"][-1]["title"])
        self.assertEqual(canonical["items"][:50], kindle["items"])
        self.assertIn("v1/radar/kindle.json", manifest["files"])

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
