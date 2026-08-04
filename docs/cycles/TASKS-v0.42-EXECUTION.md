# TASKS-v0.42-EXECUTION.md — the published side of the world has no executed control

## Runbook amendments

**Cycle:** v0.42
**Entering release:** v0.17.8, **published**; v0.17.7 published; v0.17.6
permanently withheld and local-only; v0.17.5 published
**Entering ref (hypothesis):** local-only audit child
`827192d2b3ed56fbe04ac0df0cc6536ef037e066`, one commit ahead of published
`main` at `993813c755e9f759a4ee165954c7a1df984f6b10`
**Prior cycle:** v0.41 — closed, published, and fully discharged. Every step
landed; two of them landed better than specified.
**Autonomy:** the standing `CYCLE_AUTONOMY_AUTHORITY` block governs. Every
decision is taken in §3 or delegated in §5 with a decision rule and a required
falsifier. Two milestone steps are **dormant by construction** and execute only
under their named grants, recording dated not-granted observations otherwise. No
operator question is routed mid-cycle.

**This cycle is worth running with no grant issued.** Its P1 subject needs no
authorization at all; both grants are repairs and relief, not the substance.

Amendment entries, if any step's contract changes mid-cycle, are appended below
this line in the form `Step N — <what changed> — YYYY-MM-DD`.

---

## 0. Why this cycle exists

v0.41 discharged everything and two steps exceeded their contracts. TRIGGER-REACH
did not merely repair the dangling clause — it replaced free-prose trigger text
with a registry of predicate identifiers, so `GOVERNED_ARTIFACT_ROW_SPECS` now
names `review-export-attention` and `state-artifact-byte-boundary` and the row
text is *derived* from them. A cross-reference can no longer dangle, because
there is no longer a string to dangle. DISPOSITION-SUBSTANCE produced structured
dispositions — `kind=unheld-lever; lever=Grant E; recoverable_bytes=84896` and
`kind=measured-change; subject=review-source export; baseline_bytes=2803926; …`
— so the archival row now names its unspent lever with a number attached, which
is exactly the second planted control existing to be satisfiable. REVIEW-SOURCE
recovered 146,241 bytes. And the assembled self-test caught that R12/53 still
hard-coded v0.40's governed export value and had stopped mutating the live row —
the derive-don't-assert discipline catching itself mid-cycle.

Then the operator authorized publication, and v0.41 became the first cycle to
create and publish a release in the same cycle. That is a lifecycle shape the
protocol has never specified, and my runbook did not anticipate it — DR33 said
the close defaults to unpublished-local and nothing described what to do if a
grant arrived. Codex improvised, correctly, and disclosed the result.

The result is this. Published `main` is the closing commit. The audit child is
one commit ahead, local-only, and it carries 1,519 bytes of append — of which
1,396 is the post-push publication audit paragraph holding both five-field
verification records, and the remainder reaches
`PROGRESS-v0.41.md`'s `cycle-ending review-export audit`. So a reader of the
published repository sees a closed v0.41 with **no cycle-ending export audit
field and no evidence that the publication was verified**. The local tree has
both.

Every prior publication pushed `main` to an audit child that already existed,
because the release being published had been created a cycle earlier. Publishing
in the same cycle makes the audit child necessarily post-publication, so it can
never appear in its own published tip.

That is the visible symptom. The cause underneath it is larger, and measuring it
is what makes this cycle worth running:

**`ls-remote` appears zero times in `run` and zero times in every `tools/*.py`.**

Every remote fact in these records — "remote `main` remained `dd605acc`", "no
v0.17.8 tag existed", "direct readback found v0.17.7 peeling to `cd4fd58b`" — is
a hand-run command whose output was transcribed into prose. Nothing executes it,
nothing re-derives it, and nothing fails if a transcription is wrong. In a
project whose whole discipline is that a claimed property nothing executes is not
a property, the published side — the only externally visible surface, the one the
retraction bar attaches to, the one whose preconditions make an irreversible push
safe — is governed entirely by prose.

To be fair to what does exist: a plain non-force push fails on its own if the
remote has diverged, and the hosted run on the published commit is real external
verification. The protection is not zero. But no control compares the published
tip against the local record, and no control re-derives a single remote fact the
records assert.

---

## 1. Findings carried in

| # | Priority | Finding | Measured basis |
|---|---|---|---|
| F1 | **P1** | No executed control reads remote state | `grep -c ls-remote` returns **0** for `run` and **0** across every `tools/*.py`. `cycle_check.py` mentions `origin/main` only to *prohibit* asserting a literal hash. Every remote precondition, readback, and absence observation in the records is a transcription. |
| F2 | **P1** | The published tip is a strictly weaker record than the local tip, and nothing measures the gap | Published `main` is `993813c755e9f759a4ee165954c7a1df984f6b10`. `STATE.md` measured 192,892 bytes at the assembled closing worktree and 194,411 as delivered — a 1,519-byte audit-child append, of which the post-push publication audit paragraph is **1,396**. `PROGRESS-v0.41.md` carries `closing_tree=993813c7…; bytes=2674239; audit_delta=+16554` in that same unpushed commit. The `Optional cycle-ending audit disclosure` trigger reads "a closed cycle … which records no cycle-ending audit field" — true of the published view, false of the local one, and the row was evaluated against the local one. |
| F3 | **P1** | Same-cycle publication is an unspecified lifecycle shape | v0.17.5's audit child `dd605acc` is recorded as "preserved in published history" because it existed before the push. v0.17.8 was created and published in one cycle, so its audit child post-dates the push by construction. The protocol names no ordering for this, and my v0.41 runbook assumed it could not occur. The audit child carries two separable payloads — the export audit, measurable at the closing tree before any push, and the post-push record, which cannot exist until after. |
| F4 | **P1** | Capacity: the levers no longer clear the boundary | Delivered export 2,675,890 bytes, reconciling with the reported 2,674,239-byte closing tree plus a 1,651-byte audit-child append. Headroom 324,110 bytes, 10.80%, **1.51 high-water cycles**; **106,502 bytes above** the 2,569,388-byte attention boundary, firing for a third consecutive cycle. The v0.40 pair drops 82,012 at retention, leaving roughly 2,593,878 — still 24,490 above. Grant E's lever measures **84,896** — not the ~128,859 I projected, a 52% overestimate that is mine — which would reach roughly 2,508,982, clearing by 60,406. But underlying growth net of the manifest exclusion was **+72,403** last cycle, which returns the close to roughly 2,581,385, about 12,000 **above** the boundary again. `STATE.md` is 194,411 of 453,741, 42.8%, up 21,752 this cycle. |

