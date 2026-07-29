# PROGRESS-v0.20.md — append-only execution record

This file records v0.20 task and gate events after their implementation
commits exist. Each entry names the measured result, every applicable
acceptance criterion, the golden delta, and the real implementation commit.
Entries are append-only; corrections are new dated entries.

### 2026-07-29 · ACTIVATE — v0.20 admitted

- owner: Codex
- commit: 2a9e1c8
- result: PASS for cycle activation only; E0 remains unchecked. Before
  activation, local `main` was the intentionally unpushed forward publication
  audit `72b6f425114e06b1e148e0aa360e280a690e4f0c`, one commit ahead of
  measured `origin/main`
  `692069ead0b8823d6874d8f2fc0a593d9f26704f`.
- worktree acceptance: PASS. The only pre-activation worktree item was the
  operator-supplied untracked `TASKS-v0.20-EXECUTION.md`; implementation commit
  `2a9e1c8` contains only that runbook, the `AGENTS.md` v0.20 declaration, and
  this new append-only progress-log skeleton.
- lifecycle acceptance: PASS. After the implementation commit,
  `./run cycle-check` reports active v0.20 open with seventeen closed execution
  runbooks. `./run checklist-audit` resolves the entering **158/158** checked
  tasks, reports the same three retractions, and finds zero exemptions.
  `git diff --check` passed.
- G1 activation observation: `cycle-check` passes locally only because the
  measured `origin/main` has not moved from the literal value asserted in the
  current `STATE.md` header. This is evidence for E0's fixed-point gate, not
  evidence that the publication-freshness rule is satisfiable.
- test acceptance: NOT RUN at this preparatory checkpoint; E0 owns the complete
  entering matrix and G1–G5 measurements.
- golden-E2E delta: NOT MEASURED; no claim.
- protected artifact delta: NOT MEASURED; no protected or pinned file changed.

### 2026-07-29 · E0 — entering state and drafted gates measured

- owner: Codex
- commit: 3794100
- result: PASS. The read-only Gate contains every acceptance surface; only the
  runbook status/checklist and this append-only record moved. `STATE.md`
  remained blob `fb996dc34c41b81da8418946896898c3125a3ad7`,
  byte-identical to the entering tree.
- entering-matrix acceptance: PASS. The first sandboxed `./run ci-local` was a
  loopback-bind permission non-result; the identical permitted invocation
  passed **20/20** with **133** workspace tests, **55** net tests (**29 + 26**),
  shell **248/248** on Python 3.11.4, locked Rust 1.78, zero
  rustc/clippy/fmt/ShellCheck failures, `invariant-scan` **11/11 rules / 23
  controls**, all **176/176** pins, protected databases **2/2**, and golden
  **11/11**. A clean constrained Python 3.12.13 rebuild resolved **21/21**
  packages and passed shell **248/248**. Standalone golden passed **11/11**.
- hosted-state acceptance: PASS as a recorded red result, not a green matrix.
  GitHub run `30417274925` remains failed at exact remote head `692069e…`.
  E0 found a later attempt **2** than the draft's attempt 1. Six blocking job
  instances succeeded; only `shell (Python 3.11)` failed, at
  `active cycle and amendment consistency`, because `cycle-check` reported
  asserted `origin/main` `344124819c…` versus measured `692069ead0…`, then
  exited 1.
- G1 acceptance: PASS and CONFIRMED. Exact commit `72b6f42…` passed while the
  simulated tracking ref equaled its header's `692069e…`, then the same
  immutable content failed after that ref moved to `72b6f42…`. A truth-table
  construction showed the pre-push literal passes only before, the post-push
  literal only after, and no third literal passes either; satisfiable was
  **false** because the two required values differ.
- G2 acceptance: PASS and CONFIRMED. A stale header produced one error with
  complete history. Removing its tag made `check_publication_status` return
  exit **0** with `errors=[]`. A depth-1 clone with the tag object/target but no
  connecting ancestry made `merge-base --is-ancestor` exit **1**, while the
  same check again returned zero errors over a stale header.
