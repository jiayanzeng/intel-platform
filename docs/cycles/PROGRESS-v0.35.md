# PROGRESS-v0.35.md — append-only execution record

This file records v0.35 task and gate events after their implementation
commits exist. Each entry names the measured result, every applicable
acceptance criterion, the golden delta, and the real implementation commit.
Entries are append-only; corrections are new dated entries.

### 2026-08-02 · ACTIVATE — v0.35 preparatory cycle activation

- owner: Codex
- commit: 5d51d4106e31a4f67215c6e8e66c19488ff29a46
- result: PASS for the runbook-defined preparatory activation. The sole
  pre-activation worktree item was the operator-supplied untracked v0.35
  runbook; the tracked tree was clean. The implementation commit contains that
  runbook, the `AGENTS.md` declaration moving the active cycle to v0.35, this
  progress skeleton, and the required `repomix.config.json` retention edit.
- author-contract acceptance: PASS after forward correction. The staged real
  `cycle-check` exposed one author-side schema defect before the runbook's first
  commit: the governed artifact byte-boundary authority was absent. Runbook
  amendment r1 restores the unchanged `STATE.md` 453,741-byte and
  `config/protected-artifacts.json` 1,048,576-byte authorities. The checker,
  boundaries, and trigger texts were not changed.
- entering-ref acceptance: PASS. Delivered v0.34 HEAD
  `d8d20b81b9ea9027dada74ce047a7cd92815e9f3` has immediate parent closing
  implementation `6a19d31dd00143fc85a5e6c157dceb90ce40e946`. Direct remote
  inspection resolved `main` and peeled `v0.17.1` to
  `f02379f03ccdfd1b019413234f2ad014d169fb04`, the tag ref to annotated object
  `14912f134e45277e2b4fd10b7f5bf8b4900ca20d` of local Git type `tag`, and the
  v0.34 evidence ref to exact candidate
  `1117dc6db6ec0e55e8c8f078ca8059628f9f8262`. The published closing commit's
  immediate parent remains release commit
  `7a621e39a069a1ef26438e841e7bb1ca2f34165b`.
- retention rejection acceptance: PASS. Before the retention edit, the staged
  real checker emitted exactly:
  `cycle-check: ERROR: repomix.config.json: review-export retention pattern for v0.35 must be 'docs/cycles/{TASKS,PROGRESS}-v0.{[0-9],1[0-9],2[0-9],3[0-3]}{.md,.*.md,-*.md}' to agree with the tracked retained-cycle set; found ['docs/cycles/{TASKS,PROGRESS}-v0.{[0-9],1[0-9],2[0-9],3[0-2]}{.md,.*.md,-*.md}']`.
  The implementation advances the retained set to v0.34-v0.35.
- lifecycle acceptance: EXPECTED PENDING at the preparatory checkpoint. After
  the activation commit, the real checker rejects exactly 28 stale-cycle
  observations: four trigger-bearing Architecture rows and 24 active deferral
  rows still honestly name v0.34. Step 1 owns their measured v0.35 rewrite;
  no structural, scope, retention, carry-forward, boundary, amendment, or
  activation-anchor defect remains. Artifact boundaries were read directly as
  `STATE.md` **243,402 / 453,741 bytes** and manifest **192,042 / 1,048,576
  bytes**.
- test acceptance: NOT RUN as a post-activation complete `ci-local` result;
  Step 1 owns the full 20-job entering gate, clean Python populations, exact
  delivered-tree export, and every G1-G7 construction.
- golden-E2E delta: **0**. The sandboxed attempt was a bind-denied environment
  non-result; the identical permission-complete standalone run passed **11/11**.
- publisher/ref acceptance: PASS. Activation used repository-local commands and
  direct read-only remote Git inspection only. It issued no publisher request,
  ran no scheduler, service, or model-profile command, and created, moved, or
  deleted no remote ref.

### 2026-08-02 · E0 — entering-state reconstruction and G1–G7

