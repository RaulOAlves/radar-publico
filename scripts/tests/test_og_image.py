import email.message
import sys
import unittest
import urllib.error
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SCRIPTS_DIR))

from og_image import (
    TransientFetchError,
    apply_images,
    extract_image_url,
    fetch_image_url,
    resolve_images,
)

PAGE = "https://example.com/blog/post"


class ExtractTests(unittest.TestCase):
    def test_reads_og_image_regardless_of_attribute_order(self):
        a = '<meta property="og:image" content="https://cdn.example.com/a.jpg">'
        b = '<meta content="https://cdn.example.com/a.jpg" property="og:image" />'

        self.assertEqual("https://cdn.example.com/a.jpg", extract_image_url(a, PAGE))
        self.assertEqual("https://cdn.example.com/a.jpg", extract_image_url(b, PAGE))

    def test_falls_back_to_twitter_image_and_prefers_og(self):
        twitter = '<meta name="twitter:image" content="https://cdn.example.com/t.png">'
        both = twitter + '<meta property="og:image" content="https://cdn.example.com/o.png">'

        self.assertEqual("https://cdn.example.com/t.png", extract_image_url(twitter, PAGE))
        self.assertEqual("https://cdn.example.com/o.png", extract_image_url(both, PAGE))

    def test_resolves_relative_urls_and_decodes_entities(self):
        html = '<meta property="og:image" content="/img/a.jpg?x=1&amp;y=2">'

        self.assertEqual("https://example.com/img/a.jpg?x=1&y=2", extract_image_url(html, PAGE))

    def test_rejects_non_https_and_unsafe_schemes(self):
        for bad in ("http://cdn.example.com/a.jpg", "javascript:alert(1)", "data:image/png;base64,AAAA"):
            html = f'<meta property="og:image" content="{bad}">'
            self.assertIsNone(extract_image_url(html, PAGE), bad)

    def test_returns_none_without_image_meta(self):
        self.assertIsNone(extract_image_url("<html><head><title>x</title></head></html>", PAGE))


class FakeResponse:
    def __init__(self, body: str, content_type: str = "text/html", url: str = PAGE):
        self._body = body.encode("utf-8")
        self.headers = email.message.Message()
        self.headers["Content-Type"] = content_type
        self._url = url

    def read(self, size=-1):
        return self._body if size < 0 else self._body[:size]

    def geturl(self):
        return self._url

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False


def http_error(code: int):
    return urllib.error.HTTPError(PAGE, code, "x", email.message.Message(), None)


class FetchTests(unittest.TestCase):
    def test_returns_image_from_page(self):
        body = '<meta property="og:image" content="https://cdn.example.com/a.jpg">'

        result = fetch_image_url(PAGE, opener=lambda request, timeout: FakeResponse(body))

        self.assertEqual("https://cdn.example.com/a.jpg", result)

    def test_sends_identifying_user_agent_and_timeout(self):
        seen = {}

        def opener(request, timeout):
            seen["agent"] = request.get_header("User-agent")
            seen["timeout"] = timeout
            return FakeResponse("")

        fetch_image_url(PAGE, opener=opener)

        self.assertIn("RadarPublico", seen["agent"])
        self.assertLessEqual(seen["timeout"], 15)

    def test_definitive_failures_return_none(self):
        for code in (403, 404, 410):
            def opener(request, timeout, code=code):
                raise http_error(code)

            self.assertIsNone(fetch_image_url(PAGE, opener=opener), code)

    def test_non_html_page_returns_none(self):
        result = fetch_image_url(PAGE, opener=lambda r, timeout: FakeResponse("%PDF", "application/pdf"))

        self.assertIsNone(result)

    def test_transient_failures_raise(self):
        def server_error(request, timeout):
            raise http_error(503)

        def offline(request, timeout):
            raise urllib.error.URLError("sem rede")

        def slow(request, timeout):
            raise TimeoutError()

        for opener in (server_error, offline, slow):
            with self.assertRaises(TransientFetchError):
                fetch_image_url(PAGE, opener=opener)


class ResolveTests(unittest.TestCase):
    ITEMS = [{"url": "https://a.example/1"}, {"url": "https://b.example/2"}]

    def test_fetches_only_urls_missing_from_cache_and_does_not_mutate_input(self):
        cache = {"https://a.example/1": "https://img/a.jpg"}
        calls = []

        def fetcher(url):
            calls.append(url)
            return "https://img/b.jpg"

        result = resolve_images(self.ITEMS, cache, fetcher)

        self.assertEqual(["https://b.example/2"], calls)
        self.assertEqual({"https://a.example/1": "https://img/a.jpg", "https://b.example/2": "https://img/b.jpg"}, result)
        self.assertEqual({"https://a.example/1": "https://img/a.jpg"}, cache)

    def test_definitive_absence_is_cached_but_transient_error_is_not(self):
        def fetcher(url):
            if "a.example" in url:
                return None
            raise TransientFetchError()

        result = resolve_images(self.ITEMS, {}, fetcher)

        self.assertEqual({"https://a.example/1": None}, result)

    def test_apply_images_adds_image_only_when_known(self):
        cache = {"https://a.example/1": "https://img/a.jpg", "https://b.example/2": None}

        items = apply_images(self.ITEMS, cache)

        self.assertEqual("https://img/a.jpg", items[0]["image"])
        self.assertNotIn("image", items[1])
        self.assertNotIn("image", self.ITEMS[0])


if __name__ == "__main__":
    unittest.main()
