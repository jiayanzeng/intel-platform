# TASKS-v0.18-EXECUTION.md — the wire, not the fixture

v0.18 has one theme: **the corrected compliance gate has never met a real
`robots.txt`.**

v0.17 rewrote the robots comparison target, added `origin_of` on the RFC 9309
observation that policy is per-origin rather than per-host, made the harvest
preflight executable, and gave R11 the controls its scope claimed. Every one of
those was proven against fixtures. `AGENTS.md`'s own rule says what that is
worth: **fixtures prove the state machine, not the wire.** The gate that now
decides whether this system may fetch from a publisher has been exercised
exclusively against strings the project wrote itself.

This cycle does three things and deliberately no more:

1. **fixes case sensitivity in the two keys that govern publisher-facing
   behaviour**, so a redirect that changes host capitalisation cannot split a
   politeness bucket;
2. **evaluates the live origins offline** — fetch each configured origin's real
   `robots.txt`, run it through the shipped matcher, record the verdict, and
   harvest nothing;
3. **runs the first live harvest under the corrected gate**, and converts
   whatever it surfaces into offline regressions.

**The public `/v1/*` JSON bodies, the SQLite schema, and the golden regression's
11 invariants are unchanged. Golden stays 11/11 byte-identical through every
task. The protected corpus is not written by any step in this file.**

**Version disposition.** Default is a patch release **`v0.15.2`**. Step 2 changes
cache and limiter keying, which is a correctness fix, not a surface. **`v0.16.0`**
applies only if a `/v1/*` body or route moves. A live harvest producing documents
is **not** a version trigger — it is an observation. Record the fired trigger at
Step 7.

---

## Entering state (asserted, not yet verified)

**Every sentence here is a hypothesis until Step 1 (E0) measures it.**

- `v0.15.1` is published. Release commit
  `a0ba69e0a3e8385287274bb404d5123f9a2b8ac7`, annotated tag object
  `d6a71c1a2afabd7ce7b335756b7ae66ff36cf1ba`. v0.17 is closed 7/7 with
  `Release disposition: release (as of 2026-07-28)`. **None of this is reopened.**
- HEAD is `f13c6129d608ab9259f421dce6ed419ce469c225`.
- `./run ci-local` **20/20**; **131** workspace; **55** net (**29**
  `intel-ingest` + **26** `cored`); shell **244/244**; `invariant-scan` **11
  rules / 23 controls**; pins **146/146** (**144** evidence + **2**
  authorization); protected databases **2/2**; golden **11/11**; retractions
  **three**.
- `A4`, the **editable-L1 controller residual**, the **R3/R4 open-bottom
  limitations**, the **active-runbook measured-value heuristic**, and **T7 robots
  single-flight** remain open. **L2** remains scheduled and is not executed here.
- `ci-local` enters at 20 jobs and exits at 20.

### Gaps this runbook is drafted against (verify, do not trust)

| # | Location | Claim to verify |
|---|---|---|
| **G1** [P2] | `crates/ingest/src/lib.rs` `host_of` / `origin_of`; `gate()` calling `cache.allowed(&origin, …)` and `limiter.acquire(&host_of(url))` | **Scheme and host are compared case-sensitively.** Both are case-insensitive per RFC 3986, so `https://Example.org/a` and `https://example.org/b` produce two robots-cache entries and **two politeness buckets** — meaning the crawler can exceed its own promised rate against one publisher. Source URLs come from operator config and are consistent, but **redirect `Location` headers are publisher-controlled**, so the input is not. Confirm the keying, then confirm reachability through the redirect path. |
| **G2** [P1] | The v0.15.1 robots correction; `config/core.json` source list | **The live blast radius of the fixed defect is unquantified.** The one configured network source, `arxiv-cs`, has a **single-segment** path — for which the old `split('/').nth(3)` derivation and the new one agree. If that holds, the truncation never affected any URL this system actually fetched, and the closing record should say so. **Bounding an incident is not minimising it**; an unbounded one invites both overstatement and understatement later. |
| **G3** [P1] | `AGENTS.md` HC13; every robots test in `crates/ingest` and `crates/compliance` | **No real publisher policy has ever reached the matcher.** Wildcards, `$` anchors, `Allow` exceptions, group selection, and `Crawl-delay` are all proven against strings written by this project. |
| **G4** [P2] | `config/core.json` | **Three of four configured sources point at `example.org`.** Only `arxiv-cs` is a real publisher, so “live harvest” means one origin. Confirm, and record it as a product fact — not as something this cycle fixes. |
| **G5** [P1] | T7 robots single-flight, still deferred | **Concurrent harvesting is not coordinated.** With T7 open, more than one harvester process against one origin is not merely untested, it is unimplemented. This constrains how the live steps may be run. |
| **G6** [P3] | The audit report naming shell **244/244 on Python 3.11** | The prior release recorded both interpreters. Confirm 3.12 was exercised at this commit, or record that it was not. |

