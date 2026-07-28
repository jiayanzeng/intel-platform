# TASKS-v0.19-EXECUTION.md — the failure path, and the record of it

v0.18 put the shipped matcher in front of a real publisher policy and ran the
first harvest under a gate that enforces what it claims. arXiv answered **404**
on every attempt, published no `Crawl-delay`, issued no redirect, returned no
5xx, and served three clean OAI-PMH pages. That is the best possible outcome and
the least informative one: **every failure branch of the compliance gate is still
proven only against strings this project wrote.**

Two things are true at entry and neither is a code defect:

1. The gate's *success* path met the wire. Its *failure* path did not, and one
   failure branch — `Policy::Unreachable` — is cached for **24 hours** in the
   same map as a successful policy, where it also **replaces** whatever good
   policy was there. One dropped packet therefore denies a publisher for a day
   and destroys the answer we already had.
2. `STATE.md` says publication is pending. It is not; it completed. Nothing this
   project runs can tell that the authoritative status document is false.

v0.19 does four things and deliberately no more:

1. **makes the status document's truth executable**, and corrects it forward;
2. **brings the review corpus back under budget**, because the export that this
   project's own review loop depends on is at capacity;
3. **exercises the gate's failure path** and gives negative results a policy that
   is RFC 9309's rather than an accident of the cache;
4. **disposes of the unowned preview surface** that shipped in v0.15.2.

**The public `/v1/*` JSON bodies, the SQLite schema, and the golden regression's
11 invariants are unchanged. Golden stays 11/11 byte-identical through every
task. The protected corpus is not written by any step in this file.**

**Version disposition.** Default is a patch release **`v0.15.3`**. Step 4 changes
robots-cache behaviour on the failure path, which is a correctness fix, not a
surface. **`v0.16.0`** applies only if a `/v1/*` body or route moves, **or if
Step 5 promotes the preview to a supported operator surface.** Record the fired
trigger at Step 7, not the default inherited here.

---

## Entering state (asserted, not yet verified)

**Every sentence here is a hypothesis until Step 1 (E0) measures it.**

- `v0.15.2` is published. Release commit
  `b3c4c4d3b695ceff27a9d4a2ec610fc851939324`, annotated tag object
  `22beef8e023e52024cfe9614273e2d82b39f4956`. v0.18 is closed 7/7 with
  `Release disposition: release (as of 2026-07-28)`. **None of this is reopened.**
  The dated v0.18 closing record is immutable; every correction in this cycle is
  a forward append.
- `origin/main` is `3441248…`, the v0.18 closing audit commit. `STATE.md` still
  asserts `f13c6129…` and "remote tag absent".
- Protected pins are **161** — **159** evidence plus **2** authorization
  surfaces. Golden is **11/11**. Local CI is **20/20** with **131** workspace
  tests, **55** net tests (**29** `intel-ingest` + **26** `cored`), shell
  **245/245** on Python 3.11 and 3.12, `invariant-scan` **11/11 rules /
  23 controls**.
- All five version authorities read `0.15.2`.
- `AGENTS.md` still declares **v0.18** the active cycle.
- A4, the editable-L1 controller residual, the R3/R4 open-bottom deny-lists, the
  active-runbook measured-value heuristic, and T7 robots single-flight remain
  open. L2 remains scheduled. **No step in this file closes or narrows any of
  them.**

---

## Drafted gates

Each is a hypothesis read out of the repomix export by path and line. E0
confirms or refutes each with command output. **A refuted gate is deleted from
the cycle, not worked around.**

| Gate | Where | Hypothesis |
|---|---|---|
| **G1** [P1] | `crates/compliance/src/lib.rs:697–748`; `crates/ingest/src/net.rs:58` | **A transient failure is cached like a policy.** `policy_for` stores `Policy::Unreachable` unconditionally at `:714`, and `cached` returns it until `ROBOTS_TTL` — **24 hours** — expires. So one DNS/TLS/5xx blip denies that origin for a day with no retry, **and overwrites a previously cached good policy**. RFC 9309 §2.3.1.4 contemplates the opposite: a crawler that cannot reach the policy may fall back to a cached copy. **This is fail-*closed*, so it is not a compliance violation and must never be written up as one.** It is a wrong caching policy and an unstated consequence of a documented one. |
| **G2** [P2] | `STATE.md:3`, `STATE.md:132–134`; `tools/cycle_check.py` | **The authoritative status document is false and nothing executes against it.** It claims publication is pending, `origin/main` is `f13c6129…`, and the remote tag is absent. `cycle-check`, `checklist-audit`, `progress-check`, and `version-check` all pass anyway. `version-check` reconciles version literals to tags; **nothing reconciles the status header to the refs or to the newest closed disposition.** |
| **G3** [P2] | `repomix.config.json`; the export | **The review loop is at capacity.** The export is **4,868,973** bytes across **338** files and the project store reports 99% used. Measured composition: `evidence/**` **1,613,598** (**33.4%**, 178 files), closed cycles ≤ v0.11 **653,077** (**13.5%**), `STATE.md` **533,952** (**11.0%**, 8,135 lines in one file). The evidence bodies exist to be re-hashed, not read; `config/protected-artifacts.json` already carries every pin name, hash, byte count, and provenance string. |
| **G4** [P2] | `intel-compliance --features diagnostics`; `intel-ingest --features robots-preview` and its binary | **A surface shipped in a tag with no owner.** v0.18's closing record calls the preview "feature-gated and unsupported" and says promotion needs a named owner plus explicit support authorization. Neither exists. An unowned surface in a published tag is discovered later and mistaken for production. |
| **G5** [P3] | `crates/ingest/src/lib.rs:155–174` | **`unknown` sentinels.** `host_of` returns `"unknown"` and `origin_of` returns `"https://unknown"` for a URL that fails `absolute_url_parts`. Show whether any production input can reach them — configured URLs are validated and redirects arrive through `reqwest::Url::join` — and if none can, **close it clean as not-a-defect.** A clean check is a result. |
| **G6** [P3] | v0.18 `LIVE-HARVEST` record | **Politeness was reported, not measured.** All three page requests reported the **0.500 s** operator floor (`DEFAULT_RPS = 2.0`, `apps/cored/src/main.rs:144`), but total wall time was **46.38 s** including the net build, so the log line is the only evidence the waits happened. State whether the existing `acquires`-counting tests are the proof, or whether nothing measures the interval. |

