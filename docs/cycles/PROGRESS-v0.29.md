# PROGRESS-v0.29.md — append-only execution record

This file records v0.29 task and gate events after their implementation
commits exist. Each entry names the measured result, every applicable
acceptance criterion, the golden delta, and the real implementation commit.
Entries are append-only; corrections are new dated entries.

### 2026-07-31 · ACTIVATE — v0.29 admitted after two measured draft corrections

- owner: Codex
- commit: 1cf49cf8e1574b7ac6ac1c43ca16ee8794da7e38
- corrective commit: b3228b1ed018e09693f0760a7faaa6d5df5bf788
- result: PASS after two author-side activation defects were measured and
  corrected without amending, rebasing, or squashing either commit. The draft
  repeated the reserved cycle-closing token in prose while every task remained
  unchecked, and it refreshed only the deferred governed table while all three
  trigger-bearing architecture rows still named v0.28. The first committed
  `./run cycle-check` exited 1 and named both defect classes. The dated
  amendment removes the reserved token from prose, records reviewer errors five
  and six, discloses Step 8's corrected preservation count, and remeasures the
  three architecture rows for v0.29. The exact entry point then passed with
  active v0.29 open, twenty-six closed execution runbooks, and three historical
  runbooks.
- worktree acceptance: PASS with the supplied draft accounted for. Before
  activation, the sole worktree item was the operator-supplied untracked
  `docs/cycles/TASKS-v0.29-EXECUTION.md`. Activation commit `1cf49cf…`
  contains that runbook, the `AGENTS.md` v0.29 declaration, the progress
  skeleton, and the runbook-mandated `repomix.config.json` retention edit. The
  runbook's contradictory three-file/same-activation wording is reconciled by
  its dated amendment; no other path entered the activation commit.
- entering-ref acceptance: PASS with the drafted branch relationship corrected.
  Before activation, HEAD was v0.28 audit record
  `d9ecea493d3bc254051a0fa87fafe0b244cb0d19` on
  `codex/v0.23-action-migration`, whose immediate parent was recorded v0.28
  closure `ec8eaa2ab7c8c23d5a923a08ae36ab7692b4b664`. Locally recorded
  `origin/main` and the peeled v0.17.0 tag both resolved to
  `4af2841816dd3e43fb8423153b91aa22ccb87537`; HEAD was 23 commits ahead
  and zero behind that remote-tracking ref. Local `main` remained stale at
  `eb2d9df8b3ffd3e0380d506e958fb5a3adb2d42e`. No ref moved, and no mutable
  `origin/main` hash was added to `STATE.md`'s header.
- retention acceptance: PASS. Activation moved the tracked ignore glob from
  `2[0-5]` to `2[0-6]`. On corrective tree `b3228b1…`, the exact project-root
  `./run export-check` passed **99 derived / 7 required / 152 exported** at
  **2,411,393 bytes**, retaining exactly v0.27, v0.28, and v0.29 beneath the
  **3,000,000-byte** ceiling.
- lifecycle acceptance: PASS after the recorded corrections.
  `checklist-audit` passed **224 checked / 3 retracted / 224 matched / 0
  exemptions**. Before this entry existed, `progress-check` correctly exited 1
  because the new skeleton contained no dated progress entry.
- artifact acceptance: PASS at the preparatory checkpoint. Manifest validation
  reported schema 2 with **2 artifacts / 316 pinned files**; two complete
  `verify-artifacts` runs matched every pin and both protected databases at
  **0.09 s / 0.09 s real**. The manifest measured **182,780 bytes** and no
  protected or pinned byte changed.
- scope acceptance: PASS. The activation commit is the scope anchor; the
  declared no-release intent requires no release-authority path at activation.
  The compatibility correction used only the declared `ARCHITECTURE.md`
  permission plus the standing runbook path.
- test acceptance: NOT RUN at this preparatory checkpoint; E0 owns the clean
  rebuild, complete 20-job matrix, and both constrained Python populations.
