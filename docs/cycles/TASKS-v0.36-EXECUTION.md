# TASKS-v0.36-EXECUTION.md — empty-witness acceptances

**Cycle:** v0.36
**Entering release:** v0.17.2, closed locally at v0.35, **unpublished**
**Entering ref (hypothesis):** closing commit `9996c6820d720160b64607575d0270d2e5393ef9`
**Prior cycle:** v0.35 — closed locally, **not fully discharged under its own
acceptance criteria**
**Autonomy:** Step 0 installs standing cycle authority. After it lands, one gate
remains (§3). Everything else is Codex's to decide and record.

---

## 0. Why this cycle exists

### Named root cause: **empty-witness acceptance**

Findings that look independent are one defect wearing several costumes. Each
acceptance was discharged by an executable whose witness set was empty, and an
empty witness is indistinguishable from a passing one:

| Finding | The claimed property | The witness actually executed |
|---|---|---|
| G1 | store canonical identity ≡ view canonical identity | `assert_eq!(vec![], vec![])` on a single-sector corpus |
| G2 | every checked v0.35 task resolves to progress and a commit | zero v0.35 boxes examined |
| G3 | the closing tree was export-audited | no audit child exists |
| G6 | public value-domain changes take a minor version | `AGENTS.md` says outright: "no executed control enforces it" |

Same family as the unsatisfiable checker rules, the silent no-op paths, the
vacuous regex patterns. The standing principle is unchanged — **a claimed
property that nothing executes is not a property.** v0.36 adds the missing
clause: *and a property whose executable witness is empty is not executed.*

Every remedy here has two halves: fix the instance, and make the emptiness
itself a failure.

---

## 1. Gaps carried in from v0.35

| # | Priority | Gap | Measured basis |
|---|---|---|---|
| G1 | **P1** | Persisted canonical identity is sector-scoped; both governing documents state a global rule; no control distinguishes them | `assign_canonical_ids_tx` orders `sector, published_day, id` and calls `kept.clear()` on each sector change. `AGENTS.md` and `ARCHITECTURE.md` §8 both say "re-materialized from the global rule (earliest by `(published_day, id)`)". `dedup_near` sorts `(published_day, id)` with no sector axis. |
| G2 | **P1** | `checklist-audit` examined **zero** v0.35 boxes | `CHECKED_RE = ^- \[x\] \*\*([^*]+)\*\*` requires bold; all nine v0.35 boxes are unbolded. Direct measurement: v0.34 → 7 matched of 17 `- [x]` lines; **v0.35 → 0 of 9**. |
| G3 | **P2** | Step 7's mandatory `cycle-ending review-export audit` field is absent | Required at `TASKS-v0.35-EXECUTION.md:1091` — "This runbook requires that audit field". Zero occurrences in `PROGRESS-v0.35.md`; deferred there to "the first post-push append". |
| G4 | **P2** | v0.35 box ids and v0.35 progress ids are different namespaces | Boxes read `Step 1 · E0`; progress headers read `### 2026-08-02 · E0 — …`. `normalize_task_id` splits only on `" — "`, so the two never equate. |
| G5 | **P3** | `PROGRESS-v0.35.md` carries **zero** `- runbook:` fields | 16 entries, 16 `- commit:` fields, 0 `- runbook:` fields. Matching falls to the unqualified branch of `matching_commit`, order-dependent when two cycles share a task id. |
| G6 | **P2** | The public value-domain minor-version rule has no control | `AGENTS.md` (2026-07-30): "This criterion is prose adjudicated at R-CLOSE; no executed control enforces it." Same family as G1–G3, self-declared. |

**Reachability of G1 is higher than the v0.35 self-review recorded.** It reports
the divergence as hidden because both protected databases hold one sector.
`config/subscriptions.json` entitles `acme-research` to `["science",
"technology"]`; `compute_view_resp` hands `sector_corpus(st, sectors)` — the
whole requested set — to `dedup_near` in one batch; `config/core.json` defines
both sectors and `config/schedule.json` harvests both for that client. The
shipped default configuration reaches it.

**And it crosses a license class.** `arxiv-cs` (science) is `IndexOnly`;
`techwire` (technology) is `CcBy`. A cross-sector collapse makes one license
class's document the representative for another's in `/view` analysis output.
`STATE.md` tracks entitlement/licensing outcome as a must-not-move class.

---

## Step 0 · AUTONOMY — install standing cycle authority

**Runs first, before ACTIVATE.** Everything after Step 0 executes under the
authority Step 0 installs. This step edits files outside the cycle documents;
that is intended and is the whole point of running it first.

### 0a — why the authority is needed, in one measured example

`AGENTS.md` currently says of the export audit: *"its `bytes` value and
`audit_delta` are backed by the operator-local command and captured output."*
Elsewhere it says *"Operator-local `./run export-check` remains the real-byte,
retained-set, and excluded-content control."*

Read one way, **operator-local** names where a command runs — the local machine
rather than a hosted runner. Read another way, it names *who* runs it. Under the
second reading a mandatory local measurement becomes something Codex cannot
perform, and the only remaining home for it is "the first post-push append" —
which is exactly where v0.35 put it, and exactly why G3 exists.

So 0a is a one-sentence disambiguation, added adjacent to the existing
definition in `AGENTS.md`:

