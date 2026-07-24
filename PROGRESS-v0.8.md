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

### 2026-07-23 · T4C — reproducible split-provider model configuration

- owner: 🤖 Codex
- measured: root `.env` and variants are ignored; committed `.env.example`
  contains no API-key-shaped secret. LAN/online chat profiles, an independent
  embedding role, and the legacy shared fallback all resolved under
  failure-capable tests. A proxy-sensitive fake proved loopback core clients set
  `trust_env=False` while remote clients retain it. `./run config` measured a
  bare harvest target of `data/live-smoke.db`; the ignored local file resolves
  the supplied LAN chat URL, keeps the DeepSeek chat URL ready, leaves both keys
  blank, and leaves embeddings unset. Explicit
  `CORE_DB=data/named-smoke.db` still won. Missing embedding configuration made
  `./run verify-llm` exit 2 cleanly without a traceback.
- acceptance: ignore/example secret checks ✅ · deliberately wrong legacy
  endpoint overridden by both chat profiles and the embedding role ✅ ·
  loopback proxy inheritance refused by a failure-capable test ✅ · legacy
  one-endpoint compatibility ✅ · `bash -n run` and safe/explicit harvest DB
  resolution ✅ · isolated verifier creates, ingests 13 fixtures, checks, and
  tears down ✅ · endpoint failures reported as measured failures, not
  tracebacks ✅ · warning-denied workspace/net checks, **90** workspace tests,
  **20** net tests, clippy, fmt, **77** shell tests, and locked Rust **1.78.0**
  check all passed ✅ · documentation/status/runbook updated ✅
- real-model gate: operator measurements were LAN embeddings HTTP **501** and
  DeepSeek embeddings HTTP **404**. The Codex LAN retry started an isolated
  fixture core and ingested 13 documents but received **No route to host**.
  Therefore embeddings did not populate and the real public HC1 check did not
  pass. **T4 remains deferred.** A deterministic mock passed **6/6 required
  verifier checks** with one latency diagnostic; that validates the harness
  only and was not substituted for real-model evidence.
- golden E2E: unchanged — final temporary DB
  `/private/tmp/intel-platform-t4c-final-golden.UCwRAP/golden.db`; initial
  fixture ingest 13; acme re-ingest +0; 12 analyzed; dropped
  `techwire::tw-004` for `osdaily::osd-004` at hamming 12; DeepSeek RISING
  z=10.0; second acme run +0; quant-desk exactly 1 document; ordinary
  `/v1/ask` answer with 4 citations, no retrieval notes, and
  `techwire::tw-004` suppressed. DB finished 14/0/0 with integrity `ok`; ports
  8788 and 8899 were clear.
- commit: this T4C implementation/status commit (see git history)
- notes / gate: before implementation, `data/core.db` had already changed from
  the T2 handoff hash after the operator's reported bare zero-document harvest.
  Direct measurement found its logical corpus unchanged at 1,764/0/0 and
  integrity `ok`, but SHA-256 now
  `db2f186e291c64192e567c9dfb979dd9877eb32b13c2ce2724a4acf1761a37a0`;
  size 6,729,728 bytes; mtime `2026-07-23 20:08:13 +0800`; cursor
  `arxiv-cs|NULL|2026-07-20|NULL|2026-07-23 12:08:13`. T4C made no further
  change to that file. No dependency, lockfile, sector, license, robots, or
  dedup invariant changed.

### 2026-07-23 · T4W — split-provider wire gate recorded

- owner: 🤖 Codex
- measured: operator run 1 used LAN chat plus DMXAPI embeddings on a fresh
  13-document fixture DB. DMXAPI returned HTTP 503 for backfill and fusion.
  The independent real LAN-chat/public-HC1 leg returned 4 citations, all 4
  `IndexOnly`, with no 16-token gated overlap. The verifier reported **3/5**,
  not a pass. Operator run 2 repeated the 503s, then stalled in chat until
  interrupted at 1m41s and printed a `KeyboardInterrupt` traceback. A fresh
  Codex one-vector probe independently reproduced HTTP 503 from the configured
  `/v1/embeddings` route.
- acceptance: configured embedding role re-probed on the wire and 503 recorded
  ✅ · partial 3/5 explicitly not promoted to T4 completion ✅ · interrupt
  classified as a verifier defect rather than endpoint evidence ✅ · protected
  archive unchanged ✅ · warning-denied offline/net checks, **90** workspace
  tests, **20** net tests, clippy, fmt, **77** shell tests, `bash -n run`, and
  locked Rust **1.78.0** check all passed ✅ · complete golden unchanged ✅
- gate: **T4 remains deferred.** Required real embedding backfill and hybrid
  fusion failed. The mock and BM25-only path were not substituted; the
  independently successful HC1 leg is retained as useful partial evidence only.
- golden E2E: exact on
  `/private/tmp/intel-platform-t4w-golden.5nqKKI/golden.db` — initial 13; acme
  +0 and 12 analyzed; dropped `techwire::tw-004` for `osdaily::osd-004` at
  hamming 12; DeepSeek z=10.0; second acme +0; quant-desk 1; public ask 4
  citations, no retrieval notes, `techwire::tw-004` suppressed; DB 14/0/0,
  integrity `ok`; ports 8788/8899 clear.
