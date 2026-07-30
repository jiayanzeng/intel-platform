# TASKS-v0.28-EXECUTION.md — the clock, the ceiling, and the order

## Runbook amendments

### 2026-07-30 · Activation syntax correction

The supplied draft already contained a blank cycle-closing heading while all
task boxes remained unchecked. After activation commit `c44af84…`,
`./run cycle-check` exited 1 with
an error that an open runbook cannot contain the reserved closing heading.
The prior cycle's activation form contains no closing-record heading; R-CLOSE
appends that record only when the cycle closes. This amendment therefore removes
the premature blank template and rephrases G2's reference to the reserved
heading so it is not mistaken for the heading itself. Every objective, decision
gate, acceptance criterion, declared-scope row, and standing prohibition remains
semantically unchanged.
The activation commit is not amended, rebased, or squashed.

### 2026-07-30 · Activation lifecycle-fixture correction

The first permission-complete `./run ci-local` reached the shell lane and
measured two exact-current-cycle fixtures still encoding v0.27. The active
deferred table has 15 trigger-bearing rows, not the prior 14, and v0.28's
declared `no-release` scope has no release-authority/forbid overlap, not
v0.27's one `shell/intel_shell/app.py` overlap. The runbook already required the
trigger count control to be corrected when the population changed; the scope
fixture was an additional activation assumption. This amendment permits only
those two expected-value corrections before E0 is restarted. It changes no
checker behavior, objective, decision gate, acceptance criterion, scope row, or
standing prohibition. Step 3 still removes the temporary exact trigger count as
written.

### 2026-07-30 · E0 measurements and drafted-value corrections

Step 1 — measured answers recorded and completion checked — 2026-07-30

E0 restarted only after the activation compatibility commit and its separate
audit record existed. The permission-complete entry point then passed all 20
local jobs. The seven drafted gates settled as follows.

- **Entering state.** Before activation, candidate-lineage HEAD was
  `ddf08d2063f384d6c3d6d5ddef87b65a9167625c` on
  `codex/v0.23-action-migration`, exactly one commit beyond locally recorded
  `origin/main`; local `main` was not that commit and remained 102 commits
  behind `origin/main`. The active worktree contained only this supplied
  untracked runbook. After the recorded activation corrections, `./run
  ci-local` passed 20/20 with 145 workspace tests, 62 net tests, invariant
  12/46, clean clippy/fmt/ShellCheck and locked Rust 1.78. Standalone golden
  passed 11/11. Clean Python 3.11.4 and 3.12.13 lanes each collected and passed
  293 with zero skips; `tools/test_population.py` derived `collected=293`,
  `equivalent=true`, and `equivalent_passed=293`. Both complete artifact
  verifications matched 301 pins and took 0.10 s real; the manifest was 174,152
  bytes. The architecture table had 11 data rows / 2 governed rows; the active
  deferred table had 15 governed rows, correcting the drafted 14.
  `checklist-audit` passed 216 checked / 3 retracted / 216 matched / 0
  exemptions. `STATE.md` was 6,984 lines / 453,741 bytes, and the drafted
  region sizes were corrected to 12,540; 17,273; 127,922; 185,799; 43,650;
  38,748; and 27,809 bytes in the stated order. The named
  `docs/state-archive` consumer search remained empty across `tools/*.py`,
  `run`, `AGENTS.md`, `ARCHITECTURE.md`, and `config/*.json`; no manifest pin
  names it.
- **G1 — confirmed by execution.** In a throwaway clone, every active deferred
  measured cell was blanked while its measured-column header retained
  `2026-07-30`. `./run cycle-check` exited 0. The real architecture and active
  runbook rows each carried their own valid date, so removing a header date
  from the real tables would reject zero current governed rows. The header
  fallback is therefore vacuous when present, exactly as drafted.
- **G2 — confirmed.** The v0.24, v0.25, v0.26, and v0.27 closing records each
  say `2026-07-30`. At most one cycle closing on a date can be distinguished by
  a date-only discriminator; three of these four later measurements are not
  distinguishable from a copied token.
- **G3 — confirmed by execution.** `tools/cycle_check.py:1707` discarded the
  `(architecture_rows, deferral_rows)` return, and the only consumer was the
  activation-corrected exact-current-cycle test asserting `(2, 15)`; no
  production floor existed. A throwaway clone with every trigger in both
  governed tables changed to `none` produced derived counts `(0, 0)` and
  `./run cycle-check` exited 0.
- **G4 — confirmed.** `tools/export_check.py` only checked inclusion:
  `SOURCE_ROOTS` was exactly `crates`, `apps`, `tools`, `shell`, and seven
  `REQUIRED_PATHS` covered neither cycle retention, observations, nor
  `docs/state-archive`; no byte bound existed. The exact project-root
  `./run export-check` passed 99 derived sources / 7 required paths / 182
  exported files. A retained output measured 4,975,987 bytes, 99.52% of decimal
  5 MB with 24,013 bytes headroom. Raw exported-file composition was:
  `docs/cycles` 34 files / 1,435,284 bytes; observations 13 / 949,344;
  repository root 12 / 713,006 (including `STATE.md` at 453,741);
  `docs/state-archive` 1 / 297,739; and all other reviewed files 122 /
  1,564,264. The externally measured project-knowledge observation remains
  2,067 chunks against a 2,000 limit on 2026-07-30.
- **G5 — confirmed by execution.** A throwaway clone passed `cycle-check`
  before and after moving closed v0.24 out of `docs/cycles`, while its reported
  closed-execution count fell 25 to 24. `checklist-audit` also exited 0 both
  times while checked/matched coverage fell 216 to 209. The
  `audit_deferred` complete-progress-glob assertion still passed. Moving closed
  cycle documents is therefore the silent no-op the draft described; only
  export scope may change.
- **G6 — confirmed with bounded blast radius.** The doc comment at
  `crates/store/src/sqlite.rs:228-235` states source partition and before-insert
  requirements but no ordering requirement. Lines 300-303 return the last
  non-null `published_raw` in positional order. For a misordered window that
  places a middle timestamp last, the field reports that middle timestamp, not
  the oldest. The test at `apps/cored/src/main.rs:2370-2373` compares to
  `incoming.last()` and encodes the same assumption. This can misreport one
  observational diagnostic string; detection still commits the poll and no
  filing or identity is dropped.
