# TASKS-v0.27-EXECUTION.md — the window, not the clock

v0.16.1 is published and v0.26 is closed. Annotated object
`ae593e88…` targets closing commit `397d100a…`, whose parent is release commit
`b9af84b8…`; post-push run **30535121730** passed all seven executable jobs at
that exact commit, and authenticated candidate run **30531390933** remains the
closing evidence with 7 signed identities accepted and 0 rejected. The identity
correction shipped and was validated against an independently fetched sample:
**200 kept / 0 dropped** on live bytes, all twenty cross-issuer false collapses
gone, golden byte-identical at 11/11 with its Hamming-12 true positive intact.
**Every condition placed on the harvest was measured or explicitly returned as
not exercised**, including the one that mattered most — the fresh feature
distribution was `{4:40, 5:86, 6:48, 7:20, 8:5, 10:1}`, zero rows in the 11–25
calibration gap, so the 26-feature floor's justification survived contact with a
second real corpus.

**The sixth author-side unsatisfiable rule was mine, and so is the thing that
generated both of them.** Amendment 1 diagnosed schema 2's two disjoint
containers and fixed the instance — observations. Step 7 of that same file then
required a chained admission record for a hosted receipt set, which fails for the
identical reason: `pinned_files` rejects `admission` as an extra key, and
`artifacts` demands a SQLite-shaped `expected` that cannot truthfully describe a
JSON receipt. **I patched the instance and left the generator running.** The
generator is the operating contract's admission language, which reads as though
one admission mechanism covers every pinned byte. This cycle fixes that, with an
executable control, so the seventh instance cannot be written.

**The cadence was matched to the wrong half of the publisher's sentence.** The
committed feed body says, in one `<description>`: *up to 200 of the latest
filings … updated every 10 minutes.* v0.26 chose 600 seconds to match the second
clause. **The clause that governs safety is the first one.** A fixed
latest-N window does not lose data because it is rebuilt slowly; it loses data
when it rolls further than one poll interval, and nothing in this system measures
that or detects it when it happens.

**What the committed bytes say, measured before this file was written.** The 200
items span **77.5 minutes** — 16:13:52 to 17:31:22 EDT on 2026-07-29 — with a
**median gap of 11 seconds** between consecutive filings and a maximum gap of 215
seconds. At the density of the busiest observed hour (133 filings), the entire
200-item window turns over in roughly **90 minutes**. Against that, a 600-second
poll has about **7.75×** headroom. **The number may well be right. The recorded
reason for it is not, and the margin has never been written down.**

**Both live samples were taken while the publisher was idle.** The v0.25 capture
completed at **03:34:00Z** and the v0.26 corrective replay at **09:18:39Z** —
23:34 and 05:18 Eastern, both outside filing hours. The bodies are byte-identical
at SHA-256 `154556cd…`, and `lastBuildDate` stayed at 2026-07-29T21:50:03 EDT
across **7h28m**, which is itself a measured contradiction of the ten-minute
rebuild claim. **The byte identity is not evidence that the feed is slow. It is
evidence that neither measurement could test the thing that matters**, because
the window only moves when filings arrive, and none did.

**So the live path has never been observed under the only conditions that produce
loss.** That is this cycle's subject: make the loss detectable before anyone
runs the 600-second clock, which has still never run.

---

## Declared scope

| Scope class | Path or value |
|---|---|
| `scope_version` | `1` |
| `disposition_intent` | `release` |
| `allow` | `crates/store/src/lib.rs` |
| `allow` | `crates/store/src/sqlite.rs` |
| `allow` | `crates/ingest/src/lib.rs` |
| `allow` | `crates/ingest/src/rss.rs` |
| `allow` | `apps/cored/src/main.rs` |
| `allow` | `crates/**/tests/**` |
| `allow` | `shell/tests/**` |
| `allow` | `config/schedule.json` |
| `allow` | `config/invariant-rules.json` |
| `allow` | `tools/invariant_scan.py` |
| `allow` | `tools/cycle_check.py` |
| `allow` | `observations/**` |
| `allow` | `evidence/v0.27/deferred-audit/report.json` |
| `allow` | `AGENTS.md` |
| `allow` | `ARCHITECTURE.md` |
| `release_authority` | `Cargo.toml` |
| `release_authority` | `Cargo.lock` |
| `release_authority` | `crates/*/Cargo.toml` |
| `release_authority` | `apps/*/Cargo.toml` |
| `release_authority` | `shell/intel_shell/__init__.py` |
| `release_authority` | `shell/intel_shell/app.py` |
| `release_authority` | `CHANGELOG.md` |
| `release_authority` | `README.md` |
| `forbid` | `crates/compliance/src/**` |
| `forbid` | `crates/extract/src/**` |
| `forbid` | `crates/view/src/**` |
| `forbid` | `shell/intel_shell/[a-z]*.py` |
| `forbid` | `config/core.json` |
| `forbid` | `config/subscriptions*.json` |
| `forbid` | `config/protected-artifacts.json` |
| `forbid` | `tools/evidence_artifacts.py` |
| `forbid` | `fixtures/**` |
| `forbid` | `run` |

**The five production permissions are conditional on Step 4's decision.**
`apps/cored/src/main.rs` is permitted **only** to surface a coverage result on the
existing `/ingest` response and for nothing else. **If Step 4 records and defers,
all five go unmodified and Step 8 records each permission as unused.**

**`crates/extract/src/**` and `crates/view/src/**` are forbidden.** The identity
guard shipped and was validated against live bytes; **this cycle does not reopen
it.** `DEDUP_MIN_FEATURES` stays at 26 and both radius declarations stay at 16.

**`tools/evidence_artifacts.py` and `config/protected-artifacts.json` are
forbidden.** Step 5 corrects the *documentation* of what the validator does; it
does not change what the validator does. **A cycle that fixes prose by moving the
code it describes has fixed nothing.**

**Amendment obligation known in advance.** Step 7's hosted receipt directory is
`evidence/ci-runs/<run-id>-<attempt>/**` and its run id cannot exist until the
run does. **Step 7 adds that exact directory by a dated `## Runbook amendments`
entry in the same commit that first needs it** — and registers the receipts as
`pinned_files` with a `supporting` grade and **no `admission` key**, which is what
v0.26's amended Step 7 established works. This paragraph is notice, not
permission, and it is not a licence to edit the manifest for any other purpose.

## Runbook amendments

### 2026-07-30 — idle-sample elapsed time corrected by committed timestamps

The opening narrative and Step 2 item 4 drafted **7h28m** between the capture at
`2026-07-30T03:34:00Z` and the corrective content request at
`2026-07-30T09:18:39.680936Z`. Executing the subtraction measures
**5h44m39.680936s / 20,679.680936 seconds**. The timestamps and both requested
Step 2 conclusions are unchanged; only the authored elapsed-time claim is
wrong. WINDOW-MEASURE records the measured interval and does not bless the
draft.

---

## Entering state (asserted, not yet verified)

**Every sentence here is a hypothesis until Step 1 (E0) measures it.**

- `v0.16.1` is published. Release commit `b9af84b8785bcd52c16ab0225d66386ecd872c4d`,
  closing commit `397d100ae425d5d059cef8a8ddb2ac13cfde52f5`, annotated object
  `ae593e882898b9c49d5e91e2d50b6ca1f02ac49b`, post-push run **30535121730**.
  Closing evidence is candidate `1cd88acd99704cc76c866331e505db446936e469` and
  run **30531390933** on `refs/heads/codex/v0.26-evidence-1cd88ac`.
  **v0.26 is closed and is not reopened.**
- Local `main` is one commit ahead at post-push audit `e0d43ff…`, unpushed, under
  the accepted rhythm. **Do not amend, rebase, or squash it.**
