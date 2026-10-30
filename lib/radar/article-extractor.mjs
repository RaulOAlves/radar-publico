import { Readability } from "@mozilla/readability";
import { JSDOM } from "jsdom";

export function extractArticle(documentHtml, sourceUrl) {
  const dom = new JSDOM(documentHtml, { url: sourceUrl });
  dom.window.document.querySelectorAll("script, style, nav, header, footer, aside, form").forEach((node) => node.remove());
  const article = new Readability(dom.window.document).parse();
  if (!article?.content?.trim()) return null;
  return {
    title: article.title,
    html: article.content,
    text: article.textContent,
  };
}
