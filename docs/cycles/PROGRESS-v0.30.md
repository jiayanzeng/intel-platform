# PROGRESS-v0.30.md — append-only execution record

This file records v0.30 task and gate events after their implementation
commits exist. Each entry names the measured result, every applicable
acceptance criterion, the golden delta, and the real implementation commit.
Entries are append-only; corrections are new dated entries.

### 2026-07-31 · ACTIVATE — v0.30 preparatory cycle activation

- owner: Codex
- commit: bea40e64849015fdfc9b471f2adb7ab3ce4fcbf7
- result: PASS for the runbook-defined preparatory activation. The sole
  pre-activation worktree item was the operator-supplied untracked
  `docs/cycles/TASKS-v0.30-EXECUTION.md`; tracked and staged diffs were empty.
  The implementation commit contains only that runbook, the `AGENTS.md`
  declaration moving the active cycle to v0.30, this progress skeleton, and
  the required `repomix.config.json` retention edit.
- entering-ref acceptance: PASS. Before activation, HEAD was v0.29 audit
  commit `d824be06582dfb76b9fe4b5d70ff33f4a505d6cc`, whose immediate parent was
  v0.29 closure commit `20ddf90bb2b1d8654b410cdafe8f67e6d006a115`.
  The local remote-tracking `origin/main` and peeled v0.17.0 tag both resolved
  to `4af2841816dd3e43fb8423153b91aa22ccb87537`; HEAD was 44 commits ahead
  and zero behind that remote-tracking ref. Local `main` remained at
  `eb2d9df8b3ffd3e0380d506e958fb5a3adb2d42e`. No ref moved, and no mutable
  `origin/main` hash was added to `STATE.md`'s header.
- retention rejection acceptance: PASS. With active v0.30 present and before
  the retention edit, the real checker emitted exactly:
  `cycle-check: ERROR: repomix.config.json: review-export retention pattern for v0.30 must be 'docs/cycles/{TASKS,PROGRESS}-v0.{[0-9],1[0-9],2[0-7]}{.md,.*.md,-*.md}'; found ['docs/cycles/{TASKS,PROGRESS}-v0.{[0-9],1[0-9],2[0-6]}{.md,.*.md,-*.md}']`.
  The implementation then changed only that final retained range.
- lifecycle acceptance: EXPECTED PENDING at the preparatory checkpoint. After
  the activation commit, `cycle-check` rejected exactly the three
  trigger-bearing `ARCHITECTURE.md` rows because they still named v0.29.
  The activation section explicitly assigns their measured v0.30 rewrite to
  E0; no other lifecycle defect was reported. Before this entry existed,
  `progress-check` correctly rejected the empty progress skeleton.
- test acceptance: NOT RUN at this preparatory checkpoint; E0 owns the clean
  rebuild, the complete 20-job matrix, both constrained Python populations,
  both protected-artifact timing runs, and the activation-tree export.
- golden-E2E delta: NOT MEASURED; E0 owns the first post-activation golden
  measurement.
- publisher/ref acceptance: PASS. Activation used only repository and local
  Git inspection. It issued no publisher request, ran no scheduler, and
  created, moved, or deleted no ref.

### 2026-07-31 · E0 — entering state rebuilt and G1–G6 settled

- owner: Codex
- commit: 2b0b890c988de9facd901ccef444a1ed0dad5c58
- result: PASS. The supplied runbook was the sole pre-activation worktree
  item; v0.29 audit `d824be06…` and closure `20ddf90b…` were exactly where the
  entering state placed them. The stale retention pattern produced the exact
  required v0.30 rejection before activation changed `2[0-6]` to `2[0-7]`.
  The activation pair is `bea40e64…` plus audit `e7b2c588…`.
- decision-gate acceptance: PASS after the runbook-required activation
  rewrite. The first clean Python 3.11 execution collected 306, passed 305,
  failed the one current-trigger-table test, and skipped zero because the
  three architecture governed rows still named v0.29. This is a measured
  non-pass. E0 rewrote those rows with v0.30 measurements as the activation
  section requires; the result-of-record rerun and every complete local gate
  then passed. No remaining E0 gate tripped.
