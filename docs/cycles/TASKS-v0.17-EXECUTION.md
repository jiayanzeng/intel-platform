# TASKS-v0.17-EXECUTION.md — compliance-surface runbook for Codex

v0.17 has one theme, and it is the project's oldest one turned on the product:
**a claimed property that nothing executes is not a property.**

v0.16 applied that to the harness — a runner whose jobs could not fail, a
parity rule whose exemptions were asserted, a document location restated at
every consumer. This cycle's audit found the same shape three layers into the
product itself:

- a doc comment above `robots_path_of` states that robots patterns are matched
  against path **plus query**; the code returns the **first path segment**;
- `AGENTS.md` requires `./run verify-artifacts` before every live harvest; the
  harvest entry point performs a different check and relies on the operator
  remembering;
- **R11**'s declared scope names four config spellings plus module-local derived
  variables; one control executes one of them.

Each is a sentence with nothing behind it.

## Read this before anything else

**Do not run a live harvest until Step 3 lands.**

`gate()` calls `robots_path_of()` before **every** fetch, and the function
returns only the first path segment. A publisher rule `Disallow: /private/secret`
does not prefix-match the truncated `/private`, so the fetch is **allowed**. The
failure is **fail-open, and only for multi-segment rules** — single-segment rules
still match, which is why nothing caught it. This is not merely a bug in a
crawler; it is a gate that does not enforce the publisher policy it claims to
honor, on a system that fetches from real publishers over real network egress.
Suspending live harvest is cheap. Fetching a page a publisher disallowed is not
retractable.

This cycle does four things and deliberately no more:

1. **turns the ingest net lane green**, because until `./run ci-local` completes,
   nothing else in this runbook can be verified end to end;
2. **derives the robots path from a parsed URL**, fixing the parsing class rather
   than the one function;
3. **makes the live-harvest preflight executable** at the entry point;
4. **gives R11 the control breadth its scope claims.**

**The public `/v1/*` JSON bodies, the SQLite schema, and the golden regression's
11 invariants are unchanged. Golden stays 11/11 byte-identical through every
task.**

**Version disposition.** Default is a patch release **`v0.15.1`**: Step 3 changes
live-harvest behaviour by refusing URLs that were previously fetched, which is a
correctness fix, not a new surface. **`v0.16.0`** applies only if a `/v1/*` body
or route moves. **A new third-party dependency is not by itself a version
trigger.** Record the fired trigger at Step 7.

---

## Entering state (asserted, not yet verified)

**Every sentence here is a hypothesis until Step 1 (E0) measures it.** The prior
cycle's runbook carried a stale `origin/main`; do not assume this one is better.

- `v0.15.0` is published. Annotated tag object
  `b7ee3445728e1816e1622c9498ffc2f165ed5dd5` dereferences to release commit
  `8f97205a3ed4fe82f6a5ede2febce7a5d82d9f81`. `origin/main` is
  `cdae3c922a2156701c0df0ceb4f45fc937fa7f20`; publication CI **30350691515** and
  publication-audit CI **30350848907** both passed. Release evidence remains
  dispatch run **30347262430** attempt 1 against the separate evidence candidate
  `43706216c06608039d9c3e7ef2b86024b22d4a79`. **None of this is reopened.**
- v0.16 is closed: 8/8 boxes, `Cycle closed: 2026-07-28`,
  `Release disposition: release (as of 2026-07-28)`.
- **At the release commit:** `./run ci-local` **20/20**; **126** workspace;
  **49** net (**23** `intel-ingest` + **26** `cored`); shell **243/243** on
  Python 3.11.4 and 3.12.13; `invariant-scan` **11 rules / 19 controls**; pins
  **131/131** (**129** evidence + **2** authorization); protected databases
  **2/2**; golden **11/11**; retractions **three**.
- **At HEAD today:** the ingest net lane reports **22 passed / 1 failed** and
  `ci-local` stops at job **11/20**. Every other independently exercised job
  passes. **The repository is not currently green.**
- `A4`, the **editable-L1 controller residual**, the **R3/R4 open-bottom
  limitations**, the **active-runbook measured-value heuristic**, and **R11's
  control-breadth gap** all remain open. **L2** remains scheduled and is not
  executed in this cycle.
- `ci-local` enters at 20 jobs and exits at 20.

