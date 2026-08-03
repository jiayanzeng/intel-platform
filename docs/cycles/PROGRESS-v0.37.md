# PROGRESS-v0.37.md — append-only execution record

This file records v0.37 task and gate events after their implementation
commits exist. Each entry names the measured result, every applicable
acceptance criterion, the golden delta, and the real implementation commit.
Entries are append-only; corrections are new dated entries.

### 2026-08-03 · ACTIVATE — v0.37 cycle activation

- owner: Codex
- runbook: `docs/cycles/TASKS-v0.37-EXECUTION.md`
- commit: 5884ef7754431ffe5017dc1f2fde5902aef2ed52
- result: PASS under the runbook's explicit ordering fallback. The
  pre-activation post-push worktree check classified the untracked v0.37
  runbook as an older open cycle and failed with exactly eight unchecked boxes
  plus a missing closing record. Activation therefore precedes completion of
  PUBLISH's repository append, while PUBLISH remains the first active step.
- declaration acceptance: PASS. `cycle-check` now resolves v0.37 solely from
  the AGENTS declaration and finds no active-runbook scope, retention,
  carry-forward, governed-boundary, or publication-record defect. Its only
  post-activation findings are the four Architecture trigger rows that still
  name v0.36; PUBLISH owns their fresh v0.37 measurements.
- author-contract correction: PASS. The supplied runbook omitted the canonical
  `Deferred means deferred` heading, its required action column, 25 immediately
  prior trigger subjects, and both governed artifact byte boundaries. The
  activation commit carries every prior subject, keeps every trigger and both
  byte boundaries unchanged, and rephrases the one cross-step measured-value
  acceptance against its same-worktree authority.
- retention acceptance: PASS. With the v0.37 runbook/progress pair staged in
  the Git-derived set, the configured excluded boundary advanced exactly
  through v0.35 and the retained set was exactly the v0.36-v0.37 task/progress
  pairs. Project-root `export-check` passed at **100 derived / 7 required / 154
  exported / 2,791,496 bytes / 2 retained cycles**.
- excluded boundary: `docs/cycles/{TASKS,PROGRESS}-v0.{[0-9],1[0-9],2[0-9],3[0-5]}{.md,.*.md,-*.md}`.
- golden-E2E delta: **0**. The first sandbox-denied loopback bind was a
  non-result; the permission-complete identical command passed **11/11**.
- protected-input acceptance: PASS. The three untracked amendment inputs
  remain untouched and untracked. No production source, dependency, protected
  byte, publisher configuration, version authority, tag, or remote ref moved
  during activation.

### 2026-08-03 · ACTIVATE — runbook-qualification correction

- owner: Codex
- runbook: `TASKS-v0.37-EXECUTION.md`
- commit: 5884ef7754431ffe5017dc1f2fde5902aef2ed52
- result: CORRECTION. The earlier entry's repository-relative `runbook` value
  is not the basename-qualified form consumed by `checklist-audit`; this
  append-only correction supplies the exact qualifier without changing the
  earlier measurement or implementation identity.
- checklist acceptance: PASS when evaluated with this correction; ACTIVATE
  resolves to the real activation commit.
- golden-E2E delta: **0**, unchanged at **11/11**.

### 2026-08-03 · PUBLISH — exact DR7 publication with one control bound deferred

- owner: Codex
- runbook: `TASKS-v0.37-EXECUTION.md`
- commit: 9474e92a05d78295e0c2dd096195608f35fc1f2b
- result: **PASS for the irreversible publication outcome; EXPLICITLY
  DEFERRED for the refuted historical multi-release checker claim.** Record
  commit `17ef4ec` contains the published State/header update and fresh
  governed observations; the named implementation commit forward-records the
  measured entry-point bound without changing any remote fact.
- DR7 preconditions: PASS immediately before push. Remote `main` was exact
  `f02379f03ccdfd1b019413234f2ad014d169fb04`; both release tags were absent;
  the ancestor check exited 0; local annotated objects
  `16ee7bcb2214859156edbceeb5e314ac1a67f39b` and
  `0fe42d7a6a86e94bb95a93a86b7a4b09917b97f4` peeled to the granted closing
  commits.
