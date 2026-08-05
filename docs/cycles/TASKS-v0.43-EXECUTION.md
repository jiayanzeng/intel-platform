# TASKS-v0.43-EXECUTION.md — the reviewer's output is now a first-order capacity term

## Runbook amendments

**Cycle:** v0.43
**Entering release:** v0.17.9, closed locally and unpublished; v0.17.8 and
v0.17.7 published; v0.17.6 permanently withheld
**Entering ref (hypothesis):** audit child `6f07edf84c3ce40f1ef4c9e97e5d101242490243`
**Prior cycle:** v0.42 — closed clean. R17 landed with the offline guard and the
historical-shape guard both intact.
**Autonomy:** the standing `CYCLE_AUTONOMY_AUTHORITY` block governs. Every
decision is taken in §3 or delegated in §5 with a decision rule and a required
falsifier. Three milestone steps are **dormant by construction** and execute only
under their named grants, recording dated not-granted observations otherwise. No
operator question is routed mid-cycle.

**This runbook is deliberately shorter than its predecessors**, for the reason
F1 gives. Amendment entries are appended below this line in the form
`Step N — <what changed> — YYYY-MM-DD`.

Step 3 — halted after the committed diff exposed an undeclared tools/version_check.py change; checkbox reopened and scope left unchanged — 2026-08-05
Step 2 — LEDGER gains sub-part 2c, the ledger floor-literal classification, under the amended scope — 2026-08-05
Step 2 — LEDGER gains sub-part 2d, reopened-task progress correspondence, under a second scope authority — 2026-08-05

---

## 0. Why this cycle exists

v0.42 discharged R17 exactly as specified, including both halves that mattered:
the offline path reports a visible non-failing `unavailable` verdict, and the
control requires every v0.42-forward published cycle's expected `main` commit to
carry that cycle's own export audit **without retroactively rejecting the
historical cross-cycle shape**. `ls-remote` now executes inside `cycle_check.py`.
The published side of this project is a measurement.

Capacity is the standing problem, and this cycle it acquired an uncomfortable
answer. Measuring the per-file growth returns this ordering:

`docs/cycles/TASKS-v0.42-EXECUTION.md` **+63,834** · `STATE.md` +27,406 ·
`docs/cycles/PROGRESS-v0.42.md` +24,831 · `tools/cycle_check.py` +13,157

The largest single line item in the growth of the artifact that constrains review
is the runbook I wrote. The retained cycle-document set is 178,284 bytes, 6.52%
of the export, and my runbooks have run 56,135 → 59,795 → 63,834 across three
cycles. `STATE.md`, the protected manifest, and the export total each carry a
governed byte boundary with a trigger and a dated disposition. The cycle-document
set carries none, and it is the component growing fastest and the one produced by
the reviewer rather than by the code.

Underneath that sits a mechanical cause. The deferral ledger holds 31 subjects.
Each cycle re-materializes all of them in the runbook and again in the progress
log, and retention keeps two cycles, so the export carries the same ledger four
times — 11,124 bytes of TASKS-v0.42 and 11,294 of TASKS-v0.41 for the tables
alone. Carry-forward compares runbook to runbook, which is the only reason the
prior cycle's runbook has to be in the export at all.

So the chain is: consolidate the ledger, and the prior runbook stops being needed
for review; give the cycle-document set a boundary, and the reviewer's own output
becomes governed like everything else. Neither needs a grant.

That will not clear the attention boundary. Nothing available will — §6 states
the arithmetic for every combination, including both grants together. This cycle
does the work that makes the remaining choice cheap and states the numbers so the
choice can be made once rather than deferred a fifth time.

---

## 1. Findings carried in

| # | Priority | Finding | Measured basis |
|---|---|---|---|
| F1 | **P1** | The reviewer's output is the largest term in export growth, and nothing measures it | Per-file deltas across the two delivered exports: `TASKS-v0.42-EXECUTION.md` +63,834, ahead of `STATE.md` +27,406 and `PROGRESS-v0.42.md` +24,831. Retained cycle documents total **178,284 bytes / 6.52%** of the export. Delivered drafts ran 44,490 → 47,826 → 46,977 and the committed runbooks 56,135 → 59,795 → 63,834, so execution expands a draft by roughly a third as observations are filled in. Three governed byte boundaries exist — `STATE.md` at 453,741, the manifest at 1,048,576, the export at 3,000,000 — and none covers this set. |
| F2 | **P1** | The deferral ledger is written four times into every export | 31 subjects, re-materialized in the runbook and the progress log, retained two cycles. The runbook tables alone measure 11,124 bytes in v0.42 and 11,294 in v0.41. `check_deferred_trigger_carry_forward` compares the active runbook against the immediately prior runbook, which is what forces the prior runbook to stay in the review export; the checkers themselves read `docs/cycles/` from the worktree, not from the export. |
| F3 | **P1** | Capacity: no available combination clears the boundary | Delivered export 2,732,434 bytes, reconciling with the reported 2,730,969-byte closing tree plus a 1,465-byte audit-child append, and the governed 2,710,728 plus the audited +20,241. Headroom **267,566 bytes, 8.92%, 1.24 high-water cycles**. The export stands **163,046 bytes above** the 2,569,388-byte attention boundary at the delivered tree and 141,340 above at the governed parent — a fourth consecutive firing. Codex measures Grant E's remaining shortfall at 56,444. `STATE.md` is 221,817 of 453,741, **48.9%**, up 27,406 this cycle. |
| F4 | **P2** | The published-tip gap widened rather than closed | Grant F was not issued; `origin/main` remains `993813c755e9f759a4ee165954c7a1df984f6b10`. The unpublished distance now carries v0.41's audit child, all of v0.42, and the local-only `v0.17.9` tag. R17 guards v0.42-forward publications; the v0.41 gap itself stands unrepaired and is now one item inside a larger one. |