- commit: this T4W gate/status commit (see git history)
- notes: `data/core.db` remained 1,764/0/0, integrity `ok`, SHA-256
  `db2f186e291c64192e567c9dfb979dd9877eb32b13c2ce2724a4acf1761a37a0`.
  Documentation only; no runtime, dependency, lockfile, policy, or protected
  corpus change.

### 2026-07-23 · T4H — verifier fails fast with bounded provider waits

- owner: 🤖 Codex
- measured: pre-fix negative controls reported **6 failed, 7 passed**: timeout
  doubles saw 120s instead of role values, three invalid values were accepted,
  and the 503 embedding double reached a public-API constructor prepared to
  fail. After implementation the final targeted command passed **14/14**,
  including a controlled `KeyboardInterrupt` that exits 130 without a traceback.
  Role timeouts override a deliberately wrong shared timeout, the legacy shared
  fallback still configures both roles, and invalid/non-positive values fail.
- live negative control: DMXAPI returned HTTP **503** after 0.17s on a fresh
  13-document isolated core. The verifier stopped immediately with **0/1**,
  never called fusion or LAN chat, printed no traceback, and cleaned up. The
  wrapper completed in **2.4s**. T4 remains deferred.
- success control: isolated mock configuration with 5s role timeouts passed
  **6/6** — embeddings 13 missing → 0; clean retrieval notes; 5 hybrid docs;
  public ask 5 citations; 5 IndexOnly citation documents; no gated overlap.
  This proves the success path remains complete but is not real-model evidence.
- acceptance: failure-capable prerequisite guard ✅ · role/shared/invalid timeout
  guards ✅ · live 503 fail-fast/no-chat/no-traceback/teardown ✅ · deterministic
  full success path ✅ · warning-denied offline/net checks, **90** workspace
  tests, **20** net tests, clippy, fmt, **84** shell tests, `bash -n run`,
  Python bytecode compile, and locked Rust **1.78.0** check all passed ✅ ·
  `.env.example`, README, runbook, STATE, and progress updated ✅
- golden E2E: exact on
  `/private/tmp/intel-platform-t4h-final-golden.jF8Ser/golden.db` — initial 13; acme
  +0 and 12 analyzed; dropped `techwire::tw-004` for `osdaily::osd-004` at
  hamming 12; DeepSeek z=10.0; second acme +0; quant-desk 1; public ask 4
  citations, no retrieval notes, `techwire::tw-004` suppressed; DB 14/0/0,
  integrity `ok`; ports 8787/8788/8899 clear.
- commit: this T4H harness-hardening commit (see git history)
- notes: `data/core.db` remained 1,764/0/0, integrity `ok`, SHA-256
  `db2f186e291c64192e567c9dfb979dd9877eb32b13c2ce2724a4acf1761a37a0`.
  No dependency, lockfile, sector, license, robots, dedup, or protected-corpus
  invariant changed.

### 2026-07-24 · B0.1 — v0.8.1 entering state verified and registered

- owner: 🤖 Codex
- measured: `HEAD` is `6d42a75`; the only false entering claim was a clean
  worktree, because the operator-added `TASKS-v0.8.1-EXECUTION.md` was
  untracked. Warning-denied offline/net checks passed; **90** workspace tests,
  **20** net tests, and **84** shell tests passed (one existing Starlette
  deprecation warning); clippy, fmt, and the locked warning-denied Rust
  **1.78.0** check passed. Ports 8787/8788/8899 were clear.
- acceptance: every entering-state number confirmed or corrected in `STATE.md`
  ✅ · `data/core.db` measured at 1,764/0/0, integrity `ok`, 6,729,728 bytes,
  SHA-256 `db2f186e…1a37a0` ✅ · `data/live-smoke.db` measured at 2,600/0/0,
  integrity `ok`, 9,490,432 bytes, SHA-256 `94f03e9e…0462c4a` ✅ · both cursor
  rows, mtimes, and full hashes recorded ✅ · manual golden command sequence
  captured in full ✅
- golden E2E: unchanged on disposable DB
  `/private/tmp/intel-platform-b0.1-golden.L0tF8n/full-golden.db` — initial
  fetched/new 13/13; first and second acme re-ingests +0; 12 analyzed; dropped
  `techwire::tw-004` for `osdaily::osd-004` at hamming 12; DeepSeek RISING
  z=10.0 from 3 sources; quant-desk 1; public ask 4 citations with
  `techwire::tw-004` suppressed and clean notes; acme/quant `deepseek` search
  6/0, every IndexOnly snippet NULL; bad key 401; DB 14/0/0, integrity `ok`.
- commit: this B0.1 baseline/status commit (see git history)
- notes / gate: the clean-worktree correction was written to `STATE.md` before
  the remaining measurements. The first sandboxed local bind failed with
  `Operation not permitted` and was not counted; the permitted local-only run
  passed. Both protected DB hashes were unchanged afterward; no runtime,
  dependency, lockfile, policy, or corpus change was made.

### 2026-07-24 · G1 — golden E2E is one executable, blocking check

- owner: 🤖 Codex
- measured: `./run golden` owns a fresh temporary DB/output directory plus real
  core, mock-model, and public-API processes; the restored tree exited 0 with
  **11/11 named checks**. A temporary 20-word perturbation to the syndicated
  fixture moved it out of the duplicate threshold; the same command exited 1
  with **7/11**, explicitly failing the hamming-12 check and reporting the
  dependent 13-doc, z=12.0, and 5-citation drift. Restoring the fixture returned
  the command to 11/11.