- **G7 — confirmed with no implementation.** `AGENTS.md:331` says that adding,
  removing, or redefining a value in an existing `/v1/*` response field takes a
  minor version and openly states that the criterion is prose adjudicated at
  R-CLOSE with no executed control. `ARCHITECTURE.md:445-452` says that adding,
  removing, renaming, or incompatibly reshaping a field on any named response,
  including internal loopback responses, is minor unless the surface is first
  removed from the contract; lines 454-459 repeat the public value-domain
  criterion as prose rather than an invariant rule. These are semantic release
  judgments over unmaterialized historical contracts. No bounded detector is
  available from the current authorities without first defining a machine-
  readable surface/value-domain schema, so the honest self-declaration remains
  the correct posture and implementation is deferred to a later operator
  decision.

### 2026-07-30 · Trigger identity enforcement

Step 2 — governed observations bound to active-cycle identity — 2026-07-30

The data-first commit `5342663f89e3e2b499bfc1bf42b15c44705de58b`
re-measured the two governed architecture rows with row-owned `v0.28` and
ISO-date tokens and passed the pre-tightening checker. The rule deletes the
header fallback, resolves active-cycle identity from the declaration, and
applies that identity gate only at v0.28 forward. Focused lifecycle tests pass
46/46; the real `cycle-check` passes; registered self-test derives 12 rules /
48 controls. The two new R12 mutations execute the dated-header/undated-cell
and prior-cycle-copy failures independently. Standalone golden passes 11/11
with delta zero. No closed runbook changed.

### 2026-07-30 · Trigger population and carry-forward enforcement

Step 3 — nonzero populations and prior subjects enforced — 2026-07-30

The real transition corrects one drafted characterization: v0.27 → v0.28 has
14 prior governed subjects, 15 active subjects, zero drops, and one addition.
“First live SEC RSS harvest” and “Observation-byte manifest coverage” were
dropped in v0.26 → v0.27, not in the current transition; that comparison is
14 → 14 with two drops and two additions. The checker now derives its prior
runbook from `execution_runbooks()`, rejects either governed table at population
zero, and rejects a missing prior subject unless the active runbook carries a
valid dated completion. Fixtures using the two real historical subject names
prove that legitimate completion form. Focused tests pass 50/50,
`cycle-check` passes, registered self-test derives 12 rules / 49 controls, and
standalone golden passes 11/11 with delta zero. No closed runbook changed.

### 2026-07-30 · Review-corpus reduction and workflow-record scope

Step 4 — export scope reduced and State history archived — 2026-07-30

The archival itself changed no file under `docs/cycles/`: lifecycle coverage
remained 219/219 before and after, and no historical cycle document was edited,
moved, or deleted. The acceptance criterion's literal “no file” wording
conflicts with the standing per-task workflow, which requires this active
runbook's completion box and a later append-only progress entry. Those two
control-plane records are the only cycle-directory changes attributable to
closing Step 4; neither is a corpus-retention reduction or a historical edit.

The new through-v0.21 State archive is a byte-exact concatenation of the removed
history, the prior through-v0.13 archive, and removed reference §8/§9. Three
slice hashes and whole reconstructed-output comparisons all matched. State
retains v0.22-forward and reference §1–§7. The first post-reduction export is
2,465,363 bytes / 152 files, retains exactly the v0.26–v0.28 TASKS/PROGRESS
pairs and every observation Markdown file, and excludes the SEC body plus the
State-archive directory. All 301 pins, lifecycle checks, invariant 12/49,
current-tag post-push record count one, and golden 11/11 pass. After the
mandatory status and completion records, the final implementation-tree export
is 2,469,697 bytes / 152 files, 49.39% of decimal 5 MB.

One sandboxed `ci-local` attempt and one sandboxed Python dependency install
were environment non-results; their exact entry points passed with the required
permissions. Two population-log wrappers assigned zsh's read-only `status`
variable after pytest had passed; direct pytest entry points then exited 0 and
the comparator parsed their machine-readable records. The first direct
networked Repomix attempt was rejected for repository-egress risk. With explicit
operator authorization, Repomix 1.17.0 was installed with lifecycle scripts
disabled in an isolated temporary directory containing no repository data, then
the real `./run export-check` executed it against the repository inside the
network-restricted sandbox and passed.

v0.17.0 is published and v0.27 is closed. Annotated object `df4fc3b0…` targets
closing commit `4af28418…`, whose parent is release commit `d5969207…`; post-push
run **30550582370** passed all seven executable jobs at that exact commit, and
authenticated candidate run **30545771070** remains the closing evidence with 7
signed identities accepted and 0 rejected. Every count in the Codex report was
re-derived independently and every one held: 12 rules / 46 planted controls from
`config/invariant-rules.json`; 301 `pinned_files[]`; 20 `ci-local` jobs derived by
`ci_local_job_count()`; seven executable hosted jobs derived from six job
definitions, a two-way Python matrix, and one schedule-gated `drift`; 180
exported files. **No claim in that report was refuted.**

**One reviewer hypothesis was refuted by measurement and is recorded as an error,
not a finding.** The reviewer suspected T7 and NEGATIVE-CACHE Decision B were
trigger-shaped residuals living in ungoverned `ARCHITECTURE.md` prose, because
that table has 11 data rows of which only **2** carry live triggers. That was
wrong. Both are governed rows in the active runbook's **Deferred means deferred**
table, `check_trigger_freshness` reads both tables, and both carried dated
observations. The reviewer measured the second table only after drafting the
suspicion. **The finding below survived that check; the accusation did not.**

**The freshness rule is asserted against a clock coarser than the cycle rate.**
`v0.24`, `v0.25`, `v0.26`, and `v0.27` all record `Cycle closed: 2026-07-30` —
four releases (`v0.15.8`, `v0.16.0`, `v0.16.1`, `v0.17.0`) in one calendar day.
The rule's only discriminator is an ISO date at **day** resolution. At four
cycles per day a date cannot distinguish a row re-measured this cycle from a row
copied verbatim from the last one.

