# PROGRESS-v0.28.md — append-only execution record

This file records v0.28 task and gate events after their implementation
commits exist. Each entry names the measured result, every applicable
acceptance criterion, the golden delta, and the real implementation commit.
Entries are append-only; corrections are new dated entries.

### 2026-07-30 · ACTIVATE — v0.28 admitted with one measured draft correction

- owner: Codex
- commit: c44af842d42cf350aab575ea14c22be508c54bd3
- corrective commit: 18b2c23dbc0e64b06fe9dc178c55ecd6e6256610
- result: PASS after an author-side activation defect was measured and corrected
  without amending, rebasing, or squashing either commit. The supplied draft
  included the checker's reserved cycle-closing heading while every task
  remained unchecked, both as a premature empty template and as literal prose
  inside G2. The first committed `./run cycle-check` exited 1. The dated
  runbook amendment removes the template and rephrases only the reserved token;
  the exact entry point then passed with active v0.28 open, twenty-five closed
  execution runbooks, and three historical runbooks.
- worktree acceptance: PASS with the supplied draft accounted for. Before
  activation, the only worktree item was the operator-supplied untracked
  `docs/cycles/TASKS-v0.28-EXECUTION.md`. Activation commit `c44af84…`
  contains only that runbook, the `AGENTS.md` v0.28 declaration, and this
  progress-log skeleton. The syntax correction is isolated in `18b2c23…`.
- entering-ref acceptance: PASS with the runbook's branch-name hypothesis
  corrected. Before activation, HEAD was post-push audit
  `ddf08d2063f384d6c3d6d5ddef87b65a9167625c` on branch
  `codex/v0.23-action-migration`, not local `main`. The locally recorded
  `origin/main` is its immediate ancestor (`origin/main...ddf08d2` measured
  `0 1`); local `main` remains the stale
  `eb2d9df8b3ffd3e0380d506e958fb5a3adb2d42e`, 102 commits behind
  `origin/main`. No ref changed, and no mutable branch hash was added to
  `STATE.md`'s header.
- lifecycle acceptance: PASS after the recorded syntax correction.
  `checklist-audit` passed **216 checked / 3 retracted / 216 matched / 0
  exemptions**. Before this entry existed, `progress-check` correctly exited 1
  because the new skeleton had no dated progress entry.
- scope acceptance: PASS. The activation commit is the scope anchor; the
  declared static no-release intent requires no release-authority paths, and
  the active runbook, progress record, and `STATE.md` are standing-allowed.
- test acceptance: NOT RUN at this preparatory checkpoint; E0 owns the complete
  entering matrix and drafted-gate measurements.
- golden-E2E delta: NOT MEASURED; no claim.
- publisher-request acceptance: PASS. Activation used only repository and local
  Git-object commands; it made no request to a publisher origin.
- protected artifact delta: NOT MEASURED; no protected or pinned file changed.

### 2026-07-30 · ACTIVATE-AMENDMENT — lifecycle fixtures aligned to v0.28

- owner: Codex
- commit: be5b9e1827cd4a2a870512f53b5c1baa94e9f413
- result: PASS. The first permission-complete E0 `./run ci-local` measured two
  shell failures after every preceding Rust, invariant, lifecycle, lint, MSRV,
  and net job passed: the active deferred population was `(2, 15)` while the
  v0.27 fixture expected `(2, 14)`, and v0.28's no-release scope derived zero
  release-authority/forbid overlaps while the v0.27 fixture expected
  `shell/intel_shell/app.py`.
- correction acceptance: PASS. The dated runbook amendment permits only the two
  exact-current-cycle fixture corrections. Focused
  `shell/tests/test_cycle_check.py` passed **45/45**, and `cycle-check` passed
  with v0.28 open. No checker implementation changed. Step 3 remains responsible
  for replacing the temporary exact trigger-population assertion with a derived
  expectation.
- environment acceptance: PASS with one non-result recorded. The first
  sandboxed `ci-local` attempt reached the net lane but its loopback wire server
  was denied by the execution sandbox; the permission-complete rerun passed that
  exact test and the complete net lane before reaching the two lifecycle-fixture
  failures above.
- golden-E2E delta: NOT MEASURED in this corrective checkpoint; E0 restarts and
  owns the complete matrix plus standalone golden.
