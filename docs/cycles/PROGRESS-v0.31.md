# PROGRESS-v0.31.md — append-only execution record

This file records v0.31 task and gate events after their implementation
commits exist. Each entry names the measured result, every applicable
acceptance criterion, the golden delta, and the real implementation commit.
Entries are append-only; corrections are new dated entries.

### 2026-07-31 · ACTIVATE — v0.31 preparatory cycle activation

- owner: Codex
- commit: f814149
- result: PASS for the runbook-defined preparatory activation. The sole
  pre-activation worktree item was the operator-supplied untracked
  `docs/cycles/TASKS-v0.31-EXECUTION.md`; tracked and staged diffs were empty.
  The implementation commit contains only that runbook, the `AGENTS.md`
  declaration moving the active cycle to v0.31, this progress skeleton, and
  the required `repomix.config.json` retention edit.
- entering-ref acceptance: PASS. Before activation, HEAD was v0.30 audit
  commit `5af3209bbab4116f15bfdef10c1e17befbf27e63`, whose immediate parent was
  v0.30 closing commit `00ad3fe1390bac5d6b848581550c88d12dd2ea8e`.
  The local remote-tracking `origin/main` and peeled v0.17.0 tag both resolved
  to `4af2841816dd3e43fb8423153b91aa22ccb87537`; HEAD was 60 commits ahead
  and zero behind that remote-tracking ref. Local `main` remained at
  `eb2d9df8b3ffd3e0380d506e958fb5a3adb2d42e`. No publication ref moved, and
  no mutable `origin/main` hash was added to `STATE.md`'s header.
- retention rejection acceptance: PASS. With active v0.31 present and before
  the retention edit, the real checker emitted exactly:
  `cycle-check: ERROR: repomix.config.json: review-export retention pattern for v0.31 must be 'docs/cycles/{TASKS,PROGRESS}-v0.{[0-9],1[0-9],2[0-8]}{.md,.*.md,-*.md}'; found ['docs/cycles/{TASKS,PROGRESS}-v0.{[0-9],1[0-9],2[0-7]}{.md,.*.md,-*.md}']`.
  This matched the predicted text. The implementation then changed only that
  final retained range.
- lifecycle acceptance: EXPECTED PENDING at the preparatory checkpoint. After
  the activation commit, `cycle-check` rejected exactly the four
  trigger-bearing `ARCHITECTURE.md` rows because they still named v0.30.
  The activation section explicitly assigns their measured v0.31 rewrite to
  E0; no other lifecycle defect was reported. Before this entry existed,
  `progress-check` correctly rejected the empty progress skeleton.
- test acceptance: NOT RUN at this preparatory checkpoint; E0 owns the clean
  rebuild, the complete 20-job matrix, both constrained Python populations,
  both protected-artifact timing runs, and the activation-tree export.
- golden-E2E delta: NOT MEASURED; E0 owns the first post-activation golden
  measurement.
- publisher/ref acceptance: PASS. Activation used only repository and local
  Git inspection. It issued no publisher request, ran no scheduler, and
  created, moved, or deleted no publication ref.

### 2026-07-31 · E0 — rebuild entering state and settle G1–G6

- owner: Codex
- commit: edcf492820eb8d65b158fea65c9b7f62b494d21c
- result: PASS. The implementation record corrects every entering hypothesis
  that measurement displaced, checks E0, and changes only `STATE.md`,
  `ARCHITECTURE.md`, and the active runbook. The active runbook's dated
  amendment entry discloses the Step 1 completion-block change.
- decision-gate acceptance: PASS. The post-activation E0 worktree was clean;
  v0.30 closing commit
  `00ad3fe1390bac5d6b848581550c88d12dd2ea8e` and audit child
  `5af3209bbab4116f15bfdef10c1e17befbf27e63` were exactly where the
  runbook placed them; and every local entry gate passed. Step 1's gate
  contains all of its acceptance criteria because all are entering-state or
  local-gate measurements.
