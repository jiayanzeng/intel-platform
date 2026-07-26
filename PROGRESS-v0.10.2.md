# PROGRESS-v0.10.2.md — append-only execution record

This file records v0.10.2 task and gate events after their implementation
commits exist. Each entry names the measured result, every applicable
acceptance criterion, the golden delta, and the real implementation commit.
Entries are append-only; corrections are new dated entries.

### 2026-07-26 · E0-GATE — supplied runbook admitted before baseline restart

- owner: Codex
- commit: c0b2856fea45b576c63e4b6507e4bf9e277fe145
- result: BLOCKED, then corrected without claiming E0 complete. The read-only
  opener found only the operator-supplied untracked
  `TASKS-v0.10.2-EXECUTION.md`; `AGENTS.md` still correctly declared the
  latest closed cycle, v0.10.1.
- identity evidence: entering HEAD was
  `384662d673a33a6f181358304bb5daed08eac0fc`
  (`v0.10.1-1-g384662d`), local `main` was 12 ahead / 0 behind
  `origin/main` at `5bcabcb870a906b0b830bf3c8c391bbe3ced71b0`, and annotated
  tag object `8ded63f79ed12b4180e8bcd0bcff4ef30a080a79` dereferenced
  exactly to `e5af6bc5df8261cc004bd4d3247b70f8cbe930bb`.
- correction: committed the reviewed runbook, declared v0.10.2 active, created
  this progress log, distinguished structural receipt validation from
  authenticated producer evidence, and corrected PUBLISH so the hardened
  workflow is available before it audits the immutable v0.10.1 checkout.
- lifecycle acceptance: `./run cycle-check` passed with active v0.10.2 and six
  closed execution runbooks. `./run checklist-audit` resolved the entering
  62/62 checked tasks with zero exemptions.
- test acceptance: NOT RUN at this gate checkpoint. E0 remains unchecked and
  restarts from the clean post-audit tree.
- golden-E2E delta: NOT MEASURED; no claim.
- protected artifact delta: NOT MEASURED; no protected file was touched.

### 2026-07-26 · E0 — entering state rebuilt and F1–F4 confirmed

- owner: Codex
- commit: c3be9465b87c3e3a74e2c740b0e430d377a332fb
- result: PASS after the separately recorded cycle-activation correction.
  Clean HEAD `9d5b08ece5447648c09073987b520dccb17d8fcf` was
  `v0.10.1-3-g9d5b08e`; annotated v0.10.1 still dereferenced to release
  commit `e5af6bc5df8261cc004bd4d3247b70f8cbe930bb`. The approved
  activation pair explains local `main` being 14 ahead / 0 behind
  `origin/main` at `5bcabcb870a906b0b830bf3c8c391bbe3ced71b0`.
- baseline acceptance: PASS. The permitted `./run ci-local` rerun passed
  19/19 with 99 workspace tests, 20 net tests, warning-denied builds,
  clippy/fmt, Rust 1.78 check/tests, 138 Python 3.11 shell tests, golden 11/11,
  protected artifacts 2/2, both evidence pins, fingerprints, and lifecycle
  auditors. The sandboxed eight-control permission failure is an environment
  non-result.
- Python acceptance: PASS. The independent Python 3.12.13 lane passed
  138/138, and both interpreter lanes matched 21/21 exact packages.
- defect acceptance: PASS. F1 accepts on field format plus ancestry and does
  not enforce exact release SHA, success, complete single-run matrix, or
  provenance. F2 has no dirty/expected-HEAD precondition. F3 trusts
  completion flags without HTTP/schema validation and does not halt on resumed
  `LEAK`. F4 has four stale v0.10 task/progress literals in `AGENTS.md`.
- receipt census: seven committed accepted rows, all at
  `45fa3d49860643fdb2595d82340e364d33566e7d`, all `success`, all
  `run_id=30187058897`; E0 confirmed these happen to agree but are not
  enforced.
- lifecycle acceptance: PASS. Standalone `version-check`, `cycle-check`, and
  `checklist-audit` passed; the latter resolved the entering 62/62 checked
  tasks with zero exemptions.
- golden-E2E delta: none. Standalone `./run golden` passed 11/11 with every
  exact anchor unchanged.
- protected artifact delta: none. Both protected databases matched 2/2 and
  both v0.10.1 evidence reports printed `PIN MATCH`.
