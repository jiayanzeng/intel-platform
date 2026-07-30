# PROGRESS-v0.26.md — append-only execution record

This file records v0.26 task and gate events after their implementation
commits exist. Each entry names the measured result, every applicable
acceptance criterion, the golden delta, and the real implementation commit.
Entries are append-only; corrections are new dated entries.

### 2026-07-30 · ACTIVATE — v0.26 admitted with its supplied scope table

- owner: Codex
- commit: a90d080e1da18e8f16549b53c542b54259d74920
- result: PASS. The supplied runbook's declared scope parsed in its original
  executable Markdown-table dialect after the activation anchor existed; no
  translation or scope correction was required.
- worktree acceptance: PASS. Before activation the only worktree item was the
  operator-supplied untracked
  `docs/cycles/TASKS-v0.26-EXECUTION.md`. Implementation commit
  `a90d080e1da18e8f16549b53c542b54259d74920` contains only that runbook, the
  `AGENTS.md` v0.26 declaration, and this progress-log skeleton. Its immediate
  parent remains the unamended v0.25 post-push audit
  `12d0601e202efe36c6a36d42254bf39f3d12744d`.
- entering-ref acceptance: PASS with one entering-hypothesis correction.
  Before activation, HEAD was post-push audit
  `12d0601e202efe36c6a36d42254bf39f3d12744d` on branch
  `codex/v0.23-action-migration`, not on local `main`; local `main` remained
  `eb2d9df8b3ffd3e0380d506e958fb5a3adb2d42e`. Read-only remote inspection
  resolved `main` and the peeled v0.16.0 tag to closing commit
  `c66c2b02191e3ca3126dddc3c004b175899b414e`, with annotated tag object
  `54f8cb2f89ed53d9e0b485f6cd46924a51e41813`; historical
  `refs/heads/candidate/v0.16.0` remained
  `3481e4ba85d65c927b7d0fc3a430bc04fb094394`. No ref changed, and
  `STATE.md`'s header was not given a mutable branch-hash assertion.
- lifecycle acceptance: PASS. `cycle-check` reports active v0.26 open with
  twenty-three closed execution runbooks and three historical runbooks.
  `checklist-audit` passes **198 checked / 3 retracted / 198 matched / 0
  exemptions**. `progress-check` correctly reported that the new skeleton had
  no dated entry before this audit record existed.
- scope acceptance: PASS. The activation commit is the scope anchor, so its
  `activation..HEAD` diff is empty. The static release-intent rule accepts the
  complete declared release-authority set.
- test acceptance: NOT RUN at this preparatory checkpoint; E0 owns the complete
  entering matrix and drafted-gate measurements.
- golden-E2E delta: NOT MEASURED; no claim.
- publisher-request acceptance: PASS. Activation invoked repository and GitHub
  ref/lifecycle commands only; it made no request to a publisher origin.
- protected artifact delta: NOT MEASURED; no protected or pinned file changed.

### 2026-07-30 · ACTIVATE-CORRECTION — trigger-table count made current

- owner: Codex
- commit: b6806e4b714a9eb0c42619834c4ac5f56985a9a8
- result: PASS. The first clean Python 3.11 E0 shell lane executed the live
  trigger-freshness control and found that v0.26 has **13** trigger-bearing
  rows while the exact current-table test still asserted **12**.
- fail-before acceptance: PASS. The clean constrained lane collected **284**,
  passed **283**, failed the exact
  `test_current_trigger_freshness_tables_are_complete` assertion, and skipped
  **0**. The observed count was `(2, 13)` against expected `(2, 12)`; this was
  a gate finding, not a passing shell measurement.
- gate-scope acceptance: PASS. The dated runbook amendment widens E0's gate
  only for `shell/tests/test_cycle_check.py`, which the full-matrix acceptance
  criterion already exercises and declared scope already permits. No objective,
  acceptance criterion, done condition, production permission, publisher
  permission, or trigger changed.
