# TASKS-v0.15-EXECUTION.md — derived-scope runbook for Codex

v0.15 has one theme: **scope that is asserted becomes scope that is derived.**

v0.12 registered absence claims as rules. v0.13 made those rules provably able to
fire. v0.14 made each control prove *where* it fired, and audited the rules for
overclaiming. Across all three cycles the recurring defect was never a wrong
rule — it was a **hand-maintained list deciding what gets checked**:

- `cargo test -p cored --features net` existed in no job, so two tests compiled
  and never ran;
- `range(1, 10)` decided which rules pytest exercised, so an eleventh rule would
  have gone unguarded;
- a deferral row declared a requirement that no step discharged.

Each was fixed individually. The class was not. Three lists still decide scope
by hand, and nothing checks any of them against the thing they describe:

- **the local and hosted check sets have no correspondence check at all** —
  `run` holds 20 `ci_local_job` invocations and `.github/workflows/ci.yml` holds
  seven blocking jobs, and nothing asserts that a check in one exists in the
  other;
- **`EXPECTED_RUNNER_JOB_IDENTITIES`** (`tools/audit_deferred.py:55-65`) is a
  hardcoded frozenset of seven identities, never derived from `ci.yml`;
- **the four injectable `/view` stage names** are declared in Rust
  (`apps/cored/src/main.rs:558, 982, 987, 992`) and independently re-declared in
  Python (`tools/benchmark_view.py:54-57`), across a language boundary.

This cycle does four things and deliberately no more:

1. **registers local/hosted check parity as R10**, so a check that exists in one
   place and not the other fails CI;
2. **derives the expected hosted identity set from `ci.yml`** instead of
   restating it;
3. **gives the `/view` stage names one source**;
4. **records two review-discipline rules** that v0.14 paid for, one of them
   executable.

It ships no new ingestion source and no subscriber-facing surface. **The public
`/v1/*` JSON bodies, the SQLite schema, and the golden regression's 11
invariants are unchanged. Golden stays 11/11 byte-identical through every task.**

**Version disposition — decided at Step 4, not inherited here.** Default is a
patch release **`v0.14.1`**, because Steps 2, 3, 5, and 6 touch only harness,
tooling, and documentation. **`v0.15.0`** applies if and only if Step 4 changes
an observable name — a `x-intel-view-stage-*` header, a stage string, or any
public surface. Record the fired trigger in Step 4.

---

## Entering state (asserted, not yet verified)

**Every sentence here is a hypothesis until Step 1 (E0) measures it.**

- `v0.14.0` is published: annotated tag object
  `dddc1a52d28a1832727a8d8eb5e87fc7168511c6` dereferences to release commit
  `4ad4c8d71075731dd87c360e8b0d3d91d80b5518`. `origin/main` is
  `a75c9cf5defa42e985811b01f9905b6ac99797fd`, ahead of the release commit by the
  closing-audit, supersession, and publication-record commits. Release evidence
  is dispatch run **30324186389** against candidate `ee9ee0f9…`.
  **None of this is reopened.**
- `./run ci-local` **20/20**; Rust **125 workspace / 48 net** (23 `intel-ingest`
  + 25 `cored`); shell **225/225** local and **224 passed / 1 skipped** hosted on
  each interpreter; `invariant-scan` **9 rules / 15 controls**; golden **11/11**;
  pins **101**; protected databases **2/2**; `checklist-audit` **121** checked
  with **3** retractions; `cycle-check` reports `v0.14`, state `closed`.
- The hosted skip is `test_on_site_production_measurements_match_committed_receipt`
  (`shell/tests/test_deferred_audit.py:1192-1199`), which skips when the
  protected corpora and a built `cored` are absent. **This is intended and is
  not a finding.** Do not re-raise it.
- `A4`, the **editable-L1 controller residual**, and the **stated R3/R4
  open-bottom limitations** (`ARCHITECTURE.md:217-222`) all remain open. **L2**
  remains scheduled and is not executed in this cycle.
- **`ci-local` enters at 20 jobs and exits at 20.** R10 runs inside the existing
  `registered static invariants` job.

### Gaps this runbook is drafted against (verify, do not trust)