> **"Operator-local" names the execution environment, not the executing party.**
> It means a command that runs on the local machine rather than a hosted runner.
> Codex running it discharges the requirement in full; no criterion is deferred
> on the grounds that a command is operator-local.

### 0b — add the standing authority block to `AGENTS.md`

Add a new section following the §8 pattern — marker-delimited, so it is
mechanically checkable. Use this text verbatim; it is written to be the
authority, not a summary of one:

```
<!-- CYCLE_AUTONOMY_AUTHORITY:START -->
**Cycle execution authority — standing, granted 2026-08-03 through
TASKS-v0.36-EXECUTION.md Step 0.** Within a declared cycle, Codex decides and
records rather than asking. This covers: selecting among design options a
runbook presents or leaves open; choosing implementation seams; setting
`accepted_by` on exemption, deferral, and disposition records to the authorizing
runbook by name; selecting a release disposition and version by the runbook's
stated rule; selecting a value inside an already-accepted boundary or ceiling;
registering new invariant rules and planted controls; editing any tracked file
the cycle's scope reaches, including `run`, `AGENTS.md`, and `ARCHITECTURE.md`,
with the justification the relevant document requires; and re-pinning
`authorization`-grade bytes in `config/protected-artifacts.json` after a
legitimate edit to the file they pin.

A recorded decision naming its basis and what would have changed it is complete
work. A question routed to the operator inside this scope is not.

Evidence-ref pushes are covered when all of these hold: the ref matches
`refs/heads/codex/v<cycle>-evidence-<short-sha>`; `git ls-remote` confirms
immediately beforehand that it does not exist, and the result is recorded; the
push is non-force and creates exactly that one ref; and `main` and every tag are
untouched. A pre-existing ref is a finding, not a detail.

**Ask first — this list is exhaustive and is not widened by convenience:**
publishing `main` or any release tag; admitting a publisher under the
`append_only_chained_records_with_wire_evidence_and_operator_approval`
lifecycle; writing, replacing, or re-pinning any protected database,
`observation`-grade byte, or structural-archive byte; moving an accepted
boundary or ceiling rather than selecting inside it; adding a retraction; any
change that moves an entitlement or licensing outcome for a configured
subscription; and any live publisher request against a real wire.

Decision gates under §1 are unchanged. A tripped gate still stops its task and
is recorded; this authority never converts a gate into a workaround. Autonomy is
permission to decide, never permission to proceed past a measurement.
<!-- CYCLE_AUTONOMY_AUTHORITY:END -->
```

### 0c — mirror it

Copy the block byte-identically into `docs/intel-platform-OPERATIONS.md`,
following the `MODEL_PROFILE_AUTHORITY` precedent. Mirror enforcement per
**C5**.

### 0d — re-pin what moved

If `run` changed, update its `authorization`-grade entry in
`config/protected-artifacts.json`. This is routine work, explicitly inside the
authority, and is **not** a stop condition — the stop condition names protected
databases, `observation`-grade bytes, and the structural archive, none of which
this touches.

### 0e — commit Step 0 by itself

One commit, no cycle work mixed in. `AGENTS.md` **Active cycle:** still reads
v0.35 at this point; ACTIVATE moves it next. If `cycle-check` objects to editing
the contract before activation, that objection is a finding worth recording —
report it and proceed by activating first, then applying 0a–0d.

**Acceptance.**
- Exactly one `CYCLE_AUTONOMY_AUTHORITY` block in each of the two documents, and
  the two are byte-identical — proved by the C5 rule, not by inspection.
- The mirror rule fails before the block is added to the second document and
  passes after. If it cannot be made to fail, it is not a control.
- `ci-local` clean; `verify-artifacts` matches every pin including any re-pinned
  `run`.
- The `operator-local` disambiguation is present and adjacent to the existing
  definition, not in a footnote.

---

## 2. Decisions taken — do not re-litigate

Settled. Execute them. If a measurement **refutes the stated basis** of one,
record the refutation, stop that step, continue with the rest of the cycle; do
not proceed on a falsified premise, and do not substitute a preference without a
measurement.

### DR1 — Canonical identity is sector-scoped at **both** layers

`/view` collapse is partitioned by sector so it agrees with the store. Both
governing documents are corrected to state the rule as **global within a
sector**, sector axis explicit.

Basis: (i) the alternative writes a persistent `canonical_id` from a science row
to a technology row — a cross-sector pointer inside the boundary registered rule
**R7** exists to keep scoped, and the shape of the retracted v0.12 HC2
cross-sector oracle; (ii) v0.11 STORE-IDENTITY through v0.26 R5 is four cycles
driving store and view toward *one* identity authority, and institutionalising a
semantic divergence now runs against that grain; (iii) `ARCHITECTURE.md` §8's
headline is "Dedup identity is a corpus property", and a view-level identity
that varies with the requester's entitlement set is a property of the question,
which that document reserves for `/retrieve` ranking only; (iv) the collapse
crosses a license class.

Refuting measurement: if E0 finds that sector-partitioning `/view` moves an
entitlement or licensing outcome, that is **stop-and-report** under §3, not a
reason to switch options.

### DR2 — v0.35 is **not** reconstructed; the correction is forward and dated

