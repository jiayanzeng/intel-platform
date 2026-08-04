# TASKS-v0.39-EXECUTION.md — make the review export tell the truth about itself

## Runbook amendments

**Cycle:** v0.39
**Entering release:** v0.17.5, closed locally at v0.38, unpublished; v0.17.2,
v0.17.3, and v0.17.4 published with post-push records
**Entering ref (hypothesis):** audit child `dd605acc…`, the immediate child of
closing commit `55045ae481ce8d1ef285522b3c0a57c91fe5cb54`
**Prior cycle:** v0.38 — closed, fully discharged; SEC EDGAR admitted under
Grant B; v0.17.4 published under Grant A
**Autonomy:** the standing `CYCLE_AUTONOMY_AUTHORITY` block governs. Every
decision is taken in §3 or delegated in §5 with a decision rule and a required
falsifier. One milestone step is **dormant by construction** and executes only
under Grant C, recording a dated not-granted observation otherwise. No operator
question is routed mid-cycle.

**This cycle is worth running with no grant issued.** Unlike v0.38, the
autonomous remainder is the whole point: Grant C is publication housekeeping,
and the substantive work needs no authorization at all.

Amendment entries, if any step's contract changes mid-cycle, are appended below
this line in the form `Step N — <what changed> — YYYY-MM-DD`.

---

## 0. Why this cycle exists

The review export is the only channel through which this project is
independently reviewed. Every acceptance criterion I write, every figure I
verify, every refusal I affirm rests on the export being a faithful image of a
commit. Two measurements say it currently is not, and a third says the channel
is closer to failing than any other governed quantity in the repository.

1. **It is not an image of a commit.** Three untracked working-tree files ride
   inside it at 43,124 bytes. `tools/export_check.py` verifies that every
   Git-tracked path under `crates`, `apps`, `tools`, and `shell` appears in the
   export. It never verifies the converse for anything else, so a file that
   exists only in the worktree enters the review artifact — and enters the
   governed figure that names a tree — and nothing reports it.
2. **It is the one quantity closest to its limit with no boundary inside
   failure.** `STATE.md` sits at 28.83% of its governed boundary and the
   protected manifest at 19.12%; both carry a boundary strictly inside failure
   and a dated `trigger-fired disposition:` requirement when crossed. The
   export sits at **93.30%**, and the only executed control is
   `export_bytes > MAX_EXPORT_BYTES`. Its deferral trigger reads "the export
   crosses the declared ceiling." Both fire at the failure, and the remedy
   behind them is a spent grant.
3. **Its exclusion set is a hardcoded parallel list.** The consequence has
   already landed: v0.38 captured three raw SEC wire bodies in one directory
   and excluded one of them, because `EXCLUDED_EXPORT_FILENAMES` names a single
   basename. The unexcluded HTML page occupies 44.89% of the remaining
   headroom.

The unifying shape is the project's own: a control that checks one direction
and reports success, a trigger that can only fire once acting is too late, and
a scope list asserted where it could be derived. Every remedy here fixes the
instance and makes the gap itself fail.

The arithmetic is the reason this needs no grant. The derived recovery —
retention advance plus the raw-wire-body class plus removing uncommitted bytes
— is on the order of 211,791 bytes, which clears the 2.5-cycle headroom target
that v0.37 missed without touching the ceiling, without a structural-archive
write, and without altering one observation byte.

---

## 1. Findings carried in

| # | Priority | Finding | Measured basis |
|---|---|---|---|
| F1 | **P1** | The delivered review export contains bytes that are in no commit | Three untracked amendment inputs total 43,124 bytes inside the export — 21.46% of remaining headroom. `check_export` derives required paths from `git ls-files` over `SOURCE_ROOTS = ("crates", "apps", "tools", "shell")` and asserts `sources - actual`; there is no `actual - tracked` assertion for any path outside those roots, so `docs/**`, `config/**`, `observations/**`, and `fixtures/**` are unguarded in that direction. |
| F2 | **P1** | The export ceiling is enforced only at the failure | `check_export` appends an error when `export_bytes > MAX_EXPORT_BYTES`; nothing fires below it. The deferral trigger is "the export crosses the declared ceiling." The delivered export is 2,799,094 of 3,000,000 — 93.30%, 200,906 bytes, 1.87 cycles at the derived denominator. Both governed in-repo artifacts already have the correct shape: a boundary inside failure plus a dated `trigger-fired disposition:` on crossing. |
| F3 | **P1** | The excluded raw-wire-body set is asserted, not derived | `EXCLUDED_EXPORT_FILENAMES = ("sec-edgar-usgaap.rss.xml",)` and `EXCLUDED_EXPORT_PREFIXES = ("docs/state-archive/",)` are literal tuples. `excluded_export_paths` reads `repomix.config.json` — correctly — but only looks for patterns whose basename equals a hardcoded name, so any other observation exclusion is neither required nor rejected. The v0.38 capture pinned three raw wire bodies in one directory; the 90,189-byte HTML page and the 2,621-byte robots body were not excluded while the RSS body was. |
| F4 | **P2** | The live egress path's safety properties are stated in no governing document | `harvest-sec`, `INTEL_CRAWLER_CONTACT`, and `refuse_protected_harvest` each appear **zero** times in `ARCHITECTURE.md` and `AGENTS.md`. The guards exist in `run` and have executing witnesses in `shell/tests/test_harvest_preflight.py`, but the invariant registry derives its rules from claims in the governing documents, so no rule can register against a guarantee that is never claimed. Three deferral rows — recurring scheduled run, multi-publisher runtime, third publisher — are queued behind that gap. |
| F5 | **P3** | A declared-scope forbid row is a pattern that matches nothing | The `docs/cycles/**` forbid row carries its exception as trailing prose inside the value cell. `literal_table_cell` only strips backticks when the cell both opens and closes with one, so the pattern compiles to `^\`docs/cycles/.*\`\ \(except…\)$` and matches no repository-relative path. **This is hygiene, not a hole:** `scope_changed_path_allowed` denies by default, so I ran both the vacuous and the clean pattern through the real function and they produce identical allow/deny outcomes on closed-cycle documents, the amendment inputs, and the active pair. The defect is that a line reads as an executed control and examines nothing — in the scope machinery, in a project whose core invariant is that a claimed property nothing executes is not a property. The prior runbooks carrying this row are immutable; the correction is forward. |