- owner: Codex
- commit: a5adc0e277291fcd6c85160f66f1aacc07e363cf
- result: PASS. The implementation refreshes every governed observation,
  records all seven construction-backed dispositions, and changes only
  `STATE.md`, `ARCHITECTURE.md`, and the active runbook.
- entering-state acceptance: PASS. The sole initial worktree item was the
  operator-supplied untracked runbook. Exact delivered v0.34 audit child
  `d8d20b81b9ea9027dada74ce047a7cd92815e9f3` immediately follows closing
  implementation `6a19d31dd00143fc85a5e6c157dceb90ce40e946`. Direct remote
  inspection resolved `main` and peeled `v0.17.1` to closing commit
  `f02379f03ccdfd1b019413234f2ad014d169fb04`, its immediate parent to release
  commit `7a621e39a069a1ef26438e841e7bb1ca2f34165b`, annotated tag object
  `14912f134e45277e2b4fd10b7f5bf8b4900ca20d` to Git type `tag`, and the v0.34
  evidence ref to exact candidate
  `1117dc6db6ec0e55e8c8f078ca8059628f9f8262`. Historical tags `v0.8.0` and
  `v0.10.2` were absent.
- delivered-export acceptance: PASS after one DNS-denied bootstrap non-result.
  Project-root `./run export-check` in an isolated exact-tree clone at
  `d8d20b81b9ea9027dada74ce047a7cd92815e9f3` emitted **100 derived / 7
  required / 151 exported / 2,559,695 bytes / 2 retained cycles**, confirming
  both the reviewer's figure and audit-child identity with protected content
  excluded.
- G1 acceptance: PASS by independent construction of every real registry
  mutant. **67/68** expected target lines were unique. All **40** R12 targets
  were named control-site marker lines. R1/1's target occurred twice; its
  minimum unique anchor is four lines beginning at the planted helper with
  target offset three. The complete per-rule table is in State, and the real
  self-test rejected all **12/12 rules / 68 controls**.
- G2 acceptance: PASS by execution of both branches. v0.35 tracked and fallback
  constructions agree on the boundary through v0.33. A skipped v0.36 tracked
  construction remains through v0.33 while its arithmetic fallback extends
  through v0.34. Production passes the Git-derived set; two named test call
  sites reach fallback, and R12's `retention-skipped` construction relies on
  the divergence. The unchanged trigger is therefore satisfied and Step 3
  owns the criterion correction.
- G3 acceptance: PASS by derivation. Published **77,014**, **77,862**,
  **86,946**, and **79,962 bytes/cycle** denominators all belong to the former
  three-cycle-retention epoch. Delivered v0.34 is the sole point after the
  retention change, so no adjacent same-kind post-retention pair exists and
  none was synthesized.
- G4 acceptance: PASS from the executable workflow, launcher, lockfile, and
  installed crate manifests. Hosted `net` pins Rust 1.91; `msrv` pins Rust
  1.78 over the offline workspace; report-only `drift` writes its MSRV text to
  the step summary and nothing consumes it. The locked net chain reaches seven
  ICU 2.2.0 crates that each declare Rust 1.86. The seven-crate offline
  `intel-compliance` graph contains no ICU edge; the present-tense dependency-
  gate prose is a rejected-dependency counterfactual stated as fact.
- G5 acceptance: PASS without a trigger edit. The four Architecture plus 24
  active deferred rows classify as **21 event-shaped / 5 authorization-shaped
  / 2 self-discharging**. State names every authorization-shaped and self-
  discharging subject and the classification rule.
- G6 acceptance: PASS from `r10_report`: **local_jobs=20, local_checks=24,
  blocking_jobs=6, hosted_checks=23**, 45 exemptions, no finding. Step 5 moves
  only `local_jobs` to 22 and `blocking_jobs` to 8 because the two lanes reuse
  the existing canonical net check.
- G7 acceptance: PASS by the locked edge
  `cored → intel-ingest → reqwest 0.11.27 → url 2.5.8 → idna 1.1.0 →
  idna_adapter 1.2.2 → icu_* 2.2.0`; no corresponding offline compliance edge
  exists.
