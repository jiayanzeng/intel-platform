# TASKS-v0.29-EXECUTION.md — the pairs the fix created

## Runbook amendments

### 2026-07-31 · RETENTION-BIND measured completion

Step 2 — derived retention binding recorded and completion checked — 2026-07-31

The implementation derives the tracked brace pattern from the active cycle and
the one `CYCLE_RETENTION_DEPTH` authority. It deliberately broadens the
irrelevant lower alternative from `[6-9]` to `[0-9]`: the added v0.0–v0.5 names
do not exist, exported paths stay identical, and no second lower-bound literal
is needed. The real checker rejected the old pattern before the config was
updated. A focused no-export fixture and registered R12 mutation independently
exercise the stale-pattern rejection. No objective, decision gate, acceptance
criterion, scope row, or standing prohibition changes.

### 2026-07-31 · E0 preparatory manifest-byte correction

Step 1 — measured answers recorded and completion checked — 2026-07-31

E0 measured the unchanged `config/protected-artifacts.json` file at **182,774
bytes**, not the **182,780** transcribed in the activation progress record and
activation architecture observation. The manifest's Git blob is byte-identical
across those trees, so this is a record correction rather than a product or
manifest change. E0 forward-corrects the value in `STATE.md`, the live governed
row, this runbook's measured deferred observation, and its append-only progress
entry. The pin population, verification results, and decision gate do not
change.

### 2026-07-31 · Activation retention-edit reconciliation

The activation instructions first say the preparatory commit contains only the
new runbook, the `AGENTS.md` declaration, and the progress skeleton, then
separately require `repomix.config.json` to move from `2[0-5]` to `2[0-6]` “at
activation.” Those instructions cannot both describe the same commit literally.
This amendment follows the explicit retention instruction: the activation
implementation commit contains those three lifecycle files plus only the
already-declared `repomix.config.json` edit. No other scope, objective, gate,
acceptance criterion, or prohibition changes.

Step 8 — reviewer-error preservation count corrected — 2026-07-31

### 2026-07-31 · Activation lifecycle correction

Activation commit `1cf49cf…` exposed two additional reviewer errors. First, the
draft repeated the checker's reserved cycle-closing Markdown token in prose
while all task boxes were unchecked. The real `cycle-check` therefore exited 1
with `declared runbook cannot mix unchecked boxes with` that reserved token,
recreating the first recorded reviewer error despite the draft's claim that the
token was absent. This amendment rephrases both prose occurrences without
adding a closing heading.

Second, the draft updated the 17 deferred observations to v0.29 but overlooked
the three trigger-bearing rows in `ARCHITECTURE.md`, even though the current
checker governs both tables. The same invocation named all three stale rows and
required active-cycle identity. This amendment permits only their v0.29
activation measurements before E0 restarts. The original four reviewer errors
remain intact; these two are errors five and six, and the Step 8 preservation
criterion is corrected accordingly. No objective, decision gate, declared
scope, standing prohibition, or task order changes.

### 2026-07-31 · Activation scope-fixture correction

The first permission-complete E0 `./run ci-local` passed every preceding
lifecycle, invariant, Rust, net, lint, format, and MSRV gate, then measured the
v0.28 exact-current-cycle scope fixture still requiring zero
release-authority/forbid overlaps. The v0.29 table deliberately declares both
Python version files as release authorities while its broad shell-source forbid
also matches them; release-authority precedence is the stated behavior. This is
the exact fixture class the activation instructions assign for correction.
The amendment permits only
`shell/tests/test_cycle_check.py::test_current_scope_has_no_release_forbid_overlap`
to replace its hardcoded empty tuple with a second, independent derivation from
the active table and release-authority paths. It does not change scope semantics,
production code, a task contract field, or any expected value literal. E0
restarts only after this correction and its audit record are committed.

v0.28 closed `no-release` on 2026-07-31 and every substantive claim in the Codex
report was re-derived and held. The export is **2,530,129 bytes** — the byte
count Codex reported, matched exactly on receipt. Invariant totals moved **12
rules / 46 controls → 12 / 49**, and the three added `R12` controls are exactly
the three this reviewer asked for: `header-only-trigger-measurement-date`,
`stale-trigger-cycle-identity`, and `silently-dropped-trigger-subject`. The
header-date fallback is gone — `valid_dates` now reads only `measured`. The
discarded return value is bound at `cycle_check.py:1907` and a zero population in
either governed table is a named error. The hardcoded `(2, 14)` is replaced by a
derivation that counts rows through a **second, independent implementation** and
asserts the two agree — that is the one paired declaration in this cycle that was
done right, and Step 3 and Step 4 below both use it as the template. Carry-forward
rejects a silent drop and accepts a dated completion, and both paths are tested.
`export_check` grew a 3,000,000-byte ceiling, a derived retention set checked in
**both** directions, and two absence assertions, with five new controls. The
archival is proven by three recorded SHA-256 comparisons and
`checklist-audit` held at **219 → 219** across it. The manifest change from 301
to 316 pins went through the sanctioned path: explicit operator authorization on
2026-07-31, a dated amendment, scope narrowed to two evidence paths plus the
manifest, landing in one implementation commit. **The standing prohibition was
respected rather than routed around.**

**Six reviewer errors, all mine, all recorded before anything else.**

