# TASKS-v0.40-EXECUTION.md — the corrective release, and a gate that can still act

## Runbook amendments

**Cycle:** v0.40
**Entering release:** v0.17.6, closed locally at v0.39, **permanently withheld**
— its tagged closing tree carries a disclosed publication-assertion defect and
must never be published; v0.17.2 through v0.17.5 published with post-push records
**Entering ref (hypothesis):** audit child `5885529a5f33e9c773f81d8d9434e47d77161d34`
**Prior cycle:** v0.39 — executed in full, all eight boxes checked, **not a
clean strict success**: R-CLOSE carries one recorded, immutable defect
**Autonomy:** the standing `CYCLE_AUTONOMY_AUTHORITY` block governs. Every
decision is taken in §3 or delegated in §5 with a decision rule and a required
falsifier. **No grant is requested and no step is dormant.** Publication rides
the handoff with the seam stated. No operator question is routed mid-cycle.

Amendment entries, if any step's contract changes mid-cycle, are appended below
this line in the form `Step N — <what changed> — YYYY-MM-DD`.

---

## 0. Why this cycle exists

v0.39 built three controls that worked. `export-check` now rejects an untracked
byte, derives the raw-wire-body class from `git check-attr` rather than a
literal tuple, and refuses a scope pattern that matches nothing; R16 registers
the bounded live-egress path with ten planted controls and names its own limits
honestly. The export came in at 2,743,797 bytes, byte-exact against the report.

And then R-CLOSE tagged a tree that fails the project's own gate.

The defect itself is small: the closing tree's `STATE.md` header still spent the
phrase `release commit` on the *previous* release's parent, so the freshness
assertion compared a historical object against the current one. The forward
correction in the audit child is right, the refusal to move the tag is right,
and the disclosure is complete. Codex handled an irreversible discovery
correctly.

What matters is why it was irreversible by the time anyone could see it.
`check_publication_status` resolves the annotated tag before it evaluates
anything, and returns when the tag cannot be resolved — which is precisely the
pre-tag state. The assertion that failed needs two inputs, the `STATE.md` header
and the runbook's `- **Release commit:**` field, and **both exist at the closing
worktree**. Nothing about it requires the tag. It sits below an early return
that the tag's absence triggers, so the earliest moment it can speak is the
moment after the tree it governs became immutable.

That is a new species of the family this project has spent six cycles closing.
Not a claim nothing executes, and not a trigger that fires too late — a control
whose *earliest possible evaluation point* is after the state it governs can no
longer be changed. It cannot prevent; it can only report a fact that is already
permanent.

So v0.40 has two jobs, in this order: make that failure impossible before
repeating the operation, then perform the operation. A corrective release closed
under a gate that has already proved it can fail early is worth something. A
corrective release closed under the same conditions that produced v0.17.6 is
worth nothing.

Three consequences ride along, and one of them is mine.

---

## 1. Findings carried in

| # | Priority | Finding | Measured basis |
|---|---|---|---|
| F1 | **P1** | The control governing the tagged closing tree cannot run before that tree is immutable | `check_publication_status` reaches `measured_object = git rev-parse <tag>`, and on `None` appends "publication verification unavailable" and returns. The freshness loop over `TAGGED_CLOSING_STATE_REF_ASSERTIONS` sits below that return. Its inputs are the `STATE.md` header paragraph and `RELEASE_COMMIT_RE` over the runbook's closing record — neither needs a tag. The assertion is tag-independent; only its position is not. |
| F2 | **P1** | The lifecycle has no way to say "withheld" | `UNPUBLISHED_LOCAL_CLOSE_RE` hardcodes the status literal `unpublished-local-close`, the only representable non-published state. v0.17.6's record is byte-shaped identically to v0.17.5's while that release was merely awaiting a grant. The distinction between "awaiting authorization" and "must never be authorized" exists only in prose — and prose is what a future cycle or operator reads past. |
| F3 | **P1** | The most consequential open item in the project has no deferral row | v0.39's `Deferred means deferred` table carries the same 30 subjects as v0.38's, adds none, and has no `Deferred completions` section. The permanently withheld release is tracked by narrative alone, so no dated-observation machinery re-examines it each cycle. Every other open item in this project earns a trigger and a dated observation; this one did not. |
| F4 | **P2** | The attention boundary I specified last cycle moves the wrong way | `boundary = 3,000,000 − (2 × denominator)`, and the denominator is the latest **positive** adjacent-cycle governed delta — a single sample. A quiet cycle shrinks the reserve. Worked example at the current figures: growth of +60,000 yields a governed field of 2,789,600 against a recomputed boundary of 2,880,000 → `clear`; growth of +107,226 yields 2,836,826 against 2,785,548 → `fired`. The same byte count can be either verdict depending on the *previous* cycle's size rather than on current risk, and at the limit a near-zero-growth cycle sets the boundary to within a few bytes of the ceiling. C17 asked for a boundary that moves when growth does; I did not ask which direction. |
| F5 | **P2** | A closed-release tag that can never reach a remote breaks hosted full verification | `check_release_record` requires `git rev-parse <tag>` to resolve for every closed tagged-closing release whenever `verify_local_tag_refs` is true, appending "annotated tag cannot be resolved for the tagged-closing protocol" otherwise. v0.17.6's tag exists locally and can never exist on `origin`, so a hosted `cycle-check` run without `--skip-local-tag-verification` can never pass again. That makes the second clause of the `--skip-local-tag-verification` removal trigger unsatisfiable until F2 is fixed. **Stated as a hypothesis:** I read the code path but could not run Git, and E0 settles it. |

