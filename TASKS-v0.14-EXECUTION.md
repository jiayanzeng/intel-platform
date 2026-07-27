# TASKS-v0.14-EXECUTION.md — control-precision and production-surface runbook for Codex

v0.14 is a **rule-integrity cycle**, and it continues the line v0.12 and v0.13
established.

v0.12 registered absence claims as rules. v0.13 proved those rules can fire, by
making `fail_before` an executed control rather than a validated string. What
neither cycle established is that a rule fires **for the reason it claims**, and
at **the site it names**:

- **A control proves the rule failed somewhere.** R7's two call-site controls
  carry identical `expected_fail` text, so the self-test cannot distinguish a
  control that fired at the mutated site from one that fired anywhere else in
  the tree. A rule with a subtly over-broad regex passes its own control.
- **R5 was found to enforce a naming convention rather than the invariant, and
  nothing had checked whether the other rules share that shape.** R1, R3, R4,
  and R6 have been read but never mutated against a renamed or restructured
  equivalent. R3 in particular hunts known provider names and is open at the
  bottom by construction.
- **Two production properties are upheld by statement order and file placement,
  not by anything that would refuse.** Identity installation precedes the
  listener bind because two lines in `main()` happen to be in that order. The
  store's fault-injection seam stays out of the shipped binary because one
  `Cargo.toml` line sits under `[dev-dependencies]` rather than
  `[dependencies]`. Both are correct today and neither is guarded.
- **v0.13's own runbook omitted a step its deferral table required.** The
  CI-runner evidence row declared re-measurement at the new release commit; no
  task discharged it, and the omission cost two extra hosted rounds. That was a
  template gap, and template gaps recur.

This cycle does five things and deliberately no more:

1. **makes every control site-specific**, so a control proves its rule fired
   where the mutation was applied;
2. **audits the remaining rules for R5's shape**, converting what can be
   converted to allow-lists and recording plainly what cannot;
3. **registers the two unguarded production properties** as rules;
4. **disposes of an undocumented production behavior knob** rather than leaving
   it discoverable only by source reading;
5. **fixes the runbook template** so the v0.13 omission cannot recur.

It ships no new ingestion source and no subscriber-facing surface. **The public
`/v1/*` JSON bodies, the SQLite schema, and the golden regression's 11
invariants are unchanged. Golden stays 11/11 byte-identical through every task
in this file.**

**Version disposition (decide at R-CLOSE, default recorded here).** The default
is a **minor release `v0.14.0`**, because Step 6 changes observable `/view`
behavior or its configuration surface under every disposition except pure
documentation. The alternative — **`v0.13.1`** — applies if and only if Step 6
lands as documentation with no code change. **Recommendation: decide at Step 6,
record the trigger there, and do not let R-CLOSE inherit a default.**
`v0.13.0` stays published and unmoved.

---

## Entering state (asserted, not yet verified)

Taken from `STATE.md` (v0.13.0), `PROGRESS-v0.13.md`, and the post-publication
report. **Every sentence here is a hypothesis until Step 1 (E0) measures it.**

- `v0.13.0` is released and published. Annotated tag object
  `24a6a2aca52974891d120e0f2b295a93d629c1f7` dereferences to release commit
  `5ecd42bb6ca44f1588e53e493c67fee17d071b09`, which is also `origin/main`.
  Release evidence is authenticated dispatch run **30277584129** against
  candidate `7faaa4e1…`. **None of this is reopened by this cycle.**
- `./run ci-local` **20/20**; Rust **124 workspace / 47 net** (23 `intel-ingest`
  + 24 `cored`); shell **216/216** under Python 3.11.4 and 3.12.13; golden
  **11/11**; pins **86** (84 evidence + 2 authorization); protected databases
  **2/2**; `checklist-audit` **111** checked with **3** retractions;
  `cycle-check` reports `v0.13`, state `closed`.
- **Local `main` is two append-only audit commits ahead of `origin/main`**, which
  remains exactly at the release commit. This is a deliberate consequence of
  publication authorization covering one atomic push. It diverges from prior
  practice: v0.12's `origin/main` was its closing audit commit.
