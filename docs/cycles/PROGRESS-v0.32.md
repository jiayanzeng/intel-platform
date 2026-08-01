# PROGRESS-v0.32.md — append-only execution record

This file records v0.32 task and gate events after their implementation
commits exist. Each entry names the measured result, every applicable
acceptance criterion, the golden delta, and the real implementation commit.
Entries are append-only; corrections are new dated entries.

### 2026-08-01 · ACTIVATE — v0.32 preparatory cycle activation

- owner: Codex
- commit: 9ecc8c1
- result: PASS for the runbook-defined preparatory activation. The sole
  pre-activation worktree item was the operator-supplied untracked
  `docs/cycles/TASKS-v0.32-EXECUTION.md`; tracked and staged diffs were empty.
  The implementation commit contains only that runbook, the `AGENTS.md`
  declaration moving the active cycle to v0.32, this progress skeleton, and
  the required `repomix.config.json` retention edit.
- entering-ref acceptance: PASS. Before activation, HEAD was the v0.31
  post-push audit commit `9625fb1f7a7af2e85bad8418480b5b89093b707b`,
  whose immediate parent was closing commit
  `f02379f03ccdfd1b019413234f2ad014d169fb04`. The local remote-tracking
  `origin/main` and peeled v0.17.1 tag both resolved to that closing commit;
  annotated tag object `14912f134e45277e2b4fd10b7f5bf8b4900ca20d`
  had Git type `tag`; local `main` remained
  `eb2d9df8b3ffd3e0380d506e958fb5a3adb2d42e`. The activation commit was two
  commits ahead of and zero behind remote-tracking `origin/main`. No
  publication ref moved, and no mutable `origin/main` hash was added to
  `STATE.md`'s header.
- retention rejection acceptance: PASS after making the new paths visible to
  the Git-derived reader by staging them. Before the retention edit, the real
  checker emitted exactly:
  `cycle-check: ERROR: repomix.config.json: review-export retention pattern for v0.32 must be 'docs/cycles/{TASKS,PROGRESS}-v0.{[0-9],1[0-9],2[0-9]}{.md,.*.md,-*.md}' to agree with the tracked retained-cycle set; found ['docs/cycles/{TASKS,PROGRESS}-v0.{[0-9],1[0-9],2[0-8]}{.md,.*.md,-*.md}']`.
  This matched the predicted line byte-for-byte. An earlier invocation while
  the runbook was still untracked stopped at `cannot derive 3-cycle retention
  set ending at v0.32`; it did not examine the stale-pattern construction and
  is `not measured`, not a prediction mismatch. The implementation then changed
  only the final retained range.
- lifecycle acceptance: EXPECTED PENDING at the preparatory checkpoint. After
  the activation commit, `cycle-check` rejected exactly the four
  trigger-bearing `ARCHITECTURE.md` rows because they still named v0.31. The
  activation section explicitly assigns their measured v0.32 rewrite to E0;
  no other lifecycle defect was reported. Before this entry existed,
  `progress-check` was not interpreted as an acceptance result because the
  progress skeleton contained no task event.
- test acceptance: NOT RUN at this preparatory checkpoint; E0 owns the clean
  rebuild, the complete 20-job matrix, both constrained Python populations,
  both protected-artifact timing runs, and the activation-tree export.
- golden-E2E delta: NOT MEASURED; E0 owns the first post-activation golden
  measurement.
- publisher/ref acceptance: PASS. Activation used only repository and local
  Git inspection. It issued no publisher request, ran no scheduler, and
  created, moved, or deleted no publication ref.

### 2026-08-01 · E0 — rebuild entering state and settle G1–G6

- owner: Codex
- commit: 4ba1de7
- result: PASS. The exact implementation commit is
  `4ba1de7f60e1161106380a3644dace61ff7907fa`; it updates only
  `ARCHITECTURE.md`, `STATE.md`, and the active runbook with measured entry
  facts, dated trigger observations, the Step 1 amendment disclosure, and the
  checked E0 completion.
