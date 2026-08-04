# TASKS-v0.41-EXECUTION.md — make the relief lever reachable before the ceiling arrives

## Runbook amendments

**Cycle:** v0.41
**Entering release:** v0.17.7, closed locally at v0.40, unpublished and awaiting
an operator decision; v0.17.6 permanently withheld; v0.17.5 published
**Entering ref (hypothesis):** audit child `2c457feb870d62b16a5f9d9ca06aefcb3dc4cf8b`
**Prior cycle:** v0.40 — closed clean. The v0.17.7 tag checkout passes
`cycle-check`, which is what the cycle existed to prove.
**Autonomy:** the standing `CYCLE_AUTONOMY_AUTHORITY` block governs. Every
decision is taken in §3 or delegated in §5 with a decision rule and a required
falsifier. One milestone step is **dormant by construction** and executes only
under Grant E, recording a dated not-granted observation otherwise. No operator
question is routed mid-cycle.

**This cycle is worth running with no grant issued.** Three of its four steps
need no authorization, and together they recover more bytes than the grant does.

Amendment entries, if any step's contract changes mid-cycle, are appended below
this line in the form `Step N — <what changed> — YYYY-MM-DD`.

---

## 0. Why this cycle exists

v0.40 did what it was asked. The tag-independent assertions were hoisted above
the tag-resolution early return, and the pre-tag verdict is now a distinct
`local-tag-reconciliation=pre-tag` state gated on HEAD sitting exactly at the
release commit — tighter than I specified, and better, because it opens no hole
for an arbitrarily missing tag. The withheld state landed as a labelled field
with a control rejecting a withheld release presented as pending, and
`withheld-hosted` resolves F5 rather than documenting it. The attention basis
now selects the maximum positive adjacent governed delta, widening the reserve
from 214,452 to 430,612 bytes, and the quiet-cycle fixture proves the old
selector would have rejected what the new one accepts. Registry 16/108,
checklist 317 = 308 + 9, retractions held at 3. And the v0.17.7 tag checkout
passes `cycle-check` — the thing v0.17.6 could not claim.

The corrected attention predicate then fired, which is the control working.
What happened next is the problem.

The deferral row that names the largest relief lever — the second `STATE.md`
archival — carries a checker-pinned trigger reading *"the export ceiling
trigger fires, or STATE.md reaches its governed artifact byte boundary."* In
v0.39 I replaced the export-capacity trigger with the attention predicate and
never noticed that this row pointed at the old one by name. There is no longer
any "export ceiling trigger": the ceiling is a bare hard failure at
`export_bytes > MAX_EXPORT_BYTES`, with no trigger attached. So v0.40 read the
clause against the fixed ceiling, correctly under the words, found it unfired,
and recorded `none`.

The lever is therefore reachable only through its second clause — `STATE.md`
reaching 453,741 bytes, some 285,013 bytes and roughly fourteen cycles away —
while the export it exists to relieve sits **0.91 high-water cycles** from the
ceiling. The relief arrives long after the emergency.

And when the attention predicate did fire, the disposition it demanded was
satisfied by text. `TRIGGER_FIRED_DISPOSITION_RE` accepts any non-`none` string.
v0.40's disposition retained the ceiling, retained the retention depth, adopted
the basis, and recovered zero bytes. Every word of it is true. None of it is
responsive.

So the shape of this cycle is: a control fired, its required answer could be
given without doing anything, and the lever it should have reached was pointed
at a trigger that no longer exists. Both defects are mine — I sharpened the
referring trigger and left the reference dangling, and I specified a disposition
requirement that constrains only its own presence.

The fourth finding is the one that makes the cycle survivable without a grant.

---

## 1. Findings carried in

| # | Priority | Finding | Measured basis |
|---|---|---|---|
| F1 | **P1** | The archival trigger points at a trigger that no longer exists | `GOVERNED_ARTIFACT_ROW_SPECS["STATE.md"]` pins the clause "the export ceiling trigger fires, or STATE.md reaches its governed artifact byte boundary". Grepping `export_check.py` for every `MAX_EXPORT_BYTES` site returns one comparison, `export_bytes > MAX_EXPORT_BYTES`, whose message reads "exceeds ceiling" — a hard failure, not a trigger. The only export trigger is the attention predicate, under a different name. v0.40 recorded the row as unfired with the observation "the export attention predicate fired but the fixed export ceiling did not", which is correct against the text. Entering `STATE.md` is 172,659 of 453,741, so the surviving clause is 281,082 bytes away at an observed rate near 20,000 per cycle. |
| F2 | **P1** | A fired attention trigger can be discharged without recovering a byte | `TRIGGER_FIRED_DISPOSITION_RE` matches `trigger-fired disposition:` followed by any text that is not `none`, bounded by the next `.`, `;`, or `\|`. It constrains presence, not substance. The v0.40 disposition retains the ceiling, retention depth, and basis; the export did not move because of it. |
| F3 | **P1** | Capacity is inside one high-water cycle | The delivered export is 2,803,926 bytes, byte-reconciled against the reported closing tree at 2,801,474 plus a 2,452-byte audit-child append. Headroom is 196,074 bytes, 6.54%, **0.91 cycles** at the 215,306-byte high-water denominator. The export stands 234,538 bytes above the 2,569,388-byte attention boundary, so the predicate is firing at the entering tree. |
| F4 | **P1** | Nearly 7% of the review export is a hash table for bytes the export excludes | `config/protected-artifacts.json` is 200,439 bytes, of which the `pinned_files` array is 194,191 — **96.9%**. Of its 339 pins, **9** reference files present in the export; 324 point under `evidence/`, which `evidence/**` excludes wholesale. A reviewer can verify 9 of 339 hashes and no more, by construction. The non-pin content — schema, lifecycle, admission chain, artifacts — is roughly 6,246 bytes and is the part review actually uses. |
| F5 | **P2** | Growth is concentrated in what must stay reviewable | Per-file deltas across the two delivered exports total **+60,129**: `STATE.md` +19,850, `tools/` +18,152 (`invariant_scan.py` +9,967, `cycle_check.py` +8,185), `shell/tests/` +9,214, `config/invariant-rules.json` +5,414. Production code moved zero bytes. Every growing file is checker source, checker tests, the rule registry, or dated records — the apparatus the discipline requires. Exclusion buys cycles; it does not bend the curve. |

