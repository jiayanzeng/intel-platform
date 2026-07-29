# TASKS-v0.22-EXECUTION.md — the record that cannot contain itself

v0.21 closed cleanly and v0.15.5 is published. R12 now invokes the real
`check_publication_status` entry point over nine planted cases and independently
disables all seven rule families; `invariant-scan` reads 12/12 rules and 30
controls. Codex's production review holds — `/v1/ask` still routes model output
through core `/attest`, IndexOnly text is excluded from public responses,
hydration is sector-scoped in core SQL, canonical identity is re-materialized
globally through the single threshold, and no model client exists in the Rust
core.

Two forward items were carried out of v0.21, and **the first of them is not what
I said it was.**

In the v0.21 publication decision I described G3 as an ordering problem and
proposed a two-phase close that cites candidate hosted evidence. That
diagnosis was incomplete. `cycle_check.py` requires a closing record to contain
both:

```
- **Release commit:** `<40 hex>`
- **Annotated tag object:** `<40 hex>`
```

**A record that must name the hash of the commit containing it cannot exist in
that commit.** No ordering of steps fixes that, and citing candidate evidence
instead of post-push evidence does not touch it. This is a second fixed point,
in the required fields rather than in the sequence — the same species as v0.19's
`origin/main` freshness rule, which v0.20 resolved by moving the value out of
the text rather than by trying to make the text right.

The second item is heavier than a tooling defect. Three closed runbooks record
annotated tags `v0.8.0` and `v0.10.2` that independent remote inspection could
not find, and hosted CI can never settle it because it runs
`cycle-check --skip-local-tag-verification`. **That is a claim about release
identity that nothing corroborates.**

This cycle does two substantial things and three cheap ones:

1. **resolves the closing-record fixed point** by an explicit operator decision
   among enumerated options, each with its coverage cost stated;
2. **classifies the missing historical tags** before any record or ref is
   changed;
3. gives named dispositions to three residuals that are currently neither
   accepted nor open.

**The public `/v1/*` JSON bodies, the SQLite schema, the robots matcher, the
negative TTL, the politeness limiter, and the golden regression's 11 invariants
are unchanged. Golden stays 11/11 byte-identical through every task. No crate
under `crates/` or `apps/` is modified by any step in this file.**

**Version disposition.** Default is a patch release **`v0.15.6`**. No `/v1/*`
route or body moves and no crate changes. **No publication trigger is visible at
entry: the published head is green and its controls are failure-capable.** A
no-release close is legitimate. **`v0.16.0`** applies only if a `/v1/*` body or
route moves.

---

## Entering state (asserted, not yet verified)

**Every sentence here is a hypothesis until Step 1 (E0) measures it.**

- `v0.15.5` is published. Release commit
  `b7c4b10eb506923e3ea854a32d1dc3f4c83b0eaa`, annotated tag object
  `f2bfeacc1dc8207841430e3827e7babed5605b47`. v0.21 is closed 6/6 with
  `Release disposition: release (as of 2026-07-29)`. **None of this is
  reopened.**
- Post-push run `30435272303` attempt 1 passed all seven executable jobs at the
  exact release head.
- Local `main` is one commit ahead at closing audit `188055a`, unpushed, touching
  only `STATE.md`, the v0.21 runbook, and its progress log.
- Protected pins are **206** — **204** evidence plus **2** authorization
  surfaces. Golden is **11/11**. Local CI is **20/20** with **133** workspace
  tests, **55** net tests (**29** `intel-ingest` + **26** `cored`), shell
  **258/258** on Python 3.11 and 3.12, `invariant-scan` **12/12 rules /
  30 controls**.
- `export-check` passes 90 derived sources, 7 required paths, 149 exported paths,
  and is **operator-local**: `.github/workflows/ci.yml` does not invoke it.
- G4 was accepted with a date: the final append-only audit of each cycle is
  locally verified when written and first hosted-verified at the following
  publication.
- A4, the editable-L1 controller residual, the R3/R4 open-bottom deny-lists, the
  active-runbook measured-value heuristic, T7 robots single-flight, and
  NEGATIVE-CACHE Decision B remain open. L2 remains scheduled. **No step in this
  file closes or narrows any of them.**

---

## Drafted gates

