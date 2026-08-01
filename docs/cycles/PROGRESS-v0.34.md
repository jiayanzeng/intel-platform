# PROGRESS-v0.34.md — append-only execution record

This file records v0.34 task and gate events after their implementation
commits exist. Each entry names the measured result, every applicable
acceptance criterion, the golden delta, and the real implementation commit.
Entries are append-only; corrections are new dated entries.

### 2026-08-02 · ACTIVATE — v0.34 preparatory cycle activation

- owner: Codex
- commit: bb4257000cd6a752e807af9f48d0fe871e20d216
- result: PASS for the runbook-defined preparatory activation. The sole
  pre-activation worktree item was the operator-supplied untracked v0.34
  runbook; tracked and staged diffs were empty. The implementation commit
  contains only that runbook, the `AGENTS.md` declaration moving the active
  cycle to v0.34, this progress skeleton, and the required
  `repomix.config.json` retention edit.
- author-contract acceptance: PASS after forward correction. The first staged
  real `cycle-check` exposed three author-side schema defects before the
  runbook's first commit: no deferred measured-observation column, no carried
  `MSRV current-restatement membership` subject, and a G5 action with no
  literal discharging `Step N`. Runbook amendment r1 records the correction;
  the checker was not weakened.
- entering-ref acceptance: PASS. Exact delivered v0.33 HEAD was audit child
  `e0ab6964f76b0a919c5214607ef141eb5b118deb`, whose immediate parent was
  closing implementation `70781081abd42ed9a49e22ed100efdb039a9b762`.
  Direct remote inspection resolved `main` and peeled `v0.17.1` to
  `f02379f03ccdfd1b019413234f2ad014d169fb04`, the tag ref to annotated
  object `14912f134e45277e2b4fd10b7f5bf8b4900ca20d` of Git type `tag`, and the
  closing commit's immediate parent to release commit
  `7a621e39a069a1ef26438e841e7bb1ca2f34165b`.
- retention rejection acceptance: PASS. Before the retention edit the staged
  real checker emitted exactly:
  `cycle-check: ERROR: repomix.config.json: review-export retention pattern for v0.34 must be 'docs/cycles/{TASKS,PROGRESS}-v0.{[0-9],1[0-9],2[0-9],3[0-1]}{.md,.*.md,-*.md}' to agree with the tracked retained-cycle set; found ['docs/cycles/{TASKS,PROGRESS}-v0.{[0-9],1[0-9],2[0-9],30}{.md,.*.md,-*.md}']`.
  The implementation advances the retained set to v0.32–v0.34.
- delivered-tree acceptance: PASS after two environment non-results. The
  workspace invocation was not an exact-tree measurement because the closed
  v0.33 checker discovered the untracked future runbook. An isolated clone of
  exact audit child `e0ab6964f76b0a919c5214607ef141eb5b118deb` then had a
  DNS-denied dependency bootstrap, followed by an empty-venv shell rejection;
  neither is the passing result. After installing the exact constrained set,
  the same clone passed all **20/20** jobs, checklist **261 checked / 3
  retracted / 261 matched / 261 commits resolved**, registered invariants
  **12 rules / 68 controls**, warning-denied current/net/MSRV lanes, and golden
  **11/11**. Its shell lane collected **348**, passed **347**, and skipped the
  one named, reasoned `on_site` node; E0 owns clean real-workspace populations
  through `tools/test_population.py`.
- artifact acceptance: PASS. Two complete real-workspace verifications matched
  **332 pins / 2 artifacts**, the exact structural State archive, and both
  protected databases in **0.12 s / 0.10 s real**.
- delivered-export acceptance: PASS. Project-root `./run export-check` at exact
  audit child `e0ab6964f76b0a919c5214607ef141eb5b118deb` emitted
  **2,634,692 bytes / 153 files**, confirming the reviewer inference and the
  exact tree identity.