---

## 2. Grant C — exact required content, dormant until issued

Not assumed, not implied, not partially in force. Grant C is in force only when
the operator has issued it with at least the content below; Codex records the
grant text verbatim in the progress log before the gated step runs.

> Authorize publishing, once, non-force: `origin` `main` fast-forward to the
> exact v0.38 audit child, then annotated tag `v0.17.5` at its verified local
> object peeling to closing commit
> `55045ae481ce8d1ef285522b3c0a57c91fe5cb54`. No other ref moves.

Reviewer recommendation, for the operator's consideration: **issue it.** The
reasoning is the same one that published the first three releases — an
unpublished close is carried by an absence observation the lifecycle itself
records as unable to refresh — and the divergence count now stands at 1 within
the current epoch. Nothing in this runbook depends on it either way.

The exact ref identities are hypotheses at authoring time and are re-measured
immediately before the push. A mismatch is a stop, and the grant does not
transfer to different objects.

---

## 3. Decisions taken — do not re-litigate

If a measurement refutes a stated basis, record the refutation, stop that step,
continue with the rest, and surface it at handoff.

### DR15 — ACTIVATE precedes publication

Measured twice. v0.36 rejected a pre-activation post-push append; v0.38's
pre-activation entry point read the untracked runbook as an older open cycle
and failed with seven unchecked boxes plus one missing closing record, so its
activation fallback ran first. The ordering is settled by those two
measurements, not derived again at runtime: activate, then run the dormant
publication step in its numbered position.

### DR16 — the export images the checked tree

The property is decided: every path in the delivered export is Git-tracked at
the tree being exported, or is a declared exclusion validated against a derived
class. The mechanism for the three untracked amendment inputs is C15's.

**The standing prohibition is about the files, not the index.** "The three
untracked amendment inputs stay untouched" forbids editing, moving, renaming,
or deleting them. It does not forbid `.gitignore`, a Repomix exclusion, or
committing them as historical records. Codex is not to stall on this ambiguity;
it is resolved here.

### DR17 — the exclusion class is derived and cannot be enumerated

`tools/export_check.py` is scanned by `check_source_cycle_literals`, which
rejects any cycle literal in `tools/*.py`. An exact observation path contains
one. The hardcoded-tuple approach is therefore not merely against house
discipline — it is unsatisfiable in that file for any future capture. The class
must be derived from repository bytes. C16 owns the seam.

### DR18 — the ceiling does not move; a boundary is selected inside it

Moving an accepted ceiling is ask-first and is not requested. Selecting a value
inside an already-accepted boundary is squarely within the standing authority.
Step 4 selects a boundary strictly below 3,000,000 and gives it the same shape
the two in-repo artifacts already have. C17 owns the value and its derivation.

### DR19 — no structural-archive write; the shortfall rides the handoff

DR8 was spent at v0.37. `docs/state-archive/**` stays forbidden. If the derived
recovery does not reach the target, the exact shortfall is recorded and the
archival question rides the handoff. The ceiling is not moved and no archival
grant is assumed into existence.

### DR20 — version disposition rule, carried

DR13's three clauses govern unchanged, in precedence order: minor for a new
route or observable named surface; minor for any addition, removal, or
redefinition of a value in the domain of a serialized `/v1/*` field, adjudicated
against the R15 manifest diff rather than prose; otherwise patch. Export
tooling, invariant registration, and governing-document prose are none of these.
Expected: **patch v0.17.6** if a release ships; the reasoning is recorded either
way. A manifest diff showing domain movement is a stop under §4.

### DR21 — the v0.39 close defaults to unpublished-local

As DR10 and DR14 did: local annotated tag, fresh dated absence observation, and
the publication question rides the handoff. Grant C, if issued, covers v0.17.5
only and does not extend to any later release.

---

## 4. Retained gate and stop conditions

**Publishing `main` or any release tag beyond Grant C's exact refs requires
separate exact operator authorization.** Grant C, if issued, is spent once and
establishes no standing publication authority.

Stop-and-report conditions — halt the affected step, record the measurement,
continue unaffected work, surface at handoff:

1. A Grant C precondition fails, or its post-push hosted run fails.
2. A measurement indicates a **published** record contains a false claim. This
   now covers the v0.35 through v0.38 records on the published lineage.
3. A change would move an entitlement or licensing outcome for a configured
   subscription, a golden input, a protected database, an `observation`-grade
   byte, a structural-archive byte, or a dependency resolution.
4. Any `/v1/*` payload byte or manifest domain moves outside a declared
   disposition.
5. A change would move an accepted boundary or ceiling — including the
   3,000,000-byte export ceiling and both governed artifact byte boundaries —
   rather than select inside it.
6. Any live publisher request of any kind. Grant B was spent at v0.38 and this
   runbook requests no wire.
