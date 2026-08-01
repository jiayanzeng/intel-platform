# TASKS-v0.31-EXECUTION.md — name the commit, or the rule is not a rule

## Runbook amendments

Step 1 — G1–G6 measured, entering state rebuilt, and completion checked — 2026-07-31
Step 2 — operator selected patch release v0.17.1 to ship the boundary correction and executable bindings; all five authorities remain 0.17.0 — 2026-07-31
Step 3 — checked-tree export binding, written ceiling, and distinct cycle-ending audit path implemented and completion checked — 2026-07-31
Step 4 — tracked Rust-floor file partition and historical-exclusion reader implemented and completion checked — 2026-08-01
Step 5 — Git-tracked retained-set authority bound to the configured pattern without a glob matcher and completion checked — 2026-08-01

**Three reviewer errors, all mine, recorded before anything else.**

1. **v0.30 Step 4's acceptance criteria specified an equality without naming the
   commit at which it is evaluated, and the resulting rule has no satisfying
   assignment across the closing commit pair.** I wrote "the live row's value
   must equal the last export figure that record contains" and separately
   discussed the audit-append delta, but never asked whether the *closing
   implementation commit* — which is already in closed state — can satisfy that
   equality. Measurement below indicates it cannot. This is the fifth
   author-side rule with no satisfying assignment on this project's record and
   the second one I have written. **G1 settles it by execution; Step 3 owns the
   correction.**
2. **v0.30 Step 3's acceptance criteria accepted a named exclusion list as a
   discharge, and the list that shipped is read by nothing.**
   `OFFLINE_MSRV_HISTORICAL_EXCLUSIONS` is declared at
   `tools/version_check.py:270` and no module, test, or scanner imports it. My
   criterion said "record the list as a named permanent obligation"; a tuple of
   prose strings sitting in a module satisfies that sentence and satisfies
   nothing else. **A declaration with no reader is rule zero's exact
   prohibition, and I put it in the cycle whose subject was rule zero.**
   G2 settles the reader question; Step 4 owns it.
3. **v0.29 and v0.30 both placed the release/no-release decision after
   RE-MEASURE, which made `release` structurally unavailable while presenting it
   as a live operator option.** Publication requires hosted evidence at the
   release commit; the release commit does not exist until the version
   authorities move; the version authorities were never scheduled before
   RE-MEASURE. Both closing records then correctly refused publication on
   exactly that ground. **The distance the v0.30 trigger now governs was
   produced in part by my own step ordering.** This file moves the disposition
   decision to Step 2, before any implementation, and declares
   `disposition_intent` as `release` so the scope gate keeps the option open.

---

**The named root cause for this cycle.** v0.30 built four real bindings and
every one of them binds two facts that must agree. **Two of them never state
*where* the agreement is evaluated, and one of them ships a component that
nothing reads.**

| v0.30 binding | what it binds | what is missing | consequence |
|---|---|---|---|
| latest-at-close | governed row ↔ last progress field | **the commit at which the comparison happens** | the closing implementation commit and its audit child cannot both satisfy it |
| offline MSRV floor | restatements ↔ executable pins | **a reader for the exclusion list** | a new current restatement outside the registry is invisible |
| retention pattern | glob ↔ active cycle + depth | **the real runbook set** | arithmetic and the retained-set authority diverge on a skipped cycle number |
| forward-boundary family | derived names ↔ semantic registry | nothing — this one is complete | — |

**A binding evaluated inside a multi-commit protocol is not specified until it
names its evaluation point, and a list nobody imports is prose that happens to
be indented.** The objective of v0.31 is that every rule this project executes
states the tree it is executed against, and every declared membership is either
consumed by code or lives outside code.

---

## Declared scope

| Scope class | Path or value |
|---|---|
| `scope_version` | `1` |
| `disposition_intent` | `release` |
| `allow` | `tools/cycle_check.py` |
| `allow` | `tools/export_check.py` |
| `allow` | `tools/version_check.py` |
| `allow` | `tools/invariant_scan.py` |
| `allow` | `config/invariant-rules.json` |
| `allow` | `shell/tests/**` |
| `allow` | `repomix.config.json` |
| `allow` | `AGENTS.md` |
| `allow` | `ARCHITECTURE.md` |
| `release_authority` | `Cargo.toml` |
| `release_authority` | `Cargo.lock` |
| `release_authority` | `crates/*/Cargo.toml` |
| `release_authority` | `apps/*/Cargo.toml` |
| `release_authority` | `shell/intel_shell/__init__.py` |
| `release_authority` | `shell/intel_shell/app.py` |
| `release_authority` | `CHANGELOG.md` |
| `release_authority` | `README.md` |
| `forbid` | `run` |
| `forbid` | `.github/workflows/**` |
| `forbid` | `tools/model_profiles.py` |
| `forbid` | `tools/evidence_artifacts.py` |
| `forbid` | `apps/**/src/**` |
| `forbid` | `crates/**/src/**` |
| `forbid` | `crates/**/examples/**` |
| `forbid` | `crates/**/tests/**` |
| `forbid` | `shell/intel_shell/**` |
| `forbid` | `config/core.json` |
| `forbid` | `config/schedule.json` |
| `forbid` | `config/entities.json` |
| `forbid` | `config/subscriptions*.json` |
| `forbid` | `config/protected-artifacts.json` |
| `forbid` | `observations/**` |
| `forbid` | `docs/state-archive/**` |
| `forbid` | `fixtures/**` |
| `forbid` | `docs/cycles/**` |

**`disposition_intent` is `release`, and that is the deliberate correction of my
third reviewer error.** Declaring `release` makes the scope gate additionally
require that every derived release authority is covered by a declared
`release_authority` pattern — the same set v0.30 declared and whose coverage its
parse confirmed. It does **not** authorize a release, does not oblige one, and a
`no-release` close remains a valid disposition under this declaration. What it
removes is the structural situation in which the operator is offered an option
the runbook's own ordering has already foreclosed.

**Every production source path is forbidden and no step needs one.** v0.30's
`crates/store/src/sqlite.rs` allowance is gone because ORDER-CONST closed. If a
step believes it needs a production source path, that belief is the finding:
record it and stop.

**`run` and `.github/workflows/**` remain forbidden.** `run` is an
`authorization` pin, read as the MSRV authority and never written; the workflow
is read as the hosted MSRV authority and never written. **No new lane job can
ship**, so every check built this cycle must live inside `./run version-check`
or `./run cycle-check`, which are the only two lifecycle entry points present in
both the local matrix and the hosted `shell` job.