1. **The supplied v0.28 draft could not activate.** It carried the reserved
   cycle-closing heading while every task box was unchecked, and
   `cycle_check` rejects exactly that combination. **This reviewer had read that
   code path in the prior review and drafted the template anyway.** It cost an
   activation cycle and amendment 1. **This file contains no closing-record
   heading**; R-CLOSE appends one when the cycle closes.
2. **The drafted entering state asserted 14 governed deferred rows while the
   drafted table contained 15.** A self-inconsistent draft, corrected by
   amendment 2 as `(2, 15)`.
3. **The drafted entering state placed `ddf08d20…` on local `main`, one commit
   ahead of published `main`.** Measured: that commit was on
   `codex/v0.23-action-migration`, and local `main` was **102 commits behind**
   `origin/main`. Labelling it a hypothesis is why E0 caught it; it was still
   wrong.
4. **Every drafted `STATE.md` region size was ~7 bytes low**, because this
   reviewer measures from a Repomix export that strips one trailing newline per
   file — an artifact noted in the *previous* review and then not corrected for.
   **Every byte figure this reviewer derives from an export is a lower bound.**
5. **The supplied v0.29 draft repeated the reserved closing token in prose.**
   The checker treats that exact token as a closing heading even inside the
   sentence claiming the heading is absent, so activation failed in the same
   way error 1 says v0.28 failed.
6. **The supplied v0.29 draft refreshed only one of the two governed tables.**
   Its deferred rows named v0.29, but all three trigger-bearing architecture
   observations still named v0.28, so the active-cycle identity gate rejected
   them at activation.

**The projection was also low.** 2,375,647 drafted against 2,530,129 delivered,
because the retained set was priced without v0.28's own documents. Arithmetic on
a pre-change tree is not a measurement, and the runbook said so; it was still off
by 154,482 bytes.

**The named root cause for this cycle.** v0.28 converted three asserted
properties into executed ones. In doing so it created **four new pairs of
declarations that must agree**, which is this project's *other* named defect
class — the one `R5` exists for. **One of the four is bound. Three are not.**

| pair | binding | consequence if they diverge |
|---|---|---|
| `governed_trigger_subjects` ↔ `check_trigger_table` | **derived test, cross-implementation** | caught |
| `repomix.config.json` retention glob ↔ `CYCLE_RETENTION_DEPTH` + active cycle | **none in either CI lane** | silently over-large export |
| `TRIGGER_FLOOR_FORWARD_BOUNDARY` ↔ `TRIGGER_FRESHNESS_FORWARD_BOUNDARY` | **none** | `UnboundLocalError`, not a defect report |
| `archive_recency_cmp` ↔ the SQL `ORDER BY` beside it | **none** | wrong diagnostic boundary string |

**The retention pair fires next cycle, guaranteed.** The glob reads
`docs/cycles/{TASKS,PROGRESS}-v0.{[6-9],1[0-9],2[0-5]}{.md,.*.md,-*.md}`. It is
correct for active v0.28 and **wrong the moment v0.29 activates** — it must
become `2[0-6]`. Nothing derives it. And the only thing that checks it,
`./run export-check`, appears in **neither** lane: `ci_local_jobs` lists 20 jobs
and export-check is not among them, and `.github/workflows/ci.yml` contains zero
occurrences of the string `export`. **So a forgotten hand-edit produces exactly
the condition v0.28 was built to prevent, and the checker that would catch it is
the one nobody runs automatically.**

**This does not reopen the v0.22 G3 disposition, and Step 2 must not be allowed
to.** That disposition refused a hosted duplicate of `export-check`, and its
reasoning holds: export-check inspects an artifact that exists only when an
operator makes one. **The retention pattern is a different object.** It is a
tracked repository file whose correctness is a pure function of the active cycle
declaration, and it can be verified with no export in existence.

**The boundary pair is not reachable today and this file says so.**
`(0, 28) ≥ (0, 23)`, so the floor branch never runs without the freshness branch
having bound its variables. Demonstrated by reconstruction: with the constants
reordered, the checker raises `UnboundLocalError` instead of reporting a defect —
**the checker's own error path replaced by a traceback.** A latent coupling
between two module constants that nothing asserts.

**The ordering pair is correct today and this file says that too.** SQL orders
`published_day IS NULL` ascending so NULL-day rows land last in a newest-first
list; Rust's `Option::cmp` makes `None` the minimum. **They agree.** The new test
`coverage_boundary_uses_archive_order_for_a_misordered_window` genuinely fails
against the old `.rev().find_map()` — its window is `middle, oldest, newest`, so
positional order returns `2026-07-09` where archive order returns `2026-07-05`.
**What is missing is anything binding the two declarations, and any case
exercising the NULL-day term where the agreement is subtlest.**

**One live governed row overstates its own margin.** The export-bound disposition
records **514,154 bytes / 20.68%** headroom from the Step 5 implementation tree
at 2,485,846. The closing export measured 2,526,556 and the delivered export is
2,530,129, so the true margin is **469,871 bytes / 15.66%** — the row is
**~44,283 bytes optimistic about a trigger it governs.** Not false; correctly
labelled as the Step 5 measurement. **But a trigger row's stated margin should be
the current one, because that number is what a reader uses to decide the trigger
is far away.**