---

## 2. No grant is requested

There is no dormant step. v0.17.6 must never be published, so there is no
entering publication to authorize, and v0.17.7 does not exist until R-CLOSE
creates it. Publication rides the handoff, which states both readings of the
seam rather than resolving it here — advancing `main` past v0.17.6's closing
commit would place a superseded, forward-corrected tree inside published
history without publishing it as a release, and reasonable people can weigh
that differently. That is the operator's call to make on a full statement, not
mine to pre-empt in a runbook that also builds the gate.

---

## 3. Decisions taken — do not re-litigate

If a measurement refutes a stated basis, record the refutation, stop that step,
continue with the rest, and surface it at handoff.

### DR22 — v0.17.6 is permanently withheld

The tag `v0.17.6`, its object, and its target are never moved, deleted,
re-pointed, or published. Codex's recovery judgment is adopted as the record:
the safe path is a new corrective release, not tag movement. This is settled
and is not reopened by a later cycle finding the defect cosmetic, by the
accumulation of unpublished closes, or by any argument that the audit child's
correction makes the tagged tree acceptable. It does not: a checkout of that tag
fails `cycle-check`, and the project's release artifact is the tagged tree.

### DR23 — the gate lands before the operation repeats

Step 2 completes before Step 6 creates any tag. A corrective release closed
under the conditions that produced v0.17.6 would prove nothing, and would risk
producing a second immutable defect in the cycle whose purpose is to recover
from the first. This is a hard ordering, not a preference.

### DR24 — the stop-condition set was incomplete, and that gap is mine

My v0.39 §4 protected **published** records from measured false claims and said
nothing about immutable local ones. A tagged closing tree becomes immutable the
instant the tag is created, and from that instant it deserves the same
protection. Codex withheld publication and disclosed the defect on its own
judgment; the contract did not require either. §4 below is corrected. I record
this as an author-side omission rather than an execution gap, because the
correct behaviour happened despite the contract rather than because of it.

### DR25 — a correction to the attention basis may only widen the reserve

Whatever estimator Step 4 selects, the resulting reserve is greater than or
equal to the current 214,452-byte reserve, measured at the same tree. A change
that makes the alarm quieter is a weakening wearing the costume of a fix, and
the planted control in Step 4 is what distinguishes the two. The 3,000,000-byte
ceiling itself does not move.

### DR26 — version disposition rule, carried

DR20's three clauses govern unchanged, in precedence order: minor for a new
route or observable named surface; minor for any addition, removal, or
redefinition of a value in the domain of a serialized `/v1/*` field, adjudicated
against the R15 manifest diff rather than prose; otherwise patch. Checker and
lifecycle work is none of these. Expected: **patch v0.17.7**; the reasoning is
recorded either way. A manifest diff showing domain movement is a stop under §4.

### DR27 — the v0.40 close defaults to unpublished-local

As DR10, DR14, and DR21 did. The new release closes with a local annotated tag
and a fresh dated observation. Whether that observation uses the existing status
or the one Step 3 introduces is Step 3's own outcome, applied to itself.

---

## 4. Retained gate and stop conditions

**Publishing `main` or any release tag requires exact operator authorization,
and none is in force.** No push beyond the standing evidence-ref authority.

Stop-and-report conditions — halt the affected step, record the measurement,
continue unaffected work, surface at handoff:

1. A measurement indicates a **published** record contains a false claim. This
   covers the v0.35 through v0.39 records on the published lineage.
2. **A measurement indicates an immutable local record contains a false claim.**
   A tagged closing tree is immutable from tag creation; an append-only
   observation, a pinned artifact, and a closed-cycle document are immutable
   from commit. Per DR24 this is new, and it is the condition v0.39 needed.
3. Creating a tag whose tree has not passed the Step 2 gate, or discovering
   after tag creation that it would not have. Either is a stop before any
   further ref work.
4. A change would move an entitlement or licensing outcome, a golden input, a
   protected database, an `observation`-grade byte, a structural-archive byte,
   or a dependency resolution.
5. Any `/v1/*` payload byte or manifest domain moves outside a declared
   disposition.
6. A change would move an accepted boundary or ceiling — including the
   3,000,000-byte export ceiling and both governed artifact byte boundaries —
   rather than select inside it. Per DR25, widening the attention reserve inside
   the fixed ceiling is selection, not movement.
7. Any live publisher request of any kind. No wire is requested this cycle.
8. Any proposal that would move, delete, re-point, or publish the `v0.17.6` tag.

---

## 5. Codex-owned determinations

Measure, decide, record the reasoning and the falsifier. A recorded decision
naming what would have changed it is complete work; a question routed to the
operator inside this scope is not.

### C20 — where the tag-independent assertions are evaluated

