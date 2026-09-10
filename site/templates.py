# -*- coding: utf-8 -*-
"""Shared page shell for grovelandconcrete.com.

Content modules build a list of page dicts and call render_page() on each.
Page dict contract:
{
  "route": "/concrete-driveways/",         # required, trailing slash, "/" for home
  "title": "...",                          # required, <title> text (site name appended automatically unless is_home)
  "meta_description": "...",               # required
  "h1": "...",                             # optional, defaults to a stripped title
  "breadcrumbs": [("Home","/"), ("Services","/services/"), ("Concrete Driveways", None)],
  "body_html": "...",                      # required, main content (no header/nav/footer)
  "schema": [ {...}, ... ],                # optional extra JSON-LD objects; BreadcrumbList + WebPage added automatically
  "noindex": False,                        # optional
  "is_home": False,                        # optional, True only for "/"
  "og_image": "/static/brand/png/social-badge-512.png",  # optional override
}
"""
import json
from _data import (
    DOMAIN, BASE_URL, PUBLIC_NAME, BUSINESS, NAV_PRIMARY, FOOTER_LEGAL,
    SERVICES, SERVICE_ORDER, CITIES, CITY_ORDER, TOOLS, TOOL_ORDER,
    TURNSTILE_SITE_KEY,
)
from _photos import gallery_section, photos_for, image_schema
from _seo import title_for, description_for

_STATIC = __import__("pathlib").Path(__file__).resolve().parent / "static"


def _minify_css(css: str) -> str:
    css = __import__("re").sub(r"/\*.*?\*/", "", css, flags=__import__("re").S)
    css = __import__("re").sub(r"\s*\n\s*", "", css)
    return __import__("re").sub(r"\s*([{}:;,>])\s*", r"\1", css).replace(";}", "}")


# Fonts + stylesheet are inlined into every page: one fewer render-blocking
# request each (and no cross-origin Google Fonts round trip). ~14 KB per page.
INLINE_CSS = _minify_css((_STATIC / "fonts" / "fonts.css").read_text(encoding="utf-8") + "\n" + (_STATIC / "styles.css").read_text(encoding="utf-8"))
PRELOAD_FONTS = ["/static/fonts/fjalla-one-400-latin.woff2"]  # display font only; body font is discovered from the inline CSS
# Content-hashed script name so /static/site.<hash>.js can be cached immutably for a year.
SITE_JS = "/static/site." + __import__("hashlib").md5((_STATIC / "site.js").read_bytes()).hexdigest()[:10] + ".js"

# route -> service key, so render_page can append the photo gallery to each service page
_SERVICE_BY_ROUTE = {v["route"]: k for k, v in SERVICES.items()}

DEFAULT_OG_IMAGE = "/static/brand/png/og-default.jpg"  # 1200x630, generated from the logo

# Logo lockups (brand/png + brand/webp are the source; static/ holds the copies
# the site serves). "-h160" / "-h400" are pre-downscaled renders so the header
# and footer don't ship the 1-2 MB masters; the light/dark pairs swap the
# wordmark colour for dark backgrounds / dark colour scheme.
LOGO_HEADER = {
    "light_webp": "/static/brand/webp/logo-horizontal-light-h160.webp",
    "dark_webp": "/static/brand/webp/logo-horizontal-dark-h160.webp",
    "light_png": "/static/brand/png/logo-horizontal-light-h160.png",
    "dark_png": "/static/brand/png/logo-horizontal-dark-h160.png",
    "width": 943, "height": 160,
}
# srcset pairs (566w = h96 render for phones, 943w = h160 for desktop) and the
# CSS pixel widths the logo is actually displayed at (see --logo-h in styles.css).
LOGO_SIZES = "(max-width:400px) 248px, (max-width:860px) 283px, (max-width:1060px) 318px, 377px"
def _logo_srcset(kind):  # kind: light_webp / dark_webp / light_png / dark_png
    base = LOGO_HEADER[kind].replace("-h160.", "-h96.")
    return f"{base} 566w, {LOGO_HEADER[kind]} 943w"
LOGO_FOOTER = {
    "webp": "/static/brand/webp/logo-full-dark-h400.webp",
    "png": "/static/brand/png/logo-full-dark-h400.png",
    "width": 563, "height": 400,
}


def turnstile_html() -> str:
    """Cloudflare Turnstile widget + loader. Empty while the site key is still
    the placeholder so forms don't render a broken widget; must be paired with
    TURNSTILE_SECRET_KEY on the Pages Function, which enforces the token only
    when the secret is set."""
    if not TURNSTILE_SITE_KEY or TURNSTILE_SITE_KEY.startswith("{{"):
        return ""
    return (
        f'<div class="cf-turnstile" data-sitekey="{_esc(TURNSTILE_SITE_KEY)}"></div>'
        '<script src="https://challenges.cloudflare.com/turnstile/v0/api.js" async defer></script>'
    )


