# PROGRESS-v0.36.md — append-only execution record

This file records v0.36 task and gate events after their implementation
commits exist. Each entry names the measured result, every applicable
acceptance criterion, the golden delta, and the real implementation commit.
Entries are append-only; corrections are new dated entries.

### 2026-08-03 · ACTIVATE — v0.36 preparatory cycle activation

- owner: Codex
- runbook: `docs/cycles/TASKS-v0.36-EXECUTION.md`
- commit: f44681c1dce0c5c2efc0d3fb4a30900fdb4163f5
- result: PASS for the runbook-defined activation after the Step 0e ordering
  exception. The pre-activation `ci-local` lifecycle lane rejected the
  v0.36-specific task path while v0.35 remained declared and treated the
  untracked v0.36 runbook as an older incomplete cycle. Activation therefore
  committed first; AUTONOMY remains a separate subsequent implementation.
- author-contract correction: PASS. The supplied runbook had no
  machine-readable declared-scope table, used a noncanonical deferred heading
  while omitting all 24 immediately prior trigger subjects, and omitted the
  governed artifact byte-boundary authority. The activation commit adds the
  required scope metadata and exact release-authority set, carries forward all
  prior subjects/triggers, retains the supplied v0.36-specific deferred rows,
  and carries the existing `453741` / `1048576` boundaries byte-identically.
- retention acceptance: PASS. With the new runbook/progress pair staged in the
  Git-derived set, the unchanged checker required
  `docs/cycles/{TASKS,PROGRESS}-v0.{[0-9],1[0-9],2[0-9],3[0-4]}{.md,.*.md,-*.md}`
  and rejected the prior boundary through v0.33. The committed pattern retains
  exactly v0.35-v0.36 and excludes execution cycles through v0.34.
- lifecycle acceptance: EXPECTED PENDING at activation. After scope,
  retention, carry-forward, and boundary corrections, the real checker
  reported only its pre-commit activation-anchor conditions plus the required
  stale-observation population: four Architecture rows and 32 active deferral
  rows do not yet name v0.36. E0 owns their dated measurement and rewrite.
- golden-E2E delta: **0**. The sandboxed first run was a loopback-bind
  permission non-result; the permission-complete identical command passed
  **11/11**.
- protected/publisher/ref acceptance: PASS. Activation did not change a
  protected byte, production source, dependency, publisher/scheduler
  configuration, version authority, tag, or remote ref. The operator-supplied
  amendment remains untracked and untouched.

### 2026-08-03 · AUTONOMY — stopped at lifecycle-contract conflict

- owner: Codex
- runbook: `docs/cycles/TASKS-v0.36-EXECUTION.md`
- commit: 1c67a81a6fa0bca48e03a8127550499efd0a5520
- result: **BLOCKED** under §3 stop-and-report condition 3. Step 0 cannot
  satisfy its clean-`ci-local` acceptance under the runbook's simultaneous
  instructions, so its checkbox remains open and every later step remains
  dependency-blocked.
- ordering measurement: FAIL before activation in the way Step 0e anticipated.
  With v0.35 still declared, `ci-local` rejected the v0.36 task path and
  treated the new runbook as an incomplete older cycle. The documented
  exception activated v0.36 first.
- mirror/control experiment: PASS before the gate. The unmirrored real scan
  failed on missing Operations START/END markers. After the exact mirror and
  generalized R6 were assembled, the focused test and full self-test passed
  **12/12 rules / 74 controls**, including the planted missing-START and
  mismatch cases. This unaccepted implementation was restored after the gate;
  the restored standing suite passes **12/12 rules / 73 controls**.
- exact acceptance entry point: FAIL. The permission-complete `./run ci-local`
  passed release-version consistency, then stopped at active-cycle consistency
  with exactly two defects: the verbatim authority block's
  `TASKS-v0.36-EXECUTION.md` literal is forbidden below AGENTS §0, and the
  v0.17.2 local-tag descendant requires a post-push record that cannot
  truthfully exist while the release is unpublished and has no hosted
  publication run.