- acceptance: one-command lifecycle and disposable writes ✅ · every
  `AGENTS.md §6` number asserted with named output ✅ · planted fixture drift
  exits non-zero and names the correct check ✅ · blocking push/PR CI job
  present with `continue-on-error: false` ✅ · `AGENTS.md §5.5/§6` updated to
  make the command authoritative ✅ · full matrix green: 90 workspace, 20 net,
  84 shell, warning-denied checks, clippy, fmt, `bash -n`, Python compile, and
  locked Rust 1.78 ✅ · both protected hashes unchanged ✅
- golden E2E: exact, **11/11** — initial 13/13; 12 analyzed; exact
  `techwire::tw-004` → `osdaily::osd-004` duplicate at hamming 12; DeepSeek
  RISING z=10.0 from 3 sources; second acme +0; quant 1; public ask 4 citations
  and `techwire::tw-004` suppressed; all IndexOnly snippets NULL; DeepSeek
  search 6/0; bad key 401.
- commit: this G1 harness/CI/status commit (see git history)
- notes / gate: the first implementation run failed before assertions because
  the background API lacked `PYTHONPATH=shell`; the pid-aware readiness check
  surfaced it immediately. A later hardening trial exported an empty
  `CORE_TOKEN`, which correctly made core requests return 401; the harness now
  unsets it. Both failures were repaired and not counted as passes. No
  dependency, lockfile, policy, or protected-corpus change.

### 2026-07-24 · P1 — live harvests cannot overwrite recorded evidence

- owner: 🤖 Codex
- measured: bare `./run config` resolved a fresh
  `data/live-20260724T064350Z-16718.db`; explicit
  `CORE_DB=data/named-smoke.db` still won. Protected-target controls for
  `data/core.db` and `./data/live-smoke.db` both exited 2 before egress, naming
  the full recorded hash and a safe exact override command.
- acceptance: fresh timestamp/PID default printed before the first request ✅ ·
  both protected paths and B0.1 hashes recorded in
  `config/protected-artifacts.sha256` ✅ · canonicalized protected paths refused
  legibly ✅ · `./run verify-artifacts` reports 2/2 match ✅ · planted scratch
  mismatch exits 1 and reports expected/actual hashes plus 0/1 ✅ · artifact
  verification runs first in `./run test` ✅ · README and `AGENTS.md §7`
  updated ✅ · both protected databases unchanged ✅ · full matrix green ✅
- golden E2E: unchanged, `./run golden` **11/11**.
- commit: this P1 protection/status commit (see git history)
- notes / gate: the mismatch control modified only a disposable copy under
  `/private/tmp`; neither protected file was deleted, renamed, or rewritten.
  Final hashes remained `db2f186e…1a37a0` and `94f03e9e…0462c4a`; no
  dependency, lockfile, source, license, robots, sector, or dedup change.

### 2026-07-24 · E1 — embedding model-key and dimension collision closed

- owner: 🤖 Codex
- measured: all three failure-capable controls failed before the fix. Store
  accepted a 1,024-dimensional vector after a 32-dimensional vector under
  `shared-model` (`Ok(1)`); `/retrieve` emitted no note for a planted
  32-versus-1,024 row/query mismatch; and the verifier reported a green
  zero-request backfill on a fresh pre-embedded database before reaching the
  later-stage failure double. After the fix, the upsert is rejected
  transactionally with model/existing/received dimensions, retrieval reports
  one ignored mismatched vector, and the verifier fails and stops when no real
  embedding request occurred.
- acceptance: one stored dimension per model key ✅ · structured mismatch names
  `shared-model`, 32, and 1,024 ✅ · `/retrieve` dimension note visible ✅ ·
  `/embeddings/stats` exposes count/dimension/inconsistency ✅ · reserved
  `mock-embed-32` key explicit in demo/golden ✅ · unnamed non-loopback provider
  exits 2 before services ✅ · fresh verifier requires ≥1 provider request,
  zero missing, and matching stored dimension ✅ · all three pre/post controls
  proven ✅ · HC3 intact ✅ · warning-denied checks, **92** workspace tests,
  **20** net tests, **85** shell tests, clippy, fmt, `bash -n`, Python compile,
  and locked Rust **1.78.0** check passed ✅
- success control: isolated deterministic mock passed **6/6** — 13 missing → 0,
  one request, provider/stored dimension 32, clean notes, five hybrid docs,
  five public citations, five IndexOnly citation documents, and no gated
  overlap. This validates the harness only; it is not real-model evidence.
- golden E2E: unchanged — `./run golden` **11/11**; the strict-dimension
  decision gate did not trip.
- commit: this E1 implementation/status commit (see git history)
- notes: `./run verify-artifacts` remained 2/2. Protected hashes stayed
  `db2f186e…1a37a0` and `94f03e9e…0462c4a`; port 8788 was clear. The first
  isolated success attempt encountered an ambient-proxy disconnect and was not
  counted; the corrected loopback run set `NO_PROXY`/`no_proxy` and passed. No
  dependency, lockfile, provider call from core, or policy/protected-corpus
  change.

### 2026-07-24 · T4L — local embedding server transport gate

