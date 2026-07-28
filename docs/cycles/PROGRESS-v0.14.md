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

### 2026-07-28 · RULE-SHAPE-AUDIT — claims match executable rule shapes

- runbook: `TASKS-v0.14-EXECUTION.md`
- owner: Codex
- commit: e80c523553b2f0f360330e073ff19c480f75cc4f
- result: PASS. R1 is now an allow-list over the five enumerable production
  store callers. Each must call `assign_canonical_ids_tx` exactly once, and
  every other production canonical-identity helper call is reported with
  file, line, helper token, and enclosing caller. Its site-specific control
  plants the E0 `rebuild_identity_with_limit` seam and fails at
  `crates/store/src/sqlite.rs:672`. R6 was already an exact allow-list over the
  two governed marker-delimited authorization blocks.
- mutation acceptance: PASS with four isolated outcomes against the revised
  rules. The renamed R1 seam now FAILs at its planted line; an unknown
  inference-gateway call still makes R3 PASS; an unknown
  `INFERENCE_CREDENTIAL` form still makes R4 PASS; and renaming both
  `MODEL_PROFILE_AUTHORITY` markers still makes R6 FAIL in both enumerated
  files. All four disposable worktrees were removed afterward.
- stated-limitation acceptance: PASS. R3 is an open-bottom deny-list over
  recognized OpenAI, Anthropic, and LLM vocabulary; an unknown provider or
  inference-gateway spelling is outside coverage, so R3 does not prove HC3
  against arbitrary new vocabulary. R4 is an open-bottom deny-list over
  registered credential names and value shapes; unknown names or encodings
  are outside coverage, so R4 does not prove that every possible secret form
  is absent. These limits are explicit here, in each registry `scope`, and in
  `ARCHITECTURE.md`; they narrow scanner claims, not the governing HC3 and
  credential-disclosure prohibitions.
- source-preservation acceptance: PASS. Implementation commit
  `e80c523553b2f0f360330e073ff19c480f75cc4f` changed zero files under
  `crates/` or `apps/`.
- invariant acceptance: PASS. The focused module passed **13/13** under Python
  3.11.4 and 3.12.13. The full self-test passed **7/7 rules / 11
  site-specific controls**.
- regression acceptance: PASS. The exact implementation tree passed
  `./run ci-local` **20/20** with **124** workspace Rust tests, **47** net
  tests, zero rustc/clippy/fmt/ShellCheck failures, locked Rust 1.78 green,
  protected databases **2/2**, and all **86/86** pins exact.
- golden-E2E delta: **0**. The matrix and mandatory standalone run both
  remained **11/11** byte-identical.

### 2026-07-28 · R8-IDENTITY-BEFORE-BIND — identity precedes listener

- runbook: `TASKS-v0.14-EXECUTION.md`
- owner: Codex
- commit: ab266df2fc671649b6bff0ea1ce6eb2c21796fa2
- result: PASS. `ARCHITECTURE.md` now states that production `cored` runs its
  one `build_robots_cache` crawler-identity construction call before the sole
  `TcpListener::bind`; when `net` is enabled, this installs the process-scoped
  identity before the listener can accept a request. R8 enumerates those two
  call sites in production `main`, requires exactly one of each, and compares
  their source order.
- control acceptance: PASS. Reordering the calls made R8 fail at
  `apps/cored/src/main.rs:1333`; deleting identity construction failed at line
  1333 with the missing-call finding; and adding a second bind before identity
  construction failed at line 1331 with the two-bind finding. All three
  controls are site-specific and distinguish the offending condition.
- invariant acceptance: PASS. R8 passes on HEAD. The complete self-test passes
  **8/8 rules / 14 controls**, and the focused invariant module passes
  **14/14** on Python 3.11.4 and 3.12.13.
- source-preservation acceptance: PASS. Implementation commit
  `ab266df2fc671649b6bff0ea1ce6eb2c21796fa2` changed zero files under
  `crates/` or `apps/`.