---

## How to run this file

Execute top to bottom, one task and one commit at a time. Follow `AGENTS.md §5`
after **every** task. Implementation and audit-record commits stay separate.

- **🤖 = Codex executes and self-verifies end to end** — no live model endpoint,
  no live server session, no publication, no push.
- **🧑 = exactly one named operator action or decision.**

**Dependency gates.** Step 2 precedes Step 3, because the executable status
check must exist before `STATE.md` is restructured. Step 3 precedes Step 4, so
the failure-path work is reviewed against an export that fits. Step 6 is blocked
by every preceding implementation step; Step 7 by Step 6.

### Cycle activation (before E0)

In a separate preparatory implementation/audit pair: confirm the worktree is
clean and record the measured `origin/main`; commit **only** this runbook at
`docs/cycles/TASKS-v0.19-EXECUTION.md`, the `AGENTS.md` header moving the active
cycle declaration from v0.18 to v0.19, and a new `docs/cycles/PROGRESS-v0.19.md`.
Run `cycle-check` and `checklist-audit`. **Do not claim E0's acceptance from this
commit, and do not correct `STATE.md` here** — Step 2 owns that, and correcting
it at activation would destroy Step 2's fail-before control.

### Global definition of done

Protected hashes exact; all **161** pins match until Step 6 adds more; golden
**11/11 byte-identical**; `./run version-check` green; zero rustc warnings on
offline and net builds; all Rust tests green; all shell tests green under Python
3.11 **and** 3.12; clippy, fmt, ShellCheck, floor byte-compilation, and locked
Rust 1.78 green.

**No harvested or observed output is promoted to evidence.** Receipts, bundles,
and pins come from authenticated CI only.

---

## Deferred means deferred

| Deferred item | Unchanged trigger | v0.19 action before the trigger |
|---|---|---|
| T7 robots single-flight | a second concurrent harvester | none — **and Step 4 must not implement it while touching the same function** |
| Postgres | a second archive writer | none |
| pgvector | exact cosine stops fitting the measured request budget | none |
| Multi-host seam hardening | an actual core/shell host split | none |
| A4 untrusted-shell boundary | a third-party/untrusted shell, or any claim HC1 is invariant under shell replacement | none |
| L2 forced-command wrapper | an operator server session | none — remains scheduled |
| R3/R4 open-bottom coverage | a provider or credential spelling outside registered vocabulary | none |
| Second configured publisher | an explicit, separate compliance review per publisher | none — **do not add a source in this cycle** |
| Unreachable last-known-good fallback | a measured live transient robots outage for an admitted publisher while a usable last-known-good policy exists, followed by explicit operator authorization of the more-permissive fallback | **Step 4 records the deferral and implements only the short negative TTL; no fallback** |
| CI-runner evidence | an authenticated receipt set with identified matrix legs, durably committed | **re-measure at the new release commit — discharged by Step 6** |

---

## Step 1 · E0 — Rebuild the entering state and confirm the drafted gates 🤖

**Objective.** Confirm HEAD is green, settle G1–G6, and produce the inputs Steps
2–5 need.

**Gate.** Read-only repository, object, and local execution measurements plus
`PROGRESS-v0.19.md` and this runbook's status records only. **`STATE.md` is not
edited in this step** — its falsity is Step 2's fail-before control and must
survive E0 intact. No production path, dependency, lockfile, protected artifact,
or public surface changes.

**Steps.**

1. Run the full entering matrix and standalone `./run golden`, plus
   `verify-artifacts`, `cycle-check`, `checklist-audit`, `progress-check`,
   `version-check`, `invariant-scan`. **Record both Python lanes.**
2. **Measure the refs.** Record `git rev-parse origin/main`, the annotated
   `v0.15.2` tag object, and its peeled target, locally and remotely. Compare
   each against what `STATE.md:3` and `STATE.md:132–134` assert, and record the
   deltas as measured values, not prose.