**`config/protected-artifacts.json` is forbidden and this cycle declares no
manifest change.** A version bump under Step 6 touches version authorities, not
the manifest.

**`docs/cycles/**` stays forbidden wholesale.** v0.30 proved the standing
precedence keeps the active pair editable while every closed document is
protected by the diff gate.

---

## Entering state (asserted, not yet verified)

**Every line here is a hypothesis for E0. Byte figures marked *export-derived*
were computed from the delivered Repomix export with the measured
one-byte-per-file correction applied; the export file's own size is exact. Where
E0 disagrees, E0 is right.**

- v0.30 closed `no-release` on 2026-07-31 with closing implementation commit
  `00ad3fe1390bac5d6b848581550c88d12dd2ea8e` and separate audit commit
  `5af3209bbab4116f15bfdef10c1e17befbf27e63`. **v0.17.0 remains published** at
  closing commit `4af2841816dd3e43fb8423153b91aa22ccb87537` with annotated tag
  object `df4fc3b044ca12335e773dcc0b9bdd4e0db90afd`. Neutral ref
  `refs/heads/codex/v0.30-evidence-2528498` holds candidate
  `2528498ba7bdce3f280fa1a9c4d6fe266cac05ab`.
- Worktree clean; `ci-local` **20/20**; golden **11/11**; `invariant-scan`
  **12 rules / 55 controls**; `checklist-audit` **239 checked / 3 retracted /
  239 matched / 239 commits resolved**; Rust **146** workspace and **62** net
  (**32 ingest + 30 cored**); shell **317** collected / **317** passed / **0**
  skipped on both constrained lanes.
- Manifest: **331** pins, **191,395** bytes *(export-derived)*, **2** artifacts,
  schema 2; two verifications at **0.12 s / 0.09 s**.
- **The delivered review export is 2,583,624 bytes across 153 files** — exact,
  because it is the export file's own size. That is **86.12%** of the
  3,000,000-byte ceiling and **416,376** bytes of headroom.
- The governed export row records **2,576,273** against the closing
  implementation tree. The delivered export exceeds it by **7,351** bytes,
  which is exactly the R-CLOSE progress append: `PROGRESS-v0.30.md` moved
  **28,276 → 35,627** repository bytes and the whole R-CLOSE entry measures
  **7,349** export bytes plus its separator. **Because the total export
  difference between the two closing commits equals the progress-only
  difference, every other file — including `ARCHITECTURE.md` — is byte-identical
  across that pair.** G1 owns what that implies.
- `STATE.md` **289,117** bytes *(export-derived)*; the recorded next-archival
  boundary is **453,741**, leaving **164,624** bytes. Two measured State
  observations exist: **+33,393** across v0.29 and **+31,695** across v0.30.
- Delivered-export sequence: v0.28 **2,530,129**, v0.29 **2,521,787**
  (**−8,342**), v0.30 **2,583,624** (**+61,837**). **Three points, two
  delivered-to-delivered observations, opposite signs.** G6 owns stating what
  that does and does not support.
- The v0.28 pair measures **65,441** plus **31,453** = **96,894** repository
  bytes *(export-derived)* and leaves the export at v0.31 activation.
- Governed rows: `ARCHITECTURE.md` **13** data rows of which **4** are
  trigger-bearing, all four carrying v0.30-identified close-time values; the
  v0.30 deferred table **21** rows.
- Retention glob is `2[0-7]`, correct for v0.30 and **wrong for v0.31**;
  `cycle-check` rejects it automatically in both lanes. The derivation is
  `last_excluded = 31 − 3 = 28`, so the expected pattern is
  `docs/cycles/{TASKS,PROGRESS}-v0.{[0-9],1[0-9],2[0-8]}{.md,.*.md,-*.md}`.
- `tools/cycle_check.py` declares **five** module-global forward boundaries.
  The fifth, `GOVERNED_EXPORT_FORWARD_BOUNDARY` at `(0, 30)`, is registered with
  `TRIGGER_IDENTITY_FORWARD_BOUNDARY` as its prerequisite. The derived
  completeness check covers it automatically.
- `tools/version_check.py` declares **2** offline MSRV authorities and **22**
  current restatements; zero extraction from either authority raises, and a
  restatement disagreeing with the derived value raises.
  **`OFFLINE_MSRV_HISTORICAL_EXCLUSIONS` at `:270` has no importer.**
- Within the exported subset, **20** files contain a `1.78` or `1.86` literal
  across **183** occurrences. Two of them — `shell/tests/test_version_check.py`
  and `tools/invariant_scan.py` — belong to none of the three declared classes,
  because both construct MSRV mutations. **The exported subset is not the
  tracked set**, so this classification is partial by construction and G2 owns
  the complete one.
- `tools/cycle_check.py` derives the retention glob by arithmetic on the active
  cycle's final version component and never reads the runbook set;
  `tools/export_check.py` sorts the real runbooks and keeps the last three. They
  share only `CYCLE_RETENTION_DEPTH`.
- **55** planted controls: **22** point into `tools/cycle_check.py`, **6** into
  `crates/store/src/sqlite.rs`, **2** into `tools/version_check.py`, and the
  remainder elsewhere. R12 carries **27**.
- `run` declares **20** `ci_local_jobs` and none of them is `export-check`;
  `MAX_EXPORT_BYTES` appears only in `tools/export_check.py` and its test.
  **The 3,000,000-byte ceiling is therefore enforced in no automated lane.**
- Rough activation projection: dropping the v0.28 pair removes **96,894** bytes
  *(export-derived)* and this runbook plus a progress skeleton adds roughly
  70,000. **Arithmetic on a pre-change tree is not a measurement** and is
  labelled the same way it was the last three times.

---

## Drafted gates

