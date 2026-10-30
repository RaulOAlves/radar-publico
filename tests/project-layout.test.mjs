import assert from "node:assert/strict";
import { readdir } from "node:fs/promises";
import test from "node:test";

test("somente handler público fica no diretório api", async () => {
  assert.deepEqual(await readdir(new URL("../api/radar/", import.meta.url)), ["article.mjs"]);
});
