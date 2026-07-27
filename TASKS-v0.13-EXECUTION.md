# TASKS-v0.13-EXECUTION.md — boundary-closure and rule-integrity runbook for Codex

v0.13 is a **correction cycle**, and it corrects the layer v0.12 built.

v0.12 answered "a claimed property that nothing executes is not a property" by
building `./run invariant-scan`: repo-wide absence claims stopped being readings
and became registered rules. That was the right move. But the rules themselves
inherited the exact defect they exist to prevent:

- **`fail_before` is a string, not a control.** `TASKS-v0.12-EXECUTION.md:357`
  defines it as "the commit or captured output *proving it has fired*."
  `invariant_scan.py:389` validates that it is a non-empty string and nothing
  else. The v0.12 acceptance evidence
  (`PROGRESS-v0.12.md:182`, `STATE.md:217`) demonstrates only that an **empty**
  field is refused. No rule's fail-before state is ever reconstructed, and no
  rule is ever observed to fire in CI. `invariant-scan: 6/6 PASS` proves the
  rules do not fire now; it does not prove they can.
- **R5 enforces a naming convention, not the invariant.** `THRESHOLD_DECL` only
  matches constants whose *name* contains DEDUP/CANONICAL plus
  DISTANCE/THRESHOLD. A second threshold under any other name, passed at a
  production call site, passes R5 cleanly — which is the v0.11 divergence R5
  was registered to close, renamed. **The `STORE-IDENTITY` retraction's stated
  correction does not hold.**
- **`tools/invariant_scan.py` is the only tool in the repository with no unit
  test.** `cycle_check`, `audit_deferred`, `evidence_artifacts`,
  `model_profiles`, `verify_llm`, `benchmark_view`, `view_invalidation`, and
  `python_constraints` all have one. The tool that adjudicates every repo-wide
  absence claim is the one whose own behavior nothing asserts.

The second half of this cycle closes a boundary that `ARCHITECTURE.md` already
claims is closed. Two of the four body-reading core paths hydrate documents
without a sector predicate, and one of them — `/attest`, the HC1 enforcement
point — has no sector parameter at all and therefore cannot be fixed by
choosing a different method.

This cycle does five things and deliberately no more:

1. **makes `fail_before` executable**, so a registered rule that cannot fire is
   a CI failure rather than a well-formed string;
2. **rebinds R5 to the invariant instead of to a naming convention**, by
   converting it from a deny-list hunt to an allow-list assertion over
   production call sites;
3. **closes the body-hydration seam** at `/retrieve` and `/attest` by removing
   the non-scoped method from the store's public surface entirely, so the
   compiler — not a regex — enforces it;
4. **records the `ARCHITECTURE.md` HC2 claim as false** without rewriting a
   published release;
5. **makes the crawler's operator contact a required configuration** that
   refuses to start rather than a placeholder that ships.

It ships no new ingestion source and no subscriber-facing surface. **The public
`/v1/*` JSON bodies, the SQLite schema, and the golden regression's 11
invariants are unchanged. Golden stays 11/11 byte-identical through every task
in this file.** The internal core request schema for `/attest` does change, and
that change is the point of Step 5.

**Version disposition (decide at R-CLOSE, default recorded here).** The default
is a **minor release `v0.13.0`**, on the v0.12.0 precedent: UA-CONTACT
introduces a **required operator configuration** and changes net-build startup
semantics from "starts with a placeholder identity" to "refuses to start." The
alternative — `v0.12.1` for Steps 2–5 and 7 alone, deferring UA-CONTACT — is
defensible if Step 6 slips, since everything else is internal. **Recommendation:
one cycle, `v0.13.0`,** with the rule-integrity steps gated ahead of the
boundary steps, so the apparatus that will certify the boundary fix is itself
trustworthy before it certifies anything. `v0.12.0` stays published and unmoved;
its defects are recorded as errata, not erased.

---

## Entering state (asserted, not yet verified)

Taken from `STATE.md` (v0.12.0), `PROGRESS-v0.12.md`, and the Codex post-release
self-audit. **Every sentence here is a hypothesis until Step 1 (E0) measures
it.** Prior measurement is not permission to skip the entering-state run —
including when the prior measurement is your own or your predecessor's.

- `v0.13.0` is not begun. `v0.12.0` is released and published: annotated tag
  object `94d8215bc2151fecba1280dc793d3f5953cd8055` dereferences to release
  commit `e5faf0c161a4256f33976664685653d8bd805d5d`; the closing append-only
  audit commit `466ebb3fc9736923110803e087acc798e417d084` is HEAD and matches
  `origin/main`. Hosted run **30253646597** attempt **1** passed seven jobs.
  **None of this is reopened by this cycle.**
