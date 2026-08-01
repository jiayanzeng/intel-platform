# PROGRESS-v0.33.md — append-only execution record

This file records v0.33 task and gate events after their implementation
commits exist. Each entry names the measured result, every applicable
acceptance criterion, the golden delta, and the real implementation commit.
Entries are append-only; corrections are new dated entries.

### 2026-08-01 · ACTIVATE — v0.33 preparatory cycle activation

- owner: Codex
- commit: 353a17e67c3cac5699f43dd65b15725e3e35d5e1
- result: PASS for the runbook-defined preparatory activation. The sole
  pre-activation worktree item was the operator-supplied untracked r2 runbook;
  tracked and staged diffs were empty. The implementation commit contains only
  the runbook, the `AGENTS.md` declaration moving the active cycle to v0.33,
  this progress skeleton, and the required `repomix.config.json` retention
  edit.
- author-contract acceptance: PASS after forward correction. The first staged
  real `cycle-check` exposed four r2 author defects before activation: unknown
  `conditional` scope class, no measured-observation deferral column, missing
  carry-forward of `MSRV current-restatement membership`, and two action cells
  that named `Steps N–M` instead of executable `Step N` references. r3 records
  the correction at the runbook's top; the checker was not weakened. The
  manifest path is now an `allow` whose use remains prose-constrained to Step 5
  Option B and explicit operator selection.
- entering-ref acceptance: PASS. Before activation, HEAD was exact v0.32 audit
  child `70b7f93c94c67e43f6f4a29ede5823081955f3fa` and its immediate parent was
  closing implementation `86b8db0b4026c23371317c7881dcc9497806c20b`.
  Direct remote inspection—not the closing record—resolved `main` and peeled
  `v0.17.1` to `f02379f03ccdfd1b019413234f2ad014d169fb04`, resolved the
  tag ref to annotated object `14912f134e45277e2b4fd10b7f5bf8b4900ca20d`
  of Git type `tag`, and confirmed the closing commit's immediate parent is
  release commit `7a621e39a069a1ef26438e841e7bb1ca2f34165b`.
- retention rejection acceptance: PASS after staging the new paths so the
  Git-derived reader examined the construction. Before the retention edit the
  real checker emitted exactly:
  `cycle-check: ERROR: repomix.config.json: review-export retention pattern for v0.33 must be 'docs/cycles/{TASKS,PROGRESS}-v0.{[0-9],1[0-9],2[0-9],30}{.md,.*.md,-*.md}' to agree with the tracked retained-cycle set; found ['docs/cycles/{TASKS,PROGRESS}-v0.{[0-9],1[0-9],2[0-9]}{.md,.*.md,-*.md}']`.
  The implementation then changed only the final retained range, advancing the
  retained set to v0.31–v0.33.
- delivered-tree acceptance: PASS with two named environment non-results. An
  isolated local clone of exact delivered v0.32 HEAD cleared lifecycle,
  checklist **254 checked / 3 retracted / 254 matched / 254 commits resolved**,
  registered invariants **12 rules / 61 controls**, warning-denied Rust and net
  tests, Python, and golden **11/11**. Its first net run was not measured because
  the sandbox denied the loopback bind; the permitted rerun passed. Its
  protected-artifact lane was not measured because local-only database bytes are
  intentionally absent from a clone. In the real workspace two complete
  verifications matched **331 pins / 2 artifacts** and both protected databases
  in **0.09 s / 0.10 s real**.
- lifecycle acceptance: EXPECTED PENDING at the preparatory checkpoint. The
  committed activation `cycle-check` rejected exactly **28** stale-cycle
  observations: four trigger-bearing `ARCHITECTURE.md` rows and 24 active
  deferral rows still honestly name v0.32. E0 owns their measured v0.33 rewrite;
  no structural, scope, retention, boundary, or activation-anchor defect
  remained. Artifact boundaries were read directly as `STATE.md` **352,895 /
  453,741 bytes** and manifest **191,395 / 1,048,576 bytes**.
- test acceptance: NOT RUN as a complete 20-job workspace result at this
  preparatory checkpoint; E0 owns the post-activation full entry point, both
  local Python populations through `tools/test_population.py`, the exact
  delivered-export measurement, and every G1–G6 construction.
- golden-E2E delta: NOT MEASURED as a post-activation task result; E0 owns the
  mandatory standalone measurement.
- publisher/ref acceptance: PASS. Activation used only repository, local Git,
  and direct read-only remote Git inspection. It issued no publisher request,
  ran no scheduler or model-profile command, and created, moved, or deleted no
  publication ref.

### 2026-08-01 · E0 — entering state rebuilt; G1–G6 settled