- trigger acceptance: PASS. All four Architecture rows and all 24 active
  deferred rows carry an ISO-dated v0.35 observation; trigger text is
  unchanged. The retained-arithmetic trigger is honestly recorded as fired.
- Python acceptance: PASS. Clean exact 21-package Python 3.11.4 and 3.12.13
  lanes each collected/passed **352**, failed **0**, skipped **0**, and emitted
  the same one accepted warning. `tools/test_population.py` independently
  derived `collected=352`, `equivalent=true`, and `equivalent_passed=352`.
  The first sandboxed 3.11 lane was a loopback/`ps` permission and pre-refresh
  non-result, not the passing measurement.
- artifact acceptance: PASS. Schema validation found **2 artifacts / 332
  pinned files**; two complete checks matched every pin and both protected
  databases in **0.11 s / 0.10 s real**. No protected byte changed.
- gate acceptance: PASS with the Step 1 checkbox still open. `./run ci-local`
  passed all **20/20** jobs, checklist **268 / 3 / 268 / 268**, registered
  invariants **12 rules / 68 controls**, zero Rust warnings, constrained Python
  3.11.4 **352/352**, embedded golden **11/11**, all protected artifacts, and
  the activation progress mapping.
- golden-E2E delta: **0**. The mandatory standalone post-task run passed
  byte-identical **11/11** after the final record and checkbox update.
- publisher/ref acceptance: PASS. Step 1 issued no publisher request, ran no
  scheduler, service, or model-profile command, changed no dependency,
  production source, public response, release value, or protected byte, and
  created, moved, or deleted no remote ref.

### 2026-08-02 · ANCHOR — mutant-derived planted-control locations

- owner: Codex
- commit: 457f53384451febfd95609d9c8fb8da0f1de5747
- result: PASS. Registry schema v4 replaces all 68 `expected_line` integers
  with authored `expected_anchor` literals and optional zero-based line offsets.
  The self-test resolves each anchor exactly once only after constructing its
  mutant, then independently builds the expected finding.
- geometry acceptance: PASS. All **68** mutant anchors are unique: **43** are
  one-line and **25** are multi-line; **8** carry nonzero offsets. R1/1 uses a
  nine-line anchor at offset 3. All 40 R12 controls retain their pre-existing
  named control-site marker, with R12/39 extending it by one unchanged line.
  No registered anchor is wholly supplied by its `replace_with`.
- non-unique acceptance: PASS through the real `./run invariant-scan` entry
  point. Temporary R1 registries emitted exactly `expected_anchor occurs 0
  times in constructed mutant; expected exactly 1` and `expected_anchor occurs
  2 times in constructed mutant; expected exactly 1`, each at
  `crates/store/src/sqlite.rs`, and each exited 1.
- wrong-line acceptance: PASS. A constructed R7 checker moved its real finding
  from line 410 to line 411; self-test exited 1 and printed both the missing
  expected line and the observed one-line-late finding.
- mutant-boundary acceptance: PASS. A temporary R3 anchor existing only in
  `replace_with` resolved and passed **1/1 rule / 1 control**. A temporary R7
  anchor existing only in the original file was absent after mutation and
  received the zero-occurrence rejection.
- registered-suite acceptance: PASS at **12/12 rules / 68 controls**; no
  control was added, removed, or weakened. The focused
  `shell/tests/test_invariant_scan.py` suite passed **27/27**.
- absolute-line acceptance: PASS. `config/invariant-rules.json` contains **0**
  `expected_line` or other hand-typed absolute finding-line fields; there are
  no survivors to name.
- gate acceptance: PASS with the ANCHOR checkbox still open. `./run ci-local`
  passed **20/20**, checklist **268 / 3 / 268 / 268**, zero Rust warnings,
  constrained Python 3.11.4 **357/357**, embedded golden **11/11**, every pin,
  and both protected databases.
- trigger acceptance: PASS. The unchanged planted-line trigger fired on the
  schema change and its assigned work completed. The active row records that
  Step 7 will move the subject into the dated Deferred completions table.
