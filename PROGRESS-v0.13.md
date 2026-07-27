# PROGRESS-v0.13.md — append-only execution record

This file records v0.13 task and gate events after their implementation
commits exist. Each entry names the measured result, every applicable
acceptance criterion, the golden delta, and the real implementation commit.
Entries are append-only; corrections are new dated entries.

### 2026-07-27 · E0-GATE — clean worktree confirmed and v0.13 admitted

- owner: Codex
- commit: 5223d783b43c250102418163ef124f4e662b727b
- result: PASS for cycle activation only; E0 remains unchecked. The mandated
  opener found entering HEAD
  `466ebb3fc9736923110803e087acc798e417d084`, described as
  `v0.12.0-1-g466ebb3`, with local `main` and `origin/main` aligned (zero ahead
  / zero behind). The only worktree entry was the operator-supplied untracked
  `TASKS-v0.13-EXECUTION.md`. Annotated `v0.12.0` remained tag object
  `94d8215bc2151fecba1280dc793d3f5953cd8055`, peeled to
  `e5faf0c161a4256f33976664685653d8bd805d5d`.
- correction: implementation commit
  `5223d783b43c250102418163ef124f4e662b727b` committed only the supplied
  runbook, the `AGENTS.md` active-cycle header, and the empty append-only
  progress log.
- lifecycle acceptance: PASS. `./run cycle-check` reports active v0.13 open
  with ten closed execution runbooks. `./run checklist-audit` resolves the
  entering **99/99** checked tasks, reports the one existing v0.11 retraction
  separately, and finds zero exemptions. `git diff --check` passed.
- test acceptance: NOT RUN at this preparatory checkpoint; E0 owns the
  entering matrix and C1–C5 reproduction.
- golden-E2E delta: NOT MEASURED; no claim.
- protected artifact delta: NOT MEASURED; no protected or pinned file was
  touched.

### 2026-07-27 · E0 — entering state rebuilt and five findings confirmed

- runbook: `TASKS-v0.13-EXECUTION.md`
- owner: Codex
- commit: ed7249c1cf6429c6482592551a2a6e7dc996d9d3
- result: PASS. The permitted entering matrix passed **20/20** with **121**
  workspace Rust tests, **21** net tests, **205/205** Python 3.11 shell tests,
  zero rustc/clippy/fmt/ShellCheck failures, locked Rust 1.78 green,
  protected databases **2/2**, all **71/71** pins, and golden **11/11**. The
  initial sandboxed matrix is an environment non-result because eight shell
  controls were denied loopback/process access after 197 tests passed.
  Python 3.12 passed **205/205**, with both interpreters verifying **21/21**
  exact packages. Standalone golden repeated **11/11**.
- C1 acceptance: PASS as a confirmed release-blocking finding. A real `cored`
  over exactly two scratch documents returned an empty `/retrieve` context for
  a finance scope querying science-only text; direct
  `documents_by_ids(["science-b"])` nevertheless returned the science body,
  proving upstream ranking rather than final hydration supplied containment.
  `/attest` has no sector field and returned HTTP 200 with a violation naming
  the out-of-sector `IndexOnly` document; a nonexistent id returned HTTP 400.
  The cross-sector existence/match oracle is live. No `/retrieve` body leak
  reproduced.
- C2 acceptance: PASS as a confirmed coverage defect. The renamed
  `INGEST_FUZZ_LIMIT=17` production mutation exited 0 with the exact line
  `invariant-scan: R5 PASS: Production Rust has one private
  canonical-distance constant and no numeric canonical-distance call
  argument.` The original named-constant and numeric-call controls separately
  exited 1 with `R5 FAIL` at `sqlite.rs:33` and `sqlite.rs:207`.
- C3 acceptance: PASS as a confirmed harness defect. Sixteen enumerated shell
  test files contain no invariant-scan test. Replacing R4's provider-key regex
  with the never-matching `(?!)` pattern still exited 0 and reported **6/6**
  rules passing, proving `fail_before` is not executed.
- C4/C5 acceptance: PASS as confirmed findings. The architecture's endpoint
  table and HC2 prose contradict the unscoped `/retrieve` and `/attest`
  hydration paths. The crawler already shares one UA constant across both
  clients and `RobotsCache`, but that constant has the stale `0.1` version and
  `you@example.com`; there is no contact override or startup refusal.
- published-baseline acceptance: PASS. Annotated `v0.12.0` remains object
  `94d8215bc2151fecba1280dc793d3f5953cd8055`, peeled to
  `e5faf0c161a4256f33976664685653d8bd805d5d`; all 71 pins and both protected
  databases re-verified byte-exact. No C1–C5 row refuted.
- golden-E2E delta: **0**; the mandatory post-task run remained **11/11**
  byte-identical.
- cleanup: both disposable worktrees, their temporary database/log, and the
  spawned core process were removed; the live tree returned clean before the
  task record.

### 2026-07-27 · FAIL-BEFORE-EXEC — invariant controls made executable

- runbook: `TASKS-v0.13-EXECUTION.md`
- owner: Codex
- commit: b398f1266324eb43b4b77519f527d09e3b1eb1c9
- result: PASS. Registry schema 2 gives every R1–R6 rule a reconstructible
  exact-text mutation and expected failure substring. The scanner applies one
  control at a time in a fresh copy of the Git-tracked tree, runs only the
  owning rule, and requires exit 1 plus the recorded reason. The existing
  no-argument CI path executes this same self-test.
- preservation acceptance: PASS. All six former decorative `fail_before`
  strings are preserved byte-for-byte as `fail_before_note`; a dedicated test
  asserts the exact mapping. No R1–R6 matcher, pattern, scope outcome, or rule
  matching logic changed.