- G3 acceptance: PASS with corrected measurements. Root-run Repomix 1.17.0
  produced **2,713,184 characters / 147 files** and **2,718,308** serialized
  bytes. The pattern excludes **17 / 657,725 bytes** and retains **20 /
  633,876 bytes** under `docs/cycles/`; missed `TASKS-v0.6.md` and
  `TASKS-v0.7.md` total **31,147 bytes**, not the draft's 30,842.
- G4/source-drift acceptance: PASS. `run` has no export command and `AGENTS.md`
  has no Repomix/export-check rule. The current source set derived from
  `git ls-files` is **88**, all **88/88** present in the export. The recorded
  **89** at EXPORT-BUDGET differs by exactly the later-deleted
  `crates/ingest/src/bin/robots_preview.rs`; no discrepancy remains open.
- G5 acceptance: PASS and CONFIRMED. An unrelated nearby `outstanding` matched
  after `publication`. The bounded header-only false refusal is accepted for
  this four-change cycle; it cannot produce a false pass.
- object/pin acceptance: PASS. Remote main is `692069e…`; annotated
  `v0.15.3` is object `2039e014…`, peeled to `dbff27d559…`. Standalone
  `verify-artifacts` passed all **176/176** pins and protected databases
  **2/2**.
- status acceptance: PASS after the implementation commit exists.
  `cycle-check`, `progress-check`, `version-check`, and `invariant-scan` are
  green; the expected pre-audit `checklist-audit` refusal named only E0's
  missing progress entry and is rerun after this append.
- golden-E2E delta: **0**; mandatory standalone execution passed **11/11**.

### 2026-07-29 · SELF-REF — publication fixed point removed

- owner: Codex
- commit: b365f8a
- result: PASS. E0 confirmed G1 and G2 before implementation. The implementation
  commit contains only `tools/cycle_check.py`, its focused test file,
  `STATE.md`, and the v0.20 runbook's SELF-REF status/checklist record. No
  closed runbook, historical append, crate, dependency, schema, protected
  artifact, database, or public surface changed.
- fail-before acceptance: PASS. With the corrected checker and the entering
  header still intact, `./run cycle-check` exited **1** and reported exactly
  `STATE.md: publication status header must not assert a literal origin/main
  hash; publishing the asserting commit moves that ref, so record mutable-ref
  measurements in a dated body append`.
- structural-prohibition acceptance: PASS. `origin/main` is absent from the
  freshness comparison and a live-header literal is structurally refused in
  both the historical formatted wording and an unformatted assignment. The
  implementation comment records why publishing moves this one mutable ref.
  The live `STATE.md` header carries publication disposition, version,
  annotated tag object, and peeled release commit with no `origin/main` hash;
  E0's exact branch measurement is preserved in the dated 2026-07-29 body
  append.
- immutable/unavailable acceptance: PASS. Both tag-object and tag-target
  freshness labels still fire on wrong values. Missing tag ref, missing peeled
  target, and unavailable ancestry now each append a named error; no
  unavailable input silently returns or continues without a report.
- rule-1 acceptance: PASS. The original focused control still proves that a
  reachable annotated release cannot coexist with a live header calling
  publication pending. The rule's implementation is unchanged.
- focused-test acceptance: PASS. `shell/tests/test_cycle_check.py` passed
  **24/24**, covering the prohibition, passing header, both retained freshness
  labels, every unavailable-input report, unchanged rule 1, and body-only
  historical ref tolerance.
- full-matrix acceptance: PASS. On the exact implementation candidate,
  permitted `./run ci-local` passed **20/20** with **133** workspace tests,
  **55** net tests (**29 + 26**), shell **252/252** on Python 3.11.4, locked
  Rust 1.78, zero rustc/clippy/fmt/ShellCheck failures, `invariant-scan`
  unchanged at **11/11 rules / 23 controls**, all **176/176** pins, protected
  databases **2/2**, and golden **11/11**. Python 3.12.13 independently passed
  shell **252/252** against the exact **21-package** constraints.