- `ci-local` is 20/20. Workspace **139**; net **56** (**30** `intel-ingest`
  including replay + **26** `cored`). `invariant-scan` is **12 rules / 44
  controls**. Golden is **11/11**. `checklist-audit` is **208 checked / 3
  retracted / 208 matched / 0 exemptions**. Both Python lanes collect and pass
  **291** with zero skips; hosted passes 290 plus one named `on_site` skip.
  Retractions remain **three**.
- Pins are **286**; both protected databases exact; root `export-check` is **99
  derived / 7 required / 177 exported**.
- Two publisher sources are configured and **both have now been fetched, but
  never in one production runtime.** The 600-second SEC schedule **has never
  run.**
- The fifth and sixth author-side unsatisfiable rules and the quarantined CADENCE
  retrieval stand on the record as recorded. **No step here revisits any of
  them** except Step 5, which addresses what produced the fifth and sixth.
- A4, editable L1, R3/R4 open-bottom, the active-runbook measured-value
  heuristic, T7, robots negative-cache Decision B, the FastAPI version-literal
  relocation, terms-gate operator responsibility, and live multi-publisher
  behaviour remain open. L2 remains scheduled. `v0.8.0` and `v0.10.2` remain
  local-only. **No step in this file closes or narrows any of them.**

---

## Drafted gates

| Gate | Where | Hypothesis |
|---|---|---|
| **G1** [P1] | `crates/ingest/src/rss.rs`; `crates/store/src/lib.rs` `Cursors`; `crates/store/src/sqlite.rs` `append_new` | **Nothing can detect that the window rolled past between polls.** `Cursors::high_water` exists and the OAI-PMH path consumes it; `rss.rs`'s own module header lists conditional-GET cursors as an unimplemented production addition. Cross-poll de-duplication appears to rest on `INSERT OR IGNORE` by id, which cannot distinguish "nothing new" from "everything between the polls is gone." **Determine, by reading and by execution, whether any code, test, log line, or field would reveal a gap** — and state what the ingest result reports today for a re-fetched identical window. |
| **G2** [P1] | `observations/v0.25/feed-shape/sec-edgar-usgaap.rss.xml` (pinned) | **The window's span, not the rebuild interval, governs loss.** Confirm or refute from the pinned bytes: channel `description` declares *up to 200 of the latest filings … updated every 10 minutes*; the 200 items span **77.5 minutes** (16:13:52–17:31:22 EDT 2026-07-29); median consecutive gap **11 s**, maximum **215 s**; busiest observed hour **133** filings. Confirm `lastBuildDate` is 2026-07-29T21:50:03 EDT and unchanged between the 03:34:00Z and 09:18:39Z captures. **No publisher request: the bytes are pinned.** |
| **G3** [P1] | v0.26 HARVEST records; `crates/ingest/src/net.rs` | **The response's cache validators were never recorded, and the client could not use them if they were.** The corrective record names the absence of `Location` and `Retry-After` and says nothing about `ETag` or `Last-Modified`. Determine whether either was captured anywhere in committed evidence, and confirm that `get_text` sends no conditional request header. **If the validators were not captured, that is a gap in the harvest observation to record — not a reason to fetch anything.** |
| **G4** [P1] | `AGENTS.md`; `ARCHITECTURE.md`; `tools/evidence_artifacts.py` (read-only) | **The contract's admission language is the generator of the fifth and sixth unsatisfiable rules.** Enumerate every place the operating contract or architecture describes admitting a protected or pinned byte, and for each, state which of the two manifest containers it is true of. `artifacts[]` carries `admission` and requires SQLite-shaped `expected`; `pinned_files[]` takes arbitrary `evidence/`, `observations/`, or registered authorization paths and forbids `admission`. **Name every sentence that is true of neither or of only one while reading as though it covers both.** |
| **G5** [P2] | `config/core.json` (read-only); `run`; v0.26 HARVEST records | **Two origins in one production runtime is the last unexercised condition.** Both live phases were SEC-only and said so. Enumerate what it would take to exercise the origin-keyed robots cache and per-host limiter across both origins in one runtime, price each path against the `run` hash pin, and state the exact request count each would incur. |
| **G6** [P2] | `crates/store/src/sqlite.rs` `append_new` | **Determine what an identical re-fetch actually returns**, by execution: fetched, new, per-source `ok`, and whether canonical reassignment runs over the unchanged set. This is the baseline any coverage signal must be distinguishable from. |
| **G7** [P2] | `ARCHITECTURE.md §8`; v0.25 public value-domain criterion | **Whether the core-internal `/ingest` response body is a "named surface" for versioning has never been decided.** The v0.25 criterion is scoped to `/v1/*`. Step 4 may add a field to a core-internal body. **Determine the question and record it; do not let Step 8 improvise a version.** |

---

## How to run this file

Execute top to bottom, one task and one commit at a time. Follow `AGENTS.md §5`
after **every** task. Implementation and audit-record commits stay separate.

- **🤖 = Codex executes and self-verifies end to end** — no publication, no push
  to `main`, no ref creation or deletion **in the working repository**.
- **🧑 = exactly one named operator action or decision.**

**Interpretive rules, binding throughout.** An exit code of 0 from a construction
the checker never examined is **not measured**. A measurement that disagrees with
an acceptance criterion is **reported as measured**; the criterion is what gets
corrected. **A publisher's own sentence is evidence of what the publisher says,
not of what the publisher does** — where the two can be distinguished by
measurement, say which one a claim rests on. And **an undetected loss is worse
than a detected one**: a step that reduces the chance of losing a filing without
making loss visible has not discharged this cycle's objective.

**Dependency gates.** Step 2 blocks Steps 3 and 4. Step 3 and Step 4 are
independent of each other. Step 5 is independent and may run any time after Step
1. **Step 6 runs only if Steps 2, 3, 4, and 5 are complete and the operator
authorizes it**; deferral is a complete outcome. Step 7 is blocked by every
preceding implementation step; Step 8 by Step 7.

### Cycle activation (before E0)

In a separate preparatory implementation/audit pair: confirm the worktree is
clean and record the measured refs **without asserting a literal `origin/main`
hash in `STATE.md`'s header**. Commit **only** this runbook at
`docs/cycles/TASKS-v0.27-EXECUTION.md` — including its `## Declared scope` table
— the `AGENTS.md` header moving the active declaration from v0.26 to v0.27, and a
new `docs/cycles/PROGRESS-v0.27.md`. **Local `main` already carries the unpushed
post-push audit `e0d43ff…`; activation sits on top of it and does not amend,
rebase, or squash it.** If the trigger-bearing row count changes, correct the
exact lifecycle count control as v0.26 did and record it as a dated amendment.

### Global definition of done

Protected hashes exact; all 286 pins match until Step 7 adds more; **golden 11/11
byte-identical**; `./run version-check` green; zero rustc warnings on offline and
net builds; all Rust tests green; all shell tests green under Python 3.11 **and**
3.12; shell results recorded as collected / passed / skipped with every skip named
and compared by `tools/test_population.py`, never as a bare `N/N`; clippy, fmt,
ShellCheck, floor byte-compilation, and locked Rust 1.78 green.

**Golden and the SEC sample are both controls, in opposite directions.** Golden
must keep collapsing its Hamming-12 pair; the 200-document SEC set must keep
producing **200 kept / 0 dropped**. Any Step 4 change touches ingest and storage,
not identity — **so if either control moves, stop and record it as the finding**,
because a coverage change that alters identity behaviour has reached somewhere it
was not permitted to reach.

---

## Deferred means deferred