| Gate | Where | Hypothesis |
|---|---|---|
| **G1** [P1] | `tools/cycle_check.py`: `RELEASE_COMMIT_RE`, `TAG_OBJECT_RE`, `newest_closed_release` | **The closing record's required fields are self-referential.** `Release commit` names the hash of the commit that carries the record; `Annotated tag object` names the tag over it. Neither is knowable at write time. Prove this is a field constraint, not a step ordering: show that **no** permutation of R-CLOSE's steps produces a release commit whose tree contains a valid closing record. **The correction in the v0.21 decision record — a two-phase close on candidate evidence — is necessary but not sufficient, and E0 should say so.** |
| **G2** [P1] | `docs/cycles/TASKS-v0.8-EXECUTION.md`, `TASKS-v0.8.1-EXECUTION.md`, `TASKS-v0.10.2-EXECUTION.md`; remote refs | **Three closed runbooks name annotated tags that no remote ref provides.** `v0.8.0` and `v0.10.2` did not resolve under independent remote inspection. Classify each as **local-only**, **deleted**, or **never created** before anything is changed. **Do not create, move, or delete a tag in this step, and do not edit a closed runbook.** |
| **G3** [P2] | `.github/workflows/ci.yml`; `AGENTS.md` | **The export budget is verified only when an operator remembers.** `export-check` exists, derives correctly, and never runs in CI. v0.20 permitted operator-local status *provided it was stated*. Confirm whether it is stated where a contributor would find it, and if not, that omission is the finding. |
| **G4** [P2] | `config/protected-artifacts.json`; `verify-artifacts` | **The evidence manifest grows without a stated bound.** It is **119,354** characters, and pins moved 159 → 176 → 191 → 206 across four cycles — roughly 15 per cycle, all retained forever. `verify-artifacts` re-hashes every pin on every run. Determine whether unbounded growth is an accepted property with a stated reason, or an unexamined default. **A recorded acceptance is a complete answer.** |
| **G5** [P3] | v0.21 warning disposition | **Two third-party warnings are recorded but have no trigger.** The `StarletteDeprecationWarning` and the hosted GitHub Actions Node-runtime deprecation annotation are noted as non-blocking each cycle. State the condition under which either becomes work, or record that they are permanently accepted. **A refuted G5 is deleted, not worked around.** |

---

## How to run this file

Execute top to bottom, one task and one commit at a time. Follow `AGENTS.md §5`
after **every** task. Implementation and audit-record commits stay separate.

- **🤖 = Codex executes and self-verifies end to end** — no publication, no push,
  and **no ref creation, movement, or deletion.**
- **🧑 = exactly one named operator action or decision.**

**Dependency gates.** Step 2 precedes Step 3, because a decision about how
releases are recorded must precede any judgement about historical release
records. Step 5 is blocked by every preceding implementation step; Step 6 by
Step 5.

### Cycle activation (before E0)

In a separate preparatory implementation/audit pair: confirm the worktree is
clean and record the measured refs **without asserting a literal `origin/main`
hash in `STATE.md`'s header**. Commit **only** this runbook at
`docs/cycles/TASKS-v0.22-EXECUTION.md`, the `AGENTS.md` header moving the active
declaration from v0.21 to v0.22, and a new `docs/cycles/PROGRESS-v0.22.md`.
**Local `main` already carries the unpushed closing audit `188055a`; activation
sits on top of it and does not amend, rebase, or squash it.**

### Global definition of done

Protected hashes exact; all **206** pins match until Step 5 adds more; golden
**11/11 byte-identical**; `./run version-check` green; zero rustc warnings on
offline and net builds; all Rust tests green; all shell tests green under Python
3.11 **and** 3.12; clippy, fmt, ShellCheck, floor byte-compilation, and locked
Rust 1.78 green.

---

## Deferred means deferred

| Deferred item | Unchanged trigger | v0.22 action before the trigger |
|---|---|---|
| T7 robots single-flight | a second concurrent harvester | none |
| NEGATIVE-CACHE Decision B | a measured live transient robots outage for an admitted publisher while a usable last-known-good policy exists, plus operator authorization | none |
| Postgres / pgvector / multi-host seam | unchanged | none |
| A4 untrusted-shell boundary | a third-party/untrusted shell, or any claim HC1 is invariant under shell replacement | none |
| L2 forced-command wrapper | an operator server session | none — remains scheduled |
| R3/R4 open-bottom coverage | a spelling outside registered vocabulary | none |
| Second configured publisher | a separate compliance review per publisher | none — **do not add a source** |
| CI-runner evidence | an authenticated receipt set with identified matrix legs, durably committed | **re-measure at the new release or closing commit — discharged by Step 5** |

