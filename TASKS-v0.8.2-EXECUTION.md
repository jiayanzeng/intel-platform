# TASKS-v0.8.2-EXECUTION.md — conformance runbook for Codex

v0.8.2 is a **conformance cycle**. It ships no ingestion source, no product
surface, and no new dependency. Its entire job is to close the gap between what
`ARCHITECTURE.md` and `STATE.md` *claim* and what the tree actually *executes* —
the gap the post-v0.8.1 audit found in six places, and this document's own
source audit found in five more.

It sits **before** `TASKS-v0.9-EXECUTION.md`. v0.9 is an evidence-and-operations
cycle whose first real task is a `/view` benchmark against a disposable copy of
the live archive. Running that benchmark before Step 5 below would measure the
wrong thing (see A3), and copying the protected archives before Step 1 would
copy an unmeasured integrity state (see B0.2). So this cycle runs first.

**Entering state (asserted, not verified).** `HEAD` is `e212a7c`, two
operational/documentation commits ahead of annotated tag `v0.8.0` (`bfc8c5a`).
Runtime version sources report 0.8.0. The claimed matrix is 92 workspace Rust
tests, 20 net tests, 88 shell tests under Python 3.11 and 3.12; golden `11/11`;
protected artifacts `2/2` exact; warning-denied offline/net checks, clippy, fmt,
ShellCheck, Python floor compilation, and locked Rust 1.78 green. Protected
artifacts are `data/core.db` (1,764 documents) and `data/live-smoke.db` (2,600
documents), recorded in `config/protected-artifacts.sha256`.

**Every sentence above is a hypothesis until Step 1 measures it.** Prior
measurement is not permission to skip the entering-state run (`AGENTS.md §0`).

**How to run this file.** Top to bottom, one task and one commit at a time.
Obey `AGENTS.md §5` after every step: check the gate → implement → run every
acceptance criterion and capture the output → `./run golden` → `./run
verify-artifacts` → update `STATE.md` with what you *measured* → append
`PROGRESS-v0.8.md` → check the box here → commit.

Owner tags:

- **🤖 = Codex executes and self-verifies end to end.** Do not ask the operator
  to run anything marked 🤖.
- **🧑 = exactly one human input is required, named inline.** Everything else in
  that task is still yours.

**Progress log.** Continue appending to `PROGRESS-v0.8.md`. It already carries
v0.8 and v0.8.1; splitting the trail now would make the correction entries this
cycle produces harder to trace than the claims they correct. Step 2 records
that decision in `AGENTS.md`.

**Global definition of done.** Golden E2E `11/11` and byte-identical unless a
step declares otherwise; protected artifacts `2/2` exact after every step;
0 rustc warnings on `--workspace` **and** `--features net`; clippy and fmt
clean; all Rust and shell tests green; offline MSRV floor still 1.78; Python
floor still 3.11; `Cargo.lock` untouched except by a genuine dependency change
that a step declares (HC12).

**Why this cycle exists.** v0.8.1 turned the golden E2E, the protected
artifacts, the release version, and the Python floor into things a machine
checks. It did not do the same for the invariants in `ARCHITECTURE.md §3`. Four
of those invariants are currently enforced by prose alone, and one of them ships
with a verifier that is structurally incapable of failing. That last one is the
project's own §0 rule — *a test double that cannot fail is not a test* — sitting
uncaught in `crates/store/examples/`.

---

## Step 1 · B0.2 — Verify the entering state, and take the integrity census 🤖

**Objective.** Re-measure the entering state, and establish the one number
nobody has ever measured: how many rows in each protected archive carry a NULL
`simhash` or a NULL `canonical_id`. Every finding in this cycle is about what
happens when those are non-zero; the remediation must be designed against the
real number, not an assumption.

**Gate.** If any entering claim is false, record the correction in `STATE.md`
first and do not proceed. If the census finds a NULL of either kind in a
protected archive, **stop**: that is a corpus finding, not a code finding, and
it changes A2's design. Record it and surface it before writing any code.

**Steps.**

1. Clean build and test, both configs and the shell (`AGENTS.md §4`).
   `./run test`, then `./run golden`, then `./run verify-artifacts`.
2. Record `git rev-parse HEAD`, `git describe --tags`, `git status
   --porcelain`, and `git remote -v` (Step 11 needs the remote answer).
3. Census, **read-only, without opening the archives through `SqliteStore`**.
   `SqliteStore::open` runs `backfill_simhashes` and would silently repair the
   very thing being measured. Use `sqlite3` directly, on the protected files:

   ```
   for db in data/core.db data/live-smoke.db; do
     echo "== $db"
     sqlite3 "$db" "SELECT COUNT(*) FROM documents;"
     sqlite3 "$db" "SELECT COUNT(*) FROM documents WHERE simhash IS NULL;"
     sqlite3 "$db" "SELECT COUNT(*) FROM documents WHERE canonical_id IS NULL;"
     sqlite3 "$db" "PRAGMA integrity_check;"
   done
   ```