Partition `check_publication_status` into what needs the tag and what does not,
derived by reading each assertion's inputs rather than by assuming my partition
is right. Hoist the tag-independent part above the tag-resolution early return.

Rule: the pre-tag path reports its own verdict distinctly, so an operator can
tell "the tag does not exist yet and everything checkable is correct" from "the
tag does not exist yet and something is already wrong." The former is the normal
pre-tag state and must not become a failure; the latter must. If the partition
turns out to be smaller than F1 claims — if the freshness assertion depends on
the tag in some way I did not see — report that as the finding and hoist
whatever genuinely is independent.

### C21 — the withheld-release record form

A closed release that is permanently withheld needs a representable state
carrying its reason. Follow the existing labelled-field precedent
(`POST_PUSH_RECORD_RE`, `UNPUBLISHED_LOCAL_CLOSE_RE`) rather than inventing a
prose form.

Rule: the new state is not reachable by default and not a synonym for the
existing one — a release recorded as withheld must be treated by every consumer
as settled rather than pending, including the handoff surface. It must also
carry the information F5 needs: that this release's tag is expected to exist
locally and never remotely, so hosted verification can be correct rather than
merely skipped. Recording a release as withheld is a decision with consequences;
the form must make an unreasoned withholding fail.

### C22 — the attention denominator estimator

Select an estimator that does not shrink the reserve when a cycle is quiet — a
maximum over a stated recent window, a stated multi-cycle mean, or a floor
beneath the single-sample value are all candidates; measure which the recorded
governed series actually supports rather than picking on elegance. The governed
margin and the attention boundary consume the same denominator today, so decide
explicitly whether they should continue to and record why.

Rule: DR25 binds the outcome. The planted control is the one that matters — a
recorded series in which a quiet cycle would previously have raised the boundary
must fail before and pass after.

### C23 — anything E0 surfaces

Standing latitude to add rules and planted controls; none to add acceptance
criteria that nothing executes.

---

## 6. Dependency gates

- Steps 2, 3, and 4 require **Step 1 complete**; they are otherwise independent
  and may interleave.
- **Step 6 requires Step 2 complete.** Per DR23 no tag is created until the
  pre-tag gate exists and has demonstrated an early failure on a planted case.
- Step 5 runs only if operational or production code moved; checker changes
  qualify.
- Step 6 requires every prior box checked and every deferral row dated.

---

## Declared scope

The standing always-allowed set remains `STATE.md`, this runbook, and
`docs/cycles/PROGRESS-v0.40.md`. Release-authority precedence applies only at
R-CLOSE. Every pattern below is a literal repository glob, per the control
v0.39 registered.

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
| `allow` | `tools/version_check.py` |
| `allow` | `config/invariant-rules.json` |
| `allow` | `config/checklist-exemptions.json` |
| `allow` | `config/protected-artifacts.json` |
| `allow` | `shell/tests/**` |
| `allow` | `repomix.config.json` |
| `allow` | `run` |
| `forbid` | `docs/state-archive/**` |
| `forbid` | `tools/model_profiles.py` |
| `forbid` | `tools/evidence_artifacts.py` |
| `forbid` | `tools/domain_manifest.py` |
| `forbid` | `.github/workflows/**` |
| `forbid` | `config/core.json` |
| `forbid` | `config/entities.json` |
| `forbid` | `config/schedule.json` |
| `forbid` | `config/subscriptions*.json` |
| `forbid` | `observations/**` |
| `forbid` | `fixtures/**` |
| `forbid` | `crates/**` |
| `forbid` | `apps/**` |
| `forbid` | `docs/cycles/**` |
| `release_authority` | `Cargo.toml` |
| `release_authority` | `Cargo.lock` |
| `release_authority` | `crates/*/Cargo.toml` |
| `release_authority` | `apps/*/Cargo.toml` |
| `release_authority` | `shell/intel_shell/__init__.py` |
| `release_authority` | `shell/intel_shell/app.py` |
| `release_authority` | `CHANGELOG.md` |
| `release_authority` | `README.md` |

This cycle touches lifecycle checkers and their tests, and nothing else.
`crates/**` and `apps/**` are forbidden outright: no step here needs production
Rust, and release-authority precedence still carries the manifests at R-CLOSE.
`tools/domain_manifest.py` moves to forbid — R15's baseline is exact and this
cycle has no business near it. `docs/cycles/**` is a clean pattern; this runbook
and `PROGRESS-v0.40.md` reach the worktree through the standing status set,
which is consulted before forbid, so every closed-cycle document and every
untracked amendment input stays denied. `observations/**`, `config/schedule.json`,
and `docs/state-archive/**` remain forbidden; DR8 and Grant B are spent.

---

## ACTIVATE

Ordered. The first action is not the declaration.

1. **Fill every observation cell in the deferral table first, in the worktree,
   before the activation commit.** The delivered draft ships 31 template cells.
   Each names v0.40 but carries no ISO date, so `check_trigger_freshness` emits
   one error per row against this runbook if it is committed unfilled. **That
   failure is predicted here, not discovered later**: it is the cost of my
   refusing to write a date onto a measurement I did not take, and it is
   discharged by measuring, never by relaxing the check or by copying v0.39's
   cells forward unchanged.
