# -*- coding: utf-8 -*-
from _data import SERVICES, BASE_URL, BUSINESS
from _photos import PHOTOS, photos_for, figure_html, image_schema

GALLERY_ORDER = ["paver-driveways", "paver-patios", "sidewalks-walkways", "retaining-walls"]


def get_pages():
    sections = []
    for key in GALLERY_ORDER:
        items = [p for p in photos_for(key) if p["services"][0] == key]
        if not items:
            continue
        figs = "\n".join(figure_html(p) for p in items)
        svc = SERVICES[key]
        sections.append(f'''
<section id="{key}" class="tight">
  <div class="wrap">
    <h2><a href="{svc["route"]}">{svc["name"]}</a></h2>
    <div class="gallery">
{figs}
    </div>
  </div>
</section>''')
    real = sum(1 for p in PHOTOS if p["kind"] == "real")
    body_html = f'''
<div class="wrap">
  <p class="lede">{real} job photos from Groveland Concrete crews, plus a few concept renderings (labelled) that show a finish before it is built. Projects are across Central Florida; the same crews, materials and specs serve Groveland, Mascotte, Minneola, Clermont, Montverde, Howey-in-the-Hills and rural Lake County.</p>
  <p class="form-note">Jump to: {" · ".join(f'<a href="#{k}">{SERVICES[k]["name"]}</a>' for k in GALLERY_ORDER)}</p>
</div>
{"".join(sections)}
<section>
  <div class="wrap" style="text-align:center">
    <h2>Want this on your lot?</h2>
    <p class="lede" style="margin:0 auto 20px">Tell us about your driveway, pool deck, patio or walkway and we'll put a written, line-itemized estimate together after a site walk.</p>
    <div class="cta-row" style="justify-content:center">
      <a class="btn btn-primary btn-lg" href="/contact/">Request a free estimate</a>
      <a class="btn btn-outline btn-lg" href="tel:{BUSINESS['phone_tel_placeholder']}">Call {BUSINESS['phone_placeholder']}</a>
    </div>
  </div>
</section>
'''
    return [{
        "route": "/gallery/",
        "title": "Photo Gallery — Paver Driveways, Pool Decks & Walkways",
        "meta_description": "Groveland Concrete job photos: paver driveways, marble and travertine pool decks, raised paver terraces, entry steps and walkways across Groveland and South Lake County.",
        "h1": "Photo Gallery",
        "breadcrumbs": [("Home", "/"), ("Photo Gallery", None)],
        "nav_active": "/services/",
        "body_html": body_html,
        "schema": image_schema([p for p in PHOTOS if p["kind"] == "real"], BASE_URL),
    }]
