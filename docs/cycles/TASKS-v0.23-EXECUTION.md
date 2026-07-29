# TASKS-v0.23-EXECUTION.md — the workflow, and the scope that governs it

> **Draft r2, 2026-07-29.** Supersedes the r1 draft, which was never committed.
> Amendments fold in an independent re-measurement review (F1–F6), two gaps that
> review did not reach, and one document-architecture change. Nothing here has
> been activated; the `## Runbook amendments` discipline begins at the activation
> commit, not before it.

v0.22 executed the tagged-close protocol for the first time. Release parent
`a83db73…` is untagged, closing commit `15b6d289…` carries the record naming it,
the annotated v0.15.6 object `47c5b314…` targets the child, and remote `main`
peels to the same commit. **The published tree now contains its own closed
runbook** — the first time in this project's history — and G3 is corrected
forward rather than described.

Two things are wrong, and both are in prose rather than in code.

**`ARCHITECTURE.md` §8 still describes the pre-Option-C mapping.** Its Option C
paragraph describes the two-commit tagged close correctly. Its release-identity
tail says the authoritative mapping is the annotated tag to its exact **release
commit**, and that a separate audit "may follow the tagged commit." Under
Option C the tag targets the *closing* commit `C`. One document states both.

**And v0.22's own scope prohibition was unsatisfiable.** I wrote "Do not modify
any crate under `crates/` or `apps/`" into a cycle whose release necessarily
bumps `apps/cored/Cargo.toml` from `0.15.5` to `0.15.6` and rewrites
`Cargo.lock`. Release commit `a83db73…` did exactly that. The intent was "no
Rust source or behavior change"; the text said something a release cannot
satisfy. **That is the fourth unsatisfiable rule I have authored into this
project, and the first one no checker could have caught, because runbook scope
is prose and no tool reads it.** E0 measures that count rather than inheriting
it; see G6.

Meanwhile the trigger scheduled out of v0.22 is not pending. GitHub named
**2026-06-16** as the date runners begin defaulting to Node 24, with Node 20
removal in fall 2026; both hosted runs annotated the forced migration while
staying green. **The condition was satisfied six weeks before the disposition
that called it future was written.**

This cycle does five things:

1. **reconciles the release-identity prose to the protocol that is executed**,
   by deleting the duplicate rather than rewriting it;
2. **migrates the workflow's actions and pins the floating one**, in the one
   workflow that produces this project's evidence;
3. **makes runbook scope machine-readable and checked**;
4. **re-evaluates every recorded trigger against current measurement**;
5. **measures two defect populations that have been asserted from memory.**

**The public `/v1/*` JSON bodies, the SQLite schema, the robots matcher, the
negative TTL, the politeness limiter, and the golden regression's 11 invariants
are unchanged. Golden stays 11/11 byte-identical through every task.**

---

## Declared scope (draft — Step 4 validates and, if wrong, corrects it)

This block is committed at activation as the first subject of the rule Step 4
builds. **It is a draft: nothing validates it until Step 4 lands, and Step 4 must
record whether it needed correction.** An unvalidated block that turns out wrong
is itself a measurement.

```yaml
scope_version: 1
disposition_intent: release
allow:
  - .github/workflows/ci.yml
  - tools/cycle_check.py
  - tools/invariant_scan.py
  - config/invariant-rules.json
  - shell/tests/test_cycle_check.py
  - shell/tests/test_invariant_scan.py
  - AGENTS.md
  - ARCHITECTURE.md
release_authorities:
  - Cargo.toml
  - Cargo.lock
  - crates/*/Cargo.toml
  - apps/*/Cargo.toml
  - shell/intel_shell/__init__.py
  - shell/intel_shell/app.py
  - CHANGELOG.md
  - README.md
forbid:
  - crates/**/*.rs
  - apps/**/*.rs
  - shell/intel_shell/**
  - config/core.json
  - config/subscriptions*.json
```

**Two conflicts this block already exposes, both for Step 4 to resolve rather
than paper over:**

- `shell/intel_shell/app.py` carries the public FastAPI version literal **and**
  is production source. It is therefore in `release_authorities` and matched by
  `forbid`. A path-glob scope cannot express "the version line only." Step 4's
  default resolution is that `release_authorities` wins over `forbid` at R-CLOSE
  and human diff classification in `STATE.md` covers the rest — **and Step 4 must
  state that this weakens the rule for exactly one file.** Moving the literal
  into `__init__.py` and importing it would remove the overlap; that is a source
  change, out of scope here, and belongs in the forward record.
- `shell/tests/**` sits under `shell/` but is not production source, which is why
  `forbid` names `shell/intel_shell/**` rather than `shell/**`. If Step 4's
  matcher is prefix-based rather than glob-based this distinction collapses.

**Standing always-allowed status paths** are defined inside the checker, not
re-enumerated per cycle: `STATE.md`, the active `docs/cycles/PROGRESS-vX.Y.md`,
and the active `docs/cycles/TASKS-vX.Y-EXECUTION.md`. `AGENTS.md` is *not* in the
standing set — it is in this cycle's `allow` because Steps 2, 4, and 5 each edit
it.

---

## Entering state (asserted, not yet verified)

**Every sentence here is a hypothesis until Step 1 (E0) measures it.**