- artifact/export acceptance: PASS. Two complete artifact checks matched all
  **332** pins and both databases in **0.12 s / 0.13 s real**; `run` remained
  **45,409 bytes** at its pinned hash. Project-root export-check passed at
  **100 derived / 7 required / 152 exported / 2,724,915 bytes / 2 retained
  cycles**, exactly v0.35-v0.36, with both protected byte classes excluded.
- operator-local acceptance: NOT LANDED. The requested adjacent clarification
  was assembled and measured, then restored with the rest of the unaccepted
  Step 0 implementation; retaining it while the task is blocked would present
  partial implementation as accepted work.
- prohibited alternatives: NOT TAKEN. No post-push record was fabricated, no
  local tag was deleted, no release was published, the required verbatim block
  was not weakened, and scope-forbidden `tools/cycle_check.py` was not changed.
- golden-E2E delta: **0**. The post-restore permission-complete command passed
  **11/11**.
- amendment acceptance: PASS. The operator-supplied untracked amendment remains
  untouched.

### 2026-08-03 · AMENDMENT-A1R2 — autonomy/lifecycle runbook correction

- owner: Codex
- runbook: `docs/cycles/TASKS-v0.36-EXECUTION.md`
- commit: 6a3c108dd19378549a503c220c8917c7b34055ea
- result: PASS. The amendment-only commit changes the active runbook, scope,
  dependency gates, hypotheses, and amendment disclosures; it changes no
  implementation, protected byte, closed-cycle document, tag, or remote ref.
- author-side correction: PASS. Step 0's authority block now names no cycle
  document; Step 1A owns truthful unpublished-local-close lifecycle semantics;
  scope allows the exact remaining implementation surfaces without a winning
  overlapping forbid; E0 now owns H1–H13 and exactly two untracked amendments.
- disclosure acceptance: PASS. The runbook contains exactly one amendment
  heading and dated entries for Steps 0, 1, 1A, and 7. Direct `cycle-check`
  reports no undisclosed-amendment or declared-scope error.
- interim lifecycle acceptance: EXPECTED PENDING. Direct `cycle-check` reports
  exactly `publication post-push record required` for unpublished v0.17.2 and
  no other defect, matching A1r2 §5. Step 1A, not this amendment commit,
  discharges that truthful failure.
- golden-E2E delta: **0**. The permission-complete command passed **11/11**.
- amendment inputs: PASS. Both reviewer-supplied amendment files remain
  untracked and untouched.

### 2026-08-03 · AUTONOMY — corrected authority installation

- owner: Codex
- runbook: `docs/cycles/TASKS-v0.36-EXECUTION.md`
- commit: b38579ddd0e8080b786701da8436afc05c54a799
- result: PASS under A1r2's explicit interim verification lane. The
  cycle-neutral authority block is present exactly once in each governing
  document, the two copies are byte-identical, and the adjacent
  `operator-local` clarification makes execution responsibility explicit.
- mirror/control acceptance: PASS. Generalized R6 derives both authority
  marker names and requires one ordered pair per document. Its real
  missing-START and mismatch mutations fail; the complete registered scan
  passes **12/12 rules / 74 controls**.
- placement acceptance: PASS. `CONTRACT_CYCLE_PATH_RE` finds only
  `TASKS-v0.36-EXECUTION.md` and `PROGRESS-v0.36.md` at AGENTS lines 16–17,
  both above the line-25 §0 boundary; the new block contributes no match.
- interim lifecycle acceptance: EXPECTED PENDING. Direct `cycle-check` reports
  exactly the missing v0.17.2 post-push record and no other defect. Step 1A
  owns that truthful lifecycle state; no record was fabricated and no tag or
  remote ref moved.
- individual job identities: EXERCISED **22/22**, omitted **0**. Twenty passed:
  version consistency, invariant self-test, deferred evidence, Python
  byte-compile, ShellCheck, workspace check/test, net check/test, net 1.86
  success, net 1.85 refusal, clippy, rustfmt, Rust 1.78 check/test, shell pytest,
  golden, artifacts, persisted fingerprints, and progress-check. The shell
  lane passed **366/366** with the one accepted warning; artifacts matched all
  **332** pins and both protected databases.
- checklist identity: FINDING, not hidden. `checklist-audit` compares the
  progress entry's qualified repository-relative runbook path with a basename,
  so ACTIVATE remains unmatched. This is the scheduled G2/G4/G5 instance owned
  by Step 2; repairing it here would violate task order.