7. The derived exclusion class, once implemented, would exclude a path that is
   not a raw publisher wire body — or would fail to exclude one that is.

---

## 5. Codex-owned determinations

Measure, decide, record the reasoning and the falsifier. A recorded decision
naming what would have changed it is complete work; a question routed to the
operator inside this scope is not.

### C15 — disposition of the three untracked amendment inputs

Rule: the files are not edited, moved, renamed, or deleted. Among the
mechanisms that make the export image the tree, prefer the one introducing the
fewest hand-maintained entries and the fewest new failure modes; a mechanism
requiring a per-file literal in a scanned tool is excluded by DR17. Record which
mechanism was chosen, why, and what measurement would have selected differently.

### C16 — the derived raw-wire-body class seam

The class to be derived is "raw publisher response bytes captured as evidence,
pinned for integrity, and of no value as review source." One candidate seam,
offered as a starting measurement and not as the answer: each observation
capture directory carries a `.gitattributes` marking exactly its raw wire
bodies `binary`, and those marks are already load-bearing for byte preservation.

Rule: derived from repository bytes; no cycle literal in `tools/*.py`;
non-vacuous in **both** directions, proven by planted controls — a file the
derivation classifies as a raw wire body but which is absent from the exclusion
configuration must fail, and an exclusion configured for a file the derivation
does not so classify must also fail. A control that passes because the
derivation returned an empty set is the exact defect this cycle exists to close.
If the candidate seam turns out not to partition the current pins cleanly,
report that as the finding and derive from whatever does; do not widen the
class to make the seam fit.

### C17 — the export boundary value and its shape

Derive from a stated principle rather than picking a number — for example, a
margin that guarantees a stated number of cycles of headroom at the
checker-derived denominator, so the boundary moves when growth does. Hard
constraints: strictly below 3,000,000; the ceiling itself untouched; crossing
requires a dated `trigger-fired disposition:` in the same shape the two in-repo
artifact rows already use, so one mechanism governs all three. Record the
principle, the resulting value, and the falsifier.

### C18 — where the live-path guarantees are stated, and which rule registers them

Decide whether the guarantees belong in `ARCHITECTURE.md`, `AGENTS.md`, or both,
following the existing `source:` conventions of the registry; then decide
whether a new rule or an extension of an existing one is the honest home. Rule:
state only guarantees that an executable already enforces — a claim written to
be registered, rather than a claim the code already keeps, inverts the
discipline. If a guarantee Codex believes should hold turns out not to be
enforced, that is a finding for the handoff, not a claim to write down.

### C19 — anything E0 surfaces

Standing latitude to add rules and planted controls; none to add acceptance
criteria that nothing executes.

---

## 6. Dependency gates

- Step 2 executes only under Grant C; otherwise it records a dated not-granted
  observation and its box is checked over that observation — a recorded
  non-execution is the step's truthful completion.
- Steps 3, 4, 5, and 6 require **Step 1 complete**. Step 2 requires only
  Grant C.
- Step 4 requires Step 3, because the boundary is measured against an export
  whose contents are already truthful.
- Step 5 is independent of Steps 3 and 4 and may interleave.
- Step 6 runs only if production or operational code moved.
- Step 7 requires every prior box checked — executed, or truthfully
  not-granted — and every deferral row dated.

---

## Declared scope

The standing always-allowed set remains `STATE.md`, this runbook, and
`docs/cycles/PROGRESS-v0.39.md`. Release-authority precedence applies only at
R-CLOSE.

| Scope class | Path or value |
|---|---|
| `scope_version` | `1` |
| `disposition_intent` | `release` |
| `allow` | `AGENTS.md` |
| `allow` | `ARCHITECTURE.md` |
| `allow` | `docs/intel-platform-OPERATIONS.md` |
| `allow` | `tools/cycle_check.py` |
| `allow` | `tools/export_check.py` |
| `allow` | `tools/invariant_scan.py` |
| `allow` | `tools/checklist_audit.py` |
| `allow` | `tools/progress_check.py` |
| `allow` | `tools/domain_manifest.py` |
| `allow` | `tools/version_check.py` |
| `allow` | `config/invariant-rules.json` |
| `allow` | `config/checklist-exemptions.json` |
| `allow` | `config/protected-artifacts.json` |
| `allow` | `shell/tests/**` |
| `allow` | `crates/**/tests/**` |
| `allow` | `repomix.config.json` |
| `allow` | `.gitignore` |
| `allow` | `run` |
| `forbid` | `docs/state-archive/**` |
| `forbid` | `tools/model_profiles.py` |
| `forbid` | `tools/evidence_artifacts.py` |
| `forbid` | `.github/workflows/**` |
| `forbid` | `config/core.json` |
| `forbid` | `config/entities.json` |
| `forbid` | `config/schedule.json` |
| `forbid` | `config/subscriptions*.json` |
| `forbid` | `observations/**` |
| `forbid` | `fixtures/**` |
| `forbid` | `docs/cycles/**` |
| `release_authority` | `Cargo.toml` |
| `release_authority` | `Cargo.lock` |
| `release_authority` | `crates/*/Cargo.toml` |
| `release_authority` | `apps/*/Cargo.toml` |
| `release_authority` | `shell/intel_shell/__init__.py` |
| `release_authority` | `shell/intel_shell/app.py` |
| `release_authority` | `CHANGELOG.md` |
| `release_authority` | `README.md` |