- `v0.15.6` is published under the tagged-close protocol. Release parent
  `a83db73aac3d5ef1e9a427662340eb1eb8a49df1`, closing commit
  `15b6d28973058c833a77e9600741d29eda02cdc1`, annotated tag object
  `47c5b314acd6f7fb42bba2f90312bf1185277c5c` targeting the closing commit.
  Closing evidence is candidate run `30443692105`; post-push run `30446796322`
  is dated forward confirmation. v0.22 is closed 6/6. **None of this is
  reopened.**
- Local `main` is one commit ahead at `c9e3394…`, unpushed, per the accepted
  cycle-ending rhythm.
- Protected pins are **221** — **219** evidence plus **2** authorization
  surfaces. Golden is **11/11**. Local CI is **20/20** with **133** workspace
  tests, **55** net tests (**29** `intel-ingest` + **26** `cored`), shell
  **266/266** on Python 3.11 and 3.12, `invariant-scan` **12/12 rules /
  36 controls** with **13** R12 mutations, `checklist-audit` **177/177** with
  **three** retractions.
- `.github/workflows/ci.yml` pins `actions/checkout@v4` ×7,
  `actions/attest-build-provenance@v4` ×7, `actions/upload-artifact@v4` ×7,
  `dtolnay/rust-toolchain@master` ×6, `Swatinem/rust-cache@v2` ×5, and
  `actions/setup-python@v5` ×2.
- G3 is refuted; G4 is accepted with bounds (**1 MiB** manifest or two
  consecutive `verify-artifacts` runs at **≥1.00 s**); the shell
  `StarletteDeprecationWarning` is accepted until its named trigger.
- A4, the editable-L1 controller residual, the R3/R4 open-bottom deny-lists, the
  active-runbook measured-value heuristic, T7 robots single-flight, and
  NEGATIVE-CACHE Decision B remain open. L2 remains scheduled. `v0.8.0` and
  `v0.10.2` remain valid local-only annotated tags under the A/A/E disposition,
  with `--skip-local-tag-verification` retained under its removal trigger.
  **No step in this file closes or narrows any of them.**

---

## Drafted gates

| Gate | Where | Hypothesis |
|---|---|---|
| **G1** [drafted P2 — E0 settles it] | `ARCHITECTURE.md` §8 release-identity tail versus its Option C paragraph; `AGENTS.md` R-CLOSE | **The document states both mappings.** Establish severity by **forcing the recorded identity onto the wrong commit**, not by adding an unrecorded tag — see E0 step 2. Prediction, not record: `check_tagged_closing_identity` and `check_publication_status` should both reject, which bounds this to a wasted release attempt rather than a bad published tag. |
| **G2** [P1] | `.github/workflows/ci.yml`; the fired Node trigger | **The evidence-producing workflow runs on an undeclared runtime.** Determine, from each action's own release notes or `action.yml` and from the github.blog changelog entry — **nothing secondary** — the current declared runtime of all six pins and the lowest major declaring Node 24. |
| **G3** [P1] | `dtolnay/rust-toolchain@master` | **A fully floating ref runs in the workflow that signs this project's evidence.** `attest-build-provenance` produces the attestations backing 219 evidence pins, and the toolchain action runs before it in all six usages. |
| **G4** [P1] | every runbook's prose Gate and prohibition blocks; `tools/cycle_check.py` | **Runbook scope is unreadable by any tool.** `grep -i scope tools/cycle_check.py` returns **zero** occurrences and no entry point compares a declared scope against a diff. **The zero is the claim; do not assert a function count** — define a counting method or omit the number. Enumerate the release-authority path set, and reproduce v0.22's contradiction as a measurement. |
| **G5** [P1] | `ARCHITECTURE.md`'s dated-dispositions table | **At least one recorded trigger was already satisfied when written, and nothing re-evaluates any of them.** Re-evaluate **every row that names a trigger** against present measurement. A table whose remaining triggers are genuinely unfired is a clean result and is recorded as one. |
| **G6** [P2] | this runbook's intro; `STATE.md`'s recorded failure family | **Two overlapping defect populations are asserted from memory.** `STATE.md` records a four-member *checker-rules-that-report-wrongly* family (v0.19 unsatisfiable, v0.20 no-op inputs, v0.21 vacuous, v0.22 self-referential). This runbook asserts a four-member *author-side-rules-that-cannot-be-satisfied* population (v0.19 freshness, v0.20 R-CLOSE ordering, v0.22 field set, v0.22 crate prohibition). They overlap on two members. **Give each a stated membership criterion and measure both against it**; a criterion makes a count reproducible where a citation list only makes it auditable. |

---

## How to run this file

Execute top to bottom, one task and one commit at a time. Follow `AGENTS.md §5`
after **every** task. Implementation and audit-record commits stay separate.

- **🤖 = Codex executes and self-verifies end to end** — no publication, no push
  to `main`, no ref creation or deletion **in the working repository**.
- **🧑 = exactly one named operator action or decision.**

**Disposable clones.** Several measurements require a throwaway clone. **State
its provenance every time**: a clone of the *local* repository carries `v0.8.0`
and `v0.10.2`; a clone of the *remote* does not. Refs created inside a disposable
clone are not repository refs and are not covered by the ref prohibitions below.
Delete the clone after measuring and confirm no ref changed in the working
repository.