- activation acceptance: PASS. Before the retention edit, the real checker
  emitted the predicted stale-pattern rejection byte-for-byte, as preserved in
  `STATE.md`. After activation it reported the named
  `exempt-open-empty-progress` state, exactly matching the open-cycle
  empty-progress branch. Activation commits are
  `f8141496c571da85b8dd7a5e022534b95bf561d8` and
  `9ed9f9e8086f703d9d349878e6fe14320e5e7b9d`.
- G1 acceptance: PASS by execution. In a no-hardlink clone, the real v0.30
  closing implementation commit exited **1** with
  `row=2576273, latest_progress=2464445,
  tree=e7b2c58814e2223d9899b83b3f3491344ce85337`; its audit child exited
  **0** with `governed_export=bound`. `ARCHITECTURE.md` is byte-identical
  across the pair. The truthful earlier and later values cannot each satisfy
  both evaluation points, so the runbook's unsatisfiable-rule hypothesis is
  confirmed.
- G2 acceptance: PASS by exhaustive tracked-tree classification. At activation
  audit tree `9ed9f9e8086f703d9d349878e6fe14320e5e7b9d`,
  `git ls-files` contained **75** literal-bearing files / **683**
  occurrences. The declared historical-exclusion tuple has no reader. File
  precedence classified every path as executable authority, registered current
  restatement, control construction, or historical family: **0**
  unclassified, **6** multiply classified. Those six are
  `.github/workflows/ci.yml`, `run`, `AGENTS.md`, `README.md`, `STATE.md`,
  and `rust-toolchain.toml`; their exact memberships and the complete path
  families are recorded in `STATE.md`. Within-file current-versus-history
  separation remains text-undecidable and is explicitly distinct from the
  complete file-level partition.
- G3 acceptance: PASS by execution. A full distinct-seed Git construction made
  v0.33 active with no v0.32 and retained a closed v0.31. The real
  `cycle-check` exited **0** with
  `governed_export=exempt-open-empty-progress`; the permission-complete real
  `export-check` exited **1** because both v0.30 TASKS/PROGRESS documents were
  missing. An initial sandbox DNS failure was a non-result. Only the
  operator-local entry point catches the reachable skipped-v0.x divergence;
  neither automated lane does.
- G4 acceptance: PASS by exhaustive search. `MAX_EXPORT_BYTES` has one
  authority in `tools/export_check.py`; `export-check` occurs in no
  `ci_local_jobs` or workflow step. An automated `cycle-check` comparison can
  constrain the figure written in the governed row at the checked tree. It
  cannot create or measure an export, enumerate its paths, verify retained
  documents, or detect excluded protected bytes.
- G5 acceptance: PASS. The no-release implementation commit and audit child
  both evaluate the closed comparison; only the latter can satisfy the
  truthful new value under the current protocol. In the release shape, `R` is
  open and exempt; closing child `C`, tagged checkout `C`, and the first
  post-push descendant are satisfiable when the row and closing field name the
  export measured on `R` and the post-push append adds no later governed field.
  Step 3 must repair the former without breaking any of those four points.
- G6 acceptance: PASS. Activation audit tree
  `9ed9f9e8086f703d9d349878e6fe14320e5e7b9d` exported **153 files /
  2,544,715 bytes**, leaving **455,285 bytes / 15.18%** and retaining exactly
  v0.29–v0.31. Delivered v0.28→v0.29 and v0.29→v0.30 observations are
  **−8,342** and **+61,837**; the separate v0.30-delivered→v0.31-activation
  observation is **−38,909**. Under the named latest-positive denominators,
  the export ceiling is **7.36 cycles** away and the State boundary is nearer
  at **5.19 cycles**. Retention returns export bytes; live State has no reclaim
  mechanism before another archive.
- deferred/governed acceptance: PASS. All **22** deferred rows and all four
  trigger-bearing architecture rows now carry v0.31 measurements. The
  published-release divergence hypothesis was corrected: v0.31 is open, so
  only v0.29 and v0.30 are post-correction closed observations. No public
  surface changed, and the trigger has not fired. All three runbook-header
  reviewer errors remain recorded as reviewer errors.