**And it is satisfiable without any per-row date at all.**
`tools/cycle_check.py:1479-1483` computes `valid_dates` from
`f"{header_measurement} {measured}"`. The v0.27 table header reads
`Measured 2026-07-30`, so **every row passes on the header token alone**,
regardless of its own cell. `AGENTS.md:286-288` documents this as intended — "in
its measured-observation cell **or that column's header**" — so this is an
author-side allowance, **not an implementation defect, and it is the reviewer's
to correct.** The executed property today is *"the table bears one parseable ISO
token."* The claimed property is *"every recorded trigger carries a dated
observation showing it has not yet fired."* Those are not the same property.

**Comparing v0.26 to v0.27, Codex did genuinely re-measure.** T7, Decision B, and
the manifest row all changed text and numbers between cycles. **This is a latent
hole, not an observed staleness, and the runbook says so.** It is ranked P1
anyway, because a rule whose whole purpose is to catch a lapsed discipline must
not depend on the discipline it exists to check.

**The count the rule computes is thrown away.** `check_trigger_freshness` returns
`(architecture_rows, deferral_rows)`; the call site at
`tools/cycle_check.py:1707` discards it. The only consumer is
`shell/tests/test_cycle_check.py:1147`, which asserts `counts == (2, 14)` — a
hardcoded pair, the recurring defect class. **Nothing in the running check
enforces a floor**, so a cycle that set every trigger cell to `none` would pass
with zero governed rows and report nothing.

**Separately, the review corpus has crossed a measured ceiling and nothing
measures it.** Project-knowledge indexing reported **2,067 chunks against a 2,000
limit** on 2026-07-30 — the export no longer indexes fully, so search over it is
incomplete. The export is **4,928,231 bytes: 98.6% of 5 MB**, with 71,769 bytes
of headroom. One more cycle of `STATE.md` growth plus a `TASKS`/`PROGRESS` pair
exhausts it. `tools/export_check.py` derives sources from `git ls-files` over
four roots and checks seven required paths — **it verifies inclusion only. There
is no upper bound anywhere in the repository.** About **69%** of what the
reviewer reads is history, not source.

**A closed cycle document may never be edited, and no closed cycle document will
be moved.** `cycle_identity.cycle_documents_dir` returns `docs/cycles` as the
*sole* cycle-document directory; `cycle_check` iterates **every** execution file
there through `check_closed_execution` and `check_authority`; `checklist_audit`
resolves checked boxes across `execution_runbooks()`; and `cycle_check:1777-1781`
requires `audit_deferred`'s inputs to equal the **complete** progress glob.
Moving a closed runbook out of `docs/cycles` would silently delete it from
validation **while `audit_deferred`'s completeness assertion kept passing**,
because that assertion re-derives from the same glob it would have shrunk. **That
is a silent no-op by construction and this cycle will not build one.** The only
sanctioned lever for cycle documents is **export scope** — and the precedent
already exists: `v0.6`–`v0.11` are excluded from the export today, remain in the
repository, and remain fully audited.

**This cycle's subject: make both properties executable, and shrink the corpus
without shrinking what is checked.**

---

## Declared scope

| Scope class | Path or value |
|---|---|
| `scope_version` | `1` |
| `disposition_intent` | `no-release` |
| `allow` | `tools/cycle_check.py` |
| `allow` | `tools/export_check.py` |
| `allow` | `crates/store/src/sqlite.rs` |
| `allow` | `crates/store/src/lib.rs` |
| `allow` | `crates/**/tests/**` |
| `allow` | `shell/tests/**` |
| `allow` | `config/invariant-rules.json` |
| `allow` | `tools/invariant_scan.py` |
| `allow` | `repomix.config.json` |
| `allow` | `docs/state-archive/**` |
| `allow` | `AGENTS.md` |
| `allow` | `ARCHITECTURE.md` |
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
| `forbid` | `fixtures/**` |
| `forbid` | `docs/cycles/TASKS-v0.[12]*-EXECUTION.md` |
| `forbid` | `docs/cycles/PROGRESS-v0.[12]*.md` |

**`disposition_intent` is `no-release`, and that is a decision, not a placeholder.**
No step here moves a route, a response shape, a `/v1/*` value domain, a
dependency, a schema, or a public surface. Step 6 may change one internal
`/ingest` diagnostic *string* in an edge case that has never been observed;
`ARCHITECTURE.md §8` versions named response **shapes**, and the separate v0.25
criterion is scoped to `/v1/*` value domains. **Neither fires.** Step 8 may still
select `release` at a patch level if the operator wants the corrected detector
shipped, but it must state that reason explicitly rather than inheriting it.

**`run` and `tools/model_profiles.py` are forbidden because they are
`authorization`-grade pins.** Editing either changes a `sha256` in
`config/protected-artifacts.json`, which is itself forbidden. `./run export-check`
already invokes `tools/export_check.py` with the export path as its only
argument — **every change in Steps 4 and 5 fits behind that existing interface.**
If a step believes it needs `run`, that belief is the finding: **record it and
stop, do not edit a pinned artifact to make a convenience work.**

**`observations/**` is forbidden and the pinned SEC body is not being deleted.**
`observations/v0.25/feed-shape/sec-edgar-usgaap.rss.xml` is an `observation`-grade
pin among 301. Step 4 removes it from the **export**, not the repository. The
manifest verifies the repository file and is untouched by export scope. **A cycle
that shrank the review corpus by deleting evidence would have destroyed the thing
the corpus exists to review.**

**`docs/cycles/**` closed documents are forbidden as a hard rule.** Not trimmed,
not moved, not banner-edited, not archived. See the header. The `forbid` patterns
above are deliberately broad; the two active v0.28 documents are standing-allowed
by `cycle_check:1369-1372` and need no entry.

---

## Entering state (asserted, not yet verified)

**Every line here is a hypothesis for E0 to confirm or refute against the actual
files. Nothing in this section may be relied upon before Step 1 records it.**