- lifecycle acceptance: EXPECTED PENDING at the preparatory checkpoint. The
  committed activation `cycle-check` rejects exactly **28** stale-cycle
  observations: four trigger-bearing Architecture rows and 24 active deferral
  rows still honestly name v0.33. E0 owns their measured v0.34 rewrite; no
  structural, scope, retention, carry-forward, boundary, or activation-anchor
  defect remains. Artifact boundaries were read directly as `STATE.md`
  **206,530 / 453,741 bytes** and manifest **192,042 / 1,048,576 bytes**.
- test acceptance: NOT RUN as a post-activation 20-job task result; E0 owns the
  complete open-task-box entry point, clean Python populations through the
  repository comparator, every G1–G6 construction, and the mandatory
  standalone golden run.
- golden-E2E delta: **0** on the exact delivered-tree complete gate; E0 owns
  the post-activation standalone measurement.
- publisher/ref acceptance: PASS. Activation used only repository, local Git,
  direct read-only remote Git inspection, and the operator-local export. It
  issued no publisher request, ran no scheduler or model-profile command, and
  created, moved, or deleted no remote ref.

### 2026-08-02 · E0 — entering-state reconstruction and G1–G6

- owner: Codex
- commit: a6fe72fd862d93ca3ae75103d73f759d5130e47d
- result: PASS. Exact delivered v0.33 audit child
  `e0ab6964f76b0a919c5214607ef141eb5b118deb` and the active v0.34 E0 tree
  both passed the complete local entry point. The implementation records every
  gate disposition, refreshes all governed observations, and changes only
  `STATE.md`, `ARCHITECTURE.md`, and the active runbook.
- entering-state acceptance: PASS. The sole pre-activation item was the
  operator-supplied runbook; v0.33 audit child `e0ab6964…` immediately follows
  closing implementation `70781081…`. Direct remote inspection resolved
  `main` and peeled `v0.17.1` to `f02379f03ccdfd1b019413234f2ad014d169fb04`,
  tag object `14912f134e45277e2b4fd10b7f5bf8b4900ca20d` remained annotated Git type
  `tag`, and the release parent remained `7a621e39a069a1ef26438e841e7bb1ca2f34165b`.
- delivered-export acceptance: PASS. Exact-tree `./run export-check` emitted
  **100 derived / 7 required / 153 exported / 2,634,692 bytes**, confirming the
  reviewer's audit-child inference. It retained exactly v0.31–v0.33 and
  excluded both protected byte classes.
- G1 acceptance: PASS by four real-entrypoint constructions. Renamed `## 5.`
  failed on five unresolved §5 consumers; keeping only marker plus §7 failed on
  every live §2/§5/§6/§6b consumer; a duplicated marker failed with
  `required exactly once; found 2`. Full-tail deletion uniquely passed
  `cycle-check` with `state_regions=not-measured`; `version-check` separately
  rejected zero current restatements. The two State-region silent returns and
  three publication-status silent returns, their reachability, and their
  independent or deliberate bounds are enumerated in State. The G1 finding is
  confirmed, so Step 2 is not cancelled.
- G2 acceptance: PASS by real-entrypoint construction. The last-per-progress
  governed series is **2,576,273 → 2,629,379 (+53,106) → 2,706,393
  (+77,014) → 2,592,441 (−113,952)**; State also records every intermediate
  governed field and signed delta. A constructed latest **+3,000-byte** pair
  made the exact **290,607 / 3,000 = 96.87-cycle** row pass the real checker.
  The selected v0.31→v0.32 basis predates the v0.33 archive, and no current
  field or checker branch carries the epoch fact.
- G3 acceptance: PASS by three exact delivered exports and two complete
  decompositions. v0.31→v0.32 measured **+79,962 bytes**. v0.32→v0.33 measured
  **+77,862 steady growth**, **−177,542 net State reclaim**, and **+6 bytes**
  of retention-pattern/serialization movement, reconciling the delivered
  **−99,674-byte** delta. State records each component, share, and reclaim
  mechanism. The export is **4.57 cycles** away on the latest positive
  delivered denominator and **4.69** on the latest post-archive steady-growth
  denominator; the next State archive is **7.93 cycles** away on its latest
  same-kind denominator. Export arrives first under the latest and averaged
  denominators.
