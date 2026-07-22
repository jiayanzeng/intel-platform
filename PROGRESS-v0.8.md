# PROGRESS-v0.8.md — execution log

Append-only. One block per task, written **immediately** on completion
(`AGENTS.md §5`). This is the audit trail: it records what was *measured*, so a
claim in `STATE.md` can always be traced to a run. Do not edit past entries;
correct them with a new dated entry.

**Block format:**

```
### <date> · <task id> — <one-line result>
- owner: 🤖 Codex | 🧑 human-assisted
- measured: <the numbers / outputs you captured>
- acceptance: <criterion> ✅/❌ … (all of them)
- golden E2E: unchanged | <the delta, if the task changed it>
- commit: <hash>
- notes / gate: <anything deferred, skipped, or found false>
```

---

### 2026-07-20 · T2 (partial) — live arXiv harvest reached the wire

- owner: 🧑 on-site run (pre-Codex), recorded here for continuity
- measured: `./run harvest-arxiv` against `oaipmh.arxiv.org/oai`; page 1 = 1,300
  docs, page 2 = 1,764 (last page); `{"fetched":1764,"new":1764, ok:true,
  error:null}`; `documents_analyzed: 1708` (56 near-dups suppressed, all 1,764
  stored). Build `cored --features net` clean in 8.79 s on Rust 1.91.1.
- acceptance: real OAI-PMH XML parsed, 0 errors ✅ · `resumptionToken` paging
  across > 1 page on the wire ✅ · interruption-resume ❌ (not yet tested — see
  Step 2 / T2 in the runbook) · 503 / Retry-After ❌ (not observed; arXiv issued
  none)
- golden E2E: not run this session
- commit: (pack `repomix` v1.16.1, 82 files) — no code commit; ops run
- notes / gate: **T2 is not complete.** "Reached the wire" is progress; resume
  behavior is the remaining gate. Two follow-ups to carry into the next runs:
  (1) this run wrote 1,764 live docs into `data/core.db` — isolate live runs with
  `CORE_DB=data/live-smoke.db` before the next harvest so the 12-doc golden corpus
  stays clean; (2) the clippy dump from this session shows `items_after_test_module`
  still firing in `sqlite.rs`, contradicting `STATE.md`'s "fixed" claim (handled
  in Step 4 / T6).

---

<!-- Codex appends below, one block per completed step, newest at the bottom. -->

### 2026-07-20 · B0 — entering state verified and corrected

- owner: 🤖 Codex
- measured: clean Rust 1.91.1 baseline: workspace check 0 rustc warnings;
  workspace tests 80 passed; net cored check 0 rustc warnings; net ingest tests
  17 passed; shell tests 69 passed with 1 Starlette deprecation warning. Clippy
  exits 101 on one `items_after_test_module` diagnostic in `sqlite.rs`; with
  only that lint allowed, the remainder is clean. Fmt check exits 1 with diffs
  in 13 Rust files.
- acceptance: Rust/shell counts captured ✅ · 0 rustc warnings on offline and
  net configs ✅ · golden result captured and unchanged ✅ · clippy inventory
  captured, including the two accepted `unnecessary_map_or` allows ✅ · golden
  vs live DB paths answered and isolated ✅
- golden E2E: unchanged — fixture ingest 13; acme 13 → 12; dropped
  `techwire::tw-004` for `osdaily::osd-004` at hamming 12; DeepSeek RISING
  z=10.0; re-ingest +0; quant 1; `/v1/ask` 4 citations with
  `techwire::tw-004` suppressed.
- commit: this B0 baseline-verification commit (see git history)
- notes / gate: corrected `STATE.md`'s false claim that the test module had
  already been moved last; recorded the newly measured fmt failure and that CI
  is report-only rather than commented out (the ordered T6 step owns the stale
  wording in `TASKS-v0.8.md`). Golden ran on a temporary fixture DB;
  `data/core.db` remained 1,764 documents and byte-size/mtime unchanged. Port
  8788 is held by foreign PID 59269; operator command `kill 59269` is required
  before T2.

### 2026-07-20 · T2 — BLOCKED: capped live run clears its resume token