- local-regression acceptance: PASS. `./run ci-local` passed **20/20**:
  warning-denied **146** workspace tests and **62** net tests (**32 ingest +
  30 cored**), locked Rust 1.78, clean clippy/fmt/ShellCheck, floor
  byte-compilation, both protected archives, embedded golden **11/11**, and
  every other registered job. `invariant-scan --self-test` passed **12 rules /
  55 controls**. Focused SEC identity measured **201 input / 201 kept / 0
  dropped**, including **200 SEC kept / 0 dropped**. No checker changed, so
  **0** planted-control expected-line values were re-derived.
- population acceptance: PASS. Clean constrained Python **3.11.4** and
  **3.12.13** lanes each collected/passed **317**, failed **0**, and skipped
  **0**, with the same one accepted warning. The executed comparator derived
  `{"collected":317,"equivalent":true,"equivalent_passed":317,"hosted":{"on_site_skipped":0,"passed":317,"skipped":[]},"local":{"passed":317,"skipped":0},"schema_version":1}`.
- manifest acceptance: PASS. Schema validation reported **2 artifacts / 331
  pinned files** in the unchanged **191,395-byte** manifest. Two consecutive
  permission-complete verifications took **0.10 s / 0.10 s real** and matched
  both protected databases.
- control acceptance: PASS. Before E0 was checked, `checklist-audit` passed
  **239 checked / 3 retracted / 239 matched / 239 commits resolved / 0
  exemptions**. `version-check` passed at v0.17.0 with three executable
  offline pins normalizing to 1.78 and all 22 registered restatements agreeing.
  The active lifecycle check passed before this audit append with
  `governed_export=exempt-open-empty-progress`; with the measurement below
  present it passed with `governed_export=exempt-open-latest-at-close`.
  `checklist-audit` then passed **240 checked / 3 retracted / 240 matched / 240
  commits resolved / 0 exemptions**.
- governed review-export measurement: tree=`edcf492820eb8d65b158fea65c9b7f62b494d21c`; bytes=`2556451`
- export acceptance: PASS. Exact E0 implementation tree
  `edcf492820eb8d65b158fea65c9b7f62b494d21c` produced **100 derived / 7
  required / 153 exported / 2,556,451 bytes**, retained exactly three cycles,
  and left **443,549 bytes / 14.78%** beneath the ceiling.
- golden-E2E delta: **0**. Embedded, pre-commit standalone, and exact
  implementation-commit standalone executions each passed **11/11**
  byte-identically.
- publisher/ref acceptance: PASS. E0 issued no publisher request, ran no
  scheduler or model-profile command, and changed no cadence, production
  source, dependency, schema, manifest, protected byte, version value, tag,
  publication ref, or working-repository ref.

### 2026-07-31 · DISPOSITION-FIRST — select patch release v0.17.1

- owner: Codex
- commit: 6a11b0e6dd2f2e121d395faf088537be620d6d63
- result: PASS. The operator selected `release v0.17.1` before implementation.
  The recorded reason is to ship the order-independent internal boundary
  derivation together with three cycles of executable binding corrections,
  rather than inheriting a release conclusion from green gates.
- decision-gate acceptance: PASS. E0 is complete and its implementation/audit
  pair exists. Step 2's gate contains every acceptance criterion because this
  task changes only the two lifecycle records that state the operator's
  decision, measured classification, and unchanged authorities/refs.
- classification acceptance: PASS. E0 compared the unpublished distance with
  published v0.17.0 and found no route, response-shape, serialized `/v1/*`
  value-domain, dependency, or schema movement. The difference remains one raw
  boundary string in an internal loopback `/ingest` diagnostic for a
  misordered window. Neither release-classification trigger fires, so patch is
  the measured class.
- version acceptance: PASS. The selected exact version is **v0.17.1**.
  `./run version-check` still reported all five authorities at **0.17.0**:
  `apps/cored/Cargo.toml`, `shell/intel_shell/__init__.py`,
  `shell/intel_shell/app.py`, the `STATE.md` header, and `CHANGELOG.md`.
  Their release-authority diff from the E0 audit commit was empty. Step 6 owns
  their later movement.
- lifecycle acceptance: PASS. `STATE.md` and the dated Step 2 runbook amendment
  both record the selection, date, and reason. The active lifecycle check
  passed with `governed_export=exempt-open-latest-at-close`.
