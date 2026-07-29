# PROGRESS-v0.23.md — append-only execution record

This file records v0.23 task and gate events after their implementation
commits exist. Each entry names the measured result, every applicable
acceptance criterion, the golden delta, and the real implementation commit.
Entries are append-only; corrections are new dated entries.

### 2026-07-29 · ACTIVATE — v0.23 admitted with one validation defect

- owner: Codex
- commit: 09cb119
- result: FAIL at the first post-commit `cycle-check`; the committed
  `Manifest retention/indexing` deferral row said `re-measure only` without
  assigning that non-none action to a named Step N. The failure was preserved
  and corrected forward rather than amended.
- worktree acceptance: PASS. Before activation the only worktree item was the
  operator-supplied untracked `docs/cycles/TASKS-v0.23-EXECUTION.md`.
  Implementation commit `09cb119` contains only that runbook, the `AGENTS.md`
  v0.23 declaration, and this progress-log skeleton.
- entering-ref acceptance: PASS. Before activation, local `main` was
  `c9e3394df927aa56f45e2a5205555130717f5f83`, one commit ahead of measured
  remote `main` `15b6d28973058c833a77e9600741d29eda02cdc1`. Annotated tag
  object `47c5b314acd6f7fb42bba2f90312bf1185277c5c` peeled to that same remote
  closing commit. No ref changed.
- lifecycle acceptance: FAIL for `cycle-check` with the exact defect above;
  `checklist-audit` independently passed **177/177** with the same three
  retractions and zero exemptions. `progress-check` correctly reported that
  the new skeleton had no dated entry before this audit record existed.
- test acceptance: NOT RUN at this preparatory checkpoint; E0 owns the complete
  entering matrix and drafted-gate measurements.
- golden-E2E delta: NOT MEASURED; no claim.
- protected artifact delta: NOT MEASURED; no protected or pinned file changed.

### 2026-07-29 · ACTIVATE-CORRECTION — deferral assignment made executable

- owner: Codex
- commit: 88590f6
- result: PASS. A dated `Runbook amendments` entry preserves the activation
  defect, and the manifest-retention action now names Step 1 as its discharging
  step. No Step objective, gate, acceptance criterion, or done condition
  changed.
- runbook-validity acceptance: PASS. `./run cycle-check` reports active v0.23
  open with twenty closed execution runbooks and three historical runbooks.
- scope acceptance: PASS. The correction changes only this active runbook, a
  standing status path. It does not change `STATE.md`, workflow, source,
  dependency, schema, protected artifact, public surface, or any ref.
- golden-E2E delta: NOT MEASURED; no claim.

### 2026-07-29 · E0 — entering state and six gates measured

- owner: Codex
- commit: 6c2d0d8
- result: PASS. The implementation commit changes only the active runbook's E0
  execution record and checklist box. The first post-status `cycle-check`
  correctly rejected an execution record placed inside Step 1's committed
  `Done when` region; moving the record behind a section boundary restored the
  committed Step text without amending any objective, gate, acceptance
  criterion, or done condition.
- entering-matrix acceptance: PASS. Clean constrained Python **3.11.4** and
  **3.12.13** rebuilds resolved the same **21** packages and each passed shell
  **266/266** with the same one third-party warning. A permitted
  `./run ci-local` passed **20/20** with **133** workspace tests, **55** net
  tests (**29 + 26**), warning-denied current and locked Rust 1.78 lanes, clean
  clippy/fmt/ShellCheck, **12/12 rules / 36 controls**, **221/221** pins,
  protected databases **2/2**, and embedded golden **11/11**. The earlier
  sandbox loopback denial was recorded as a non-result. Standalone
  `export-check` passed **90** derived sources, **7** required paths, and
  **153** exported paths after its sandbox DNS non-result.
- G1 acceptance: PASS at measured **P2**. In a disposable clone of the local
  repository, forcing the recorded `v0.15.6` identity onto release parent
  `a83db73…` made `cycle-check` exit **1** with all four parent/tree agreement
  defects over both the closed runbook and `STATE.md`. The checker demonstrably
  read the constructed tag; the clone was deleted and working refs remained
  byte-identical.
- G2/G3 acceptance: PASS from primary sources read 2026-07-29. The Node 24
  migrations are checkout **v5**, upload-artifact **v6**, and setup-python
  **v6**; current rust-cache v2 and attest-build-provenance v4 resolve to Node
  24 implementations, while rust-toolchain is composite. Floating
  `dtolnay/rust-toolchain@master` resolved to
  `2c7215f132e9ebf062739d9130488b56d53c060c`, dated
  **2026-07-16T09:35:07-07:00**; all **6/6** uses precede attestation.
- G4 acceptance: PASS. The scope grep returned zero lines; all **17** release
  authorities were enumerated without an undefined entry-point count. v0.22's
  literal no-`apps/` contradiction was reproduced from its prohibition and
  release commit's `apps/cored/Cargo.toml` change; the separate `Cargo.lock`
  nuance is recorded.
- G5 acceptance: PASS. Three event triggers were freshly evaluated: manifest
  **127,982 bytes**, verification **0.10 s / 0.09 s**, not fired; shell
  **266/266** in both lanes with one warning and no relevant constraint refresh,
  not fired; Node migration, still fired. The refuted no-trigger row is
  explicitly out of scope, and both promoted obligations were rechecked.
- G6 acceptance: PASS. Reproducible criteria produce **4** checker-reporting
  members and **4** unsatisfiable author-side members with exact overlap **2**.
  Every member is cited to its closed runbook/progress section and classified
  by actual discovery site; the record does not claim they were all found by a
  checker.
- identity/scope acceptance: PASS. Local and remote annotated `v0.15.6` object
  `47c5b314…` peel to closing commit `15b6d289…`, whose first parent is release
  parent `a83db73…`; all **221/221** pins and protected databases **2/2**
  re-verified. `.github/workflows/ci.yml` and `STATE.md` remained entering blobs
  `96e85af9…` and `e36cdc67…`; no working ref changed.
- lifecycle acceptance: PASS after the implementation commit.
  `cycle-check`, `progress-check`, `version-check`, and `invariant-scan` were
  green. The expected pre-audit `checklist-audit` refusal named only E0's
  not-yet-appended progress entry.
- golden-E2E delta: **0**. The first sandboxed post-status run was a loopback
  permission non-result; the identical permitted run passed **11/11**.
