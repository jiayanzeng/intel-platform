# v0.38 WIRE-ADMISSION — SEC EDGAR admission report

Measured on **2026-08-04** local time under the operator's initiating Grant B.
The grant text is recorded verbatim before execution in
`docs/cycles/PROGRESS-v0.38.md`.

## Evidence-before-harvest result

The dated evidence capture completed first. Its exact per-request facts and
DR12 comparisons are in `sec-edgar-evidence-comparison.md`: one sequential,
no-redirect, no-retry request each for the publisher's robots policy, published
access terms, and configured US GAAP RSS feed; all returned HTTP 200. The
robots bytes are identical to v0.25, the current terms preserve every material
condition of the pinned determination, and the changing RSS contents preserve
the measured 200-item parser-facing shape. DR12 therefore passed and allowed
admission to proceed.

The observation files remained read-only evidence. They were never named to or
read by the harvest entry point. The capture is the HTTP status, `Location`,
request-count, request-ordering, and timing witness; the separate harvest below
is the production-parser and fresh-persistence witness. The production log does
not expose response headers or an HTTP request counter, so this report does not
misattribute the capture's HTTP telemetry to the later parser request.

## Production live harvest

Immediately before harvest, `./run down` reported a clean shutdown state and
`lsof -iTCP:8788 -sTCP:LISTEN -n -P` found no listener. The required
`./run verify-artifacts` preflight matched **2 artifacts / 338 pinned files**.
The configured monitored contact was present; it is deliberately redacted from
this record.

One permission-complete `./run harvest-sec` invocation selected the fresh path
`data/live-20260803T195324Z-37051.db`, built and started the `net` core with
`config/core.json`, and posted only sector `finance` and source
`sec-edgar-usgaap`. The source configuration still names the live URL
`https://www.sec.gov/Archives/edgar/usgaap.rss.xml`; no fixture or observation
path was introduced. The resulting stdout facts were:

```text
SEC wire ingest: {"coverage":"first_window","documents":200,"fetched":200,"new":200,"source_id":"sec-edgar-usgaap"}
ARCHIVE: {"database":"data/live-20260803T195324Z-37051.db","documents":200,"integrity_check":"ok","licenses":["PublisherPermitted"],"null_canonical_id":0,"null_simhash":0,"sec_documents":200}
WIRE: robots: https://www.sec.gov -> Body(allow); path=/Archives/edgar/usgaap.rss.xml; allowed=true; effective-crawl-delay=0.500s
WIRE: ingest coverage: source_id=sec-edgar-usgaap outcome=first_window poll_continues=true
SEC_HARVEST_DB=data/live-20260803T195324Z-37051.db
SEC_HARVEST_LOG=.run/cored.log
stopped.
```

The first-window result is nonempty and exact: **200 fetched / 200 new / 200
stored**. The live robots cache fetched the publisher policy, allowed the exact
RSS path, and applied the **0.500-second** effective delay before the document
request. The successful parser result came from the live configured feed, not
the evidence copy. The process owned by the harness then shut down cleanly.

This was one manual, single-source admission harvest. It is not a recurring
scheduler run and supplies no concurrency, conditional GET/304, repeated-fetch,
retry-count, redirect-count, or historical-backfill result.

## Fresh archive facts

The immutable candidate archive measures:

- SHA-256:
  `fb1046b79e7501d51e2dde3fd89fb7dfe0094defa6205b12afb39a21dff06044`
- bytes: **253,952**
- `PRAGMA integrity_check`: **ok**
- documents: **200**
- exact source / sector / license population:
  `sec-edgar-usgaap` / `finance` / `PublisherPermitted` = **200**
- published-day ordinal range: **20,665–20,668**
- null `simhash`: **0**; null `canonical_id`: **0**
- noncanonical rows: **0**; distinct canonical identities: **200**
- cursors: **0**; embeddings: **0**; signal-history rows: **0**

The zero cursor count is expected for this non-paged latest-window RSS source;
it is not a conditional-request or recurrence claim.

## Entitlement and licensing result

The actual public shell was exercised through its `v1/signals` handler against
the fresh archive and the two committed hashed subscriptions. The shell
resolved each presented configured token, passed only that subscription's
sectors to core, and core applied its SQL sector filter:

| Subscription | Entitled sectors | Documents analyzed | SEC addition |
|---|---|---:|---|
| `acme-research` | `science`, `technology` | **0** | none |
| `quant-desk` | `finance` | **200** | **200 SEC documents** |

Both responses named the expected client and sectors, and both reported zero
near-duplicate collapses. Thus the only intended entitlement movement is the
**200-document finance addition for `quant-desk`**. `acme-research` remains
unable to observe the SEC corpus. The stored value `PublisherPermitted` is
already expressible and was returned through the fixture-backed retrieval gate
in Step 2; the live archive re-measures all 200 rows with that exact license.
No subscription configuration, sector assignment, or public response domain
changed.

## Admission disposition

**Admit.** Fresh evidence is materially compatible under DR12; the production
live path persisted a coherent first window; the fresh archive is internally
sound; and entitlement/license outcomes match the designed finance-only
addition. The database is therefore eligible for a new non-retroactive initial
record under `artifacts[]`. The five capture files plus this report are
observation-grade `pinned_files[]`; they carry no admission chain.
