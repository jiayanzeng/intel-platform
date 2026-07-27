# PROGRESS-v0.13.md — append-only execution record

This file records v0.13 task and gate events after their implementation
commits exist. Each entry names the measured result, every applicable
acceptance criterion, the golden delta, and the real implementation commit.
Entries are append-only; corrections are new dated entries.

### 2026-07-27 · E0-GATE — clean worktree confirmed and v0.13 admitted

- owner: Codex
- commit: 5223d783b43c250102418163ef124f4e662b727b
- result: PASS for cycle activation only; E0 remains unchecked. The mandated
  opener found entering HEAD
  `466ebb3fc9736923110803e087acc798e417d084`, described as
  `v0.12.0-1-g466ebb3`, with local `main` and `origin/main` aligned (zero ahead
  / zero behind). The only worktree entry was the operator-supplied untracked
  `TASKS-v0.13-EXECUTION.md`. Annotated `v0.12.0` remained tag object
  `94d8215bc2151fecba1280dc793d3f5953cd8055`, peeled to
  `e5faf0c161a4256f33976664685653d8bd805d5d`.
- correction: implementation commit
  `5223d783b43c250102418163ef124f4e662b727b` committed only the supplied
  runbook, the `AGENTS.md` active-cycle header, and the empty append-only
  progress log.
- lifecycle acceptance: PASS. `./run cycle-check` reports active v0.13 open
  with ten closed execution runbooks. `./run checklist-audit` resolves the
  entering **99/99** checked tasks, reports the one existing v0.11 retraction
  separately, and finds zero exemptions. `git diff --check` passed.
- test acceptance: NOT RUN at this preparatory checkpoint; E0 owns the
  entering matrix and C1–C5 reproduction.
- golden-E2E delta: NOT MEASURED; no claim.
- protected artifact delta: NOT MEASURED; no protected or pinned file was
  touched.

### 2026-07-27 · E0 — entering state rebuilt and five findings confirmed

- runbook: `TASKS-v0.13-EXECUTION.md`
- owner: Codex
- commit: ed7249c1cf6429c6482592551a2a6e7dc996d9d3
- result: PASS. The permitted entering matrix passed **20/20** with **121**
  workspace Rust tests, **21** net tests, **205/205** Python 3.11 shell tests,
  zero rustc/clippy/fmt/ShellCheck failures, locked Rust 1.78 green,
  protected databases **2/2**, all **71/71** pins, and golden **11/11**. The
  initial sandboxed matrix is an environment non-result because eight shell
  controls were denied loopback/process access after 197 tests passed.
  Python 3.12 passed **205/205**, with both interpreters verifying **21/21**
  exact packages. Standalone golden repeated **11/11**.
- C1 acceptance: PASS as a confirmed release-blocking finding. A real `cored`
  over exactly two scratch documents returned an empty `/retrieve` context for
  a finance scope querying science-only text; direct
  `documents_by_ids(["science-b"])` nevertheless returned the science body,
  proving upstream ranking rather than final hydration supplied containment.
  `/attest` has no sector field and returned HTTP 200 with a violation naming
  the out-of-sector `IndexOnly` document; a nonexistent id returned HTTP 400.
  The cross-sector existence/match oracle is live. No `/retrieve` body leak
  reproduced.
- C2 acceptance: PASS as a confirmed coverage defect. The renamed
  `INGEST_FUZZ_LIMIT=17` production mutation exited 0 with the exact line
  `invariant-scan: R5 PASS: Production Rust has one private
  canonical-distance constant and no numeric canonical-distance call
  argument.` The original named-constant and numeric-call controls separately
  exited 1 with `R5 FAIL` at `sqlite.rs:33` and `sqlite.rs:207`.
- C3 acceptance: PASS as a confirmed harness defect. Sixteen enumerated shell
  test files contain no invariant-scan test. Replacing R4's provider-key regex
  with the never-matching `(?!)` pattern still exited 0 and reported **6/6**
  rules passing, proving `fail_before` is not executed.
- C4/C5 acceptance: PASS as confirmed findings. The architecture's endpoint
  table and HC2 prose contradict the unscoped `/retrieve` and `/attest`
  hydration paths. The crawler already shares one UA constant across both
  clients and `RobotsCache`, but that constant has the stale `0.1` version and
  `you@example.com`; there is no contact override or startup refusal.
- published-baseline acceptance: PASS. Annotated `v0.12.0` remains object
  `94d8215bc2151fecba1280dc793d3f5953cd8055`, peeled to
  `e5faf0c161a4256f33976664685653d8bd805d5d`; all 71 pins and both protected
  databases re-verified byte-exact. No C1–C5 row refuted.
- golden-E2E delta: **0**; the mandatory post-task run remained **11/11**
  byte-identical.
- cleanup: both disposable worktrees, their temporary database/log, and the
  spawned core process were removed; the live tree returned clean before the
  task record.

### 2026-07-27 · FAIL-BEFORE-EXEC — invariant controls made executable

- runbook: `TASKS-v0.13-EXECUTION.md`
- owner: Codex
- commit: b398f1266324eb43b4b77519f527d09e3b1eb1c9
- result: PASS. Registry schema 2 gives every R1–R6 rule a reconstructible
  exact-text mutation and expected failure substring. The scanner applies one
  control at a time in a fresh copy of the Git-tracked tree, runs only the
  owning rule, and requires exit 1 plus the recorded reason. The existing
  no-argument CI path executes this same self-test.