`observations/**` and `config/schedule.json` return to **forbid**: Grant B was
spent at v0.38, no wire is requested, and this cycle changes how evidence bytes
are *selected for review*, never the bytes themselves. Any diff under
`observations/**` is a violation to report, not a scope question.
`docs/state-archive/**` stays forbidden per DR19. `crates/**/src/**`,
`apps/**/src/**`, and `shell/intel_shell/**` are absent from `allow` because no
step here needs production source; if a measurement says otherwise, that is a
stop-and-report, not a scope widening. `.gitignore` and `repomix.config.json`
are allowed for C15 and C16.

The `docs/cycles/**` forbid row is a **clean pattern**, corrected per F5. The
exception that used to ride inside its value cell as prose belongs here instead:
this runbook and `PROGRESS-v0.39.md` reach the worktree through the standing
status set, which `scope_changed_path_allowed` consults before it consults
forbid — so the clean pattern denies every closed-cycle document, including the
three amendment inputs, while the active pair passes. I measured both forms
against the real function; the outcomes are identical, which is why F5 is
hygiene rather than a hole.

---

## ACTIVATE

Ordered. The first action is not the declaration.

1. **Fill every observation cell in the deferral table first, in the worktree,
   before the activation commit.** The delivered draft ships 30 template cells.
   Each names v0.39 but carries no ISO date, so `check_trigger_freshness` will
   emit exactly 30 `requires a valid dated measured observation` errors against
   this runbook if it is committed unfilled. **That failure is predicted here,
   not discovered later**: it is the cost of my refusing to write a date onto a
   measurement I did not take, and it is discharged by measuring, never by
   relaxing the check or by copying v0.38's cells forward unchanged.
2. Move the `AGENTS.md` active-cycle declaration to v0.39; create
   `docs/cycles/PROGRESS-v0.39.md`; commit this runbook.
3. Advance review retention through the derived pattern so exactly the
   v0.38–v0.39 pairs are retained; if the derived value and
   `repomix.config.json` disagree, the disagreement is the finding — record it
   before changing either side.

**Acceptance criteria.** `cycle-check` resolves v0.39 from the declaration
alone and passes on its first post-activation run; the retention set derives to
exactly two cycles ending at the active one; the excluded boundary is reported
as a measurement rather than asserted; no deferral observation cell remains a
template, and each carries a real date and the active cycle name.

**Done when** the cycle is declared and every governed table is populated from
derivation.

---

## Step 1 · E0 — entering-state reconstruction

Every figure below is a hypothesis produced by reading a source export. No
repository command produced any of them. Confirm or refute against real bytes;
a refuted hypothesis is a finding, not an error to route around.

| # | Hypothesis | How to settle |
|---|---|---|
| H1 | Object graph: release parent `37f552c0…` → closing commit `55045ae481ce8d1ef285522b3c0a57c91fe5cb54` (immediate child) ← local annotated tag object `946bdc01…`; audit child `dd605acc…` is the closing commit's immediate child and current HEAD | `rev-parse`, `cat-file`, first-parent walk |
| H2 | Remote `main` is `a7d6c80e7e5ccd963e8ebb46ee054b30af88abb0` and is an ancestor of the audit child; `v0.17.2`, `v0.17.3`, `v0.17.4` present remotely; `v0.17.5` absent both locally-published and remotely | `ls-remote`, `merge-base --is-ancestor` — these are also Grant C preconditions and are recorded twice: here, and immediately before any push |
| H3 | `STATE.md` is 130,818 bytes against its 453,741 boundary; the protected manifest is 200,440 against 1,048,576; three post-push records and four unpublished-local observations exist, of which v0.17.5's is current | `wc -c`, `verify-artifacts`, anchored grep counts |
| H4 | Registry is 15 rules / 84 planted controls; exemptions 9; retractions 3; the closing checklist reads 302 / 3 / 293 / 293 / 9 | run the tools; do not copy any figure from a checker's own output where the construction can produce it independently |
| H5 | The delivered export is 2,799,094 bytes across 163 file entries, of which three are untracked amendment inputs totalling 43,124 bytes; `export-check` passes on that export today | export at the entering tree; compare the entry set against `git ls-files` |
| H6 | Whether any exported path outside `crates`, `apps`, `tools`, and `shell` is untracked is **unmeasured beyond those three files** — the full partition is the deliverable, not this row | enumerate every export entry against the tracked set |
| H7 | Four observation files are raw publisher wire bodies marked `binary` by their directory `.gitattributes`; two of the four are absent from the export and two are present | read each `.gitattributes`; intersect with the export entry set |
| H8 | Retention currently excludes through v0.36; advancing drops the v0.37 pair at 75,857 bytes, and the derived recovery available without any grant totals 211,791 bytes | measure at the activation tree, not from this table |
| H9 | The checker-derived margin denominator is the latest positive adjacent-cycle governed pair, currently +107,226 | read the derivation and run it |

Plus the standing entering measurements: `git status --porcelain` with its
expected untracked set stated exactly, full `./run ci-local`,
`invariant-scan --self-test`, both complete Python populations, and golden —
counts, not adjectives.

**Acceptance criteria.** Every hypothesis carries a dated verdict: confirmed,
refuted, or unmeasurable with a stated reason. H6's partition is enumerated in
full rather than spot-checked. No figure in this document is treated as
established by appearing here.

**Done when** dependent steps start from measurements rather than from this
runbook.

---

## Step 2 · PUBLISH-V17-5 — dormant, Grant C

**Objective.** Execute Grant C exactly, or record its absence truthfully.

If granted: record the grant text verbatim; measure every precondition
immediately before the push — `ls-remote` resolving `main` and confirming
`v0.17.5` absent, ancestry proven, the local annotated object peeling to the
granted closing commit; push the branch fast-forward and then the tag,
non-force, creating exactly those two ref movements; record the push-triggered
hosted run with its id, attempt, and conclusion; append the five-field post-push
record at column zero — the record pattern is line-anchored and an indented
append matches nothing; update the `STATE.md` status header, which is current
status rather than a dated measurement and would be a false claim if it still
said unpublished. The dated absence observation stays in place untouched as a
true historical measurement.