- golden-E2E delta: **0**. The final permission-complete command passed
  **11/11**.
- protected/scope acceptance: PASS. `run` remains **45,409 bytes** at its
  existing authorization-grade pin. No dependency, production source,
  protected byte, v0.35 byte, amendment input, tag, or remote ref changed.
- governed review-export measurement: tree=`b38579ddd0e8080b786701da8436afc05c54a799`; bytes=`2766495`

### 2026-08-03 · E0 — entering-state reconstruction

- owner: Codex
- runbook: `docs/cycles/TASKS-v0.36-EXECUTION.md`
- commit: 9937a819dbbb699995e3cb03d1c16d4fce43bc6e
- result: PASS. Every H1–H13 hypothesis has a dated confirmed/refuted verdict
  in the active runbook; no hypothesis was left unmeasured.
- checklist measurements: H1 REFUTED at **270 checked / 268 matched / 268
  resolved / 3 retracted** before E0's own box was marked. v0.35 remains 0/9
  under the bold-only regex; v0.34 is 7 audited boxes among 17 checked lines.
  After marking E0, the live pre-audit population is **271/268**. The three
  v0.36 misses share the repository-relative-path versus basename bug assigned
  to Step 2.
- identity measurements: H4 prints the empty `store=[] extract=[]` vectors and
  201/0 kept/dropped result. H6's new nonempty 43-feature cross-sector witness
  persists both store canonical ids as self while the view drops technology
  for science at distance 0. The production fixture has 6 science and 7
  technology documents, 42 cross-sector pairs, and **0** distances at or below
  16 (range 22–41).
- export/object measurements: exact release-parent and closing exports are
  **2,725,527 / 151** and **2,737,957 / 151**, confirming only the hypothesized
  +12,430 delta. The release/tree, closing/tree, annotated tag object, peeled
  target, and immediate parent all resolve as recorded. Read-only
  `git ls-remote origin` found none of those five object ids.
- lifecycle measurements: H11 finds only the two active declaration literals
  above AGENTS §0. H12 confirms the post-push rule uses
  `head != measured_target` with no publication fact. H13 confirms 22 ordered
  jobs and first-failure return. Exactly the two expected amendment inputs are
  untracked and untouched.
- acceptance identities: EXERCISED **22/22**, omitted **0**. Twenty pass,
  including workspace and Rust 1.78 tests with both identity witnesses, net
  1.86 success / 1.85 refusal, invariant **12/12 rules / 74 controls**, shell
  **366/366**, artifacts **332** pins plus both databases, and golden **11/11**.
  Direct `cycle-check` retains only the expected Step 1A defect;
  `checklist-audit` retains the scheduled Step 2 qualification findings.
- golden-E2E delta: **0**.
- prohibited movement: PASS. No dependency, production source, protected
  byte, v0.35 byte, amendment input, tag, or remote ref changed. Disposable
  measurement clones and fixture database were removed after capture.
- governed review-export measurement: tree=`9937a819dbbb699995e3cb03d1c16d4fce43bc6e`; bytes=`2780874`

### 2026-08-03 · ACTIVATE — runbook-qualifier correction

- owner: Codex
- runbook: `TASKS-v0.36-EXECUTION.md`
- commit: f44681c1dce0c5c2efc0d3fb4a30900fdb4163f5
- result: FORWARD CORRECTION. The earlier ACTIVATE entry's repository-relative
  qualifier is not equal to the basename contract used by
  `matching_commit`. This append-only entry supplies the accepted basename;
  the earlier measured activation record remains unchanged.
- golden-E2E delta: **0**; this correction changes audit qualification only.

### 2026-08-03 · AUTONOMY — runbook-qualifier correction

- owner: Codex
- runbook: `TASKS-v0.36-EXECUTION.md`
- commit: b38579ddd0e8080b786701da8436afc05c54a799
- result: FORWARD CORRECTION. The corrected AUTONOMY implementation already
  exists and its earlier evidence remains authoritative; this entry supplies
  only the basename qualifier the current auditor compares.
- golden-E2E delta: **0**; no implementation or measurement changed.