- publication acceptance: PASS. A non-force branch push moved only `main` to
  `e068cacc76685791c54ab47c84be6abbd592271d`; the subsequent non-force push
  created only v0.17.2 and v0.17.3. Fresh `ls-remote` resolved all direct and
  peeled refs to the five granted objects. Nothing was deleted or forced.
- hosted acceptance: PASS. Push-triggered run **30824053490**, attempt **1**,
  on exact `e068cacc76685791c54ab47c84be6abbd592271d` concluded success and all
  **9** blocking job identities passed.
- record acceptance: PASS. Both exact five-field post-push records are at
  column zero; the two earlier absence observations remain untouched. The
  current header says published and the v0.17.3 publication-epoch count resets
  to zero.
- lifecycle acceptance: PASS for newest v0.17.3 and **REFUTED as stated for
  both releases**. Direct `cycle-check` passes and reports
  `release=v0.17.3`. Entry-point audit proves `newest_closed_release()` returns
  only that release, so the same run never reads v0.17.2's older record. Fresh
  remote/object measurements independently match v0.17.2, but calling that a
  two-release executable result would be false. The affected historical
  reconciliation control is explicitly deferred under §2; no published claim
  was found false.
- planted-control acceptance: PASS unmodified at **14/14 rules / 81
  controls**. The required/fresh post-push, unpublished-observation precedence,
  and published-missing-record mutants still fail at their control sites.
- artifact acceptance: PASS. Schema v2 validates **2 artifacts / 332 pinned
  files**; consecutive complete checks matched the State archive and both
  databases in **0.10 s / 0.09 s real**.
- progress acceptance: PASS at the executable point. `progress-check` accepted
  the prior ACTIVATE record before this append.
- stop conditions: one author-side acceptance basis was refuted as described;
  no DR7 precondition, hosted run, published-record truth, entitlement,
  licensing, protected byte, dependency, payload, or boundary stop fired.
- golden-E2E delta: **0**. The permission-complete final PUBLISH worktree
  passed **11/11**; the initial sandbox-denied bind was a non-result.

### 2026-08-03 · E0 — entering-state reconstruction

- owner: Codex
- runbook: `TASKS-v0.37-EXECUTION.md`
- commit: 8ccabcac7823af18197ac09c80dfbe75904b6b2d
- result: PASS with measured refutations preserved. H1, H3, H7, H8, and H9
  were confirmed; H4 and H6 were refuted; H2 was confirmed at the entering DR7
  boundary and superseded by publication; H5 was partly confirmed and otherwise
  refuted by commit-exact export measurements. The complete dated table is in
  the runbook and its measured evidence is summarized in State.
- H3 acceptance: PASS. A test-only nonce seam pre-created the exact candidate
  directory and deterministically reproduced the entering
  PID-plus-nanoseconds constructor's caught `AlreadyExists` panic, **1/1**. No
  production code moved.
- H4 acceptance: PASS as a refutation. The live figures are **14 rules / 81
  controls**, **9 exemptions**, **3 retractions**, and pre-E0 checklist **289
  checked / 3 retracted / 280 matched / 280 resolved / 9 exemptions**, not the
  hypothesis's 287/3/278+9.
- H5/H6 acceptance: PASS as measured corrections. The v0.35 retained pair is
  **148,051 bytes**. Exact exports are **2,858,294 / 151 / 2** at entering
  `e068cacc…` and **2,746,484 / 151 / 2** at activation `5884ef77…`; the
  source-review 2,901,790/154 was a worktree containing three untracked inputs.
  Pre-record State is **345,139 bytes**, with one permanent-tail marker, two
  absence observations, and two later post-push records.
- H7/C8 acceptance: PASS. Runtime introspection enumerated exactly six public
  routes, all with `response_model=None`; five handlers return dictionaries and
  `/v1/brief` returns `PlainTextResponse`. C8 therefore selects response-model
  introduction.
- standing-gate acceptance: PASS. Permission-complete `ci-local` passed all
  **22/22** identities; invariant self-test passed **14/14 rules / 81
  controls**; Python 3.11 and 3.12 each passed **368/368** with identical
  population summaries; artifacts matched **2 databases / 332 pinned files**.
  The first 3.12 attempt was a sandbox-denied non-result and is not counted.