- owner: 🤖 Codex
- measured: after a clear-port/fresh-DB preflight,
  `HARVEST_MAX_PAGES=1 CORE_DB=data/live-smoke.db ./run harvest-arxiv` fetched
  and parsed 1,300 real page-1 records (`ok=true`, `error=null`), logged that
  more pages follow, and stopped at cap 1. The persisted row was
  `arxiv-cs | cursor=NULL | high_water='2026-07-20'`. Code inspection confirmed
  the capped break is followed by unconditional `complete()`, which clears the
  checkpoint and advances high-water. The existing fake test observes the
  intermediate checkpoint call but never checks final resume state.
- acceptance: run 1 non-NULL cursor ❌ (`NULL`) · run 2 resumes from token ❌
  (not run; no token exists, so a second run would test the prohibited
  high-water path) · real XML parse errors on run 1: 0 ✅, but the required
  two-run criterion remains incomplete · `data/core.db` untouched ✅ · 503 /
  Retry-After explicitly not observed ✅
- golden E2E: unchanged — acme 13 → 12; dropped `techwire::tw-004` for
  `osdaily::osd-004` at hamming 12; DeepSeek RISING z=10.0; re-ingest +0;
  quant 1; `/v1/ask` 4 citations with `techwire::tw-004` suppressed.
- commit: this T2 gate-result commit (see git history)
- notes / gate: **T2 is not complete.** The decision gate tripped at the first
  cursor assertion. No workaround and no misleading second run were attempted.
  Repair requires distinguishing capped exit from exhausted completion and a
  test that asserts final persisted resume state; that repair is outside this
  verification step and was not implemented here.

### 2026-07-20 · H1 — live harvest evidence now reflects actual outcomes

- owner: 🤖 Codex
- measured: positive live run against a fresh `data/live-smoke.db` fetched
  1,764 documents over two pages (1,300 then 1,764) with 0 parse errors. The
  robots section showed only real decisions:
  `https://oaipmh.arxiv.org -> Unavailable(allow)`, allowed=true, effective
  crawl-delay 0.500s. All four derived checklist boxes were checked. A
  controlled real zero-document run (`fetched=0, new=0, ok=true`) reported NOT
  VERIFIED and left all four boxes unchecked.
- acceptance: capped/live robots section shows a real disposition, not page
  output ✅ · positive checklist matches documents/pages/parse/cursor evidence
  ✅ · zero-document checklist is fully unchecked ✅ · workspace 80, net 17,
  shell 69 tests green and both rustc-warning checks clean ✅
- golden E2E: unchanged — acme 13 → 12; dropped `techwire::tw-004` for
  `osdaily::osd-004` at hamming 12; DeepSeek RISING z=10.0; re-ingest +0;
  quant 1; `/v1/ask` 4 citations with `techwire::tw-004` suppressed.
- commit: this H1 harness-evidence commit (see git history)
- notes / gate: logging/checklist only; no fetch, robots, cursor, or corpus
  outcome changed. `data/core.db` hash/size/mtime/count remained exact. T2's
  capped-run cursor bug remains blocked and was not worked around.

### 2026-07-20 · T6 — clippy and fmt are clean and blocking

- owner: 🤖 Codex
- measured: lint-fix commit `097b017` moved the SQLite vector layer before the
  test module and applied rustfmt to the 13-file B0 inventory. Clippy exits 0
  under `-D warnings`; fmt check exits 0. Workspace check/test: 0 rustc warnings
  and 80 passed. Net check/test: 0 rustc warnings and 17 passed. Shell: 69
  passed with the existing 1 Starlette deprecation warning. CI now sets the
  lint job's `continue-on-error: false`.
- acceptance: `items_after_test_module` eliminated and clippy clean ✅ · two
  MSRV-preserving `unnecessary_map_or` allows retained ✅ · fmt clean ✅ · lint
  job blocking ✅ · fix and gate split into two commits ✅ · full tests green ✅
  · stale STATE/TASKS claims corrected ✅
- golden E2E: unchanged — fresh temporary fixture DB; acme 13 → 12; dropped
  `techwire::tw-004` for `osdaily::osd-004` at hamming 12; DeepSeek RISING
  z=10.0; re-ingest +0; quant 1; `/v1/ask` 4 citations with
  `techwire::tw-004` suppressed. `data/core.db` retained its exact count,
  hash, size, and mtime.
- commit: lint fix `097b017`; this separate T6 gate/status commit (see git
  history)
- notes / gate: no MSRV increase and no behavior change. The decision gate did
  not trip; both commands were green before CI was made blocking.

### 2026-07-20 · T1 — HC1 is structurally enforced on `/v1/ask`