| Gate | Where | Hypothesis |
|---|---|---|
| **G1** [P1] | `tools/cycle_check.py:1820-1870`; `docs/cycles/PROGRESS-v0.30.md`; the v0.30 closing commit pair | **The latest-at-close rule cannot be satisfied at the closing implementation commit.** At that commit the runbook carries the closing record and no unchecked box, so the active state is closed and the comparison runs. The only governed progress field visible there is the earlier one naming the activation audit tree, because the R-CLOSE entry containing the later field is appended afterwards. The export arithmetic above indicates `ARCHITECTURE.md` did not move between the two commits, so the row already carried the later figure while the last visible field carried the earlier one. **Settle by execution: run the real `./run cycle-check` at both commits of the v0.30 closing pair in a throwaway clone and record each exit code and each emitted line verbatim.** Then state which of the two branches holds — a closing implementation commit at which the checker errors, or an audit-record commit that moved an invariant document — and say plainly that neither value satisfies both commits. |
| **G2** [P1] | `tools/version_check.py:46-295`; `git ls-files` | **A declared exclusion list with no importer is not an exclusion.** Confirm by exhaustive search that nothing reads `OFFLINE_MSRV_HISTORICAL_EXCLUSIONS`. Then derive, from `git ls-files` rather than from the export, the complete set of tracked files containing a Rust floor literal, and classify each as executable authority, registered current restatement, historical family, or control construction. **State whether a file-level partition of that set is achievable today, name every file that lands in none of the classes and every file that lands in more than one, and rule explicitly on whether within-file current-versus-historical separation is decidable.** If it is not, say so; that residual is the honest one and it is not the same as the file-level gap. |
| **G3** [P2] | `tools/cycle_check.py:1058-1074`; `tools/export_check.py:88-126` | **One retention set, two derivations, and the divergence is reachable inside the v0.x family.** v0.30 settled the version-family boundary and left the arithmetic in place. A single skipped cycle number diverges them without leaving `v0.<n>`: with an active `v0.33` and no `v0.32`, the arithmetic retains two documents while the retained-set authority requires three, and the missing one is excluded by the configured glob. **Settle by execution against a throwaway tree carrying a skipped cycle number** — run the real `cycle-check` and the real `export-check` in it, record what each does, and record which lane, if any, would have caught it. |
| **G4** [P2] | `run`; `.github/workflows/ci.yml`; `tools/export_check.py:37,166` | **A governed trigger is enforced by no automated lane.** The export ceiling is a trigger on a governed row, and the only code that compares real bytes against it runs in an operator-local entry point present in neither the local matrix nor the workflow. **Confirm by exhaustive search.** Then determine whether the *recorded* governed figure can be compared against the single ceiling authority inside an entry point that already runs, and state exactly what such a check would and would not observe — in particular that it constrains a written figure and never measures an export. |
| **G5** [P2] | `AGENTS.md` §5; `ARCHITECTURE.md` §8; the R-CLOSE protocol section | **The closing protocol has two shapes and only one has been exercised under the new content binding.** A `no-release` close is an implementation commit plus an audit child; a `release` close is release commit, closing commit, annotated tag, then a post-push `STATE.md` append — four points at which a governed row may be read. **Enumerate every commit in each shape at which `cycle-check` evaluates the governed export comparison, and state for each whether a satisfying assignment exists.** A correction that fixes the two-commit shape and breaks the four-commit shape is not a correction. |
| **G6** [P3] | v0.28–v0.30 closing records; `STATE.md` | **Two governed byte boundaries move in opposite directions and only one has a reclaiming mechanism.** Derive the activation export for this cycle and state plainly how many delivered-to-delivered observations exist and what their signs are. Then record which of the export ceiling and the `453,741`-byte State boundary is nearer in cycles under explicitly named denominators, and record that retention returns bytes to the export every cycle while nothing returns bytes to `STATE.md`. |

---

## How to run this file

Execute top to bottom, one task and one commit at a time. Follow `AGENTS.md §5`
after **every** task. Implementation and audit-record commits stay separate.

- **🤖 = Codex executes and self-verifies end to end** — no publication, no push
  to `main`, no ref creation or deletion **in the working repository**, except
  where Step 8 is explicitly authorized.
- **🧑 = exactly one named operator action or decision.**

**Interpretive rules, binding throughout.** An exit code of 0 from a
construction the checker never examined is **not measured**. A measurement that
disagrees with an acceptance criterion is **reported as measured**; the
criterion is what gets corrected. **A rule that does not name the tree it is
evaluated against is unspecified, and a declared membership that nothing imports
is prose.** A rule that cannot fail has not passed: every step here demonstrates
its rejection path against real output before its acceptance path.

**The planted-control line-number hazard, stated in advance.**
`invariant_scan.self_test` compares the emitted finding against
`expected_file:expected_line:` exactly. Twenty-two controls point into
`tools/cycle_check.py` and two into `tools/version_check.py`. **Any insertion
shifts every control site below it.** Re-derive the affected `expected_line`
values from real self-test output after each edit, and **record how many were
re-derived** — that figure is this cycle's evidence for the deferred row that
records the hazard. Do not change the control schema; that remains out of scope.

**Dependency gates.** Step 1 blocks everything. Step 2 is an operator decision
taken immediately after Step 1 and blocks Step 6, Step 7, and Step 8. Steps 3,
4, and 5 are independent of one another, but **Step 3 and Step 5 both edit
`tools/cycle_check.py`**, so whichever runs second re-derives the control line
numbers the first shifted. Step 5 **may be skipped entirely under its own
decision gate.** Step 6 executes only under one Step 2 outcome. Step 7 is
blocked by every preceding implementation step; Step 8 by Step 7.

**No amendment obligation is known in advance.** This cycle declares no evidence
directory that cannot exist yet and no manifest change. If an amendment becomes
necessary it takes the established form: a dated `## Runbook amendments` entry
in the same commit that first needs it. **This is notice of the mechanism, not
permission for a scope change.**

### Cycle activation (before E0)

In a separate preparatory implementation/audit pair: confirm the worktree is
clean and record the measured refs **without asserting a literal `origin/main`
hash in `STATE.md`'s header**. Commit **only** this runbook at
`docs/cycles/TASKS-v0.31-EXECUTION.md` — including its `## Declared scope` table
— the `AGENTS.md` header moving the active declaration from v0.30 to v0.31, a
new `docs/cycles/PROGRESS-v0.31.md`, and the `repomix.config.json` retention
edit.

**This file deliberately contains no reserved cycle-closing heading and no blank
closing template.** v0.28 and v0.29 both failed activation on exactly that, and
both failures were this reviewer's. The closing record is appended when the
cycle closes.

**The retention glob must move from `2[0-7]` to `2[0-8]`. Record the exact
rejection text before making the edit.** The derivation is public and the
expected line is predictable; capturing the real one is the point, and a
difference between the predicted and the emitted text is itself a finding.