- `./run ci-local` **20/20**; Rust **121 workspace / 21 net**; committed shell
  suite **205/205** under Python 3.11.4 and 3.12.13; golden **11/11**; evidence
  pins **71/71** (69 evidence files + 2 authorization surfaces); protected
  databases **2/2**; `checklist-audit` **99/99** with the v0.11
  `STORE-IDENTITY` retraction reported separately; `cycle-check` reports cycle
  `v0.12`, state `closed`; `progress-check` passes through R-CLOSE.
- Local and remote branches are aligned and the worktree is clean. Unlike
  v0.12, this cycle activates from a **clean tree**.
- `A4` remains open. The **L1 model-profile controller residual** remains open
  pending the scheduled server-side **L2 forced-command wrapper**, which
  requires a live server session and is **not** executed in this cycle.
- **The `ci-local` job count enters at 20 and exits at 20.** No task in this
  file adds a job. Step 2's self-test runs inside existing job 20 and its unit
  tests inside the existing shell suite.

### Defects this runbook is drafted against (verify, do not trust)

**C1** and **C5** are the Codex post-v0.12.0 self-audit's two findings.
**C2**, **C3**, **C4**, and the C1/C5 augments are additions from independent
re-verification of the repomix export of the v0.12.0 worktree on 2026-07-27, and
must be honored alongside them.

**C2 was reproduced by execution against an extracted copy of the export, not
against HEAD.** An extracted copy is not the repository (HC13). E0 must
reproduce it against HEAD in a scratch worktree or it does not count.

| # | Location | Claim to verify |
|---|---|---|
| **C1** [P1] | `apps/cored/src/main.rs:1111-1148`, `:1127`; `AttestReq` at `:615` | **`/attest` hydrates caller-supplied document ids with no sector predicate and has no sector parameter to supply one.** `context_doc_ids` arrives in the request body and goes straight to `documents_by_ids`. `/attest` is the HC1 enforcement point (`ARCHITECTURE.md:173`). Codex's audit reviewed the HC1 paths and reported no additional violations; this is one. Unlike C1-augment below, it **cannot** be fixed by choosing a different store method — the request type carries no scope. |
| **C1** [augment] | `apps/cored/src/main.rs:1081`; `crates/store/src/sqlite.rs:284` | `/retrieve` hydrates fused ids through `documents_by_ids`, which filters by id only. This is the Codex P2 finding, independently confirmed by reading. `/docs` at `:1235` already uses `documents_by_ids_in_sectors` (`sqlite.rs:307`) and is the compliant model. |
| **C1** [augment] | `crates/store/src/sqlite.rs:352`, `:1090` | **Do not over-claim the severity.** Codex did not reproduce a cross-sector leak, and reading confirms why: `search()` and `vector_search()` each return empty on empty sectors, and both filter sectors in SQL, so today's fused ids are already in-scope. The defect is that the final boundary is upheld by three upstream checks instead of failing closed itself — which is precisely what `ARCHITECTURE.md:189` claims it does not depend on. E0 must record whether a leak reproduces; **if one does, that is a severity escalation and a release-blocking finding, not a routine confirmation.** |
| **C1** [augment] | `apps/cored/src/main.rs:1577`, `:1625`, `:1850` | **The regression-test pattern already exists and was simply never applied here.** `/docs`, `/embeddings/missing`, and `/view` each have a cross-sector test; `/retrieve` and `/attest` have none. `attest_endpoint_refuses_an_index_only_body` (`:1478`) is the only `/attest` endpoint test and asserts the refusal path only. |
| **C1** [augment] | `crates/core/src/lib.rs:291`, `:313-339` | **State the leak channel precisely or the fix will be mis-scoped.** `/attest` returns `{clean_answer, violations[]}`, never a body. The exposure is an *oracle*: a 400 on an unresolvable id discriminates existence, and `violations[]` confirms a 16-token normalized n-gram match against any `IndexOnly` document in any sector. Not reachable through the shipped shell, which passes citations derived from a sector-filtered `/retrieve` (`app.py:152-157`). |
| **C2** [P1] | `tools/invariant_scan.py:60-67` (`THRESHOLD_DECL`), `:363-370`; `config/invariant-rules.json` R5 | **R5 enforces a naming convention, not the invariant.** `THRESHOLD_DECL` matches only constants named with DEDUP/CANONICAL **and** DISTANCE/THRESHOLD. A second production threshold under any other name passes both halves of R5. Reproduced against an extracted copy: adding `const INGEST_FUZZ_LIMIT: u32 = 17;` and using it at the `sqlite.rs:207` ingest call site yields `invariant-scan: R5 PASS` with production at distance 17 and maintenance at 16 — the v0.11 divergence, renamed. `checklist-retractions.json` names THRESHOLD-ONE as `corrected_by`; that correction does not hold. |
| **C2** [augment] | `tools/invariant_scan.py:63-68` | R5's two recorded fail-before states **do** fire, and E0 must confirm both rather than assume the rule is inert: a second DEDUP-named constant is caught, and `assign_canonical_ids_tx(&tx, 16)` at `sqlite.rs:207` is caught at that exact line. The defect is coverage, not total failure. **The root cause is shape:** R5 is a deny-list hunting for known-bad text, while the claim is an allow-list about what every production call site must be. A deny-list over source is inherently open at the bottom. |
| **C3** [P2] | `tools/invariant_scan.py:389`, `:405-424`; `TASKS-v0.12-EXECUTION.md:357-358`, `:387` | **`fail_before` is decorative.** It is required, validated as a non-empty string, and never executed. The v0.12 acceptance criterion "every rule … has a captured fail-before" and the standing prohibition "do not add a rule you cannot make fire" are both discharged by a non-emptiness check on prose. A rule whose regex is silently wrong reports PASS forever. |
| **C3** [augment] | `shell/tests/` (16 files) vs `tools/invariant_scan.py` | `tools/invariant_scan.py` has **no unit test**, alone among the tools. The check that adjudicates every repo-wide absence claim — including the one `AGENTS.md:231-232` requires such claims to be discharged by — is the one whose behavior nothing asserts. |
| **C4** [P2] | `ARCHITECTURE.md:181`, `:189` | The prose claims "Every endpoint that returns document bodies takes an explicit sector set whose predicate is enforced in core SQL," and the HC2 invariant row claims "every body-returning query requires an explicit sector set and fails closed when it is empty, **so a shell bug cannot bypass filtering**." Two of the four body-reading paths do not. The stated *rationale* — independence from shell correctness — is exactly what C1 falsifies. |
| **C4** [augment] | `ARCHITECTURE.md:173` vs `:181` | The endpoint table two rows above the claim already records `/attest` as taking `{answer, context_doc_ids}` with no sector set, and marks it **enforces HC1**. The document contradicts itself within nine lines. |
| **C5** [P3] | `crates/ingest/src/net.rs:19` | The live crawler advertises `contact: you@example.com`. There is no configuration override and nothing refuses to start. This is the Codex P3 finding, confirmed. |
| **C5** [augment] | `crates/ingest/src/net.rs:42`, `:111`, `:325`; `apps/cored/src/main.rs:158` | **The Codex diagnosis is half wrong and the fix must not follow it.** There is exactly one `USER_AGENT` const, and both clients *and* `RobotsCache` already use it, so "used consistently by both clients and `RobotsCache`" is already true. The defect is placeholder value + no override + no refusal. Codex's proposed "required configurable User-Agent" is **dangerous as stated**: `net.rs:14-18` records that the token passed to `RobotsCache` must match the token sent on the wire, because a crawler obeying rules written for a different UA is not obeying them. Making the whole string operator-editable puts robots group selection under operator typo. Only the contact substring may be configurable. |
| **C5** [augment] | `crates/ingest/src/net.rs:19` vs `STATE.md:3` | The UA advertises `intel-platform/0.1` at release `v0.12.0`. The product **token** should stay stable — publishers write robots groups against it — but the advertised version is simply false and has been since v0.2. |