---

## 2. Grant E — exact required content, dormant until issued

Not assumed, not implied, not partially in force. Grant E is in force only when
the operator has issued it with at least the content below; Codex records the
grant text verbatim in the progress log before Step 5 runs.

> Authorize a second structural archival of `STATE.md`: move the closed-cycle
> records through v0.38 into a new append-only file under `docs/state-archive/`,
> pin it at `structural` grade in the protected manifest, and leave the status
> header and the v0.39 and v0.40 records in place. No other byte moves.

Reviewer recommendation, for the operator's consideration: **issue it.** The
measured case is in §6 — the no-grant work alone leaves the close roughly 94,000
bytes above the attention boundary, and the archival closes that gap with margin.
Withholding it is defensible and costs nothing irreversible; the cycle then
completes with a disposition that names the exact remaining gap and the exact
unheld lever, which is what F2's fix exists to require.

Archival is not reversible in practice — the archive becomes a pinned structural
byte and the records it holds are immutable thereafter. The boundary between
archived and retained is chosen once.

---

## 3. Decisions taken — do not re-litigate

If a measurement refutes a stated basis, record the refutation, stop that step,
continue with the rest, and surface it at handoff.

### DR28 — the archival trigger is repaired by naming the predicate, not by widening it

The dangling clause is replaced with a reference to the predicate that actually
exists. The repair does not make the archival trigger fire on anything the
attention predicate would not, and does not lower the attention predicate to
reach it. A trigger repaired by making it easier to fire is a different defect
wearing the same fix.

### DR29 — the runbook ships the current pinned text, and Step 2 moves both halves together

The row text is compared byte-exact against `GOVERNED_ARTIFACT_ROW_SPECS`. This
runbook's deferral table therefore carries the **existing** clause verbatim, so
ACTIVATE passes; Step 2 changes the checker spec and the row in the same commit.
Writing the corrected text into the table now would fail at activation, and
writing it only in the checker would fail immediately after. **Both halves move
together or neither does.** This ordering is stated here so it is not
rediscovered as a blocker.

### DR30 — the export ceiling does not move, and no lever is invented

The 3,000,000-byte ceiling is operator-selected and stays. The attention reserve
may only widen, per DR25. If the measured recovery does not clear the boundary,
the exact shortfall is recorded and rides the handoff. No new exclusion class is
created to make a number look better than the export is.

### DR31 — the manifest's integrity role is untouched

Whatever Step 4 decides about what review *sees*, `config/protected-artifacts.json`
remains tracked, remains the authority `verify-artifacts` checks, and keeps every
pin. This cycle changes what the review export carries, never what integrity
holds. Under Grant E, Step 5 adds exactly one `structural` pin and changes
nothing else in that file.

### DR32 — version disposition rule, carried

DR20's three clauses govern unchanged, in precedence order: minor for a new route
or observable named surface; minor for any addition, removal, or redefinition of
a value in the domain of a serialized `/v1/*` field, adjudicated against the R15
manifest diff rather than prose; otherwise patch. Export selection, trigger
repair, and archival are none of these. Expected: **patch v0.17.8**; the
reasoning is recorded either way. A manifest diff showing domain movement is a
stop under §4.

### DR33 — the v0.41 close publishes under the initiating authorization

The operator's initiating message says, verbatim, “I authorize you to publish
before you begin the current task.” This supplies the ask-first authorization
for v0.17.7 and the v0.41 release before activation. It does not widen Grant E,
does not authorize v0.17.6, and leaves every R-CLOSE precondition intact.

---

## 4. Retained gate and stop conditions

**Publishing `main`, v0.17.7, and the v0.41 release is explicitly authorized by
the initiating operator message.** Grant E remains separate and unissued. No
other publication or push beyond the standing evidence-ref authority is in
force, and v0.17.6 remains permanently withheld.

Stop-and-report conditions — halt the affected step, record the measurement,
continue unaffected work, surface at handoff:

1. A measurement indicates a **published** record contains a false claim.
2. A measurement indicates an **immutable local record** contains a false claim
   — a tagged closing tree from tag creation, an append-only observation, a
   pinned artifact, or a closed-cycle document from commit.
3. A change would move an entitlement or licensing outcome, a golden input, a
   protected database, an `observation`-grade byte, a dependency resolution, or
   any pin in the protected manifest other than the single `structural` pin
   Grant E adds.
4. Any `/v1/*` payload byte or manifest domain moves outside a declared
   disposition.
5. A change would move an accepted boundary or ceiling — including the
   3,000,000-byte export ceiling and both governed artifact byte boundaries —
   or would narrow the attention reserve, rather than select inside it.
6. Any live publisher request of any kind.
7. Any proposal that would move, delete, re-point, or publish the `v0.17.6` tag.
8. A derived exclusion would remove a path whose bytes a reviewer can actually
   verify from the export, or would leave a path that no reviewer can.

---

## 5. Codex-owned determinations

Measure, decide, record the reasoning and the falsifier. A recorded decision
naming what would have changed it is complete work; a question routed to the
operator inside this scope is not.

### C24 — how a fired disposition is made responsive without becoming unsatisfiable