| Deferred item | Unchanged trigger | Measured 2026-07-30 | v0.27 action |
|---|---|---|---|
| T7 robots single-flight | a second concurrent harvester | 2026-07-30 — ingest is sequential; two configured sources are not two concurrent harvesters; both live phases were single-origin | **none — Step 6, if it runs, still does not fire this** |
| NEGATIVE-CACHE Decision B | a live transient robots outage for an admitted publisher while a usable last-known-good policy exists, plus operator authorization | 2026-07-30 — two live robots requests, both HTTP 200, byte-identical policy; no outage | none |
| Conditional GET (`ETag` / `If-Modified-Since`) | an operator-authorized cycle whose scope permits the `net` request path plus a live 304 observation | 2026-07-30 — three source module headers name it as unimplemented; `get_text` sends no validator; 892,641 bytes would transfer on every poll | **none — G3 records the gap, Step 4 does not implement it** |
| `edgar:*` extension field mapping | an operator-authorized cycle permitting `crates/ingest/src/**` for mapping, with a connector review | 2026-07-30 — all 15 observed extension local names enumerated and unmapped; bodies remain the form type alone | none |
| Live multi-publisher behaviour in one runtime | Steps 2–5 complete plus explicit operator authorization | 2026-07-30 — both origins fetched, never in one runtime; cache and limiter cross-origin behaviour unmeasured | **Step 6 — decided, not assumed** |
| Postgres / pgvector / multi-host seam | unchanged | 2026-07-30 — single writer, single host | none |
| A4 untrusted-shell boundary | a third-party/untrusted shell, or any claim HC1 is invariant under shell replacement | 2026-07-30 — one first-party shell; no such claim made | none |
| L2 forced-command wrapper | an operator server session | 2026-07-30 — none has occurred | none — remains scheduled |
| R3/R4 open-bottom coverage | a spelling outside registered vocabulary | 2026-07-30 — none observed | none |
| Third configured publisher | a completed compliance review, then a separate admission decision | 2026-07-30 — no review pending | none |
| `v0.8.0` / `v0.10.2` publication | operator-authorized push of both exact annotated objects | 2026-07-30 — not authorized | none — **no historical ref touched** |
| `--skip-local-tag-verification` removal | both historical tags published plus a passing hosted full-history `cycle-check` without the flag | 2026-07-30 — tags unpublished | none — **the flag stays** |
| Manifest retention/indexing | 1 MiB manifest, or two consecutive `verify-artifacts` runs ≥1.00 s | 2026-07-30 — 286 pins; re-measure at E0 | **Step 1 — re-measure only** |
| Version literal in `app.py` | a cycle whose declared scope permits shell source changes | 2026-07-30 — literal present; this cycle forbids `shell/intel_shell/[a-z]*.py` | none — recorded, not acted on |

---

## Step 1 · E0 — Rebuild the entering state and settle seven gates 🤖

**Objective.** Confirm HEAD is green and settle G1–G7.

**Gate.** Read-only repository, object, disposable-clone, and local execution
measurements plus `PROGRESS-v0.27.md` and this runbook's status records. **No
publisher request of any kind, and none is needed: every byte this cycle reasons
from is pinned or committed.** No ref created, moved, or deleted in the working
repository; `STATE.md`, `config/core.json`, and `config/schedule.json` unedited.

**Steps.**

1. Run the full entering matrix and standalone `./run golden`, plus
   `verify-artifacts`, `evidence-report`, `cycle-check`, `checklist-audit`,
   `progress-check`, `version-check`, `invariant-scan`, and `export-check` from
   the root. **Record shell as collected / passed / skipped and cite the
   comparator's derived output.**
2. **Settle G1 by reading and by execution.** Quote the RSS fetch path and
   `append_new` by file and line. State whether any cursor, watermark, log line,
   field, or test could reveal a rolled window, and **state what the `/ingest`
   response reports today** for a source whose window moved entirely.
3. **Settle G2 from the pinned bytes.** Report the channel `description`
   verbatim-in-substance, the window's first and last item timestamps and span,
   the median and maximum consecutive gaps, the per-hour counts, and
   `lastBuildDate` at both capture times. **Confirm or refute each drafted
   number.** If any differs, the measurement is the result and the runbook is the
   error.
4. **Settle G3.** Search committed evidence for `ETag` and `Last-Modified` on the
   live response and state whether either exists. Quote `get_text`'s request
   headers. **Record the observation gap without proposing to close it by
   request.**
5. **Settle G4.** Enumerate every admission-describing sentence in `AGENTS.md`
   and `ARCHITECTURE.md` with file and line, and classify each as true of
   `artifacts[]`, true of `pinned_files[]`, true of both, or **true of neither
   while reading as though it covers both**. The last class is the generator.
6. **Settle G5.** Enumerate and price the paths to a two-origin runtime, each
   with its exact request count and its effect on pinned bytes.
7. **Settle G6 by execution.** Ingest the same 200-document window twice into a
   fresh archive and report fetched, new, per-source `ok`, and whether canonical
   reassignment ran the second time.
8. **Settle G7.** State whether §8's "named surface" covers the core-internal
   `/ingest` body, with the reasoning, as a question for Step 8 to decide — **not
   as a decision E0 makes.**
9. Re-measure manifest size and `verify-artifacts` wall time. Re-verify the
   published `v0.16.1` objects and all 286 pins.

**Acceptance criteria.** Entering matrix with both interpreters and comparator
citation · G1 answered by reading **and** execution with the current `/ingest`
report stated · G2's every drafted number confirmed or refuted from pinned bytes
· G3 answered with `get_text`'s headers quoted and the gap recorded · G4's
sentences enumerated and classified with the neither-class named · G5's paths
priced with request counts · G6 answered by execution · G7 stated as a question
with reasoning · manifest and verify time freshly measured · published objects
and all pins re-verified · golden 11/11 · **no publisher request made**.

**Done when** every gate carries a measurement and G1 says, in one sentence,
what the system would report if it lost a filing.

---

## Execution records

### E0 execution record — 2026-07-30

**Entering matrix.** `./run ci-local` passed all twenty jobs at the cycle
activation descendant. The workspace carried **139** tests; the two net lanes
carried **56** tests (**30** ingest, including the SEC replay, and **26**
cored). Current and locked Rust 1.78 warning-denied builds, clippy, fmt,
ShellCheck, floor byte-compilation, the embedded golden, and all **12**
registered invariant rules / **44** planted controls passed. The first
sandboxed invocations of `ci-local` and standalone golden could not bind a
loopback listener and were recorded as environment non-results; both passed at
their actual entry points when rerun with loopback permission. Standalone
golden passed **11/11**.

Independent clean constrained Python 3.11.4 and 3.12.13 rebuilds each collected
**291**, passed **291**, failed **0**, and skipped **0**; each named the one
collected `on_site` test and emitted the accepted Starlette deprecation warning.
The required comparator, run over their machine-readable summaries, derived:

`test-population-compare: {"collected":291,"equivalent":true,"equivalent_passed":291,"hosted":{"on_site_skipped":0,"passed":291,"skipped":[]},"local":{"passed":291,"skipped":0},"schema_version":1}`

Standalone `evidence-report`, `cycle-check`, `checklist-audit`,
`progress-check`, `version-check`, and `invariant-scan` passed. Root
`export-check` passed **99 derived / 7 required / 179 exported** after its
sandboxed npm lookup was recorded as an environment non-result and the command
was rerun with network permission.

**G1 — RSS has no window-position state.** The RSS fetch path at
`crates/ingest/src/rss.rs:26-42` either reads the complete fixture or calls
`net::get_text`; `Source::fetch` at lines 58-86 reparses every descendant
`item`. It never reads or writes `SourceContext.cursors`; cored states at
`apps/cored/src/main.rs:812-815` that RSS ignores the cursor adapter.
`SqliteStore::append_new` at `crates/store/src/sqlite.rs:201-210` inserts the
present ids and runs canonical assignment only when its inserted count is
positive. Finally, `/ingest` at `apps/cored/src/main.rs:818-871` reports the
number fetched, the number newly inserted, and per-source `ok`, document count,
and error.

No RSS cursor, watermark, response field, log line, or test retains the oldest
or newest member of the preceding latest-200 window or reports an id that
disappeared. The existing repeat-ingest coverage establishes idempotence for
the same ids, not window continuity. Executing cored offline against the pinned
body and a fresh archive produced HTTP 200 with
`{"fetched":200,"new":200,"results":[{"sector":"finance","source_id":"sec-edgar-usgaap","ok":true,"documents":200,"error":null}]}`
and, on the identical second ingest, HTTP 200 with the same source result but
`"new":0`. Between calls, a failure-capable SQLite trigger was installed to
abort any `canonical_id` update; the second call still returned 200, proving
canonical reassignment did not run when `append_new` returned zero. The archive
held 200 documents, zero null canonical ids, and zero cursor rows.