---

## 2. Grants — exact required content, all three dormant

None is assumed, implied, or partially in force. Each is in force only when the
operator has issued it with at least the content below; Codex records the grant
text verbatim before the gated step runs. Any one may be issued alone.

### Grant E — second `STATE.md` archival · **recovers ~84,896**

> Authorize a second structural archival of `STATE.md`: move the closed-cycle
> records through v0.38 into a new append-only file under `docs/state-archive/`,
> pin it at `structural` grade in the protected manifest, and leave the status
> header and the v0.39-forward records in place. No other byte moves.

### Grant G — publish `main` and `v0.17.9` · **repairs F4 entirely**

> Authorize publishing, once, non-force and atomically: `origin` `main`
> fast-forward to the exact v0.42 audit child, and annotated tag `v0.17.9` at its
> verified local object peeling to closing commit
> `0382622bbfaeaf7092830460d6432a2eb777b031`. No other ref moves.

This subsumes the unissued Grant F: advancing `main` to the v0.42 audit child
carries v0.41's audit child and every v0.42 commit with it, so the published tip
becomes complete in one act rather than two. R17 now checks the export-audit
containment before the push rather than after.

### Grant H — review retention depth of one cycle · **recovers ~88,665 per cycle, permanently**

> Authorize reducing the accepted review-export retention depth from two cycles
> to one, retaining only the active cycle's documents. The 3,000,000-byte ceiling
> is unchanged.

Executes only if Step 2 has made the deferral ledger canonical, because until
then the prior runbook is what carry-forward compares against. If Step 2 does not
complete, this records not-applicable rather than not-granted.

Ref identities are hypotheses at authoring time and are re-measured immediately
before any push; a grant does not transfer to different objects.

---

## 3. Decisions taken — do not re-litigate

If a measurement refutes a stated basis, record the refutation, stop that step,
continue with the rest, and surface it at handoff.

### DR40 — the ledger becomes canonical, and this runbook is the last to reproduce it

One document holds the deferral ledger. Cycles update it; they do not restate it.
Carry-forward compares the ledger against its own prior state. This runbook still
carries the full 31-row table because Step 2 has not run yet — **that is the last
time**, and the table below is therefore both an input and an exhibit.

### DR41 — the cycle-document set gets a governed boundary

In the same shape the other three already have: a derived boundary strictly
inside failure, a trigger, and a dated `trigger-fired disposition:` on crossing.
Per DR25's precedent the reserve may only widen. The reviewer's output is
governed like everything else or it is the one ungoverned growing thing in a
project that governs growth.

### DR42 — I write shorter runbooks from here

Not a preference. At a measured 63,834 bytes committed and a roughly 1.35×
expansion from draft to close, the document is a capacity term, and a reviewer
who names a growth driver and then keeps driving it is not applying the standard
being asked of the code. Prose is cut; measurements, hypotheses, controls, and
falsifiers are not.

### DR43 — no ceiling movement; the remaining choice is stated, not taken

The 3,000,000-byte ceiling stays. Retention depth moves only under Grant H. If
the measured recovery does not clear the boundary — and §6 says it will not — the
exact shortfall is recorded under the structured `unheld-lever` disposition v0.41
built, and the handoff carries the arithmetic.

### DR44 — version disposition rule, carried

DR20's three clauses govern unchanged, in precedence order: minor for a new route
or observable named surface; minor for any addition, removal, or redefinition of
a value in the domain of a serialized `/v1/*` field, adjudicated against the R15
manifest diff rather than prose; otherwise patch. Ledger consolidation, a
document boundary, and retention depth are none of these. Expected **patch
v0.17.10**; the reasoning is recorded either way.

### DR45 — the close defaults to unpublished-local

Grant G authorizes publishing the *entering* release and the existing lineage,
not a v0.43 release. If a publication grant for v0.43 arrives mid-cycle, DR35's
same-cycle ordering governs from that moment and R17 enforces it.

---

## 4. Retained gate and stop conditions

**Publishing beyond Grant G's exact refs requires separate exact operator
authorization.** No push beyond Grant G and the standing evidence-ref authority.

Stop-and-report — halt the affected step, record the measurement, continue
unaffected work, surface at handoff:

1. A measurement indicates a **published** record contains a false claim.
2. A measurement indicates an **immutable local record** contains a false claim.
3. R17 reports the remote disagreeing with a recorded assertion, as distinct from
   reporting it unavailable or merely lagging.
4. A change would move an entitlement or licensing outcome, a golden input, a
   protected database, an `observation`-grade byte, a dependency resolution, or
   any manifest pin other than the single `structural` pin Grant E adds.
5. Any `/v1/*` payload byte or manifest domain moves outside a declared
   disposition.
6. A change would move an accepted boundary or ceiling — including the
   3,000,000-byte export ceiling and both governed artifact byte boundaries — or
   would narrow any attention reserve. Retention depth moves only under Grant H.
7. Any live publisher request of any kind.
8. Any proposal that would move, delete, re-point, or publish the `v0.17.6` tag.
9. Ledger consolidation would drop, merge, or reword a deferral subject or
   trigger. Consolidation relocates; it does not edit.

---

## 5. Codex-owned determinations

Measure, decide, record the reasoning and the falsifier. A recorded decision
naming what would have changed it is complete work; a question routed to the
operator inside this scope is not.

### C32 — where the canonical ledger lives and how carry-forward reads it