| # | Location | Claim to verify |
|---|---|---|
| **H1** [P1] | `run` (20 `ci_local_job` calls); `.github/workflows/ci.yml` has six blocking jobs (`core:51`, `lint:139`, `net:205`, `msrv:296`, `shell:362`, `golden:472`) and one report-only job (`drift:540`, excluded by job-level `continue-on-error: true`); the shell matrix makes seven blocking identities | **Nothing asserts local and hosted check parity.** A check may exist in `ci-local` and not hosted, or the reverse, and no tool reports it. This is the un-fixed class behind NET-TEST-EXEC, where a cargo invocation was absent from both. |
| **H2** [P2] | `tools/audit_deferred.py:55-65` | **`EXPECTED_RUNNER_JOB_IDENTITIES` is hardcoded**, never derived from `ci.yml`. Adding a blocking job without editing the constant fails loudly (safe direction); **removing one from both silently narrows coverage** (unsafe direction). The correspondence is unasserted either way. |
| **H3** [P2] | `apps/cored/src/main.rs:558, 982, 987, 992`; `tools/benchmark_view.py:41-59` | **The four injectable stage names are declared twice across a language boundary.** Note precisely: `benchmark_view.py`'s 11-key map is a **superset** — seven entries are header-only and have no `diagnostic_delay` call site: `process_main_to_listener_ready`, `store_open`, `store_connection`, `store_schema_fts`, `store_cursor_migration`, `store_fingerprint_backfill`, and `handler_total`. The claim is about the four injectable names, not the whole map. Renaming one in Rust leaves Python asking for a stage that no longer exists. |
| **H4** [P2] | v0.14 review record in `PROGRESS-v0.14.md` | **An acceptance criterion that cites a step's measured value goes stale** when a later step changes the quantity. v0.14's Step 8 required hosted counts to "match Step 2's recorded values" while Steps 4–5 deliberately raised them. This is the sibling of the deferral-row gap `TEMPLATE-REMEASURE` closed. |
| **H5** [P3] | `AGENTS.md`; v0.14 review record | **Two review-discipline lessons are recorded but not binding.** (a) A claim about what a command does is verified at the command's **entry point**, not its caller — v0.14's false self-test finding came from reading `run`'s wrapper and not `invariant_scan.py`'s `main()`. (b) A closing record should state a disposition **as of a date**, so a later authorization supersedes rather than contradicts it. |

---

## How to run this file

Execute top to bottom, one task and one commit at a time. Follow `AGENTS.md §5`
after **every** task. Implementation and audit-record commits stay separate. Do
not batch status updates.

- **🤖 = Codex executes and self-verifies end to end** — no live model endpoint,
  no live server session, no publication, no push.
- **🧑 = exactly one named operator action or decision.**

**Dependency gates.** Step 3 is blocked by Step 2, because deriving the identity
set should reuse the `ci.yml` parser Step 2 builds rather than write a second
one. Step 7 is blocked by every preceding implementation step. Step 8 is blocked
by Step 7. Steps 4, 5, and 6 are independent and may run in any order after
Step 1.

### Cycle activation (before E0)

In a separate preparatory implementation/audit pair: confirm the worktree is
clean and `origin/main` is `a75c9cf5…`; commit **only** this runbook, the
`AGENTS.md` header declaring v0.15 active, and a new `PROGRESS-v0.15.md`; run
`cycle-check` and `checklist-audit`. **Do not claim E0's acceptance from this
commit.**

### Session opener

```bash
git status --porcelain=v1
git describe --tags --always --dirty
git rev-parse HEAD
git rev-list --left-right --count origin/main...HEAD
git tag --list 'v0.14*' --format='%(refname:short) %(objectname) %(*objectname)'
sed -n '1,20p' AGENTS.md
sed -n '1,6p' STATE.md
```

### Global definition of done

Protected hashes exact; all **101** pins match until Step 7 adds more; golden
**11/11 byte-identical**; `./run version-check` green; zero rustc warnings on
offline and net builds; all Rust tests green; all shell tests green under Python
3.11 **and** 3.12; clippy, fmt, ShellCheck, floor byte-compilation, and locked
Rust 1.78 green. No mock, fixture, double, health response, hand-authored
receipt, or workflow configuration is promoted to wire evidence.

`invariant-scan` enters at **9 rules / 15 controls** and exits at **10 rules**,
with the control count measured and recorded by Step 2 rather than predicted
here. **State counts as measured relations, never as predictions inherited from
an earlier step** — that is H4, and this runbook is bound by it.

---

## Deferred means deferred