3. **Confirm G2 is undetectable.** Show that `cycle-check`, `checklist-audit`,
   `progress-check`, and `version-check` all pass at HEAD **while `STATE.md` is
   false**. That passing output is the finding.
4. **Confirm G1 by construction.** Write a temporary, executing control against
   the trait fetcher: (a) an origin whose first fetch returns `Unreachable` is
   denied, and is still denied on a second call with **zero additional fetches**;
   (b) an origin with a cached allowing policy, re-fetched after TTL expiry into
   `Unreachable`, is thereafter denied. Report `RobotsCache::fetches()` for each.
   **If either fails to reproduce, refute G1 and delete Step 4 from the cycle.**
   Remove the control after measurement; Step 4 owns the durable tests.
5. **Confirm G5 by construction**, or close it clean with the reason.
6. **Answer G6 from the test corpus**, not from the harvest log: name the tests
   that prove the limiter is consulted, and state plainly whether anything
   asserts the elapsed interval.
7. **Measure G3.** Record the export's total bytes, file count, and the byte
   totals for `evidence/**`, closed cycles ≤ v0.11, and `STATE.md`.
8. Re-verify the published `v0.15.2` objects and all **161** pins unchanged.

**Acceptance criteria.** Entering matrix captured with both interpreters named ·
measured refs recorded beside the `STATE.md` assertions they contradict · all
four status tools shown passing over a false `STATE.md` · G1 reproduced with
fetch counts, or refuted · G5 confirmed or closed clean · G6 answered from named
tests · G3 byte totals recorded · published objects and 161 pins re-verified ·
`STATE.md` unchanged by this step · golden 11/11.

**Done when** every drafted gate is CONFIRMED or REFUTED with command output.

---

## Step 2 · STATUS-TRUE (G2) — The status document is checked, then corrected 🤖

**Objective.** Make "`STATE.md` tells the truth about publication" an executed
property, and only then make it true.

**Gate.** `tools/cycle_check.py` (or a sibling status checker) and its shell
tests, `run`'s dispatch if a new subcommand is added, `STATE.md`,
`PROGRESS-v0.19.md`, and this runbook's status records. **The v0.18 closing
record, `PROGRESS-v0.18.md`, and every closed runbook are immutable.** No
production Rust path, dependency, lockfile, schema, protected database, or
public surface changes.

**Order matters: the check lands first and must fail on the repository as it
stands.** Correcting `STATE.md` first would leave the check unproven.

**Steps.**

1. Add an executable status reconciliation with exactly two rules:
   - **(a) Disposition agreement.** If the newest closed execution runbook
     declares `Release disposition: release` and names an annotated tag that
     exists and peels to a commit reachable from `HEAD`, then `STATE.md`'s header
     status block must not assert that publication is pending or outstanding.
   - **(b) Assertion freshness.** Any `origin/main`, tag-object, or tag-target
     hash asserted **in `STATE.md`'s header block** must equal the measured ref.
     **Scope the rule to the header block only** — the append-only body records
     historical measurements that were true when written and must never be
     rewritten to satisfy a checker.
2. **Fail-before is the repository itself.** Run the new check at the current
   commit and capture its non-zero exit and both rule messages. Record that
   output verbatim; it is this step's proof.
3. Add focused tests for both rules, including a passing case, so the check
   cannot degrade into an always-pass.
4. **Then** write the forward publication-audit append to `STATE.md`: the
   measured `origin/main`, the annotated tag object and its peeled release
   commit, the atomic push result, and the publication CI run at the closing
   commit — **its id, attempt, and conclusion, read from the run, not inferred
   from the push succeeding.** If no publication CI run exists, say so; an absent
   run is a recorded fact, not a gap to fill with a re-dispatch.
5. Update the `STATE.md` header status block to the measured present.
6. Re-run all four status tools plus the new one and record them green.

**Acceptance criteria.** New check fails at the entering commit with both rule
messages captured · focused tests cover both rules and a passing case · the
forward append names measured refs and the publication run's id/attempt/
conclusion, or records its absence · no closed runbook, dated closing record, or
historical `STATE.md` append is edited · all status tools green after ·
`invariant-scan` unchanged or increased · golden 11/11.

**Done when** a false publication status is something this project can fail on.

---

## Step 3 · EXPORT-BUDGET (G3) — Keep the review corpus reviewable 🤖

**Objective.** Bring the repomix export back under budget without removing a
single fact the review loop depends on.

**Gate.** `repomix.config.json`, `STATE.md`, a new `docs/state-archive/`
directory, and status records. **No file is deleted from the repository.**
Exclusion changes what the export ships, not what `verify-artifacts` hashes. No
production path, dependency, lockfile, schema, protected artifact, or public
surface changes.

**Steps.**

1. Add ignore patterns for `evidence/**` and
   `docs/cycles/{TASKS,PROGRESS}-v0.{8,9,10,11}*`. **Keep
   `config/protected-artifacts.json`** — it is the manifest that makes the
   excluded evidence bodies redundant to read, and excluding it would be the one
   change that actually loses information.