def _esc(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def _nav_html(active_route: str) -> str:
    items = []
    for label, route in NAV_PRIMARY:
        cls = ' class="active"' if route == active_route else ""
        items.append(f'<a href="{route}"{cls}>{_esc(label)}</a>')
    return "\n".join(items)


def header_html(active_route: str = "") -> str:
    return f"""
<header class="site-header">
  <div class="wrap header-row">
    <a class="brand" href="/" aria-label="{PUBLIC_NAME} — home">
      <picture>
        <source srcset="{_logo_srcset('dark_webp')}" sizes="{LOGO_SIZES}" media="(prefers-color-scheme: dark)" type="image/webp">
        <source srcset="{_logo_srcset('dark_png')}" sizes="{LOGO_SIZES}" media="(prefers-color-scheme: dark)" type="image/png">
        <source srcset="{_logo_srcset('light_webp')}" sizes="{LOGO_SIZES}" type="image/webp">
        <img class="brand-logo" src="{LOGO_HEADER['light_png']}" srcset="{_logo_srcset('light_png')}" sizes="{LOGO_SIZES}" width="{LOGO_HEADER['width']}" height="{LOGO_HEADER['height']}" alt="{PUBLIC_NAME}" fetchpriority="high" decoding="async">
      </picture>
    </a>
    <button class="nav-toggle" id="navToggle" aria-expanded="false" aria-controls="primaryNav" aria-label="Open menu">
      <span></span><span></span><span></span>
    </button>
    <nav class="primary-nav" id="primaryNav">
      {_nav_html(active_route)}
    </nav>
    <a class="btn btn-primary header-cta" href="tel:{BUSINESS['phone_tel_placeholder']}">Call {BUSINESS['phone_placeholder']}</a>
  </div>
</header>
""".strip()


def footer_html() -> str:
    service_links = "\n".join(
        f'<li><a href="{SERVICES[s]["route"]}">{_esc(SERVICES[s]["name"])}</a></li>' for s in SERVICE_ORDER
    )
    city_links = "\n".join(
        f'<li><a href="{CITIES[c]["route"]}">{_esc(CITIES[c]["name"])}</a></li>' for c in CITY_ORDER
    )
    legal_links = "\n".join(f'<li><a href="{route}">{_esc(label)}</a></li>' for label, route in FOOTER_LEGAL)
    return f"""
<footer class="site-footer">
  <div class="wrap footer-grid">
    <div class="footer-brand">
      <a class="brand footer-brand-logo" href="/" aria-label="{PUBLIC_NAME} — home">
        <picture>
          <source srcset="{LOGO_FOOTER['webp']}" type="image/webp">
          <img src="{LOGO_FOOTER['png']}" width="{LOGO_FOOTER['width']}" height="{LOGO_FOOTER['height']}" alt="{PUBLIC_NAME}" loading="lazy">
        </picture>
      </a>
      <p class="footer-disclosure">{_esc(BUSINESS["disclosure_short"])}</p>
    </div>
    <div class="footer-col">
      <h2>Services</h2>
      <ul>{service_links}</ul>
    </div>
    <div class="footer-col">
      <h2>Service Area</h2>
      <ul>{city_links}</ul>
    </div>
    <div class="footer-col">
      <h2>Contact</h2>
      <ul>
        <li><a href="tel:{BUSINESS['phone_tel_placeholder']}">{BUSINESS['phone_placeholder']}</a></li>
        <li><a href="mailto:{BUSINESS['email_placeholder']}">{BUSINESS['email_placeholder']}</a></li>
        <li><a href="/contact/">Request an estimate</a></li>
        <li><a href="/gallery/">Photo gallery</a></li>
      </ul>
    </div>
  </div>
  <div class="wrap footer-bottom">
    <span>&copy; 2026 {PUBLIC_NAME}. Groveland &amp; South Lake County, FL.</span>
    <ul class="legal-links">{legal_links}</ul>
  </div>
</footer>
""".strip()


def breadcrumbs_html(crumbs) -> str:
    if not crumbs:
        return ""
    parts = []
    for label, route in crumbs:
        if route:
            parts.append(f'<a href="{route}">{_esc(label)}</a>')
        else:
            parts.append(f'<span aria-current="page">{_esc(label)}</span>')
    return f'<nav class="breadcrumbs" aria-label="Breadcrumb">{" <span class=\"sep\">/</span> ".join(parts)}</nav>'


def breadcrumb_schema(crumbs, base_url: str):
    items = []
    for i, (label, route) in enumerate(crumbs, start=1):
        entry = {"@type": "ListItem", "position": i, "name": label}
        if route:
            entry["item"] = base_url + route
        items.append(entry)
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items}


