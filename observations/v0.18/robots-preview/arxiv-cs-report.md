# v0.18 ROBOTS-PREVIEW — `arxiv-cs`

Observed at **2026-07-28T14:00:57Z**. `arxiv-cs` is the only configured network
source; the other three configured sources are fixture-only `example.org`
placeholders.

## Wire result

- configured URL:
  `https://oaipmh.arxiv.org/oai?verb=ListRecords&metadataPrefix=oai_dc&set=cs`
- robots comparison target:
  `/oai?verb=ListRecords&metadataPrefix=oai_dc&set=cs`
- request count: **1**
- request URL and path: `https://oaipmh.arxiv.org/robots.txt`,
  `/robots.txt`
- redirects followed: **0**
- HTTP result: **404**, `Content-Type: text/html; charset=utf-8`
- raw response:
  [`arxiv-cs-robots.txt`](arxiv-cs-robots.txt), **11,083 bytes**
- raw-response SHA-256:
  `fe5a8ce88b89f96db55e8d9a7eb3d978f3d364bf31d48c4880422511e9035ab2`
- crawler product token/version: `intel-platform/0.15.1`; the monitored contact
  was loaded from the ignored `.env` and is intentionally not recorded

The feature-gated client constructs the literal `/robots.txt` URL and disables
redirects. Its executing loopback control observed exactly one request, for
`/robots.txt`, carrying the byte-identical installed crawler identity. The live
preview reported the same one request, literal path, and zero followed
redirects. No document or harvest URL was requested.

## Shipped-gate result

The publisher served no robots policy: the response is an arXiv 404 page, so
there is no applicable group or rule to parse.

- publisher-policy outcome: `Unavailable`
- selected group/product token: none (neither a specific group nor `*` exists)
- matched rule: none
- `Allow` exception: none
- `Crawl-delay`: none
- configured per-source `MissingPolicy`: `robots_on_missing: "allow"` →
  `RfcAllowAll`
- configured-target verdict: **allow**
- Step 4 decision: **GO**

This is absence-only permission. It does not override an explicit `Disallow`,
and a 5xx, DNS, TLS, connection, or timeout failure would still deny.

## Executed controls

- Fail-before matcher diagnostics: the focused build exited **101** because
  `parse_with_diagnostics` and its group/decision provenance types did not
  exist.
- Pass-after matcher diagnostics: **2/2** focused and **40/40** complete
  `intel-compliance --features diagnostics`.
- Fail-before preview control: the focused build exited **101** with
  `fetch_robots_preview`, `robots_preview_target`, and the preview fixture
  absent.
- Pass-after preview controls: **30/30** ingest library tests plus **1/1**
  preview-binary test under `--features robots-preview`. The loopback-only
  preview test proved the single `/robots.txt` request and installed
  User-Agent; its first sandboxed attempt was a non-result because sandboxing
  refused the loopback bind, and the identical permitted invocation passed.
- Full acceptance: local CI **20/20** with **131** workspace tests, **55** net
  tests, shell **244/244**, zero warning/lint/format failures, locked Rust 1.78,
  all **146/146** pins, protected databases **2/2**, and golden **11/11**. The
  first supplemental preview clippy run found two `needless_borrow` warnings;
  the two call sites were corrected and preview clippy then passed with
  `-D warnings`. The mandatory final standalone golden remained **11/11**.