- positive-control acceptance: PASS. The real
  `./run invariant-scan --self-test` passed the clean R1–R6 scan and all
  **6/6** controls. Temporarily changing R4's provider-key regex to `(?!)`
  made the same command exit **1** with `SELF-TEST R4/1 FAIL: mutation did not
  make the rule fail`; restoring it returned the matrix to green. The new
  focused module passed **10/10**, including malformed-registry and
  unimplemented-rule exit-2 cases.
- CI acceptance: PASS. The corrected `./run ci-local` passed **20/20** with
  **121** workspace Rust tests, **21** net tests, **215/215** Python 3.11
  shell tests, warning-denied builds, clippy/fmt/ShellCheck, locked Rust 1.78,
  protected databases **2/2**, all **71/71** pins, and golden **11/11**.
  Python 3.12 independently passed **215/215** and verified **21/21** exact
  packages.
- integration note: an initial attempt to add the explicit flag to `run`
  tripped the protected authorization-surface pin and one evidence test, so it
  was a non-result. `run` was restored byte-exact at SHA-256
  `7afede56f13b5ee73d3f1dbe92910ce535908623676db21664409855c5ac006d`
  and is absent from the implementation diff.
- golden-E2E delta: **0**; the mandatory post-task standalone run remained
  **11/11** byte-identical.
- decision gate: PASS for this assurance task. The C1 body-boundary release
  blocker remains open for its ordered correction task.

### 2026-07-27 · THRESHOLD-BIND-GATE — production parameter seam found

- runbook: `TASKS-v0.13-EXECUTION.md`
- owner: Codex
- commit: 146feeb8fd4e205e9075b1c6c3f1428b26f8be0f
- result: BLOCKED before implementation, with the runbook-required follow-up
  recorded. A strict candidate R5 enumerated every production call to
  `assign_canonical_ids`, `assign_canonical_ids_tx`, and
  `rematerialize_canonical_ids_with_distance`, excluded the `#[cfg(test)]`
  seam, and required each distance argument to be exactly
  `DEDUP_MAX_DISTANCE`.
- gate measurement: the candidate exited **1** against unmodified HEAD with
  `invariant-scan: R5 FAIL: crates/store/src/sqlite.rs:685:
  assign_canonical_ids_tx distance argument must be DEDUP_MAX_DISTANCE; found
  max_distance`. The no-argument public maintenance method binds the constant
  at line 657, but its production parameterized helper forwards
  `max_distance` at the transaction call.
- disposition: Step 3 expressly forbids changing `crates/` to make its rule
  green and requires a source finding to be handled in a follow-up task. The
  candidate matcher was therefore not committed, no Rust source changed, and
  THRESHOLD-BIND remains unchecked. The disclosed
  THRESHOLD-SOURCE-SEAM follow-up owns only removal of the production
  parameter seam; the original Step 3 contract is unchanged and resumes after
  that correction.
- regression acceptance: PASS. The committed pre-rewrite invariant scanner
  remains green with R1–R6 and all **6/6** executable controls. `cycle-check`,
  `checklist-audit`, and `git diff --check` passed.
- golden-E2E delta: **0**; the mandatory post-gate run remained **11/11**
  byte-identical.

### 2026-07-27 · THRESHOLD-SOURCE-SEAM — production parameter removed

- runbook: `TASKS-v0.13-EXECUTION.md`
- owner: Codex
- commit: 0b266ade7e051b0cc394e7c598ef77d908b5adc8
- result: PASS. The public no-argument
  `rematerialize_canonical_ids` method now opens its transaction and calls
  `assign_canonical_ids_tx` directly with `DEDUP_MAX_DISTANCE`. The production
  `rematerialize_canonical_ids_with_distance(max_distance)` helper is absent.
- test-seam acceptance: PASS. Alternate distances remain reachable only
  through the `#[cfg(test)]` `assign_canonical_ids` method, which uses the same
  real transaction, materialization, commit, and rollback path. The focused
  `intel-store` suite passed **21/21**, including boundary, differential,
  missing-fingerprint rollback, ordering, update, and deletion controls.
- strict-rule acceptance: PASS. Re-applying the strict R5 candidate against
  the post-task source returned `R5 PASS`, overall **1/1**, exit **0**. All
  five production `assign_canonical_ids_tx` calls pass the single token
  `DEDUP_MAX_DISTANCE`; the one `max_distance` call is inside the test-only
  seam. No tool or registry file is present in the implementation diff.
- Rust acceptance: PASS. Warning-denied workspace check/test passed **121**
  tests; warning-denied net check and `intel-ingest` net tests passed
  **21/21**; clippy and fmt were clean; locked Rust 1.78 check/test passed
  **121** tests.
- golden-E2E delta: **0**; the mandatory post-task run remained **11/11**
  byte-identical.
- disposition: the gate-mandated source correction is complete.
  THRESHOLD-BIND may resume without an exemption or a source change in its
  rule-only commit.

### 2026-07-27 · THRESHOLD-BIND — R5 rebound to production call sites

- runbook: `TASKS-v0.13-EXECUTION.md`
- owner: Codex
- commit: 3928680edc05e116ef66a24e625e255b3b380fe6
- result: PASS. R5 enumerates production calls to
  `assign_canonical_ids`, `assign_canonical_ids_tx`, and
  `rematerialize_canonical_ids_with_distance`, excludes test-only Rust, and
  requires every distance argument to be the exact single token
  `DEDUP_MAX_DISTANCE`. Findings name the file, line, call, and offending
  token. The independent declaration half still requires exactly one private
  `DEDUP_MAX_DISTANCE: u32 = 16`.
- fail-before acceptance: PASS. The renamed-threshold control exited **1** with
  `R5 FAIL: crates/store/src/sqlite.rs:208: assign_canonical_ids_tx distance
  argument must be DEDUP_MAX_DISTANCE; found INGEST_FUZZ_LIMIT`. The two
  original controls also exited **1**: the second named constant failed at
  line 33, and the literal `16` call failed at line 207. Unmodified HEAD passed
  R5 at **1/1**.