**Dependency gates.** Step 2 precedes everything, because a document that
instructs a wrong tag is cheapest to fix while no release is in flight. Step 3
precedes Step 6, since the migrated workflow must be the one that produces the
candidate evidence. Step 4 precedes Step 5; both change `AGENTS.md` and must not
collide in one commit. Step 6 is blocked by every preceding implementation step;
Step 7 by Step 6.

### Cycle activation (before E0)

In a separate preparatory implementation/audit pair: confirm the worktree is
clean and record the measured refs **without asserting a literal `origin/main`
hash in `STATE.md`'s header**. Commit **only** this runbook at
`docs/cycles/TASKS-v0.23-EXECUTION.md` — **including its draft `## Declared
scope` block** — the `AGENTS.md` header moving the active declaration from v0.22
to v0.23, and a new `docs/cycles/PROGRESS-v0.23.md`. **Local `main` already
carries the unpushed audit `c9e3394…`; activation sits on top of it and does not
amend, rebase, or squash it.**

### Global definition of done

Protected hashes exact; all **221** pins match until Step 6 adds more; golden
**11/11 byte-identical**; `./run version-check` green; zero rustc warnings on
offline and net builds; all Rust tests green; all shell tests green under Python
3.11 **and** 3.12; clippy, fmt, ShellCheck, floor byte-compilation, and locked
Rust 1.78 green.

---

## Deferred means deferred

Each row carries a **dated measured observation** showing the trigger has not
fired. Per Step 5, an observation may be a dated negative statement where the
condition is an event rather than a quantity.

| Deferred item | Unchanged trigger | Measured 2026-07-29 | v0.23 action |
|---|---|---|---|
| T7 robots single-flight | a second concurrent harvester | one configured harvester; ingest is sequential | none |
| NEGATIVE-CACHE Decision B | a live transient robots outage for an admitted publisher while a usable last-known-good policy exists, plus operator authorization | no such outage observed | none |
| Postgres / pgvector / multi-host seam | unchanged | single writer, single host | none |
| A4 untrusted-shell boundary | a third-party/untrusted shell, or any claim HC1 is invariant under shell replacement | one first-party shell; no such claim made | none |
| L2 forced-command wrapper | an operator server session | no operator server session has occurred | none — remains scheduled |
| R3/R4 open-bottom coverage | a spelling outside registered vocabulary | none observed | none |
| Second configured publisher | a separate compliance review per publisher | no review opened | none — **do not add a source** |
| `v0.8.0` / `v0.10.2` publication | operator-authorized push of both exact annotated objects | not authorized | none — **no historical ref touched** |
| `--skip-local-tag-verification` removal | both historical tags published plus a passing hosted full-history `cycle-check` without the flag | tags unpublished | none — **the flag stays** |
| Manifest retention/indexing | 1 MiB manifest, or two consecutive `verify-artifacts` runs ≥1.00 s | re-measure at E0 step 6 | re-measure only |
| Version literal in `app.py` | a cycle whose declared scope permits shell source changes | literal present in production source | none — recorded, not acted on |

---

## Step 1 · E0 — Rebuild the entering state and settle six gates 🤖

**Objective.** Confirm HEAD is green and settle G1–G6, including G1's severity
and G6's counts, rather than inheriting either.

**Gate.** Read-only repository, object, disposable-clone, and local execution
measurements plus network reads of admissible published sources,
`PROGRESS-v0.23.md`, and this runbook's status records only. **No ref is
created, moved, or deleted in the working repository.**
**`.github/workflows/ci.yml` and `STATE.md` are not edited in this step.**

**Interpretive rule, binding on every construction in this step.** **An exit code
of 0 from a construction the checker never examined is "not measured," never
"does not reject."** Before recording any negative result, show that the rule
under test actually read the constructed input. This is the v0.21 vacuous-pattern
lesson applied to test constructions instead of rules; Step 4 or 5 should carry
it into `AGENTS.md`.

**Steps.**

1. Run the full entering matrix and standalone `./run golden`, plus
   `verify-artifacts`, `cycle-check`, `checklist-audit`, `progress-check`,
   `version-check`, `invariant-scan`, and `export-check`. **Record both Python
   lanes.**
2. **Settle G1's severity by forcing the recorded identity onto the wrong
   commit.** In a disposable clone **of the local repository** (state the
   provenance), run `git tag -f -a v0.15.6 a83db73…` and then `cycle-check`.
   Record the exit code and **every** message.
   - **Do not construct this with a novel tag name.** `cycle_check.py` contains
     no `for-each-ref` and no tag enumeration; it resolves only recorded
     identities. An unrecorded tag is invisible to every rule, and a 0 exit from
     it measures the instrument, not the property.
   - **If it rejects**, record **P2** with the grounds it rejected on. A releaser
     following the stale prose necessarily produces a *recorded* identity, so
     rejecting recorded wrong identities is exactly the property that bounds the
     defect. **State that the downgrade was measured, not argued.**
   - **If it does not reject**, first apply the interpretive rule and show the
     rules read the input. Only then is it P1, and Step 2 grows a guard.
   Delete the clone and confirm no ref changed in the working repository.
3. **Measure G2 from admissible sources only:** the github.blog changelog entry
   for the Node 20 deprecation, and each action's own releases page or
   `action.yml`. **Secondary sources circulate conflicting dates and are not
   admissible.** For each of the six pins record the runtime its currently pinned
   major declares, the lowest major declaring Node 24, and the URL and date read.
   **Do not choose a version from memory.**