- owner: 🤖 Codex + 🧑 operator launch input
- measured: the operator supplied separate chat (`:8080`, no embeddings flag)
  and dedicated embedding (`:8081`, `embeddinggemma-300M-Q8_0.gguf`,
  `--embeddings`) Docker commands. Live `POST :8080/v1/embeddings`,
  `GET :8081/v1/models`, `POST :8081/v1/embeddings`, and a bounded
  `GET :8081/health` retry all returned curl exit **7**, HTTP **000**, and
  `Couldn't connect to server`; no response body was received.
- gate: **T4L deferred.** The historical 501 body could not be confirmed or
  refuted, and no API-reported local model name or embedding dimension was
  measured. The local endpoint was not written into `.env`; redacted
  `./run config` still reports LAN chat plus the prior DMXAPI embedding role,
  whose 503 evidence remains in `STATE.md`. No mock or fifth provider was used.
- acceptance: exact transport failure recorded ✅ · supplied launch parameters
  distinguished from wire evidence ✅ · DMXAPI evidence preserved ✅ ·
  reachable local embedding endpoint/model/dimension ❌ · split local role in
  config ❌
- golden E2E: unchanged — `./run golden` **11/11**.
- verification: protected artifacts **2/2**; warning-denied offline/net checks,
  **92** workspace tests, **20** net tests, **85** shell tests, clippy, fmt, and
  locked warning-denied Rust **1.78.0** check passed. Protected hashes stayed
  `db2f186e…1a37a0` and `94f03e9e…0462c4a`; ports 8787/8788/8899 were clear.
- commit: this T4L gate/status commit (see git history)
- notes: documentation only. No dependency, lockfile, runtime, provider
  configuration, or protected-corpus change.

### 2026-07-24 · T4L retry — LAN path confirmed, service ports still closed

- owner: 🤖 Codex
- measured: local `en0` is `192.168.0.105/24`; ARP resolved LAN target
  `192.168.0.192` to `5c:b4:7e:cd:45:92`. Direct proxy-bypassed health/model
  requests to ports 8080 and 8081 still returned curl exit 7 / HTTP 000 /
  connection refused. ICMP reported `No route to host`.
- gate: unchanged. The LAN address and subnet are correct, but neither Docker
  published port accepted TCP. No 501 body, API model name, or vector dimension
  was measured, and no local provider configuration was written.
- regression: `./run golden` remained **11/11**; protected artifacts remained
  **2/2 MATCH**.
- commit: this T4L retry/status commit (see git history)

### 2026-07-24 · T4L completion — dedicated LAN embeddings measured

- owner: 🤖 Codex + 🧑 operator SSH-forward input
- measured: forwarded chat/embedding health and model-list endpoints all
  returned HTTP 200. Chat model is
  `gemma-4-26B-A4B-it-UD-IQ4_XS.gguf`; its embedding request returned the exact
  HTTP 501 body naming `--embeddings`. Dedicated model is
  `embeddinggemma-300M-Q8_0.gguf`; a real embedding request returned one
  index-0 vector of **768 dimensions**.
- configuration: ignored `.env` now names the reported models and direct LAN
  endpoints `:8080/v1` and `:8081/v1`; redacted `./run config` confirmed both.
  The 503 DMXAPI record was preserved.
- HC13: short single-item wire shape/index/dimension observed. Full bodies,
  13-item batch behavior, ordering/short responses, and load stalls remain
  untested until T4.
- acceptance: 501 diagnosis/body confirmed ✅ · dedicated endpoint reachable
  ✅ · API model name and measured dimension recorded ✅ · split roles explicit
  ✅ · DMXAPI evidence preserved ✅
- golden/verification: golden **11/11**, artifacts **2/2**, warning-denied
  offline/net checks, **92** workspace, **20** net, **88** shell, clippy, fmt,
  `bash -n`, and locked Rust **1.78.0** all passed.
- commit: this T4L completion/status commit (see git history)

### 2026-07-24 · T4P completion — real adversarial outcome measured

- owner: 🤖 Codex
- measured: real forwarded Gemma chat + EmbeddingGemma run ingested 13/13 and
  passed **6/6**. Embeddings completed 13 missing → 0 in one 13-full-body
  request, dimension/stats 768, latency 0.50s; retrieval notes were clean with
  five hybrid context documents.
- public HC1: ordinary answer returned four citations, all four IndexOnly, with
  no independent-oracle overlap. Adversarial outcome was **NOT EXERCISED** with
  `violations: []` and seven IndexOnly context documents. No real-model guard
  firing is claimed.
- HC13: no batch-size rejection, short response, context-window rejection, or
  stall observed. Silent truncation and raw pre-sort response ordering remain
  unobservable from this client response.
- acceptance: adversarial leg exercised against real model ✅ · three-state
  outcome and violations recorded ✅ · LEAK control remains proven ✅ ·
  result classified as non-pass/non-leak rather than promoted to guard firing ✅
- golden/verification: golden **11/11**, artifacts **2/2**, warning-denied
  offline/net checks, **92** workspace, **20** net, **88** shell, clippy, fmt,
  `bash -n`, and locked Rust **1.78.0** all passed.
- commit: this T4P completion/status commit (see git history)

### 2026-07-24 · T4 closure — one uninterrupted real-model run green