The unpushed chain is technically rebuildable — the closing commit and tag
object appear in zero tracked files, so reconstruction would rename no recorded
object. That is not the blocker. `PROGRESS-v0.35.md:1047` records `checklist
acceptance: PASS at the assembled closing worktree: 268 checked / 3 retracted /
268 matched / 268 commits resolved` — a dated measurement *of the tree it sits
in*. Correcting that tree makes the figure false, so it would have to be edited,
and **no dated historical measurement is edited** is a standing prohibition.
Forward correction wins on the project's own rule.

Every v0.35 byte stays as it is.

### DR3 — v0.35's boxes are exempted, with runbook-level acceptance

Nine entries in `config/checklist-exemptions.json`, one per v0.35 box, each
carrying the real measured cause — not a placeholder. Set
`accepted_by: "repository operator through TASKS-v0.36-EXECUTION.md Step 3"`,
following the precedent already in `config/checklist-retractions.json`.
Authorising this runbook *is* the acceptance.

The file-level `record_date` and `accepted_by` move accordingly; the current
value `"none; all checked tasks are resolvable"` becomes false and is replaced
with a true one.

### DR4 — No retraction

The bar is a twice-verified measured false claim in an immutable **published**
record. v0.35 is unpublished, and `268 / 3 / 268 / 268` is a true tool output
attached to a vacuous property, not a false measurement. The count stays at
**3**. If you believe the bar is met, quote it, state the verification, and stop
under §3 rather than acting.

### DR5 — Version disposition rule, pre-stated

Apply it; do not ask. In precedence order:

1. **Minor** if a new route or a new observable named surface ships.
2. **Minor** if the release adds a value to, removes a value from, or redefines
   a value in the domain of any field already serialized in a `/v1/*` response
   body — `AGENTS.md`, 2026-07-30. Ask of DR1 explicitly: does partitioning
   `/view` change *which values a field can take*, or only *which documents are
   selected*? Answer it in writing with the measurement. Document selection is
   not a value-domain change; say so, or find otherwise and take minor.
3. Otherwise **patch**.

Record the reasoning either way, and name the behaviour movement in the
disposition reason rather than letting the version number imply it didn't
happen.

### DR6 — Evidence-ref pushes are pre-authorised

Per the Step 0b block. No further request.

---

## 3. The one retained gate

**Publication of `main` or any release tag requires separate exact operator
authorisation.** Not granted here, not requested by this runbook.

It is the only irreversible act in the cycle: a published record becomes
immutable and falls under the retraction bar. Keeping it gated is what makes the
rest safe to run unattended.

**Stop-and-report conditions.** Halt the affected step, record the measurement,
continue with unaffected work, surface it at handoff:

1. A measurement indicates a **published** record contains a false claim.
2. A change would move an entitlement or licensing outcome for any configured
   subscription.
3. A change would write, replace, or re-pin a protected database, an
   `observation`-grade byte, or the structural archive. *(Re-pinning
   `authorization`-grade bytes such as `run` after a legitimate edit is routine
   and does not stop.)*
4. A change would move an accepted boundary or ceiling rather than select inside
   it.
5. A refuting measurement against DR1's stated basis.

Nothing else stops. Everywhere else, decide and record.

---

## 4. Codex-owned determinations

Research against the real repository and decide. For each: measure, apply the
rule, record the reasoning and what would have changed your answer.

### C1 — where the sector partition lives

DR1 fixes *what* is true; you choose *where* it is implemented — a sector key
inside `dedup_near`, grouping in `compute_view`, partitioning in
`sector_corpus`, or something the code suggests that this list doesn't.

**Rule:** choose the seam that makes store and view provably **one** rule rather
than two agreeing ones. R5 exists because no common dependency module or
manifest edge joins the two crates; if your seam creates one, say so, because
that also fires the threshold-authority deferral trigger. Prefer the seam whose
divergence is detectable by a registered rule with executable planted controls.

### C2 — how box coverage is derived

Step 2b must make an empty witness fail. Derive the expected task-id set from
the runbook's own structure — step headings are the obvious source; measure
before committing to it. H2 measures the boundary between task boxes and
closing-checklist lines.

**Rule:** derive, never declare. No per-cycle list, no minimum box count, no
exclusion list of line forms. If the structure won't support derivation, that
finding outranks convenience — record it and propose the document-shape change
that would make derivation possible.

### C3 — whether `- runbook:` qualifiers become mandatory

**Rule:** enforce only if you can measure a real collision or real
order-dependence in the tracked corpus. A prophylactic requirement with no
demonstrated failure is the same defect class this cycle exists to close.

### C4 — whether G6 gets a control this cycle

The value-domain minor rule is self-declared unenforced prose. Decide whether a
control is constructible: it would need a machine-readable statement of each
serialized `/v1/*` field's value domain, diffed across releases.

**Rule:** if constructible within this cycle's scope, build it — it is the same
defect class as G1–G3 and leaving it while fixing the others is inconsistent. If
not, say precisely what makes it not constructible and register it as a deferral
row with a trigger, not as an open comment. Do not build a partial control that
reports success on the fields it happens to cover.

### C5 — how the mirrored-block rule is enforced

R6 currently names `MODEL_PROFILE_AUTHORITY` specifically. Step 0 adds a second
marker-delimited block to the same document pair.

**Rule:** prefer generalising R6 to **derive** its marker set from the documents
— every marker-delimited authority block appears exactly once in each document
and each pair is byte-identical. That is derive-don't-assert and it makes the
third block free. Add a separate rule only if measurement shows generalisation
weakens the existing control; if so, state the weakening concretely.