Decide the document and the comparison. Rule: the ledger is a stable document,
not a cycle document, so it neither churns retention nor is dropped by it.
Carry-forward must still fail when a subject disappears or a trigger is reworded
— **prove that with a planted control before adopting the change**, because a
consolidation that silently loosens the ledger is worse than the duplication it
removes. Migration is byte-faithful per stop condition 9; if any subject or
trigger cannot be relocated unchanged, that is the finding, not a licence to
adjust it.

**Decision — 2026-08-05.** The authority is `docs/DEFERRED.md`: it is stable,
Git-tracked, inside `docs/*.md`, and outside `docs/cycles/`, so cycle retention
cannot duplicate or discard it. The comparison baseline is that same ledger at
the parent of the commit that first adds the active runbook. v0.43 has one
explicit migration fallback to the immediately prior runbook because no ledger
exists at that parent; later cycles have no fallback construction to inherit.
The active-cycle marker must advance exactly once, and active cycle documents
may not restate the table. A missing marker, a dropped prior subject, or any
byte change in a carried trigger is the falsifier; registered R12 mutations
execute all three failures.

### C33 — the cycle-document boundary and its derivation

Derive from a stated principle rather than picking a number, in the shape of the
existing governed rows. Decide what the set is — the retained documents, or all
tracked cycle documents — and record why. Rule: the boundary is strictly inside
whatever failure it guards, crossing requires a dated disposition, and the
predicate registry v0.41 built is where its identifier belongs.

**Decision — 2026-08-05.** Govern the exact retained cycle-document set, not
all tracked historical cycle documents, because only the active-plus-prior
runbook/progress set enters the bounded review export. At clean baseline tree
`f8407acaf3fdc3aa4b330950217489f2c117cb62`, the export measured **2,726,105
bytes**. Its four retained documents held **139,368 raw repository bytes** and
**139,364 Repomix content bytes**, so the measured non-cycle payload was
**2,586,741 bytes**. Preserve one maximum-positive-adjacent-governed-growth
cycle, **215,306 bytes**, between the document boundary and the unchanged
**3,000,000-byte** failure ceiling: `3,000,000 - 2,586,741 - 215,306 =
197,953`. The boundary is therefore **197,953 raw bytes**; raw bytes are the
conservative set measure because they include the four final newlines Repomix
removes. At the baseline it left **58,585 bytes / 29.60%**. A larger later
high-water delta must lower the boundary; quiet or smaller growth cannot shrink
the reserve. Non-cycle growth remains governed independently by the whole-export
attention predicate. A derived boundary not strictly inside the export ceiling,
an incorrect baseline subtraction or reserve, an unregistered predicate, or a
crossing without the standard dated substantive disposition is the falsifier.
The executable checker re-derives each quantity it can obtain from repository
authorities and measures the current Git-derived retained set.

### C34 — the archival boundary, if Grant E is issued

Grant E names v0.38. Measure the region against real bytes first; the previously
projected and measured figures disagreed by 52% and the measured one governs.
Follow the v0.37 precedent so the existing derived structural-archive exclusion
removes it with no new mechanism. If the measured region disagrees with the
grant's wording, stop and report rather than choosing a different boundary.

### C35 — anything E0 surfaces

Standing latitude to add rules and planted controls; none to add acceptance
criteria that nothing executes.

### C36 — the ledger is a registered current net-floor restatement

**Decision — 2026-08-05.** Classify the ledger's live subject and trigger as
registered current restatements of the executable net floor, not as historical
family prose. The dated observation is not a carry-forward identity and is
rewritten without the `1.86` and `1.85` numerals, leaving every floor literal on
that line in the live subject or trigger. A dedicated net-floor registry derives
its authority from the executed `run` selection and the tracked toolchain
declaration, and registers both live ledger occurrences. The falsifier is a
derived net floor different from the ledger value: the planted control moves
both authorities together and must fail specifically on `docs/DEFERRED.md`.
Historical-family membership would instead permit that live claim to go stale,
so it is rejected. A choice that required editing the dated observation after a
future floor move would also falsify this decision; removing its numerals now
prevents that demand.

### C37 — reopened tasks derive progress supersession from validated amendments

**Decision — 2026-08-05.** A checked task with multiple valid qualified
progress entries is reopened only when its Step has a disclosed amendment whose
contract fields actually differ from the first committed runbook. The existing
step-to-box mapping supplies the task alias; append order then makes the last
valid qualified entry authoritative and every earlier qualified entry
superseded. No progress field is added or edited. A disclosure without a real
contract change cannot activate supersession, an unamended ambiguity remains a
failure, zero valid entries fail, and entries that cannot be ordered fail rather
than being guessed. This uses the cycle checker's shared validated-amendment
authority, so `tools/checklist_audit.py` carries no second Runbook-amendments
heading literal.

---

## 6. The arithmetic, so the choice can be made once

Hypotheses for E0 to confirm. Projections are arithmetic over measured inputs and
have been wrong before by half; the measured figures govern.

| Input | Bytes |
|---|---|
| Delivered export at the entering tree | 2,732,434 |
| Attention boundary | 2,569,388 |
| Distance above it now | 163,046 |
| Ceiling headroom now | 267,566 (1.24 high-water cycles) |
| v0.41 pair dropped at retention | 89,619 |
| Grant E lever | ~84,896 |
| Grant H lever, per cycle thereafter | ~88,665 |
| Observed non-cycle-document growth | ~+47,000 |

Projected close, assuming this cycle's own document pair lands near 65,000 rather
than v0.42's 88,665:

| Grants issued | Projected close | vs boundary | Ceiling runway |
|---|---|---|---|
| none | ~2,754,800 | ~185,400 above | ~1.14 cycles |
| E | ~2,669,900 | ~100,500 above | ~1.53 cycles |
| H | ~2,666,100 | ~96,800 above | ~1.55 cycles |
| E and H | ~2,581,300 | **~11,900 above** | ~1.94 cycles |