The requirement is that a fired trigger's disposition be answerable against a
later measurement rather than by restating awareness. Candidates: naming a
measured byte movement; naming an explicitly unheld lever together with the
quantity it would recover; escalating when the predicate fires in consecutive
cycles with the measured quantity not improving.

**Hard rule, and it is the important half.** The remedy must be satisfiable in
the state this project is actually in — a cycle whose only remaining lever is
ask-first must be able to close truthfully by saying exactly that, with the
number attached. A control that cannot be discharged without a grant is an
author-side unsatisfiable rule, and this project has owned seven of those. Prove
satisfiability against the current entering measurements before adopting the
predicate, and record that proof.

### C25 — what the export carries in place of the pin index

The measured fact is that 194,191 bytes index files absent from the export and
6,246 bytes carry the lifecycle, admission chain, and artifact list that review
uses. Decide the mechanism and the derivation together.

Rule: prefer the mechanism that adds no new artifact requiring synchronization;
if the review-relevant head is judged worth keeping, its staleness must be a
failure rather than a silent divergence. The exclusion class is derived from
repository bytes in the shape of the three that already exist, non-vacuous in
both directions, and never a threshold chosen to reach a number. **If no honest
derivation exists, report that as the finding, take the retention advance alone,
and state the shortfall** — do not invent a class to hit the boundary.

### C26 — where the archival boundary falls, if Grant E is issued

The measured regions: records from the first v0.38 entry to end of file total
128,859 bytes; from v0.37, 105,646; from v0.36, 81,841. Grant E names v0.38.
Confirm against real bytes, and follow the v0.37 archival precedent for naming,
pinning, and the derived structural-archive exclusion that already exists.

Rule: the boundary is chosen once and the archive is immutable after. If the
measured region disagrees with the grant's wording, the disagreement is the
finding — stop and report rather than choosing a different boundary than the one
authorized.

### C27 — anything E0 surfaces

Standing latitude to add rules and planted controls; none to add acceptance
criteria that nothing executes.

---

## 6. The arithmetic, stated so no step has to guess

All figures are hypotheses for E0 to confirm against real bytes.

| Quantity | Bytes |
|---|---|
| Delivered export at the entering tree | 2,803,926 |
| Attention boundary | 2,569,388 |
| Distance above the boundary now | 234,538 |
| Ceiling headroom now | 196,074 (0.91 high-water cycles) |
| Pin-index exclusion, if Step 4 finds a derivation | ~200,439 |
| Second archival through v0.38, under Grant E | ~128,859 |
| Observed net growth per cycle, retention churn included | ~+60,129 |

Projected close without Grant E: roughly 2,663,600 — about 94,200 **above** the
boundary, so the predicate fires again and Step 3's disposition must say so with
the number. Projected close with Grant E: roughly 2,534,800 — about 34,600
**below** the boundary, and near 2.16 high-water cycles of ceiling headroom.

Per F5 this buys cycles rather than solving the trend. That belongs in the
handoff, not in a step.

---

## 7. Dependency gates

- Steps 2, 3, and 4 require **Step 1 complete**; they are otherwise independent
  and may interleave.
- Step 5 executes only under Grant E; otherwise it records a dated not-granted
  observation and its box is checked over that observation — a recorded
  non-execution is the step's truthful completion.
- **Step 5 requires Step 2 complete** when granted, so the archival lands under
  a trigger that names the predicate it answers.
- Step 6 runs if operational code moved; checker changes qualify.
- Step 7 requires every prior box checked and every deferral row dated.

---

## Declared scope

The standing always-allowed set remains `STATE.md`, this runbook, and
`docs/cycles/PROGRESS-v0.41.md`. Release-authority precedence applies only at
R-CLOSE. Every pattern below is a literal repository glob.

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

`docs/state-archive/**` and `config/protected-artifacts.json` are allowed **only
for Step 5 and only under Grant E**, and the standing prohibitions bind that.
Without the grant, neither is touched and any diff under them is a violation to
report. `crates/**` and `apps/**` are forbidden outright: no step here needs
production source, and release-authority precedence still carries the manifests
at R-CLOSE. `docs/cycles/**` is a clean pattern; this runbook and
`PROGRESS-v0.41.md` reach the worktree through the standing status set, which is
consulted before forbid, so every closed-cycle document and every untracked
amendment input stays denied.

---

## ACTIVATE

Ordered. The first action is not the declaration.

1. **Fill every observation cell in the deferral table first, in the worktree,
   before the activation commit.** The delivered draft ships 31 template cells.
   Each names v0.41 but carries no ISO date, so `check_trigger_freshness` emits
   one error per row against this runbook if it is committed unfilled. **That
   failure is predicted here, not discovered later**: it is the cost of my
   refusing to write a date onto a measurement I did not take, and it is
   discharged by measuring, never by relaxing the check or by copying v0.40's
   cells forward unchanged.
2. Move the `AGENTS.md` active-cycle declaration to v0.41; create
   `docs/cycles/PROGRESS-v0.41.md`; commit this runbook.
3. Advance review retention through the derived pattern so exactly the
   v0.40–v0.41 pairs are retained; if the derived value and
   `repomix.config.json` disagree, the disagreement is the finding — record it
   before changing either side.
4. Per DR29, leave the `Second STATE.md archival` trigger cell exactly as
   delivered. It matches the current checker spec and must not be corrected here.

**Acceptance criteria.** `cycle-check` resolves v0.41 from the declaration alone
and passes on its first post-activation run; the retention set derives to exactly
two cycles ending at the active one; the attention state is reported as a
measurement rather than asserted; no deferral observation cell remains a
template, and each carries a real date and the active cycle name.

**Done when** the cycle is declared and every governed table is populated from
derivation.

---

## Step 1 · E0 — entering-state reconstruction