- publisher-request acceptance: PASS. No publisher or scheduler command ran.
- protected artifact delta: PASS. No protected or pinned file changed.

### 2026-07-30 · E0 — entering state rebuilt and G1–G7 settled

- owner: Codex
- commit: 5d73b2936d3f94883dbc6b2d3a7fb1e84713175a
- result: PASS. Every entering hypothesis and gate answer is recorded in
  `STATE.md` and the runbook's dated E0 amendment; differences from the draft
  are corrections, not silently retained assertions.
- entering-matrix acceptance: PASS. Permission-complete `./run ci-local` passed
  all **20/20** jobs with warning-denied **145** workspace tests, **62** net
  tests, locked Rust 1.78, clean rustc/clippy/fmt/ShellCheck,
  `invariant-scan` **12 rules / 46 controls**, embedded golden, protected
  artifacts, and lifecycle checks. Standalone golden passed **11/11**.
- shell-population acceptance: PASS. Clean constrained Python 3.11.4 and
  3.12.13 lanes each collected/passed **293**, failed zero, and skipped zero.
  `tools/test_population.py` derived `collected=293`, `equivalent=true`, and
  `equivalent_passed=293`.
- artifact acceptance: PASS. Both complete verifications matched **301** pins
  and both protected databases at **0.10 s / 0.10 s real**. The manifest
  measured **174,152 bytes**, below 1 MiB.
- lifecycle/shape acceptance: PASS with drafted values corrected. The
  architecture table measured **11 data / 2 governed** rows, the active
  deferred table **15 governed** rows, and `checklist-audit` **216 checked / 3
  retracted / 216 matched / 0 exemptions**. Entering `STATE.md` measured
  **6,984 lines / 453,741 bytes** and its seven regions measured **12,540 /
  17,273 / 127,922 / 185,799 / 43,650 / 38,748 / 27,809 bytes**.
- G1 acceptance: PASS by execution. Blanking every deferred measured cell while
  retaining a dated column header made `cycle-check` exit **0**. All real
  governed rows carry their own date, so removing a real header token would
  reject zero current rows.
- G2 acceptance: PASS. v0.24–v0.27 each close on `2026-07-30`; a date-only
  discriminator distinguishes at most one cycle on that date.
- G3 acceptance: PASS by execution. The current call discarded derived counts
  and only the temporary lifecycle fixture consumed `(2, 15)`. Setting every
  trigger to `none` derived `(0, 0)` and `cycle-check` exited **0**.
- G4 acceptance: PASS. The exact project-root `./run export-check` passed **99
  derived / 7 required / 182 exported**. The retained export was **4,975,987
  bytes**, **99.52%** of decimal 5 MB with **24,013 bytes** headroom. Raw
  composition was cycle docs **34 / 1,435,284**, observations **13 / 949,344**,
  root **12 / 713,006**, state archive **1 / 297,739**, and other reviewed
  paths **122 / 1,564,264**. The 2026-07-30 external observation remains
  **2,067 chunks / 2,000 limit**. Source inspection confirmed no ceiling.
- G5 acceptance: PASS by execution. Moving closed v0.24 in a throwaway clone
  left both commands at exit **0**, while `cycle-check` closed coverage fell
  **25 → 24** and checklist checked/matched coverage fell **216 → 209**.
  `audit_deferred`'s complete-progress-glob assertion still passed.
- G6 acceptance: PASS. The unstated ordering assumption and
  `incoming.last()`-equivalent implementation are recorded with the bounded
  effect: a misordered window can misreport one diagnostic string, while the
  poll still commits and identity is unchanged.
- G7 acceptance: PASS with no implementation. The public value-domain and named
  response-shape release criteria are enumerated at their exact authorities.
  No bounded detector exists without a machine-readable historical contract;
  their honest prose-adjudicated status remains.
- deferred-table acceptance: PASS. All **15** governed rows now carry
  E0-remeasured observations containing both `v0.28` and `2026-07-30`.
- environment acceptance: PASS with non-results named. Sandboxed loopback,
  dependency-install, population-wrapper, and direct networked Repomix attempts
  were not interpreted as measurements. Their actual entry points passed under
  the required permissions; Repomix was downloaded with scripts disabled
  outside the repository and executed against repository bytes only with
  network denied after explicit operator authorization.
- golden-E2E delta: **0**; embedded and post-record standalone outcomes remain
  byte-identical at **11/11**.
