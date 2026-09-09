# -*- coding: utf-8 -*-
"""Static site builder for grovelandconcrete.com.

Imports every content module, renders each page through templates.render_page,
and writes dist/<route>/index.html. Content modules that don't exist yet are
skipped with a warning instead of failing the whole build, so this can be run
incrementally while parallel content modules are still being written.
"""
import datetime
import importlib
import pathlib
import shutil
import subprocess
import sys
import time

sys.path.insert(0, str(pathlib.Path(__file__).parent))

from templates import render_page
from _data import (
    BASE_URL, DOMAIN, PUBLIC_NAME, BUSINESS, SERVICES, SERVICE_ORDER, CITIES, CITY_ORDER,
    TOOLS, TOOL_ORDER, GUIDES, GUIDE_ORDER, COMPARISONS, COMPARISON_ORDER,
)

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
            p["_module"] = mod_name
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


def _git_lastmod(path: pathlib.Path) -> str:
    """Last commit date of the content module that produced a page (falls back to today)."""
    try:
        out = subprocess.run(["git", "log", "-1", "--format=%cI", "--", str(path)], capture_output=True, text=True, cwd=ROOT, timeout=10).stdout.strip()
        if out:
            return out[:10]
    except Exception:
        pass
    return datetime.date.today().isoformat()


def write_sitemap(pages):
    urls = []
    cache = {}
    for p in pages:
        if p.get("noindex"):
            continue
        loc = BASE_URL + p["route"]
        mod = p.get("_module")
        if mod not in cache:
            cache[mod] = _git_lastmod(ROOT / f"{mod}.py") if mod else datetime.date.today().isoformat()
        urls.append(f"  <url><loc>{loc}</loc><lastmod>{cache[mod]}</lastmod></url>")
    body = "\n".join(urls)
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{body}
</urlset>
"""
    (DIST / "sitemap.xml").write_text(xml, encoding="utf-8")


def write_llms_txt():
    """llms.txt — plain-text map of the site for AI crawlers/answer engines."""
    def block(title, order, reg):
        return [f"## {title}", ""] + [f"- [{reg[k]['name']}]({BASE_URL}{reg[k]['route']})" + (f": {reg[k]['short']}" if reg[k].get("short") else "") for k in order] + [""]
    lines = [
        f"# {PUBLIC_NAME}", "",
        f"> {BUSINESS['disclosure_short']}", "",
        f"Website: {BASE_URL}",
        f"Phone: {BUSINESS['phone_placeholder']} ({BUSINESS['phone_tel_placeholder']})",
        f"Email: {BUSINESS['email_placeholder']}",
        "Service area: Groveland, Mascotte, Minneola, Howey-in-the-Hills, Clermont, Montverde and rural/unincorporated Lake County, Florida (South Lake County).",
        "Focus: rural lots, long driveways, RV and boat pads, workshop slabs, paver driveways and patios, pool decks, walkways and retaining walls — with Florida Building Code based specs (4-inch minimum slab, 4,000 PSI, rebar for vehicle loads, 1/8 in/ft drainage slope, 7/28-day cure).",
        "Not a general contractor: requests are routed to a licensed provider serving the area.", "",
    ]
    lines += block("Services", SERVICE_ORDER, SERVICES)
    lines += block("Service area pages", CITY_ORDER, CITIES)
    lines += block("Planning tools & calculators", TOOL_ORDER, TOOLS)
    lines += block("Guides", GUIDE_ORDER, GUIDES)
    lines += block("Comparisons", COMPARISON_ORDER, COMPARISONS)
    lines += ["## Other pages", "",
              f"- [Photo gallery]({BASE_URL}/gallery/): job photos from the provider (paver driveways, pool decks, walkways, retaining walls)",
              f"- [About]({BASE_URL}/about/)",
              f"- [Request a free estimate]({BASE_URL}/contact/)",
              f"- [Permit directory]({BASE_URL}/permits/): links to the building department for each jurisdiction in the service area",
              f"- [Sitemap]({BASE_URL}/sitemap.xml)", ""]
    (DIST / "llms.txt").write_text("\n".join(lines), encoding="utf-8")


def write_favicon_and_manifest():
    from PIL import Image
    src = ROOT / "static" / "brand" / "png"
    ico_sizes = [(16, 16), (32, 32), (48, 48)]
    base = Image.open(src / "favicon-48.png").convert("RGBA")
    base.save(DIST / "favicon.ico", format="ICO", sizes=ico_sizes)
    manifest = {
        "name": PUBLIC_NAME, "short_name": "Groveland Concrete", "start_url": "/", "display": "browser",
        "background_color": "#F4F3ED", "theme_color": "#F4F3ED",
        "icons": [
            {"src": "/static/brand/png/favicon-192.png", "sizes": "192x192", "type": "image/png"},
            {"src": "/static/brand/png/favicon-512.png", "sizes": "512x512", "type": "image/png"},
        ],
    }
    import json as _json
    (DIST / "site.webmanifest").write_text(_json.dumps(manifest, indent=2), encoding="utf-8")


def write_headers_and_redirects():
    headers = f"""/*
  X-Content-Type-Options: nosniff
  X-Frame-Options: SAMEORIGIN
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: camera=(), microphone=(), geolocation=(), payment=()
  Strict-Transport-Security: max-age=31536000; includeSubDomains

/static/images/*
  Cache-Control: public, max-age=31536000, immutable

/static/brand/*
  Cache-Control: public, max-age=2592000

/static/styles.css
  Cache-Control: public, max-age=86400

/static/site.js
  Cache-Control: public, max-age=86400

/favicon.ico
  Cache-Control: public, max-age=604800

/sitemap.xml
  Cache-Control: public, max-age=3600

/llms.txt
  Cache-Control: public, max-age=3600
"""
    (DIST / "_headers").write_text(headers, encoding="utf-8")
    redirects = f"""https://www.{DOMAIN}/* https://{DOMAIN}/:splat 301
"""
    (DIST / "_redirects").write_text(redirects, encoding="utf-8")


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
    write_llms_txt()
    write_favicon_and_manifest()
    write_headers_and_redirects()
    write_404()

    # functions/ and workers/ already live at the project root beside dist/,
    # which is exactly where Cloudflare Pages expects them — nothing to copy.
    print(f"\n[build] {len(pages)} page(s) written to {DIST}")


if __name__ == "__main__":
    main()
