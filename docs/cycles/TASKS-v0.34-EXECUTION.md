# TASKS-v0.34-EXECUTION.md — the checker is now the largest thing it checks

## Runbook amendments

*(Appended per step as each completes, in the established form:
`Step N — <what was implemented> — <date>`.)*

**r1 — 2026-08-02 — activation-contract correction.** Executing the real
`cycle-check` against the staged operator-supplied runbook exposed three
author-side schema defects before its first commit: the deferred table omitted
the required measured-observation column, it failed to carry forward the prior
cycle's `MSRV current-restatement membership` subject, and the planted-control
action named `G5` without a literal discharging `Step N`. The table now carries
the last measured v0.33 observations until E0 replaces them with v0.34
measurements, restores the missing subject, and assigns G5 to Step 1. The
checker was not weakened.

Step 1 — rebuilt both entry states, executed G1–G2, derived G3–G6, and refreshed every trigger observation — 2026-08-02

Step 2 — made State structural admission independent of its delegated semantic restatement and exposed every publication-status bound — 2026-08-02

Step 3 — made the governed margin entry point emit both representativeness and structural-epoch limits — 2026-08-02

---

**One reviewer error, mine, recorded before anything else.**

1. **v0.33 Step 4 required the permanent tail's lower boundary to be "enforced in
   its own right, not via the restatement," and then supplied one example of the
   failure mode — a cut stopping short of line 5320. That example is not the
   worst case, and the shipped control satisfies the example without satisfying
   the sentence.** `check_state_archival_region_contract` gates its
   permanent-tail marker rule on `has_restatement`, which is itself derived by
   delegating to `version_check`. I measured the consequence by execution:
   **removing the entire permanent tail — marker, §1 through §7, and the
   registered restatement with them — produces zero errors from the region
   contract.** The composite lane still fails, but only through
   `version-check`'s zero-extraction rule, which is the borrowed protection that
   v0.33's own G1 existed to stop relying on. **I wrote a criterion whose named
   test was satisfiable without its stated property, in the cycle whose subject
   was checks that admit nothing to execution.** That is the same defect as
   v0.32's "named denominator" criterion, one cycle later, and it is mine. G1
   settles it; Step 2 owns it.

**One finding that is not a reviewer error, recorded here so it is not confused
for one.** The margin basis-selection rule — *latest positive adjacent same-kind
governed pair* — was Codex's design, not something this runbook's predecessor
specified. It is a good rule and it does what v0.33 Step 3 asked. Its gap is
described in G2 and belongs to the rule, not to its author's instructions.

---

## The named root cause for this cycle

Two halves, and they are the same shape.

**First: a guard whose precondition can be destroyed by the event it guards
against is not a guard.**

| v0.33 control | what it guards | what admits it to execution | measured consequence |
|---|---|---|---|
| publication admission gate | the publication-reconciliation family | nothing outside itself — **this one is complete** | all three constructions rejected; correct |
| State region contract | the permanent tail and every `STATE §N` anchor | `has_restatement`, **which lives inside the permanent tail** | full-tail removal → **0 errors** |
| governed margin basis | the margin's denominator identity | the existence of *some* positive adjacent pair | a basis of any magnitude is accepted, including one that predates a structural change |

**Second: the lifecycle machinery is now the dominant consumer of the budget it
enforces.** Measured across the v0.32→v0.33 delivered exports, with the
archival's one-time reclaim held separate:

| component | bytes/cycle | share of net growth | reclaim mechanism |
|---|---|---|---|
| `tools/cycle_check.py` + `tools/invariant_scan.py` | **+35,138** | 45.1% | **none** |
| their tests + `config/invariant-rules.json` + `tools/evidence_artifacts.py` | +15,416 | 19.8% | **none** |
| `STATE.md` | +31,177 | 40.0% | archival — **just fired, next one ≈8 cycles out** |
| `ARCHITECTURE.md` + `AGENTS.md` | +4,568 | 5.9% | none |
| `config/protected-artifacts.json` | +647 | 0.8% | deferred, 1,324 cycles of margin |
| cycle documents, net of retention | −9,084 | −11.7% | retention — **at steady state** |
| **net** | **+77,862** | 100% | — |

**Roughly 72% of per-cycle export growth now has no reclaim mechanism at all,
and 65% of it is the checkers.** The export's largest single group is no longer
`STATE.md` or the cycle documents — it is `tools/` at **602,232 bytes / 23.0%**.
`cycle_check.py` grew 17% and `invariant_scan.py` grew 14% in one cycle.

The arithmetic that follows is the reason this is a cycle subject and not an
observation. The export has **365,308 bytes** of margin at the delivered tree.
At **+77,862/cycle** that is **4.69 cycles** — a breach around **v0.38**. The
next `STATE.md` archival becomes available at **≈7.9 cycles** — around **v0.41**.
**The export breaches roughly three cycles before its largest lever returns.**

