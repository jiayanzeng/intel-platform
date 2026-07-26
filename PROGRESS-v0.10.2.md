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

### 2026-07-26 · RCPT-AUTH — CI-runner receipt contract authenticated

- owner: Codex
- commit: 2863d42ff31d5c964478bee1420df221d0dbab18
- result: PASS. The structural guard retains ancestry and now requires the
  exact released commit, case-insensitive `success`, and one
  `run_id`/`run_attempt` with job counts `core=1`, `golden=1`, `lint=1`,
  `msrv=1`, `net=1`, and `shell=2`.
- failure-capable controls: PASS. The fail-before run produced the expected
  seven failures / eight passes against the old guard and unattested
  workflow. Pass-after synthetic tests reject a hand-authored non-release
  ancestor, a failed conclusion, a partial matrix, and a two-run matrix; the
  complete seven-receipt release matrix promotes.
- authenticated tier: PASS as a wired, deliberately inert path. All seven
  workflow jobs emit workflow/repository/event/checkout identity; explicit
  `publish_evidence=true` signs each exact receipt and persists its bundle.
  Authenticated mode verifies subject bytes, expected repository and workflow
  signer, hosted-runner provenance, and exact released checkout. Missing and
  invalid bundle controls each reject all seven receipts. No hosted bundle
  was generated or accepted, so producer provenance remains unclaimed until
  PUBLISH.
- Python acceptance: PASS. The focused suite passed 18/18 with required
  process/loopback permission; its corpus-free subset passed 17/17 under both
  Python 3.11.4 and 3.12.13. Both full shell lanes passed 145/145 with the
  pre-existing single Starlette deprecation warning.
- workflow acceptance: PASS. The workflow parsed as YAML, contains seven
  receipt emit/upload paths and seven conditional build-provenance actions,
  and `git diff --check` passed.
- golden-E2E delta: none. `./run golden` passed 11/11 with every named corpus,
  duplicate, signal, rerun, entitlement, citation, snippet, and auth anchor
  unchanged.
- protected artifact delta: none. Both protected databases matched 2/2 and
  both v0.10.1 evidence reports printed `PIN MATCH`.

### 2026-07-26 · SUBJ-ENFORCE — production audit subject made mandatory

- owner: Codex
- commit: 1c91c645750f102dc93af33722c0cdaf0ee4ee7f
- result: PASS. Production audit creation requires `--expected-head`, resolves
  the subject HEAD, requires exact equality, and requires
  `git status --porcelain=v1` to be empty before calling any measurement. The
  validated SHA is the released-commit input to RCPT-AUTH.
- failure-capable controls: PASS. Three fail-before tests failed 3/3 because
  the old `run_production` did not accept an expected-head contract.
  Pass-after instrumentation proves wrong HEAD and dirty tracked state each
  abort before the measurement function and leave no report, while a clean
  matching repository proceeds and writes its receipt.
- invocation acceptance: PASS. The direct production CLI rejects a missing
  `--expected-head`. `./run audit-deferred --output ...` defaults to immutable
  release `e5af6bc5df8261cc004bd4d3247b70f8cbe930bb`; the exercised wrapper
  rejected current pre-release HEAD
  `170f471cab6c0b198a7254cc495b95efe0c71d2a`, wrote no output, and checked
  protected evidence before and after.
- Python acceptance: PASS. The corpus-free deferred-audit subset passed 22/22
  under Python 3.11.4 and 3.12.13. Both full shell lanes passed 150/150 with
  the pre-existing single Starlette deprecation warning.
- source acceptance: PASS. Python compilation, `bash -n run`, and
  `git diff --check` passed. Measurement content did not change.
- golden-E2E delta: none. `./run golden` passed 11/11 with every named anchor
  unchanged.
- protected artifact delta: none. Both protected databases matched 2/2 and
  both v0.10.1 evidence reports printed `PIN MATCH`.

### 2026-07-26 · RESUME-STRICT — resumed adversarial cells validated

- owner: Codex
- commit: fc8f3fb1d2d9ceb5b4735cb44e3e4721f0bb1b9a
- result: PASS. Resume accepts only a full fresh-completion schema with
  HTTP 200, true completion/context/valid flags, internally consistent target
  context, typed outcome/overlap/list fields, and complete non-negative
  retry/8/12/16-token telemetry.
- failure-capable controls: PASS. Fail-before was three failures / one pass:
  the old predicate reused the contradictory HTTP-502 cell and the
  schema-incomplete cell and did not halt on a synthetic resumed `LEAK`; the
  already-complete cell remained reusable. Pass-after was 4/4: invalid cells
  retry, the valid cell is reused byte-for-byte, and the leak records
  target/shape then raises immediately.
- protected-report compatibility: PASS. A direct schema census accepted all
  45/45 committed completed attempts. The synthetic leak was a control, not a
  protected-evidence finding; the pinned report remains zero `LEAK`.
- Python acceptance: PASS. The focused verifier suite passed 23/23. Both full
  shell lanes passed 153/153 under Python 3.11.4 and 3.12.13 with the
  pre-existing single Starlette deprecation warning.
- source acceptance: PASS. Python compilation and `git diff --check` passed;
  only the verifier harness and its tests changed outside task records.
- golden-E2E delta: none. `./run golden` passed 11/11 with every named anchor
  unchanged.
- protected artifact delta: none. Both protected databases matched 2/2 and
  both v0.10.1 evidence reports printed `PIN MATCH`.