---

## 2. Grants — exact required content, both dormant until issued

Neither is assumed, implied, or partially in force. Each is in force only when the
operator has issued it with at least the content below; Codex records the grant
text verbatim in the progress log before the gated step runs.

### Grant E — second `STATE.md` archival

> Authorize a second structural archival of `STATE.md`: move the closed-cycle
> records through v0.38 into a new append-only file under `docs/state-archive/`,
> pin it at `structural` grade in the protected manifest, and leave the status
> header and the v0.39 through v0.41 records in place. No other byte moves.

Recommendation: **issue it**, with the correction that it no longer suffices. At
the measured 84,896 bytes it clears the boundary at activation and, on last
cycle's growth, does not hold that clearance to the close. It remains the largest
lever that needs no new mechanism, and spending it does not foreclose anything.

### Grant F — advance `main` to the v0.41 audit child

> Authorize one non-force fast-forward of `refs/heads/main` from
> `993813c755e9f759a4ee165954c7a1df984f6b10` to the exact v0.41 audit child
> `827192d2b3ed56fbe04ac0df0cc6536ef037e066`. No tag moves and no other ref moves.

Recommendation: **issue it.** This publishes one commit whose entire content is
dated records — the post-push verification of a publication that already happened
and the cycle-ending export audit of a tree that is already published. It moves
no tag, changes no artifact, and repairs the F2 gap for v0.41 specifically rather
than leaving it permanent. Preconditions are measured immediately before the push
and a mismatch is a stop.

The ref identities above are hypotheses at authoring time and are re-measured
immediately before any push. A grant does not transfer to different objects.

---

## 3. Decisions taken — do not re-litigate

If a measurement refutes a stated basis, record the refutation, stop that step,
continue with the rest, and surface it at handoff.

### DR34 — the audit child's two payloads are separated

The cycle-ending export audit is measurable at the closing tree and does not
require a push. The post-push verification record cannot exist before one. They
travel together today only because they have always been written together. Per
DR35 they stop travelling together.

### DR35 — same-cycle publication has a specified ordering

Release parent → closing commit → annotated tag → **audit child carrying the
export audit alone** → push `main` to that audit child together with the tags →
post-push verification record appended in a later commit, as every prior cycle
has done. This restores the historical shape in which the published tip carries
its own cycle's export audit, and it is what F3 shows the protocol was missing
rather than an invention. C29 owns its exact expression and controls.

### DR36 — I own the DR33 gap and the projection error

My v0.41 runbook stated that the close defaults to unpublished-local and gave no
ordering for a grant arriving mid-cycle, so the first same-cycle publication ran
without a specified shape. And §6 of that runbook projected the archival lever at
roughly 128,859 bytes against a measured 84,896 — 52% high — which materially
overstated the case for Grant E at the moment the operator was weighing it. Both
are recorded as author-side, not execution, errors.

### DR37 — no ceiling and no retention-depth movement

The 3,000,000-byte ceiling and the accepted two-cycle retention depth are
operator-selected and stay. Per F4 the remaining levers after Grant E are all
ask-first, and that is a decision to put to the operator with numbers, not one to
take inside a cycle. If the measured recovery does not clear the boundary, the
exact shortfall is recorded under the structured disposition v0.41 built.

### DR38 — version disposition rule, carried

DR20's three clauses govern unchanged, in precedence order: minor for a new route
or observable named surface; minor for any addition, removal, or redefinition of
a value in the domain of a serialized `/v1/*` field, adjudicated against the R15
manifest diff rather than prose; otherwise patch. Remote measurement, publication
ordering, and archival are none of these. Expected: **patch v0.17.9**; the
reasoning is recorded either way. A manifest diff showing domain movement is a
stop under §4.

### DR39 — the v0.42 close defaults to unpublished-local

Grant F authorizes one fast-forward to an existing commit and nothing else;
Grant E authorizes archival and nothing else. Neither authorizes publishing a
v0.42 release. If the operator issues a publication grant mid-cycle, **DR35's
ordering applies from that moment** — which is precisely the gap DR36 owns, now
closed in advance.

---

## 4. Retained gate and stop conditions

**Publishing a release tag, or moving `main` beyond Grant F's exact
fast-forward, requires separate exact operator authorization.** No push beyond
Grant F and the standing evidence-ref authority.

Stop-and-report conditions — halt the affected step, record the measurement,
continue unaffected work, surface at handoff:

1. A measurement indicates a **published** record contains a false claim. This
   now covers everything reachable from published `main`, including the v0.35
   through v0.41 records and both published closing trees.
2. A measurement indicates an **immutable local record** contains a false claim.
3. **A measurement shows the published tip contradicting the local record**, as
   opposed to merely lagging it. Lag is F2 and is repaired by Grant F;
   contradiction is a different thing and stops.
4. A change would move an entitlement or licensing outcome, a golden input, a
   protected database, an `observation`-grade byte, a dependency resolution, or
   any manifest pin other than the single `structural` pin Grant E adds.
5. Any `/v1/*` payload byte or manifest domain moves outside a declared
   disposition.
6. A change would move an accepted boundary or ceiling — including the
   3,000,000-byte export ceiling, the two-cycle retention depth, and both
   governed artifact byte boundaries — or would narrow the attention reserve.