**And the reviewer's own verification range narrowed.** With retention depth 3,
only v0.26–v0.28 are exported. **This reviewer can no longer independently read
the closed cycle documents it used to check.** That was the correct trade and
`checklist-audit` at 219 → 219 across the archival is the evidence the repository
still validates them — but the claim "no historical cycle document was moved,
edited, or deleted" now rests on Codex's measurement and the checkers, **not on
this reviewer having looked.** Said plainly rather than left implied.

---

## Declared scope

| Scope class | Path or value |
|---|---|
| `scope_version` | `1` |
| `disposition_intent` | `no-release` |
| `allow` | `tools/cycle_check.py` |
| `allow` | `tools/export_check.py` |
| `allow` | `crates/store/src/sqlite.rs` |
| `allow` | `crates/**/tests/**` |
| `allow` | `shell/tests/**` |
| `allow` | `config/invariant-rules.json` |
| `allow` | `tools/invariant_scan.py` |
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
| `forbid` | `tools/model_profiles.py` |
| `forbid` | `config/protected-artifacts.json` |
| `forbid` | `tools/evidence_artifacts.py` |
| `forbid` | `apps/cored/src/main.rs` |
| `forbid` | `crates/ingest/src/**` |
| `forbid` | `crates/compliance/src/**` |
| `forbid` | `crates/extract/src/**` |
| `forbid` | `crates/view/src/**` |
| `forbid` | `shell/intel_shell/**` |
| `forbid` | `config/core.json` |
| `forbid` | `config/schedule.json` |
| `forbid` | `config/subscriptions*.json` |
| `forbid` | `observations/**` |
| `forbid` | `docs/state-archive/**` |
| `forbid` | `fixtures/**` |
| `forbid` | `docs/cycles/TASKS-v0.2[0-8]-EXECUTION.md` |
| `forbid` | `docs/cycles/PROGRESS-v0.2[0-8].md` |

**Release authorities are declared even though the intent is `no-release`,
because Step 8 has a real decision to make.** See R-CLOSE: the correction shipped
by v0.28 COVERAGE-ORDER is **unpublished**, and published v0.17.0 still contains
the positional `.rev().find_map()` boundary derivation.

**`config/schedule.json` is forbidden and the 600-second clock does not run.**
Step 6 produces a **design and a decision**, not traffic. If any step believes it
needs to change a cadence value or issue a publisher request, **that belief is
the finding: record it and stop.**

**`config/protected-artifacts.json` is forbidden.** Step 7's evidence
registration follows v0.28's established path exactly: an explicit operator
authorization, a dated amendment, scope narrowed to the exact evidence paths plus
the manifest, one implementation commit. **This paragraph is notice of the
mechanism, not the authorization.**

**`docs/state-archive/**` is forbidden.** v0.28's archival is complete and
byte-proven. **A second archival is not in this cycle's scope**; Step 5 records
what should trigger the next one, and recording is not doing.

---

## Entering state (asserted, not yet verified)

**Every line here is a hypothesis for E0. Every byte figure was derived from a
Repomix export that strips one trailing newline per file and is therefore a lower
bound — E0 measures the repository, and where E0 disagrees, E0 is right.**

- v0.28 closed `no-release` at closure commit `ec8eaa2a…` with audit record
  `d9ecea49…`; no tag, version authority, remote `main`, or release ref moved;
  v0.17.0 remains published at closing commit `4af28418…`.
- Worktree clean; `ci-local` **20/20**; golden **11/11**; `invariant-scan`
  **12 rules / 49 controls**; `checklist-audit` **224/224**; shell **303**
  collected / **303** passed / **0** skipped on both constrained lanes.
- Manifest: **316** pins, **182,773** bytes (≈578 B/pin), against the 1 MiB
  bound — **865,803 bytes** of headroom.
- Export: **2,530,129** bytes, **152** files, **84.3%** of the 3,000,000 ceiling,
  **469,871** bytes of headroom.
- Governed rows: `ARCHITECTURE.md` **12** data rows of which **3** are
  trigger-bearing; the v0.28 deferred table **15**.
- Retention glob is `2[0-5]`, correct for v0.28 and **wrong for v0.29**.
- `export-check` is in neither CI lane: 20 `ci_local_jobs`, zero `export`
  occurrences in `ci.yml`.
- `architecture_trigger_rows` and `deferral_trigger_rows` have exactly one store
  (line 1907) and one load (line 1919), with no initialization.
- `cycle_check.py:1492-1497` contains two branches whose guards are
  `required_cycle_name is None` and `required_cycle_name is not None` with the
  same body and the same second condition — **an exhaustive pair that reads as a
  distinction and is not one.**
- Rough growth: `STATE.md` gained ≈22,600 bytes in v0.28 and the manifest ≈8,700;
  `docs/cycles` is near steady-state under depth 3 (v0.26 pair 160,724; v0.27
  116,523; v0.28 96,892). **E0 derives the real per-cycle rate; this is an
  estimate and is labelled one.**

---

## Drafted gates