4. Re-verify both SHA-256 hashes **after** the census. `sqlite3` opens
   read-write by default and can rewrite a journal; if a hash moved, that is
   itself the finding — record it and stop.

**Acceptance.** Entering matrix re-measured and each number recorded ·
`git remote -v` output captured verbatim · four census numbers per archive
recorded · `PRAGMA integrity_check` = `ok` for both · both hashes exact
**after** the census · any false entering claim corrected in `STATE.md` before
Step 2 begins.

**Golden.** `11/11`, unchanged. **Commit:** one B0.2 baseline/status commit.

---

## Step 2 · D0 — Repoint `AGENTS.md` at the cycle actually being executed 🤖

**Objective.** `AGENTS.md` currently instructs an agent to read
`TASKS-v0.8-EXECUTION.md` (line 13), to read that file's objective and gate at
`§5.1`, and to check that file's box at `§5.8`. That cycle closed. An agent
following the contract literally would execute a closed runbook. Fix the
pointers *before* doing any work under them, or every subsequent step is done
against the wrong contract.

This step changes pointers and nothing else. Every other stale claim in the
documentation is Step 10's problem, deliberately kept in a separate commit so
that a pointer fix and a status correction never hide inside one another
(`AGENTS.md §5.9`).

**Gate.** If any pointer edit would also change a rule, stop — that is a Step 10
edit, not this one.

**Steps.**

1. `AGENTS.md` header: point at `TASKS-v0.8.2-EXECUTION.md` for this cycle's
   order and `TASKS-v0.9-EXECUTION.md` as the next cycle, with
   `PROGRESS-v0.8.md` still the log and a one-line note saying why it is not
   being split.
2. `AGENTS.md §5.1` and `§5.8`: same repoint.
3. `AGENTS.md §7`: leave the block rules alone; they are current.

**Failure-capable control.** `grep -rn "TASKS-v0.8-EXECUTION" AGENTS.md` must
return nothing except an explicit historical reference, if you keep one.

**Acceptance.** No live instruction in `AGENTS.md` points at a closed runbook ·
grep control clean · no rule text changed in this commit (`git diff` reviewed
line by line and the review recorded).

**Golden.** `11/11`, unchanged. **Commit:** one D0 pointer commit, docs only.

---

## Step 3 · A1 — Give the fingerprint verifier the ability to fail 🤖

**Objective.** `crates/store/examples/verify_fingerprints.rs` already contains
the NULL-fingerprint check: line 59 fails when `documents.len() !=
stored.len()`, and `fingerprints()` excludes NULL rows, so a NULL would make
those counts diverge. That clause is **unreachable by construction**. Line 24
calls `SqliteStore::open`, which runs `backfill_simhashes` and fills every NULL
before line 25 reads anything. The verifier can detect a *stale* fingerprint; it
can never detect a *missing* one, because opening the archive repairs it first.

It is also referenced nowhere — not in `run`, not in `.github/workflows/ci.yml`,
not in `AGENTS.md`, not in `STATE.md`. `cargo check --all-targets` compiles it.
Nothing executes it.

This step comes **before** A2 on purpose. A2 changes what the code does when a
fingerprint is missing; without a check that can observe a missing fingerprint,
A2's own acceptance criteria would be unfalsifiable.

**Gate.** If the census in Step 1 found NULLs in a protected archive, this
verifier must report them without modifying the archive. If it cannot be made
to do that read-only, stop and record — do not run it against a protected file.

**Steps.**

1. Read the NULL counts with a raw `rusqlite::Connection` opened
   `OpenFlags::SQLITE_OPEN_READ_ONLY`, **before** any `SqliteStore::open` call,
   exactly as `canonical_ids()` in the same file already does.
2. Report `null_fingerprints=N` and `null_canonical_ids=N` as first-class output
   lines alongside the existing `fingerprint_mismatches`, and fail on either.
3. Add `./run verify-fingerprints <db> [reference-db]` and wire it into
   `./run test` immediately after `verify-artifacts`, against a **fixture** DB —
   never a protected one.
4. Add a `verify-fingerprints` step to the `core` CI job over the golden
   fixture DB the harness already builds.

**Failure-capable control (required).** On a scratch copy, plant the fault the
verifier is supposed to catch and prove it catches it:

```
cp <fixture.db> /tmp/a1-null.db
sqlite3 /tmp/a1-null.db "UPDATE documents SET simhash = NULL WHERE id = (SELECT MIN(id) FROM documents);"
./run verify-fingerprints /tmp/a1-null.db     # must exit non-zero, name the id
sqlite3 /tmp/a1-null.db "SELECT COUNT(*) FROM documents WHERE simhash IS NULL;"  # must still be 1
```

The second `sqlite3` is the load-bearing half: it proves the verifier **did not
repair what it was measuring**. Repeat for a planted NULL `canonical_id`, and
for a planted body edit that leaves the fingerprint stale.

**Acceptance.** Planted NULL simhash ⇒ non-zero exit naming the document id ✅ ·
archive still holds the NULL after the run ✅ · planted NULL canonical id ⇒
non-zero exit naming the id ✅ · planted stale fingerprint ⇒ non-zero exit
(the pre-existing clause still works) ✅ · clean fixture ⇒ exit 0 with all three
counts printed as `0` ✅ · `./run test` runs it and `bash -n run` +
`shellcheck ./run` pass ✅ · CI step present ✅.

**Golden.** `11/11`, unchanged — this step adds a check, it does not change
behavior. **Commit:** one A1 verifier commit.

---

## Step 4 · A2 — Close the persisted-fingerprint invariant at all three sites 🤖

**Objective.** `ARCHITECTURE.md §3.8` states that `/view` and canonical
assignment consume the persisted fingerprint, that `/retrieve` reuses **only**
the persisted fingerprint, and that a missing value is *an error rather than an
invitation to hide a failed migration by recomputing*. `STATE.md §2.10` repeats
it. The code honors that at exactly one of three sites.

| site | file | current behavior | required |
|---|---|---|---|
| `/view` | `sqlite.rs:181` (`load_all_with_fingerprints`) | errors on NULL ✅ | keep, but make the error legible |
| `/retrieve` | `main.rs:838-842` | **recomputes** `simhash(title + body)` on a miss | error naming the document |
| canonical assignment | `sqlite.rs:515-516` | **silently excludes** `WHERE simhash IS NOT NULL` | error, or an explicit counted skip |

The upstream cause of the `/retrieve` miss is `fingerprints()` at
`sqlite.rs:453`, which itself filters `WHERE simhash IS NOT NULL` — so the map
handed to `/retrieve` is missing keys by construction, and the `None` arm is
reached without any error ever surfacing.

There is a second, quieter contradiction: the schema comment at `sqlite.rs:48-51`
asserts *"`canonical_id` is always set"*. That holds for every row inserted
through `append_new_tx` (the only Rust insert path, and it always fingerprints).
It does **not** hold for a row that arrived by migration, because
`assign_canonical_ids_tx` skips NULL-fingerprint rows entirely.

**Present risk is low; the invariant defect is not.** Both insert paths
fingerprint, `backfill_simhashes` is transactional, and Step 1 should confirm
zero NULLs in both archives. Say so plainly in `STATE.md` rather than
overstating. What is being fixed is that the guarantee is asserted structurally
and enforced by prose.

**Gate.** If closing the canonical-assignment site changes any `canonical_id`
in the golden corpus, **stop** — that is corpus movement, not a lint fix.

**Steps.**

1. Add `SqliteStore::missing_fingerprints() -> Vec<String>` (ids with NULL
   `simhash`), one query, no repair.
2. `fingerprints()`: keep the SQL filter but have the caller-facing contract be
   total. Simplest honest shape — return `Result<HashMap<String,u64>>` **and**
   have `/retrieve` fail closed when a fused doc id is absent from the map,
   with `500` and a message naming the id and pointing at
   `./run verify-fingerprints`.
3. Delete the `None => simhash(...)` arm at `main.rs:841` and its comment. The
   comment ("Pre-T9.1 rows carry no fingerprint; fall back rather than fail") is
   an accurate description of a decision that `ARCHITECTURE.md §3.8` reverses;
   remove it rather than leaving a dead reason (`ARCHITECTURE.md §7`).
4. `assign_canonical_ids_tx`: drop `WHERE simhash IS NOT NULL` and return an
   error naming the first offending id, **or** keep the filter and return the
   skipped count so the caller can refuse. Pick one and record which in
   `STATE.md §2.10` with the reason.
5. Make `load_all_with_fingerprints`'s failure legible: today a NULL surfaces as
   rusqlite's `InvalidColumnType at index 13`, which names no document. Map it
   to an error carrying the document id.
6. Correct `STATE.md §2.10` — its current sentence is false for two of the three
   sites, and correcting a claim found false is `AGENTS.md §5.6`, not optional.