- shell acceptance: PASS after environment retry. The first sandboxed
  standalone attempts denied loopback binds and `ps` after **211** passing
  tests; permitted repeats passed **219/219** under both Python 3.11.4 and
  3.12.13.
- regression acceptance: PASS. `./run ci-local` remained **20/20** with
  **124** workspace Rust tests, **47** net tests, zero rustc/clippy/fmt/
  ShellCheck failures, locked Rust 1.78 green, protected databases **2/2**,
  and all **86/86** pins exact.
- golden-E2E delta: **0**. The matrix and mandatory standalone run both
  remained **11/11** byte-identical.

### 2026-07-28 · R9-TEST-SEAM — fault injector remains dev-only

- runbook: `TASKS-v0.14-EXECUTION.md`
- owner: Codex
- commit: 9968f9f426b28e373e24907954cecea2f08bd78a
- result: PASS as a guard gap, not a live-defect fix. E0's locked release build
  had already verified `test_clear_fingerprint` absent from both the release
  symbol table and binary strings. R9 now enumerates every root-declared
  workspace manifest and permits `test-support` only as its package feature
  declaration or on a dev-dependency edge.
- control acceptance: PASS. Moving the existing `intel-store` feature
  activation from `apps/cored/Cargo.toml` `[dev-dependencies]` into
  `[dependencies]` made R9 fail at exact line 15 and name the non-dev section.
  R9 passes on HEAD.
- preservation acceptance: PASS. Implementation commit
  `9968f9f426b28e373e24907954cecea2f08bd78a` changed no `Cargo.toml` and no
  Rust source file.
- invariant acceptance: PASS. The complete scanner passes **9/9 rules / 15
  site-specific controls**, and the focused invariant module passes **15/15**
  under Python 3.11.4 and 3.12.13.
- shell acceptance: PASS. The complete shell suite passes **220/220** under
  Python 3.11.4 and 3.12.13.
- regression acceptance: PASS. `./run ci-local` remained **20/20** with
  **124** workspace Rust tests, **47** net tests, zero rustc/clippy/fmt/
  ShellCheck failures, locked Rust 1.78 green, protected databases **2/2**,
  and all **86/86** pins exact.
- golden-E2E delta: **0**. The matrix and mandatory standalone run both
  remained **11/11** byte-identical.

### 2026-07-28 · DIAGNOSTIC-KNOB-GATE — option (b) selected

- owner: Operator + Codex
- commit: 28c5917973691642d35371b25dd82f4cd2c1f08a
- result: GATE PASS for the required disposition only; implementation has not
  started. The operator selected option **(b)**.
- decision and reasoning: retain the bounded diagnostic delay used by
  `benchmark_view.py`, but make any configured use loud at startup and document
  it as a deliberate operator knob. This adopts the runbook's cheapest honest
  disposition: the defect is silent activation, while feature-gating would add
  a second build configuration and removal would require re-deriving the
  existing view-decomposition evidence.
- version trigger: pending implementation. Option (b) is a runtime behavior and
  operator-surface change, so successful DIAGNOSTIC-KNOB completion fires
  **v0.14.0**, not the documentation-only v0.13.1 path.
- test and golden acceptance: NOT RUN for this decision-only checkpoint; no
  implementation or runtime file changed.

### 2026-07-28 · DIAGNOSTIC-KNOB — bounded delay is loud and documented

- runbook: `TASKS-v0.14-EXECUTION.md`
- owner: Codex
- commit: 010536c575b9bf089665a97b0f534aa547825e3d
- result: PASS under operator-selected option **(b)**. The choice and reasoning
  were recorded before implementation in decision audit commit
  `5c0855cbf15d0753d0941083f3086275f15cb834`. `cored` now emits a startup
  warning whenever either diagnostic variable is set; the warning names both
  raw settings and the effective bounded delay.