| Gate | Where | Hypothesis |
|---|---|---|
| **G1** [P1] | `repomix.config.json`; `tools/export_check.py`; `run`; `.github/workflows/ci.yml` | **The retention window is a hand-edited glob whose only verifier runs nowhere automatic.** Confirm the glob's current `2[0-5]` bound, confirm `export-check` is absent from both lanes, and then **demonstrate by execution** what `export_check` reports against an export taken with a v0.29 active declaration and an unedited glob. Record the exact error text. **If it does not fail, the derivation is weaker than claimed and that is the finding.** |
| **G2** [P1] | `tools/cycle_check.py` | **Determine whether the retention pattern can be verified with no export in existence.** `cycle_check` already resolves the active cycle and already runs in both lanes. State what it would take to check the glob against `CYCLE_RETENTION_DEPTH` and the active declaration, and **state explicitly whether that duplicates `export-check` or checks a different object.** The v0.22 G3 disposition refused a hosted duplicate; **decide whether this proposal is one, and if it is, say so and stop.** |
| **G3** [P2] | `tools/cycle_check.py:1907,1919,1385,1386` | **Reproduce the unbound path.** With the two boundary constants reordered in a throwaway copy, run the checker against a cycle between them and record whether it reports a defect or raises. **Confirm it is unreachable under the current constants** and state precisely what relationship must hold. |
| **G4** [P2] | `crates/store/src/sqlite.rs:34-39,296-312` | **Establish whether the Rust comparator and the SQL ordering actually agree, term by term**, including the NULL-day term where SQL uses `published_day IS NULL` ascending and Rust relies on `Option::cmp` making `None` the minimum. **Confirm or refute agreement by execution over a fixture containing NULL-day rows on both sides**, not by reading. Then state what binds them today. |
| **G5** [P2] | `ARCHITECTURE.md` export-bound row; v0.28 closing measurements | **A live trigger row overstates its own margin.** Confirm the row records 2,485,846 / 514,154 / 20.68% while the closing export measured 2,526,556 and the delivered export is 2,530,129. **Determine which number a governed row should carry** — the measuring step's or the cycle's last — and record the rule, because this recurs every cycle. |
| **G6** [P1] | `config/schedule.json`; v0.26–v0.28 records | **The 600-second SEC clock has never run, and everything three cycles built exists to make it safe.** Enumerate what is now proven — coverage detection before insert, order-independent boundary derivation, the corrected cadence criterion, the 7.75× measured margin — and what is **still unproven**: recurring execution, peak-season density, deadline-day density, and the hours neither live sample covered. **Produce the bounded design and the exact refusal conditions. Do not run anything.** |
| **G7** [P2] | published v0.17.0; v0.28 COVERAGE-ORDER | **The published artifact still contains the defect v0.28 corrected.** Confirm that v0.17.0 as tagged derives the incoming boundary positionally and that the correction exists only in unpublished descendants. **State the exact user-visible consequence** — a wrong raw boundary string in one internal diagnostic for a misordered window, no shape change, no `/v1/*` value change — **so Step 8 decides on the real size of it and not on an impression.** |

---

## How to run this file

Execute top to bottom, one task and one commit at a time. Follow `AGENTS.md §5`
after **every** task. Implementation and audit-record commits stay separate.

- **🤖 = Codex executes and self-verifies end to end** — no publication, no push
  to `main`, no ref creation or deletion **in the working repository**.
- **🧑 = exactly one named operator action or decision.**

**Interpretive rules, binding throughout.** An exit code of 0 from a construction
the checker never examined is **not measured**. A measurement that disagrees with
an acceptance criterion is **reported as measured**; the criterion is what gets
corrected. **Two declarations of one fact are a defect until something binds
them** — and the binding must be a second, independent derivation that the first
cannot satisfy by construction, which is why the v0.28 trigger-count test is the
template and a self-consistency assertion is not. **A rule that cannot fail has
not passed.** Every step here must demonstrate its rejection path against real
output before demonstrating its acceptance path.

**Dependency gates.** Step 1 blocks everything. Step 2 blocks Step 3 only if G2
concludes the binding belongs in `cycle_check`. Steps 3, 4, and 5 are independent
of each other. **Step 6 is a design and a decision and runs no traffic under any
outcome.** Step 7 is blocked by every preceding implementation step; Step 8 by
Step 7.

**Amendment obligation known in advance.** Step 7's hosted receipt directory is
`evidence/ci-runs/<run-id>-<attempt>/**` and its run id cannot exist until the
run does. Step 7 adds that exact directory by a dated `## Runbook amendments`
entry in the same commit that first needs it, following v0.28's authorized
pattern. **This is notice, not permission.**

### Cycle activation (before E0)

In a separate preparatory implementation/audit pair: confirm the worktree is
clean and record the measured refs **without asserting a literal `origin/main`
hash in `STATE.md`'s header**. Commit **only** this runbook at
`docs/cycles/TASKS-v0.29-EXECUTION.md` — including its `## Declared scope`
table — the `AGENTS.md` header moving the active declaration from v0.28 to v0.29,
and a new `docs/cycles/PROGRESS-v0.29.md`.

**This file deliberately contains no reserved cycle-closing heading and no
blank closing template.** v0.28's activation failed on exactly that and the
failure was this reviewer's. R-CLOSE appends the record when the cycle closes.

**Activation will fail `export-check` if the retention glob is not updated, and
that is expected.** The glob must move from `2[0-5]` to `2[0-6]` so the retained
set is v0.27, v0.28, v0.29. **Make that edit at activation and record it**, then
let Step 2 remove the need to remember it. If any exact-current-cycle fixture
encodes v0.28 values, correct it by dated amendment as v0.28 did.

**Every governed row in the table below already carries `v0.29` and a date**, so
activation is green under the v0.28 identity rule. **Those dates are carried
forward and are hypotheses until E0 rewrites them with v0.29 measurements.**