2. Archive `STATE.md`'s appends through v0.13 into
   `docs/state-archive/STATE-through-v0.13.md`, **byte-identical to the text
   removed**, with a pointer left in `STATE.md`. Retain the header, the active
   cycle, and the two most recent closed cycles in place. **This is archival,
   not regeneration** — `STATE.md` is append-only and replacing it is how drift
   started before.
3. Prove the archive is lossless: concatenating the archive and the retained
   body reproduces the prior `STATE.md` byte-for-byte, demonstrated by a hash
   comparison against the pre-change file.
4. Re-run the export **from the project root**, so `repomix.config.json` is
   picked up. Running it from anywhere else silently drops `Cargo.lock`, which is
   the root cause of the lockfile drift this project already paid for once.
5. Record the export's byte count and file count before and after.

**Acceptance criteria.** Post-export contains `Cargo.lock`,
`config/protected-artifacts.json`, `AGENTS.md`, `run`, and every file under
`crates/`, `apps/`, `tools/`, `shell/` · export size recorded before and after ·
archive concatenation reproduces the prior `STATE.md` by hash · no repository
file deleted · `verify-artifacts` **161/161** and protected databases **2/2**
after · `cycle-check`, `checklist-audit`, `progress-check`, and Step 2's new
check all green after the split · golden 11/11.

**Done when** the review corpus fits and the archive is provably lossless.

---

## Step 4 · NEGATIVE-CACHE (G1) — A failure is not a policy 🤖

**Objective.** Give `Policy::Unreachable` a caching policy chosen on RFC 9309
grounds rather than inherited from the success path.

**Gate.** `crates/compliance/src/lib.rs`, `crates/ingest/src/net.rs` constants
and tests, the sole production cache-construction call in
`apps/cored/src/main.rs`, and current status/audit records. **Blocked on E0
confirming G1.** No `/v1/*` body, route, schema, dependency, lockfile, protected
artifact, document-request control flow, or connector behavior changes. **Do
not implement single-flight while you are in `policy_for`** — T7 is deferred and
its trigger has not fired.

**This is two decisions, not one, and the second one is 🧑.**

**Steps.**

1. **Decision A (🤖, uncontroversial): a negative result gets its own, short
   TTL.** A failed fetch must not occupy a 24-hour slot. Introduce a named
   constant beside `ROBOTS_TTL` and apply it only to `Unreachable`. State the
   chosen value and why. Fail-before: an origin that fails once is retried after
   the negative TTL and not before.
2. **Decision B (🧑, permissive direction — the operator chooses): does an
   unreachable fetch fall back to the last known good policy?** RFC 9309
   §2.3.1.4 permits a crawler to use a previously cached copy. Today the failure
   *overwrites* it. Falling back is **more permissive than current behaviour**
   and must be an explicit decision, not a side effect of fixing Decision A.
   - If **yes**: retain the last good policy with its own named staleness bound,
     use it while within bound, and **deny once the bound is exceeded**. A test
     must prove the deny past the bound, or the bound is decoration.
   - If **no**: record it as deferred with a named trigger and implement only
     Decision A. **A deferred B is a complete step.**
3. Write the durable tests E0's temporary control stood in for: repeated denial
   without re-fetch inside the negative TTL; retry after it; and the overwrite
   case, asserted in whichever direction Decision B chose.
4. **Preserve every fail-closed property that is not in scope.** `Unavailable`
   (404) still routes through the per-source `MissingPolicy`. An explicit
   `Disallow` is still honoured. A network reach with no cache is still rejected
   before any request. The operator deny-list still subtracts only.
5. **Do not touch the limiter, the `apply_crawl_delay` ratchet, or `acquires`.**
   The one-way slow-down ratchet is correct and was fixed once already.

**Acceptance criteria.** Fail-before captured for every new test · negative TTL
named, applied only to `Unreachable`, and justified · Decision B recorded as
implemented-with-bound or deferred-with-trigger, never as "observed" · the four
listed fail-closed properties re-proven by existing tests, unchanged · limiter
and ratchet untouched, shown by unchanged blobs or an enumerated diff · net and
offline suites green · golden 11/11.

**Done when** the gate's failure branch has a policy someone chose.

---

## Step 5 · PREVIEW-DISPOSITION (G4) — One owner or no surface 🧑🤖

**Objective.** Give the feature-gated preview shipped in v0.15.2 exactly one
disposition.

**Gate.** 🧑 **One operator decision.** Scope is the preview's own sources,
manifests, feature declarations, tests, binary, `ARCHITECTURE.md`, and status
records. No default-build behaviour, `/v1/*` surface, schema, dependency,
lockfile, or protected artifact changes **unless** promotion is chosen, in which
case the version trigger moves to `v0.16.0` and Step 7 must record it.

**Steps.**

1. Choose one, and only one:
   - **Promote** — name the owner, state the support commitment, and bring it
     under the same rules as every other operator surface: an entry in
     `ARCHITECTURE.md`, coverage in the default matrix, and an `invariant-scan`
     rule if it can drift.
   - **Retire** — delete the feature, its binary, and its gates. The v0.18
     observations remain valid: they record what the *shipped* matcher said, and
     deleting the preview does not retract them. Note that the published v0.15.2
     tag still contains it; that is history, not a live surface.
   - **Retain with a trigger** — keep it inert, name the condition under which
     it becomes supported, and put it in the deferral table. **"Keep it around"
     without a trigger is not this option.**