- protected-input acceptance: PASS. The three amendment inputs remain
  untouched and untracked. No dependency, production source, protected byte,
  public payload, version authority, or remote ref moved in E0.
- stop conditions: none. The measured hypothesis refutations are findings, not
  stop conditions; no architecture, gate, or corpus-integrity condition fired.
- golden-E2E delta: **0**. The final permission-complete worktree passed
  **11/11**; the preceding sandbox-denied bind was a non-result.

### 2026-08-03 · TEST-ISOLATION — collision-proof identity scratch directory

- owner: Codex
- runbook: `TASKS-v0.37-EXECUTION.md`
- commit: f5c9c235b546012a2d99d131a79c873f56ee465e
- result: PASS. Atomic `create_dir` now retries only `AlreadyExists` while
  incrementing an attempt component; every other filesystem error remains an
  immediate failure. This is the std-only C9 construction and adds no
  dependency.
- forced-collision acceptance: PASS. The executable witness pre-created
  attempt zero for a fixed nonce, called the same constructor, and proved it
  created attempt one. The focused test passed **1/1**.
- repeated-suite acceptance: PASS. The complete `intel-store` suite ran under
  default parallelism **10 consecutive times**. Each run passed **24 unit + 1
  license + 3 identity-measure + 0 doctests**, including the parser-produced
  SEC measurement, with **0** `AlreadyExists` failures.
- placement acceptance: PASS. No production code moved; the implementation and
  control are confined to `crates/store/tests/sec_identity_measure.rs`.
- architecture/dependency acceptance: PASS. The change is std-only, affects no
  runtime path or type boundary, and preserves every architecture invariant.
- stop conditions: none. The forced witness and every repeated suite run were
  green; no corpus, protected-byte, dependency, or scope stop fired.
- golden-E2E delta: **0**. The final permission-complete worktree passed
  **11/11**.

### 2026-08-03 · STATE-ARCHIVE — structural history through v0.35

- owner: Codex
- runbook: `TASKS-v0.37-EXECUTION.md`
- commit: 882c698d607b9a36c253c0f3b0a316772063c90b
- result: PASS. C10 retains the current v0.37 publication epoch, the
  immediately prior v0.36 body, and the permanent tail. DR8 moved the older
  v0.29–v0.35 bodies into the one new structural archive.
- scope-gate correction: PASS and bounded. The supplied scope forbade the
  validator that owns the exact structural-archive registry, making DR8's pin
  acceptance inexpressible. The gate was widened only for registration and a
  focused control of `STATE-through-v0.35.md`; no prefix admission was added.
- byte-identity acceptance: PASS. The implementation parent's **258,658-byte**
  v0.35–v0.29 slice is byte-identical to the archive. The measured
  **48,303-byte prefix + 258,658-byte archive + 43,964-byte tail** reconstructs
  the **350,925-byte** pre-cut State at SHA-256
  `7db0bc5ff34b35da174805914c1725248357b746d7f0783e16d5264ee7cf5cf5`.
- pin acceptance: PASS. The new structural pin binds **258,658 bytes** at
  SHA-256 `fb1114f68755cbb8fc5d1fdad9e2ec114bf2604871102fa84d280f2bc90191a7`.
  Schema validation reports **2 artifacts / 333 pinned files** and the focused
  validator suite passed **20/20**, including an unregistered sibling refusal.
- artifact acceptance: PASS. Two complete checks matched both archives, every
  other pin, and **2/2** protected databases in **0.09 s / 0.10 s real**.
  Manifest size is **193,830 / 1,048,576 bytes**; neither growth trigger fired.
- live-State acceptance: PASS. Post-record State is **94,681 / 453,741 bytes**
  and retains the permanent tail, both post-push records, the publication
  header, the v0.37/v0.36 bodies, and every lifecycle/version parser field.
  `cycle-check`, `version-check`, and `progress-check` passed.
- delivered-export acceptance: PASS. The final project-root worktree export is
  **2,558,258 bytes / 154 files / 2 retained cycles**, **41,742 bytes** below
  C10's target and **441,742 bytes / 14.72% / 3.08 cycles** below the ceiling.
  The exact implementation commit, excluding the three untracked inputs, is
  **2,514,762 / 151 / 2**, **85,238 bytes** below target and **485,238 bytes /
  16.17% / 3.38 cycles** below the ceiling.