- owner: 🤖 Codex
- measured: real-corpus n-sweep covered 1,764 live IndexOnly documents, 17,640
  single-doc clean trials, 4,851 four-doc clean trials, and 1,763 substantive
  seeded sentence leaks. `n=15` had 1/4,851 operational false positives;
  **`n=16` had 0/4,851 false positives and 1,763/1,763 true positives**;
  `n=17` fell to 1,762/1,763 true positives. Selected 16. Full curve is in
  `STATE.md §8`.
- acceptance: IndexOnly sentence refused in core ✅ · CcBy sentence allowed ✅ ·
  analytical answer byte-preserved ✅ · leaking mock first proven to contain
  gated text, then absent from public `/v1/ask` response ✅ · real Rust/HTTP
  leaking-model E2E returned the constant refusal ✅ · n-sweep recorded ✅ ·
  workspace 84, net 17, shell 70 tests green; clippy/fmt and both
  warning-denied checks clean ✅
- golden E2E: ordinary output unchanged — fresh fixture DB; acme 13 → 12;
  dropped `techwire::tw-004` for `osdaily::osd-004` at hamming 12; DeepSeek
  RISING z=10.0; re-ingest +0; quant 1; `/v1/ask` kept the ordinary mock answer,
  4 citations, and `techwire::tw-004` suppression. `data/core.db` retained its
  exact count, hash, size, and mtime.
- commit: this T1 HC1-attestation commit (see git history)
- notes / gate: the gate held only at `n=16`; the anticipated 8 was rejected
  because its four-document clean FPR measured 1.0513%. One punctuation-less
  record lacked an eligible complete sentence in the visible 800 characters
  and is explicitly identified in STATE. No dependency or MSRV change.

### 2026-07-20 · T5 — every redirect is re-gated before the next request

- owner: 🤖 Codex
- measured: cross-origin fake returned first/start → 302 second/blocked; robots
  calls were first/robots.txt and second/robots.txt, while page calls contained
  only first/start because second's `Disallow` stopped the request. Same-origin
  start → final made 2 page calls and exactly 1 robots fetch. Fixture negative
  control remained 0 robots fetches. Both reqwest clients set `Policy::none()`.
- acceptance: cross-origin policy fetched and honored before body request ✅ ·
  same-origin redirect reused cached policy ✅ · fixture issued zero fetches ✅ ·
  both clients disable automatic redirects ✅ · workspace 84, net 19, shell 70
  tests green; warning-denied checks, clippy, and fmt clean ✅
- golden E2E: unchanged — fresh fixture DB; acme 13 → 12; dropped
  `techwire::tw-004` for `osdaily::osd-004` at hamming 12; DeepSeek RISING
  z=10.0; re-ingest +0; quant 1; ordinary `/v1/ask` answer, 4 citations, and
  `techwire::tw-004` suppression unchanged. `data/core.db` retained exact count,
  hash, size, and mtime.
- commit: this T5 redirect-regating commit (see git history)
- notes / gate: Design 1 selected; no request is made to a redirected origin
  before its gate. The first full workspace run failed on a pre-existing
  timestamp-only `intel-store` temp-DB collision (3 rows vs 2); the exact test
  passed alone, and a test-only pid + atomic-sequence filename fix made the full
  matrix pass. The failure and fix are recorded in STATE; no production store
  behavior changed.

### 2026-07-20 · T3 — persisted fingerprints consumed without output drift

- owner: 🤖 Codex
- measured: corrected the false runbook premise: `data/core.db` already had a
  populated `simhash` column (**1,764 rows, 0 NULL fingerprints, 0 NULL canonical
  ids**). On a disposable copy with that column removed, store open restored it
  and produced **1,764/1,764** stored fingerprints with **0 fresh-compute
  mismatches** and **0 canonical-id mismatches** against the original. Direct
  verification of the original also found 0 fingerprint mismatches.
- acceptance: stored fingerprint equals fresh compute ✅ · pre-column migration
  backfills the same 1,764 rows ✅ · dedup consumes the persisted value, proven
  by a deliberately violating double ✅ · document edits refresh the value ✅ ·
  workspace 86, net 19, shell 70 tests green; warning-denied checks, clippy, and
  fmt clean ✅
- golden E2E: byte-identical — fresh fixture DB; acme 13 → 12; dropped
  `techwire::tw-004` for `osdaily::osd-004` at hamming 12; DeepSeek RISING
  z=10.0; re-ingest +0; quant 1; ordinary `/v1/ask` answer, 4 citations, and
  `techwire::tw-004` suppression unchanged. `data/core.db` retained exact count,
  hash, size, and mtime.