- publication acceptance: PASS. This selection chooses the release-shaped
  Step 6–Step 8 workflow but does not itself authorize Step 8's separate
  publication act. Remote-tracking `origin/main` and the peeled v0.17.0 tag
  remained `4af2841816dd3e43fb8423153b91aa22ccb87537`; annotated tag object
  `df4fc3b044ca12335e773dcc0b9bdd4e0db90afd` was unchanged. No version
  authority, tag, `main`, release ref, or publication ref moved.
- golden-E2E delta: **0**. The mandatory Step 2 standalone execution passed
  **11/11** byte-identically.
- boundary acceptance: PASS. The task changed no artifact beyond `STATE.md`
  and the active runbook. It made no publisher request, scheduler run,
  model-profile command, cadence change, manifest edit, production-source
  edit, or protected-byte edit.

### 2026-08-01 · CLOSE-POINT — bind the governed export to a checked tree

- owner: Codex
- commit: 33d5bb9e2b51a71d372600a7a0ef73ccba011200
- result: PASS. The closed-cycle comparison now binds the architecture row to
  the last governed progress measurement already visible in the exact checked
  tree. A later, explicitly non-governing cycle-ending audit records the
  closing-tree export without asking a record to measure a tree containing
  itself.
- decision-gate acceptance: PASS. G1 established that the former rule had no
  satisfying assignment at a no-release implementation commit; G5 established
  the release-shaped four-point sequence. The task changed only the declared
  checker, controls, tests, contracts, and cycle records. It did not touch the
  manifest, protected bytes, production source, dependencies, schema,
  toolchains, publisher state, or refs.
- rejection-before-acceptance: PASS. Before implementation, the focused
  governed-export suite passed **5** and failed **3**: the checker ignored a
  valid cycle-ending audit, accepted a misordered audit, and did not import or
  enforce the export ceiling. After implementation, all **8/8** focused cases
  passed.
- closed-tree contract acceptance: PASS. The exact checked tree now selects
  the last `governed review-export measurement` already present in that tree,
  regardless of whether later bytes increase or decrease. A closed tree with
  no governed field still fails, and a row superseded by the selected governed
  field still fails. Open trees retain the named
  `exempt-open-empty-progress` and `exempt-open-latest-at-close` paths.
- cycle-ending-audit acceptance: PASS. The exact non-governing form is
  `cycle-ending review-export audit` with closing tree, bytes, and signed
  audit delta. The checker permits zero or one only after the final governed
  field and only after closure, reports `bound-with-cycle-ending-audit`, and
  never promotes it into the governed comparison.
- release-sequence acceptance: PASS. A real-fixture four-state integration
  exercised release parent `R` open and exempt, closing child `C` bound,
  annotated-tag checkout `C` bound, and the first post-push descendant bound
  with the cycle-ending audit. Together with the governed unit family, all
  **9/9** release-sequence cases passed.
- ceiling acceptance: PASS. `cycle-check` imports the single
  `MAX_EXPORT_BYTES` authority from `tools/export_check.py` and rejects a
  written governed-row figure above it at every checked tree. Its diagnostic
  explicitly says this constrains the repository's written figure and does
  not create or measure an export; operator-local `export-check` remains the
  real-byte and retained-set control.
- planted-control acceptance: PASS. Registered R12 now rejects both an
  over-ceiling governed row and a cycle-ending audit placed before the final
  governed field. The full self-test passed **12 rules / 57 controls**. From
  the real self-test output, **9** `expected_line` values were re-derived:
  seven shifted existing controls and the two new controls.
- local-regression acceptance: PASS. `./run ci-local` passed **20/20**:
  warning-denied **146** workspace tests and **62** net tests (**32 ingest +
  30 cored**), locked Rust 1.78, clean clippy/fmt/ShellCheck, floor
  byte-compilation, both protected archives, embedded golden **11/11**, and
  every other registered job. Focused `test_cycle_check.py` passed **64** and
  `test_invariant_scan.py` passed **22**.
