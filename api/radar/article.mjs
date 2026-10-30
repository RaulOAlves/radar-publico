import { readFile } from "node:fs/promises";

import { getOriginalArticle } from "./article-service.mjs";

const CANONICAL = new URL("../../public/v1/radar/radar-canonico.json", import.meta.url);

async function loadCanonical() {
  return JSON.parse(await readFile(CANONICAL, "utf8"));
}

export async function GET(request) {
  const id = new URL(request.url).searchParams.get("id");
  try {
    const result = await getOriginalArticle(id, { canonical: await loadCanonical() });
    return Response.json(result.body, {
      status: result.status,
      headers: { "Cache-Control": "no-store" },
    });
  } catch (error) {
    console.error("radar article extraction failed", { id, error: String(error) });
    return Response.json({ error: "extracao_indisponivel" }, {
      status: 502,
      headers: { "Cache-Control": "no-store" },
    });
  }
}