### Global definition of done

Protected hashes exact; all **316** pins match until Step 7 adds more; **golden
11/11 byte-identical**; `./run version-check` green; zero rustc warnings on
offline and net builds; all Rust tests green; all shell tests green under Python
3.11 **and** 3.12; shell results recorded as collected / passed / skipped with
every skip named and compared by `tools/test_population.py`, never as a bare
`N/N`; clippy, fmt, ShellCheck, floor byte-compilation, and locked Rust 1.78
green.

**`checklist-audit` and the export ceiling are this cycle's two controls.** The
audit total must not fall. The export must stay under 3,000,000 bytes at every
measured point, and **every export figure recorded must name the tree it was
measured on**, which is the discipline G5 exists to settle.

---

## Deferred means deferred

| Deferred item | Unchanged trigger | Measured observation (cycle-identified) | v0.29 action |
|---|---|---|---|
| T7 robots single-flight | a second concurrent harvester | v0.29 · 2026-07-31 — E0 started no harvester and made no publisher request; only the existing sequential form remains exercised | none |
| NEGATIVE-CACHE Decision B | a live transient robots outage for an admitted publisher while a usable last-known-good policy exists, plus operator authorization | v0.29 · 2026-07-31 — E0 observed no live outage and created no last-known-good policy; the trigger is absent | none |
| Conditional GET (`ETag` / `If-Modified-Since`) | an operator-authorized cycle whose scope permits the `net` request path plus a live 304 observation | v0.29 · 2026-07-31 — the activation-to-E0 diff leaves forbidden `crates/ingest/src/**` byte-identical and no live request or 304 occurred | none — the gap stays recorded |
| `edgar:*` extension field mapping | an operator-authorized cycle permitting `crates/ingest/src/**` for mapping, with a connector review | v0.29 · 2026-07-31 — `crates/ingest/src/**` is forbidden and byte-identical; no connector review occurred | none |
| Live multi-publisher behaviour in one runtime | further origins beyond the two configured, or concurrency | v0.29 · 2026-07-31 — the v0.27 sequential two-origin result remains the only live execution; E0 made no publisher request | none — complete, do not re-exercise |
| First recurring scheduled SEC run | explicit operator authorization of a bounded scheduled window, separate from any cycle scope | v0.29 · 2026-07-31 — G6 confirms the 600-second clock has never run and records a 1,260-second, at-most-three-invocation design with exact refusals; E0 executes no traffic | **Step 6 — design and recorded decision only** |
| Postgres / pgvector / multi-host seam | unchanged | v0.29 · 2026-07-31 — E0 exercised the existing single-writer SQLite and single-host topology only | none |
| A4 untrusted-shell boundary | a third-party/untrusted shell, or any claim HC1 is invariant under shell replacement | v0.29 · 2026-07-31 — E0 exercised only the first-party shell and makes no shell-replacement invariance claim | none |
| L2 forced-command wrapper | an operator server session | v0.29 · 2026-07-31 — E0 opened no operator server session | none — remains scheduled |
| R3/R4 open-bottom coverage | a spelling outside registered vocabulary | v0.29 · 2026-07-31 — registered invariant self-test passed 12 rules / 49 controls and exposed no unregistered spelling | none |
| Third configured publisher | a completed compliance review, then a separate admission decision | v0.29 · 2026-07-31 — no compliance review completed and no admission decision is pending | none |
| `v0.8.0` / `v0.10.2` publication | operator-authorized push of both exact annotated objects | v0.29 · 2026-07-31 — no publication authorization was given and E0 moved no ref | none — **no historical ref touched** |
| `--skip-local-tag-verification` removal | both historical tags published plus a passing hosted full-history `cycle-check` without the flag | v0.29 · 2026-07-31 — both historical tags remain unpublished, so the trigger is absent | none — **the flag stays** |
| Manifest retention/indexing | 1 MiB manifest, or two consecutive `verify-artifacts` runs ≥1.00 s | v0.29 · 2026-07-31 — E0 measured 316 pins and 182,774 bytes; complete runs took 0.11 s / 0.10 s real, so neither trigger fired | **Step 1 — re-measure only** |
| Version literal in `app.py` | a cycle whose declared scope permits shell source changes | v0.29 · 2026-07-31 — the literal remains, while `shell/intel_shell/**` is forbidden and unchanged through E0 | none — recorded, not acted on |
| Release-classification criteria with no executed control | an operator decision that prose adjudication is insufficient | v0.29 · 2026-07-31 — the contract still declares prose adjudication and E0 received no operator decision to replace it | none — recorded, not acted on |
| Second `STATE.md` archival | the export ceiling trigger fires, or `STATE.md` alone exceeds the bound Step 5 records | v0.29 · 2026-07-31 — E0 derives normalized State growth at 22,525 bytes/cycle; v0.28's archival remains byte-proven, the export ceiling has not fired, and Step 5 will record the next State-size boundary | **Step 5 — record the next boundary, do not archive** |

---

## Step 1 · E0 — Rebuild the entering state and settle seven gates 🤖

**Objective.** Confirm HEAD is green and settle G1–G7. **Every assertion in
`## Entering state` is a hypothesis. Report the measured value, especially where
it differs — and expect the byte figures to differ, because the reviewer's came
from a newline-stripping export.**

