# -*- coding: utf-8 -*-
"""Aggregator/hub index pages built purely from the _data.py registries, so
they stay correct automatically as content modules add real pages."""
from _data import (
    SERVICES, SERVICE_ORDER, CITIES, CITY_ORDER, TOOLS, TOOL_ORDER,
    GUIDES, GUIDE_ORDER, COMPARISONS, COMPARISON_ORDER,
)


def _cards(order, registry, desc_key="short"):
    return "\n".join(
        f'''<div class="card">
          <h3><a href="{registry[k]["route"]}">{registry[k]["name"]}</a></h3>
          {f'<p>{registry[k][desc_key]}</p>' if registry[k].get(desc_key) else ""}
        </div>''' for k in order
    )


def get_pages():
    pages = []

    pages.append({
        "route": "/services/",
        "title": "Concrete & Hardscape Services",
        "meta_description": "Every concrete and hardscape service Groveland Concrete covers in South Lake County — driveways, RV/boat pads, workshop slabs, patios, repair, and more.",
        "h1": "Services",
        "breadcrumbs": [("Home", "/"), ("Services", None)],
        "nav_active": "/services/",
        "body_html": f'<div class="wrap" style="padding-bottom:60px"><p class="lede">Eight services, each confirmed with a real provider serving South Lake County — nothing advertised without a matching, staffed capability.</p><div class="grid grid-3" style="margin-top:24px">{_cards(SERVICE_ORDER, SERVICES)}</div></div>',
    })

    pages.append({
        "route": "/service-area/",
        "title": "Service Area — South Lake County",
        "meta_description": "Where Groveland Concrete focuses: Groveland, Mascotte, Minneola, Howey-in-the-Hills, Clermont, Montverde, and rural/unincorporated Lake County.",
        "h1": "Service Area",
        "breadcrumbs": [("Home", "/"), ("Service Area", None)],
        "nav_active": "/service-area/",
        "body_html": f'''<div class="wrap" style="padding-bottom:60px">
  <p class="lede">We focus on Groveland and the rural, large-lot communities of South Lake County. Our Clermont and Montverde pages cover the acreage and lake-adjacent edges of those cities specifically — not their denser suburban cores, which a general contractor page is better suited for.</p>
  <div class="grid grid-3" style="margin-top:24px">{_cards(CITY_ORDER, CITIES, desc_key=None)}</div>
</div>''',
    })

    pages.append({
        "route": "/tools/",
        "title": "Planning Tools & Calculators",
        "meta_description": "Free calculators and planning tools for driveways, RV/boat pads, workshop slabs, drainage, and permits in South Lake County.",
        "h1": "Tools & Calculators",
        "breadcrumbs": [("Home", "/"), ("Tools", None)],
        "nav_active": "/tools/",
        "body_html": f'<div class="wrap" style="padding-bottom:60px"><p class="lede">Built from published Florida Building Code specs and Central Florida ready-mix pricing ranges — not a generic nationwide calculator.</p><div class="grid grid-3" style="margin-top:24px">{_cards(TOOL_ORDER, TOOLS)}</div></div>',
    })

    guide_and_compare_order = list(GUIDE_ORDER) + list(COMPARISON_ORDER)
    guide_and_compare_registry = {**GUIDES, **COMPARISONS}
    pages.append({
        "route": "/guides/",
        "title": "Guides & Comparisons",
        "meta_description": "Educational guides and side-by-side comparisons for concrete and hardscape decisions in South Lake County, FL.",
        "h1": "Guides & Comparisons",
        "breadcrumbs": [("Home", "/"), ("Guides", None)],
        "nav_active": "/guides/",
        "body_html": f'<div class="wrap" style="padding-bottom:60px"><div class="grid grid-2" style="margin-top:10px">{_cards(guide_and_compare_order, guide_and_compare_registry, desc_key=None)}</div></div>',
    })

    return pages