- Post-publication run **30281407090** passed at the release commit and is
  recorded but **not promoted**; release evidence is unchanged.
- `A4` remains open. The **L1 model-profile controller residual** remains open
  pending the scheduled server-side **L2 forced-command wrapper**, which
  requires a live server session and is **not** executed in this cycle.
- **The `ci-local` job count enters at 20 and exits at 20.** No task in this file
  adds a job; new rules run inside existing job 20.

### Defects and gaps this runbook is drafted against (verify, do not trust)

**G1–G4** are the v0.14 candidate inputs recorded in `STATE.md:697-713` at the
close of v0.13. **G5–G6** are additions from independent review of the v0.13.0
export on 2026-07-27 and must be honored alongside them.

| # | Location | Claim to verify |
|---|---|---|
| **G1** [P2] | `config/invariant-rules.json` R7 controls 2–3; R6 control 1 | **A control proves the rule failed, not where.** R7's two call-site controls share `expected_fail` text, so self-test output cannot distinguish them and neither asserts the mutated file or line. R6's control carries the full `invariant-scan: R6 FAIL:` prefix where other rules carry the message only, so strictness is inconsistent across the registry. An over-broad regex passes its own control. |
| **G2** [P1] | `tools/invariant_scan.py` R1, R3, R4, R6 implementations | **R5's shape defect was never checked against the other rules.** R5 enforced a naming convention until v0.13's THRESHOLD-BIND rebound it to call sites. R1, R3, R4, and R6 have been read but never mutated against a *renamed or restructured* equivalent. **R3 is expected to be irreducibly deny-list** — it hunts known provider names and cannot enumerate unknown ones. If so, that must be **recorded as a stated limitation**, not quietly converted or left implied. |
| **G3** [P2] | `apps/cored/src/main.rs:1333` vs `:1370` | **Identity-before-bind is guarded by statement order.** `build_robots_cache` precedes `TcpListener::bind` in `main()`. The property "a net build cannot serve without an installed identity" therefore rests on two lines being in that order in an untestable function, evidenced by one manual binary run. v0.13's move to `main()` was the correct placement and a net reduction in structural guard. |
| **G4** [P2] | `TASKS-v0.13-EXECUTION.md` deferral table vs its step list | **The runbook template permits a declared requirement with no discharging step.** v0.13's "CI-runner evidence · re-measure at the new release commit" row had no RE-MEASURE task. Nothing detects a deferral row whose action is asserted but unassigned. |
| **G5** [P2] | `apps/cored/src/main.rs:906-918`, called at `:558`, `:982`, `:987`, `:992` | **An undocumented production behavior knob.** `diagnostic_delay` sleeps up to 10 000 ms in the `/view` request path when `CORE_VIEW_DIAGNOSTIC_DELAY_STAGE` matches, gated by neither a feature nor `debug_assertions`. Its only legitimate caller is `tools/benchmark_view.py:363-369`. It appears in no `.env.example`, `README.md`, `deploy/README.md`, or `ARCHITECTURE.md` entry. An operator who exports it for a benchmark and forgets degrades `/view` silently — no log line, no health signal. |
| **G6** [P3] | `apps/cored/Cargo.toml:26-27`; `crates/store/src/sqlite.rs:634-643` | **A shipped-binary property upheld by one line's section placement.** `test_clear_fingerprint` is a `pub` fault injector gated on `test-support`. It stays out of the release build only because `intel-store … features = ["test-support"]` sits under `[dev-dependencies]`. **This was verified clean** — workspace `resolver = "2"`, dev-dependencies are not built by `cargo build` — so this is a *guard* gap, not a live defect. Moving that line one section up would silently ship a fault injector. |

---

## How to run this file

Execute top to bottom, one task and one commit at a time. Follow `AGENTS.md §5`
after **every** task: verify the gate contains the scope of every acceptance
criterion, check the gate, implement, run and capture every acceptance
criterion, run `./run golden`, update `STATE.md`, append `PROGRESS-v0.14.md`,
check the box here, and commit. Implementation commit and audit-record commit
stay separate. Do not batch status updates.

- **🤖 = Codex executes and self-verifies end to end**, with no live model
  endpoint, no live server session, no publication, and no push.