- complete-suite acceptance: PASS. `./run ci-local` passed all **20/20** jobs:
  warning-denied **146** workspace tests and **62** net tests (**32 ingest +
  30 cored**), locked Rust 1.78 check/test, clean rustc/clippy/fmt/ShellCheck,
  shell pytest, embedded golden **11/11**, protected artifacts, persisted
  fingerprints, lifecycle checks, and registered `invariant-scan` **12 rules /
  51 controls**. Focused cycle tests passed **53/53**.
- constrained-Python acceptance: PASS. Clean Python **3.11.4** and
  **3.12.13** environments each resolved all **21** constraints, collected
  **306**, passed **306**, failed **0**, and skipped **0**. Each emitted the
  same one accepted `StarletteDeprecationWarning`.
  `tools/test_population.py` derived `collected=306`, `equivalent=true`, and
  `equivalent_passed=306`, with both populations passed 306 / skipped 0.
- protected-artifact acceptance: PASS. Manifest validation reported schema 2,
  **2 artifacts / 331 pinned files**. Two complete verifications matched every
  pin and both databases at **0.09 s / 0.10 s real**. The unchanged manifest
  is **191,395 bytes**, leaving **857,181 bytes** to 1 MiB.
- G1 acceptance: PASS by execution. Exactly four forward-boundary constants
  and all six pair relations were classified. Scope is independent of all
  three trigger boundaries; freshness must not follow identity or floor;
  identity and floor are mutually independent. A real throwaway checker
  passed before and after identity moved from `(0, 28)` to `(0, 22)`, while a
  stale governed cell still produced the exact v0.30 identity error. The
  lowered declaration is silently always-on whenever freshness is reachable
  and is itself unobservable. BOUNDARY-COVER is unblocked without a live P1
  reclassification.
- G2 acceptance: PASS by execution and exhaustive search. The two `run` pins
  carry `1.78.0`; the hosted pin carries `1.78`; normalization derived one
  value, `1.78`, with multiplicity three. Live `STATE.md:3763` instead stated
  offline `1.75`. The local net entry point is ambient and hosted net pins
  1.91; exact searches found **0** `rustup 1.86`, `cargo +1.86`, or workflow
  `toolchain: 1.86` constructions.
- G2 inventory acceptance: PASS. Exact tracked-text enumeration found **582**
  floor-stating lines: **300** in cycle documents, **205** in State archives,
  **24** in live State, and **53** elsewhere. Current executable pins and
  restatements are enumerated in `STATE.md`; historical records are classified
  separately. Identical syntax occurs in present and historical prose, so no
  general scan can distinguish them without metadata. FLOOR-BIND must carry a
  named, hand-maintained current-restatement registry and a permanent
  historical-exclusion obligation.
- G3 acceptance: PASS by execution in both full Git trees. At synthetic
  `v1.0`, automated `cycle-check` rejected the unrepresentable retention
  derivation and operator-local `export-check` passed at **2,524,391 bytes /
  152 files**. At synthetic `v1.3`, `cycle-check` passed while `export-check`
  rejected **4,605,031 bytes / 203 files**, **51** outside-depth cycle
  documents, and the ceiling. Automated lanes catch the loud `v1.0` case;
  none catches the silent `v1.3` case because export-check is operator-local.
- G4 acceptance: PASS by exhaustive search. Only `cycle_check.py`, its test,
  and the invariant self-test touch the governed table; none compares measured
  numeric content. The v0.29 audit child grew its progress record by exactly
  **4,965 repository bytes**, matching the delivered-export delta from
  **2,516,822** to **2,521,787**. That one appended audit-entry size is the
  named fixed-point residual; MARGIN-BIND owns the executable rule and empty
  record state.