Both grants together roughly double the ceiling runway and land just short of the
boundary. Nothing available clears it. That is the finding, not a failure of the
cycle, and it is why §7 of the handoff states the remaining levers with numbers.

---

## 7. Dependency gates

- Steps 2 and 3 require **Step 1 complete**; otherwise independent.
- Step 2b executes only under Grant H **and** only if 2a completed; otherwise it
  records not-granted or not-applicable, distinguishing the two.
- Steps 4 and 5 execute only under Grants E and G respectively; otherwise each
  records a dated not-granted observation and its box is checked over it — a
  recorded non-execution is the step's truthful completion.
- Step 6 runs if operational code moved; checker changes qualify.
- Step 7 requires every prior box checked and every ledger row dated.

---

## Declared scope

The standing always-allowed set remains `STATE.md`, this runbook, and
`docs/cycles/PROGRESS-v0.43.md`. Release-authority precedence applies only at
R-CLOSE. Every pattern is a literal repository glob.

| Scope class | Path or value |
|---|---|
| `scope_version` | `1` |
| `disposition_intent` | `release` |
| `allow` | `AGENTS.md` |
| `allow` | `ARCHITECTURE.md` |
| `allow` | `docs/*.md` |
| `allow` | `tools/cycle_check.py` |
| `allow` | `tools/version_check.py` |
| `allow` | `tools/checklist_audit.py` |
| `allow` | `tools/export_check.py` |
| `allow` | `tools/invariant_scan.py` |
| `allow` | `tools/progress_check.py` |
| `allow` | `config/invariant-rules.json` |
| `allow` | `config/checklist-exemptions.json` |
| `allow` | `config/protected-artifacts.json` |
| `allow` | `docs/state-archive/**` |
| `allow` | `shell/tests/**` |
| `allow` | `repomix.config.json` |
| `allow` | `run` |
| `forbid` | `tools/model_profiles.py` |
| `forbid` | `tools/evidence_artifacts.py` |
| `forbid` | `tools/domain_manifest.py` |
| `forbid` | `tools/audit_deferred.py` |
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

`docs/*.md` does not cross a path separator, so it reaches a new ledger document
and `docs/intel-platform-OPERATIONS.md` while `docs/cycles/**` and
`docs/state-archive/**` stay governed by their own rows.
`docs/state-archive/**` and `config/protected-artifacts.json` are touched only by
Step 4 and only under Grant E. `crates/**` and `apps/**` are forbidden outright;
release-authority precedence still carries the manifests at R-CLOSE. This
runbook and `PROGRESS-v0.43.md` reach the worktree through the standing status
set, consulted before forbid.

---

## ACTIVATE

Ordered. The first action is not the declaration.

1. **Fill every observation cell in the ledger table first, in the worktree,
   before the activation commit.** The delivered draft ships 31 template cells,
   each naming v0.43 with no ISO date, so `check_trigger_freshness` emits one
   error per row if committed unfilled. **That failure is predicted here, not
   discovered later**: it is the cost of my refusing to date a measurement I did
   not take, and it is discharged by measuring, never by relaxing the check or
   copying v0.42's cells forward.
2. Move the `AGENTS.md` active-cycle declaration to v0.43; create
   `docs/cycles/PROGRESS-v0.43.md`; commit this runbook.
3. Advance review retention through the derived pattern for the depth currently
   accepted; Grant H changes the depth only at Step 2b, never here. If the
   derived value and `repomix.config.json` disagree, the disagreement is the
   finding — record it before changing either side.

**Acceptance criteria.** `cycle-check` resolves v0.43 from the declaration alone
and passes on its first post-activation run; the retention set derives to the
accepted depth ending at the active cycle; the attention state is reported as a
measurement rather than asserted; no ledger observation cell remains a template,
and each carries a real date and the active cycle name.

**Done when** the cycle is declared and every governed table is populated from
derivation.

---

## Step 1 · E0 — entering-state reconstruction

Hypotheses from reading a source export. No repository command produced any of
them. A refuted hypothesis is a finding, not an error to route around.

| # | Hypothesis | How to settle |
|---|---|---|
| H1 | Release parent `5452355945d2717cbd84ea2224148dbd0f4c1ac7` → closing commit `0382622bbfaeaf7092830460d6432a2eb777b031` ← annotated object `a7852c55deba9b509c0235dfba38e2a0426c2501`; audit child `6f07edf84c3ce40f1ef4c9e97e5d101242490243` is its immediate child and HEAD | `rev-parse`, `cat-file`, first-parent walk |
| H2 | Remote `main` is `993813c755e9f759a4ee165954c7a1df984f6b10`; v0.17.7 and v0.17.8 present; v0.17.6 and v0.17.9 absent; the unpublished distance spans v0.41's audit child through v0.42's | R17's executed reading, captured rather than restated |
| H3 | A checkout of `v0.17.9` still passes `cycle-check` | detached checkout, run it |
| H4 | F1 holds: retained cycle documents total 178,284 bytes / 6.52%, with `TASKS-v0.42-EXECUTION.md` at 63,834 the largest growth item of the cycle | measure the tree and the two exports |
| H5 | F2 holds: 31 subjects; the v0.42 and v0.41 runbook tables measure 11,124 and 11,294 bytes; carry-forward is the only reason the prior runbook must be exported | read the comparison; confirm the checkers read `docs/cycles/` from the worktree |
| H6 | Delivered export 2,732,434 / 157 entries, all tracked; 163,046 above the 2,569,388 boundary; headroom 267,566 at the 215,306 denominator | export at the entering tree; run `export-check` |
| H7 | Grant E's lever is near 84,896 and `STATE.md` is 221,817 of 453,741 | measure directly; the measured figure governs over §6 |
| H8 | Registry 17 rules / 119 controls; exemptions 9; retractions 3; the v0.42 closing checklist reconciles | run the tools; derive rather than copy |