**Every governed row below already carries `v0.31` and a date**, so activation is
green under the identity rule. **Those dates are carried-forward hypotheses and
E0 rewrites every one of them with v0.31 measurements.** The four
trigger-bearing rows in `ARCHITECTURE.md` still name v0.30 and **must be
remeasured at activation or the identity gate rejects them.** Note that the
governed export row is one of those four and its content binding is exempt while
the cycle is open with an empty progress record; **record the reported exemption
name rather than assuming which one applies.**

### Global definition of done

Protected hashes exact; all **331** pins match; **golden 11/11 byte-identical**;
`./run version-check` green; zero rustc warnings on offline and net builds; all
Rust tests green; all shell tests green under Python 3.11 **and** 3.12; shell
results recorded as collected / passed / skipped with every skip named and
compared by `tools/test_population.py`, never as a bare `N/N`; clippy, fmt,
ShellCheck, floor byte-compilation, and locked Rust 1.78 green.

**`checklist-audit` and the export ceiling are this cycle's two controls.** The
audit total must not fall. The export must stay under 3,000,000 bytes at every
measured point, and **every export figure recorded must name the tree it was
measured on.**

---

## Deferred means deferred

| Deferred item | Unchanged trigger | Measured observation (cycle-identified) | v0.31 action |
|---|---|---|---|
| T7 robots single-flight | a second concurrent harvester | v0.31 · 2026-07-31 — E0 observed no publisher request, scheduler run, or second concurrent harvester; the trigger did not fire | none |
| NEGATIVE-CACHE Decision B | a live transient robots outage for an admitted publisher while a usable last-known-good policy exists, plus operator authorization | v0.31 · 2026-07-31 — E0 made no publisher request and observed no qualifying outage or authorization; the trigger did not fire | none |
| Conditional GET (`ETag` / `If-Modified-Since`) | an operator-authorized cycle whose scope permits the `net` request path plus a live 304 observation | v0.31 · 2026-07-31 — production net paths are forbidden and E0 made no publisher request or live 304 observation; the trigger did not fire | none — the gap stays recorded |
| `edgar:*` extension field mapping | an operator-authorized cycle permitting `crates/ingest/src/**` for mapping, with a connector review | v0.31 · 2026-07-31 — the production ingest path is forbidden, unchanged, and no connector review occurred; the trigger did not fire | none |
| Live multi-publisher behaviour in one runtime | further origins beyond the two configured, or concurrency | v0.31 · 2026-07-31 — E0 contacted no publisher and observed neither a further origin nor concurrent harvesting; the trigger did not fire | none — complete, do not re-exercise |
| First recurring scheduled SEC run | explicit operator authorization of a bounded scheduled window, separate from any cycle scope | v0.31 · 2026-07-31 — no bounded-window authorization was given and no scheduler ran; the trigger did not fire | none — design complete, execution separately gated |
| Postgres / pgvector / multi-host seam | unchanged | v0.31 · 2026-07-31 — E0 measured no production, deployment, schema, or multi-host change; the seam remains unchanged | none |
| A4 untrusted-shell boundary | a third-party/untrusted shell, or any claim HC1 is invariant under shell replacement | v0.31 · 2026-07-31 — E0 observed no third-party shell and made no replacement-invariance claim; the trigger did not fire | none |
| L2 forced-command wrapper | an operator server session | v0.31 · 2026-07-31 — E0 ran no model-profile command or operator server session; the trigger did not fire | none — remains scheduled |
| R3/R4 open-bottom coverage | a spelling outside registered vocabulary | v0.31 · 2026-07-31 — E0's registered self-test found no observed outside-vocabulary spelling; the open-bottom limitation remains | none |
| `--features net` Rust 1.86 execution | a scoped cycle authorized to change evidence topology and an executable local or hosted lane that actually pins and runs the net path on Rust 1.86 | v0.31 · 2026-07-31 — exhaustive authority search still found no executable 1.86 lane and the cycle forbids evidence-topology changes; the trigger did not fire | none — deferred under the v0.30 operator outcome |
| Third configured publisher | a completed compliance review, then a separate admission decision | v0.31 · 2026-07-31 — configuration is unchanged and E0 performed no review or admission; the trigger did not fire | none |
| `v0.8.0` / `v0.10.2` publication | operator-authorized push of both exact annotated objects | v0.31 · 2026-07-31 — local identities remain present, no publication was authorized, and no historical ref moved; the trigger did not fire | none — no historical ref touched |
| `--skip-local-tag-verification` removal | both historical tags published plus a passing hosted full-history `cycle-check` without the flag | v0.31 · 2026-07-31 — both historical tags remain unpublished and the workflow byte is unchanged; the removal trigger did not fire | none — the flag stays |
| Manifest retention/indexing | 1 MiB manifest, or two consecutive `verify-artifacts` runs ≥1.00 s | v0.31 · 2026-07-31 — E0 measured 331 pins / 191,395 bytes and two complete 0.10 s / 0.10 s verifications; neither trigger fired | Step 1, Step 7, and Step 8 — re-measured only; no registration |
| Version literal in `app.py` | a cycle whose declared scope permits shell source changes | v0.31 · 2026-07-31 — E0 changed no shell source or version literal; the path remains reachable only under the selected Step 6 release shape | Step 6 — reachable only as a release authority under one operator outcome |
| Release-classification criteria with no executed control | an operator decision that prose adjudication is insufficient | v0.31 · 2026-07-31 — no such operator decision occurred; the prose-adjudication limitation remains unchanged | none — recorded, not acted on |
| Second `STATE.md` archival | the export ceiling trigger fires, or `STATE.md` reaches 453,741 bytes | v0.31 · 2026-07-31 — E0 measured the activation export at 2,544,715 bytes and State at 289,117 bytes, leaving 455,285 and 164,624 bytes respectively; neither trigger fired | Step 1 and Step 8 — boundary re-derived; no archive |
| Planted-control line numbers re-derived by hand | a control-schema change, or a cycle in which the re-derived count exceeds the controls it protects | v0.31 · 2026-07-31 — Step 3 re-derived 9 expected-line values from emitted fail-before output: 7 shifted existing values plus 2 new registered controls; 9 remains below the 57 controls protected | Step 3, Step 4, and Step 5 — shifted values re-derived and counted |
| Retention derivation across a version-family boundary | an active cycle whose name is not of the form `v0.<n>` — raising at `v1.0`–`v1.2`, silently under-excluding from `v1.3` onward | v0.31 · 2026-07-31 — active v0.31 remains inside the supported family; E0 separately executed a skipped-v0.x construction that exposed a distinct set/arithmetic divergence for Step 5 | Step 5 — settled under its own decision gate |
| Published-release divergence | the unpublished distance contains a measured runtime behaviour difference persisting across three consecutive closed cycles, or acquires any public-surface change | v0.31 · 2026-07-31 — v0.31 is open, so only v0.29 and v0.30 are post-correction closed-cycle persistence observations; no public-surface change exists and the trigger has not fired | Step 2 and Step 8 — disposition selected before implementation |
| MSRV current-restatement membership | a current restatement of either Rust floor lands outside the registry without failing a check | v0.31 · 2026-07-31 — E0 derived 75 tracked literal-bearing files / 683 occurrences: file-level precedence classified all files, with 0 unclassified and 6 multi-class; the historical tuple has no reader and within-file present-versus-history separation is not text-decidable | Step 4 — file-level partition bound; within-file residual named |