2. Move the `AGENTS.md` active-cycle declaration to v0.40; create
   `docs/cycles/PROGRESS-v0.40.md`; commit this runbook.
3. Advance review retention through the derived pattern so exactly the
   v0.39–v0.40 pairs are retained; if the derived value and
   `repomix.config.json` disagree, the disagreement is the finding — record it
   before changing either side.

**Acceptance criteria.** `cycle-check` resolves v0.40 from the declaration alone
and passes on its first post-activation run; the retention set derives to
exactly two cycles ending at the active one; the excluded boundary is reported
as a measurement rather than asserted; no deferral observation cell remains a
template, and each carries a real date and the active cycle name.

**Done when** the cycle is declared and every governed table is populated from
derivation.

---

## Step 1 · E0 — entering-state reconstruction

Every figure below is a hypothesis produced by reading a source export. No
repository command produced any of them, and the defective tree is not in the
export at all — only HEAD is — so everything about the tagged tree's content
comes from Codex's report and must be settled against real bytes. A refuted
hypothesis is a finding, not an error to route around.

| # | Hypothesis | How to settle |
|---|---|---|
| H1 | Object graph: release parent `acfa801102197ce2d94adaa5a14a3ad102893549` → closing commit `7c9305f01219412048ec75236f2bf1e61112c178` (immediate child) ← local annotated tag object `66ee2cbbe374b99722bec49b8176571777aaa899`; audit child `5885529a5f33e9c773f81d8d9434e47d77161d34` is the closing commit's immediate child and current HEAD | `rev-parse`, `cat-file`, first-parent walk |
| H2 | Remote `main` is `dd605acc037da405fa6b2b5366b09349c330c194` and is an ancestor of HEAD; `v0.17.2` through `v0.17.5` present remotely; `v0.17.6` absent remotely and present locally | `ls-remote`, `merge-base --is-ancestor`, local `show-ref` |
| H3 | **The defect reproduces exactly.** A checkout of tag `v0.17.6` fails `cycle-check` with a publication-assertion freshness error, and the header at that tree spends the phrase `release commit` on `37f552c0c326098bdcf8f19de7eac19670d74680` | check out the tag in a detached worktree; run the checker; read the header. Whether that tree *also* asserts the correct parent elsewhere is **unmeasured** and decides whether the tree is self-contradictory or simply wrong |
| H4 | F1's partition holds: the freshness assertion's inputs are the header and the runbook release-commit field, and the early return at unresolvable tag is what makes it unreachable pre-tag | read the call graph; construct a worktree with no tag and confirm which assertions are reached |
| H5 | F5 holds: a `cycle-check` run with `verify_local_tag_refs` true, in a checkout lacking the local `v0.17.6` tag, fails on that tag | simulate the hosted condition; run it |
| H6 | Registry 16 rules / 100 controls; exemptions 9; retractions 3; the v0.39 closing checklist reads 303 / 3 / 294 / 294 / 9 | run the tools; derive rather than copy any figure a checker prints |
| H7 | The delivered export is 2,743,797 bytes across 158 entries, all tracked; `STATE.md` 152,809 of 453,741; manifest 200,440 of 1,048,576; attention boundary 2,785,548 with the export 41,751 below it | export at the entering tree; run `export-check` and read its reported state |
| H8 | The derived denominator remains +107,226 because the v0.38→v0.39 governed delta is negative, and F4's worked example follows from that | read the derivation; recompute both branches |

Plus the standing entering measurements: `git status --porcelain` with its
expected untracked set stated exactly, full `./run ci-local`,
`invariant-scan --self-test`, both complete Python populations, and golden —
counts, not adjectives.

**Acceptance criteria.** Every hypothesis carries a dated verdict: confirmed,
refuted, or unmeasurable with a stated reason. H3 is settled by executing
against the real tag rather than by citing the prior cycle's record, and its
unmeasured half is answered. No figure in this document is treated as
established by appearing here.

**Done when** dependent steps start from measurements rather than from this
runbook.

---

## Step 2 · PRE-TAG-GATE — a control that can still act

Per F1, DR23, and C20. The assertion that caught v0.17.6 is correct and stays
strict. What changes is when it is allowed to speak.

Hoist the tag-independent publication assertions above the tag-resolution early
return so they evaluate at a closing worktree with no tag present, and give
`R-CLOSE` an explicit gate that runs them at the assembled closing tree before
any tag is created.

**Planted controls, and the second is the one that matters.** First: a closing
worktree whose header spends the assertion phrase on the prior release's parent
fails, with no tag in existence. Second: the normal pre-tag state — correct
header, no tag yet — **passes** the hoisted portion rather than being swallowed
by a blanket unavailability verdict. A gate that fails every pre-tag worktree
would satisfy the first control and be worthless, and only the second
distinguishes the real fix from that one.

**Acceptance criteria.** The hoisted partition is derived from each assertion's
inputs and recorded, not asserted from this document; both planted controls fail
before and pass after, each anchored at a registered control site; the pre-tag
verdict is distinguishable from the post-tag verdict in the checker's own
output; the strictness of the existing assertion is unchanged, proved by a
control reproducing the v0.39 header shape and failing under the new form;
`./run ci-local` is clean.

