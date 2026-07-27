# TASKS-v0.11-EXECUTION.md — invariant-enforcement runbook for Codex

v0.11 is an **invariant-enforcement cycle**, and it is the first cycle in four
whose subject is the *product source* rather than the evidence machinery.
v0.10.3 closed and published with a green 19-job local matrix, 187 shell tests on
both Python lanes, golden 11/11, protected artifacts 2/2, **39/39** evidence pins,
and 77/77 checked tasks across eight closed runbooks with zero exemptions. The
evidence apparatus is now sound. The v0.10.3 self-audit turned that apparatus on
the source and found that the source is not.

The audit is **accurate**. All eight findings reproduce against the shipped tree,
and every reported pass holds.

The findings share **one root cause**, and this cycle is organized around naming
it: *the invariant is written in a comment and upheld by the way the shipped
caller happens to invoke it, not by anything at the boundary that would refuse.*
This is the project's founding doctrine (`AGENTS.md §0` — a claimed property that
nothing executes is not a property) turned on the invariants themselves. Every
finding has the same shape:

- `main.rs:28` and `ARCHITECTURE.md:173` both state the core is **loopback-only**.
  Nothing checks. `./run` happens to export `CORE_BIND=127.0.0.1:$CORE_PORT`.
- `main.rs:14-17` states that a buggy shell "can at worst grant the wrong sectors
  — never bypass the filter mechanism itself." Two endpoints take no sectors at
  all; the shipped caller happens to pass already-filtered ids.
- `compliance/src/lib.rs:480-484` promises publisher policy is "a lower bound on
  our courtesy." Adopting a `Crawl-delay` throws away the clock that enforces it.
- `ingest/src/lib.rs:150-159` documents a one-way publisher-plus-operator
  composition. A `Reach::Network` fetch with no cache silently performs neither.
- `billing.py:66-68` says persistence is batched "so a batch can be saved once."
  The save is batched; the mutation is not.

And the reason the test suite is green through all of it is HC13, stated in the
project's own words: **fixtures prove the state machine, not the wire.** The
politeness tests assert the configured rate, never elapsed time. The robots tests
exercise one group, never two. The ingest test asserts the pre-T2 fail-open
behavior *on purpose*. Nothing is lying; nothing is executing the claim either.

This cycle does eight things and deliberately no more:

1. **refuses a non-loopback bind** — the topology invariant becomes structural;
2. **binds `/docs` and `/embeddings/missing` to a sector set** — HC2 stops having
   exceptions the architecture does not name;
3. **merges same-token robots groups** — without reintroducing the `*` bug the
   existing comment correctly warns about;
4. **normalizes percent-encoded robots paths** — unreserved octets only;
5. **preserves the politeness clock across a `Crawl-delay` transition**;
6. **fails closed when a network fetch has no robots cache**;
7. **makes billing batches atomic in memory, not just on disk**;
8. **rematerializes canonical identity in the maintenance write path**.

It ships no new ingestion source and no subscriber-facing surface. The public
`/v1/*` JSON bodies and the database schema are unchanged. **Golden stays 11/11
byte-identical through every task in this file** — it is the tripwire for all
eight. The default disposition at R-CLOSE is a **minor release `v0.11.0`**, not a
patch: `/docs` gains a required parameter (an internal-API break) and robots and
bind behavior change. That follows the v0.10.0 precedent, where a minor bump was
chosen for internal-API and runtime change with the public body unchanged.

---

## Entering state (asserted, not yet verified)

Taken from `STATE.md` (v0.10.3) and the v0.10.3 self-audit. **Every sentence here
is a hypothesis until Step 1 (E0) measures it.** Prior measurement is not
permission to skip the entering-state run — including when the prior measurement
is your own or your predecessor's.

- Worktree clean; `./run ci-local` **19/19**; golden **11/11**; protected
  artifacts **2/2 exact**; **39/39** evidence pins match; `cycle-check`,
  `checklist-audit` (**77/77**, zero exemptions), and `progress-check` green.
- Rust **99 workspace / 20 net** tests, 0 rustc warnings. Python **3.11 and 3.12:
  187 shell tests each**; **21/21** exact packages on both interpreters. Both
  lanes emit one third-party Starlette/httpx deprecation warning, which is not a
  project warning-gate failure.
- Version authorities read **0.10.3** (`apps/cored/Cargo.toml:3`,
  `shell/intel_shell/__init__.py:9`). `v0.10.3` was released **and published**.
- All eight formal execution runbooks are closed and administratively complete.

**The v0.10.3 guards are confirmed live and must not regress.** Independently
re-verified during review: the deferred receipt declares `evidence_grade:
release` with `attestations_required: true`; `expected_job_identities` is an exact
`(job, matrix)` set; all seven accepted receipts carry distinct matrix identities
with `attestation_verified: true`; every recorded receipt path **resolves to a
committed file**; `task` reads `v0.10.3 RECEIPT` (derived, not hard-coded); the
one-way classifier invariants at `verify_llm.py:472` are shared by fresh
classification (`:221`) and resume (`:591`) so the two cannot drift; and all 39
pins re-hash byte-exactly.

### Defects this runbook is drafted against (verify, do not trust)

Each was read out of the shipped tree on 2026-07-27 by path and line and is a
hypothesis until E0 confirms or refutes it. **S1–S8** correspond to the eight
v0.10.3 self-audit findings. The **[augment]** rows are additions from independent
re-verification and must be honored alongside them.