### E0 measured verdicts — 2026-08-05

| # | Verdict | Executed measurement |
|---|---|---|
| H1 | **confirmed** | Local object reads identify `a7852c55deba9b509c0235dfba38e2a0426c2501` as an annotated tag peeling to closing commit `0382622bbfaeaf7092830460d6432a2eb777b031`; its immediate parent is release parent `5452355945d2717cbd84ea2224148dbd0f4c1ac7`. Entering audit child `6f07edf84c3ce40f1ef4c9e97e5d101242490243` has the closing commit as its immediate parent and was exact entering HEAD. |
| H2 | **confirmed** | Permission-capable direct `ls-remote` returns `main=993813c755e9f759a4ee165954c7a1df984f6b10`, exact direct/peeled v0.17.7 and v0.17.8 refs, and empty output for v0.17.6, v0.17.9, v0.8.0, and v0.10.2. The first-parent walk from main to entering HEAD contains **16 commits**, beginning with v0.41's audit child and ending with v0.42's audit child. R17 independently reports `verdict=measured`, **30 refs / 1 audit**, and the same main. |
| H3 | **confirmed** | A temporary detached worktree at annotated `v0.17.9` resolved to closing commit `0382622…`; its real `./run cycle-check` passed with `active=v0.42`, `state=closed`, `local_tag_refs=verified`, `governed_export=bound`, and **40 closed execution cycles / 3 historical records**. The temporary worktree was then removed. |
| H4 | **confirmed** | Exact entering export contains **178,284 cycle-document content bytes / 6.52%**: v0.42 runbook **63,834**, v0.42 progress **24,831**, v0.41 runbook **59,795**, v0.41 progress **29,824**. Comparing the exact **2,675,890-byte** prior delivered export with the **2,732,434-byte** entering export makes the new v0.42 runbook the largest positive item at **+63,834**, ahead of State **+27,406**, v0.42 progress **+24,831**, and `cycle_check.py` **+13,157**. |
| H5 | **confirmed** | Both runbooks carry **31** subjects. The bytes after `## Deferred means deferred` through the next heading are exactly **11,124** in v0.42 and **11,294** in v0.41. Source tracing shows `check_deferred_carry_forward` chooses and reads the immediately prior runbook from `execution_runbooks(root)` in the worktree; `export_check.py` separately derives retained cycle paths from Git and never supplies review-export bytes to that comparison. No second semantic consumer requiring prior-runbook export membership appeared. |
| H6 | **confirmed** | The exact entering commit passes project-root `export-check` at **2,732,434 bytes / 157 derived and exported Git-tracked entries / 2 retained cycles**. It is **163,046 bytes above** the **2,569,388-byte** attention boundary and leaves **267,566 bytes / 8.92% / 1.24 high-water cycles** below the ceiling at the **215,306-byte** denominator. |
| H7 | **partly confirmed, partly refuted by one byte** | The directly delimited first-v0.38-record-to-permanent-tail region is exactly **84,896 bytes**, confirming the lever. The actual entering `STATE.md` is **221,818 / 453,741 bytes**, not 221,817; **221,817** is its Repomix content payload after the file's terminal newline is outside the `<file>` body. Raw repository bytes govern the artifact boundary. |
| H8 | **confirmed** | Direct JSON derivation gives **17 rules / 119 fail-before controls / 9 exemptions / 3 retractions**. `checklist-audit` passes and reconciles v0.42 at **7 checked / 7 matched / 7 commits resolved**; after ACTIVATE the aggregate is **333 checked / 3 retracted / 324 matched / 324 resolved / 9 exemptions**. |

Plus the standing entering measurements: `git status --porcelain` with its
expected untracked set stated exactly, full `./run ci-local`,
`invariant-scan --self-test`, both complete Python populations, and golden —
counts, not adjectives.

**Acceptance criteria.** Every hypothesis carries a dated verdict: confirmed,
refuted, or unmeasurable with a stated reason. H2 and H3 are settled by executing
rather than citing prior records. No figure in this document is treated as
established by appearing here.

**Done when** dependent steps start from measurements rather than from this
runbook.

---

## Step 2 · LEDGER — write the deferral ledger once

Per F2, DR40, C32, and stop condition 9.

**2a — canonical ledger.** Relocate the 31 subjects, triggers, and their current
dated observations into one stable document per C32, byte-faithfully. Move
carry-forward to compare the ledger against its own prior state. Cycles update
the ledger; runbooks and progress logs reference it.

**2b — retention depth, under Grant H and only after 2a.** Reduce the accepted
depth to one cycle and re-derive the retention pattern. If Grant H is absent,
record not-granted; if 2a did not complete, record not-applicable, and keep those
two verdicts distinct.

**2c — classify the ledger's floor literals.** Per C36, bind the live subject
and trigger to the derived net floor while leaving the dated observation free of
floor numerals. Re-run every tracked-file classifier only after the ledger and
its registry are both committed.

**2d — resolve reopened-task progress correspondence.** Per C37, derive
reopening from the Step's validated amendment and make the last valid qualified
entry in recoverable append order authoritative. Preserve every dated progress
entry and add no exemption or retraction.

**Planted controls.** A ledger missing a subject that the prior state carried
fails. A ledger whose trigger text differs from the prior state's fails. And a
cycle that simply omits its ledger update fails rather than silently inheriting —
that third one is what stops consolidation from becoming a quieter ledger, and it
is the control to write first.