---

## How to run this file

Execute top to bottom, one task and one commit at a time. Follow `AGENTS.md §5`
after **every** task: verify the gate contains the scope of every acceptance
criterion, check the gate, implement, run and capture every acceptance
criterion, run `./run golden`, update `STATE.md`, append `PROGRESS-v0.13.md`,
check the box here, and commit. Implementation commit and audit-record commit
stay separate. Do not batch status updates.

- **🤖 = Codex executes and self-verifies end to end**, with no live model
  endpoint, no live server session, no publication, and no push.
- **🧑 = exactly one named operator action or decision is required.**

**Dependency gates.** Step 3 is blocked by Step 2: R5 must not be rewritten
until a rewritten rule can be *proven* to fire, or the rewrite reproduces the
defect it fixes. Step 6 is blocked by Steps 3 and 5 — the new rule must be
allow-list-shaped (Step 3 establishes the shape) and must be registered against
the post-fix tree (Step 5 produces it). Step 7 is blocked by Steps 3, 5, and 6,
because a retraction record names its `corrected_by` tasks and those tasks must
exist. Step 4 is independent and may run at any point after Step 1.

### Cycle activation (before E0)

`AGENTS.md` declares v0.12, now closed with a valid release record. This runbook
arrives into a **clean worktree**.

In a **separate preparatory implementation/audit pair** before E0:

1. Confirm the tree is clean and HEAD matches `origin/main` at
   `466ebb3fc9736923110803e087acc798e417d084`. If it is not, stop and report.
2. Commit **only** this runbook, the `AGENTS.md` header declaring v0.13 active,
   and a new `PROGRESS-v0.13.md`.