| # | Location | Claim to verify |
|---|---|---|
| **S1** [P1] | `apps/cored/src/main.rs:1237`, `:1273` | `CORE_BIND` is read with a `127.0.0.1:8788` default and passed straight to `TcpListener::bind(&bind)`. No validation. `CORE_BIND=0.0.0.0:8788` exposes every internal endpoint. `main.rs:28` claims "Binding: 127.0.0.1 only" and `ARCHITECTURE.md:173` claims "The core is loopback-only" — **neither is enforced anywhere**; only `run:_start_cored` happens to export a loopback value. |
| **S1** [augment] | `apps/cored/src/main.rs:287-302` | `guard()` returns `Ok(())` unconditionally when `state.token` is `None`, and `CORE_TOKEN` is `std::env::var(...).ok()`. On a non-loopback bind the default posture is therefore **no authentication at all**. Whether the token stays optional under a *loopback* bind is a decision to record, not an oversight to silently fix. |
| **S2** [P1] | `apps/cored/src/main.rs:1216-1226`; `crates/store/src/sqlite.rs:279-298` | `docs()` accepts `DocsQ { ids: String }` — **no sectors** — and calls `documents_by_ids()`, whose SQL is `WHERE id IN (…)` with no sector predicate. Contrast `/retrieve` (`:1051`), which reaches the same store call only through `intel_retrieve::hybrid(…, &req.sectors, …)`, both of whose legs (`search` `:308`, `vector_search` `:986`) filter `d.sector IN (…)` in SQL and return empty on an empty sector set. |
| **S2** [augment] | `apps/cored/src/main.rs:1144-1163`; `crates/store/src/sqlite.rs:894-906` | **`/embeddings/missing` is the same defect and the audit does not name it.** `docs_missing_embeddings(model)` selects the whole corpus with no sector *and no license* predicate, and the handler returns `body` for every row. It is broader than `/docs`: `/docs` requires the caller to know ids; this one **enumerates**. `ARCHITECTURE.md:184` ("HC2 sector filtering | core SQL | a shell bug must not bypass it") has **two** exceptions, not one. |
| **S2** [augment] | `apps/cored/src/main.rs:1221` | `docs()` calls `parse_sectors(&p.ids)` — a function named for sectors, used to split ids. Cosmetic, but it is literally why the missing sector binding reads as correct at the call site. |
| **S3** [P1] | `crates/compliance/src/lib.rs:158-180` | `parse()` selects the single longest matching product token and keeps `groups[i]` only. Because the comparison is strict `>`, a **second group with the same token loses entirely**. RFC 9309 §2.2.1 requires groups matching the product token to be combined. |
| **S3** [augment] | `crates/compliance/src/lib.rs:87-92` | **The doc-comment deliberately justifies non-merging, and its reasoning is correct — for a different case.** It warns that merging `*` into a specific match would let a site that disallows `/` for `*` deny us everything. That is true and must be preserved. A fix that reads the audit literally ("merge all matching groups") **reintroduces exactly the bug this comment prevents.** Merge only *same-specificity* matches. |
| **S4** [P1] | `crates/compliance/src/lib.rs:229-263` | `path_matches()` compares raw strings; `grep -n 'percent\|decode\|urlencod'` over the crate returns **nothing**. `/foo/bar/%62%61%7A` evades a `/foo/bar/baz` rule. RFC 9309 §2.2.2 requires normalization before comparison. |
| **S5** [P1] | `crates/compliance/src/lib.rs:626-630`, `:575-593`, `:498-505` | `set_host_rate()` does `map.insert(host, Arc::new(RateLimiter::per_second(rps)))` — a **fresh** limiter whose `last` is `None`. `policy_for()` calls `limiters.acquire(&host)` at `:505` (setting `last`), then `gate()` calls `apply_crawl_delay()` → `set_host_rate()`, discarding it. The next acquire sees `last: None` and does not sleep, so the first document request after `robots.txt` is **not delayed**. |
| **S5** [augment] | `crates/compliance/src/lib.rs:579`, `:595-599` | The replacement also resets `acquires` to zero, so `acquires_for(host)` under-counts by exactly the `robots.txt` fetch. The doc-comment says that counter exists so "a harvest test [can] confirm the limiter is consulted once per page **without timing the actual waits**" — i.e. the transition corrupts the very counter the suite uses in place of timing. Any fix must preserve the counter, and the new test must time the wait. |
| **S6** [P2] | `crates/ingest/src/lib.rs:168-177` | `if let Some(cache) = &ctx.robots_cache` — when `None`, `Reach::Network` silently performs **no publisher check at all** and falls through to the operator deny-list. Dormant in the shipped topology (`main.rs:145-161`: the `net` build always supplies a cache and `expect`s rather than starting fail-open), but the library seam permits it. |
| **S6** [augment] | `crates/ingest/src/lib.rs:425-441` | The test `with_no_cache_the_configured_policy_governs_exactly_as_before_t2` constructs `Reach::Network` + `robots_cache: None` and **asserts the fetch is allowed**. The suite encodes the defect. This test must be *inverted*, not deleted. |
| **S7** [P2] | `shell/intel_shell/app.py:270-282`; `billing.py:61-90` | `_apply_events` loops `billing.apply_event(store, ev, …)`, mutating shared process-lifetime state per event, and raises HTTP 400 on a later failure with earlier mutations already applied. `store.save()` at `:267` is skipped, so disk is clean — but the **live** entitlement state is now partially applied for every subsequent request, and the unrelated save at `:214` would persist it. `apply_event`'s docstring says persistence is batched "so a batch can be saved once"; the save is batched, the mutation is not. |
| **S8** [P2] | `crates/store/src/sqlite.rs:400-427`, `:431-438` | `update_document()` writes a recomputed `simhash` and a new `published_day` but never touches `canonical_id`, and runs as a bare `conn.execute` outside any transaction. `delete_document()` removes a row inside a transaction but leaves surviving duplicates pointing at the deleted `canonical_id`. Neither has a caller outside its own module — this is a public contract that can violate the corpus-identity invariant before anyone calls it. |
| **S8** [augment] | `crates/store/src/sqlite.rs:600-609`, `:637` | The fix primitive already exists: `assign_canonical_ids_tx(&tx, max_distance)` is transaction-scoped and callable from both sites. `delete_document` already holds a transaction; `update_document` would need one. The `max_distance` value must come from the **same constant the ingest path uses** — introduce one if none exists rather than writing a second literal. |

