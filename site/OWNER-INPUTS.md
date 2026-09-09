# Owner inputs needed — grovelandconcrete.com

Nothing below is published with real values yet. The site works and builds with placeholders; swap these in Cloudflare before going live.

## Required before launch

| Placeholder | Where it's used | What to provide |
|---|---|---|
| `{{LEGAL_PROVIDER_AND_LICENSE_IF_REQUIRED}}` | `Service` schema `provider.name` on service pages | Legal name (and license number, if legally required for this kind of advertising) of the provider requests get routed to |
| `{{TURNSTILE_SITE_KEY}}` | `_data.py` → rendered on the `/` hero form and `/contact/` form | Public site key from a Cloudflare Turnstile widget created for this domain. The widget is not rendered while this is the placeholder; set it together with `TURNSTILE_SECRET_KEY` on the Pages Function or every form submission will be rejected with 403. |

## Already filled in (2026-09-08)

- Email: `hello@grovelandconcrete.com` is a Cloudflare Email Routing alias forwarding to `opusdigitalmarketingflorida@gmail.com` (destination verified on the account). The contact worker's `CONTACT_DESTINATION` secret points at the same Gmail.

- Phone `(352) 604-5480` / `+13526045480` is live in `_data.py` (`BUSINESS.phone_placeholder` keys kept their old names).
- `RATE_LIMIT_KV` namespace ID is set in `wrangler.jsonc`.
- Textual similarity check vs. windermereconcrete.com (`/groveland/`, `/minneola/`, `/clermont/`, `/montverde/`): 0 shared 8-grams on 2026-09-08 — the no-duplication rule holds for all four.
- Logo: owner-supplied GC lockup is in production (header horizontal lockup, footer stacked with light wordmark, favicons). See `brand/00-brand-guide.md`.

## Cloudflare setup checklist

0. **www redirect (dashboard only):** Rules > Redirect Rules > template "Redirect from WWW to root" (301). Pages `_redirects` cannot match a hostname, so this is the only place it can live.

1. Create the Pages project, connect this repo, set build output directory to `dist` (no build command needed — run `python build.py` locally/in CI before deploy, or wire it as the Pages build command if Python is available in the build image).
2. Create the `grovelandconcrete-contact` Worker (`workers/contact-email/`) and bind it as a service in `wrangler.jsonc`.
3. Set the `CONTACT_DESTINATION` secret on the contact-email worker to the real destination email.
4. Enable Cloudflare Email Routing for the domain and verify the sender address used in `workers/contact-email/src/index.js` (`hello@grovelandconcrete.com`).
5. Create a Turnstile widget for the domain; put the site key in `/contact/`'s `data-sitekey` and the secret key as `TURNSTILE_SECRET_KEY` on the Pages Function environment.
6. Create a KV namespace for `RATE_LIMIT_KV` and put its ID in `wrangler.jsonc`.
7. Point DNS for `grovelandconcrete.com` at the Pages project once approved for launch.
8. Register the domain property in Google Search Console (Domain property) and Bing Webmaster Tools; submit `sitemap.xml`; enable IndexNow with a generated key.

## Still open from the research/build phase

- Confirm the Ocoee/GCM Best Services catalog files found on the old SSD (`Projetos\ocoeeconcrete`, `gcm-site`) are the current, authoritative version.
- Palette tokens (`clay`/`ochre` etc.) still come from the retired Township Grid direction; the logo's own accent is orange `#F26A1B`-ish. Decide whether to shift `--clay`/`--ochre` toward the logo orange for buttons/links.
- Legal review of `/contact/` disclosure language and whether the provider's name/license must appear before form submission in this jurisdiction.