### C6 — anything else E0 surfaces

Standing latitude to add rules. No latitude to add acceptance criteria that
nothing executes.

---

## 5. Dependency gates

- Everything requires **Step 0 complete**.
- Step 2 requires **E0 complete**.
- Step 3 requires **Step 2 complete**.
- Step 4 requires **E0 complete** and **C1 recorded**.
- Step 5 requires **Step 3 complete**.
- Step 6 runs **only if** Step 4 moved production Rust, under DR6.
- Step 7 requires every prior step complete or explicitly deferred with a dated
  observation.

---

## Declared scope

The standing always-allowed set remains `STATE.md`, this runbook, and
`docs/cycles/PROGRESS-v0.36.md`. The table is otherwise exact; release-authority
precedence applies only at R-CLOSE.

| Scope class | Path or value |
|---|---|
| `scope_version` | `1` |
| `disposition_intent` | `release` |
| `allow` | `AGENTS.md` |
| `allow` | `ARCHITECTURE.md` |
| `allow` | `docs/intel-platform-OPERATIONS.md` |
| `allow` | `tools/invariant_scan.py` |
| `allow` | `tools/checklist_audit.py` |
| `allow` | `config/invariant-rules.json` |
| `allow` | `config/checklist-exemptions.json` |
| `allow` | `shell/tests/**` |
| `allow` | `crates/view/src/lib.rs` |
| `allow` | `crates/store/tests/sec_identity_measure.rs` |
| `allow` | `repomix.config.json` |
| `allow` | `config/protected-artifacts.json` |
| `forbid` | `docs/state-archive/**` |
| `forbid` | `tools/model_profiles.py` |
| `forbid` | `tools/evidence_artifacts.py` |
| `forbid` | `apps/**/src/**` |
| `forbid` | `crates/store/src/**` |
| `forbid` | `crates/extract/src/**` |
| `forbid` | `crates/ingest/src/**` |
| `forbid` | `crates/core/src/**` |
| `forbid` | `crates/analyze/src/**` |
| `forbid` | `crates/compliance/src/**` |
| `forbid` | `crates/enrich/src/**` |
| `forbid` | `crates/registry/src/**` |
| `forbid` | `crates/retrieve/src/**` |
| `forbid` | `shell/intel_shell/**` |
| `forbid` | `.github/workflows/**` |
| `forbid` | `run` |
| `forbid` | `config/core.json` |
| `forbid` | `config/schedule.json` |
| `forbid` | `config/entities.json` |
| `forbid` | `config/subscriptions*.json` |
| `forbid` | `observations/**` |
| `forbid` | `fixtures/**` |
| `forbid` | `docs/cycles/**` (except this runbook and `PROGRESS-v0.36.md`, by standing precedence) |
| `release_authority` | `Cargo.toml` |
| `release_authority` | `Cargo.lock` |
| `release_authority` | `crates/*/Cargo.toml` |
| `release_authority` | `apps/*/Cargo.toml` |
| `release_authority` | `shell/intel_shell/__init__.py` |
| `release_authority` | `shell/intel_shell/app.py` |
| `release_authority` | `CHANGELOG.md` |
| `release_authority` | `README.md` |

This table was absent from the supplied runbook and was added at activation
because the v0.23-forward static scope sub-rule cannot admit an active cycle
without it. The allowed implementation paths are the minimum set implied by
Steps 0, 2, 3, 4, and activation; protected databases, observation-grade bytes,
the structural archive, live publisher paths, the workflow, and the launcher
remain forbidden. The exact `crates/view/src/lib.rs` allowance admits DR1's
sector partition while every other production Rust family remains forbidden.

---

## ACTIVATE

- Move `AGENTS.md` **Active cycle:** to `v0.36`.
- Create `docs/cycles/PROGRESS-v0.36.md` with the dated-entry skeleton.
- Commit this runbook.
- Advance the review-export retention boundary. Do **not** hand-edit the pattern
  in `repomix.config.json` — v0.35's ONE-RETENTION step made it derived from the
  Git-tracked retained-cycle set through
  `expected_review_export_retention_pattern`. Move the tracked set and let
  `cycle-check` state the derived pattern. If the derived value and the file
  disagree, that disagreement is the finding; record it before changing either.

**Acceptance.** `cycle-check` resolves v0.36 from the declaration alone;
retention derives to retain exactly v0.35–v0.36; the excluded-cycle boundary is
reported as a measurement, not asserted.

---

## Step 1 · E0 — entering-state reconstruction

Every figure below is a **hypothesis from a source-export review**. No
repository command produced any of them. Confirm or refute each against real
bytes. A refuted hypothesis is a finding to record, not an error to route
around.