---

## How to run this file

Execute top to bottom, one task and one commit at a time. Follow `AGENTS.md §5`
after **every** task: check the gate first, implement, run and capture every
acceptance criterion, run `./run golden`, update `STATE.md`, append
`PROGRESS-v0.11.md`, check the box here, and commit. Implementation commit and
audit-record commit stay separate. Do not batch status updates.

- **🤖 = Codex executes and self-verifies end to end**, with no live model
  endpoint, no publication, and no push. These tasks' correctness is provable
  offline.
- **🧑 = exactly one named operator action or decision is required.**

Steps 2–9 are **independent**. Each may be reordered if a gate blocks, but none
may be merged into another commit, and each must leave golden at 11/11 on its
own.

### Cycle activation (before E0)

`AGENTS.md` correctly declares the latest closed cycle, v0.10.3, and this runbook
arrives untracked. In a **separate preparatory implementation/audit pair** before
E0: commit this reviewed runbook, declare v0.11 active in the `AGENTS.md` header,
and create `PROGRESS-v0.11.md`. Run `cycle-check` and `checklist-audit`. **Do not
claim E0's test, golden, or artifact acceptance from this preparatory
correction.**

### Session opener (run before reading further)

```bash
git status --porcelain=v1
git describe --tags --always --dirty
git rev-parse HEAD
git remote -v
git rev-list --left-right --count origin/main...HEAD
sed -n '1,20p' AGENTS.md
sed -n '1,6p' STATE.md
```

### Global definition of done

Protected hashes exact; **all 39** evidence pins still match; golden **11/11
byte-identical**; `./run version-check` green; zero rustc warnings on offline and
net builds; all Rust tests green; all shell tests green under Python 3.11 **and**
3.12; clippy, fmt, ShellCheck, floor byte-compilation, and locked Rust 1.78 green.
No mock, fixture, double, health response, hand-authored receipt, or workflow
configuration is promoted to wire evidence.

**The `ci-local` job count enters and exits this cycle at 19.** Every fix in this
cycle lands as tests inside existing jobs. Any task that nonetheless changes the
count records the new count in `STATE.md` and `PROGRESS-v0.11.md` in the same
task, with the reason. **Rust and Python test counts will rise; record the new
counts per task rather than at the end.** Every check this cycle adds must run on
`ci.yml` runners, so it may touch only source, config, and git — never the built
`cored` binary or the protected DBs.

**The public `/v1/*` JSON bodies and the SQLite schema do not change in this
cycle.** `/docs` and `/embeddings/missing` are internal core endpoints; changing
their query contract is an internal-API change and is in scope.

---

## Deferred means deferred

None of the six standing deferral triggers fires in this cycle. In particular,
**S1 is not the multi-host trigger firing.** Enforcing loopback is the *current*
topology being made structural; if an operator genuinely needs a non-loopback
bind, that is the multi-host seam trigger and it opens a design task, not a flag.

| Deferred item | Unchanged trigger | v0.11 action before the trigger |
|---|---|---|
| T7 robots single-flight | a second concurrent harvester | none |
| Postgres | a second archive writer | none |
| pgvector | exact cosine stops fitting the measured request budget | none |
| Multi-host seam hardening | an actual core/shell host split | none — S1 **enforces** the single-host premise rather than relaxing it |
| A4 untrusted-shell boundary | a third-party/untrusted shell, or any claim HC1 is invariant under shell replacement | none — S2 narrows the shipped-shell blast radius; it does **not** make HC1 invariant under shell replacement, and no task may claim so |
| CI-runner evidence | an authenticated receipt set with identified matrix legs, durably committed | re-measure at the new release commit only |
| `/view` materialization | already fired in v0.10; promoted to a future implementation | none |

---

## Step 1 · E0 — Rebuild the entering state and re-confirm the eight defects 🤖

**Objective.** Reproduce the v0.10.3 closed state from commands, and confirm or
refute S1–S8 and every `[augment]` row against HEAD before changing anything.

**Gate.** If the worktree is not clean, or `git describe` does not resolve to the
published v0.10.3 release commit or a descendant, stop and report.

**Steps.**

1. Capture the full offline matrix: `./run ci-local`, `./run golden`,
   `./run verify-artifacts`, `./run version-check`, `./run cycle-check`,
   `./run checklist-audit`, `./run progress-check`. Record exact counts.
2. Independently re-hash all 39 pinned artifacts against
   `config/protected-artifacts.json` — do not accept `validate`'s own summary as
   the only witness.
