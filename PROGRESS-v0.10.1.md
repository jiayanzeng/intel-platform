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

### 2026-07-26 · RECEIPT — clean released-commit deferred audit

- owner: Codex
- commit: 6ad0dbd771d11e980af65258003990a528f00852
- result: PASS. The current auditor measured a separate clean detached
  worktree at release commit `45fa3d49860643fdb2595d82340e364d33566e7d`
  with explicit runner-receipt input and byte-exact protected database copies.
  The fresh report is
  `evidence/v0.10.1/deferred-audit/report.json`.
- pre-check control: PASS. The immutable v0.10 receipt reports dirty non-release
  subject `d9cab128…`, CI-runner defer under remote presence, and
  1 promoted / 6 deferred. The fresh receipt is byte-different and reports
  clean release subject `45fa3d49…`, CI-runner promote under the
  released-commit receipt trigger, and 2 promoted / 5 deferred.
- subject acceptance: PASS. The detached worktree status stayed empty before
  and after measurement. Its copied core/live-smoke databases matched SHA-256
  `db2f186e…` and `94f03e9e…`. After final verification, the temporary
  worktree and only its copied databases were removed.
- receipt acceptance: PASS. Seven candidates were accepted, zero rejected,
  and every stable logical path is under `evidence/ci-runs/`. The report's
  pgvector p95 was 7.431750 ms at 2,600 documents, below the 16.264 ms anchor.
  T7, Postgres, pgvector, multi-host, and A4 deferred; CI-runner and future
  `/view` materialization promoted.
- artifact acceptance: PASS. The fresh schema-2 report SHA-256 is
  `00cf14ae931b864616e19c437168d9ef8723791ddee6dc7866794f6850319362`.
  It contains no local absolute path, credential, endpoint, authorization, or
  tunnel alias. The old artifact remained byte-exact at
  `ea23f7f2077155b4f4614edeb0afef02bf43252a7733bbc0f25b0b03db742a76`.
- prose acceptance: PASS. The v0.10 release narrative now records the measured
  correction: runner evidence promotes because released-commit receipts exist,
  not because a Git remote exists.
- shell acceptance: PASS. Python 3.11.4 and 3.12.13 each passed 129 tests with
  one third-party Starlette warning; `py_compile` passed. The first sandboxed
  production attempt was a `ps` permission non-result; the permitted rerun is
  the counted report.
- golden-E2E delta: none. Standalone `./run golden` passed 11/11.
- protected artifact delta: none. `./run verify-artifacts` passed 2/2 before
  and after the production audit and again at final acceptance.

### 2026-07-26 · X-REGEN — conformant fresh real-model adversarial battery

- owner: Codex
- commit: 2613f5c05cf579273965467984d847ff2efb68fb
- result: PASS. A fresh no-resume run against the operator-confirmed chat and
  embedding roles completed 45/45 target-valid, model-completed cells. All 45
  real-model outcomes were `NOT EXERCISED`, none was `LEAK`, and the separate
  deployed-path positive control fired `GUARD FIRED`.
- order disposition: the runbook's PIN/X-REGEN numbering is dependency
  inverted: PIN requires the X1 pin “after Step 8,” while X-REGEN requires its
  report added to that pin. The explicit dependency was followed, so X-REGEN
  and its own pin completed before the remainder of PIN.
- provider gate: PASS. The bounded probe resolved completion-only chat model
  `gemma-4-26B-A4B-it-UD-IQ4_XS.gguf` and independent embedding model
  `embeddinggemma-300M-Q8_0.gguf`; the embedding capability returned exactly
  768 dimensions. Keys remained redacted.
- live failure-capable control: PASS. The first fresh run recorded two
  30-second HTTP-502/model-incomplete cells and failed coverage. The harness
  now records invalid invocations separately, never counts them as attempts,
  and retries within an explicit three-invocation budget. Transient/permanent
  502 tests prove completion and exhaustion paths. A second fresh run
  exercised that retry path but showed the 30-second ceiling was shorter than
  repeatable cell latency; it was interrupted after exhaustion and is a
  non-result.
- final matrix acceptance: PASS. The operator's `.env` was untouched; a
  mode-600 temporary copy raised only the chat timeout to 60 seconds and was
  deleted after use. The final no-resume matrix needed zero transport retries,
  had maximum latency 32,599.289 ms, maximum real-model gated run four tokens,
  and zero nonzero `n=8/12/16` matches. The positive control measured longest
  22 and `{n=8:15,n=12:11,n=16:7}`. `ATTEST_NGRAM` remains 16.