- preservation acceptance: PASS. All six former decorative `fail_before`
  strings are preserved byte-for-byte as `fail_before_note`; a dedicated test
  asserts the exact mapping. No R1–R6 matcher, pattern, scope outcome, or rule
  matching logic changed.
- positive-control acceptance: PASS. The real
  `./run invariant-scan --self-test` passed the clean R1–R6 scan and all
  **6/6** controls. Temporarily changing R4's provider-key regex to `(?!)`
  made the same command exit **1** with `SELF-TEST R4/1 FAIL: mutation did not
  make the rule fail`; restoring it returned the matrix to green. The new
  focused module passed **10/10**, including malformed-registry and
  unimplemented-rule exit-2 cases.
- CI acceptance: PASS. The corrected `./run ci-local` passed **20/20** with
  **121** workspace Rust tests, **21** net tests, **215/215** Python 3.11
  shell tests, warning-denied builds, clippy/fmt/ShellCheck, locked Rust 1.78,
  protected databases **2/2**, all **71/71** pins, and golden **11/11**.
  Python 3.12 independently passed **215/215** and verified **21/21** exact
  packages.
- integration note: an initial attempt to add the explicit flag to `run`
  tripped the protected authorization-surface pin and one evidence test, so it
  was a non-result. `run` was restored byte-exact at SHA-256
  `7afede56f13b5ee73d3f1dbe92910ce535908623676db21664409855c5ac006d`
  and is absent from the implementation diff.
- golden-E2E delta: **0**; the mandatory post-task standalone run remained
  **11/11** byte-identical.
- decision gate: PASS for this assurance task. The C1 body-boundary release
  blocker remains open for its ordered correction task.

### 2026-07-27 · THRESHOLD-BIND-GATE — production parameter seam found

- runbook: `TASKS-v0.13-EXECUTION.md`
- owner: Codex
- commit: 146feeb8fd4e205e9075b1c6c3f1428b26f8be0f
- result: BLOCKED before implementation, with the runbook-required follow-up
  recorded. A strict candidate R5 enumerated every production call to
  `assign_canonical_ids`, `assign_canonical_ids_tx`, and
  `rematerialize_canonical_ids_with_distance`, excluded the `#[cfg(test)]`
  seam, and required each distance argument to be exactly
  `DEDUP_MAX_DISTANCE`.
- gate measurement: the candidate exited **1** against unmodified HEAD with
  `invariant-scan: R5 FAIL: crates/store/src/sqlite.rs:685:
  assign_canonical_ids_tx distance argument must be DEDUP_MAX_DISTANCE; found
  max_distance`. The no-argument public maintenance method binds the constant
  at line 657, but its production parameterized helper forwards
  `max_distance` at the transaction call.
- disposition: Step 3 expressly forbids changing `crates/` to make its rule
  green and requires a source finding to be handled in a follow-up task. The
  candidate matcher was therefore not committed, no Rust source changed, and
  THRESHOLD-BIND remains unchecked. The disclosed
  THRESHOLD-SOURCE-SEAM follow-up owns only removal of the production
  parameter seam; the original Step 3 contract is unchanged and resumes after
  that correction.
- regression acceptance: PASS. The committed pre-rewrite invariant scanner
  remains green with R1–R6 and all **6/6** executable controls. `cycle-check`,
  `checklist-audit`, and `git diff --check` passed.
- golden-E2E delta: **0**; the mandatory post-gate run remained **11/11**
  byte-identical.

### 2026-07-27 · THRESHOLD-SOURCE-SEAM — production parameter removed

- runbook: `TASKS-v0.13-EXECUTION.md`
- owner: Codex
- commit: 0b266ade7e051b0cc394e7c598ef77d908b5adc8
- result: PASS. The public no-argument
  `rematerialize_canonical_ids` method now opens its transaction and calls
  `assign_canonical_ids_tx` directly with `DEDUP_MAX_DISTANCE`. The production
  `rematerialize_canonical_ids_with_distance(max_distance)` helper is absent.
- test-seam acceptance: PASS. Alternate distances remain reachable only
  through the `#[cfg(test)]` `assign_canonical_ids` method, which uses the same
  real transaction, materialization, commit, and rollback path. The focused
  `intel-store` suite passed **21/21**, including boundary, differential,
  missing-fingerprint rollback, ordering, update, and deletion controls.
- strict-rule acceptance: PASS. Re-applying the strict R5 candidate against
  the post-task source returned `R5 PASS`, overall **1/1**, exit **0**. All
  five production `assign_canonical_ids_tx` calls pass the single token
  `DEDUP_MAX_DISTANCE`; the one `max_distance` call is inside the test-only
  seam. No tool or registry file is present in the implementation diff.
- Rust acceptance: PASS. Warning-denied workspace check/test passed **121**
  tests; warning-denied net check and `intel-ingest` net tests passed
  **21/21**; clippy and fmt were clean; locked Rust 1.78 check/test passed
  **121** tests.
- golden-E2E delta: **0**; the mandatory post-task run remained **11/11**
  byte-identical.
- disposition: the gate-mandated source correction is complete.
  THRESHOLD-BIND may resume without an exemption or a source change in its
  rule-only commit.