- self-test acceptance: PASS. `./run invariant-scan --self-test` passed R1–R6
  plus **8** executable controls. The focused invariant module passed
  **10/10** under both Python 3.11.4 and 3.12.13. R5's claim and scope now
  describe call-site binding, not a naming convention.
- CI acceptance: PASS. `./run ci-local` remained **20/20** with **121**
  workspace Rust tests, **21** net tests, **215/215** Python 3.11 shell tests,
  warning-denied builds, clippy/fmt/ShellCheck, locked Rust 1.78, all
  **71/71** pins, protected databases **2/2**, and golden **11/11**.
- source acceptance: PASS. The implementation diff contains zero paths under
  `crates/`; the separately completed THRESHOLD-SOURCE-SEAM task owns the
  source correction.
- shape lesson: **a deny-list over source text is open at the bottom, and a
  repo-wide absence claim should be expressed as an allow-list over call sites
  wherever the call sites are enumerable.** R5 now enforces that lesson.
- golden-E2E delta: **0**; the mandatory standalone post-task run remained
  **11/11** byte-identical.

### 2026-07-27 · UA-CONTACT — crawler identity made required

- runbook: `TASKS-v0.13-EXECUTION.md`
- owner: Codex
- commit: d5fbcb2f6d50425c1953ea4c2e41f067179d2a68
- result: PASS. Net startup now requires `INTEL_CRAWLER_CONTACT` inside
  `build_robots_cache`; the structural `intel-platform` token cannot be
  supplied by the operator. The process installs one immutable identity,
  derives its advertised version from cored's `CARGO_PKG_VERSION`, and shares
  those exact bytes between both HTTP clients and `RobotsCache`.
- refusal acceptance: PASS against the real net binary. Unset and empty
  contacts exited **101** before binding with
  `INTEL_CRAWLER_CONTACT is required for a net-enabled harvester`.
  `ops@example.com`, `you@operator.test`, and `changeme` each exited **101**
  with an explicit placeholder refusal. A valid
  `crawler-operator@unit.test` value reached listener readiness; the process
  was then stopped immediately without a publisher request.
- identity acceptance: PASS. The cored net suite measured
  `intel-platform/0.12.0`, proving the version comes from the product crate.
  The loopback wire control captured byte-identical
  `intel-platform/0.12.0 (research prototype; contact:
  wire-contact@unit.test)` headers from the document and robots clients. The
  same installed string is passed to `RobotsCache`. The first wire attempt was
  a host-proxy non-result; with the repository-documented loopback `NO_PROXY`
  path, both requests reached the local listener.
- offline acceptance: PASS. A dedicated default-feature test proves
  `build_robots_cache` returns `None` without reading or requiring contact
  configuration. Workspace tests increased **121 → 122**. Net
  `intel-ingest` tests increased **21 → 22**, and the additional net-enabled
  cored suite passed **22/22**.
- documentation acceptance: PASS. `.env.example` carries the required empty
  setting, so an unchanged copy refuses safely; README and deploy guidance
  document the required value, rejected placeholders, and immutable product
  token.
- CI acceptance: PASS. `./run ci-local` remained **20/20** with **122**
  workspace Rust tests, **22** net tests, **215/215** shell tests,
  warning-denied builds, clippy/fmt/ShellCheck, locked Rust 1.78, all
  **71/71** pins, protected databases **2/2**, and golden **11/11**.
- golden-E2E delta: **0**; the mandatory standalone post-task run remained
  **11/11** byte-identical.

### 2026-07-27 · BODY-BOUNDARY — document hydration sector-scoped

- runbook: `TASKS-v0.13-EXECUTION.md`
- owner: Codex
- commit: 59924122a45e16294b7e135fc4930401b7b5b7cc
- result: PASS. Final `/retrieve` hydration and `/attest` both call
  `documents_by_ids_in_sectors` with their required request sector set.
  `CoreClient.attest`, the shipped `/v1/ask` path, and both live-verifier
  replays pass the subscription sectors. The unscoped `documents_by_ids`
  method is private and `#[cfg(test)]`; warning-denied production builds
  therefore prove that no production caller can name it.
- gate acceptance: PASS after two disclosed pre-implementation widenings.
  `CHANGELOG.md` is in scope because the task itself requires the changed
  error semantics there. `tools/verify_llm.py` is in scope because production
  caller inventory found two live-harness calls that must carry the new
  required sector argument. No schema, public `/v1/*` response field, test
  battery, or public result schema changed.
- fail-before/pass-after acceptance: PASS. Before the correction, the forged
  post-ranking retrieval-id control exited **101** because unscoped final
  hydration returned a technology row to a finance scope. The 16-token
  attestation control separately exited **101** because the same cross-sector
  `IndexOnly` row produced a successful violation response rather than an
  unknown-id refusal. After the correction, both focused controls passed,
  including empty-sector cases. The retrieval injection is deliberately at
  the exact final hydration boundary because the already-scoped ranking legs
  cannot make an endpoint-only happy path failure-capable.
- oracle and error-semantics acceptance: PASS. Out-of-sector and nonexistent
  attestation ids now both return HTTP **400** with the exact body
  `unknown context document id`; the body does not name the hidden document
  and no violation payload is returned. That indistinguishability is recorded
  here and in `CHANGELOG.md`.
- E0 wire acceptance: PASS against a rebuilt real `cored` over a fresh archive
  containing exactly `finance::a` and `science::b`. Finance-scoped retrieval
  for science-only `alpha` returned empty BM25, vector, fused, context, and
  suppressed lists. The 16-token `science::b` probe, `does-not-exist`, and an
  empty-sector probe all returned the same unknown-id refusal. A stale
  pre-rebuild binary first reproduced the old HTTP 200
  `violations:[{"doc_id":"science::b"}]` behavior; rebuilding the changed
  source produced the passing pair. All temporary wire-control files,
  databases, and processes were removed.