- G5 acceptance: PASS. Comparable export points are v0.28 delivered
  **2,530,129**, v0.29 delivered **2,521,787** (−8,342), and v0.30 activation
  audit tree `e7b2c588…` **2,464,445** (−57,342). Three points yield only two
  interval observations, both negative, and support no growth rate. The exact
  activation export retained v0.28–v0.30 across **152** files and left
  **535,555 bytes / 17.85%**. Under the existing explicit planning
  denominators, State is nearer its trigger at **8.72 cycles** versus the
  export's **17.19**.
- G6 acceptance: PASS. The production and test SQL ordering clause bodies
  were byte-identical at **123 bytes**, SHA-256
  `47c5f7d45b5b92974f3f33de54be41cfeb06305db8221c7877f1c0a944f453aa`.
  A `macro_rules!` constructor can expand the one clause with distinct
  compile-time select/tail literals and no runtime formatting or allocation.
  ORDER-CONST is therefore unblocked rather than skipped.
- governed-record acceptance: PASS. All **20** deferred rows now carry
  v0.30-measured observations; the three architecture rows carry the exact
  activation export, manifest/timings, and clean two-lane warning result.
  `cycle-check` passed with active v0.30 open.
- control acceptance: PASS. `checklist-audit` remained **232 checked / 3
  retracted / 232 matched / 232 commits resolved / 0 exemptions** before the
  mandatory E0 checkbox. E0 edited neither `cycle_check.py` nor `sqlite.rs` and
  re-derived **0** planted-control line values. Focused SEC identity kept all
  **200 SEC** rows and dropped **0**.
- golden-E2E delta: **0** — embedded and final standalone executions each
  passed **11/11** byte-identically.
- publisher/ref acceptance: PASS. E0 issued no publisher request, ran no
  scheduler or model-profile command, and changed no cadence, dependency,
  schema, production source, manifest, protected byte, version authority, tag,
  or working-repository ref.

### 2026-07-31 · BOUNDARY-COVER — derive and bind the boundary family

- owner: Codex
- commit: 30e31c7f2ce4fda46d8a54f6bcbd9c8c9717fc59
- result: PASS. `module_forward_boundaries()` derives every
  `tools/cycle_check.py` module-global name ending in `_FORWARD_BOUNDARY`;
  the derived and registered sets are the same four names, and a fifth
  unregistered name is now an automatic error.
- decision-gate acceptance: PASS. G1 measured a lowered identity declaration
  as silently always-on inside freshness, not a reachable runtime defect, so
  no P1 reclassification applied.
- derivation acceptance: PASS. An exhaustive `tools/` declaration search found
  exactly four boundary constants, all in `cycle_check.py`, and direct
  execution printed identical derived and registry memberships. No member list
  participates in the derivation.
- namespace-bound acceptance: PASS with a named residual. The production
  docstring and R12 scope state that derivation is limited to
  `tools/cycle_check.py` module globals. No current boundary lies outside that
  namespace; a future boundary in another tools module remains explicitly
  outside this binding.
- semantic-relation acceptance: PASS. The registry states independent reasons
  for scope and freshness and declares freshness as the prerequisite for both
  identity and floor. The generic evaluator rejects identity or floor earlier
  than freshness without a hand-written pair comparison.
- rejection-before-acceptance: PASS. Before the complete green run, direct
  injection produced `tools/cycle_check.py module-scoped forward-boundary
  registry is missing PLANTED_UNREGISTERED_FORWARD_BOUNDARY`, and isolated
  identity reversal produced `TRIGGER_IDENTITY_FORWARD_BOUNDARY must be
  greater than or equal to TRIGGER_FRESHNESS_FORWARD_BOUNDARY`. R12 retains
  `floor-before-freshness` and adds `unregistered-forward-boundary`; disabling
  either production branch produces its named failure. R12 passed **24**
  controls and the complete registry passed **12 rules / 52 controls**.
- prior-control acceptance: PASS. The focused initialized-population,
  derived-registry, identity-order, and exhaustive missing-date pair tests
  passed **4/4**. The complete shell population passed **308/308** on Python
  3.11.4 and **308/308** on Python 3.12.13, each with zero skips and the same
  one governed Starlette warning.