**If one or more filings leave the latest-200 window before any poll observes
them, a completely advanced replacement window reports ordinary success —
`fetched=200`, `new=200`, source `ok=true` — and reports no loss.**

**G2 — all draft quantities confirmed from the pinned bytes.** An independent
byte parse measured **892,641** bytes at SHA-256 `154556cd81bda4fc2372386bf43aa7b4414335560dd1371c45bae09f1a8d9de3`
and the channel description: “This is a list of up to 200 of the latest filings
containing financial statements tagged using the US GAAP or IFRS taxonomies,
updated every 10 minutes.” There are **200** items, newest-first. The oldest is
`Wed, 29 Jul 2026 16:13:52 EDT`, the newest is
`Wed, 29 Jul 2026 17:31:22 EDT`, and the span is **4,650 seconds / 77.5
minutes**. Across the timestamp-sorted items, the median consecutive gap is
**11.0 seconds** and the maximum is **215.0 seconds**; the EDT hour counts are
`{16: 133, 17: 67}`. Channel `lastBuildDate` and `pubDate` are both
`Wed, 29 Jul 2026 21:50:03 EDT`. The 03:34:00Z and 09:18:39Z captures were
byte-identical, so every quantity, including `lastBuildDate`, was identical at
both capture times. Every drafted number is confirmed.

**G3 — validators were neither captured nor usable.** A repository-wide search
found no committed live-response `ETag` or `Last-Modified`; the v0.26 record
captured absence of `Location` and `Retry-After` only. At
`crates/ingest/src/net.rs:149-166`, the document client sets the installed
`User-Agent`; the locked reqwest 0.11.27 builder supplies
`Accept: */*`. Lines 171-178 then issue exactly
`client.get(url).send()` with no request-specific header. Thus the effective
application headers are `User-Agent: intel-platform/<version> (research
prototype; contact: <operator contact>)` and `Accept: */*`, with no
`If-None-Match` or `If-Modified-Since`. This is an observation gap, not
permission to issue another request: each successful poll currently transfers
the complete 892,641-byte body.

**G4 — admission-language classification.** The admission-describing statements
were enumerated as follows:

| Statement | Classification |
|---|---|
| `ARCHITECTURE.md:49`, the manifest holds immutable artifact facts and chained admissions | both, as a file-level inventory statement |
| `ARCHITECTURE.md:67`, “Protected-artifact admission is an executable append-only chain” | **neither when “protected-artifact” is read to cover both containers** |
| `ARCHITECTURE.md:68-70`, current artifact SHA equals newest admission and `prior_sha256` chains | `artifacts[]` |
| `ARCHITECTURE.md:70-72`, every admission record names task/date, wire evidence, approval, and retroactivity | `artifacts[]` |
| `ARCHITECTURE.md:72-76`, validate the chain and verify recorded bytes/facts; initial A2 records are retroactive | `artifacts[]` for the chain and initial records; both containers are byte-validated by the named commands |
| `AGENTS.md:412-415`, the two databases' provenance authority and immutability | `artifacts[]` |
| `AGENTS.md:417-421`, “Protected-artifact admission is executable under manifest schema v2” and a new artifact/hash requires a record | **neither when “protected-artifact” or “new … expected hash” is read to cover both containers** |
| `AGENTS.md:421`, never edit or replace an earlier admission record | `artifacts[]` |
| `AGENTS.md:422-427`, run both validation commands before a manifest proposal | both |
| `AGENTS.md:429-431`, one command rejects a broken chain and the other measures bytes/facts | `artifacts[]` for the chain; both for byte validation |
| `AGENTS.md:431-433`, the two existing v0.10/A2 records are retroactive | `artifacts[]` |

The generator is the pair of unqualified opening claims at
`ARCHITECTURE.md:67` and `AGENTS.md:417-421`: schema 2 gives chained
`admission` only to `artifacts[]`, while `pinned_files[]` rejects that key.

**G5 — priced paths to one two-origin production runtime.**

1. A documented operator sequence can change no repository or pinned byte:
   derive a temporary config from committed configuration, omit the arXiv
   fixture, set `max_pages: 1`, retain fixtureless SEC, run the net cored binary
   against a fresh archive, and select only both named sources. A successful
   bounded pass is exactly **4 publisher requests** — one robots and one content
   request to each origin — and changes **0 pins**.
2. Editing `config/core.json` to express that same construction also costs
   exactly **4 publisher requests** and changes **0 currently pinned files**, but
   it changes core-owned production configuration and is forbidden this cycle.
3. Generalizing the existing `harvest-arxiv` dispatcher while retaining its
   arXiv reachability preflight costs **5 publisher requests** on a successful
   bounded pass: the preflight plus the four shipped-gate requests. It changes
   the one hash-pinned `run` byte surface, so the current pin would fail and the
   path is forbidden.
4. A new bounded multi-origin `run` subcommand can avoid the preflight and cost
   exactly **4 publisher requests**, but it still changes that same one pinned
   `run` surface and is forbidden.
5. A direct two-connector observer can cost exactly **4 publisher requests** and
   change **0 pins**, but it omits the cored/store runtime and therefore does not
   answer Step 6. Deferral costs **0 requests**, changes **0 pins**, and leaves
   the condition unmeasured.

These counts assume the required non-error, no-redirect, no-retry bounded
observer; any construction unable to enforce those bounds is not a Step 6 path.

**G6 — duplicate-window execution.** The fresh-archive execution described in
G1 measured first ingest **200 fetched / 200 new / `ok:true`**, second ingest
**200 fetched / 0 new / `ok:true`**, and proved with a failure-capable trigger
that canonical reassignment did not run the second time.

**G7 — question reserved for R-CLOSE.** Does `ARCHITECTURE.md §8`'s phrase
“observable route, response body, schema, or other named surface” include the
core-internal loopback `/ingest` response body, making an added coverage field
a minor release? The text is not restricted to `/v1/*` and `/ingest` has a
named serialized body, which argues yes; its explicitly internal, non-public
role argues for distinguishing it from the public-value-domain rule. E0 records
the ambiguity and leaves the reusable criterion to Step 8.

**Artifacts, manifest, and published objects.** The manifest measured **165,488
bytes**. Two consecutive full `verify-artifacts` runs measured **0.21 s / 0.23
s real**; schema validation passed with two artifacts and **286 pinned files**,
and both databases and all pins matched. `evidence-report` measured
`data/core.db` at 1,764 documents / one cursor and `data/live-smoke.db` at 2,600
documents / one cursor, both integrity `ok`. Read-only local object
verification found annotated tag object
`ae593e882898b9c49d5e91e2d50b6ca1f02ac49b`, tagged closing commit
`397d100ae425d5d059cef8a8ddb2ac13cfde52f5`, and its sole parent release commit
`b9af84b8785bcd52c16ab0225d66386ecd872c4d`. Activation's read-only remote
verification found remote `main` and peeled `v0.16.1` at that same closing
commit and the same annotated tag object.

**Boundary.** E0 made no publisher request, created/moved/deleted no working-
repository ref, and left `STATE.md`, `config/core.json`, and
`config/schedule.json` byte-unchanged.

### WINDOW-MEASURE execution record — 2026-07-30

The committed
`derives_sec_latest_window_timing_from_pinned_body` test executes against the
point-of-use length- and SHA-asserted publisher body. It derives, rather than
uses as inputs, **200** timestamps, oldest
`Wed, 29 Jul 2026 16:13:52 EDT`, newest
`Wed, 29 Jul 2026 17:31:22 EDT`, a **4,650-second / 77.5-minute** span, 199
consecutive gaps, **11-second** median, **215-second** maximum, and hour
population `{16: 133, 17: 67}`. It derives the complete gap histogram, checks
that the gaps sum to the endpoint span, and confirms channel `lastBuildDate`
and `pubDate`. Focused replay passed **2/2**.