7. Any live publisher request of any kind.
8. Any proposal that would move, delete, re-point, or publish the `v0.17.6` tag.

---

## 5. Codex-owned determinations

Measure, decide, record the reasoning and the falsifier. A recorded decision
naming what would have changed it is complete work; a question routed to the
operator inside this scope is not.

### C28 — how remote state becomes an executed measurement

Decide what an executed remote control reads, where it lives, and how its output
enters the records so that a transcription cannot silently disagree with it.
Publication preconditions, tag absence, ref identity, and the published tip's
relationship to local HEAD are all candidates; measure which of them the records
currently assert and cover those.

**Hard rule, and it is the half that matters.** The control must not make an
offline or network-restricted run fail. Local `ci-local`, hosted CI, and any
sandboxed execution must all still pass with the network absent — the correct
behaviour there is a recorded `unavailable` verdict that is *visible in the
output*, never a silent pass and never a failure. A control that requires the
network to succeed is an author-side unsatisfiable rule in a project whose
verification runs in three environments, and this lineage has owned eight of
those. Prove satisfiability in the offline case before adopting the control, and
record that proof.

### C29 — the exact expression of DR35's ordering, and its controls

Decide where the same-cycle ordering is stated — `AGENTS.md` R-CLOSE,
`ARCHITECTURE.md` §8, or both under the existing pointer discipline — and what
executes it. Rule: the property to enforce is that a cycle's own export audit is
present in whatever commit that cycle publishes, if it publishes. Planted
controls in both directions: a same-cycle publication ordering that would leave
the export audit outside the published tip fails, and the historical
cross-cycle shape, where the published audit child carries the prior cycle's
audit, still passes. A control that only recognizes the new shape breaks every
prior cycle's record.

### C30 — the archival boundary, if Grant E is issued

Grant E names v0.38 and retains v0.39 through v0.41. Measure the region against
real bytes before moving anything; the previously projected and measured figures
disagreed by 52% and the measured one governs. Follow the v0.37 archival
precedent for naming and pinning, so the existing derived structural-archive
exclusion removes it with no new mechanism. Rule: the boundary is chosen once and
the archive is immutable after; if the measured region disagrees with the grant's
wording, stop and report rather than choosing a different boundary than the one
authorized.

### C31 — anything E0 surfaces

Standing latitude to add rules and planted controls; none to add acceptance
criteria that nothing executes.

---

## 6. Dependency gates

- Steps 2 and 3 require **Step 1 complete**; they are otherwise independent.
- Step 3 executes only under Grant E; Step 4 only under Grant F. Otherwise each
  records a dated not-granted observation and its box is checked over that
  observation — a recorded non-execution is the step's truthful completion.
- **Step 4 requires Step 2 complete** when granted, so the fast-forward is made
  and verified under the executed remote control rather than under transcription.
- Step 5 runs if operational code moved; checker changes qualify.
- Step 6 requires every prior box checked and every deferral row dated.

---

## Declared scope

The standing always-allowed set remains `STATE.md`, this runbook, and
`docs/cycles/PROGRESS-v0.42.md`. Release-authority precedence applies only at
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
for Step 3 and only under Grant E**, and the standing prohibitions bind that.
Without the grant, neither is touched and any diff under them is a violation to
report. `run` is allowed because C28 may place the executed remote control there.
`crates/**` and `apps/**` are forbidden outright; release-authority precedence
still carries the manifests at R-CLOSE. `docs/cycles/**` is a clean pattern; this
runbook and `PROGRESS-v0.42.md` reach the worktree through the standing status
set, which is consulted before forbid.

---

## ACTIVATE

Ordered. The first action is not the declaration.

1. **Fill every observation cell in the deferral table first, in the worktree,
   before the activation commit.** The delivered draft ships 31 template cells.
   Each names v0.42 but carries no ISO date, so `check_trigger_freshness` emits
   one error per row against this runbook if it is committed unfilled. **That
   failure is predicted here, not discovered later**: it is the cost of my
   refusing to write a date onto a measurement I did not take, and it is
   discharged by measuring, never by relaxing the check or by copying v0.41's
   cells forward unchanged.
2. Move the `AGENTS.md` active-cycle declaration to v0.42; create
   `docs/cycles/PROGRESS-v0.42.md`; commit this runbook.
3. Advance review retention through the derived pattern so exactly the
   v0.41–v0.42 pairs are retained; if the derived value and
   `repomix.config.json` disagree, the disagreement is the finding — record it
   before changing either side.
4. The `Second STATE.md archival` trigger cell is delivered as the text the
   predicate registry now derives. Leave it exactly as delivered; the registry is
   the authority and this table follows it.

**Acceptance criteria.** `cycle-check` resolves v0.42 from the declaration alone
and passes on its first post-activation run; the retention set derives to exactly
two cycles ending at the active one; the attention state is reported as a
measurement rather than asserted; no deferral observation cell remains a
template, and each carries a real date and the active cycle name.

**Done when** the cycle is declared and every governed table is populated from
derivation.

---

## Step 1 · E0 — entering-state reconstruction

Every figure below is a hypothesis produced by reading a source export. No
repository command produced any of them, and this cycle's subject makes one
category especially untrustworthy: everything about the remote is, at authoring
time, a transcription of a transcription. Confirm or refute against real bytes
and real refs; a refuted hypothesis is a finding, not an error to route around.