---

## How to run this file

Execute top to bottom, one task and one commit at a time. Follow `AGENTS.md §5`
after **every** task. Implementation and audit-record commits stay separate.

- **🤖 = Codex executes and self-verifies end to end** — no live model endpoint,
  no live server session, no publication, no push.
- **🧑 = exactly one named operator action or decision.** Steps 3 and 4 require
  real network egress and are the operator's to run; Codex prepares, reads, and
  records.

**Dependency gates.** Step 2 precedes Steps 3 and 4, so the live run uses the
corrected keying. **Step 4 is gated on Step 3's verdict and does not begin until
that verdict is recorded.** Step 5 is gated on Step 4. Step 6 is blocked by every
preceding implementation step; Step 7 by Step 6.

### Cycle activation (before E0)

In a separate preparatory implementation/audit pair: confirm the worktree is
clean and record the measured `origin/main`; commit **only** this runbook at
`docs/cycles/TASKS-v0.18-EXECUTION.md`, the `AGENTS.md` header declaring v0.18
active, and a new `docs/cycles/PROGRESS-v0.18.md`; run `cycle-check` and
`checklist-audit`. **Do not claim E0's acceptance from this commit.**

### Global definition of done

Protected hashes exact; all **146** pins match until Step 6 adds more; golden
**11/11 byte-identical**; `./run version-check` green; zero rustc warnings on
offline and net builds; all Rust tests green; all shell tests green under Python
3.11 **and** 3.12; clippy, fmt, ShellCheck, floor byte-compilation, and locked
Rust 1.78 green.

**No live-harvest output is promoted to evidence.** Receipts, bundles, and pins
come from authenticated CI only. A harvested document is an observation; the
durable artifact is the offline test it produces.

---

## Deferred means deferred

| Deferred item | Unchanged trigger | v0.18 action before the trigger |
|---|---|---|
| T7 robots single-flight | a second concurrent harvester | none — **and Step 4 must not create one** |
| Postgres | a second archive writer | none |
| pgvector | exact cosine stops fitting the measured request budget | none |
| Multi-host seam hardening | an actual core/shell host split | none |
| A4 untrusted-shell boundary | a third-party/untrusted shell, or any claim HC1 is invariant under shell replacement | none |
| L2 forced-command wrapper | an operator server session | none — remains scheduled |
| R3/R4 open-bottom coverage | a provider or credential spelling outside registered vocabulary | none |
| CI-runner evidence | an authenticated receipt set with identified matrix legs, durably committed | **re-measure at the new release commit — discharged by Step 6** |

---

## Step 1 · E0 — Rebuild the entering state and bound the prior incident 🤖

**Objective.** Confirm HEAD is green, settle G1 and G2, and produce the input
Step 3 needs.

**Steps.**

1. Run the full entering matrix and standalone `./run golden`, plus
   `verify-artifacts`, `cycle-check`, `checklist-audit`, `progress-check`,
   `version-check`, `invariant-scan`. **Record both Python lanes** (G6) or record
   that only one was exercised.
2. **Bound the v0.15.1 incident** (G2). For every URL this system would fetch
   from `config/core.json`, compute the comparison target under the **old**
   derivation and the **new** one, and report where they differ. State the result
   as a measured claim: either no configured source was affected, or these were.
   Do the same for the redirect path — a `Location` target with a multi-segment
   path is where the two derivations diverge even when the configured URL does
   not.