- governed review-export measurement: tree=`882c698d607b9a36c253c0f3b0a316772063c90b`; bytes=`2514762`
- protected-input acceptance: PASS. The three amendment inputs remain
  untouched and untracked; no protected database, observation-grade byte,
  dependency, production code, payload, or accepted boundary moved.
- stop conditions: none. C10's target was met and no hard ceiling, artifact,
  scope, corpus, or architecture stop fired.
- golden-E2E delta: **0**. The final permission-complete worktree passed
  **11/11**.

### 2026-08-03 · DOMAIN-MANIFEST — executable public response domains

- owner: Codex
- runbook: `TASKS-v0.37-EXECUTION.md`
- commit: 3e593448032085ba664c237a6dfeba4454bf624d
- result: PASS. C8 selected and completed the byte-identical model-introduction
  branch for all six public routes; production shell code moved, so Step 5's
  hosted condition is satisfied.
- scope-gate correction: PASS and bounded. Multi-line response-model
  decorators invalidated `audit_deferred.py`'s one-line textual route parser,
  while the supplied scope omitted that tool. The gate now admits only its
  AST-based decorator discovery; no receipt, disposition, or audit outcome
  changed. The three source-rederivation controls passed on Python 3.11 and
  3.12.
- derived-manifest acceptance: PASS. `tools/domain_manifest.py` reads the
  actual FastAPI OpenAPI result, requires exactly six modeled `/v1/*` routes,
  and recursively records each declared status/media field domain. The
  **47,135-byte** v0.17.4 baseline contains **6 routes / 31 status-media
  variants / 112 field occurrences**; a fresh derivation reports **0
  differences**.
- registered-control acceptance: PASS. R15 executes the production manifest
  checker. Its control-site mutants added a `Signal.kind` enum value, removed
  `SignalsResponse.graph`, and changed `SearchHit.rank` from number to string;
  each failed before the unmutated tree passed. Full self-test totals are
  **15/15 rules / 84 controls** with **0** hand-typed absolute finding lines.
- byte-identity acceptance: PASS. The complete configured-subscription witness
  exercised **10 successful response records** across all six routes and both
  configured subscribers where applicable. Its canonical envelope remained
  exactly **6,869 bytes**, SHA-256
  `dfec8ff81d68526dd5468ce22660be9d7678c6a8fdd8e52d6ac921c83371cef3`,
  before and after response-model introduction.
- shell acceptance: PASS. Permission-complete Python 3.11 and 3.12 each passed
  the identical **370/370** collected population with no skips and one accepted
  `StarletteDeprecationWarning`; constraints and dependencies did not move.
- classification acceptance: PASS. The executable manifest diff is empty and
  the byte witness proves no `/v1/*` route, response field, value domain,
  entitlement, or licensing outcome moved. DR9 clause 2 therefore has a
  measured patch-compatible input rather than a prose assertion.
- protected-input acceptance: PASS. The three amendment inputs remain
  untouched and untracked; no protected database, observation-grade byte,
  dependency declaration, hosted workflow, golden input, or remote ref moved.
- stop conditions: none. C8 succeeded byte-identically and no §3.4,
  architecture, scope, dependency, protected-byte, or corpus-integrity stop
  fired.
- golden-E2E delta: **0**. The final permission-complete worktree passed
  **11/11**.

### 2026-08-03 · RE-MEASURE-FIX — pre-install invariant topology

- owner: Codex
- runbook: `TASKS-v0.37-EXECUTION.md`
- commit: b39965e146973688624a6db0d8a0e28603d5d1ba
- finding: Hosted run **30832624982**, attempt **1**, on exact candidate
  `2e5921f0d0d3f4d64bde56b95325216d33caa59b` passed **8/9** blocking
  identities and failed only Python 3.11's pre-install invariant step. R15's
  subprocess imported FastAPI/Pydantic before the workflow's unchanged install
  phase and exited without a domain difference. The run was not retried and
  immutable ref `codex/v0.37-evidence-2e5921f` was not moved.