**Done when** a closing tree that would produce a defective tag fails while it
is still amendable.

---

## Step 3 · WITHHELD-STATE — say the thing that is true

Per F2, F5, DR22, and C21. The project's records currently present a
permanently withheld release exactly as they present one awaiting a grant. That
is how a future cycle publishes a defective tag — not through malice, but by
reading a handoff that says the same words it said the last four times, when the
answer those times was yes.

Introduce the withheld state per C21, carrying its reason and the local-only tag
expectation; apply it to v0.17.6; and make hosted verification correct for a
withheld release rather than merely skipped, so F5's obstacle is removed rather
than documented.

**Planted controls.** A withheld record without a reason fails. A release
recorded as withheld that is nonetheless presented as a pending publication
question fails. A hosted-shaped verification over a withheld release passes
without the skip flag, and the same verification over a release that is merely
unpublished still requires its tag.

**Acceptance criteria.** The new state is a labelled-field form following the
existing precedent; it is not reachable by default and is not a synonym for the
existing status, proved by a control; v0.17.6's record carries it with the
disclosed defect as its reason; the handoff surface treats a withheld release as
settled; `invariant-scan --self-test` totals are stated; `./run ci-local` is
clean.

**Done when** no reader of these records can mistake a permanent refusal for a
pending question.

---

## Step 4 · ATTENTION-BASIS — the alarm may not get quieter as the room fills

Per F4, DR25, and C22. I specified this boundary one cycle ago and specified it
wrong in one direction: the reserve is two times a single-sample denominator, so
a quiet cycle raises the boundary toward the ceiling and a near-zero-growth
cycle very nearly disables it.

Select an estimator per C22, bounded by DR25: the reserve at the same tree does
not shrink.

**Planted control.** A recorded governed series containing a quiet cycle — under
which the current derivation would raise the boundary — fails before and passes
after. The control must exercise the series, not a hand-written boundary value;
a control that asserts a constant proves nothing about the estimator.

**Acceptance criteria.** The estimator is derived from the recorded governed
series and its choice is recorded with a falsifier; the reserve at the entering
tree is greater than or equal to its current value, stated as a comparison; the
ceiling is unchanged and that is stated; whether the governed margin continues to
share the denominator is decided explicitly rather than inherited; the planted
control fails before and passes after; the deferral row carries a dated
observation naming the corrected predicate and whether it has fired.

**Done when** a quiet cycle cannot make the export look safer than it is.

---

## Step 5 · RE-MEASURE — hosted, conditional

Runs if operational or production code moved; checker changes qualify. Evidence
ref under the standing authority: under `refs/heads/codex/`, naming the active
cycle and a short commit id, with the `ls-remote` absence pre-check recorded,
non-force, exactly one ref created, `main` and every tag untouched. Report run
id, attempt, ref, and blocking identity result. A pre-existing ref is a finding,
not a detail.

If it does not run, record the dated reason and name which claims rest on local
execution only.

**Acceptance criteria.** Either a hosted run is reported with its id, attempt,
ref, and blocking identity result, and the remote readback shows `main` and
every tag unmoved — or the dated skip reason is recorded together with the
claims that consequently rest on local execution alone. The absence pre-check is
recorded either way.

**Done when** every claim in this cycle names the machine that witnessed it.

---

## Step 6 · R-CLOSE — the corrective release

Per DR23 this step does not begin until Step 2's gate exists. The established
two-commit tagged close, with one addition that is the point of the cycle:

release parent → assembled closing worktree → **run the Step 2 pre-tag gate and
require it to pass** → closing commit → local annotated tag → **append-only
audit child as the immediate next commit**, carrying
`- cycle-ending review-export audit: closing_tree=…; bytes=…; audit_delta=…`
measured against the closing tree it follows. The audit child is the final commit
of v0.40 and the next cycle's entering ref. Every other criterion is evaluated at
the assembled closing worktree; the audit-field criterion alone at the audit
child.

The `STATE.md` header is written so that the assertion phrase names this
release's parent and nothing else, and historical objects are named in wording
that does not spend the phrase. That discipline is now enforced rather than
remembered.

**Acceptance criteria.**

- The pre-tag gate passed at the assembled closing worktree, before the tag
  existed, and its verdict is recorded.
- **A checkout of the new annotated tag passes `cycle-check`.** This is the
  criterion v0.39 could not claim, it is evaluated after the tag exists, and it
  is the cycle's actual deliverable.
- Dated disposition per DR26, naming any behaviour movement rather than letting
  the version imply its absence; the serialized-field clause adjudicated against
  the R15 manifest diff rather than prose.
- `version-check` passes with authorities and restatements counted.
- `checklist-audit` passes with all figures stated inline in the closing record
  and a non-zero v0.40 line. A closing record that points elsewhere for its own
  figures is not a closing record.
- The governed export row is bound; the audit child is present in the stated
  order; `audit_delta` reconciles against the closing tree.
- Per DR27 a fresh dated observation for the new release, in whichever form Step
  3 established for a release that is unpublished but not withheld.
