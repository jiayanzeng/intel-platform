# PROGRESS-v0.10.1.md — append-only execution record

This file records v0.10.1 task and gate events after their implementation
commits exist. Each entry names the measured result, every applicable
acceptance criterion, the golden delta, and the real implementation commit.
Entries are append-only; corrections are new dated entries.

### 2026-07-26 · E0-GATE — known dirty inputs corrected before baseline restart

- owner: Codex
- commit: f56d2c40ec1a7a9b3f2bbfcf4037ed151ec469f8
- result: BLOCKED, then corrected without claiming E0 complete. The first
  session opener found the operator-supplied runbook, three modified tracked
  Finder metadata files, and one untracked Finder metadata file. E0's literal
  clean-tree gate therefore stopped before `ci-local` or downstream acceptance.
- gate evidence: `git status --porcelain=v1` named modified `.DS_Store`,
  `crates/.DS_Store`, and `shell/.DS_Store`, plus untracked
  `TASKS-v0.10.1-EXECUTION.md` and `evidence/.DS_Store`. HEAD was
  `6c53d8585d43d46723a83ba1635012b7ab00671f`, described as
  `v0.10.0-1-g6c53d85-dirty`.
- identity evidence: annotated tag object
  `f70fd84ca0995088d2890096f3429bb878409979` dereferenced exactly to release
  commit `45fa3d49860643fdb2595d82340e364d33566e7d`; `origin` was present.
- correction: added `*.DS_Store` to `.gitignore`, removed the three existing
  metadata files from Git tracking without deleting the local files, committed
  the supplied runbook, declared v0.10.1 active, created this progress log, and
  changed one quoted historical authority phrase in the now-inactive v0.10
  runbook to past tense so `cycle-check` would not mistake it for live
  authority.
- runbook review: recorded that CIR must execute the new workflow definition
  while checking out the audited release commit; RECEIPT must run the new
  auditor against an explicit clean release worktree and explicit receipt
  input; Step 6's decline summary is 1 promoted / 6 deferred; historical
  18-job measurements remain immutable when the current count later becomes 19.
- lifecycle acceptance: `./run cycle-check` passed with active v0.10.1 and
  five closed execution runbooks. `./run checklist-audit` resolved the existing
  52/52 checked tasks with zero exemptions.
- test acceptance: NOT RUN at this gate checkpoint. E0 remains unchecked and
  restarts from the clean post-audit tree.
- golden-E2E delta: NOT MEASURED; no claim.
- protected artifact delta: NOT MEASURED; no protected file was touched.

### 2026-07-26 · E0 — entering state rebuilt and D1–D6 confirmed

- owner: Codex
- commit: 30b6a83fb97567e24d836dbee8941e453e8c63cb
- result: PASS after the separately recorded dirty-input correction. Clean
  HEAD `3f81e31f324e9624cbbacb3be8ec6b817561b2aa` was
  `v0.10.0-3-g3f81e31`; annotated v0.10.0 still dereferenced to release commit
  `45fa3d49860643fdb2595d82340e364d33566e7d`, and `origin` was present.
- baseline acceptance: PASS. The permitted `./run ci-local` rerun passed
  18/18 with 99 workspace tests, 20 net tests, warning-denied builds,
  clippy/fmt, Rust 1.78 check/tests, 120 Python 3.11 shell tests, golden 11/11,
  protected artifacts 2/2, fingerprints, and lifecycle/progress auditors. The
  sandboxed 113-pass/7-bind-denial attempt is a non-result.
- Python acceptance: PASS. The separate Python 3.12.13 lane passed 120/120
  with the same one third-party Starlette warning.
- defect acceptance: PASS. D4's stored validity accepts the HTTP-502 timeout
  and the shipped report has 0 model-completed attempts; D2's receipt describes
  dirty non-release commit `d9cab128`; D1 has one receipt reader and no
  producer; D3 has no production-audit test or evidence-JSON pin; D5 is 45
  `NOT EXERCISED` cells at threshold 16; D6's ambient duplicate can mask the
  asserted FastAPI drift.
- static-count correction: PASS. Rust sources contain 58 `#[test]`, 42
  `#[tokio::test]`, and four `cfg(feature = "net")` gates. Runtime 99/20
  remains authoritative.