3. Run `cycle-check` and `checklist-audit`.

**Do not claim E0's test, golden, or artifact acceptance from this preparatory
commit.**

### Session opener (run before reading further)

```bash
git status --porcelain=v1
git describe --tags --always --dirty
git rev-parse HEAD
git rev-list --left-right --count origin/main...HEAD
git tag --list 'v0.12*' --format='%(refname:short) %(objectname) %(*objectname)'
sed -n '1,20p' AGENTS.md
sed -n '1,6p' STATE.md
```

### Global definition of done

Protected hashes exact; **all 71** evidence pins still match; golden **11/11
byte-identical**; `./run version-check` green; zero rustc warnings on offline and
net builds; all Rust tests green; all shell tests green under Python 3.11 **and**
3.12; clippy, fmt, ShellCheck, floor byte-compilation, and locked Rust 1.78
green. No mock, fixture, double, health response, hand-authored receipt, or
workflow configuration is promoted to wire evidence.

Rust and shell test **counts will move** in this cycle and every task records
its own delta. **Golden 11/11 does not move.** If it moves by even one
document / id / distance, stop — that is corpus corruption, not progress.

**Every check this cycle adds must run on `ci.yml` runners** — source, config,
and git only. `invariant-scan` remains **static**: no built binary, no protected
DB, no network, no Docker, no SSH. The Step 2 self-test may write only to a
temporary directory it creates and removes.

---

## Deferred means deferred

None of the standing deferral triggers fires in this cycle.

| Deferred item | Unchanged trigger | v0.13 action before the trigger |
|---|---|---|
| T7 robots single-flight | a second concurrent harvester | none |
| Postgres | a second archive writer | none |
| pgvector | exact cosine stops fitting the measured request budget | none |
| Multi-host seam hardening | an actual core/shell host split | none |
| A4 untrusted-shell boundary | a third-party/untrusted shell, or any claim HC1 is invariant under shell replacement | none — **Step 5 narrows the honest-shell-bug case only and must not be written up as narrowing A4** |
| L2 forced-command wrapper | an operator server session | none — remains scheduled, not executed |
| CI-runner evidence | an authenticated receipt set with identified matrix legs, durably committed | re-measure at the new release commit only |

**Step 5 is not A4 closing.** Adding a sector scope to `/attest` makes the core
refuse an out-of-scope id supplied by an *honest* shell with a bug. It does
nothing about a rewritten shell that omits the call or passes a false scope —
which is A4, and which `ARCHITECTURE.md:181` already records as accepted. Any
progress entry that blurs this fails its own acceptance.

---

## Step 1 · E0 — Rebuild the entering state and confirm C1–C5 🤖

**Objective.** Reproduce the post-v0.12.0 state from commands and confirm or
refute every finding against HEAD before changing anything.

**Gate.** The session opener has run and its output is captured. The worktree is
clean. If HEAD is not `466ebb3f…`, stop and report.

**Steps.**

1. Run the full entering matrix and capture every number: `./run ci-local`,
   standalone `./run golden`, `./run verify-artifacts`, `./run cycle-check`,
   `./run checklist-audit`, `./run progress-check`, `./run version-check`,
   `./run invariant-scan`.
2. **Reproduce C1 with a failure-capable control, not a reading.** Against a
   scratch DB and the real `cored`, seed two documents in two different sectors.
   Then: (a) call `/retrieve` with sector A and confirm no sector-B body
   returns — record whether the observed containment comes from the hydration
   query or from the upstream ranking legs, by also calling `documents_by_ids`
   directly with a sector-B id and recording that it returns the body; (b) call
   `/attest` with a sector-B `context_doc_ids` and an answer that shares a
   16-token normalized phrase with that document's body, and record the response.
   **If (b) returns a violation for a document outside the caller's scope, C1 is
   confirmed as a live oracle and the release disposition changes.**
3. **Reproduce C2 mechanically against HEAD**, in a scratch worktree created
   with `git worktree add`, never in the live tree: add a second production
   threshold under a name containing neither DEDUP nor CANONICAL, route the
   `sqlite.rs:207` call site through it, and run `./run invariant-scan`. Record
   the exit code and the R5 line verbatim. Remove the worktree afterwards.
4. **Confirm R5's two recorded fail-before states do fire**, by the same
   scratch-worktree method, and record both FAIL lines verbatim. C2 is a
   coverage defect; if R5 turns out to be wholly inert, that is a larger finding
   and must be recorded as such.
5. **Reproduce C3 mechanically:** confirm no test module or test file exercises
   `tools/invariant_scan.py`, and confirm that mutating one rule's regex to a
   pattern that cannot match still yields `invariant-scan: PASS`.
6. Confirm or refute C4 and C5 by reading the cited lines and recording what is
   and is not enforced.