- **🧑 = exactly one named operator action or decision is required.**

**Dependency gates.** Step 2 gates Steps 3, 5, and 6 — every rule those steps
register or modify must carry site-specific controls, so the precision fix lands
before new rules are written against the old standard. Step 8 is blocked by
every preceding implementation step. Step 9 is blocked by Step 8. Step 7 is
independent and may run at any point after Step 1.

### Pre-cycle · Remote reconciliation 🧑

**Local `main` is two append-only audit commits ahead of `origin/main`.** Before
E0, the operator decides one of:

- **(a) Push the two audit commits** to `origin/main`, restoring the v0.12
  pattern in which the remote carries the closing audit record. The published
  `v0.13.0` tag does not move.
- **(b) Leave them local** and record, in `STATE.md`, that the remote
  deliberately stops at the release commit and why.

**Do not begin E0 until this is decided and recorded.** An entering state that
disagrees with the remote is the condition every prior drift defect started
from. If (a) is chosen, verify by read-only means that the tag still
dereferences to `5ecd42bb…` afterwards.

### Cycle activation (before E0)

In a **separate preparatory implementation/audit pair**: confirm the worktree is
clean, commit **only** this runbook, the `AGENTS.md` header declaring v0.14
active, and a new `PROGRESS-v0.14.md`; then run `cycle-check` and
`checklist-audit`. **Do not claim E0's acceptance from this commit.**

### Session opener (run before reading further)

```bash
git status --porcelain=v1
git describe --tags --always --dirty
git rev-parse HEAD
git rev-list --left-right --count origin/main...HEAD
git tag --list 'v0.13*' --format='%(refname:short) %(objectname) %(*objectname)'
sed -n '1,20p' AGENTS.md
sed -n '1,6p' STATE.md
```

### Global definition of done

Protected hashes exact; **all 86** evidence pins still match until Step 8 adds
more; golden **11/11 byte-identical**; `./run version-check` green; zero rustc
warnings on offline and net builds; all Rust tests green; all shell tests green
under Python 3.11 **and** 3.12; clippy, fmt, ShellCheck, floor byte-compilation,
and locked Rust 1.78 green. No mock, fixture, double, health response,
hand-authored receipt, or workflow configuration is promoted to wire evidence.

`invariant-scan` enters at **7 rules / 11 controls** and exits at **9 rules**
with a control count recorded by Step 2. `ci-local` enters and exits at **20**.

---

## Deferred means deferred

None of the standing deferral triggers fires in this cycle.

| Deferred item | Unchanged trigger | v0.14 action before the trigger |
|---|---|---|
| T7 robots single-flight | a second concurrent harvester | none |
| Postgres | a second archive writer | none |
| pgvector | exact cosine stops fitting the measured request budget | none |
| Multi-host seam hardening | an actual core/shell host split | none |
| A4 untrusted-shell boundary | a third-party/untrusted shell, or any claim HC1 is invariant under shell replacement | none |
| L2 forced-command wrapper | an operator server session | none — remains scheduled, not executed |
| CI-runner evidence | an authenticated receipt set with identified matrix legs, durably committed | **re-measure at the new release commit — discharged by Step 8, which exists for this row** |

**Every row above whose action is not "none" must name the step that discharges
it.** That correspondence is Step 7's subject and is checked in this cycle.

---

## Step 1 · E0 — Rebuild the entering state and confirm G1–G6 🤖

**Objective.** Reproduce the post-v0.13.0 state from commands and confirm or
refute every gap against HEAD before changing anything.

**Gate.** The session opener has run, its output is captured, and the pre-cycle
remote decision is recorded.

**Steps.**

1. Run the full entering matrix: `./run ci-local`, standalone `./run golden`,
   `./run verify-artifacts`, `./run cycle-check`, `./run checklist-audit`,
   `./run progress-check`, `./run version-check`,
   `./run invariant-scan --self-test`.
2. **Reproduce G1 mechanically**: apply R7's control 2 mutation and R7's control
   3 mutation to separate scratch trees and show the self-test output is
   indistinguishable between them. Then construct an **over-broad** variant of
   one rule's regex, confirm it still passes its own control, and record it.
   That is the finding, not the narrative.