2. Whichever is chosen, make `ARCHITECTURE.md` say it.
3. If retiring, confirm the feature-gated suites disappear from the supplemental
   matrix rather than silently continuing to pass against dead code.

**Acceptance criteria.** Exactly one disposition recorded · owner named, or
trigger named, or deletion complete · `ARCHITECTURE.md` matches the choice ·
default build unchanged unless promotion was chosen · supplemental suite counts
reconciled against the choice · golden 11/11.

---

## Step 6 · RE-MEASURE 🤖🧑

**Objective.** Produce release-grade hosted evidence for the v0.19 candidate.

**Gate.** 🧑 **One narrow authorization: a non-`main` branch push.** Remote
mutation is limited to the exact candidate branch and its authenticated hosted
evidence dispatch. Repository admission is limited to that run's signed
receipt/bundle pairs, the release-posture deferred-audit report,
`config/protected-artifacts.json`, and status records. No tag, `main` advance,
publication, product path, public surface, dependency, lockfile, schema, or
protected database changes.

**Steps.**

1. Push the candidate to `candidate/<version the trigger sets>`. **Name the
   branch after the decided version, not before the decision.**
2. **Read the remote branch's `ci.yml` and confirm it contains every invocation
   you expect before dispatching**, and that its blob equals the local one.
3. Dispatch with `publish_evidence: true` and `audit_sha` set to the candidate.
4. **Read every count out of the hosted log**, not from job status, and compare
   each against the local measurement **at the same commit**. That equality is
   the criterion, not any number written earlier in this file. Where a hosted
   count differs from local by a declared on-site-only skip, state the skip.
5. Commit the signed receipt/bundle set, re-run `./run verify-artifacts` and
   `./run evidence-report`, and record the new pin count in `STATE.md`,
   `PROGRESS-v0.19.md`, and the pending closing record.
6. Run `./run audit-deferred` in release posture with attestations required.

**Acceptance criteria.** Hosted run pinned to the candidate · every count read
from the log and equal to local at that commit · identity set matches the derived
value · signed set committed and re-derived · new pin count in three places ·
`origin/main` unchanged, no tag · golden 11/11.

---

## Step 7 · R-CLOSE 🧑🤖

**Objective.** Close the cycle with a measured record.

**Gate.** Steps 1–6 complete and boxed. Worktree clean. **🧑 One operator
decision: publication.**

**Steps.**

1. Re-run the complete definition of done at the release commit and capture it.
2. **Record the version choice and the trigger that fired at Step 4 or Step 5.**
   The patch default is a classification, not a trigger; v0.18 established that
   distinction and it holds here.
3. Record evidence candidate and release commit as **separate named fields**,
   with the branch name matching the decided version.
4. **State the release disposition as of a date**, in the form
   `cycle_check.py`'s validator reads.
5. **Record G1's severity honestly.** The pre-fix behaviour was fail-*closed*:
   it denied access this system was entitled to and discarded a good policy. It
   never permitted a fetch a publisher had refused. **Do not describe it as a
   compliance violation, and do not describe it as cosmetic.** Retractions stay
   at three unless a measured false published claim says otherwise.
6. **Record what Step 2 changed about the project's own epistemics**: before this
   cycle, a false publication status passed every check the project runs.
7. **Record the export budget as a measured before/after**, and name the archive
   file as the new home of the moved `STATE.md` text.
8. Classify every diff path exactly once in `STATE.md`; update `CHANGELOG.md`,
   `README.md`, and the release authorities.
9. Reconcile `ARCHITECTURE.md`. **A4, the L1 controller residual, the R3/R4
   open-bottom limitations, the measured-value heuristic, and T7 robots
   single-flight must all still read as open.** Add Decision B's deferral if it
   was deferred.
10. Check R-CLOSE's box and replace the pending heading with the canonical
    `Cycle closed:` record **in one commit**, so `cycle-check` never observes an
    invalid intermediate state.
11. State the publication disposition as a decision with a trigger.
12. **Carry the one-publisher fact forward unchanged.** Three of four configured
    sources are placeholders. A second publisher remains a separate compliance
    decision and is not opened here.

---

## Cycle checklist

- [x] **E0** — entering matrix with both interpreters; G1 reproduced with fetch
  counts or refuted; G2's undetectability shown by four passing tools over a
  false `STATE.md`; G5 confirmed or closed clean; G6 answered from named tests;
  G3 byte totals recorded; `STATE.md` unedited
- [x] **STATUS-TRUE** — new check fails at the entering commit with both rule
  messages captured; focused tests including a passing case; forward publication
  append with measured refs and the CI run's id/attempt/conclusion or its
  recorded absence; no closed record edited
- [x] **EXPORT-BUDGET** — ignores added; `STATE.md` archived losslessly with a
  hash-verified concatenation; export re-run from project root; before/after
  sizes recorded; `Cargo.lock` and the pin manifest still present; 161/161 exact
