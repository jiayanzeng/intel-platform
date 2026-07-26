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

### 2026-07-26 · AGENTS-NEUTRAL — cycle-specific workflow paths eliminated

- owner: Codex
- commit: 110b2b4099052347ff04ed9367aa4352fd3eb0d3
- result: PASS. The four stale v0.10 task/progress literals now resolve through
  the single active-cycle declaration. The only concrete literals left are the
  declared active `TASKS-v0.10.2-EXECUTION.md` and
  `PROGRESS-v0.10.2.md`, both before §0; §§0–4 retain their meanings.
- failure-capable control: PASS. Fail-before was one pass / one failure because
  the old checker accepted a clean scratch contract and also accepted a
  planted stale `PROGRESS-v1.2.md`. Pass-after was 2/2: the clean scratch root
  passes, while the stale path returns failure and names its `AGENTS.md` line.
- lifecycle acceptance: PASS. Actual `./run cycle-check` reports v0.10.2 open,
  six closed execution runbooks, and three historical task documents.
- Python acceptance: PASS. Both full shell lanes passed 155/155 under Python
  3.11.4 and 3.12.13 with the pre-existing single Starlette deprecation
  warning.
- source acceptance: PASS. Python compilation, literal census, and
  `git diff --check` passed. No product path or invariant changed.
- golden-E2E delta: none. `./run golden` passed 11/11 with every named anchor
  unchanged.
- protected artifact delta: none. Both protected databases matched 2/2 and
  both v0.10.1 evidence reports printed `PIN MATCH`.

### 2026-07-26 · PUBLISH — v0.10.1 published and hosted evidence authenticated

- owner: Codex
- commit: 1f04094f490386f655362523aaab7eb6fdd2ed9d
- authorization/result: PASS. The operator explicitly authorized publication.
  Remote `main` is reviewed Step 5 audit record
  `817e7f3e7c1878c18f474532df4d50c2b17fcbdc`; remote annotated tag object
  `8ded63f79ed12b4180e8bcd0bcff4ef30a080a79` remains unchanged and
  dereferences to v0.10.1 release
  `e5af6bc5df8261cc004bd4d3247b70f8cbe930bb`.
- failure-capable control: PASS. Temporary commit
  `7c41fca18aa2845f8f7e1b2cb196ff706975e6c7` planted only shell version
  `9.9.9`. Hosted run 30194605219 failed both shell version checks while the
  other five executed nodes passed. Seven receipts persisted; RCPT-AUTH
  rejected the two `conclusion:"failure"` shell receipts and accepted zero
  executions. The remote/local branch and temporary worktree were deleted.
- hosted acceptance: PASS. Workflow-dispatch run 30194678764 used definition
  head `817e7f3e7c1878c18f474532df4d50c2b17fcbdc`, checked out exact release
  `e5af6bc5df8261cc004bd4d3247b70f8cbe930bb`, and passed core, golden, lint,
  MSRV, net, and both Python shell legs. All seven receipt, attestation,
  bundle-persistence, and upload steps passed under run attempt 1.
- authentication acceptance: PASS after one measured integration correction.
  The sandbox trust-initialization attempt and the first permitted
  extension-incompatible attempt both accepted zero. Presenting unchanged
  persisted `.sigstore` bytes under an ephemeral `.jsonl` verifier name then
  authenticated 7/7 subject digests, repository, workflow signer, and
  hosted-runner identity with zero rejection. The adapter has an offline
  byte/cleanup regression test.
- receipt acceptance: PASS. A clean detached v0.10.1 worktree produced five
  deferred / two promoted, exact-cosine p95 8.962542 ms at 2,600 documents,
  seven accepted authenticated receipts, zero rejected, and one complete
  run-id/attempt matrix.
- pin acceptance: PASS.
  `evidence/v0.10.2/deferred-audit/report.json` is 28,968 bytes at SHA-256
  `4e11a8b3a3a64b5519469289f5cdf246bf13a0045954aa22c38703bbe6d29d9b`.
  Manifest validation reports schema 2, two protected artifacts, and three
  pinned files; no host path or secret pattern appears in the report.
- Python acceptance: PASS. Both current shell lanes passed 156/156 under
  Python 3.11.4 and 3.12.13 with the pre-existing single Starlette
  deprecation warning.
- golden-E2E delta: none. Final `./run golden` passed 11/11 with every named
  anchor unchanged.
- protected artifact delta: none. Both protected databases matched 2/2 and all
  three evidence reports printed `PIN MATCH`. Temporary protected-database
  copies were removed with the detached worktree; originals did not change.

### 2026-07-26 · R-CLOSE — v0.10.2 release identity created