3. **Confirm G1 by construction.** Show the two keys are case-sensitive and show
   the reachable input: a redirect whose `Location` differs from the request host
   only in capitalisation. If it turns out the redirect path normalises host case
   before `gate()` sees it, **say so and close G1 as not-a-defect** — a clean
   check is a result.
4. Inventory the configured sources (G4) and record how many are real publishers.
5. Re-verify the published `v0.15.1` objects and all 146 pins unchanged.

**Acceptance criteria.** Entering matrix captured with both interpreters named ·
G2 answered as a measured comparison over configured and redirect URLs · G1
confirmed or closed clean, with the reachable input shown · source inventory
recorded · published objects and 146 pins re-verified · golden 11/11.

**Done when** the prior cycle's incident has a measured boundary and Step 2 knows
whether it has work.

---

## Step 2 · ORIGIN-CASE (G1) — Publisher keys are case-insensitive 🤖

**Objective.** Make the robots-cache key and the politeness key agree with the
URL specification, so one publisher gets one bucket.

**Gate.** `crates/ingest/src/lib.rs` and its tests. **Skip this step entirely if
E0 closed G1 clean** — record the skip with E0's finding as the reason.

**Steps.**

1. Normalise **scheme and host** to lowercase where they are used as keys.
   **Do not normalise the path**: paths are case-sensitive per RFC 3986, and
   lowercasing one would silently change robots verdicts.
2. Preserve the port and continue excluding userinfo.
3. Add tests that fail before the change: two URLs differing only in host
   capitalisation must share one robots-cache entry and one limiter bucket, and a
   redirect into a differently-cased host must not open a second bucket.
4. State whether percent-encoding in the authority is in scope. If it is not, say
   so rather than leaving it ambiguous.

**Acceptance criteria.** Case-differing hosts share one cache entry and one
limiter bucket, demonstrated fail-before/pass-after · path case unchanged, with a
test that would catch it if it were · port and userinfo behaviour unchanged ·
golden 11/11.

---

## Step 3 · ROBOTS-PREVIEW (G3) — Read the policy, fetch nothing else 🧑🤖

**Objective.** Put the shipped matcher in front of a real publisher policy
without harvesting a single document.

**Gate.** 🧑 **Operator runs the network step.** Codex prepares the command,
reads the output, and records. **This step fetches `robots.txt` and nothing
else.**

**Steps.**

1. Codex prepares a read-only preview that, for each configured network source:
   fetches only that origin's `/robots.txt`, parses it with the **shipped**
   `intel-compliance` parser under the **installed** crawler User-Agent, and
   prints the verdict for the configured URL, the matched rule, and any
   `Crawl-delay`. **Reuse the shipped matcher — a reimplementation would preview
   a different program than the one that will run.**
2. Record the raw `robots.txt` bytes and their SHA-256 alongside the verdict.
   Publisher policies change; a verdict without the bytes it was computed from
   is not reproducible.
3. **Record what the policy says about the group actually selected**: which
   product token matched, whether it was the specific group or the `*` fallback,
   and whether any `Allow` carved an exception.
4. **This step's output is a decision, not a formality.** If the configured URL
   is disallowed, **Step 4 does not run**, and that is a successful cycle: the
   gate did its job and the finding is that this source is not harvestable as
   configured. Record it and stop at Step 5.
5. If the origin serves no `robots.txt`, record which `MissingPolicy` applies and
   what the gate will therefore do.

**Acceptance criteria.** Verdict recorded per configured network source, with the
raw policy bytes and their hash · the matched group and rule named · the
`Crawl-delay`, if any, recorded · a written go/no-go for Step 4 · **no request
issued to any path other than `/robots.txt`** · golden 11/11.

**Done when** the matcher's first contact with a real policy is on the record.

---

## Step 4 · LIVE-HARVEST (G3, G5) — The first harvest under a correct gate 🧑🤖

**Objective.** Exercise what fixtures cannot: paging, `resumptionToken`, cursor
durability, real XML shapes, redirects, and adherence to a published
`Crawl-delay`.