**Failure-capable control (required).** Re-run every A1 control. Then, on a
scratch fixture core with a planted NULL: `/view` must fail naming the id;
`/retrieve` must fail naming the id; canonical assignment must fail or report
the skip. Prove each **before** the fix produces the old behavior (recompute /
silent skip) and **after** the fix produces the new one.

**Acceptance.** Three sites changed ✅ · each proven by a planted-NULL control
that failed before and passes after ✅ · no recompute remains on any request
path (`grep -n "simhash(" apps/cored/src/main.rs` returns only the import) ✅ ·
`STATE.md §2.10` corrected ✅ · full matrix green ✅ · both protected hashes
exact ✅.

**Golden.** `11/11` and byte-identical. The golden corpus has no NULLs, so no
number may move. If one moves, the gate has tripped. **Commit:** one A2 commit.

---

## Step 5 · A3 — Put sector filtering and id lookup back in SQL (HC2) 🤖

**Objective.** HC2 says sector filtering is enforced in **core SQL**
(`AGENTS.md §2`, `ARCHITECTURE.md §3.2` and the invariant map at line 150).
`store.search` honors that: `WHERE ... d.sector IN (...)` at `sqlite.rs:211`.
`/view` does not. `sector_corpus` (`main.rs:254-263`) calls
`load_all_with_fingerprints()` and filters with a Rust `HashSet`.

Enforcement is still inside the core, so this is a **placement** violation, not
a demonstrated leak — say that precisely. But the placement is load-bearing for
a second reason the audit note did not cover: the same full-corpus
materialization happens at three more sites, and none of them was flagged.

| endpoint | line | loads | needs |
|---|---|---|---|
| `/view` | `main.rs:694` → `254` | whole corpus + bodies + fingerprints | one sector set |
| `/retrieve` | `main.rs:827` | whole corpus + bodies | ≤ 8 fused ids |
| `/attest` | `main.rs:874` | whole corpus + bodies | ≤ 8 declared ids |
| `/docs` | `main.rs:976` | whole corpus + bodies | the requested ids |

Three of those four answer a question about at most eight documents by
deserializing every row and every body in the archive. Against the 12-document
golden corpus that is invisible. Against `live-smoke.db` at 2,600 documents it
is not. **This is why A3 precedes v0.9's `/view` benchmark:** benchmarking
`/view` cold/warm while `/retrieve` and `/attest` still do a full scan would
set an SLO against an artifact of this defect and then defend it.

**Gate.** If any SQL rewrite changes the golden numbers, stop. The point is
identical output at lower cost and correct placement — not new behavior.

**Steps.**

1. Add `SqliteStore::documents_in_sectors(&[String]) ->
   Result<Vec<(Document, u64)>>` — the `load_all_with_fingerprints` projection
   plus `WHERE sector IN (...)`, with the same not-null fingerprint contract A2
   established. Empty sector list ⇒ empty result, matching `search`'s existing
   guard at `sqlite.rs:200`.
2. Add `SqliteStore::documents_by_ids(&[&str]) -> Result<Vec<Document>>` —
   `WHERE id IN (...)`, bound parameters, no format-string interpolation of
   caller input.
3. `sector_corpus` calls (1). `/retrieve`, `/attest`, and `/docs` call (2).
4. Keep `load_all()` for genuinely whole-corpus consumers only, and note at its
   definition which callers those are.

**Failure-capable control (required).** A test that inserts a document in an
unentitled sector and asserts it is absent from `/view` **and** that the SQL
never returned it — assert on the store method, not only the handler, or the
test proves the Rust filter rather than the SQL one. For `documents_by_ids`,
plant an id containing a quote and a comma and assert it is bound, not
interpolated.

**Acceptance.** Four call sites converted ✅ · sector filter provably in SQL by
a store-level test ✅ · injection-shaped id bound safely ✅ · unentitled sector
absent from `/view` ✅ · full matrix green ✅ · a recorded before/after
wall-clock for one `/retrieve` against a **disposable copy** of `live-smoke.db`
(the number v0.9 will build its SLO on) ✅.

**Golden.** `11/11` and byte-identical. **Commit:** one A3 commit.

---

## Step 6 · A4 — Make `/attest`'s scope non-forgeable, or record the accepted risk 🤖

**Objective.** `ARCHITECTURE.md` line 149 justifies putting HC1 in the core with
one sentence: *the shell is rewritable; an invariant a rewrite can delete is not
one.* That justification holds for `/search` and `/view`, which gate
unconditionally at the data source. It does **not** hold for `/attest`.

`attest` (`main.rs:881`) inspects only `req.context_doc_ids` — a list supplied
by the shell it exists to constrain. `attest_answer`
(`crates/core/src/lib.rs:317-319`) then filters that list to `License::IndexOnly`
rows. A shell that passes `[]`, that drops the IndexOnly ids from the list, or
that simply does not call `/attest`, receives a clean answer. The core cannot
tell, because it does not know what the shell actually put in the prompt.