| # | Hypothesis | How to settle |
|---|---|---|
| H1 | Object graph: release parent `5bd805214cb72ed694c83e9eec1ce6d17396a69e` → closing commit `993813c755e9f759a4ee165954c7a1df984f6b10` (immediate child) ← published annotated object `4a477722df218059097ff648a07379ec5683dd08`; audit child `827192d2b3ed56fbe04ac0df0cc6536ef037e066` is the closing commit's immediate child and current HEAD | `rev-parse`, `cat-file`, first-parent walk |
| H2 | **Remote reality.** `main` is exactly the closing commit; v0.17.7 and v0.17.8 present with the recorded objects and peels; v0.17.6 absent; local HEAD is exactly one commit ahead of published `main` | direct `ls-remote` and `merge-base`, run and captured rather than restated |
| H3 | F2 holds: the audit-child append is 1,519 bytes, the post-push paragraph 1,396 of them, and `PROGRESS-v0.41.md`'s `cycle-ending review-export audit` field is in that same unpushed commit | diff the two trees; read the field's blob at each |
| H4 | F1 holds: zero `ls-remote` occurrences in `run` and in every `tools/*.py`, and no executed control reads any remote fact | grep the tree; enumerate which recorded remote assertions have an executing witness and which do not — **the enumeration is the deliverable**, not the count |
| H5 | The published tip lacks v0.41's cycle-ending export audit field, so the `Optional cycle-ending audit disclosure` trigger is true of the published view and false of the local one | check out published `main` in a detached worktree and look |
| H6 | The delivered export is 2,675,890 bytes / 157 entries, all tracked; attention boundary 2,569,388 with the export 106,502 above it; headroom 324,110 at the 215,306 high-water denominator | export at the entering tree; run `export-check` and read its reported state |
| H7 | Grant E's lever measures near 84,896 bytes at the v0.38 boundary, and `STATE.md` is 194,411 of 453,741 | measure `STATE.md` directly; the measured figure governs over any projection in this document |
| H8 | Registry 16 rules / 115 controls; exemptions 9; retractions 3; the v0.41 closing checklist reconciles at 325 items | run the tools; derive rather than copy any figure a checker prints |

### Step 1 measured verdicts — 2026-08-05

| # | Verdict | Executed result |
|---|---|---|
| H1 | **confirmed** | `rev-parse`, `cat-file`, and the first-parent walk prove release parent `5bd805214cb72ed694c83e9eec1ce6d17396a69e` → closing commit `993813c755e9f759a4ee165954c7a1df984f6b10` → audit child `827192d2b3ed56fbe04ac0df0cc6536ef037e066`, each as an immediate child. Annotated object `4a477722df218059097ff648a07379ec5683dd08` peels to the closing commit. At the entering measurement, the audit child was exact HEAD. |
| H2 | **confirmed at entry** | Direct `ls-remote` reads `main=993813c755e9f759a4ee165954c7a1df984f6b10`; v0.17.7 is annotated object `2287b41558e69bb86490df71b6907a2f0eb73310` peeling to `cd4fd58b39c855cc769d3696a6b389f735066022`; v0.17.8 is annotated object `4a477722df218059097ff648a07379ec5683dd08` peeling to exact main; v0.17.6 is absent. `merge-base` proves entering HEAD was main's one-commit descendant. ACTIVATE has since added its required implementation and audit commits locally; no remote ref moved. |
| H3 | **refuted by one byte** | The exact audit-child `STATE.md` append is **1,520 bytes**, not 1,519. Its post-push section is exactly **1,396 bytes**, and the same audit child adds v0.41's `cycle-ending review-export audit` field to `PROGRESS-v0.41.md`. |
| H4 | **confirmed** | `rg` finds **zero** `ls-remote` occurrences in `run` and `tools/*.py`. The executed-witness enumeration immediately below shows that all recorded remote assertions remain transcriptions even where an offline control verifies related local objects. |
| H5 | **confirmed** | A detached checkout of exact published main contains no v0.41 cycle-ending audit field; the entering audit child does. The trigger is therefore true for the published view and false locally. |
| H6 | **confirmed** | The detached entering-tree export passes at **2,675,890 bytes / 157 tracked entries / 2 retained cycles**, **106,502 bytes above** the **2,569,388-byte** attention boundary, with **324,110 bytes / 10.80% / 1.51 high-water cycles** below the ceiling at the **215,306-byte** high-water denominator. |
| H7 | **partly confirmed, partly refuted** | The exact v0.38-to-permanent-tail lever is **84,896 bytes**. Entering `STATE.md` is **194,412 / 453,741 bytes**, not 194,411. |
| H8 | **confirmed** | The registered self-test derives **16/16 rules / 115 controls**; the closing checklist derives **325 checked / 3 retracted / 316 matched / 316 resolved / 9 exemptions**. |

H4's required recorded-assertion enumeration is:

| Recorded assertion class | Executing witness before Step 2 | Result |
|---|---|---|
| Local annotated-object type, peel, closing parent/tree, release-parent ancestry, and State/header identity | `cycle-check` plus Git object reads | **witnessed locally**; these controls do not read the remote |
| Post-push record shape, local object/target freshness, closing-commit identity, and nonzero hosted-run field | `cycle-check` | **witnessed locally**; remote ref presence and the hosted run's actual conclusion are not refreshed |
| Remote `main` identity and ancestry position | none | **unwitnessed transcription** |
| Remote release-tag direct object, peeled target, presence, or absence, including the permanently withheld and historical tags | none | **unwitnessed transcription**; the unpublished-local path explicitly admits that offline Git cannot refresh absence |
| Remote evidence-ref absence before creation, exact identity after push, and immutability on later reads | none | **unwitnessed transcription**; non-force push protects only the mutation attempt itself |
| Remote publication topology claimed by pre-push, post-push, progress, and deferral records | none | **unwitnessed transcription** |
| Published-tip presence or absence of the cycle-ending export-audit field | none | **unwitnessed until the operator performs a detached remote checkout**, as Step 1 did manually |
| Hosted run conclusion and its correspondence to the remote ref named by a record | hosted CI measures the checked-out commit; local tooling verifies only record syntax and downloaded evidence | **partly witnessed**, but no executed local control binds the recorded remote ref reading to that run |