### Gaps this runbook is drafted against (verify, do not trust)

| # | Location | Claim to verify |
|---|---|---|
| **F1** [P1] | `crates/ingest/src/lib.rs:109` `robots_path_of` → `url.split('/').nth(3)`; called from `gate()` at `lib.rs:170` | **The robots path is truncated to its first segment.** `https://example.org/private/secret/file` yields `/private`, so `Disallow: /private/secret` does not match and the fetch is allowed. Fragments are also carried into the compared path, and the query survives only when the path has no second segment. |
| **F1a** [P1] | `crates/ingest/src/net.rs` redirect loop | **The blast radius is wider than the audit stated.** `gate()` is called at the top of the loop, so it runs before the **first** fetch as well as before each redirect. Every gated fetch is affected, not only redirects. Confirm. |
| **F1b** [P1] | `lib.rs:107-108` doc comment | **The comment contradicts the code it documents**, claiming path-plus-query matching with the query string included. Whichever way the fix goes, the comment and the code must end up saying the same thing. |
| **F1c** [P2] | `lib.rs` robots tests using `Disallow: /`, `/techwire`, `/admin` | **No existing test uses a multi-segment rule.** The corpus is shaped so the defect cannot appear — a test set that cannot fail. Confirm, then fix the corpus, not just the function. |
| **F1d** [P2] | `lib.rs:117` `host_of` → `url.split('/').nth(2)` | **Sibling instance of the same class.** Hand-rolled parsing by string splitting; a URL carrying a query but no path (`https://host?a=b`) yields a host of `host?a=b`. Classify it; fix it or state why not. |
| **F2** [P1] | `crates/ingest/src/net.rs:392` `user_agent_wire_server`; test at ~441 | **The raw TCP double fails reproducibly on the operator's platform** with “connection closed before message completed”, blocking the mandatory ingest net lane. The double writes the response, `shutdown(Shutdown::Write)`s, then drops the stream at the end of the loop iteration. A close with unread bytes still queued produces an RST rather than a FIN on some platforms, which discards response bytes the client has not yet read. **That is a hypothesis, not a diagnosis — measure the mechanism.** |
| **F3** [P2] | `run`'s `cmd_harvest_arxiv` calling `refuse_protected_harvest`; `AGENTS.md:304` | **The contract requires a preflight the entry point does not perform.** Refusing a protected *destination* and verifying protected artifact *bytes* are different controls. The requirement is currently satisfied only by the operator remembering. |
| **F4** [P2] | `config/invariant-rules.json` R11, one `fail_before` entry | **R11's scope claims four spellings** — `config/core.json`, `config/entities.json`, `CORE_CONFIG`, `CORE_ENTITIES` — **plus module-local derived variables. One control exercises one of them.** R5, R7, R8, and R10 each carry three. |
| **F5** [P1] | `crates/ingest/Cargo.toml`: `reqwest` is `optional`, enabled only by the `net` feature; `lib.rs` compiles without it | **The obvious fix does not compile.** `robots_path_of` lives in the feature-free part of the crate, so `reqwest::Url` is unavailable there. Adding the `url` crate instead risks the **Rust 1.78 MSRV floor**: this project has already measured that `idna`/`icu_*` version selection breaks low MSRVs. Measure before choosing. |

---

## How to run this file

Execute top to bottom, one task and one commit at a time. Follow `AGENTS.md §5`
after **every** task. Implementation and audit-record commits stay separate. Do
not batch status updates.

- **🤖 = Codex executes and self-verifies end to end** — no live model endpoint,
  no live server session, **no live harvest**, no publication, no push.
- **🧑 = exactly one named operator action or decision.**

**Dependency gates.** Step 2 runs first: until the ingest net lane is green,
`./run ci-local` cannot complete and no later step can produce a full-matrix
acceptance. Steps 3, 4, and 5 are independent and may run in any order after
Step 2. Step 6 is blocked by every preceding implementation step. Step 7 is
blocked by Step 6.

### Cycle activation (before E0)

In a separate preparatory implementation/audit pair: confirm the worktree is
clean and record the measured `origin/main`; commit **only** this runbook at
`docs/cycles/TASKS-v0.17-EXECUTION.md`, the `AGENTS.md` header declaring v0.17
active, and a new `docs/cycles/PROGRESS-v0.17.md`; run `cycle-check` and
`checklist-audit`. **Do not claim E0's acceptance from this commit.**