- [x] **NEGATIVE-CACHE** — fail-before captured; negative TTL named and applied
  only to `Unreachable`; Decision B implemented-with-bound or
  deferred-with-trigger; the four fail-closed properties re-proven; limiter and
  ratchet untouched
- [ ] **PREVIEW-DISPOSITION** — exactly one disposition; owner named, or trigger
  named, or deletion complete; `ARCHITECTURE.md` matches
- [ ] **RE-MEASURE** — hosted run pinned; every count equals local at the same
  commit; branch named after the decided version
- [ ] **R-CLOSE** — version cites its trigger; G1's severity recorded as
  fail-closed and neither inflated nor minimised; export before/after recorded;
  all open items still open

---

## Standing prohibitions

- **Do not edit `STATE.md` before Step 2's check exists and has failed.** Its
  current falsity is the only fail-before control this cycle gets for free.
- **Do not edit any closed runbook, dated closing record, or historical
  `PROGRESS`/`STATE` append.** Every correction is a forward append. Moving text
  into `docs/state-archive/` in Step 3 is archival and must be byte-identical.
- **Do not delete a repository file to shrink the export.** Exclusion is an
  export concern; `verify-artifacts` still hashes what is on disk.
- **Do not exclude `config/protected-artifacts.json`, `Cargo.lock`, `AGENTS.md`,
  or any file under `crates/`, `apps/`, `tools/`, `shell/`.**
- **Do not run repomix from anywhere but the project root.**
- **Do not turn Step 4 into single-flight.** T7 is deferred; its trigger — a
  second concurrent harvester — has not fired.
- **Do not weaken any fail-closed property while fixing the negative cache.**
  `Unavailable` still routes through the per-source `MissingPolicy`; an explicit
  `Disallow` is still honoured; a network reach with no cache is still rejected
  before any request; the operator deny-list still only subtracts.
- **Do not touch the politeness limiter, the `apply_crawl_delay` ratchet, or
  `acquires`.**
- **Do not add a configured source.** Each new publisher is a separate
  compliance decision with its own review.
- **Do not describe G1 as a compliance violation.** It denied access; it never
  granted any.
- **Do not claim any task closes or narrows A4**, the L1 residual, the R3/R4
  open-bottom limitations, or T7.
- **Do not batch `STATE.md` / `PROGRESS-v0.19.md` updates or combine two tasks in
  one commit.**
- If any Step's Objective, Acceptance criteria, or "Done when" is amended after
  this file is first committed, name the amendment in a dated
  `## Runbook amendments` block in the same commit.

---

## Runbook amendments

### 2026-07-29 · Step 4 Gate scope correction

Step 4's original Gate omitted the one `apps/cored/src/main.rs` construction
call that must pass the named production negative TTL into `RobotsCache`, and
also omitted the status/audit records required by `AGENTS.md §5`. The Gate is
widened to those exact surfaces and now distinguishes cache construction from
the unchanged document-request and connector control flow. The Objective,
Acceptance criteria, and Done-when condition are unchanged.

---

## Execution records

### 2026-07-29 · E0

PASS. The Gate contains every acceptance surface: only this status record, the
E0 checklist box, and the append-only v0.19 progress record move; `STATE.md`
remains blob `f8f07f6944140ccc2ab4a34da2e2cf3b18767601`, byte-identical to `HEAD`.

- **Entering matrix:** the first sandboxed `./run ci-local` was a permission
  non-result when a loopback-only net test could not bind. The identical
  permitted command passed **20/20** with **131** workspace tests, **55** net
  tests (**29** `intel-ingest` + **26** `cored`), shell **245/245** under
  Python 3.11.4, zero rustc/clippy/fmt/ShellCheck failures, locked Rust 1.78,
  `invariant-scan` **11/11 rules / 23 controls**, **161/161** pins, protected
  databases **2/2**, and golden **11/11**. A clean constrained Python 3.12.13
  rebuild resolved **21/21** packages and independently passed shell
  **245/245**. Standalone `./run golden` passed **11/11**, delta **0**.
- **Refs and G2:** local and remote `origin/main` are
  `344124819cb3c554f851d0cac3f0f1ed08d1aa10`; local and remote annotated
  `v0.15.2` are object `22beef8e023e52024cfe9614273e2d82b39f4956`,
  peeled to `b3c4c4d3b695ceff27a9d4a2ec610fc851939324`, which is reachable from
  `HEAD`. This contradicts the header's asserted remote main
  `f13c6129d608ab9259f421dce6ed419ce469c225` and remote-tag absence.
  Nevertheless `cycle-check`, `checklist-audit`, `progress-check`, and
  `version-check` all passed, confirming G2 and its fail-before premise.
- **G1:** CONFIRMED by a temporary executing trait-fetcher control, then
  removed. A first `Unreachable` denial remained denied after the fake upstream
  changed to allow, with `RobotsCache::fetches()=1` and fake calls **1**. A
  cached allowing policy re-fetched after its TTL into `Unreachable`; after the
  fake upstream changed back to allow, the cache still denied with fetches
  **2** and fake calls **2**. The source blob was restored byte-identically.