Today's shell is correct: `prompts.build_context` (`prompts.py`) emits exactly
one citation per context block, and `app.py:152-157` passes every citation's
`doc_id`, and `_core_guard` turns an attest failure into a `502`/`500` rather
than a bare answer. That is a well-written shell — which is precisely the
property the architecture says it must not have to rely on.

**Gate.** This is the only step in the cycle that changes a seam contract
(HC10 — `examples/coreClient.ts` and the README move with it). If the design
below cannot be implemented without changing the golden E2E's citation numbers,
**stop, record the finding and the accepted risk in `STATE.md §2.1`, and move
to Step 7.** An honestly recorded accepted risk is a result; a rushed seam
change is not.

**Design.** A context receipt, process-scoped exactly like `RobotsCache` and
`HostLimiters` under HC8:

1. `/retrieve` mints an opaque receipt id bound to the exact doc-id set it
   served, and returns it alongside `context`.
2. `AppState` holds a bounded map (receipt id → doc-id set), same bounding
   discipline as `RobotsCache`'s 512-origin cap — say 256 receipts, evicted
   oldest-first, with a short TTL.
3. `/attest` accepts `{answer, receipt}`. It resolves the doc-id set itself. A
   missing, expired, or unknown receipt is a `400`, not a pass.
4. Keep `context_doc_ids` accepted for one release for the TypeScript client,
   but have the core **refuse** it when a receipt is also configured, and record
   the removal date.

**Failure-capable control (required).** A mock shell that (a) sends `[]`,
(b) sends a receipt for a different retrieval, and (c) omits the receipt
entirely. All three must be refused. Then re-run T4P's existing leaking-mock
control and confirm it still reports `GUARD FIRED`. A control that only proves
the honest path still works proves nothing here.

**Acceptance.** Either the receipt shipped with all three negative controls
refused and the T4P leak control still firing ✅ · **or** the gate tripped, with
the specific reason and the accepted risk written into `STATE.md §2.1` and the
trigger for revisiting it recorded ✅ · if shipped: `examples/coreClient.ts`,
README, and `ARCHITECTURE.md §5` updated together (HC10) ✅.

**Golden.** May change only if the receipt path alters citation counts — which
it should not. State the expected value before running it (`AGENTS.md §6`).

**Commit:** one A4 commit, whichever way the gate falls.

---

## Step 7 · A5 — Bound the `/view` cache and validate its key 🤖

**Objective.** `view_cache` (`main.rs:65`, inserted at `681`) is an unbounded
`HashMap<String, CachedView>` keyed on a caller-supplied string. `parse_sectors`
does no validation against `cfg.sectors`, so every distinct `?sectors=` value —
including nonexistent ones — inserts a permanent entry holding a full
`ViewResp`. Nothing evicts. `RobotsCache` in the same process is deliberately
bounded to 512 origins and given a 24h TTL; the view cache got neither.

Loopback-only and token-guarded, so the severity is low. But `cored` is the one
process expected to stay up across harvests, and unbounded growth there is the
kind of thing that surfaces as an unexplained OOM three weeks later.

**Steps.** Intersect parsed sectors with `cfg.sectors` before they become a
cache key; bound the map (256 entries, oldest-first eviction) with the bound as
a named constant carrying the same style of comment `RobotsCache` has.

**Failure-capable control.** Insert 300 distinct valid keys; assert the map
never exceeds the bound and that a still-valid entry survives. Request 50
nonexistent sectors; assert the map does not grow.

**Acceptance.** Bound enforced under test ✅ · unknown sector does not create an
entry ✅ · cache hit/miss behavior otherwise unchanged, proven by the existing
`view_is_memoized_between_ingests_and_refreshed_after_one` test ✅.

**Golden.** `11/11`, unchanged. **Commit:** one A5 commit.

---

## Step 8 · A6 — Extend `version-check` to the tag and the changelog 🤖

**Objective.** `tools/version_check.py` reconciles four sources:
`apps/cored/Cargo.toml`, `shell/intel_shell/__init__.py`, the FastAPI
`version=` literal, and the `STATE.md` header. R1 also cut annotated tag
`v0.8.0` and added `CHANGELOG.md` — neither of which the checker reads. A future
release can therefore tag one version, changelog a second, and ship a third,
and `./run version-check` stays green. R1 made release identity executable for
four of the six things that carry it.