The objective of v0.34 is that **no control's admission depends on the thing it
protects**, and that the operator chooses the export lever on measured
projections rather than at the ceiling.

---

## Declared scope

| Scope class | Path or value |
|---|---|
| `scope_version` | `1` |
| `disposition_intent` | `no-release` |
| `allow` | `tools/cycle_check.py` |
| `allow` | `tools/invariant_scan.py` |
| `allow` | `config/invariant-rules.json` |
| `allow` | `shell/tests/**` |
| `allow` | `AGENTS.md` |
| `allow` | `ARCHITECTURE.md` |
| `allow` | `tools/export_check.py` |
| `allow` | `repomix.config.json` |
| `allow` | `tools/version_check.py` |
| `forbid` | `docs/state-archive/**` |
| `forbid` | `config/protected-artifacts.json` |
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
| `forbid` | `observations/**` |
| `forbid` | `fixtures/**` |
| `forbid` | `docs/cycles/**` (except this runbook and `PROGRESS-v0.34.md`, by standing precedence) |
| `release_authority` | `Cargo.toml`, `Cargo.lock`, `crates/*/Cargo.toml`, `apps/*/Cargo.toml`, `shell/intel_shell/__init__.py`, `shell/intel_shell/app.py`, `CHANGELOG.md`, `README.md` |

**`docs/state-archive/**` returns to `forbid` and
`config/protected-artifacts.json` returns to `forbid`.** The v0.28 archive is
now a pinned structural artifact at SHA-256
`b9442f7bedf9024351ef0bafe0e6f7a4d58a0883e9c2f81bbbadebfb476d5886`. Editing
either path would move a pin or the bytes it protects. **A write to either is a
scope finding, not a convenience.**

**`disposition_intent` is `no-release`, and the reason is structural.** Every
production source, workflow, publisher and scheduler path is forbidden, and no
step is scheduled to change runtime behaviour or any `/v1/*` surface. **Step 7
verifies this against the measured diff rather than inheriting it from this
table.** If a step measures a production behaviour change, the scope gate was
violated and the disposition reopens before Step 6, not at Step 7.

---

## Entering state

**Every line here is a hypothesis. Report the measured value, especially where
it differs.**

- v0.33 closed **2026-08-01** with `no-release`. Closing implementation
  `70781081abd42ed9a49e22ed100efdb039a9b762`; audit child
  `e0ab6964f76b0a919c5214607ef141eb5b118deb`.
- Published **v0.17.1** remains current: `main` and peeled tag at
  `f02379f03ccdfd1b019413234f2ad014d169fb04`, annotated object
  `14912f134e45277e2b4fd10b7f5bf8b4900ca20d`, release commit
  `7a621e39a069a1ef26438e841e7bb1ca2f34165b`.
- `ci-local` **20/20**; Python 3.11.4 and 3.12.13 each **348/348**;
  `invariant-scan` **12 rules / 68 controls**; golden **11/11**, delta **0**;
  `checklist-audit` **261 / 3 / 261 / 261**; manifest **332 pins /
  192,042 bytes**; retractions held at **3**.
- `STATE.md` is **206,530 bytes** against **453,741**, leaving **247,211** —
  **7.93 cycles** at the latest positive same-kind **+31,177**.
- The delivered export is **2,634,692 bytes / 153 files**, retaining exactly
  v0.31–v0.33. The recorded closing-tree figure is **2,628,346**; the delivered
  export is **6,346 bytes** larger, **consistent with the audit child but not
  proven to be it**. E0 owns that confirmation.
- The governed row evaluates **2,592,441** with **407,559** remaining and
  **5.29 cycles** on the v0.31→v0.32 governed basis of **+77,014**.
- **`tools/` is the largest export group at 602,232 bytes / 23.0%.**

---

## Gaps this cycle must settle