Irreversibility is accepted and one-directional, per the DR7 precedent. Once
pushed, the retraction bar applies and no later failure is grounds to delete or
force-move a ref. A failed post-push run makes the truthful state "published,
hosted verification failed" — recorded and stopped on, never unwound.

If not granted: one dated not-granted observation, and the absence observation
continues to carry the state.

**Acceptance criteria.** Either the published path passes `cycle-check` with the
fresh post-push record and the Step 1A planted controls unmodified — especially
the one proving a published release still requires its record — or the
not-granted observation is recorded with its date. `progress-check` passes.

**Done when** the records match the remote exactly, or the cycle truthfully
states that it awaits the grant.

---

## Step 3 · EXPORT-TRUTH — no property discharged by something that examines nothing

Per DR16, DR17, C15, and C16. F1, F3, and F5 are one defect wearing three
costumes: a check that runs in one direction, a class asserted where it could be
derived, and a pattern that matches nothing. Parts 3a and 3b move together —
neither ships alone, because one makes a silent gap into a hard failure and the
other keeps that failure satisfiable as captures accumulate. Part 3c is
independent and cheap.

**3a — only committed bytes.** Extend the export check so that every path in
the export is Git-tracked at the exported tree, or is a validated declared
exclusion. Planted control: an untracked file present in the worktree at export
time fails the check, anchored at the control site. Then resolve the three
amendment inputs per C15 without touching the files.

**3b — the raw-wire-body class, derived.** Replace `EXCLUDED_EXPORT_FILENAMES`
and `EXCLUDED_EXPORT_PREFIXES` with a derivation per C16. Planted controls in
both directions, per §5: an unexcluded member of the derived class fails, and a
configured exclusion outside the derived class fails. The existing guards that
already work — exact paths only, no glob metacharacters, the target must exist
— are kept and re-expressed over the derived class rather than discarded.

**3c — no vacuous declared pattern.** Reject a declared-scope pattern that
cannot match any repository-relative path — a backtick or unescaped whitespace
inside the compiled value is sufficient evidence, and Codex may choose a
stronger predicate. Planted control: the exact vacuous row this cycle corrected
fails, and the corrected row passes. The immutable prior runbooks carrying that
row are not edited; the check applies to the active declaration.

**Acceptance criteria.** No literal path list survives in `tools/export_check.py`
for either the excluded class or the required set; `check_source_cycle_literals`
passes over the edited file, which is the executable proof that no per-capture
literal was introduced; both planted controls fail before and pass after, each
anchored at a registered control site; the derivation is exercised against the
real pin population and its output is reported rather than asserted; every
export entry is partitioned into tracked, derived-exclusion, or defect, with the
partition exhaustive by construction; the vacuous-pattern control fails before
and passes after, and the active declaration compiles to patterns that each
match at least one candidate path or are reported; `./run ci-local` is clean.

**Done when** an uncommitted byte in the review export is a failing check, the
next publisher capture needs no edit to a tool to be classified correctly, and a
scope line that examines nothing cannot be written without failing.

---

## Step 4 · CEILING-TRIGGER — a boundary inside the failure

Per DR18 and C17. The export is the only governed quantity whose sole control
fires after the property has already failed. Give it the shape the other two
already have.

Select and register a boundary strictly inside 3,000,000, derived from a stated
principle rather than chosen; make crossing it require a dated
`trigger-fired disposition:` in the same form the in-repo artifact rows use;
and sharpen the deferral trigger from "the export crosses the declared ceiling"
to the boundary predicate, so the row can fire while acting is still possible.
The `Second STATE.md archival` row's trigger text is pinned by the checker and
is **not** edited — it already reads "the export ceiling trigger fires," so
sharpening the ceiling trigger propagates to it without touching its bytes.

Planted control: an export measured at or above the boundary without a dated
disposition fails, and the same export with one passes. A fix that makes the
failure vanish by making the rule reachable in fewer cases has quietly weakened
a real property; only that control distinguishes the two.

**Acceptance criteria.** The boundary is derived from a written principle and
the derivation is executable; the planted control fails before and passes after;
the trigger sharpening is recorded as a criterion correction with its reasoning,
not slipped in as an edit; the ceiling value itself is unchanged and that is
stated; the deferral row carries a dated observation naming the new predicate
and whether it has fired.

**Done when** the export can announce that it needs attention before it is too
late to give it any.

---

## Step 5 · WIRE-CONTRACT — state what the live path guarantees

Per F4 and C18. v0.38 admitted a publisher and shipped a bounded live egress
command whose guards are real and tested, and whose guarantees appear in no
governing document. The registry derives rules from claims; an unclaimed
guarantee cannot be registered, and three deferral rows about widening the
publisher surface are queued behind that gap.

State the guarantees the executables already keep — artifact preflight before
any network work, refusal to target a protected database, a required declared
contact before bind, a single configured source per invocation, fresh-path only
with no observation file consumed — in the governing documents per C18, then
register them with planted controls in the established form.

**Acceptance criteria.** Every stated guarantee names the executable that keeps
it and the control that proves it; no guarantee is written that an executable
does not already enforce, and any belief that outran the code is recorded as a
handoff finding instead; `invariant-scan --self-test` totals are stated;
`./run ci-local` is clean; zero hand-typed absolute finding-line fields.

**Done when** widening the publisher surface would have something to violate.