- publisher/ref/protected acceptance: PASS. No publisher request, scheduler,
  model-server session, historical ref movement, protected-byte change,
  dependency change, route change, or public value-domain change occurred.

### 2026-07-30 · TRIGGER-IDENTITY — freshness bound to the active cycle

- owner: Codex
- data commit: 5342663f89e3e2b499bfc1bf42b15c44705de58b
- commit: 3e80d0b79f7151cc4ee28b516d73d46e09b85b1c
- result: PASS. The mandatory data-first commit re-measured only the two
  trigger-bearing architecture rows with row-owned `v0.28` and ISO-date
  tokens. The rule-second commit removes the header fallback, preserves
  v0.23-forward own-cell date freshness, and requires v0.28-forward exact
  active-cycle identity resolved through `resolve_cycle(root)`. No closed
  runbook changed.
- separate-commit acceptance: PASS. Data commit `5342663…` passed the
  pre-tightening `cycle-check`; rule commit `3e80d0b…` passed the tightened
  checker. The implementation hashes are distinct, adjacent, and ordered data
  before rule.
- planted-control acceptance: PASS by execution. R12 retains its generic
  missing-date mutation as control 15 and gains two independent controls:
  control 16 catches a row with no own-cell date even when the header carries
  `2026-07-30`; control 17 catches a `v0.27` row supplied to the active v0.28
  checker. Each mutation's configured `expected_fail` matched the real
  self-test output.
- invariant acceptance: PASS. `./run invariant-scan --self-test` derived
  **12/12 rules / 48 controls**, including R12 **20/20**. No aggregate control
  total is hardcoded in tooling or tests.
- lifecycle acceptance: PASS. Focused
  `shell/tests/test_cycle_check.py` passed **46/46**. The real
  `./run cycle-check` passed with active v0.28, 25 closed execution runbooks,
  three historical runbooks, and both governed live tables in the new format.
- golden-E2E delta: **0**. The first sandboxed invocation could not bind its
  isolated loopback port and was recorded as an environment non-result. The
  permission-complete execution of the exact `./run golden` entry point passed
  **11/11** byte-identically.
- publisher/ref/protected acceptance: PASS. No publisher request, scheduler,
  model-server session, closed document, production runtime source, dependency,
  schema, protected artifact, golden input, public route, serialized value
  domain, tag, or branch ref changed.

### 2026-07-30 · TRIGGER-FLOOR — population and carry-forward enforced

- owner: Codex
- commit: 1dde546029fbaf4f1b84c7628f07e06587d99316
- result: PASS. The active call site binds both governed-row counts, rejects
  either table at zero, and checks immediately prior deferred subjects against
  the active table or a valid ISO-dated **Deferred completions** table. The
  prior runbook is selected by version from `execution_runbooks()` and is not
  hardcoded.
- population acceptance: PASS by derivation and execution. The focused test
  derives expected counts from both live tables rather than a numeric literal;
  the real result is **2 architecture / 15 deferred**. A planted all-`none`
  construction made `cycle-check` name and reject both zero-population tables.
- carry-forward acceptance: PASS. The real v0.27 → v0.28 comparison measured
  **14 → 15**, zero dropped, and one added subject:
  “Release-classification criteria with no executed control.” This corrects the
  draft's transition wording. The two named drops, “First live SEC RSS harvest”
  and “Observation-byte manifest coverage,” occurred in v0.26 → v0.27, whose
  populations measured **14 → 14** with two additions. A fixture using those
  exact subject names proves both are expressible through dated completions
  without changing historical files.
- planted-control acceptance: PASS by execution. R12 control 18 disables the
  carry-forward rejection; the registered self-test then reports
  `silently-dropped-trigger-subject` at the real control site.
- lifecycle/invariant acceptance: PASS. Focused lifecycle tests passed
  **50/50**; real `cycle-check` passed with both current tables and the actual
  v0.27 predecessor; `invariant-scan` derived **12/12 rules / 49 controls**,
  including R12 **21/21**.
- golden-E2E delta: **0**. The permission-complete `./run golden` execution
  passed **11/11** byte-identically.
- publisher/ref/protected acceptance: PASS. No publisher request, scheduler,
  model-server session, closed runbook, production runtime source, dependency,
  schema, protected artifact, golden input, public route, serialized value
  domain, tag, or branch ref changed.