3. **Reproduce G2 mechanically**: for each of R1, R3, R4, R6, construct a
   *renamed or restructured* equivalent of the violation the rule claims to
   forbid and record whether the rule fires. Use a scratch worktree
   (`git worktree add`), never the live tree.
4. Confirm G3 by reading `main()` and recording what would detect a reordering.
5. Confirm G4 by checking every v0.13 deferral row against its step list.
6. Confirm G5 by reading the four call sites and searching the documentation set
   for the two environment variables.
7. Confirm G6 by building `cored` in release configuration and verifying
   `test_clear_fingerprint` is absent from the binary. **G6 is expected to
   refute as a live defect and confirm as a guard gap** — record it that way.
8. Record which of G1–G6 refute. A refuted row is a finding, not a failure.

**Acceptance criteria.** Entering matrix captured in full · G1 reproduced as two
indistinguishable control outputs plus one over-broad regex that passes · G2
reproduced as four recorded mutation outcomes · G3/G4/G5 dispositions recorded ·
G6 recorded as guard gap with the release-build check captured · published
`v0.13.0` tag, commit, and all 86 pins unchanged and re-verified · golden 11/11.

**Done when** every gap this runbook acts on has been confirmed or refuted by
execution.

---

## Step 2 · CONTROL-PRECISION (G1) — A control must prove where it fired 🤖

**Objective.** Make every registered control assert a site-specific failure, so
a rule cannot pass its own control by failing elsewhere.

**Gate.** `tools/invariant_scan.py`, `config/invariant-rules.json`,
`shell/tests/test_invariant_scan.py`. **No rule's matching logic changes in this
task** — Steps 3–5 do that, and mixing them hides a logic change inside a schema
change.

**Steps.**

1. Extend each control's `expected_fail` to include the **file and line** the
   mutation targets, and normalize every control to the same strictness: message
   only, with file and line supplied as separate asserted fields. R6's full-prefix
   form is brought into line with the rest.
2. Make the self-test assert that the failure it observed names the mutated file
   **and** the expected line, not merely that some failure occurred with matching
   text.
3. Add a **negative meta-control**: a rule whose regex is deliberately widened to
   match unrelated text must now **fail** its own control, because the reported
   site will not match the mutation site. Demonstrate it, capture it, revert it.
4. Extend `shell/tests/test_invariant_scan.py` to cover the new assertion,
   including a control whose expected site is wrong.
5. Record the new control count in `STATE.md` and `PROGRESS-v0.14.md`.

**Acceptance criteria.** Every control asserts file and line · R7's two
call-site controls are distinguishable in self-test output · the widened-regex
meta-control fails, demonstrated and reverted · shell tests green on both
interpreters · no rule's matching logic changed in this commit · `ci-local`
still 20 · golden 11/11.

**Done when** a control proves its rule fired at the site the control mutated.

---

## Step 3 · RULE-SHAPE-AUDIT (G2) — Find R5's defect in the rules that were never checked 🤖

**Objective.** Determine, by mutation rather than reading, which of R1, R3, R4,
and R6 enforce their invariant and which enforce a convention.

**Gate.** `tools/invariant_scan.py` and `config/invariant-rules.json`. **Source
under `crates/` and `apps/` may not change.** If a rewritten rule fails against
HEAD, that is a finding to record and act on in a follow-up task — the same gate
that produced THRESHOLD-SOURCE-SEAM in v0.13.

**Steps.**

1. For each of R1, R3, R4, R6: construct the renamed/restructured equivalent
   from E0 and record whether the rule fires.
2. Convert to an **allow-list over enumerable sites** every rule that can be so
   converted, following THRESHOLD-BIND's shape: enumerate the sites, assert the
   permitted form, report file, line, and offending token.
3. **Record honestly which rules cannot be converted.** R3 is expected to be
   irreducibly deny-list: an unknown provider name cannot be enumerated in
   advance. If so, state that limitation in the rule's `scope`, in
   `ARCHITECTURE.md`, and in `PROGRESS-v0.14.md`, in the same plain language A4
   uses. **A stated limitation is a property; an implied one is not.**