| Deferred item | Unchanged trigger | v0.15 action before the trigger |
|---|---|---|
| T7 robots single-flight | a second concurrent harvester | none |
| Postgres | a second archive writer | none |
| pgvector | exact cosine stops fitting the measured request budget | none |
| Multi-host seam hardening | an actual core/shell host split | none |
| A4 untrusted-shell boundary | a third-party/untrusted shell, or any claim HC1 is invariant under shell replacement | none |
| L2 forced-command wrapper | an operator server session | none — remains scheduled, not executed |
| R3/R4 open-bottom coverage | a provider or credential spelling outside registered vocabulary | none — the stated limitations stand and are not narrowed |
| CI-runner evidence | an authenticated receipt set with identified matrix legs, durably committed | **re-measure at the new release commit — discharged by Step 7** |

---

## Step 1 · E0 — Rebuild the entering state and confirm H1–H5 🤖

**Objective.** Reproduce the post-v0.14.0 state from commands, and confirm or
refute every gap against HEAD before changing anything.

**Gate.** Read-only measurements in the repository and mutations confined to
disposable scratch worktrees. Permanent changes are limited to this active
runbook's E0 gate/checklist record and `STATE.md`; no source, workflow,
configuration, protected artifact, or historical record changes.

**Steps.**

1. Run the full entering matrix: `./run ci-local`, standalone `./run golden`,
   `./run verify-artifacts`, `./run cycle-check`, `./run checklist-audit`,
   `./run progress-check`, `./run version-check`, `./run invariant-scan`.
2. **Reproduce H1 mechanically.** In a scratch worktree (`git worktree add`),
   delete one cargo invocation from a hosted job in `ci.yml` and confirm every
   existing tool still reports green. Then do the reverse: delete one
   `ci_local_job` line from `run` and confirm the same. Capture both.
3. **Reproduce H2**: add an eighth blocking job to `ci.yml` in a scratch
   worktree and record what fails; then remove a job from both `ci.yml` and the
   constant and record that nothing does.
4. **Reproduce H3**: rename one stage string in `main.rs` and record whether any
   test, rule, or tool reports the Python side is now stale.
5. Confirm H4 by reading v0.14's Step 8 criterion and its amendment, and H5 by
   reading `AGENTS.md` for the two absent rules.
6. Record which of H1–H5 refute. A refuted row is a finding.

**Acceptance criteria.** Entering matrix captured in full · H1 reproduced in
both directions as command output · H2 reproduced in both directions · H3
reproduced · H4/H5 dispositions recorded · published `v0.14.0` tag, commit, and
all 101 pins unchanged and re-verified · golden 11/11.

**Done when** every gap this runbook acts on has been confirmed or refuted by
execution.

---

## Step 2 · R10-CI-PARITY (H1) — Local and hosted check sets must correspond 🤖

**Objective.** Make a check that exists in one place and not the other fail CI.

**Gate.** `tools/invariant_scan.py`, `config/invariant-rules.json`,
`shell/tests/test_invariant_scan.py`, `ARCHITECTURE.md`, this active runbook's
gate/amendment/checklist record, and `.github/workflows/ci.yml` only for
required hosted counterparts. `run` may change only if a machine-readable
correspondence marker is required. **No source under `crates/` or `apps/`
changes.**

**Steps.**

1. Decide and record the correspondence mechanism before implementing. Options:
   parse both files and match on normalized command text; or introduce an
   explicit shared manifest that both consume. **Prefer parsing what already
   exists over adding a third list** — a manifest that itself needs maintaining
   reproduces the defect one level up. If a marker is unavoidable, say plainly
   in `PROGRESS-v0.15.md` why parsing was insufficient.
2. Register **R10**: every check invoked by `run`'s `ci-local` has a hosted
   counterpart in `ci.yml`, and every blocking hosted step has a local
   counterpart. Report both directions with file, line, and the unmatched
   command.
3. **Record deliberate exemptions explicitly**, not silently. Steps legitimately
   hosted-only (artifact upload, attestation, receipt emission) or
   legitimately local-only belong in a declared exemption list with a stated
   reason, and R10 must report the exemption count so it cannot grow unnoticed.
4. Cite the `ARCHITECTURE.md` sentence stating the parity property as `source`.
   If none exists, **add it first** — a rule with no prose to cite is a check
   without a claim.
5. Provide site-specific controls per the v0.14 schema: remove a local check;
   remove a hosted check; add an unexempted hosted-only step. All must FAIL
   naming the file and line.
6. Measure and record the resulting rule and control counts. **Do not predict
   them anywhere in this file.**