### 2026-07-30 · DOC-SLIM — review corpus halved without coverage loss

- owner: Codex
- commit: 66a38731bed044cd48a09ec07c0583070c2be2bd
- result: PASS. Repomix scope excludes the pinned SEC RSS body,
  `docs/state-archive/**`, and cycle documents older than the v0.26–v0.28
  retention set. Every observation Markdown file remains. Live State retains
  v0.22-forward and reference §1–§7; the new through-v0.21 archive preserves
  the removed history, prior archive, and reference §8/§9.
- checklist acceptance: PASS. Before and after the archival itself,
  `checklist-audit` remained **219 checked / 3 retracted / 219 matched / 0
  exemptions**. No validated content fell. The mandatory Step 4 runbook and
  this progress record then raise the ordinary workflow total to 220; no
  historical cycle file was edited, moved, or deleted.
- byte-identity acceptance: PASS by hash and whole-output comparison. The
  **185,680-byte** historical slice matched its archived destination at
  `c2535b16bdec70a4fc3551a3ebfc3bfbc3f02ef337a33aaa47f1942cacad6d6c`;
  the embedded **297,739-byte** prior archive matched at
  `3233af5b4c148f7a7f4700edba3238dc67245f28d83dc07cc53c26ebdca6a414`;
  and the **66,557-byte** reference slice matched at
  `beca80003f472db3c22aca1fb54d2eb5777a13b66568ab8c3f996d47a3538c98`.
  Reconstructed State and archive comparisons both returned exact true. The
  immediate split changed State **462,196 → 209,959 bytes**; mandatory current
  records leave final live State at **212,857 bytes** and the archive at
  **549,976 bytes**.
- lifecycle/artifact acceptance: PASS. `cycle-check`, `progress-check`,
  manifest validation, `verify-artifacts` over all **301** pins and both
  protected databases, and `invariant-scan` **12/12 rules / 49 controls**
  passed after archival.
- publication-record acceptance: PASS by the actual entry point. The newest
  closed release resolved to v0.17.0; `POST_PUSH_RECORD_RE` found exactly
  **one** complete record for that tag, and `check_publication_status` returned
  zero errors.
- export acceptance: PASS. The exact project-root command passed **99 derived
  sources / 7 required / 152 exported**. The final implementation-tree export
  is **2,469,697 bytes**, **49.39%** of decimal 5 MB. Raw composition is cycle
  docs **6 / 343,965 bytes**, observations **12 / 56,703**, root **12 /
  472,800**, state archive **0 / 0**, and other reviewed paths **122 /
  1,582,306**. The cycle files are exactly TASKS/PROGRESS for v0.26, v0.27,
  and v0.28; all eight observation Markdown files remain; the RSS body and
  both State archives are absent.
- golden-E2E delta: **0**. The permission-complete `./run golden` execution
  passed **11/11** byte-identically.
- publisher/ref/protected acceptance: PASS. No publisher request, scheduler,
  model-server session, historical cycle edit, production runtime source,
  dependency, schema, protected artifact, golden input, public route,
  serialized value domain, tag, or branch ref changed.

### 2026-07-30 · EXPORT-BOUND — review corpus ceiling and retention enforced

- owner: Codex
- commit: 1a949e691b388487302b75ea89939eba23d8896c
- result: PASS. `export_check` now measures output bytes, enforces the declared
  **3,000,000-byte** ceiling, derives the exact retained cycle-document set from
  `cycle_identity` plus the one depth constant, and rejects both excluded byte
  classes. Forbidden `run` was not edited.
- ceiling acceptance: PASS. `ARCHITECTURE.md` carries the trigger-bearing v0.28
  disposition and reason for the round bound. The fixed-point final
  implementation-tree export passed at **2,485,846 bytes / 152 files**, leaving
  **514,154 bytes / 20.68%** headroom beneath the ceiling.
- retention acceptance: PASS. Depth **3** resolves the active execution cycle
  plus its two immediate predecessors and each matching progress record. The
  real export contained exactly those six derived paths; neither a missing
  retained document nor an older cycle document was accepted. The implementation
  contains no written expected file list, and the fixture population is derived
  from the same depth constant rather than an expected count.
- absence acceptance: PASS. The checker discovers the repository's unique
  pinned SEC RSS capture and rejects its exact exported path; it separately
  rejects any `docs/state-archive/**` path. The real export contained neither
  excluded byte class.