- local-gate acceptance: PASS. Clean constrained Python 3.11.4 and 3.12.13
  rebuilds each resolved all 21 pinned packages, collected/passed 325, failed
  0, skipped 0, and emitted the same one accepted Starlette warning. The
  machine comparator derived `collected=325`, `equivalent=true`, and
  `equivalent_passed=325`. The exact `./run ci-local` entry point passed all
  20 jobs, including warning-denied current and locked Rust 1.78 lanes, 146
  workspace tests plus the focused identity diagnostic, 32 ingest-net tests,
  30 cored-net tests, clippy, fmt, ShellCheck, 12 invariant rules / 58 planted
  controls, protected bytes, and its embedded golden 11/11. An earlier
  sandboxed invocation was `not measured` because its loopback wire-server bind
  was denied; the exact permitted rerun is the recorded pass.
- published-state acceptance: PASS by independent remote measurement. Remote
  `main` and peeled `v0.17.1` both resolved to closing commit
  `f02379f03ccdfd1b019413234f2ad014d169fb04`; annotated object
  `14912f134e45277e2b4fd10b7f5bf8b4900ca20d` had Git type `tag`; the
  closing commit's immediate parent was release commit
  `7a621e39a069a1ef26438e841e7bb1ca2f34165b`.
- G1 acceptance: PASS by exhaustive search and direct measurement. No checker
  compared `STATE.md` or the manifest against their prose boundaries. At exact
  activation-audit tree `7ba89795403b2b8fab84ff53abeba6ad4a220d23`,
  `STATE.md` was 324,290 bytes with 129,451 bytes / 3.68 cycles remaining at
  +35,173 bytes/cycle; the manifest was 191,395 bytes with 857,181 bytes / an
  unbounded latest-zero-delta estimate, or 99.43 cycles at the last positive
  +8,621 bytes/cycle; the export was 2,617,984 bytes with 382,016 bytes / 5.40
  cycles remaining at +70,780 bytes/cycle. `STATE.md` is nearest and its
  estimate worsened.
- governed review-export measurement: tree=`7ba89795403b2b8fab84ff53abeba6ad4a220d23`; bytes=`2617984`
- G2 acceptance: PASS by execution of the real function and entry point in a
  tracked throwaway clone. A staged file containing `offline needs >= 1.75`
  returned verbatim `'wrong_floor_rows': [], 'wrong_floor_occurrences': 0`
  and `version-check: PASS (0.17.1)`. The current detector's value-closure bound
  is therefore unnamed; Step 3 owns contextual candidate recognition or an
  explicit bound.
- G3 acceptance: PASS by exhaustive derivation and execution. The tracked
  current-version set was enumerated across Architecture, changelog, lockfile,
  README, State, cored manifest, current/prior cycle records, and both shell
  literals. A README-line-1-only change to `v9.9.9` in a throwaway exact-v0.31
  clone left `version-check`, `cycle-check`, and `invariant-scan --self-test`
  green, demonstrating that every shared local/hosted lifecycle entry point
  ignores that present-tense restatement.
- G4 acceptance: PASS. Local and remote `codex/*` refs were exhaustively
  enumerated: the local reused branch named v0.23 targeted the activation audit,
  its remote targeted the v0.31 post-push audit, and cycle-qualified remote
  evidence refs existed only for v0.24 through v0.30. Run 30685356489's seven
  receipts and seven Sigstore bundles verified 7/7 against signed v0.17.1
  release digest and the reused source ref. Digest/ref claims are load-bearing;
  the branch's later mutable target is not. Fresh-ref absence and readback are
  executable only at operation time and cannot become durable in-tree history.
- G5 acceptance: PASS. Direct Git blobs measured +2,729 progress bytes and
  +2,572 State bytes from the v0.31 release parent to post-push audit; their
  exact +5,301-byte sum reconciled the delivered export movement. This corrects
  the entering two-newline hypothesis. A differing delivered export should
  require the cycle-ending audit; the latest append's own contribution remains
  necessarily undisclosed, because naming it recreates the fixed point.
- G6 acceptance: PASS by exhaustive search. No executable control distinguishes
  trigger firing from non-firing or defines a restart. The live v0.32 row now
  says the trigger fired at v0.31, v0.17.1 publication disposed it, no new
  runtime/public difference exists, and reset is undefined pending Step 5;
  firing and reset remain operator adjudications.
- activation/deferred acceptance: PASS. The stale-retention rejection matched
  the predicted line byte-for-byte and remains quoted in State and activation
  progress; the earlier untracked-runbook stop is recorded as `not measured`.
  All 24 deferred rows now carry v0.32 measured observations, and all four
  Architecture trigger rows carry v0.32 close-adjacent measurements. The real
  activation entry point's governed exemption is recorded by the exact name
  `exempt-open-empty-progress`.