- golden-E2E delta: **0**. The mandatory standalone post-task run passed
  byte-identical **11/11**.
- publisher/ref acceptance: PASS. ANCHOR changed only the registered lifecycle
  tool, registry, focused tests, State, and active runbook. It issued no
  publisher request, ran no scheduler, service, or model-profile command,
  wrote no protected byte, and changed no dependency, production source,
  release authority, or remote ref.

### 2026-08-02 · ONE-RETENTION — one Git-derived retained-cycle authority

- owner: Codex
- commit: fc448a3770b0d18495b0ea7bb957b4d015c27270
- result: PASS. Option A was feasible and selected. The formatter now requires
  `retained_cycle_paths`; its arithmetic `None` branch is deleted. Every live
  caller supplies a set derived by `expected_retained_cycle_paths` for that
  construction's committed Git tree.
- fixture acceptance: PASS. Cycle fixtures initialize Git and commit their
  runbook/progress documents before deriving the configured retention pattern.
  The autouse arithmetic substitute is gone. A skipped-cycle control obtains a
  deliberately stale pattern from a separate consecutive tracked construction
  and proves those bytes fail in the skipped tracked construction.
- failure-control acceptance: PASS. R12 adds one real optional-parameter
  mutation and rejects it as `optional-retained-set-parameter`, moving the
  registry for a stated reason to **12 rules / 69 controls** and R12 to **41**
  controls. No hand-typed absolute finding line was introduced.
- criterion acceptance: PASS. The active deferral row is forward-corrected to
  govern an omitted retained set or a live caller-supplied non-Git-derived set.
  The prior wording remains truthfully recorded as fired in Step 1. Amendment
  r2 clarifies that the no-edit instruction protects the closed v0.34 record;
  no historical measurement was changed.
- entry-point acceptance: PASS. Real `cycle-check` accepted the exact v0.35
  boundary through `3[0-3]`. An isolated current-tool construction containing
  only the stale `3[0-2]` pattern exited 1 and named both the required exact
  pattern and the stale found value.
- focused acceptance: PASS. `shell/tests/test_cycle_check.py` passed **85/85**;
  focused R12 self-test passed **1/1 rule / 41 controls**.
- gate acceptance: PASS with the ONE-RETENTION checkbox still open. `./run
  ci-local` passed **20/20**, checklist **268 / 3 / 268 / 268**, zero Rust
  warnings, registered invariants **12 rules / 69 controls**, constrained
  Python 3.11.4 **357/357**, embedded golden **11/11**, all **332** pins, and
  both protected databases.
- golden-E2E delta: **0**. The mandatory standalone post-task run passed
  byte-identical **11/11**.
- publisher/ref acceptance: PASS. ONE-RETENTION changed only the lifecycle
  checker, invariant harness and registry, focused tests, State, and active
  runbook. It issued no publisher request, ran no scheduler, service, or
  model-profile command, wrote no protected byte, and changed no dependency,
  production source, public response, release authority, or remote ref.

### 2026-08-02 · POST-LEVER BASIS — first two-cycle-epoch denominator

- owner: Codex
- commit: 2a34a2cc9452837607fb88c9ce4570d7ce67faaa
- result: PASS. Exact Step 3 audit child
  `cd9a119f309096d2d715a54fde6302a5f95362d0` exported **2,551,288 bytes /
  151 files / 2 retained cycles**, with **100 derived / 7 required** paths and
  both protected byte classes excluded. One sandboxed npm-DNS failure was a
  non-result; the identical permission-complete project-root run passed.
- series acceptance: PASS. State restates every append-only governed field and
  the checker's last-field-per-cycle series with retention depth at every
  point. The newest adjacent governed pair is v0.34→v0.35, **2,527,180 [2]
  → 2,551,288 [2] = +24,108 bytes/cycle**. Published 77,014, 77,862,
  86,946, and 79,962 denominators are marked epoch-stale because all were
  measured under depth three.