7. Record which of C1–C5 **refute**. A refuted row is a finding, not a failure —
   the later step then narrows or closes with the reason recorded.

**Acceptance criteria.** Entering matrix captured in full · C1 reproduced as a
measured request/response pair against the real `cored`, with the containment
source identified · C2 reproduced as command output against HEAD in a scratch
worktree, and R5's two recorded fail-befores separately confirmed to fire · C3
reproduced as command output · C4/C5 dispositions recorded · published `v0.12.0`
tag, commit, and all 71 pins unchanged and re-verified · golden 11/11.

**Done when** the entering state is a set of captured measurements and every
finding this runbook acts on has been confirmed or refuted by execution.

---

## Step 2 · FAIL-BEFORE-EXEC (C3) — Make a registered rule prove it can fire 🤖

**Objective.** Convert `fail_before` from a validated string into an executed
control, and give the adjudicating tool the unit test every other tool has.

**Gate.** `tools/invariant_scan.py`, `config/invariant-rules.json`,
`shell/tests/test_invariant_scan.py` (new), `run`, and the two `AGENTS.md`
sentences that define the field. **No rule's logic changes in this task** — Step
3 does that, and mixing them hides the rewrite inside the harness change.

**Steps.**

1. Change `fail_before` from a free string to a **reconstructible control**: a
   structure naming the file, the mutation to apply, and the expected FAIL
   substring. Keep the existing prose in a separate `fail_before_note` field so
   no recorded evidence is discarded.
2. Add `invariant_scan.py --self-test`: for each registered rule, copy the tree
   to a temporary directory, apply that rule's mutation, run **only** that rule,
   and assert it exits non-zero with the expected substring. Then assert the
   unmutated tree passes. A rule whose mutation does **not** produce a failure
   is a self-test failure.
3. Wire `--self-test` into existing ci-local job 20. **Do not add a job.**
4. Add `shell/tests/test_invariant_scan.py` covering, at minimum: a rule whose
   regex cannot match is rejected by `--self-test`; a malformed registry exits
   2; a rule id with no implemented check exits 2; each of R1–R6 fires on its
   own recorded mutation and passes on the clean tree.
5. Record the new shell and ci-local numbers in `STATE.md` in this same task.

**Acceptance criteria.** `./run invariant-scan --self-test` green and part of
job 20 · ci-local remains **20** · mutating any one rule's regex to a
non-matching pattern turns `--self-test` **red**, demonstrated and captured ·
`shell/tests/test_invariant_scan.py` present and green under Python 3.11 and
3.12 · every pre-existing `fail_before` prose string preserved, none deleted ·
no rule's matching logic changed in this commit · golden 11/11.

**Done when** a registered rule that cannot fire fails CI, and that failure has
been observed rather than argued.

---

## Step 3 · THRESHOLD-BIND (C2) — Rebind R5 from a name to the invariant 🤖

**Objective.** Make R5 assert what it claims: that every production call site
passes the one canonical constant — not that no *differently named* constant
exists.

**Gate.** `tools/invariant_scan.py` R5 implementation and its
`config/invariant-rules.json` entry. `crates/store/src/sqlite.rs` may not change
in this task; if the rewritten rule fails against HEAD, that is a **finding to
record and act on in a follow-up task**, not a licence to edit the source until
the rule goes green.

**Steps.**

1. Rewrite R5 as an **allow-list**: enumerate every production call site of
   `assign_canonical_ids`, `assign_canonical_ids_tx`, and
   `rematerialize_canonical_ids_with_distance`, and assert the distance argument
   at each is the single token `DEDUP_MAX_DISTANCE`. Any other token — literal,
   constant, expression — fails, and the finding names the file, line, and
   offending token.
2. Keep the existing "exactly one declared canonical-distance constant" half.
   The allow-list catches divergence; this half catches a dead duplicate.
3. Register **both** halves with reconstructible fail-before mutations under
   Step 2's schema, including the `INGEST_FUZZ_LIMIT`-shaped mutation from
   C2 — the case the old rule missed is now a required control.
4. Update the R5 `claim` and `scope` text so it describes call-site binding
   rather than constant naming, and update its `source` citation.
5. Record in `PROGRESS-v0.13.md` the **shape lesson**, explicitly: a deny-list
   over source text is open at the bottom, and a repo-wide absence claim should
   be expressed as an allow-list over call sites wherever the call sites are
   enumerable.

**Acceptance criteria.** R5's rewritten form FAILs on the `INGEST_FUZZ_LIMIT`
mutation, captured verbatim · R5 still FAILs on both original fail-before
mutations · R5 PASSes on unmutated HEAD · `--self-test` green · the recorded
claim text no longer describes a naming convention · zero source files under
`crates/` changed in this commit · golden 11/11.

**Done when** the mutation that silently passed at E0 is red, and R5's recorded
claim is a description of what it checks.