**Acceptance criteria.** All three planted controls fail before and pass after,
each anchored at a registered control site; migration is proved byte-faithful
subject by subject and trigger by trigger rather than by count; the checkers'
reads of `docs/cycles/` are unchanged so nothing depends on export membership;
2b's two negative verdicts are distinguishable in the output; `./run ci-local` is
clean. `version-check` passes with the ledger tracked, and the classification
chosen for it fails when the derived net floor moves — proved by a planted
control that mutates the derived floor and observes the check fire on the
ledger. The classification is recorded with the reasoning that selected it and
the measurement that would have selected differently. No dated historical
measurement is edited to reach the pass. `checklist-audit` passes with the
reopened task's correspondence resolved to exactly one authoritative commit,
chosen by a rule derived from recorded state rather than declared per instance,
and proved by planted controls in both directions. No dated progress entry is
edited, and no exemption or retraction is added.

**Done when** the ledger exists once and no cycle document restates it.

---

**Measured result — 2026-08-05.** 2a is `completed`. Exact cell comparison
against v0.42 at activation parent `6f07edf8…` reports **31 subjects / 0 subject
differences / 0 trigger differences**. `docs/DEFERRED.md` is the sole active
table; the runbook and progress record contain no `## Deferred means deferred`
heading. R12's stale-cycle control was written first, followed by the missing-
subject and reworded-trigger controls; the registered self-test executes all
three fail-before mutations. The focused checker suite passes **98/98**.
The complete registry passes **17/17 rules / 121 controls**, full
`./run ci-local` passes **22/22**, Python 3.11 and 3.12 each pass **399/399**,
and the embedded plus standalone golden runs each pass **11/11**.

2b is `not-granted`, not `not-applicable`: 2a completed, but Grant H is absent.
The derived retention depth and v0.42–v0.43 configured set therefore remain
**2 cycles**. `cycle-check` emits `retention_change=not-granted`; the separate
`not-applicable` value remains a distinct accepted machine value for the case
where 2a does not complete.

2c is `completed` after tracked candidate
`4a5c0e27229a3616708a8e4671cb811967024bf1` existed. At that exact committed
state, `version-check` derives **2** agreeing net-floor authorities at **1.86**,
extracts **2** ledger current restatements at the same value, and classifies the
ledger as `registered current restatement` over **596** tracked files. The
ledger observation contains neither floor numeral and no closed dated
measurement was edited. Moving both derived authorities together to **1.87**
without changing the ledger fails specifically at `docs/DEFERRED.md`; disabling
that comparison is independently rejected by R12's registered fail-before
mutation. Historical-family classification was measured as the alternative
that would not fire and was rejected per C36.

The exact tracked candidate passes the focused version suite **16/16**, the
complete registered scan **17/17 rules / 123 controls**, full `./run ci-local`
**22/22**, Python 3.11 and 3.12 **403/403** each, and embedded golden **11/11**.
`cycle-check` reports the canonical ledger at **33 subjects**, depth **2**, and
`retention_change=not-granted`; the two amendment-required enumeration subjects
carry dated v0.43 observations and action `none`.

2d is `completed`. The checklist consumes the cycle checker's shared amendment
derivation and maps the validated Step to its derived task box. Before this
completion's required audit entry exists, the live v0.43 check resolves the two
qualified LEDGER records in append order, keeps `90f8ef9f…` as superseded
history, and attests `67e75f65856a04a912273c9ed4e7c2459cc8bd04` as the sole
authority. R13's five new planted controls prove the opposite directions:
unamended ambiguity and a disclosure without a contract change both fail; zero
valid entries and unrecoverable order fail; and a legitimate reopening selects
the later entry. The complete registry passes **17/17 rules / 128 controls**.

No dated progress entry was edited and no exemption or retraction was added.
The permission-capable full local gate passes **22/22**, Python 3.11 and the
clean Python 3.12.13 rebuild each pass **403/403**, and embedded golden passes
**11/11**. The initial sandboxed full-gate attempt was not accepted because its
loopback wire-test bind was denied; the identical permission-capable rerun
passed that wire test. The canonical ledger now carries **34 subjects**, adding
the dated twice-fired declared-scope-sufficiency observation required by A2.

## Step 3 · DOC-BOUNDARY — govern the reviewer's own output

Per F1, DR41, DR42, and C33. Three growing quantities in this repository carry a
governed boundary. The fastest-growing one, and the only one produced by the
reviewer, carries none.

Derive a boundary per C33, register its predicate identifier alongside the
existing ones, and require a dated disposition on crossing.

**Planted control.** A cycle-document set at or above the boundary without a
dated disposition fails, and the same set with one passes. The disposition
predicate v0.41 built already distinguishes a measured change from an unheld
lever; reuse it rather than inventing a second vocabulary.

**Acceptance criteria.** The boundary is derived from a written principle and the
derivation is executable; the planted control fails before and passes after,
anchored at a registered control site; the predicate identifier is in the same
registry as the others; the current set's position against the boundary is
reported as a measurement; `./run ci-local` is clean.

**Done when** the document I write is governed by the standard I apply to the
code.

---

**Re-execution gate — 2026-08-05.** After Amendment A1 closed Step 2, the
unchanged DOC-BOUNDARY implementation passed its focused suite **115/115**, the
complete registered scan **17/17 rules / 123 controls**, `cycle-check`, and
`version-check`. The retained set measured **149,990 raw bytes / 4 paths**
against the derived **197,953-byte** boundary, leaving **47,963 bytes**; the
crossing trigger did not fire.