- status acceptance: PASS before the implementation commit:
  `cycle-check`, `checklist-audit`, `progress-check`, `version-check`,
  `invariant-scan`, manifest validation, and `verify-artifacts` were green.
  After checking SELF-REF and before this legally hash-bearing append, the
  expected checklist refusal named only the missing SELF-REF progress entry;
  it is rerun after this append.
- golden-E2E delta: **0**. Mandatory standalone `./run golden` passed
  **11/11** on the exact implementation candidate.

### 2026-07-29 · EXPORT-PATTERN — closed-cycle range completed

- owner: Codex
- commit: ba1b4e7
- result: PASS. The implementation commit contains only the one-line
  `repomix.config.json` pattern and the required `STATE.md` / runbook status
  records. No repository file, tool, crate, dependency, protected artifact,
  database, or public surface was deleted or modified.
- pattern acceptance: PASS. The former enumerated
  `v0.{8,9,10,11}*` expression is now the range-shaped
  `v0.{[6-9],1[01]}{.md,.*.md,-*.md}` under the existing
  `{TASKS,PROGRESS}` prefix. The numeric classes cover every cycle v0.6
  through v0.11; the suffix alternatives cover base records, point cycles,
  and execution runbooks without matching v0.12. Repomix 1.17.0 executed the
  expression successfully, and JSON validation passed.
- size acceptance: PASS. Immediate project-root exports before and after the
  one-line change measured **147 → 145 files**, **2,735,717 → 2,704,779
  characters**, and **2,740,883 → 2,709,638 serialized bytes**.
- inclusion acceptance: PASS. The complete path-set diff removed exactly
  `docs/cycles/TASKS-v0.6.md` and `docs/cycles/TASKS-v0.7.md`. All **18/18**
  task/progress files from v0.12 through active v0.20 remained. No
  non-`docs/cycles/` inclusion changed, and `git status` confirmed neither
  historical source file was deleted.
- integrity acceptance: PASS. `verify-artifacts` passed all **176/176** pins
  and both protected databases **2/2**. `cycle-check`, `version-check`,
  JSON validation, and `git diff --check` passed.
- golden-E2E delta: **0**. Mandatory standalone `./run golden` passed
  **11/11**.

### 2026-07-29 · EXPORT-CHECK — derived source completeness enforced

- owner: Codex
- commit: 36e47b4
- result: PASS. Step 3 was complete before implementation. The implementation
  commit contains `run`, `tools/export_check.py`, its focused shell test, the
  updated `run` authorization pin, `STATE.md`, and the v0.20 runbook's
  status/checklist record. No crate, dependency, schema, protected database,
  evidence artifact, or public surface changed.
- derived-set acceptance: PASS. `./run export-check` uses pinned Repomix
  1.17.0 from the project root, derives all tracked `crates/`, `apps/`,
  `tools/`, and `shell/` paths with `git ls-files`, and separately requires
  the seven named root/control paths. No source count is pinned. The final
  candidate contained all **90/90** derived source paths and **7/7** required
  paths in its **147-file** export.
- fail-before acceptance: PASS. A disposable invocation from `crates/` exited
  **1**, explicitly named missing required path `Cargo.lock`, and reported 95
  missing paths. A root invocation with only a disposable config's
  `enableSecurityCheck` changed to `true` made Repomix omit exactly
  `crates/ingest/src/lib.rs`; the checker exited **1** and named that missing
  derived source.
- restoration acceptance: PASS. The real `repomix.config.json` was never
  changed, remained SHA-256
  `0470cb2ba232a549e94a95ece5e337f025cde2fb17cd37a330af6a3d5e35b2ee`,
  and `git diff --exit-code -- repomix.config.json` passed after both controls.
- execution-posture acceptance: PASS. The command and help text say
  **operator-local**. The check is absent from both `ci-local` and hosted CI
  because it writes a multi-megabyte export and `npx` may fetch its pinned
  tool. The final restricted invocation's DNS refusal was a non-result; the
  permitted identical retry passed.
