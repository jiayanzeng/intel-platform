# PROGRESS-v0.24.md — append-only execution record

This file records v0.24 task and gate events after their implementation
commits exist. Each entry names the measured result, every applicable
acceptance criterion, the golden delta, and the real implementation commit.
Entries are append-only; corrections are new dated entries.

### 2026-07-29 · ACTIVATE — v0.24 admitted with three validation defects

- owner: Codex
- commit: 46a44b2
- result: FAIL at the first post-commit `cycle-check`. The committed
  declared-scope block used YAML rather than the required Markdown table;
  `Manifest retention/indexing` said `re-measure only` without assigning the
  action to a named Step N; and Step 6's acceptance criterion cited the
  invariant-count increase from Step 3 instead of stating the same-commit
  relation.
- worktree acceptance: PASS. Before activation the only worktree item was the
  operator-supplied untracked
  `docs/cycles/TASKS-v0.24-EXECUTION.md`. Implementation commit `46a44b2`
  contains only that runbook, the `AGENTS.md` v0.24 declaration, and this
  progress-log skeleton.
- entering-ref acceptance: PASS. Before activation, HEAD was the unamended
  post-closing audit
  `ed54112ae69fd990bdbb0ae705e2671fb31678a4`. Read-only remote inspection
  resolved `main` and peeled `v0.15.7` to closing commit
  `e7715fb97b86b91a2a58bc7b73bf99308c2aae9b`, with annotated tag object
  `b579c2c18e4eeb549617ea20a9175b0c26dc621d`. Local `main` remained
  `eb2d9df8b3ffd3e0380d506e958fb5a3adb2d42e`; no ref changed.
- lifecycle acceptance: FAIL for `cycle-check` with the exact three defects
  above. `checklist-audit` independently passed **184 checked / 3 retracted /
  184 matched / 0 exemptions**. `progress-check` correctly reported that the
  new skeleton had no dated entry before this audit record existed.
- scope acceptance: NOT MEASURED at activation. The static sub-rule could not
  evaluate a declared scope because the committed block did not use its
  accepted schema; an exit 1 on that unparsed construction is not a successful
  firing.
- test acceptance: NOT RUN at this preparatory checkpoint; E0 owns the complete
  entering matrix and drafted-gate measurements.
- golden-E2E delta: NOT MEASURED; no claim.
- protected artifact delta: NOT MEASURED; no protected or pinned file changed.

### 2026-07-29 · ACTIVATE-CORRECTION — live contract made valid

- owner: Codex
- commit: 6c5ca4c
- result: PASS. The active runbook carries a dated amendment and now uses the
  checker's Markdown declared-scope table, assigns manifest re-measurement to
  Step 1, and states Step 6's invariant-count acceptance as a same-candidate
  relation with the population-equivalence rule executing.
- scope acceptance: PASS. `./run cycle-check` accepts the `release` intent and
  all declared release-authority coverage. The Python forbid is
  `shell/intel_shell/[a-z]*.py`, leaving
  `shell/intel_shell/app.py` as the sole release-authority overlap described by
  the runbook.
- amendment acceptance: PASS. The machine-readable
  `Step 6 — … — 2026-07-29` disclosure matches the one changed acceptance
  block; `cycle-check` reports no undisclosed objective, acceptance, or
  done-condition edit.
- lifecycle acceptance: PASS. `cycle-check` reports active v0.24 open with
  twenty-one closed execution runbooks and three historical runbooks;
  `checklist-audit` passes **184 checked / 3 retracted / 184 matched / 0
  exemptions**; `progress-check` passes at the preceding ACTIVATE record.
- scope delta: only the active runbook changed. No source, workflow, tool,
  dependency, schema, protected artifact, public surface, or ref changed.
- golden-E2E delta: NOT MEASURED; no claim.

### 2026-07-29 · E0 — entering state rebuilt and six gates settled

- owner: Codex
- commit: 4b08552
- result: PASS. The implementation commit changes only the active runbook,
  records the complete measured E0 result, and checks E0. `STATE.md`, `run`,
  and `.github/workflows/ci.yml` remain unedited.
- entering-matrix acceptance: PASS after two classified environment
  non-results. Empty Python 3.11.4 and 3.12.13 environments each resolved 21
  constrained packages and collected 275, passed 275, and skipped 0 shell
  tests; both skip sets were empty. The permitted `./run ci-local` passed all
  20 jobs with 133 workspace tests, 55 net tests (29 ingest + 26 cored),
  warning-denied current and Rust 1.78 lanes, clean
  clippy/fmt/ShellCheck, `invariant-scan` 12/12 rules / 38 controls, all 236
  pins, protected databases 2/2, and embedded golden 11/11. Standalone golden
  passed 11/11. The first sandboxed matrix loopback-bind failure and first
  sandboxed export DNS failure were non-results; the identical permitted
  commands passed.
- standalone acceptance: PASS. `cycle-check`, `progress-check`,
  `version-check`, `invariant-scan`, manifest validation, and project-root
  `export-check` passed. `checklist-audit` passed before E0 was checked and,
  after the implementation commit but before this required append existed,
  correctly named E0 as the sole unmatched checked task.
- G1 acceptance: CONFIRMED. The suite contains one `skipif`, zero
  `pytest.skip(` calls, zero pytest configuration files, and no structured
  report producer or consumer. The one conditional node and its
  protected-corpora-and-built-`cored` reason are named in the runbook record.
