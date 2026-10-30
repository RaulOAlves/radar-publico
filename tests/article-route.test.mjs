import assert from "node:assert/strict";
import test from "node:test";

import handler, { GET } from "../api/radar/article.mjs";

test("handler padrão delega para GET", () => {
  assert.equal(handler.fetch, GET);
});

test("rota responde 404 para GUID inexistente sem buscar fonte", async () => {
  const response = await GET(new Request("https://radar.example/api/radar/article?id=radar-ffffffffffffffff"));
  assert.equal(response.status, 404);
  assert.deepEqual(await response.json(), { error: "artigo_nao_encontrado" });
});

test("rota rejeita ausência de GUID", async () => {
  const response = await GET(new Request("https://radar.example/api/radar/article"));
  assert.equal(response.status, 404);
});
