# -*- coding: utf-8 -*-
"""Shared structural data for grovelandconcrete.com.

Positioning: Groveland Concrete is a concrete & paving contractor (service-area
business) serving Groveland and South Lake County — same model as
ocoeeconcrete.com / windermereconcrete.com. Never "general contractor", never a
license number: "Fully Insured" / "Free Estimates" / "Written Workmanship
Warranty" only. No fake reviews, project counts or years-in-business."""

DOMAIN = "grovelandconcrete.com"
BASE_URL = f"https://{DOMAIN}"
PUBLIC_NAME = "Groveland Concrete"

BUSINESS = {
    "public_name": PUBLIC_NAME,
    "domain": DOMAIN,
    "phone_placeholder": "(352) 604-5480",
    "phone_tel_placeholder": "+13526045480",
    "email_placeholder": "hello@grovelandconcrete.com",
    "destination_email_placeholder": "opusdigitalmarketingflorida@gmail.com",
    # Short "who we are" blurb — used in the footer, the trust box on service/city/guide
    # pages, llms.txt and the Organization schema. (Key name kept for compatibility.)
    "disclosure_short": (
        "Groveland Concrete is a concrete and paving contractor serving Groveland and South Lake "
        "County — concrete driveways, RV and boat pads, workshop slabs, patios, paver driveways "
        "and patios, pool decks, walkways, and retaining walls. Fully insured, free estimates, and every "
        "job backed by our workmanship warranty in writing."
    ),
    # Consent line under the forms / privacy policy.
    "disclosure_form": (
        "By submitting this form you agree that Groveland Concrete may contact you by phone, text, "
        "or email about your project. We do not sell your information to third parties."
    ),
    "trust_points": ["Concrete & Paving Contractor", "Fully Insured", "Free Estimates", "Written Workmanship Warranty"],
}

# Cloudflare Turnstile public site key. While this is still the placeholder the
# widget is NOT rendered on any form (see templates.turnstile_html), and the
# Pages Function skips verification while TURNSTILE_SECRET_KEY is unset — set
# both together when going live (OWNER-INPUTS.md).
TURNSTILE_SITE_KEY = "{{TURNSTILE_SITE_KEY}}"

BRAND = {
    "clay": "#6E3B25",
    "parchment": "#E3E1D8",
    "ink": "#201F1B",
    "ochre": "#C77F35",
    "ink_on_dark": "#EFE7DA",
}

# ---------------------------------------------------------------------------
# Cities Groveland Concrete owns the primary commercial intent for.
# Clermont and Montverde are intentionally excluded (Tier-1 overlap with
# windermereconcrete.com, deferred pending owner resolution).
# ---------------------------------------------------------------------------
CITIES = {
    "groveland": {
        "name": "Groveland",
        "route": "/groveland/",
        "county": "Lake County",
        "kind": "anchor",
    },
    "mascotte": {
        "name": "Mascotte",
        "route": "/mascotte/",
        "county": "Lake County",
        "kind": "city",
    },
    "minneola": {
        "name": "Minneola",
        "route": "/minneola/",
        "county": "Lake County",
        "kind": "city",
    },
    "howey-in-the-hills": {
        "name": "Howey-in-the-Hills",
        "route": "/howey-in-the-hills/",
        "county": "Lake County",
        "kind": "city",
    },
    "rural-lake-county": {
        "name": "Rural & Unincorporated Lake County",
        "route": "/rural-lake-county/",
        "county": "Lake County",
        "kind": "area",
    },
    "clermont": {
        "name": "Clermont",
        "route": "/clermont/",
        "county": "Lake County",
        "kind": "city",
    },
    "montverde": {
        "name": "Montverde",
        "route": "/montverde/",
        "county": "Lake County",
        "kind": "city",
    },
}
CITY_ORDER = [
    "groveland", "mascotte", "minneola", "howey-in-the-hills", "rural-lake-county",
    "clermont", "montverde",
]

# Clermont and Montverde also appear in windermereconcrete.com's declared
# Tier-1 radius. The owner has confirmed (2026-09-07) that sibling hubs may
# both publish pages about the same city as long as there is no textual
# duplication/similarity — verified for these two via an n-gram/diff check
# against windermereconcrete.com's live /clermont/ and /montverde/ pages
# before publishing. See research/01-radius-cities-south-lake.md for the
# overlap note and architecture/01-sitemap-and-url-ownership.md for the
# original (now superseded) deferral.
CITY_OVERLAP_NOTE = (
    "Clermont and Montverde also appear in a sibling hub's service area. "
    "Both sites may cover the same city as long as the content is not "
    "duplicated or textually similar — confirmed for these two pages."
)

