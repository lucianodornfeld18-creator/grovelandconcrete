# -*- coding: utf-8 -*-
"""Photo library for grovelandconcrete.com.

Source of truth is ../images/photos.json (written by the photo pipeline); the
site serves /static/images/<slug>-{1600,960,480}.webp. Photos tagged
kind="rendering" are AI concept images and are labelled as such on the page.
"""
import json
import pathlib

_JSON = pathlib.Path(__file__).resolve().parent.parent / "images" / "photos.json"
PHOTOS = json.loads(_JSON.read_text(encoding="utf-8")) if _JSON.exists() else []

_SERVICE_KEYS = ("paver-driveways", "paver-patios", "sidewalks-walkways", "retaining-walls",
                 "concrete-driveways", "rv-and-boat-pads", "workshop-slabs",
                 "concrete-patios", "concrete-repair-resurfacing")


def _esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def photos_for(service_key, include_secondary=True, real_first=True):
    out = [p for p in PHOTOS if (p["services"][0] == service_key or (include_secondary and service_key in p["services"]))]
    if real_first:
        out.sort(key=lambda p: (p["kind"] != "real", p["services"][0] != service_key))
    return out


FEATURED_SLUGS = [
    "gray-paver-driveway-charcoal-grid-border-groveland-concrete",
    "marble-paver-lanai-pool-deck-groveland-concrete",
    "raised-paver-terrace-stone-wall-pergola-groveland-concrete",
    "front-entry-steps-porcelain-paver-treads-groveland-concrete",
    "paver-driveway-entry-pillar-light-groveland-concrete",
    "travertine-paver-pool-deck-square-pool-groveland-concrete",
]


def featured(limit=6):
    """Home-page strip: hand-picked real photos, one look each (driveway, pool
    deck, raised terrace, entry steps, pillar, travertine deck)."""
    by_slug = {p["slug"]: p for p in PHOTOS}
    picked = [by_slug[s] for s in FEATURED_SLUGS if s in by_slug]
    if len(picked) < limit:
        for p in PHOTOS:
            if p["kind"] == "real" and p not in picked:
                picked.append(p)
            if len(picked) >= limit:
                break
    return picked[:limit]


def figure_html(p, sizes="(max-width:560px) 100vw, (max-width:1120px) 50vw, 360px", eager=False):
    slug = p["slug"]
    srcset = ", ".join(f"/static/images/{slug}-{w}.webp {w}w" for w in (480, 960, 1600))
    badge = '<span class="photo-badge">Concept rendering</span>' if p["kind"] == "rendering" else ""
    return (
        f'<figure class="photo">'
        f'<a href="/static/images/{slug}-1600.webp" target="_blank" rel="noopener">'
        f'<img src="/static/images/{slug}-960.webp" srcset="{srcset}" sizes="{sizes}" '
        f'width="{p["w"]}" height="{p["h"]}" alt="{_esc(p["alt"])}" '
        f'{"" if eager else "loading=\"lazy\" "}decoding="async"></a>{badge}'
        f'<figcaption>{_esc(p["alt"])}</figcaption></figure>'
    )


def gallery_section(service_key, service_name, limit=9):
    items = photos_for(service_key)[:limit]
    if not items:
        return ""
    has_render = any(p["kind"] == "rendering" for p in items)
    note = (' Images marked "concept rendering" are illustrations of the finish, not job photos.' if has_render else "")
    figs = "\n".join(figure_html(p) for p in items)
    return f'''
<section class="alt">
  <div class="wrap">
    <span class="eyebrow">Recent work</span>
    <h2>{_esc(service_name)} — photos from the provider serving South Lake County</h2>
    <p class="lede">Job photos from the licensed provider that Groveland Concrete routes requests to. Projects shown are across Central Florida; every job is planned for its own lot, soil and access.{note}</p>
    <div class="gallery">
{figs}
    </div>
    <p style="margin-top:18px"><a class="card-link" href="/gallery/">See the full photo gallery &rarr;</a></p>
  </div>
</section>
'''


def home_strip(limit=6):
    figs = "\n".join(figure_html(p) for p in featured(limit))
    return f'''
<section>
  <div class="wrap">
    <span class="eyebrow">Recent Work</span>
    <h2>Driveways, pool decks and walkways built by the provider we route to</h2>
    <p class="lede">Real job photos from Central Florida — paver driveways, marble and travertine pool decks, raised terraces and entry steps. See how the work is finished before you request an estimate.</p>
    <div class="gallery" style="margin-top:26px">
{figs}
    </div>
    <div class="cta-row" style="margin-top:22px">
      <a class="btn btn-outline" href="/gallery/">Browse the full gallery</a>
    </div>
  </div>
</section>
'''


def image_schema(items, base_url):
    return [{
        "@context": "https://schema.org",
        "@type": "ImageObject",
        "contentUrl": f"{base_url}/static/images/{p['slug']}-1600.webp",
        "name": p["alt"],
        "description": p["alt"] + (" (concept rendering)" if p["kind"] == "rendering" else ""),
        "width": p["w"], "height": p["h"],
    } for p in items]
