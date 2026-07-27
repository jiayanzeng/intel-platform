# PROGRESS-v0.14.md — append-only execution record

This file records v0.14 task and gate events after their implementation
commits exist. Each entry names the measured result, every applicable
acceptance criterion, the golden delta, and the real implementation commit.
Entries are append-only; corrections are new dated entries.

### 2026-07-28 · E0-GATE — remote reconciled and v0.14 admitted

- owner: Codex
- commit: b078252c378ca18c65670bae0a3d6d6e0529be09
- result: PASS for cycle activation only; E0 remains unchecked. The operator
  selected pre-cycle option (a) and manually pushed the two v0.13 append-only
  audit commits. Read-only verification found local `main` and `origin/main`
  aligned (zero ahead / zero behind) at
  `0eff6e4c4987b7ebb138cf0bb1da6ebe8bd851b9`, described as
  `v0.13.0-2-g0eff6e4`. The only worktree entry was the operator-supplied
  untracked `TASKS-v0.14-EXECUTION.md`.
- published-tag acceptance: PASS. Annotated `v0.13.0` remains tag object
  `24a6a2aca52974891d120e0f2b295a93d629c1f7`, dereferencing exactly to release
  commit `5ecd42bb6ca44f1588e53e493c67fee17d071b09`.
- activation acceptance: PASS. Implementation commit
  `b078252c378ca18c65670bae0a3d6d6e0529be09` committed only the supplied
  runbook, the `AGENTS.md` v0.14 declaration, and the empty append-only
  progress log.
- lifecycle acceptance: PASS. `./run cycle-check` reports active v0.14 open
  with eleven closed execution runbooks. `./run checklist-audit` resolves the
  entering **111/111** checked tasks, reports the three existing retractions
  separately, and finds zero exemptions. `git diff --check` passed.
- test acceptance: NOT RUN at this preparatory checkpoint; E0 owns the full
  entering matrix and G1–G6 reproduction.
- golden-E2E delta: NOT MEASURED; no claim.
- protected artifact delta: NOT MEASURED; no protected or pinned file was
  touched.

### 2026-07-28 · E0 — entering state rebuilt and G1–G6 measured

- runbook: `TASKS-v0.14-EXECUTION.md`
- owner: Codex
- commit: 6193a12d093e5e67c01f51fcdd6832a465aa1dd7
- result: PASS. After invalidating stale Rust artifacts that embedded a deleted
  v0.13 scratch-worktree path, the permitted clean-cache `./run ci-local`
  passed **20/20** with **124** workspace Rust tests, **47** net tests
  (**23** `intel-ingest` + **24** `cored`), zero rustc/clippy/fmt/ShellCheck
  failures, locked Rust 1.78 green, protected databases **2/2**, all **86/86**
  pins, and golden **11/11**. The clean matrix's shell lane passed **215** and
  skipped its deliberately on-site-only test because golden had not yet built
  `target/debug/cored`; standalone Python 3.11.4 and 3.12.13 then each passed
  the full **216/216** and verified **21/21** exact packages.
- G1 acceptance: PASS. Separate scratch worktrees made R7 control 2 fail at
  `apps/cored/src/main.rs:1135` and control 3 fail at line 1182, while their
  self-test summaries remained byte-identical. A third scratch tree used a
  shortened, mis-broad R7 matcher; its control still returned status 1 with the
  expected substring while also blaming unrelated safe hydration calls at
  lines 1182 and 1290.
- G2 acceptance: PASS with four recorded mutation outcomes. A renamed
  production threshold seam made R1 PASS; an unknown inference-gateway form
  made R3 PASS; an unknown credential form made R4 PASS; and identically
  renamed authority markers made R6 FAIL in both governed files.
- G3/G4/G5 acceptance: PASS. Identity construction is statement-order-only
  before the listener bind; v0.13's release-commit re-measure action names no
  discharging step; and both diagnostic-delay variables are absent from every
  named operator-facing document while remaining active at four `/view`
  stages.
- G6 acceptance: PASS as a guard gap, not a live defect. The locked release
  build succeeded and `test_clear_fingerprint` was absent from both its symbol
  table and binary strings; no current rule protects the dev-dependency
  placement that makes this true.
- published-baseline acceptance: PASS. Annotated `v0.13.0` remains object
  `24a6a2aca52974891d120e0f2b295a93d629c1f7`, peeling to release commit
  `5ecd42bb6ca44f1588e53e493c67fee17d071b09`; all **86** pins and both
  protected databases re-verified exact.
- golden-E2E delta: **0**. The mandatory post-task standalone run remained
  **11/11** byte-identical.
- cleanup: all seven disposable mutation worktrees were removed; the live tree
  contained only the E0 state/runbook change before its implementation commit.

### 2026-07-28 · CONTROL-PRECISION — controls prove their failure site

- runbook: `TASKS-v0.14-EXECUTION.md`
- owner: Codex
- commit: 970b717f380b932e96fab6687ac09e38b6eb3413
- result: PASS. Registry schema 3 gives every one of the **11** controls a
  message-only `expected_fail` plus explicit `expected_file` and
  `expected_line`. Loading refuses unsafe paths, a file other than the mutated
  file, and non-positive line values. Self-test acceptance now requires one
  complete finding that associates the rule, exact file, exact line, and
  message.
- site acceptance: PASS. R7 control 2 now reports
  `apps/cored/src/main.rs:1135`; control 3 reports line 1182. R6's full-prefix
  exception was normalized to a message and its unchanged mismatch result now
  reports the first differing block line,
  `intel-platform-OPERATIONS.md:407`.
- negative meta-control acceptance: PASS. A deliberately mis-broad R7 matcher
  still exited 1 and emitted the legacy message for unrelated safe scoped calls
  at lines 1182 and 1290, but did not emit the expected mutated site at line
  1135. The site assertion therefore rejected it. The mutation was in-memory
  only and the real **7/7 rules / 11 controls** self-test passed immediately
  afterward.
- shell acceptance: PASS. The focused invariant module passed **13/13**,
  including the explicit wrong-site and over-broad controls. The full shell
  suite passed **218/218** under both Python 3.11.4 and 3.12.13; both
  interpreters verified **21/21** exact packages.
- preservation acceptance: PASS. No R1–R7 matching logic or source under
  `crates/` or `apps/` changed; R6 gained failure-location reporting only.
  `./run ci-local` remained **20/20** with **124** workspace Rust tests,
  **47** net tests, warning/lint/MSRV gates green, all **86** pins exact, and
  both protected databases exact.
- golden-E2E delta: **0**. The matrix and mandatory standalone run both
  remained **11/11** byte-identical.