The required full `./run ci-local` then stopped at checked-task evidence. Both
the original LEDGER progress entry and Amendment A1's required post-completion
entry are valid and runbook-qualified, so `checklist-audit` rejects them as
`multiple valid runbook-qualified entries` at progress lines **110** and
**203**. Release/version and active-cycle checks passed before that failure.
The progress log is append-only, the active task workflow required the second
entry after the reopened task completed, `tools/checklist_audit.py` is outside
declared scope, and adding an exemption would reduce an existing control's
reach to make its finding disappear. No permitted truthful change can satisfy
this gate. DOC-BOUNDARY remains open; Steps 4–7 do not execute against the
failed matrix.

## Step 4 · ARCHIVE — dormant, Grant E

**Objective.** Execute Grant E exactly, or record its absence truthfully.

If granted: record the grant text verbatim; confirm the region against real bytes
per C34; move the closed-cycle records through v0.38 into a new append-only file
under `docs/state-archive/` on the v0.37 precedent; pin it `structural`, which the
existing derived exclusion then removes with no new mechanism; leave the header
and the v0.39-forward records in place. Archived records are not edited in transit
— an archival that rewrites a dated measurement is a prohibited edit wearing a
move.

If not granted: one dated not-granted observation carrying the measured quantity
under the structured `unheld-lever` disposition.

**Acceptance criteria.** Either the archive exists with its structural pin and the
derived exclusion removes it, with the archived bytes proved byte-identical to
what `STATE.md` held — or the not-granted observation is recorded with its date
and the unrecovered quantity. `STATE.md` remains valid against its header and
boundary controls either way; the manifest changes by exactly one pin or not at
all; `./run ci-local` is clean.

**Done when** the lever is spent as authorized, or its absence carries a number.

---

## Step 5 · PUBLISH — dormant, Grant G

**Objective.** Execute Grant G exactly, or record its absence truthfully.

If granted: record the grant text verbatim; measure every precondition
immediately before the push under R17's executed reading — remote `main` at the
exact recorded commit, the target resolving to the exact audit child, `v0.17.9`
absent remotely, its local object peeling to the recorded closing commit,
ancestry proven, published tags unmoved; one atomic non-force push; then read the
remote back and record what moved and the push-triggered hosted run.

Irreversibility is accepted and one-directional. Once pushed, the retraction bar
covers the newly published commits, and no later finding is grounds to delete or
force-move a ref. A failed post-push run makes the truthful state "published,
hosted verification failed" — recorded and stopped on, never unwound.

If not granted: one dated observation naming exactly what a reader of published
history still cannot see, and the unpublished distance in commits.

**Acceptance criteria.** Either the remote readback shows `main` at the exact
audit child and `v0.17.9` at its verified object with every other tag unmoved,
the post-push records appended at column zero, the status header updated, and
R17's export-audit containment satisfied — or the dated not-granted observation
names the gap precisely. `v0.17.6` is absent remotely in either case.

**Done when** published history is complete, or its incompleteness is a
measurement rather than an implication.

---

## Step 6 · RE-MEASURE — hosted, conditional

Runs if operational or production code moved; checker changes qualify. Evidence
ref under the standing authority: under `refs/heads/codex/`, naming the active
cycle and a short commit id, absence pre-check recorded under R17's reading,
non-force, exactly one ref created, `main` and every tag untouched beyond Grant G.
Report run id, attempt, ref, and blocking identity result. A pre-existing ref is a
finding, not a detail.

**Acceptance criteria.** Either a hosted run is reported with its id, attempt,
ref, and blocking identity result, and the remote readback shows every tag
unmoved and `main` where Step 5 left it — or the dated skip reason is recorded
with the claims that consequently rest on local execution alone. The absence
pre-check is recorded either way.

**Done when** every claim in this cycle names the machine that witnessed it.

---

## Step 7 · R-CLOSE

The established close with the v0.40 pre-tag gate standing: release parent →
assembled closing worktree → **pre-tag gate must pass** → closing commit →
annotated tag → **append-only audit child as the immediate next commit**, carrying
`- cycle-ending review-export audit: closing_tree=…; bytes=…; audit_delta=…`
measured against the closing tree it follows. Per DR45 the close is
unpublished-local; if a v0.43 publication grant arrives, DR35's ordering governs
and R17 enforces it.

**Acceptance criteria.**

- The pre-tag gate passed before the tag existed, and its verdict is recorded.
- **A checkout of the new annotated tag passes `cycle-check`.**
- Dated disposition per DR44, adjudicated against the R15 manifest diff.
- `version-check` passes with authorities and restatements counted.
- `checklist-audit` passes with figures stated inline and a non-zero v0.43 line.
- The governed export row is bound; the audit child is present in order;
  `audit_delta` reconciles against the closing tree.
- Every ledger row carries a dated v0.43 observation in its canonical home; the
  attention disposition and the new document-boundary disposition each use the
  structured form.
- Headroom restated in bytes, percent, and high-water cycles, with recovery
  attributed to each lever separately and the shortfall stated exactly.
- Per DR42, the closing runbook and progress pair are measured and the figure
  compared against v0.42's 88,665.
- `invariant-scan --self-test`, both Python populations, and golden: counts
  stated, zero hand-typed absolute finding-line fields.
- No publication beyond Grant G's refs. No process instruction inside a dated
  record.

**Done when** the cycle is closed, audited, truthfully represented, and the
handoff written.

---

## Closing-record assembly template

*Assembled at Step 7 in the established field form, every figure inline. Release
identity, evidence candidate, hosted run, governed export, artifact boundaries,
attention state and disposition, cycle-document boundary and disposition, ledger
disposition, divergence disposition, scope reconciliation, publication boundary,
checklist reconciliation, golden reconciliation, and the pre-tag and post-tag
gate verdicts each carry measured values. No annotated-tag-object field; the tag
targets the closing commit only after it exists.*

---

## Governed artifact byte-boundary authority

- governed artifact byte boundary: path=`STATE.md`; bytes=`453741`
- governed artifact byte boundary: path=`config/protected-artifacts.json`; bytes=`1048576`