### 2026-08-03 · E0 — runbook-qualifier correction

- owner: Codex
- runbook: `TASKS-v0.36-EXECUTION.md`
- commit: 9937a819dbbb699995e3cb03d1c16d4fce43bc6e
- result: FORWARD CORRECTION. The E0 implementation and full H1–H13 record are
  unchanged; this entry supplies only the basename qualifier required by the
  existing matching contract.
- checklist acceptance: PASS for the three currently checked v0.36 boxes.
  Step 2 still owns recognition of v0.35's plain boxes, derived expected-box
  coverage, empty-witness failure, and C3's corpus-wide qualifier decision.
- golden-E2E delta: **0**; no implementation or measurement changed.

### 2026-08-03 · LIFECYCLE-TRUTH — unpublished local close representation

- owner: Codex
- runbook: `TASKS-v0.36-EXECUTION.md`
- commit: eb897a549e314e92d38272c5c237a337413f3957
- result: PASS. A locally tagged, unpublished v0.17.2 close now passes
  `cycle-check` through one dated origin tag-absence observation without a
  fabricated post-push field. The reported status explicitly says offline Git
  cannot independently refresh remote absence.
- C7 decision: PASS with limitation recorded. No non-self-reported offline Git
  fact can prove continuing remote-tag absence; the selected observation is
  backed by `git ls-remote origin refs/tags/v0.17.2
  'refs/tags/v0.17.2^{}'`, exit 0 with empty output on 2026-08-03. A durable
  signed hosted publication receipt available offline would have changed the
  choice.
- two-direction lifecycle acceptance: PASS. Before the new branch, the planted
  valid observation failed with `publication post-push record required`; after
  the branch it returns `publication=unpublished-local-close`. The distinct
  published descendant control still fails without its post-push record, and a
  present complete post-push record takes precedence over the older absence
  observation.
- control acceptance: PASS. Both publication directions follow distinct R12
  control-site markers, the real scan passes **12/12 registered rules**, and
  `invariant-scan --self-test` passes **12/12 rules / 75 controls** with zero
  hand-typed absolute finding-line fields.
- full local acceptance: PASS **22/22** jobs. The permission-complete run covers
  version/cycle/checklist/invariant/evidence controls, workspace and Rust 1.78
  check/test, net check/test, Rust 1.86 success and 1.85 refusal, clippy,
  rustfmt, shell **366/366** with the one accepted warning, protected artifacts,
  persisted fingerprints, progress, and golden **11/11**.
- golden-E2E delta: **0**.
- prohibited movement: PASS. No post-push field was fabricated; no publication,
  tag/ref movement, production-source change, dependency change, protected
  byte, v0.35 byte, amendment input, or release authority changed.
- governed review-export measurement: tree=`eb897a549e314e92d38272c5c237a337413f3957`; bytes=`2795304`

### 2026-08-03 · BOX-COVERAGE — non-vacuous checked-task audit

- owner: Codex
- runbook: `TASKS-v0.36-EXECUTION.md`
- commit: 066c15934e9bb778887724d200da00df51eafe86
- result: PASS for Step 2's deliberately red acceptance state. Both bold and
  plain task boxes are recognized, structural Step coverage cannot be empty,
  and the unmodified v0.35 runbook now fails rather than passing vacuously.
- C2 decision: PASS. The audit derives **283 Step headings / 287 task boxes**
  across all **34** tracked execution runbooks. A sole in-section box wins;
  otherwise heading-derived aliases resolve the centralized checklist.
  Progress/declaration-backed extras remain visible. No per-cycle list, minimum
  count, or line-form exclusion exists.
- C3 decision: PASS. The real `T4` collision between v0.8 and v0.8.1 in their
  shared progress record makes cross-runbook order dependence measurable. The
  first structurally derived plain-task-box runbook establishes the
  forward-only qualification epoch; older immutable records retain their
  original contract.
- planted-control acceptance: PASS. Registered R13 catches an all-unbolded
  valid runbook when plain recognition is removed, an id absent from progress,
  a derived Step with no task box, and a forward task with no runbook qualifier.
  All expected findings derive from unique control-site markers.