- **G5:** CLOSED CLEAN as not a production defect. A temporary executing
  control passed `not-an-absolute-url` to the production network entry:
  `reqwest::Url::parse` returned `relative URL without a base` before the gate,
  with robots fetches **0** and page fetches **0**. Redirects are derived by
  `reqwest::Url::join` and rejected before the next gate when invalid; every
  URL that reaches `host_of`/`origin_of` on the network path is therefore an
  absolute `reqwest::Url`. The helper sentinels can occur only on non-network
  fixture/helper inputs and cannot key a production request. The temporary test
  was removed and the source blob restored byte-identically.
- **G6:** ANSWERED. `rate_limiter_consulted_between_pages` proves two harvest
  pages cause two limiter acquisitions, and
  `fetching_robots_txt_is_itself_rate_limited` proves the policy fetch also
  acquires the shared host limiter.
  `crawl_delay_update_preserves_clock_counter_and_waits_new_interval` measures
  an imposed publisher delay of 10 seconds, but no test measures the default
  **0.500-second** interval between harvest pages. The v0.18 live log therefore
  reported that floor; the page test proves consultation, not elapsed time.
- **G3:** CONFIRMED, with the drafted quantities corrected by execution.
  Root-run Repomix 1.17.0 collected **340** files, excluded one Rust file under
  its security scan, and wrote **4,887,220 bytes / 339 included files**
  (`4,877,747` content characters). Gitignored `.DS_Store` excluded,
  `evidence/**` contributes **1,613,565 bytes / 178 regular files**; the exact
  Step 3 closed-cycle pattern contributes **657,725 bytes / 17 files**; and
  `STATE.md` is **534,657 bytes / 8,133 lines**.
- **Final integrity:** standalone `verify-artifacts` passed **161/161** pins
  and protected databases **2/2**. The same local/remote `v0.15.2` tag object,
  peeled target, and `origin/main` were re-read after the temporary controls.
  No protected file, published object, production path, dependency, lockfile,
  schema, public surface, or `STATE.md` byte changed.

### 2026-07-29 · STATUS-TRUE

PASS. Step 2's Gate contains every acceptance surface: the reconciliation
landed inside the already-executed `cycle-check`, its focused shell tests,
`STATE.md`, and this runbook/progress status. No closed runbook, dated closing
record, historical `STATE.md` append, production Rust path, dependency,
lockfile, schema, protected database, or public surface moved.

- **Fail-before:** with the check present and `STATE.md` still unchanged,
  `./run cycle-check` exited **1** with exactly two defects:
  `publication disposition agreement` reported that reachable annotated
  `v0.15.2` contradicted the pending/outstanding header, and
  `publication assertion freshness` reported asserted `origin/main`
  `f13c6129d608ab9259f421dce6ed419ce469c225` versus measured
  `344124819cb3c554f851d0cac3f0f1ed08d1aa10`. The verbatim messages are in the
  forward `STATE.md` audit.
- **Focused controls:** `shell/tests/test_cycle_check.py` passed **20/20** on
  Python 3.11.4 and Python 3.12.13. New tests independently fail a pending
  reachable release, fail stale `origin/main`/annotated-object/tag-target
  assertions, accept current refs, and prove historical body text is excluded.
- **Forward correction:** the header and new audit name measured local/remote
  main `344124819c…`, tag object `22beef8e…`, and peeled release target
  `b3c4c4d3…`. They record the authorized atomic publication's exact remote
  postcondition and GitHub publication CI run `30375179895`, attempt **1**,
  event `push`, exact head `344124819c…`, status `completed`, conclusion
  `success`; no run was dispatched or replayed.
- **Pass-after:** `cycle-check`, `checklist-audit`, `progress-check`,
  `version-check`, and the new reconciliation all pass. `invariant-scan`
  remains **11/11 rules / 23 controls**.
- **Golden-E2E delta:** **0**; the mandatory standalone invocation passed
  **11/11**.

### 2026-07-29 · EXPORT-BUDGET

PASS. Step 3's Gate contains every acceptance surface: only the Repomix
selection, the byte-identical State archive and pointer, current status, this
runbook, and its progress audit move. No production path, dependency, lockfile,
schema, protected artifact, public surface, or repository file was deleted.

- **Before/after:** root-run Repomix 1.17.0 moved from **4,887,220 bytes /
  339 included files** (340 collected; one Rust source security-excluded) to
  **2,640,795 bytes / 146 files**. The post-export contains `Cargo.lock`,
  `config/protected-artifacts.json`, `AGENTS.md`, `run`, and all **89/89**
  tracked files under `crates/`, `apps/`, `tools/`, and `shell/`. Its security
  scan is disabled so a source cannot be silently omitted; registered
  self-testing invariant R4 remains the credential control.
- **Exact exclusions:** `evidence/**` and
  `docs/cycles/{TASKS,PROGRESS}-v0.{8,9,10,11}*` are excluded from the review
  export. The protected-artifact manifest remains included and continues to
  pin the excluded evidence bytes.