- reclaim acceptance: PASS by a controlled same-tree export pair. Depth two
  emitted **2,551,288 bytes / 151 files**; the depth-three counterfactual
  emitted **2,649,296 bytes / 153 files** and added only the v0.33 runbook and
  progress pair. The real reclaim is **98,008 bytes**, refuting the supplied
  97,951-byte figure by **57 bytes**.
- boundary acceptance: PASS. The export's **448,712-byte** remainder is
  **18.61 cycles** at +24,108. Exact-tree State is **256,218 / 453,741**;
  exact delivered v0.34 State was 243,402, making its post-retention delta
  +12,816 and its **197,523-byte** remainder **15.41 cycles**. State is nearer
  by **3.20 cycles**. Each denominator is one adjacent pair and carries the
  checker's unbounded-representativeness warning.
- lever acceptance: PASS. The measured post-retention basis does not require
  an immediate lever, so none was selected. No archive, `REQUIRED_PATHS`
  change, manifest exclusion, or depth-one retention change was made.
- golden-E2E delta: **0**. The mandatory standalone post-task run passed
  byte-identical **11/11**.
- publisher/ref acceptance: PASS. POST-LEVER BASIS changed only State and the
  active runbook. It issued no publisher request, ran no scheduler, service,
  or model-profile command, wrote no protected byte, and changed no code,
  dependency, public response, release authority, or remote ref.
- governed review-export measurement: tree=`cd9a119f309096d2d715a54fde6302a5f95362d0`; bytes=`2551288`

### 2026-08-02 · NET-FLOOR — executable Rust 1.86 boundary

- owner: Codex
- commit: d4e60eb5e5997d996f5d13c8204a85886230fd53
- result: PASS. The exact negative command `RUSTFLAGS="" rustup run 1.85.0
  cargo check -p cored --features net --locked --all-targets` exited nonzero
  on the locked packages' declared MSRV, including
  `idna_adapter@1.2.2 requires rustc 1.86` and the ICU 2.2.0 declarations.
  The identical `rustup run 1.86.0` command exited **0** after compiling the
  complete graph. Neither result was a registry, network, lockfile, or
  unrelated compile failure; the measured net floor is genuinely **1.86**.
- dependency acceptance: PASS. `cargo tree` measured `cored → intel-ingest →
  reqwest 0.11.27 → url 2.5.8 → idna 1.1.0 → idna_adapter 1.2.2 → icu_*`
  2.2.0. `intel-compliance` remains a seven-crate offline graph with no ICU
  edge. `AGENTS.md` now states that measured net edge and keeps
  `texting_robots` only as the rejected-dependency counterfactual.
- parity acceptance: PASS. The launcher and hosted workflow each add a
  success lane and a failure-capable refutation lane. R10 reports
  **local_jobs=22, local_checks=24, blocking_jobs=8, hosted_checks=23**, with
  no new residual exemption or finding. The four topology figures are now
  pinned only by a separately named current-topology test; exemption-base
  derivation remains count-independent.
- topology acceptance: PASS. The exact hosted identity set is now **9**:
  `core`, `golden`, `lint`, `msrv`, `net`, `net-msrv-1-85`,
  `net-msrv-1-86`, and both shell matrices. Step 6 therefore requires
  **9 receipt JSON files / 9 Sigstore bundles**. The workflow parser's
  exact-set test and each dynamic deferred-audit success, rejection, and
  verifier population assertion now derive that figure; historical seven-job
  evidence is unchanged.
- version acceptance: PASS. Before and after the edit, `version-check`
  reported **3 executable pins / 22 offline-MSRV current restatements / 3
  release-version current restatements**. The package-scoped net `rustup run`
  commands are not offline `--workspace --locked` authorities, so no registry
  pattern changed.
- protected-byte acceptance: PASS. Pre-proposal schema validation and complete
  artifact verification passed. Exactly the existing `run` pin changed, to
  **43,907 bytes / `a05562dd1612678aa7c78f1aa8efe09e4c2e4392175c2363b25778577f36b818`**.
  The manifest is **192,370 bytes**, delta **+328**, with **2 artifacts / 332
  pinned files**. Both `artifacts[]` entries, every admission record, and
  `tools/model_profiles.py` at **28,297 bytes / `1920761c…`** are
  byte-identical. The workflow is **32,533 bytes / `74a1dc3d…`**.