- CI acceptance: PASS. `./run ci-local` remained **20/20** with **124**
  workspace Rust tests, **22** net tests, **215/215** Python 3.11 shell tests,
  warning-denied builds, clippy/fmt/ShellCheck, locked Rust 1.78, all
  **71/71** pins, protected databases **2/2**, and golden **11/11**. Python
  3.12 independently passed **215/215** and verified **21/21** exact
  packages. Initial sandboxed standalone golden and Python 3.12 runs were
  loopback/process-denial non-results; identical permitted reruns passed.
- public-body acceptance: PASS. The real public `/v1/ask` golden path remained
  byte-identical, including four citations and one near-duplicate suppressed.
- golden-E2E delta: **0**; the mandatory standalone post-task run remained
  **11/11** byte-identical.
- disposition: the measured C1 release blocker is cleared.

### 2026-07-27 · R7-BODY-SECTOR — hydration boundary registered

- runbook: `TASKS-v0.13-EXECUTION.md`
- owner: Codex
- commit: c4f4d65e64229641e249c6beabe48d08f24a5425
- result: PASS. R7 cites `ARCHITECTURE.md:181-183`, enumerates production
  method and UFCS calls to both document-by-id hydration methods outside the
  store, permits only `documents_by_ids_in_sectors`, and separately refuses a
  public declaration of the unscoped `documents_by_ids`.
- fail-before acceptance: PASS. All three reconstructible controls exited
  **1** with concrete findings. Re-publication failed at
  `crates/store/src/sqlite.rs:289`; routing `/retrieve` back through the
  unscoped method failed at `apps/cored/src/main.rs:1126`; routing `/attest`
  back through it failed at `apps/cored/src/main.rs:1173`.
- clean/self-test acceptance: PASS. Clean R7 passed **1/1**. The complete
  scanner reported **7/7** and passed **11** executable controls. The focused
  invariant module increased **10 → 11** and passed under Python 3.11.4 and
  3.12.13.
- enforcement placement: the compiler is primary. BODY-BOUNDARY made the
  unscoped method private and unavailable in production; R7 is the cheaper
  secondary alarm for a future re-`pub`, not a regex substitute for
  visibility.
- CI acceptance: PASS. The final `./run ci-local` remained **20/20** with
  **124** workspace Rust tests, **22** net tests, **216/216** Python 3.11
  shell tests, warning-denied builds, clippy/fmt/ShellCheck, locked Rust 1.78,
  all **71/71** pins, protected databases **2/2**, invariant scan **7/7**, and
  golden **11/11**. Python 3.12 independently passed **216/216** and verified
  **21/21** exact packages. An earlier CI rerun stopped at checklist-audit
  because the R7 box had been checked before an implementation hash and
  progress receipt could exist; restoring the task to open for the acceptance
  run, then checking it in the implementation commit, followed the required
  two-commit protocol.
- source acceptance: PASS. The implementation diff contains no path under
  `crates/` or `apps/`.
- golden-E2E delta: **0**; the mandatory standalone post-task run remained
  **11/11** byte-identical.

### 2026-07-27 · RETRACT-HC2 — false v0.12 invariant claims retracted

- runbook: `TASKS-v0.13-EXECUTION.md`
- owner: Codex
- commit: a2d41c9d822fdae4ef017dae44aefa65551e4a53
- result: PASS. The retraction registry now records the false v0.12 R-CLOSE
  HC2 claim and, separately, the defective THRESHOLD-ONE correction. The first
  is corrected by BODY-BOUNDARY plus R7-BODY-SECTOR; the second is corrected
  by THRESHOLD-SOURCE-SEAM plus THRESHOLD-BIND.
- architecture acceptance: PASS. `/retrieve` and `/attest` request shapes now
  name sectors; the body-boundary sentence and HC2 table row describe the
  explicit core-SQL predicates, empty-set refusal, and private test-only
  unscoped seam that the source and R7 enforce. A4 remains open because a
  rewritten shell can bypass or falsify `/attest`; the editable-L1 residual
  remains open until the scheduled server-side L2 wrapper lands.
- historical-record acceptance: PASS. The
  `PROGRESS-v0.12.md` task diff is exactly **31 additions / 0 deletions**.
  Original task records and checked boxes were not edited.
- checklist acceptance: PASS before this task's checkbox and receipt were
  created. v0.12 remained **11/11** checked with its two retractions reported
  separately; the repository reported **106** checked tasks and **three**
  retractions across cycles, with zero exemptions.
- immutability acceptance: PASS. Annotated v0.12.0 tag object
  `94d8215bc2151fecba1280dc793d3f5953cd8055` still peels exactly to release
  commit `e5faf0c161a4256f33976664685653d8bd805d5d`; schema validation and
  `verify-artifacts` matched all **71/71** protected pins and both protected
  databases **2/2**. No path under `evidence/` or
  `config/protected-artifacts.json` changed.
- CI acceptance: PASS. `./run ci-local` remained **20/20** with **124**
  workspace Rust tests, **22** net tests, **216/216** Python 3.11 shell tests,
  warning-denied builds, clippy/fmt/ShellCheck, locked Rust 1.78, invariant
  scan **7/7** with **11** executable controls, all **71/71** pins, protected
  databases **2/2**, and golden **11/11**. Python 3.12 independently passed
  **216/216** and verified **21/21** exact packages.
- golden-E2E delta: **0**; the mandatory standalone post-task run remained
  **11/11** byte-identical.

### 2026-07-27 · NET-TEST-EXEC — cored net tests executed by CI

