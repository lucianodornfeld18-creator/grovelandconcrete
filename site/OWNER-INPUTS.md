# Owner inputs needed — grovelandconcrete.com

Nothing below is published with real values yet. The site works and builds with placeholders; swap these in Cloudflare before going live.

## Required before launch

Nothing blocks the lead form any more — it posts to Web3Forms and was verified working on 2026-09-12.

| Placeholder | Where it's used | What to provide |
|---|---|---|
| `{{TURNSTILE_SITE_KEY}}` | `_data.py` → rendered on the `/` hero form and `/contact/` form | Optional now. The widget is not rendered while this is the placeholder. Verification no longer happens on our side: if you turn Turnstile on, set the site key here **and** the matching secret on the Web3Forms access key in the Web3Forms dashboard, or every submission is rejected. |

## Lead form — Web3Forms (2026-09-12)

Both lead forms (`/` hero, `/contact/`) POST to `https://api.web3forms.com/submit` with the access key
`2e0e19f8-95b6-4a53-a05d-f1bd94f16650`, set in `_data.py` as `WEB3FORMS_ACCESS_KEY`. The key is public
by design — it ships in the HTML and only authorises posting to that one endpoint.

- **Where leads land:** whatever inbox is registered against that access key in the Web3Forms account.
  That is set on Web3Forms' side, not in this repo — check it there before relying on it.
- Hidden fields per form: `access_key`, `subject` (says which page the lead came from), `from_name`,
  `redirect` (→ `/thank-you/`, only used when JS is off), `page_url`, and `botcheck` — Web3Forms' own
  honeypot, which replaced the old `company` honeypot the retired Pages Function used to check.
- `site.js` intercepts the submit and posts JSON, so it can show Web3Forms' error message instead of a
  guess; with JS off the native POST goes through and `redirect` lands the visitor on `/thank-you/`.
  UTM/gclid tags are appended only when the visitor actually arrived with them.
- CSP had to be widened for this: `form-action` and `connect-src` now include `https://api.web3forms.com`
  (`build.py`). Without the `form-action` entry the browser blocks the no-JS submit outright.
- **The old path still exists but is dead:** `functions/api/contact.js` → `grovelandconcrete-contact`
  Worker, plus the `CONTACT_EMAIL` service binding and `RATE_LIMIT_KV` in `wrangler.jsonc`. Nothing links
  to it. Kept as a one-line fallback (point the two form actions back at `/api/contact`). Delete the
  Function, the Worker and the binding once Web3Forms has proven itself.

## Already filled in (2026-09-08)

- Positioning (2026-09-09): Groveland Concrete presents as a concrete & paving contractor, same model as ocoeeconcrete/windermereconcrete. No "information resource" / "routed to a provider" language anywhere. Never say "general contractor", never "we are not", never a license number — Fully Insured / Free Estimates / Written Workmanship Warranty.

- Email: `hello@grovelandconcrete.com` is a Cloudflare Email Routing alias forwarding to `opusdigitalmarketingflorida@gmail.com` (destination verified on the account). The contact worker's `CONTACT_DESTINATION` secret points at the same Gmail.

- Phone `(352) 604-5480` / `+13526045480` is live in `_data.py` (`BUSINESS.phone_placeholder` keys kept their old names).
- `RATE_LIMIT_KV` namespace ID is set in `wrangler.jsonc`.
- Textual similarity check vs. windermereconcrete.com (`/groveland/`, `/minneola/`, `/clermont/`, `/montverde/`): 0 shared 8-grams on 2026-09-08 — the no-duplication rule holds for all four.
- Logo: owner-supplied GC lockup is in production (header horizontal lockup, footer stacked with light wordmark, favicons). See `brand/00-brand-guide.md`.

## Cloudflare setup checklist

0. **www redirect (dashboard only):** Rules > Redirect Rules > template "Redirect from WWW to root" (301). Pages `_redirects` cannot match a hostname, so this is the only place it can live.

1. Create the Pages project, connect this repo, set build output directory to `dist` (no build command needed — run `python build.py` locally/in CI before deploy, or wire it as the Pages build command if Python is available in the build image).
2. ~~Create the `grovelandconcrete-contact` Worker (`workers/contact-email/`) and bind it as a service in `wrangler.jsonc`.~~ Done, now unused — Web3Forms delivers the leads.
3. ~~Set the `CONTACT_DESTINATION` secret on the contact-email worker to the real destination email.~~ Done, now unused.
4. Enable Cloudflare Email Routing for the domain and verify the sender address used in `workers/contact-email/src/index.js` (`hello@grovelandconcrete.com`).
5. ~~Create a Turnstile widget for the domain; put the site key in `/contact/`'s `data-sitekey` and the secret key as `TURNSTILE_SECRET_KEY` on the Pages Function environment.~~ Superseded 2026-09-12: Turnstile, if wanted, is configured on the Web3Forms access key (see above).
6. ~~Create a KV namespace for `RATE_LIMIT_KV` and put its ID in `wrangler.jsonc`.~~ Done, but only the retired Pages Function used it.
7. Point DNS for `grovelandconcrete.com` at the Pages project once approved for launch.
8. Register the domain property in Google Search Console (Domain property) and Bing Webmaster Tools; submit `sitemap.xml`; enable IndexNow with a generated key.

## Still open from the research/build phase

- Confirm the Ocoee/GCM Best Services catalog files found on the old SSD (`Projetos\ocoeeconcrete`, `gcm-site`) are the current, authoritative version.
- Palette tokens (`clay`/`ochre` etc.) still come from the retired Township Grid direction; the logo's own accent is orange `#F26A1B`-ish. Decide whether to shift `--clay`/`--ochre` toward the logo orange for buttons/links.