- authorization-pin acceptance: PASS. `run` moved from
  `caae4e8007fc885241bf1ac7c844e397a149970048e036be285e356449030678`
  / **42,056 bytes** to
  `0fc7f0be0ea2d8c68ff63be55dd0b73cc1385ce966b8307506a5387543f18779`
  / **43,044 bytes**. The model-profile functions, models dispatch, mirrored
  authorization policy, and `tools/model_profiles.py`
  (`1920761c97ffa6fc7b5242c16384fb6f1b0727937f9e1cfd7e00826c913554df`,
  **28,297 bytes**) are unchanged. Manifest validation, all **176/176** pins,
  protected databases **2/2**, and R6 pass.
- failure-capable-test acceptance: PASS. Focused tests pass **3/3**, including
  a newly tracked source that fails without changing a count and a named
  missing-`Cargo.lock` failure. Final `invariant-scan` passes **11/11 rules /
  23 controls**; a pre-final R10 line-shift was caught and corrected before
  the implementation candidate.
- full-matrix acceptance: PASS. The permitted `./run ci-local` passed
  **20/20** with **133** workspace tests, **55** net tests (**29 + 26**),
  shell **255/255** on Python 3.11.4, locked Rust 1.78, zero
  rustc/clippy/fmt/ShellCheck failures, all pins and databases exact, and
  golden **11/11**. Python 3.12.13 independently passed shell **255/255**;
  its first restricted invocation was a permission non-result and the
  permitted identical retry passed.
- golden-E2E delta: **0**. Mandatory standalone `./run golden` passed
  **11/11**.

### 2026-07-29 · EXPORT-CONTRACT — measured operating rules recorded

- owner: Codex
- commit: 15b7d48
- result: PASS. The implementation commit contains only `AGENTS.md`,
  `ARCHITECTURE.md`'s stale review-export paragraph, `STATE.md`, and the
  v0.20 runbook's status/checklist record. No tool, crate, configuration,
  dependency, protected artifact, database, or public surface changed.
- root-rule acceptance: PASS. `AGENTS.md` requires project-root generation and
  records why: the measured non-root invocation did not load the project
  configuration and silently dropped `Cargo.lock`. It points at
  `./run export-check`, which generates at the root and derives tracked source
  paths with `git ls-files`.
- security-rule acceptance: PASS. `AGENTS.md` requires
  `enableSecurityCheck=false`, records the **340 collected / 339 included**
  measurement and omitted `crates/ingest/src/lib.rs`, retains registered
  self-testing R4 as the credential control, and points at
  `./run export-check`.
- architectural-scope acceptance: PASS. No HC was added or renumbered.
  `ARCHITECTURE.md` now correctly describes the check as an executable
  operator-local contract, not a hosted repository invariant. It also records
  why the multi-megabyte, potentially network-fetching check remains outside
  local/hosted CI.
- executable acceptance: PASS. `./run export-check` found **90/90** derived
  sources and **7/7** required paths in **147** exported paths.
  `cycle-check` and `git diff --check` passed. The expected pre-audit
  `checklist-audit` refusal named only EXPORT-CONTRACT's not-yet-possible
  progress entry; it is rerun after this hash-bearing append.
- golden-E2E delta: **0**. Mandatory standalone `./run golden` passed
  **11/11**.

### 2026-07-29 · RE-MEASURE — v0.15.4 release evidence admitted

- owner: Codex
- commit: 5631e70
- result: PASS. The operator authorized exactly the Step 6 Gate's
  non-`main` candidate push and authenticated hosted dispatch. The
  implementation commit contains the seven signed receipt/bundle pairs from
  that run, its release-posture deferred-audit report, the 15 append-only
  manifest admissions, `STATE.md`, and the v0.20 runbook status/pending-closing
  records. No tag, `main` advance, publication, product path, public surface,
  dependency, lockfile, schema, or protected database changed.
- version/candidate acceptance: PASS. The runbook's mechanical patch default
  selected `v0.15.4` because no `/v1/*` route or body and no crate changed.
  Exact candidate
  `8230d4f24f565afcde92931c987adff4339036af` was pushed to
  `candidate/v0.15.4`.