- owner: 🤖 Codex
- measured: separate fresh run passed **6/6** required checks. Models:
  `gemma-4-26B-A4B-it-UD-IQ4_XS.gguf` chat and
  `embeddinggemma-300M-Q8_0.gguf` embeddings, each 30s timeout. The SSH
  loopback aliases carried requests to the direct LAN roles recorded in
  `.env`.
- stages: 13/13 fixture ingest ✅ · one real embedding request, 13 missing → 0,
  dimension/stats 768, 0.16s ✅ · clean fusion and five context docs, 0.02s ✅ ·
  public ask 12.97s, four citations/all IndexOnly/no overlap ✅ · adversarial
  ask 6.00s, NOT EXERCISED, `violations: []`, never LEAK ✅
- acceptance: all required checks green in the same run ✅ · model names,
  dimension, and stage latencies recorded ✅ · no prior partial result carried
  forward ✅ · protected artifacts unchanged ✅
- golden/verification: golden **11/11**, artifacts **2/2**, warning-denied
  offline/net checks, **92** workspace, **20** net, **88** shell, clippy, fmt,
  `bash -n`, Python compile, and locked Rust **1.78.0** all passed.
- commit: this T4 closure implementation/status commit (see git history)
- notes: T4 is complete. The real model did not exercise the attestation guard;
  failure-capable GUARD FIRED and LEAK controls remain the structural evidence.

### 2026-07-24 · T4P — adversarial HC1 positive control implemented

- owner: 🤖 Codex
- measured: the public-path chat client is wrapped in-process so the verifier
  captures the exact raw answer sent to core `/attest`, then calls `/attest`
  directly with that answer and the same citation ids. It reports exactly
  `GUARD FIRED`, `NOT EXERCISED`, or `LEAK`, including violation document ids;
  the independent Python overlap oracle remains separate from core.
- failure-capable control: pre-implementation targeted collection failed
  because the classifier did not exist. Post-implementation, a canned real
  20-token IndexOnly span plus deliberately broken attestation reported
  **LEAK**, named `source::gated`, and made the verifier finish with exit 1.
  Companion controls proved `GUARD FIRED`/violation reporting and
  `NOT EXERCISED`.
- full-path controls: normal mock passed **6/6** and reported
  `NOT EXERCISED`; deliberately leaking mock passed **7/7**, public output was
  the constant refusal, and the adversarial leg reported **GUARD FIRED** with
  `violations: ['arxiv-cs::oai:arXiv.org:2607.01455']`. These are harness
  controls only.
- gate: **live T4P exercise deferred.** Fresh model-list probes to LAN ports
  8080 and 8081 both returned curl exit 7 / HTTP 000 / connection refused with
  no body. No real model received the adversarial prompt, so no real-model
  `GUARD FIRED` or `NOT EXERCISED` outcome is claimed.
- acceptance: adversarial public leg present ✅ · exact raw answer replayed to
  `/attest` with same context ids ✅ · three-state reporting and violations
  payload ✅ · independent oracle retained ✅ · LEAK control exits non-zero ✅ ·
  exercised against a real model ❌
- golden E2E: unchanged — `./run golden` **11/11**.
- verification: protected artifacts 2/2; warning-denied offline/net checks,
  **92** workspace tests, **20** net tests, **88** shell tests, clippy, fmt,
  `bash -n`, Python compile, and locked Rust **1.78.0** check passed. Protected
  hashes stayed `db2f186e…1a37a0` and `94f03e9e…0462c4a`; ports
  8787/8788/8899 were clear.
- commit: this T4P implementation/status commit (see git history)
- notes: no dependency, lockfile, core invariant, public response shape, or
  protected-corpus change.

### 2026-07-24 · T4 — uninterrupted closure run stopped at embedding gate

- owner: 🤖 Codex
- preflight: `./run down`; ports 8787/8788/8899 clear; protected artifacts
  2/2; redacted config resolved LAN chat `:8080`, model `default`, 30s, and
  DMXAPI embeddings, model `openAI`, 30s.
- measured: one uninterrupted isolated run ingested **13/13** fresh fixtures.
  DMXAPI `POST /v1/embeddings` returned HTTP **503 Service Unavailable** after
  **0.16s**. The verifier stopped immediately at **0/1 required checks** and
  exited 1; fusion, chat, public HC1, and the adversarial leg were not called.
- gate: **T4 deferred at embedding backfill.** No earlier partial success or
  mock evidence was carried into this run, and no retry/provider substitution
  was attempted. The client surfaced status/URL but not the provider response
  body; that requested evidence is absent and is not guessed.
- golden/verification: golden **11/11**; artifacts **2/2**; warning-denied
  offline/net checks; **92** workspace, **20** net, and **88** shell tests;
  clippy, fmt, `bash -n`, Python compile, and locked Rust **1.78.0** check all
  passed. Protected hashes remained exact.
- commit: this T4 gate/status commit (see git history)

### 2026-07-24 · R1 — v0.8.0 release identity made executable

- owner: 🤖 Codex
- decision: operator selected option **(b), cut v0.8.0**. Harvest durability,
  HC1 enforcement, and persisted fingerprint identity are material release
  changes, so leaving runtime artifacts at v0.7.4 would make deployed evidence
  ambiguous.