- **Lossless archive:** pre-split `STATE.md` was **535,858 bytes**, SHA-256
  `9553fb682d04e1b2a925e90bd11ab2ae867bd0e6025193abde9a643c9239f3b6`.
  The exact removed block is **297,739 bytes**, SHA-256
  `3233af5b4c148f7a7f4700edba3238dc67245f28d83dc07cc53c26ebdca6a414`,
  at `docs/state-archive/STATE-through-v0.13.md`. Replacing the retained
  pointer once with those bytes reconstructed **535,858 bytes** at the exact
  pre-split SHA-256.
- **Integrity and status:** `evidence_artifacts.py validate` and
  `verify-artifacts` passed **161/161** pins and protected databases **2/2**.
  `cycle-check`, `progress-check`, `version-check`, and Step 2's reconciliation
  pass after the split. The expected pre-audit `checklist-audit` refusal says
  only that the checked box has no progress entry yet; it is rerun after that
  entry cites the real implementation commit. `git diff --diff-filter=D` names
  no deletion.
- **Golden-E2E delta:** **0**; the mandatory standalone invocation passed
  **11/11**.

### 2026-07-29 · NEGATIVE-CACHE

PASS. The dated Gate amendment adds only the sole production cache-construction
call and the status records required to apply and audit the named TTL. No
document-request control flow, connector behavior, `/v1/*` surface, schema,
dependency, lockfile, protected artifact, limiter, crawl-delay ratchet, or
single-flight behavior moved.

- **Fail-before:** both durable controls independently exited **101** before the
  cache supported separate TTLs.
  `unreachable_retries_after_its_short_ttl_but_not_before` remained denied when
  its expected 60-second negative TTL expired, and
  `unreachable_overwrites_last_good_when_fallback_is_deferred` remained denied
  when its expected ten-second overwrite TTL expired.
- **Decision A:** `ROBOTS_NEGATIVE_TTL` is **300 seconds**, named beside the
  **86,400-second** `ROBOTS_TTL` and passed through the one production cache
  construction. RFC 9309 requires complete disallow while unreachable. Five
  minutes avoids a tight retry loop without allowing one transient failure to
  occupy the successful-policy cache's full day. Executing controls prove
  `Unavailable` keeps the ordinary TTL while only `Unreachable` expires at the
  negative boundary.
- **Decision B:** the operator selected **no fallback** on 2026-07-29. An
  unreachable result overwrites an expired good policy and denies. The
  permissive alternative is deferred until a measured live transient robots
  outage affects an admitted publisher while a usable last-known-good policy
  exists, followed by explicit operator authorization.
- **Executing results:** the retry control holds `Unavailable` at calls **1**
  beyond the negative boundary, holds `Unreachable` at calls **1** before its
  boundary, and refetches at calls **2** exactly at expiry. The overwrite
  control measures good calls **1**, unreachable calls **2**, no refetch inside
  the negative TTL, and recovery at calls **3** exactly at expiry.
- **Fail-closed preservation:** unchanged tests re-prove default 404 handling,
  explicit publisher `Disallow`, network-without-cache rejection before a
  request, and the subtractive operator deny-list. The `apply_crawl_delay`
  source slice is unchanged at SHA-256 `ea16d8cac28b094f23eba38c5656c800a79515c049b57f0a85f85abe6bd77327`;
  the complete limiter slice including `acquires` is unchanged at
  `4280d757274fd3ae739a2e600054b1fe517287cff64e56abea82176ea73c38ed`.
- **Matrix:** final `./run ci-local` passes **20/20** with **133** workspace
  tests, **55** net tests (**29 + 26**), locked warning-denied Rust 1.78,
  shell **248/248** on Python 3.11.4, invariant **11/11 rules / 23 controls**,
  all **161/161** pins, protected databases **2/2**, clippy/fmt/ShellCheck
  clean, and golden **11/11**. The constrained Python 3.12.13 lane independently
  passes **248/248**.
- **Status sequencing:** `cycle-check`, `progress-check`, and `version-check`
  pass. The expected pre-audit `checklist-audit` refusal names only the checked
  box without a progress entry; it is rerun after the real implementation
  commit is recorded.
- **Golden-E2E delta:** **0**; the mandatory standalone invocation and the final
  local matrix both passed **11/11**.

---

## Provenance of this draft

Every gate above was read out of the repomix export of the v0.15.2 tree on
2026-07-29 by path and line, and each is written as a hypothesis for E0 to
confirm or refute — not as a settled fact.

**Codex's v0.18 closing audit was independently verified and holds.** The
architectural constraints it reports as enforced are enforced: `gate()` checks
the publisher policy before the operator deny-list and both must permit
(`crates/ingest/src/lib.rs:208–235`); the robots cache and the politeness
limiter are the **same** `Arc<HostLimiters>` in production, so
`apply_crawl_delay` mutates the limiter `gate()` actually waits on
(`apps/cored/src/main.rs:196–205, 805–817`); `apply_crawl_delay` ratchets one
way only and reuses the existing per-host limiter rather than replacing it
(`crates/compliance/src/lib.rs:684–693`, `827–866`); and `/robots.txt` is
itself fetched through the limiter (`:702–704`). Codex's P2 finding on
`STATE.md` reproduces exactly at `STATE.md:3` and `STATE.md:132–134`.

The one thing the audit did not reach is the failure branch, which is what this
cycle is for.