---

## Step 1 · E0 — Rebuild the entering state and settle six gates 🤖

**Objective.** Confirm HEAD is green and settle G1–G6. **Every assertion in
`## Entering state` is a hypothesis.** Report the measured value, especially
where it differs.

**Decision gate.** If the worktree is dirty, if v0.30's closing and audit commits
are not where the entering state places them, or if any local gate fails at
entry, **record and stop.**

**Acceptance criteria.**

- All 20 `ci-local` jobs pass; `invariant-scan` passes its registered self-test;
  golden **11/11**; all pins verified twice with both real times recorded; both
  Python lanes reported as collected/passed/skipped via
  `tools/test_population.py`.
- G1 settled **by execution against the real v0.30 closing pair**, with each
  emitted line recorded verbatim and the two-branch conclusion stated plainly.
- G2 settled **by exhaustive search over `git ls-files`**, with the complete
  classification produced and every unclassified and multiply-classified file
  named.
- G3 settled **by execution** against a throwaway tree carrying a skipped cycle
  number, recording both entry points' behaviour and which lane would catch it.
- G4 settled **by exhaustive search**, with an explicit ruling on what a
  figure-level ceiling comparison would and would not observe.
- G5 settled with every commit in both closing shapes enumerated and each one
  ruled satisfiable or not.
- G6 settled with the activation export derived and the available observations
  stated with their signs.
- The activation rejection text produced by the stale retention glob is recorded
  verbatim, and any difference from the predicted text is reported as a finding.
- The deferred table's rows are rewritten with **v0.31** measured observations,
  and the four trigger-bearing `ARCHITECTURE.md` rows carry v0.31
  close-adjacent measurements.
- **The governed-export exemption reported by the real entry point at
  activation is recorded by name**, and the reported name is compared against
  what the open-cycle rule says should apply.

**Done when** every gate carries a measured answer and the entering state is
either confirmed or corrected in `STATE.md`.

- [x] **E0**

---

## Step 2 · DISPOSITION-FIRST — The release decision, taken before the work 🧑

**Objective.** Put the release disposition in front of the operator **now**,
while every option is still structurally available, and record the selection
with its date and reason.

**Decision gate.** Blocked by Step 1 only. **If E0 measures that the divergence
trigger has not in fact reached its third consecutive closed cycle, record that
correction and present the decision anyway** — the trigger's arithmetic is E0's
to verify, and the decision does not depend on it.

**Why this step exists and why it is second.** Publication requires hosted
evidence measured at the release commit. The release commit does not exist until
the version authorities move. In v0.29 and v0.30 the version authorities were
never scheduled before hosted verification, so both closing records refused
publication on precisely that ground while the closing step presented
publication as an option. **That was my error twice, and moving this decision
ahead of the implementation is the correction.** Selecting `no-release` here
costs nothing; selecting `release` here is the only ordering under which
`release` is real.

**🧑 The operator's decision, and only the operator's.** Publication
authorization is a separate explicit act and is **not** implied by this runbook,
by green gates, or by hosted evidence. Three outcomes, none defaulted:

- **`no-release`, with the fired trigger explicitly disposed.** Close v0.31 on
  its own record and state the reason the distance remains acceptable now that
  the governed condition has been reached. **A fired trigger is not an
  obligation to publish, but it is an obligation to decide rather than inherit.**
  Steps 6 through 8 run in their no-release shape.
- **`release` at patch.** Ship the order-independent boundary derivation and
  three cycles of bindings. No route, response shape, `/v1/*` value domain,
  dependency, or schema has moved across the unpublished distance, so the
  named-surface rule and the public value-domain criterion both stay unfired and
  patch is the classification. This requires a stated reason of its own and may
  not be inherited from "the gates are green." Step 6 executes, Step 7 measures
  the release commit, and Step 8 runs the four-commit tagged-closing protocol.
- **`release` at minor.** Only if E0 or a later step measures a surface movement
  the prior three closing records missed. **This outcome must be supported by a
  measurement, not by caution**; selecting it without one would inflate a
  classification the same way the prior records were careful not to deflate it.

**Acceptance criteria.**

- The selection, its date, and its reason are recorded in `STATE.md` and in a
  dated `## Runbook amendments` entry.
- The classification argument is restated from measurement rather than inherited:
  whichever outcome is selected, the record names what was compared and what was
  found unchanged.
- **If `release` is selected**, the record names the exact version and states
  that the five version authorities have not yet moved at this point.
- **If `no-release` is selected**, the record states the disposition of the
  governed divergence trigger explicitly, including whether it has fired and
  what the next observation will be.
- No version authority, tag, `main`, release ref, or publication ref moves in
  this step. **This step records a decision and changes no artifact besides the
  two lifecycle records.**

**Done when** the disposition is selected, dated, reasoned, and recorded, and
every later step knows which shape it runs in.

- [x] **DISPOSITION-FIRST**

---

## Step 3 · CLOSE-POINT — Name the commit the rule is evaluated at 🤖

**Objective.** Make the latest-at-close binding satisfiable at every commit of
whichever closing shape Step 2 selected, and correct the contract to say where
the comparison happens.