- expected-line acceptance: PASS from real self-test output. The edit shifted
  **five existing** `cycle_check.py` values: boundary `1467 → 1500`, three
  freshness controls `1569 → 1646`, and carry-forward `1796 → 1873`. All five
  were re-derived; the new completeness control was registered at line 1500.
- complete-suite acceptance: PASS. The first sandboxed `ci-local` attempt
  failed only because the net wire test's loopback bind was denied; the
  authorized rerun passed all **20/20** jobs, including warning-denied **146**
  workspace tests, **62** net tests, locked Rust 1.78, clean
  rustc/clippy/fmt/ShellCheck, shell **308/308**, protected artifacts, and
  embedded golden **11/11**. The first sandboxed Python 3.12 run similarly
  measured eight permission failures from loopback binds/process inspection;
  its authorized rerun passed **308/308**.
- golden-E2E delta: **0** — embedded and final standalone executions each
  passed **11/11** byte-identically.
- surface/protected/publisher acceptance: PASS. No production source, route,
  response shape, `/v1/*` value domain, dependency, schema, manifest,
  protected byte, publisher configuration, scheduler state, version authority,
  tag, or working-repository ref changed. No publisher request, scheduler, or
  model-profile command ran.

### 2026-07-31 · FLOOR-BIND — bind the executable offline Rust floor

- owner: Codex
- commit: 31058371f3131cffe4ea06ff17783663ff1ad596
- result: PASS. The existing `version-check` entry point now derives the
  offline Rust floor from three executable pins, normalizes raw `1.78.0` and
  `1.78` forms to one value, and binds **22** named current restatements to
  derived 1.78.
- decision-gate acceptance: PASS. `run` and `.github/workflows/**` were read
  but are absent from the implementation diff. No hosted job, toolchain pin,
  or evidence topology changed.
- executable-authority acceptance: PASS. `run` yielded two raw `1.78.0`
  pins, the hosted MSRV job yielded one raw `1.78` pin, and explicit
  normalization derived one value, 1.78. `./run version-check` reported
  `pins=3`, `raw=[1.78, 1.78.0]`, and `normalized=1.78`.
- nonvacuity acceptance: PASS by rejection before acceptance. Removing all
  matches from either authority file produced its named zero-extraction error;
  changing the hosted pin to 1.79 produced an explicit normalized
  disagreement. The focused rejection population passed **4/4** before the
  complete green run.
- restatement acceptance: PASS. The hand-maintained
  `OFFLINE_MSRV_RESTATEMENTS` registry extracted **22** current statements,
  all equal to derived 1.78. Changing its README statement to 1.77 was
  rejected. The false live run-reference line remains as the retained
  `offline needs >= 1.75` claim and is immediately followed by its 1.78
  forward correction; the current rejected-dependency comment now uses the
  derived baseline.
- historical-record acceptance: PASS. No dated historical record was
  rewritten. `OFFLINE_MSRV_HISTORICAL_EXCLUSIONS` names the permanent manual
  exclusion obligation: cycle documents, State archives, `CHANGELOG.md`,
  evidence and observations, dated State narrative outside the current
  correction, and historical clauses inside current AGENTS, README,
  toolchain, and workflow text.
- existing-entrypoint acceptance: PASS. The binding executes inside
  `version-check`, already present in local and hosted lifecycle lanes; no new
  lane job was required.
- registered-control acceptance: PASS after the direct rejections. R12 adds
  independent `zero-authority-pins` and `stale-offline-restatement`
  constructions. Disabling either production branch produced the named
  finding at `tools/version_check.py:354`; R12 passed **26** controls and the
  full self-test passed **12 rules / 54 controls**.
- population-correction acceptance: PASS. The run-reference block preserves
  `49 Rust + 69 shell` as the v0.6 baseline and appends the measured current
  population, **146 Rust + 313 shell**. Python 3.11.4 and 3.12.13 each
  collected and passed **313/313** with zero skips and the same one accepted
  Starlette warning.