Every figure below is a hypothesis produced by reading a source export. No
repository command produced any of them. Confirm or refute against real bytes; a
refuted hypothesis is a finding, not an error to route around.

| # | Hypothesis | How to settle |
|---|---|---|
| H1 | Object graph: release parent `b8fe1c2c1c2c842868a70581dee390939ef68595` → closing commit `cd4fd58b39c855cc769d3696a6b389f735066022` (immediate child) ← local annotated tag object `2287b41558e69bb86490df71b6907a2f0eb73310`; audit child `2c457feb870d62b16a5f9d9ca06aefcb3dc4cf8b` is the closing commit's immediate child and current HEAD | `rev-parse`, `cat-file`, first-parent walk |
| H2 | Remote `main` is `dd605acc037da405fa6b2b5366b09349c330c194`; `v0.17.2` through `v0.17.5` present remotely; `v0.17.6` and `v0.17.7` both absent remotely and present locally; v0.17.6 still carries its withheld record | `ls-remote`, `show-ref`, `merge-base --is-ancestor` |
| H3 | **The v0.17.7 tag checkout still passes.** A fresh detached checkout of the tag passes `cycle-check` with `local-tag-reconciliation=verified` | check out the tag in a detached worktree and run it, rather than citing the prior record |
| H4 | F1 holds: no export trigger bears the name the archival clause references, and the surviving clause is the `STATE.md` boundary at 281,082 bytes' distance | grep every `MAX_EXPORT_BYTES` site; read the pinned spec; measure `STATE.md` |
| H5 | F2 holds: a disposition consisting of any non-`none` sentence satisfies the current predicate | construct one and run the check |
| H6 | F4 holds: the manifest is 200,439 bytes with a 194,191-byte pin array; 9 of 339 pins reference paths present in the export | intersect the pin paths against the export entry set |
| H7 | The delivered export is 2,803,926 bytes / 158 entries, all tracked; attention boundary 2,569,388 with the export 234,538 above it; ceiling headroom 196,074 at the 215,306 high-water denominator | export at the entering tree; run `export-check` and read its reported state |
| H8 | Archivable regions: from the first v0.38 record to end of file 128,859 bytes; from v0.37 105,646; from v0.36 81,841 | measure `STATE.md` directly |
| H9 | Registry 16 rules / 108 controls; exemptions 9; retractions 3; the v0.40 closing checklist reads 317 / 3 / 308 / 308 / 9 with v0.40 at 7/7/7 | run the tools; derive rather than copy any figure a checker prints |

### E0 dated verdicts — 2026-08-04

| # | Verdict | Measured result |
|---|---|---|
| H1 | confirmed | `rev-parse`, `cat-file`, and the first-parent edges derive release parent `b8fe1c2c…` → closing commit `cd4fd58b…` → audit child `2c457feb…`; annotated object `2287b415…` peels to the closing commit. The current E0 HEAD is its two task/audit descendants. |
| H2 | confirmed | Fresh `ls-remote` reads `main=dd605acc…`, exact remote tags v0.17.2–v0.17.5, and no remote v0.17.6/v0.17.7. Both later tags exist locally; State carries the exact permanent-withholding record for v0.17.6. |
| H3 | confirmed | A fresh detached checkout of the real v0.17.7 tag passed `cycle-check` with `local-tag-reconciliation=verified`; no prior-cycle assertion was used as its witness. |
| H4 | refuted in quantity; finding confirmed | Exhaustive `MAX_EXPORT_BYTES` search finds the hard `>` ceiling plus the separately named attention boundary, but no “export ceiling trigger.” Entering State was 172,660 / 453,741 bytes, leaving **281,081**, not 281,082 bytes. |
| H5 | confirmed | Direct construction at the actual `export_attention_errors` entry point with `v0.41 · 2026-08-04 — trigger-fired disposition: aware` returned `[]` while the boundary fired. Any dated non-`none` sentence is presently sufficient. |
| H6 | refuted in two quantities; intersection confirmed | The manifest is **200,440**, not 200,439 bytes. Its JSON array payload is 194,173 bytes; the pin field including key and separator is **194,191** bytes. Exactly **9/339** pins name exported paths: two `.gitattributes`, five evidence/observation records, `run`, and `tools/model_profiles.py`. |
| H7 | confirmed | Exact entering tree export passed at **2,803,926 bytes / 158 tracked entries / two retained cycles**, **234,538** above the 2,569,388 attention boundary and **196,074 / 0.91** high-water cycles below the ceiling. The initial untracked draft worktree separately failed at 2,851,841 / 159, as it must. |
| H8 | refuted | Initial suffixes beginning at v0.38/v0.37/v0.36 were **128,860 / 105,647 / 81,842** bytes, each one above the hypotheses. The regions from those starts to the permanent marker were **84,896 / 61,683 / 37,878** bytes; only those are potentially movable under Grant E. |
| H9 | confirmed | Direct tools derive **16 rules / 108 controls**, **9** exemptions, and **3** retractions. The real v0.17.7 tagged tree derives closing checklist **317 / 3 / 308 / 308 / 9**, with v0.40 at **7/7/7**. The active-cycle ACTIVATE audit then raises the live checked total to 318 without changing the other four figures. |

Plus the standing entering measurements: `git status --porcelain` with its
expected untracked set stated exactly, full `./run ci-local`,
`invariant-scan --self-test`, both complete Python populations, and golden —
counts, not adjectives.

**Acceptance criteria.** Every hypothesis carries a dated verdict: confirmed,
refuted, or unmeasurable with a stated reason. H3 is settled by executing against
the real tag rather than by citing the prior cycle's record. No figure in this
document is treated as established by appearing here.

**Done when** dependent steps start from measurements rather than from this
runbook.

---