- bound acceptance: PASS. The live delay path uses the tested bounding helper:
  missing or invalid values become zero and valid values are capped at
  **10,000 ms**. The focused Rust test passed under offline and net feature
  builds.
- documentation acceptance: PASS. `.env.example`, `README.md`,
  `deploy/README.md`, and `ARCHITECTURE.md` now name both variables, all four
  stages, the bound, startup warning, and unset-by-default operating rule. The
  architecture records that only timing changes; no `/view` response body
  changes.
- startup-warning acceptance: PASS with a failure-capable check. The real
  decomposition control observed the warning in **3/3** delayed core logs,
  measured analysis median delta **122.232000 ms** versus sector-load median
  delta **0.186000 ms**, and printed both PASS lines. Its exit status **1** is
  the runbook control's specified success signal. A corrupted warning fixture
  was independently rejected. Focused benchmark tests passed **4/4** under
  Python 3.11.4 and 3.12.13.
- version acceptance: PASS. Option (b) changes runtime behavior and the
  operator configuration surface, firing **v0.14.0**; the documentation-only
  v0.13.1 path does not apply.
- regression acceptance: PASS. `./run ci-local` passed **20/20** with **125**
  workspace Rust tests, **48** net tests (**23** `intel-ingest` + **25**
  `cored`), zero rustc/clippy/fmt/ShellCheck failures, locked Rust 1.78 green,
  protected databases **2/2**, and all **86/86** pins exact. Standalone shell
  passed **221/221** on Python 3.11.4 and 3.12.13 with **21/21** exact packages
  on both. `invariant-scan --self-test` remained **9/9 rules / 15 controls**.
- golden-E2E delta: **0**. The matrix and mandatory standalone run both
  remained **11/11** byte-identical.

### 2026-07-28 · TEMPLATE-REMEASURE — active deferrals require owners

- runbook: `TASKS-v0.14-EXECUTION.md`
- owner: Codex
- commit: 7fde11f6e74af7807e5d6cd7bdf4d40c594424c7
- result: PASS. `AGENTS.md` now requires each non-`none` action in an active
  **Deferred means deferred** table to name an existing discharging `Step N`;
  runbooks that change the release commit must contain a RE-MEASURE step for
  that commit. `cycle-check` enforces the row assignment on the active runbook.
- fail-before acceptance: PASS. A scratch active runbook with a non-`none`
  Runner-evidence action and no step failed with `deferred row 'Runner
  evidence' has a non-none action but names no discharging Step N`. A companion
  fixture assigned to an existing Step 2 RE-MEASURE passed. The real v0.14
  runbook also passed.
- preservation acceptance: PASS. No closed execution runbook, progress log, or
  source under `apps/` or `crates/` changed. v0.13's omission remains intact as
  the originating evidence; closed runbooks are not retroactively checked by
  this new active-runbook rule.
- shell acceptance: PASS. The focused cycle-check module passed **11/11** on
  Python 3.11.4 and 3.12.13. The complete shell suite passed **223/223** on
  both interpreters.
- regression acceptance: PASS. `./run ci-local` passed **20/20** with **125**
  workspace Rust tests, **48** net tests (**23** `intel-ingest` + **25**
  `cored`), zero rustc/clippy/fmt/ShellCheck failures, locked Rust 1.78 green,
  protected databases **2/2**, and all **86/86** pins exact.
  `invariant-scan --self-test` remained **9/9 rules / 15 controls**.
- golden-E2E delta: **0**. The matrix and mandatory standalone run both
  remained **11/11** byte-identical.

### 2026-07-28 · STEP8-COUNT-AMENDMENT — compare one candidate, not one step