**Gate.** 🧑 **Operator runs the harvest.** **Blocked on Step 3's go verdict.**

**Steps.**

1. Run `./run harvest-arxiv` with the **default fresh harvest database**. **Do
   not set `CORE_DB` to the golden corpus or any protected path** — the preflight
   and `refuse_protected_harvest` should both stop that, and neither is a reason
   to try it.
2. **Exactly one harvester process against one origin, start to finish** (G5).
   T7 single-flight is unimplemented; concurrency here would be running a
   deferred design's trigger conditions on purpose.
3. **Honour the observed `Crawl-delay` from Step 3.** If the run would exceed it,
   stop the run rather than the clock.
4. Record what the wire showed and fixtures could not: the number of `ListRecords`
   pages, whether `resumptionToken` appeared and was followed correctly, whether
   the cursor survived across the run, any redirect encountered and the origin it
   led to, any HTTP status other than 200, any XML shape the parser did not
   expect, documents fetched, documents retained after near-duplicate
   suppression, and wall-clock duration.
5. **Record surprises as surprises.** Anything that differs from what the
   fixtures model is this cycle's actual product, more valuable than a clean run.
6. **Do not tune anything mid-run** to make the numbers nicer. A run that reveals
   a defect is the successful outcome.

**Acceptance criteria.** Harvest ran against an isolated database with the
protected corpus untouched, verified by hash after · exactly one harvester
process · observed `Crawl-delay` honoured, or the run stopped · paging,
`resumptionToken`, cursor, redirect, and XML observations recorded · document
counts recorded as observations, not pins · `./run verify-artifacts` green after
the run · golden 11/11.

---

## Step 5 · WIRE-FINDINGS — Turn observations into regressions 🤖

**Objective.** Make Step 4's findings durable. A harvest is a hypothesis
generator; the tests are what survive.

**Gate.** Offline. Whatever crates Step 4's findings implicate.

**Steps.**

1. For each finding, decide exactly one disposition: **fixed with an offline
   regression test**, or **deferred with a named trigger** in the deferral table.
   Nothing may be recorded as merely observed.
2. Where a real XML shape, status code, or redirect differed from the fixtures,
   add that shape to the fixture corpus so it can never surprise again.
3. **If Step 4 produced no findings, say so in one sentence and close the step
   empty.** An empty Step 5 is a valid outcome and a meaningful one — it means the
   fixtures were faithful. Do not manufacture work to fill it.
4. Do not import harvested documents into the golden corpus. Golden's 11
   invariants are unchanged by this cycle.

**Acceptance criteria.** Every Step 4 finding carries exactly one disposition ·
new fixtures derived from real observed shapes · no harvested document enters the
protected corpus · golden 11/11 byte-identical · full matrix green.

---

## Step 6 · RE-MEASURE 🤖🧑

**Objective.** Produce release-grade hosted evidence for the v0.18 candidate.

**Gate.** 🧑 **One narrow authorization: a non-`main` branch push.** No tag, no
`main` advance, no publication.

**Steps.**

1. Push the candidate to `candidate/<version the trigger sets>`. **Name the
   branch after the decided version, not before the decision** — the prior cycle
   pushed `candidate/v0.16.0` for what was a patch.
2. **Read the remote branch's `ci.yml` and confirm it contains every invocation
   you expect before dispatching.**
3. Dispatch with `publish_evidence: true` and `audit_sha` set to the candidate.
4. **Read every count out of the hosted log**, not from job status, and compare
   each against the local measurement **at the same commit**. That equality is the
   criterion, not any number written earlier in this file.
5. Commit the signed receipt/bundle set, re-run `./run verify-artifacts` and
   `./run evidence-report`, and record the new pin count in `STATE.md`,
   `PROGRESS-v0.18.md`, and the pending closing record.
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
2. Record the version choice and the trigger that fired.
3. Record evidence candidate and release commit as **separate named fields**,
   with the branch name matching the decided version.
4. **State the release disposition as of a date**, in the form read from
   `cycle_check.py`'s validator.
5. **Record the bounded scope of the v0.15.1 robots incident** from E0 — which
   configured URLs were and were not affected. Correct forward; retractions stay
   at three unless a measured false published claim says otherwise.