### Session opener

```bash
git status --porcelain=v1
git rev-parse HEAD origin/main
git tag --list 'v0.15*' --format='%(refname:short) %(objectname) %(*objectname)'
bash --version | head -1
rustc --version && cargo --version
sed -n '1,20p' AGENTS.md
sed -n '1,6p' STATE.md
```

### Global definition of done

Protected hashes exact; all **131** pins match until Step 6 adds more; golden
**11/11 byte-identical**; `./run version-check` green; zero rustc warnings on
offline and net builds; all Rust tests green; all shell tests green under Python
3.11 **and** 3.12; clippy, fmt, ShellCheck, floor byte-compilation, and locked
Rust 1.78 green. No mock, fixture, double, health response, hand-authored
receipt, or workflow configuration is promoted to wire evidence.

`invariant-scan` enters at **11 rules / 19 controls**. **Every count after Step 5
is measured and recorded by the step that produces it, never predicted here.**

---

## Deferred means deferred

| Deferred item | Unchanged trigger | v0.17 action before the trigger |
|---|---|---|
| T7 robots single-flight | a second concurrent harvester | none — **Step 3 fixes path derivation, not concurrency** |
| Postgres | a second archive writer | none |
| pgvector | exact cosine stops fitting the measured request budget | none |
| Multi-host seam hardening | an actual core/shell host split | none |
| A4 untrusted-shell boundary | a third-party/untrusted shell, or any claim HC1 is invariant under shell replacement | none |
| L2 forced-command wrapper | an operator server session | none — remains scheduled, not executed |
| R3/R4 open-bottom coverage | a provider or credential spelling outside registered vocabulary | none — stated limitations stand |
| CI-runner evidence | an authenticated receipt set with identified matrix legs, durably committed | **re-measure at the new release commit — discharged by Step 6** |

---

## Step 1 · E0 — Rebuild the entering state and confirm F1–F5 🤖

**Objective.** Establish what is true at HEAD before changing anything, and
settle the two questions that decide this cycle's shape: whether the net-lane
failure is platform-deterministic or flaky, and whether any **published** record
makes a false completeness claim about robots enforcement.

**Steps.**

1. Run every job `ci-local` can reach, plus standalone `./run golden`,
   `verify-artifacts`, `cycle-check`, `checklist-audit`, `progress-check`,
   `version-check`, `invariant-scan`. Record the `CARGO_TARGET_DIR` used and the
   exact job at which `ci-local` stops.
2. **Characterise F2 before fixing it.** Run the failing test **at least ten
   times** on the operator's platform and record the failure rate. Determine
   whether it also fails at the **release commit** `8f97205a…` on this machine —
   that separates “post-release drift” from “this platform was never green.”
   Confirm the hosted lane still passes at the same commit. **A flake and a
   platform-deterministic failure call for different fixes; say which this is.**
3. **Measure the F2 mechanism, do not assume it.** Capture whether the client
   sees a FIN or an RST, and whether bytes remain queued on the server socket at
   close. The hypothesis in the F2 row is a starting point to be confirmed or
   discarded, not a conclusion to implement against.
4. **Reproduce F1 by table, not by example.** Build a case table over the
   distinguishing inputs — multi-segment path, path with query, path with
   fragment, path with both, no path, trailing slash, port, userinfo,
   percent-encoding, `//` in path — and record current output for each. That
   table is Step 3's specification.
5. **Confirm F1a**: show that `gate()` runs before the first fetch, not only on
   redirect. **Confirm F1c**: show that no existing robots test uses a
   multi-segment rule.
6. **Settle the published-record question.** Search the published records —
   `CHANGELOG.md`, tagged `STATE.md`, closed progress logs — for any claim that
   robots enforcement is **complete**, as opposed to a scoped statement that a
   given audit found no violation. **These are different sentences and only the
   first would be false.** If a completeness claim exists in an immutable
   published record, the retraction bar applies: verify twice, and treat moving
   the retraction count off three as a decision, not a formality. A doc comment
   inside source is corrected forward and is not a retraction.