- runbook: `TASKS-v0.14-EXECUTION.md`
- owner: Operator + Codex
- commit: 38b316fdfff4079f8ebb5f1e78543d487e019244
- result: PASS. One disclosed Step 8 amendment corrects the global definition
  of done, Step 8's log-reading instruction, and its acceptance criterion. The
  final scanner total is **9 rules / 15 controls**: CONTROL-PRECISION preserves
  11 controls while adding site precision, R8 adds three, and R9 adds one.
  Hosted evidence must now equal the local self-test at the same candidate
  commit and the pair must be **9 / 15**.
- root cause: the former criterion was anchored to a moment—Step 2's recorded
  value—when the durable property is an equality between hosted and local
  measurements at one commit. A step-number anchor goes stale as soon as a
  later step legitimately changes the quantity; a property relation does not.
  This is the second runbook defect of the same broader shape as v0.13's
  deferral row: the text declared a requirement that later execution could not
  correctly discharge.
- deferred candidate: consider a sibling to
  `check_active_deferral_assignments` that detects acceptance criteria citing a
  step's measured value rather than an invariant relation. This is recorded as
  a **v0.15 candidate input** only and is not implemented in v0.14.
- validation acceptance: PASS. `./run cycle-check` accepted the disclosed
  amendment; the focused cycle-check module passed **11/11** under Python
  3.11.4 and 3.12.13; `./run ci-local` passed **20/20**; and the mandatory
  standalone golden remained **11/11**.
- pre-hosted count finding: explicit discovery on the amendment tree reported
  **125** workspace tests and **48** net tests split as **23** `intel-ingest`
  plus **25** `cored`. This differs from the operator-provided Step 8
  expectation of 24 + 24 and is recorded without changing source or
  reconciling the counts.
- preservation acceptance: PASS. `origin/main` remains
  `0eff6e4c4987b7ebb138cf0bb1da6ebe8bd851b9`; no branch or tag was pushed, no
  closed runbook or progress log changed, and A4 plus the editable-L1
  controller residual remain open.
- golden-E2E delta: **0**. Matrix and standalone golden both remained
  **11/11** byte-identical.

### 2026-07-28 · RE-MEASURE-GATE — remote workflow lacks self-test invocation

- runbook: `TASKS-v0.14-EXECUTION.md`
- owner: Codex
- commit: 546c1a04a080a01d00fc9f351ad34f1fbe3fc149
- result: BLOCKED before workflow dispatch. The authorized push placed exact
  post-amendment commit `0af15157efc88357b84d0c08492c938cfef00660`
  at non-`main` branch `candidate/v0.14.0`; this supersedes `066609b…` as the
  candidate.
- remote preservation: PASS. A remote read confirmed `origin/main` unchanged
  at `0eff6e4c4987b7ebb138cf0bb1da6ebe8bd851b9`, no `v0.14.0` tag, and zero
  workflow runs for the candidate branch. Nothing was published.
- workflow preflight: FAIL. The remote candidate's `ci.yml` contains the
  workspace test, `intel-ingest` net test, `cored` net test, both shell matrix
  legs, and golden. Its invariant command is only `./run invariant-scan`;
  there is no `./run invariant-scan --self-test` invocation, so no hosted log
  can report the required **9 rules / 15 controls** self-test pair.
- disposition: STOP. No workflow was dispatched, no source was edited to make
  the candidate green or bypass the preflight, and no receipt, attestation,
  pin, hosted identity, or release-grade v0.14 evidence claim was created.
  RE-MEASURE remains unchecked.
- local comparison finding: the post-amendment tree measured **125** workspace
  tests and **48** net tests split as **23** `intel-ingest` + **25** `cored`,
  diverging from the operator-provided 24 + 24 expectation. This was reported
  and not reconciled.
- last valid regression anchor: the exact candidate code plus disclosed
  amendment passed local CI **20/20**, shell **223/223** on both interpreters,
  `invariant-scan --self-test` **9/9 rules / 15 controls**, and golden
  **11/11**.

### 2026-07-28 · SELF-TEST-SCOPE — registry-derived coverage and wiring correction