- implementation: Rust `cored`, Python `__version__`, FastAPI, and the STATE
  header now report 0.8.0; Cargo's lock entry records `cored` 0.8.0; a v0.8.0
  changelog records T1/T2/T3/T4/T5/T6 completion and T7's measured deferral.
  Dependency-free `./run version-check` parses all four sources, runs inside
  `./run test`, and is a blocking CI step.
- failure-capable control: planted Python `__version__ = "0.8.1"`;
  `./run version-check` exited 1 and named
  `shell/intel_shell/__init__.py: 0.8.1` as the disagreeing file. Restored to
  0.8.0 and the command passed.
- acceptance: release decision/rationale recorded ✅ · four version sources
  agree ✅ · version gate wired into test and CI ✅ · planted mismatch rejected
  with named file ✅ · changelog present ✅ · release tag target `v0.8.0` ✅
- golden E2E: unchanged — permitted loopback run passed **11/11**. An initial
  sandboxed invocation could not bind port 8788 and made no assertions.
- verification: protected artifacts **2/2** exact; warning-denied offline/net
  checks; **92** workspace, **20** net, and **88** shell tests; clippy, fmt,
  `bash -n`, Python compile; locked Rust **1.78.0** check/tests all passed.
- commit: this R1 release commit (see git history)

### 2026-07-24 · C1 — on-site Python floor and shell harness enforced in CI

- owner: 🤖 Codex
- implementation: the blocking shell job is now a Python **3.11/3.12** matrix.
  The 3.11 lane byte-compiles every Python file under `tools/` and `shell/`
  with `python3.11 -m py_compile` and runs `shellcheck ./run`. `AGENTS.md §4`
  records Python 3.11 as the supported floor; `run`'s help and header agree.
- failure-capable control: planted a same-quote PEP 701 f-string in
  `tools/version_check.py`. Python **3.12.13** accepted it; Python **3.11.4**
  exited 1 and named that file with `SyntaxError: f-string: unmatched '{'`.
  Removed the line and both complete trees compiled cleanly.
- shellcheck control: ShellCheck **0.11.0** initially exited 1 on unused poll
  counters, an ambiguous empty assignment, redundant same-command environment
  assignments, and the intentional daemon-subshell `CORE_CONFIG` scope.
  Replaced both polls with arithmetic counters, made the empty string explicit,
  removed the redundant assignments, and added only narrow, reasoned
  `SC2030`/`SC2031` disables. `shellcheck ./run` and `bash -n run` now pass.
- Python matrix: **88 tests passed** under both 3.11.4 and 3.12.13 with the
  existing Starlette warning. A preliminary local 3.12 command omitted
  `PYTHONPATH=shell` and failed collection; the CI-shaped rerun included it and
  is the measured pass.
- acceptance: both Python lanes green ✅ · 3.12-only construct rejected by the
  3.11 floor ✅ · complete floor byte-compile ✅ · shellcheck blocking and clean
  ✅ · Python floor recorded ✅
- golden/verification: golden unchanged at **11/11**; protected artifacts
  **2/2** exact; warning-denied offline/net checks, **92** workspace tests,
  **20** net tests, clippy, fmt, and locked Rust **1.78.0** check/tests passed.
- commit: this C1 implementation/status commit (see git history)

### 2026-07-24 · v0.9 — next execution runbook drafted

- owner: 🤖 Codex
- scope: added `TASKS-v0.9-EXECUTION.md` as an evidence-and-operations cycle
  with no new ingestion source or subscriber-facing product surface.
- order: fresh B0 baseline → executable evidence provenance → reproducible
  provider-wire probe → disposable `/view` cold/warm benchmark with
  predeclared SLO → deferred-trigger audit → explicit release close.
- gates preserved: T7 remains triggered only by a second concurrent harvester;
  Postgres by a second writer; pgvector by measured corpus/latency beyond
  SQLite's comfort; UDS/mTLS by an actual host split; `/view` materialization by
  measured warm-up crossing the defined SLO. Benchmark/audit tasks may promote
  future design work but may not implement around those gates.
- evidence discipline: every task has an objective, gate, measured acceptance
  criteria, failure-capable control, golden check, protected-artifact check,
  real-wire/fixture boundary, and one-task commit requirement. The v0.9 tasks
  are explicitly **not executed** by drafting them.
- acceptance: fresh B0 first ✅ · all five required deferred triggers explicit
  and unchanged ✅ · `/view` disposable-copy measurement/SLO task present ✅ ·
  provider, live-evidence, and release identity addressed before new surface ✅
- golden/verification: golden **11/11**; artifacts **2/2** exact;
  warning-denied offline/net checks; **92** workspace, **20** net, and **88**
  shell tests under Python 3.11.4 and 3.12.13; clippy, fmt, ShellCheck, floor
  byte-compilation, and locked Rust **1.78.0** check/tests passed.
- commit: this v0.9 runbook/status commit (see git history)

### 2026-07-24 · B0.2 — v0.8.2 entering state and archive integrity verified

- owner: 🤖 Codex
- measured: clean Cargo target; pinned Rust/Cargo 1.91.1; floor Rust/Cargo
  1.78.0; Python 3.11.4 and 3.12.13. Workspace tests **92**, net tests **20**,
  and shell tests **88** on each Python lane. Warning-denied offline/net checks,
  clippy, fmt, ShellCheck 0.11.0, Python byte-compilation, and locked Rust 1.78
  check/tests all exited 0.