**Decision gate.** Blocked by Step 1. If G1 measured that the closing
implementation commit **does** satisfy the rule today — that is, if
`ARCHITECTURE.md` moved between the v0.30 pair after all — then the finding is an
audit-record commit carrying a non-record change, and the correction is a
contract clarification rather than a checker change. **Record the
reclassification and treat it at that reduced scope.**

**The fixed point, stated so the acceptance criteria are satisfiable.** No
record inside a tree can carry a measurement of a tree containing that record.
v0.30's rule tried to escape that by writing the closing tree's own figure into
the closing tree and supplying the matching progress field afterwards, which
leaves the closing commit itself unable to pass. **Two shapes are available and
either satisfies this step.** The governed row may record the last tree the
closing commit can already see, in which case the closing audit's own
measurement must be written under a distinct field name so it does not become a
"later" governed field. Or the closing implementation commit may be exempted by
a named, reported path in the same family as the two open-cycle exemptions, in
which case the exemption must expire at the audit child and must be demonstrated
expiring. **A third shape that satisfies the property is equally acceptable; the
property, not the mechanism, is what this step owes.**

**Acceptance criteria.**

- **`cycle-check` passes at a constructed closing implementation tree and at its
  audit child**, both demonstrated by execution against real fixtures, under
  whichever closing shape Step 2 selected.
- **If `release` was selected, the four-commit shape is covered too**: the
  release commit, the closing commit, the tagged checkout, and the post-push
  descendant each either satisfy the comparison or take a named reported path,
  and each is demonstrated.
- The contract text states **which commit the comparison is evaluated at**, in
  the same symmetric form the existing rule uses, so a later cycle cannot select
  an evaluation point opportunistically.
- **A vacuous pass is not available at any of those commits.** A construction
  that would let a closed cycle carry a figure nothing compares must be
  demonstrated failing.
- A registered `R12` control proves the newly named path is exercised.
  **Demonstrate the rejection before the acceptance.**
- The existing open-cycle exemptions and the superseded-figure rejection are
  unchanged, confirmed by test.
- The recorded governed figure is additionally compared against the single
  ceiling authority, and **the check's own text states that it constrains a
  written figure and does not measure an export.** If G4 ruled that comparison
  unachievable inside an entry point that already runs, record the ruling and
  omit it.
- Every `expected_line` shifted by this edit is re-derived from real self-test
  output and the count is recorded.

**Done when** the closing sequence has no commit at which the rule has no
satisfying assignment, demonstrated by execution rather than by argument.

- [x] **CLOSE-POINT**

---

## Step 4 · EXCLUSION-READ — A list nothing imports is not a list 🤖

**Objective.** Either give the historical-exclusion declaration a reader that
makes it load-bearing, or move it out of code so it stops looking like a
control.

**Decision gate.** `run` and `.github/workflows/**` are **forbidden.** The
offline pins are read, never written. **If any part of this step would add a
hosted job, change a toolchain pin, or alter the evidence topology, stop and
record it.**

**Why this is not tidying.** The exclusion tuple was accepted last cycle as the
honest discharge of a membership that cannot be derived. It is honest prose and
it is also unreachable code, and this project's first rule says a claimed
property nothing executes is not a property. The registry beside it *is* read,
so the module currently contains one binding and one decoration that look
identical to a reader.

**The bound, stated so the criteria are satisfiable.** Within-file separation of
a current restatement from a dated quotation is not decidable by text: identical
literals appear in both, and single lines intentionally carry a refuted figure
beside the current one. **File-level partition is decidable and is what this
step builds.** A file that begins stating a floor and belongs to no declared
class must fail; a line inside an already-classified file remains outside the
binding and that residual is named, not papered over.

**Acceptance criteria.**

- Either `OFFLINE_MSRV_HISTORICAL_EXCLUSIONS` acquires a real reader, or it
  leaves `tools/version_check.py` for a document. **Both outcomes are
  acceptable; leaving an unread tuple in the module is not.**
- If it acquires a reader: the tracked file set is derived from `git ls-files`,
  never enumerated by hand, and every tracked file containing a Rust floor
  literal is partitioned into executable authority, registered current
  restatement, historical family, or control construction. **Class precedence is
  declared explicitly** because at least two files legitimately belong to two
  classes, and a file matching none is an error.
- **A file yielding zero classifications must fail loudly**, demonstrated by a
  planted control, or the partition passes vacuously — the silent no-op family
  this project has now caught five times.
- The within-file residual is stated in the check's own text, not only in a
  cycle document. **A bounded derivation that does not name its bound is the
  finding, not a detail.**
- The binding lives in an entry point that already runs in both lanes.
- A registered `R12` control proves an unclassified file is rejected.
  **Demonstrate the rejection before the acceptance.**
- Dated historical records that quote the refuted figure **must keep quoting it
  and must not be rewritten.**
- Every `expected_line` shifted by this edit is re-derived from real self-test
  output and the count is recorded.

**Done when** a new file stating a Rust floor outside every declared class fails
automatically, or the declaration no longer lives in code.

- [x] **EXCLUSION-READ**

---

## Step 5 · RETENTION-ONE — One retained set, one authority 🤖

**Objective.** Bind the configured retention pattern to the single retained-set
authority so the arithmetic derivation cannot disagree with the set the export
actually keeps.

**Decision gate.** Blocked by nothing and **skippable in full.** If G3 concluded
that binding the two derivations requires reimplementing a brace-glob matcher —
which would be a second declaration of the export tool's own matching semantics
and therefore this cycle's root cause in a new place — **record that and stop.**
The arithmetic derivation stays, the skipped-cycle divergence gets a trigger,
and nothing is built. **A worse implementation bought for symmetry is not an
improvement.**

**The cheap shape, offered so the gate is a real choice.** The configured
pattern implies a retained set under the same arithmetic that produced it. That
implied set can be compared against the retained-set authority over the real
tracked runbook collection without matching a single glob, because both sides
reduce to a set of cycle versions. **If that comparison is achievable, it binds
the two derivations at file granularity in both lanes and needs no matcher.**

**Acceptance criteria.**

- The retained cycle set is derived **once**, from the real tracked runbook
  collection, and the configured pattern is checked against it rather than
  against a string produced by a second derivation.
- **The check runs without an export in existence**, preserving the property the
  prior cycle built deliberately.
- A skipped cycle number is rejected, demonstrated by execution against a
  throwaway tree rather than by argument.