- `main` is at post-push audit `ddf08d20…`, one commit ahead of published `main`,
  unpushed, under the `AGENTS.md:335-341` cycle-ending rhythm accepted 2026-07-29.
  Activation sits on top of it and does **not** amend, rebase, or squash it.
- Worktree clean; 20/20 local gates; invariant **12 rules / 46 controls**; golden
  **11/11**; **301** pins; both constrained Python lanes **293** collected,
  **293** passed, **0** skipped.
- `ARCHITECTURE.md`'s dated-dispositions table has **11** data rows, of which
  exactly **2** are trigger-bearing: protected evidence-manifest growth (1 MiB /
  ≥1.00 s) and shell `StarletteDeprecationWarning`.
- The active runbook's deferred table has **14** trigger-bearing rows.
- `test_cycle_check.py:1147` asserts `counts == (2, 14)`.
- Export: **4,928,231 bytes**, **180** files, **98.6%** of 5 MB.
  Composition: `docs/cycles` **1,381,995** (28.2%); `observations` **949,233**
  (19.4%) of which the pinned RSS body is **892,641**; repository root
  **711,433** (14.5%) of which `STATE.md` is **453,160**; `docs/state-archive`
  **297,471** (6.1%); reviewed source ≈ **1.51 MB** (≈31%).
- `docs/state-archive/` has **zero** consumers: no reference in `tools/*.py`,
  `run`, `AGENTS.md`, `ARCHITECTURE.md`, or `config/*.json`, and no pin.
- `STATE.md` is 6,983 lines, reverse-chronological. Region sizes:
  header/status **12,533**; v0.27 active execution **17,266**; appends
  v0.26→v0.22 **127,832**; appends v0.21→v0.14 **185,660**; reference §1–§7
  **43,411**; §8 v0.8 **38,688**; §9 v0.8.1 **27,770**.
- Checked boxes across the **exported** runbooks v0.12–v0.27 total **128**. The
  full `checklist-audit` figure is higher because v0.6–v0.11 remain audited while
  unexported. **E0 measures the real total; this runbook asserts no number for it.**

---

## Drafted gates

| Gate | Where | Hypothesis |
|---|---|---|
| **G1** [P1] | `tools/cycle_check.py:1479-1483`; `AGENTS.md:286-288` | **The per-row date requirement is vacuous whenever the column header carries a date.** Confirm by execution, not reading: blank every measured cell in a scratch runbook's deferred table, leave the dated header, and run `cycle_check`. **If it exits 0, the rule protects nothing it claims to protect.** Then state whether any governed row in the tree today would fail if the header token were removed. |
| **G2** [P1] | the four cycle-closing record blocks in v0.24–v0.27 | **Confirm all four record `2026-07-30`.** If so, state the maximum number of cycles that can close on one date and still be distinguishable by the current rule. **The answer is the size of the hole.** |
| **G3** [P1] | `tools/cycle_check.py:1707`; `shell/tests/test_cycle_check.py:1135-1148` | **The governed-row count is computed and discarded.** Confirm the call site binds nothing, that the only consumer is a test asserting a hardcoded `(2, 14)`, and that no floor exists. Then determine, by execution, what `cycle_check` reports when every trigger cell in both tables reads `none`. **Report the exit code.** |
| **G4** [P1] | `tools/export_check.py`; project-knowledge index | **Nothing bounds the export.** Confirm `export_check` asserts inclusion only, that `SOURCE_ROOTS` is `crates/apps/tools/shell` and `REQUIRED_PATHS` names seven paths, and that neither constrains `docs/cycles`, `observations`, or `docs/state-archive`. Re-measure export bytes and file count. **Record the 2,067-chunk / 2,000-limit observation with its date as the entering measurement.** |
| **G5** [P1] | `tools/cycle_identity.py:36-57`; `tools/cycle_check.py:1740-1788`; `tools/checklist_audit.py:18` | **Determine, by execution, what stops being checked if a closed runbook leaves `docs/cycles`.** Move one closed runbook to a scratch path in a throwaway clone, run `cycle-check` and `checklist-audit`, and record both exit codes and both counts. **Confirm specifically whether `audit_deferred`'s complete-progress-glob assertion still passes.** If it does, that is the silent no-op and the reason Step 5 touches export scope only. |
| **G6** [P2] | `crates/store/src/sqlite.rs:299-302`; `apps/cored/src/main.rs:2370-2373` | **`incoming_oldest_published_raw` trusts positional order.** `.iter().rev().find_map()` is correct only if the incoming window arrives newest-first, and the doc comment states the partition and before-insert preconditions but **not** the ordering one. The test asserts against `incoming.last()`, encoding the assumption on a fixture written newest-first. Determine what the field reports for a window that is not newest-first, and **state the blast radius honestly** — the field is observational and detection never fails the poll. |
| **G7** [P2] | `AGENTS.md:330`; `ARCHITECTURE.md §8` | **Two release-classification criteria are self-declared as enforced by nothing.** Enumerate them and their exact wording. **Do not implement anything.** Record whether the honest self-declaration is the correct posture or whether a bounded detector is available, and leave it for a later cycle to decide. |

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
corrected. **A rule that cannot fail has not passed.** Every step that tightens a
checker must first demonstrate the loosened checker accepting something it should
reject — the demonstration is the evidence, and a step that skips it has proven
nothing regardless of its exit code. And **shrinking the corpus must never shrink
the checked set**: any step that reduces what the reviewer reads must state, by
execution, what remains validated.

**Dependency gates.** Step 1 blocks everything. Step 2 blocks Step 3. Step 4
blocks Step 5. Step 6 is independent and may run any time after Step 1. Step 7 is
blocked by every preceding implementation step; Step 8 by Step 7.

**The two-commit ordering in Step 2 and Step 3 is mandatory and is not
stylistic.** Tightening a checker and updating the rows it governs in one commit
would combine a gate with its own fix. Splitting them leaves each commit green:
the data update satisfies both the old and new rule, and the checker change then
lands against already-conforming data. **A step that lands them together must
record that it did and why, and that record is a defect, not a note.**

### Cycle activation (before E0)

