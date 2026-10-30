import assert from "node:assert/strict";
import test from "node:test";

import { getOriginalArticle } from "../lib/radar/article-service.mjs";

const canonical = {
  items: [{ id: "radar-0123456789abcdef", url: "https://example.com/original", title: "Radar" }],
};

test("busca somente URL resolvida pelo GUID canônico", async () => {
  let requestedUrl;
  const result = await getOriginalArticle("radar-0123456789abcdef", {
    canonical,
    fetchImpl: async (url, options) => {
      requestedUrl = url;
      assert.equal(options.redirect, "error");
      return { ok: true, text: async () => "<article><p>Texto completo.</p></article>" };
    },
    extract: () => ({ title: "Original", html: "<p>Texto completo.</p>", text: "Texto completo." }),
  });
  assert.equal(requestedUrl, "https://example.com/original");
  assert.equal(result.status, 200);
  assert.equal(result.body.html, "<p>Texto completo.</p>");
});

test("não faz requisição para GUID inexistente", async () => {
  const result = await getOriginalArticle("radar-ffffffffffffffff", {
    canonical,
    fetchImpl: async () => { throw new Error("não deveria buscar"); },
  });
  assert.equal(result.status, 404);
});

test("falha de origem não retorna texto parcial", async () => {
  const result = await getOriginalArticle("radar-0123456789abcdef", {
    canonical,
    fetchImpl: async () => ({ ok: false, status: 403 }),
  });
  assert.equal(result.status, 502);
  assert.equal(result.body.error, "fonte_indisponivel");
});

test("não devolve artigo extraído maior que o limite do Kindle", async () => {
  const result = await getOriginalArticle("radar-0123456789abcdef", {
    canonical,
    fetchImpl: async () => ({ ok: true, text: async () => "<article>ok</article>" }),
    extract: () => ({ title: "Grande", html: "x".repeat(350_001), text: "Grande" }),
  });
  assert.equal(result.status, 413);
  assert.equal(result.body.error, "artigo_grande_demais");
});