4. **Measure G3.** Record what `dtolnay/rust-toolchain@master` resolves to right
   now — commit SHA and date — and confirm the six usages precede
   `attest-build-provenance` in their jobs.
5. **Confirm G4.** Record `grep -i scope tools/cycle_check.py` and its zero
   result; enumerate the exact release-authority path set; and **reproduce
   v0.22's contradiction as a measurement** — the prohibition text beside the
   release commit's changed paths. **Do not state a function or entry-point
   count** unless you define the counting method in the same sentence.
6. **Re-evaluate every row that names a trigger in `ARCHITECTURE.md`'s
   dated-dispositions table (G5).** For each: the condition, the measured present
   value, whether it has fired. **Re-measure the manifest byte size and
   `verify-artifacts` wall time rather than copying v0.22's figures.** Rows with
   no trigger — the REFUTED one — are out of scope and are recorded as such.
7. **Measure G6's two populations.** State a membership criterion for each, then
   enumerate members from closed runbooks and PROGRESS records **with citations**,
   and record where each member was found — a checker firing, a review, or an E0
   enumeration. **Report both sizes.** Do not force them into one taxonomy.
8. Re-verify the published `v0.15.6` objects — including that the peeled tag is
   the closing commit and its first parent is the release parent — and all
   **221** pins unchanged.

**Acceptance criteria.** Entering matrix captured with both interpreters named ·
G1 settled by the forced-identity construction, with clone provenance, exit code,
every message, and a P2/P1 record stating the basis · interpretive rule applied
to any zero exit · every action's runtimes read from admissible sources with URL
and date · `@master` SHA and date recorded · G4's zero-grep recorded, release
authorities enumerated, v0.22's contradiction reproduced, no undefined count
asserted · every triggered row re-evaluated with freshly measured values · both
G6 populations enumerated with criteria, citations, and discovery sites · no ref
changed in the working repository · published objects and 221 pins re-verified ·
`ci.yml` and `STATE.md` unedited · golden 11/11.

**Done when** every drafted gate is CONFIRMED or REFUTED with command output.

---

## Step 2 · RELEASE-PROSE (G1) — Delete the duplicate, not just the stale copy 🤖

**Objective.** Give the release protocol's mechanics exactly one prose home.

**Gate.** `ARCHITECTURE.md`, `AGENTS.md`, and status records — plus
`tools/cycle_check.py`, `shell/tests/test_cycle_check.py`, and
`config/invariant-rules.json` **only if E0 found G1 to be P1**. No workflow,
crate, source, dependency, schema, protected artifact, or public surface changes.

**Rewriting the stale paragraph fixes the instance and leaves the class.** The
mechanics are stated twice — in `AGENTS.md` R-CLOSE, which Codex executes, and in
`ARCHITECTURE.md` §8, which restates them. Restated state drifts, which is why
this project has one version authority and one lockfile.

**Steps.**

1. **`ARCHITECTURE.md` §8 keeps release-identity *semantics*** — the
   minor/patch/no-release classification, which is genuinely architectural — **and
   delegates tag *mechanics* to `AGENTS.md` R-CLOSE by a one-line pointer.**
   Remove the mechanical mapping sentences rather than correcting them.
2. **State the boundary explicitly** in whichever document retains the mechanics:
   releases through `v0.15.5` used the prior shape and their records retain it;
   `v0.15.6` onward uses the tagged close. A reader must not have to infer this
   from dates.
3. **Acceptance is a zero, not a match.** Grep `ARCHITECTURE.md` for any sentence
   mapping a tag to a commit and record the grep with its output. **Zero
   mechanical mapping sentences remain** is stronger and simpler than "one
   mapping stated in both documents."
4. **Add an executable literal-scan rule only if E0 found P1.** If E0 found P2,
   do not add one — a guard duplicating `check_tagged_closing_identity` is
   apparatus over a clean check, and this project's standing preference is to
   record the clean check. **Note honestly in the record that a one-time grep
   reduces the class rather than deleting it**, and name the literal-scan rule as
   the forward option if the duplicate ever recurs.

**Acceptance criteria.** Mechanics stated in exactly one document with a pointer
from the other · pre-v0.15.6 boundary stated explicitly · grep for mechanical
mapping sentences in `ARCHITECTURE.md` returns zero, recorded with its output ·
rule added **only** if E0 found P1, with a detected planted failure · the
grep-versus-rule distinction recorded honestly · `cycle-check`,
`checklist-audit`, `progress-check` green · golden 11/11.

---

## Step 3 · ACTION-MIGRATION (G2, G3) — The workflow that signs the evidence 🤖🧑

**Objective.** Move every action to a major that declares Node 24, and pin the
floating one.

**Gate.** 🧑 **One narrow authorization: a non-`main` branch push for hosted
verification.** Scope is `.github/workflows/ci.yml` and status records. No crate,
Rust or Python source, dependency-graph, schema, protected-database, or public
surface changes. **The `--skip-local-tag-verification` flag is not removed.**

**This is the highest-risk step in the cycle.** `attest-build-provenance`
produces the attestations backing 219 evidence pins.

