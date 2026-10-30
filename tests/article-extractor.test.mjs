import assert from "node:assert/strict";
import test from "node:test";

import { extractArticle } from "../api/radar/article-extractor.mjs";

test("extrai corpo editorial e remove navegação", () => {
  const result = extractArticle(`<!doctype html><html><head><title>Título</title></head><body>
    <nav>Menu e rastreio</nav><article><h1>Título</h1><p>Primeiro parágrafo completo.</p><p>Segundo parágrafo completo.</p></article>
  </body></html>`, "https://example.com/noticia");

  assert.equal(result.title, "Título");
  assert.match(result.html, /Primeiro parágrafo completo/);
  assert.match(result.html, /Segundo parágrafo completo/);
  assert.doesNotMatch(result.html, /Menu e rastreio/);
});

test("rejeita HTML sem corpo extraível", () => {
  assert.equal(extractArticle("<html><body><nav>Somente menu</nav></body></html>", "https://example.com"), null);
});