- G4 acceptance: PASS by exhaustive tracked search. The only referent is the
  dated external v0.28 observation, **2,067 project-knowledge chunks / 2,000
  limit** beside a 4,975,987-byte export. No repository chunker or current
  project-knowledge index exists; the 3,000,000-byte ceiling is an internally
  executable but externally uncalibrated proxy. No lever or ceiling change was
  selected.
- G5 acceptance: PASS by retained-cycle derivation. Controls are **58 → 61 →
  68**, shifted-existing expectations **36 → 12 → 25**, and combined physical
  checker bytes **192,695 → 208,356 → 243,494**. Ratios **62.07% → 19.67% →
  36.76%** are non-monotonic; the latest shifted count is 43 below the controls
  protected, so the second trigger clause is not approaching at a defensible
  linear rate.
- G6 acceptance: PASS. Exact delivered ranking is export **4.69 cycles**,
  State **7.93**, manifest **1,323.85**. No live Architecture row asserted the
  superseded ordering; the State-nearest claim remains only in dated v0.32
  history and is corrected forward.
- trigger acceptance: PASS. All **4** trigger-bearing Architecture rows and all
  **24** active deferred observations now name v0.34 and 2026-08-02 without
  changing any trigger. The real lifecycle entry point reports the activation
  exemption exactly as `exempt-open-empty-progress`; post-implementation
  `cycle-check` passed from HEAD with State **219,255 / 453,741 bytes**,
  manifest **192,042 / 1,048,576 bytes**, and state regions `bound`.
- Python acceptance: PASS after clean rebuilds. Constrained Python 3.11.4 and
  3.12.13 each emitted **348 collected / 348 passed / 0 failed / 0 skipped**
  and the same one accepted warning. `tools/test_population.py` derived
  `collected=348`, `equivalent=true`, and `equivalent_passed=348`. The earlier
  3.11 attempt before freshness rewrites failed the expected freshness test and
  is not the passing result.
- full-gate acceptance: PASS with E0's task box still open. `./run ci-local`
  passed **20/20**, checklist **261 / 3 / 261 / 261**, registered invariants
  **12/12 rules / 68 controls**, warning-denied Rust and net builds, clippy,
  fmt, Rust 1.78 locked lanes, shell **348/348**, protected artifacts, and
  embedded golden **11/11**.
- artifact acceptance: PASS. Two independent complete runs matched **332 pins
  / 2 artifacts**, the exact State archive, and both protected databases in
  **0.12 s / 0.10 s real**.
- scope acceptance: PASS. No production source, workflow, dependency, release
  authority, protected artifact, publisher request, scheduler, service,
  model-profile command, remote ref, public response/value-domain, or runtime
  behaviour changed. Published-epoch divergence remains zero.
- golden-E2E delta: **0**. The complete gate and required standalone post-task
  run each passed **11/11**.

### 2026-08-02 · REGION-FLOOR — independent State structural admission

- owner: Codex
- commit: 02d8db86a2432222433cec29a1a51332911fc478
- result: PASS. `cycle-check` now rejects loss of State's complete permanent
  tail from its own structural admission path, keeps semantic current-
  restatement ownership delegated to `version-check`, and emits an explicit
  bound for every G1 publication-status path that has no local ref fact to
  reconcile.
- before/after acceptance: PASS. E0's exact delivered-tree full-tail deletion
  passed `cycle-check` with `state_regions=not-measured`; only the composite
  `version-check` lane rejected the lost restatement. With REGION-FLOOR copied
  into the identical construction, `cycle-check` itself emitted the named
  structural defect `permanent-tail marker required exactly once; found 0`
  and `FAIL (1 defect(s))`.
- structural/semantic acceptance: PASS. Emitted success text names
  `structural=bound`, `semantic_current_restatement=present`, and
  `semantic_owner=version-check`. Structural admission covers the status
  header, permanent-tail marker, adjacency, region overlap, headings,
  increasing anchors, external references, and ordinal report; the semantic
  offline-MSRV restatement remains read only by `version-check`.