- Every deferral row carries a dated v0.40 observation with its trigger
  unchanged except where Step 4 recorded a corrected criterion.
- `invariant-scan --self-test`, both Python populations, and golden: counts
  stated, zero hand-typed absolute finding-line fields.
- Headroom restated in bytes, percent, and cycles at the derived denominator,
  against the target and the corrected reserve.
- No publication of any kind.
- No process instruction left inside a dated record. v0.39's R-CLOSE record
  carries the sentence about fields being replaced before commit; a dated record
  states what was measured, not what remains to be done.

**Done when** the release this cycle exists to produce is closed, tagged, and
provably clean at its own tag.

---

## Closing-record assembly template

*Assembled at Step 6 in the established field form, with every figure stated
inline. The release identity, evidence candidate, hosted run, governed export,
artifact boundaries, attention state, deferral disposition, divergence
disposition, scope reconciliation, publication boundary, checklist
reconciliation, golden reconciliation, and the pre-tag and post-tag gate
verdicts each carry their measured values. This tree contains no
annotated-tag-object field; the local annotated tag targets the closing commit
only after it exists.*

---

## Governed artifact byte-boundary authority

- governed artifact byte boundary: path=`STATE.md`; bytes=`453741`
- governed artifact byte boundary: path=`config/protected-artifacts.json`; bytes=`1048576`

**Carried forward byte-identically.** A change to either figure is an
architectural change requiring its own justification and operator
authorization. The 3,000,000-byte review-export ceiling remains separately
governed and is not moved by this cycle; Step 4 adjusts only the reserve
selected inside it, and only upward.

---

## Deferred means deferred

The full carry-forward population from the immediately prior runbook with every
trigger unchanged, plus one new subject per F3. **Each observation cell below is
a template.** ACTIVATE replaces each with a dated v0.40 measurement before any
semantic acceptance, and Step 6 replaces them again with close measurements. A
template surviving into any acceptance point is a defect, not an oversight.