**The hosted set produced here is verification-only and is never admitted to the
manifest. Pins grow only at Step 6.**

**Steps.**

1. Update each action to the major E0 determined, **using E0's recorded sources
   rather than a version chosen here.** Where a major changes inputs or outputs,
   record the migration note from its own release notes.
2. **Pin `dtolnay/rust-toolchain` to a full 40-character commit SHA**, not a
   branch or floating name. Record the SHA, its date, and how it was obtained.
   **State the cost in the same breath**: pinned actions do not receive upstream
   fixes automatically. Name the trigger for revisiting the pin.
3. **Do this as one workflow edit**, but make the diff attributable: E0's
   per-action runtime table is what lets a later failure be traced without six
   separate hosted runs.
4. **Verify the evidence chain survives, in this order:**
   - `verify-artifacts` still matches all **221** existing pins. These are static
     files. **A pass here proves the manifest is intact and proves nothing about
     the new attestation machinery. Say so in the record.**
   - A hosted dispatch on the candidate branch produces a **new** authenticated
     receipt/bundle set, and that set verifies. **This is the only measurement
     that tests the upgraded signing action.**
   - The identity set derived from the hosted run matches the expected value.
5. **If the new set does not verify, classify the failure before reverting.** The
   cryptographic check runs through `gh attestation verify`, whose decoder is
   selected by bundle extension, so the compatibility surface is the **operator's
   `gh` CLI**, not repository code — and this step's gate forbids touching
   repository code anyway. Distinguish *the upgraded signing action produced a
   set that does not verify* from *the operator's CLI predates the bundle
   format*. Same operational outcome, materially different claim.
   **Record `gh --version` either way, and record whether that same `gh` verified
   the existing 221 pins** — a CLI upgrade between the two measurements would
   confound the comparison.
6. **If it does not verify, revert only that one action pin to its prior major,
   re-measure, and record the split outcome.** Do not proceed to Step 4 with an
   unverified evidence chain, and **do not weaken verification to make it pass.**
7. Confirm the Node-runtime annotation is gone from the hosted log, and record
   any annotation that replaces it.

**Acceptance criteria.** Every action at a major declaring Node 24, each citing
E0's recorded source · `dtolnay/rust-toolchain` pinned to a full commit SHA with
date and revisit trigger · existing 221 pins verify, with the explicit note that
this does not test the new signing path · a **new** hosted authenticated set
produced and verified, stated as verification-only and not admitted · any failure
classified as action-side or CLI-side with `gh --version` recorded · Node-runtime
annotation absent and any replacement recorded · a failing upgrade reverted
rather than worked around · golden 11/11.

---

## Step 4 · SCOPE-DECLARED (G4) — Make the declaration readable 🤖

**Objective.** Make runbook scope machine-readable and checked against the
cycle's own diff.

**Gate.** `tools/cycle_check.py`, `shell/tests/test_cycle_check.py`,
`config/invariant-rules.json`, `tools/invariant_scan.py`,
`shell/tests/test_invariant_scan.py`, `AGENTS.md`, this runbook's own scope
block, and status records. **Blocked on E0 confirming G4.** No workflow, crate,
source, dependency, schema, protected artifact, or public surface changes.

**Two sub-rules with different firing times. State both; claim neither for the
other.**

- **Static sub-rule — fires at activation.** If the declared or recorded
  disposition is `release`, the declared scope must permit every enumerated
  release-authority path. **This is the sub-rule that would have caught v0.22, at
  activation.**
- **Diff sub-rule — fires at the first per-task gate after an offending commit.**
  Every path changed between the activation anchor and `HEAD` falls within the
  declared scope. **It cannot fire at activation, because activation's diff is
  empty.**

**Steps.**

1. Define the scope block schema. **Keep it small** — a schema that takes a cycle
   to fill in will be filled in badly. **Reuse `check_active_deferral_assignments`'s
   table-parsing conventions** rather than inventing a second dialect for
   structured runbook content.
2. **Define a standing always-allowed status set inside the checker**, not in
   each cycle's block: `STATE.md`, the active `PROGRESS-vX.Y.md`, and the active
   runbook. Without it every block re-enumerates the same paths and a cycle that
   forgets one fails on its own audit commits. **`AGENTS.md` is deliberately not
   standing** — it is a contract, and a cycle that edits it should have to say so.
3. **Define the diff range endpoints exactly** — whether the activation anchor is
   inclusive or exclusive of its own edits — and state the convention in
   `AGENTS.md`. An off-by-one silently exempts or includes the activation paths,
   and the fixture will otherwise encode whichever convention the implementation
   happened to pick.
4. **Resolve the two conflicts this runbook's draft block already exposes.**
   `shell/intel_shell/app.py` is both a release authority and forbidden
   production source; the default resolution is that `release_authorities` wins
   at R-CLOSE, and **the record must state that this weakens the rule for exactly
   one file** and name the literal-relocation as a forward option. Confirm the
   matcher is glob-based, so `shell/intel_shell/**` does not swallow
   `shell/tests/**`.
5. **Apply the rule from v0.23 forward only.** Closed runbooks have no scope
   block and **must not be retrofitted**; a check demanding one from immutable
   documents would fail on history. State the boundary in `AGENTS.md`.