- provenance: `HEAD=e212a7cdf269c171e1db4fb06002090a0939a95a`;
  `git describe --tags=v0.8.0-2-ge212a7c`; worktree contained only
  `?? TASKS-v0.8.2-EXECUTION.md`; `git remote -v` produced no output.
- census: read-only direct SQLite measured `data/core.db` as
  **1,764 documents / 0 NULL simhash / 0 NULL canonical_id / integrity ok** and
  `data/live-smoke.db` as
  **2,600 documents / 0 NULL simhash / 0 NULL canonical_id / integrity ok**.
  Post-census artifact verification remained **2/2 MATCH** at
  `db2f186e…1a37a0` and `94f03e9e…0462c4a`.
- acceptance: every entering claim re-measured ✅ · remote output captured
  verbatim (empty) ✅ · all archive census values captured ✅ · both integrity
  checks `ok` ✅ · both hashes exact after census ✅ · no false entering claim
  found ✅
- golden E2E: unchanged — permitted loopback run passed **11/11**. The first
  sandboxed attempt could not bind port 8788 and made no assertions.
- commit: this B0.2 baseline/status commit (see git history)
- notes / gate: gate clear. The system Python 3.12 lacked pytest; an isolated
  temporary 3.12 environment was created from `shell/requirements.txt`, and
  its actual 88-test pass is the result counted. `Cargo.lock` was untouched.

### 2026-07-24 · D0 — agent contract points at the active conformance cycle

- owner: 🤖 Codex
- measured: `AGENTS.md` now names `TASKS-v0.8.2-EXECUTION.md` as the current
  cycle, `TASKS-v0.9-EXECUTION.md` as the next cycle, and
  `PROGRESS-v0.8.md` as the intentionally contiguous correction trail.
- acceptance: no live instruction points at `TASKS-v0.8-EXECUTION.md` ✅ ·
  `rg "TASKS-v0\\.8-EXECUTION" AGENTS.md` returned no matches ✅ · line-by-line
  diff review found only pointer/continuity edits and no rule change ✅
- golden E2E: unchanged — **11/11**.
- verification: protected artifacts **2/2 MATCH**; `git diff --check` clean.
- commit: this D0 pointer commit (see git history)
- notes / gate: gate clear. No stale status claim or block rule was edited;
  those remain assigned to D1.

### 2026-07-24 · A1 — fingerprint verifier observes defects before repair

- owner: 🤖 Codex
- measured: pre-fix NULL-simhash control exited 0, backfilled the row, and left
  0 NULLs; a correct-fingerprint/NULL-canonical control also exited 0. After
  the fix, each control exited **1**, printed the offending
  `golden::fingerprint-control` id, and a direct read-only query still counted
  the planted NULL. A stale-body control exited **1** and named the same id.
  The clean deterministic fixture exited 0 with `null_fingerprints=0`,
  `null_canonical_ids=0`, and `fingerprint_mismatches=0`.
- implementation: raw `SQLITE_OPEN_READ_ONLY` queries run before
  `SqliteStore::open`; `./run verify-fingerprints <db> [reference-db]` added;
  `./run test` runs it immediately after artifact verification; core CI creates
  the same scratch fixture and executes the command.
- acceptance: planted NULL simhash rejected and named ✅ · NULL survived the
  run ✅ · planted NULL canonical id rejected and named ✅ · planted stale
  fingerprint rejected ✅ · clean fixture printed all three zero counts ✅ ·
  integrated `./run test` passed 92 workspace / 20 net / 88 shell tests ✅ ·
  `bash -n run` and ShellCheck passed ✅ · core CI step present ✅
- golden E2E: unchanged — **11/11**.
- verification: warning-denied offline/net checks, clippy, and fmt passed;
  protected artifacts **2/2 MATCH**; `Cargo.lock` untouched.
- commit: this A1 verifier commit (see git history)
- notes / gate: gate clear. The golden E2E database is process-owned and
  deleted on exit, so the core job uses the new deterministic one-document
  scratch fixture; no protected archive was opened through `SqliteStore`.

### 2026-07-24 · A2 — all persisted-fingerprint consumers fail closed

- owner: 🤖 Codex
- pre-fix controls: two unchanged store tests failed 0/2: `/view` load exposed
  only SQLite `Invalid column type Null`, and canonical assignment silently
  returned `Ok(0)`. A scratch live core measured `/view` 500 unnamed,
  `/retrieve` **200** with `golden::fingerprint-control`, and ingest/canonical
  assignment **200** while the row remained NULL/NULL.
- measured after: the same scratch core returned **500** at `/view`,
  `/retrieve`, and ingest-triggered canonical assignment. Every response named
  `golden::fingerprint-control` and `./run verify-fingerprints`; a direct query
  still measured `simhash IS NULL=1`, `canonical_id IS NULL=1`.
- implementation: added `missing_fingerprints()`; `/view` decodes nullable
  storage into a document-naming error; `/retrieve` deleted its recompute arm
  and refuses an absent fused id; canonical assignment dropped
  `WHERE simhash IS NOT NULL` and errors on the first missing value.
  `STATE.md §2.10` and the schema comment now describe the enforced behavior.