6. **Record the live-harvest result as a first**: the first harvest this project
   has run under a gate that enforces the policy it claims to. Include the
   policy bytes' hash from Step 3.
7. Classify every diff path exactly once in `STATE.md`; update `CHANGELOG.md`,
   `README.md`, and the release authorities.
8. Reconcile `ARCHITECTURE.md`. **A4, the L1 controller residual, the R3/R4
   open-bottom limitations, the measured-value heuristic, and T7 robots
   single-flight must all read as open.**
9. Check R-CLOSE's box and replace the pending heading with the canonical
   `Cycle closed:` record **in one commit**.
10. State the publication disposition as a decision with a trigger.
11. **Record the one-real-source fact** (G4) as an open product question for a
    later cycle: three of four configured sources are placeholders, so this
    platform currently aggregates one publisher. **Do not add sources here** —
    each new publisher is its own compliance decision.

---

## Cycle checklist

- [ ] **E0** — entering matrix with both interpreters; G2 bounded by measured
  comparison over configured and redirect URLs; G1 confirmed or closed clean;
  source inventory recorded
- [ ] **ORIGIN-CASE** — case-differing hosts share one cache entry and one limiter
  bucket, fail-before/pass-after; path case untouched — or the step skipped with
  E0's clean finding as the reason
- [ ] **ROBOTS-PREVIEW** — real policy fetched, verdict and matched rule recorded
  with the raw bytes and hash; written go/no-go; nothing but `/robots.txt`
  requested
- [ ] **LIVE-HARVEST** — isolated database, protected corpus hash-verified after;
  one process; `Crawl-delay` honoured; paging, `resumptionToken`, cursor,
  redirect, and XML observations recorded
- [ ] **WIRE-FINDINGS** — every finding fixed with a regression or deferred with a
  trigger; or an explicit empty close
- [ ] **RE-MEASURE** — hosted run pinned; every count equals local at the same
  commit; branch named after the decided version
- [ ] **R-CLOSE** — version cites its trigger; v0.15.1 incident scope recorded;
  live-harvest first recorded with the policy hash; all open items open

---

## Standing prohibitions

- **Do not harvest before Step 3 returns a go verdict.** The point of a gate is
  that it is consulted before the fetch, not explained after it.
- **Do not run two harvester processes against one origin.** T7 single-flight is
  deferred and unimplemented; concurrency would be executing a deferred design's
  trigger conditions deliberately.
- **Do not point a harvest at the protected corpus or any protected path**, and
  do not work around `refuse_protected_harvest` or the preflight.
- **Do not promote harvested output to evidence.** Receipts, bundles, and pins
  come from authenticated CI only. A harvested document is an observation.
- **Do not import harvested documents into the golden corpus.** Golden's 11
  invariants are unchanged by this cycle.
- **Do not tune a live run mid-flight to improve its numbers.** A run that
  reveals a defect has succeeded.
- **Do not add a configured source.** Each new publisher is a separate compliance
  decision with its own review.
- **Do not lowercase URL paths.** Scheme and host are case-insensitive; paths are
  not, and normalising them would silently change robots verdicts.
- **Do not reimplement the matcher for the preview.** A preview that runs
  different code previews a different program.
- **Do not claim any task closes or narrows A4**, the L1 residual, the R3/R4
  open-bottom limitations, or **T7 robots single-flight**.
- **Do not manufacture findings to fill Step 5.** An empty step, stated plainly,
  is a result.
- **Do not predict a count this file has not measured.** Where a quantity is
  needed, state the relation instead.
- **Do not delete or hand-edit `Cargo.lock`** (HC12); do not raise the offline
  Rust 1.78 floor or lower the Python 3.11 floor.
- **Do not run a live server session.** L2 remains scheduled.
- Do not change the public `/v1/*` JSON bodies, the SQLite schema, or the golden
  regression's 11 invariants.
- Do not commit `.env`, provider keys, tokens, or private key material.
- Do not batch `STATE.md` / `PROGRESS-v0.18.md` updates or combine two tasks in
  one commit.