| # | Hypothesis | How to settle |
|---|---|---|
| H1 | `checklist-audit` at HEAD reports `checked=268 retracted=3 entries_matched=268 commits_resolved=268`, and its v0.35 line reads `checked=0 entries_matched=0 commits_resolved=0` | run it; capture the per-runbook lines verbatim |
| H2 | v0.34 contributes 7 audited boxes from 17 `- [x]` lines; the other 10 are closing-checklist lines, not task boxes | count both classes per runbook across the full tracked set |
| H3 | The three retractions name `TASKS-v0.11-EXECUTION.md` and `TASKS-v0.12-EXECUTION.md`, tracked but excluded from the review export | `git ls-files docs/cycles` |
| H4 | The sole store↔view equivalence assertion is `sec_identity_measure.rs:353`, and both sides are empty — `(201, 0)` kept/drops, `store_drops.is_empty()` | run the test with both vectors printed before the assertion |
| H5 | No test constructs a multi-sector corpus and asserts canonical identity; the only multi-sector store test is `sector_and_id_scoped_queries_bind_and_filter_in_sql`, which tests SQL scoping | enumerate every `SectorId(` construction in test code |
| H6 | A cross-sector pair with identical text and ≥26 features yields `canonical_id` = self for both from the store, and one drop from `dedup_near` | write it as a real test; report both outputs |
| H7 | Whether any real fixture pair crosses the science↔technology boundary inside hamming 16 is **unknown** | compute the full cross-sector pairwise distance distribution over the shipped fixture corpus |
| H8 | The delivered review export measures **2,754,916 bytes / 152 files** against the recorded release-parent **2,742,486 / 152** — a delta of **+12,430 bytes at zero file-count movement** | measure the export at the release parent and at the closing commit; report both and the delta |
| H9 | Neither `9996c682…` nor `16ee7bcb…` appears in any tracked file; only `d425888…` and tree `c2ab865…` are recorded | grep the tracked corpus for all four |
| H10 | `run` is pinned at grade `authorization`, **45,409 bytes**, and `AGENTS.md` is not pinned at all | read `config/protected-artifacts.json`; confirm before Step 0d assumes it |

Additional required measurements:

- The exact object graph: release parent, its tree, closing commit, its tree,
  tag object, tag target. Confirm the closing commit's immediate parent is the
  release parent and that no remote ref matches any of them.
- `git status --porcelain`: confirm the only untracked entry is
  `docs/cycles/AMENDMENT-r4-STEP5A-NET-FLOOR-TOOLCHAIN.md`.
- Full `./run ci-local`, `invariant-scan --self-test`, shell tests, golden.
  Report counts, not adjectives.

**Acceptance.** Every hypothesis H1–H10 carries a dated verdict: confirmed,
refuted, or unmeasurable-with-stated-reason. H7's answer is reported whichever
way it comes out; it does not gate DR1.

---

## Step 2 · BOX-COVERAGE — make an empty witness fail

Two halves. Both required. The second is the one that matters.

**2a — recognise the boxes.** Extend `CHECKED_RE` to accept both the bold and
plain forms. Keep `normalize_task_id`'s `" — "` split.

**2b — make emptiness a failure.** Per C2. A runbook contributing zero
resolvable boxes must be distinguishable from a runbook with no boxes, and the
former must fail.

**Planted controls.** Register a rule in `config/invariant-rules.json` with
executable `fail_before` mutants covering at least: (i) a runbook whose boxes
are all unbolded, (ii) a runbook whose box ids match no progress entry, (iii) a
derived step with no box at all. Each fails before the fix and passes after,
anchored by control-site marker, never by a hand-typed line number.

**Acceptance.**
- The audit prints a per-runbook line for every tracked execution runbook.
- Running the fixed audit against the **unmodified** v0.35 runbook, before the
  Step 3 exemptions land, **fails**, and the failure names the real reason. A
  pass here means 2b did not work — that is the control for this step.
- `invariant-scan --self-test` passes; new totals stated.
- Zero hand-typed absolute finding-line fields survive.

---

## Step 3 · V035-DECLARE — turn a silent gap into a declared one

Per DR2 and DR3. Every v0.35 byte stays untouched.

- Append a dated correction to `PROGRESS-v0.36.md`: the v0.35 closing record's
  checklist figures are a true tool output over prior cycles only; zero v0.35
  boxes were examined; the executable link between v0.35's task boxes, progress
  entries, and commits does not exist and cannot be created without editing a
  closed cycle's dated measurement.
- Add nine exemptions to `config/checklist-exemptions.json` with the measured
  cause in each `reason` and the DR3 `accepted_by`.
- Update the file-level `record_date` and `accepted_by`, which currently assert
  something now known to be false.

**Acceptance.** `checklist-audit` finishes with **no undeclared v0.35 gap**:
nine recorded exemptions whose stated reason matches the measured cause, figure
stated. No `TASKS-v0.35-EXECUTION.md` or `PROGRESS-v0.35.md` byte moved — verify
with `git diff --stat` and report it.

---

## Step 4 · IDENTITY-SCOPE — one identity, proved

Per DR1, seam per C1.

**4a — the divergence gets a real test.** Replace the empty-witness assertion at
`sec_identity_measure.rs:353` with one that cannot pass on empty input: assert
the drop sets are equal **and** the shared set is non-empty, or build a corpus
that produces drops. An equality assertion over two empty vectors is not a
control, and leaving one anywhere in this cycle defeats the cycle.

**4b — the scope gets a registered rule.** A rule proving both layers partition
by sector, with planted controls that fail if either partition is removed.

**4c — the documents state what is true.** `AGENTS.md` and `ARCHITECTURE.md` §8
say **global within a sector**, sector axis explicit. `ARCHITECTURE.md` changes
carry architectural justification. Re-measure R1's `source` anchor against the
moved line range — the registry's ranges are positional and this is exactly the
edit that invalidates them.