4. Register site-specific controls for every rewritten rule, per Step 2.
5. Record the shape lesson: a deny-list over source text is open at the bottom,
   and the honest response is either an allow-list or a stated limitation —
   never a rule whose claim is broader than its check.

**Acceptance criteria.** Four mutation outcomes recorded · every convertible
rule is an allow-list with site-specific controls · every non-convertible rule
carries an explicit stated limitation in three places · zero source files under
`crates/` or `apps/` changed in this commit · `invariant-scan --self-test` green
· golden 11/11.

**Done when** no registered rule claims more than it checks.

---

## Step 4 · R8-IDENTITY-BEFORE-BIND (G3) 🤖

**Objective.** Restore, as a rule, the structural guard that v0.13's correct
relocation gave up.

**Gate.** `tools/invariant_scan.py`, `config/invariant-rules.json`. No source
under `crates/` or `apps/` changes.

**Steps.**

1. Register **R8**: in production `cored`, the crawler-identity construction
   call precedes the sole `TcpListener::bind`, and no bind exists before it.
   Express it as an ordering assertion over enumerated sites, not a text search.
2. Cite the `ARCHITECTURE.md` sentence stating the property as `source`. If no
   such sentence exists, **add one first** — a rule with no prose to cite is a
   check without a claim.
3. Provide site-specific controls: reorder the two statements; delete the
   identity construction; add a second bind before it. All must FAIL.

**Acceptance criteria.** R8 registered with three site-specific controls, all
demonstrated FAIL · R8 PASSes on HEAD · the cited architecture sentence exists ·
`invariant-scan` reports 8 rules · `ci-local` still 20 · golden 11/11.

**Done when** reordering `main()` turns CI red.

---

## Step 5 · R9-TEST-SEAM (G6) 🤖

**Objective.** Guard the section placement that keeps a fault injector out of
the shipped binary.

**Gate.** `tools/invariant_scan.py`, `config/invariant-rules.json`. No manifest
or source changes — **G6 is a guard gap, not a live defect**, and this task must
not pretend otherwise.

**Steps.**

1. Register **R9**: no workspace manifest enables `test-support` outside
   `[dev-dependencies]`, and no `pub` item gated on `test-support` is reachable
   from a non-dev dependency edge.
2. Provide a site-specific control: move `apps/cored/Cargo.toml`'s
   `test-support` line into `[dependencies]` and require R9 to FAIL naming that
   file and line.
3. Record in `PROGRESS-v0.14.md` that the release build was verified clean at E0
   and that R9 exists to keep it so — **not** to fix something that was broken.

**Acceptance criteria.** R9 registered with a site-specific control,
demonstrated FAIL · R9 PASSes on HEAD · release-build cleanliness recorded as
pre-existing · `invariant-scan` reports 9 rules · golden 11/11.

**Done when** shipping the fault injector requires defeating a check rather than
editing one line.

---

## Step 6 · DIAGNOSTIC-KNOB (G5) — Dispose of the undocumented production delay 🧑🤖

**Objective.** Decide what `diagnostic_delay` is, and make the answer visible.

**Gate.** `apps/cored/src/main.rs`, `tools/benchmark_view.py`, `.env.example`,
`README.md`, `deploy/README.md`, `ARCHITECTURE.md`, and their tests. **🧑 One
operator decision: which disposition.** No change to `/view` response bodies.

**Options — record the choice and its reasoning, do not default.**

- **(a) Feature-gate it** behind a `diagnostics` feature the benchmark enables.
  Cleanest separation; costs a second build configuration for
  `benchmark_view.py` and a CI job or invocation to keep it compiling.
- **(b) Keep it, make it loud, document it.** Emit a startup warning naming both
  variables and the configured delay whenever they are set, and document them as
  a deliberate operator knob. Cheapest honest option; the silence is what makes
  the current state a defect, not the existence of the knob.
- **(c) Remove it** and have the benchmark measure stages another way. Smallest
  production surface; largest cost to the existing view-decomposition evidence,
  which must then be re-derived.

**Steps.**

1. Record the decision and reasoning in `PROGRESS-v0.14.md` **before**
   implementing.