The entering `git status --porcelain` population was exactly the three retained
untracked amendment inputs plus this then-untracked v0.42 runbook. After
ACTIVATE committed the runbook, the worktree returned to exactly the same three
untracked amendment inputs. Full `./run ci-local` passes **22/22** jobs;
Python 3.11.4 and 3.12.13 each pass the complete **396/396** population with
the same named `on_site` identity and no skip; the registered invariant suite
passes **16/16 rules / 115 controls**; golden passes **11/11** with delta zero.
The clean rebuilt environments each resolve the exact pinned **21-package**
set. No E0 decision gate or stop condition fired.

Plus the standing entering measurements: `git status --porcelain` with its
expected untracked set stated exactly, full `./run ci-local`,
`invariant-scan --self-test`, both complete Python populations, and golden —
counts, not adjectives.

**Acceptance criteria.** Every hypothesis carries a dated verdict: confirmed,
refuted, or unmeasurable with a stated reason. H2 and H5 are settled by executing
against the real remote and a real detached checkout rather than by citing prior
records. H4's enumeration distinguishes recorded remote assertions that have an
executing witness from those that do not. No figure in this document is treated
as established by appearing here.

**Done when** dependent steps start from measurements rather than from this
runbook.

---

## Step 2 · REMOTE-WITNESS — make the published side something that executes

Per F1, F2, F3, DR34, DR35, C28, and C29. Two halves that belong together: the
remote becomes measurable, and the ordering that leaves the published tip short
becomes specified.

**2a — an executed remote control.** Per C28, and read C28's hard rule before
writing anything: an offline run must still pass, with a visible `unavailable`
verdict rather than a silent pass or a failure. Cover the remote assertions H4's
enumeration finds unwitnessed, beginning with the ones that guard an irreversible
act.

**2b — the same-cycle publication ordering.** Per DR35 and C29, state it where
the protocol lives and give it controls in both directions: an ordering that
would leave a cycle's own export audit outside its published tip fails, and the
historical cross-cycle shape still passes.

**Planted controls.** For 2a: a transcribed remote fact that disagrees with the
executed reading fails, and an offline invocation records `unavailable` and
passes — the second is the one that matters, because a control satisfying only
the first would break `ci-local`, hosted CI, and every sandboxed run. For 2b: as
C29 states, both directions.

**Acceptance criteria.** Offline satisfiability is proved against the real gates
and the proof is recorded before the control is adopted; all four planted
controls fail before and pass after, each anchored at a registered control site;
the remote control's output distinguishes measured, unavailable, and disagreeing
without collapsing them; the ordering statement follows the existing pointer
discipline rather than duplicating prose across documents; `./run ci-local` is
clean with and without network access.

**Done when** the published side of this project is a measurement rather than a
sentence.

---

## Step 3 · ARCHIVE — dormant, Grant E

**Objective.** Execute Grant E exactly, or record its absence truthfully.

If granted: record the grant text verbatim; confirm the archivable region against
real bytes per C30; move the closed-cycle records through v0.38 into a new
append-only file under `docs/state-archive/` following the v0.37 precedent; pin
it at `structural` grade, which the existing derived structural-archive exclusion
then removes from the export with no new mechanism; leave the status header and
the v0.39 through v0.41 records in place. The archived records are not edited in
transit — an archival that rewrites a dated measurement is a prohibited edit
wearing a move.

If not granted: one dated not-granted observation, and the deferral row carries
the measured quantity under the structured `unheld-lever` disposition v0.41 built.

**Acceptance criteria.** Either the archive exists with its structural pin and the
derived exclusion removes it, with the archived bytes byte-identical to what
`STATE.md` held before the move and proved so — or the not-granted observation is
recorded with its date and the unrecovered quantity. `STATE.md` remains valid
against its header and boundary controls either way; the protected manifest
changes by exactly one pin or not at all; `./run ci-local` is clean.

**Done when** the lever is either spent exactly as authorized, or its absence is
recorded with the measured number attached.

---

## Step 4 · REPAIR-TIP — dormant, Grant F

**Objective.** Execute Grant F exactly, or record its absence truthfully.

If granted: record the grant text verbatim; measure every precondition
immediately before the push under Step 2's executed control — remote `main` at
the exact recorded closing commit, the target resolving to the exact audit child,
ancestry proven, both published tags unmoved; one non-force fast-forward creating
exactly one ref movement; then read the remote back and record what moved.

Irreversibility is accepted and one-directional. Once pushed, the retraction bar
covers the newly published commit, and no later finding is grounds to delete or
force-move a ref.

If not granted: one dated observation recording that published `main` remains one
commit behind the complete record, naming exactly what a reader of published
history cannot see.

**Acceptance criteria.** Either the remote readback shows `main` at the exact
audit child with every tag unmoved and the published tip now carrying v0.41's
export audit and post-push records — or the dated not-granted observation names
the gap precisely. No tag moves in either case. `cycle-check` passes truthfully on
the resulting state.

**Done when** v0.41's published record is complete, or its incompleteness is
recorded as a measurement rather than left implicit.

---

## Step 5 · RE-MEASURE — hosted, conditional

Runs if operational or production code moved; checker and `run` changes qualify.
Evidence ref under the standing authority: under `refs/heads/codex/`, naming the
active cycle and a short commit id, with the absence pre-check recorded — under
Step 2's executed control if it has landed — non-force, exactly one ref created,
`main` and every tag untouched beyond Grant F. Report run id, attempt, ref, and
blocking identity result. A pre-existing ref is a finding, not a detail.

If it does not run, record the dated reason and name which claims rest on local
execution only.

**Acceptance criteria.** Either a hosted run is reported with its id, attempt,
ref, and blocking identity result, and the remote readback shows every tag
unmoved and `main` where Step 4 left it — or the dated skip reason is recorded
together with the claims that consequently rest on local execution alone. The
absence pre-check is recorded either way.

**Done when** every claim in this cycle names the machine that witnessed it.

---

## Step 6 · R-CLOSE