- golden-E2E delta: NOT MEASURED; no claim.
- publisher-request acceptance: PASS. Activation used repository, local Git,
  protected-byte verification, and the operator-local export only; it made no
  request to a publisher origin and ran no scheduler.

### 2026-07-31 · ACTIVATE-AMENDMENT — scope fixture aligned to v0.29

- owner: Codex
- commit: b92902edf861e4a3a21eba509519c0b9b46b2870
- result: PASS. The first permission-complete E0 `./run ci-local` passed
  release/cycle/checklist checks, registered invariants **12/49**, evidence,
  warning-denied workspace and net Rust lanes, clippy, fmt, and locked Rust
  1.78 before the shell lane collected **303**, passed **302**, and failed the
  v0.28 exact-current-cycle assertion that release-authority/forbid overlap
  must be empty.
- correction acceptance: PASS. The active v0.29 table intentionally makes
  `shell/intel_shell/__init__.py` and `shell/intel_shell/app.py` both release
  authorities and matches both with the broad shell-source forbid; documented
  release-authority precedence is unchanged. The fixture now derives that
  overlap independently with Python's standard `fnmatchcase` over the parsed
  table and the separately enumerated release-authority paths. No expected
  overlap value is hardcoded and no production checker behavior changed.
- focused acceptance: PASS. Constrained Python 3.11 ran
  `shell/tests/test_cycle_check.py` at **50/50**, and the real
  `cycle-check` entry point passed with active v0.29 open.
- environment acceptance: PASS with one non-result recorded. The first
  sandboxed full CI attempt reached the net lane but could not bind its
  loopback wire-test server. The permission-complete rerun passed that lane and
  exposed the fixture failure above; it is the result used for the correction.
- golden-E2E delta: NOT MEASURED in this compatibility checkpoint; E0 restarts
  from this committed correction and owns the complete matrix plus standalone
  golden.
- publisher/protected acceptance: PASS. No publisher or scheduler command ran,
  and no protected or pinned file changed.

### 2026-07-31 · E0 — entering state rebuilt and G1–G7 settled

- owner: Codex
- commit: 64ebc2eaa2955a6f0974a5654deddb97c31eece0
- result: PASS. The permission-complete clean rerun passed all **20/20**
  `ci-local` jobs. The entering closure and audit commits were where the
  corrected activation record placed them, the E0 entry tree after the
  committed scope-fixture correction was clean, and no decision gate tripped.
- complete-suite acceptance: PASS. Warning-denied Rust execution passed
  **146** workspace tests and **62** net tests (**32** ingest including three
  replay tests, plus **30** cored), locked Rust 1.78, clippy, rustfmt,
  ShellCheck, `invariant-scan` **12 rules / 49 controls**, embedded golden
  **11/11**, protected-artifact verification, and persisted-fingerprint
  verification. The separately required post-task `./run golden` passed
  **11/11**.
- constrained-Python acceptance: PASS. Clean Python **3.11.4** and **3.12.13**
  environments each resolved all **21** exact constraints and each reported
  `collected=303`, `passed=303`, `failed=0`, and `skipped=[]`.
  `tools/test_population.py` independently derived `collected=303`,
  `equivalent=true`, and `equivalent_passed=303`, with local and comparison
  populations both passed 303 / skipped 0. Each lane emitted the same one
  accepted `StarletteDeprecationWarning`; no dependency byte changed.
- protected-artifact acceptance: PASS. Manifest validation reported schema 2,
  **2 artifacts / 316 pinned files**. Two complete verification runs matched
  every pin and both protected databases at **0.11 s / 0.10 s real**. The
  unchanged manifest is **182,774 bytes**. This forward-corrects the activation
  record's false **182,780-byte** transcription without changing the manifest,
  pin count, or prior verification outcome.
- G1 acceptance: PASS by execution. A no-hardlink throwaway clone with active
  v0.29 and the stale `2[0-5]` glob ran the real export and exited 1 with
  `unexpected cycle document outside retention depth 3` for exactly
  `docs/cycles/PROGRESS-v0.26.md` and
  `docs/cycles/TASKS-v0.26-EXECUTION.md`, followed by
  `FAIL (2 defect(s); derived_sources=99, exported=154)`. The configured local
  lane has 20 jobs with no export-check and the hosted workflow has zero
  `export` occurrences.