- focused acceptance: PASS. The unchanged failure-capable entry point now
  expects `(2, 13)` and passes **1/1**.
- lifecycle acceptance: PASS. `cycle-check` accepts the amended open v0.26
  runbook and its original activation anchor.
- scope acceptance: PASS. Only the active runbook and the exact shell
  lifecycle-count test changed. No production source, manifest, dependency,
  schema, protected artifact, public surface, configured source, or ref
  changed.
- complete-matrix acceptance: NOT YET CLAIMED. E0 restarts its clean Python
  lane after this correction and owns the complete entering result.
- golden-E2E delta: NOT MEASURED; no claim.
- publisher-request acceptance: PASS. The correction ran only a local focused
  lifecycle test and `cycle-check`; no publisher request occurred.

### 2026-07-30 · E0 — entering state rebuilt and seven gates settled

- owner: Codex
- commit: 4b9ed740953e7800480e59992c9364557c81a1d7
- result: PASS. Every drafted gate has an executed or enumerated measurement;
  G2 executed the shipped parser over the committed publisher-response bytes
  and accepted 200 documents.
- entering-matrix acceptance: PASS. `./run ci-local` passed all twenty stages:
  135 workspace Rust tests, 55 net-lane tests, current and Rust 1.78
  warning-denied builds, clippy, fmt, ShellCheck, floor byte-compilation,
  invariants 12/12 with 39 controls, and embedded golden 11/11.
- shell-population acceptance: PASS. Clean constrained Python 3.11.4 and
  3.12.13 lanes each collected 284, passed 284, and skipped 0. The comparator
  derived `collected=284`, `equivalent=true`, `equivalent_passed=284`, local
  `passed=284/skipped=0`, hosted `passed=284/on_site_skipped=0/skipped=[]`.
- standalone-controls acceptance: PASS. `golden` passed 11/11;
  `cycle-check`, `checklist-audit`, `progress-check`, `version-check`, and
  `invariant-scan` passed; root `export-check` passed 96 derived / 7 required /
  172 exported.
- G1 acceptance: PASS with finding. Store canonical assignment reads its
  private threshold at `crates/store/src/sqlite.rs:32`; view collapse reads an
  independent literal at `crates/view/src/lib.rs:44`. The execution record
  quotes R1 and R5's exact claims/scopes. R1 observes store caller topology and
  R5 observes the store constant bindings; neither compares the view value, so
  one declaration can move while the other remains 16 without either firing.
- G2 acceptance: PASS. A failure-capable disposable-clone integration probe
  executed shipped `RssSource` over the committed body and passed 1/1 with
  `parser-result=accepted documents=200`. Reqwest defaults a charset-less
  response to UTF-8 before roxmltree; this snapshot is lossless only because
  its bytes are pure ASCII. This is replay evidence, not fixture or live-wire
  evidence.
- G3 acceptance: PASS with finding. Schema-2 enumeration found 2 artifacts and
  266 pinned files, zero under `observations/`. The observation's prose hash is
  not executable; Step 2 must pin all five files before deriving its document
  measurements.
- G4 acceptance: PASS with finding. Offline finance ingest returned HTTP
  success with the fixture-backed source `ok:true` and fixtureless SEC
  `ok:false`, erroring that the binary lacks `net`. The shell pipeline printed
  the per-source error, continued, and exited 0. No existing test covers that
  exact fixtureless result or pipeline disposition.
- G5 acceptance: PASS. An external-effect capture double around the exact bare
  `harvest-arxiv` dispatcher recorded its generated config, three curl
  constructions, exact source-filtered ingest body, and zero SEC-origin
  requests. An isolated core confirmed that exact body selected only arXiv.
- G6 acceptance: PASS. Executing scheduler resolution produced the full
  quant-desk job at 7,200 seconds; no per-source cadence is needed, so SEC
  inherits the two-hour job interval.