- owner: Codex
- commit: a966f554cd7db5a3fa33aaf369a727584dd0cd5f
- result: PASS. The exact delivered v0.32 tree, current publication identity,
  all six runbook gates, both governed-byte pressures, and every v0.33 trigger
  observation were measured and recorded before implementation work began.
- entering-state acceptance: PASS with one corrected hypothesis. Exact
  delivered HEAD was audit child `70b7f93c94c67e43f6f4a29ede5823081955f3fa`
  over closing implementation `86b8db0b4026c23371317c7881dcc9497806c20b`.
  Checklist was **254 checked / 3 retracted / 254 matched / 254 commits
  resolved**, not 253. Registered invariant baseline was **12 rules / 61
  controls**.
- publication acceptance: PASS by direct read-only remote inspection. Remote
  `main` and peeled `v0.17.1` both resolved to
  `f02379f03ccdfd1b019413234f2ad014d169fb04`; annotated object
  `14912f134e45277e2b4fd10b7f5bf8b4900ca20d` had Git type `tag`; its closing
  commit's immediate parent was release commit
  `7a621e39a069a1ef26438e841e7bb1ca2f34165b`.
- delivered-export acceptance: PASS. Project-root `./run export-check` at exact
  audit child `70b7f93c94c67e43f6f4a29ede5823081955f3fa` emitted **2,734,366 bytes /
  153 files**, confirming the inferred tree and the exact **4,979-byte**
  closing-tree-to-audit-child difference. Activation's real checker reported
  the named governed state `exempt-open-empty-progress`.
- G1 acceptance: PASS as a measured finding. At the real delivered-tree
  `cycle-check`, absent and renamed headers both PASSed; absent `STATE.md`
  failed only through the independent governed-artifact reader. `version-check`
  rejected all three, proving composite protection is borrowed. `git log -G`
  placed the overstating sentence in reviewer-authored v0.21 release commit
  `b7c4b10eb506923e3ea854a32d1dc3f4c83b0eaa`, so it is classified as a
  reviewer error.
- G2 acceptance: PASS. Governed→governed **+77,014** leaves **3.81 cycles**;
  closing→closing **+80,284** leaves **3.37**; delivered→delivered **+79,962**
  leaves **3.32**. Only governed→governed is visible honestly at the governed
  row's closing evaluation point. Historical 5.65 is a criterion/evaluation-
  point error with correct arithmetic on mixed-kind inputs.
- G3 acceptance: PASS. Exact delivered State decomposed to **2,405 header +
  306,676 dated append + 43,814 permanent tail = 352,895 bytes** over 5,368
  lines. All live external anchors and the registered restatement were derived;
  no §3 reference exists. The inventory corrected two reviewer omissions:
  `.github/workflows/ci.yml` and `crates/compliance/Cargo.toml`. At complete
  entry points, `version-check` rejected over-cut/restatement removal but
  accepted renamed §5/five-section removal, while `cycle-check` accepted all
  four.
- G4 acceptance: PASS as a bounded negative result. Exhaustive search found no
  archive digest, complement, order, or truncation reader. Git history and the
  v0.21 recorded SHA are not standing byte-fidelity controls.
- G5 acceptance: PASS. Every executable State reader and archival effect is
  recorded. Real checklist measurement before and after the Option B throwaway
  cut remained **254 / 3 / 254 / 254**; post-cut `version-check` retained 22
  current MSRV and 3 release restatements.
- G6 acceptance: PASS. State has **3.23 closing / 3.53 delivered cycles** of
  same-kind margin; export has **3.81 governed / 3.37 closing / 3.32 delivered
  cycles**. Option B's measured counterfactual returns exactly **178,125
  bytes** to each boundary, leaving State **174,770** and delivered-tree export
  **2,556,241**. No option was selected and no archive was written.
- trigger acceptance: PASS. All 24 active deferral rows and all four governed
  Architecture rows carry dated v0.33 measurements with unchanged triggers.
- test acceptance: PASS. The complete entry point passed **20/20** with E0's
  box open; `invariant-scan --self-test` emitted **12/12 rules / 61 controls**.
  Python 3.11.4 and 3.12.13 each emitted collected/passed **336**, failed 0,
  skipped 0; `tools/test_population.py` derived `collected=336`,
  `equivalent=true`, `equivalent_passed=336`. Two complete artifact runs
  verified **331 pins / 2 artifacts** and both databases in **0.09 s / 0.10 s
  real**. The first sandboxed net/Python attempts were `not measured` because
  loopback/process inspection was denied; permitted reruns supplied the passing
  results.
- golden-E2E delta: **0**. The mandatory final standalone run passed **11/11**.
- publisher/ref acceptance: PASS. No publisher request, scheduler, service,
  model-profile command, archive write, or ref mutation occurred.