## Step 2 · TRIGGER-REACH — point the lever at a trigger that exists

Per F1, DR28, and DR29. The row that names the largest relief lever references
an export trigger by a name nothing bears. Replace that clause with a reference
to the predicate that actually exists, changing the checker spec and the table
row in one commit.

**Planted controls.** A governed row whose trigger clause names a predicate the
repository does not define fails — which is the general defect, not just this
instance. And a state in which the attention predicate is firing while the
archival row reads unfired fails, since that is exactly the condition v0.40
recorded truthfully and which nothing objected to.

Per DR28 the repair must not widen what fires. A control demonstrating that the
archival trigger fires on no export state the attention predicate would not is
what separates the repair from a loosening.

**Acceptance criteria.** The checker spec and the active row move in the same
commit and agree byte-for-byte afterward; both planted controls fail before and
pass after, each anchored at a registered control site; the general control is
expressed over the pinned row specs rather than over this one subject; a
demonstration that the repaired trigger fires on no state the attention
predicate would not is recorded; `./run ci-local` is clean.

**Done when** the relief lever can be reached in the regime that needs it.

---

## Step 3 · DISPOSITION-SUBSTANCE — an answer that a later measurement can test

Per F2 and C24. The attention predicate fired and its required disposition was
satisfied by a true sentence that moved nothing. The predicate constrains its own
presence and nothing else.

Make a fired disposition answerable against a later measurement, per C24 — and
read C24's hard rule before writing the predicate, because the state this project
is in right now is one where the only remaining lever may be ask-first, and a
control that cannot be discharged truthfully in that state is the eighth
author-side unsatisfiable rule rather than a fix.

**Planted controls.** A disposition that restates awareness without a measurable
commitment fails. A disposition that truthfully names an unheld ask-first lever
together with the quantity it would recover **passes** — and that second control
is the one that matters, because a predicate satisfying only the first would
force a false claim or a stall in exactly the situation the project now occupies.

**Acceptance criteria.** Both planted controls fail and pass as stated, each
anchored at a registered control site; satisfiability is proved against the
entering measurements and the proof is recorded before the predicate is adopted;
the predicate applies to governed trigger dispositions generally rather than to
the export row alone, or the narrower scope is recorded with its reason;
`invariant-scan --self-test` totals are stated; `./run ci-local` is clean.

**Done when** "we are aware" is no longer a complete answer to a fired trigger.

---

## Step 4 · REVIEW-SOURCE — stop spending the export on hashes review cannot check

Per F3, F4, C25, and DR31. Nearly seven percent of the review export is a pin
index for bytes the export excludes, and a reviewer can verify nine of its three
hundred thirty-nine entries.

Derive a fourth exclusion class in the shape of the three that already exist, and
decide per C25 what if anything the export keeps in the index's place. The
manifest itself does not change; only what the review export carries does.

**Planted controls.** A path the derivation classifies as excludable but which
the configuration still exports fails, and a configured exclusion the derivation
does not classify fails — non-vacuous in both directions, as the raw-wire class
already is. If a review-relevant head is retained, a control proving its
staleness fails is required; a head that can silently diverge from the manifest
is worse than no head.

**Acceptance criteria.** The class is derived from repository bytes with no
enumerated path list; both direction controls fail before and pass after, each
anchored at a registered control site; the derivation is exercised against the
real pin population and its output reported rather than asserted; the manifest
remains byte-identical unless Grant E's single structural pin lands; the
resulting export size and attention state are stated as measurements; per C25, if
no honest derivation exists that is the recorded finding and the shortfall is
stated rather than a class invented to reach the boundary; `./run ci-local` is
clean.

**Done when** the review export carries what review can use.

---

## Step 5 · ARCHIVE — dormant, Grant E

**Objective.** Execute Grant E exactly, or record its absence truthfully.

If granted: record the grant text verbatim; confirm the archivable region against
real bytes per C26; move the closed-cycle records through v0.38 into a new
append-only file under `docs/state-archive/` following the v0.37 precedent; pin
it at `structural` grade, which the existing derived structural-archive exclusion
then removes from the export without a new mechanism; leave the status header and
the v0.39 and v0.40 records in place. The archived records are not edited in
transit — an archival that rewrites a dated measurement is a prohibited edit
wearing a move.

If not granted: one dated not-granted observation, and the deferral row carries
the exact quantity the grant would have recovered.

**Acceptance criteria.** Either the archive exists with its structural pin and
the derived exclusion removes it, with the archived bytes byte-identical to what
`STATE.md` held before the move and proved so — or the not-granted observation is
recorded with its date and the unrecovered quantity. `STATE.md` remains valid
against its header and boundary controls either way; the protected manifest
changes by exactly one pin or not at all; `./run ci-local` is clean.

**Done when** the largest lever is either spent exactly as authorized, or its
absence is recorded with the number attached.

---

## Step 6 · RE-MEASURE — hosted, conditional

Runs if operational or production code moved; checker changes qualify. Evidence
ref under the standing authority: under `refs/heads/codex/`, naming the active
cycle and a short commit id, with the `ls-remote` absence pre-check recorded,
non-force, exactly one ref created, `main` and every tag untouched. Report run
id, attempt, ref, and blocking identity result. A pre-existing ref is a finding,
not a detail.

If it does not run, record the dated reason and name which claims rest on local
execution only.

**Acceptance criteria.** Either a hosted run is reported with its id, attempt,
ref, and blocking identity result, and the remote readback shows `main` and every
tag unmoved — or the dated skip reason is recorded together with the claims that
consequently rest on local execution alone. The absence pre-check is recorded
either way.

**Done when** every claim in this cycle names the machine that witnessed it.

---

## Step 7 · R-CLOSE