**Acceptance criteria.** R10 registered with at least three site-specific
controls, all demonstrated FAIL · R10 PASSes on HEAD · exemptions declared with
reasons and counted in the report · `--self-test` green across all rules ·
`ci-local` still **20** · measured rule/control counts recorded in `STATE.md`
and `PROGRESS-v0.15.md` · golden 11/11.

**Done when** deleting a cargo invocation from either side turns CI red.

---

## Step 3 · IDENTITY-DERIVE (H2) 🤖

**Objective.** Derive the expected hosted identity set from `ci.yml` instead of
restating it.

**Gate.** `tools/audit_deferred.py`, `shell/tests/test_deferred_audit.py`.
Reuse Step 2's parser; do not write a second one.

**Steps.**

1. Replace `EXPECTED_RUNNER_JOB_IDENTITIES` with a value derived from `ci.yml`'s
   blocking jobs and their matrix legs, excluding report-only jobs by an
   explicit, stated criterion rather than by name.
2. Preserve `LEGACY_RUNNER_JOB_COUNTS` behavior for already-pinned historical
   receipt sets. **Previously admitted evidence must continue to validate
   unchanged** — if derivation would invalidate a pinned set, that is a finding
   to report before proceeding, not a reason to re-pin.
3. Add tests: a job added to `ci.yml` appears in the derived set without editing
   Python; a report-only job stays excluded; a removed job narrows the set and
   the narrowing is **reported**, not silent.
4. Re-run `./run verify-artifacts` and confirm all 101 pins still validate.

**Acceptance criteria.** Identity set derived from `ci.yml` · report-only
exclusion stated as a criterion, not a name list · all three tests green on both
interpreters · **all 101 pins validate unchanged** · a silent narrowing is now
impossible, demonstrated · golden 11/11.

**Done when** adding or removing a hosted job needs no Python edit and cannot
narrow coverage unnoticed.

---

## Step 4 · STAGE-SOURCE (H3) 🧑🤖

**Objective.** Give the four injectable `/view` stage names one source.

**Gate.** `apps/cored/src/main.rs`, `tools/benchmark_view.py`,
`shell/tests/test_benchmark_view.py`, this active runbook's operator decision,
authorized H1/H3/Step 7 corrections, gate/amendment/checklist record, and — if
a generated or exported list is chosen — its output path. **🧑 One operator
decision: whether any observable name changes, which sets the version.**

**Operator decision and scope — 2026-07-28.** No observable name changes:
the `x-intel-view-stage-*` header set and all stage strings remain identical to
v0.14.0, so the **v0.14.1** trigger fires. The scoped set is derived only from
the four `diagnostic_delay("…")` call sites; the seven header-only map entries
remain outside the assertion and untouched. Current control flow confirms that
`sector_load`, `analysis`, and `response_build` are injectable only on a cache
miss because a hit returns before `compute_view_resp`; `serialization` remains
injectable on both paths because `into_response` runs after either result.

**Mechanism decision.** A Python test reads both source files, derives the Rust
call-site set, and asserts it is a subset of `DIAGNOSTIC_HEADERS`. This avoids a
build/export step and lets `benchmark_view.py` remain independently runnable.
Equality is deliberately not asserted because it would fold the seven
header-only measurements into the injectable scope.

**Steps.**

1. **State the scope precisely before implementing.** Only the four names with
   `diagnostic_delay` call sites are in scope. `benchmark_view.py`'s map is a
   superset containing header-only entries; those are not part of this task and
   must not be quietly folded in.
2. Choose and record the mechanism: export the names from Rust for Python to
   consume, or assert correspondence in a test that reads both files. **Prefer
   the assertion if exporting requires a build step**, since `benchmark_view.py`
   must remain runnable without one.
3. Implement it so that renaming a stage in Rust without updating Python fails a
   test naming both files.
4. **Record the version trigger here.** If no observable name changes ⇒
   `v0.14.1`. If any `x-intel-view-stage-*` header or stage string changes ⇒
   `v0.15.0`. State which fired and why.

**Acceptance criteria.** Scope limited to the four injectable names, stated
explicitly · mechanism recorded with reasoning · a Rust-side rename fails a test
naming both files, demonstrated · header-only entries untouched · version
trigger recorded in this step · golden 11/11.

**Done when** the stage list cannot diverge across the language boundary
unnoticed.

---

## Step 5 · CRITERION-SHAPE (H4) 🤖

**Objective.** Make an acceptance criterion that cites a step's measured value a
detectable error.

**Gate.** `tools/cycle_check.py` (or whichever tool owns runbook structure),
its tests, `ARCHITECTURE.md` for the required limitation, and this active
runbook's gate/amendment/checklist record. **No closed runbook is edited.**