| Gate | Sources | What must be measured |
|---|---|---|
| **G1** [P1] | `tools/cycle_check.py` `check_state_archival_region_contract`; `state_has_registered_current_restatement`; `tools/version_check.py` | **The region contract's admission depends on the region it protects.** Executing the shipped contract directly, I measured: renamed `## 5.` heading → **1 error**, naming every unresolved reference; §1–§6 archived with §7 kept → **1 error**; **entire permanent tail removed → 0 errors**; duplicated marker → **1 error**. Confirm all four at the complete `./run cycle-check` entry point. Then state plainly **which check, if any, catches full-tail removal from inside `cycle-check`**, and whether `version-check`'s zero-extraction rejection is the only floor. **Enumerate every remaining `return None` and early `return` in the contract and in `check_publication_status`, and say for each whether a construction reaches it silently.** |
| **G2** [P1] | `tools/cycle_check.py` margin basis selection; `ARCHITECTURE.md` review-export row; every tracked `PROGRESS-v*.md` governed measurement | **The basis rule enforces identity and arithmetic but not representativeness.** The code accepts any positive adjacent delta as the denominator with no floor and no epoch awareness. Two consequences to measure: **(a)** construct a governed series whose latest positive adjacent delta is small — a few thousand bytes — and record what margin the real entry point then accepts; **(b)** state explicitly that the current live basis, v0.31→v0.32, **predates the v0.33 archival**, and whether the check can know that. **Derive the full governed series over every tracked progress record and report every adjacent delta, positive and negative, with its sign.** |
| **G3** [P1] | both delivered exports; `tools/export_check.py`; `repomix.config.json` | **Derive the export growth decomposition and project the breach cycle.** Per component, per cycle, over as many delivered or governed pairs as the tracked records allow — not just the one pair this reviewer could measure. State each component's bytes/cycle, its share, and **whether it has any reclaim mechanism**. Then project the ceiling breach and the next `STATE.md` archival availability under named denominators, and **say which arrives first**. My arithmetic is 4.69 cycles to breach against 7.9 to the next archival; **confirm or refute with the fuller series.** |
| **G4** [P2] | `ARCHITECTURE.md` v0.28 export row; `STATE.md` v0.28 records; `config/protected-artifacts.json` | **The 3,000,000-byte ceiling is a proxy and its referent should be restated.** v0.28 recorded an external project-knowledge observation of **2,067 chunks against a 2,000 limit** alongside a then-4,975,987-byte export. Determine by search what the ceiling is currently understood to stand for, whether any tracked record still states the referent, and **whether the referent itself is measurable from inside the repository.** If it is not, say so — a proxy that nobody can check against its referent is a number, and the row should say which it is. |
| **G5** [P2] | `tools/cycle_check.py`; `tools/invariant_scan.py`; `shell/tests/test_cycle_check.py`; `config/invariant-rules.json` | **Measure the control-growth trend, not just this cycle's total.** v0.33 added **7** controls and shifted **25 of 61** existing `expected_line` values — 41% churn. Derive the per-cycle series of control count, shifted-value count, and combined checker bytes across the retained window. **State whether the deferred `Planted-control line numbers re-derived by hand` trigger — "a cycle in which the re-derived count exceeds the controls it protects" — is approaching, and at what rate.** |
| **G6** [P3] | `ARCHITECTURE.md` dispositions; the v0.33 deferred table | **Which governed byte boundary is nearest is no longer the one the records last named.** The last current statement of nearest-boundary is v0.32's, and it says `STATE.md`. Post-archival the export is nearer by roughly three cycles. **Restate the ranking with a dated v0.34 measurement and confirm that no live row still asserts the superseded ordering.** |

---

## Governed artifact byte-boundary authority

- governed artifact byte boundary: path=`STATE.md`; bytes=`453741`
- governed artifact byte boundary: path=`config/protected-artifacts.json`; bytes=`1048576`

**Carried forward byte-identically.** A change to either figure is an
architectural change requiring its own justification and operator
authorization. **The 3,000,000-byte export ceiling is separately governed and
G4 examines what it stands for — examining a number is not proposing to move
it, and Step 5 is the only place a move may be selected.**

---

## Deferred means deferred

Every trigger is carried **unchanged**. The observation column is rewritten with
**v0.34** dated measurements; the trigger column is not edited to match what
happened.