- silent-exit acceptance: PASS. No reachable closed release emits
  `not-applicable` with the no-ref bound; portable hosted mode emits
  `not-requested` with the absent-local-tag-object bound and names the checks
  that remain; a legacy release emits `verified protocol=legacy` and states
  that R-CLOSE post-push does not apply. The current local tagged-closing path
  emits `verified protocol=tagged-closing release=v0.17.1`.
- planted-control acceptance: PASS. R12 removes the entire permanent tail and
  observes the real `cycle_check.run` entry point; disabling the structural
  marker branch makes the finding disappear. The initial self-test rejected a
  stale expected location. Manual replay of every R12 mutation yielded **27**
  shifted existing `expected_line` values, all copied from emitted findings
  rather than offset-computed; the final suite passed **12/12 rules / 68
  controls**.
- focused-test acceptance: PASS. `shell/tests/test_cycle_check.py` passed
  **85/85**, including the new full-tail, structural-header, no-release,
  portable-hosted, and legacy-protocol cases.
- full-gate acceptance: PASS with REGION-FLOOR's task box still open.
  `./run ci-local` passed **20/20**, checklist **262 / 3 / 262 / 262**,
  registered invariants **12/12 rules / 68 controls**, warning-denied
  current/net/MSRV Rust lanes, clippy, fmt, clean Python 3.11.4 shell
  **352/352**, all **332** pins, both protected databases, and embedded golden
  **11/11**.
- scope acceptance: PASS. No production source, workflow, dependency, release
  authority, protected artifact, publisher request, scheduler, service,
  model-profile command, remote ref, public response/value-domain, or runtime
  behaviour changed. Published-epoch divergence remains zero.
- golden-E2E delta: **0**. The complete gate and required standalone
  `./run golden` each passed **11/11**.

### 2026-08-02 · BASIS-BOUND — emitted governed-margin limits

- owner: Codex
- commit: 9b4f1da6e6723808d3f8a586443e7386a2dab96e
- result: PASS. The governed margin retains its executable latest-positive-
  adjacent same-kind selection and arithmetic, while the real `cycle-check`
  entry point now emits both limits the selected denominator cannot prove.
- emitted-bound acceptance: PASS. Successful output says a single adjacent
  pair carries **no representativeness guarantee** and that the checker
  **cannot detect a basis predating a structural change**. Focused lifecycle
  tests passed **85/85** and assert the exact emitted report.
- constraint-choice acceptance: PASS. Only two positive governed deltas exist,
  **53,106** and **77,014 bytes**, so a numeric floor would not prove
  representativeness. A trailing window would mix the v0.33 one-time
  **−113,952-byte** archive reclaim into steady growth. No independent
  machine-readable epoch authority aligns an archival event to governed
  progress measurements, so an epoch rule would self-attest from prose. The
  emitted bound is the evidence-supported outcome; difficulty was not the
  rationale.
- history acceptance: PASS. No dated historical margin figure was edited; the
  limitation, rationale, and current result were recorded forward.
- invariant acceptance: PASS after one expected stopped attempt. The first
  complete gate stopped at R12 control 37 on a stale source location. Exact
  mutation replay emitted `tools/cycle_check.py:2935`; the single shifted
  existing `expected_line` was copied from that output, not calculated. No
  control or control schema changed, the population remained **68**, and the
  final registered suite passed **12/12 rules / 68 controls**.
- full-gate acceptance: PASS with BASIS-BOUND's task box still open.
  `./run ci-local` passed **20/20**, checklist **263 / 3 / 263 / 263**,
  warning-denied current/net/MSRV Rust lanes, clippy, fmt, clean Python 3.11.4
  shell **352/352**, all **332** pins, both protected databases, and embedded
  golden **11/11**.
- scope acceptance: PASS. No production source, workflow, dependency, release
  authority, protected artifact, publisher request, scheduler, service,
  model-profile command, remote ref, public response/value-domain, or runtime
  behaviour changed. Published-epoch divergence remains zero.
- golden-E2E delta: **0**. The complete gate and required standalone
  `./run golden` each passed **11/11**.