6. **Fail-before against a fixture — not against v0.22.** Construct a scope block
   reproducing v0.22's prohibition, apply it to that cycle's changed path set, and
   capture the rejection naming `apps/cored/Cargo.toml` and `Cargo.lock`. **Do not
   edit the closed v0.22 runbook to create a control.**
7. **Validate this runbook's activation-committed draft block and record whether
   it needed correction.** It landed unvalidated by construction; whether it was
   right is a measurement worth having. If this file's scope cannot be expressed
   in the schema, **the schema is wrong and this step says so** rather than
   widening the scope to fit.
8. Carry E0's interpretive rule — *exit 0 on an unexamined construction is "not
   measured"* — into `AGENTS.md` beside the planted-failure discipline.
9. Register the new rule as an R12 planted-failure mutation and report the new
   rule and control counts in `STATE.md`, `PROGRESS-v0.23.md`, and the pending
   closing record.

**Acceptance criteria.** Schema small and reusing the existing table dialect ·
both sub-rules implemented with their firing times stated separately · standing
allowed set inside the checker, `AGENTS.md` excluded from it · diff endpoints
defined and documented · `app.py` overlap resolved with the weakening stated ·
matcher confirmed glob-based · v0.23-forward boundary in `AGENTS.md` · fixture
fail-before with no closed runbook edited · this runbook's draft block validated
and its correctness recorded · interpretive rule carried into `AGENTS.md` · new
rule has a detected planted failure · counts in three places · golden 11/11.

**Done when** a declared scope that a release cannot satisfy fails at activation,
**and** a commit outside declared scope fails at its own task gate.

---

## Step 5 · TRIGGER-FRESHNESS (G5) — A trigger states what it measured 🤖

**Objective.** Make every recorded trigger carry a dated measurement, and act on
E0's re-evaluation.

**Gate.** `ARCHITECTURE.md`'s dated-dispositions table, this runbook's deferral
table, `AGENTS.md`, `tools/cycle_check.py` or `tools/invariant_scan.py` and their
tests, and status records. **Blocked on E0's re-evaluation.** No workflow, crate,
source, dependency, schema, protected artifact, or public surface changes.

**Steps.**

1. **Name the rule's document set explicitly**: the live `ARCHITECTURE.md`
   dated-dispositions table and the **active** runbook's "Deferred means
   deferred" table, **v0.23-forward**, mirroring Step 4's boundary. An unscoped
   rule is either vacuous — the family v0.21 closed — or it fails on append-only
   history that must not be retrofitted.
2. Require every row **that names a trigger** to carry a **dated measured
   observation**. Rows with no trigger, such as the REFUTED one, are out of
   scope and the rule must say so rather than fail on them.
3. **A measurement may be a dated negative observation where the condition is an
   event rather than a quantity.** L2's trigger is "an operator server session";
   there is no metric, and "2026-07-29: no operator server session has occurred"
   is a complete measurement. **Without this, the rule has no satisfying
   assignment for event-shaped triggers and becomes the fifth unsatisfiable rule
   in this project's record.**
4. Add the format rule with a planted-failure control. **Check the presence and
   the date of a measurement clause, not its truth.** A checker cannot evaluate
   "GitHub has named a date," and a rule reporting on what it cannot see is the
   family v0.21 closed.
5. **Backfill every triggered row with E0's freshly measured value**, dated.
   **This runbook is again its own first subject** — its deferral table already
   carries a measured column, and the rule must accept it or the schema is wrong.
6. **Act on any trigger E0 found already fired.** The Node one is handled by
   Step 3 and its row becomes a completed disposition. **For any other, record it
   and assign it forward with a named cycle — do not absorb it into this cycle's
   scope.** That is the rule v0.22 established when this same trigger fired
   mid-cycle, and it holds regardless of convenient timing.
7. **Report the re-evaluated and fired counts exactly. If the answer is one, say
   one** — a single instance is a finding, not a pattern.

**Acceptance criteria.** Document set named and bounded v0.23-forward · only
triggered rows in scope · dated negative observations accepted for event-shaped
conditions · rule checks presence and date, not truth, with a detected planted
failure · every triggered row backfilled with a freshly measured value · this
runbook's own table validated by the rule · additionally fired triggers assigned
forward, not absorbed · counts reported exactly · golden 11/11.

---

## Step 6 · RE-MEASURE 🤖🧑

**Objective.** Produce release-grade hosted evidence for the v0.23 candidate,
**on the migrated workflow**.

**Gate.** 🧑 **One narrow authorization: a non-`main` branch push.** Remote
mutation is limited to the exact candidate branch and its authenticated hosted
evidence dispatch. Repository admission is limited to that run's signed
receipt/bundle pairs, the release-posture deferred-audit report,
`config/protected-artifacts.json`, and status records. No tag, `main` advance,
publication, source, public surface, dependency, lockfile, schema, or protected
database changes.

**Steps.**

1. Push the candidate to a **neutral branch name that does not prejudge Step 7's
   disposition**, as `candidate/v0.15.5-v0.22` did.
2. **Read the remote branch's `ci.yml` and confirm its blob equals the local one
   before dispatching.** This matters more than usual: the workflow itself is
   what changed.
3. Dispatch with `publish_evidence: true` and `audit_sha` set to the candidate.
4. **Read every count out of the hosted log**, not from job status, and compare
   each against the local measurement **at the same commit**.
