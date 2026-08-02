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