**Decision gate.** If the worktree is dirty, if v0.28's closure and audit commits
are not where the entering state places them, or if any local gate fails at
entry, **record and stop.**

**Acceptance criteria.**

- All 20 `ci-local` jobs pass; invariant **12/49**; golden **11/11**; **316** pins
  verified twice with both real times recorded; both Python lanes reported as
  collected/passed/skipped via `tools/test_population.py`.
- G1 settled **by execution**, with the exact `export_check` error text recorded.
- G2 settled with an explicit duplication ruling against the v0.22 G3 disposition.
- G3 settled **by reproduction** in a throwaway copy.
- G4 settled **by execution over NULL-day fixtures on both sides**.
- G5 settled with a stated rule for which measurement a governed row carries.
- G6 settled as an enumeration of proven versus unproven, with no traffic.
- G7 settled with the exact user-visible consequence stated.
- The per-cycle growth rate of `STATE.md`, the manifest, and the export is
  **derived**, and the resulting cycles-of-headroom figure recorded.
- The deferred table's 17 rows are rewritten with **v0.29** measured observations.

**Done when** every gate carries a measured answer and the entering state is
either confirmed or corrected in `STATE.md`.

- [x] **E0**

---

## Step 2 · RETENTION-BIND — Stop hand-editing a glob every cycle 🤖

**Objective.** Bind the retention window to the active cycle declaration so a
forgotten edit fails in a lane that actually runs.

**Decision gate.** If G2 concluded this duplicates `export-check` and reopens the
v0.22 G3 disposition, **record that and stop.** The disposition stands until an
operator decides otherwise, and **a reviewer's proposal is not that decision.**

**Acceptance criteria.**

- The retention pattern's correctness is verified in a lane that runs
  automatically. The intended object is `repomix.config.json` — a tracked file
  whose correct contents are a pure function of the active cycle and
  `CYCLE_RETENTION_DEPTH` — **checked with no export in existence**, which is
  what distinguishes it from `export-check`.
- The expected pattern is **derived**, never written down twice. If the check
  compares against a literal, it has recreated the defect it was built to remove.
- A registered `R12` control proves, by execution, that a stale retention pattern
  is rejected. **Demonstrate the rejection before the acceptance.**
- `./run export-check` still passes at the project root, and its derived-source,
  required-path, ceiling, retention, and absence checks are all unchanged.
- If the binding cannot be made derivable — for instance because the glob's brace
  syntax cannot be generated from the depth — **say so plainly and record the
  hand-edit as a permanent, named cycle obligation instead of pretending it is
  solved.**

**Done when** activating a cycle without touching the glob fails automatically,
demonstrated.

- [x] **RETENTION-BIND**

---

## Step 3 · BOUNDARY-BIND — Remove a coupling and a false distinction 🤖

**Objective.** Make the two forward boundaries' required relationship explicit,
and delete a branch pair that implies a distinction it does not make.

**Decision gate.** If G3 showed the unbound path is reachable under the current
constants, **that is a live defect, not a latent one** — record the reclassification
and treat it at P1.

**Acceptance criteria.**

- The floor check can no longer read an unbound variable under any ordering of the
  two constants. Initialize, nest, or derive — **choose one, record why**, and do
  not leave the safety resting on an unasserted comparison between two literals.
- If the relationship between the boundaries is load-bearing, something asserts
  it. A checker that raises `UnboundLocalError` instead of reporting a defect has
  **replaced its own error path with a traceback**, and that is the outcome being
  designed out.
- `cycle_check.py:1492-1497`'s exhaustive branch pair collapses to the single
  condition it already is. **Confirm by test that behaviour is unchanged** — this
  is a readability correction and must be proven not to be more.
- A test covers a cycle name between the two boundaries.

**Done when** no ordering of the two constants produces a traceback, demonstrated
by reproduction rather than by argument.

- [ ] **BOUNDARY-BIND**

---

## Step 4 · ORDER-BIND — Bind the comparator to the ordering it mirrors 🤖

**Objective.** Make the Rust comparator and the SQL `ORDER BY` a bound pair rather
than two independent statements of one ordering.

**Decision gate.** Independent of Steps 2 and 3. `apps/cored/src/main.rs` and
`crates/ingest/src/**` are **forbidden**: this step reaches the store and its
tests only.

**The blast radius is bounded and every record must say so.** The field is
observational, detection never fails the poll, and a divergence produces a
**wrong raw boundary string in one internal diagnostic** — not a dropped filing,
not data loss. **Do not inflate this.**

**Acceptance criteria.**

- Something binds the two orderings such that changing the SQL without changing
  the comparator fails. **A test asserting the comparator against itself is not a
  binding** — the v0.28 trigger-count test is the template: a second, independent
  derivation the first cannot satisfy by construction. The natural form here is a
  fixture inserted into the store, ordered once by SQL and once by the comparator,
  asserted equal.
- The NULL-day term is covered on **both** sides: SQL's `published_day IS NULL`
  ascending and Rust's `None`-as-minimum, over a fixture containing NULL-day rows
  in both the held archive and the incoming window.
- The existing misordered-window test is unchanged and still passes.
- Golden stays **11/11 byte-identical** and SEC identity stays **200 kept / 0
  dropped**. **If either moves, stop.**