- invariant acceptance: PASS **13/13 rules / 79 controls** with zero
  hand-typed absolute finding-line fields.
- fixed-v0.35 acceptance: EXPECTED FAIL with exactly **9** missing-qualifier
  defects. v0.35 reports **8 Steps / 9 task boxes / 9 checked / 0 matched / 0
  resolved**. The complete pre-declaration population is **281 checked / 272
  matched / 272 resolved / 0 exemptions / 3 retractions**. Step 3 owns the nine
  declarations; a pass at this point would violate Step 2.
- per-runbook output acceptance: PASS. The audit prints a population line for
  every one of the **34** tracked execution runbooks, including v0.36 at **9
  Steps / 10 task boxes / 4 checked / 4 matched / 4 resolved** before this
  implementation entry exists.
- golden-E2E delta: **0**; the permission-complete standalone run passed
  **11/11** after a sandbox-denied bind non-result.
- protected/scope acceptance: PASS. No production source, dependency,
  protected byte, v0.35 byte, tag/ref, amendment input, or release authority
  changed.
- governed review-export measurement: tree=`066c15934e9bb778887724d200da00df51eafe86`; bytes=`2818105`

### 2026-08-03 · V035-DECLARE — forward correction for nine silent gaps

- owner: Codex
- runbook: `TASKS-v0.36-EXECUTION.md`
- commit: c9ec9bad85a4ad5ceff0f1654f38a46ea429cfa2
- dated correction: The v0.35 closing record's **268 checked / 3 retracted /
  268 matched / 268 resolved** figures are a true tool output over prior-cycle
  bold boxes. The old audit examined **zero** of v0.35's nine plain task boxes,
  so those figures do not establish an executable v0.35 task/progress/commit
  link.
- DR2/DR3 disposition: PASS. Reconstructing the link would edit a closed
  runbook or its dated progress measurement. Exactly **9** forward exemptions,
  one per v0.35 box, record the missing qualifier; all eight Step boxes also
  name their box-id/progress-id mismatch. Acceptance is the repository operator
  through the active Step 3.
- DR4 disposition: PASS with no retraction. The recorded tool output is true,
  v0.35 is unpublished, and the twice-verified published-false bar is not met.
- checklist acceptance: PASS before this audit entry at **282 checked / 3
  retracted / 273 matched / 273 resolved / 9 exemptions**. v0.35 reports **8
  Steps / 9 task boxes / 9 checked / 0 matched / 0 resolved / 9 exemptions**;
  no gap is undeclared.
- assembled audit population: PASS at **283 checked / 3 retracted / 274
  matched / 274 resolved / 9 exemptions**. The active v0.36 line is **9 Steps
  / 10 task boxes / 6 checked / 6 matched / 6 resolved**.
- immutable-byte acceptance: PASS. `TASKS-v0.35-EXECUTION.md` worktree and
  `HEAD` both resolve to blob `1a5424c704ab56bf9a0ce3c261a20e92eabc7bc5`;
  `PROGRESS-v0.35.md` both resolve to
  `510d27f22f2687f6dfd48c49eacd7442d60bb77f`. Targeted diff exited 0.
- golden-E2E delta: **0**; standalone golden passed **11/11**.
- prohibited movement: PASS. No v0.35 byte, production source, dependency,
  protected byte, tag/ref, amendment input, or release authority changed.
- governed review-export measurement: tree=`c9ec9bad85a4ad5ceff0f1654f38a46ea429cfa2`; bytes=`2827155`

### 2026-08-03 · IDENTITY-SCOPE — one sector-partitioned identity rule

- owner: Codex
- runbook: `TASKS-v0.36-EXECUTION.md`
- commit: b945957871ae1fa5d3a3697a4f0c660347bd8311
- result: PASS. Store canonicalization and view collapse now translate their
  boundary types into shared `intel_extract::assign_dedup_identity`, which owns
  ordering, sector partitioning, eligibility, distance comparison, and
  canonical selection. No crate, manifest edge, lockfile, or MSRV moved.
- C1/architecture acceptance: PASS. The entering graph already contained the
  shared `intel-extract` dependency, firing the threshold-authority trigger.
  Architecture records why identity is global within a sector; R1's positional
  source was re-measured at `ARCHITECTURE.md:118-124`. R5 retains the
  boundary-local radius control.