---

## Step 4 · UA-CONTACT (C5) — A crawler identity that refuses to be a placeholder 🤖

**Objective.** Make the operator contact required configuration, enforced by
refusal at startup, without putting robots group selection under operator typo.

**Gate.** `crates/ingest/src/net.rs`, `apps/cored/src/main.rs`
`build_robots_cache`, `.env.example`, `config/core.json` if a config field is
chosen over an environment variable, and their tests. No change to robots
parsing, redirect handling, backoff, or the politeness limiter.

**Steps.**

1. Split the UA into a **structural product token** and a **configurable
   contact**. `intel-platform` stays a compile-time constant and remains the
   token handed to `RobotsCache`; only the contact substring is operator
   supplied. Record in a comment why the token is not configurable, citing the
   group-selection reason at `net.rs:14-18`.
2. Correct the advertised version so it derives from the crate version rather
   than the frozen `0.1`.
3. **Refuse to start** a `net` build when the contact is unset, empty, or
   matches a placeholder pattern (`example.com`, `you@`, `changeme`). Put the
   refusal in `build_robots_cache`, which already carries this idiom and its
   rationale — a net-enabled harvester that starts without a real identity is
   fail-open on exactly the thing this task closes.
4. Offline builds are unaffected: nothing is fetched, so no publisher is asked.
   Assert this rather than assuming it.
5. Add tests in both directions: a valid contact builds; each placeholder form
   refuses; the offline build path is unchanged; the string handed to
   `RobotsCache` is byte-identical to the string sent on the wire.
6. Update `.env.example`, `README.md`, and `deploy/README.md` with the new
   required setting.

**Acceptance criteria.** A `net` build with no contact configured **refuses to
start**, captured · each placeholder form refuses · a configured contact appears
identically in both clients and in `RobotsCache` · the offline build is
unchanged and its test proves it · advertised version matches the crate version
· `.env.example` documents the setting · golden 11/11.

**Done when** shipping a placeholder crawler identity is impossible rather than
merely discouraged.

---

## Step 5 · BODY-BOUNDARY (C1) — Remove the non-scoped hydration seam 🤖

**Objective.** Make every production document hydration carry an explicit sector
predicate, and close the seam so a future caller cannot reintroduce the defect
by choosing the wrong method.

**Gate.** `crates/store/src/sqlite.rs`, `apps/cored/src/main.rs`,
`shell/intel_shell/core_client.py`, `shell/intel_shell/app.py`, and their tests.
**No schema change. No change to the public `/v1/*` JSON bodies.** The internal
`/attest` request schema does change.

**Steps.**

1. Point `/retrieve` at `documents_by_ids_in_sectors`, passing the `req.sectors`
   it already holds.
2. Add a required `sectors` field to `AttestReq` and hydrate through
   `documents_by_ids_in_sectors`. Thread `sub.sectors` from `app.py` through
   `core_client.attest`.
3. **Close the seam, do not just fix the instances.** After 1 and 2,
   `documents_by_ids` has zero production callers. Remove `pub` so the compiler
   — not a regex, and not the next reviewer — enforces it. If any caller
   remains, record why before weakening this step.
4. **Record the error-semantics change explicitly.** An out-of-sector id and a
   nonexistent id both become `400 unknown context document id`. That
   indistinguishability is the point: it removes the existence oracle. It is a
   behavioral change and belongs in `PROGRESS-v0.13.md` and `CHANGELOG.md`, not
   discovered later.
5. Add cross-sector regression tests for `/retrieve` and `/attest`, modelled on
   `docs_filters_requested_ids_by_sector_and_fails_closed_when_empty`
   (`main.rs:1577`). Each must fail-before and pass-after, and each must assert
   the empty-sectors case fails closed.
6. Add an `/attest` oracle test: an answer sharing a 16-token phrase with an
   out-of-sector `IndexOnly` document returns **no** violation naming that
   document.
7. Re-run the E0 step-2 control and record it now returns nothing across
   sectors.

**Acceptance criteria.** Zero production callers of `documents_by_ids` and the
method is no longer `pub`, verified by build · `/retrieve` and `/attest` both
fail closed on empty sectors · both new cross-sector tests fail-before and
pass-after, captured in both directions · the oracle test passes · the E0
control reproduces empty · public `/v1/*` bodies byte-identical · golden
**11/11 byte-identical** · the error-semantics change recorded in two places.

**Done when** the sector predicate is a property of the hydration boundary
rather than an inherited property of its callers.

---

## Step 6 · R7-BODY-SECTOR — Register the boundary as an executable rule 🤖

**Objective.** Give `ARCHITECTURE.md`'s body-boundary sentence an executable
home, so the C1 class cannot return by inspection passing.