**Steps.** Parse the newest `## vX.Y.Z` heading in `CHANGELOG.md` and include it
in the reconciliation. Add `git describe --tags --abbrev=0` as a fifth source,
**warning** rather than failing when the working tree is ahead of the tag (the
normal state mid-cycle) and **failing** when the tag names a different version
than `Cargo.toml` at a tagged commit.

**Failure-capable control.** Change only the changelog heading to `v0.8.1`;
`./run version-check` must exit 1 and name `CHANGELOG.md`. Restore byte-for-byte
and confirm it passes. Repeat for a mismatched tag on a scratch branch.

**Acceptance.** Both planted mismatches exit 1 and name the right file ✅ ·
mid-cycle ahead-of-tag state does not fail ✅ · still passes at `0.8.0` ✅ ·
runs under the Python 3.11 floor ✅.

**Golden.** `11/11`, unchanged. **Commit:** one A6 commit.

---

## Step 9 · D1 — Reconcile HC9 and every stale status claim 🤖

**Objective.** One documentation commit, no code. Six separate contradictions,
each of which would mislead the next agent.

1. **HC9 is internally contradictory.** `AGENTS.md §2` says cursors are the one
   documented SQLite exception *and then* adds "without recording why", which is
   an escape clause. `ARCHITECTURE.md` line 153 drops the escape clause and
   states cursors are the sole exception. Meanwhile `ARCHITECTURE.md` line 44
   explicitly permits `sqlite:///…` subscriptions, and the tree has
   `subscriptions` (`shell/intel_shell/config.py`), plus `documents`,
   `embeddings`, `signals_history`, and `cursors` in `crates/store/src/sqlite.rs`.
   Resolve it by scope, which is what the rule was always about: HC9 governs
   **shell-owned configuration** persistence, where atomic-JSON is the default
   and SQLite requires a recorded reason; the **core archive** is SQLite by
   design and always was. Write the exception list explicitly — cursors,
   subscriptions, and the core store's own tables — with one line each.
2. **`TASKS-v0.8.md` line 157** still labels T4 `DEFERRED: embeddings
   unavailable`. T4 closed in v0.8.1 with a 6/6 real-model run.
3. **`TASKS-v0.8.md` line ~270** states HC1 is *"currently violated in principle
   on `/v1/ask`"*. T1 shipped `/attest`. This is the single most misleading
   sentence in the repository: it describes the project's headline invariant as
   broken when it is enforced.
4. **`TASKS-v0.8.md` line 264** says *"The corpus is 12 documents"* in the
   deferred-`/view` precondition. The live archives are 1,764 and 2,600. That
   sentence is the trigger for a deferred task; a stale trigger cannot fire.
5. **`AGENTS.md §4`** still reads *"clippy is tracked separately until T6
   promotes it to a gate."* T6 promoted it; the `lint` job is
   `continue-on-error: false`.
6. **`AGENTS.md §6`** labels the golden expectation `(v0.7)` while `./run
   golden` now asserts eleven named checks. The prose is already declared
   non-authoritative, but the version label invites the wrong comparison.

Also: `TASKS-v0.8.1-EXECUTION.md` line 33 says *"Five of the nine steps"*; the
file has ten numbered steps.

**Method.** `TASKS-v0.8.md` is a closed cycle's rationale. Do not rewrite its
body — add a dated status banner at the top recording what has since changed and
which lines are superseded. Rewriting closed-cycle rationale is how the drift
this project already fixed once gets reintroduced.

**Acceptance.** HC9 stated identically in both files, with the exception list ✅ ·
`TASKS-v0.8.md` banner added, body unrewritten ✅ · items 5 and 6 corrected ✅ ·
step-count typo fixed ✅ · `grep -rn "currently violated" *.md` returns nothing
live ✅ · no rule changed except HC9's scope, which is a rewording of an existing
rule and is called out as such in the commit message ✅.

**Golden.** `11/11`, unchanged. **Commit:** one D1 documentation commit.

---

## Step 10 · D2 — Make the progress log's own format executable 🤖

**Objective.** `PROGRESS-v0.8.md` declares itself append-only and specifies
`- commit: <hash>`. Of its 30 commit lines, 26 read "see git history" and only
two carry a real hash (`097b017`, `2b036d9`). Entry order is also broken: the
`T4 closure` entry at line 654 precedes the `T4P implementation` entry at 676
and the `T4 stopped at embedding gate` entry at 713 — later-written blocks
placed above the earlier events they depend on. An audit trail whose ordering
and identifiers are optional is a narrative, not a trail.

**Do not edit past entries.** The file's own rule is that corrections are made
by a new dated entry. Follow it.

**Steps.**

1. Append one dated correction entry recording the two defects, the counts
   above, and the specific out-of-order line numbers.