- commit: this T3 persistence/migration commit (see git history)
- notes / gate: the output gate did not trip. The first verifier compile failed
  on an iterator lifetime and was fixed; the first migration test then exposed
  an FTS update-trigger interaction and failed with `database disk image is
  malformed`. It was not counted as a pass. The backfill now suspends/recreates
  that trigger transactionally. No dependency, lockfile, MSRV, or policy change.

### 2026-07-20 · T4 — DEFERRED: no real-model credentials/configuration

- owner: 🤖 Codex
- measured: `LLM_BASE_URL` absent; `LLM_API_KEY` absent; no repository-local key
  assignment; no listeners on 8000/8899/11434. Contrary to v0.7's egress note,
  DeepSeek and OpenAI `/v1/models` are both reachable now and return 401 without
  credentials. `./run verify-llm` exited 2 asking for endpoint configuration.
- acceptance: `verify_llm.py` green against a real endpoint ❌ (not run; no
  configured endpoint/key) · live-model HC1 spot-check ❌ (not run for the same
  gate) · mock substituted ❌ (deliberately not used as T4 evidence)
- golden E2E: unchanged — fresh fixture DB; acme 13 → 12; dropped
  `techwire::tw-004` for `osdaily::osd-004` at hamming 12; DeepSeek RISING
  z=10.0; re-ingest +0; quant 1; ordinary `/v1/ask` answer, 4 citations, and
  `techwire::tw-004` suppression unchanged. `data/core.db` retained exact count,
  hash, size, and mtime.
- commit: this T4 gate/deferral record (see git history)
- notes / gate: **T4 is deferred, not complete against a model.** Public egress
  is no longer the blocker; usable endpoint configuration and credentials are.
  No code, dependency, lockfile, or runtime policy changed.

### 2026-07-20 · T7 — DEFERRED: single-writer trigger has not fired

- owner: 🤖 Codex
- measured: scheduler dry-run produced five configured jobs, while inspection
  confirmed `Scheduler.tick` calls them synchronously in one loop and the shipped
  service is one `Type=oneshot` `scheduler --once` process. Scheduler tests passed
  8/8; `lsof data/core.db` found no active holder. `pgrep` process enumeration
  failed with missing sysmond (exit 3) and was not counted as evidence.
- acceptance: recorded decision that the concurrency trigger has not fired ✅ ·
  single-flight implementation not added ✅ (required by the one-writer gate)
- golden E2E: unchanged — fresh fixture DB; acme 13 → 12; dropped
  `techwire::tw-004` for `osdaily::osd-004` at hamming 12; DeepSeek RISING
  z=10.0; re-ingest +0; quant 1; ordinary `/v1/ask` answer, 4 citations, and
  `techwire::tw-004` suppression unchanged. `data/core.db` retained exact count,
  hash, size, and mtime.
- commit: this T7 gate/deferral record (see git history)
- notes / gate: **T7 is intentionally deferred.** There is no second concurrent
  harvester, so adding a lock would route around the task's decision gate. No
  code, dependency, lockfile, or runtime policy changed.

### 2026-07-22 · T2 corrective attempt — durable locally, BLOCKED on live run 1

- owner: 🤖 Codex
- measured: the strengthened pre-fix fake failed with checkpoint history
  `oai_page2.xml` but actual resume state `None`. After the repair, an injected
  fake commit failure left cursor state unchanged; an SQLite trigger aborting
  the cursor write rolled the page insert back to 0 documents / 0 cursor rows;
  close + reopen retained the page-2 token and `pending_high_water`, then final
  completion promoted the max across both pages. Workspace **90**, net ingest
  **20**, shell **70** tests passed; both `-D warnings` checks, clippy, and fmt
  passed; locked Rust **1.78.0** offline check passed with `-D warnings`.
- acceptance: cap leaves durable token locally ✅ · second fixture run starts at
  page 2 and not page 1 ✅ · documents + cursor transaction rollback proven ✅ ·
  pending high-water survives process restart ✅ · legacy cursor schema
  migration proven ✅ · live run 1 non-NULL token ❌ (first `ListRecords`
  request timed out before a page; no cursor row) · live run 2 begins from token
  ❌ (correctly not run) · real XML across both runs ❌ · protected
  `data/core.db` untouched ✅ · 503/Retry-After recorded as not observed ✅