**Gate.** `tools/invariant_scan.py`, `config/invariant-rules.json`,
`shell/tests/test_invariant_scan.py`. No source under `crates/` or `apps/`
changes in this task.

**Steps.**

1. Register **R7** as an allow-list in Step 3's shape: every production document
   hydration call site outside `crates/store/src/sqlite.rs` resolves to
   `documents_by_ids_in_sectors`, and `documents_by_ids` is not `pub`.
2. Cite the exact `ARCHITECTURE.md` sentence and line as `source`, per the v0.12
   registration contract.
3. Provide reconstructible fail-before mutations: re-`pub` the method; route
   `/retrieve` back through it; route `/attest` back through it. All three must
   FAIL.
4. **Prefer the compiler where the compiler suffices** — record this in
   `PROGRESS-v0.13.md`. R7 exists to catch a future re-`pub`, not to substitute
   for the visibility change Step 5 makes. A rule that duplicates a compiler
   guarantee is cheap; a rule that *replaces* one is a downgrade.

**Acceptance criteria.** R7 registered with three reconstructible fail-befores,
all three demonstrated FAIL, captured · R7 PASSes on the post-Step-5 tree ·
`--self-test` green across all seven rules · ci-local remains **20** ·
`invariant-scan` reports **7/7** · golden 11/11.

**Done when** the body-boundary claim in `ARCHITECTURE.md` is a check rather
than a reading.

---

## Step 7 · RETRACT-HC2 (C4) — Record the false invariant honestly 🤖

**Objective.** Record that `ARCHITECTURE.md`'s HC2 claim was false during
v0.12's lifetime, correct it forward, and leave the published release untouched.

**Gate.** `config/checklist-retractions.json`, `ARCHITECTURE.md`,
`PROGRESS-v0.12.md` (**append only**), `STATE.md`. **Do not edit the `v0.12.0`
tag, its commit, or any of its 71 pins.**

**Steps.**

1. Add a retraction entry in the `STORE-IDENTITY` shape, naming the false
   sentence by file and line, the reason, and `corrected_by` referencing
   BODY-BOUNDARY and R7-BODY-SECTOR.
2. Add a **second** retraction for the `STORE-IDENTITY` correction itself: R5 as
   registered in v0.12 did not discharge the claim `THRESHOLD-ONE` was recorded
   as correcting. `corrected_by` references THRESHOLD-BIND. **A retraction whose
   correction was itself defective is a retraction, not a footnote.**
3. Correct `ARCHITECTURE.md:181` and the HC2 row to describe what is now
   enforced, and reconcile the `:173` endpoint table row for `/attest` so the
   document no longer contradicts itself.
4. Append — never edit — an errata entry to `PROGRESS-v0.12.md`. Verify by diff
   that the task produced only additions.
5. Confirm `checklist-audit` reports checked and retracted separately, and that
   the v0.12 checklist still reads 11/11 with **three** retractions now
   reported across cycles.
6. Restate A4 and the L1 controller residual as open, in the same plain language
   they already use. **Neither is narrowed by this cycle.**

**Acceptance criteria.** Both retraction records validated · `ARCHITECTURE.md`
internally consistent and matching enforced reality · `PROGRESS-v0.12.md`
diff is additions only · `checklist-audit` green with retractions reported
separately · `v0.12.0` tag, commit, and 71 pins byte-identical · A4 and the L1
residual both still stated as open · golden 11/11.

**Done when** the record of what v0.12 enforced is true, including the record of
what its own correction failed to correct.

---

## Step 8 · R-CLOSE — Version disposition and closing record 🧑🤖

**Objective.** Decide the release, account for every diff path, and close the
cycle with a record that is measured rather than assumed.

**Gate.** Steps 1–7 complete and boxed. Worktree clean. **🧑 One operator
decision: the version disposition and whether to publish.**

**Steps.**

1. Re-run the complete definition of done and capture every number.
2. Record the version choice **with reasoning**, not as a default. The recorded
   default is `v0.13.0`; the alternative is `v0.12.1` if UA-CONTACT did not
   land. State which trigger fired.
3. Classify every path in the diff exactly once in `STATE.md`.
4. Update `CHANGELOG.md`, `README.md`, and the release authorities; confirm
   `version-check` agrees at the exact annotated tag.
5. Reconcile `ARCHITECTURE.md`'s invariant table against enforced reality one
   final time. **A4 and the L1 controller residual must both still read as
   open.** Do not let this cycle's fixes be written up as closing either.
6. Append the **Cycle closing record**: date, disposition, release, release
   commit, annotated tag object, and per-Step implementation commits.
7. State the publication disposition as a decision with a trigger.

**Acceptance criteria.** Version choice recorded with reasoning · every diff
path accounted for · `ARCHITECTURE.md` invariant table matches enforced reality
· A4 and the L1 residual both still open · checklist fully checked, all
retractions reported, `checklist-audit` green · `invariant-scan` 7/7 with
`--self-test` green · all pins match · golden 11/11.