---

## Step 6 · RE-MEASURE — hosted, conditional

Runs only if production or operational code moved; edits to `run` and to the
checkers qualify. Evidence ref under the standing authority: under
`refs/heads/codex/`, naming the active cycle and a short commit id, with the
`ls-remote` absence pre-check recorded, non-force, exactly one ref created,
`main` and every tag untouched. Report run id, attempt, ref, and blocking
identity count. A pre-existing ref is a finding, not a detail.

If it does not run, record the dated reason and name which claims rest on local
execution only.

**Acceptance criteria.** Either a hosted run is reported with its id, attempt,
ref, and blocking identity result, and the remote readback shows `main` and
every tag unmoved — or the dated skip reason is recorded together with the
claims that consequently rest on local execution alone. The absence pre-check is
recorded either way.

**Done when** every claim in this cycle names the machine that witnessed it.

---

## Step 7 · R-CLOSE

The established two-commit tagged close, stated here so it needs no amendment:
release parent → closing commit carrying the record with this cycle's boxes
checked → local annotated tag if a release ships → **append-only audit child as
the immediate next commit**, carrying
`- cycle-ending review-export audit: closing_tree=…; bytes=…; audit_delta=…`
measured against the closing tree it follows. The audit child is the final
commit of v0.39 and the next cycle's entering ref. Every other criterion is
evaluated at the assembled closing worktree; the audit-field criterion alone at
the audit child. Deferring that field past the cycle remains prohibited.

**Acceptance criteria.**

- Dated disposition per DR20, naming any behaviour movement rather than letting
  the version imply its absence; the serialized-field clause adjudicated
  against the R15 manifest diff rather than prose.
- `version-check` passes with authorities and restatements counted.
- `checklist-audit` passes with all four figures stated and a non-zero v0.39
  line.
- The governed export row is bound; the audit child is present in the stated
  order; `audit_delta` reconciles against the closing tree.
- Per DR21: a fresh dated absence observation for any new release, and
  post-close `cycle-check` passes truthfully on the mixed state with the Step 1A
  planted controls unmodified.
- Every deferral row carries a dated v0.39 observation with its trigger
  unchanged except where Step 4 recorded a corrected criterion.
- `invariant-scan --self-test`, both Python populations, and golden: counts
  stated, zero hand-typed absolute finding-line fields.
- Headroom restated in bytes, percent, and cycles at the checker-derived
  denominator, against the target — and if the target is missed, the exact
  shortfall stated in the deferral row rather than absorbed into prose.
- No publication beyond Grant C's refs.

**Done when** the cycle is closed, audited, truthfully represented, and the
handoff written.

---

## Closing-record assembly template

*Assembled at Step 7 in the established field form. The release-parent
identity, evidence candidate, hosted run, governed export, artifact boundaries,
deferral disposition, divergence disposition, scope reconciliation,
publication boundary, checklist reconciliation, and golden reconciliation each
carry their measured values. This tree contains no annotated-tag-object field;
the local annotated tag targets the closing commit only after it exists.*

---

## Governed artifact byte-boundary authority

- governed artifact byte boundary: path=`STATE.md`; bytes=`453741`
- governed artifact byte boundary: path=`config/protected-artifacts.json`; bytes=`1048576`

**Carried forward byte-identically.** A change to either figure is an
architectural change requiring its own justification and operator
authorization. The 3,000,000-byte review-export ceiling remains separately
governed and is not moved by this cycle; Step 4 selects a boundary inside it.

---

## Deferred means deferred

The full carry-forward population from the immediately prior runbook, with every
trigger unchanged. **Each observation cell below is a template.** ACTIVATE
replaces each with a dated v0.39 measurement before any semantic acceptance, and
Step 7 replaces them again with close measurements. A template surviving into
any acceptance point is a defect, not an oversight.