- The `/ingest` response shape and every `/v1/*` value domain are unchanged, and
  both are recorded explicitly for Step 8.

**Done when** a divergence between the two orderings is detected by execution.

- [ ] **ORDER-BIND**

---

## Step 5 · MARGIN-TRUTH — Make a governed row carry its current margin 🤖

**Objective.** Correct one live trigger row's stated headroom and settle the rule
for which measurement a governed row carries, because this recurs every cycle.

**Decision gate.** Blocked by nothing. **`docs/state-archive/**` is forbidden:
this step records the next archival boundary and does not archive.**

**Acceptance criteria.**

- The export-bound row records the **cycle's last** export measurement and its
  true headroom, and names the tree it was measured on. The Step 5 figure is not
  deleted — **superseded openly, in the house forward-correction form.**
- G5's rule is written into `AGENTS.md` where the trigger-freshness contract
  lives: a governed row's measured cell carries the latest measurement available
  at close, not the one taken by whichever step first wrote it. **State it
  symmetrically so a later cycle does not argue the opposite.**
- The next `STATE.md` archival boundary is **recorded with a trigger** and a
  dated observation that it has not fired, using v0.28's reasoned-boundary form
  rather than a line count. E0's derived growth rate is the input.
- Every export figure written this cycle names its tree.

**Done when** the three live trigger rows each carry a current, cycle-identified
margin and the recording rule is executable prose in the contract.

- [ ] **MARGIN-TRUTH**

---

## Step 6 · SCHEDULE-DESIGN — Design the run that has never happened 🧑🤖

**Objective.** Produce the bounded design for a first recurring scheduled SEC run,
and record the operator's decision. **This step issues no publisher traffic under
any outcome.**

**Decision gate.** `config/schedule.json` is **forbidden** and no cadence value
changes. **If any part of this step would send a request, stop.**

**Why now.** v0.26 chose the cadence, v0.27 corrected its criterion and built
pre-insert coverage detection, v0.28 made the boundary derivation order-independent.
**All three exist to make a recurring clock safe, and the clock has never run.**
The apparatus is unexercised in the mode it was designed for — the system-level
form of this project's own first principle.

**🧑 The operator's decision, and only the operator's.** Three outcomes, none
defaulted:

- **Authorize a bounded scheduled window in a later cycle** — Step 6 delivers the
  design and the refusal conditions; execution needs its own explicit authorization.
- **Authorize nothing and record why** — a reasoned refusal is a complete outcome
  and closes this step.
- **Decline to decide yet** — the deferred row stays with its trigger unchanged.

**Acceptance criteria.**

- The design states the exact bounded window, the maximum request count, the
  abort conditions, what would be measured, and **what the run could not prove**
  even if it succeeded — peak-season density, deadline-day density, and the hours
  neither live sample covered.
- The design states which existing controls would observe the run and which would
  not, by name.
- The refusal conditions are stated as executable checks where possible and as
  operator judgements where not, **with the split made explicit rather than
  blurred.**
- The operator's decision is recorded with its date and reason.
- **No publisher request, no scheduler run, no cadence change.** Confirmed by a
  complete log search, as v0.27 and v0.28 both did.

**Done when** the design exists, the decision is recorded, and nothing has been
sent.

- [ ] **SCHEDULE-DESIGN**

---

## Step 7 · RE-MEASURE — Hosted verification on a neutral branch 🤖

**Objective.** Produce authenticated hosted evidence at an exact candidate on a
neutral ref, without publishing.

**Decision gate.** Blocked by Steps 2–6. No push to `main`, no tag.

**Acceptance criteria.**

- All seven executable hosted jobs pass at the exact candidate; the
  dependency-drift job skips under its declared report-only condition.
- Attestations required; every signed identity accepted, zero rejected; the
  complete runner matrix found.
- Both shell lanes compared by `tools/test_population.py` with comparator-derived
  `collected`, `equivalent`, and `equivalent_passed`. **Every number written is
  the comparator's output, never transcribed from a log.**
- **316** pins verified on the candidate; golden **11/11**.
- Any manifest registration follows v0.28's authorized path exactly: explicit
  operator authorization, dated amendment, scope narrowed to the exact evidence
  paths plus the manifest, one implementation commit.

**Done when** the candidate carries release-grade authenticated evidence.

- [ ] **RE-MEASURE**

---

## Step 8 · R-CLOSE 🧑🤖

**Objective.** Close v0.29 with an explicit, reasoned disposition.

**The drafted intent is `no-release`, but this cycle's decision is not a
formality.** Published **v0.17.0 still contains the defect v0.28 corrected**: it
derives the incoming coverage boundary positionally, so a window that is not
newest-first yields a wrong raw boundary string. The correction exists only in
unpublished descendants. **G7 measures the exact size of that consequence so this
decision rests on a number rather than an impression.**

**🧑 The operator's decision, and only the operator's.** Publication
authorization is a separate explicit act and is **not** implied by this runbook,
by green gates, or by Step 7's evidence. Two options, stated so neither is a
default:

- **`no-release`** — close v0.29 on its own record. The correction and this
  cycle's bindings ride into a later release.
- **`release` at patch** — ship the order-independent boundary derivation. No
  route, response shape, `/v1/*` value domain, dependency, or schema moves, so
  the named-surface rule and the public value-domain criterion both stay unfired.
  **This requires a stated reason of its own** and may not be inherited from
  "the gates are green."