The general coverage criterion and its two named terms are recorded at
`observations/v0.27/sec-latest-window-margin.md`: for consecutive successful
polls over a stable fixed latest-N identity set, coverage holds if and only if
the **poll interval** is shorter than the **time the window takes to advance by
N items**. Against this one measured latest-200 span, the 600-second interval
has `4,650 / 600 = 7.75` observed headroom; equivalently, one interval consumes
**12.90%** of the span. This rests on one post-close window on one Wednesday
and establishes none of peak-season density, deadline-day density, or density
during hours neither live sample covered.

Both captures fell outside filing hours and kept identical body bytes, hash,
and `lastBuildDate`. The authored **7h28m** elapsed-time claim is refuted by
the committed timestamps: 03:34:00Z to 09:18:39.680936Z is
**5h44m39.680936s / 20,679.680936 seconds**, recorded in the dated runbook
amendment rather than blessed. The unchanged observable representation across
far more than ten minutes refutes the ten-minute rebuild claim as a description
of idle observable behavior, while simultaneously failing to test window
velocity because no filing arrived.

Warning-denied workspace tests passed **140**; warning-denied net tests passed
**31 ingest + 26 cored = 57**. Clippy and fmt passed. The SEC identity control
remained **200 kept / 0 dropped**, and standalone golden remained
byte-identical at **11/11**. No schedule or production source changed, the
scheduler did not run, and no publisher request occurred.

### CADENCE-CRITERION execution record — 2026-07-30

`ARCHITECTURE.md` now appends a new dated cadence-criterion row after the
byte-identical v0.26 row. The new row corrects the governing reason from the
publisher's ten-minute rebuild description to latest-window advance time and
records the unchanged 600-second interval against the measured 4,650-second
span: **7.75×** span/poll headroom, or **12.90%** of the observed span consumed
per interval. It names the one-Wednesday-window basis and the peak-season,
deadline-day, and uncovered-hour gaps. The measured positive margin does not
imply a number change, so none is recommended or applied.

The v0.25 terms row and the v0.26 cadence row have identical before/after
SHA-256 values. The new row expressly says the cadence correction satisfies
neither the terms condition nor the coverage-detection objective.

The new shell test resolves the SEC job through committed `load_schedule` and
`build_jobs`, extracts the cadence asserted by the new architecture row, and
compares them. Its planted 601-second architecture value raises the expected
`601 != scheduled 600` failure, proving the check is non-vacuous. Focused
scheduler tests passed **10/10** in both interpreters. Complete constrained
Python 3.11 and 3.12 lanes each collected and passed **292** with zero skips;
the comparator derived `collected=292`, `equivalent=true`, and
`equivalent_passed=292`.

Standalone golden remained **11/11**. `config/schedule.json` is byte-unchanged,
no scheduler ran, and no publisher request or production-source change
occurred.

### ADMISSION-LANGUAGE execution record — 2026-07-30

The two G4 claims that could be read as true of neither manifest container now
name schema v2's disjoint capabilities in both `AGENTS.md` and
`ARCHITECTURE.md`: `artifacts[]` requires the SQLite `expected` shape and
carries the chained `admission` record; `pinned_files[]` accepts immutable bytes
under `evidence/` or `observations/`, plus exact registered authorization paths,
with an applicable grade and forbids `admission`. The operating contract now
requires a pinning task to name its intended container and identifies a
requirement expressible by neither container as an author-side defect to record
and correct. The fifth and sixth v0.26 instances are motivating data only; their
historical dispositions remain closed.

The executing fixture validates both documented shapes in one disposable
manifest: one SQLite artifact and three pins covering an evidence path, an
observation path, and an exact authorization path. It then mutates the manifest
and proves both exact v0.26 failures:
`pinned_files[0]: keys differ; missing=[], extra=['admission']` and
`artifacts[0]: keys differ; missing=['expected'], extra=[]`. The stated
limitation is explicit: fixtures prove documentation/validator agreement today,
not against a future validator change; v0.27 forbids that change.

The focused fixture passed **1/1** under Python 3.11 and 3.12. Complete
constrained lanes each collected and passed **293** with zero skips; the
comparator derived `collected=293`, `equivalent=true`, and
`equivalent_passed=293`. `invariant-scan` passed unchanged at **12 rules / 44
controls**. Standalone golden remained **11/11**. The forbidden validator
remained SHA-256
`3e5e0c5ff6e12c25180833124faaaf91dc43b5171e893e83500e029d04e99af5`;
the forbidden manifest remained SHA-256
`8711aa1b95d6071c6492594aa20a3c4ab8a1756ffe4b5ed72b5208f39ed9a3da`.
No production source changed and no publisher request occurred.

### COVERAGE-DETECTION execution record — 2026-07-30

The operator authorized exactly **Option 1: overlap watermark, id-only** on
2026-07-30. Its claim is exact only under its two stated dependencies: each
incoming fixed window is a contiguous interval in publication order, and
document ids remain stable between polls. Under those conditions, any shared id
proves the old and new covered intervals abut, while an empty overlap against a
non-empty source is reported as a possible gap without measuring its size.

The committed replay derives the premises from the pinned body rather than from
the authorization message: **200 items**, **zero ascending inversions** in
document order, **200 unique GUIDs**, **200 distinct accession numbers**, every
GUID hosted at `www.sec.gov`, and every accession embedded in the corresponding
GUID. The RSS parser constructs each document id from source id plus GUID.
Accession immutability supports stable ids; stability across a future
publisher re-issue remains an explicit dependency that this one pinned body
cannot execute. The same replay derives **8 shared timestamp values**, seven
pairs and one triple, with maximum multiplicity three; this supports avoiding a
timestamp watermark whose boundary could land inside a tie.

The store owns the held-set query, and cored performs it for each successful
non-paged source **before** the one combined tail `append_new`. It passes
`sel.source.id()` and that source's `docs`, so a combined batch is never treated
as one window. The result is computed before commit and carried directly into
the matching `IngestSourceResult`, not left at a default or back-filled later.
The response and log distinguish `first_window`, `empty_window`, `overlap`, and
`gap_detected`; a detected gap carries the publisher's raw
`held_newest_published_raw` and `incoming_oldest_published_raw` strings.
Cursor-paged OAI-PMH is explicitly scoped out as `not_applicable_paged`, because
consecutive pages legitimately need not overlap.

The non-failing direction is a recorded decision: `gap_detected` remains
visible but the incoming window is committed and the poll succeeds, because
discarding it would compound possible loss. Empty overlap is conservative. A
publisher re-issue or GUID-form change can yield a false positive without data
loss; no zero-false-positive claim is made.

Execution proved all boundary cases. A fresh source ingesting the pinned
200-document window reported `first_window`; the identical second poll reported
`overlap` and **0 new**. A genuinely disjoint sequence stored 67 old documents,
omitted the intervening 66, and supplied 67 new documents. It reported
`gap_detected` with raw boundary pair
`Wed, 29 Jul 2026 16:26:17 EDT` /
`Wed, 29 Jul 2026 17:00:13 EDT`, then committed all 67 incoming documents.
Assessment after that insert returned `overlap`, proving the populated response
field was carried from the pre-insert check. A combined non-paged ingest
reported overlap for `techwire` and a gap for `osdaily`, proving per-source
partitioning. An empty store did not report a gap, and a cursor-paged fixture
reported `not_applicable_paged` while committing its cursor.