- focused acceptance: PASS. The invariant and deferred-audit suites passed
  **68/68**. Registered invariant self-test remains **12 rules / 69 controls**
  with **0** hand-typed absolute finding-line fields.
- gate acceptance: PASS with the Step 5 checkbox still open. `./run ci-local`
  passed all derived **22/22** jobs, checklist **268 / 3 / 268 / 268**, zero
  Rust warnings, constrained Python 3.11.4 **358/358** with the same one
  accepted warning, embedded golden **11/11**, all **332** pins, and both
  protected databases.
- golden-E2E delta: **0**. The mandatory standalone post-task run passed the
  same byte-identical **11/11** assertions.
- publisher/ref acceptance: PASS. NET-FLOOR issued no publisher request, ran
  no scheduler, service, or model-profile command, changed no dependency
  resolution, production source, public response, value domain, release
  value, or publication ref, and changed only the authorized existing `run`
  protected pin.

### 2026-08-02 · NET-FLOOR-HOSTED-GATE — syntactic counterpart did not execute 1.85

- owner: Codex
- commit: a71813d01c225d05933aa57b24f3fd507b22c17e
- result: BLOCKED at Step 5 decision-gate clause 3. This forward correction
  supersedes the preceding local-only completion claim without rewriting it.
  R10 classified a hosted command as the counterpart of the explicit local
  1.85 construction even though the hosted command executed the repository's
  1.91 override.
- candidate/ref acceptance: PASS for the authorized mutation, not for hosted
  evidence. Candidate `d33c251d477aa4b1ee6b5b2ebd531b1fda428e99`
  was clean at tree `21718887d19bf1e2115d6fc8bb5348d0a72adb4b`.
  Direct pre-push `ls-remote` exited zero with no entry for fresh ref
  `refs/heads/codex/v0.35-evidence-d33c251`; the operator explicitly
  authorized that exact candidate to that one ref. The sole push created it,
  and immediate plus final readback each resolved it to the exact candidate.
  The ref was not reused, forced, moved, or repurposed.
- hosted measurement: FAIL. Workflow-dispatch run **30746841903**, attempt
  **1**, targeted the exact candidate and evidence ref with evidence signing.
  Eight of nine blocking identities passed, including the named 1.86 success
  job; `live-fetch MSRV refutes (1.85)` failed because its `cargo check`
  exited **0** after compiling the complete locked net graph. The report-only
  dependency-drift job skipped under its declared condition.
- root-cause measurement: the toolchain action installed and set default
  1.85.0, then logged `toolchain '1.91-x86_64-unknown-linux-gnu' is currently
  in use (overridden by .../rust-toolchain.toml)`. The job invoked bare
  `cargo`, which therefore used 1.91. Its success is not a 1.85 pass and does
  not refute the locally measured floor; it proves the named hosted lane did
  not execute the construction it claimed.
- parity acceptance: FAIL. Local `rustup run 1.85.0 cargo ...` and hosted bare
  `cargo ...` canonicalized as counterparts despite different effective
  toolchains. The decision-gate clause 3 classification gap is therefore
  measured at the real hosted entry point. No lane, checker, exemption, or
  claim was changed to route around it.
- stop disposition: PASS. Step 5 is unboxed and marked BLOCKED; Step 6 is
  ineligible. The failed run was not retried, no receipt or bundle was accepted
  as release-grade evidence, and the created evidence ref remains immutable.
- local measurements: PASS but insufficient for task completion. Exact-
  candidate Python 3.11.4 and 3.12.13 populations each collected/passed
  **358**, failed **0**, skipped **0**, with the same one accepted warning.
  The mandatory post-finding standalone golden passed **11/11**, delta **0**.
