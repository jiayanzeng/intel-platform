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

### 2026-07-28 · R10-CI-PARITY — local and hosted check scope derived

- runbook: `TASKS-v0.15-EXECUTION.md`
- owner: Codex
- commit: 35a5583f7c9f05bf7e713bcc2afebec3c86e8249
- mechanism decision: PASS. R10 parses `run`'s real function bodies and
  dispatch plus `ci.yml`'s jobs, matrix axes, steps, actions, and commands. No
  third manifest or correspondence marker was added. This was preferred
  because both existing authorities are regular enough to parse, while a
  marker would create another hand-maintained scope list.
- parity acceptance: PASS. The clean report derives **20 local jobs / 24
  normalized checks** and **6 blocking hosted jobs / 23 normalized checks**.
  The workflow now runs `checklist-audit` and `progress-check` in its Python
  3.11 leg. The sole local-only verification is protected database bytes,
  which hosted runners intentionally do not contain; hosted CI validates the
  manifest schema.
- exemption acceptance: PASS. R10 reports and the focused test pins **45**
  explicit exemptions: one report-only drift job, one operator-local protected
  database check, 18 runner setup steps, one Python environment setup step,
  and 24 release receipt/attestation/persistence steps.
- control acceptance: PASS. All three site-specific controls fail with exact
  file and line: local check removal at `run:439`, hosted check removal at
  `.github/workflows/ci.yml:221`, and an unpaired hosted check at line 228.
  No-argument scanner execution passes **10/10 rules / 18 controls**.
- test acceptance: PASS. The focused scanner module passed **20/20** on Python
  3.11.4 and 3.12.13. Full shell passed **228/228** on both interpreters with
  **21/21** exact packages.
- matrix acceptance: PASS. `./run ci-local` remains **20/20**, with **125**
  workspace Rust tests, **48** net tests (**23 + 25**), zero
  rustc/clippy/fmt/ShellCheck failures, locked Rust 1.78 green, all **101/101**
  pins, and protected databases **2/2**.
- preservation acceptance: PASS. No source under `crates/` or `apps/`, public
  API body, SQLite schema, dependency, protected artifact, or closed record
  changed.
- golden-E2E delta: **0**. Matrix and mandatory standalone golden both remained
  **11/11** byte-identical.

### 2026-07-28 · IDENTITY-DERIVE — hosted receipt scope derived

- runbook: `TASKS-v0.15-EXECUTION.md`
- owner: Codex
- commit: e853ce380782a04c1573ea67fd657b8572e9b2c8
- derivation acceptance: PASS. `tools/audit_deferred.py` imports and reuses
  R10's workflow parser. It derives `core`, `golden`, `lint`, `msrv`, `net`,
  `shell/python=3.11`, and `shell/python=3.12` from the six blocking workflow
  jobs and their matrix legs. `EXPECTED_RUNNER_JOB_IDENTITIES` and the
  deferred-test fixture's duplicate identity tuple are removed.
- report-only acceptance: PASS. The exclusion criterion is job-level
  `continue-on-error: true`, not a name list. A scratch `derived-report` job
  carrying that property stayed outside the set, while a scratch blocking
  `derived-extra` job entered it without any Python authority edit.
- narrowing acceptance: PASS. Exact identities are recovered from the
  protected historical deferred-audit reports and compared with the current
  workflow-derived set. Removing `golden` in a scratch workflow emitted
  `workflow-derived runner identity set narrowed relative to protected
  historical evidence`, accepted **0** executions, and exposed the removed
  `('golden', None)` identity. The current derived and protected sets are
  equal at seven identities.
- compatibility acceptance: PASS. `LEGACY_RUNNER_JOB_COUNTS` still governs
  reports admitted before exact identity matrices existed. Deferred-evidence
  re-derivation stayed green, and `./run verify-artifacts` validated all
  **101/101** pins and both protected databases byte-identically.
- test acceptance: PASS. The deferred-audit module passed **40/40** on Python
  3.11.4 and 3.12.13; the three required mutation tests passed on both.
  Complete shell passed **231/231** on both interpreters with **21/21** exact
  packages. The first sandboxed module run was a non-result only because
  macOS denied its on-site `ps` call; the permitted complete runs are the
  recorded results.
- matrix acceptance: PASS. `./run ci-local` remained **20/20**, with **125**
  workspace Rust tests, **48** net tests (**23 + 25**), zero
  rustc/clippy/fmt/ShellCheck failures, locked Rust 1.78 green,
  `invariant-scan` **10/10 rules / 18 controls**, and all protected evidence
  exact.
- golden-E2E delta: **0**. Matrix and mandatory standalone golden both remained
  **11/11** byte-identical.

### 2026-07-28 · STAGE-SOURCE — injectable stage scope derived

- runbook: `TASKS-v0.15-EXECUTION.md`
- owner: Codex
- commit: a806ede26047f995b098ab5f0f1dd1a6e6b6629f
- operator-decision acceptance: PASS. The operator authorized no observable
  rename. `apps/cored/src/main.rs` and `tools/benchmark_view.py` have no diff;
  every `x-intel-view-stage-*` header and stage string remains identical to
  v0.14.0. The **v0.14.1** release trigger fired; the active cycle remains
  v0.15.
- scope acceptance: PASS. Parsing the current Rust source derives exactly
  `analysis`, `response_build`, `sector_load`, and `serialization`. The test
  asserts that derived set is a subset of Python's 11-key
  `DIAGNOSTIC_HEADERS`, not equal to it. Seven header-only entries remain
  untouched: `handler_total`, `process_main_to_listener_ready`,
  `store_connection`, `store_cursor_migration`,
  `store_fingerprint_backfill`, `store_open`, and `store_schema_fts`.
- path-scope acceptance: PASS. Current code confirms that a cache hit returns
  before `compute_view_resp`; `sector_load`, `analysis`, and
  `response_build` therefore inject only on misses. `serialization` executes
  later in `into_response` and injects on both hits and misses.
- mechanism acceptance: PASS. The correspondence test reads both existing
  source files and needs no generated artifact or build step, so
  `benchmark_view.py` remains independently runnable. No four-name tuple was
  restated in Python.
- control acceptance: PASS. A scratch Rust rename emitted
  `apps/cored/src/main.rs:987: diagnostic_delay stage 'analysis_renamed' is
  absent from tools/benchmark_view.py:41: DIAGNOSTIC_HEADERS`. A Python map
  deletion also failed and named both files.
- correction acceptance: PASS. The active H1 row now distinguishes six
  blocking jobs from seven identities; H3 names all seven header-only entries;
  Step 7 names `candidate/v0.14.1`. No cycle artifact or closed runbook changed.
- test acceptance: PASS. The benchmark-view module passed **6/6** on Python
  3.11.4 and 3.12.13. Full shell passed **233/233** on both interpreters with
  **21/21** exact packages, a **+2** delta attributable to
  `test_rust_diagnostic_delay_stages_are_benchmark_headers` and
  `test_stage_correspondence_controls_name_both_files`.
- matrix acceptance: PASS. `./run ci-local` remained **20/20**, Rust remained
  **125** workspace / **48** net (**23 + 25**), zero
  rustc/clippy/fmt/ShellCheck failures, locked Rust 1.78 green,
  `invariant-scan` remained **10/10 rules / 18 controls**, and all **101/101**
  pins plus both protected databases remained exact.
- golden-E2E delta: **0**. Matrix and mandatory standalone golden both remained
  **11/11** byte-identical.
