# PROGRESS-v0.15.md — append-only execution record

This file records v0.15 task and gate events after their implementation
commits exist. Each entry names the measured result, every applicable
acceptance criterion, the golden delta, and the real implementation commit.
Entries are append-only; corrections are new dated entries.

### 2026-07-28 · E0-GATE — v0.15 admitted

- owner: Codex
- commit: 31916e01098ae9b68d2b6af10877ad91ea6d270f
- result: PASS for cycle activation only; E0 remains unchecked. Read-only
  verification found local `main` and `origin/main` aligned (zero ahead / zero
  behind) at `a75c9cf5defa42e985811b01f9905b6ac99797fd`, described as
  `v0.14.0-3-ga75c9cf`. The only worktree entry was the operator-supplied
  untracked `TASKS-v0.15-EXECUTION.md`.
- published-tag acceptance: PASS. Annotated `v0.14.0` remains tag object
  `dddc1a52d28a1832727a8d8eb5e87fc7168511c6`, dereferencing exactly to release
  commit `4ad4c8d71075731dd87c360e8b0d3d91d80b5518`.
- activation acceptance: PASS. Implementation commit
  `31916e01098ae9b68d2b6af10877ad91ea6d270f` committed only the supplied
  runbook, the `AGENTS.md` v0.15 declaration, and the empty append-only
  progress log.
- lifecycle acceptance: PASS. `./run cycle-check` reports active v0.15 open
  with twelve closed execution runbooks. `./run checklist-audit` resolves the
  entering **121/121** checked tasks, reports the three existing retractions
  separately, and finds zero exemptions. `git diff --check` passed.
- test acceptance: NOT RUN at this preparatory checkpoint; E0 owns the full
  entering matrix and H1–H5 reproduction.
- golden-E2E delta: NOT MEASURED; no claim.
- protected artifact delta: NOT MEASURED; no protected or pinned file was
  touched.

### 2026-07-28 · E0 — entering state rebuilt and H1–H5 measured

- runbook: `TASKS-v0.15-EXECUTION.md`
- owner: Codex
- commit: 2e5cb8fbac29be03791c175afdafca996fcb0fb4
- result: PASS with one hypothesis correction. The permitted clean
  `./run ci-local` passed **20/20** with **125** workspace Rust tests, **48**
  net tests (**23** `intel-ingest` + **25** `cored`), zero
  rustc/clippy/fmt/ShellCheck failures, locked Rust 1.78 green, Python 3.11.4
  **225/225**, all **101/101** pins, protected databases **2/2**, and golden
  **11/11**. Standalone Python 3.12.13 passed **225/225** with **21/21** exact
  packages.
- entering-command acceptance: PASS. Standalone `golden`,
  `verify-artifacts`, `cycle-check`, `checklist-audit`, `progress-check`,
  `version-check`, and no-argument `invariant-scan` all passed. The scanner
  measured **9/9 rules / 15 controls**. Annotated `v0.14.0` remained tag object
  `dddc1a52d28a1832727a8d8eb5e87fc7168511c6`, peeling to unchanged release
  commit `4ad4c8d71075731dd87c360e8b0d3d91d80b5518`.
- H1 acceptance: PASS in both directions. Deleting the hosted
  `intel-ingest --features net` test step and, separately, deleting the local
  net-test `ci_local_job` line (leaving **19** calls) each left the existing
  invariant/lifecycle/version tools green and the focused
  invariant/deferred modules at **53 passed / 1 intended skip**.
- H2 acceptance: PASS as a measured partial refutation. An eighth blocking job
  left `invariant-scan` green but made the existing workflow receipt-count
  assertion fail at **8 != 7**. Removing `golden` from both `ci.yml` and
  `EXPECTED_RUNNER_JOB_IDENTITIES` was not silent: the deferred-audit module
  reported **8 failed / 28 passed / 1 skipped**, including **6 != 7** and
  fixture assumptions retaining the seventh identity. The identity authority
  remains hard-coded; Step 3 must derive it while preserving these alarms.
- H3 acceptance: PASS. A Rust-only rename of the injectable `sector_load`
  string left `invariant-scan` **9/9 / 15**, offline `cored` **24/24**, and
  benchmark-view **4/4** green while Python remained stale.
- H4/H5 acceptance: PASS. Git history shows v0.14 Step 8's stale “match Step
  2's recorded values” criterion and its same-candidate amendment.
  `AGENTS.md` lacks both proposed review-discipline rules.
- cleanup acceptance: PASS. All five disposable mutation worktrees were
  removed; closed runbooks, progress logs, protected artifacts, and source
  files were unchanged.
- golden-E2E delta: **0**. The mandatory post-task standalone run remained
  **11/11** byte-identical.