- artifact acceptance: PASS. The fresh report at
  `evidence/v0.10.1/real-model-adversarial/report.json` is 62,978 bytes with
  SHA-256
  `beec8bfa87b17c6b0552544fcfc810b517a8a8dd10067e2460dbce7342dda3f7`.
  Its invariant/secret scan found no credential-shaped value, endpoint, LAN
  address, loopback tunnel port, SSH command, prompt, or raw model answer. The
  v0.10 report stayed exact at
  `98fb3a3a1acac844aeccd0da0be2457ff9327ee0733f8570d7edc34b1870f13c`.
- pin acceptance: PASS. Manifest schema 2 now validates corpus-free pinned
  files by exact bytes and SHA-256; X1 is pinned, and a disposable byte
  mutation makes `validate` fail. Protected database verification remains a
  separate exact 2/2 result.
- shell acceptance: PASS. Python 3.11.4 and 3.12.13 each passed 132/132 with
  one third-party Starlette warning. The sandboxed seven-bind-denial run is a
  non-result; the permitted rerun is counted.
- golden-E2E delta: none. Standalone `./run golden` passed 11/11.
- protected artifact delta: none. `./run verify-artifacts` passed 2/2 at the
  exact recorded hashes.

### 2026-07-26 · PIN — pinned and source-rederived evidence receipts

- owner: Codex
- commit: edd77a4835057fb0a0836b39600cbe54a88b5092
- result: PASS. Manifest schema 2 now pins both v0.10.1 JSON evidence files by
  exact bytes/SHA-256, and a new corpus-free command re-derives the receipt's
  source/config/Git fields. The tracked local CI count is now 19.
- pin acceptance: PASS. Deferred audit
  `00cf14ae931b864616e19c437168d9ef8723791ddee6dc7866794f6850319362`
  (27,786 bytes) and X1
  `beec8bfa87b17c6b0552544fcfc810b517a8a8dd10067e2460dbce7342dda3f7`
  (62,978 bytes) both matched. `validate` needs no corpus; local `verify`
  checks these pins before its independent protected-database measurements.
- re-derivation acceptance: PASS.
  `tools/audit_deferred.py --rederive` recomputed the scheduler, writer,
  multi-host, attestation-boundary, and CI-runner source measurements and
  matched five dispositions, seven unchanged trigger strings, row count seven,
  and `v2_materialization_implemented=false`. It excludes host/time, remote
  text, receipt execution detail, source hashes, and numeric pgvector/view
  measurements; whole-file pins cover the corpus-dependent rows.
- runnerless acceptance: PASS as configuration. The same manifest/re-derive
  commands are one blocking Python 3.11 `ci.yml` step with full Git history;
  YAML parsed and a static test requires the step. No post-PIN hosted execution
  is claimed. The on-site production pytest is guarded on both protected DBs
  and a built `cored`, so a corpus-less runner skips it.
- on-site production acceptance: PASS. The guarded test invoked full
  `production_measurements()`/`evaluate()` and matched the committed
  environment-independent snapshot; its focused run passed in 2.64s.
- failure-capable controls: PASS. A scratch receipt flipping the T7 disposition
  failed with `REDERIVATION MISMATCH source_dispositions`. A disposable copy of
  the pinned deferred receipt with one appended byte failed manifest
  validation on SHA-256. Neither committed receipt was altered.
- count/documentation acceptance: PASS. `run` help names the 19-job matrix;
  current STATE and acceptance records say 19. Historical 18-job results remain
  explicitly historical; the v0.10 and v0.10.1 runner-comparison records now
  state when the change occurred.
- full local-CI acceptance: PASS. `./run ci-local` passed 19/19, including 99
  workspace tests, 20 net tests, warning-denied builds, clippy/fmt, Rust 1.78,
  136 Python 3.11 shell tests, the new re-derivation, golden, pins/protected
  evidence, fingerprints, and lifecycle records. Python 3.12.13 independently
  passed 136/136. Targeted PIN lanes passed 23/23 on both interpreters;
  ShellCheck, Bash syntax, and workflow YAML parsing passed.
- golden-E2E delta: none. Both the 19-job matrix and final standalone permitted
  lifecycle passed 11/11. The first standalone attempt's denied loopback bind
  is an environment non-result.
- protected artifact delta: none. `./run verify-artifacts` passed exact 2/2;
  both pinned JSON files also matched.
