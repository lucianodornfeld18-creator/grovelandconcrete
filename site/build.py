# -*- coding: utf-8 -*-
"""Static site builder for grovelandconcrete.com.

Imports every content module, renders each page through templates.render_page,
and writes dist/<route>/index.html. Content modules that don't exist yet are
skipped with a warning instead of failing the whole build, so this can be run
incrementally while parallel content modules are still being written.
"""
import importlib
import pathlib
import shutil
import sys
import time

sys.path.insert(0, str(pathlib.Path(__file__).parent))

from templates import render_page
from _data import BASE_URL

ROOT = pathlib.Path(__file__).parent
DIST = ROOT / "dist"

CONTENT_MODULES = [
    "content_home",
    "content_legal",
    "content_hubs",
    "content_services_driveways",
    "content_services_rest",
    "content_tools_calculator",
    "content_tools_rest",
    "content_cities",
    "content_cities_extra",
    "content_guides",
    "content_comparisons",
    "content_gallery",
]


def load_pages():
    all_pages = []
    seen_routes = {}
    for mod_name in CONTENT_MODULES:
        try:
            mod = importlib.import_module(mod_name)
        except ModuleNotFoundError:
            print(f"[build] SKIP  {mod_name} (not written yet)")
            continue
        importlib.reload(mod)
        pages = mod.get_pages()
        for p in pages:
            route = p["route"]
            if route in seen_routes:
                raise SystemExit(f"[build] DUPLICATE ROUTE: {route} in both {seen_routes[route]} and {mod_name}")
            seen_routes[route] = mod_name
            all_pages.append(p)
        print(f"[build] OK    {mod_name} -> {len(pages)} page(s)")
    return all_pages


def write_page(page: dict):
    route = page["route"]
    out_dir = DIST if route == "/" else DIST / route.strip("/")
    out_dir.mkdir(parents=True, exist_ok=True)
    html = render_page(page)
    (out_dir / "index.html").write_text(html, encoding="utf-8")


def write_static():
    static_src = ROOT / "static"
    static_dst = DIST / "static"
    if static_dst.exists():
        shutil.rmtree(static_dst)
    shutil.copytree(static_src, static_dst)


def write_robots():
    content = f"""User-agent: *
Allow: /
Disallow: /thank-you/
Disallow: /api/

User-agent: GPTBot
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: Bingbot
Allow: /

Sitemap: {BASE_URL}/sitemap.xml
"""
    (DIST / "robots.txt").write_text(content, encoding="utf-8")


def write_sitemap(pages):
    urls = []
    for p in pages:
        if p.get("noindex"):
            continue
        loc = BASE_URL + p["route"]
        urls.append(f"  <url><loc>{loc}</loc></url>")
    body = "\n".join(urls)
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{body}
</urlset>
"""
    (DIST / "sitemap.xml").write_text(xml, encoding="utf-8")


def write_404():
    # Cloudflare Pages serves dist/404/index.html or dist/404.html for unmatched routes
    # depending on config; keep both to be safe.
    src = DIST / "404" / "index.html"
    if src.exists():
        shutil.copy(src, DIST / "404.html")


def _rmtree_retry(path: pathlib.Path, attempts: int = 5, delay: float = 0.5):
    """dist/ is sometimes still held open by a local test server (e.g. `python
    -m http.server` serving it for QA) — retry briefly instead of failing the
    whole build over a transient Windows file lock."""
    for i in range(attempts):
        try:
            shutil.rmtree(path)
            return
        except PermissionError:
            if i == attempts - 1:
                raise
            time.sleep(delay)


def main():
    if DIST.exists():
        _rmtree_retry(DIST)
    DIST.mkdir(parents=True)

    pages = load_pages()
    for page in pages:
        write_page(page)

    write_static()
    write_robots()
    write_sitemap(pages)
    write_404()

    # functions/ and workers/ already live at the project root beside dist/,
    # which is exactly where Cloudflare Pages expects them — nothing to copy.
    print(f"\n[build] {len(pages)} page(s) written to {DIST}")


if __name__ == "__main__":
    main()