7. **Measure F5's cost.** Determine what adding `url` (or an equivalent) does to
   the locked dependency graph under Rust **1.78**, without committing the
   result. Record the versions that resolve and whether any transitive crate
   declares a `rust-version` above the floor. **Do not delete `Cargo.lock` to
   resolve anything** (HC12).
8. Re-verify the published `v0.15.0` tag, release commit, `origin/main`, and all
   131 pins unchanged.

**Acceptance criteria.** Entering matrix captured with its stopping point and
target directory · F2 failure rate measured over ≥10 runs and classified · F2
mechanism measured · F1 case table produced · F1a and F1c confirmed or refuted ·
published-record question answered in writing with the distinction named · F5
cost measured under 1.78 with the lockfile untouched · published `v0.15.0`
objects and 131 pins re-verified · golden 11/11.

**Done when** Step 3 has a specification and Step 2 has a diagnosis.

---

## Step 2 · NET-DOUBLE (F2) — Turn the mandatory lane green 🤖

**Objective.** Make the ingest net lane pass on the operator's platform without
weakening what its test proves.

**Gate.** `crates/ingest/src/net.rs` test support only. **No product path
changes.** If a fix requires touching product code, stop and report — that would
mean the defect is not in the double.

**Steps.**

1. Fix the mechanism E0 measured. Candidate directions, in preference order —
   **choose on evidence, not on this ordering**: drain the client socket to EOF
   before dropping the stream so no unread bytes force an RST; close the read and
   write halves explicitly in the order the measurement indicates; handle a
   connection that closes before sending complete headers as a skipped
   connection rather than a panic, instead of consuming one of the `take(n)`
   slots.
2. **Preserve what the test is for.** It exists to prove both live clients put
   **byte-identical** `User-Agent` bytes on the wire. Do not replace the raw
   socket with an HTTP framework that normalizes headers — that would make the
   test pass by removing its subject.
3. Demonstrate the fix against the measurement: the recorded failure rate before,
   and a clean run of the same size after. **A single green run is not evidence
   against a rate.**
4. State plainly whether the fix is platform-general or specific to the observed
   behaviour, and what would make it fail again.

**Acceptance criteria.** The failing test passes at the same repetition count E0
used to measure it · the byte-identical `User-Agent` assertion is intact and
still capable of failing, shown by a deliberate mismatch · no product path
changed · `cargo test -p intel-ingest --features net --locked` green · full
`ci-local` reaches job 20 · golden 11/11.

**Done when** `./run ci-local` completes on the operator's platform.

---

## Step 3 · ROBOTS-PATH (F1, F1a, F1b, F1c, F1d) — Derive the path, do not slice it 🤖

**Objective.** Make the robots comparison operate on the URL the publisher's
policy is written against.

**Gate.** `crates/ingest/src/lib.rs` and its tests;
`crates/ingest/src/net.rs` test support only for the redirect acceptance
criterion; `crates/ingest/Cargo.toml` only if Step 1 concluded a dependency is
the right answer. **This is a compliance-surface change: it is expected to
refuse URLs that were previously fetched. That is the fix, not a regression.**

**Steps.**

1. **Choose the derivation strategy against F5's measurement.** Either add a
   parsing dependency that resolves under Rust 1.78 with the lockfile committed
   and `--locked` honoured, or implement the derivation in-crate. If in-crate,
   the implementation is only acceptable with the full case table from E0 as
   executing tests — hand-rolled parsing without property coverage is what
   produced this defect.
2. Derive **path plus query, excluding the fragment**, from the parsed URL.
   Percent-encoding and an empty path must both behave predictably; state the
   chosen behaviour for each row of the case table.
3. **Fix `host_of` in the same commit or state why not** (F1d). It is the same
   class in the same file; leaving it means the class was not fixed.
4. **Make the comment and the code agree** (F1b). Whichever behaviour ships, the
   doc comment states exactly that and nothing more.
5. **Fix the corpus, not just the function** (F1c). Add robots tests with
   multi-segment `Disallow` rules that **fail before the change and pass after**,
   including at least: a multi-segment rule that must block, a multi-segment rule
   that must not block a sibling path, a rule against a path carrying a query,
   and a URL carrying a fragment.
6. **Confirm the redirect path** (F1a): the gate applies to the first URL and to
   each redirect target, demonstrated by a test with a cross-origin redirect into
   a multi-segment disallowed path.