- H6/H7 acceptance: PASS. The before **43-feature** pair was store self/self but
  view science/technology collapse at distance **0**. The after three-document
  witness produces the same nonempty science duplicate drop from both layers
  while preserving the cross-sector pair. The shipped **6×7 / 42-pair**
  distribution remains 22–41 with **0** distances at or below 16.
- rule acceptance: PASS. R14 failed before on both absent consumer calls and the
  absent shared sector partition. It passes after with three planted controls
  that independently remove view consumption, remove store consumption, and
  replace the shared sector key. Full self-test: **14/14 rules / 81 controls**.
- public-output/DR5 acceptance: PASS. Separate Step 3 and Step 4 builds exercised
  signals, brief, search, and ask for both configured subscriptions plus both
  billing routes. Canonical `/v1/*` payloads are byte-identical at **15,719
  bytes**, SHA-256
  `0c2ec212b9e398eddd38053c7157b8dd283f35f3908ad1b8c2f6481a912f09ea`;
  acme remains **12 documents / 1 collapse**, quant remains **1 / 0**, and no
  licensing or entitlement outcome moves. The reachable counterexample changes
  document selection but not any serialized field's value domain, so DR5 clause
  2 does not require minor.
- full local acceptance: PASS **22/22** jobs. Shell passed **368/368** with the
  accepted warning; Rust 1.78 and net 1.86 passed, net 1.85 refused the locked
  ICU edge, lint was clean, artifacts matched **332** pins plus both protected
  databases, and no job identity was omitted.
- golden-E2E delta: **0**; embedded golden passed **11/11**.
- prohibited movement: PASS. No v0.35 byte, protected byte, amendment input,
  release authority, tag, or remote ref moved.
- governed review-export measurement: tree=`b945957871ae1fa5d3a3697a4f0c660347bd8311`; bytes=`2844319`

### 2026-08-03 · AUDIT-CHILD — v0.35 closing-export disclosure

- owner: Codex
- runbook: `TASKS-v0.36-EXECUTION.md`
- commit: 9dea180cb872c6fa5c28b09907e2b452a7904952
- field acceptance: PASS. A dated v0.36 State append carries the exact required
  non-governing field for v0.35 closing commit
  `9996c6820d720160b64607575d0270d2e5393ef9`; no v0.35 byte was rewritten and
  no push was performed.
- independent measurement: PASS. An isolated detached clone measured the
  closing commit with project-root `./run export-check` at **2,737,957 bytes /
  151 files / 2 retained cycles**. Direct Git inspection separately supplied
  tree object `2fbb5ef5323ef010c2cbacddfcd713375881a4e6`, release parent
  `d4258883645a99f9499895bf064e453de9be1281`, and the closing commit's last
  governed field, **2,742,486 bytes**. Independent subtraction produced
  `audit_delta=-4529`.
- H8 discrepancy acceptance: PASS. H8's exact release-parent re-export is
  **2,725,527 bytes**, so its direct closing movement is **+12,430**. The
  immutable governed baseline is **+16,959** above that exact parent result;
  `+16,959 − 4,529 = +12,430`. The record exposes both baselines and does not
  absorb their discrepancy.
- full local acceptance: PASS **22/22** jobs over the assembled audit state.
  Shell passed **368/368** with the one accepted warning; all **14/14 rules /
  81 controls** passed, Rust 1.78 and net 1.86 passed, net 1.85 produced the
  required locked-ICU refusal, golden passed **11/11**, and all **332** pins
  plus both protected databases matched. The pre-implementation run had passed
  release and cycle consistency, then stopped exactly at checked-task evidence
  because the checked box could not yet name this implementation commit; that
  measured failure was the prescribed implementation/audit boundary, not a
  pass.
- golden-E2E delta: **0**; standalone golden passed **11/11**.
- prohibited movement: PASS. No production source, dependency, protected byte,
  v0.35 byte, amendment input, release authority, tag, or remote ref moved.
- governed review-export measurement: tree=`9dea180cb872c6fa5c28b09907e2b452a7904952`; bytes=`2850622`

### 2026-08-03 · RE-MEASURE — exact candidate authenticated 9/9