- runbook: `TASKS-v0.13-EXECUTION.md`
- owner: Codex
- commit: 2567f48aaba879011857db9177ebd60624678cc7
- result: PASS. The existing local and hosted `net` jobs now run
  `cargo test -p cored --features net --locked` with the required
  non-placeholder test contact after the existing
  `cargo test -p intel-ingest --features net --locked`.
- gate acceptance: PASS after a disclosed pre-implementation widening.
  Changing the hash-pinned `run` bytes required the forward
  `config/protected-artifacts.json` authorization pin to remain in scope.
  The new pin is
  `30475367926eff8b990b70dac6d17339c4e6ec0e685aa4b01f8d01a2c328b304`
  at **41104** bytes; the v0.12.0 tag and release commit retain the old
  `7afede56f13b5ee73d3f1dbe92910ce535908623676db21664409855c5ac006d`
  **40980-byte** launcher. No source under `apps/` or `crates/` changed.
- execution/count acceptance: PASS. `ci-local` stayed **20/20** jobs. The net
  job moved **22 → 46** executed tests: `intel-ingest` remained **22/22** and
  `cored` added **24/24**, including
  `net_build_refuses_missing_empty_and_placeholder_contacts` and
  `valid_contact_builds_one_versioned_identity_for_cache_and_clients`.
  The default-feature workspace count remained **124**.
- fail-before acceptance: PASS. In a disposable exported tree, inverting the
  placeholder assertion made the exact new cored command exit **101** with
  **23 passed / 1 failed**, naming
  `net_build_refuses_missing_empty_and_placeholder_contacts` and the required
  `INTEL_CRAWLER_CONTACT` refusal. Restoring the assertion made the same
  command pass **24/24**. Restored scratch and live source hashes matched.
- hosted acceptance: PASS by workflow-definition inspection, not live hosted
  execution. Publication and push are withheld, so no new GitHub run exists.
  The hosted net job contains the exact cored test step and the job identity
  inventory remains the same seven values: `core`, `lint`, `net`, `msrv`,
  `shell`, `golden`, and `drift`.
- net-gated inventory acceptance: PASS. The cored command lists and executes
  both direct `#[cfg(feature = "net")]` tests. The existing ingest command
  lists and executes the module-gated
  `both_live_clients_send_the_installed_user_agent_byte_identically`,
  `cross_origin_redirect_reads_and_honors_new_robots_before_fetching`, and
  `same_origin_redirect_reuses_the_cached_robots_policy` tests. All other
  `cfg(feature = "net")` occurrences select production code; no net-gated
  test item is unreached.
- control lesson: `cargo check --all-targets` proves a test compiles and says
  nothing about whether it runs. A `--features` gate splits the compiled and
  executed sets; only the feature-matched `cargo test` invocation executes
  that test.
- deferred cosmetic notes: R7's two call-site controls intentionally retain
  identical `expected_fail` strings, so their self-test output does not
  distinguish the two fresh-tree mutations. R6 intentionally retains an
  `expected_fail` value containing the full `invariant-scan: R6 FAIL:` prefix,
  which produces the doubled prefix in output. Both are recorded for a
  future site-specific-control pass and were not changed in v0.13.
- CI acceptance: PASS. Full permitted `./run ci-local` passed **20/20** with
  **124** workspace tests, the **46-test** net job, Python 3.11 **216/216**,
  invariant scan **7/7** with **11** controls, warning-denied builds,
  clippy/fmt/ShellCheck, locked Rust 1.78, all **71/71** pins, protected
  databases **2/2**, and golden **11/11**. Python 3.12 independently passed
  **216/216** and verified **21/21** exact packages. Initial sandboxed
  standalone golden and Python 3.12 runs were loopback/process-permission
  non-results; identical permitted reruns passed.
- golden-E2E delta: **0**; the mandatory standalone post-task run remained
  **11/11** byte-identical.

### 2026-07-27 · R-CLOSE — local release candidate recorded; publication pending

- runbook: `TASKS-v0.13-EXECUTION.md`
- owner: Codex
- commit: b18ece34424e03c531bc0e90f1a633262f252d12
- result: PENDING PUBLICATION. The complete verified local candidate is
  committed, but R-CLOSE remains unchecked because the separate operator
  publication trigger has not fired.
- version-choice acceptance: PASS. The operator authorized `v0.13.0` because
  UA-CONTACT landed; the `v0.12.1` alternative does not apply. Cargo, Python,
  FastAPI, STATE, README, and the newest changelog release heading read
  0.13.0. `Cargo.lock` changed only the local cored package version.
- release-facing correction acceptance: PASS. `CHANGELOG.md` says published
  v0.12.0 named an out-of-sector document in an attestation violation, that
  the live exposure was an existence-and-16-token-match oracle rather than a
  body leak, and that v0.13.0 closes it. The HC2 retraction says the claim was
  falsified by measurement. The out-of-sector/nonexistent
  `400 unknown context document id` semantics are recorded in CHANGELOG and
  this progress log.
- diff classification acceptance: PASS. The release diff contains **29**
  paths; the five `STATE.md` classes enumerate **29** paths with zero
  duplicates, and a sorted mechanical comparison produced no unmatched path.
  `PROGRESS-v0.12.md` is **93 additions / 0 deletions** relative to v0.12.0;
  no `evidence/` or `data/` path changed.
- architecture acceptance: PASS by source/enforcement reconciliation.
  `ARCHITECTURE.md`'s HC2 row matches the sector-scoped SQL hydration and
  private test-only unscoped seam. A4 explicitly remains open for a rewritten
  shell, and the L1 controller residual explicitly remains open until the
  scheduled server-enforced L2 wrapper lands.
