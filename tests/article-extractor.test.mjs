import assert from "node:assert/strict";
import test from "node:test";

import { extractArticle } from "../lib/radar/article-extractor.mjs";

test("extrai corpo editorial e remove navegação", async () => {
  const result = await extractArticle(`<!doctype html><html><head><title>Título</title></head><body>
    <nav>Menu e rastreio</nav><article><h1>Título</h1><img src="https://rastreador.example/pixel.png"><p>Primeiro parágrafo completo.</p><p>Segundo parágrafo completo.</p></article>
  </body></html>`, "https://example.com/noticia");

  assert.equal(result.title, "Título");
  assert.match(result.html, /Primeiro parágrafo completo/);
  assert.match(result.html, /Segundo parágrafo completo/);
  assert.doesNotMatch(result.html, /Menu e rastreio/);
  assert.doesNotMatch(result.html, /rastreador\.example/);
});

test("rejeita HTML sem corpo extraível", async () => {
  assert.equal(await extractArticle("<html><body><nav>Somente menu</nav></body></html>", "https://example.com"), null);
});