- G2 acceptance: CONFIRMED. Grep reproduced v0.19's on-site-skip clause and its
  absence from v0.21, v0.22, and v0.23. The record places v0.22's honest
  266-collected / 265-passed / 1-skipped hosted result beside v0.23's false
  275-collected / 275-passed / 0-skipped hosted claim and measured
  275-collected / 274-passed / 1-skipped result.
- G3 acceptance: CONFIRMED and exactly bounded. Commit `edd77a4` introduced the
  conditional test during v0.10.1. All seventeen applicable retained
  RE-MEASURE and POST-PUSH run logs were read, with no retention gap. The exact
  affected set contains one progress record: v0.23 RE-MEASURE for hosted run
  `30459746825`, plus the same copied false number in the closed execution
  record. The v0.23 POST-PUSH entry for run `30462710258` already supersedes
  it with 275 collected / 274 passed / 1 named on-site skip.
- G4 acceptance: answered after stating the criterion. The three existing
  retractions concern later-falsified product/invariant or task-acceptance
  properties of resolved checked tasks, with explicit operator acceptance and
  correction. Repository practice uses a dated superseding append for an
  incorrect progress measurement. Applying that distinction leaves the count
  at three, subject to Step 4's named operator decision.
- G5 acceptance: CONFIRMED after the preserved activation defect. The original
  YAML construction was not parsed and therefore not measured. Correction
  commit `6c5ca4c` passed the live release intent with all 17 release
  authorities covered and one declared authority/forbid overlap. Two focused
  tests passed: a missing-authority construction was detected and the current
  population/overlap was verified.
- G6 acceptance: CONFIRMED. Both clean local lanes named the sole warning as
  `starlette.testclient.StarletteDeprecationWarning` for the deprecated
  Starlette `httpx` path. It is the accepted warning; neither its error/failure
  nor dependency-refresh trigger fired.
- retention acceptance: PASS. The manifest is 136,625 bytes. Consecutive full
  verifications took 0.10 s and 0.09 s and matched all 236 pins and protected
  databases 2/2, so neither retention threshold fired.
- published-object/ref acceptance: PASS. Annotated object `b579c2c1…` peels
  locally and remotely to closing commit `e7715fb9…`, whose first parent is
  release parent `8bb6a714…`; remote `main` remains at the closing commit.
  No auxiliary working-repository ref was created, moved, or deleted during
  E0.
- golden-E2E delta: **0**. The post-record standalone invocation passed
  **11/11**.

### 2026-07-29 · POPULATION-EXPLICIT — conditional set named and reported

- owner: Codex
- commit: df92e4b
- result: PASS. The sole environment-conditional shell test now carries the
  registered `on_site` marker alongside its unchanged `skipif`, and both
  unchanged full-suite command shapes emit one stable JSON population summary.
- marker/enumeration acceptance: PASS.
  `pytest shell/tests --collect-only -m on_site -q` enumerated exactly
  `tests/test_deferred_audit.py::test_on_site_production_measurements_match_committed_receipt`.
  The marker declares membership while the existing condition still decides
  execution.
- machine-summary acceptance: PASS. The sorted schema reports
  `schema_version`, collected, passed, failed, the full `on_site` node set, and
  each skip's node id, marker set, and reason. The targeted hosted test command
  emits no second summary; the local and hosted full-suite invocations obtain
  the same option from `shell/pytest.ini`.
- population-preservation acceptance: PASS. Local Python 3.11.4 and 3.12.13
  each collected **275**, passed **275**, failed **0**, and skipped **0**. A
  disposable clean checkout under each interpreter collected **275**, passed
  **274**, failed **0**, and skipped **1**. That skip is the enumerated node,
  marked `on_site` and `skipif`, for
  `on-site production audit requires protected corpora and built cored`.
  These populations and outcomes equal E0's before-state measurements.
- command-shape/pin acceptance: PASS. An initial explicit-option construction
  was rejected by the authorization pin and R10 classifier. The accepted
  construction preserves both `pytest shell/tests -q` commands. `run` changes
  by one explanatory comment only, from SHA-256
  `0fc7f0be0ea2d8c68ff63be55dd0b73cc1385ce966b8307506a5387543f18779`
  at **43,044 bytes** to
  `44314ddfc182de68d4aaa444f2c6bd074fe08858d8d46f98aafa461dd6672397`
  at **43,125 bytes**; its dispatch, authorization policy, and model-profile
  functions are unchanged.
- full acceptance: PASS. `./run ci-local` passed all **20** jobs with workspace
  **133**, net **55** (**29 + 26**), warning-denied current and Rust 1.78 lanes,
  clean clippy/fmt/ShellCheck, `invariant-scan` **12 rules / 38 controls**, all
  **236** pins, protected databases **2**, and embedded golden **11 checks**.
  Manifest validation, `verify-artifacts`, `cycle-check`, ShellCheck, and diff
  checks passed. The pre-audit `checklist-audit` correctly named this checked
  task as its sole unmatched progress entry.
- scope acceptance: PASS. The implementation changes only `STATE.md`,
  `config/protected-artifacts.json`, the active runbook, `run`,
  `shell/pytest.ini`, `shell/tests/conftest.py`, and the one marked test.
  `.github/workflows/ci.yml`, runtime source, dependencies, schemas, protected
  databases, configured sources, public surfaces, and refs are unchanged.
- golden-E2E delta: **0**. The mandatory post-record standalone execution
  passed all **11** checks.