| Deferred item | Unchanged trigger | Measured observation (cycle-identified) | v0.39 action |
|---|---|---|---|
| T7 robots single-flight | a second concurrent harvester | v0.39 · 2026-08-04 — No harvester has run in v0.39 and no second concurrent harvester appeared, so the trigger has not fired. | none |
| NEGATIVE-CACHE Decision B | a live transient robots outage for an admitted publisher while a usable last-known-good policy exists, plus operator authorization | v0.39 · 2026-08-04 — No publisher wire was touched and no Decision B authorization was issued; neither half of the combined trigger fired. | none |
| Conditional GET (`ETag` / `If-Modified-Since`) | an operator-authorized cycle whose scope permits the `net` request path plus a live 304 observation | v0.39 · 2026-08-04 — The net request path is outside declared scope and no live 304 was observed, so the combined trigger did not fire. | none |
| `edgar:*` extension field mapping | an operator-authorized cycle permitting `crates/ingest/src/**` for mapping, with a connector review | v0.39 · 2026-08-04 — The mapping path is outside declared scope and no connector review occurred, so the combined trigger did not fire. | none |
| Live multi-publisher behaviour in one runtime | further origins beyond the two configured, or concurrency | v0.39 · 2026-08-04 — Configuration still names the two publisher origins, arXiv and SEC; no further origin or concurrent runtime appeared. | none |
| First recurring scheduled SEC run | explicit operator authorization of a bounded scheduled window, separate from any cycle scope | v0.39 · 2026-08-04 — Grant C concerns publication only; no scheduled-window authorization was issued and no scheduled run executed. | none |
| Postgres / pgvector / multi-host seam | unchanged | v0.39 · 2026-08-04 — No Postgres, pgvector, or multi-host seam was introduced. | none |
| A4 untrusted-shell boundary | a third-party/untrusted shell, or any claim HC1 is invariant under shell replacement | v0.39 · 2026-08-04 — No third-party shell or replacement-shell HC1 claim appeared, so the trigger did not fire. | none |
| L2 forced-command wrapper | an operator server session | v0.39 · 2026-08-04 — No operator server session occurred, so the trigger did not fire. | none |
| R3/R4 open-bottom coverage | a spelling outside registered vocabulary | v0.39 · 2026-08-04 — The fresh registered scan passes **15/15 rules / 84 controls** and found no outside registered-vocabulary spelling. | none |
| `--features net` Rust 1.86 execution | a scoped cycle authorized to change evidence topology and an executable local or hosted lane that actually pins and runs the net path on Rust 1.86 | v0.39 · 2026-08-04 — Hosted run **30852480662** and the v0.17.5 release-parent local gate remain the most recent passing pinned Rust 1.86 lanes; workflow and evidence topology are scope-forbidden here. | none |
| GitHub attestation verifier version admission | the installed or proposed `gh attestation verify` version differs from the exact repository pin, or its accepted bundle/workflow contract changes | v0.39 · 2026-08-04 — The repository pin remains **2.96.0** and no accepted bundle/workflow contract changed, so the trigger did not fire. | none |
| Third configured publisher | a completed compliance review, then a separate admission decision | v0.39 · 2026-08-04 — No third-publisher compliance review or admission occurred. | none |
| `v0.8.0` / `v0.10.2` publication | operator-authorized push of both exact annotated objects | v0.39 · 2026-08-04 — Fresh remote readback finds both historical tag names absent and no authorization to publish them was issued. | none |
| `--skip-local-tag-verification` removal | both historical tags published plus a passing hosted full-history `cycle-check` without the flag | v0.39 · 2026-08-04 — Both historical tags remain unpublished and the hosted flag is unchanged, so the combined trigger did not fire. | none |
| Manifest retention/indexing | the manifest reaches its governed artifact byte boundary, or two consecutive clean `./run verify-artifacts` runs each take ≥1.00 s real | v0.39 · 2026-08-04 — The manifest is **200,440 / 1,048,576 bytes**; the latest complete checks match **3 artifacts / 339 pins** at **0.10 s / 0.11 s real**. Neither trigger clause fired. | none |
| Version literal in `app.py` | a cycle whose declared scope permits shell source changes | v0.39 · 2026-08-04 — Shell production source is absent from `allow`; release-authority precedence has not yet moved any literal in the open cycle. | Step 7 |
| Release-classification criteria with no executed control | an operator decision that prose adjudication is insufficient | v0.39 · 2026-08-04 — Fresh R15 derivation reports **0** public response-domain differences across **6 routes / 112 field occurrences**; R-CLOSE remains pending and no broader operator decision displaced the boundary. | Step 7 |
| Second `STATE.md` archival | the export ceiling trigger fires, or `STATE.md` reaches its governed artifact byte boundary | v0.39 · 2026-08-04 — State is **130,819 / 453,741 bytes** and the staged activation export is **2,774,259 / 3,000,000 bytes**; neither existing trigger fired. DR19 forbids archival this cycle. | none |
| Retention derivation across a version-family boundary | an active cycle whose name is not of the form `v0.<n>` — raising at `v1.0`–`v1.2`, silently under-excluding from `v1.3` onward | v0.39 · 2026-08-04 — The active cycle remains in the `v0.<n>` family, so the trigger did not fire. | none |
| Published-release divergence | the unpublished distance contains a measured runtime behaviour difference persisting across three consecutive closed cycles within the current publication epoch, or acquires any public-surface change | v0.39 · 2026-08-04 — The entering epoch count is **1** and fresh R15 derivation reports **0** public response-domain differences; neither trigger has fired before Grant C executes. | Step 7 |
| MSRV current-restatement membership | a current restatement of either Rust floor lands outside the registry without failing a check | v0.39 · 2026-08-04 — Fresh `version-check` derives **3** executable offline pins at 1.78, **22** offline-floor restatements, and **3** release restatements; all **585** currently tracked files are classified. | none |
| Retention arithmetic fallback | the retention formatter again permits an omitted retained set, or any live production or fixture caller supplies a set not derived by `expected_retained_cycle_paths` for that root | v0.39 · 2026-08-04 — The configured boundary is advanced for the derived v0.38–v0.39 retained pair; no omitted or non-derived retained set has appeared. | none |
| Optional cycle-ending audit disclosure | a closed cycle whose delivered export differs from its governed figure and which records no cycle-ending audit field | v0.39 · 2026-08-04 — The v0.39 audit field is required and reserved for the immediate Step 7 audit child, the first point at which the closing tree exists. | Step 7 audit child |
| License enum semantics | a second publisher requires an inexpressible license value | v0.39 · 2026-08-04 — No publisher work occurred and no inexpressible license value appeared. | none |
| Terms-level automated-access gate | a candidate's terms restrict beyond robots.txt | v0.39 · 2026-08-04 — No fresh terms were fetched; the pinned SEC determination remains the latest publisher-specific decision and no new restriction appeared. | none |
| Feed shape observation | an uncovered publisher feed shape | v0.39 · 2026-08-04 — No feed was fetched and no uncovered publisher feed shape appeared. | none |
| Threshold-authority limitation | a common dependency module or manifest edge appears between store and view | v0.39 · 2026-08-04 — The completed shared `intel-extract` seam remains unchanged and no new dependency module or manifest edge appeared. | none |
| ARCHITECTURE.md §8 / AGENTS.md R-CLOSE tag-mechanics duplication | the restatements diverge | v0.39 · 2026-08-04 — The two in-scope tag-mechanics restatements still agree before any v0.39 edit, so the trigger has not fired. | none |
| Review-export capacity | the export crosses the declared ceiling | v0.39 · 2026-08-04 — The staged activation export is **2,774,259 / 3,000,000 bytes**, leaving **225,741 bytes / 7.52% / 2.11 cycles** at the checker-derived +107,226-byte denominator. The existing ceiling trigger did not fire; Step 4 owns the corrected pre-failure boundary predicate. | Step 3 and Step 4 |