- topology-repair acceptance: PASS. The blocking manifest derivation now uses
  only Python AST over the actual application decorators and Pydantic type
  annotations. The installed shell witness independently compares that result
  with FastAPI's runtime OpenAPI output, including the pinned native 422
  domain.
- pre-install acceptance: PASS. Python 3.11 with site packages disabled passed
  **15/15 rules / 84 controls**. The dependency-free manifest check passed at
  **6 routes / 112 field occurrences**.
- runtime acceptance: PASS. The installed derivation/runtime comparison had
  **0 differences**; the combined payload/runtime witness passed on Python
  3.11 and 3.12 without changing the **370-test** collected population.
- remote acceptance: PASS as a recorded failed candidate. The first ref was
  absent immediately before one non-force creation; remote `main`, v0.17.2,
  v0.17.3, and every unrelated ref remained unchanged. RE-MEASURE remains open
  and requires a fresh candidate/ref rather than reuse, force, or retry.
- stop conditions: none. The failure is a correctable hosted-topology finding,
  not a dependency addition, protected-byte movement, entitlement/licensing
  movement, or publisher-wire event.
- golden-E2E delta: **0**. The post-repair authoritative local pipeline passed
  **11/11**.

### 2026-08-03 · RE-MEASURE — exact candidate passed 9/9

- owner: Codex
- runbook: `TASKS-v0.37-EXECUTION.md`
- commit: 128475f05912c6bf3b76f31e28b9296d8dded6d3
- condition/result: PASS. Step 4 moved production shell code, so hosted
  verification ran. Exact audited candidate
  `99012c86dcdda8ea32f1b1afa016f793118e9087` has complete hosted evidence on
  a fresh immutable ref after the first-candidate topology finding was fixed.
- local acceptance: PASS. The exact candidate passed the permission-capable
  `ci-local` matrix at **22/22** jobs, including **15/15 rules / 84 controls**,
  Python 3.11 at **370/370**, both Rust floor pairs, all protected artifacts,
  and golden **11/11**. The preceding sandbox-denied loopback bind is recorded
  as a non-result, not selected as the gate outcome.
- candidate/ref acceptance: PASS. Immediately before the only push for this
  candidate, `git ls-remote` exited **0** with no entry for fresh ref
  `refs/heads/codex/v0.37-evidence-99012c8`. One non-force push created exactly
  that ref at the candidate. The failed first-candidate ref stayed exact and
  was never moved or retried.
- hosted-job acceptance: PASS. Workflow-dispatch run **30834599847**, attempt
  **1**, targeted the declared SHA/ref and completed `success`. All **9/9**
  blocking identities passed and persisted **9 receipts / 9 Sigstore
  bundles**; dependency drift was the sole declared report-only skip. The run
  was dispatched once and not retried.
- population acceptance: PASS. Local Python 3.11 and 3.12 each passed
  **370/370**. Each hosted lane collected **370**, passed **369**, and skipped
  only the named, reasoned, `on_site` production-audit node. Both direct
  `tools/test_population.py` comparisons derived `equivalent=true` and
  `equivalent_passed=370`.
- remote acceptance: PASS. Final direct readback kept the two evidence refs at
  their respective exact candidates, remote `main` at `e068cacc…`, and the
  v0.17.2/v0.17.3 annotated objects and peeled targets unchanged. No unrelated
  ref moved.
- protected-input acceptance: PASS. The three amendment inputs remain
  untouched and untracked; no workflow, dependency, protected byte,
  publisher-wire path, entitlement/licensing outcome, serialized value
  domain, release tag, or publication authority moved.
- stop conditions: none. The fresh candidate satisfied Step 5 and did not
  consume or broaden DR7.
- golden-E2E delta: **0**. Hosted and final permission-complete local golden
  passed **11/11**.

### 2026-08-03 · R-CLOSE — v0.17.4 tagged local close

- owner: Codex
- runbook: `TASKS-v0.37-EXECUTION.md`
- commit: 514bec6c95e47017fafab452775ac4b8824ca6b9
- result: PASS. DR9 selects patch **v0.17.4** because explicit response models
  and the release-baselined domain manifest expose and validate the existing
  serialized contract without adding a route or observable named runtime
  surface. The untagged release parent is this checked closing commit's
  immediate parent; the annotated tag is created locally only after this tree
  exists.