5. Record the hosted `invariant-scan` rule and control counts; Steps 4 and 5 add
   rules and they must be detected here.
6. **Record this run id prominently.** Under the tagged close it is the evidence
   the closing record cites, and it is needed before the push rather than after.
7. Commit the signed receipt/bundle set, re-run `./run verify-artifacts` and
   `./run evidence-report`, and record the new pin count in `STATE.md`,
   `PROGRESS-v0.23.md`, and the pending closing record. **These are the first
   pins admitted this cycle; Step 3's set was verification-only.**
8. Run `./run audit-deferred` in release posture with attestations required.

**Acceptance criteria.** Hosted run pinned to the candidate on a neutral branch ·
remote `ci.yml` blob confirmed equal to local before dispatch · every count read
from the log and equal to local at that commit · hosted `invariant-scan` counts
recorded and increased by Steps 4–5 · candidate run id recorded as citable
closing evidence · signed set committed and re-derived · new pin count in three
places · `origin/main` unchanged, no tag · golden 11/11.

---

## Step 7 · R-CLOSE 🧑🤖

**Objective.** Close the cycle under the tagged-close protocol.

**Gate.** Steps 1–6 complete and boxed. Worktree clean. **🧑 One operator
decision: publication.**

**Steps.**

1. **Follow the Option C tagged-close protocol as `AGENTS.md` states it**, with
   Step 2's corrected documents in force: release parent `R` untagged, closing
   child `C` naming `R` with no tag-object field, tag over `C`, atomic push,
   post-push result in a dated forward append.
2. Re-run the complete definition of done at the release parent and capture it.
3. Record the version choice and the trigger that fired.
4. **Name the publication trigger.** Unlike the last two cycles one is visible at
   entry: the published workflow runs actions on a runtime they do not declare,
   and the published `ARCHITECTURE.md` instructs a future releaser to tag `R`.
   **State which is the trigger, or that both are.**
5. Record evidence candidate and release parent as **separate named fields**.
6. **State the release disposition as of a date**, in the form
   `cycle_check.py`'s validator reads.
7. **Record G1's settled severity and its basis.** If E0 downgraded it to P2, say
   the downgrade was measured — and name the construction that measured it, since
   the r1 draft's construction would have measured nothing.
8. **Record G6's two measured populations with their criteria**, not a remembered
   count. State where each member was found. **The claim that earlier members
   were "found by the checkers" must be cited per member, not asserted for the
   group** — v0.22's field-set defect was found by an E0 enumeration, not by a
   rule firing.
9. **Record the scope defect as author-side and as the first found only by human
   review**, because runbook scope was prose. Step 4 closes that asymmetry and is
   this cycle's actual product.
10. **Record Step 3's evidence-chain result explicitly** — that a new
    authenticated set was produced and verified under the upgraded signing
    action, with the action-side/CLI-side classification if it failed — not
    merely that the old pins still match.
11. Record Step 5's re-evaluated and fired counts, and Step 4's finding on
    whether the activation-committed scope block was correct.
12. Classify every diff path exactly once in `STATE.md`; update `CHANGELOG.md`,
    `README.md`, and the release authorities.
13. Reconcile `ARCHITECTURE.md`. **A4, the L1 controller residual, the R3/R4
    open-bottom limitations, the measured-value heuristic, T7, and
    NEGATIVE-CACHE Decision B must all still read as open**, and the A/A/E tag
    disposition unchanged. Add the `app.py` version-literal relocation as a
    recorded forward option.
14. Record the post-push hosted result as a **dated forward append**. Under the
    tagged close it is confirmation, not the closing event; **a red post-push run
    is a finding for v0.24 and does not invalidate the close.**
15. **Record one forward observation, not a task.** v0.21, v0.22, and v0.23 are
    three consecutive cycles whose entire defect population lived in the
    apparatus rather than in runtime code. That work was debt repayment with
    measurable output — Option C corrected a real published-tree defect, R12
    corrected controls that could not fail. **After this cycle the scheduled
    apparatus queue is empty**, and every remaining open item is product or
    architecture. Note that v0.24 is the natural place to test whether the
    apparatus makes product work cheap. **Do not schedule it here.**
16. **Carry the one-publisher fact forward unchanged.** `arxiv-cs` remains the
    sole real publisher; the other three configured sources remain fixtures.

---

## Cycle checklist

- [ ] **E0** — entering matrix with both interpreters; G1 settled by the
  forced-identity construction with clone provenance and full messages;
  interpretive rule applied to any zero exit; action runtimes from admissible
  sources with URL and date; `@master` SHA recorded; G4's zero-grep recorded with
  release authorities enumerated and v0.22's contradiction reproduced, no
  undefined count asserted; triggered rows re-evaluated with fresh measurements;
  both G6 populations enumerated with criteria and discovery sites; no working-
  repository ref changed
- [ ] **RELEASE-PROSE** — mechanics in exactly one document with a pointer from
  the other; pre-v0.15.6 boundary stated; `ARCHITECTURE.md` grep returns zero
  mechanical mapping sentences; rule added only if E0 found P1; grep-versus-rule
  distinction recorded honestly
- [ ] **ACTION-MIGRATION** — every action on a Node-24 major from E0's sources;
  `dtolnay/rust-toolchain` SHA-pinned with a revisit trigger; a **new** hosted
  authenticated set produced and verified as verification-only; failure
  classified action-side or CLI-side with `gh --version`; annotation gone; any
  failing upgrade reverted rather than worked around