The established two-commit tagged close, with the v0.40 gate now standing: release
parent → assembled closing worktree → **run the pre-tag gate and require it to
pass** → closing commit → local annotated tag → **append-only audit child as the
immediate next commit**, carrying
`- cycle-ending review-export audit: closing_tree=…; bytes=…; audit_delta=…`
measured against the closing tree it follows. The audit child is the final commit
of v0.41 and the next cycle's entering ref. Every other criterion is evaluated at
the assembled closing worktree; the audit-field criterion alone at the audit
child.

The `STATE.md` header spends the release-commit assertion phrase on this release's
parent and nothing else; historical objects are named in wording that does not
spend it.

**Acceptance criteria.**

- The pre-tag gate passed at the assembled closing worktree, before the tag
  existed, and its verdict is recorded.
- **A checkout of the new annotated tag passes `cycle-check`**, as v0.17.7's did.
- Dated disposition per DR32, naming any behaviour movement rather than letting
  the version imply its absence; the serialized-field clause adjudicated against
  the R15 manifest diff.
- `version-check` passes with authorities and restatements counted.
- `checklist-audit` passes with all figures stated inline in the closing record
  and a non-zero v0.41 line.
- The governed export row is bound; the audit child is present in the stated
  order; `audit_delta` reconciles against the closing tree.
- Per DR33 a fresh dated post-push record for each authorized release ref.
- Every deferral row carries a dated v0.41 observation, with the archival row's
  trigger reflecting Step 2's repair and the capacity row reporting the attention
  state as a measurement.
- If the attention predicate is still firing, its disposition satisfies Step 3's
  predicate on its own terms — the cycle's own control applied to the cycle.
- `invariant-scan --self-test`, both Python populations, and golden: counts
  stated, zero hand-typed absolute finding-line fields.
- Headroom restated in bytes, percent, and cycles at the derived denominator,
  with the recovery attributed to each lever separately and the exact shortfall
  stated if the boundary is not cleared.
- Publication moves only `main`, v0.17.7, and the new release tag under the
  initiating authorization; v0.17.6 and every other ref remain untouched.
- No process instruction left inside a dated record.

**Done when** the cycle is closed, audited, truthfully represented, and the
handoff written.

---

## Closing-record assembly template

*Assembled at Step 7 in the established field form, with every figure stated
inline. The release identity, evidence candidate, hosted run, governed export,
artifact boundaries, attention state and its disposition, deferral disposition,
divergence disposition, scope reconciliation, publication boundary, checklist
reconciliation, golden reconciliation, and the pre-tag and post-tag gate verdicts
each carry their measured values. This tree contains no annotated-tag-object
field; the local annotated tag targets the closing commit only after it exists.*

---

## Governed artifact byte-boundary authority

- governed artifact byte boundary: path=`STATE.md`; bytes=`453741`
- governed artifact byte boundary: path=`config/protected-artifacts.json`; bytes=`1048576`

**Carried forward byte-identically.** A change to either figure is an
architectural change requiring its own justification and operator authorization.
The 3,000,000-byte review-export ceiling remains separately governed and is not
moved by this cycle.

---

## Deferred means deferred

The full carry-forward population from the immediately prior runbook with every
trigger unchanged. **Per DR29 the `Second STATE.md archival` trigger cell below
is the current checker-pinned text and is not corrected here** — Step 2 moves it
together with the spec. **Each observation cell is a template.** ACTIVATE
replaces each with a dated v0.41 measurement before any semantic acceptance, and
Step 7 replaces them again with close measurements. A template surviving into any
acceptance point is a defect, not an oversight.