- owner: Codex
- commit: 7d127abac0b993c9e98294ee1c03ff01153de9d0
- result: PASS. The operator approved v0.10.2 because the cycle hardens
  workflow provenance, evidence authentication and subject checks,
  adversarial resume validation, and cycle-lifecycle enforcement. It changes
  no public or internal API behavior, runtime behavior, storage path, database
  schema, cache representation, licensing outcome, dependency, or retrieval
  output, so the patch disposition accurately describes the delta.
- release identity: PASS. `v0.10.2` is annotated tag object
  `d821f8b2eb6f39fe4a7d06a88cd61de771c7b0ba`, which dereferences exactly to
  release commit `7d127abac0b993c9e98294ee1c03ff01153de9d0`. The annotation is
  `intel-platform v0.10.2`; this later audit record does not move the tag.
- release gate: PASS. The committed fresh real-model report contains 45/45
  target-valid/model-completed cells, `NOT EXERCISED` 45, and `LEAK` 0. The
  separate deployed-handler positive control is `GUARD FIRED`. Resume now
  revalidates the complete HTTP-200 schema and halts on a reused `LEAK`.
- diff inventory: PASS. All 21 paths in `v0.10.1..v0.10.2` are classified
  exactly once in `STATE.md`: five public/release metadata, two operations and
  workflow, eight executable evidence/controls, six documentation/task
  metadata, and zero runtime/storage/internal-API paths.
- version authorities: PASS. Rust package, Python package, FastAPI literal,
  `STATE.md`, and newest changelog heading all read 0.10.2. Cargo mechanically
  changed only the `cored` package version in `Cargo.lock`; no dependency
  resolution moved.
- publication outcome: PASS. PUBLISH advanced remote `main` only through
  reviewed Step 5 audit `817e7f3e7c1878c18f474532df4d50c2b17fcbdc`
  and published the unchanged immutable v0.10.1 tag. Hosted run 30194678764
  passed the complete seven-job matrix; the pinned production audit
  authenticated 7/7 receipts with zero rejection and recorded two promoted /
  five deferred rows. No v0.10.2 push is authorized.
- candidate acceptance: PASS. Before the release commit, `./run ci-local`
  passed 19/19 with 99 workspace tests, 20 net tests, warning-denied builds,
  clippy/fmt, Rust 1.78 locked check/tests, 156 Python 3.11 shell tests, golden
  11/11, protected artifacts 2/2, three matching pins, and lifecycle auditors.
  The independent Python 3.12.13 lane passed 156/156 and verified 21/21 exact
  packages. Standalone manifest validation, protected verification, golden,
  version-check, and `git diff --check` passed.
- golden-E2E delta: none. Both candidate golden runs passed 11/11 with the
  exact 13 → 12 corpus, hamming-12 near-duplicate pair, DeepSeek z=10.0, +0
  rerun, one quant document, and four-citation public answer anchors.
- protected artifact delta: none. All three pinned reports matched and both
  protected databases remained exact 2/2 with unchanged corpus facts.
- final closure audit: PASS. Against the checked runbook, exact closing record,
  and this R-CLOSE entry, `./run ci-local` passed 19/19; `cycle-check` reported
  v0.10.2 closed with seven closed execution runbooks; `checklist-audit`
  resolved 69/69 checked tasks with zero exemptions; `progress-check` resolved
  R-CLOSE to the release commit; version-check matched the exact HEAD tag;
  golden remained 11/11; protected artifacts remained 2/2 with all three pins
  matching; and the separate Python 3.12.13 lane passed 156/156 and verified
  21/21 exact packages.
- exact commands:

  ```bash
  cargo check -p cored
  ./run version-check
  jq '{aggregate, counts, attempts: (.attempts | length)}' evidence/v0.10.1/real-model-adversarial/report.json
  git diff --name-status e5af6bc5df8261cc004bd4d3247b70f8cbe930bb
  ./run ci-local
  PYTHONPATH=shell .venv/py312/bin/python -m pytest shell/tests -q
  .venv/py312/bin/python tools/python_constraints.py shell/constraints.txt
  python3 tools/evidence_artifacts.py validate
  ./run verify-artifacts
  ./run golden
  git tag -a v0.10.2 -m 'intel-platform v0.10.2'
  git rev-parse 'v0.10.2^{tag}'
  git rev-parse 'v0.10.2^{commit}'
  git cat-file -t v0.10.2
  ./run cycle-check
  ./run checklist-audit
  ./run progress-check
  ```

> **Closed-cycle status correction — 2026-07-26.** The immutable
> `evidence/v0.10.2/deferred-audit/report.json` carries the task field
> `v0.10.1 RECEIPT`. That label is wrong: the artifact records the v0.10.2
> deferred audit. Its bytes remain immutable and correctly pinned at SHA-256
> `4e11a8b3a3a64b5519469289f5cdf246bf13a0045954aa22c38703bbe6d29d9b`;
> this annotation does not move the pin. The v0.10.3 auditor derives new task
> labels from the active-cycle declaration.