**Steps.**

1. Extend the runbook checker to reject an **active** runbook whose acceptance
   criteria reference another step's recorded or measured quantity — the pattern
   v0.14's Step 8 used. Match on the relation, not on one phrasing: a criterion
   may cite an invariant relation ("hosted equals local at the same commit") but
   not a step's stored number.
2. **Accept that this check is heuristic and say so.** Register its limitation
   in `ARCHITECTURE.md` in the same plain language as the R3/R4 open-bottom
   entries. **A stated limitation is a property; an implied one is not.**
3. Provide a fail-before: a scratch runbook with a step-value criterion fails;
   this runbook passes.
4. Do not retroactively fail closed runbooks. v0.14's record stands as the
   originating evidence.

**Acceptance criteria.** Checker rejects a step-value criterion, demonstrated ·
this runbook passes · limitation stated in `ARCHITECTURE.md` · closed runbooks
unmodified · shell tests green on both interpreters · golden 11/11.

**Done when** the defect that cost v0.14 a wasted dispatch cannot be written
into an active runbook silently.

---

## Step 6 · REVIEW-DISCIPLINE (H5) 🤖

**Objective.** Make two lessons v0.14 paid for binding rather than remembered.

**Gate.** `AGENTS.md`, `tools/cycle_check.py`, and its tests.

**Steps.**

1. Add to `AGENTS.md`, beside the existing evidence rules: **a claim about what
   a command does is verified at the command's entry point, not its caller.**
   Cite v0.14 as the originating evidence — a false finding produced by reading
   `run`'s wrapper instead of `invariant_scan.py`'s `main()`, and its mirror in
   v0.13, where the tool was read and the wrapper was not.
2. Add: **a closing record states its disposition as of a date**, so a later
   authorization supersedes rather than contradicts it.
3. Make (2) executable: `cycle-check` requires a closed cycle's disposition
   field to carry a date. Provide a fail-before with an undated disposition.
4. (1) is a discipline rule for humans and agents and is **not** made executable.
   Say so explicitly rather than leaving its status ambiguous.

**Acceptance criteria.** Both rules present in `AGENTS.md` with v0.14 cited ·
undated disposition fails `cycle-check`, demonstrated · the non-executable
status of rule (1) stated explicitly · closed runbooks unmodified · golden
11/11.

**Done when** the two lessons are enforced or explicitly marked unenforceable.

---

## Step 7 · RE-MEASURE 🤖🧑

**Objective.** Produce release-grade hosted evidence for the v0.15 candidate.

**Gate.** 🧑 **One narrow authorization: a non-`main` branch push.** No tag, no
`main` advance, no publication.

**Steps.**

1. Push the candidate to `candidate/v0.14.1`. Record branch and commit.
2. **Read the remote branch's `ci.yml` and confirm it contains every invocation
   you expect before dispatching.**
3. Dispatch on that branch with `publish_evidence: true` and `audit_sha` set to
   the candidate.
4. **Read every count out of the hosted log**, not from job status: workspace,
   both net legs, both shell legs, the invariant rule and control counts, and
   golden. Compare each against the local measurement **at the same commit** —
   that equality is the criterion, not any number written earlier in this file.
5. Commit the signed receipt/bundle set, re-run `./run verify-artifacts` and
   `./run evidence-report`, and record the new pin count in `STATE.md`,
   `PROGRESS-v0.15.md`, and the pending closing record.
6. Confirm the hosted identity set matches Step 3's **derived** value.
7. Run `./run audit-deferred` in release posture with attestations required.

**Acceptance criteria.** Hosted run id pinned to the candidate · every count read
from the log and equal to the local measurement at that commit · identity set
matches the derived value · signed set committed and re-derived · new pin count
in three places · `origin/main` unchanged, no tag · golden 11/11.

**Done when** v0.15's hosted evidence exists at the same grade as v0.14's.

---

## Step 8 · R-CLOSE 🧑🤖

**Objective.** Close the cycle with a measured record.

**Gate.** Steps 1–7 complete and boxed. Worktree clean. **🧑 One operator
decision: publication.**

**Steps.**

1. Re-run the complete definition of done at the release commit and capture it.
2. Record the version choice, citing the trigger **fired in Step 4**.
3. Record evidence candidate and release commit as **separate named fields**.
4. **State the release disposition as of a date**, per Step 6.
5. Classify every diff path exactly once in `STATE.md`; update `CHANGELOG.md`,
   `README.md`, and the release authorities.