**Acceptance.**
- H6 and H7 answered with printed outputs, before and after the change.
- The new rule fails before and passes after, with planted controls.
- `ci-local` clean; golden delta stated.
- The observable-output question answered explicitly: does any `/v1/*` response
  change for any configured subscription — yes or no, with the measurement, and
  for `acme-research` specifically, since that is the two-sector case. Feed the
  answer to DR5 clause 2.
- If a licensing or entitlement outcome moves, **stop** under §3.

---

## Step 5 · AUDIT-CHILD — discharge the v0.35 Step 7 field

The missing field is `- cycle-ending review-export audit: closing_tree=…;
bytes=…; audit_delta=…`.

It requires **no push**. All three values are local, and Step 0a settles the
reading that made this look otherwise. The v0.33 and v0.34 audit children were
local commits made immediately after their closing commits and delivered as the
next cycle's entering ref. The v0.35 deferral to "the first post-push append"
was not forced by the authorisation boundary; the criterion was satisfiable
inside the cycle. **This runbook has checked whether that criterion had a
satisfying assignment and finds that it did.** Record it as an execution gap,
not as an author-side unsatisfiable rule.

Under DR2 the audit child is a **v0.36 commit** whose field measures v0.35's
existing closing tree, dated to the day it was measured and marked plainly as a
v0.36 append discharging a v0.35 criterion.

**Acceptance.** The field exists in the exact required form; all three values
measured; none copied from a checker's own output where the construction can
produce it independently; `audit_delta` reported against H8's numbers with any
discrepancy explained rather than absorbed.

---

## Step 6 · RE-MEASURE — hosted, conditional

Runs **only if** Step 4 moved production Rust. Push per DR6 — no further
authorisation.

Nine blocking job identities at the exact candidate commit; the pinned
release-grade verifier accepts every signed bundle; receipts bind the declared
effective toolchains. Report the run id, attempt number, the ref, the
`ls-remote` pre-check result, and the identity count.

If it does not run, record the dated reason and state which claims therefore
rest on local execution only.

---

## Step 7 · R-CLOSE

Two-commit tagged close: untagged release parent → separate closing commit
carrying the record → annotated tag over the closing commit → append-only audit
child.

Disposition per **DR5**. Apply the rule, record the reasoning, do not ask.

**Acceptance criteria.**
- Dated disposition with the structural reason — the measured content of the
  unpublished distance, not "nothing shipped".
- DR5 clause 2 answered in writing with its measurement.
- `version-check` passes with every authority and restatement count stated.
- **`checklist-audit` passes with all four figures stated, and its v0.36 line
  shows a non-zero checked count.** A v0.36 line reading `checked=0` fails this
  step outright — that is the property Step 2 built, applied to its own cycle.
- The governed export row bound to the last governed field visible in the
  closing tree, and the audit child carrying `- cycle-ending review-export
  audit: closing_tree=…; bytes=…; audit_delta=…`. **Required in this cycle
  before Step 7 is checked**; it is local, needs no authorisation, and there is
  no satisfying assignment in which it defers out of the cycle.
- Both artifact boundaries measured with remaining cycles; nearest named.
- Every deferral row carries a dated v0.36 observation.
- `invariant-scan --self-test` passes; totals stated; zero hand-typed absolute
  finding-line fields.
- Golden 11/11 embedded and standalone; delta stated.
- Publication of `main` and any tag remains the retained gate (§3) and is not
  performed.

---

## Governed artifact byte-boundary authority

- governed artifact byte boundary: path=`STATE.md`; bytes=`453741`
- governed artifact byte boundary: path=`config/protected-artifacts.json`; bytes=`1048576`

**Carried forward byte-identically.** A change to either figure is an
architectural change requiring its own justification and operator
authorization. The 3,000,000-byte review-export ceiling remains separately
governed.

---

## Deferred means deferred

Each row keeps its original trigger. A v0.36 observation records that the
trigger has **not** fired; it does not weaken, restate, or re-scope it.