In a separate preparatory implementation/audit pair: confirm the worktree is
clean and record the measured refs **without asserting a literal `origin/main`
hash in `STATE.md`'s header**. Commit **only** this runbook at
`docs/cycles/TASKS-v0.28-EXECUTION.md` — including its `## Declared scope`
table — the `AGENTS.md` header moving the active declaration from v0.27 to v0.28,
and a new `docs/cycles/PROGRESS-v0.28.md`.

**This runbook's deferred table is already written in Step 2's target format** —
every governed row carries both an ISO date and the literal `v0.28`. That
satisfies the current rule (a date in the cell) and the tightened rule (date plus
active-cycle identity) **simultaneously**, so activation is green under the old
checker and Step 2 introduces no ordering hazard for this file. **The dates in
those cells are carried forward from v0.27 and are hypotheses until E0 rewrites
them with v0.28 measurements.** If the trigger-bearing row count changes, correct
the exact lifecycle count control and record it as a dated amendment.

### Global definition of done

Protected hashes exact; all **301** pins match; **golden 11/11 byte-identical**;
`./run version-check` green; zero rustc warnings on offline and net builds; all
Rust tests green; all shell tests green under Python 3.11 **and** 3.12; shell
results recorded as collected / passed / skipped with every skip named and
compared by `tools/test_population.py`, never as a bare `N/N`; clippy, fmt,
ShellCheck, floor byte-compilation, and locked Rust 1.78 green.

**`checklist-audit` is this cycle's corpus control.** Its total must not fall.
Steps 4 and 5 change what the reviewer reads and must not change what the
repository validates — **so if that number moves down by even one, stop and
record it as the finding.** The count rising is expected as v0.28 checks boxes.

---

## Deferred means deferred

| Deferred item | Unchanged trigger | Measured observation (cycle-identified) | v0.28 action |
|---|---|---|---|
| T7 robots single-flight | a second concurrent harvester | v0.28 · 2026-07-30 — E0 started no harvester; the prior bounded runtime remains sequential rather than concurrent | none — no step here starts a harvester |
| NEGATIVE-CACHE Decision B | a live transient robots outage for an admitted publisher while a usable last-known-good policy exists, plus operator authorization | v0.28 · 2026-07-30 — E0 observed no transient robots outage and no usable stale policy | none |
| Conditional GET (`ETag` / `If-Modified-Since`) | an operator-authorized cycle whose scope permits the `net` request path plus a live 304 observation | v0.28 · 2026-07-30 — E0 confirmed `crates/ingest/src/**` remains forbidden and `get_text` sends no validator | none — the gap stays recorded |
| `edgar:*` extension field mapping | an operator-authorized cycle permitting `crates/ingest/src/**` for mapping, with a connector review | v0.28 · 2026-07-30 — E0 confirmed ingest source remains forbidden and RSS bodies remain the form type alone | none |
| Live multi-publisher behaviour in one runtime | further origins beyond the two configured, or concurrency | v0.28 · 2026-07-30 — E0 issued no publisher request; v0.27's four-start sequential runtime remains the latest measurement | none — complete, do not re-exercise |
| Postgres / pgvector / multi-host seam | unchanged | v0.28 · 2026-07-30 — E0 re-ran the single-writer, single-host local matrix; no multi-host authority exists | none |
| A4 untrusted-shell boundary | a third-party/untrusted shell, or any claim HC1 is invariant under shell replacement | v0.28 · 2026-07-30 — E0 exercised only the first-party shell and made no replacement-invariance claim | none |
| L2 forced-command wrapper | an operator server session | v0.28 · 2026-07-30 — E0 opened no operator server session | none — remains scheduled |
| R3/R4 open-bottom coverage | a spelling outside registered vocabulary | v0.28 · 2026-07-30 — invariant-scan passed R3/R4 and E0 observed no outside spelling | none |
| Third configured publisher | a completed compliance review, then a separate admission decision | v0.28 · 2026-07-30 — E0 found no pending third-publisher review or admission | none |
| `v0.8.0` / `v0.10.2` publication | operator-authorized push of both exact annotated objects | v0.28 · 2026-07-30 — E0 received no authorization and moved no historical ref | none — **no historical ref touched** |
| `--skip-local-tag-verification` removal | both historical tags published plus a passing hosted full-history `cycle-check` without the flag | v0.28 · 2026-07-30 — E0 confirmed the historical tags remain unpublished and the flag remains | none — **the flag stays** |
| Manifest retention/indexing | 1 MiB manifest, or two consecutive `verify-artifacts` runs ≥1.00 s | v0.28 · 2026-07-30 — E0 measured 301 pins, 174,152 bytes, and 0.10 s / 0.10 s real; neither bound fired | **Step 1 — re-measure only** |
| Version literal in `app.py` | a cycle whose declared scope permits shell source changes | v0.28 · 2026-07-30 — E0 confirmed the literal remains present while `shell/intel_shell/**` is forbidden | none — recorded, not acted on |
| Release-classification criteria with no executed control | an operator decision that prose adjudication is insufficient | v0.28 · 2026-07-30 — G7 enumerated both semantic criteria and found no bounded detector from current authorities | **none — G7 records, Step 7 does not implement** |

---

## Step 1 · E0 — Rebuild the entering state and settle seven gates 🤖

**Objective.** Confirm HEAD is green and settle G1–G7. **Every assertion in
`## Entering state` is a hypothesis; measure each and report the measured value,
including where it differs from what is written above.**

**Decision gate.** If the worktree is dirty, if `main` is not exactly one commit
ahead of published `main` at `ddf08d20…`, or if any local gate fails at entry,
**record and stop.**

**Acceptance criteria.**

- All 20 `ci-local` jobs pass; invariant **12/46**; golden **11/11**; **301** pins
  verified twice with both real times recorded; both Python lanes reported as
  collected/passed/skipped via `tools/test_population.py`.
- G1 settled **by execution**: a scratch runbook with blanked measured cells and a
  dated header is run through `cycle_check`, and its exit code is recorded.
- G2 settled: the four closing dates are quoted from their four files.
- G3 settled **by execution**: the all-`none` scratch case is run and its exit code
  and reported counts are recorded.