SERVICES = {
    "concrete-driveways": {"name": "Concrete Driveways", "route": "/concrete-driveways/", "short": "Standard and long driveways, poured and finished for Florida sun and rain."},
    "rv-and-boat-pads": {"name": "RV & Boat Pads", "route": "/rv-and-boat-pads/", "short": "Concrete pads sized and reinforced for RVs, trailers, and boats."},
    "workshop-slabs": {"name": "Workshop Slabs", "route": "/workshop-slabs/", "short": "Slabs for workshops, metal buildings, and barns on rural lots."},
    "concrete-patios": {"name": "Concrete Patios", "route": "/concrete-patios/", "short": "Patios finished for Central Florida heat, humidity, and rain."},
    "concrete-repair-resurfacing": {"name": "Concrete Repair & Resurfacing", "route": "/concrete-repair-resurfacing/", "short": "Crack repair, resurfacing, and replace-vs-repair guidance."},
    "sidewalks-walkways": {"name": "Sidewalks & Walkways", "route": "/sidewalks-walkways/", "short": "Walkways and sidewalks sized and reinforced correctly."},
    "paver-driveways": {"name": "Paver Driveways", "route": "/paver-driveways/", "short": "Paver installation built for vehicle loads, base depth, and edge restraint."},
    "paver-patios": {"name": "Paver Patios", "route": "/paver-patios/", "short": "Paver patios and walkways for comfort, pattern, and outdoor living."},
    "retaining-walls": {"name": "Retaining Walls", "route": "/retaining-walls/", "short": "Retaining walls sized to solve real slope and drainage problems."},
}
SERVICE_ORDER = list(SERVICES.keys())

TOOLS = {
    "driveway-cost-calculator": {"name": "Driveway Cost & Volume Calculator", "route": "/tools/driveway-cost-calculator/", "short": "Estimate cubic yards and cost range for a standard or long driveway."},
    "rv-boat-pad-calculator": {"name": "RV & Boat Pad Calculator", "route": "/tools/rv-boat-pad-calculator/", "short": "Size a concrete pad to your RV, trailer, or boat."},
    "workshop-slab-guide": {"name": "Workshop Slab Thickness Guide", "route": "/tools/workshop-slab-guide/", "short": "Decision guide for slab thickness, edge detail, and vapor barrier."},
    "site-access-checklist": {"name": "Concrete Truck Site-Access Checklist", "route": "/tools/site-access-checklist/", "short": "Check whether a mixer truck can reach and turn around on your lot."},
    "drainage-slope-planner": {"name": "Drainage & Slope Planner", "route": "/tools/drainage-slope-planner/", "short": "Plan slope and drainage before you pour."},
    "permits": {"name": "South Lake Permit Directory", "route": "/permits/", "short": "Real links to the building/permit department for each jurisdiction in the service area."},
}
TOOL_ORDER = list(TOOLS.keys())

GUIDES = {
    "long-driveway-cost-florida": {"name": "How Much a Long Driveway Really Costs in Florida", "route": "/blog/long-driveway-cost-florida/"},
    "concrete-truck-access-rural-driveway": {"name": "Can a Concrete Truck Reach a House on a Long Rural Driveway?", "route": "/blog/concrete-truck-access-rural-driveway/"},
    "concrete-vs-gravel-driveway-florida": {"name": "Concrete vs. Gravel for a Long Rural Driveway in Florida", "route": "/blog/concrete-vs-gravel-driveway-florida/"},
    "rv-pad-vs-driveway": {"name": "RV Pad vs. Driveway: What's the Difference?", "route": "/blog/rv-pad-vs-driveway/"},
    "boat-pad-vs-rv-pad": {"name": "Boat Pad vs. RV Pad: Do You Need Different Concrete?", "route": "/blog/boat-pad-vs-rv-pad/"},
    "best-base-sandy-soil-florida": {"name": "The Best Base for Concrete on Sandy Central Florida Soil", "route": "/blog/best-base-sandy-soil-florida/"},
    "why-concrete-driveway-cracking": {"name": "Why Is My New Concrete Driveway Already Cracking?", "route": "/blog/why-concrete-driveway-cracking/"},
    "maintain-concrete-driveway-florida-climate": {"name": "Maintaining a Concrete Driveway in Florida's Climate", "route": "/blog/maintain-concrete-driveway-florida-climate/"},
    "fixing-flooding-sloped-driveway": {"name": "Fixing a Sloped Driveway That Floods in Florida Rainstorms", "route": "/blog/fixing-flooding-sloped-driveway/"},
    "repair-vs-replace-driveway": {"name": "Repair or Replace? Deciding on an Aging Driveway", "route": "/blog/repair-vs-replace-driveway/"},
    "resurfacing-vs-new-pour-cost": {"name": "Resurfacing vs. a New Pour: Comparing the Real Cost", "route": "/blog/resurfacing-vs-new-pour-cost/"},
    "is-resurfacing-worth-it-before-selling": {"name": "Is Resurfacing a Driveway Worth It Before Selling a Rural Property?", "route": "/blog/is-resurfacing-worth-it-before-selling/"},
}
GUIDE_ORDER = list(GUIDES.keys())

COMPARISONS = {
    "rebar-vs-wire-mesh": {"name": "Rebar vs. Wire Mesh for a Concrete Driveway", "route": "/compare/rebar-vs-wire-mesh/"},
    "paver-vs-concrete-driveway": {"name": "Paver Driveway vs. Concrete Driveway in Florida", "route": "/compare/paver-vs-concrete-driveway/"},
    "stamped-vs-plain-patio": {"name": "Stamped Concrete vs. a Plain Patio", "route": "/compare/stamped-vs-plain-patio/"},
}
COMPARISON_ORDER = list(COMPARISONS.keys())

NAV_PRIMARY = [
    ("Services", "/services/"),
    ("Service Area", "/service-area/"),
    ("Tools", "/tools/"),
    ("Permits", "/permits/"),
    ("Blog", "/blog/"),
    ("About", "/about/"),
]

FOOTER_LEGAL = [
    ("Privacy Policy", "/privacy-policy/"),
    ("Terms", "/terms/"),
    ("Accessibility", "/accessibility/"),
]