2. Implement it. Under (a) or (b), the ≤10 000 ms bound stays and is asserted by
   a test.
3. Document the outcome in every location the variables were missing from.
4. **The version disposition follows from this step:** (a) or (b) ⇒ `v0.14.0`;
   (c) requires re-deriving benchmark evidence and still ⇒ `v0.14.0`;
   documentation-only ⇒ `v0.13.1`. Record the fired trigger here, not at R-CLOSE.

**Acceptance criteria.** Decision recorded with reasoning before implementation
· delay bound asserted by test · both variables documented in `.env.example` and
the operator-facing docs · under (b), the startup warning is demonstrated ·
version trigger recorded · golden 11/11.

**Done when** the knob's existence and effect are discoverable without reading
`main.rs`.

---

## Step 7 · TEMPLATE-REMEASURE (G4) — Close the gap that cost v0.13 two rounds 🤖

**Objective.** Make a deferral row whose action is asserted but unassigned a
detectable error.

**Gate.** `AGENTS.md`, `tools/progress_check.py` or `tools/cycle_check.py`
(whichever owns runbook structure), and its tests. No change to any closed
runbook.

**Steps.**

1. Amend `AGENTS.md` so every "Deferred means deferred" row whose action is not
   `none` must name the step that discharges it, and every runbook that changes
   the release commit must contain a RE-MEASURE step.
2. Make it executable: extend the runbook checker to fail when an active
   runbook has a deferral row with a non-`none` action that names no step.
3. Provide a fail-before: a scratch runbook with an unassigned row fails; the
   v0.14 file passes.
4. Do **not** retroactively fail closed runbooks. Record v0.13's omission as the
   originating evidence and leave its record intact.

**Acceptance criteria.** `AGENTS.md` amended · checker fails on an unassigned
deferral row, demonstrated · this runbook passes · closed runbooks unmodified ·
shell tests green on both interpreters · golden 11/11.

**Done when** the omission that cost v0.13 two hosted rounds cannot recur
silently.

---

## Step 8 · RE-MEASURE — Hosted evidence for the candidate 🤖🧑

**Objective.** Produce release-grade hosted evidence for the v0.14 candidate.

**Gate.** 🧑 **One narrow authorization: a non-`main` branch push.** No tag, no
`main` advance, no publication.

**Steps.**

1. Push the candidate to `candidate/v0.14.0`. Record branch and commit.
2. **Verify the remote branch's `ci.yml` contains every invocation you expect
   before dispatching.** Dispatching against a ref whose workflow you have not
   read is how v0.13 nearly shipped an unexecuted job.
3. Dispatch on that branch with `publish_evidence: true` and `audit_sha` set to
   the candidate.
4. **Read the per-invocation counts out of the hosted log**, not from job status:
   `intel-ingest` net, `cored` net, workspace, both shell legs, and the
   invariant self-test's rule and control counts.
5. Commit the signed receipt/bundle set, re-run `./run verify-artifacts` and
   `./run evidence-report`, and record the new pin count in `STATE.md`,
   `PROGRESS-v0.14.md`, and the pending closing record.
6. Confirm the hosted identity set is still **seven**.
7. Run `./run audit-deferred` in release posture with attestations required.

**Acceptance criteria.** Hosted run id pinned to the candidate · every count read
from the log · self-test rule and control counts match Step 2's recorded values ·
signed set committed and re-derived · new pin count in three places · identity
set still seven · `origin/main` unchanged, no tag · golden 11/11.

**Done when** v0.14's hosted evidence exists at the same grade as v0.13's.

---

## Step 9 · R-CLOSE — Version disposition and closing record 🧑🤖

**Objective.** Close the cycle with a measured record.

**Gate.** Steps 1–8 complete and boxed. Worktree clean. **🧑 One operator
decision: publication.**

**Steps.**

1. Re-run the complete definition of done at the release commit.
2. Record the version choice, citing the trigger **fired in Step 6**, not a
   default inherited here.
3. Record evidence candidate and release commit as **separate named fields**.
4. Classify every diff path exactly once in `STATE.md`; update `CHANGELOG.md`,
   `README.md`, and the release authorities.