- runbook: `TASKS-v0.14-EXECUTION.md`
- owner: Operator + Codex
- commit: bb5ce61fef2d90cf63f7382baed5488fe68c3569
- result: PASS. The focused pytest parameterization now loads every rule id
  from `config/invariant-rules.json`, asserts exact registered-id coverage and
  a non-empty control set, and exercises each rule's controls at their expected
  sites. Omitting the final registered id made the new coverage assertion red;
  the failure-capable guard test passed by observing that rejection.
- wiring decision: preserve the existing no-argument self-test behavior.
  Current code and v0.13 evidence candidate `7faaa4e…` both route
  no-argument `./run invariant-scan` through `self_test`. Job 20 and hosted
  Python 3.11 therefore already execute all registry-loaded controls; both
  hosted shell pytest legs independently execute the derived focused coverage.
  No redundant flag-only edit was made to `run` or `ci.yml`.
- retained-log evidence: v0.13 run **30277584129** lint contains no invariant
  step; the invariant execution is in its Python 3.11 shell job. That retained
  log prints every R1–R7 control and ends verbatim
  `invariant-scan: SELF-TEST PASS (7/7 rules, 11 controls)`. The published
  record attributes the count to that hosted Python 3.11 log, so the claim is
  supported.
- retraction disposition: retraction #4 and the proposed second retraction
  were refused because the retained code and log falsify their reasons.
  `config/checklist-retractions.json` remains unchanged with the three valid
  forward retractions; no closed runbook or progress log was edited.
- directive corrections: (1) the accepted net split is **23**
  `intel-ingest` + **25** `cored`; (2) the assertion that no hosted job emits a
  self-test count was false because no-argument execution emits it; and (3)
  the assertion that v0.13 review checked only the harness and not wiring was
  false because the committed CLI default and retained hosted execution prove
  the wiring. The preceding RE-MEASURE-GATE entry is therefore a syntax-only
  non-result, corrected forward here.
- active-runbook acceptance: PASS. A disclosed gate-added SELF-TEST-SCOPE task
  records the measured behavior, and Step 8 now requires the exact hosted
  registered-rule and self-test summary lines plus both derived shell pytest
  legs.
- test acceptance: PASS. The focused module passed **17/17** under Python
  3.11.4 and 3.12.13; implicit and explicit scanner commands both ended
  `SELF-TEST PASS (9/9 rules, 15 controls)`; complete shell passed **225/225**
  on both interpreters.
- regression acceptance: PASS. `./run ci-local` remained **20/20** with
  **125** workspace tests, **48** net tests (**23 + 25**), zero
  rustc/clippy/fmt/ShellCheck failures, locked Rust 1.78 green, protected
  databases **2/2**, and all **86/86** pins exact. No source under `crates/` or
  `apps/` changed.
- golden-E2E delta: **0**. Matrix and mandatory standalone golden both remained
  **11/11** byte-identical.

### 2026-07-28 · RE-MEASURE — authenticated replacement-candidate evidence

- runbook: `TASKS-v0.14-EXECUTION.md`
- owner: Codex
- commit: f8cfe16f03454a1f8665e874601035dcccae1665
- candidate acceptance: PASS. Only non-`main` branch
  `candidate/v0.14.0` was advanced, to exact SELF-TEST-SCOPE audit commit
  `ee9ee0f9ed96cb2cb7759c3c3e59fbf8f325ae1a`. Read-only verification left
  `origin/main` at `0eff6e4c4987b7ebb138cf0bb1da6ebe8bd851b9` and found no
  `v0.14.0` tag. No publication or live server session occurred.
- workflow preflight: PASS. The exact candidate's remote `ci.yml` was read
  before dispatch and confirmed to check out `audit_sha` in the workspace,
  net, both shell, lint, MSRV, and golden jobs.
- hosted acceptance: PASS. Workflow-dispatch run **30324186389**, attempt
  **1**, used `publish_evidence: true` and
  `audit_sha=ee9ee0f9ed96cb2cb7759c3c3e59fbf8f325ae1a`; all seven
  evidence identities succeeded and report-only drift was skipped.