| Deferred item | Unchanged trigger | Measured observation (cycle-identified) | v0.34 action |
|---|---|---|---|
| T7 robots single-flight | a second concurrent harvester | v0.34 · 2026-08-02 — no second concurrent harvester ran; trigger did not fire | none |
| NEGATIVE-CACHE Decision B | a live transient robots outage for an admitted publisher while a usable last-known-good policy exists, plus operator authorization | v0.34 · 2026-08-02 — no publisher request, outage exercise, or operator authorization occurred; trigger did not fire | none |
| Conditional GET (`ETag` / `If-Modified-Since`) | an operator-authorized cycle whose scope permits the `net` request path plus a live 304 observation | v0.34 · 2026-08-02 — scope forbade the net request path and no live 304 was observed; trigger did not fire | none — the gap stays recorded |
| `edgar:*` extension field mapping | an operator-authorized cycle permitting `crates/ingest/src/**` for mapping, with a connector review | v0.34 · 2026-08-02 — production source remained forbidden and no connector review occurred; trigger did not fire | none |
| Live multi-publisher behaviour in one runtime | further origins beyond the two configured, or concurrency | v0.34 · 2026-08-02 — no live third origin or concurrent publisher runtime ran; trigger did not fire | none — complete, do not re-exercise |
| First recurring scheduled SEC run | explicit operator authorization of a bounded scheduled window, separate from any cycle scope | v0.34 · 2026-08-02 — no scheduler or service ran and no authorization was supplied; trigger did not fire | none — the 600-second clock still has never issued a request |
| Postgres / pgvector / multi-host seam | unchanged | v0.34 · 2026-08-02 — no topology, dependency, schema, or production-source path changed | none |
| A4 untrusted-shell boundary | a third-party/untrusted shell, or any claim HC1 is invariant under shell replacement | v0.34 · 2026-08-02 — no third-party shell or replacement-invariance claim appeared; trigger did not fire | none |
| L2 forced-command wrapper | an operator server session | v0.34 · 2026-08-02 — no model-profile command or server session occurred; trigger did not fire | none — remains scheduled |
| R3/R4 open-bottom coverage | a spelling outside registered vocabulary | v0.34 · 2026-08-02 — the registered vocabulary passed and no new spelling appeared; trigger did not fire | none |
| `--features net` Rust 1.86 execution | a scoped cycle authorized to change evidence topology and an executable local or hosted lane that actually pins and runs the net path on Rust 1.86 | v0.34 · 2026-08-02 — no executable Rust-1.86 lane was added; trigger did not fire | none |
| Third configured publisher | a completed compliance review, then a separate admission decision | v0.34 · 2026-08-02 — no compliance review or admission decision occurred; trigger did not fire | none |
| `v0.8.0` / `v0.10.2` publication | operator-authorized push of both exact annotated objects | v0.34 · 2026-08-02 — neither historical tag was present remotely and no historical ref moved; trigger did not fire | none — no historical ref touched |
| `--skip-local-tag-verification` removal | both historical tags published plus a passing hosted full-history `cycle-check` without the flag | v0.34 · 2026-08-02 — both tags remained absent and the flag remained unchanged; trigger did not fire | none — the flag stays |
| Manifest retention/indexing | the manifest reaches its governed artifact byte boundary, or two consecutive clean `./run verify-artifacts` runs each take ≥1.00 s real | v0.34 · 2026-08-02 — two complete real-workspace runs measured the unchanged manifest at 192,042 bytes / 332 pins and matched both protected databases in 0.12 s / 0.10 s real; neither trigger fired | none — the archive pin is registered and the manifest is `forbid` this cycle |
| Version literal in `app.py` | a cycle whose declared scope permits shell source changes | v0.34 · 2026-08-02 — no shell source or release value changed; trigger did not fire | none — `shell/intel_shell/**` is forbidden |
| Release-classification criteria with no executed control | an operator decision that prose adjudication is insufficient | v0.34 · 2026-08-02 — no such operator decision was supplied; trigger did not fire | none — recorded, not acted on |
| Second `STATE.md` archival | the export ceiling trigger fires, or `STATE.md` reaches its governed artifact byte boundary | v0.34 · 2026-08-02 — exact delivered State was 206,530 / 453,741 bytes, leaving 247,211 bytes or 7.93 cycles at the latest 31,177-byte same-kind growth; the delivered export was 2,634,692 / 3,000,000 bytes, leaving 365,308 bytes or 4.69 cycles at the latest 77,862-byte pre-reclaim growth. The export is nearer; neither trigger fired | Step 1 — G3 places the next archival availability in cycles |
| **Planted-control line numbers re-derived by hand** | a control-schema change, or a cycle in which the re-derived count exceeds the controls it protects | v0.34 · 2026-08-02 — Step 3's emitted-bound source path added no control and changed no control schema. Its first complete gate stopped on one stale existing location; exact R12 control-37 replay emitted line 2935, which was copied rather than offset-computed. The latest 1 is 67 below the unchanged 68 controls protected, so neither trigger clause fired. Step 2's earlier 27-value schema-change re-derivation remains preserved in its dated task and progress record | Step 3 — completed; the one shifted value came from emitted output |
| Retention derivation across a version-family boundary | an active cycle whose name is not of the form `v0.<n>` — raising at `v1.0`–`v1.2`, silently under-excluding from `v1.3` onward | v0.34 · 2026-08-02 — v0.34 still matched `v0.<n>`; trigger did not fire | none — recorded, not acted on |
| Published-release divergence | the unpublished distance contains a measured runtime behaviour difference persisting across three consecutive closed cycles within the current publication epoch, or acquires any public-surface change | v0.34 · 2026-08-02 — no measured runtime or public-surface change existed; the publication-epoch count remained zero | Step 7 — restate the epoch count under the v0.32 reset rule |
| MSRV current-restatement membership | a current restatement of either Rust floor lands outside the registry without failing a check | v0.34 · 2026-08-02 — contextual floor predicates found no unregistered live current restatement; trigger did not fire | none — completed control remains active |
| Retention arithmetic fallback | the `retained_cycle_paths=None` branch produces an answer that differs from the tracked retained set in any construction a control or test relies on | v0.34 · 2026-08-02 — production supplied the Git-derived set while synthetic fallback divergence remained possible; trigger did not fire | none — recorded, not acted on |
| Optional cycle-ending audit disclosure | a closed cycle whose delivered export differs from its governed figure and which records no cycle-ending audit field | v0.34 · 2026-08-02 — the general checker retained deliberate optionality and v0.33 separately recorded its required audit field | none — the v0.32 ruling stands; this runbook separately requires its own |