5. Reconcile `ARCHITECTURE.md`. **A4 and the L1 controller residual must both
   still read as open.** Record R3's stated limitation from Step 3 alongside
   them if it was not convertible.
6. Check R-CLOSE's box and replace the pending heading with the canonical
   `Cycle closed:` record **in one commit**, so `cycle-check` never observes an
   invalid intermediate state.
7. State the publication disposition as a decision with a trigger.

**Acceptance criteria.** Version choice cites Step 6's trigger · evidence
candidate and release commit recorded separately · every diff path classified ·
`ARCHITECTURE.md` matches enforced reality · A4, the L1 residual, and any stated
rule limitation all recorded as open · `invariant-scan` 9 rules green · all pins
match · golden 11/11.

**Done when** v0.14's disposition is a recorded, measured decision.

---

## Cycle checklist

- [x] **E0** — entering matrix captured; G1 reproduced as indistinguishable
  control outputs plus a passing over-broad regex; G2 reproduced as four
  mutation outcomes; G3/G4/G5 recorded; G6 recorded as guard gap with the
  release-build check captured
- [x] **CONTROL-PRECISION** — every control asserts file and line; R7's two
  controls distinguishable; widened-regex meta-control fails and is reverted; no
  rule logic changed
- [x] **RULE-SHAPE-AUDIT** — four mutation outcomes recorded; convertible rules
  are allow-lists with site-specific controls; non-convertible rules carry a
  stated limitation in three places; no source changed
- [x] **R8-IDENTITY-BEFORE-BIND** — registered with three site-specific
  controls, all demonstrated FAIL; cited architecture sentence exists
- [x] **R9-TEST-SEAM** — registered with a site-specific control, demonstrated
  FAIL; release-build cleanliness recorded as pre-existing
- [x] **DIAGNOSTIC-KNOB** — disposition decided and recorded before
  implementation; delay bound asserted; variables documented; version trigger
  recorded here
- [x] **TEMPLATE-REMEASURE** — `AGENTS.md` amended and the check executable;
  unassigned deferral row fails; closed runbooks unmodified
- [ ] **RE-MEASURE** — hosted run pinned to candidate; every count read from the
  log; signed set committed; new pin count in three places; identity set seven
- [ ] **R-CLOSE** — version choice cites Step 6's trigger; evidence candidate and
  release commit separate; A4, L1 residual, and any stated limitation open

---

## Standing prohibitions

- **Do not touch published releases.** `v0.13.0`, `v0.12.0`, `v0.11.0`,
  `v0.10.3`, and unpublished `v0.10.2` are immutable — tags, commits, and pins.
- **Do not edit any closed runbook or progress log.** v0.13's omission is
  recorded, not corrected in place.
- **Do not uncheck a box in a closed runbook.**
- **Do not convert a deny-list rule into an allow-list you cannot enumerate.**
  If the sites are not enumerable, the honest output is a stated limitation. A
  rule that claims more than it checks is worse than an admitted gap.
- **Do not add an `invariant-scan` rule without a site-specific control.** After
  Step 2 this is a CI failure, not a matter of judgement.
- **Do not let `invariant-scan` acquire a runtime dependency.** Static analysis
  over source, config, and git only.
- **Do not add a ci-local job.** The count enters at 20 and exits at 20.
- **Do not edit source under `crates/` or `apps/` in Steps 3, 4, 5, or 7.** A
  rule that fails against HEAD is a finding, not a licence.
- **Do not claim any task closes or narrows A4**, and do not claim the L1
  controller residual is closed. Both remain open.
- **Do not run a live server session.** L2 remains scheduled.
- Do not change the public `/v1/*` JSON bodies, the SQLite schema, or the golden
  regression's 11 invariants. Golden stays 11/11 byte-identical after **every**
  task.
- Do not hand-edit `Cargo.lock` (HC12), raise the offline Rust 1.78 floor, lower
  the Python 3.11 floor, or let core call an LLM (HC3).
- Do not commit `.env`, provider keys, tokens, or private key material.
- Do not batch `STATE.md` / `PROGRESS-v0.14.md` updates or combine two tasks in
  one commit.