2. Add `tools/progress_check.py` and `./run progress-check`, enforcing on the
   **newest** entry only: header matches `### <ISO date> · <task id> — <text>`;
   an `- owner:` line; a `- commit:` line whose value matches `[0-9a-f]{7,40}`;
   and a date greater than or equal to the previous entry's.
3. Wire it into `./run test`. Scope it to the newest entry so history stays
   readable without a mass rewrite the file's own rules forbid.
4. From this cycle forward, `AGENTS.md §5.7` is satisfied only by a real hash.
   Since the hash is not known until the commit exists, the accepted pattern is:
   commit, then `git commit --amend` the progress line with the resulting short
   hash, or write the hash in the *next* entry's `notes`. Pick one, record it in
   `AGENTS.md §5`, and use it consistently for the rest of this cycle.

**Failure-capable control.** Append a scratch entry with `- commit: see git
history` — `./run progress-check` must exit 1 naming that line. Then one with a
date earlier than its predecessor — must exit 1 naming the ordering. Remove
both and confirm exit 0.

**Acceptance.** Both planted defects rejected with a named reason ✅ · clean file
passes ✅ · correction entry appended and no past entry edited (`git diff` shows
additions only) ✅ · `AGENTS.md §5` records the chosen hash-capture pattern ✅ ·
`shellcheck ./run` and the 3.11 byte-compile pass ✅.

**Golden.** `11/11`, unchanged. **Commit:** one D2 commit.

---

## Step 11 · C2 — Make CI a thing that ran, not a thing that is configured 🧑

**Objective.** `.github/workflows/ci.yml` is well-built: `--locked` everywhere,
a separate `--features net` job, a 1.78 MSRV job, blocking `lint`, a blocking
`golden` job, a 3.11/3.12 shell matrix, and a scheduled drift report. Every
comment in it traces to a real scar. And — per the audit — this checkout has no
git remote and no CI run evidence, so **not one of those jobs has ever
executed**.

That makes the workflow file the fourth instance of the exact failure `AGENTS.md
§0` names: `--features net` unbuilt for two cycles, robots policy never fetched,
an MSRV asserted against an unparseable lockfile, and now a CI configuration
nothing has run. It also means several `STATE.md` sentences are currently
unbacked: *"blocking in CI"* (clippy/fmt), *"the CI shell job is a blocking
3.11/3.12 matrix"*, and G1's *"runs as a blocking CI job"*. Those describe a
file, not a run.

**🧑 Human input required (exactly one):** decide and provide **either** a git
remote to push to, so a real run produces evidence, **or** an instruction to
proceed local-only. Nothing else in this step is the operator's.

**Gate.** Until captured output exists from an actual execution, every
`STATE.md` sentence asserting CI enforcement must be reworded to *"configured in
`.github/workflows/ci.yml`; verified locally by `./run ci-local`; never executed
by a CI runner."* That rewording is not optional and does not wait for the
operator's answer.

**Steps.**

- **If a remote is provided:** push, capture the run URL and per-job conclusions,
  and record them in `STATE.md` and `PROGRESS-v0.8.md`. Then plant one failure
  the workflow must catch — the cleanest is the C1 control, a PEP 701 f-string
  that 3.12 accepts and 3.11 rejects — confirm the 3.11 lane goes red, and
  revert. A green pipeline nobody has seen fail is still an unexecuted claim.
- **If local-only:** add `./run ci-local`, which executes the same job matrix in
  order (`version-check`, floor byte-compile, `shellcheck`, workspace check and
  test under `-D warnings`, net check and test, clippy, fmt, 1.78 locked check
  and test, pytest, `./run golden`, `./run verify-artifacts`,
  `./run verify-fingerprints`, `./run progress-check`), stops at the first
  failure, and prints a per-job summary. Then apply the rewording above.
- **Either way:** the `shell` job depends on ShellCheck being preinstalled on
  `ubuntu-latest`. That is true of current GitHub-hosted images and pinned
  nowhere. A runner image change would silently delete the gate rather than fail
  it — the same shape as the bug this whole file exists to prevent. Add an
  explicit install-or-assert step, and print `shellcheck --version`.

**Acceptance.** Operator decision recorded ✅ · either a run URL with per-job
conclusions **or** `./run ci-local` executing the full matrix with captured
output ✅ · one planted failure demonstrably caught (remote path) or the
equivalent local control (local path) ✅ · ShellCheck presence asserted rather
than assumed ✅ · every `STATE.md` CI sentence now matches what was actually
executed ✅.

**Golden.** `11/11`, unchanged. **Commit:** one C2 commit.

---

## Deferred beyond v0.8.2 (gates kept, unchanged)

- **T7 single-flight** — trigger is a second concurrent harvester. The shipped
  scheduler is one synchronous writer. Still not fired.
