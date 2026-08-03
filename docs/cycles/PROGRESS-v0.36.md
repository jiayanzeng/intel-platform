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