- hosted count acceptance: PASS from raw logs, not job status. Workspace
  results sum to **125 passed / 0 failed**. Net is **48**: **23**
  `intel-ingest` plus **25** `cored`. Python 3.11 and 3.12 each report
  **224 passed / 1 skipped / 1 third-party warning** and execute the
  registry-derived invariant-control module. The scanner lines are verbatim
  `invariant-scan: PASS (9/9 registered rules)` and
  `invariant-scan: SELF-TEST PASS (9/9 rules, 15 controls)`. Hosted golden is
  verbatim `golden result: PASS (11/11 checks)`.
- evidence acceptance: PASS. Seven receipt/bundle pairs name run
  **30324186389**, attempt **1**, success, Linux, and both event and checkout
  SHA equal to the evidence candidate. Release-grade `audit-deferred` required
  attestations, accepted **7**, rejected **0**, and measured **5 deferred / 2
  promoted**. Re-derivation passed with rows **7**, source dispositions **5**,
  triggers **7**, release grade, and attestations required.
- artifact acceptance: PASS. The fourteen hosted files and **34,076-byte**
  audit report add fifteen forward pins. Manifest validation,
  `verify-artifacts`, and `evidence-report` report **101/101** pins: **99/99
  evidence** plus **2/2 authorization surfaces**, with protected databases
  exact **2/2**.
- measured non-results: the first detached audit lacked the intentionally
  ignored protected databases; a re-derivation omitted the receipt directory;
  sandboxed attestation checks could not reach GitHub; and sandboxed standalone
  golden could not bind loopback. The first Python 3.12 standalone suite also
  had eight sandbox-only failures because loopback binds and `ps` were denied.
  Each stopped without a pass claim. The same complete audit, corrected
  re-derivation, permitted golden command, and permitted Python 3.12 suite then
  passed.
- regression acceptance: PASS. `./run ci-local` passed **20/20** with **125**
  workspace tests, **48** net tests (**23 + 25**), zero
  rustc/clippy/fmt/ShellCheck failures, locked Rust 1.78 green, all **101/101**
  pins exact, `invariant-scan` **9/9 rules / 15 controls**, and golden
  **11/11**. Standalone shell passed **225/225** on Python 3.11.4 and 3.12.13
  with **21/21** exact packages on both.
- preservation acceptance: PASS. No source under `crates/` or `apps/` and no
  closed runbook or progress log changed. A4 and the editable-L1 controller
  residual remain open; L2 remains scheduled. R-CLOSE remains pending its
  separate operator publication decision.
- golden-E2E delta: **0**. Hosted, matrix, and mandatory standalone golden all
  remained **11/11** byte-identical.

### 2026-07-28 · REVIEW-CORRECTION — command behavior is proved at its entry point

- runbook: `TASKS-v0.14-EXECUTION.md`
- owner: Operator + Codex
- commit: 4ad4c8d71075731dd87c360e8b0d3d91d80b5518
- correction: one of the three review findings stands. The expected net split
  was incorrectly stated as 24 + 24; the measured and accepted split is
  **23** `intel-ingest` + **25** `cored`.
- withdrawn finding: Step 8 did not demand output no hosted job produces.
  No-argument `./run invariant-scan` emits
  `invariant-scan: SELF-TEST PASS (9/9 rules, 15 controls)`, so the criterion
  was satisfiable as written.
- withdrawn finding: the statement that Directive 2 verified the harness but
  not the wiring was observationally true but inconsequential. The wiring was
  already correct, and the v0.13 acceptance criterion was true when checked.
- root cause: the reviewer read the shell wrapper and inferred tool behavior
  without reading `main()`, after previously making the mirrored mistake of
  reading the tool without checking its wrapper. A command-behavior claim is
  verified at the command's entry point, not its caller. The earlier probe also
  passed `--rules`, which suppresses default self-test, and misread the absent
  self-test line as evidence about no-argument execution.