- The existing stale-glob rejection continues to fire at the active cycle,
  confirmed by test, and its emitted text remains useful to a reader who must
  make the edit.
- A registered `R12` control proves the new disagreement is caught.
  **Demonstrate the rejection before the acceptance.**
- Every `expected_line` shifted by this edit is re-derived and the count
  recorded.

**Done when** the two derivations cannot disagree, or the reason they must
remain separate is recorded and nothing changed.

- [x] **RETENTION-ONE**

---

## Step 6 · VERSION-SET — Move the version authorities, and only those 🤖

**Objective.** Under one Step 2 outcome only, move every version authority to
the selected version so a release commit exists for hosted measurement.

**Decision gate.** **Executes only if Step 2 selected a release outcome. If Step
2 selected `no-release`, record the gate as tripped and skip this step
entirely** — an unexecuted step under a recorded gate is a result, not a gap.
`config/protected-artifacts.json` and every production source path remain
forbidden.

**The blast radius is bounded and every record must say so.** This step changes
declared versions and the changelog. It changes no route, response shape,
`/v1/*` value domain, dependency resolution beyond the workspace's own package
versions, schema, or behaviour. **Do not let a version bump carry anything
else.**

**Acceptance criteria.**

- The Rust package, Python package, public FastAPI literal, `STATE.md` header,
  and newest `CHANGELOG.md` release all state the selected version, and their
  agreement is confirmed by the entry point that already checks it.
- The lockfile is updated by the toolchain, never by hand, and **is not deleted
  to resolve anything.** Locked builds pass.
- Golden stays **11/11 byte-identical** and the SEC identity population is
  unchanged. **If either moves, stop.**
- The `/ingest` response shape and every `/v1/*` value domain are unchanged, and
  both are recorded explicitly for the closing decision.
- No tag is created, no ref moves, and no push occurs. **This step produces a
  commit, not a publication.**
- The complete local matrix and both Python lanes pass at the release commit.

**Done when** a release commit exists whose version authorities agree, or the
gate is recorded as tripped and nothing changed.

- [ ] **VERSION-SET**

---

## Step 7 · RE-MEASURE — Hosted verification at the exact candidate 🤖

**Objective.** Produce authenticated hosted evidence at an exact candidate,
targeting whichever commit Step 2's outcome makes correct.

**Decision gate.** Blocked by Steps 3 through 6. **The workflow is forbidden**,
so the job matrix, the receipt population, and the signed identity count must be
identical to the prior cycle's; **if any of them moves, that is a finding and not
a result.** Under a release outcome the candidate **is** the release commit and
the measurement must be of that commit, not of a neutral copy of its tree; under
`no-release` the candidate goes to a neutral ref only.

**Acceptance criteria.**

- All seven executable hosted jobs pass at the exact candidate; the
  dependency-drift job skips under its declared report-only condition.
- Attestations required; every signed identity accepted, zero rejected; the
  complete runner matrix found.
- Both shell lanes compared by `tools/test_population.py` with
  comparator-derived `collected`, `equivalent`, and `equivalent_passed`. **Every
  figure written is the comparator's output, never transcribed from a log.**
- All pins verified on the candidate, unchanged; golden **11/11**.
- **No manifest registration occurs.** This cycle declares none and expects none.
- **Under a release outcome, the record states that the measured candidate is
  the release commit itself** and names it, because the closing record will cite
  this evidence and evidence from publishing cannot exist in the published tree.
- No push to `main` and no tag in this step.

**Done when** the candidate carries release-grade authenticated evidence at the
commit the selected disposition requires.

- [ ] **RE-MEASURE**

---

## Step 8 · R-CLOSE 🧑🤖

**Objective.** Close v0.31 in the shape Step 2 selected, and execute the
publication if and only if it was separately authorized.

**🧑 The operator's authorization.** Step 2 selected a disposition; **this step
requires the operator's explicit authorization to act on it.** A selection is
not a push. If the selection was a release outcome, the operator authorizes the
atomic push of the closing commit and its annotated tag here, or withholds it and
the cycle closes `no-release` with that change of mind recorded and reasoned.

**Acceptance criteria.**

- The closing record names the closing date and the dated release disposition,
  and — under a release outcome — the release name and release commit under the
  two-commit tagged closing protocol, with no tag-object field in the closing
  tree.
- **Under a release outcome**, the release commit is the closing commit's
  immediate parent, the annotated tag targets the closing commit, the push is
  atomic, and the first commit after it carries the complete post-push record.
- **Under `no-release`**, the intentionally unreleased commits are named and
  every version source and tag is left unchanged.
- Every declared permission is reconciled as used or unused, by path. **The
  release-authority set is reconciled explicitly** whichever outcome ran,
  because declaring `release` intent and then not using those paths is a fact
  the record owes a reader.
- Every gate G1–G6 has a recorded measured answer, including Step 5's
  skip-or-implement ruling and Step 6's gate disposition.
- **The three reviewer errors in this file's header are preserved in the cycle
  record as reviewer errors**, not restated as findings and not quietly dropped.
- The total of `expected_line` values re-derived across the cycle is recorded,
  as evidence for the deferred row that names the hazard.
- The governed divergence trigger carries a dated observation stating plainly
  whether it fired and how it was disposed.
- `STATE.md` records the final export figure against the ceiling **naming its
  tree**, the `checklist-audit` control, and the derived growth observations with
  their count stated.

**Done when** the disposition is authorized, recorded, and measured.

- [ ] **R-CLOSE**

---

## Cycle checklist

- [ ] Worktree clean at entry; v0.30 closing and audit commits where E0 measures them
- [ ] Stale retention glob rejection recorded verbatim before the activation edit
- [ ] Every entering-state hypothesis measured and confirmed or corrected
- [ ] G1–G6 each carry a measured answer; G1, G2, and G3 answered **by execution**
- [ ] The release disposition selected and reasoned **before** any implementation step
- [ ] Every new binding demonstrated **rejecting** before demonstrated passing
- [ ] Every rule touched this cycle names the tree it is evaluated against
- [ ] No declared membership left in code without a reader
- [ ] No binding implemented as a self-consistency assertion
- [ ] No binding whose membership is written by hand rather than derived
- [ ] No expected value hardcoded in any test added or edited this cycle
- [ ] Re-derived planted-control line numbers counted and recorded at every step
- [ ] No closed cycle document edited, moved, or deleted
- [ ] Workflow file byte-identical across the complete cycle diff
- [ ] Manifest byte-identical across the complete cycle diff
- [ ] `checklist-audit` total does not fall; every figure recorded
- [ ] Export under 3,000,000 bytes at every measured point, each naming its tree
- [ ] Golden **11/11** byte-identical at every step
- [ ] SEC identity population unchanged
- [ ] Both Python lanes reported as collected/passed/skipped, comparator-derived
- [ ] Deferred table rows all carry v0.31-identified observations
- [ ] No publisher request, no scheduler run, no cadence change
- [ ] Three reviewer errors preserved as such in the cycle record