---

## Step 1 · E0 — Rebuild the entering state and settle G1–G6 🤖

**Objective.** Confirm `HEAD` is green and settle all six gates. **Every line
under `## Entering state` is a hypothesis.**

**Decision gate.** If the worktree is dirty apart from this untracked runbook,
if the v0.33 closing and audit commits are not where the entering state places
them, if published v0.17.1 identity has moved, or if any local gate fails at
entry — **record and stop.**

**Acceptance criteria.**

- All **20** `ci-local` jobs pass; `invariant-scan` passes its registered
  self-test with rule and control totals stated; golden **11/11**; all pins
  verified twice with both real times recorded; both Python lanes reported
  through `tools/test_population.py`, never as a bare `N/N`.
- Published state confirmed **by direct remote inspection**, not from the
  closing record.
- **The delivered-export identity is settled** by measuring `./run export-check`
  at the exact audit-child tree `e0ab6964f76b0a919c5214607ef141eb5b118deb`.
  The reviewer measured **2,634,692 bytes** and inferred the audit child from a
  6,346-byte difference; **confirm or refute by measurement.**
- G1 settled **by execution at the real entry point**, with all four
  constructions recorded verbatim and every silent early return enumerated.
- G2 settled **by construction and execution**, with the small-denominator case
  run against the real entry point and the full governed series reported with
  signs.
- G3 settled **by derivation across every pair the tracked records allow**, with
  each component's reclaim mechanism stated and the two projections compared.
- G4 settled **by exhaustive search**, with the ceiling's referent named or its
  absence stated plainly.
- G5 settled **by derivation**, with the trend series reported.
- G6 settled, with the superseded nearest-boundary claim confirmed as dated
  history and not a live assertion.
- The deferred table is rewritten with **v0.34** measured observations, triggers
  unchanged, and every trigger-bearing `ARCHITECTURE.md` row carries a v0.34
  measurement.
- The governed-export exemption reported at activation is recorded **by name**.

**Done when** every gate carries a measured answer and the entering state is
confirmed or corrected in `STATE.md`.

- [x] **E0**

---

## Step 2 · Break the region contract's circular precondition 🤖

**Objective.** Make the State region contract detect the destruction of the
region it protects, without borrowing the answer from another tool.

**Dependency gate.** Requires G1 settled. **If G1 refutes the finding at the
real entry point — if `./run cycle-check` rejects full-tail removal through some
path this reviewer did not execute — this step is cancelled and instead records
the refutation and names the check that supplied the floor.**

**The shape, measured.** `check_state_archival_region_contract` gates its
marker-count rule on `has_restatement`, and `has_restatement` delegates to
`version_check.offline_msrv_report` over a line that lives inside the permanent
tail. When an over-cut removes the tail, the restatement goes with it, the
marker rule is skipped, `not marker_matches` is true, `not top_headings` is
true, and the function returns `None` having reported nothing. **The guard's
precondition is inside the thing it guards.**

**Acceptance criteria.**

- **The rejection precedes the acceptance.** Record the real entry point's
  output for full-tail removal before the fix and after it.
- A `STATE.md` with no permanent-tail marker and no numbered top-level heading
  produces a **named defect from `cycle-check` itself**, not from
  `version-check`. The two tools may both report; **`cycle-check` reporting
  nothing is the failure this step exists to remove.**
- **The delegation to `version_check` is not removed** — it is the correct
  answer to the duplicate-control problem and v0.33 was right to build it. What
  changes is that the *structural* rules no longer depend on it. **State which
  rules are structural and which are semantic, in the check's own emitted
  text.**
- Every remaining silent early return enumerated by G1 is either given a named
  defect or given a **recorded bound in the check's emitted output stating why
  it cannot have one.** One of the two for each, not neither.
- Registered R12 plants the full-tail-removal case and observes the real entry
  point missing it when the branch is disabled. Every shifted `expected_line`
  value is **re-derived from real emitted self-test output** and the count
  recorded.
- Focused lifecycle tests pass with the count stated; the complete `ci-local`
  entry point passes **with the task box still open**; standalone `./run golden`
  passes **11/11** with delta **0**.

**Done when** no construction of `STATE.md` causes the region contract to report
clean by examining nothing.

- [x] **REGION-FLOOR**

---

