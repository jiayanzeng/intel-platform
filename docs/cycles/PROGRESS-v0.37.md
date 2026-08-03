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