**Done when** v0.13's disposition is a recorded, measured decision, and the
record of v0.12's is true.

---

## Cycle checklist

- [ ] **E0** — entering matrix captured; C1 reproduced as a measured
  request/response pair with the containment source identified; C2 reproduced
  against HEAD in a scratch worktree and R5's two original fail-befores
  separately confirmed to fire; C3 reproduced as command output; C4/C5
  dispositions recorded
- [ ] **FAIL-BEFORE-EXEC** — `fail_before` reconstructible and executed;
  `--self-test` in ci-local job 20 with the count still 20; a non-matching regex
  turns CI red, demonstrated; `shell/tests/test_invariant_scan.py` green on both
  interpreters; no rule logic changed
- [ ] **THRESHOLD-BIND** — R5 is an allow-list over production call sites; the
  `INGEST_FUZZ_LIMIT` mutation FAILs; both original fail-befores still FAIL;
  clean tree PASSes; no `crates/` source changed
- [ ] **UA-CONTACT** — net build refuses to start without a real contact; every
  placeholder form refused; product token structural and identical on the wire
  and in `RobotsCache`; advertised version derived from the crate; offline build
  unchanged and proven so
- [ ] **BODY-BOUNDARY** — zero production callers of `documents_by_ids` and it
  is no longer `pub`; `/retrieve` and `/attest` sector-scoped and fail closed on
  empty sectors; both regression tests fail-before/pass-after; oracle test
  passes; error-semantics change recorded twice; public bodies byte-identical
- [ ] **R7-BODY-SECTOR** — R7 registered with three reconstructible
  fail-befores, all demonstrated FAIL; `invariant-scan` 7/7; ci-local still 20
- [ ] **RETRACT-HC2** — both retraction records validated;
  `ARCHITECTURE.md` self-consistent and matching enforced reality;
  `PROGRESS-v0.12.md` additions only; `v0.12.0` tag, commit, and 71 pins
  byte-identical; A4 and the L1 residual still open
- [ ] **R-CLOSE** — version choice recorded with reasoning; every diff path
  classified; `ARCHITECTURE.md` matches enforced reality; A4 and the L1 residual
  both still open

---

## Standing prohibitions

- **Do not touch the `v0.12.0` release.** The tag object, its commit, its
  receipt/bundle files, and all 71 pins are immutable. Corrections go forward as
  a new release; they never edit a published one. The same holds for `v0.11.0`,
  `v0.10.3`, and the unpublished local `v0.10.2`.
- **Do not edit `PROGRESS-v0.12.md`.** It is append-only. The errata entry is an
  append; verify by diff that the task produced only additions.
- **Do not uncheck a box in a closed runbook.** Retraction is a record, not an
  edit.
- **Do not fix `documents_by_ids` by adding a sector-aware wrapper beside it.**
  That closes the instance and preserves the seam — the exact error v0.12's
  standing prohibition on exporting `DEDUP_MAX_DISTANCE` was written against.
  The non-scoped method leaves the public surface.
- **Do not make the crawler's product token operator-configurable.** Only the
  contact substring. A crawler that obeys rules written for a different UA than
  it presents is not obeying them (`net.rs:14-18`).
- **Do not add an `invariant-scan` rule you cannot make fire** — and after Step
  2, "cannot make fire" is a CI failure rather than a matter of judgement. A
  rule whose fail-before is prose only is refused.
- **Do not let `invariant-scan` acquire a runtime dependency.** Static analysis
  over source, config, and git only — no built binary, no protected DB, no
  network, no Docker, no SSH. The self-test may use a temporary directory only.
- **Do not add a ci-local job.** The count enters at 20 and exits at 20.
- **Do not claim any task in this cycle closes or narrows A4**, and do not claim
  the L1 controller residual is closed. Step 5 constrains an honest shell with a
  bug; A4 concerns a shell that lies. `ARCHITECTURE.md` must keep saying both
  are open.
- **Do not run a live server session in this cycle.** L2 remains scheduled.
- **Do not edit source to make a rewritten rule go green.** In Step 3, a rule
  that fails against HEAD is a finding to record, not a licence to change
  `crates/`.
- Do not change the public `/v1/*` JSON bodies, the SQLite schema, or the golden
  regression's 11 invariants. Golden stays 11/11 byte-identical after **every**
  task.
- Do not hand-edit `Cargo.lock` (HC12), raise the offline Rust 1.78 floor, lower
  the Python 3.11 floor, or let core call an LLM (HC3).
- Do not commit `.env`, provider keys, tokens, private key material, or raw
  secret-bearing responses.
- Do not batch `STATE.md` / `PROGRESS-v0.13.md` updates or combine two tasks in
  one commit.