- **Postgres / pgvector / tantivy** — Postgres is a *concurrency* trigger, not a
  size one; pgvector wins only above ~10⁵ documents. `docs/T8-scale-design-note.md`.
- **Multi-host seam (UDS / mTLS)** — one host today.
- **Materialize `/view`** — precondition is measured warm-up cost crossing a
  predeclared SLO. A3 changes the cost model, which is exactly why the
  measurement belongs in v0.9 and after A3, not before it.

A5 bounds a cache and A3 moves filtering into SQL; **neither is permission to
open the materialization gate.** Measuring is not implementing.

---

## Cycle checklist

- [x] **B0.2** — entering state re-measured; NULL simhash/canonical census on both protected archives; hashes exact after the census
- [x] **D0** — `AGENTS.md` points at the cycle actually being executed
- [x] **A1** — fingerprint verifier can fail; planted NULL survives the run; wired into `./run test` and CI
- [x] **A2** — `/retrieve`, `fingerprints()`, and canonical assignment all fail closed on a missing fingerprint; `STATE.md §2.10` corrected
- [x] **A3** — sector filtering and id lookup in SQL at all four call sites; `/retrieve` cost measured against a disposable live copy
- [ ] **A4** — `/attest` scope non-forgeable, or the risk explicitly accepted with a trigger
- [ ] **A5** — view cache bounded and its key validated
- [ ] **A6** — `version-check` covers changelog and tag; both planted mismatches caught
- [ ] **D1** — HC9 resolved by scope; every stale status claim corrected; closed-cycle rationale bannered, not rewritten
- [ ] **D2** — progress-log format executable; correction entry appended; no past entry edited
- [ ] **C2** — CI executed or honestly downgraded; ShellCheck presence asserted

---

## Standing prohibitions for this cycle

- Do **not** touch `Cargo.lock` (HC12). No new dependency is needed by any step
  above; if one appears to be, that is a finding, not a step.
- Do **not** raise the offline MSRV floor above 1.78 or the Python floor above
  3.11. If a fix wants `Option::is_none_or`, keep the `#[allow]` and say why.
- Do **not** move license gating, sector filtering, or `/attest` out of the core
  (HC1, HC2). A3 moves filtering *further into* the core; that is the direction.
- Do **not** let the core call a model (HC3). A4's receipt is bookkeeping about
  strings the core was handed.
- Do **not** open, write, harvest into, or copy `data/core.db` or
  `data/live-smoke.db` except read-only, and never through `SqliteStore::open`,
  which repairs on open.
- Do **not** rewrite past `PROGRESS-v0.8.md` entries. Corrections are new dated
  entries.
- Do **not** batch status updates. `AGENTS.md §5`, every step.
- If a gate trips: record the measurement and stop. A gate you silence is worse
  than a task you skip.

---

## Provenance of this runbook

Written on 2026-07-24 against the `repomix` pack of the tree at `e212a7c` and
the Codex session transcript through the post-v0.8.1 audit report. **Nothing in
it was executed** — no build, no test, no query, no network call was made while
writing it.

Every claim about the source is a **read** of that pack, and reads go stale.
Specifically read and quoted from it: `main.rs:254-263, 674-694, 827-849,
874-892, 969-983`; `sqlite.rs:45-54, 143, 172-184, 194-239, 327-358, 389-446,
450-458, 511-559`; `crates/core/src/lib.rs:313-339`;
`crates/store/examples/verify_fingerprints.rs` in full; `shell/intel_shell/app.py`
`/v1/ask` and `_core_guard`; `prompts.build_context`; `tools/version_check.py`;
`.github/workflows/ci.yml`; `run`'s `cmd_test`; `ARCHITECTURE.md`;
`AGENTS.md`; the `PROGRESS-v0.8.md` entry headers and `- commit:` lines.

Three claims here are **not** reads and must be re-measured before they are
relied on:

- **The absence of a git remote and of any CI run** is the audit report's
  measurement, not one taken here — a `repomix` pack contains no `.git`.
  Step 11 re-measures it with `git remote -v` in Step 1.
- **Zero NULL fingerprints in the protected archives** is likewise the audit's
  measurement. **Zero NULL `canonical_id`s has never been measured by anyone**;
  the migration path (`backfill_simhashes` at `sqlite.rs:143`) fills fingerprints
  on open but never re-materializes canonical ids, and Step 1 exists to settle
  this.
- **The performance characterization in A3** ("invisible at 12 documents, not at
  2,600") is arithmetic from the recorded document counts, not a benchmark.
  A3's acceptance criteria include taking the actual number.

Treat this document the way `AGENTS.md §0` says to treat `STATE.md`: as a claim
until something executes it.