- G2 acceptance: PASS; Step 2 is unblocked. The proposed automatic check reads
  tracked `repomix.config.json` and compares its retention pattern with an
  independent derivation from the active cycle and
  `CYCLE_RETENTION_DEPTH`, without an export in existence. `export-check`
  inspects an operator-created artifact's actual paths, size, and excluded
  bytes. These are different objects, so the proposal neither duplicates the
  operator-local check nor reopens v0.22 G3.
- G3 acceptance: PASS by reproduction. A throwaway active-v0.25 clone with
  freshness moved to `(0, 28)` and floor moved to `(0, 23)` ran the real
  checker and raised `UnboundLocalError` for unbound
  `architecture_trigger_rows`. The current `(0, 28) >= (0, 23)` relationship
  makes the path latent, but nothing binds the required
  `floor >= freshness` ordering.
- G4 acceptance: PASS by execution. A throwaway Rust store fixture containing
  known-day and NULL-day rows in both the held archive and incoming window
  executed one focused test and passed. SQL selected held raw
  `2026-07-10`; Rust selected incoming raw `incoming-null-raw`, confirming
  agreement over known/null, day, raw-byte, and id terms. An earlier
  incorrectly exact-filtered command executed zero tests and is a construction
  non-result. The two orderings have no permanent binding today.
- G5 acceptance: PASS. The architecture row's labelled Step 5 measurement was
  **2,485,846 bytes / 514,154 bytes / 20.68%** headroom; the closing tree
  measured **2,526,556**, and the delivered export **2,530,129**. The selected
  rule is that a governed row carries the latest measurement available at
  close while preserving earlier measurements as openly superseded history.
- G6 acceptance: PASS with no traffic. The recorded design bounds a later,
  separately authorized scheduler window to **1,260 seconds** and at most
  three SEC invocations at the unchanged **600-second** cadence, using fresh
  unprotected archive/state paths and an isolated SEC-only schedule copy. It
  enumerates preflight, origin/cadence/count, coverage, exception, database,
  and deadline refusals. Proven inputs are pre-insert coverage detection,
  order-independent boundaries, the corrected window-advance criterion, and
  the pinned **4,650 / 600 = 7.75×** margin. Recurring execution, peak-season
  density, deadline-day density, and uncovered hours remain unproven.
- G7 acceptance: PASS. Tagged v0.17.0 still uses positional
  `.iter().rev().find_map(...)`; unpublished descendant `e6b3c1e` owns the
  comparator correction. The consequence is one wrong raw boundary string in
  an internal diagnostic for a misordered window: no dropped row, response
  shape change, `/v1/*` field change, or public serialized value-domain change.
- growth acceptance: PASS by derivation. Normalizing the **453,741-byte**
  v0.28 starting State for its later **252,237-byte** mechanical removal gives
  **201,504**; final **224,029** means **22,525 bytes/cycle** of live-State
  growth. The manifest grew **8,622 bytes**, from 174,152 to 182,774. The real
  delivered-to-activation export rollover decreased **118,736 bytes**, from
  2,530,129 to 2,411,393, so that negative observation yields no finite
  exhaustion estimate. The deliberately narrow positive State-plus-manifest
  denominator is **31,147 bytes/cycle**. The final E0 implementation export
  passed at **2,430,678 bytes / 152 files**, leaving **569,322 bytes / 18.98%**
  or **18.28 cycles** at that planning denominator.
- governed-record acceptance: PASS. All **17** deferred rows now carry E0's
  v0.29 measured observations. The three live architecture trigger rows carry
  the final E0 export, actual manifest/timings, and clean two-lane warning
  result. `cycle-check` passed with active v0.29 open.
- golden-E2E delta: **0** — standalone **11/11** before implementation and
  **11/11** after the completed task record.