- acceptance: three sites changed and proven before/after ✅ · A1 controls
  rerun (clean pass; NULL simhash/canonical and stale-body all exit 1) ✅ ·
  `rg "simhash\\(" apps/cored/src/main.rs` returned no matches ✅ · full matrix
  **95 workspace / 20 net / 88 shell** ✅ · warning-denied checks, clippy, fmt,
  ShellCheck, and locked Rust 1.78 check/tests ✅ · protected hashes exact ✅
- golden E2E: unchanged — **11/11**, so the corpus-movement gate is clear.
- commit: this A2 invariant-closure commit (see git history)
- notes / gate: present archive risk remains low and measured: B0.2 found zero
  NULL fingerprints/canonical ids in both protected archives. This closes a
  structural defect without claiming an observed protected-corpus failure.

### 2026-07-24 · A3 — sector and id scoping moved into core SQL

- owner: 🤖 Codex
- implementation: `documents_in_sectors` applies bound sector predicates and
  returns persisted fingerprints; `documents_by_ids` binds every requested id.
  `/view`, `/retrieve`, `/attest`, and `/docs` now use those methods.
  `load_all` is documented for genuine whole-archive integrity/export/test
  consumers only.
- failure-capable controls: a finance row inserted beside technology rows was
  absent from the store's technology query and from `/view` ✅ · an id
  `quoted',finance-doc` returned exactly itself through `documents_by_ids`,
  proving binding rather than interpolation ✅ · empty sector/id lists returned
  empty results ✅
- measured performance: fresh disposable copies of the protected 2,600-row
  archive, same `POST /retrieve` request (`learning`, `science`, `k=8`):
  **0.039740s before** and **0.016264s after**. Both were HTTP 200 with
  fused/context/suppressed = **8/8/0**. The 2.44× ratio is one-shot wall-clock
  evidence, not a promoted SLO.
- acceptance: four handler call sites converted ✅ · sector predicate proven
  in store SQL ✅ · injection-shaped id safely bound ✅ · unentitled sector
  absent from `/view` ✅ · full matrix **97 workspace / 20 net / 88 shell** ✅ ·
  warning-denied checks, clippy, fmt, ShellCheck, and locked Rust 1.78
  check/tests ✅
- golden E2E: unchanged — **11/11**.
- verification: protected artifacts **2/2 MATCH**; `Cargo.lock` untouched.
- commit: this A3 SQL-scoping commit (see git history)
- notes / gate: output-preservation gate clear. The benchmark copies lived
  under `/private/tmp`; neither protected archive was opened through
  `SqliteStore` or modified.

### 2026-07-24 · A4 — accepted risk: a receipt cannot bind a shell-owned prompt

- owner: 🤖 Codex
- measured: source tracing found `/retrieve` returns context before the shell
  constructs the prompt, `/attest` receives only values the shell chooses, and
  the shell owns the public `/v1/ask` response. Under the proposed
  `{answer, receipt}` request, a valid receipt minted for retrieval B is
  indistinguishable from the intended receipt for retrieval A; no request
  field identifies which context actually entered the prompt. Omitting
  `/attest` altogether also leaves no event for the core to refuse.
- acceptance: prescribed different-retrieval negative control cannot be made
  failure-capable with the proposed seam ❌ · no misleading receipt mechanism
  shipped ✅ · accepted risk and exact trust boundary recorded in
  `STATE.md §2.1` ✅ · revisit trigger recorded ✅ · `ARCHITECTURE.md` corrected
  to stop claiming arbitrary shell rewrites are constrained ✅
- golden E2E: expected before execution and measured unchanged: **11/11**,
  including `/v1/ask` at **4 citations**.
- verification: protected artifacts **2/2 MATCH**; `git diff --check` clean;
  no runtime seam or `Cargo.lock` change.
- commit: this A4 gate-result commit (see git history)
- notes / gate: **gate tripped.** The shipped shell remains in the trusted
  computing base for answer attestation. Revisit before supporting an
  untrusted/third-party shell or restating rewrite-resistant HC1; the required
  design must make public egress traverse a non-bypassable core-owned
  attestation boundary without moving the model call into core (HC3).

### 2026-07-24 · A5 — `/view` cache bounded and keyed by configured sectors

- owner: 🤖 Codex
- pre-fix control: the new 300-configured-sector test failed at the 257th
  request with `view cache exceeded its declared bound`.
- implementation: introduced named `VIEW_CACHE_CAPACITY = 256`; `ViewCache`
  evicts oldest insertions first; `/view` intersects request sectors with
  `cfg.sectors`, sorts and de-duplicates them, and skips caching when none are
  configured.
- measured after: 300 distinct configured keys never exceeded **256** entries;
  the newest valid entry remained a hit without incrementing `view_computes`;
  **50** nonexistent-sector requests added **0** entries. Existing memoization,
  generation invalidation, and no-op-ingest cache tests passed.
- acceptance: bound enforced under test ✅ · unknown sector creates no entry
  ✅ · hit/miss and generation behavior unchanged ✅ · full matrix **98
  workspace / 20 net / 88 shell** ✅ · warning-denied checks, clippy, fmt,
  ShellCheck, and locked Rust 1.78 check/tests ✅
- golden E2E: unchanged — **11/11**.
- verification: protected artifacts **2/2 MATCH**; `git diff --check` clean;
  `Cargo.lock` untouched.
- commit: this A5 cache-bound commit (see git history)
- notes / gate: gate clear. Empty results for all-unknown sector requests are
  still returned, but never retained in the process-scoped cache.