**Carried forward byte-identically.** A change to either figure is an
architectural change requiring its own justification and operator authorization.
The 3,000,000-byte export ceiling remains separately governed and is not moved.
Step 3 adds a boundary; it moves none.

---

## Deferred ledger authority

The canonical 31-row population, unchanged subject and trigger cells, current
v0.43 observations, and active actions live only in `docs/DEFERRED.md`.
Carry-forward now compares that document with its own activation-parent state.

- **Ledger migration result:** `completed`
- **Retention-depth disposition:** `not-granted`
- **Retention depth:** `2` cycles (unchanged)

---

## Standing prohibitions

- Ledger consolidation relocates; it never drops, merges, or rewords a subject or
  trigger.
- `docs/state-archive/**` and `config/protected-artifacts.json` are touched only
  by Step 4 and only under Grant E.
- No archived record edited in transit. Moving a dated measurement is permitted;
  changing one is not.
- No push beyond Grant G's exact refs and the standing evidence-ref authority. No
  force-push, ref deletion, or tag movement anywhere, ever.
- The `v0.17.6` tag, its object, and its target are never moved, deleted,
  re-pointed, or published.
- No closed-cycle document, observation, fixture, or immutable local record
  edited; corrections are forward and dated.
- No tag created before the pre-tag gate has passed at that tree.
- No wire request of any kind. No control adopted that requires network access to
  succeed.
- No expectation, anchor, or figure copied from a checker's own output where the
  construction can produce it independently.
- No acceptance criterion discharged by inspection where a registered
  self-testing rule with an executable `fail_before` can exist.
- No hardcoded scope list where the scope can be derived.
- No acceptance discharged by an executable whose witness set is empty.
- No step that newly tracks a file is accepted until every gate that classifies
  tracked files has been run at the tracked state. A gate run over an untracked
  file measures a state that will not exist.
- No change that reduces the reach of an existing control, or widens a trigger, to
  make a failure disappear.
- No retraction added without quoting the bar and obtaining an operator decision.
- The three untracked amendment inputs are not edited, moved, renamed, or deleted.

---

## Cycle checklist

- [x] ACTIVATE
- [x] E0
- [x] LEDGER
- [ ] DOC-BOUNDARY
- [ ] ARCHIVE
- [ ] PUBLISH
- [ ] RE-MEASURE
- [ ] R-CLOSE

*Box ids match the `PROGRESS-v0.43.md` entry ids exactly.*

---

## Handoff

One report: each DR executed and whether any measurement refuted its basis; each
C-determination with its reasoning and falsifier; every stop condition triggered
or an explicit none; all three grant outcomes, executed or not-granted with the
quantity or gap named; the closing export with recovery attributed to each lever
and the shortfall stated; the closing cycle-document pair measured against
v0.42's 88,665; and the v0.44 findings list — findings, not proposed acceptance
criteria.

Then the capacity choice, which has now been deferred four times and should be
made once. §6 gives the arithmetic: both grants together roughly double the
ceiling runway and still land near 12,000 bytes above the attention boundary.
What remains beyond them, each with what it would recover: raising the
operator-selected 3,000,000-byte ceiling; archiving `CHANGELOG.md` on the
`STATE.md` pattern at roughly 83,770 bytes; or a further redefinition of review
source. Growth stays concentrated in checker code, checker tests, the rule
registry, dated records, and — until this cycle — the reviewer's own documents.
That is the apparatus this discipline requires, growing because the discipline is
working. The handoff states the runway in cycles at the high-water denominator so
the choice arrives with numbers rather than as an emergency.

---

## Provenance

**Measured on the delivered post-v0.42 export (2,732,434 bytes / 157 entries,
reconciling with the reported 2,730,969-byte closing tree plus a 1,465-byte audit
append and the governed 2,710,728 plus the audited +20,241):** per-file deltas
against the prior export placing `TASKS-v0.42-EXECUTION.md` at +63,834 ahead of
`STATE.md` at +27,406, which is F1's basis; the 178,284-byte retained
cycle-document total at 6.52%; the 11,124- and 11,294-byte deferral tables in the
v0.42 and v0.41 runbooks, which is F2's; the delivered-draft series 44,490 →
47,826 → 46,977 against the committed 56,135 → 59,795 → 63,834, giving the ~1.35×
execution expansion; `STATE.md` at 221,817 of 453,741; the attention boundary at
2,569,388 with the delivered export 163,046 above it; R17's registered claim
confirming both the offline `unavailable` verdict and the non-retroactive
historical-shape guard; one `ls-remote` occurrence in `cycle_check.py` against
zero last cycle; the registry at 17 rules / 119 controls counted from
`config/invariant-rules.json`; and `scope_pattern_regex` compiled directly to
confirm `docs/*.md` does not cross a separator.

**Verified unchanged against the checker that will scan this runbook:**
`STEP_HEADING_RE`, `DEFERRED_HEADING`, `AMENDMENTS_HEADING`,
`AMENDMENT_ENTRY_RE`, `CONTRACT_FIELD_LABELS`, `SCOPE_HEADING_RE`,
`SCOPE_CLASSES`, `STEP_REFERENCE_RE`, the quantity-clause predicate, the
declared-scope pattern-population control, and the registry-derived archival
trigger text this table reproduces.

**Hypotheses, not measurements:** anything requiring `.git` or the network — the
object graph, every remote ref, ancestry, the published tip's content, and
whether the `v0.17.9` tag checkout still passes. §6's projections are arithmetic
over measured inputs; the previous archival projection was 52% high, so the
measured figures govern.

**What I did not do:** no repository command, no wire request, no test run, no
push. Every figure is for Step 1 to confirm against real bytes.
