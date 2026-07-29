# TASKS-v0.21-EXECUTION.md — the checkers, checked

v0.20 closed cleanly. The self-reference defect is gone, the export is derived
rather than pinned, `AGENTS.md` carries both export rules with their measured
reasons, and hosted CI at the published head is green for the first time in two
cycles. Codex's review of the production paths holds — `/v1/ask` still routes
model output through core `/attest`, hydration is still sector-scoped SQL,
robots policy and redirect re-gating are unchanged, and no model client exists
in the Rust core.

**The problem is not in the product. It is in the third consecutive cycle where
`check_publication_status` shipped a rule that does not do what it says.**

v0.19 gave it a rule with no satisfying assignment. v0.20 gave it two silent
no-op paths on unavailable inputs, and fixed them. v0.21 opens with a third:
**one of the two surviving freshness labels currently matches nothing at all.**
The live `STATE.md` header asserts annotated tag object
`7a5c9f7396c043f2b89974585fdd4e5146180e86`, and
`STATE_REF_ASSERTIONS`'s `annotated tag object` pattern returns **zero matches**
against that header, because the header writes ``Remote annotated `v0.15.4` tag
object`` and the pattern requires `annotated` followed immediately by an
optional `tag ` and then `object`. `[^`\n]{0,120}` cannot bridge a backtick. The
rule reports no error and examines nothing.

That is a different failure from v0.20's G2. G2 was about **absent inputs**.
This is a **present input the pattern cannot see** — and it is indistinguishable
from a clean pass, because in every pattern-based checker this project owns,
**zero matches and zero defects produce identical output.**

This cycle does three things and deliberately no more:

1. **removes the vacuous-pattern class** the same way v0.20 removed the
   self-reference class — by inverting the requirement rather than tightening
   the pattern;
2. **gives every publication-status rule a planted-failure control**, reusing
   `invariant-scan`'s existing 23-control mechanism rather than inventing new
   apparatus;
3. **measures what the published tree actually asserts about its own cycle**,
   which no cycle has ever done.

**The public `/v1/*` JSON bodies, the SQLite schema, the robots matcher, the
negative TTL, the politeness limiter, and the golden regression's 11 invariants
are unchanged. Golden stays 11/11 byte-identical through every task. No crate
under `crates/` or `apps/` is modified by any step in this file.**

**Version disposition.** Default is a patch release **`v0.15.5`**. No `/v1/*`
route or body moves and no crate changes. **Unlike v0.20, no publication trigger
is visible at entry: the published head is green.** A tooling-only cycle closing
without a release is legitimate — v0.14 did it — and Step 6 must decide on a
trigger rather than inherit the patch default as a reason. **`v0.16.0`** applies
only if a `/v1/*` body or route moves.

---

## Entering state (asserted, not yet verified)

**Every sentence here is a hypothesis until Step 1 (E0) measures it.**

- `v0.15.4` is published. Release commit
  `8c1eff03ff3e67b18176e8bf533de0f9501e0257`, annotated tag object
  `7a5c9f7396c043f2b89974585fdd4e5146180e86`. v0.20 is closed 7/7 with
  `Release disposition: release (as of 2026-07-29)`. **None of this is
  reopened.**
- Post-push hosted run `30425601829` passed all seven executable jobs at the
  release commit.
- Local `main` is one commit ahead at closing audit `8fc2181`, unpushed.
- Protected pins are **191** — **189** evidence plus **2** authorization
  surfaces. Golden is **11/11**. Local CI is **20/20** with **133** workspace
  tests, **55** net tests (**29** `intel-ingest` + **26** `cored`), shell
  **255/255** on Python 3.11 and 3.12, `invariant-scan` **11/11 rules /
  23 controls**.
- The review export is **147 files** and **90** tracked sources under `crates/`,
  `apps/`, `tools/`, `shell/`. `./run export-check` exists and is
  **operator-local**: it is not invoked by `.github/workflows/ci.yml`.
- A4, the editable-L1 controller residual, the R3/R4 open-bottom deny-lists, the
  active-runbook measured-value heuristic, T7 robots single-flight, and
  NEGATIVE-CACHE Decision B remain open. L2 remains scheduled. **No step in this
  file closes or narrows any of them.**

---

## Drafted gates

| Gate | Where | Hypothesis |
|---|---|---|
| **G1** [P1] | `tools/cycle_check.py`, `STATE_REF_ASSERTIONS[0]` | **The `annotated tag object` freshness rule is vacuous against the live header.** The pattern requires `annotated (?:tag )?object`; the header writes ``annotated `v0.15.4` tag object``, and the character class excludes backticks. Running the pattern against `STATE.md`'s header block returns **zero matches** while the header asserts `7a5c9f73…`. The `tag target` label is unaffected: `release commit` matches and returns `8c1eff03…`. **One of two surviving labels is checking nothing.** |
| **G2** [P1] | every pattern-based checker: `cycle_check`, `checklist_audit`, `progress_check` | **No control proves a control matched.** A regex that finds nothing and a regex that finds nothing wrong produce identical output and identical exit codes. G1 is one instance; enumerate how many rules across the three tools can pass vacuously, and whether any already do. **This is the general form of the defect and the reason it recurred three cycles running.** |
| **G3** [P1] | published tag `v0.15.4` | **Nothing has ever measured what the published tree asserts about itself.** Hosted CI runs at the release commit; the cycle's final records land in a local commit afterward. Whether the published tree contains a closed v0.20 runbook, a matching R-CLOSE progress entry, and a header consistent with both is unknown. **Measure it directly in a disposable clone of the tag. Report whatever it says — a clean result is a result.** |
| **G4** [P2] | the cycle-ending push rhythm | **Each cycle's last commit is verified one cycle late, or never.** `8fc2181` is unpushed, as `72b6f42` was before it. The rhythm is established and defensible, but its consequence — the final append-only record of every cycle is hosted-unverified at the time it is written — has never been stated as a property. State it, and decide whether it is accepted or corrected. |
| **G5** [P2] | `check_publication_status`, the two `return`s after a release-object mismatch | **A rule-2 failure masks rule 1.** A mismatched tag object or target returns before the pending-publication check runs. Confirm, and decide whether masking is intended — reporting one root-cause defect instead of two derived ones is a defensible design, but it should be a decision, not an artifact of statement order. |
| **G6** [P3] | `PENDING_PUBLICATION_RE`; v0.20's G5 | **Confirm the proximity window's disposition.** The pattern matches `publication` followed within 240 characters by `pending` or `outstanding`. Report what v0.20 decided about it and whether that decision was recorded or merely reached. **A refuted G6 is deleted, not worked around.** |

---

## How to run this file

Execute top to bottom, one task and one commit at a time. Follow `AGENTS.md §5`
after **every** task. Implementation and audit-record commits stay separate.

- **🤖 = Codex executes and self-verifies end to end** — no publication, no push.
- **🧑 = exactly one named operator action or decision.**

**Dependency gates.** Step 2 precedes Step 3, because the planted-failure
controls must exist before the published head is judged against them. Step 3
precedes Step 4. Step 5 is blocked by every preceding implementation step;
Step 6 by Step 5.

### Cycle activation (before E0)

In a separate preparatory implementation/audit pair: confirm the worktree is
clean and record the measured refs **without asserting a literal `origin/main`
hash in `STATE.md`'s header** — that prohibition is now enforced and must not be
re-violated by activation. Commit **only** this runbook at
`docs/cycles/TASKS-v0.21-EXECUTION.md`, the `AGENTS.md` header moving the active
declaration from v0.20 to v0.21, and a new `docs/cycles/PROGRESS-v0.21.md`.
**Local `main` already carries the unpushed closing audit `8fc2181`; activation
sits on top of it and does not amend, rebase, or squash it.**

### Global definition of done

Protected hashes exact; all **191** pins match until Step 5 adds more; golden
**11/11 byte-identical**; `./run version-check` green; zero rustc warnings on
offline and net builds; all Rust tests green; all shell tests green under Python
3.11 **and** 3.12; clippy, fmt, ShellCheck, floor byte-compilation, and locked
Rust 1.78 green.

---

## Deferred means deferred

| Deferred item | Unchanged trigger | v0.21 action before the trigger |
|---|---|---|
| T7 robots single-flight | a second concurrent harvester | none |
| NEGATIVE-CACHE Decision B | a measured live transient robots outage for an admitted publisher while a usable last-known-good policy exists, plus operator authorization | none |
| Postgres / pgvector / multi-host seam | unchanged | none |
| A4 untrusted-shell boundary | a third-party/untrusted shell, or any claim HC1 is invariant under shell replacement | none |
| L2 forced-command wrapper | an operator server session | none — remains scheduled |
| R3/R4 open-bottom coverage | a spelling outside registered vocabulary | none |
| Second configured publisher | a separate compliance review per publisher | none — **do not add a source** |
| CI-runner evidence | an authenticated receipt set with identified matrix legs, durably committed | **re-measure at the new release commit — discharged by Step 5** |

---

## Step 1 · E0 — Rebuild the entering state and settle six gates 🤖

**Objective.** Confirm HEAD is green, measure the published tree, and settle
G1–G6.

**Gate.** Read-only repository, object, disposable-clone, and local execution
measurements plus `PROGRESS-v0.21.md` and this runbook's status records only.
No production path, tool, configuration, dependency, protected artifact, or
public surface changes. **`STATE.md` is not edited in this step.**

**Steps.**

1. Run the full entering matrix and standalone `./run golden`, plus
   `verify-artifacts`, `cycle-check`, `checklist-audit`, `progress-check`,
   `version-check`, `invariant-scan`, and `export-check`. **Record both Python
   lanes.**
2. **Confirm G1 by measurement, not by reading.** Apply
   `STATE_REF_ASSERTIONS[0]`'s compiled pattern to the exact text
   `STATE_HEADER_RE` extracts from the live `STATE.md`, and report the match
   list. Report the same for `STATE_REF_ASSERTIONS[1]`. **Report the tag-object
   hash the header does contain**, so the record shows an assertion present and
   unexamined rather than merely a pattern that missed.
3. **Confirm G1 is not merely cosmetic.** Construct a header carrying a *wrong*
   tag-object hash in the live phrasing and show `check_publication_status`
   reports no error. That is the finding: the rule cannot fail.
4. **Enumerate G2.** Across `cycle_check.py`, `checklist_audit.py`, and
   `progress_check.py`, list every rule whose failure mode is "a pattern found
   nothing." For each, state whether a vacuous pass is currently possible and
   whether anything would notice. **A count is required; "several" is not a
   measurement.**
5. **Measure G3 directly.** In a disposable full-history clone checked out at
   tag `v0.15.4`, run `cycle-check`, `checklist-audit`, `progress-check`,
   `version-check`, and `invariant-scan`. Record each exit code and every
   message. **Report whether the published tree contains a closed v0.20 runbook,
   an R-CLOSE progress entry resolving to a real commit, and a header consistent
   with both.** If it is all consistent, say so plainly and close G3 clean.
6. **State G4 as a property.** Name the commits held unpushed at the end of the
   last three cycles and the interval before each was hosted-verified, if it was.
7. **Confirm or refute G5** by constructing a header with both a wrong tag object
   and a pending-publication claim, and reporting how many errors appear.
8. **Answer G6** from v0.20's record, not from re-derivation.
9. Re-verify the published `v0.15.4` objects and all **191** pins unchanged.

**Acceptance criteria.** Entering matrix captured with both interpreters named ·
G1 shown as a rule that cannot fail, with the unexamined hash reported · G2
enumerated with a count · G3 measured at the published tag with every exit code
and message recorded · G4 stated as a property with named commits and intervals ·
G5 confirmed or refuted by error count · G6 answered from the record · published
objects and 191 pins re-verified · `STATE.md` unchanged by this step · golden
11/11.

**Done when** every drafted gate is CONFIRMED or REFUTED with command output.

---

## Step 2 · MATCH-PROOF (G1, G2) — A rule that matched nothing is not a passing rule 🤖

**Objective.** Remove the vacuous-pattern class and make every publication-status
rule provably capable of failing.

**Gate.** `tools/cycle_check.py`, `tools/invariant_scan.py` and its control
corpus, `config/invariant-rules.json` if the rule registry lives there, their
focused tests, and status records. **Blocked on E0 confirming G1 and G2.** No
closed runbook, historical append, crate, dependency, schema, protected
database, or public surface changes.

**Steps.**

1. **Invert the requirement rather than widen the pattern.** The header **must**
   assert the annotated tag object and the release commit, and both **must** be
   fresh. A required assertion that the pattern cannot find is a *failure*, not a
   silent skip. This is the same move that fixed `origin/main` in v0.20:
   converting "if asserted, must be fresh" into a total requirement removes the
   vacuous state instead of chasing the phrasing.
   - **Do not fix this by loosening `[^`\n]{0,120}` to allow backticks.** That
     re-admits the class the moment someone writes a different sentence, and it
     widens the window in which an unrelated hash can be captured.
2. **Fail-before is the repository itself.** Run the corrected check against the
   current header and capture the exit and message: the header asserts a tag
   object the current pattern cannot see.
3. **Register each publication-status rule as a planted-failure control.**
   `invariant-scan` already proves 11 rules against 23 planted failures; that is
   this project's existing answer to "does the control detect anything," and it
   should be reused rather than reinvented. Every rule in
   `check_publication_status` — the `origin/main` prohibition, tag-object
   freshness, target freshness, pending-publication, and each
   unavailable-input report — gets a planted failure that must be detected.
4. **Then** rewrite the `STATE.md` header so both required assertions are
   present in a form the corrected rule matches, and state the phrasing
   requirement in a comment beside the pattern so the next author does not have
   to rediscover it.
5. Report the new rule and control counts, and record them in `STATE.md`,
   `PROGRESS-v0.21.md`, and the pending closing record.
6. **Do not weaken the `origin/main` prohibition or the pending-publication
   rule.**

**Acceptance criteria.** Both tag assertions required, not conditional ·
corrected check fails at the entering header with its message captured · the
backtick-widening fix explicitly rejected in the record with its reason · every
publication-status rule has a planted failure that `invariant-scan` detects ·
new rule/control counts recorded in three places · `origin/main` prohibition and
rule 1 unchanged and re-proven · focused tests green on both interpreters ·
golden 11/11.

**Done when** no rule in this family can pass by examining nothing.

---

## Step 3 · PUBLISHED-HEAD (G3, G4) — Judge the tree that was actually shipped 🤖🧑

**Objective.** Make "the published head is a self-consistent closed cycle" a
measured fact, and decide what to do about the commits that habitually sit
behind it.

**Gate.** Disposable-clone measurements, `STATE.md`, `AGENTS.md` if the push
rhythm becomes a recorded rule, and status records. **Blocked on Step 2.** 🧑
**One operator decision, at step 3.** No crate, dependency, schema, protected
artifact, or public surface changes. **Nothing is pushed by this step.**

**Steps.**

1. Re-run E0's published-tag measurement against the **corrected** checkers from
   Step 2, and record every exit code and message. A rule that was vacuous at E0
   may now report; that difference is the value of Step 2 and belongs in the
   record.
2. **Record the result as it comes.** If the published tree is consistent, close
   G3 clean in one sentence and move on — **a clean check is a result, not a gap
   to fill.** If it is not, record precisely what it asserts versus what is true,
   and **do not correct it inside this step**: a defect in a published tree is a
   forward-correction subject with its own trigger, not a repair to be slipped
   into a measurement task.
3. **🧑 Decide G4.** The cycle-ending record is written after the push and lands
   in the next cycle. Choose one:
   - **Accept** — record it in `AGENTS.md` as the intended rhythm, with the
     consequence stated plainly: the final append-only record of each cycle is
     hosted-unverified when written and is verified at the following
     publication. An accepted property that is written down is not a defect.
   - **Correct** — name the mechanism that would verify it, and the trigger for
     building it. **Do not build it in this cycle.**
   - **Defer** — with a named trigger, into the deferral table.
4. Whatever is chosen, make the record say which, with a date.

**Acceptance criteria.** Published-tag suite re-run under corrected checkers with
every exit code and message recorded · G3 closed clean or recorded as a
forward-correction subject with a trigger, and **not repaired here** · G4
recorded as accepted, corrected-with-trigger, or deferred-with-trigger, dated ·
no push · golden 11/11.

---

## Step 4 · MASKING (G5, G6) — Decide the order, do not inherit it 🤖

**Objective.** Turn two statement-order artifacts into recorded decisions.

**Gate.** `tools/cycle_check.py`, its focused tests, and status records.
**Blocked on E0 confirming or refuting G5 and G6.** **If E0 refutes either, that
half of this step is deleted from the cycle, not worked around.** No other
surface changes.

**Steps.**

1. **G5.** A release-object mismatch currently returns before rule 1 runs.
   Decide and record: either masking is intended — one root-cause defect is
   better than two derived ones — and a comment says so, or all applicable rules
   report and a test proves two errors appear together. **Either is defensible;
   only silence is not.**
2. **G6.** Record v0.20's disposition of the proximity window. If it was accepted,
   restate the acceptance with its reason. If it was reached but never written
   down, write it down now — **that gap is the finding**, and it is the same
   species as the one this whole cycle is about.
3. Add or adjust focused tests to match whichever decision each gate takes, and
   register any new rule as a planted-failure control per Step 2.

**Acceptance criteria.** G5 recorded as intended-masking-with-comment or
all-rules-report-with-test · G6's disposition restated or newly recorded with a
date · refuted halves deleted rather than worked around · any new rule has a
planted-failure control · focused tests green on both interpreters · golden
11/11.

---

## Step 5 · RE-MEASURE 🤖🧑

**Objective.** Produce release-grade hosted evidence for the v0.21 candidate.

**Gate.** 🧑 **One narrow authorization: a non-`main` branch push.** Remote
mutation is limited to the exact candidate branch and its authenticated hosted
evidence dispatch. Repository admission is limited to that run's signed
receipt/bundle pairs, the release-posture deferred-audit report,
`config/protected-artifacts.json`, and status records. No tag, `main` advance,
publication, product path, public surface, dependency, lockfile, schema, or
protected database changes.

**Steps.**

1. Push the candidate to `candidate/<version the trigger sets>`. **Name the
   branch after the decided version, not before the decision** — and note that
   Step 6 may decide there is no release, in which case the branch name must not
   have prejudged it.
2. **Read the remote branch's `ci.yml` and confirm it contains every invocation
   you expect before dispatching**, and that its blob equals the local one.
3. Dispatch with `publish_evidence: true` and `audit_sha` set to the candidate.
4. **Read every count out of the hosted log**, not from job status, and compare
   each against the local measurement **at the same commit**.
5. **Confirm the new planted-failure controls are detected in the hosted
   `invariant-scan`**, and record the rule and control counts from the hosted
   log. Local detection is not the acceptance.
6. Commit the signed receipt/bundle set, re-run `./run verify-artifacts` and
   `./run evidence-report`, and record the new pin count in `STATE.md`,
   `PROGRESS-v0.21.md`, and the pending closing record.
7. Run `./run audit-deferred` in release posture with attestations required.

**Acceptance criteria.** Hosted run pinned to the candidate · every count read
from the log and equal to local at that commit · hosted `invariant-scan` proves
every registered rule and every declared planted-failure control at the
candidate commit, with rule and control counts recorded ·
identity set matches the derived value · signed set committed and re-derived ·
new pin count in three places · `origin/main` unchanged, no tag · golden 11/11.

---

## Step 6 · R-CLOSE 🧑🤖

**Objective.** Close the cycle with a measured record, and decide publication on
a trigger rather than a default.

**Gate.** Steps 1–5 complete and boxed. Worktree clean. **🧑 One operator
decision: publication.**

**Steps.**

1. Re-run the complete definition of done at the release or closing commit and
   capture it.
2. Record the version choice and the trigger that fired.
3. **State the publication disposition as a decision with a trigger, and note
   that no trigger was visible at entry.** The published head was green when this
   cycle opened, so unlike v0.20 there is no red-head trigger to inherit. **A
   no-release close is a complete and legitimate outcome here**; if release is
   chosen, name what the published head would otherwise be missing.
4. Record evidence candidate and release or closing commit as **separate named
   fields**.
5. **State the release disposition as of a date**, in the form
   `cycle_check.py`'s validator reads. A no-release close names the intentionally
   unreleased commits and leaves every version source and tag unchanged.
6. **Record G1 as the third instance in a family, not as an isolated bug.**
   v0.19 shipped an unsatisfiable rule, v0.20 two silent no-op paths, v0.21 a
   vacuous pattern — each found only after the previous fix. Name the common
   cause: **a checker's rules were never themselves subject to the
   planted-failure discipline the rest of the project uses.** That is what Step 2
   corrects, and it is the cycle's actual product.
7. **Record G3's result as measured**, whichever way it came out, and G4's
   disposition with its date.
8. Classify every diff path exactly once in `STATE.md`; update `CHANGELOG.md`,
   `README.md`, and the release authorities if a release is chosen.
9. Reconcile `ARCHITECTURE.md`. **A4, the L1 controller residual, the R3/R4
   open-bottom limitations, the measured-value heuristic, T7, and NEGATIVE-CACHE
   Decision B must all still read as open.**
10. Check R-CLOSE's box and replace the pending heading with the canonical
    `Cycle closed:` record **in one commit**.
11. If a release is published, confirm afterward that hosted CI at the new remote
    head is **green** and record the run id. **If it is not green, that is the
    finding and the cycle does not close on a claim.**
12. **Carry the one-publisher fact forward unchanged.** `arxiv-cs` remains the
    sole real publisher; the other three configured sources remain fixtures.

---

## Execution records

### 2026-07-29 · E0

PASS. The read-only Gate contains every acceptance surface: only this runbook
status record and the append-only progress record move. `STATE.md` remained
blob `7db364ad67d27b2c0aa7cf448ef7db45e1a29ec0`, byte-identical to the entering
tree.

- **Entering matrix:** clean constrained Python 3.11.4 and 3.12.13
  environments each resolved the same **21** packages and passed shell
  **255/255** with the same third-party `StarletteDeprecationWarning`.
  `./run ci-local` passed **20/20** with **133** workspace tests, **55** net
  tests (**29 + 26**), locked Rust 1.78, zero
  rustc/clippy/fmt/ShellCheck failures, `invariant-scan` **11/11 rules / 23
  controls**, all **191/191** pins, protected databases **2/2**, and embedded
  golden **11/11**. Standalone golden passed **11/11**, delta **0**.
  `verify-artifacts`, `cycle-check`, `checklist-audit`, `progress-check`,
  `version-check`, and `invariant-scan` passed locally. Project-root
  `export-check` passed **90/90** derived sources, **7/7** required paths, and
  **149** exported paths; the two-path increase from the entering draft's 147
  is exactly the newly admitted v0.21 runbook and progress log.
- **G1 — CONFIRMED.** `STATE_HEADER_RE` extracted the live header verbatim.
  `STATE_REF_ASSERTIONS[0]` returned `[]`; assertion 1 returned
  `['8c1eff03ff3e67b18176e8bf533de0f9501e0257']`. The header nevertheless
  contains tag object
  `7a5c9f7396c043f2b89974585fdd4e5146180e86`. Replacing that object with forty
  zeroes in the same live phrasing produced `errors=[]`: the rule cannot fail
  on the phrasing it claims to check.
- **G2 — CONFIRMED, count 4.** Entry-point inspection across
  `cycle_check.py`, `checklist_audit.py`, and `progress_check.py` found four
  publication-status regex rules for which zero matches is interpreted as
  success, all in `check_publication_status`: the `origin/main` prohibition,
  pending-publication prohibition, annotated-tag-object freshness, and
  tag-target freshness. The first two are negative scanners and have focused
  examples, but none of the four has an `invariant-scan` planted-failure
  control. Both freshness rules iterate matches without a cardinality
  requirement: tag object is vacuous now; tag target currently finds one match
  but a rephrasing to zero would be silent. `checklist_audit` has no equivalent
  silent required-pattern pass once a checked box exists: missing entry or
  commit evidence is an error, while zero checked boxes makes no audit claim
  and active lifecycle is owned by `cycle-check`. `progress_check` explicitly
  errors on zero dated headers, owners, or commits. No existing command notices
  G1's zero-match state.
- **G3 — CONFIRMED as a forward-correction subject.** A disposable
  full-history clone of the published remote at exact tag target
  `8c1eff03ff3e67b18176e8bf533de0f9501e0257` measured:
  `cycle-check` exit **1**, with six messages saying remote-missing historical
  tags `v0.8.0` and `v0.10.2` do not resolve to the tag objects and commits
  recorded by three closed runbooks; `checklist-audit` exit **0**, **164/164**
  checked tasks resolved; `progress-check` exit **0**, latest
  `RE-MEASURE · 5631e70`; `version-check` exit **0**, exact `v0.15.4`;
  `invariant-scan` exit **0**, **11/11 rules / 23 controls**. The published
  tree has R-CLOSE unchecked, no cycle closing record, and no R-CLOSE progress
  entry. Its header says publication is still in progress, so it is not a
  header consistent with a closed v0.20 record. Remote inspection independently
  found no `v0.8.0` or `v0.10.2` refs. This task records the defect and does not
  repair it.
- **G4 — CONFIRMED as a property.** The last three held commits are:
  v0.18 closing audit
  `344124819cb3c554f851d0cac3f0f1ed08d1aa10`, first hosted-verified **9:51:54**
  later by successful candidate run `30414648482` at descendant
  `197e93effe9a6abf9c59488a9849c6dcda47646c`; v0.19 publication finding
  `72b6f425114e06b1e148e0aa360e280a690e4f0c`, first hosted-verified **2:20:18**
  later by successful candidate run `30423736121` at descendant
  `8230d4f24f565afcde92931c987adff4339036af`; and v0.20 closing audit
  `8fc21813763c19a90ee17e7b95d1e87330a916b8`, which remains on no remote branch
  and has no hosted verification.
- **G5 — CONFIRMED.** With correct refs, a wrong tag-object assertion in the
  live phrasing plus a pending-publication claim produced one error — pending
  only, because G1 hid the wrong object. With the measured tag ref itself
  changed to forty zeroes, the same pending header again produced exactly one
  error: release-object agreement. The early return masked the applicable
  pending-publication rule.
- **G6 — CONFIRMED as already recorded, not a new gap.** v0.20 accepted the
  240-character proximity window as bounded looseness because it scans only the
  live header and can cause only a loud conservative refusal, never a false
  pass. The decision is present in both the v0.20 execution record and progress
  log.
- **Objects and pins:** remote `main` and the peeled `v0.15.4` target remain
  `8c1eff03ff3e67b18176e8bf533de0f9501e0257`; annotated tag object remains
  `7a5c9f7396c043f2b89974585fdd4e5146180e86`. Manifest validation passed
  **191/191** pins; protected databases remain **2/2** exact.

### 2026-07-29 · MATCH-PROOF

PASS. E0 confirmed G1 and G2, so the Gate opened. The implementation changes
only `cycle_check`, its focused tests, `invariant_scan` and its registry, plus
the permitted status records. No closed runbook, historical append, crate,
dependency, schema, protected database, robots path, configured source, or
public surface changed.

- **Required, not conditional:** the corrected check converts zero matches for
  either immutable assertion into `publication assertion required`; found
  assertions must still equal the measured refs. Before editing `STATE.md`, the
  corrected command exited **1** against the entering header with exactly
  `STATE.md: publication assertion required: status header must assert the
  annotated tag object in the required unambiguous phrasing`.
- **Narrow grammar retained:** the live header now names the release before the
  assertion and phrases the assertions as `annotated tag object <hash>` and
  `release commit <hash>`. The pattern's `[^`\n]` class was deliberately not
  widened: admitting intervening backticks would allow an unrelated hash to
  satisfy the assertion and reintroduce the silent class after a rephrasing.
- **Executable controls:** new registered R12 invokes the actual
  `check_publication_status` entry point with nine planted cases: mutable
  `origin/main`, missing and stale tag-object assertions, missing and stale
  target assertions, pending publication, missing annotated-tag ref, missing
  peeled target, and unavailable ancestry. Its seven registry fail-before
  mutations independently disable the seven rule families; all seven produce
  their exact expected findings. Pending closing count: `invariant-scan`
  **12/12 registered rules / 30 controls**, up from **11/11 / 23**.
- **Existing prohibitions re-proven:** the `origin/main` condition and pending
  rule 1 are unchanged apart from R12 site comments. Their focused cases pass,
  and R12 controls that replace either condition with `False` are detected.
- **Acceptance:** `cycle-check` passes. Focused `cycle_check` and
  `invariant_scan` tests pass **47/47** under Python 3.11.4 and independently
  **47/47** under Python 3.12.13. The complete scanner passes **12/12 / 30**.
  The first restricted golden invocation was a loopback-bind permission
  non-result; the identical permitted invocation passed **11/11**, delta
  **0**. `git diff --check` passes. An early synthetic control name shaped like
  a real cycle literal was rejected by `cycle-check`; neutral control names
  replaced it before acceptance.

### 2026-07-29 · PUBLISHED-HEAD

PASS with G3 recorded as a forward-correction subject. The Gate contained every
acceptance surface: one fresh disposable clone, `STATE.md`, `AGENTS.md`, and
this task's status records. The published tree was not modified, and nothing
was pushed.

- **Identity:** the fresh full-history SSH clone checked out exact tag target
  `8c1eff03ff3e67b18176e8bf533de0f9501e0257`; `v0.15.4` resolved to annotated
  tag object `7a5c9f7396c043f2b89974585fdd4e5146180e86` and peeled to that same target.
  The unauthenticated HTTPS spelling attempted first returned `Repository not
  found`; the configured SSH remote produced the measured clone.
- **Corrected cycle checker:** current `cycle_check.run(<published-root>)`
  exited **1** with these seven messages:
  1. `docs/cycles/TASKS-v0.10.2-EXECUTION.md: annotated tag 'v0.10.2' does not
     resolve to recorded tag object d821f8b2eb6f39fe4a7d06a88cd61de771c7b0ba`
  2. `docs/cycles/TASKS-v0.10.2-EXECUTION.md: release 'v0.10.2' does not
     dereference to recorded commit 7d127abac0b993c9e98294ee1c03ff01153de9d0`
  3. `docs/cycles/TASKS-v0.8-EXECUTION.md: annotated tag 'v0.8.0' does not
     resolve to recorded tag object 314c1dd914a3d8e9193445874a419ed762581e6e`
  4. `docs/cycles/TASKS-v0.8-EXECUTION.md: release 'v0.8.0' does not
     dereference to recorded commit bfc8c5af85734583f966ee70d2ec521155432205`
  5. `docs/cycles/TASKS-v0.8.1-EXECUTION.md: annotated tag 'v0.8.0' does not
     resolve to recorded tag object 314c1dd914a3d8e9193445874a419ed762581e6e`
  6. `docs/cycles/TASKS-v0.8.1-EXECUTION.md: release 'v0.8.0' does not
     dereference to recorded commit bfc8c5af85734583f966ee70d2ec521155432205`
  7. `STATE.md: publication assertion required: status header must assert the
     annotated tag object in the required unambiguous phrasing`

  The final message is the Step 2 differential: the published checker emitted
  only the first six, while the corrected total rule exposes the header
  assertion it previously examined zero times.
- **Remaining corrected suite:** current `checklist_audit.run` exited **0**,
  emitting one clean line for each of eighteen published runbooks and
  `PASS (checked=164, retracted=3, entries_matched=164,
  commits_resolved=164, exemptions=0)`. Current `progress_check` exited **0**
  with `PASS (2026-07-29 · RE-MEASURE · 5631e70)`. Published
  `version-check` exited **0**, reported version **0.15.4** for
  `apps/cored/Cargo.toml`, `shell/intel_shell/__init__.py`,
  `shell/intel_shell/app.py`, `STATE.md`, and `CHANGELOG.md`, then reported
  exact HEAD tag **0.15.4** and `PASS (0.15.4)`. Current `invariant_scan`
  against the published registry exited **0**, emitted PASS for R1–R11 and
  each of their 23 exact fail-before sites, then
  `SELF-TEST PASS (11/11 rules, 23 controls)`.
- **G3 disposition:** the published tree has v0.20 R-CLOSE unchecked, no v0.20
  cycle closing record, no R-CLOSE progress entry, and a header describing
  publication preparation rather than a closed cycle. It is a
  forward-correction subject. It was not repaired here. Trigger: the next
  operator-authorized `main` publication after v0.15.4; a no-release close
  leaves it open until a later publication.
- **G4 decision — Accept, 2026-07-29:** the operator accepts the intended
  rhythm and its consequence. `AGENTS.md` now states that each cycle's final
  append-only audit record is hosted-unverified when written after publication
  and is verified at the following publication. Required local gates and
  append-only evidence support it until then.
- **No-push acceptance:** final `git ls-remote` still reported `main` and the
  peeled `v0.15.4` target at
  `8c1eff03ff3e67b18176e8bf533de0f9501e0257` and annotated tag object
  `7a5c9f7396c043f2b89974585fdd4e5146180e86`. Standalone golden passed
  **11/11**, delta **0**.

### 2026-07-29 · MASKING

PASS. E0 confirmed both G5 and G6, so neither half was deleted. The Gate
contains the implementation: `tools/cycle_check.py`, its focused tests, and
status records only.

- **G5 — intentional masking, 2026-07-29:** release-object agreement is the
  root-cause boundary. If the measured annotated object or peeled target
  differs from the closed runbook, later pending-publication and
  header-freshness conclusions rely on an untrusted release identity. The two
  early returns remain, and an inline comment records that they mask derived
  rules intentionally.
- **G5 control:** a header asserting pending publication with otherwise fresh
  immutable hashes was combined with a measured tag object of forty `f`
  characters. The focused test receives exactly one error,
  `publication release-object agreement`; it receives no derived disposition
  error. This proves the chosen order rather than merely documenting it.
- **G6 — accepted bounded looseness restated, 2026-07-29:** v0.20's execution
  record constructed `publication is complete and exact. An unrelated export
  review has outstanding documentation` and observed a match. It accepted that
  false positive because the 240-character expression is scoped to the live
  header paragraph and can cause only a loud conservative refusal, never a
  false pass. The expression and that disposition are unchanged.
- **Acceptance:** focused `cycle_check` tests pass **26/26** on Python 3.11.4
  and independently **26/26** on Python 3.12.13. No new rule was added, and the
  existing complete scanner passes **12/12 rules / 30 controls**. Standalone
  golden passes **11/11**, delta **0**.

---

## Cycle checklist

- [x] **E0** — entering matrix with both interpreters; G1 shown as a rule that
  cannot fail, with the unexamined hash reported; G2 enumerated with a count; G3
  measured at published tag `v0.15.4` with every exit code and message; G4 stated
  as a property with named commits; G5 confirmed or refuted by error count; G6
  answered from the record; `STATE.md` unedited
- [x] **MATCH-PROOF** — both tag assertions required rather than conditional;
  fail-before captured at the entering header; backtick-widening explicitly
  rejected with its reason; every publication-status rule has a detected planted
  failure; new counts in three places
- [x] **PUBLISHED-HEAD** — published-tag suite re-run under corrected checkers;
  G3 closed clean or recorded as a forward-correction subject and **not repaired
  here**; G4 recorded as accepted, corrected, or deferred, dated; no push
- [x] **MASKING** — G5 decided and commented or tested; G6's disposition
  recorded with a date; refuted halves deleted
- [ ] **RE-MEASURE** — hosted run pinned; counts equal local at the same commit;
  hosted `invariant-scan` proves every registered rule and declared
  planted-failure control at that commit, with counts recorded
- [ ] **R-CLOSE** — publication decided on a trigger, with no-release named as
  legitimate; G1 recorded as the third instance in a family with its common
  cause; G3 and G4 recorded as measured; all open items still open

---

## Standing prohibitions

- **Do not fix G1 by allowing backticks in the pattern's character class.** That
  re-admits the class at the next rephrasing and widens the capture window.
- **Do not fix G1 by rewriting only the header.** A header edit makes the current
  text match; it leaves the rule unable to fail on the next one.
- **Do not weaken the `origin/main` prohibition or the pending-publication rule**
  while correcting the tag assertions.
- **Do not repair a published-tree defect inside Step 3.** Measurement and repair
  are separate; a repair folded into a measurement task is how a finding gets
  softened into a fix nobody reviewed.
- **Do not build G4's verification mechanism in this cycle**, whatever Step 3
  decides. Naming a trigger is the deliverable.
- **Do not amend, rebase, or squash `8fc2181`.**
- **Do not invent a new control framework for G2.** `invariant-scan`'s planted
  failures already are this project's answer; reuse them.
- **Do not modify any crate under `crates/` or `apps/`.** This cycle is tooling
  and documentation. A source change is a scope violation.
- **Do not touch the robots matcher, the negative TTL, the politeness limiter, or
  the crawl-delay ratchet.**
- **Do not add a configured source.**
- **Do not claim any task closes or narrows A4**, the L1 residual, the R3/R4
  open-bottom limitations, T7, or NEGATIVE-CACHE Decision B.
- **Do not batch `STATE.md` / `PROGRESS-v0.21.md` updates or combine two tasks in
  one commit.**
- If any Step's Objective, Acceptance criteria, or "Done when" is amended after
  this file is first committed, name the amendment in a dated
  `## Runbook amendments` block in the same commit.

---

## Provenance of this draft

Every gate above was read out of the repomix export of the v0.15.4 tree on
2026-07-29 by path and line, and each is written as a hypothesis for E0 to
confirm or refute.

**G1 is not a hypothesis — it is measured.** Extracting `STATE.md`'s header with
`STATE_HEADER_RE` and applying `STATE_REF_ASSERTIONS`'s two compiled patterns to
it returns `[]` for `annotated tag object` and
`['8c1eff03ff3e67b18176e8bf533de0f9501e0257']` for `tag target`, while the header
plainly asserts tag object `7a5c9f7396c043f2b89974585fdd4e5146180e86`. E0 should
reproduce it rather than take this on faith, but the expected result is known.

**v0.20's own work is sound and is not reopened.** The `origin/main` prohibition
is correctly structural; `git_status` replaces the silent `merge-base` return
with a named unavailable-input error; both unresolvable-ref paths now report;
rule 1 is intact; `export_check.py` derives its expected set from `git ls-files`
with no pinned count; `AGENTS.md` carries both export rules with their measured
reasons and points at the executing check; and `TASKS-v0.6.md` and
`TASKS-v0.7.md` are excluded. `export-check` is operator-local and not invoked by
`ci.yml`, which the v0.20 runbook permitted provided it was stated — confirm at
E0 that it was stated, and if it was not, that omission belongs in Step 4's
record rather than in a new gate.

**G3 exists because the export cannot answer it.** The export shows the local
working tree, which includes the unpushed `8fc2181`. What the published tree
contains is a different question, and no cycle has ever measured it. It may well
be clean. It should still be measured.