| Deferred item | Unchanged trigger | Measured observation (cycle-identified) | v0.36 action |
|---|---|---|---|
| T7 robots single-flight | a second concurrent harvester | *record dated observation* | none |
| NEGATIVE-CACHE Decision B | a live transient robots outage for an admitted publisher while a usable last-known-good policy exists, plus operator authorization | *record dated observation* | none |
| Conditional GET (`ETag` / `If-Modified-Since`) | an operator-authorized cycle whose scope permits the `net` request path plus a live 304 observation | *record dated observation* | none |
| `edgar:*` extension field mapping | an operator-authorized cycle permitting `crates/ingest/src/**` for mapping, with a connector review | *record dated observation* | none |
| Live multi-publisher behaviour in one runtime | further origins beyond the two configured, or concurrency | *record dated observation* | none |
| First recurring scheduled SEC run | explicit operator authorization of a bounded scheduled window, separate from any cycle scope | *record dated observation* | none |
| Postgres / pgvector / multi-host seam | unchanged | *record dated observation* | none |
| A4 untrusted-shell boundary | a third-party/untrusted shell, or any claim HC1 is invariant under shell replacement | *record dated observation* | none |
| L2 forced-command wrapper | an operator server session | *record dated observation* | none |
| R3/R4 open-bottom coverage | a spelling outside registered vocabulary | *record dated observation* | none |
| `--features net` Rust 1.86 execution | a scoped cycle authorized to change evidence topology and an executable local or hosted lane that actually pins and runs the net path on Rust 1.86 | *record dated observation* | none |
| GitHub attestation verifier version admission | the installed or proposed `gh attestation verify` version differs from the exact repository pin, or its accepted bundle/workflow contract changes | *record dated observation* | none |
| Third configured publisher | a completed compliance review, then a separate admission decision | *record dated observation* | none |
| `v0.8.0` / `v0.10.2` publication | operator-authorized push of both exact annotated objects | *record dated observation* | none |
| `--skip-local-tag-verification` removal | both historical tags published plus a passing hosted full-history `cycle-check` without the flag | *record dated observation* | none |
| Manifest retention/indexing | the manifest reaches its governed artifact byte boundary, or two consecutive clean `./run verify-artifacts` runs each take ≥1.00 s real | *record dated observation* | none |
| Version literal in `app.py` | a cycle whose declared scope permits shell source changes | *record dated observation* | none |
| Release-classification criteria with no executed control | an operator decision that prose adjudication is insufficient | *record dated observation* | none |
| Second `STATE.md` archival | the export ceiling trigger fires, or `STATE.md` reaches its governed artifact byte boundary | *record dated observation* | none |
| Retention derivation across a version-family boundary | an active cycle whose name is not of the form `v0.<n>` — raising at `v1.0`–`v1.2`, silently under-excluding from `v1.3` onward | *record dated observation* | none |
| Published-release divergence | the unpublished distance contains a measured runtime behaviour difference persisting across three consecutive closed cycles within the current publication epoch, or acquires any public-surface change | *record dated observation* | none |
| MSRV current-restatement membership | a current restatement of either Rust floor lands outside the registry without failing a check | *record dated observation* | none |
| Retention arithmetic fallback | the retention formatter again permits an omitted retained set, or any live production or fixture caller supplies a set not derived by `expected_retained_cycle_paths` for that root | *record dated observation* | none |
| Optional cycle-ending audit disclosure | a closed cycle whose delivered export differs from its governed figure and which records no cycle-ending audit field | *record dated observation* | **Step 5 and Step 7** |
| SEC EDGAR admission | the three v0.25 determinations closed: license enum semantics, terms-level automated-access gate, feed shape | *record dated observation* | none |
| License enum semantics | a second publisher requires a license value the current enum cannot express | *record dated observation* | none |
| Terms-level automated-access gate | a candidate publisher's terms restrict automated access beyond robots.txt | *record dated observation* | none |
| Feed shape observation | a publisher feed shape not covered by a captured observation | *record dated observation* | none |
| Threshold-authority limitation | a common dependency module or manifest edge appears between store and view | *C1's seam may fire this — record a dated observation* | **Step 4** |
| ARCHITECTURE.md §8 / AGENTS.md R-CLOSE tag-mechanics duplication | the two restatements diverge | *record dated observation* | none |
| Review-export capacity | the governed export crosses its declared ceiling | *record dated headroom in bytes, %, and cycles* | **Step 7** |
| Public value-domain control (G6) | a `/v1/*` field's value domain changes with no control to detect it | *record C4's dated decision and its basis* | **Step 7 if C4 defers** |

---

## Standing prohibitions

- No closed-cycle document, observation, or fixture edited. Under DR2 this
  includes every v0.35 byte, without exception.
- No dated historical measurement edited. Corrections are forward and dated.
- No push except DR6's evidence ref. No `main` push, no tag publication, no
  other remote ref mutation.
- No expectation, anchor, or figure copied from a checker's own output where the
  construction can produce it independently.
- No acceptance criterion phrased as a repo-wide absence discharged by
  inspection; it needs a registered self-testing `invariant-scan` rule with an
  executable `fail_before`.
- No hardcoded scope list where the scope can be derived.
- **No acceptance discharged by an executable whose witness set is empty.** If a
  comparison, a count, or a match set can be empty, the emptiness itself must
  fail.
- No retraction added (DR4).
- The Step 0b ask-first list is not widened by convenience, and the autonomy
  block is never read as permission to proceed past a tripped gate.
- The untracked amendment file stays untouched.

---

## Cycle checklist

- [ ] **AUTONOMY** — authority block installed, mirrored, and mechanically enforced
- [x] **ACTIVATE** — declaration at v0.36, progress skeleton, retention derived
- [ ] **E0** — H1–H10 settled with dated verdicts
- [ ] **BOX-COVERAGE** — both halves; the unfixed v0.35 runbook now fails
- [ ] **V035-DECLARE** — nine exemptions with measured causes; zero v0.35 bytes moved
- [ ] **IDENTITY-SCOPE** — divergence measured, both layers partitioned, rule registered
- [ ] **AUDIT-CHILD** — v0.35 Step 7 field discharged
- [ ] **RE-MEASURE** — conditional; run id and identity count, or dated reason
- [ ] **R-CLOSE** — closing record, audit child, non-zero v0.36 checked count

*Box ids match the `PROGRESS-v0.36.md` entry ids exactly. That is the property
Step 2 makes executable; this runbook is its first subject.*

---

## Handoff

One report at the end, not a stream of questions. Include: each §2 decision and
whether any measurement refuted its basis; each C-determination with its
reasoning and falsifier; every stop-and-report condition triggered, or an
explicit statement that none were; and a **gaps-and-findings list for v0.37** —
what you measured that this runbook did not anticipate, stated as findings, not
as proposed acceptance criteria.