---

## Step 1 · E0 — Rebuild the entering state and settle five gates 🤖

**Objective.** Confirm HEAD is green and settle G1–G5, with G1 established as a
field constraint rather than an ordering one.

**Gate.** Read-only repository, object, disposable-clone, and local execution
measurements plus `PROGRESS-v0.22.md` and this runbook's status records only.
**No ref is created, moved, or deleted.** No production path, tool,
configuration, dependency, protected artifact, or public surface changes.
**`STATE.md` is not edited in this step.**

**Steps.**

1. Run the full entering matrix and standalone `./run golden`, plus
   `verify-artifacts`, `cycle-check`, `checklist-audit`, `progress-check`,
   `version-check`, `invariant-scan`, and `export-check`. **Record both Python
   lanes.**
2. **Confirm G1 as a field constraint.** Enumerate the fields
   `newest_closed_release` requires and, for each, state whether its value is
   knowable before the commit carrying it exists. Then show by construction that
   a closing record placed in the release commit cannot satisfy
   `RELEASE_COMMIT_RE`, and that placing the tag over any commit whose tree
   contains the record cannot satisfy `TAG_OBJECT_RE`. **The deliverable is the
   demonstration that no step permutation helps**, not another instance of the
   failure.
3. **Measure what closing the runbook early would cost today.** In a disposable
   clone, mark a runbook closed with `Release: v0.15.6` while no such tag exists
   and run `cycle-check`. Record the exact message — this is v0.20's
   unavailable-input reporting firing correctly, and Step 2's options must each
   say how they avoid tripping it.
4. **Classify G2's tags.** Search every reflog, every remote, every local ref
   namespace, and the objects themselves for `v0.8.0` and `v0.10.2`. Report for
   each: does an object with the recorded hash exist anywhere; does any ref point
   at it; does the recorded release commit exist. **Report the classification —
   local-only, deleted, or never created — with the evidence for it. Change
   nothing.**
5. **Confirm or refute G3** by showing whether `AGENTS.md` or another contributor-
   facing document states that `export-check` is operator-local.
6. **Measure G4.** Record the manifest's byte size, pin count, the per-cycle pin
   growth across the last four cycles, and the wall time `verify-artifacts`
   takes at 206 pins. Search the repository for any stated retention policy.
7. **Answer G5** from the record: are the two warnings accepted, or merely
   repeated each cycle without a decision?
8. Re-verify the published `v0.15.5` objects and all **206** pins unchanged.

**Acceptance criteria.** Entering matrix captured with both interpreters named ·
G1 established as a field constraint with the no-permutation demonstration · the
early-close message recorded verbatim · G2 classified per tag with evidence and
**no ref touched** · G3 confirmed or refuted from the document text · G4 measured
with growth rate and verify time · G5 answered from the record · published
objects and 206 pins re-verified · `STATE.md` unchanged by this step · golden
11/11.

**Done when** every drafted gate is CONFIRMED or REFUTED with command output.

---

## Step 2 · CLOSE-FIELDS (G1) — Decide what a closing record may assert 🧑🤖

**Objective.** Choose, on the record, how a published tree can contain its own
closed cycle — and implement the choice.

**Gate.** 🧑 **One operator decision, at step 1.** Scope is
`tools/cycle_check.py`, its focused tests, `invariant_scan`'s registry and
controls, `AGENTS.md`'s R-CLOSE contract, and status records. **Blocked on E0
confirming G1.** No closed runbook, historical append, crate, dependency,
schema, protected database, or public surface changes.

**Steps.**

