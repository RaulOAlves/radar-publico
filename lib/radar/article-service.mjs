import { resolveArticle } from "./article-core.mjs";
import { extractArticle } from "./article-extractor.mjs";

const MAX_DOCUMENT_BYTES = 1_000_000;
const MAX_ARTICLE_BYTES = 350_000;
const SOURCE_TIMEOUT_MS = 12_000;

export async function getOriginalArticle(id, deps) {
  const article = resolveArticle(deps.canonical, id);
  if (!article) return { status: 404, body: { error: "artigo_nao_encontrado" } };

  let response;
  try {
    response = await (deps.fetchImpl || fetch)(article.url, {
      redirect: "error",
      signal: AbortSignal.timeout(SOURCE_TIMEOUT_MS),
      headers: { "user-agent": "Radar-Kindle/1.0 (+https://radar-publico-opal.vercel.app)" },
    });
  } catch (error) {
    return { status: 502, body: { error: "fonte_indisponivel" } };
  }
  if (!response.ok) return { status: 502, body: { error: "fonte_indisponivel" } };

  const documentHtml = await response.text();
  if (new TextEncoder().encode(documentHtml).byteLength > MAX_DOCUMENT_BYTES) {
    return { status: 413, body: { error: "fonte_grande_demais" } };
  }
  const extracted = (deps.extract || extractArticle)(documentHtml, article.url);
  if (!extracted) return { status: 422, body: { error: "fonte_sem_corpo_extraivel" } };
  if (new TextEncoder().encode(extracted.html).byteLength > MAX_ARTICLE_BYTES) {
    return { status: 413, body: { error: "artigo_grande_demais" } };
  }
  return {
    status: 200,
    body: {
      id: article.id,
      source_url: article.url,
      title: extracted.title || article.title,
      html: extracted.html,
      fetched_at: new Date().toISOString(),
    },
  };
}