- G4 settled: export bytes, file count, and per-area composition re-measured; the
  2,067-chunk observation recorded with its date.
- G5 settled **by execution in a throwaway clone**: both exit codes and both counts
  recorded before and after moving one closed runbook, with an explicit statement
  of whether `audit_deferred`'s completeness assertion still passed.
- G6 settled: the ordering precondition and its absence from the doc comment
  confirmed by path and line; the mis-ordered behaviour stated.
- G7 settled: both criteria enumerated verbatim with their exact locations.
- The deferred table's 15 rows are rewritten with **v0.28** measured observations.

**Done when** every gate carries a measured answer and the entering state is
either confirmed or corrected in `STATE.md`.

- [x] **E0**

---

## Step 2 · TRIGGER-IDENTITY — Bind freshness to the cycle, not the calendar 🤖

**Objective.** Replace a day-resolution discriminator with a cycle-scoped one, and
remove the header fallback that makes the per-row requirement optional.

**Decision gate.** If G1 exited **1** on the blanked-cell scratch case — that is,
if the header fallback does *not* actually make the rule vacuous — **stop and
record it.** The premise of this step would be refuted and the reviewer's
`cycle_check:1479-1483` reading would be the error.

**Two commits, in this order.**

1. **Data first.** Update the **two** trigger-bearing rows in `ARCHITECTURE.md`'s
   dated-dispositions table so each measured cell carries both a valid ISO date
   and the literal active cycle name, re-measured this cycle. This runbook's
   deferred table is already in that form. **This commit passes the current
   checker.**
2. **Rule second.** Require each governed row's **own** cell to contain a valid
   ISO date **and** the active cycle name resolved via
   `cycle_identity.resolve_cycle(root)`. **Delete the header fallback** from both
   `tools/cycle_check.py` and `AGENTS.md:286-288`. Gate on a new
   `TRIGGER_IDENTITY_FORWARD_BOUNDARY = (0, 28)`.

**`check_trigger_freshness` runs against the active runbook and `ARCHITECTURE.md`
only** — `cycle_check:1703-1712` sits inside the active-identity branch — **so no
closed runbook is retrofitted and none may be edited to satisfy this.** If any
closed document appears to need a change, that is the finding.

**Acceptance criteria.**

- Registered R12 gains planted `fail_before` controls proving, by execution, that
  the tightened checker rejects: **(a)** a governed row whose cell has no date
  while the header does; **(b)** a governed row naming a prior cycle
  (`v0.27`) instead of the active one. Each control's `expected_fail` is asserted
  against real output, not inspection.
- `invariant-scan` passes at its new derived rule/control totals, and the totals
  are reported as measured — **no expected count is hardcoded anywhere.**
- `cycle-check` passes on the real tree with both tables in the new format.
- Both commits are individually green and separate, and the progress record names
  both hashes.

**Done when** a row copied forward from v0.27 without re-measurement fails, and
the failure is demonstrated rather than argued.

- [x] **TRIGGER-IDENTITY**

---

## Step 3 · TRIGGER-FLOOR — Stop discarding the count 🤖

**Objective.** Make the governed-row population an enforced quantity instead of a
returned value nobody binds, and make dropping a deferred row require a reason.

**Decision gate.** Blocked by Step 2. If G3's all-`none` scratch case exited **1**
under the current code, the premise is refuted — **record and stop.**

**Acceptance criteria.**

- The call site at `tools/cycle_check.py:1707` **binds** the returned counts, and
  a zero population in either governed table is an error naming which table.
- `shell/tests/test_cycle_check.py:1135-1148` no longer asserts a hardcoded
  `(2, 14)`. The expected population is **derived** from the tables themselves;
  the test asserts the derivation agrees with the checker, not a literal pair.
  **A test that must be edited every time a row is added is the defect this step
  exists to remove.**
- **Carry-forward:** every trigger-bearing subject in the immediately prior
  cycle's runbook deferred table must either appear in the active table or be
  named in the active runbook with a dated completion. The prior runbook is
  resolved from `execution_runbooks()`, never hardcoded.
- The carry-forward rule is validated against the **real** v0.27 → v0.28
  transition, which legitimately drops rows: v0.27 dropped "First live SEC RSS
  harvest" and "Observation-byte manifest coverage" from v0.26. **If the rule
  cannot express a legitimate drop, the rule is wrong, not the history** —
  correct the rule and record that you did.
- A planted R12 control proves a silently dropped row is rejected.

**Done when** setting every trigger to `none`, or dropping a deferred row without
a completion, both fail — each demonstrated by execution.

- [x] **TRIGGER-FLOOR**

---

## Step 4 · DOC-SLIM — Shrink the corpus, not the checked set 🤖

**Objective.** Bring the export from 98.6% of 5 MB to roughly half, by **export
scope** plus **one sanctioned archival**, with zero loss of validated content.

**Decision gate.** If G5 showed that moving a closed runbook out of `docs/cycles`
does **not** silently reduce `cycle-check` or `checklist-audit` coverage, the
constraint below is over-tight — **record the measurement and stop for an operator
decision.** Do not relax it unilaterally.

**Four reductions. The first three touch `repomix.config.json` only.**

1. **The pinned SEC RSS body** (`observations/v0.25/feed-shape/sec-edgar-usgaap.rss.xml`,
   **892,641 bytes, 18.1%**) leaves the export. It is an `observation`-grade pin
   among 301; the manifest verifies the **repository** file and is untouched by
   export scope. Its analysis lives in the adjacent `.md` reports, which stay.
   **Keep every `observations/**/*.md`.**
2. **`docs/state-archive/**`** (**297,471 bytes, 6.1%**) leaves the export. G4
   confirms zero consumers and no pin: nothing executes against it.
3. **Cycle-document retention depth 3** — the active cycle and the two
   immediately prior. With v0.28 active that retains v0.26, v0.27, v0.28 and
   drops v0.12–v0.25 (**1,110,354 bytes**). **The glob is not trusted**: Step 5
   derives the expected retained set and proves the pattern, which is how a
   vacuous or over-broad pattern gets caught rather than assumed.