- operator-decision acceptance: PASS. The operator selected outcome 1 on
  2026-07-31 because it binds already-authorized executable evidence without
  changing lane topology. Exact searches returned zero `rustup run 1.86`,
  `cargo +1.86`, and workflow `toolchain: 1.86` constructions. The active
  deferred table now carries the unexecuted net-floor claim and its
  operator-selected trigger; it is not a project guarantee.
- complete-suite acceptance: PASS. The clean local entry point passed all
  **20/20** jobs, including warning-denied **146** workspace tests, **62** net
  tests, locked Rust 1.78 check/test, clean rustc/clippy/fmt/ShellCheck,
  shell **313/313**, protected artifacts, and embedded golden **11/11**.
  The lifecycle checker and `version-check` passed after the final State and
  runbook updates.
- golden-E2E delta: **0** — embedded and final standalone executions each
  passed **11/11** byte-identically.
- surface/protected/publisher acceptance: PASS. No dependency, production
  behavior, route, response shape, `/v1/*` value domain, schema, manifest,
  protected byte, publisher configuration, scheduler state, version
  authority, tag, or working-repository ref changed. No publisher request,
  scheduler, or model-profile command ran.

### 2026-07-31 · MARGIN-BIND — bind the governed export margin

- owner: Codex
- commit: 72ebc6dc4e4ac7ae401d171ebdc4680186424104
- result: PASS. At close, the one content-governed architecture export row now
  binds its visible and machine values to the last machine-readable export
  figure in this active cycle's append-only progress record.
- governed review-export measurement: tree=`e7b2c58814e2223d9899b83b3f3491344ce85337`; bytes=`2464445`
- decision-gate acceptance: PASS. Neither `docs/state-archive/**` nor
  `config/protected-artifacts.json` appears in the implementation diff. The
  task archived and registered nothing.
- independent-authority acceptance: PASS. The architecture row's
  `Governed review-export bytes` marker is first bound to its visible
  `export of **N bytes**` figure, then compared at close with the last exact
  progress field above. The progress field names the independently measured
  activation audit tree and its **2,464,445-byte** export; a row asserting
  itself cannot satisfy the second derivation.
- empty-state acceptance: PASS by execution. Before this audit field existed,
  the real active entry point reported
  `governed_export=exempt-open-empty-progress`. The focused open-empty
  construction returned the same named exemption, while the identical empty
  progress record in closed state produced a required error. With this field
  present, the open cycle takes `exempt-open-latest-at-close`; both exemptions
  expire at close.
- fixed-point acceptance: PASS. `AGENTS.md` now states that the governed value
  is the last tree measurable when the row is written, in either direction.
  The subsequent append-only closing record is the named **cycle-ending audit
  delta**, recorded separately rather than masquerading as a newer governed
  measurement. The measured prior instance remains **+4,965 export bytes**,
  exactly one v0.29 audit append.
- rejection-before-acceptance: PASS. Focused tests first rejected a
  superseded figure and a closed empty record **2/2**. R12 then rejected the
  `superseded-export-figure` construction at `tools/cycle_check.py:1863`
  before the complete acceptance population ran.
- content-scope acceptance: PASS. Only the architecture subject beginning
  `review-export size and retention bound` is content-bound. All other
  governed subjects are explicitly outside the heterogeneous content rule
  while retaining their existing date and active-cycle identity checks.
- expected-line acceptance: PASS from real self-test output. The edit shifted
  **six existing** cycle-checker values: two boundary controls
  `1500 → 1519`, three freshness controls `1646 → 1665`, and carry-forward
  `1873 → 2041`. The new margin control is registered at line 1863. The final
  distribution is **22** controls into `cycle_check.py` and **6** into
  `sqlite.rs`.
- fixture-correction record: the first complete lifecycle-test run passed 57
  and failed two old fixture assumptions: it omitted the fifth boundary and
  left the new export trigger present in a zero-population construction. The
  first correction attempt had an indentation error and collected no tests.
  After both fixture and indentation corrections, the complete file passed
  **59/59**.