- local matrix acceptance: PASS. `./run ci-local` passed **20/20** with
  **124** workspace tests, **46** net-job tests (**22** ingest + **24**
  cored), Python 3.11 **216/216**, invariant scan **7/7** with all **11**
  controls, warning-denied builds, clippy/fmt/ShellCheck, locked Rust 1.78,
  all **71/71** pins, protected databases **2/2**, and golden **11/11**.
  Python 3.12 independently passed **216/216** and **21/21** constraints.
- golden-E2E delta: **0**; the mandatory standalone candidate run remained
  **11/11** byte-identical.
- checklist acceptance: PENDING by operator directive. `checklist-audit`
  passes at **108** checked with **three** retractions; R-CLOSE is the sole
  unchecked v0.13 box. This is recorded as a gap, not reported as a pass.
- publication disposition: PENDING OPERATOR DECISION. The named trigger is a
  separate operator authorization to publish `v0.13.0`, and it has not fired.
  `version-check` passes at 0.13.0 while HEAD is ahead of v0.12.0, so no local
  tag was needed or created. No push or remote mutation occurred. Read-only
  verification returned `origin/main` unchanged at
  `466ebb3fc9736923110803e087acc798e417d084` and no v0.13.0 tag.

### 2026-07-27 · RE-MEASURE — blocked by hosted net-test failure

- runbook: `TASKS-v0.13-EXECUTION.md`
- owner: Codex
- commit: 0d611db0c12cf663901deb6783c1b1a143e1f8ef
- result: **FAIL / BLOCKED.** Operator-authorized workflow-dispatch run
  **30274895522**, attempt **1**, audited exact candidate
  `b18ece34424e03c531bc0e90f1a633262f252d12` from
  `candidate/v0.13.0` with `publish_evidence: true`. The run finished
  **Failure**, so the directive's stop condition fired and R-CLOSE was not
  resumed.
- branch/candidate acceptance: PASS. The exact candidate was pushed only to
  `candidate/v0.13.0`; the remote branch resolved to that commit and its
  workflow contains `cargo test -p cored --features net --locked`.
- hosted-run acceptance: FAIL. `core`, `lint`, `msrv`, both `shell` matrix
  legs, and `golden` passed; `net` failed; report-only `drift` was skipped.
  The cored invocation did execute **24** tests, but returned **23 passed /
  1 failed** and exit **101**. The failure was
  `tests::attest_endpoint_refuses_an_index_only_body`, whose startup path
  reported `cored refused to start: could not configure crawler identity:
  http: could not install crawler User-Agent`. Both cycle-added contact tests
  passed in that same hosted invocation.
- invariant-self-test acceptance: NOT REACHED. The `core` job passed, but its
  self-test log was not promoted as evidence after the hosted failure tripped
  the stop condition; no claim about **11** reconstructed hosted controls is
  made.
- receipt/bundle acceptance: FAIL / NOT ADMITTED. The run exposed seven
  receipt artifact names, preserving the configured seven-identity shape, but
  the failed `net` receipt cannot satisfy seven successful identities. No
  artifact was downloaded or committed, no receipt/bundle was admitted, and
  no release audit or re-derivation was run.
- pin-count acceptance: NOT CHANGED. The manifest remains **71** total pins:
  **69/69** evidence and **2/2** authorization surfaces. There is no new pin
  count because no failed-run evidence was admitted.
- remote immutability acceptance: PASS. Final read-only verification returned
  `origin/main` unchanged at
  `466ebb3fc9736923110803e087acc798e417d084`, the candidate branch unchanged
  at `b18ece34424e03c531bc0e90f1a633262f252d12`, and no local or remote
  `v0.13.0` tag.
- release-note acceptance: PASS for truthfulness, not for hosted closure.
  `CHANGELOG.md` now describes both hosted assurances as workflow definitions,
  cites failed run **30274895522**, and leaves green release-grade hosted
  verification open.
- golden-E2E delta: **0 at the last candidate measurement, 11/11**. No
  post-failure golden command was run because the operator required an
  immediate stop on any hosted job failure; this task's golden criterion is
  therefore NOT RE-RUN and is not claimed as a fresh pass.
- checklist disposition: RE-MEASURE remains unchecked; R-CLOSE remains
  unchecked. No source under `apps/` or `crates/`, no evidence file, no tag,
  and no publication state changed.

### 2026-07-27 · NET-TEST-EXEC addendum — first hosted execution exposed D1

- runbook: `TASKS-v0.13-EXECUTION.md`
- owner: Codex
- implementation commit:
  `2567f48aaba879011857db9177ebd60624678cc7`
- measured addendum: hosted workflow-dispatch run **30274895522**, attempt
  **1**, read `cargo test -p cored --features net --locked` from the net log
  and then `running 24 tests`. This upgrades the earlier workflow-definition
  inspection to direct execution evidence: all **24** cored tests executed.
  The first thing that coverage bought was discovery of D1:

  ```
  thread 'tests::attest_endpoint_refuses_an_index_only_body' (3254) panicked at apps/cored/src/main.rs:202:33:
  cored refused to start: could not configure crawler identity: http: could not install crawler User-Agent

  test result: FAILED. 23 passed; 1 failed; 0 ignored; 0 measured; 0 filtered out; finished in 2.71s
  ```

- disposition: NET-TEST-EXEC remains accepted and checked. It promised that
  the tests execute, not that newly reached behavior was already defect-free;
  its first hosted execution made the hidden race observable.

### 2026-07-27 · IDENTITY-INSTALL — atomic startup identity

- runbook: `TASKS-v0.13-EXECUTION.md`
- owner: Codex
- commit: d0b409a05597fc43356aeeb55a25ec597e358a85
- result: PASS. Crawler-identity initialization is atomic, an unrelated
  attestation test no longer performs startup identity installation, and the
  complete local definition of done is green.