3. Confirm or refute each defect **with captured command output**:
   - **S1** — `sed -n '26,34p;1235,1240p;1270,1276p' apps/cored/src/main.rs`;
     `sed -n '285,303p' apps/cored/src/main.rs`;
     `grep -rn 'is_loopback' apps crates` (expect none);
     `grep -n 'loopback' ARCHITECTURE.md`.
   - **S2** — `sed -n '1216,1226p;1144,1163p;665,671p' apps/cored/src/main.rs`;
     `sed -n '279,298p;894,906p' crates/store/src/sqlite.rs`. Confirm neither
     handler accepts sectors and neither store query has a sector predicate.
   - **S3/S4** — `sed -n '79,98p;155,181p;225,264p' crates/compliance/src/lib.rs`.
     Then run two failure-capable controls in a scratch test: (a) a body with two
     `User-agent: intel-platform` groups, asserting the second group's `Disallow`
     is currently **not** enforced; (b) a `/foo/bar/baz` rule against
     `/foo/bar/%62%61%7A`, asserting it is currently **allowed**.
   - **S5** — `sed -n '570,600p;617,655p' crates/compliance/src/lib.rs`;
     `sed -n '480,510p' crates/compliance/src/lib.rs`. Write a paused-clock
     control (`tokio::time::pause`) proving the first acquire after
     `apply_crawl_delay` currently does **not** wait, and that `acquires_for` was
     reset.
   - **S6** — `sed -n '160,185p;420,445p' crates/ingest/src/lib.rs`;
     `sed -n '143,163p' apps/cored/src/main.rs`. Confirm both the fail-open seam
     and the test that asserts it.
   - **S7** — `sed -n '260,285p' shell/intel_shell/app.py`;
     `grep -n 'store.save()' shell/intel_shell/app.py`. Reproduce the audit's
     control: a two-event batch whose second event is invalid, asserting the
     first event's mutation survives the HTTP 400 in live state.
   - **S8** — `sed -n '395,440p;595,615p;635,645p' crates/store/src/sqlite.rs`;
     `grep -rn 'update_document\|delete_document' --include=*.rs .` (expect no
     caller outside `sqlite.rs`).
4. Confirm the **v0.10.3 guards are still live** (identity set, evidence grade,
   resolving receipt paths, shared classifier invariants, 39/39 pins). Any
   regression here supersedes this entire cycle.
5. Record the measured entering state in `STATE.md`.

**Failure-capable control.** E0 must be able to refute. If any of S1–S8 no longer
reproduces on HEAD, say so explicitly and strike that Step; do not perform a fix
whose precondition is gone.

**Acceptance criteria.** 19/19 · golden 11/11 · 2/2 exact + 39/39 pins
independently re-hashed · checklist 77/77 · each defect and augment row confirmed
or refuted by captured output · four scratch controls (S3, S4, S5, S7) demonstrate
the current wrong behavior · `STATE.md` re-stamped.

**Done when** every downstream Step rests on a re-measured baseline, not on this
document's assertions.

---

## Step 2 · BIND-LOOPBACK (S1) — Make the topology invariant structural 🤖

**Objective.** `ARCHITECTURE.md` says the core is loopback-only. Make the process
refuse to start otherwise.

**Gate.** Touches `apps/cored/src/main.rs` and its tests only. Do not add a
network dependency. Do not add an override flag — see below.

**Steps.**

1. Parse before binding. Resolve `CORE_BIND` with `ToSocketAddrs` (so
   `localhost:8788` and `[::1]:8788` work) and require that **every** resolved
   address satisfies `ip().is_loopback()`. Refuse otherwise with a message that
   names the offending address and points at the multi-host deferral.
2. Refuse, do not warn, and **do not add an override environment variable.** An
   opt-out reintroduces the defect with extra steps; a genuine need for a
   non-loopback bind is the multi-host seam trigger firing, which is a design
   task. Record this reasoning in `STATE.md §6` as a decision with its
   alternative.
3. Extract the check into a pure function (`fn loopback_only(bind: &str) ->
   Result<Vec<SocketAddr>, String>`) so it is unit-testable without binding a
   socket — runners must be able to execute it.
4. Decide the `CORE_TOKEN` question explicitly (S1 augment). Under an enforced
   loopback bind, an optional shared secret is defensible defense-in-depth.
   **Record the decision in `STATE.md §6` either way** — the defect is that it is
   currently undecided, not that it is currently optional.
5. Reconcile the claims: `main.rs:28` and `ARCHITECTURE.md:173` may now be stated
   as enforced. Update the wording to say what enforces them.
6. Tests: `0.0.0.0:8788`, `[::]:8788`, and a LAN literal each rejected;
   `127.0.0.1:8788`, `localhost:8788`, `[::1]:8788` each accepted; a hostname
   resolving to a mix of loopback and non-loopback rejected.

**Acceptance criteria.** Non-loopback binds refused before `TcpListener::bind` ·
check is a pure, runner-testable function · no override flag · `CORE_TOKEN`
disposition recorded in `STATE.md §6` · `run` and `deploy/` unaffected · golden
11/11 · 39/39 pins.

**Done when** the sentence "the core is loopback-only" is enforced by something
that refuses, not by the launcher's habits.

---

## Step 3 · SECTOR-BIND (S2) — Give HC2 no unnamed exceptions 🤖

**Objective.** Every core endpoint that returns document bodies must take an
explicit sector set and filter it in SQL, or the architecture must name it as an
exception and a test must hold that exception set fixed.

**Gate.** Internal-API change. Touches `apps/cored/src/main.rs`,
`crates/store/src/sqlite.rs`, `shell/intel_shell/core_client.py`,
`shell/intel_shell/pipeline.py`, and tests. **The public `/v1/*` bodies do not
change.** Golden must stay 11/11 byte-identical — it is the tripwire.

**Steps.**

1. Add a sector-filtered store query:
   `documents_by_ids_in_sectors(ids: &[&str], sectors: &[String])` with
   `WHERE id IN (…) AND sector IN (…)`. Follow the established fail-closed
   convention at `search:314` and `vector_search:993`: an **empty sector set
   returns empty**, never everything.
2. Add `sectors` to `DocsQ` and make `docs()` use the new query. Rename the
   `parse_sectors(&p.ids)` call site to a correctly-named splitter so the code
   stops reading as if it already did this.
3. Thread the entitled sectors from the shell: `CoreClient.docs(ids, sectors)`
   and the `pipeline.py:135` call site, which already has the client's entitled
   sector list in scope from the `/view` call that produced `kept_doc_ids`.