1. **🧑 Choose exactly one. Each option's coverage cost is stated and must be
   recorded with the choice.**

   - **Option A — Move both hashes out of the closing record.** The record keeps
     `Cycle closed`, `Release disposition`, and `Release: vX.Y.Z`. The release
     commit and tag object hashes move to a dated `STATE.md` publication append,
     and the checker resolves them from git by tag name instead of reading them
     from runbook text.
     **Cost:** the runbook no longer pins either hash, so a tag recreated over
     the same target with a different tagger or message is caught only by the
     append — which lands one cycle later. State that gap or require the append
     for every release older than the newest.

   - **Option B — Accept it, as G4 was accepted.** Record that every published
     tree shows its own cycle open, with the reason, dated.
     **Cost:** the published artifact permanently understates its own state, and
     `G3` becomes a standing property rather than a defect. Zero code, and it is
     a legitimate answer if the alternatives cost more than the property is
     worth.

   - **Option C — Drop only the tag-object field and tag the closing commit.**
     The release commit `R` carries the release edits and is not tagged. A
     closing commit `C` checks R-CLOSE's box and writes the record naming
     `Release commit: R` — knowable, because `R` already exists — with **no**
     `Annotated tag object` field. The annotated tag is created over `C`, and
     `C` plus the tag are pushed atomically. The closing record cites the
     **candidate** hosted evidence, which already exists at dispatch time; the
     post-push run id and the tag object hash go into a dated forward append.
     **Cost:** the tag object hash is no longer in the runbook at all, and the
     closing record cites candidate rather than published-head evidence — so
     "the cycle did not close until the published head was green" stops being
     literally true and must be restated as what it becomes.

   **Do not choose an option on the grounds that it is the smallest diff.**
   Record why the chosen coverage cost is acceptable.

2. **Fail-before before pass-after.** Whichever option is chosen, capture the
   corrected checker rejecting the pre-change shape, with its message verbatim.
3. **Register every changed or added rule as an R12 planted-failure control.**
   This is the discipline v0.21 established for exactly this family; a new rule
   without a planted failure re-opens the class v0.21 closed.
4. Update `AGENTS.md`'s R-CLOSE contract so the documented procedure and the
   executable check describe the same sequence. **A procedure that the checker
   cannot enforce is the thing this cycle exists to remove.**
5. **Do not repair the published v0.15.5 tree.** Whatever is chosen applies from
   the next publication forward; the existing published trees are history.
6. Report the new rule and control counts and record them in `STATE.md`,
   `PROGRESS-v0.22.md`, and the pending closing record.

**Acceptance criteria.** Exactly one option chosen and dated, with its coverage
cost recorded in the operator's own terms · fail-before captured with its
message · every changed or added rule has a detected planted failure · new
rule/control counts in three places · `AGENTS.md`'s R-CLOSE contract matches the
executable check · no closed runbook or published tree modified · focused tests
green on both interpreters · golden 11/11.

**Done when** a published tree can contain a closed cycle, or the record says
plainly why it never will.

---

## Step 3 · TAG-IDENTITY (G2) — Classify before touching anything 🧑🤖

**Objective.** Establish what `v0.8.0` and `v0.10.2` are, and decide what the
record should say.

**Gate.** 🧑 **One operator decision, at step 2.** Scope is status records, a
dated forward correction to `STATE.md`, and — **only if the operator chooses
it** — `config/checklist-retractions.json` or the closed runbooks' historical
banner mechanism. **Blocked on Step 2 and on E0's classification.** No crate,
dependency, schema, protected database, or public surface changes. **No tag is
created, moved, or deleted by 🤖 under any option.**

**Steps.**

1. Restate E0's classification per tag with its evidence.
2. **🧑 Decide, per tag, what the record should assert.** The options differ in
   what they claim, not merely in effort:
   - **The record is right and the remote is incomplete** — the tags exist
     locally or in a backup, and the correct action is to publish them.
     **Ref creation is an operator action, never Codex's**, and it must be a
     separate authorized step, not folded into this one.
   - **The record is wrong** — those releases were never tagged, and the closed
     runbooks assert a publication that did not occur. Correct forward through
     the project's existing closed-cycle correction mechanism. **Do not edit the
     closed runbooks' dated records**; use the banner and retraction machinery
     that already exists for this.
   - **Undetermined** — the evidence does not settle it. Record that, name what
     evidence would settle it, and stop. **An honest undetermined is a complete
     outcome; a guess dressed as a classification is not.**
3. **Whatever is decided, state whether this changes the retraction count.** It
   has stood at three for several cycles. If two release records were false,
   that number moves, and R-CLOSE must say so.
4. **Decide the `--skip-local-tag-verification` question separately.** Hosted CI
   passes that flag, so historical release-record tag agreement is never checked
   anywhere but an operator's clone. Either record the flag as deliberate with
   its reason, or name the trigger for removing it. **Do not remove it in this
   cycle** — doing so would turn a historical finding into a red CI head before
   the finding is resolved.