- complete-suite acceptance: PASS. Full R12 passed **27** controls and the
  complete self-test passed **12 rules / 55 controls**. The clean local entry
  point passed all **20/20** jobs, including warning-denied **146** workspace
  tests, **62** net tests, locked Rust 1.78, clean
  rustc/clippy/fmt/ShellCheck, shell **317/317**, protected artifacts, and
  embedded golden **11/11**. Python 3.11.4 and 3.12.13 each collected and
  passed **317** with zero skips and the same one accepted warning.
- golden-E2E delta: **0** — embedded and final standalone executions each
  passed **11/11** byte-identically.
- surface/protected/publisher acceptance: PASS. No dependency, production
  behavior, route, response shape, `/v1/*` value domain, schema, manifest,
  protected byte, publisher configuration, scheduler state, version
  authority, tag, or working-repository ref changed. No publisher request,
  scheduler, or model-profile command ran.

### 2026-07-31 · ORDER-CONST — declare archive recency SQL once

- owner: Codex
- commit: 1df89718d7c6c58ae0c4c4d50b2aec0c20627700
- result: PASS. One `macro_rules!` construction now expands the one archive
  ordering literal into both the production coverage-boundary query and the
  test-side SQL derivation.
- decision-gate acceptance: PASS. E0 proved the construction can use
  compile-time `concat!` with no runtime formatting or allocation. The
  implementation commit contains no `apps/cored/src/main.rs` or
  `crates/ingest/src/**` path.
- declaration/behavior acceptance: PASS. Exact search found one ordering
  clause and two macro call sites. The select prefixes and tails remain
  distinct compile-time literals; no predicate, parameter, ordering term, or
  production limit changed.
- rejection-before-acceptance: PASS with one earlier non-result recorded. An
  initial incomplete `--exact` test name ran zero tests and was not treated as
  evidence. The corrected cross-ordering test passed **1/1**; changing only
  `published_raw DESC` to `ASC` in the shared SQL clause then failed **0/1**
  with SQL-derived ids on the left and Rust-derived ids on the right.
  Restoring `DESC` made the same test pass **1/1**.
- prior-binding acceptance: PASS. The unchanged
  `coverage_boundary_uses_archive_order_for_a_misordered_window` test passed
  **1/1** after the refactor.
- SEC-identity acceptance: PASS. The diagnostic measured **201** aggregate
  inputs, **201 kept**, and **0 dropped**: **200 SEC kept / 0 dropped** plus
  the one non-SEC fixture document.
- expected-line acceptance: PASS from real self-test output. Five existing
  store controls moved: R1 `780 → 793`; R5 `230 → 242`, `229 → 241`, and
  `829 → 842`; and R7 `397 → 410`. The R5 line-33 control was unchanged. All
  six store controls re-executed; R12 passed **27** controls and the full
  self-test passed **12 rules / 55 controls**. The v0.30 cumulative shifted
  count is **11**.
- lifecycle correction record: the first complete local gate stopped before
  builds because the deferred action's `Steps 4 and 5` wording named no
  literal discharging `Step N`. Correcting that record to `Step 4 and Step 5`
  made `cycle-check` pass. This was a measured non-pass, not a product failure.
- complete-suite acceptance: PASS. The result-of-record `./run ci-local`
  passed all **20/20** jobs, including warning-denied **146** workspace tests,
  **62** net tests, locked Rust 1.78, clean rustc/clippy/fmt/ShellCheck,
  shell **317/317**, protected artifacts, and embedded golden **11/11**.
  Python 3.11.4 passed **317/317**. A first sandboxed Python 3.12 run passed
  309 and failed eight because loopback binds and `ps` were denied; the
  authorized result-of-record rerun passed **317/317**, with zero skips and
  the same one accepted warning.
- golden-E2E delta: **0** — embedded and final standalone executions each
  passed **11/11** byte-identically.
- surface/protected/publisher acceptance: PASS. The `/ingest` response shape
  and every `/v1/*` value domain are unchanged. No dependency, production
  behavior, route, schema, manifest, protected byte, publisher configuration,
  scheduler state, version authority, tag, or working-repository ref changed.
  No publisher request, scheduler, or model-profile command ran.