7. Consider whether this belongs as an `invariant-scan` rule. **The default is
   no** — this is behaviour that tests can exercise directly, and a rule that
   restates a tested property adds apparatus without adding coverage. If you
   register one anyway, it carries at least three site-specific controls.
8. **Do not claim this closes T7 robots single-flight.** That deferral is about
   concurrent fetch coordination; this is path derivation. Different items.

**Acceptance criteria.** Every E0 case-table row has a stated, tested output ·
multi-segment `Disallow` rules block, demonstrated fail-before/pass-after ·
fragments excluded, query included · redirect targets gated on the corrected path
· `host_of` fixed or explicitly deferred with a reason · doc comment matches
behaviour · MSRV 1.78 green with `Cargo.lock` committed and `--locked` honoured ·
**golden 11/11 byte-identical** · T7 unchanged and still deferred.

**Done when** a publisher rule the crawler can read is a rule the crawler obeys.

---

## Step 4 · HARVEST-PREFLIGHT (F3) — Make the contract executable 🤖

**Objective.** Stop the artifact-integrity preflight from depending on the
operator's memory.

**Gate.** `run`, its harness tests, and only the `run` authorization pin's
hash/size/provenance in `config/protected-artifacts.json` after proving the
model-profile command surface unchanged. Offline-provable — **no live harvest
is run in this cycle.**

**Steps.**

1. Invoke the artifact verification at the `cmd_harvest_arxiv` entry point,
   **before** any reachability probe or network request. Failure aborts before
   the first outbound packet.
2. **Keep the two controls distinct in the record.** Refusing a protected
   destination and verifying protected bytes are separate checks with separate
   failure messages; do not let one absorb the other.
3. Derive the requirement from `AGENTS.md` rather than restating it: if any other
   entry point is covered by the same rule, find it by search and cover it too,
   or record that harvest is the only one.
4. Add a control that fails when the preflight is removed, and make it part of
   the shell suite so `ci-local` executes it.

**Acceptance criteria.** Verification precedes reachability and harvest, shown by
ordering in a test · a removed preflight fails a test naming the entry point ·
both controls remain separately identifiable · every entry point the rule covers
is covered or the singleton is recorded · `ci-local` still **20** jobs · golden
11/11.

**Done when** the sentence in `AGENTS.md` is enforced by something that runs.

---

## Step 5 · R11-BREADTH (F4) — The controls match the scope 🤖

**Objective.** Discharge the limitation v0.16 recorded as v0.17's first task.

**Gate.** `config/invariant-rules.json`, `tools/invariant_scan.py` if the rule
schema needs it, the invariant tests, and `ARCHITECTURE.md` for the required
limitation reconciliation.

**Steps.**

1. Add controls for the spellings R11's scope claims and does not exercise:
   `config/core.json`, `CORE_CONFIG`, `CORE_ENTITIES`, and the **module-local
   variable derived from one of those names**. The last is the one most likely to
   be uncovered in practice; do not skip it because it is the hardest.
2. Each control names its file and expected line, in the form the existing rules
   use.
3. **If a claimed spelling cannot be given an executing control, narrow the
   scope sentence instead of leaving the claim unbacked.** A smaller true claim
   beats a larger asserted one.
4. Update `ARCHITECTURE.md`: if the gap closes, remove the limitation and say
   what discharged it; if it narrows, restate what remains open.
5. Measure and record the resulting rule and control counts.

**Acceptance criteria.** Every spelling in R11's scope has an executing control
or the scope is narrowed to match · all controls demonstrated fail-before ·
`--self-test` green across all rules · `ARCHITECTURE.md` reconciled · measured
counts recorded in `STATE.md` and `PROGRESS-v0.17.md` · golden 11/11.

**Done when** R11's scope sentence and its control set describe the same rule.

---

## Step 6 · RE-MEASURE 🤖🧑

**Objective.** Produce release-grade hosted evidence for the v0.17 candidate.

**Gate.** 🧑 **One narrow authorization: a non-`main` branch push.** Scope is
the exact candidate ref and remote workflow, hosted logs, the signed
receipt/bundle set, release-grade audit report, protected-file manifest,
`STATE.md`, this active runbook's gate/amendment/checklist/pending-closing
records, and the later append-only progress entry. No tag, no `main` advance,
no publication, and no closed runbook or progress-log edit.