4. **Decide `/embeddings/missing` explicitly and record it.** Two admissible
   outcomes, and the task must pick one in writing:
   - **(a) preferred** — add `sectors` to `MissingQ` and a sector predicate to
     `docs_missing_embeddings`, with the embed worker passing the full configured
     sector set. Cost is low and HC2 keeps zero exceptions.
   - **(b)** — declare it a named internal-maintenance exception. Then
     `ARCHITECTURE.md:184`'s HC2 row **must** be amended to name it, and a test
     must assert the exception set is exactly `{/embeddings/missing}` so it
     cannot silently grow.
   Silently leaving it as-is is not an option: that is the defect.
5. Tests: `/docs` with ids spanning two sectors and an entitlement for one
   returns only the entitled document; `/docs` with an empty sector set returns
   empty, not all; the same for `/embeddings/missing` under outcome (a), or the
   fixed-exception-set test under (b). Each must fail against the current code.

**Acceptance criteria.** `/docs` requires and enforces sectors in SQL ·
`/embeddings/missing` resolved under (a) or (b) with `ARCHITECTURE.md` and
`STATE.md §6` updated to match · empty sector set fails closed everywhere · shell
call sites updated · **golden 11/11 byte-identical** · 39/39 pins.

**Done when** `ARCHITECTURE.md:184` is true as written, or says exactly where it
is not and something tests that boundary.

---

## Step 4 · ROBOTS-MERGE (S3) — Combine same-token groups without merging `*` 🤖

**Objective.** RFC 9309 §2.2.1 conformance for duplicate product-token groups,
**preserving** the specific-beats-generic behavior the existing comment correctly
defends.

**Gate.** `crates/compliance/src/lib.rs` and its tests only. Read
`lib.rs:87-92` before writing a line — the comment is right about `*`, and a fix
that merges everything reintroduces the exact bug it prevents.

**Steps.**

1. Compute the best matching **specificity** first: the longest non-`*` product
   token that is a case-insensitive prefix of the UA.
2. Merge the rules of **every group containing a token at that same specificity**,
   in file order. If no non-`*` token matches, merge every `*` group instead.
   **Never merge `*` rules into a specific match.**
3. Resolve merged `Crawl-delay` conservatively: take the **maximum** across
   merged groups, consistent with `apply_crawl_delay`'s stated principle that
   publisher policy is a lower bound on our courtesy.
4. Update the doc-comment to state both halves of the rule — what is merged and
   what deliberately is not, and why.