## Step 3 · Bound the margin basis 🤖

**Objective.** Make the governed margin state what its denominator can and
cannot support.

**Dependency gate.** Requires G2 settled.

**The shape.** The basis rule correctly requires the *latest positive adjacent
same-kind governed pair* and verifies the arithmetic exactly. It says nothing
about whether that pair is representative, and nothing about whether it
predates a structural change such as an archival. The live basis is
v0.31→v0.32; **the v0.33 archival happened after it.**

**Acceptance criteria.**

- **One of these two ships, not neither:** either the basis acquires a stated
  representativeness constraint that the entry point enforces — a floor, a
  trailing window, or an epoch marker — **or** the check's own emitted output
  names the limit explicitly, in the manner of v0.32 Step 3's value-closure
  bound. **A limit stated in prose beside the check is not the check saying it.**
- If a constraint ships, the small-denominator construction from G2 is rejected
  by the real entry point and the rejection text is recorded verbatim.
- If a bound ships instead, it names **both** limits: that a single adjacent
  pair carries no representativeness guarantee, and that the check cannot detect
  a basis predating a structural change. **The reasoning for choosing a bound
  over a constraint is recorded, and "it is hard" is not a reason.**
- No dated historical margin figure is edited. **Corrections go forward.**
- If a control ships, R12 plants it and shifted `expected_line` values are
  re-derived from emitted output and counted.
- The complete entry point passes **20/20** with the task box open; golden
  **11/11**, delta **0**.

**Done when** the number that says how much room is left either cannot rest on
an unrepresentative basis, or says out loud that it might.

- [x] **BASIS-BOUND**

---

## Step 4 · Derive the export budget — measurement only 🤖

**Objective.** Establish, by measurement rather than by this reviewer's single
pair, what consumes the export budget and when it runs out.

**Dependency gate.** Requires G3 and G5 settled. **This step ships no lever, no
ceiling change, no retention change, and no exclusion.** It produces the
measurement Step 5's decision rests on. **A step that both measures the problem
and picks the answer cannot report that the answer was chosen on the
measurement.**

**Acceptance criteria.**

- A per-component, per-cycle growth table derived over **every pair the tracked
  governed and delivered records support**, not one pair. Each row states
  bytes/cycle, share of net, and reclaim mechanism or its absence.
- Archival and retention reclaims are held **separate** from steady-state
  growth. A one-time reclaim mixed into a growth denominator is exactly the
  v0.32 defect and it is not repeated here.
- The ceiling-breach projection and the next-archival-availability projection
  are both stated in cycles under named denominators, with **which arrives
  first** said plainly.
- **The measurement is recorded whether or not it supports the reviewer's
  arithmetic.** If the fuller series contradicts 4.69 versus 7.9, the
  contradiction is the finding and this runbook's root-cause table is corrected
  in the closing record.
- No file outside `STATE.md`, this runbook, and `PROGRESS-v0.34.md` is written.

**Done when** the budget is a measured series rather than a projection from one
observation.

- [ ] **BUDGET-DERIVE**

---

## Step 5 · Select and implement the export lever 🧑🤖

**Objective.** Act on Step 4's measurement, or record a dated decision not to.

**Dependency gate.** Requires Step 4 complete. **If Step 4's series shows the
breach is further out than six cycles, the operator may select Option E and this
step closes with a dated deferral rather than an implementation.**

**🧑 Operator decision — the lever.** Each option's effect must be **measured on
a throwaway construction before selection**, not estimated:

- **Option A — retention depth 3 → 2.** One-time reclaim of roughly one cycle
  pair (≈98,000 bytes) plus a small steady-state reduction. **Costs
  reviewability: the reviewer would see the active cycle and one prior instead
  of two.** Touches `tools/export_check.py` and `repomix.config.json`.
- **Option B — split the export.** A source export and a lifecycle-tooling
  export, reviewed on alternating cycles or delivered as two artifacts.
  Addresses the 65% of growth that has no lever. **Costs a review-protocol
  change and needs an explicit statement of what a single-artifact reviewer can
  no longer see in one pass.**
- **Option C — re-derive the ceiling against its referent.** Only available if
  G4 finds the referent is measurable. **If G4 finds it is not, this option is
  withdrawn rather than exercised on a guess.**
- **Option D — reduce checker growth at source.** Consolidate or factor
  `cycle_check.py` and `invariant_scan.py`, whose combined 243,492 bytes are
  9.3% of the export and 45% of its growth. **Highest risk: it edits the two
  files every control depends on, in a cycle that is also adding controls.**
- **Option E — dated deferral.** Record the projection, set an explicit trigger
  with a cycle number, and change nothing. **Legitimate if and only if Step 4's
  series supports it; "not yet urgent" is a measurement, not a feeling.**