- population acceptance: PASS. Clean constrained Python **3.11.4** and
  **3.12.13** lanes each collected/passed **322**, failed **0**, and skipped
  **0**, with the same one accepted warning. The executed comparator derived
  `{"collected":322,"equivalent":true,"equivalent_passed":322,"hosted":{"on_site_skipped":0,"passed":322,"skipped":[]},"local":{"passed":322,"skipped":0},"schema_version":1}`.
- governed review-export measurement: tree=`33d5bb9e2b51a71d372600a7a0ef73ccba011200`; bytes=`2586197`
- export acceptance: PASS. Exact CLOSE-POINT implementation tree
  `33d5bb9e2b51a71d372600a7a0ef73ccba011200` produced **100 derived / 7
  required / 153 exported / 2,586,197 bytes**, retained exactly three cycles,
  and left **413,803 bytes / 13.79%** beneath the ceiling.
- golden-E2E delta: **0**. Embedded and permission-complete standalone
  executions passed **11/11** byte-identically. The first standalone attempt
  was a non-result because the sandbox denied the core's loopback bind; the
  exact entry point then passed with the documented local-network permission.
- publisher/ref acceptance: PASS. CLOSE-POINT issued no publisher request,
  ran no scheduler or model-profile command, changed no cadence, and created,
  moved, or deleted no version, tag, release, publication, or working-repository
  ref.

### 2026-08-01 · EXCLUSION-READ — make the historical exclusion load-bearing

- owner: Codex
- commit: 801a163ca18d4625639d835c582a2d28d6e4dff3
- result: PASS. `OFFLINE_MSRV_HISTORICAL_EXCLUSIONS` is now a tuple of real
  path patterns consumed by a file-level Rust-floor partition in the existing
  `version-check` entry point. A tracked literal-bearing file outside all four
  classes fails automatically.
- decision-gate acceptance: PASS. The task added no local or hosted job,
  changed no toolchain or executable offline pin, and altered no evidence
  topology. `run`, `.github/workflows/**`, `rust-toolchain.toml`, the manifest,
  every protected byte, and every dated historical cycle/State-archive/
  evidence/observation file remained byte-unchanged.
- rejection-before-acceptance: PASS. With the two acceptance tests present
  against the old module, the focused file passed **5** and failed **2** because
  the reader did not exist. After implementation, it passed **7/7**. A direct
  planted tracked `tools/export_check.py` floor statement then emitted
  `tools/export_check.py: Rust floor literal(s) yielded zero file-level
  classifications`.
- tracked-partition acceptance: PASS. The implementation commit derived **559
  tracked paths** from `git ls-files` and found **75 literal-bearing files /
  662 bounded occurrences**, **0 unclassified**, and **6 multiply classified**.
  The six are `.github/workflows/ci.yml`, `run`, `AGENTS.md`, `README.md`,
  `STATE.md`, and `rust-toolchain.toml`, matching E0's complete file set.
- class acceptance: PASS. Precedence is executable authority → registered
  current restatement → derived Python control construction → historical
  family. Authority/restatement paths come from their existing registries,
  control constructions come from executable Python calls to
  `offline_msrv_report`, and the historical family consumes the formerly dead
  exclusion declaration as path patterns. The tracked membership is derived,
  not enumerated in a test.
- bound acceptance: PASS. The entry point itself reports `file-level only;
  within-file current restatements cannot be separated from dated historical
  quotations by identical literal text`. The six mixed files therefore remain
  deliberately outside any line-level claim.
- planted-control acceptance: PASS. Registered R12 plants the same
  unclassified-file condition; `invariant-scan --self-test` passed **12 rules /
  58 controls**. Real mutated-tree output re-derived **3** shifted
  `expected_line` values: the existing offline controls at **397 / 397** and
  the new partition control at **484**. Combined focused version/invariant
  tests passed **29/29**.
- local-regression acceptance: PASS. The permission-complete `./run ci-local`
  passed **20/20** with warning-denied **146** workspace tests and **62** net
  tests (**32 ingest + 30 cored**), locked Rust 1.78, clean
  rustc/clippy/fmt/ShellCheck, floor byte-compilation, both protected
  archives, shell **324/324**, embedded golden **11/11**, and every other
  registered job.
