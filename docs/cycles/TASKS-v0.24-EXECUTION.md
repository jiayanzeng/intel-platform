# TASKS-v0.24-EXECUTION.md — the population, not the number

v0.23 closed and v0.15.7 published atomically. Release parent
`8bb6a714…`, closing commit and tag target `e7715fb9…`, annotated object
`b579c2c1…`, published-head run `30462710258` green on all seven executable
jobs. Node 24 actions landed, the toolchain is immutably pinned, release
mechanics are single-sourced, and active-cycle scope is executable for the first
time. **The post-push audit then did what it exists to do and found that one of
the cycle's own recorded measurements was false.**

Hosted shell lanes reported **274 passed / 1 skipped**, not the **275/275**
asserted in the RE-MEASURE entry and carried into the closed execution record.
The skipped test is `test_on_site_production_measurements_match_committed_receipt`,
whose `skipif` requires `data/core.db`, `data/live-smoke.db`, and a built
`target/debug/cored` — all deliberately absent from a clean hosted checkout. The
release is valid; the count claim was not.

**The cause is a criterion I wrote, and it has been unsatisfiable for three
cycles.** v0.19's RE-MEASURE said: *where a hosted count differs from local by a
declared on-site-only skip, state the skip.* I dropped that clause when drafting
v0.21's Step 6, and v0.21, v0.22, and v0.23 each carry the bare acceptance
*every count read from the log and equal to local at that commit*. The skip is
structural and never went away, so from v0.21 the criterion had no satisfying
assignment for the shell lane. **v0.22's executor reported the discrepancy
anyway — "265 passed + 1 declared on-site" of 266. v0.23's reconciled the number
to the criterion.** Two cycles, one criterion, opposite resolutions, and nothing
chose between them. That inconsistency is the evidence.

**And the published v0.15.7 tree carries the false claim.** The correction lives
in post-closing audit commit `ed54112a…`, which is unpushed per the cycle-ending
rhythm. A reader of the tag sees `275/275`.

This cycle does three things, and a fourth only if the third turns out small:

1. **makes the environment-conditional test population explicit** — it is
   currently one test, marked only by a bare `skipif`, in a suite invoked as
   `pytest -q` with no machine-readable output;
2. **replaces the transcribed number with a derived comparison** of equivalent
   populations, and registers it as a rule with planted failures;
3. **bounds the false-count class historically** and corrects the record forward
   for every cycle it reaches;
4. **opens the second-publisher compliance review** — the one blocked item whose
   trigger is under operator control — **only if step 3's bounding is small.**

**The public `/v1/*` JSON bodies, the SQLite schema, the robots matcher, the
negative TTL, the politeness limiter, and the golden regression's 11 invariants
are unchanged. Golden stays 11/11 byte-identical through every task. No source
under `crates/`, `apps/`, or `shell/intel_shell/` is modified.**

---

## Declared scope