- artifact acceptance: PASS. Both direct manifest validations and complete
  protected-byte verifications matched 331 pins and both databases; measured
  real times were 0.17 s and 0.10 s. The manifest and protected bytes were not
  edited.
- golden-E2E delta: PASS, byte-identical **11/11** both inside `ci-local` and in
  the mandatory standalone post-task `./run golden`; delta **0**.
- publisher/ref acceptance: PASS. E0 issued no publisher request, ran no
  scheduler or model-profile command, found no listener on 8788, and created,
  moved, or deleted no publication ref. Direct remote query still found neither
  historical `v0.8.0` nor `v0.10.2` tag.

### 2026-08-01 · BOUNDARY-MEASURE — direct artifact byte boundaries

- owner: Codex
- commit: 456f37d
- result: PASS. Exact implementation commit
  `456f37d705d2aed2d5fcbc663a28f4b63400e326` implements the operator-selected
  named reported crossing, adds one machine-readable authority containing the
  two governed path/boundary pairs, reads both artifact sizes directly, and
  checks the dated governed rows. It also records the operator decision,
  measured State/Architecture outcomes, Step 2 amendment, and checked task.
- gate acceptance: PASS. `config/protected-artifacts.json`,
  `docs/state-archive/**`, `.github/workflows/**`, and `run` have no diff; no
  archive, manifest edit, or new lane was required. No dependency, schema,
  production source, public response, or value-domain change exists.
- preimplementation rejection acceptance: PASS. Committed construction
  `43945ffdb958fcebcfe44141758f99725dd7f2f2` set both live boundaries to one
  byte while the artifacts exceeded them; the old real `./run cycle-check`
  still returned PASS. This proved the prior entry point did not read the
  constructed artifacts for either boundary.
- direct-measurement acceptance: PASS. At exact implementation tree
  `fbec13ee86bc36f85e096e53ee1c80654272fd31`, the real entry point reported
  `STATE.md bytes=336654 boundary=453741 state=bound` and
  `config/protected-artifacts.json bytes=191395 boundary=1048576 state=bound`,
  with `checked_tree=HEAD-tree:fbec13ee86bc36f85e096e53ee1c80654272fd31`.
  It reported State timing `not-applicable` and manifest timing
  `out-of-scope`; no prose measurement supplies either compared byte count.
- single-authority acceptance: PASS. The active runbook's governed artifact
  byte-boundary section is the sole live executable boundary authority.
  Governed trigger rows reference that authority without numeric boundary
  restatements. The duplicate-authority fixture was rejected.
- crossing-behaviour acceptance: PASS. Temporarily setting both authorities to
  one byte made the real entry point reject both rows before any acceptance,
  with two exact `requires a dated 'trigger-fired disposition:'` defects.
  Adding dated dispositions made the same crossed construction pass and report
  `trigger-fired-disposed` twice. Restoring the real boundaries reports
  `bound` twice. Focused tests passed 70/70 across below-boundary,
  duplicate-authority, missing-row, crossed-undisposed, and
  crossed-disposed paths.
- R12 acceptance: PASS. The registered control plants a one-byte crossed but
  undisposed construction against the production check. The real self-test
  passed 12/12 rules and 59 controls. Nine shifted existing `expected_line`
  positions were re-derived from emitted production locations; the new control
  resolves to `tools/cycle_check.py:2016`.
- local-gate acceptance: PASS. `./run ci-local` passed all 20 jobs with
  warning-denied 146 workspace tests, the focused SEC identity diagnostic, 32
  ingest-net plus 30 cored-net tests, locked Rust 1.78, clean
  rustc/clippy/fmt/ShellCheck, 12 invariant rules / 59 controls, shell 330/330,
  protected artifacts exact, and embedded golden 11/11. Constrained Python
  3.11.4 and 3.12.13 each collected/passed 330, failed 0, and skipped 0; the
  machine comparator derived `collected=330`, `equivalent=true`, and
  `equivalent_passed=330`. A prior sandboxed Python 3.11 invocation was `not
  measured` because loopback binds and `ps` were denied; the exact permitted
  rerun passed.
- golden-E2E delta: PASS, byte-identical **11/11** in both the complete local
  entry point and mandatory standalone post-task `./run golden`; delta **0**.
- publisher/ref acceptance: PASS. The task made no publisher request, ran no
  scheduler or model-profile command, and created, moved, or deleted no
  publication ref.