---

## Standing prohibitions

- **No publisher request and no scheduler run.** The bounded window design
  exists and its execution authorization is again withheld from this cycle.
- **No edit to `.github/workflows/**`.** The hosted MSRV job is read as an
  authority and never written; changing the job matrix moves the evidence
  topology and is a scoped redesign for a later cycle.
- **No edit to `run` or `tools/model_profiles.py`** — both are `authorization`
  pins. `run` is read as the MSRV authority and never written.
- **No manifest edit.** This cycle declares none.
- **No production source edit.** Every `crates/**/src/**`, `apps/**/src/**`, and
  `shell/intel_shell/**` path is forbidden; the two shell version files are
  reachable only as release authorities under one operator outcome.
- **No closed cycle document is edited, moved, renamed, or deleted** — executed
  by the wholesale `docs/cycles/**` forbid through the diff gate.
- **No second `STATE.md` archival.** The boundary is re-derived; recording is not
  doing.
- **No push to `main`, no tag, no ref creation or deletion** before the
  authorized closing action in Step 8. **Declaring `release` intent in the scope
  table authorizes nothing.**
- **No hardcoded expected value** in any test written or edited this cycle, and
  **no hand-written membership list** in any binding built this cycle.
- **No binding that a single implementation can satisfy by construction.**
- **No rule ships without a demonstrated failing case, and no rule ships without
  a named evaluation point.**
- **No rewriting of a dated historical record that quotes a refuted figure.**
- **No retraction is proposed** without a twice-verified measured false claim in
  an immutable published record. **The count stands at three.** G1's finding, if
  confirmed, concerns a live checker and a live contract, not an immutable
  published record, and **this reviewer is not proposing a retraction** — a false
  retraction proposal is already on this project's record as a reviewer error.

---

## Provenance of this draft

**Read, not measured:** the Codex v0.30 report; `TASKS-v0.30-EXECUTION.md` in
full including its six amendments and closing record; `PROGRESS-v0.30.md` in
full; `AGENTS.md` §§0 and 5 including the R-CLOSE protocol section;
`ARCHITECTURE.md` §6's dispositions table and §8; `STATE.md` header, the v0.30
and v0.29 sections, and §7.

**Measured against the 2026-07-31 delivered export, by path and line:** export
size **2,583,624** bytes and **153** files, exact; `PROGRESS-v0.30.md` at
**35,626** export bytes with its R-CLOSE entry at **7,349** export bytes, which
reconciles the recorded **28,276 → 35,627** repository movement and the
**7,351**-byte delta to the byte; `STATE.md` at **289,116** export bytes and
`config/protected-artifacts.json` at **191,394**, each one below its recorded
value under the one-byte-per-file rule; the manifest's schema 2, **2** artifacts,
**331** `pinned_files[]`, and the two `authorization` grades on `run` and
`tools/model_profiles.py`; `config/invariant-rules.json` at **12** rules and
**55** `fail_before` controls with R12 at **27**, distributed **22** into
`tools/cycle_check.py`, **6** into `crates/store/src/sqlite.rs`, and **2** into
`tools/version_check.py`; **every one of the 55 `expected_line` values checked
in range, and each of the 30 pointing into those three files verified to land
exactly on its control marker** — including the new margin control at
`cycle_check.py:1863`, the boundary relationship at `:1519`, the three freshness
controls at `:1665`, the carry-forward control at `:2041`, the MSRV binding at
`version_check.py:354`, and the five re-derived store positions;
`cycle_check.py:1458-1485` the five forward boundaries and their relationship
registry; `:1726-1870` the governed-row extraction and the closed-state
comparison; `:1058-1074` and `export_check.py:88-126` the two retention
derivations; `export_check.py:37,166` the sole ceiling authority; `run`'s
**20** `ci_local_jobs` with no `export-check`; `version_check.py:46-295` the
**2** authorities, **22** restatements, zero-extraction raise, and the
exclusion tuple at `:270` with **no importer anywhere in the export**;
`ARCHITECTURE.md`'s dated dispositions table at **13** data rows of which **4**
are trigger-bearing; the v0.30 deferred table at **21** rows; `checklist-audit`
reconciled as v0.29's total plus this cycle's **7** bolded tasks;
`config/checklist-retractions.json` at **3**; `repomix.config.json` retention
glob at `2[0-7]`.

**Derived by reading code, not by executing it:** that the expected v0.31
retention pattern is `2[0-8]`, which follows from the depth authority and the
brace-range helper; that a skipped cycle number diverges the two retention
derivations, which follows from the same helper and the retained-set function;
and — the important one — **that `ARCHITECTURE.md` is byte-identical across the
v0.30 closing pair**, which follows from the two reported export sizes differing
by exactly the measured progress append while the file inventory is unchanged.
**G1's conclusion rests on that derivation and is therefore not evidence until
E0 runs the real checker at both commits.** Stating it as measured would repeat
this project's second-most-recorded reviewer error.

**Asserted and not verified:** every line under `## Entering state`; the
classification of the two unclassified MSRV-literal files, which follows from
reading the registry and is **G2's to settle over the tracked set**; the claim
that the divergence trigger reaches its third consecutive closed cycle here,
which follows from reading two closing records and is **E0's to confirm**.

**Not verifiable by this reviewer at all:** that no historical cycle document was
moved, edited, or deleted. Retention depth 3 exports only v0.28–v0.30, so v0.1
through v0.27 are outside this reviewer's reach and that claim rests on
`checklist-audit` and on Codex's measurement. Also unverifiable here: every
figure Codex reported for the closing implementation tree, since only the audit
child was delivered. **Said plainly rather than left implied.**

**Three reviewer errors are recorded in this file's header** rather than here,
because a provenance note is where a reader looks last and an error is what they
should see first.
