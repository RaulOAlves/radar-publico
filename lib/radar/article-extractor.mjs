export async function extractArticle(documentHtml, sourceUrl) {
  // Vercel precisa responder 404 para GUIDs inválidos sem carregar o parser
  // pesado. Assim a dependência só entra em cena após validar a notícia.
  const [{ Readability }, { JSDOM }] = await Promise.all([
    import("@mozilla/readability"),
    import("jsdom"),
  ]);
  const dom = new JSDOM(documentHtml, { url: sourceUrl });
  // Texto basta no Kindle. Excluir mídia impede carregamentos remotos e rastreio
  // adicional quando a fonte for aberta sob demanda.
  dom.window.document.querySelectorAll("script, style, nav, header, footer, aside, form, img, picture, source, video, audio, iframe").forEach((node) => node.remove());
  const article = new Readability(dom.window.document).parse();
  if (!article?.content?.trim()) return null;
  return {
    title: article.title,
    html: article.content,
    text: article.textContent,
  };
}