- owner: Codex
- runbook: `TASKS-v0.36-EXECUTION.md`
- commit: 3186cf403655843418246f5f4f2e8515215d1f2d
- condition/result: PASS. Step 4 moved production Rust, so the conditional
  hosted step ran. Exact candidate
  `f50db6744df726434db7f5aeffa1a08bbbf521fc` now has complete
  release-grade evidence on one fresh immutable evidence ref.
- preflight acceptance: PASS. Exact pinned `gh` **2.96.0** accepted the
  immutable **7/7** historical control population under every strict flag and
  rejected the deliberately wrong signer.
- candidate/ref acceptance: PASS. Immediately before the only push,
  `git ls-remote` exited **0** with no entry for fresh ref
  `refs/heads/codex/v0.36-evidence-f50db67`. One non-force push created exactly
  that ref; immediate and final readback resolved it to the candidate. No ref
  was reused, forced, moved, deleted, or repurposed.
- hosted-job acceptance: PASS. Workflow-dispatch run **30810557834**, attempt
  **1**, targeted the exact SHA/ref and completed `success`. All **9/9**
  blocking identities passed and persisted **9 receipts / 9 Sigstore
  bundles**; dependency drift was the sole declared report-only skip. The run
  was dispatched exactly once and not retried.
- toolchain acceptance: PASS. Three executed `jq -e` assertions proved
  `msrv=1.78.0`, `net-msrv-1-86=1.86.0`, and
  `net-msrv-1-85=1.85.0`; all exited **0**.
- release-grade verifier acceptance: PASS. Canonical single-bundle input and
  every strict flag accepted **9**, rejected **0**, and found the complete
  identity matrix. Every independently constructed certificate identity,
  repository, qualified workflow, source/signer digest, evidence ref, and
  hosted-runner claim matched. The temporary report is **41,096 bytes**,
  SHA-256
  `ab767a456411029fd4529bb8c1dc97dc135869765c33cf078add510e98ef05f7`,
  and remains outside the repository and manifest.
- population acceptance: PASS. Local Python 3.11.4 and 3.12.13 each passed
  **368/368**. Each hosted lane collected **368**, passed **367**, and skipped
  only the named, reasoned, `on_site` production-audit node. Both
  `tools/test_population.py` comparisons derived `collected=368`,
  `equivalent=true`, and `equivalent_passed=368`.
- workflow/remote acceptance: PASS. The workflow remains **39,177 bytes** /
  SHA-256
  `4ebf2c2193fe3fb11e7710b20c1c000fd073103656dc0b155bce945b57bff871`.
  Final direct readback kept remote `main`, v0.17.1, and its tag object
  unchanged, left v0.17.2 absent, and kept the evidence ref exact.
- full local acceptance: PASS **22/22** jobs over the assembled audit state.
  Shell passed **368/368** with the one accepted warning; all **14/14 rules /
  81 controls** passed, Rust 1.78 and net 1.86 passed, net 1.85 produced the
  required locked-ICU refusal, golden passed **11/11**, and all **332** pins
  plus both protected databases matched. The pre-implementation run had passed
  release and cycle consistency, then stopped exactly at checked-task evidence
  because the checked box could not yet name this implementation commit; that
  measured failure was the prescribed implementation/audit boundary, not a
  pass.
- golden-E2E delta: **0**; hosted and standalone local golden passed **11/11**.
- scope acceptance: PASS. No workflow, production source, dependency,
  protected byte, publisher request, main/tag publication, or retry occurred;
  the one DR6-authorized evidence ref was the only remote mutation.
- governed review-export measurement: tree=`3186cf403655843418246f5f4f2e8515215d1f2d`; bytes=`2857952`

### 2026-08-03 · R-CLOSE-BLOCKED — audit-before-check is unsatisfiable

- owner: Codex
- runbook: `TASKS-v0.36-EXECUTION.md`
- commit: 394a1400476263a95376ae6c7c2d6d851259b98d
- result: **BLOCKED before release implementation**. The required per-task gate
  review found that Step 7's stated gate was narrower than its mandatory
  audit-before-check criterion. Widening the gate exposed an author-side rule
  with no satisfying assignment; the R-CLOSE box remains unchecked.