4. **`STATE.md` archival** to `docs/state-archive/STATE-through-v0.21.md`,
   byte-for-byte, following the `STATE-through-v0.13.md` precedent and its banner
   form at `STATE.md:5564`. The boundary is **reasoned, not arbitrary**: live
   `STATE.md` retains v0.22-forward, the era of the current R-CLOSE tagged-closing
   protocol, since `AGENTS.md` records that v0.15.6 and later use it while
   v0.15.5 and earlier used the prior shape. Archive appends v0.21→v0.14
   (**185,660 bytes**) and reference §8/§9, the v0.8 and v0.8.1 measured-execution
   records (**66,458 bytes**). Total **252,118 bytes**; `STATE.md` drops
   453,160 → **≈201,042**.

**Projected export ≈ 2,375,647 bytes — 2.38 MB, 47.5% of 5 MB.** These are
projections from the current tree; **Step 5 records the measured result and the
measured value governs.**

**Acceptance criteria.**

- `checklist-audit` total is **identical** before and after, and both figures are
  recorded. **This is the control: it must not fall by one.**
- `cycle-check`, `progress-check`, `verify-artifacts` (**301** pins), and
  `invariant-scan` all pass unchanged after the archival.
- The archived `STATE.md` content is proven byte-identical to what was removed, by
  a recorded hash comparison — **not by reading it.**
- `cycle_check`'s post-push record check still finds **exactly one** complete
  record for the current tag: `POST_PUSH_RECORD_RE` filters on
  `match.group(3) == tag`, so older records were never load-bearing, but **prove
  it rather than citing this sentence.**
- No file under `docs/cycles/` is edited, moved, or deleted.
- Export re-measured: bytes, file count, and per-area composition.

**Done when** the export is roughly half its entering size and every executing
check reports the same coverage it reported before.

- [x] **DOC-SLIM**

---

## Step 5 · EXPORT-BOUND — Give the corpus a ceiling that fails 🤖

**Objective.** Convert "the export stays reviewable" from an unexecuted property
into a measured one, and make Step 4's glob provable rather than trusted.

**Decision gate.** Blocked by Step 4. `run` is forbidden — everything here fits
behind the existing `python3 tools/export_check.py <export>` interface.

**Acceptance criteria.**

- `export_check` measures export bytes and **fails above a declared ceiling.**
  The ceiling is a declared bound in the house pattern of the 1 MiB manifest
  bound — it gets a row in `ARCHITECTURE.md`'s dated-dispositions table with a
  real trigger and a v0.28-identified observation, **which means Step 2's rule
  now governs it.** Set it with deliberate headroom above the measured
  post-Step-4 size; **state the chosen number and the reason for that number.**
- `export_check` **derives** the expected retained cycle-document set from
  `cycle_identity` plus the declared retention depth and asserts the export
  contains **exactly** that set — no more, no fewer. **Too many files catches a
  vacuous pattern; too few catches an over-broad one that dropped the active
  runbook.** The depth is one declared constant; the file list is never written
  down.
- `export_check` asserts the pinned wire-capture body and `docs/state-archive/**`
  are **absent** from the export.
- The existing derived-source and required-path checks are unchanged and still
  pass at their measured counts.
- `shell/tests/test_export_check.py` grows controls proving each new check fails
  when it should: over-ceiling, a retained cycle document missing, a dropped
  cycle document present, and each absence assertion violated. **Each control is
  demonstrated failing before it is demonstrated passing.**

**Done when** an export that has grown past the ceiling, or whose retention set
does not match the derived one, fails — **and the failure has been produced, not
described.**

- [ ] **EXPORT-BOUND**

---

## Step 6 · COVERAGE-ORDER — State or enforce the precondition 🤖

**Objective.** Remove an unstated ordering assumption from the coverage detector
shipped in v0.17.0.

**Decision gate.** Independent of Steps 2–5. `apps/cored/src/main.rs` and
`crates/ingest/src/**` are **forbidden**: this step reaches the store and its
tests, nothing else. If the fix appears to require the handler, **record and
stop** — that is a scope finding for the operator.

**The blast radius is bounded and must be stated that way.** The field is
observational, detection never fails the poll, and the ordering premise **is**
measured for the one pinned SEC body — "200 items / zero ascending timestamp
inversions". A mis-ordered window yields a **misreported diagnostic string**, not
a dropped filing and not data loss. **Do not inflate this into a correctness
defect in any record.** Per HC13, the fixture proves the state machine, not the
wire.

**Acceptance criteria.**

- Either the ordering precondition is **enforced** — derive the oldest boundary by
  the same ordering the archive uses, or detect the inversion and report it —
  **or** it is explicitly **stated** in the doc comment alongside the existing
  partition and before-insert preconditions. **Choose one and record why.**
- A test constructs a window that is **not** newest-first and asserts the
  resulting behaviour. `main.rs:2370-2373` asserts against `incoming.last()`,
  which encodes the assumption; the new test must not.
- Golden stays **11/11 byte-identical** and SEC identity stays **200 kept / 0
  dropped**. **If either moves, stop** — this step is not permitted to reach
  identity.
- If the derivation changes, the internal `/ingest` response **shape** is
  unchanged and no `/v1/*` value domain moves. Record both explicitly for Step 8.

**Done when** a mis-ordered window has a measured, recorded behaviour instead of
an assumed one.

- [ ] **COVERAGE-ORDER**

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
- Both shell lanes compared by `tools/test_population.py` with
  comparator-derived `collected`, `equivalent`, and `equivalent_passed`. **Every
  number written is the comparator's output, never transcribed from a log.**
- **301** pins verified; golden **11/11**.
- The hosted receipt directory is added by a dated `## Runbook amendments` entry
  in the same commit that first needs it. **This paragraph is notice, not
  permission**, and registering receipts requires
  `config/protected-artifacts.json`, which this cycle **forbids** — so if Step 7
  needs a manifest change, it must be an explicit dated amendment carrying the
  operator's authorization, not an assumed allowance.

**Done when** the candidate carries release-grade authenticated evidence.

- [ ] **RE-MEASURE**

---

## Step 8 · R-CLOSE 🧑🤖