- publisher/ref acceptance: PASS. E0 ran no scheduler, issued no publisher
  request, changed no protected or pinned byte, and created, moved, or deleted
  no ref.

### 2026-07-31 · RETENTION-BIND — active cycle binds the tracked export glob

- owner: Codex
- commit: b06e1e583c580e2e7be96bbddd76c1d5e550282a
- result: PASS. `cycle-check` imports the one
  `tools.export_check.CYCLE_RETENTION_DEPTH` authority and derives the expected
  tracked Repomix brace pattern from the active declaration. It does not create
  or inspect an export.
- decision-gate acceptance: PASS. G2 established that the automatic rule
  checks configuration intent, whereas operator-local `export-check` checks an
  actual artifact's path population, size, and excluded bytes. v0.22 G3 is not
  reopened and no hosted export duplicate was added.
- rejection-before-acceptance: PASS. Before changing the tracked glob, the real
  checker exited 1 and required
  `docs/cycles/{TASKS,PROGRESS}-v0.{[0-9],1[0-9],2[0-6]}{.md,.*.md,-*.md}`;
  it named the still-present `[6-9]` alternative as the sole found mismatch.
  After the config moved to the derived zero-based range, the same entry point
  passed. The added v0.0–v0.5 matches name no existing path and change no
  export member.
- derivation acceptance: PASS. No expected retention string is stored in the
  checker or its tests. The numeric brace alternatives are generated from the
  active cycle's last component and the imported depth; the fixed prefix and
  filename suffix express path grammar, not a cycle endpoint.
- automatic-lane acceptance: PASS. `cycle-check` is already a blocking local
  and hosted lifecycle entry point. Its no-export fixture confirms no
  `repomix-output-*.xml` exists, corrupts the tracked pattern, and observes the
  named rejection. Focused lifecycle plus invariant tests passed **73/73**.
- registered-control acceptance: PASS. R12 independently appends a stale suffix
  to the active-cycle derivation and invokes the production check. Disabling
  the mismatch branch produces
  `review-export-retention planted controls were not detected:
  stale-retention-pattern`. Registered invariants pass **12/12 rules / 50
  controls**, with R12 now **22**.
- shell acceptance: PASS at the permission-complete entry point: collected
  **304**, passed **304**, failed **0**, skipped **0**, with the one governed
  Starlette warning. A preceding sandboxed attempt passed 296 and failed eight
  only at denied loopback binds/process-table inspection; it is an environment
  non-result.
- export acceptance: PASS. The completed implementation tree's real
  project-root export reports **99 derived / 7 required / 152 exported** at
  **2,446,347 bytes**, retention depth 3, under the 3,000,000-byte ceiling.
  Retained paths remain exactly v0.27–v0.29 and both excluded byte classes
  remain absent.
- golden-E2E delta: **0** — standalone **11/11**, byte-identical.
- surface/protected/publisher acceptance: PASS. No production source, route,
  response shape, `/v1/*` value domain, dependency, schema, protected or
  pinned byte, publisher configuration, scheduler state, or ref changed. No
  publisher request or scheduler run occurred.

### 2026-07-31 · BOUNDARY-BIND — reversed boundaries report, never traceback

- owner: Codex
- commit: ec4a05c1618b2baed6b835a39c84b9d44b7ba8ea
- result: PASS. Both governed row counts are initialized before either forward
  gate, and an explicit relationship check rejects
  `TRIGGER_FLOOR_FORWARD_BOUNDARY < TRIGGER_FRESHNESS_FORWARD_BOUNDARY`.
- decision-gate acceptance: PASS. G3 showed the live `(0, 28) >= (0, 23)`
  relationship makes the unbound path latent, so no P1 reclassification was
  needed.
- no-unbound acceptance: PASS by reproduction. The test sets freshness to
  `(1, 2, 4)`, floor to `(1, 2, 2)`, and executes the real checker against
  active v1.2.3 between them. It exits 1 with
  `TRIGGER_FLOOR_FORWARD_BOUNDARY must be greater than or equal to
  TRIGGER_FRESHNESS_FORWARD_BOUNDARY`; `UnboundLocalError` is absent, and the
  initialized populations reach their named zero-row errors.
