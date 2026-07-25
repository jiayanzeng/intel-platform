# V2 `/view` cold-path design

Status: design only, measured 2026-07-25. This task adds diagnostics and
failure-capable controls. It creates no cache table, schema migration, or
persisted derived response.

## Measured target

`./run benchmark-view --decompose` ran two independent rounds of ten cold
processes against byte-for-byte disposable copies of both protected archives.
Every report contains min/median/p95/max and p95 share for every stage:

- `evidence/v0.10/view-decomposition/run-1-core-1764.json`
- `evidence/v0.10/view-decomposition/run-1-live-smoke-2600.json`
- `evidence/v0.10/view-decomposition/run-2-core-1764.json`
- `evidence/v0.10/view-decomposition/run-2-live-smoke-2600.json`

The compact p95 result is:

| run / archive | cold total | spawn → ready | store open | fingerprint backfill | sector load | analysis | response build | serialization | HTTP transfer |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 / 1,764 | 1696.949 ms | 1344.249 (79.216%) | 2.845 (0.168%) | 1.857 (0.109%) | 14.453 (0.852%) | 330.248 (19.461%) | 1.217 (0.072%) | 5.091 (0.300%) | 1.202 (0.071%) |
| 1 / 2,600 | 540.458 ms | 35.547 (6.577%) | 3.700 (0.685%) | 3.138 (0.581%) | 36.963 (6.839%) | 463.776 (85.812%) | 1.605 (0.297%) | 7.739 (1.432%) | 1.645 (0.304%) |
| 2 / 1,764 | 374.208 ms | 34.142 (9.124%) | 2.233 (0.597%) | 1.671 (0.447%) | 15.493 (4.140%) | 319.076 (85.267%) | 0.972 (0.260%) | 4.896 (1.308%) | 1.054 (0.282%) |
| 2 / 2,600 | 544.959 ms | 34.284 (6.291%) | 3.096 (0.568%) | 2.497 (0.458%) | 22.148 (4.064%) | 479.292 (87.950%) | 1.582 (0.290%) | 7.658 (1.405%) | 1.209 (0.222%) |

Store-open is nested inside process startup. Its JSON breakdown separately
reports connection open, schema/FTS creation, cursor migration, and the
explicit missing-fingerprint backfill. All 40 processes reported zero
fingerprints backfilled; the backfill check itself was at most 3.138 ms.

Outside one reproduced startup outlier, analysis is the dominant cost at
85.267–87.950% of cold p95. Sector load is second at 4.064–6.839%.
Serialization and HTTP transfer are small. A future persisted result should
therefore remove analysis from restart-cold requests; optimizing SQLite open,
fingerprint backfill, or transport would not address the measured miss.

### The retained V1 outlier

V2 reproduced V1's 1,693.423417 ms outlier as a 1,696.948500 ms cold sample.
The harness localized 1,344.248750 ms to process spawn → health readiness, but
the core reported only 4.430 ms from Rust `main` entry to listener readiness,
including a 2.845 ms store open. The 1,341.403750 ms residual therefore lies
outside the timed core startup path, between process creation and observed
health readiness. That stage explains the total's magnitude and proves it was
not SQLite schema work or fingerprint backfill; the underlying host scheduling
cause is not further explained by this instrumentation. It is retained in the
distribution and p95.

## Candidate restart-safe key

The candidate key is:

```
SHA-256(
    resolved archive identity
    || canonical sector set
    || view algorithm/schema version
    || SQLite schema
    || every ordered documents row and column
    || every ordered embeddings row and column
)
```

`python3 tools/view_invalidation.py control` proves that the key changes for
all nine required inputs: archive identity, sector set, algorithm/schema
version, append, update, delete, canonical-id rematerialization, fingerprint
refresh, and embedding write. The control deliberately hashes the complete
logical rows instead of file bytes, so SQLite WAL/checkpoint layout cannot
hide a committed mutation. It is conservative: an embedding write invalidates
the result even though the current view algorithm does not consume embeddings.

The failure-capable counterexample
`python3 tools/view_invalidation.py control --omit-component embeddings`
exits non-zero with `embedding-write: STALE-RESULT RISK`. A future optimized
revision/ledger key is acceptable only if the same control is adapted to the
implemented key and still detects all nine inputs transactionally.

## Future representation and lifecycle

A future implementation task may persist the already license-gated serialized
`ViewResp` plus its candidate key as core archive/query state. It must not
persist source bodies or any alternate DTO. On lookup, core must:

1. canonicalize and validate the sector set against configured sectors;
2. enforce the same sector predicate in core SQL before either building or
   validating a result;
3. compute or transactionally maintain the complete restart-safe key;
4. return a persisted response only on an exact key match;
5. rebuild after every detected mutation, using the existing global
   canonical-id and persisted-fingerprint rules.

The future implementation may replace the full logical digest with
transactional revision components to reduce validation cost, but it may not
replace any input with the current in-memory generation. A generation that
resets at restart cannot validate a persisted result.

## Architectural constraints

- **HC1:** persist only the current core-produced `ViewResp`. Its evidence
  excerpt remains `null` for `IndexOnly`; no raw gated body enters the
  representation or a public response.
- **HC2:** the shell still supplies entitlements, while the core's SQL sector
  filter remains mandatory. A materialized result is keyed by the exact
  canonical sector set and cannot replace SQL enforcement.
- **HC3:** keying, loading, analysis, and serialization remain deterministic
  core work. No LLM call is introduced.
- **Dedup identity:** canonical ids remain a corpus-global rematerialization,
  retrieval remains rank-aware, and fingerprint refresh plus canonical-id
  changes both invalidate the key.
- **HC9:** any future persisted view is core archive/query state in the core
  SQLite store, never shell-owned configuration.

## Future implementation acceptance

The implementation task must rerun V1's exact two-archive, two-run benchmark:
ten process-restart cold samples and 100 warm samples per archive/run. Every
cell must meet the predeclared cold p95 ≤ **162.640 ms** and warm p95 ≤
**32.528 ms** thresholds. It must also pass the nine-input stale-result
control and the isolated-stage delay control; preserve the two current
protected hashes; preserve the exact `/view` body hashes
`43af73a…784f` (1,764) and `5685e69a…f81` (2,600); and leave
`./run golden` at 11/11. No threshold or baseline may be edited to bless a
miss.