R12 now has **18 planted controls**, and the repository total is **12 rules /
46 controls**. Its two new mutations (1) insert before the overlap query and
(2) replace the per-source slice with the combined batch; both produced the
registered expected failure. Full `ci-local` passed **20/20** jobs with
warning-denied **145** workspace tests and **62** net tests (**32 ingest,
including three replay tests, + 30 cored**), locked Rust 1.78, clippy, fmt,
ShellCheck, and both constrained Python lanes at **293/293** with zero skips.
The first sandboxed Python 3.12 attempt lacked permission for loopback/process
checks and was a non-result; the same entry point passed with those local
permissions. The SEC identity fixture remained **200 kept / 0 dropped**,
standalone golden stayed byte-identical at **11/11**, and `crates/extract`,
`crates/view`, `config/schedule.json`, `config/core.json`, and
`config/protected-artifacts.json` are byte-unchanged.

The allowed production permissions for `crates/ingest/src/lib.rs` and
`crates/ingest/src/rss.rs` were unused. No compliance, extract, view, or shell
production source changed; no scheduler ran; no publisher request was made.

---

## Step 2 · WINDOW-MEASURE — Establish the margin that the cadence rests on 🤖

**Objective.** Turn G2's numbers into the recorded quantity a cadence decision can
be justified against.

**Gate.** `crates/**/tests/**`, `observations/v0.27/**`, and status records.
**Blocked on E0.** No production source, no `config/schedule.json`, no
`config/core.json`, no publisher request.

**Steps.**

1. Commit a test that derives, from the pinned body, the window's item count,
   first and last timestamps, span, and consecutive-gap distribution. **Derive
   them; do not assert a table of literals the pinned bytes already determine.**
2. **State the safety criterion explicitly and generally**: a fixed latest-N
   window is covered iff the poll interval is shorter than the time the window
   takes to advance by N items. Express the observed margin as a ratio and name
   both terms.
3. **State the criterion's evidentiary base honestly.** It rests on **one**
   77.5-minute post-close window on **one** Wednesday. Record what it does not
   establish: peak-season density, deadline-day density, and any density during
   the hours neither live sample covered.
4. **Record the idle-sample finding as a property.** Both live captures fell
   outside filing hours; the bodies were byte-identical; `lastBuildDate` was
   unchanged across 7h28m. **State that this refutes the ten-minute rebuild claim
   as a description of behaviour and simultaneously fails to test window
   velocity** — one observation, two conclusions, both stated.
5. Record the whole measurement under `observations/v0.27/`.

**Acceptance criteria.** Window quantities derived from pinned bytes by a
committed test rather than asserted · safety criterion stated generally with both
terms named and the observed ratio reported · evidentiary base and its three
named gaps recorded · idle-sample finding recorded with both conclusions · no
schedule change · no publisher request · golden 11/11.

**Done when** the cadence's safety margin is a number with a stated derivation
and a stated limit.

---

## Step 3 · CADENCE-CRITERION — Correct the reason, not the measurement 🤖

**Objective.** Replace the recorded justification for 600 seconds with the one
Step 2 measured.

**Gate.** `ARCHITECTURE.md`, `shell/tests/**`, and status records. **Blocked on
Step 2.** **`config/schedule.json` is not edited in this step.** No production
source, no publisher request.

**Steps.**

1. **Record the correction plainly.** v0.26's dated cadence row justifies 600
   seconds by the publisher's ten-minute rebuild claim. Step 2 measured that the
   governing quantity is window advance time, and that the rebuild claim does not
   describe observed behaviour. **The criterion is corrected; the number is not
   changed here.** Amend the dated row by appending a new dated row — the v0.26
   row is not rewritten.
2. **State the margin in the architecture record**: 600 seconds against a
   measured 77.5-minute window span, with the ratio and the three named
   evidentiary gaps.
3. **If Step 2's measurement implies the number should change, say so and stop.**
   Changing `config/schedule.json` is an operator decision and is not in this
   step's gate. Record the recommendation and leave the value alone.
4. Add a test that fails if the architecture record states a cadence the
   committed `config/schedule.json` does not declare, **or** record why such a
   test would be vacuous. **A vacuous test is worse than none.**
5. **Do not describe the corrected cadence criterion as satisfying the terms
   condition or the coverage objective.** Cadence, terms, and detection are three
   separate gates and this step advances one.

**Acceptance criteria.** Correction recorded as a new dated row with the v0.26
row byte-unchanged · margin and ratio stated with the three evidentiary gaps ·
any implied number change recommended and **not** applied · test added or vacuity
recorded · terms row unchanged · `config/schedule.json` byte-unchanged · golden
11/11.

**Done when** the recorded reason for the cadence is the reason a measurement
supports.

---

## Step 4 · COVERAGE-DETECTION — Make a lost filing visible 🧑🤖

**Objective.** Decide how the system detects that a fixed window rolled past
between polls, and implement exactly that.

**Gate.** 🧑 **One operator decision, at step 1.** Scope is
`crates/store/src/lib.rs`, `crates/store/src/sqlite.rs`,
`crates/ingest/src/lib.rs`, `crates/ingest/src/rss.rs`, and
`apps/cored/src/main.rs` **only as the decision requires them**, their tests,
`config/invariant-rules.json`, `tools/invariant_scan.py`, `ARCHITECTURE.md`, and
status records. **Blocked on Step 2.** No compliance, extract, view, or shell
source. No `config/core.json`. No schema-breaking change and no protected-database
change. **No publisher request: every option below is testable against the pinned
body.**

**Steps.**

1. **🧑 Choose exactly one, and record the claim each makes:**

   - **Overlap watermark, id-only.** On each ingest, if the incoming window shares
     **no** id with what is already stored for that source, and the store is
     non-empty for that source, coverage was lost; report it. **Claim:** for a
     window that is contiguous in publication order, a non-empty overlap is an
     *exact* proof of no gap — if any item is shared, the new window's oldest is
     no newer than something already held, so the covered intervals abut. **Cost:**
     the exactness rests on contiguity and id stability, which must be stated as
     the conditions it depends on, and it detects the gap without measuring its
     size. **Recommended**, because it is exact, needs no new date parsing, and
     uses only what the store already holds.
   - **Timestamp watermark.** Parse `published_raw` to a full instant, keep a
     per-source high-water instant, and compare the incoming window's oldest
     instant against it. **Claim:** detects the gap and measures it. **Cost:** a
     sub-day datetime parse does not exist today — `parse_rfc822ish` is
     day-granularity and ignores the zone — so this adds a new parser and a new
     failure mode on unparseable zones, on the ingest path, for a quantity the
     overlap check answers without it.
   - **Record and defer.** A complete outcome if neither can be justified from
     Step 2. **Cost:** the 600-second clock stays unrun and undetected loss stays
     undetectable. **State that as the consequence, not as a failure.**

   **Reducing the chance of loss without making loss visible is not on this list.**

2. If implementing: put the detection where the knowledge is. **The store knows
   what is held; the ingest result is where a caller can see it.** Surface a
   per-source coverage outcome on the existing `/ingest` response and in a log
   line. **Do not fail the poll on a detected gap** — losing a filing is bad and
   discarding the rest of the window is worse. Record that choice as a decision.
3. **Prove the detector fires and does not misfire, both by execution.** A gap
   case: two disjoint windows for one source in sequence must report loss. A
   no-gap case: the identical 200-document window ingested twice must report no
   loss and must remain distinguishable from G6's baseline. **A detector with no
   demonstrated firing is not a detector.**
4. **Prove identity behaviour did not move.** The 200-document SEC set stays
   **200 kept / 0 dropped**; golden stays byte-identical at 11/11 with its
   Hamming-12 collapse. **`crates/extract` and `crates/view` stay unmodified** —
   if the chosen option seems to need them, stop and record that instead.
5. Register any new rule as an R12 planted-failure mutation and report counts in
   three places. **If no rule is added, say so and report the unchanged 12 / 44.**
6. **Do not change `config/schedule.json` or `config/core.json` in this step.**

**Acceptance criteria.** Exactly one option chosen and dated with its claim and
its stated dependencies · detection sited with the non-failing choice recorded as
a decision · firing **and** non-misfiring both proven by execution against the
pinned window · SEC 200/0 and golden 11/11 both byte-identical with extract and
view unmodified · rules and controls reported in three places · schedule and core
config untouched · unused permissions named · **no publisher request**.