**Steps.**

1. Push the candidate to `candidate/<version decided at Step 7's trigger>`.
   Record branch and commit.
2. **Read the remote branch's `ci.yml` and confirm it contains every invocation
   you expect before dispatching.**
3. Dispatch with `publish_evidence: true` and `audit_sha` set to the candidate.
4. **Read every count out of the hosted log**, not from job status: workspace,
   both net legs, both shell legs, rule and control counts, R10's derived
   exemption count, and golden. Compare each against the local measurement **at
   the same commit** — that equality is the criterion, not any number written
   earlier in this file.
5. **Confirm the ingest net lane passes hosted and locally at the same commit.**
   That equality is this cycle's specific evidence that Step 2 fixed the double
   rather than hiding it.
6. Commit the signed receipt/bundle set, re-run `./run verify-artifacts` and
   `./run evidence-report`, and record the new pin count in `STATE.md`,
   `PROGRESS-v0.17.md`, and the pending closing record.
7. Run `./run audit-deferred` in release posture with attestations required.

**Acceptance criteria.** Hosted run pinned to the candidate · every count read
from the log and equal to local at that commit · ingest net lane green in both ·
identity set matches the derived value · signed set committed and re-derived ·
new pin count in three places · `origin/main` unchanged, no tag · golden 11/11.

---

## Step 7 · R-CLOSE 🧑🤖

**Objective.** Close the cycle with a measured record.

**Gate.** Steps 1–6 complete and boxed. Worktree clean. **🧑 One operator
decision: publication.**

**Steps.**

1. Re-run the complete definition of done at the release commit and capture it.
2. Record the version choice and the trigger that fired.
3. Record evidence candidate and release commit as **separate named fields**.
4. **State the release disposition as of a date**, in the form read from
   `cycle_check.py`'s validator.
5. **Record the robots-gate correction honestly.** State what the gate did not
   enforce, from which release, and what it enforces now. Apply E0's
   published-record finding: correct forward unless a published completeness
   claim was measured to be false, in which case a retraction is a separate,
   twice-verified decision that moves the count off three.
6. **Lift the live-harvest suspension explicitly**, citing Step 3's acceptance —
   or state that it stands and why.
7. Classify every diff path exactly once in `STATE.md`; update `CHANGELOG.md`,
   `README.md`, and the release authorities.
8. Reconcile `ARCHITECTURE.md`. **A4, the L1 controller residual, the R3/R4
   open-bottom limitations, the measured-value heuristic, and R11's residual if
   Step 5 narrowed rather than closed it, must all read as open.**
9. Check R-CLOSE's box and replace the pending heading with the canonical
   `Cycle closed:` record **in one commit**.
10. State the publication disposition as a decision with a trigger.

**Acceptance criteria.** Version cites its trigger · candidate and release commit
separate · disposition dated · robots correction recorded with its scope and
first affected release · harvest suspension lifted or restated · every diff path
classified · `ARCHITECTURE.md` matches enforced reality · all pins match · golden
11/11.

---

## Cycle checklist

- [x] **E0** — entering matrix with its stopping point; F2 rate measured over ≥10
  runs and classified; F2 mechanism measured; F1 case table built; F1a and F1c
  settled; published-record question answered; F5 MSRV cost measured
- [x] **NET-DOUBLE** — failing test green at the measured repetition count; the
  byte-identical assertion still able to fail; no product path changed
- [x] **ROBOTS-PATH** — every case-table row tested; multi-segment rules block
  fail-before/pass-after; fragment excluded, query included; redirects gated;
  `host_of` fixed or deferred with a reason; comment matches code; golden
  byte-identical
- [x] **HARVEST-PREFLIGHT** — verification precedes reachability; removal fails a
  test; both controls separately identifiable
- [x] **R11-BREADTH** — every claimed spelling controlled or the scope narrowed;
  `ARCHITECTURE.md` reconciled
- [x] **RE-MEASURE** — hosted run pinned; every count equals local at the same
  commit; ingest net lane green in both
- [ ] **R-CLOSE** — version cites its trigger; robots correction recorded; harvest
  suspension resolved; all open items open

---

## Standing prohibitions