---

## Standing prohibitions

- No closed-cycle document, observation, or fixture edited; corrections are
  forward and dated. This now carries published-record weight for v0.35 through
  v0.38.
- No push beyond Grant C's refs and the standing evidence-ref authority. No
  force-push, ref deletion, or tag movement anywhere, ever.
- No wire request of any kind. Grant B was spent at v0.38.
- No expectation, anchor, or figure copied from a checker's own output where the
  construction can produce it independently.
- No acceptance criterion discharged by inspection where a registered
  self-testing rule with an executable `fail_before` can exist.
- No hardcoded scope list where the scope can be derived.
- No acceptance discharged by an executable whose witness set is empty.
- No retraction added without quoting the bar and obtaining an operator
  decision.
- The ask-first list is not widened by convenience; Grant C is a spent grant,
  not a precedent.
- The three untracked amendment inputs are not edited, moved, renamed, or
  deleted. Per DR16 this does not constrain how the export selects them.

---

## Cycle checklist

- [x] ACTIVATE
- [ ] E0
- [ ] PUBLISH-V17-5
- [ ] EXPORT-TRUTH
- [ ] CEILING-TRIGGER
- [ ] WIRE-CONTRACT
- [ ] RE-MEASURE
- [ ] R-CLOSE

*Box ids match the `PROGRESS-v0.39.md` entry ids exactly; the box-coverage rule
audits this runbook like any other.*

---

## Handoff

One report: each DR executed and whether any measurement refuted its basis; each
C-determination with its reasoning and its falsifier; every stop condition
triggered or an explicit none; the Grant C outcome, executed or not-granted with
its observation; the post-recovery headroom in bytes, percent, and cycles
against the target, with the exact shortfall if it was missed; and the v0.40
findings list — findings, not proposed acceptance criteria. A system that writes
its own criteria and grades itself against them has no independent witness,
which is the defect family this project has spent six cycles closing.

Then whichever operator questions remain open: publication of v0.17.5 if
Grant C was not issued, publication of any v0.39 release, and the standing
third-publisher question, which needs a completed compliance review before any
admission decision is even reachable.

---

## Provenance

**Measured on the delivered post-v0.38 export (2,799,094 bytes; 163 file
entries, of which one is a false positive produced by an f-string template
inside `shell/tests/test_export_check.py` and 162 are real paths):** the
`check_export` source set, required paths, ceiling comparison, and both literal
exclusion tuples; the `excluded_export_paths` validator and its basename
keying; `check_source_cycle_literals` and its scan set of `tools/*.py`, `run`,
and the workflow directory, which is what makes DR17's unsatisfiability claim a
measurement rather than a preference; the governed-margin derivation in
`tools/cycle_check.py`, including the latest-positive-adjacent-pair selection
that I formed and then refuted a hypothesis against; `GOVERNED_ARTIFACT_ROW_SPECS`
and the pinned trigger text for the `Second STATE.md archival` row; the
`Deferred means deferred` subject, trigger, and action column derivation and the
full 30-subject carry-forward population; `STEP_HEADING_RE`, the contract field
labels, and `check_active_step_value_criteria`; the registry at 15 rules and 84
planted controls counted from `config/invariant-rules.json` directly; the
protected manifest's 339 pins with their grades and the v0.38 admission chain;
the four observation `.gitattributes` files and their `binary` marks; the
Repomix retention pattern and both exact RSS exclusions; `.gitignore`; the five
release authorities at 0.17.5; and the three untracked amendment inputs at
16,833, 18,905, and 7,386 bytes.

**Executed against the checker's own code, not read from it:** I compiled the
v0.38 `docs/cycles/**` forbid value through the real `literal_table_cell` and
`scope_pattern_regex` and confirmed it matches no path, then ran both the
vacuous and the corrected pattern through the real `scope_changed_path_allowed`
and confirmed identical outcomes — which is what fixed F5 at P3 rather than P1.
I also ran this runbook's own step headings, contract-field blocks, deferral
table, and checklist through `STEP_HEADING_RE`, `BOLD_BLOCK_RE`,
`check_active_step_value_criteria`'s clause predicate, the subject/trigger/action
column derivation, and the 30-subject carry-forward comparison against the
committed v0.38 table: 7 step headings all matching, zero near-miss headings,
zero cross-step quantity clauses, 30 of 30 subjects carried with none added, and
every non-none action resolving to a real numbered step. The one predicted
failure is ACTIVATE's, and it is stated there rather than left to be found.

**What I could not measure and marked as hypotheses:** anything requiring `.git`
or the network — the object graph, remote refs, ancestry, and local tag
identity — which is why H1 and H2 exist and why Grant C's preconditions are
measured again at push time. The audit-child identity `dd605acc…` is taken from
the v0.38 report, not from an object I resolved. The 2,798,114-byte closing
figure reconciles with the delivered export to within 980 bytes, consistent with
the audit child's own `STATE.md` append, but I did not diff the two trees.

**What I did not do:** no repository command, no wire request, no test run, no
push. Every figure above is for Step 1 to confirm against real bytes.