- G7 acceptance: PASS. Generalizing `run` or adding a subcommand would require
  authorization and a replacement hash-chain admission. The viable no-pinned-
  byte path is a bounded operator sequence using a fresh archive, isolated
  loopback net core, exact SEC source selection, capture, and cleanup; a direct
  connector probe is not a harvest.
- artifact acceptance: PASS. Manifest validation reported 2 artifacts and 266
  pinned files; two `verify-artifacts` runs took 0.11 s / 0.09 s with all
  hashes exact; manifest size was 154,205 bytes.
- published-object acceptance: PASS. Read-only re-verification resolved remote
  main and peeled v0.16.0 to closing commit
  `c66c2b02191e3ca3126dddc3c004b175899b414e`, annotated tag object
  `54f8cb2f89ed53d9e0b485f6cd46924a51e41813`, and the historical candidate to
  `3481e4ba85d65c927b7d0fc3a430bc04fb094394`; local object relations matched.
- scope acceptance: PASS. The implementation changed only the active runbook
  status/evidence. `STATE.md`, core and schedule config, production source,
  fixtures, corpus, golden input, protected bytes, and refs did not change.
- golden-E2E delta: **0**; standalone and matrix golden remained 11/11 with the
  hamming-12 true-positive collapse.
- publisher-request acceptance: PASS. E0 made no publisher request.

### 2026-07-30 · REPLAY-BLOCKED — schema cannot express the required pin

- owner: Codex
- commit: d5311a5f6c91db713597ce1a88b27e9ffcfe4212
- result: BLOCKED at the Step 2 decision gate before any document-set
  measurement. The runbook requires the five v0.25 observation files to remain
  at their original paths, become manifest-pinned, and carry a chained
  admission record. Executed schema 2 cannot represent that combination.
- pre-proposal acceptance: PASS. Before constructing a candidate,
  `evidence_artifacts.py validate` and `verify-artifacts` passed with 2
  artifacts, 266 pinned files, and both protected databases exact.
- byte-enumeration acceptance: PASS. All five source files were independently
  re-hashed at 903,679 bytes total. The active execution record lists each
  path, byte count, and SHA-256; the feed remains 892,641 bytes at
  `154556cd81bda4fc2372386bf43aa7b4414335560dd1371c45bae09f1a8d9de3`.
- ordinary-pin fail-before acceptance: PASS. A disposable candidate adding an
  otherwise schema-shaped pinned-file object at the original observation path
  was examined by the real validator and failed because non-authorization pins
  must live beneath `evidence/`.
- chained-pin fail-before acceptance: PASS. A second disposable candidate
  included the required task/date/wire-reference/operator-approval/retroactive
  admission chain and was examined by the real validator; it failed the
  pinned-file exact-key check because `admission` is not allowed there.
- gate disposition: BLOCKED. Extending `tools/evidence_artifacts.py` and its
  schema is outside Step 2's Gate. Copying the bytes beneath `evidence/` would
  violate the runbook's explicit no-copy/original-path boundary. No workaround
  was implemented and no manifest proposal was made.
- replay acceptance: NOT MEASURED. Because pin-first is undischarged, no
  committed parser replay, field inventory, day-zone measurement, or extension
  enumeration was derived. The REPLAY checklist box remains unchecked.
- dependency disposition: IDENTITY-MEASURE and IDENTITY-DECISION remain blocked
  on Step 2. CADENCE remains independently eligible under the declared
  dependency graph.
- lifecycle acceptance: PASS. `cycle-check`, `progress-check`, and
  `checklist-audit` passed before this append, with the REPLAY box correctly
  unchecked.
- scope acceptance: PASS. The implementation commit changed only `STATE.md`
  and the active execution record. No schema, manifest, observation,
  production source, test, fixture, protected artifact, database, golden
  input, or ref changed.
- golden-E2E delta: **0**. The initial sandbox-only loopback bind refusal was a
  non-result; the identical permitted run passed 11/11.
- publisher-request acceptance: PASS. No publisher request was made.