**Acceptance criteria.** Classification restated per tag with evidence · one
decision per tag, dated, with its claim stated · retraction count addressed
explicitly · `--skip-local-tag-verification` recorded as deliberate or given a
removal trigger, and **not removed** · no ref created, moved, or deleted by 🤖 ·
no closed runbook's dated record edited · golden 11/11.

---

## Step 4 · RESIDUALS (G3, G4, G5) — Three things become decisions 🤖

**Objective.** Give three currently-ambient facts a stated disposition.

**Gate.** `AGENTS.md`, `ARCHITECTURE.md`'s residual table, and status records.
**Blocked on E0 confirming or refuting each gate. A refuted gate's half is
deleted from the cycle, not worked around.** No tool logic, crate, dependency,
schema, protected artifact, or public surface changes.

**Steps.**

1. **G3.** If E0 found the operator-local status of `export-check` unstated,
   state it in `AGENTS.md` alongside the two export rules it already carries,
   with the consequence: a `repomix.config.json` change is caught when an
   operator runs the check, not at push. Name the trigger for making it a hosted
   gate.
2. **G4.** Record the manifest's growth as accepted-with-reason or
   bounded-with-a-trigger. **An acceptance must state the measured growth rate
   and the verify time it currently costs**, so a future reader can tell when the
   acceptance stopped being reasonable rather than rediscovering it.
3. **G5.** Give each third-party warning one disposition: permanently accepted,
   or accepted until a named trigger. **"Recorded as non-blocking" every cycle
   is not a disposition** — it is the absence of one, repeated.
4. Add each disposition to `ARCHITECTURE.md`'s residual table so it is reachable
   from the invariant reference rather than only from a progress log.

**Acceptance criteria.** Each of G3, G4, G5 has exactly one dated disposition, or
is deleted as refuted · G4's acceptance carries the measured growth rate and
verify cost · each disposition appears in the residual table · `cycle-check`,
`checklist-audit`, and `progress-check` green · golden 11/11.

---

## Step 5 · RE-MEASURE 🤖🧑

**Objective.** Produce release-grade hosted evidence for the v0.22 candidate.

**Gate.** 🧑 **One narrow authorization: a non-`main` branch push.** Remote
mutation is limited to the exact candidate branch and its authenticated hosted
evidence dispatch. Repository admission is limited to that run's signed
receipt/bundle pairs, the release-posture deferred-audit report,
`config/protected-artifacts.json`, and status records. No tag, `main` advance,
publication, product path, public surface, dependency, lockfile, schema, or
protected database changes.

**Steps.**

1. Push the candidate to a **neutral branch name that does not prejudge Step 6's
   disposition**, as v0.21's `candidate/v0.15.4-v0.21` did.
2. **Read the remote branch's `ci.yml` and confirm it contains every invocation
   you expect before dispatching**, and that its blob equals the local one.
3. Dispatch with `publish_evidence: true` and `audit_sha` set to the candidate.
4. **Read every count out of the hosted log**, not from job status, and compare
   each against the local measurement **at the same commit**.
5. **Record the hosted `invariant-scan` rule and control counts.** If Step 2
   added rules, they must be detected here; local detection is not the
   acceptance.
6. **If Step 2 chose Option A or C, this candidate run is the evidence the new
   closing record will cite.** Record its id prominently, because Step 6 will
   need it before the push rather than after.
7. Commit the signed receipt/bundle set, re-run `./run verify-artifacts` and
   `./run evidence-report`, and record the new pin count in `STATE.md`,
   `PROGRESS-v0.22.md`, and the pending closing record.
8. Run `./run audit-deferred` in release posture with attestations required.

**Acceptance criteria.** Hosted run pinned to the candidate on a neutral branch ·
every count read from the log and equal to local at that commit · hosted
`invariant-scan` counts recorded · candidate run id recorded as citable evidence
if Step 2 requires it · signed set committed and re-derived · new pin count in
three places · `origin/main` unchanged, no tag · golden 11/11.

---

## Step 6 · R-CLOSE 🧑🤖

**Objective.** Close the cycle under whichever procedure Step 2 chose.

**Gate.** Steps 1–5 complete and boxed. Worktree clean. **🧑 One operator
decision: publication.**

**Steps.**

1. **Follow Step 2's chosen procedure, not this file's habitual one.** If Option
   A or C was chosen, the closing record is written before the push and cites the
   candidate run; if Option B was chosen, the existing sequence stands and the
   accepted property is restated here.