- **No live harvest until Step 3 is accepted.** The gate does not enforce
  multi-segment publisher rules; a fetch made under it is not retractable.
- **Do not touch published releases.** `v0.15.0`, `v0.14.1`, `v0.14.0`,
  `v0.13.0`, `v0.12.0`, `v0.11.0`, `v0.10.3`, and unpublished `v0.10.2` are
  immutable — tags, commits, pins, receipts.
- **Do not retract on inference.** A scoped audit statement that no violation was
  found is not a completeness claim. Only a measured false completeness claim in
  an immutable published record justifies a retraction, and only after verifying
  twice.
- **Do not fix F1 at the one call site.** The class is hand-rolled URL parsing by
  string splitting; `host_of` is its sibling.
- **Do not make the net test pass by removing its subject.** Any double that
  normalizes headers instead of exposing wire bytes fails this step even if it is
  green.
- **Do not treat one green run as evidence against a measured failure rate.**
- **Do not delete or hand-edit `Cargo.lock`** (HC12). If a dependency will not
  resolve under Rust 1.78, that is a finding to report, not a lockfile to remove.
- **Do not raise the offline Rust 1.78 floor** or lower the Python 3.11 floor.
- **Do not claim any task closes or narrows A4**, the L1 residual, the R3/R4
  open-bottom limitations, or **T7 robots single-flight**. Step 3 fixes path
  derivation, not concurrency.
- **Do not add an `invariant-scan` rule without at least three site-specific
  controls**, and do not register one that merely restates a directly tested
  property.
- **Do not predict a count this file has not measured.** Where a quantity is
  needed, state the relation instead.
- **Do not run a live server session.** L2 remains scheduled.
- Do not change the public `/v1/*` JSON bodies, the SQLite schema, or the golden
  regression's 11 invariants. Golden stays 11/11 after **every** task.
- Do not commit `.env`, provider keys, tokens, or private key material.
- Do not batch `STATE.md` / `PROGRESS-v0.17.md` updates or combine two tasks in
  one commit.

## Pending Cycle closing record

- **Candidate recorded:** 2026-07-28
- **Release disposition:** pending the separate Step 7 operator publication
  decision; no publication action is authorized by Step 6.
- **Release version if authorized:** v0.16.0. The runtime correction to
  publisher robots-policy enforcement fires the minor-version trigger; Step 7
  owns the final release-version record.
- **Evidence candidate:** `3481e4ba85d65c927b7d0fc3a430bc04fb094394`
  on `candidate/v0.16.0`.
- **Hosted evidence:** workflow-dispatch run `30357365420` attempt 1; all
  **7/7** derived identities authenticated, zero rejected receipts, across
  **6** blocking jobs. Hosted logs measured **131** workspace tests, **55**
  net tests (**29 + 26**), shell **243 passed / 1 declared on-site-only
  skipped** on each interpreter, `invariant-scan` **11/11 rules / 23
  controls**, R10's **45** derived exemptions, and golden **11/11**. Each
  hosted shell collected **244** tests, equal to the local candidate's
  **244 passed**; the ingest net leg is **29/29** both hosted and local.
- **Release-grade audit:** **5** deferred / **2** promoted; report SHA-256
  `34804a849db56bb05cc97d4f45541702832478768119c0251769a07dd76b1bcc`,
  **34468** bytes. Authenticated release-grade re-derivation passed.
- **Evidence pins:** **146/146** total — **144/144** evidence plus **2/2**
  authorization surfaces; protected databases exact **2/2**.
- **Release commit:** pending Step 7's final R-CLOSE measurement and decision.
- **Remote disposition:** `origin/main` remains
  `cdae3c922a2156701c0df0ceb4f45fc937fa7f20`; no `v0.16.0` tag exists.

## Runbook amendments

Step 3 — Widen the gate before the first Step 3 commit to contain the required cross-origin redirect test support — 2026-07-28
Step 4 — Widen the gate before the first Step 4 commit to reconcile the whole-file run authorization pin required by ci-local — 2026-07-28
Step 5 — Widen the gate before the first Step 5 commit to contain the required architecture reconciliation — 2026-07-28
Step 6 — Widen the gate before the first Step 6 commit to contain every evidence-admission surface and same-commit shell equality for the declared hosted-only skip — 2026-07-28