- lifecycle acceptance: PASS. Standalone `version-check`, `cycle-check`, and
  pre-E0 `checklist-audit` passed; the latter resolved the entering 52/52
  checked tasks with zero exemptions.
- golden-E2E delta: none. The standalone final lifecycle passed 11/11 with the
  exact 13 → 12 corpus, hamming-12 pair, DeepSeek z=10.0, +0 rerun, one quant
  document, and four-citation public answer anchors.
- protected artifact delta: none. Both databases matched their exact hashes
  and corpus facts at 2/2.

### 2026-07-26 · X-VALID — adversarial validity requires model completion

- owner: Codex
- commit: 22c8c93c319fa5bd19f78bf34c25621bd03c398e
- result: PASS. Classify-time and resume-time validity now independently
  require both target context and a completed model call. Stored
  `valid_attempt` is no longer trusted, and console detail includes HTTP status.
- failure-capable controls: PASS. Before the fix, the stale-resume test reused
  two attempts with no verifiable completion and the HTTP-502 control marked
  all five synthetic timeouts valid; the targeted run failed 2/2. After the
  fix, the expanded resume/timeout target passed 3/3 and timeout coverage was
  visibly FAIL.
- shipped-artifact disposition: the immutable v0.10 report is non-conformant:
  0/45 attempts carry `model_completed:true`, 44 omit the key, and one 502
  attempt records false. X-REGEN will run fresh with no resume.
- shell acceptance: PASS. Python 3.11.4 and 3.12.13 each passed 122 tests with
  one third-party Starlette warning. `py_compile` passed.
- golden-E2E delta: none. Standalone `./run golden` passed 11/11.
- protected artifact delta: none. `./run verify-artifacts` passed 2/2 at the
  exact recorded hashes.

### 2026-07-26 · X-CTRL — real-path guard control and near-match telemetry

- owner: Codex
- commit: aa3232695230f5392d37df096d5ea07fe6837c4f
- result: PASS. Report schema 2 records a separate real-path positive control,
  completeness requires it to fire, and an all-`NOT EXERCISED` aggregate is
  WARN only with that proof (otherwise FAIL). `GUARD FIRED` remains PASS and
  `LEAK` remains FAIL.
- failure-capable controls: PASS. Four pre-implementation controls failed 4/4:
  the aggregate/control gate, missing-control rejection, graduated 15-token
  near-match telemetry, and deployed-handler positive control did not exist.
  All pass after implementation; the verifier module passed 19/19.
- real-path control acceptance: PASS. An isolated real-core HTTP run ingested
  13 fixture documents, filled 13 embeddings, and routed a deterministic
  leaking chat response through real FastAPI `/v1/ask` and core `/attest`.
  It returned HTTP 200, included the target, fired `GUARD FIRED`, exposed no
  gated public overlap, and measured longest 29 with match counts
  `n=8:22`, `n=12:18`, `n=16:14`.
- matrix acceptance: PASS with explicit non-pass aggregate. The normal local
  mock completed 45/45 valid target/shape cells; all were `NOT EXERCISED`, with
  zero `n=8/12/16` matches. Coverage passed because the separate control fired,
  while aggregate status remained WARN. No real-provider result is claimed.
- classifier/telemetry acceptance: PASS. Doubles demonstrated
  `NOT EXERCISED`, `GUARD FIRED`, and `LEAK`; an exact 15-token near miss
  measured longest 15 and `{n=8:8,n=12:4,n=16:0}`. `ATTEST_NGRAM` remains 16.
- recording-policy acceptance: PASS. The temporary schema-2 report contained
  no authorization, raw/public answer, prompt, credential, endpoint URL, or
  tunnel-alias fields or values, and was not admitted as evidence.
- shell acceptance: PASS. Python 3.11.4 and 3.12.13 each passed 125 tests with
  one third-party Starlette warning. `py_compile` passed.
- golden-E2E delta: none. Standalone `./run golden` passed 11/11.
- protected artifact delta: none. `./run verify-artifacts` passed 2/2 at the
  exact recorded hashes.

### 2026-07-26 · CIR — runner-produced, ancestry-checked CI receipts

- owner: Codex
- commit: 40778a4aae72e87d03f1370db5169092c989769b
- result: PASS. Every configured workflow job now emits an `if: always()`
  receipt and persists it as an uploaded artifact. The auditor counts only
  well-formed receipts whose SHA is an ancestor of the audited HEAD, records
  rejected candidates, and promotes the CI-runner row only for a nonzero
  accepted count.