The established two-commit tagged close with the v0.40 pre-tag gate standing:
release parent → assembled closing worktree → **run the pre-tag gate and require
it to pass** → closing commit → local annotated tag → **append-only audit child
as the immediate next commit**, carrying
`- cycle-ending review-export audit: closing_tree=…; bytes=…; audit_delta=…`
measured against the closing tree it follows. Per DR39 the close is
unpublished-local; **if a publication grant arrives mid-cycle, DR35's ordering
governs from that moment** and the audit child carries the export audit alone,
with `main` pushed to it.

The `STATE.md` header spends the release-commit assertion phrase on this
release's parent and nothing else.

**Acceptance criteria.**

- The pre-tag gate passed at the assembled closing worktree, before the tag
  existed, and its verdict is recorded.
- **A checkout of the new annotated tag passes `cycle-check`**, as v0.17.7's and
  v0.17.8's did.
- Dated disposition per DR38, naming any behaviour movement rather than letting
  the version imply its absence; the serialized-field clause adjudicated against
  the R15 manifest diff.
- `version-check` passes with authorities and restatements counted.
- `checklist-audit` passes with all figures stated inline in the closing record
  and a non-zero v0.42 line.
- The governed export row is bound; the audit child is present in the stated
  order; `audit_delta` reconciles against the closing tree.
- Per DR39 a fresh dated observation for the new release.
- Every deferral row carries a dated v0.42 observation; where the attention
  predicate is still firing, its disposition satisfies the structured form
  v0.41 built, with the recovery attributed to each lever separately and the
  exact shortfall stated.
- `invariant-scan --self-test`, both Python populations, and golden: counts
  stated, zero hand-typed absolute finding-line fields.
- No publication beyond Grant F's exact fast-forward.
- No process instruction left inside a dated record.

**Done when** the cycle is closed, audited, truthfully represented, and the
handoff written.

---

## Closing-record assembly template

*Assembled at Step 6 in the established field form, with every figure stated
inline. The release identity, evidence candidate, hosted run, governed export,
artifact boundaries, attention state and its structured disposition, deferral
disposition, divergence disposition, scope reconciliation, publication boundary,
checklist reconciliation, golden reconciliation, and the pre-tag and post-tag
gate verdicts each carry their measured values. This tree contains no
annotated-tag-object field; the local annotated tag targets the closing commit
only after it exists.*

---

## Governed artifact byte-boundary authority

- governed artifact byte boundary: path=`STATE.md`; bytes=`453741`
- governed artifact byte boundary: path=`config/protected-artifacts.json`; bytes=`1048576`

**Carried forward byte-identically.** A change to either figure is an
architectural change requiring its own justification and operator authorization.
The 3,000,000-byte review-export ceiling and the two-cycle retention depth remain
separately governed and are not moved by this cycle.

---

## Deferred means deferred

The full carry-forward population from the immediately prior runbook with every
trigger unchanged; the `Second STATE.md archival` clause is the text the
predicate registry derives. **Each observation cell is a template.** ACTIVATE
replaces each with a dated v0.42 measurement before any semantic acceptance, and
Step 6 replaces them again with close measurements. A template surviving into any
acceptance point is a defect, not an oversight.

