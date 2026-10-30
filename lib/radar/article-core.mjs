const GUID = /^radar-[0-9a-f]{16}$/;

export function resolveArticle(canonical, id) {
  if (!GUID.test(id || "") || !Array.isArray(canonical?.items)) return null;
  const article = canonical.items.find((item) => item.id === id);
  if (!article || !/^https:\/\//.test(article.url || "")) return null;
  return article;
}