**Done when** the system says something a human can read when it loses a filing.

---

## Step 5 · ADMISSION-LANGUAGE — Fix the generator, not the sixth instance 🤖

**Objective.** Make it impossible to write a seventh unsatisfiable admission
clause, by stating what each manifest container can express and executing that
statement.

**Gate.** `AGENTS.md`, `ARCHITECTURE.md`, `shell/tests/**`, and status records.
**Blocked on E0 settling G4.** **`tools/evidence_artifacts.py` and
`config/protected-artifacts.json` are forbidden** — this step changes the
description, not the thing described. No production source, no publisher request.

**Steps.**

1. Replace every sentence G4 classified as true-of-neither with language naming
   the container it applies to. **State the two containers and their disjoint
   capabilities in one place**: `artifacts[]` carries the chained admission record
   and requires the SQLite `expected` shape; `pinned_files[]` accepts `evidence/`,
   `observations/`, and registered authorization paths with a grade, and **forbids
   `admission`**.
2. **Add the rule that would have caught both instances**, in the operating
   contract: a task that requires a byte to be pinned must name the container, and
   **a requirement that no container can express is an author-side defect to be
   recorded as such** rather than worked around.
3. **Make the documentation executable.** Add fixtures asserting that a candidate
   in each documented shape validates, and that each documented prohibition
   rejects — including the two exact failures v0.26 measured: `extra=['admission']`
   under `pinned_files`, and `missing=['expected']` under `artifacts`. **The
   documented capability table is a claim; these fixtures are what execute it.**
4. **State the limitation.** These fixtures prove the documentation matches the
   validator **today**. They do not prevent the validator changing away from the
   documentation later, and the contract's prohibition on editing
   `tools/evidence_artifacts.py` in this cycle is what keeps that honest here.
5. Record the fifth and sixth instances as the two data points that motivated the
   change, **without reopening either record**.

**Acceptance criteria.** Every true-of-neither sentence rewritten with its
container named · both containers and their disjoint capabilities stated in one
place · the naming rule added to the contract · fixtures execute both documented
shapes and both exact v0.26 rejections · limitation stated ·
`tools/evidence_artifacts.py` and `config/protected-artifacts.json`
byte-unchanged · prior records unreopened · golden 11/11.

**Done when** the contract cannot be read as promising an admission mechanism
that does not exist.

---

## Step 6 · MULTI-ORIGIN — The last unexercised condition, or a recorded refusal 🧑🤖

**Objective.** Decide whether both origins are exercised in one production runtime
this cycle, and if so, measure the cache and limiter across them.

**Gate.** 🧑 **One operator decision, at step 1, and it may be no.** Blocked on
Steps 2, 3, 4, and 5 complete. **This step may be deleted, in which case the
determination that deferred it is recorded in its place.** No protected database
is a target. No `config/core.json` change. No `run` change. No scheduler run.

**Steps.**

1. **🧑 Authorize or defer.** If deferring, delete this step and record the
   determination with the trigger unchanged. **A deferral here is a complete cycle
   outcome.**
2. If authorized: **re-evaluate both publishers' `robots.txt` fresh through the
   shipped gate** and compare each body's hash to the committed captures. Do not
   reuse a prior date's verdict to authorize a request today.
3. Execute one bounded ingest naming **both** sources into a fresh
   `data/live-<UTC-timestamp>-<pid>.db`. **Run `./run verify-artifacts` first and
   let the protected-target refusal stand.**
4. **Bound it exactly**: at most one robots request and one content request per
   origin, no re-request on a non-error response, no paging beyond one RSS
   response, no scheduler.
5. **Report per origin, in counts, from an observer that can see plaintext.** The
   v0.26 first attempt measured through a TLS-opaque relay and could not establish
   request counts; **use the observable construction v0.26's corrective phase
   established, and if plaintext is not observable, do not make the request.**
6. **Measure what only this configuration can show**: that the robots cache keyed
   each origin separately, and the **measured inter-request interval within each
   origin and across origins**. Per-host spacing that holds within one origin
   proves nothing about two, which is the whole point of this step.
7. **State what remains unexercised**, including T7, which two sequential origins
   still do not fire.
8. Do not admit the archive to the protected corpus or to golden.

**Acceptance criteria.** Decision recorded and dated · if deferred, step deleted
with its determination and unchanged trigger · if executed: fresh robots verdicts
through the shipped gate with hash comparisons, request counts per origin from a
plaintext-observable construction, per-origin and cross-origin intervals measured,
cache keying observed, archive fresh and unadmitted, non-exercise stated including
T7 · no protected artifact or database changed · golden 11/11.

**Done when** either both origins have run in one runtime and the record says what
the cache and limiter did, or the record says why they have not.

---

## Step 7 · RE-MEASURE — Hosted verification on a neutral branch 🤖

**Objective.** Prove the release-parent tree on hosted CI before any close.

**Gate.** Evidence paths and `config/protected-artifacts.json` **for admission
only**, plus status records. **Add the exact
`evidence/ci-runs/<run-id>-<attempt>/**` directory by a dated
`## Runbook amendments` entry in this same commit.** **No publisher request by any
hosted job.** 🧑 One narrow operator authorization for the neutral-branch push.

**Steps.**

1. Push the exact candidate to a neutral branch; do not push `main`, do not create
   a tag.
2. Record run id and attempt. Compare local and hosted shell populations with
   `tools/test_population.py` and **cite the comparator's derived output**; name
   every skip with node id, declared reason, and `on_site` marker.
3. **Register the receipt and bundle set as `pinned_files` with a `supporting`
   grade and no `admission` key**, verify every bundle against the exact receipt
   bytes, repository, workflow, candidate digest, source ref, and runner policy,
   and report the new pin count. **Do not require a chained admission record; that
   is the withdrawn sixth clause and Step 5 has just documented why.**
4. Generate the release-posture report and record its bytes, hash, grade, required
   attestations, accepted and rejected identities, and matrix completeness.
5. **Confirm no hosted job issued a publisher request**, and say how that was
   determined.

**Acceptance criteria.** Hosted run on a neutral branch with run id and attempt ·
comparator-derived populations cited, never transcribed · receipts and bundles
pinned as `supporting` with every bundle verified and the new pin count reported ·
release-posture report recorded with its counts · no publisher request by any
hosted job with the method stated · scope amendment dated in the same commit ·
golden 11/11.

---

## Step 8 · R-CLOSE 🧑🤖

**Objective.** Close the cycle under the tagged-close protocol.

**Gate.** Steps 1–7 complete and boxed, with Step 6 either complete or deleted
with its determination. Worktree clean. **🧑 One operator decision: publication.**

**Steps.**

1. **Follow the Option C tagged-close protocol as `AGENTS.md` states it.**
2. Re-run the complete definition of done at the release parent and capture it.
3. **Decide G7 explicitly and record the criterion.** State whether §8's "named
   surface" covers the core-internal `/ingest` body, and therefore whether adding
   a coverage field is a patch or a minor. **The v0.25 public value-domain
   criterion does not fire** — no `/v1/*` field gains, loses, or redefines a
   value. **Do not inherit a default silently, and record the G7 determination as
   a reusable criterion, not a one-off.**
4. Name the publication trigger, or record a no-release close as complete. **No
   corrective trigger is visible at entry**: published `v0.16.1` is green and its
   records are true.
5. Record evidence candidate and release parent as **separate named fields**, and
   the disposition **as of a date**.
6. **Record the coverage determination with its measurements** — the window span,
   the margin ratio, the option chosen, its stated dependencies, and the
   demonstrated firing and non-misfiring. If Step 4 deferred, record that as the
   result rather than as a shortfall.
7. **Record the cadence criterion correction** and that the number did not change,
   with the v0.26 row intact.
8. **Record the admission-language fix as addressing the generator of the fifth
   and sixth instances**, and that neither prior record was reopened.