2. Re-run the complete definition of done at the release or closing commit and
   capture it.
3. Record the version choice and the trigger that fired.
4. **State the publication disposition as a decision with a trigger, and note
   that no trigger was visible at entry.** The published head is green and its
   controls are failure-capable. **A no-release close is a complete outcome
   here**; if release is chosen, name what the published head would otherwise
   lack.
5. Record evidence candidate and release or closing commit as **separate named
   fields**.
6. **State the release disposition as of a date**, in the form
   `cycle_check.py`'s validator reads.
7. **Record G1 as the fourth instance of one family and the second fixed point
   in it.** v0.19 shipped an unsatisfiable rule, v0.20 two silent no-op paths,
   v0.21 a vacuous pattern, v0.22 a self-referential field set. **Record also
   that the v0.21 decision record misdiagnosed it as an ordering problem**, and
   that E0's field enumeration is what settled it. A correction to a prior
   diagnosis belongs in the record as plainly as a correction to code.
8. **Record G2's classification and decision**, and whether the retraction count
   moved.
9. Record each of Step 4's three dispositions with its date.
10. Classify every diff path exactly once in `STATE.md`; update `CHANGELOG.md`,
    `README.md`, and the release authorities if a release is chosen.
11. Reconcile `ARCHITECTURE.md`. **A4, the L1 controller residual, the R3/R4
    open-bottom limitations, the measured-value heuristic, T7, and
    NEGATIVE-CACHE Decision B must all still read as open.**
12. If a release is published, confirm afterward that hosted CI at the new remote
    head is **green** and record the run id. **If it is not green, that is the
    finding and the cycle does not close on a claim.**
13. **Carry the one-publisher fact forward unchanged.** `arxiv-cs` remains the
    sole real publisher; the other three configured sources remain fixtures.

---

## Execution records

### 2026-07-29 · E0

PASS. The Gate contained every acceptance surface: only this runbook's status
record and the append-only progress record move. `STATE.md` remained blob
`03053b14137161423a4f1bca617b8bc85d91e86b`, byte-identical to the entering
tree. No ref was created, moved, or deleted.

- **Entering matrix:** clean constrained Python **3.11.4** and **3.12.13**
  environments each resolved the same **21** packages and passed shell
  **258/258**, with the same third-party `StarletteDeprecationWarning`.
  `./run ci-local` passed all **20/20** jobs with **133** workspace tests,
  **55** net tests (**29** `intel-ingest` + **26** `cored`), locked Rust 1.78,
  zero rustc/clippy/fmt/ShellCheck failures, `invariant-scan` **12/12 rules /
  30 controls**, all **206/206** pins, protected databases **2/2**, and embedded
  golden **11/11**. Standalone golden passed **11/11**, delta **0**.
  `verify-artifacts`, `cycle-check`, `checklist-audit`, `progress-check`,
  `version-check`, and `invariant-scan` passed locally. Project-root
  `export-check` passed **90** derived sources, **7** required paths, and
  **151** exported paths; the two-path increase from the entering assertion's
  149 is exactly the newly admitted v0.22 runbook and progress log.
- **G1 — CONFIRMED as a field constraint.** For a closed release,
  `newest_closed_release` first needs a release disposition of `release`, then
  requires exactly one `Release`, `Release commit`, and `Annotated tag object`.
  The dated disposition and release name are knowable before the containing
  commit; the containing commit hash is not, because its tree includes the
  record; the annotated-tag object is not, because it includes the target
  commit hash. A disposable construction made placeholder commit
  `d50c598f53c81482794f75aba0cfd471e73919ff`; inserting that value into the
  record produced containing commit
  `5ef5015d176f4741fdef750ca2e080b0bc65977c`, not the named commit. Tagging
  that commit produced object
  `b8ec441f82330cf222a07f58229d7411a2091567`; inserting the commit and tag
  values produced containing commit
  `e85e97b997ff0e8facb2828c677a4ce07b13ea78`, while the tag over that new
  commit became `3eb5dcc719b10e41478af4176ba9f8b1f902c935`. Both constructed
  fixed-point comparisons were `no`. Committing the record changes the commit
  value; tagging that new commit changes the tag-object value. Reordering the
  same operations cannot break either dependency, so candidate evidence solves
  the hosted-evidence ordering problem but not these self-referential fields.