- workflow acceptance: PASS. Before dispatch, the remote candidate's
  `.github/workflows/ci.yml` was read through both contents and raw paths and
  confirmed to contain the expected core, lint, net, MSRV, two-shell, golden,
  cycle/checklist, invariant/progress, receipt-signing, and artifact-upload
  invocations. Remote and local workflow blobs are both
  `96e85af978981b7af9bdd8e9e11069f158f35e57`.
- hosted/count acceptance: PASS. Workflow-dispatch run `30423736121` attempt
  **1** completed successfully at the exact candidate with all **6** blocking
  jobs green. Hosted logs, not job labels, measured **133** workspace tests,
  **55** net tests (**29 + 26**), `invariant-scan` **11/11 rules / 23
  controls**, R10 **45** exemptions, and golden **11/11**, equal to local
  `./run ci-local` at that same commit. Each hosted shell lane collected the
  same **255** tests as local, with Linux reporting **254 passed + 1 declared
  on-site-only protected-corpus skip** versus macOS **255 passed**. Hosted
  Python 3.11.15 and 3.12.13 each resolved the exact **21-package**
  constraints; constrained local Python 3.11.4 and 3.12.13 each passed
  **255/255**.
- corrected-control acceptance: PASS. Hosted `shell (Python 3.11)`, step
  `active cycle and amendment consistency`, used `fetch-depth: 0` and reported
  `cycle-check: PASS` with active v0.20 open, 17 closed execution runbooks,
  three historical runbooks, and no requested local tag refs. The same job
  reported checklist **163 checked / 3 retracted / 163 matched / 0
  exemptions** and prior progress head `EXPORT-CONTRACT` at `15b7d48`.
- authentication/re-derivation acceptance: PASS. All **7/7**
  workflow-derived identities across the six jobs have successful Linux
  receipts and persisted Sigstore bundles; zero receipts were rejected and the
  single-run matrix is complete. The first committed re-derivation was a
  restricted-network non-result during online attestation verification. The
  permitted identical command passed **7** rows, **5** source dispositions,
  and **7** triggers with release grade and attestations required.
- deferred-audit acceptance: PASS. The first clean detached invocation was a
  setup non-result because its subject lacked the intentionally untracked
  protected databases and raised `FileNotFoundError` before producing a
  report. The retry exposed the already verified read-only database bytes
  through ignored links under `/private/tmp`; both hashes matched and detached
  `git status` stayed clean. The resulting report records **5 deferred / 2
  promoted / 0** deferred subsystems implemented. Exact-cosine p95 at the
  largest **2,600-document** archive is **8.958167 ms**, below the
  **16.264 ms** A3 request anchor.
- artifact acceptance: PASS. Report
  `evidence/v0.15.4/deferred-audit/report.json` is **34,608** bytes at
  SHA-256
  `b90b2f00d8129f17c09e48e2bdefb2d48d97f5d502e2723b8a5e2d0a5d25d00e`.
  The **15** new records bring the protected manifest to **191/191** pins —
  **189/189** evidence plus **2/2** authorization surfaces. Manifest schema
  v2, `verify-artifacts`, and `evidence-report` pass with protected databases
  **2/2** exact.
- status/ref acceptance: PASS. A first status draft put the exact mutable
  `origin/main` measurement back into the live header; the new SELF-REF guard
  rejected it with its named structural diagnostic. Moving the exact
  measurement to the dated body made `cycle-check` pass. A restricted final
  ref query was a DNS non-result; the permitted identical read confirms
  `origin/main` remains
  `692069ead0b8823d6874d8f2fc0a593d9f26704f`, the candidate remains exact,
  and no `v0.15.4` tag exists. The expected pre-audit `checklist-audit`
  refusal named only this not-yet-possible hash-bearing progress entry; it is
  rerun after this append.
- shell supplemental acceptance: PASS. Restricted post-audit repeats of both
  shell lanes were loopback/process-inspection permission non-results; the
  identical permitted Python 3.11.4 and 3.12.13 commands each passed
  **255/255**.
- golden-E2E delta: **0**. The first final sandboxed `./run golden` was a
  loopback-bind permission non-result; the identical permitted invocation
  passed **11/11**.