| Deferred item | Unchanged trigger | Measured observation (cycle-identified) | v0.41 action |
|---|---|---|---|
| `v0.17.6` publication, tag movement, or deletion | any proposal to publish, move, re-point, or delete the `v0.17.6` tag, its object, or its target | v0.41 · 2026-08-04 — Local annotated object `66ee2cbbe374b99722bec49b8176571777aaa899` still peels to `7c9305f01219412048ec75236f2bf1e61112c178`; fresh remote readback returns no v0.17.6 ref. No proposal arose; DR22 remains permanent. | none |
| T7 robots single-flight | a second concurrent harvester | v0.41 · 2026-08-04 — No harvester was started during activation, so no second concurrent harvester appeared and the trigger did not fire. | none |
| NEGATIVE-CACHE Decision B | a live transient robots outage for an admitted publisher while a usable last-known-good policy exists, plus operator authorization | v0.41 · 2026-08-04 — No publisher wire was touched and no Decision B authorization was issued; neither half of the combined trigger fired. | none |
| Conditional GET (`ETag` / `If-Modified-Since`) | an operator-authorized cycle whose scope permits the `net` request path plus a live 304 observation | v0.41 · 2026-08-04 — The declared scope forbids the production net path and no live 304 was observed; the trigger did not fire. | none |
| `edgar:*` extension field mapping | an operator-authorized cycle permitting `crates/ingest/src/**` for mapping, with a connector review | v0.41 · 2026-08-04 — `crates/ingest/src/**` is forbidden and no connector review occurred; the trigger did not fire. | none |
| Live multi-publisher behaviour in one runtime | further origins beyond the two configured, or concurrency | v0.41 · 2026-08-04 — Configuration still has two network publisher origins; no live or concurrent runtime ran, so neither clause fired. | none |
| First recurring scheduled SEC run | explicit operator authorization of a bounded scheduled window, separate from any cycle scope | v0.41 · 2026-08-04 — No scheduled-window authorization was issued and no scheduled run executed; the trigger did not fire. | none |
| Postgres / pgvector / multi-host seam | unchanged | v0.41 · 2026-08-04 — No Postgres, pgvector, or multi-host seam was introduced. | none |
| A4 untrusted-shell boundary | a third-party/untrusted shell, or any claim HC1 is invariant under shell replacement | v0.41 · 2026-08-04 — No third-party shell appeared and no shell-replacement-invariant HC1 claim was made. | none |
| L2 forced-command wrapper | an operator server session | v0.41 · 2026-08-04 — No operator server session occurred, so the trigger did not fire. | none |
| R3/R4 open-bottom coverage | a spelling outside registered vocabulary | v0.41 · 2026-08-04 — The registered self-test passes 16/16 rules and 108 controls; no outside spelling was found. | none |
| `--features net` Rust 1.86 execution | a scoped cycle authorized to change evidence topology and an executable local or hosted lane that actually pins and runs the net path on Rust 1.86 | v0.41 · 2026-08-04 — Workflow and evidence topology remain forbidden; the latest pinned lane remains v0.40 hosted run `30896642221`, whose Rust 1.86 success and 1.85 refusal identities passed. | none |
| GitHub attestation verifier version admission | the installed or proposed `gh attestation verify` version differs from the exact repository pin, or its accepted bundle/workflow contract changes | v0.41 · 2026-08-04 — No verifier version, pin, bundle contract, or workflow contract changed; the trigger did not fire. | none |
| Third configured publisher | a completed compliance review, then a separate admission decision | v0.41 · 2026-08-04 — No third-publisher compliance review or admission occurred. | none |
| `v0.8.0` / `v0.10.2` publication | operator-authorized push of both exact annotated objects | v0.41 · 2026-08-04 — Fresh remote readback returns neither historical tag; the publication authorization for this cycle does not name those objects, so the trigger did not fire. | none |
| `--skip-local-tag-verification` removal | both historical tags published plus a passing hosted full-history `cycle-check` without the flag | v0.41 · 2026-08-04 — The v0.17.6 withheld-hosted admission remains the bounded topology case; neither historical tag is remote and no full-history no-skip hosted pass occurred. | none |
| Manifest retention/indexing | the manifest reaches its governed artifact byte boundary, or two consecutive clean `./run verify-artifacts` runs each take ≥1.00 s real | v0.41 · 2026-08-04 — The manifest is **200,440 / 1,048,576 bytes**; two complete checks matched 3 artifacts / 339 pins in **0.10 s / 0.10 s real**. Neither clause fired. | Step 4 |
| Version literal in `app.py` | a cycle whose declared scope permits shell source changes | v0.41 · 2026-08-04 — Shell production source is absent from `allow`; release-authority precedence has not moved the literals during activation. | Step 7 |
| Release-classification criteria with no executed control | an operator decision that prose adjudication is insufficient | v0.41 · 2026-08-04 — R15 reports **0 differences / 6 routes / 112 field occurrences**; patch remains the expected disposition and no operator decision displaced the R-CLOSE boundary. | Step 7 |
| Second `STATE.md` archival | the review-export attention predicate fires, or `STATE.md` reaches its governed artifact byte boundary | v0.41 · 2026-08-04 — State is **178,178 / 453,741 bytes**. Governed review-export **2,789,050** meets the **2,569,388-byte** attention boundary while the State boundary does not, so the repaired attention clause fires. trigger-fired disposition: Grant E is not held and the measured **84,896-byte** v0.38 archival lever remains unexecuted; Step 2 makes the reachable predicate exact without changing either threshold. | Step 2 and Step 5 |
| Retention derivation across a version-family boundary | an active cycle whose name is not of the form `v0.<n>` — raising at `v1.0`–`v1.2`, silently under-excluding from `v1.3` onward | v0.41 · 2026-08-04 — Active cycle v0.41 remains in the `v0.<n>` family, so the trigger did not fire. | none |
| Published-release divergence | the unpublished distance contains a measured runtime behaviour difference persisting across three consecutive closed cycles within the current publication epoch, or acquires any public-surface change | v0.41 · 2026-08-04 — The v0.17.5 publication epoch remains at **0** because v0.17.6 is withheld and v0.17.7 carries no runtime difference; R15 reports zero public-surface differences. Neither clause fired. | Step 7 |
| MSRV current-restatement membership | a current restatement of either Rust floor lands outside the registry without failing a check | v0.41 · 2026-08-04 — `version-check` derives **3** offline pins, **22** current floor restatements, and **3** release restatements across **589** tracked files; no unregistered current restatement appeared. | none |
| Retention arithmetic fallback | the retention formatter again permits an omitted retained set, or any live production or fixture caller supplies a set not derived by `expected_retained_cycle_paths` for that root | v0.41 · 2026-08-04 — Activation advances the derived retained set to exactly v0.40–v0.41; no omitted or non-derived caller appeared. | none |
| Optional cycle-ending audit disclosure | a closed cycle whose delivered export differs from its governed figure and which records no cycle-ending audit field | v0.41 · 2026-08-04 — Step 7 reserves the mandatory audit field for its immediate audit child; the active cycle is open, where such a field is correctly unavailable. | Step 7 audit child |
| License enum semantics | a second publisher requires an inexpressible license value | v0.41 · 2026-08-04 — No publisher work occurred and no inexpressible license value appeared. | none |
| Terms-level automated-access gate | a candidate's terms restrict beyond robots.txt | v0.41 · 2026-08-04 — No fresh terms were fetched; the pinned SEC operator determination remains standing and no new candidate appeared. | none |
| Feed shape observation | an uncovered publisher feed shape | v0.41 · 2026-08-04 — No feed was fetched and no uncovered shape appeared. | none |
| Threshold-authority limitation | a common dependency module or manifest edge appears between store and view | v0.41 · 2026-08-04 — The already-recorded shared `intel-extract` seam remains; no new dependency module or manifest edge appeared. | none |
| ARCHITECTURE.md §8 / AGENTS.md R-CLOSE tag-mechanics duplication | the restatements diverge | v0.41 · 2026-08-04 — The two in-scope restatements still agree after activation; no divergence appeared. | none |
| Review-export capacity | the export meets or exceeds the executable two-governed-growth-cycle attention boundary | v0.41 · 2026-08-04 — Exact entering commit `2c457feb870d62b16a5f9d9ca06aefcb3dc4cf8b` exports **2,803,926 bytes**, **234,538 bytes above** the 2,569,388-byte attention boundary and **196,074 bytes / 6.54% / 0.91 high-water cycles** below failure. No relief lever has yet moved; the predicate fires and Step 3 must make its disposition measurable. | Step 4 |

