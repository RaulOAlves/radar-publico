import assert from "node:assert/strict";
import test from "node:test";

import { resolveArticle } from "../lib/radar/article-core.mjs";

const canonical = {
  items: [
    { id: "radar-0123456789abcdef", url: "https://example.com/news", title: "Notícia" },
    { id: "radar-aaaaaaaaaaaaaaaa", url: "http://example.com/inseguro", title: "Insegura" },
  ],
};

test("resolve apenas GUID canônico HTTPS", () => {
  assert.deepEqual(resolveArticle(canonical, "radar-0123456789abcdef"), canonical.items[0]);
});

test("rejeita GUID desconhecido, formato inválido e URL não HTTPS", () => {
  assert.equal(resolveArticle(canonical, "radar-naoexiste0000"), null);
  assert.equal(resolveArticle(canonical, "https://interno.example"), null);
  assert.equal(resolveArticle(canonical, "radar-aaaaaaaaaaaaaaaa"), null);
});