That last distinction is deliberate and is the reason runbook authorship stays
outside this loop. A system that writes its own acceptance criteria and then
grades itself against them has no independent witness, which is the exact defect
family this cycle exists to close. Report what you found; the criteria come from
review.

Then: the standing publication request for v0.17.2 and v0.36's release, which
remains the operator's to grant.

---

## Provenance

**What I read.** `AGENTS.md`, `ARCHITECTURE.md`, `STATE.md`,
`repomix.config.json`, `config/invariant-rules.json`,
`config/checklist-retractions.json`, `config/checklist-exemptions.json`,
`config/protected-artifacts.json`, `config/core.json`, `config/schedule.json`,
`config/subscriptions.json`, `tools/checklist_audit.py`,
`tools/cycle_identity.py`, `tools/progress_check.py`, `tools/cycle_check.py`
(retention paths), `run` (dispatch and `ci-local` table),
`crates/store/src/sqlite.rs`, `crates/store/tests/sec_identity_measure.rs`,
`crates/extract/src/lib.rs`, `crates/view/src/lib.rs`, `apps/cored/src/main.rs`
(view path), `docs/cycles/TASKS-v0.34-EXECUTION.md`,
`docs/cycles/PROGRESS-v0.34.md`, `docs/cycles/TASKS-v0.35-EXECUTION.md`,
`docs/cycles/PROGRESS-v0.35.md`.

**What I measured, on the delivered review export only.**

1. Export composition: **2,754,916 bytes / 152 files**; `Cargo.lock` present;
   `docs/state-archive/**` absent; excluded-cycle pattern `3[0-3]`, retaining
   exactly the v0.34 and v0.35 pairs. The v0.11 and v0.12 runbooks named by the
   retraction registry are outside the **export**, not the repository.
2. Checkbox regex applied directly: v0.34 → **7** of **17** `- [x]` lines;
   v0.35 → **0** of **9**.
3. `PROGRESS-v0.35.md`: **16** dated entries, **16** `- commit:` fields, **0**
   `- runbook:` fields; entry ids bare (`E0`, `ANCHOR`) against box ids carrying
   step ordinals (`Step 1 · E0`).
4. Zero occurrences of `cycle-ending review-export audit` in
   `PROGRESS-v0.35.md`; one in `PROGRESS-v0.34.md` at its audit child, carrying
   `closing_tree`, `bytes=2552372`, `audit_delta=+25192`.
5. `assign_canonical_ids_tx` selects `ORDER BY sector, published_day, id` and
   executes `kept.clear()` on each sector change, with a comment declaring the
   scoping deliberate; `dedup_near` sorts `(published_day, id)` with no sector
   axis; the sole equality assertion between them runs on a `finance`-filtered
   corpus producing `(201 kept, 0 drops)` and an empty `store_drops`.
6. `compute_view_resp` passes `sector_corpus(st, sectors)` — the full requested
   sector set — to `compute_view` in one batch; `config/subscriptions.json`
   entitles `acme-research` to `["science", "technology"]`.
7. Source license classes: science/`arxiv-cs` = `IndexOnly`;
   technology/`techwire` = `CcBy`, technology/`osdaily` = `IndexOnly`;
   finance/`filings-digest` = `PublicDomain`, finance/`sec-edgar-usgaap` =
   `PublisherPermitted`. A science↔technology collapse can cross a license
   class.
8. Registry population **12 rules / 73 controls**, by rule. R7 already governs
   sector-scoped hydration; R6 enforces one byte-identical marker-delimited
   block pair and names `MODEL_PROFILE_AUTHORITY` explicitly.
9. `progress-check` validates only the newest entry's shape and has no linkage
   to runbook boxes, so `checklist-audit` is the sole executable link.
10. `9996c682…` and `16ee7bcb…` appear in **zero** tracked files;
    `d425888…` and `c2ab865…` appear in `STATE.md`, `ARCHITECTURE.md`, and
    `PROGRESS-v0.35.md`. `PROGRESS-v0.35.md:1047` carries the dated `268` figure
    describing the tree it sits in — the measurement that makes DR2 what it is.
11. `config/protected-artifacts.json`: `run` and `tools/model_profiles.py`
    pinned at grade `authorization`; observation-grade and structural-archive
    bytes pinned separately; **`AGENTS.md` is not pinned**, so Step 0 needs no
    pin change for it. Lifecycle policy is
    `append_only_chained_records_with_wire_evidence_and_operator_approval` for
    publisher admission.
12. `run` contains no interactive prompt, and `tools/cycle_check.py` contains
    zero occurrences of "operator" — no tooling gate blocks autonomous
    execution. The gating is entirely in prose, which is why Step 0 edits prose.
13. `AGENTS.md` §8 already establishes the marker-delimited standing-authorization
    pattern, mirrored byte-identically and enforced by R6. Step 0 reuses it
    rather than inventing a mechanism.

**What I did not do.** I ran no repository command, no test, no checker, and no
Git operation. I did not execute the cross-sector reproduction the v0.35
self-review reports executing; G1 rests on reading both implementations and the
one control that compares them. Every figure above is a hypothesis for E0 to
confirm or refute against real repository bytes. The export byte count is the
count of the file delivered to me and may not equal the governed export at any
particular tree; H8 exists because I cannot settle that from the export alone.