- failure-capable controls: PASS. Before implementation, the targeted module
  failed 3/7: no receipt-filter function existed for ancestor or foreign
  history, and two Git-remote entries promoted a zero-receipt row. After
  implementation the expanded module passed 8/8.
- workflow acceptance: PASS as configuration, not execution. Static checks
  counted seven receipt emit steps, seven upload persistence steps, seven
  explicit checkout refs, and seven upload actions. The Python matrix has
  distinct filenames/artifacts. Ruby parsed the YAML. `workflow_dispatch`
  accepts an explicit audited SHA while receipts record actual checked-out
  `git rev-parse HEAD`; no workflow was pushed or run.
- auditor acceptance: PASS. The original direct
  `evidence/ci-runs/*.json` glob is unchanged. Synthetic Git history accepted
  an ancestor receipt and promoted, visibly rejected a sibling-branch receipt
  and deferred, and kept
  `workflow_configuration_counts_as_execution:false`.
- trigger acceptance: PASS. The row now reads
  `a runner execution receipt exists for the released commit`, ignores Git
  remote/current-runner presence for disposition, and keys only on filtered
  receipt count.
- production local state: zero candidates, zero accepted, zero rejected, and
  deferred under the restated trigger despite two remote entries. This is an
  absence measurement, not a runner-execution claim.
- shell acceptance: PASS. Python 3.11.4 and 3.12.13 each passed 129 tests with
  one third-party Starlette warning. `py_compile` passed.
- golden-E2E delta: none. Standalone `./run golden` passed 11/11.
- protected artifact delta: none. `./run verify-artifacts` passed 2/2 at the
  exact recorded hashes.

### 2026-07-26 · G-RUN — released-commit runner receipts captured

- owner: Codex
- commit: d5c2935ca8d20395728bb686b5e25f015eb59c0d
- result: PASS with explicit operator approval. `main` was fast-forwarded,
  the new workflow definition was manually dispatched against release commit
  `45fa3d49860643fdb2595d82340e364d33566e7d`, and runner run
  `30187058897` concluded success.
- runner acceptance: PASS. Core 27s, lint 18s, net 20s, MSRV 35s, Python 3.11
  24s, Python 3.12 22s, and golden 38s all passed; scheduled drift skipped as
  designed. The run measured Ubuntu 24.04.4, Rust 1.91.1/1.78.0, Python
  3.11.15/3.12.13, and ShellCheck 0.9.0.
- receipt acceptance: PASS. Seven uploaded artifacts were downloaded to the
  auditor's unchanged `evidence/ci-runs/*.json` input. Every receipt is
  strict-field JSON with run id 30187058897, attempt 1, Linux, success, and
  exact SHA `45fa3d49…`. The ancestry filter accepted 7/7, rejected zero, and
  promoted the CI-runner row for the restated released-commit receipt trigger.
- job-set comparison: PASS with explicit divergence. The runner executed seven
  grouped nodes plus one skipped scheduled-only node; `./run ci-local` passed
  eighteen finer-grained units. Cycle/checklist/progress and exact protected
  database verification are local-only; Python 3.12, manifest-only checks, and
  scheduled drift are runner-specific or separately grouped.
- failure-capable control: PASS. Temporary commit
  `8cceae90debaf7e730bebd7bd6c15183e32a6263` changed only the shell version
  literal to 9.9.9. Runner run `30187207654` failed version consistency in
  both Python lanes and named that exact value; both failure receipts still
  uploaded and every non-shell executable job passed. The throwaway branch was
  then deleted locally and remotely.
- identity/cleanup acceptance: PASS. Local and remote main were equal at
  `5bcabcb870a906b0b830bf3c8c391bbe3ced71b0` before this evidence commit.
  Local and remote tag object `f70fd84ca0995088d2890096f3429bb878409979`
  still dereferenced to release commit `45fa3d49…`; the control moved neither.
  The prerequisite automatic main-push run `30187051942` also passed.
- golden-E2E delta: none. The final `./run ci-local` passed 18/18 and included
  golden 11/11.
- protected artifact delta: none. The same local matrix verified both protected
  databases 2/2 at their exact recorded hashes.