- published-state acceptance: PASS. Final direct readback kept remote `main`
  and peeled `v0.17.1` at
  `f02379f03ccdfd1b019413234f2ad014d169fb04`, annotated tag object
  `14912f134e45277e2b4fd10b7f5bf8b4900ca20d`, and the failed-evidence ref at
  its exact candidate. No tag or published ref moved.
- scope acceptance: PASS after the stop. The blocker implementation changes
  only State and the active runbook. No publisher request, scheduler, service,
  or model-profile command ran; no production source, dependency resolution,
  protected byte, public response, value domain, release value, lane, checker,
  or exemption changed.

### 2026-08-02 · STEP-5A-MSRV-EVIDENCE-GATE — hosted 1.78 lane ran 1.91

- owner: Codex
- commit: 3b586eeb02346714727da18e4ae5597e88d5409c
- result: BLOCKED at Step 5A decision-gate clause 4 before correction or
  classification. The operator-supplied r4 prompt required measurement of all
  three affected jobs at their real hosted entry points before implementation;
  existing run **30746841903**, attempt **1**, supplies that measurement.
- `msrv` measurement: the action input was **1.78** and the action installed
  and defaulted that toolchain, but then emitted verbatim:
  `info: note that the toolchain '1.91-x86_64-unknown-linux-gnu' is currently
  in use (overridden by '/home/runner/work/intel-platform/intel-platform/rust-toolchain.toml')`.
  The job subsequently invoked bare `cargo check --workspace --locked` and
  bare `cargo test --workspace --locked`; both completed successfully. The
  hosted job did not execute the 1.78 toolchain in this run.
- net-floor measurement: `net-msrv-1-86` declared **1.86.0**, emitted the same
  active-1.91 override note, invoked bare package-scoped cargo, and passed; its
  earlier green is a **non-result** for the 1.86 floor. `net-msrv-1-85`
  declared **1.85.0**, emitted the same override note, and its bare cargo check
  compiled on 1.91; the wrapper then emitted `Rust 1.85 unexpectedly built the
  net path; the declared 1.86 floor is false.` and failed. Because the command
  did not execute 1.85, that failure is also a **non-result** for the floor.
- decision-gate acceptance: PASS for the required stop. The new measurement is
  recorded forward, but no judgment is made about whether any immutable
  published record is false. The existing `STATE.md` v0.10/G2 sentence was not
  edited, no retraction was proposed, and the explicit local 1.78 result remains
  valid local evidence rather than being conflated with hosted evidence.
- amendment acceptance: PASS after one author-contract correction. Exact r4
  text and the complete Step 5A contract are now in the active runbook. The
  checker requires machine-readable uppercase `Step 5A`. Its first execution
  also rejected A9's stored Step 5 `3 / 22 / 3` quantity; amendment r5 replaces
  that cross-step stored value with a same-tree before/after population
  relation. No historical measurement changed.
- implementation acceptance: NOT PERFORMED because clause 4 stopped the step.
  No hosted/local selection or version-proof command, R10 identity or finding,
  planted control, `AGENTS.md` rule, `run` byte, manifest pin, lane, exemption,
  or classification changed. A1–A12 remain pending after operator adjudication.
- failed-evidence preservation: PASS. Run **30746841903** was not retried and
  none of its receipts or bundles was accepted. Ref
  `codex/v0.35-evidence-d33c251` was not reused, moved, forced, or deleted. No
  push or hosted dispatch occurred under Step 5A.
- local record gates: PASS. `cycle-check`, `checklist-audit`, `version-check`,
  and `git diff --check` passed. `version-check` derived **3 executable pins /
  22 offline-MSRV current restatements / 3 release-version current
  restatements**; no version authority or classifier moved.
- golden-E2E delta: **0**. The mandatory standalone post-gate run passed
  byte-identical **11/11**.
- scope acceptance: PASS. The blocker implementation changed only State and
  the active runbook. The operator-supplied untracked amendment file remains
  untouched. No protected byte, dependency, production source, public surface,
  remote ref, publisher request, scheduler, service, or model-profile command
  changed.