- disposition: this is a v0.14 review defect only, not a codebase or v0.13
  defect. Retraction #4 was investigated and disproved. Retained v0.13 run
  **30277584129** ends
  `invariant-scan: SELF-TEST PASS (7/7 rules, 11 controls)`, while
  `tools/invariant_scan.py:1039` makes no-argument execution call `self_test`.
  Retractions remain **three**.

### 2026-07-28 · R-CLOSE — v0.14.0 selected, locally closed, publication withheld

- runbook: `TASKS-v0.14-EXECUTION.md`
- owner: Operator + Codex
- commit: 4ad4c8d71075731dd87c360e8b0d3d91d80b5518
- version acceptance: PASS. DIAGNOSTIC-KNOB option (b) added a startup warning
  and production code change, firing **v0.14.0** at Step 6. The disposition is
  not inherited from R-CLOSE's default.
- subject acceptance: PASS. Evidence candidate
  `ee9ee0f9ed96cb2cb7759c3c3e59fbf8f325ae1a` and later release commit
  `4ad4c8d71075731dd87c360e8b0d3d91d80b5518` are separate named fields.
  Authenticated run **30324186389**, attempt **1**, remains bound to the
  candidate; the release commit contains the admitted evidence and release
  reconciliation.
- publication decision: **no-release**. The named trigger is a separate
  operator authorization to advance `origin/main` and create the annotated
  `v0.14.0` tag. It has not fired. `origin/main` remains
  `0eff6e4c4987b7ebb138cf0bb1da6ebe8bd851b9`, no v0.14.0 tag exists, and no
  publication or live server session occurred.
- diff acceptance: PASS. The independently enumerated
  `0eff6e4c4987b7ebb138cf0bb1da6ebe8bd851b9..release` diff contains **37**
  paths, each classified exactly once in `STATE.md`. The five version
  authorities agree at 0.14.0; Cargo changed only the local `cored` version in
  `Cargo.lock`, with no dependency resolution movement.
- architecture acceptance: PASS. `ARCHITECTURE.md` records R8 ordering, the
  bounded warning-emitting diagnostic knob, and R3/R4's open-bottom scanner
  limitations. A4 remains open because a rewritten shell can bypass or falsify
  `/attest`; the editable-L1 controller residual remains open until scheduled
  server-side L2.
- hosted/local reconciliation: PASS. Both hosted shell legs report **224
  passed / 1 skipped** because the on-site production measurement test
  intentionally skips without protected corpora and a built `cored`. Both
  on-site lanes pass **225/225**; this is an expected environment distinction,
  not test drift.
- exact-release acceptance: PASS. At clean release commit
  `4ad4c8d71075731dd87c360e8b0d3d91d80b5518`, `./run ci-local` passed
  **20/20** with **125** workspace tests, **48** net tests (**23 + 25**), zero
  rustc/clippy/fmt/ShellCheck failures, locked Rust 1.78 green, Python 3.11
  **225/225**, all **101/101** pins exact, protected databases **2/2**, and
  golden **11/11**. The independent Python 3.12.13 lane passed **225/225** with
  **21/21** exact packages, and mandatory standalone golden passed **11/11**.
- version-check acceptance: PASS for all five 0.14.0 authorities. It correctly
  warns that the nearest tag is v0.13.0. Exact-tag confirmation remains
  inapplicable until the separately authorized tag-creation trigger fires; no
  tag was created to manufacture that result.
- preservation acceptance: PASS. Public `/v1/*` bodies, the SQLite schema,
  golden assertions, published releases, and the three valid retractions are
  unchanged. The canonical closing heading and R-CLOSE checkbox changed
  atomically in this audit record.
- golden-E2E delta: **0**. Hosted, exact-release matrix, and mandatory
  standalone golden remain **11/11** byte-identical.