- DR9 clause-2 acceptance: PASS. The complete configured witness is
  byte-identical at **6,869 bytes**, SHA-256
  `dfec8ff81d68526dd5468ce22660be9d7678c6a8fdd8e52d6ac921c83371cef3`,
  and the manifest diff is empty across **6 routes / 31 status-media variants
  / 112 field occurrences**. No payload byte, field, field-domain value,
  entitlement, or licensing outcome moves.
- version acceptance: PASS. `version-check` derives **0.17.4** from all five
  executable authorities, with **3** offline-MSRV pins at raw 1.78.0, **22**
  current offline-MSRV restatements at 1.78, and **3** current release
  restatements at 0.17.4. Cargo changes only cored's lockfile package value.
- evidence-anchor acceptance: PASS. Exact candidate
  `99012c86dcdda8ea32f1b1afa016f793118e9087`, run `30834599847` attempt 1,
  passed **9/9** blocking identities and persisted **9 receipts / 9 Sigstore
  bundles**. Both local populations pass **370/370**; both hosted comparisons
  derive equivalent **370**-test populations with one named, reasoned,
  `on_site` skip; hosted and local golden pass **11/11**.
- governed review-export measurement: tree=`514bec6c95e47017fafab452775ac4b8824ca6b9`; bytes=`2674055`
- governed-export acceptance: PASS. The exact release parent produced **104
  derived / 7 required / 158 exported / 2,674,055 bytes**, retained exactly
  v0.36–v0.37, and excluded both protected byte classes. At the latest
  +143,456-byte adjacent-cycle denominator, **325,945 bytes / 10.86% / 2.27
  cycles** remain below the fixed ceiling. The later records put the release
  parent 74,055 bytes above C10's already-met Step 3 target; this is carried as
  a v0.38 capacity finding, not represented as a ceiling breach.
- artifact-boundary acceptance: PASS. Assembled closing State measures
  **106,707 / 453,741 bytes**. The manifest remains **193,830 /
  1,048,576 bytes**, leaving **854,746 bytes / 842.11 cycles** at +1,015
  bytes/cycle. The release-parent gate matched all **333** pins and both
  protected databases.
- deferral acceptance: PASS. Every active row carries its latest dated v0.37
  observation. G6 is completed: R15's added-enum, removed-field, and
  changed-type mutations each fail at the actual serialization authority.
- invariant acceptance: PASS. The exact release-parent full gate passed
  **15/15 rules / 84 controls** with **0** hand-typed absolute finding-line
  fields. The Step 1A publication lifecycle controls remain unmodified and
  pass on the mixed two-published/one-unpublished-local state after tagging.
- divergence acceptance: PASS. Published v0.17.3 reset the epoch count to
  **0**. v0.37 introduces no measured runtime-behavior or public-surface
  difference, so no new count starts and neither divergence trigger fires.
- publication acceptance: PASS at DR10's boundary. Direct pre-close readback
  found no local or remote v0.17.4 tag. No push, `main` movement, or release-tag
  publication occurred. The local annotated tag targets only the closing
  commit after it exists; the immediate audit child owns the exact closing-tree
  export field before handoff.
- checklist acceptance: PASS at the assembled closing worktree:
  **295 checked / 3 retracted / 286 matched / 286 commits resolved / 9
  exemptions**; v0.37 is nonempty at **8/8/8**.
- full local acceptance: PASS **22/22** jobs at the exact release parent. Both
  shell lanes pass **370/370** with the accepted warning, Rust 1.78 and net
  1.86 pass, net 1.85 produces the required locked-ICU refusal, and every
  protected artifact matches. The immediate audit child re-executes the full
  gate over the delivered head.
- golden-E2E delta: **0**. The release-parent embedded and standalone pipeline
  pass **11/11**; the assembled closing-worktree standalone run and final
  audit-child embedded run are reported at their executable points.
- scope acceptance: PASS. Only declared release authorities and active
  State/runbook/progress/Architecture records move. No dependency graph,
  protected byte, fixture, observation, closed-cycle document, publisher
  request, workflow, `main`, or remote release ref moves.