- diagnosis acceptance: PASS; all three rows were confirmed against the
  entering source. D1 was a live `OnceLock::get()` then `set()` TOCTOU window.
  D2 was a live concern leak: test-only `AppState::new` reached unconditional
  robots-cache construction under `net`. D3 was a live coincidence: the test,
  local job, and hosted job all used `crawler-tests@unit.test`.
- race-closure acceptance: PASS. `get_or_init` performs the one atomic
  initialization and the implementation compares installed bytes with
  requested bytes. The lost-race branch was deleted. A mechanical source
  search returned no `USER_AGENT.set()`, `USER_AGENT.get()`, or
  `could not install crawler User-Agent` match in either gated source file.
- D2 disposition acceptance: PASS; option **(a)** was selected. `main()` now
  constructs the identity-backed robots cache and passes it into `AppState`.
  Test construction passes no cache. This keeps refusal at actual process
  startup and avoids creating a production/test-constructor difference that
  hides the startup path. The unrelated attestation test asserts the cache is
  absent and passes.
- concurrency acceptance: PASS. A barrier released **64** simultaneous
  identical installers; all succeeded and observed the same bytes. The
  subsequent differing installer returned exactly `http: crawler User-Agent
  is already configured with different bytes`.
- D3 acceptance: PASS. The valid-contact test now installs
  `identity-test@unit.test`, explicitly different from CI's
  `crawler-tests@unit.test`, then requests the CI bytes and verifies the exact
  different-bytes error. It no longer passes because unrelated literals
  coincide.
- varied-schedule acceptance: PASS. The host reports **12** logical
  processors. The full cored net suite passed **24/24** with
  `--test-threads=1`, `4`, and `64`, passed a repeated `64`-thread run, and
  passed the exact default CI invocation. The new ingest concurrency test
  raises that suite from **22/22** to **23/23**; the cored count remains
  **24/24**.