| Deferred item | Unchanged trigger | Measured observation (cycle-identified) | v0.40 action |
|---|---|---|---|
| `v0.17.6` publication, tag movement, or deletion | any proposal to publish, move, re-point, or delete the `v0.17.6` tag, its object, or its target | v0.40 · 2026-08-04 — Local annotated object `66ee2cbbe374b99722bec49b8176571777aaa899` still peels to `7c9305f01219412048ec75236f2bf1e61112c178`; fresh remote readback contains no direct or peeled v0.17.6 ref. No proposal arose; DR22 permanently withholds it. | Step 3 |
| T7 robots single-flight | a second concurrent harvester | v0.40 · 2026-08-04 — No harvester ran and no second concurrent harvester appeared; the trigger did not fire. | none |
| NEGATIVE-CACHE Decision B | a live transient robots outage for an admitted publisher while a usable last-known-good policy exists, plus operator authorization | v0.40 · 2026-08-04 — No wire was touched, no transient outage was observed, and no Decision B authorization was issued; the combined trigger did not fire. | none |
| Conditional GET (`ETag` / `If-Modified-Since`) | an operator-authorized cycle whose scope permits the `net` request path plus a live 304 observation | v0.40 · 2026-08-04 — The declared scope forbids `crates/**` and live wire; no live 304 was observed. | none |
| `edgar:*` extension field mapping | an operator-authorized cycle permitting `crates/ingest/src/**` for mapping, with a connector review | v0.40 · 2026-08-04 — `crates/ingest/src/**` is forbidden and no connector review occurred; the trigger did not fire. | none |
| Live multi-publisher behaviour in one runtime | further origins beyond the two configured, or concurrency | v0.40 · 2026-08-04 — Configuration still has two network publisher origins; no runtime or concurrency occurred. | none |
| First recurring scheduled SEC run | explicit operator authorization of a bounded scheduled window, separate from any cycle scope | v0.40 · 2026-08-04 — No scheduled-window authorization was issued and no scheduled SEC run executed. | none |
| Postgres / pgvector / multi-host seam | unchanged | v0.40 · 2026-08-04 — No Postgres, pgvector, second-writer, or multi-host seam was introduced. | none |
| A4 untrusted-shell boundary | a third-party/untrusted shell, or any claim HC1 is invariant under shell replacement | v0.40 · 2026-08-04 — No third-party shell appeared and no stronger shell-replacement claim was made; A4 remains open. | none |
| L2 forced-command wrapper | an operator server session | v0.40 · 2026-08-04 — No operator server session occurred; L2 remains scheduled. | none |
| R3/R4 open-bottom coverage | a spelling outside registered vocabulary | v0.40 · 2026-08-04 — The registered scan passed R3 and R4 within their declared vocabularies at **16/16 rules / 100 controls**; no outside spelling was found. | none |
| `--features net` Rust 1.86 execution | a scoped cycle authorized to change evidence topology and an executable local or hosted lane that actually pins and runs the net path on Rust 1.86 | v0.40 · 2026-08-04 — Workflow and evidence topology remain forbidden; the latest pinned lane remains hosted run `30875346351`, where the explicit Rust 1.86 success and 1.85 refusal identities passed. | none |
| GitHub attestation verifier version admission | the installed or proposed `gh attestation verify` version differs from the exact repository pin, or its accepted bundle/workflow contract changes | v0.40 · 2026-08-04 — No verifier pin, bundle shape, workflow, or accepted contract changed. | none |
| Third configured publisher | a completed compliance review, then a separate admission decision | v0.40 · 2026-08-04 — No third-publisher compliance review or admission occurred. | none |
| `v0.8.0` / `v0.10.2` publication | operator-authorized push of both exact annotated objects | v0.40 · 2026-08-04 — Fresh remote readback contains neither historical tag; no publication authorization was issued. Local v0.8.0 remains an annotated object and local v0.10.2 remains available for E0's exact identity check. | none |
| `--skip-local-tag-verification` removal | both historical tags published plus a passing hosted full-history `cycle-check` without the flag | v0.40 · 2026-08-04 — The historical remote-tag premise is still false; E0 and Step 3 will measure the additional withheld-release obstacle and its removal. | Step 3 |
| Manifest retention/indexing | the manifest reaches its governed artifact byte boundary, or two consecutive clean `./run verify-artifacts` runs each take ≥1.00 s real | v0.40 · 2026-08-04 — The manifest is **200,440 / 1,048,576 bytes**; two complete checks matched **3/3 artifacts / 339 pins** in **0.11 s / 0.09 s real**. Neither trigger clause fired. | none |
| Version literal in `app.py` | a cycle whose declared scope permits shell source changes | v0.40 · 2026-08-04 — Production shell source is absent from `allow`; no literal moved at activation. Release-authority precedence is reserved for Step 6. | Step 6 |
| Release-classification criteria with no executed control | an operator decision that prose adjudication is insufficient | v0.40 · 2026-08-04 — R15 reports **0 differences across 6 routes / 112 field occurrences**; DR26 provisionally selects patch, and no broader operator decision displaced the prose boundary. | Step 6 |
| Second `STATE.md` archival | the export ceiling trigger fires, or `STATE.md` reaches its governed artifact byte boundary | v0.40 · 2026-08-04 — Entering State is **152,810 / 453,741 bytes**. The pre-activation worktree export is not an acceptance measurement: it truthfully fails at **2,788,376 bytes** because the v0.40 runbook is untracked, outside active retention, and above the old attention boundary; ACTIVATE owns the corrected active-tree measurement. | none |
| Retention derivation across a version-family boundary | an active cycle whose name is not of the form `v0.<n>` — raising at `v1.0`–`v1.2`, silently under-excluding from `v1.3` onward | v0.40 · 2026-08-04 — The active candidate remains in the `v0.<n>` family; the version-family trigger did not fire. | none |
| Published-release divergence | the unpublished distance contains a measured runtime behaviour difference persisting across three consecutive closed cycles within the current publication epoch, or acquires any public-surface change | v0.40 · 2026-08-04 — Published v0.17.5's epoch remains at **0**; permanently withheld v0.17.6 never resets it, activation adds no runtime behavior, and R15 reports no public-surface movement. | Step 6 |
| MSRV current-restatement membership | a current restatement of either Rust floor lands outside the registry without failing a check | v0.40 · 2026-08-04 — `version-check` derives **3 pins / 22 current offline-floor restatements / 3 current release restatements**, classifying all **587** tracked files; no unregistered current restatement appeared. | none |
| Retention arithmetic fallback | the retention formatter again permits an omitted retained set, or any live production or fixture caller supplies a set not derived by `expected_retained_cycle_paths` for that root | v0.40 · 2026-08-04 — The entering authority derives exactly v0.38–v0.39; ACTIVATE advances it to v0.39–v0.40. No omitted or non-derived caller appeared. | none |
| Optional cycle-ending audit disclosure | a closed cycle whose delivered export differs from its governed figure and which records no cycle-ending audit field | v0.40 · 2026-08-04 — Step 6 requires and reserves the audit field for the immediate audit child; it is evaluated only after the cycle-closing commit exists. | Step 6 audit child |
| License enum semantics | a second publisher requires an inexpressible license value | v0.40 · 2026-08-04 — No publisher work occurred and no inexpressible license value appeared. | none |
| Terms-level automated-access gate | a candidate's terms restrict beyond robots.txt | v0.40 · 2026-08-04 — No fresh terms were fetched; the pinned SEC operator-owned determination remains standing. | none |
| Feed shape observation | an uncovered publisher feed shape | v0.40 · 2026-08-04 — No feed was fetched and no uncovered shape appeared. | none |
| Threshold-authority limitation | a common dependency module or manifest edge appears between store and view | v0.40 · 2026-08-04 — No dependency or manifest edge moved; the existing shared `intel-extract` seam remains in place. | none |
| ARCHITECTURE.md §8 / AGENTS.md R-CLOSE tag-mechanics duplication | the restatements diverge | v0.40 · 2026-08-04 — Entering review finds both documents still agree on the two-commit tagged close; Step 2 must preserve that agreement while moving the pre-tag evaluation point. | none |
| Review-export capacity | the export meets or exceeds the executable two-governed-growth-cycle attention boundary | v0.40 · 2026-08-04 — The pre-activation worktree measured **2,788,376 bytes** against the old **2,785,548-byte** boundary and therefore fired, while also failing its untracked/out-of-retention checks. ACTIVATE records the tracked v0.39–v0.40 result; Step 4 must widen the current **214,452-byte** reserve and record the corrected predicate. | Step 4 |