### 2026-08-01 · ADMIT-GATE — publication-status family fails closed

- owner: Codex
- commit: 118ba84d038866233b178147d4133a9cd63fa8bd
- result: PASS. `cycle-check` now admits the publication-status family only
  after a regular `STATE.md` file and a matching leading `**As of:**` header
  exist, and selects the newest actual release across later no-release cycles.
- fail-before acceptance: PASS. At the exact delivered-tree entry point, absent
  and renamed headers passed while absent State failed only through the
  independent artifact reader. With the fix copied into those same three
  constructions, the entry point emitted distinct `publication admission
  header required`, `publication admission header shape`, and `publication
  admission file required` defects; the absent-file case correctly retained
  its separate governed-artifact defect.
- relationship acceptance: PASS. A check-site comment records that
  `version_check.state_version()` independently binds the release version while
  `cycle-check` binds publication status; neither hand-written regex is treated
  as the other's family-admission floor.
- invariant acceptance: PASS. R12 separately disables the three admission
  outcomes and the newest-actual-release selector through the real
  `cycle_check.run` entry point. Focused self-test passed **37/37 R12 controls**;
  the full registry passed **12/12 rules / 65 controls**. Real emitted mutation
  findings re-derived **25 shifted existing** `expected_line` values plus the
  four new values: admission branches at line 603 and selector at line 562.
- architecture acceptance: PASS. The live publication-reconciliation paragraph
  now states the selector, admission outcomes, R12 coverage, and independent
  version parser accurately. Git authorship measured the original v0.21
  overstatement as this runbook reviewer's error, so it is corrected forward
  without rewriting dated history.
- test acceptance: PASS. Focused lifecycle tests passed **74/74** on constrained
  Python 3.11.4 and independently on 3.12.13. The complete `./run ci-local`
  entry point passed **20/20** with the task box still open. Both Python lanes
  collected/passed **340**, failed 0, and skipped 0; the repository comparator
  derived `collected=340`, `equivalent=true`, and `equivalent_passed=340`.
- golden-E2E delta: **0**. The required standalone post-task run passed
  **11/11**.
- scope acceptance: PASS. No production source, workflow, dependency, schema,
  manifest, protected byte, publisher, scheduler, service, model profile,
  public response/value-domain state, or publication ref changed.

### 2026-08-01 · MARGIN-KIND — export margin uses one governed series

- owner: Codex
- commit: ae15a8c89b86e89bc3998b164837d669784fbd4f
- result: PASS. The live governed export row now names and executes one
  governed→governed series rather than combining candidate and delivered
  measurements.
- series acceptance: PASS. The checker reads the last governed fields in
  `PROGRESS-v0.31.md` and `PROGRESS-v0.32.md`: **2,629,379 → 2,706,393**.
  It requires the current term to equal the row marker and re-derives the
  **77,014-byte/cycle** denominator, **293,607-byte** ceiling remainder, and
  **3.81-cycle** two-decimal quotient. The row names both source records and
  therefore states its evaluation points.
- historical acceptance: PASS. The dated v0.32 **5.65** measurement was not
  rewritten. The live v0.33 row corrects it forward as a mixed-kind criterion
  and evaluation-point error, while the historical calculation remains evidence
  of what was computed at that time.
- executable-bound acceptance: PASS. Closing→closing and
  delivered→delivered remain valid operator measurements but are excluded from
  the machine marker because they lack a common repository progress authority.
  The permitted marker is in the governed row's measured cell and every source,
  term, delta, remainder, and quotient is re-read or re-derived.
- invariant acceptance: PASS. R12 plants a row whose declared prior term no
  longer matches its named governed progress series, executes the real
  `cycle_check.run` entry point, and observes the plant disappear when the
  comparison branch is disabled. Focused self-test passed **38/38 R12
  controls**; the full registry passed **12/12 rules / 66 controls**. Mutation
  output re-derived **29 shifted existing** line values and the one new value at
  line **2401**; none was computed by offset.
- test acceptance: PASS. Focused lifecycle tests passed **76/76** on Python
  3.11.4. The complete entry point passed **20/20** with the task box open.
  Python 3.11.4 and 3.12.13 each collected/passed **342**, failed 0, and skipped
  0; `tools/test_population.py` derived `collected=342`, `equivalent=true`, and
  `equivalent_passed=342`. The malformed no-`PYTHONPATH` invocation and the
  sandbox-denied loopback/process-inspection invocation were non-results; the
  correctly formed permitted command supplied the passing Python 3.12 result.
- golden-E2E delta: **0**. The required standalone post-task run passed
  **11/11**.
- scope acceptance: PASS. No production source, workflow, dependency, schema,
  manifest, protected byte, publisher, scheduler, service, model profile,
  public response/value-domain state, or publication ref changed.
