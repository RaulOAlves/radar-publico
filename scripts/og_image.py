"""Imagem principal (og:image) da página de cada matéria, para o feed RSS.

Só biblioteca padrão. Falha aberta: sem imagem o item sai só com texto.
"""
from __future__ import annotations

import html
import json
import re
import urllib.error
import urllib.request
from pathlib import Path
from typing import Callable
from urllib.parse import urljoin

USER_AGENT = "Mozilla/5.0 (compatible; RadarPublico/1.0; +https://radar-publico-opal.vercel.app)"
TIMEOUT_SECONDS = 8
MAX_BYTES = 400_000
HTML_TYPES = {"text/html", "application/xhtml+xml"}
TRANSIENT_STATUS = {408, 429}
META_TAG = re.compile(r"<meta\s[^>]*>", re.IGNORECASE)
ATTRIBUTE = re.compile(r"""([\w:-]+)\s*=\s*(?:"([^"]*)"|'([^']*)')""")
# do mais para o menos preferido
IMAGE_KEYS = ("og:image:secure_url", "og:image", "twitter:image", "twitter:image:src")


class TransientFetchError(Exception):
    """Falha que pode passar sozinha (rede, timeout, 5xx): não vai para o cache."""


def extract_image_url(page: str, base_url: str) -> str | None:
    found: dict[str, str] = {}
    for tag in META_TAG.findall(page):
        attributes = {
            name.lower(): html.unescape(double if double is not None else single)
            for name, double, single in ATTRIBUTE.findall(tag)
        }
        key = (attributes.get("property") or attributes.get("name") or "").lower()
        if key in IMAGE_KEYS and attributes.get("content", "").strip():
            found.setdefault(key, attributes["content"].strip())
    for key in IMAGE_KEYS:
        if key in found:
            url = urljoin(base_url, found[key])
            if url.startswith("https://"):
                return url
    return None


def fetch_image_url(url: str, opener: Callable = urllib.request.urlopen) -> str | None:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "text/html"})
    try:
        with opener(request, timeout=TIMEOUT_SECONDS) as response:
            if response.headers.get_content_type() not in HTML_TYPES:
                return None
            page = response.read(MAX_BYTES).decode("utf-8", errors="ignore")
            return extract_image_url(page, response.geturl())
    except urllib.error.HTTPError as error:
        if error.code >= 500 or error.code in TRANSIENT_STATUS:
            raise TransientFetchError(str(error.code)) from error
        return None
    except (urllib.error.URLError, OSError) as error:
        raise TransientFetchError(str(error)) from error


def resolve_images(
    items: list[dict], cache: dict[str, str | None], fetcher: Callable[[str], str | None] = fetch_image_url
) -> dict[str, str | None]:
    """Devolve um cache novo com as URLs que faltavam. Ausência definitiva é guardada (None)."""
    result = dict(cache)
    for item in items:
        url = item["url"]
        if url in result:
            continue
        try:
            result[url] = fetcher(url)
        except TransientFetchError:
            continue
    return result


def apply_images(items: list[dict], cache: dict[str, str | None]) -> list[dict]:
    return [{**item, "image": cache[item["url"]]} if cache.get(item["url"]) else item for item in items]


def load_cache(path: Path) -> dict[str, str | None]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def save_cache(path: Path, cache: dict[str, str | None]) -> None:
    path.write_text(json.dumps(cache, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