---

## Standing prohibitions

- The `v0.17.6` tag, its object, and its target are never moved, deleted,
  re-pointed, or published. Per DR22 this is permanent.
- No closed-cycle document, observation, fixture, or immutable local record
  edited; corrections are forward and dated.
- No push beyond the standing evidence-ref authority. No force-push, ref
  deletion, or tag movement anywhere, ever.
- No tag created before the Step 2 gate has passed at that tree.
- No wire request of any kind.
- No expectation, anchor, or figure copied from a checker's own output where the
  construction can produce it independently.
- No acceptance criterion discharged by inspection where a registered
  self-testing rule with an executable `fail_before` can exist.
- No hardcoded scope list where the scope can be derived.
- No acceptance discharged by an executable whose witness set is empty.
- No change that reduces the reach of an existing control in order to make a
  failure disappear.
- No retraction added without quoting the bar and obtaining an operator
  decision.
- The three untracked amendment inputs are not edited, moved, renamed, or
  deleted; the v0.39 export mechanism already keeps them out of review.

---

## Cycle checklist

- [x] ACTIVATE
- [ ] E0
- [ ] PRE-TAG-GATE
- [ ] WITHHELD-STATE
- [ ] ATTENTION-BASIS
- [ ] RE-MEASURE
- [ ] R-CLOSE

*Box ids match the `PROGRESS-v0.40.md` entry ids exactly; the box-coverage rule
audits this runbook like any other.*

---

## Handoff

One report: each DR executed and whether any measurement refuted its basis; each
C-determination with its reasoning and its falsifier; every stop condition
triggered or an explicit none; the H3 verdict including its currently unmeasured
half; the pre-tag and post-tag gate verdicts at R-CLOSE; the reserve before and
after Step 4; and the v0.41 findings list — findings, not proposed acceptance
criteria.

Then the publication question, stated once and in full, because it is now more
than a yes or no. Publishing `main` and `v0.17.7` would advance the branch past
v0.17.6's closing commit, placing a superseded and forward-corrected tree inside
published history while never publishing it as a release. One reading is that
this is ordinary — published history always contains superseded states, and the
project's own machinery supersedes by append rather than edit. The other is that
the retraction bar should not be approached casually, and that a defective tree
entering published history deserves an explicit decision rather than an
inherited one. The handoff states both, the exact refs, and the measured
divergence position; it does not recommend.

---

## Provenance

**Measured on the delivered post-v0.39 export (2,743,797 bytes / 158 file
entries, byte-exact against the reported closing figure):** the early return at
`measured_object is None` in `check_publication_status` and the position of the
`TAGGED_CLOSING_STATE_REF_ASSERTIONS` loop below it, which is F1's whole basis;
that assertion's pattern and its two inputs; `UNPUBLISHED_LOCAL_CLOSE_RE`'s
hardcoded status literal; the `resolved_tag is None` branch in
`check_release_record` and its dependence on `verify_local_tag_refs`, which is
F5's basis; `EXPORT_ATTENTION_HEADROOM_CYCLES = 2` and the
`3,000,000 − (2 × denominator)` derivation, from which F4's worked example was
computed directly; the `git check-attr -z binary` exclusion derivation and the
`untracked_export_errors` control that v0.39 built, both confirmed present; the
new declared-scope pattern-population control that rejects a backtick or
whitespace, which is why this runbook's table is clean; the registry at 16 rules
and 100 planted controls counted from `config/invariant-rules.json` directly,
with R16 carrying 10 and honestly naming its own `CORE_DB` override limit; nine
exemptions and three retractions; `STATE.md` at 152,809 and the manifest at
200,439 against their boundaries; the v0.39 deferral table at 30 subjects with
none added and no completions section, which is F3's basis; and the disclosure
records in `STATE.md` and `PROGRESS-v0.39.md`.

**Verified unchanged against the v0.38-era checker:** `STEP_HEADING_RE`,
`DEFERRED_HEADING`, `AMENDMENTS_HEADING`, `AMENDMENT_ENTRY_RE`,
`CONTRACT_FIELD_LABELS`, `SCOPE_HEADING_RE`, `SCOPE_CLASSES`,
`STEP_REFERENCE_RE`, the quantity-clause predicate, and the pinned
`Second STATE.md archival` trigger text — so this runbook's shape is checked
against the checker that will actually scan it, not against last cycle's.

**What I could not measure and marked as hypotheses:** anything requiring `.git`
or the network — the object graph, remote refs, ancestry, local tag identity,
and **the content of the tagged tree at `7c9305f…`, which is not in the export
at all.** Everything I say about the defective header comes from Codex's report,
which is why H3 requires executing against the real tag rather than citing the
record. F5 is a code-path reading, not a run.

**What I did not do:** no repository command, no wire request, no test run, no
push. Every figure above is for Step 1 to confirm against real bytes.