- **Early-close control — PASS.** A disposable full-history clone with every
  v0.22 box checked and a syntactically complete `v0.15.6` closing record,
  while no such tag existed, exited 1 with this exact output:

  ```
  cycle-check: ERROR: docs/cycles/TASKS-v0.22-EXECUTION.md: annotated tag 'v0.15.6' does not resolve to recorded tag object f2bfeacc1dc8207841430e3827e7babed5605b47
  cycle-check: ERROR: docs/cycles/TASKS-v0.22-EXECUTION.md: release 'v0.15.6' does not dereference to recorded commit b9f617664578a3bb5e29892c512a3dda8e991c24
  cycle-check: ERROR: STATE.md: publication verification unavailable: annotated tag ref 'v0.15.6' cannot be resolved
  cycle-check: FAIL (3 defect(s))
  ```

  This is correct unavailable-input behavior. Step 2's selected design must
  avoid requiring a not-yet-created local tag to validate an early close.
- **G2 — CONFIRMED and classified LOCAL-ONLY for both tags.** Exhaustive
  inspection covered **45** local refs, **803** reflog entries, all **40**
  remote refs, and the recorded objects. Local `refs/tags/v0.8.0` points at
  annotated tag object
  `314c1dd914a3d8e9193445874a419ed762581e6e`, whose payload targets existing
  commit `bfc8c5af85734583f966ee70d2ec521155432205`. Local
  `refs/tags/v0.10.2` points at annotated tag object
  `d821f8b2eb6f39fe4a7d06a88cd61de771c7b0ba`, whose payload targets existing
  commit `7d127abac0b993c9e98294ee1c03ff01153de9d0`. Both tag objects have type
  `tag`; both targets have type `commit`; the two release commits appear in
  local `main`'s reflog. Remote enumeration found neither tag name nor any of
  the four recorded object ids. No ref or closed runbook changed.
- **G3 — REFUTED.** The omission hypothesis is false. Contributor-facing
  `ARCHITECTURE.md` already states that the review-export budget is an
  executable **operator-local contract**, that `./run export-check` derives the
  tracked set from `git ls-files`, and that the check is intentionally absent
  from local/hosted CI because it writes a multi-megabyte export and `npx` may
  fetch its pinned toolchain. `AGENTS.md` carries both measured operating rules
  and points contributors at the command. `.github/workflows/ci.yml` contains
  no `export-check`, `export_check`, or Repomix invocation, as documented.
- **G4 — CONFIRMED as an unexamined default.** The manifest is **119,353
  bytes/characters**, not the draft's 119,354, and contains **206** pins.
  Release-tag snapshots measure total pins **161 → 176 → 191 → 206** for
  v0.15.2 through v0.15.5, exactly **+15 per cycle**; the draft's 159 first
  value was v0.15.2's evidence-only subtotal, excluding the two authorization
  pins. `/usr/bin/time -p ./run verify-artifacts` at 206 pins measured
  **0.10 s real / 0.05 s user / 0.04 s sys**. The repository states
  `immutable_evidence` and append-only admission, which explains why existing
  evidence cannot be silently rewritten, but it contains no dated acceptance
  of unbounded pin growth, no retention bound, and no trigger for revisiting
  the full re-hash cost. Step 4 therefore must give this behavior a disposition.
- **G5 — CONFIRMED.** The record repeatedly calls the
  `StarletteDeprecationWarning` and hosted GitHub Actions Node-runtime
  deprecation annotation third-party and non-blocking. Neither warning has a
  named work trigger or a permanent-acceptance decision. “Non-blocking” is the
  repeated absence of a disposition, so Step 4 must disposition each warning.
- **Final identity and integrity:** local and remote annotated `v0.15.5` object
  `f2bfeacc1dc8207841430e3827e7babed5605b47` both peel to release commit
  `b7c4b10eb506923e3ea854a32d1dc3f4c83b0eaa`; remote `main` remains that
  commit. Manifest schema-v2 validation and final `verify-artifacts` pass all
  **206/206** pins and protected databases **2/2**. Final standalone golden
  passes **11/11**, delta **0**.

---

## Cycle checklist

- [x] **E0** — entering matrix with both interpreters; G1 established as a field
  constraint with the no-permutation demonstration; early-close message recorded
  verbatim; G2 classified per tag with evidence and no ref touched; G3 confirmed
  or refuted; G4 measured with growth rate and verify cost; G5 answered from the
  record; `STATE.md` unedited