- refusal-semantics acceptance: PASS by execution against the real net binary.
  Missing and empty `INTEL_CRAWLER_CONTACT` each exited **101** with
  `INTEL_CRAWLER_CONTACT is required for a net-enabled harvester`;
  `ops@example.com` exited **101** with `must name a real operator contact,
  not placeholder "ops@example.com"`. The deliberately different initialized
  identity returned the unchanged different-bytes error. The branch
  discrimination is now measured: missing/empty → `is required`; placeholder
  → `must name a real operator contact`; different installed bytes → `already
  configured with different bytes`; the failed hosted run's `could not
  install crawler User-Agent` could only be the removed race loser.
- CI acceptance: PASS. With both `NO_PROXY` and `no_proxy` set to
  `127.0.0.1,localhost`, full `./run ci-local` passed **20/20** with **124**
  Rust workspace tests, **47** tests in the net job (**23** ingest + **24**
  cored), Python 3.11 **216/216**, invariant scan **7/7** with **11**
  controls, warning-denied builds, clippy/fmt/ShellCheck, locked Rust 1.78,
  all **71/71** pins, protected databases **2/2**, and golden **11/11**.
  Python 3.12 independently passed **216/216** and verified **21/21**
  constrained packages.
- environment qualification: the pre-existing ingest cross-origin wire test
  failed without the loopback proxy exclusion in both the current tree and an
  exported pre-change `f4e8195f2a15735efe8c387b1eb836faeb585752` tree.
  With the explicit exclusion, the focused test and complete **23/23** ingest
  suite passed. This is an environment qualification, not credited to the
  implementation.
- golden-E2E delta: **0**; the mandatory standalone run passed **11/11**
  byte-identically.
- record lesson: a green parallel test run is not evidence of race-freedom,
  and a process-global initialized from a test binary is order-dependent by
  default.

### 2026-07-27 · RE-MEASURE retry — authenticated hosted evidence

- runbook: `TASKS-v0.13-EXECUTION.md`
- owner: Codex
- commit: 394755eb00e5f0ef88f4fe01d352e06b4bb9e09f
- result: **PASS.** Release-grade hosted evidence now exists for exact
  candidate `7faaa4e1271616ff9390111c863d12fbcfa4d2fd` without publishing it.
- branch/candidate acceptance: PASS by remote execution and read-only
  verification. The operator-authorized force update changed only
  `candidate/v0.13.0`; the remote ref resolved to the exact candidate and its
  workflow contains `cargo test -p cored --features net --locked`.
- hosted-run acceptance: PASS. Workflow-dispatch run **30277584129**, attempt
  **1**, used `publish_evidence: true` and
  `audit_sha=7faaa4e1271616ff9390111c863d12fbcfa4d2fd`, completed **Success**
  in **50 seconds**, and produced exactly seven successful evidence
  identities: core, golden, lint, MSRV, net, shell Python 3.11, and shell
  Python 3.12. The report-only drift node remained skipped and emitted no
  eighth identity.
- hosted-net acceptance: PASS by direct log measurement, not job-status
  inference. The log records
  `cargo test -p intel-ingest --features net --locked` at **23 passed / 0
  failed**, followed by `cargo test -p cored --features net --locked`,
  `running 24 tests`, and **24 passed / 0 failed**. The cored run includes the
  formerly failing attestation test and both cycle-added contact tests; the
  ingest run includes the concurrent identity-installation control.
- invariant-self-test acceptance: PASS by hosted log measurement. The Python
  3.11 job ran `./run invariant-scan`, passed registered rules **7/7**,
  reconstructed R1 through R7 individually, and ended `SELF-TEST PASS (7/7
  rules, 11 controls)`.
- signed-evidence acceptance: PASS. Seven downloaded artifacts yielded
  fourteen receipt/bundle files; their ZIP digests matched the hosted values.
  Every receipt names run **30277584129**, attempt **1**, success, Linux, and
  both event and checked-out SHA
  `7faaa4e1271616ff9390111c863d12fbcfa4d2fd`. The files are committed under
  `evidence/ci-runs/30277584129-1/`.
- release-audit acceptance: PASS by execution. Release-posture
  `audit-deferred` required the expected candidate, repository, workflow,
  branch ref, GitHub-hosted runners, and attestations; it accepted **7**
  authenticated identities, rejected **0**, and measured **5 deferred / 2
  promoted**. `audit-deferred --rederive` passed with rows **7**, source
  dispositions **5**, triggers **7**, release grade, and attestations
  required. The resulting **34,038-byte** report hashes to
  `6d9ebf6d9463303235b12d6f7d8c88a3676de2361696cf5238b7336eb8468a52`.
- pin-count acceptance: PASS by manifest validation, artifact verification,
  and `evidence-report`. The fourteen hosted inputs plus one audit report add
  fifteen forward pins. The new count is **86 total**: **84/84 evidence** and
  **2/2 authorization surfaces**; protected databases remain exact **2/2**.
- local-definition acceptance: PASS by execution after evidence admission.
  With explicit loopback proxy exclusion, `./run ci-local` passed **20/20**
  with **124** workspace tests, **47** net tests (**23** ingest + **24**
  cored), Python 3.11 **216/216**, invariant scan **7/7** with **11**
  controls, all **86/86** pins, and golden **11/11**. Python 3.12 independently
  verified **21/21** constraints and passed **216/216** tests.
- remote-immutability acceptance: PASS by read-only verification.
  `origin/main` remains
  `466ebb3fc9736923110803e087acc798e417d084`; the v0.12.0 annotated tag
  object remains `94d8215bc2151fecba1280dc793d3f5953cd8055` and peels to
  `e5faf0c161a4256f33976664685653d8bd805d5d`; no local or remote v0.13.0
  tag exists. No tag, `main` push, or publication occurred.
- standing-constraint acceptance: PASS. No source changed during
  RE-MEASURE; `PROGRESS-v0.12.md` remains **93 additions / 0 deletions** from
  v0.12.0; public `/v1/*` bodies, SQLite schema, protected databases, A4, and
  the editable-L1 controller residual did not move. No live server session or
  L2 work occurred.
- golden-E2E delta: **0**. The post-admission `ci-local` golden and the
  mandatory standalone run each passed **11/11** byte-identically.
- checklist disposition: RE-MEASURE is checked. `checklist-audit` resolves
  **110** checked tasks with **three** retractions; R-CLOSE remains the sole
  unchecked task pending the named trigger of a separate operator
  authorization to publish `v0.13.0`.

### 2026-07-27 · Publication completion addendum — v0.13.0 release

- runbook: `TASKS-v0.13-EXECUTION.md`
- owner: Codex
- commit: 5ecd42bb6ca44f1588e53e493c67fee17d071b09
- result: **PASS.** UA-CONTACT landed, so the operator selected `v0.13.0`
  rather than the correction-only `v0.12.1` alternative. Directive 5 fired the
  separately named publication trigger.
- release-identity acceptance: PASS. Evidence candidate
  `7faaa4e1271616ff9390111c863d12fbcfa4d2fd`, hosted dispatch
  **30277584129** attempt **1**, release commit
  `5ecd42bb6ca44f1588e53e493c67fee17d071b09`, and annotated tag object
  `24a6a2aca52974891d120e0f2b295a93d629c1f7` are separate named fields in the
  canonical closing record.
- failed-run provenance acceptance: PASS. Run **30274895522**, attempt **1**,
  is recorded as measured, non-admitted evidence. Its cored net invocation ran
  all **24** tests and failed **23 passed / 1 failed** with `could not install
  crawler User-Agent`, surfacing the D1 identity-install race. No receipt or
  bundle from that run was admitted.
- diff-accounting acceptance: PASS by execution. `git diff --name-only
  v0.12.0` contains **44** paths, each classified exactly once in `STATE.md`;
  no path under `data/` changed. `PROGRESS-v0.12.md` remains **93 additions /
  0 deletions** from v0.12.0.
- release-document acceptance: PASS. `README.md`, `CHANGELOG.md`, `STATE.md`,
  all five release authorities, and the closing record agree on `v0.13.0`.
  Current release state records **86/86 pins**: **84/84 evidence files** and
  **2/2 authorization surfaces**. Historical entering-state references to 71
  remain historical rather than current-release claims.
- architecture acceptance: PASS by reconciliation. The invariant table still
  states A4 is open because a rewritten shell can bypass or falsify
  `/attest`, and the L1 residual is open because an edited controller can
  rewrite the client-side allowlist; L2 remains scheduled.
- definition-of-done acceptance: PASS at the exact release commit.
  `./run ci-local` passed **20/20** with Rust workspace **124**, net **47**
  (**23** ingest + **24** cored), Python 3.11 **216/216**, invariant scan
  **7/7** with **11** controls, all **86/86** pins, protected databases
  **2/2**, and golden **11/11**. Python 3.12 independently verified **21/21**
  constraints and passed **216/216**.
- checklist acceptance: PASS. R-CLOSE was checked in the same audit-record
  change that replaced `Pending Cycle closing record` with the sole canonical
  `Cycle closing record`; `checklist-audit` resolves **111** checked tasks and
  **three** retractions, and `cycle-check` resolves v0.13 as closed.
- golden-E2E delta: **0**. The release-commit matrix and mandatory standalone
  run both passed **11/11** byte-identically.
- carried-forward inputs: PASS. Four v0.14 candidates were recorded without
  implementation: file-and-line `expected_fail` controls; allow-list audits
  for R1/R3/R4/R6; a mandatory RE-MEASURE template step; and possible R8
  identity-before-bind coverage.
- standing constraints: PASS. No source, public `/v1/*` body, SQLite schema,
  protected evidence, prior tag, live server state, or L2 state changed.