- golden E2E: unchanged — fresh fixture DB; initial ingest 13; acme re-ingest
  +0; 12 analyzed; dropped `techwire::tw-004` for `osdaily::osd-004` at hamming
  12; DeepSeek RISING z=10.0; quant 1; ordinary `/v1/ask` answer with 4
  citations and `techwire::tw-004` suppressed. Temporary DB ended at 14 rows
  with 0 NULL fingerprints/canonical ids; `data/core.db` retained 1,764 rows and
  SHA-256 `ddb2c7fb81038b670104fb8d619e7cd15a021f3e9028ba6be59f0604fafc8f3a`.
- commit: this T2 durability/gate-record commit (see git history)
- notes / gate: privileged arXiv Identify returned 200 and the real robots
  verdict was `Unavailable(allow)` with 0.500s effective delay. The first
  `ListRecords` request for 2026-07-19 through 2026-07-22 timed out:
  `fetched=0`, `new=0`, `ok=false`; all HC13 boxes were unchecked. The prior
  disposable smoke DB is recoverable at
  `/private/tmp/intel-platform-live-smoke-before-t2r-20260722.db`. The complete
  golden required `NO_PROXY/no_proxy=127.0.0.1,localhost` because macOS system
  proxy discovery routed Python loopback through `httpcore._sync.http_proxy`;
  direct curl and two fixture ingests proved cored stayed healthy. **T2 remains
  unchecked and blocked; this is not a wire pass.**

### 2026-07-23 · T2 — interruption-resume proven on the live wire

- owner: 🤖 Codex
- measured: clean preflight at `2b036d9`; `./run down` succeeded and port 8788
  was clear. The zero-row 2026-07-22 timeout DB was preserved, then run 1 used a
  fresh `data/live-smoke.db` and command `HARVEST_MAX_PAGES=1
  CORE_DB=data/live-smoke.db ./run harvest-arxiv`. The sandboxed HTTP `000000`
  probe was not counted. With network permission, Identify returned 200; run 1
  fetched/added **1,300**, reported `ok=true`, and durably stored token
  `verb%3DListRecords%26metadataPrefix%3Doai_dc%26from%3D2026-07-21%26until%3D2026-07-22%26set%3Dcs%26skip%3D522`
  with `pending_high_water=2026-07-21`. After stopping `cored` and independently
  confirming the port clear, the identical run 2 began with that exact token,
  fetched/added the next **1,300**, reached 2,600 stored / 2,487 analyzed, and
  advanced the token to `from%3D2026-07-22...skip%3D88` with
  `pending_high_water=2026-07-22`.
- acceptance: run 1 non-NULL cursor ✅ · run 2's first request used that exact
  cursor and did not restart fresh page 1 ✅ · two real OAI-PMH pages parsed
  with no observed error and both results `ok=true` ✅ · real robots verdict
  `Unavailable(allow)` with 0.500s effective delay captured on both runs ✅ ·
  503/Retry-After explicitly **not observed** ✅ · protected `data/core.db`
  remained 1,764 rows and byte-identical ✅ · workspace **90**, net ingest
  **20**, and shell **70** tests passed; both warning-denied checks, clippy, fmt,
  and locked Rust **1.78.0** offline check passed ✅
- golden E2E: unchanged — fresh temporary fixture DB; initial ingest 13; acme
  re-ingest +0; 12 analyzed; dropped `techwire::tw-004` for
  `osdaily::osd-004` at hamming 12; DeepSeek RISING z=10.0; quant-desk 1;
  ordinary `/v1/ask` answer with 4 citations, no retrieval degradation notes,
  and `techwire::tw-004` suppressed. Temporary DB ended at 14 rows with 0 NULL
  fingerprints/canonical ids. `data/core.db` retained SHA-256
  `ddb2c7fb81038b670104fb8d619e7cd15a021f3e9028ba6be59f0604fafc8f3a`.
- commit: atomic implementation `2b036d9`; this T2 closure/status commit (see
  git history)
- notes / gate: T2 is complete. Run-1 evidence is preserved under
  `/private/tmp/intel-platform-t2-run1-20260723-*`; run-2 evidence under
  `/private/tmp/intel-platform-t2-run2-20260723-*`; the golden DB under
  `/private/tmp/intel-platform-t2-golden.gyEOy7/`. No 503 was forced, no
  production policy was weakened, and no code or dependency changed in the
  closure commit.