| Deferred item | Unchanged trigger | Measured observation (cycle-identified) | v0.42 action |
|---|---|---|---|
| `v0.17.6` publication, tag movement, or deletion | any proposal to publish, move, re-point, or delete the `v0.17.6` tag, its object, or its target | v0.42 · 2026-08-05 — Local readback resolves annotated object `66ee2cbbe374b99722bec49b8176571777aaa899` to closing commit `7c9305f01219412048ec75236f2bf1e61112c178`; executed remote readback returned no v0.17.6 ref. No proposal to move, publish, re-point, or delete it arose; DR22 remains settled. | none |
| T7 robots single-flight | a second concurrent harvester | v0.42 · 2026-08-05 — Permission-capable process inspection found no running `cored`, harvest, pipeline, or scheduler process, so no second concurrent harvester appeared and the trigger did not fire. | none |
| NEGATIVE-CACHE Decision B | a live transient robots outage for an admitted publisher while a usable last-known-good policy exists, plus operator authorization | v0.42 · 2026-08-05 — No publisher wire was touched and no Decision B authorization was issued; neither half of the combined trigger occurred. | none |
| Conditional GET (`ETag` / `If-Modified-Since`) | an operator-authorized cycle whose scope permits the `net` request path plus a live 304 observation | v0.42 · 2026-08-05 — The declared scope forbids the net request path, no publisher wire was touched, and no live 304 was observed. | none |
| `edgar:*` extension field mapping | an operator-authorized cycle permitting `crates/ingest/src/**` for mapping, with a connector review | v0.42 · 2026-08-05 — `crates/ingest/src/**` is forbidden and no connector review occurred; the trigger did not fire. | none |
| Live multi-publisher behaviour in one runtime | further origins beyond the two configured, or concurrency | v0.42 · 2026-08-05 — `config/core.json` still contains exactly two real network publisher origins plus three fixture sources on `example.org`; process inspection found no concurrent publisher runtime and no further origin appeared. | none |
| First recurring scheduled SEC run | explicit operator authorization of a bounded scheduled window, separate from any cycle scope | v0.42 · 2026-08-05 — No bounded scheduled-window authorization was issued and process inspection found no scheduler run. | none |
| Postgres / pgvector / multi-host seam | unchanged | v0.42 · 2026-08-05 — No tracked diff exists and dependency search found only historical/documentation mentions of pgvector; no Postgres dependency, pgvector implementation, or multi-host seam was introduced. | none |
| A4 untrusted-shell boundary | a third-party/untrusted shell, or any claim HC1 is invariant under shell replacement | v0.42 · 2026-08-05 — No third-party or untrusted shell was introduced and the governing documents continue to state the shipped-shell trust boundary rather than claiming replacement-invariant HC1. | none |
| L2 forced-command wrapper | an operator server session | v0.42 · 2026-08-05 — No model-profile command or operator server session occurred; L2 remains scheduled and unexecuted. | none |
| R3/R4 open-bottom coverage | a spelling outside registered vocabulary | v0.42 · 2026-08-05 — The executed registered scan passes R3 and R4 inside their stated vocabularies, and the full self-test passes **16/16 rules / 115 controls**. No outside spelling was identified by this cycle; the open-bottom limit remains explicit. | none |
| `--features net` Rust 1.86 execution | a scoped cycle authorized to change evidence topology and an executable local or hosted lane that actually pins and runs the net path on Rust 1.86 | v0.42 · 2026-08-05 — Workflow and evidence topology remain forbidden. The latest committed pinned result is v0.41 candidate run `30925977431`, which passed the explicit Rust 1.86 success and 1.85 declared-MSRV refusal identities; no lane topology moved. | none |
| GitHub attestation verifier version admission | the installed or proposed `gh attestation verify` version differs from the exact repository pin, or its accepted bundle/workflow contract changes | v0.42 · 2026-08-05 — Installed GitHub CLI is **2.96.0**, equal to `PINNED_GH_ATTESTATION_VERSION`; no verifier pin or accepted bundle/workflow contract changed. | none |
| Third configured publisher | a completed compliance review, then a separate admission decision | v0.42 · 2026-08-05 — No third-publisher compliance review or admission occurred; configured network publishers remain arXiv and SEC. | none |
| `v0.8.0` / `v0.10.2` publication | operator-authorized push of both exact annotated objects | v0.42 · 2026-08-05 — Executed remote readback returned neither historical tag; local objects remain `314c1dd914a3d8e9193445874a419ed762581e6e` and `d821f8b2eb6f39fe4a7d06a88cd61de771c7b0ba`. No authorization to publish them was issued. | none |
| `--skip-local-tag-verification` removal | both historical tags published plus a passing hosted full-history `cycle-check` without the flag | v0.42 · 2026-08-05 — R12's withheld-hosted planted admission still passes, but executed remote readback found both historical tags absent and no hosted full-history run without the flag occurred; neither removal clause advanced. | Step 2 |
| Manifest retention/indexing | the manifest reaches its governed artifact byte boundary, or two consecutive clean `./run verify-artifacts` runs each take ≥1.00 s real | v0.42 · 2026-08-05 — The manifest is **200,440 / 1,048,576 bytes** and two complete verifications matched **3/3 artifacts / 339 pins** in **0.10 s / 0.10 s real**. Neither boundary nor timing clause fired. | none |
| Version literal in `app.py` | a cycle whose declared scope permits shell source changes | v0.42 · 2026-08-05 — Shell source is absent from `allow`; all five executable authorities still report **0.17.8**, so release-authority precedence has not moved the literals before close. | Step 6 |
| Release-classification criteria with no executed control | an operator decision that prose adjudication is insufficient | v0.42 · 2026-08-05 — R15 reports **0 differences across 6 routes / 112 field occurrences**. DR38 therefore currently selects patch, and no broader operator decision displaced the R-CLOSE adjudication boundary. | Step 6 |
| Second `STATE.md` archival | the review-export attention predicate fires, or `STATE.md` reaches its governed artifact byte boundary | v0.42 · 2026-08-05 — State measured **194,412 / 453,741 bytes** before the activation record and the exact v0.38-to-permanent-tail region is **84,896 bytes**. The accepted staged v0.41–v0.42 export is **2,647,307 bytes**, so the attention predicate fires while the State byte boundary does not. Grant E is not issued. trigger-fired disposition: kind=`unheld-lever`; lever=`Grant E`; recoverable_bytes=`84896`. | Step 3 |
| Retention derivation across a version-family boundary | an active cycle whose name is not of the form `v0.<n>` — raising at `v1.0`–`v1.2`, silently under-excluding from `v1.3` onward | v0.42 · 2026-08-05 — The supplied cycle name is in the `v0.<n>` family; the version-family trigger did not fire. | none |
| Published-release divergence | the unpublished distance contains a measured runtime behaviour difference persisting across three consecutive closed cycles within the current publication epoch, or acquires any public-surface change | v0.42 · 2026-08-05 — Executed readback gives published `main=993813c755e9f759a4ee165954c7a1df984f6b10`; local HEAD is its one-commit descendant and that distance changes only `STATE.md` and `PROGRESS-v0.41.md`. R15 remains exact, so no runtime or public-surface movement appears and the publication-epoch count remains **0**. | Step 4 |
| MSRV current-restatement membership | a current restatement of either Rust floor lands outside the registry without failing a check | v0.42 · 2026-08-05 — `version-check` derives **3** executable offline pins at 1.78, **22** current floor restatements, **3** release restatements, and classifies all **591** tracked files; no unregistered current floor restatement appeared. | none |
| Retention arithmetic fallback | the retention formatter again permits an omitted retained set, or any live production or fixture caller supplies a set not derived by `expected_retained_cycle_paths` for that root | v0.42 · 2026-08-05 — Before activation, the configured derivation still retains exactly v0.40–v0.41 and correctly rejects the untracked v0.42 draft; no omitted or non-derived retained set appeared. ACTIVATE advances the same derived pattern to v0.41–v0.42. | none |
| Optional cycle-ending audit disclosure | a closed cycle whose delivered export differs from its governed figure and which records no cycle-ending audit field | v0.42 · 2026-08-05 — Local audit child `827192d2b3ed56fbe04ac0df0cc6536ef037e066` contains v0.41's `closing_tree=993813c…; bytes=2674239; audit_delta=+16554` field, while executed remote `main=993813c…` and direct blob readback prove the published tip lacks it. The trigger is false locally and true in the published view. | Step 2 and Step 4 |
| License enum semantics | a second publisher requires an inexpressible license value | v0.42 · 2026-08-05 — No publisher work occurred and no inexpressible license value appeared. | none |
| Terms-level automated-access gate | a candidate's terms restrict beyond robots.txt | v0.42 · 2026-08-05 — No fresh terms were fetched; the pinned SEC determination remains the latest publisher-specific operator adjudication. | none |
| Feed shape observation | an uncovered publisher feed shape | v0.42 · 2026-08-05 — No feed was fetched and no uncovered feed shape appeared. | none |
| Threshold-authority limitation | a common dependency module or manifest edge appears between store and view | v0.42 · 2026-08-05 — Store and view continue to share the already-admitted `intel-extract` identity seam; no new module, manifest edge, dependency, or radius authority appeared. | none |
| ARCHITECTURE.md §8 / AGENTS.md R-CLOSE tag-mechanics duplication | the restatements diverge | v0.42 · 2026-08-05 — Source tracing finds `ARCHITECTURE.md` §8 delegates tag mechanics exclusively to AGENTS.md R-CLOSE; no duplicate mechanics currently diverge. Step 2 will re-measure this after adding same-cycle ordering. | none |
| Review-export capacity | the export meets or exceeds the executable two-governed-growth-cycle attention boundary | v0.42 · 2026-08-05 — The accepted staged v0.41–v0.42 export is **2,647,307 bytes / 157 tracked files / 2 retained cycles**, **77,919 bytes above** the 2,569,388-byte attention boundary, with **352,693 bytes / 11.76% / 1.64 high-water cycles** below the unchanged ceiling. Grant E contributes zero and remains an unheld **84,896-byte** lever. trigger-fired disposition: kind=`unheld-lever`; lever=`Grant E`; recoverable_bytes=`84896`. | Step 3 |