```yaml
scope_version: 1
disposition_intent: release
allow:
  - shell/tests/**
  - shell/pytest.ini
  - tools/test_population.py
  - tools/cycle_check.py
  - tools/invariant_scan.py
  - config/invariant-rules.json
  - config/protected-artifacts.json
  - .github/workflows/ci.yml
  - run
  - observations/**
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

`run` and `.github/workflows/ci.yml` are in `allow` because Step 2 changes how
the shell suite is invoked; `run` is a pinned authorization surface, so its pin
moves and Step 2 records the before/after hashes. `shell/intel_shell/app.py`
remains in `release_authorities` and matched by `forbid`, resolved as v0.23
established: **authorities win at R-CLOSE for the version literal only, and the
`STATE.md` diff classification covers the rest.** The relocation of that literal
into `__init__.py` remains a recorded forward option and is **not** taken here.

---

## Entering state (asserted, not yet verified)

**Every sentence here is a hypothesis until Step 1 (E0) measures it.**

- `v0.15.7` is published. Release parent `8bb6a71446b043b10ce16077499fdc07abb91b98`,
  closing commit `e7715fb97b86b91a2a58bc7b73bf99308c2aae9b`, annotated tag
  object `b579c2c18e4eeb549617ea20a9175b0c26dc621d`. v0.23 is closed. **None of
  this is reopened.** Candidate run `30459746825` is the closing evidence;
  `30462710258` is dated forward confirmation.
- Local `main` is one commit ahead at post-closing audit `ed54112a…`, unpushed,
  carrying the POST-PUSH correction.
- Protected pins are **236**. Golden is **11/11**. Local CI is **20/20** with
  **133** workspace tests, **55** net tests (**29 + 26**), `invariant-scan`
  **12/12 rules / 38 controls**, `checklist-audit` **184/184** with **three**
  retractions.
- **Local** shell lanes are **275/275** on Python 3.11 and 3.12; **hosted** lanes
  are **274 passed / 1 skipped**. The difference is one declared `skipif`.
- Exactly **one** `@pytest.mark.skipif` exists across `shell/tests/**`, in
  `test_deferred_audit.py`. No `pytest.ini`, `pyproject.toml`, `setup.cfg`, or
  `conftest.py` exists. `ci_pytest()` invokes `py -m pytest shell/tests -q` and
  captures nothing machine-readable.
- A4, the editable-L1 controller residual, the R3/R4 open-bottom deny-lists, the
  active-runbook measured-value heuristic, T7 robots single-flight, and
  NEGATIVE-CACHE Decision B remain open. L2 remains scheduled. `v0.8.0` and
  `v0.10.2` remain local-only under A/A/E, with
  `--skip-local-tag-verification` retained under its removal trigger.
  **No step in this file closes or narrows any of them.**

---

## Drafted gates

| Gate | Where | Hypothesis |
|---|---|---|
| **G1** [P1] | `shell/tests/test_deferred_audit.py`; `run` `ci_pytest()` | **The environment-conditional population is implicit and the count is transcribed.** One `skipif` carries the whole difference between hosted and local, it is identifiable only by reading the decorator, and `pytest -q` emits nothing a tool can compare. Confirm the count is one, confirm no pytest config exists, and confirm no tool consumes the suite's output. |
| **G2** [P1] | RE-MEASURE acceptance in v0.21–v0.23 versus v0.19 | **The criterion has had no satisfying assignment since v0.21.** v0.19 carried the on-site-skip clause; v0.21, v0.22, and v0.23 carry bare equality. Reproduce the clause's presence and absence by grep across the closed runbooks, and record that v0.22 resolved the conflict by reporting the skip while v0.23 resolved it by reconciling the number. **The divergence is the finding, not either record.** |
| **G3** [P1] | hosted logs from the first cycle in which the `skipif` test existed | **The false-count class may reach further back than v0.23.** v0.22 recorded "265 passed + 1 declared on-site" of 266. v0.21 recorded "258/258" and v0.20 "255/255" with no skip stated. **Determine when the conditional test was introduced, then read the hosted log for every RE-MEASURE and POST-PUSH run from that cycle forward.** Report the exact set of records whose hosted count omitted a skip. **Bound it; do not estimate it, and do not assume the class is larger than measurement shows.** |
| **G4** [P2] | `config/checklist-retractions.json`; the affected records | **Whether this moves the retraction count is an open question, not a foregone one.** It has stood at three. Determine whether an incorrect measurement inside an append-only progress entry meets this project's existing retraction criterion, or whether a dated superseding entry — which v0.23's POST-PUSH already used — is the established instrument. **State the criterion before applying it.** |
| **G5** [P2] | v0.23's SCOPE-DECLARED record; this file's scope block | **The scope rule's first real exercise is this cycle.** v0.23's block was validated retroactively by the rule that came after it. This block is the first written against a live rule. Confirm it passes at activation, and record whether the static sub-rule fires as designed on a `release` intent. |
| **G6** [P3] | the "1 warning" in both lanes | **A warning is reported every cycle and named in none.** Both hosted and local lanes report one warning. Identify it, and state whether it is the accepted `StarletteDeprecationWarning` under its existing trigger or something else. **A refuted G6 is deleted, not worked around.** |

---

## How to run this file

Execute top to bottom, one task and one commit at a time. Follow `AGENTS.md §5`
after **every** task. Implementation and audit-record commits stay separate.

- **🤖 = Codex executes and self-verifies end to end** — no publication, no push
  to `main`, no ref creation or deletion **in the working repository**.
- **🧑 = exactly one named operator action or decision.**

**Disposable clones.** State provenance every time — local or remote — and
confirm afterward that no working-repository ref changed. Refs inside a
disposable clone are not repository refs.

**Interpretive rules, binding throughout.** An exit code of 0 from a construction
the checker never examined is **not measured**, never *does not reject*. And a
measurement that disagrees with an acceptance criterion is **reported as
measured**; the criterion is what gets corrected. **v0.23's shell count is the
live example of what happens when that ordering inverts.**

**Dependency gates.** Step 2 precedes Step 3. Step 3 precedes Step 4, because a
derived comparison must exist before the historical record is corrected against
it. **Step 5 is conditional: it runs only if Step 4's affected-record set is
two or fewer.** Step 6 is blocked by every preceding implementation step; Step 7
by Step 6.

### Cycle activation (before E0)

In a separate preparatory implementation/audit pair: confirm the worktree is
clean and record the measured refs **without asserting a literal `origin/main`
hash in `STATE.md`'s header**. Commit **only** this runbook at
`docs/cycles/TASKS-v0.24-EXECUTION.md` — **including its `## Declared scope`
block, which the live rule now validates** — the `AGENTS.md` header moving the
active declaration from v0.23 to v0.24, and a new
`docs/cycles/PROGRESS-v0.24.md`. **Local `main` already carries the unpushed
audit `ed54112a…`; activation sits on top of it and does not amend, rebase, or
squash it.**

### Global definition of done

Protected hashes exact; all **236** pins match until Step 6 adds more; golden
**11/11 byte-identical**; `./run version-check` green; zero rustc warnings on
offline and net builds; all Rust tests green; all shell tests green under Python
3.11 **and** 3.12; clippy, fmt, ShellCheck, floor byte-compilation, and locked
Rust 1.78 green.

**Shell acceptance changes at Step 3.** Until then, record shell results as
**collected / passed / skipped** with every skip named — not as `N/N`. **Do not
write a bare equality claim anywhere in this cycle.**

---

## Deferred means deferred

Each row carries a dated measured observation; per v0.23's rule an observation
may be a dated negative statement where the condition is an event.

| Deferred item | Unchanged trigger | Measured 2026-07-29 | v0.24 action |
|---|---|---|---|
| T7 robots single-flight | a second concurrent harvester | one configured harvester; ingest is sequential | none |
| NEGATIVE-CACHE Decision B | a live transient robots outage for an admitted publisher while a usable last-known-good policy exists, plus operator authorization | no such outage observed | none |
| Postgres / pgvector / multi-host seam | unchanged | single writer, single host | none |
| A4 untrusted-shell boundary | a third-party/untrusted shell, or any claim HC1 is invariant under shell replacement | one first-party shell; no such claim made | none |
| L2 forced-command wrapper | an operator server session | no operator server session has occurred | none — remains scheduled |
| R3/R4 open-bottom coverage | a spelling outside registered vocabulary | none observed | none |
| Second configured publisher | a completed compliance review per publisher, then a separate admission decision | no review completed | **Step 5 opens the review only; it does not admit a source** |
| `v0.8.0` / `v0.10.2` publication | operator-authorized push of both exact annotated objects | not authorized | none — **no historical ref touched** |
| `--skip-local-tag-verification` removal | both historical tags published plus a passing hosted full-history `cycle-check` without the flag | tags unpublished | none — **the flag stays** |
| Manifest retention/indexing | 1 MiB manifest, or two consecutive `verify-artifacts` runs ≥1.00 s | re-measure at E0 | re-measure only |
| Version literal in `app.py` | a cycle whose declared scope permits shell source changes | literal present in production source | none — recorded, not acted on |

---

## Step 1 · E0 — Rebuild the entering state and settle six gates 🤖

**Objective.** Confirm HEAD is green, bound the false-count class, and settle
G1–G6.

**Gate.** Read-only repository, object, disposable-clone, hosted-log, and local
execution measurements plus `PROGRESS-v0.24.md` and this runbook's status
records only. **No ref created, moved, or deleted in the working repository.**
**`STATE.md`, `run`, and `ci.yml` are not edited in this step.**

**Steps.**

1. Run the full entering matrix and standalone `./run golden`, plus
   `verify-artifacts`, `cycle-check`, `checklist-audit`, `progress-check`,
   `version-check`, `invariant-scan`, and `export-check`. **Record shell results
   as collected / passed / skipped with the skip named, in both lanes and in
   both interpreters.**
2. **Confirm G1.** Count `@pytest.mark.skipif` and `pytest.skip(` across
   `shell/tests/**`; confirm the absence of any pytest configuration file; and
   show that no tool reads the suite's output.
3. **Confirm G2 by grep across the closed runbooks.** Record the on-site-skip
   clause present in v0.19's RE-MEASURE and absent from v0.21, v0.22, and v0.23,
   and record v0.22's and v0.23's opposite resolutions side by side.
4. **Bound G3.** Determine the first cycle in which
   `test_on_site_production_measurements_match_committed_receipt` existed —
   `git log --diff-filter=A` on its introducing commit is sufficient. From that
   cycle forward, read the **hosted log** of every RE-MEASURE and POST-PUSH run
   recorded in `PROGRESS-v0.*.md` and compare its shell summary against the
   record's claim. **Report the exact affected set. If the answer is one record,
   say one.** Where a hosted log has aged out of retention, say so rather than
   inferring.
5. **State G4's criterion before answering it.** Read
   `config/checklist-retractions.json` and whatever defines a retraction, state
   the criterion, and only then say whether an incorrect measurement inside an
   append-only entry meets it — or whether v0.23's dated superseding entry is
   the established instrument.
6. **Confirm G5.** Record whether this runbook's scope block passed at
   activation and whether the static sub-rule fired on the `release` intent.
7. **Identify G6's warning by name** in both lanes, or refute the gate.
8. Re-measure the manifest byte size and `verify-artifacts` wall time rather than
   copying v0.23's figures.
9. Re-verify the published `v0.15.7` objects — the peeled tag is the closing
   commit and its first parent is the release parent — and all **236** pins
   unchanged.

**Acceptance criteria.** Entering matrix with both interpreters, shell recorded
as collected/passed/skipped with the skip named · G1 confirmed with counts and
the absence of pytest config · G2's clause presence/absence and the two opposite
resolutions recorded · **G3 bounded to an exact affected set**, with any
retention gap stated rather than inferred · G4's criterion stated before its
answer · G5 recorded · G6 named or refuted · manifest and verify time freshly
measured · published objects and 236 pins re-verified · no working-repository ref
changed · `STATE.md`, `run`, `ci.yml` unedited · golden 11/11.

**Done when** every drafted gate is CONFIRMED or REFUTED with command output.

---

## Step 2 · POPULATION-EXPLICIT (G1) — Name the conditional set 🤖

**Objective.** Make the environment-conditional population declarable,
enumerable, and machine-readable.

**Gate.** `shell/pytest.ini`, `shell/tests/**`, `run`, `.github/workflows/ci.yml`,
`config/protected-artifacts.json` for `run`'s pin, and status records. **Blocked
on E0 confirming G1.** No `shell/intel_shell/**`, crate, dependency, schema,
protected-database, or public surface changes.

**Steps.**

1. Add a pytest configuration registering an `on_site` marker, and apply it to
   the one conditional test **alongside** its existing `skipif` — the marker
   declares membership, the `skipif` decides execution. **Do not replace the
   `skipif` with the marker**; the condition it encodes is what makes the skip
   correct, and losing it would turn a declared skip into an unexplained one.
2. Make the population enumerable: `pytest --collect-only -m on_site` must list
   exactly the conditional set, and its complement must be environment-invariant.
   **Record the enumeration.**
3. Emit a machine-readable summary from `ci_pytest()` — collected, passed,
   failed, and every skip with its node id and reason — in both the local and
   hosted invocations. **Both lanes must emit the same format**, or the
   comparison Step 3 builds has nothing to compare.
4. Confirm `run`'s dispatch, authorization policy, and model-profile functions
   are otherwise unchanged, and record the pin's before/after hashes and byte
   sizes.
5. **Do not change which tests run anywhere.** Collected and passed counts in
   each environment must be identical before and after this step, and the record
   must show that.

**Acceptance criteria.** Marker registered and applied without removing the
`skipif` · `--collect-only -m on_site` enumerates exactly the conditional set,
recorded · machine-readable summary emitted in identical format by both lanes ·
collected and passed counts unchanged in every environment, shown · `run` pin
updated with before/after hashes · manifest validation and all pins exact ·
golden 11/11.

---

## Step 3 · POPULATION-COMPARE (G2) — Compare populations, not integers 🤖

**Objective.** Replace the transcribed equality claim with a derived comparison
of equivalent populations, and make the criterion satisfiable.

**Gate.** `tools/test_population.py`, `tools/cycle_check.py` or
`tools/invariant_scan.py` and their tests, `config/invariant-rules.json`,
`AGENTS.md`'s RE-MEASURE contract, `run`, and status records. **Blocked on
Step 2.** No source, crate, dependency, schema, protected-database, or public
surface changes.

**Steps.**

1. Build the comparator. Given a local and a hosted summary it asserts:
   - **collected is equal** in both environments;
   - **local passed equals hosted passed plus hosted `on_site` skips**;
   - **every skip is named with its node id and declared reason**, and every
     skipped node carries the `on_site` marker.
   A skip that is *not* marked `on_site` is a **failure**, not a difference —
   that is the whole point of making membership explicit.
2. **Rewrite the RE-MEASURE acceptance in `AGENTS.md`** from bare equality to
   population equivalence, and **state that the number in any record must be the
   comparator's output rather than a figure read from a log by hand.** A
   transcribed number is what made v0.23's claim false.
3. **Fail-before, three ways:** a hosted summary with an unmarked skip; a
   collected-count mismatch; and a skip whose reason string is absent. Capture
   each rejection.
4. **Replay v0.23 through the comparator** using its recorded hosted and local
   figures, and show it rejects the `275/275` claim and accepts
   `274 passed + 1 on_site skip`. **This is the criterion proving it would have
   caught the defect that motivated it.**
5. Register the rule as an R12 planted-failure mutation and report the new rule
   and control counts in `STATE.md`, `PROGRESS-v0.24.md`, and the pending closing
   record.
6. **Do not make the comparator tolerant of unnamed differences.** A rule that
   accepts any discrepancy it cannot classify is the vacuous family v0.21 closed.

**Acceptance criteria.** Comparator asserts all three properties · unmarked skip
treated as failure · `AGENTS.md` RE-MEASURE acceptance rewritten to population
equivalence with derived-number requirement · three fail-befores captured ·
v0.23's figures replayed with the false claim rejected and the true one accepted ·
new rule has a detected planted failure · counts in three places · golden 11/11.

**Done when** the acceptance criterion can be met by a correct measurement.

---

## Step 4 · HISTORY-BOUND (G3, G4) — Correct forward, exactly as far as measured 🤖🧑

**Objective.** Correct the record for every affected cycle E0 identified, and no
further.

**Gate.** 🧑 **One operator decision, at step 3.** Scope is `STATE.md`, dated
forward appends, and — only if the operator chooses it —
`config/checklist-retractions.json`. **Blocked on E0's bounded set and on
Step 3.** **No closed runbook's dated record and no historical `PROGRESS` entry
is edited.** No source, tool-logic, workflow, dependency, schema, or public
surface changes.

**Steps.**

1. For each record in E0's affected set, write a **dated superseding forward
   entry** naming the record, its claimed figure, the measured hosted figure, and
   the hosted run id. **Use the instrument v0.23's POST-PUSH already used**; do
   not invent a second correction mechanism.
2. **State the scope of the class in one sentence**, with its measured size.
   **Do not describe it as systemic if it reaches one record, and do not describe
   it as isolated if it reaches four.** The number decides the adjective.
3. **🧑 Decide G4.** Applying E0's stated criterion, either these corrections are
   retractions and the count moves off three, or a dated superseding entry is the
   correct instrument and the count stands. **Record the decision with the
   criterion it applied**, so the next occurrence is not re-litigated.
4. **Record what the class did and did not affect.** No published runtime
   changed; no signed identity changed; no protected pin changed; every green job
   conclusion was real. **The defect is in the recorded measurement, and saying
   so precisely is what keeps it from being read as either cosmetic or as a
   release defect.**
5. Attribute the criterion's origin: it was authored into v0.21's Step 6 by
   dropping v0.19's clause, and it is the **fifth** author-side rule with no
   satisfying assignment. **Measure that count against v0.23's established
   population criterion rather than asserting it.**

**Acceptance criteria.** One dated superseding entry per affected record, each
naming claimed and measured figures and the hosted run id · class size stated
with an adjective the number supports · G4 decided with its criterion recorded ·
scope of non-impact stated precisely · fifth-instance count measured against
v0.23's criterion, not asserted · no closed runbook or historical entry edited ·
golden 11/11.

---

## Step 5 · PUBLISHER-REVIEW — Open the review, admit nothing 🧑🤖

**Conditional. This step runs only if Step 4's affected set is two records or
fewer. If it is larger, delete this step from the cycle and record the deferral
with its measurement.** A correction cycle that has grown does not also get a
product step.

**Objective.** Produce the compliance review that has gated a second publisher
for eight cycles — without adding one.

**Gate.** 🧑 **Operator judgement on licensing and terms is not delegable.**
Scope is `observations/v0.24/**` and status records. **No `config/core.json`
change, no configured source added, no crate, tool, workflow, or schema change.**
The admission decision is **explicitly deferred to v0.25**.

**Steps.**

1. 🧑 Name one candidate publisher and the reason it is the candidate.
2. Fetch its `robots.txt` **through the shipped matcher**, exactly as v0.18 did
   for `arxiv-cs`, and record the policy bytes, their hash, the derived verdict
   for the intended path, and the crawler identity used. **If the verdict
   disallows, that is a completed review with a negative outcome, not a failure.**
3. Record the publisher's stated licence and terms of use verbatim by reference —
   **URL and date read, no paraphrase standing in for the text.**
4. 🧑 Produce the reviewed recommendation: admissible, inadmissible, or
   undetermined-pending-named-evidence. **An honest undetermined is a complete
   outcome.**
5. **Record what this review does not establish**: nothing about the multi-origin
   behaviour of the origin-keyed robots cache or the per-host limiter, which have
   never seen two origins and will not until a source is admitted.
6. Update the deferral row: the trigger for admission becomes "a completed review
   with an admissible recommendation, plus a separate operator admission
   decision."

**Acceptance criteria.** One candidate named with its reason · policy fetched
through the shipped matcher with bytes, hash, verdict, and identity recorded ·
licence and terms cited by URL and date · one recommendation recorded, including
undetermined as a complete outcome · non-establishment stated explicitly · no
source added and `config/core.json` unchanged · deferral row updated · golden
11/11.

---

## Step 6 · RE-MEASURE 🤖🧑

**Objective.** Produce release-grade hosted evidence for the v0.24 candidate,
**under the new population comparison**.

**Gate.** 🧑 **One narrow authorization: a non-`main` branch push.** Remote
mutation is limited to the exact candidate branch and its authenticated hosted
evidence dispatch. Repository admission is limited to that run's signed
receipt/bundle pairs, the release-posture deferred-audit report,
`config/protected-artifacts.json`, and status records. No tag, `main` advance,
publication, source, public surface, dependency, lockfile, schema, or protected
database changes.

**Steps.**

1. Push the candidate to a **neutral branch name that does not prejudge Step 7's
   disposition.**
2. **Read the remote branch's `ci.yml` and confirm its blob equals the local one
   before dispatching.**
3. Dispatch with `publish_evidence: true` and `audit_sha` set to the candidate.
4. **Run the comparator, and cite its output.** Do not transcribe a count from
   the log into any record. Every non-shell count is still read from the log and
   compared at the same commit; the shell lanes are compared as populations.
5. Record the hosted `invariant-scan` rule and control counts; Step 3 adds a rule
   and it must be detected here.
6. **Record this run id prominently** — under the tagged close it is the evidence
   the closing record cites.
7. Commit the signed receipt/bundle set, re-run `./run verify-artifacts` and
   `./run evidence-report`, and record the new pin count in `STATE.md`,
   `PROGRESS-v0.24.md`, and the pending closing record.
8. Run `./run audit-deferred` in release posture with attestations required.

**Acceptance criteria.** Hosted run pinned on a neutral branch · remote `ci.yml`
blob confirmed before dispatch · shell lanes compared by the comparator with its
output cited, never transcribed · every other count read from the log and equal
at that commit · hosted `invariant-scan` counts recorded and increased by Step 3 ·
run id recorded as citable closing evidence · signed set committed and
re-derived · pin count in three places · `origin/main` unchanged, no tag · golden
11/11.

---

## Step 7 · R-CLOSE 🧑🤖

**Objective.** Close the cycle under the tagged-close protocol.

**Gate.** Steps 1–6 complete and boxed, with Step 5 either complete or recorded
as conditionally deferred. Worktree clean. **🧑 One operator decision:
publication.**

**Steps.**

1. **Follow the Option C tagged-close protocol as `AGENTS.md` states it**:
   release parent `R` untagged, closing child `C` naming `R` with no tag-object
   field, tag over `C`, atomic push, post-push result in a dated forward append.
2. Re-run the complete definition of done at the release parent and capture it.
3. Record the version choice and the trigger that fired.
4. **Name the publication trigger. One is visible at entry: the published
   v0.15.7 tree carries a false recorded count, because the correction lives in
   an unpushed commit.** State that as the trigger rather than inheriting the
   patch default.
5. Record evidence candidate and release parent as **separate named fields**.
6. **State the release disposition as of a date**, in the form
   `cycle_check.py`'s validator reads.
7. **Record the class's measured size and the adjective it supports.**
8. **Record the fifth-instance count as measured**, against the population
   criterion v0.23 established — and record that this instance is the first whose
   consequence was a false number in a published record rather than an unmeetable
   criterion.
9. **Record Step 5's outcome or its conditional deferral with the measurement
   that caused it.**
10. Classify every diff path exactly once in `STATE.md`; update `CHANGELOG.md`,
    `README.md`, and the release authorities.
11. Reconcile `ARCHITECTURE.md`. **A4, the L1 controller residual, the R3/R4
    open-bottom limitations, the measured-value heuristic, T7, and
    NEGATIVE-CACHE Decision B must all still read as open**, the A/A/E tag
    disposition unchanged, and the `app.py` relocation still a forward option.
12. Record the post-push hosted result as a **dated forward append**. Under the
    tagged close it is confirmation, not the closing event; **a red post-push run
    is a finding for v0.25 and does not invalidate the close.**
13. **Carry the one-publisher fact forward.** If Step 5 ran, `arxiv-cs` is still
    the sole *configured* publisher and the review is a document, not an
    admission.

---

## Cycle checklist

- [ ] **E0** — entering matrix with shell recorded as collected/passed/skipped;
  G1 confirmed; G2's clause presence/absence and the two opposite resolutions
  recorded; **G3 bounded to an exact set** with retention gaps stated; G4's
  criterion stated before its answer; G5 recorded; G6 named or refuted; manifest
  and verify time freshly measured
- [ ] **POPULATION-EXPLICIT** — marker registered alongside the `skipif`, not
  replacing it; `--collect-only -m on_site` enumeration recorded; identical
  machine-readable summary from both lanes; no change to which tests run, shown;
  `run` pin updated
- [ ] **POPULATION-COMPARE** — comparator asserts collected equality, passed +
  marked-skip equivalence, and named reasons; unmarked skip is a failure; three
  fail-befores; **v0.23's figures replayed with the false claim rejected**;
  `AGENTS.md` acceptance rewritten; planted failure detected
- [ ] **HISTORY-BOUND** — one dated superseding entry per affected record; class
  size stated with a supported adjective; G4 decided with its criterion; scope of
  non-impact stated; fifth-instance count measured; no closed record edited
- [ ] **PUBLISHER-REVIEW** — complete, or deleted with the measurement that made
  it conditional. Candidate named; policy fetched through the shipped matcher;
  licence cited by URL and date; one recommendation; no source added
- [ ] **RE-MEASURE** — hosted run on a neutral branch; comparator output cited,
  never transcribed; other counts equal at the same commit; run id recorded
- [ ] **R-CLOSE** — tagged close followed; publication trigger named as the
  published false count; class size and fifth-instance count recorded as
  measured; Step 5's outcome or deferral recorded; post-push in a dated forward
  append

---

## Standing prohibitions

- **Do not write a bare `N/N` shell count anywhere in this cycle.** Record
  collected, passed, and skipped with every skip named, from E0 onward.
- **Do not transcribe a count from a log into a record once the comparator
  exists.** Cite its output.
- **Do not replace the `skipif` with the marker.** The condition is what makes
  the skip correct.
- **Do not make the comparator tolerant of a difference it cannot classify.**
- **Do not change which tests run in any environment.**
- **Do not describe the false-count class with an adjective the measured size
  does not support**, in either direction.
- **Do not edit a closed runbook's dated record or a historical `PROGRESS`
  entry.** Correct forward with dated superseding entries.
- **Do not run Step 5 if Step 4's affected set exceeds two records.**
- **Do not add a configured source, and do not modify `config/core.json`**, whatever
  Step 5's recommendation says. Admission is a separate v0.25 decision.
- **Do not modify `shell/intel_shell/**`, `crates/**`, or `apps/**` source.** The
  release authorities are in scope at R-CLOSE; source is not.
- **Do not relocate the `app.py` version literal.** It remains a forward option.
- **Do not create, move, or delete any ref in the working repository**, including
  `v0.8.0` and `v0.10.2`; refs inside a disposable clone are not repository refs.
- **Do not remove `--skip-local-tag-verification`.**
- **Do not add a rule without an R12 planted-failure control**, and do not add a
  rule that evaluates a condition it cannot observe.
- **Do not write a rule with no satisfying assignment for a case it governs.**
  That is the defect this cycle exists to correct.
- **Do not touch the robots matcher, the negative TTL, the politeness limiter, or
  the crawl-delay ratchet.**
- **Do not amend, rebase, or squash `ed54112a…`.**
- **Do not claim any task closes or narrows A4**, the L1 residual, the R3/R4
  open-bottom limitations, T7, or NEGATIVE-CACHE Decision B.
- **Do not batch `STATE.md` / `PROGRESS-v0.24.md` updates or combine two tasks in
  one commit.**
- If any Step's Objective, Acceptance criteria, or "Done when" is amended after
  this file is committed at activation, name the amendment in a dated
  `## Runbook amendments` block in the same commit.

---

## Provenance of this draft

Every gate was read out of the repomix export of the v0.15.7 tree on 2026-07-29
by path, and each is a hypothesis for E0 to confirm or refute.

**Four claims here were verified against the export rather than reasoned to.**
`shell/tests/**` contains exactly **one** `@pytest.mark.skipif` and zero
`pytest.skip(` calls. No `pytest.ini`, `pyproject.toml`, `setup.cfg`, or
`conftest.py` exists anywhere in the tree. `ci_pytest()` is
`PYTHONPATH=shell py -m pytest shell/tests -q` and captures nothing structured.
And grepping the closed runbooks shows the on-site-skip clause present in
v0.19's RE-MEASURE and **absent from v0.21, v0.22, and v0.23** — while v0.20's
own record reads "shell **254 passed + 1 declared on-site-only skip**," so the
skip predates the clause's removal and never went away.

**G2 is my defect and it is the fifth in the author-side family.** v0.19 required
the skip to be stated; I dropped that requirement when drafting v0.21's Step 6
and it stayed dropped. From that point the acceptance criterion *every count read
from the log and equal to local at that commit* had no satisfying assignment for
the shell lane, and two cycles resolved the conflict in opposite directions —
v0.22 reported the discrepancy, v0.23 reconciled the number. **The count claim
was false because the criterion was unmeetable, and the executor had no rule
telling it which way to resolve that.** Step 3 is what supplies the rule.

**v0.23's execution is sound and is not reopened.** The tagged close ran
correctly, the published-head run is green on all seven executable jobs, and the
post-push audit found and recorded the count defect against its own cycle — which
is the audit working. The correction is already written in `STATE.md` and
`PROGRESS-v0.23.md`; what this cycle adds is the instrument that would have
caught it before publication, and the bounding that says how far it reaches.