**Neither A nor E is defaulted.** The reviewer's recommendation is **Option A
plus Option E's dated trigger** — A is the smallest reversible reclaim and buys
roughly 1.3 cycles, and the trigger makes the larger question return on a date
rather than at the ceiling. **B and D are the real answers to the 65%, and both
deserve their own cycle rather than a step in this one.** The decision is the
operator's.

**Acceptance criteria.**

- The selected option's measured effect is recorded **before and after** on
  named trees, in bytes and in cycles under same-kind denominators.
- Under Option A, `export_check`'s retention derivation and
  `repomix.config.json`'s pattern move together and the stale-pattern rejection
  is produced verbatim, as at every prior retention change.
- Under Option E, the deferral carries **a cycle-numbered trigger**, not a prose
  condition, and enters the deferred table with that trigger.
- Whatever ships, `checklist-audit` does not fall, the complete entry point
  passes, and golden passes **11/11** with delta **0**.
- **No governed byte boundary and no ceiling moves except under an explicitly
  selected option that names it.**

**Done when** the budget question has a dated operator answer.

- [ ] **BUDGET-LEVER**

---

## Step 6 · RE-MEASURE — authenticate the exact candidate 🧑🤖

**Objective.** Put release-grade authenticated evidence on the exact candidate,
on a fresh ref that says what it is.

**Acceptance criteria.**

- The candidate is the exact clean tree. **The ref is fresh:**
  `codex/v0.34-evidence-<sha7>`, its prior non-existence confirmed by
  `git ls-remote` **before** any push, its post-push readback confirmed, and
  both facts recorded. **A reused ref is a finding to record, not a detail to
  omit.**
- 🧑 The operator explicitly approves publishing the measured candidate to that
  new ref. It is the only remote mutation this step may perform.
- All seven executable hosted jobs pass; every receipt, attestation, bundle and
  persistence step passes; the repository verifier states accepted and rejected
  counts, and every accepted identity binds the exact candidate digest **and the
  fresh source ref**.
- Both shell lanes compared by `tools/test_population.py`, with every figure the
  comparator's output and none transcribed from a runner log.
- All pins verified, including the v0.28 archive pin, unchanged; golden
  **11/11** locally and hosted.
- **No publisher request, scheduler run, model-profile command, manifest
  registration, or protected-byte write.**
- Remote `main`, the peeled `v0.17.1` tag, and its annotated object are
  re-measured after the run and confirmed unmoved.

**Done when** the candidate carries release-grade authenticated evidence on a
ref that says what it is.

- [ ] **RE-MEASURE**

---

## Step 7 · R-CLOSE — close v0.34 with a reasoned disposition 🧑🤖

**Objective.** Close v0.34 with an explicit, reasoned disposition.

**🧑 The operator's decision, and only the operator's.** Publication
authorization is a separate explicit act, **not** implied by this runbook, by
green gates, or by hosted evidence. Two outcomes, neither defaulted:

- **`no-release`** — close on v0.34's own record and state **what the
  unpublished distance now contains**, measured against published v0.17.1. A
  distance of lifecycle controls, export configuration and cycle records is a
  reason; **"nothing shipped" is a weaker statement and is not substituted for
  it.**
- **`release` at patch** — only if a step measured something belonging in users'
  hands, which under this scope would itself be a scope finding. Selecting it
  means reopening the disposition **before** Step 6.

**Acceptance criteria.**

- The closing record names the closing date and the dated disposition and, under
  `no-release`, enumerates the intentionally unreleased commits with every
  version source and tag unchanged.
- **The governed export row equals the last governed field the closing tree can
  already see**, its margin uses the corrected basis rule, and the closing
  tree's own export appears only in the audit child's `cycle-ending
  review-export audit` field.
- **The nearest governed byte boundary is named with a dated v0.34 measurement**
  and no live row asserts the superseded ordering.
- Every declared permission is reconciled as used or unused, **by path**,
  including confirmation that `docs/state-archive/**` and
  `config/protected-artifacts.json` are byte-unchanged.
- The published-release divergence row restates the epoch count under v0.32's
  reset rule with a dated v0.34 observation.
- The count of `expected_line` values shifted across the cycle is stated and
  compared against the controls they protect, **with G5's trend series beside
  it**.
- Every reviewer error is recorded **in this file's header, not in the closing
  record**.
- 🧑 The operator authorizes the disposition explicitly.

**Done when** v0.34 is closed on a record that says what it did and what it
deliberately did not.

- [ ] **R-CLOSE**

---

## Standing prohibitions

1. **No publisher request, harvest, scheduled process, service, or
   model-profile command.** The SEC 600-second clock is not authorized to issue
   traffic by this cycle or by anything in it.
2. **No production source, workflow, dependency, schema, or release-value
   change.**