- executed-construction acceptance: PASS as a negative result. In an isolated
  clone of audit commit `0d2e8b24bcc1ec0758027e52b13ecf91458e0395`,
  one syntactically valid cycle-ending field was planted after the latest
  governed field while R-CLOSE remained open. The real `./run cycle-check`
  exited **1** with exactly one defect: `cycle-ending review-export audit is
  unavailable while the active cycle is open`.
- lifecycle proof: the checker selects open with any unchecked box and rejects
  an audit in that state; it selects closed only with zero unchecked boxes and
  one closing record. A closing tree cannot contain its own not-yet-existing
  commit id, an intervening audit commit breaks tagged R-CLOSE's immediate-
  parent rule, and the normal append-only audit child occurs after the box is
  checked. No order meets every governing clause truthfully.
- C4 disposition: DEFERRED. All six `/v1/*` routes lack response models and
  emit dynamic input-, configuration-, core-, or model-derived values. No
  exhaustive machine-readable release baseline exists; a partial observed-
  field control would be vacuous, and declared scope forbids the shell
  production work needed to establish the complete authority. The existing G6
  deferral retains its trigger and names the complete manifest that would
  change this answer.
- DR5 disposition: patch-eligible only, not closed. Step 4's complete configured
  comparison remained byte-identical at **15,719 bytes** with no new route,
  named surface, or serialized value-domain movement. If the author-side
  ordering defect is corrected without a higher-precedence finding, the next
  available patch is **v0.17.3**; no version authority moved.
- validation acceptance: `version-check` passed at **0.17.2** with **3**
  executable offline-MSRV pins, **22** current offline-MSRV restatements, and
  **3** current release-version restatements. `cycle-check` passed with v0.36
  truthfully open; `checklist-audit` passed at **286 checked / 3 retracted / 277
  matched / 277 resolved / 9 exemptions**, with v0.36 at **9/9/9**. The full
  mutation suite passed **14/14 rules / 81 controls**.
- golden-E2E delta: **0**. The first sandboxed attempt was a loopback-bind
  permission non-result; the permission-complete rerun passed **11/11**.
- artifact observation: State is **334,622 / 453,741 bytes**, leaving
  **119,119 bytes**; the unchanged manifest is **193,057 / 1,048,576 bytes**,
  leaving **855,519 bytes**. These are gate-state observations, not the missing
  Step 7 closing-basis acceptance.
- prohibited movement: PASS. No release authority, production source,
  dependency, protected byte, v0.35 byte, amendment input, local tag, `main`,
  release tag, or remote ref moved.

### 2026-08-03 · AMENDMENT-A2 — Step 7 audit ordering corrected

- owner: Codex
- runbook: `TASKS-v0.36-EXECUTION.md`
- commit: c9ecfa404ebe0f93049765ac073c7a70865084e3
- result: PASS. Reviewer A2 affirms the earlier E3 impossibility proof and
  replaces only the unsatisfiable audit-before-check clause. The satisfiable
  order is release parent → checked closing commit → local annotated tag →
  immediate append-only audit child before handoff.
- evaluation-point acceptance: PASS. Every non-audit Step 7 criterion remains
  owned by the assembled closing worktree. The audit field alone is evaluated
  at the immediate child, and the child must pass Step 1A's second-unpublished-
  release lifecycle without weakening the published-release negative control.
- checker acceptance: PASS. Direct `cycle-check` reports v0.36 truthfully open
  and names no further undisclosed interaction. `version-check` passes at
  **0.17.2** with **3 / 22 / 3** executable-floor pins, current floor
  restatements, and current release restatements.
- checklist acceptance: PASS at **286 checked / 3 retracted / 277 matched /
  277 resolved / 9 exemptions**; v0.36 remains **9/9/9** while Step 7 is open.
- golden-E2E delta: **0**; the permission-complete amendment-only run passed
  **11/11**.
- input acceptance: PASS. A2 is materialized verbatim as the third untracked
  reviewer input; all three amendment files remain untracked and were excluded
  from the implementation commit.
- scope acceptance: PASS. No production source, dependency, release authority,
  protected byte, v0.35 byte, tag, `main`, or remote ref moved.