5. Tests, each fail-before/pass-after:
   - two `User-agent: intel-platform` groups → both groups' `Disallow` rules
     enforced (the audit's control);
   - **the regression guard**: `*` disallows `/`, a specific group allows all →
     still allowed. This test is mandatory and must be named so its purpose is
     unmistakable;
   - a specific match plus an unrelated `*` group → `*` rules absent;
   - merged `Crawl-delay` takes the maximum.

**Acceptance criteria.** Same-specificity groups merged in file order · `*` never
merged into a specific match, with a named regression test · merged crawl-delay is
the maximum · doc-comment states both halves · golden 11/11.

**Done when** two identical `User-agent` lines cost a publisher nothing, and one
`*` line still costs us nothing.

---

## Step 5 · ROBOTS-NORMALIZE (S4) — Normalize percent-encoding before matching 🤖

**Objective.** RFC 9309 §2.2.2 / RFC 3986 normalization on both sides of the
comparison.

**Gate.** `crates/compliance/src/lib.rs` and its tests only. No new dependency
unless the workspace already carries a suitable one — a ~30-line normalizer is
cheaper than a lockfile change under HC12.

**Steps.**

1. Normalize **unreserved octets only**: percent-decode `%XX` when it encodes
   `ALPHA / DIGIT / '-' / '.' / '_' / '~'`. Uppercase the hex digits of every
   sequence left encoded.
2. **Do not decode reserved octets.** Decoding `%2F` to `/` would re-segment the
   path and can both over- and under-block. State this in the code comment; it is
   the trap in this fix.
3. Apply the same normalizer to the rule pattern and the request path before
   `path_matches`. Preserve `*` and trailing `$` as metacharacters through
   normalization — assert in a test that `%2A` does **not** become a wildcard.
4. Tests, each fail-before/pass-after: `/foo/bar/baz` blocks
   `/foo/bar/%62%61%7A` (the audit's case); `%2F` is **not** decoded; `%2a` does
   not become a wildcard; mixed-case hex normalizes identically; an already-
   normalized path is unchanged (idempotence).

**Acceptance criteria.** Unreserved octets decoded, reserved octets preserved ·
metacharacters survive normalization · normalizer applied to both sides ·
idempotent · all controls fail-before/pass-after · golden 11/11.

**Done when** two spellings of the same path get the same answer, and two
genuinely different paths still do not.

---

## Step 6 · DELAY-CLOCK (S5) — Preserve the politeness clock across a rate change 🤖

**Objective.** Adopting a publisher's `Crawl-delay` must change the interval, not
reset the clock or the counter.

**Gate.** `crates/compliance/src/lib.rs` and its tests only. `set_host_rate` must
stay synchronous — it is called from a sync context while `last` is an async
mutex, which is exactly why the current code replaces the whole limiter.

**Steps.**

1. Make the interval mutable in place rather than replacing the limiter. Store
   `min_interval` as an atomic (e.g. `AtomicU64` nanoseconds) that `acquire`
   reads and `set_host_rate` writes. This preserves `last` **and** `acquires`
   without making `set_host_rate` async.
2. `set_host_rate` on an unknown host still creates a limiter; on a known host it
   **updates** the existing one.
3. Keep the one-way rule at `apply_crawl_delay:491` intact — adopt only to slow
   down.
4. **Write a test that times the wait, not the configuration.** Use
   `tokio::time::pause()` / `advance()`: acquire once, apply a `Crawl-delay`,
   acquire again, and assert the second acquire actually waited the new interval.
   This is the control the audit correctly says does not exist.
5. Also assert `acquires_for(host)` is **not** reset across the rate change
   (S5 augment) and that `rate_for(host)` still reports the adopted rate.

**Acceptance criteria.** Interval updated in place · `last` and `acquires`
preserved · `set_host_rate` still sync · one-way slow-down rule intact ·
paused-clock elapsed-behavior test fails before and passes after · golden 11/11.

**Done when** the first document request after `robots.txt` waits, and something
in the suite would notice if it stopped.

---

## Step 7 · GATE-CLOSED (S6) — Fail closed when a network fetch has no robots cache 🤖

**Objective.** Close the library seam that permits a `Reach::Network` fetch with
no publisher policy.

**Gate.** `crates/ingest/src/lib.rs` and its tests only. `cored`'s own builder
comment (`main.rs:148-151`) already states the principle — "starting anyway would
mean starting a network-enabled harvester with no publisher robots check … 
refusing to start is the safe direction." This Step moves that principle from one
call site to the seam.

**Steps.**

1. Add an `IngestError` variant for a network fetch with no robots cache, and
   return it from `gate()` when `reach == Reach::Network && ctx.robots_cache.is_none()`.
2. **Invert the existing test, do not delete it.**
   `with_no_cache_the_configured_policy_governs_exactly_as_before_t2`
   (`:425-441`) asserts today's fail-open behavior. Rename it to name the new
   contract and assert the error. Preserve the `Reach::Offline` half of its
   coverage in a sibling test — offline reach with no cache must still be
   governed by the configured gate exactly as before.
3. Record the type-level alternative — making `Reach::Network` and
   `robots_cache: None` unrepresentable in `SourceContext` — in `STATE.md §6` as
   a considered-and-deferred option with its cost, rather than doing it here.
4. Tests: `Network` + `None` → the new error; `Network` + `Some(cache)` →
   unchanged behavior; `Offline` + `None` → unchanged behavior.

**Acceptance criteria.** `Reach::Network` with no cache is an error · the
defect-encoding test is inverted and its offline coverage preserved · shipped
`net` path unchanged · type-level alternative recorded in `STATE.md §6` · golden
11/11.

**Done when** a future connector cannot reach the network without a publisher
policy by forgetting a field.

---

## Step 8 · BILLING-ATOMIC (S7) — Make batches atomic in memory, not just on disk 🤖

**Objective.** A batch that returns HTTP 400 must leave live entitlement state
exactly as it found it.

**Gate.** `shell/intel_shell/app.py` and `billing.py` plus tests. Do not change
the webhook's authentication, its accepted event types, or the response shape.

**Steps.**

1. Apply the batch to a snapshot. Deep-copy the subscription state (or apply to a
   detached store instance), run every event against the copy, and publish the
   copy to the live store only after **all** events validate.
2. Keep `apply_event`'s contract — it already documents that persistence is the
   caller's job. Update its docstring to say the *mutation* is now batched too,
   so the docstring stops describing a property only half-delivered.
3. Preserve the existing `store.save()` ordering: publish, then save, then return
   results.
4. Tests, fail-before/pass-after:
   - the audit's reproduction — a two-event batch whose second event is invalid;
     assert HTTP 400 **and** that the first event's target is unchanged in live
     state (the `acme-research` sectors case);
   - after that 400, an unrelated operation that calls `store.save()` persists
     nothing from the failed batch;
   - a fully valid batch still applies every event and saves once;
   - an `ignored`/unhandled event type inside an otherwise valid batch still
     yields its `ignored` result.

**Acceptance criteria.** Failed batches leave live state and disk untouched ·
successful batches still save exactly once · docstring matches behavior · all four
controls fail-before/pass-after · golden 11/11.

**Done when** a rejected webhook cannot change who is entitled to what.

---

## Step 9 · STORE-IDENTITY (S8) — Rematerialize canonical identity on maintenance writes 🤖

**Objective.** The public store contract must not be able to leave dedup identity
stale, whether or not a product caller exists today.

**Gate.** `crates/store/src/sqlite.rs` and its tests only. No schema change.

**Steps.**

1. Wrap `update_document` in a transaction and call `assign_canonical_ids_tx`
   after the `UPDATE`, inside the same transaction.
2. Call `assign_canonical_ids_tx` inside `delete_document`'s existing transaction,
   after the row is removed, so surviving duplicates are reassigned rather than
   left pointing at a deleted id.
3. Source `max_distance` from the **same constant the ingest path uses**. If no
   shared constant exists, introduce one and route both call sites through it —
   do not write a second literal.
4. Document the cost honestly: rematerialization is corpus-wide. State in the
   doc-comment that these are maintenance APIs and are not on the ingest hot
   path, so correctness is the right trade here.
5. Tests, fail-before/pass-after: an update that changes body/fingerprint such
   that the canonical choice moves → `canonical_id` follows; an update that
   changes `published_day` such that the older-original tie-break moves →
   `canonical_id` follows; deleting a canonical row → its surviving duplicate
   becomes canonical and no row points at a deleted id; a no-op update leaves
   canonical ids byte-identical.

**Acceptance criteria.** Both methods rematerialize within their transaction ·
one shared `max_distance` constant · zero rows pointing at a deleted id in the
delete test · all four controls fail-before/pass-after · golden 11/11 · protected
DBs untouched.

**Done when** the corpus-identity invariant holds for every write path the store
exposes, not only the one the product happens to call.

---

## Step 10 · RE-MEASURE — Produce the authenticated v0.11.0 receipt 🧑

**One operator decision: authorize the hosted dispatch that produces authenticated
evidence for the v0.11.0 candidate.** Everything else is Codex's.

**Objective.** Produce a fresh release-grade deferred-audit receipt at the new
release commit under the v0.10.3 identity, authentication, durability, and
labeling rules.

**Gate.** Clean worktree at the candidate commit. `--expected-head` and
`--evidence-grade release` required. Never re-measure onto an existing evidence
path; never move a published tag.

**Steps.**

1. 🧑 Dispatch `ci.yml` from remote `main` with `audit_sha=<v0.11.0 candidate>`
   and `publish_evidence=true`. Confirm every job passes, each checkout is
   exactly the candidate, and each job emits one receipt carrying its `matrix`
   identity plus a persisted bundle.
2. Download receipts and bundles into the established
   `evidence/ci-runs/<run_id>-<attempt>/` layout; confirm seven **distinct**
   `(job, matrix)` identities.
3. On a clean worktree at the candidate, run the production audit with
   `--expected-head`, `--evidence-grade release`, `--require-attestations`, and
   the source-revision pin. Write `evidence/v0.11.0/deferred-audit/report.json`,
   confirm the trigger dispositions, and hash-pin it along with the new receipts
   and bundles.
4. Re-run `./run audit-deferred --rederive` on the new report.
5. **Negative controls, on a throwaway branch only:** one planted failing job
   (rejected as `conclusion:"failure"`) and one duplicated matrix leg (rejected by
   the identity guard). Delete the branch. Never on a release commit or tag.

**Acceptance criteria.** Seven authenticated receipts with seven distinct
identities accepted, zero rejected · both negative controls fire · new report is
release-grade, correctly labeled, hash-pinned, and re-derives · pin count updated
in `STATE.md` in the same task · golden 11/11 · published tags unmoved.

**Done when** the release rests on evidence produced under the guards this project
spent three cycles building.

---

## Step 11 · R-CLOSE — Close the cycle with one explicit release identity 🧑

**Objective.** Record the cycle's disposition and, if releasing, tag exactly one
commit.

**Gate.** Release only if the full definition of done holds and both Step 10
negative controls fired.

**Steps.**

1. **Decide the version number explicitly.** The default is **`v0.11.0`**, a
   minor bump: `/docs` gains a required parameter (internal-API break), and bind,
   robots, and billing-failure behavior change. The public `/v1/*` JSON bodies,
   the database schema, and the cache representation are unchanged — the same
   basis on which v0.10.0 was chosen. Record the reasoning, not just the number.
2. Reconcile `README.md`, `CHANGELOG.md`, `STATE.md`, `ARCHITECTURE.md`, and
   `AGENTS.md`; run `./run version-check`, `cycle-check`, `checklist-audit`,
   `progress-check`.
3. **Update `ARCHITECTURE.md §6` to reflect what is now enforced**: the HC1/HC2
   rows and the loopback claim at `:173` must describe the new structural
   guarantees — and must still say plainly what remains bypassable by a rewritten
   shell (A4). Do not let this cycle's fixes be written up as closing A4; they
   do not.
4. Append the **Cycle closing record**: date, disposition, release, release
   commit, annotated tag object, and per-Step implementation commits.
5. State the publication disposition as a decision with a trigger, not a default.

**Acceptance criteria.** Version choice recorded with reasoning · every diff path
accounted for · `ARCHITECTURE.md` invariant table matches enforced reality · A4
still stated as open · checklist fully checked and `checklist-audit` green · all
pins match · golden 11/11.

**Done when** v0.11's disposition is a recorded, measured decision.

---

## Cycle checklist

- [x] **E0** — entering state re-measured at v0.10.3; S1–S8 and every augment row confirmed or refuted; four scratch controls demonstrate current wrong behavior; v0.10.3 guards confirmed live
- [x] **BIND-LOOPBACK** — non-loopback binds refused before binding; pure runner-testable check; no override flag; `CORE_TOKEN` disposition recorded
- [x] **SECTOR-BIND** — `/docs` requires and SQL-filters sectors; `/embeddings/missing` resolved under (a) or (b) with `ARCHITECTURE.md` updated; empty sector set fails closed; golden byte-identical
- [x] **ROBOTS-MERGE** — same-specificity groups merged; `*` never merged into a specific match, with a named regression test; merged crawl-delay is the maximum
- [x] **ROBOTS-NORMALIZE** — unreserved octets decoded, reserved preserved; metacharacters survive; idempotent; controls fail-before/pass-after
- [x] **DELAY-CLOCK** — interval updated in place; `last` and `acquires` preserved; paused-clock elapsed-behavior test fails before and passes after
- [x] **GATE-CLOSED** — `Reach::Network` with no cache errors; the defect-encoding test inverted with offline coverage preserved; type-level alternative recorded
- [x] **BILLING-ATOMIC** — failed batches leave live state and disk untouched; successful batches save once; four controls fail-before/pass-after
- [x] **STORE-IDENTITY** — both maintenance writes rematerialize in-transaction; one shared `max_distance`; four controls fail-before/pass-after
- [x] **RE-MEASURE** — seven authenticated distinct-identity receipts accepted; both negative controls fired; release-grade report pinned and re-derived
- [ ] **R-CLOSE** — version choice recorded with reasoning; `ARCHITECTURE.md` matches enforced reality; A4 still open; disposition recorded with its trigger

---

## Standing prohibitions

- Do not mutate, delete, vacuum, or "refresh" `data/core.db` or
  `data/live-smoke.db`, and do not alter or re-pin any of the 39 existing
  evidence artifacts; their hashes are frozen. New evidence goes to fresh
  `evidence/v0.11.0/…` and `evidence/ci-runs/<run_id>-<attempt>/…` paths.
- **Do not weaken any v0.10.3 guard**: the `(job, matrix)` identity set, the
  `evidence_grade` requirement, the shared classifier invariants, the resolving
  receipt paths, the pin re-hash in `validate`, or the source-deterministic
  re-derivation.
- **Do not merge `*` robots rules into a specific product-token match.** The
  existing comment is correct about this and the regression test is mandatory.
- **Do not percent-decode reserved octets** in robots normalization, and do not
  let normalization turn an encoded literal into a metacharacter.
- Do not "fix" the crawl-delay transition by replacing the limiter, and do not
  reset `acquires` while doing it.
- Do not add an environment-variable override for the loopback check.
- Do not claim any task in this cycle makes HC1 invariant under shell replacement.
  A4 remains an accepted, open risk, and `ARCHITECTURE.md` must keep saying so.
- Do not change the public `/v1/*` JSON bodies, the SQLite schema, or the golden
  regression's 11 invariants. Golden stays 11/11 byte-identical after **every**
  task, not merely at cycle end.
- Do not hand-edit `Cargo.lock` (HC12), raise the offline Rust 1.78 floor, lower
  the Python 3.11 floor, or let core call an LLM (HC3). Prefer a hand-written
  normalizer over a new dependency in Step 5.
- Do not add a job or test that calls `production_measurements()`,
  `exact_cosine_measurement()`, `view_measurement()` benchmarks, or
  `verify-artifacts` unconditionally to `ci.yml` — runners have no built `cored`
  and no protected DBs. Every new check must be corpus-free and token-free.
- Do not commit `.env`, provider keys, tunnel aliases, or raw secret-bearing
  responses. The `192.168.0.192` host and its `18080`/`18081` forwarded ports are
  operator infrastructure and appear in no committed file — this matters more in
  a cycle whose subject is network binding.
- Do not batch `STATE.md` / `PROGRESS-v0.11.md` updates or combine two tasks in
  one commit.
- If any Step's Objective, Acceptance criteria, or "Done when" is amended after
  this file is first committed, name the amendment in a dated
  `## Runbook amendments` block in the same commit.

---

## Provenance of this draft

Every defect above was read out of the repomix export of the v0.10.3 tree on
2026-07-27 by path and line, and each is written as a hypothesis for E0 to confirm
or refute — not as a settled fact.

**The v0.10.3 self-audit was independently verified and is accurate.** All eight
findings reproduce at the cited locations, with the severity assignments correct
in every case — including the two the audit was careful to mark as dormant or
caller-free (S6, S8) rather than inflating them. Its positive claims also hold:
`/view`, `/search`, and `/retrieve` genuinely filter sectors in SQL, with both
retrieval legs failing closed on an empty sector set and `License::parse`
defaulting to `IndexOnly` on unparseable input; `ci-local` is exactly 19 jobs; and
the v0.10.3 machinery it inherited is intact — 39/39 pins re-hash byte-exactly,
the receipt declares `evidence_grade: release` with seven distinct verified
`(job, matrix)` identities whose paths all resolve to committed files, `task`
reads `v0.10.3 RECEIPT` from a derived value, and the one-way classifier
invariants are shared between the fresh and resume paths so they cannot drift.

Five things were added by independent re-verification:

- **`/embeddings/missing` is the same defect as `/docs`, and the audit does not
  name it.** `docs_missing_embeddings(model)` selects the entire corpus with no
  sector and no license predicate, and the handler returns `body` for every row.
  It is the broader of the two: `/docs` requires the caller to already know
  document ids, while this endpoint **enumerates**. The audit's HC2 row therefore
  understates the gap — `ARCHITECTURE.md:184` has two exceptions, not one. This
  one may well be a legitimate internal-maintenance need; what it may not be is
  unnamed.
- **The robots-merge fix has a trap, and the existing comment is the warning
  label.** `compliance/src/lib.rs:87-92` deliberately justifies *not* merging, and
  its reasoning is correct: merging `*` into a specific match would let a site
  that disallows `/` for everyone deny us everything. The audit's finding is
  about two groups sharing the *same* token, which is a different case. A fix that
  implements "merge all matching groups" literally reintroduces precisely the bug
  that comment prevents. Merge same-specificity only, and guard the `*` case with
  a named regression test.
- **The `Crawl-delay` transition also corrupts the audit counter.** Replacing the
  limiter resets `acquires` to zero alongside `last`. The doc-comment at
  `:595-599` says that counter exists so a harvest test can "confirm the limiter
  is consulted once per page **without timing the actual waits**" — so the
  transition damages the very substitute the suite uses in place of timing. The
  fix must preserve the counter, and the new test must actually time the wait.
- **The ingest suite encodes S6 on purpose.**
  `with_no_cache_the_configured_policy_governs_exactly_as_before_t2`
  (`ingest/src/lib.rs:425-441`) constructs `Reach::Network` with
  `robots_cache: None` and asserts the fetch is allowed, preserving the pre-T2
  world "bit for bit." It is not a stale test; it is a deliberate record of a
  behavior that should now change. Invert it and preserve its offline half —
  do not delete it.
- **The fix primitive for S8 already exists.** `assign_canonical_ids_tx` at
  `sqlite.rs:637` is transaction-scoped and callable from both maintenance sites;
  `delete_document` already holds a transaction. The only real design decision is
  where `max_distance` comes from, and the answer must be one shared constant
  rather than a second literal.

The through-line for this cycle: **the last three cycles hardened how the project
proves things; this one hardens what the project claims.** Every finding is a
property asserted in a comment or in `ARCHITECTURE.md` and upheld only by the way
the shipped caller happens to invoke it — loopback by the launcher's habits,
sector filtering by which ids the pipeline passes, publisher policy by which
`cored` build is compiled, politeness by a clock that is thrown away at the moment
it starts to matter, batch atomicity by a save that is skipped after the damage.
The suite is green throughout because HC13 is exactly right: fixtures prove the
state machine, not the wire. **A property is only real where something refuses to
proceed without it** — and that sentence now has to hold for invariants, not just
for evidence.