def render_page(page: dict) -> str:
    route = page["route"]
    is_home = page.get("is_home", False)
    title = title_for(route, page["title"], is_home)
    meta_description = description_for(route, page["meta_description"])
    canonical = BASE_URL + route
    og_image = BASE_URL + page.get("og_image", DEFAULT_OG_IMAGE)
    h1 = page.get("h1", page["title"])
    crumbs = page.get("breadcrumbs", [])
    robots = "noindex,nofollow" if page.get("noindex") else "index,follow,max-image-preview:large"

    schema_objects = []
    if crumbs:
        schema_objects.append(breadcrumb_schema(crumbs, BASE_URL))
    schema_objects.append({
        "@context": "https://schema.org",
        "@type": "WebPage",
        "name": page["title"],
        "url": canonical,
        "description": meta_description,
    })
    schema_objects.extend(page.get("schema", []))
    if route.startswith("/blog/") and route != "/blog/" or route.startswith("/compare/"):
        schema_objects.append({
            "@context": "https://schema.org",
            "@type": "BlogPosting",
            "headline": page.get("h1", page["title"]),
            "description": meta_description,
            "url": canonical,
            "mainEntityOfPage": canonical,
            "datePublished": page.get("_published", "2026-09-08"),
            "dateModified": page.get("_lastmod", page.get("_published", "2026-09-08")),
            "author": {"@type": "Organization", "@id": "https://grovelandconcrete.com/#organization", "name": PUBLIC_NAME},
            "publisher": {"@type": "Organization", "@id": "https://grovelandconcrete.com/#organization", "name": PUBLIC_NAME,
                          "logo": {"@type": "ImageObject", "url": f"{BASE_URL}/static/brand/png/logo-full-h400.png"}},
            "image": og_image,
            "inLanguage": "en-US",
        })

    active_route = page.get("nav_active", "")
    body_html = page["body_html"]
    svc_key = _SERVICE_BY_ROUTE.get(route)
    if svc_key and not page.get("no_gallery"):
        body_html += gallery_section(svc_key, SERVICES[svc_key]["name"])
        schema_objects.extend(image_schema(photos_for(svc_key)[:9], BASE_URL))
    crumbs_block = breadcrumbs_html(crumbs) if crumbs and not is_home else ""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{_esc(title)}</title>
<meta name="description" content="{_esc(meta_description)}">
<link rel="canonical" href="{canonical}">
<meta name="robots" content="{robots}">
<meta property="og:type" content="website">
<meta property="og:title" content="{_esc(title)}">
<meta property="og:description" content="{_esc(meta_description)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{og_image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{PUBLIC_NAME} — concrete, paver and hardscape planning for South Lake County, FL">
<meta property="og:site_name" content="{PUBLIC_NAME}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" type="image/png" sizes="32x32" href="/static/brand/png/favicon-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="/static/brand/png/favicon-192.png">
<link rel="apple-touch-icon" href="/static/brand/png/favicon-192.png">
<link rel="manifest" href="/site.webmanifest">
<meta name="theme-color" content="#F4F3ED" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#1B1A16" media="(prefers-color-scheme: dark)">
{"".join(f'<link rel="preload" as="font" type="font/woff2" href="{f}" crossorigin>' for f in PRELOAD_FONTS)}
{'<link rel="preload" as="image" href="/static/images/hero-concrete-texture-720.webp" type="image/webp" media="(max-width: 720px)" fetchpriority="high"><link rel="preload" as="image" href="/static/images/hero-concrete-texture-1200.webp" type="image/webp" media="(min-width: 721px) and (max-width: 1200px)" fetchpriority="high"><link rel="preload" as="image" href="/static/images/hero-concrete-texture-1920.webp" type="image/webp" media="(min-width: 1201px)" fetchpriority="high">' if is_home else ''}
<style>{INLINE_CSS}</style>
<script type="application/ld+json">{json.dumps(schema_objects, ensure_ascii=False)}</script>
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
{header_html(active_route)}
<main id="main">
{f'<div class="wrap"><h1 class="page-h1">{_esc(h1)}</h1>{crumbs_block}</div>' if not is_home else ''}
{body_html}
</main>
{footer_html()}
<script src="{SITE_JS}" defer></script>
</body>
</html>
"""