9. **Record what did not happen**: no `edgar:*` mapping, no conditional GET, no
   `config/core.json` change, no scheduler run, no identity change — and, if Step
   6 deferred, no two-origin runtime.
10. Record whether each conditional production permission was used, and name each
    unused one.
11. Classify every diff path exactly once in `STATE.md`; update `CHANGELOG.md`,
    `README.md`, and the release authorities.
12. Reconcile `ARCHITECTURE.md`. **A4, editable L1, R3/R4, the measured-value
    heuristic, T7, NEGATIVE-CACHE Decision B, the FastAPI version-literal
    relocation, and terms-gate operator responsibility must all still read as open
    or unchanged**, and **T7 must not be described as nearer its trigger** even if
    Step 6 ran.
13. **State the cadence posture precisely**: the 600-second schedule has never
    run, and nothing in this cycle authorized it to.
14. Record the post-push hosted result as a **dated forward append**; a red
    post-push run is a finding for v0.28 and does not invalidate the close.

---

## Cycle checklist

- [x] **E0** — entering matrix with comparator citation; G1 answered by reading and
  execution with today's `/ingest` report stated; **G2's drafted numbers confirmed
  or refuted from pinned bytes**; G3's validator gap recorded with `get_text`'s
  headers quoted; **G4's true-of-neither sentences named**; G5's paths priced with
  request counts; G6 answered by execution; G7 stated as a question; pins and
  published objects re-verified; no publisher request
- [x] **WINDOW-MEASURE** — window quantities derived by a committed test, not
  asserted; safety criterion stated generally with its ratio; three evidentiary
  gaps recorded; idle-sample finding recorded with both conclusions
- [x] **CADENCE-CRITERION** — correction appended as a new dated row with v0.26's
  intact; margin stated; any implied number change recommended and not applied;
  test added or vacuity recorded; `config/schedule.json` byte-unchanged
- [x] **COVERAGE-DETECTION** — one option chosen with its claim and dependencies;
  detection sited; **firing and non-misfiring both demonstrated**; SEC 200/0 and
  golden 11/11 byte-identical with extract and view unmodified; counts in three
  places; unused permissions named
- [x] **ADMISSION-LANGUAGE** — true-of-neither sentences rewritten with containers
  named; capabilities stated in one place; naming rule added; **fixtures execute
  both documented shapes and both exact v0.26 rejections**; validator and manifest
  byte-unchanged
- [ ] **MULTI-ORIGIN** — authorized and measured from a plaintext-observable
  construction with per-origin and cross-origin intervals, or deleted with its
  determination
- [ ] **RE-MEASURE** — hosted run on a neutral branch; comparator cited; receipts
  pinned as `supporting` with **no `admission` key**; release-posture report
  recorded; no publisher request by any hosted job; scope amendment dated
- [ ] **R-CLOSE** — **G7 decided and recorded as a reusable criterion**; coverage
  determination with measurements; cadence correction with the number unchanged;
  admission-language generator fix recorded; non-exercise stated; permission usage
  recorded; cadence posture stated; T7 not described as nearer its trigger

---

## Standing prohibitions

- **Do not make any publisher request before Step 6, and do not make one at all if
  Step 6 is deferred. This includes a retrieval issued by any tool available to
  the agent, not only a request through the shipped stack** — a request the shipped
  gate never evaluated is a request whose compliance nothing measured. Every byte
  Steps 1–5 need is pinned or committed.
- **Do not cite the content quarantined in v0.26.** Cite the committed
  observations.
- **Do not reopen the identity guard.** `DEDUP_MIN_FEATURES` stays 26, both radius
  declarations stay 16, and `crates/extract/src/**` and `crates/view/src/**` stay
  unmodified. If Step 4 appears to need them, **stop and record that** instead.
- **Do not change `tools/evidence_artifacts.py` or `config/protected-artifacts.json`
  in Step 5.** Step 5 corrects the description; Step 7 admits bytes and nothing
  else.
- **Do not require a chained admission record for any non-SQLite byte.** That is
  the withdrawn sixth clause.
- **Do not run the scheduler, and do not treat any authorization in this file as
  authorizing the 600-second clock.**
- **Do not change `config/schedule.json`'s cadence value.** Step 3 corrects the
  recorded reason; changing the number is a separate operator decision.
- **Do not implement conditional GET in this cycle.** It is deferred with a
  trigger, and a 304 is not a coverage detector.
- **Do not map the `edgar:*` extension fields.**
- **Do not fail an ingest poll because a coverage gap was detected.**
- **Do not modify `crates/compliance/src/**` or `config/core.json`.**
- **Do not modify `run`.** It is hash-pinned.
- **Do not harvest into `data/core.db` or `data/live-smoke.db`**, and do not bypass
  the harness's protected-target refusal.
- **Do not admit a harvested database to the protected corpus or to golden.**
- **Do not describe T7 as nearer its trigger.** Two sequential origins are not two
  concurrent harvesters.
- **Do not create, move, or delete any ref in the working repository**; refs in a
  disposable clone are not repository refs.
- **Do not remove `--skip-local-tag-verification`.**
- **Do not add a rule without an R12 planted-failure control**, and do not add a
  rule that evaluates a condition it cannot observe.
- **Do not write a rule with no satisfying assignment for a case it governs** —
  this cycle exists partly because that happened twice.
- **Do not amend, rebase, or squash `e0d43ff…`.**
- **Do not batch `STATE.md` / `PROGRESS-v0.27.md` updates or combine two tasks in
  one commit.**
- If any Step's Objective, Acceptance criteria, or "Done when" is amended after
  this file is committed at activation, name the amendment in a dated
  `## Runbook amendments` block in the same commit.

---

## Provenance of this draft

Every gate was read out of the repomix export of the v0.16.1 tree on 2026-07-30
by path, and each is a hypothesis for E0 to confirm or refute.

**Four claims were verified against the export rather than reasoned to.**
`crates/ingest/src/rss.rs`'s module header names conditional-GET cursors as an
unimplemented production addition, and `crates/store` and `crates/ingest/src/net.rs`
carry the same note; `Cursors::high_water` exists and the OAI-PMH path consumes it
while the RSS path does not. `crates/ingest/src/net.rs`'s `get_text` sends a
User-Agent and `Accept` and no conditional header. The v0.26 corrective HARVEST
record names the absence of `Location` and `Retry-After` and is silent on `ETag`
and `Last-Modified`. And both live captures — 03:34:00Z and 09:18:39Z — returned
byte-identical 892,641-byte bodies at SHA-256 `154556cd…`.

**Step 2's predictions, stated so they can be refuted.** This draft's author
parsed the pinned observation body directly and measured: 200 items, all timezone
`EDT`; oldest `2026-07-29 16:13:52`, newest `2026-07-29 17:31:22`, span **77.5
minutes / 4,650 seconds**; median consecutive gap **11.0 s**, maximum **215.0 s**;
per-hour counts `{16: 133, 17: 67}`; channel `lastBuildDate` and `pubDate` both
`Wed, 29 Jul 2026 21:50:03 EDT`; channel `description` declaring *up to 200 of the
latest filings … updated every 10 minutes*. **That is a direct parse of pinned
bytes, not an execution of shipped code. Step 2 executes a committed test and
reports what it finds. If any number differs, the test is the measurement and this
paragraph is the error** — as happened in v0.26, where this author's news
feature-count range of "28–36" was refuted by a measured 26–42, and the floor was
set from the measurement rather than from the draft.

**Why this cycle is about the window and not the clock.** The v0.26 cadence
decision was careful, cited only committed bytes, and chose a defensible number.
It matched the number to the publisher's rebuild claim because that was the clause
the record had captured — and the clause that governs whether a filing is lost was
sitting in the same sentence, unused. **The failure mode worth naming is not
carelessness; it is that a well-documented decision can rest on the wrong half of
its own evidence.** The correction is cheap now and would be expensive after the
600-second clock had been running through a filing rush that nothing was watching.