- [ ] **CLOSE-FIELDS** — exactly one option chosen and dated with its coverage
  cost in the operator's terms; fail-before captured; every changed rule has a
  detected planted failure; `AGENTS.md`'s R-CLOSE contract matches the checker;
  no published tree repaired
- [ ] **TAG-IDENTITY** — per-tag decision with its claim stated; retraction count
  addressed; `--skip-local-tag-verification` recorded or given a trigger and not
  removed; no ref touched by 🤖
- [ ] **RESIDUALS** — G3, G4, G5 each carry one dated disposition or are deleted
  as refuted; G4's acceptance states growth rate and verify cost; all appear in
  the residual table
- [ ] **RE-MEASURE** — hosted run pinned on a neutral branch; counts equal local
  at the same commit; candidate run id recorded as citable evidence if required
- [ ] **R-CLOSE** — Step 2's procedure followed rather than the habitual one;
  publication decided on a trigger with no-release named as legitimate; G1
  recorded as the fourth instance and the v0.21 misdiagnosis corrected; G2's
  classification recorded; all open items still open

---

## Standing prohibitions

- **Do not create, move, or delete any git ref in Steps 1–4.** Ref changes for
  `v0.8.0` or `v0.10.2` are operator actions requiring their own authorization,
  and they must never be folded into a classification task.
- **Do not edit a closed runbook's dated record** to resolve G2. The banner and
  retraction machinery exists precisely for this.
- **Do not remove `--skip-local-tag-verification` from `ci.yml` in this cycle.**
  Removing it before G2 is resolved turns a historical finding into a red
  published head.
- **Do not repair the published v0.15.5 tree**, or any earlier one. Step 2's
  choice applies from the next publication forward.
- **Do not choose a CLOSE-FIELDS option because it is the smallest diff.** Record
  why its coverage cost is acceptable.
- **Do not add a rule without an R12 planted-failure control.** That discipline
  is what v0.21 bought; adding an unguarded rule spends it.
- **Do not modify any crate under `crates/` or `apps/`.** This cycle is tooling
  and documentation. A source change is a scope violation.
- **Do not touch the robots matcher, the negative TTL, the politeness limiter, or
  the crawl-delay ratchet.**
- **Do not add a configured source.**
- **Do not amend, rebase, or squash `188055a`.**
- **Do not claim any task closes or narrows A4**, the L1 residual, the R3/R4
  open-bottom limitations, T7, or NEGATIVE-CACHE Decision B.
- **Do not batch `STATE.md` / `PROGRESS-v0.22.md` updates or combine two tasks in
  one commit.**
- If any Step's Objective, Acceptance criteria, or "Done when" is amended after
  this file is first committed, name the amendment in a dated
  `## Runbook amendments` block in the same commit.

---

## Provenance of this draft

Every gate above was read out of the repomix export of the v0.15.5 tree on
2026-07-29 by path and line, and each is written as a hypothesis for E0 to
confirm or refute.

**G1's field constraint is measured, not inferred.** `newest_closed_release`
requires `RELEASE_COMMIT_RE` — `^- \*\*Release commit:\*\* \`<40 hex>\`$` — and
`TAG_OBJECT_RE` — `^- \*\*Annotated tag object:\*\* \`<40 hex>\`$` — inside the
cycle-closing section. Both name objects that do not exist until
after the text is written. E0 should reproduce the demonstration rather than take
this on faith, but the expected result is known.

**The v0.21 decision record's diagnosis of G3 was incomplete, and this runbook
is the correction.** That record describes the v0.22 subject as "a true two-phase
close: close on already-existing candidate hosted evidence." Closing on candidate
evidence is necessary — it removes the dependency on a run that cannot exist
before the push — but it is not sufficient, because the `Annotated tag object`
field remains unknowable regardless of which evidence is cited. Option C is the
completed version of that proposal; Options A and B are the alternatives it
should be weighed against.

**v0.21's own work is sound and is not reopened.** R12 invokes the real entry
point over nine planted cases with seven independent registry mutations, all
detected; both immutable assertions are total requirements so a zero-match header
is an error; the narrow ``[^`\n]`` boundary was preserved with its reason rather
than widened; G5's masking and G6's proximity window were each recorded as
decisions; and G4 was accepted with a date. Codex's production review reproduces
against the source at every seam it names.