**Acceptance criteria.**

- The closing record names `Cycle closed`, the dated `Release disposition`, and —
  if `release` — `Release` and `Release commit:` under R-CLOSE's two-commit
  tagged-closing protocol.
- Every declared permission is reconciled as used or unused, by path.
- Every gate G1–G7 has a recorded measured answer, including G6's
  no-traffic outcome and G7's stated consequence.
- **The six reviewer errors in this file's header are preserved in the cycle
  record as reviewer errors**, not restated as findings and not quietly dropped.
- `STATE.md` records the final export figure against the ceiling **naming its
  tree**, the `checklist-audit` control, and the derived growth rate.

**Done when** the disposition is authorized, recorded, and measured.

- [ ] **R-CLOSE**

---

## Cycle checklist

- [ ] Worktree clean at entry; v0.28 closure and audit commits where E0 measures them
- [ ] Retention glob updated at activation and the edit recorded
- [ ] Every entering-state hypothesis measured and confirmed or corrected
- [ ] G1–G7 each carry a measured answer; G1, G3, and G4 answered **by execution**
- [ ] Every new binding demonstrated **rejecting** before demonstrated passing
- [ ] No binding implemented as a self-consistency assertion
- [ ] No expected value hardcoded in any test added or edited this cycle
- [ ] No closed cycle document edited, moved, or deleted
- [ ] `checklist-audit` total does not fall; every figure recorded
- [ ] Export under 3,000,000 bytes at every measured point, each naming its tree
- [ ] Golden **11/11** byte-identical at every step
- [ ] SEC identity **200 kept / 0 dropped** unchanged
- [ ] **316** pins verified; manifest bounds re-measured against 1 MiB / 1.00 s
- [ ] Both Python lanes reported as collected/passed/skipped, comparator-derived
- [ ] Deferred table rows all carry v0.29-identified observations
- [ ] No publisher request, no scheduler run, no cadence change
- [ ] Six reviewer errors preserved as such in the cycle record

---

## Standing prohibitions

- **No publisher request and no scheduler run.** Step 6 designs and decides; it
  sends nothing. The 600-second clock has never run and this cycle does not
  authorize it.
- **No closed cycle document is edited, moved, renamed, or deleted.**
- **No second `STATE.md` archival.** Step 5 records the next boundary; recording
  is not doing.
- **No push to `main`, no tag, no ref creation or deletion** before Step 8's
  authorized action.
- **No edit to `run` or `tools/model_profiles.py`** — both are `authorization`
  pins.
- **No manifest edit** except under an explicit operator authorization carried by
  a dated amendment, scoped to exact evidence paths, in one implementation commit.
- **No hardcoded expected value** in any test written or edited this cycle.
- **No binding that a single implementation can satisfy by construction.** Two
  declarations are bound only by a second, independent derivation.
- **No rule ships without a demonstrated failing case.**
- **No retraction is proposed** without a twice-verified measured false claim in
  an immutable published record. The count stands at three.

---

## Provenance of this draft

**Read, not measured:** the Codex v0.28 report; `STATE.md` header and v0.28
sections; `TASKS-v0.28-EXECUTION.md` amendments 1–10; `AGENTS.md` §§ on scope,
freshness, R-CLOSE, and the cycle-ending rhythm; `ARCHITECTURE.md` §§6–8.

**Measured against the 2026-07-31 export, by path and line:** export size
2,530,129 bytes and 152 files, matching the reported figure exactly; composition
by area; 12 rules / 49 `fail_before` controls with R12 at 21 and the three new
control names; 316 `pinned_files[]` at 182,773 bytes and ≈578 B/pin;
`cycle_check.py:1385-1386` boundary constants, `:1479-1499` the removed header
fallback and the exhaustive branch pair, `:1508-1545` the identity gate,
`:1546-1614` `governed_trigger_subjects`, `:1617-1681` completions, `:1683-1721`
carry-forward, `:1903-1934` the bound counts and floor; `test_cycle_check.py:1160-1190`
the derived pair and `:1227-1301` both carry-forward paths; `export_check.py` in
full including `MAX_EXPORT_BYTES`, `CYCLE_RETENTION_DEPTH`, and both excluded
classes; `test_export_check.py` at 8 tests; `sqlite.rs:34-39` the comparator,
`:235-243` the corrected doc comment, `:296-312` the derivation, `:1445-1468` the
misordered-window test; `repomix.config.json` retention glob; `run` `ci_local_jobs`
at 20 with no export-check; `ci.yml` with zero `export` occurrences; 274
top-level shell test functions; `config/schedule.json` `sec-edgar-usgaap: 600`.

**Measured by reconstruction, not against the repository:** the `UnboundLocalError`
demonstration, which was reproduced from the two constants and the store/load
line numbers, **not** by running the real checker.

**Asserted and not verified:** every line under `## Entering state`; all
per-cycle growth estimates and the cycles-of-headroom figure; the claim that the
NULL-day terms agree, which follows from `Option::cmp` and the SQL `IS NULL`
ordering but **is G4's to prove by execution**; the claim that no closed cycle
document was moved or edited, which now rests on Codex's measurement and the
checkers because retention depth 3 removed those files from this reviewer's
reach.

**Six reviewer errors are recorded in this file's header** rather than here,
because a provenance note is where a reader looks last and an error is what they
should see first.