6. Reconcile `ARCHITECTURE.md`. **A4, the L1 controller residual, the R3/R4
   open-bottom limitations, and Step 5's stated heuristic limitation must all
   read as open.**
7. Check R-CLOSE's box and replace the pending heading with the canonical
   `Cycle closed:` record **in one commit**.
8. State the publication disposition as a decision with a trigger.

**Acceptance criteria.** Version cites Step 4's trigger · evidence candidate and
release commit separate · disposition dated · every diff path classified ·
`ARCHITECTURE.md` matches enforced reality · all four open items recorded as
open · `invariant-scan` 10 rules green · all pins match · golden 11/11.

**Done when** v0.15's disposition is a recorded, measured, dated decision.

---

## Cycle checklist

- [x] **E0** — entering matrix captured; H1 reproduced in both directions; H2
  reproduced in both directions; H3 reproduced; H4/H5 recorded
- [x] **R10-CI-PARITY** — registered with ≥3 site-specific controls, all FAIL;
  exemptions declared with reasons and counted; mechanism recorded; measured
  counts recorded
- [x] **IDENTITY-DERIVE** — identity set derived from `ci.yml`; report-only
  exclusion is a criterion not a name list; all 101 pins validate unchanged;
  silent narrowing impossible
- [x] **STAGE-SOURCE** — scope limited to the four injectable names; Rust-side
  rename fails a test naming both files; header-only entries untouched; version
  trigger recorded here
- [x] **CRITERION-SHAPE** — step-value criterion rejected; heuristic limitation
  stated in `ARCHITECTURE.md`; closed runbooks unmodified
- [ ] **REVIEW-DISCIPLINE** — both rules in `AGENTS.md` citing v0.14; undated
  disposition fails `cycle-check`; non-executable status stated
- [ ] **RE-MEASURE** — hosted run pinned; every count equals local at the same
  commit; identity set matches derived value; new pin count in three places
- [ ] **R-CLOSE** — version cites Step 4; candidate and release commit separate;
  disposition dated; all four open items recorded open

---

## Standing prohibitions

- **Do not touch published releases.** `v0.14.0`, `v0.13.0`, `v0.12.0`,
  `v0.11.0`, `v0.10.3`, and unpublished `v0.10.2` are immutable — tags, commits,
  pins, receipts.
- **Do not edit any closed runbook or progress log.** Corrections go forward.
- **Do not solve a derived-scope gap by adding a third list.** A manifest that
  itself needs hand-maintaining reproduces the defect one level up. Parse what
  exists; if you cannot, say why in writing.
- **Do not silently exempt a check from R10.** Every exemption is declared, has
  a stated reason, and is counted in the report.
- **Do not add an `invariant-scan` rule without site-specific controls.**
- **Do not let `invariant-scan` acquire a runtime dependency.** Static analysis
  over source, config, and git only.
- **Do not add a ci-local job.** The count enters at 20 and exits at 20.
- **Do not edit source under `crates/` or `apps/` in Steps 2, 3, 5, or 6.** A
  check that fails against HEAD is a finding, not a licence.
- **Do not re-raise the hosted 1-skipped test** — it is intended behavior,
  recorded in the entering state.
- **Do not claim any task closes or narrows A4**, the L1 residual, or the R3/R4
  open-bottom limitations.
- **Do not predict a count this file has not measured.** Where a quantity is
  needed, state the relation instead.
- **Do not run a live server session.** L2 remains scheduled.
- Do not change the public `/v1/*` JSON bodies, the SQLite schema, or the golden
  regression's 11 invariants. Golden stays 11/11 after **every** task.
- Do not hand-edit `Cargo.lock` (HC12), raise the offline Rust 1.78 floor, lower
  the Python 3.11 floor, or let core call an LLM (HC3).
- Do not commit `.env`, provider keys, tokens, or private key material.
- Do not batch `STATE.md` / `PROGRESS-v0.15.md` updates or combine two tasks in
  one commit.

## Runbook amendments

Step 1 — Add the governing E0 scope gate required by `AGENTS.md §5` — 2026-07-28
Step 2 — Widen the R10 gate to contain its architecture claim and any required hosted counterpart — 2026-07-28
Step 4 — Widen the gate for the operator decision and authorized H1/H3/Step 7 corrections; record the unchanged-name v0.14.1 trigger — 2026-07-28
Step 5 — Widen the gate to contain the required architectural limitation and active checklist record — 2026-07-28