- [ ] **SCOPE-DECLARED** — schema small and reusing the existing table dialect;
  both sub-rules with firing times stated separately; standing status set inside
  the checker with `AGENTS.md` excluded; diff endpoints defined; `app.py` overlap
  resolved with the weakening stated; v0.23-forward boundary; fixture fail-before
  with no closed runbook edited; activation block validated and its correctness
  recorded; interpretive rule in `AGENTS.md`
- [ ] **TRIGGER-FRESHNESS** — document set named and bounded; only triggered rows
  in scope; dated negative observations accepted; rule checks presence and date,
  not truth; every row backfilled; this runbook's table validated; additionally
  fired triggers assigned forward; counts exact
- [ ] **RE-MEASURE** — hosted run on a neutral branch; remote `ci.yml` blob
  confirmed before dispatch; counts equal local; run id recorded as closing
  evidence; first pins of the cycle admitted here
- [ ] **R-CLOSE** — tagged-close protocol followed; publication trigger named;
  G1's severity and its measuring construction recorded; G6's populations
  measured with per-member discovery sites; evidence-chain result stated;
  post-push result in a dated forward append; v0.24 observation recorded as an
  observation

---

## Standing prohibitions

- **Do not modify Rust or Python source, or any runtime behavior.** The release
  authorities and `Cargo.lock` are expected to change at R-CLOSE and are in
  scope; **this is the distinction v0.22's prohibition got wrong.**
- **Do not create, move, or delete any ref in the working repository**, including
  `v0.8.0` and `v0.10.2`. **Refs inside a disposable clone are not repository
  refs**; state the clone's provenance, and confirm afterward that no
  working-repository ref changed.
- **Do not construct a checker test with an input the checker cannot reach.** An
  exit code from an unexamined construction is not a measurement.
- **Do not weaken evidence verification to make an upgraded signing action
  pass.** Revert the pin and record the split outcome.
- **Do not treat matching the existing 221 pins as evidence that the new
  attestation path works.** Only a new authenticated set tests it.
- **Do not admit Step 3's hosted set to the manifest.** Pins grow only at Step 6.
- **Do not choose an action version from memory or from a secondary source.**
- **Do not remove `--skip-local-tag-verification`.**
- **Do not edit a closed runbook** to construct Step 4's fail-before; use a
  fixture. **Do not retrofit scope blocks onto closed runbooks.**
- **Do not add a rule without an R12 planted-failure control.**
- **Do not add a checker rule that evaluates a condition it cannot observe.**
- **Do not write a rule with no satisfying assignment for a case it governs.**
  Step 5's event-shaped triggers are the live instance.
- **Do not absorb a newly fired trigger into this cycle.** Record it and assign
  it forward with a named cycle.
- **Do not touch the robots matcher, the negative TTL, the politeness limiter, or
  the crawl-delay ratchet.**
- **Do not add a configured source.**
- **Do not amend, rebase, or squash `c9e3394…`.**
- **Do not claim any task closes or narrows A4**, the L1 residual, the R3/R4
  open-bottom limitations, T7, or NEGATIVE-CACHE Decision B.
- **Do not batch `STATE.md` / `PROGRESS-v0.23.md` updates or combine two tasks in
  one commit.**
- If any Step's Objective, Acceptance criteria, or "Done when" is amended after
  this file is committed at activation, name the amendment in a dated
  `## Runbook amendments` block in the same commit.

---

## Provenance of this draft

Every gate was read out of the repomix export of the v0.15.6 tree on 2026-07-29
by path, and each is a hypothesis for E0 to confirm or refute. **Citations are by
section anchor rather than line number**, because Step 2 renumbers
`ARCHITECTURE.md`.

**Three claims in this draft were verified against the export rather than
reasoned to.** `grep -i scope tools/cycle_check.py` returns zero. `cycle_check.py`
contains no `for-each-ref` and no tag enumeration, which is what makes the r1
draft's G1 construction unable to measure anything. `tools/audit_deferred.py`
locates `gh` via `shutil.which` and relies on `gh attestation verify` selecting
its decoder by bundle extension, which is what puts the bundle-format
compatibility surface in the operator's CLI rather than in repository code.

**Two defects in the r1 draft are corrected here and are recorded rather than
silently fixed.** Its G1 construction — an annotated tag with an unspecified name
on the release parent — would have exited 0 because no rule enumerates refs, and
its decision rule would then have forced P1 and a guard nobody needed: an
instrument limitation manufacturing a severity. And its introduction said
"third unsatisfiable rule" while Step 7 and the provenance section said "fourth"
with four named members. **Committing a document about false claims with an
internal contradiction about its own headline defect would have been a recorded
false claim from activation onward.** Both were found by independent review, not
by any check — which is the same asymmetry G4 exists to close.

**v0.22's execution is sound and is not reopened.** Option C ran end to end: the
untagged release parent, the closing child recording it without a tag-object
field, the annotated tag over the child, the atomic push, and the dated forward
append are all present and verified, with candidate run `30443692105` as closing
evidence and `30446796322` as confirmation. The A/A/E tag disposition, the
retained hosted skip with its trigger, the refuted G3, and the bounded G4
acceptance all stand.