- population acceptance: PASS. Clean constrained Python **3.11.4** and
  **3.12.13** lanes each collected/passed **324**, failed **0**, and skipped
  **0**, with the same one accepted warning. The first sandboxed Python 3.11
  install was a DNS-denied non-result; the permission-complete retry passed.
  The executed comparator derived
  `{"collected":324,"equivalent":true,"equivalent_passed":324,"hosted":{"on_site_skipped":0,"passed":324,"skipped":[]},"local":{"passed":324,"skipped":0},"schema_version":1}`.
- authority acceptance: PASS. `version-check` read three executable offline
  pins, normalized them to one value, and bound all **22** current
  restatements. All five release authorities remain **0.17.0**; no dependency,
  lockfile, schema, route, response shape, or `/v1/*` value domain moved.
- golden-E2E delta: **0**. Embedded and mandatory standalone executions each
  passed **11/11** byte-identically.
- publisher/ref acceptance: PASS. EXCLUSION-READ issued no publisher request,
  ran no scheduler or model-profile command, changed no cadence, and created,
  moved, or deleted no version, tag, release, publication, or working-repository
  ref.

### 2026-08-01 · RETENTION-ONE — bind the configured pattern to one retained set

- owner: Codex
- commit: 54f82286831a9b18321369f86c7d2485fd9cb41b
- result: PASS. `export-check` now derives the cycle-document collection once
  from `git ls-files`; `cycle-check` imports that same retained-path authority
  and formats the configured exclusion boundary from its earliest retained
  execution runbook. Arithmetic and the real retained runbook set therefore
  cannot silently disagree on a skipped cycle.
- decision-gate acceptance: PASS. G3's cheap shape required no brace-glob
  parser or matcher. The task changed lifecycle tooling, tests, controls, and
  records only; it created or read no export and changed no production source,
  workflow, harness, dependency, schema, manifest, protected byte, or version
  authority.
- rejection-before-acceptance: PASS. Against the old checker, the new real-Git
  skipped-cycle construction made active `v1.2.4`, omitted `v1.2.3`, and saw
  the old entry point return **0**, failing the test's required **1** assertion.
  After implementation, skipped-cycle and stale-pattern cases passed **2/2**
  and the error required agreement with the tracked retained-cycle set.
- no-export acceptance: PASS. The throwaway acceptance tree asserted no
  `repomix-output-*.xml` existed. Its sentinel selects the production Git
  authority rather than the explicit test double used by generic Gitless
  fixtures.
- stale-pattern acceptance: PASS. The existing active-cycle stale-pattern
  rejection remains exercised and its diagnostic states both the derived
  corrective pattern and the configured pattern found.
- planted-control acceptance: PASS. Existing R12 retention control now exposes
  both `stale-retention-pattern` and `skipped-cycle-retained-set` when the guard
  is suppressed. Full self-test passed **12 rules / 58 controls**. All **24**
  shifted `cycle_check.py` `expected_line` values came from real mutated-tree
  output; the joint retention failure emitted at line **1151**.
- focused acceptance: PASS. Combined cycle/export/invariant tests passed
  **95/95**.
- local-regression acceptance: PASS. Permission-complete `./run ci-local`
  passed **20/20** with warning-denied **146** workspace tests and **62** net
  tests (**32 ingest + 30 cored**), locked Rust 1.78, clean
  rustc/clippy/fmt/ShellCheck, both protected archives, shell **325/325**,
  embedded golden **11/11**, and every other registered job.
- population acceptance: PASS. Clean constrained Python **3.11.4** and
  **3.12.13** lanes each collected/passed **325**, failed **0**, and skipped
  **0**, with the same one accepted warning. The executed comparator derived
  `{"collected":325,"equivalent":true,"equivalent_passed":325,"hosted":{"on_site_skipped":0,"passed":325,"skipped":[]},"local":{"passed":325,"skipped":0},"schema_version":1}`.
- golden-E2E delta: **0**. Embedded and mandatory standalone executions each
  passed **11/11** byte-identically.
- publisher/ref acceptance: PASS. RETENTION-ONE issued no publisher request,
  ran no scheduler or model-profile command, changed no cadence, and created,
  moved, or deleted no version, tag, release, publication, or working-repository
  ref.