**Objective.** Close v0.28 with an explicit, reasoned disposition.

**The drafted intent is `no-release`, and the reasoning is in `## Declared
scope`.** Nothing here moves a route, a response shape, a `/v1/*` value domain, a
dependency, a schema, or a public surface. **A cycle that improves only the
checkers is a legitimate no-release cycle**, and `AGENTS.md:61` records that
`no-release` is a real disposition under this contract.

**🧑 The operator's decision, and only the operator's.** Publication authorization
is a separate explicit act and is **not** implied by this runbook, by green
gates, or by Step 7's evidence. Two options, stated so neither is a default:

- **`no-release`** — close v0.28 on its own record. The three unpublished
  improvements ride into the next release naturally.
- **`release` at patch** — if the operator wants Step 6's corrected detector
  shipped now. **This requires a stated reason of its own**; it may not be
  inherited from "the gates are green."

**Acceptance criteria.**

- The closing record names `Cycle closed`, the dated `Release disposition`, and —
  if `release` — `Release` and `Release commit:` under R-CLOSE's two-commit
  tagged-closing protocol: untagged release parent, separate closing commit
  carrying the record, annotated tag over the closing commit.
- The declared-scope conditional permissions are reconciled: each is recorded as
  used or unused, by path.
- Every gate G1–G7 has a recorded measured answer, including G7's
  no-implementation outcome.
- The reviewer's refuted hypothesis in this runbook's header is preserved in the
  cycle record as a **reviewer error**, not restated as a finding.
- `STATE.md` records the measured export size against the new declared ceiling and
  the `checklist-audit` before/after control.

**Done when** the disposition is authorized, recorded, and measured.

- [ ] **R-CLOSE**

---

## Cycle checklist

- [ ] Worktree clean at entry; `main` one commit ahead at `ddf08d20…`, unpushed
- [ ] Every entering-state hypothesis measured and confirmed or corrected
- [ ] G1–G7 each carry a measured answer; G1, G3, and G5 answered **by execution**
- [ ] No closed cycle document edited, moved, or deleted
- [ ] `checklist-audit` total unchanged by Steps 4 and 5, both figures recorded
- [ ] `STATE.md` archival proven byte-identical by recorded hash
- [ ] Every new checker rule demonstrated **rejecting** before demonstrated passing
- [ ] No expected count hardcoded in any test added or edited this cycle
- [ ] Golden **11/11** byte-identical at every step
- [ ] SEC identity **200 kept / 0 dropped** unchanged
- [ ] **301** pins verified; manifest bounds re-measured against 1 MiB / 1.00 s
- [ ] Both Python lanes reported as collected/passed/skipped, comparator-derived
- [ ] Deferred table rows all carry v0.28-identified observations
- [ ] Reviewer error preserved as such in the cycle record

---

## Standing prohibitions

- **No closed cycle document is edited, moved, renamed, or deleted.** Not to
  shrink the export, not to satisfy a tightened rule, not for any reason.
- **No publisher request and no scheduler run.** The 600-second SEC clock has
  never run and this cycle does not authorize it.
- **No push to `main`, no tag, no ref creation or deletion** before Step 8's
  authorized action.
- **No edit to `run` or `tools/model_profiles.py`** — both are `authorization`
  pins.
- **No deletion of any pinned observation.** Export scope is not retention policy.
- **No hardcoded expected count** in any test written or edited this cycle. If a
  count must appear, it is derived from the artifact that defines it.
- **No rule ships without a demonstrated failing case.** A tightened checker whose
  rejection path was never executed is a claimed property, not a property.
- **No retraction is proposed** without a twice-verified measured false claim in
  an immutable published record. The count stands at three.

---

## Provenance of this draft

**Read, not measured:** the Codex v0.27 report; `STATE.md` header and v0.27
sections; `AGENTS.md` §§ on scope, freshness, R-CLOSE, and the cycle-ending
rhythm; `ARCHITECTURE.md` §§6–8; `TASKS-v0.27-EXECUTION.md` and
`TASKS-v0.26-EXECUTION.md`.

**Measured against the 2026-07-30 export, by path and line:** 12 rules and 46
`fail_before` controls parsed from `config/invariant-rules.json`; 301
`pinned_files[]` and their grade distribution (294 `evidence/`, 5
`observations/`, `run`, `tools/model_profiles.py`); 20 `ci-local` jobs derived
from `run:342-361`; seven executable hosted jobs derived from `.github/workflows/ci.yml`;
180 exported files; 264 top-level `test_` functions; version literals at
`apps/cored/Cargo.toml:3`, `shell/intel_shell/__init__.py:9`,
`shell/intel_shell/app.py:35`; 11 dated-disposition rows of which 2 are
trigger-bearing; 14 trigger-bearing runbook rows; `cycle_check.py:1479-1483`,
`:1707`, `:1740-1788`; `test_cycle_check.py:1147`; `cycle_identity.py:36-57`;
`checklist_audit.py:18`; `export_check.py` in full; `sqlite.rs:299-302`;
`main.rs:2370-2373`; four `Cycle closed: 2026-07-30` records; export composition
by area; `STATE.md` region sizes by line range; 128 checked boxes across exported
runbooks; zero `docs/state-archive` consumers across `tools/`, `run`,
`AGENTS.md`, `ARCHITECTURE.md`, and `config/`.

**Measured outside the repository:** project-knowledge indexing reported 2,067
chunks against a 2,000 limit on 2026-07-30.

**Asserted and not verified:** every line under `## Entering state`; all four
byte-reduction projections in Step 4 and the ≈2,375,647-byte total, which are
arithmetic on current file sizes and not post-change measurements; the claim that
older `STATE.md` post-push records are not load-bearing, which follows from
`POST_PUSH_RECORD_RE`'s tag filter but **is Step 4's to prove**.

**Reviewer error recorded at draft time.** The reviewer drafted a finding that T7
and NEGATIVE-CACHE Decision B were ungoverned prose residuals, then measured the
runbook deferred table and found both governed with dated observations. The
suspicion was withdrawn before delivery. It is recorded here because a reviewer
who reports only surviving hypotheses is reporting a filtered sample.