---

## Standing prohibitions

- `docs/state-archive/**` and `config/protected-artifacts.json` are touched only
  by Step 5 and only under Grant E. Without the grant, any diff under them is a
  violation to report.
- No archived record edited in transit. Moving a dated measurement is permitted;
  changing one is not.
- The `v0.17.6` tag, its object, and its target are never moved, deleted,
  re-pointed, or published.
- No closed-cycle document, observation, fixture, or immutable local record
  edited; corrections are forward and dated.
- No push beyond the standing evidence-ref authority. No force-push, ref
  deletion, or tag movement anywhere, ever.
- No tag created before the pre-tag gate has passed at that tree.
- No wire request of any kind.
- No expectation, anchor, or figure copied from a checker's own output where the
  construction can produce it independently.
- No acceptance criterion discharged by inspection where a registered
  self-testing rule with an executable `fail_before` can exist.
- No hardcoded scope list where the scope can be derived.
- No acceptance discharged by an executable whose witness set is empty.
- No change that reduces the reach of an existing control, or widens a trigger,
  in order to make a failure disappear.
- No retraction added without quoting the bar and obtaining an operator decision.
- The three untracked amendment inputs are not edited, moved, renamed, or
  deleted.

---

## Cycle checklist

- [x] ACTIVATE
- [x] E0
- [x] TRIGGER-REACH
- [ ] DISPOSITION-SUBSTANCE
- [ ] REVIEW-SOURCE
- [ ] ARCHIVE
- [ ] RE-MEASURE
- [ ] R-CLOSE

*Box ids match the `PROGRESS-v0.41.md` entry ids exactly; the box-coverage rule
audits this runbook like any other.*

---

## Handoff

One report: each DR executed and whether any measurement refuted its basis; each
C-determination with its reasoning and its falsifier; every stop condition
triggered or an explicit none; the Grant E outcome, executed or not-granted with
the unrecovered quantity; the closing export with recovery attributed to each
lever separately; and the v0.42 findings list — findings, not proposed acceptance
criteria.

Then one operator question, stated with numbers rather than as a reminder.

**The trend, which is not a capacity question.** Per F5, growth is concentrated
in checker source, checker tests, the rule registry, and dated records —
+60,129 bytes in the last cycle with production code unmoved. That is the
apparatus this project's discipline requires, and it grows because the discipline
is working. Exclusion and archival buy cycles. After them the remaining levers
are the operator-selected 3,000,000-byte ceiling, the two-cycle retention depth,
and what "review source" means. The handoff states the measured runway in cycles
at the high-water denominator so that decision arrives with numbers attached
rather than as an emergency.

---

## Provenance

**Measured on the delivered post-v0.40 export (2,803,926 bytes / 158 file
entries, reconciling with the reported 2,801,474-byte closing tree plus a
2,452-byte audit-child append):** the pinned `GOVERNED_ARTIFACT_ROW_SPECS`
clause for `Second STATE.md archival`, and every `MAX_EXPORT_BYTES` site in
`export_check.py`, which together are F1's whole basis; `TRIGGER_FIRED_DISPOSITION_RE`
and its non-`none` acceptance, which is F2's; the v0.40 deferral row that reads
the clause against the fixed ceiling and records `none`, which is F1 landing in
practice; the attention boundary at 2,569,388 with its 215,306-byte high-water
denominator and 430,612-byte reserve, all recomputed rather than read; the
manifest at 200,439 bytes with its 194,191-byte pin array, its 339 pins, their
top-level prefixes, and the 9-of-339 intersection with the export entry set;
`derived_required_paths` and the three existing derived exclusion classes, which
is why a fourth class is the constructible shape; per-file deltas against the
prior delivered export totalling +60,129 with production code at zero; the
`STATE.md` cycle-record offsets giving 128,859 / 105,646 / 81,841 bytes for the
v0.38 / v0.37 / v0.36 boundaries; the hoisted `tag_independent_verdict` and the
HEAD-gated `pre-tag` return, confirming v0.40's Step 2 landed with both controls
satisfiable; the `permanently-withheld` labelled field and the `withheld-hosted`
admission; and the registry at 16 rules / 108 planted controls counted from
`config/invariant-rules.json` directly.

**Verified unchanged against the checker that will scan this runbook:**
`STEP_HEADING_RE`, `DEFERRED_HEADING`, `AMENDMENTS_HEADING`,
`AMENDMENT_ENTRY_RE`, `CONTRACT_FIELD_LABELS`, `SCOPE_HEADING_RE`,
`SCOPE_CLASSES`, `STEP_REFERENCE_RE`, the quantity-clause predicate, the
declared-scope pattern-population control, and the pinned archival trigger text
this table reproduces verbatim per DR29.

**What I could not measure and marked as hypotheses:** anything requiring `.git`
or the network — the object graph, remote refs, ancestry, local tag identity, and
whether the v0.17.7 tag checkout still passes, which H3 requires executing rather
than citing. The projected close figures in §6 are arithmetic over measured
inputs, not measurements.

**What I did not do:** no repository command, no wire request, no test run, no
push. Every figure above is for Step 1 to confirm against real bytes.