3. **No write to `docs/state-archive/**` or `config/protected-artifacts.json`.**
   Both are `forbid`; the v0.28 archive is a registered pin.
4. **No closed cycle document is moved, edited, or deleted.**
5. **No historical ref is created, moved, or deleted**, including `v0.8.0` and
   `v0.10.2`.
6. **No `expected_line` value is computed by hand.** Every one is re-derived
   from real emitted self-test output and counted.
7. **No figure is transcribed from a runner log** where a comparator exists.
8. **Every export figure names the tree it was measured on**, and **no one-time
   reclaim is mixed into a growth denominator.**
9. **No dated historical measurement is edited to match a later understanding.**
10. **`checklist-audit` must not fall**, and the retraction count stays at
    **three** unless a twice-verified measured false claim in an immutable
    published record is produced.
11. **Step 4 ships no lever.** Measurement and selection stay in separate steps.

---

## Cycle checklist

- [ ] Worktree clean at entry apart from this untracked runbook
- [ ] `AGENTS.md` active-cycle declaration advanced to **v0.34**
- [ ] `PROGRESS-v0.34.md` created and appended per step, after each
      implementation commit exists
- [ ] Retention advanced; the activation rejection text recorded verbatim if the
      stale-glob construction is exercised
- [ ] All six gates settled with measured answers
- [ ] Deferred table rewritten with v0.34 observations, **triggers unchanged**
- [ ] Every trigger-bearing `ARCHITECTURE.md` row carries a v0.34 measurement
- [ ] Nearest governed byte boundary restated with a dated measurement
- [ ] Closing record + append-only audit child, per the tagged-close protocol
- [ ] Cycle-ending review-export audit field present in the audit child

---

## Provenance

**Measured by this reviewer, by executing the shipped code.** The publication
admission gate was re-run against four constructions and now rejects all three
failure cases with distinct named defects; the header-shape branch is reachable
and fires on `**AS OF:**` and `**As of :**`. The State region contract was run
against four constructions: renamed `## 5.` → 1 error naming
`crates/compliance/src/lib.rs:24`, `crates/ingest/src/arxiv_oai.rs:28`,
`rust-toolchain.toml` and others; §1–§6 archived with §7 kept → 1 error naming
`.github/workflows/ci.yml:293=§6b`, `AGENTS.md:149=§6`, `ARCHITECTURE.md:6=§2`
and others; duplicated marker → 1 error; **entire permanent tail removed → 0
errors.** `version_check` on that last tree rejects with the zero-extraction
error, so the composite fails — **through the other tool.**

**Measured by this reviewer, by direct file measurement and diff of the two
delivered exports.** The v0.33 export at **2,634,692 bytes / 153 files**,
retaining exactly v0.31–v0.33 with `docs/state-archive/**` absent; `STATE.md` at
**206,530**; `tools/` at **602,232 / 23.0%**; `cycle_check.py` at **114,466**
and `invariant_scan.py` at **129,026**; and every per-file delta in the
root-cause table. Gross growth **+153,616**, gross reclaim **−253,293**, net
**−99,677** against the recorded **−99,674**.

**Derived by arithmetic.** The **+77,862/cycle** steady-state figure and every
share in the root-cause table; **4.69** cycles to breach and **7.93** to the
next archival; the confirmation that the v0.33 archive at **178,125 bytes**
matches this reviewer's v0.33 pre-flight figure exactly, and that Cut B was the
selected option.

**Confirmed against Codex's report.** 348/348, 12 rules / 68 controls, golden
11/11 delta 0, checklist 261/3/261/261, closing-tree export 2,628,346 with
audit delta +35,905, manifest 192,042 / 332 pins with the archive pinned,
governed candidate 2,592,441, and the margin field's arithmetic —
`407559 / 77014 = 5.29` — all verify.

**Inferred, not measured.** That the delivered export corresponds to audit child
`e0ab6964f76b0a919c5214607ef141eb5b118deb`; the 6,346-byte difference is
consistent with it, and **consistency is not identity.** E0 owns it.

**Asserted and not verified.** Every entering-state line not listed above; all
hosted run contents, ref topology and remote state; whether
`./run cycle-check` as a whole behaves as the isolated functions did — only the
individual functions were executed, on a reconstruction from an XML export
rather than a repository clone.

**Not verifiable by this reviewer at all.** The contents of
`docs/state-archive/STATE-through-v0.28.md`, which is export-excluded — **so the
archive whose fidelity v0.33 made executable is one this reviewer still cannot
read, and the pin is trusted rather than checked here.** Also unverifiable: any
cycle document older than v0.31, and therefore the fuller growth series G3
requires, which is exactly why G3 is Codex's to derive and not this runbook's to
assert.

**One reviewer error is recorded in this file's header** rather than here,
because a provenance note is where a reader looks last and an error is what they
should see first.