- prior-coverage acceptance: PASS. Existing coverage remained **99**
  Git-derived source paths and **7** required paths, all present in the real
  export.
- planted-control acceptance: PASS by execution. Before the valid construction
  passed, five independent fixtures exercised and detected: over ceiling,
  retained document missing, older document present, pinned capture present,
  and State archive present. The focused suite passed **8/8**.
- shell/lifecycle/invariant acceptance: PASS. The permission-complete shell
  population collected and passed **303/303**, failed zero, and skipped zero.
  An earlier sandbox-denied loopback/process-table attempt was recorded as a
  non-result. `cycle-check` passed with the new third governed architecture
  row. Registered `invariant-scan` passed **12/12 rules / 49 controls**; its
  only registry edit preserves R12's shifted runbook source locator.
- checklist acceptance: PASS. Before the mandatory Step 5 completion box,
  `checklist-audit` remained **220 checked / 3 retracted / 220 matched / 220
  commits resolved / 0 exemptions**. The active task box and this progress
  record are the ordinary workflow increment; no historical cycle document
  changed.
- golden-E2E delta: **0**. The permission-complete `./run golden` execution
  passed **11/11** byte-identically.
- publisher/ref/protected acceptance: PASS. No publisher request, scheduler,
  model-server session, historical cycle edit, production runtime source,
  dependency, schema, protected artifact, golden input, public route,
  serialized value domain, tag, or branch ref changed.

### 2026-07-30 · COVERAGE-ORDER — incoming boundary order enforced

- owner: Codex
- commit: e6b3c1ea6571088e57689045218c809509282ee4
- result: PASS. The store now derives the incoming oldest raw boundary with the
  same known-day, day, raw-byte, and id ordering used by the archive instead of
  using the incoming slice's last position.
- decision-gate acceptance: PASS. The implementation and test are contained in
  `crates/store/src/sqlite.rs`. Forbidden `apps/cored/src/main.rs` and
  `crates/ingest/src/**` did not change; no handler seam was required.
- ordering-choice acceptance: PASS by enforcement. The archive already owns a
  complete comparator, so applying it to raw-timestamped incoming documents
  removes the precondition rather than documenting a second contract. The
  method comment now states that both boundaries use the same ordering and the
  input need not be newest-first.
- misordered-window acceptance: PASS. A middle/oldest/newest input construction
  produced `incoming_oldest_published_raw=2026-07-05` while its last element
  carried `2026-07-09`. The new assertion does not consult `incoming.last()`;
  the focused test passed **1/1**.
- bounded-effect acceptance: PASS. The value remains an observational
  diagnostic string, detection continues the poll, and no document or identity
  path changed. Pinned SEC replay tests passed with the existing measured
  **200-item / zero ascending timestamp inversion** premise.
- identity acceptance: PASS. The shipped parser-produced identity control
  reported **201 input / 201 kept / zero dropped**: all **200** SEC documents
  plus the separate filings-digest document remained distinct.
- Rust acceptance: PASS. Warning-denied workspace tests passed **146/146**,
  including **29** `cored` tests and **23** store unit tests. Workspace clippy,
  fmt, and warning-denied `cored --features net --all-targets` check passed.
- invariant acceptance: PASS. Registered self-test derived **12/12 rules / 49
  controls**. The R1, R5, and R7 expected line fields and R12 runbook source
  range were re-measured after their source files shifted; every original
  mutation and expected finding then executed successfully.
- export-bound acceptance: PASS. The exact project-root entry point passed **99
  derived / 7 required / 152 exported** at **2,494,839 bytes**, below the
  3,000,000-byte ceiling with the exact three-cycle set and both excluded byte
  classes absent.
- response-contract acceptance: PASS. The internal `/ingest` route, response
  type, field names, field types, shape, and serialization are unchanged. Only
  the value of `incoming_oldest_published_raw` is corrected for a misordered
  edge case; no `/v1/*` response shape or serialized value domain moved.
- golden-E2E delta: **0**. The permission-complete `./run golden` execution
  passed **11/11** byte-identically.
- publisher/ref/protected acceptance: PASS. No publisher request, scheduler,
  model-server session, historical cycle edit, dependency, schema, protected
  artifact, golden input, public route, `/v1/*` serialized value domain, tag,
  or branch ref changed.