- asserted-relationship acceptance: PASS. R12 independently reverses the two
  module constants and invokes the production relationship check. Disabling
  the condition yields the reconstructible
  `trigger-boundary-order planted controls were not detected:
  floor-before-freshness` failure.
- branch-collapse acceptance: PASS. The exhaustive
  `required_cycle_name is None` / `is not None` pair is one
  `if not valid_dates` branch. A direct entry-point test proves both modes
  retain one missing-date error, while active-cycle mode retains its separate
  missing-cycle-identity error.
- test acceptance: PASS. Focused lifecycle/invariant tests passed **75/75**;
  the permission-complete shell population collected and passed **306/306**
  with zero skips and the one governed Starlette warning. Registered
  invariants passed **12/12 rules / 51 controls**, with R12 at **23**.
- export acceptance: PASS. The completed implementation tree reports **99
  derived / 7 required / 152 exported** at **2,456,371 bytes**, retaining
  v0.27–v0.29 under depth 3 and both excluded byte classes.
- golden-E2E delta: **0** — standalone **11/11**, byte-identical.
- surface/protected/publisher acceptance: PASS. No production source, route,
  response shape, `/v1/*` value domain, dependency, schema, protected or
  pinned byte, publisher configuration, scheduler state, or ref changed. No
  publisher request or scheduler run occurred.

### 2026-07-31 · ORDER-BIND — SQL and Rust archive ordering cross-checked

- owner: Codex
- commit: 5e7e87cc10c1e991d84c70834336fe6a41ceec7f
- result: PASS. A test-only store fixture orders held and incoming documents
  independently through SQLite and `archive_recency_cmp`, then compares each
  production boundary against the other implementation's derived result.
- scope/blast-radius acceptance: PASS. The only Rust diff is below
  `#[cfg(test)]` in `crates/store/src/sqlite.rs`; forbidden cored and ingest
  paths are byte-identical. The bounded consequence remains one wrong raw
  boundary string in an internal observational diagnostic if a future
  divergence occurs, not data loss or a failed poll.
- rejection-before-acceptance: PASS. Temporarily changing only the production
  held query to `published_day IS NULL DESC` made the focused test execute and
  fail with SQL `Some("z-null")` versus Rust `Some("z-raw")`. A preceding
  compile attempt exposed a test-helper statement lifetime and is not counted
  as the rejection result. The SQL mutation was removed before any valid
  result or commit.
- independent-binding acceptance: PASS. The fixture contains NULL-day rows on
  both held and incoming sides and discriminates known/null, day, raw-byte, and
  id terms. SQL full ordering is compared to Rust ordering; production SQL's
  held boundary is compared to Rust's first document; production Rust's
  incoming boundary is compared to a separately inserted SQL ordering's last
  document. No expected output is hardcoded.
- existing-test acceptance: PASS. The unchanged
  `coverage_boundary_uses_archive_order_for_a_misordered_window` passed **1/1**;
  the new cross-ordering test passed **1/1** after the planted mutation was
  removed.
- store/identity acceptance: PASS. The complete store suite passed **24 unit +
  2 integration** tests. The SEC identity measurement reported **201 aggregate
  kept / 0 dropped**, consisting of **200 SEC kept / 0 dropped** plus one news
  baseline; SEC pairs remained **19,900** and cross-issuer drops **0**.
- format/export acceptance: PASS. `cargo fmt --all -- --check` passed. The
  completed implementation export reports **99 derived / 7 required / 152
  exported** at **2,464,830 bytes**, retains v0.27–v0.29 at depth 3, and
  contains neither excluded byte class.
- golden-E2E delta: **0** — standalone **11/11**, byte-identical.
- surface/protected/publisher acceptance: PASS. `/ingest` response shape is
  unchanged; every `/v1/*` field and serialized value domain is unchanged. No
  dependency, schema, protected or pinned byte, publisher configuration,
  scheduler state, or ref changed. No publisher request or scheduler run
  occurred.