---

## Standing prohibitions

- `docs/state-archive/**` and `config/protected-artifacts.json` are touched only
  by Step 3 and only under Grant E. Without the grant, any diff under them is a
  violation to report.
- No archived record edited in transit. Moving a dated measurement is permitted;
  changing one is not.
- No push beyond Grant F's exact fast-forward and the standing evidence-ref
  authority. No force-push, ref deletion, or tag movement anywhere, ever.
- The `v0.17.6` tag, its object, and its target are never moved, deleted,
  re-pointed, or published.
- No closed-cycle document, observation, fixture, or immutable local record
  edited; corrections are forward and dated.
- No tag created before the pre-tag gate has passed at that tree.
- No wire request of any kind.
- No control adopted that requires network access to succeed.
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
- [x] REMOTE-WITNESS
- [ ] ARCHIVE
- [ ] REPAIR-TIP
- [ ] RE-MEASURE
- [ ] R-CLOSE

*Box ids match the `PROGRESS-v0.42.md` entry ids exactly; the box-coverage rule
audits this runbook like any other.*

---

## Handoff

One report: each DR executed and whether any measurement refuted its basis; each
C-determination with its reasoning and its falsifier; every stop condition
triggered or an explicit none; H4's enumeration of recorded remote assertions
with and without an executing witness; both grant outcomes, executed or
not-granted with the quantity or gap named; the closing export with recovery
attributed to each lever; and the v0.43 findings list — findings, not proposed
acceptance criteria.

Then the one question that is now overdue, stated with numbers rather than as a
reminder. **The attention predicate has fired for three consecutive cycles.**
Grant E, at its measured 84,896 bytes, clears the boundary at activation and does
not hold that clearance to the close on last cycle's growth. After it, every
remaining lever is ask-first: the operator-selected 3,000,000-byte ceiling, the
accepted two-cycle retention depth, a `CHANGELOG.md` archival on the `STATE.md`
pattern, or a redefinition of what review source means. Growth remains
concentrated in checker source, checker tests, the rule registry, and dated
records — the apparatus this discipline requires, growing because the discipline
is working. The handoff states the measured runway in cycles at the high-water
denominator, and names each lever with what it would recover, so the decision
arrives with numbers rather than as an emergency.

---

## Provenance

**Measured on the delivered post-v0.41 export (2,675,890 bytes / 157 file
entries, reconciling with the reported 2,674,239-byte closing tree plus a
1,651-byte audit-child append):** `grep -c ls-remote` returning zero for `run`
and zero across every `tools/*.py`, which is F1's whole basis; the 1,519-byte
`STATE.md` delta between the recorded 192,892-byte closing worktree and the
194,411-byte delivered file, and the 1,396-byte post-push publication audit
paragraph inside it, which is F2's; `PROGRESS-v0.41.md`'s `cycle-ending
review-export audit` field carrying `closing_tree=993813c7…; bytes=2674239;
audit_delta=+16554`; the v0.17.5 record describing its audit child as "preserved
in published history" against v0.17.8's published tip being the closing commit,
which is F3's; the attention boundary at 2,569,388 with the export 106,502 above
it, the 82,012-byte v0.40 pair, and the +72,403 underlying growth once the
manifest exclusion is netted out, which are F4's; `GOVERNED_TRIGGER_PREDICATES`
and `governed_artifact_trigger_text`, from which this table's archival clause is
derived rather than copied; the structured `unheld-lever` and `measured-change`
dispositions v0.41 recorded, and Codex's measured 84,896-byte archival lever
against my projected 128,859; `config/protected-artifacts.json` absent from the
export at 157 entries; and the registry at 16 rules / 115 planted controls
counted from `config/invariant-rules.json` directly.

**Verified unchanged against the checker that will scan this runbook:**
`STEP_HEADING_RE`, `DEFERRED_HEADING`, `AMENDMENTS_HEADING`,
`AMENDMENT_ENTRY_RE`, `CONTRACT_FIELD_LABELS`, `SCOPE_HEADING_RE`,
`SCOPE_CLASSES`, `STEP_REFERENCE_RE`, the quantity-clause predicate, and the
declared-scope pattern-population control.

**What I could not measure and marked as hypotheses:** anything requiring `.git`
or the network — the object graph, every remote ref, ancestry, and the content of
the published tip, which H2 and H5 require executing rather than citing. That
limitation is this cycle's subject as well as its constraint: I am reasoning about
a published state I cannot see, from records that describe it in prose.

**What I did not do:** no repository command, no wire request, no test run, no
push. Every figure above is for Step 1 to confirm against real bytes.
