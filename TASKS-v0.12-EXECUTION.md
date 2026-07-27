# TASKS-v0.12-EXECUTION.md — correction and operations-admission runbook for Codex

v0.12 is a **correction cycle**. It exists because v0.11 closed and published
with a checklist reading 11/11 while one task's acceptance criteria were not met,
and because a body of live-verified operations work now sits in the worktree with
no runbook governing it.

Both halves share one root cause, and it is the same one v0.11 was organized
around: *a claimed property that nothing executes is not a property.* v0.11
turned that doctrine on the source. It did not turn it on the **runbook's own
verification apparatus**, and that is where it failed:

- `checklist_audit.py` resolves a checked box to a progress entry and to a real
  commit. It proves **provenance**, never **property**. A box checked over a
  false claim resolves exactly as cleanly as a true one, which is why 11/11,
  19/19, 54/54 and 11/11 golden were all green while STORE-IDENTITY's central
  criterion was false.
- STORE-IDENTITY's **Gate** ("`crates/store/src/sqlite.rs` and its tests only")
  scoped the work to one file while its **acceptance criterion** ("one shared
  `max_distance` · no second production literal") asserted a *repo-wide absence*.
  Codex was locally compliant and globally wrong. A gate narrower than its
  criterion makes the criterion unverifiable inside the gate.
- The v0.11 standing prohibition at `TASKS-v0.11-EXECUTION.md:693-696` asserts
  that the host `192.168.0.192` and ports `18080`/`18081` "appear in no committed
  file." That sentence was **already false when it was written** — see the C5
  row below. Nothing executed it, so nothing caught it.

This cycle does six things and deliberately no more:

1. **makes the non-paged ingest path atomic** — corpus identity can no longer be
   left stale by a committed append whose rematerialization failed;
2. **removes the second production threshold literal** by removing the seam that
   invites it, not by copying the constant;
3. **gives repo-wide absence claims an executable home** (`./run invariant-scan`,
   ci-local job 20) so "no second X anywhere" becomes a check rather than a
   reading;
4. **records the v0.11 retraction honestly** without rewriting a published
   release;
5. **decides the operations authorization model** and makes it structural rather
   than prompt-level;
6. **admits the model-profile work** under a runbook, with its fail-closed claims
   actually tested.

It ships no new ingestion source and no subscriber-facing surface. The public
`/v1/*` JSON bodies, the SQLite schema, and the golden regression's 11 invariants
are unchanged. **Golden stays 11/11 byte-identical through every task in this
file.**

**Version disposition (decide at R-CLOSE, default recorded here).** The default
is a **minor release `v0.12.0`**, on the v0.10.0/v0.11.0 precedent: `./run models`
is new operator-facing surface, and `/ingest` failure semantics change. The
alternative — `v0.11.1` for Steps 2-5 alone, then `v0.12.0` for the operations
half — is more honest about the two halves but costs a second hosted RE-MEASURE
and a second operator authorization. **Recommendation: one cycle, `v0.12.0`,**
with the correction steps gated ahead of the operations steps so the defect is
fixed first regardless of what happens to the operations half. `v0.11.0` stays
published and unmoved; its defect is recorded as errata, not erased.

---

## Entering state (asserted, not yet verified)

Taken from `STATE.md` (v0.11.0), `PROGRESS-v0.11.md`, and the Codex post-release
self-audit. **Every sentence here is a hypothesis until Step 1 (E0) measures it.**
Prior measurement is not permission to skip the entering-state run — including
when the prior measurement is your own or your predecessor's.

- `v0.11.0` is released and published. Annotated tag object
  `fcfa4825e6ffbc06c0ad73e18044965c10786aa8` dereferences to release commit
  `6daeb7e9f2cc0022b5e1a1dcf2ce8702b5be0321`. Hosted run **30236305375** attempt
  **1** passed seven jobs against evidence candidate
  `17221504d0c572e2b52f8509cb720d4a7c72f47d`. Manifest schema 2 matches **54/54**
  pins. **None of this is reopened by this cycle.**
- `./run ci-local` **19/19**; Rust **119 workspace / 21 net**; golden **11/11**;
  protected artifacts **2/2**; `cycle-check`, `checklist-audit` (88/88 checked
  across nine closed runbooks, zero exemptions), `progress-check` green.
- **The worktree is dirty.** Untracked: `intel-platform-OPERATIONS.md`,
  `tools/model_profiles.py`, `shell/tests/test_model_profiles.py`. Modified:
  `run`, `AGENTS.md`, `STATE.md`. This work is live-verified on real hardware but
  governed by no runbook and recorded in no progress log.
- Shell test count is **ambiguous by construction** and E0 must disambiguate it:
  `STATE.md:3` claims **200/200**; every `PROGRESS-v0.11.md` entry claims
  **191/191**; the nine-test delta is exactly `shell/tests/test_model_profiles.py`,
  which is untracked. A checkout of `v0.11.0` reproduces 191, not 200.

### Defects this runbook is drafted against (verify, do not trust)

Each was read out of the repomix export of the post-v0.11.0 worktree on
2026-07-27 by path and line and is a hypothesis until E0 confirms or refutes it.
**C1-C2** are the Codex self-audit's two findings, independently reproduced by
reading. **C3-C7** are additions from independent re-verification and must be
honored alongside them.

| # | Location | Claim to verify |
|---|---|---|
| **C1** [P1] | `apps/cored/src/main.rs:788`, `:794-795`; `crates/store/src/sqlite.rs:202-208` | `append_new` opens its own transaction and **commits**. The non-paged (RSS) handler then calls `assign_canonical_ids(16)` in a *second* transaction and `bump_generation()` after that. A failure in the second leaves documents durably committed with stale `canonical_id` **and** a stale view generation, behind an HTTP 500. Codex measured this against the real `cored`: 1 document before, HTTP 500, 5 documents after, 4 `techwire` rows committed. Contradicts `ARCHITECTURE.md:112-115` and `AGENTS.md:111-113`. |
| **C1** [augment] | `crates/store/src/sqlite.rs:806-818`; `apps/cored/src/main.rs:257-280` | **The correct shape already exists and is one function away.** `commit_harvest_page` does `append_new_tx` + `assign_canonical_ids_tx` in one transaction, and `CursorAdapter::commit_page` bumps generation only after it returns `Ok`. The paged path is correct; only the non-paged tail is not. The fix is to make `append_new` match `commit_harvest_page`, **not** to add a second method a caller may forget to choose. |
| **C1** [augment] | `apps/cored/src/main.rs:762-775` | **Do not over-fix.** Earlier *paged* commits are durable by design when a later page fails (the code comment at `:763-764` says so deliberately). A 500 from a paged source legitimately leaves rows behind. The regression test must therefore use a **non-paged** fixture (`techwire`), or it will assert a property the architecture does not claim. |
| **C2** [P2] | `apps/cored/src/main.rs:794`; `crates/store/src/sqlite.rs:32` | `DEDUP_MAX_DISTANCE = 16` is declared **module-private** in `sqlite.rs`. The store's own three call sites (`:467`, `:485`, `:817`) use it; the one production call site outside the crate uses the literal `16`. Contradicts `TASKS-v0.11-EXECUTION.md:547-549` and the claim at `PROGRESS-v0.11.md:264-267` that "there is no second production threshold literal." |
| **C2** [augment] | `crates/store/src/sqlite.rs:651` | **The API invites the literal.** `pub fn assign_canonical_ids(&self, max_distance: u32)` requires every caller to name a threshold, so any caller outside the crate *must* either import a constant or write a number. Exporting `DEDUP_MAX_DISTANCE` would satisfy the letter of Step 9 and leave the seam open. Closing the seam means the production path stops passing a threshold at all. |
| **C3** [P2] | `tools/checklist_audit.py:21`, `:272-361` | `CHECKED_RE` finds checked boxes; `run()` resolves each to a progress entry and an existing commit. **Nothing compares a box to its acceptance criteria.** This is not a bug in the tool — it is the tool's stated scope — but it means the project's headline completion number cannot detect the exact failure that occurred, and `11/11` will keep reporting green over the retracted task forever unless retraction is made a first-class record. |
| **C4** [P2] | `STATE.md:3` | The release-status header claims the shell suite is **200/200** under Python 3.11.4 and 3.12.13. Nine of those tests are in untracked `shell/tests/test_model_profiles.py`. The published release commit reproduces **191/191**. A release-identity header has absorbed uncommitted worktree state — the same class of drift `PROGRESS`/`STATE` separation exists to prevent. |
| **C5** [P2] | `TASKS-v0.11-EXECUTION.md:693-696` vs `.env.example:11`, `README.md:166`, `shell/tests/test_llm_config.py:189-212`, `PROGRESS-v0.9.md:37-39`, `STATE.md:2636-2638` | The prohibition states the `192.168.0.192` host and its `18080`/`18081` forwarded ports "appear in no committed file." **All five listed files are committed and contain them**, predating the model-profile work. The new untracked files do not create this conflict; they make it undeniable. Codex's "reconcile before committing" is correct but understates it: the rule is not merely in tension with new work, it is a false statement about the repository, and no check has ever executed it. |
| **C6** [P1] | `intel-platform-OPERATIONS.md:394-416`; `run:828-830`; `tools/model_profiles.py:27-48` | **The standing authorization is granted to a mutable artifact.** It whitelists `./run models …` without per-command approval; `cmd_models` execs `tools/model_profiles.py`; that file builds free-form shell strings (`TRANSITIONS`) and sends them over SSH. Both files are agent-editable. The whitelist's guarantee — "lifecycle on exactly five named containers" — is therefore upheld by current file *content*, not by anything that would refuse. This is A4's shape on the operations side, and it must be either made structural or named as an open accepted risk. It must not be left implied. |
| **C7** [P2] | `shell/tests/test_model_profiles.py` (9 tests) vs `tools/model_profiles.py` (35 functions) | Tests cover exactly two pure functions, `classify_profile` and `transition_script`. `intel-platform-OPERATIONS.md:33-36` claims missing containers, foreign listeners, health failures, and partial/overlapping profiles all fail closed. **Only the partial/overlapping claim executes.** Foreign-listener refusal (`:353-360`), health-failure refusal (`:275-300`), missing-container refusal (`:263-270`), and stale-socket handling (`:192-199`) are asserted in prose and verified by one live run that cannot be re-run in CI. |
| **C7** [augment] | `tools/model_profiles.py:251-260`, `:263-270`; `run:828-830` | Three smaller items to dispose of explicitly, not silently: `_container_rows` does `line.split("\t", 2)` and raises `ValueError`, not `ProfileError`, on malformed remote output; `_require_containers` demands **all five** containers exist, so intel-platform switching hard-fails if an operator ever removes an Athenaeum container (a real cross-project coupling — record it as a decision or narrow it to the profile's own roles plus those it must stop); `cmd_models` deliberately bypasses `ensure_venv` and calls bare `python3` so it works before a venv exists — correct, but currently undocumented. |

---

## How to run this file

Execute top to bottom, one task and one commit at a time. Follow `AGENTS.md §5`
after **every** task: check the gate first, implement, run and capture every
acceptance criterion, run `./run golden`, update `STATE.md`, append
`PROGRESS-v0.12.md`, check the box here, and commit. Implementation commit and
audit-record commit stay separate. Do not batch status updates.

- **🤖 = Codex executes and self-verifies end to end**, with no live model
  endpoint, no publication, and no push.
- **🧑 = exactly one named operator action or decision is required.**

**Dependency gates.** Steps 2-5 are the correction half and are **independent of
the operations half**; they must complete first. Step 8 is blocked by Steps 6 and
7 — the operations work cannot be committed until the infrastructure-disclosure
policy and the authorization model are decided, because committing it is what
makes both questions concrete. Step 9 is blocked by Step 8.

### Cycle activation (before E0)

`AGENTS.md` declares v0.11, now closed with a valid release record. This runbook
arrives untracked into a **dirty worktree**, which is new: prior cycles activated
from a clean tree.

In a **separate preparatory implementation/audit pair** before E0:

1. Capture the full dirty-state inventory first — `git status --porcelain=v1`,
   and `git diff` for each modified tracked file — into the E0 record. **Do not
   stash, revert, clean, or commit any of it.** Codex correctly preserved this
   work; preserving it is now a gate.
2. Commit **only** this runbook, the `AGENTS.md` header declaring v0.12 active,
   and a new `PROGRESS-v0.12.md`. The untracked operations files stay untracked
   until Step 8.
3. Run `cycle-check` and `checklist-audit`.

**Do not claim E0's test, golden, or artifact acceptance from this preparatory
commit.**

### Session opener (run before reading further)

```bash
git status --porcelain=v1
git describe --tags --always --dirty
git rev-parse HEAD
git rev-list --left-right --count origin/main...HEAD
git tag --list 'v0.11*' --format='%(refname:short) %(objectname) %(*objectname)'
sed -n '1,20p' AGENTS.md
sed -n '1,6p' STATE.md
```

### Global definition of done

Protected hashes exact; **all 54** evidence pins still match; golden **11/11
byte-identical**; `./run version-check` green; zero rustc warnings on offline and
net builds; all Rust tests green; all shell tests green under Python 3.11 **and**
3.12; clippy, fmt, ShellCheck, floor byte-compilation, and locked Rust 1.78 green.
No mock, fixture, double, health response, hand-authored receipt, or workflow
configuration is promoted to wire evidence.

**The `ci-local` job count enters this cycle at 19 and exits at 20.** Step 4 adds
exactly one job (`invariant-scan`) and records the new count in `STATE.md` and
`PROGRESS-v0.12.md` in that same task. No other task may change the count.

**Every check this cycle adds must run on `ci.yml` runners** — source, config, and
git only; never the built `cored` binary, the protected DBs, a network route, or
the LAN server. `invariant-scan` in particular is a **static** scan and must not
acquire a runtime dependency.

**The public `/v1/*` JSON bodies and the SQLite schema do not change.** `/ingest`
response *semantics* change only in the failure case, and that change is the
point of Step 2.

---

## Deferred means deferred

None of the standing deferral triggers fires in this cycle.

| Deferred item | Unchanged trigger | v0.12 action before the trigger |
|---|---|---|
| T7 robots single-flight | a second concurrent harvester | none |
| Postgres | a second archive writer | none |
| pgvector | exact cosine stops fitting the measured request budget | none |
| Multi-host seam hardening | an actual core/shell host split | none — the LAN model server is not a core/shell split; core and shell remain co-located on the Mac and the server hosts only model inference |
| A4 untrusted-shell boundary | a third-party/untrusted shell, or any claim HC1 is invariant under shell replacement | none — Step 7 addresses the *operations* analogue of A4 and must not be written up as narrowing A4 itself |
| CI-runner evidence | an authenticated receipt set with identified matrix legs, durably committed | re-measure at the new release commit only |

**Step 6 is not the multi-host trigger firing**, and Step 7 is not A4 closing.
Both concern operator infrastructure that sits entirely outside the core-shell
boundary. Any progress entry that blurs this fails its own acceptance.

---

## Step 1 · E0 — Rebuild the entering state and confirm the seven findings 🤖

**Objective.** Reproduce the post-v0.11.0 state from commands, preserve and
inventory the dirty worktree, and confirm or refute C1-C7 against HEAD before
changing anything.

**Gate.** The session opener has run and its output is captured. If any tracked
file in the dirty set cannot be explained by the operations work, stop and report
before proceeding.

**Steps.**

1. Run the full entering matrix and capture every number: `./run ci-local`,
   standalone `./run golden`, `./run verify-artifacts`, `./run cycle-check`,
   `./run checklist-audit`, `./run progress-check`, `./run version-check`.
2. **Disambiguate the shell test count (C4).** Run the shell suite as-is and
   record the number. Then run it with `shell/tests/test_model_profiles.py`
   temporarily moved outside the collection root — a move, restored immediately,
   never a delete — and record that number. Confirm the delta is exactly nine and
   that `STATE.md:3`'s 200 is the dirty-worktree number.
3. **Reproduce C1 with a failure-capable control, not a reading.** Against a
   scratch DB and the real `cored`, force `assign_canonical_ids` to fail after a
   successful `append_new` on a **non-paged** source (`techwire`). Record:
   documents before, HTTP status, documents after, and whether the view
   generation moved. This is the fail-before capture Step 2 inverts.
4. **Reproduce C2 mechanically:** `grep -rn 'assign_canonical_ids(' --include='*.rs'`
   and classify every hit as production or `#[cfg(test)]`. Record the exact
   production hits and their arguments.
5. **Reproduce C5 mechanically:** `grep -rln '192\.168\.0\.192\|18080\|18081'`
   over tracked files only (`git ls-files`), excluding `evidence/`. Record the
   full list. Confirm whether each hit predates the operations work.
6. Confirm or refute C3, C6, and C7 by reading the cited lines and recording what
   is and is not executed.
7. Record which of C1-C7 **refute**. A refuted row is a finding, not a failure —
   the later step then narrows or closes with the reason recorded.

**Acceptance criteria.** Entering matrix captured in full · dirty inventory
recorded and untouched · shell-count ambiguity resolved with both numbers · C1
reproduced as a measured failure-capable run, not a reading · C2 and C5
reproduced as command output · C3/C6/C7 dispositions recorded · published
`v0.11.0` tag and evidence unchanged and re-verified.

**Done when** the entering state is a set of captured measurements and every
finding this runbook acts on has been confirmed or refuted by execution.

---

## Step 2 · INGEST-ATOMIC (C1) — One durability unit for every corpus write 🤖

**Objective.** Make it structurally impossible for a committed append to leave
canonical identity stale, on **every** public write path, not only the paged one.

**Gate.** `crates/store/src/sqlite.rs`, `apps/cored/src/main.rs`, and their tests.
No schema change. No change to the `/ingest` success-path response body.

**Steps.**

1. Fold the rematerialization into `append_new` itself, mirroring
   `commit_harvest_page:806-818`: open the transaction, `append_new_tx`, and when
   `n > 0` call `assign_canonical_ids_tx(&tx, DEDUP_MAX_DISTANCE)` **inside** it,
   then commit. Update the doc-comment to state the contract in one line: adding
   documents and rematerializing identity are one durability unit.
2. **Prefer this over adding a second method.** A parallel
   `append_new_canonical` would leave `append_new` as a public way to get it
   wrong. If a genuine caller needs an append without rematerialization, that is a
   design decision to record with its reason — not a default to preserve.
3. Reduce the handler at `main.rs:788-796` to the append plus
   `if tail_new > 0 { st.bump_generation(); }`. No fallible operation may sit
   between the successful commit and the bump.
4. **Regression, fail-before/pass-after, on a non-paged source.** Invert the E0
   control: a failure injected in rematerialization must leave the document count
   unchanged and the generation unmoved, and still return 500. Assert all three.
5. **Guard the boundary of the claim with a second test.** A paged source whose
   later page fails must still leave earlier committed pages durable, with their
   canonical ids assigned and generation bumped — the existing designed behavior.
   Step 2 must not silently convert C1 into a broader atomicity claim the
   architecture does not make.
6. Record in `ARCHITECTURE.md §3` item 8 that rematerialization is now
   transactional on **every** store write path that adds, changes, or removes
   rows — replacing the current "on every ingest that adds rows" phrasing, which
   is true of intent and was not true of the code.

**Acceptance criteria.** `append_new` rematerializes in-transaction · zero
production call sites perform append and assignment in separate transactions ·
the non-paged failure control fails before and passes after, asserting count,
generation, and status · the paged-durability control passes both before and
after · `ARCHITECTURE.md` §3 item 8 matches enforced reality · golden 11/11
byte-identical · protected DBs untouched.

**Done when** the corpus-identity invariant survives a failure, not merely a
success.

---

## Step 3 · THRESHOLD-ONE (C2) — Close the seam, not just the instance 🤖

**Objective.** Remove the second production threshold literal by removing the
reason a caller has to name a threshold at all.

**Gate.** Blocked by Step 2 (which deletes the offending call site's need to
exist). `crates/store/src/sqlite.rs`, `apps/cored/src/main.rs`, `tools/`, and
tests.

**Steps.**

1. After Step 2, `main.rs` no longer calls `assign_canonical_ids`. Confirm by
   grep that **no production caller outside `crates/store/src/sqlite.rs`
   remains**.
2. Dispose of the public `assign_canonical_ids(max_distance)` seam explicitly,
   choosing one and recording the reason:
   - **(a)** keep it public as a maintenance/backfill entry point, documented as
     such, and enforce by scan that no caller outside the store crate uses it; or
   - **(b)** make it `#[cfg(test)]`-visible plus a no-argument public
     `rematerialize_canonical_ids()` that sources `DEDUP_MAX_DISTANCE` itself.
   **(b) is preferred**: it makes the threshold unnameable from outside, so the
   defect cannot recur by a different route. Choose (a) only if a real
   out-of-crate caller exists, and name it.
3. Do **not** export `DEDUP_MAX_DISTANCE`. Exporting it satisfies the letter of
   v0.11 Step 9 and leaves the seam that produced the defect wide open.
4. Write the first `invariant-scan` rule, **R1**, in a new
   `tools/invariant_scan.py`: no `assign_canonical_ids` call site outside
   `crates/store/src/sqlite.rs` may pass a numeric literal, and (under (b)) none
   may exist at all outside `#[cfg(test)]`. Ship it with a **captured
   fail-before**: reintroduce the literal in a scratch worktree, run the rule, see
   it fire, restore. A rule that has never fired is not a rule.
5. Test literals at `sqlite.rs:1462`, `:1496`, `:1503`, `:1528`, `:1638` are out
   of scope by design — but state that scope decision in the rule's docstring, so
   the next reader knows it was decided rather than missed.

**Acceptance criteria.** Zero production `assign_canonical_ids` call sites outside
the store crate · the chosen disposition recorded with its reason ·
`DEDUP_MAX_DISTANCE` not exported · R1 exists, is scoped in writing, and has a
captured fail-before/pass-after · golden 11/11.

**Done when** a second production threshold literal cannot be written without a
check refusing it.

---

## Step 4 · INVARIANT-SCAN (C3) — Give absence claims an executable home 🤖

**Objective.** Turn this project's recurring class of claim — "X appears nowhere",
"only one Y exists", "no path does Z" — from prose into exit codes.

**Gate.** Blocked by Step 3 (which creates `tools/invariant_scan.py` and R1).
Static analysis only: source, config, and git. No binary, no DB, no network.

**Steps.**

1. Promote `tools/invariant_scan.py` to a `./run invariant-scan` subcommand and
   add it to `ci-local` as **job 20**. Record the count change in `STATE.md` and
   `PROGRESS-v0.12.md` in this task, with the reason.
2. Define the rule contract in `config/invariant-rules.json`: each rule carries
   `id`, `claim` (the sentence in prose it makes executable), `source` (the file
   and line where that sentence lives), `scope`, and `fail_before` (the commit or
   captured output proving it has fired). **A rule with no `fail_before` is
   rejected by the scanner itself.**
3. Seed with R1 (Step 3) plus:
   - **R2** — the loopback claim: no production bind expression outside the
     validated path in `main.rs`.
   - **R3** — HC3: no LLM client import, base-URL constant, or provider call
     reachable from `crates/`.
   - **R4** — the credential rule from Step 6, once Step 6 has decided its text.
   - **R5** — no second `DEDUP_MAX_DISTANCE`-class threshold literal in
     production Rust (generalizes R1 to the pattern, not the instance).
   Each rule ships with its own captured fail-before. Add no rule you cannot make
   fire.
4. **Extend `checklist_audit.py` with retraction awareness** (this is the C3 fix
   proper). Add `config/checklist-retractions.json`, mirroring the exemptions
   schema — `runbook`, `task_id`, `date`, `reason`, `accepted_by`, plus
   `corrected_by` naming the later runbook and task. `checklist-audit` loads and
   validates it exactly as it validates exemptions, and reports
   `N checked, M retracted` rather than `N/N`.
5. **Amend `AGENTS.md §5` step 4** with one sentence: *an acceptance criterion
   phrased as a repo-wide absence must be discharged by a registered
   `invariant-scan` rule, not by inspection.* This is the rule that would have
   caught C2 at the time.
6. **Amend `AGENTS.md` with the gate/criterion consistency rule**: a task's Gate
   may not be narrower than the scope of its acceptance criteria. If a criterion
   asserts a property outside the Gate, either widen the Gate or move the
   criterion to a task whose Gate contains it.

**Acceptance criteria.** `./run invariant-scan` exists as ci-local job 20 · every
seeded rule has a captured fail-before and cites the prose sentence it discharges
· a rule missing `fail_before` is refused by the scanner, demonstrated ·
`checklist-audit` reports checked and retracted separately · both `AGENTS.md`
amendments landed · ci-local 20/20 · golden 11/11.

**Done when** the project's founding doctrine applies to its own verification
apparatus and not only to its source.

---

## Step 5 · RETRACT-0110 (C4) — Record the correction without rewriting the release 🤖

**Objective.** Make v0.11's false claim visible in the permanent record, at the
cost of a retraction entry rather than a rewritten history.

**Gate.** Blocked by Steps 2-4 (a retraction that names no correcting task is an
apology, not a record). **The `v0.11.0` tag, its commit, its 54 pins, and its 14
receipt/bundle files are immutable and must not be touched.** `PROGRESS-v0.11.md`
is append-only: append, never edit.

**Steps.**

1. Add the retraction record to `config/checklist-retractions.json`: runbook
   `TASKS-v0.11-EXECUTION.md`, task `STORE-IDENTITY`, the false criterion quoted
   exactly, and `corrected_by` naming this runbook's Steps 2 and 3.
2. **Append** a dated errata entry to `PROGRESS-v0.11.md` — do not edit
   `:264-267`. State what was claimed, what was true, how it was found, and
   which task corrected it. The original entry stays as written; the record of
   its falsity sits after it.
3. **Correct `STATE.md:3` (C4).** The header must state the numbers the
   **released commit** reproduces (shell 191/191), and state the worktree delta
   separately and explicitly. `AGENTS.md §5` step 6 requires correcting any prior
   claim found false; this is that.
4. Leave v0.11's checklist boxes as written. History is not rewritten; the
   retraction record is what makes the box honest.
5. **State the release disposition of v0.11.0 explicitly**: it stays published
   with a known, now-corrected defect, and this sentence goes in `STATE.md`. Do
   not let the correction read as though v0.11.0 was fine.

**Acceptance criteria.** Retraction record present and validated by
`checklist-audit` · `checklist-audit` reports checked and retracted separately ·
`PROGRESS-v0.11.md` appended, never edited (verify by diff: only additions) ·
`STATE.md` header reports released counts with the worktree delta named ·
`v0.11.0` tag object, release commit, and all 54 pins byte-identical before and
after · golden 11/11.

**Done when** a reader of the permanent record learns the true completion status
of v0.11 without needing this conversation.

---

## Step 6 · INFRA-POLICY (C5) — Decide what is actually secret 🧑

**One operator decision: what the repository may disclose about operator
infrastructure.** Everything downstream of the decision is Codex's.

**Objective.** Replace a false prohibition with a true one that something
executes.

**Gate.** No file moves until the decision is recorded. Blocked by nothing.

**Steps.**

1. 🧑 **Decide, recording the reasoning:**
   - **Option A (recommended).** `192.168.0.192` is RFC 1918 space and
     `18080`/`18081` are loopback forwards; neither is usable without already
     being on the LAN, and both already appear in five committed files including
     `README.md` and `.env.example`, where they are *documentation*. Amend the
     prohibition to bar **credentials** — `.env`, provider keys, tokens, private
     key material, raw secret-bearing responses — and drop the host/port clause,
     recording that it was never enforced and was false as written.
   - **Option B.** Keep the host/port ban and make it true: parameterize
     `README.md`, `.env.example`, `test_llm_config.py`, and
     `tools/model_profiles.py:146-149` behind placeholders and an operator-local
     untracked config, and accept that `STATE.md` and `PROGRESS-v0.9.md` are
     append-only history that cannot be cleaned — meaning the ban can only ever
     apply *going forward*, which must be stated.
   - Option B costs real work and leaves a permanently unenforceable historical
     clause. Option A costs one honest sentence. **Choose A unless a specific
     threat model argues otherwise, and name that threat model if so.**
2. Write the decision into `TASKS-v0.12-EXECUTION.md`'s standing prohibitions,
   `AGENTS.md`, and `STATE.md §6` decision log — including the finding that the
   v0.11 clause was false when written and unexecuted for its whole life.
3. Implement **R4** in `invariant-scan`: a credential scan over tracked files
   (key-shaped strings, `.env` contents, `Authorization:` values, private-key
   headers), with a captured fail-before produced by planting a fake key in a
   scratch worktree.
4. If Option B is chosen, do the parameterization in this task and record which
   files could not be cleaned and why.

**Acceptance criteria.** Decision recorded with reasoning in all three locations ·
the v0.11 clause's falsity named explicitly · R4 registered with a captured
fail-before · a planted fake credential is refused, demonstrated · under Option
B, every remaining hit is listed with its reason · golden 11/11.

**Done when** the disclosure rule is one sentence that a check can fail.

---

## Step 7 · OPS-AUTHORITY (C6) — Make the standing authorization structural 🧑

**One operator decision: the enforcement level of the server authorization.**

**Objective.** Stop the whitelist from depending on the current contents of two
agent-editable files.

**Gate.** Blocked by nothing, but must complete before Step 8 commits the files
the authorization governs.

**Steps.**

1. 🧑 **Decide the enforcement level, recording the reasoning:**
   - **L0 — named risk.** Keep the authorization as prose and record it in
     `ARCHITECTURE.md` alongside A4 as an accepted open risk, in the same plain
     language A4 uses. Cheapest; honest; changes nothing mechanically.
   - **L1 — allowlist at construction (recommended minimum).** Every remote
     command is built by one function that asserts the command matches a
     compiled allowlist (`docker start|stop|restart|ps` over exactly the five
     names, `curl` against `/health` and `/v1/models` on 8080-8082, `nvidia-smi`,
     `ip -br address`, `git status`), raising `ProfileError` otherwise. Tests
     assert both directions: every emitted command passes, and planted commands
     (`docker rm`, `docker run`, `rm -rf`, a sixth container name) are refused.
     `TRANSITIONS` stops being free-form text and becomes structured tuples the
     allowlist can check.
   - **L2 — server-side restriction.** An `authorized_keys`
     `command="…"` forced-command wrapper on the server, so the *server* refuses
     anything outside the lifecycle set regardless of what the Mac sends. This is
     the only genuinely structural option, and it is the only one that survives a
     confused or compromised agent session.
   - **Recommendation: L1 now, L2 scheduled.** L1 is offline-testable and lands
     this cycle; L2 requires a server session and can ride the next one.
     Recording L2 as scheduled — with its trigger — prevents L1 from being
     mistaken for the finished job.
2. Hash-pin `run` and `tools/model_profiles.py` in the protected-artifact set, so
   a change to the executable surface of the authorization is a visible,
   deliberate event rather than a quiet edit.
3. Write the chosen level into `intel-platform-OPERATIONS.md §5` and `AGENTS.md`
   in identical words. **If the two texts can drift, they will**: add an
   `invariant-scan` rule (**R6**) asserting the two blocks are byte-identical,
   with a captured fail-before.
4. **State plainly what the authorization does not do.** It cannot prevent an
   agent that edits `model_profiles.py` from changing what runs, unless L2 is in
   place. That sentence goes in `OPERATIONS.md §5` regardless of which level is
   chosen — this is the ops-side analogue of `ARCHITECTURE.md` keeping A4 stated
   as open, and it must not be softened.

**Acceptance criteria.** Level decided and recorded with reasoning · under L1,
allowlist tests pass in both directions with at least four planted refusals · two
files hash-pinned · `OPERATIONS.md §5` and `AGENTS.md` byte-identical and R6
enforcing it with a captured fail-before · the "what this does not do" sentence
present · if L2 is scheduled, its trigger is named · golden 11/11.

**Done when** the authorization's guarantee no longer rests on the goodwill of
the file that implements it.

---

## Step 8 · OPS-ADMIT — Bring the operations work under the record 🤖

**Objective.** Commit the live-verified model-profile work under a runbook, with
its provenance and its measured evidence recorded like any other task.

**Gate.** Blocked by Steps 6 and 7. The worktree inventory from E0 must still
match — if anything in the operations files changed since E0, re-measure before
committing. **No live server access is required or permitted in this task:** the
2026-07-27 live matrix is prior measured evidence and is recorded as such, not
re-run.

**Steps.**

1. Commit `tools/model_profiles.py`, `shell/tests/test_model_profiles.py`,
   `intel-platform-OPERATIONS.md`, and the `run`/`AGENTS.md` modifications as
   **one implementation commit**, with the Step 6 and Step 7 decisions already
   applied to their text.
2. Record the shell test count moving 191 → 200 in `STATE.md` and
   `PROGRESS-v0.12.md`, resolving C4: the number is now true of the committed
   tree.
3. **Record the live evidence as prior measured evidence with its date and
   provenance** — the 2026-07-27 matrix, the false `intel-embed` health label and
   its cause, the `osascript`-vs-Terminal.app route finding, and the container
   IDs. Label it exactly as what it is: a single live run on real hardware, not a
   reproducible check. Per HC13, name what it cannot prove — it cannot prove the
   sequences are correct after any future edit, which is what Step 9 is for.
4. Dispose of the three C7-augment items explicitly: make `_container_rows` raise
   `ProfileError` on malformed remote output; decide whether
   `_require_containers` keeps demanding all five containers (record the
   cross-project coupling either way); document why `cmd_models` bypasses
   `ensure_venv`.
5. Add `docs/` or `OPERATIONS.md` one-liner recording where
   `model_profiles.py` lives as the single source of truth for both projects, or
   that it is duplicated and how the copies are kept in sync. **Two repos, one
   controller, no stated ownership is how drift starts.**

**Acceptance criteria.** All operations files committed in one implementation
commit · shell suite 200/200 on both interpreters, with the count now true of
`HEAD` · live evidence recorded with date, provenance, and its HC13 limits · all
three C7-augment items disposed with recorded reasons · controller ownership
stated · ci-local 20/20 · golden 11/11 · protected artifacts and 54 pins exact.

**Done when** the operations work is governed by the same contract as every other
line in the repository.

---

## Step 9 · OPS-FAILCLOSED (C7) — Test the refusals that are currently prose 🤖

**Objective.** Make `OPERATIONS.md`'s four fail-closed claims executable offline.

**Gate.** Blocked by Step 8. No network, no Docker, no SSH — every new test runs
on a `ci.yml` runner with nothing but the interpreter.

**Steps.**

1. Extract the decision logic behind each claim into a pure function taking
   observed state and returning a disposition, leaving the I/O in the caller:
   container inventory → refuse/proceed; listener observation → refuse/proceed;
   health poll result → refuse/proceed; socket state → reuse/move-aside/refuse.
2. Test each in both directions. A refusal test that only asserts the happy path
   is the same defect class as C2.
   - **missing container** — absent name refuses, and the message names it.
   - **foreign listener** — an unmanaged listener on 18080/18081/28080-28082
     refuses; a *managed* control socket on the same port is reused, not killed.
     `OPERATIONS.md` recovery step 2 explicitly forbids killing unknown
     processes; that sentence must be the test.
   - **health failure** — a non-200, a 200 with a non-`{"status":"ok"}` body, and
     a timeout each refuse. The third matters: `_remote_health` returns `False`
     on non-zero exit, so a hung server and a dead one must be distinguishable in
     the message even though both refuse.
   - **stale socket** — a stale socket file is moved aside; a live one is
     reused; an unreadable one refuses.
3. Add a test asserting the emitted transition scripts never contain
   `docker run`, `docker rm`, `docker rmi`, `docker pull`, or any path under
   `/data/models` — the existing test covers the first two for four profiles;
   widen it to the full ask-first set from `OPERATIONS.md §5`.
4. Record the new shell test count in the same task.

**Acceptance criteria.** All four claims have both-direction tests · the managed
socket is reused and never killed, asserted · hung and dead servers produce
distinguishable messages · the ask-first command set is asserted absent from
every emitted script · new count recorded · ci-local 20/20 · golden 11/11.

**Done when** `OPERATIONS.md`'s refusal claims fail a test when they stop being
true.

---

## Step 10 · RE-MEASURE — Produce the authenticated v0.12.0 receipt 🧑

**One operator decision: authorize the hosted dispatch.**

**Objective.** Produce a fresh release-grade deferred-audit receipt at the new
release commit under the v0.10.3 identity, authentication, durability, and
labeling rules — **unchanged**. This cycle weakens no guard.

**Gate.** Clean worktree at the candidate commit. `--expected-head` and
`--evidence-grade release` required. Never re-measure onto an existing evidence
path; never move a published tag.

**Steps.**

1. 🧑 Dispatch `ci.yml` from remote `main` with `audit_sha=<v0.12.0 candidate>`
   and `publish_evidence=true`. Confirm every job passes, each checkout is
   exactly the candidate, and each job emits one receipt carrying its `matrix`
   identity plus a persisted bundle.
2. Download receipts and bundles into `evidence/ci-runs/<run_id>-<attempt>/`;
   confirm seven **distinct** `(job, matrix)` identities.
3. On a clean worktree at the candidate, run the production audit with
   `--expected-head`, `--evidence-grade release`, `--require-attestations`, and
   the source-revision pin. Write `evidence/v0.12.0/deferred-audit/report.json`,
   confirm the trigger dispositions, and hash-pin it with the new receipts and
   bundles.
4. Re-run `./run audit-deferred --rederive` on the new report.
5. **Negative controls, on a throwaway branch only:** one planted failing job and
   one duplicated matrix leg. Delete the branch. Never on a release commit or tag.
6. **Confirm the new ci-local job count reaches the hosted matrix correctly.**
   `invariant-scan` is job 20 locally; verify whether it lands inside an existing
   hosted job or changes the seven-identity set. **If it would change the set,
   stop** — the identity set is a v0.10.3 guard and this cycle does not weaken
   it; fold the scan into an existing job instead.

**Acceptance criteria.** Seven authenticated receipts with seven distinct
identities accepted, zero rejected · both negative controls fire · new report is
release-grade, correctly labeled, hash-pinned, and re-derives · pin count updated
in `STATE.md` in the same task · the hosted identity set is still exactly seven ·
golden 11/11 · published tags unmoved.

**Done when** the correction rests on evidence produced under the same guards the
defect escaped.

---

## Step 11 · R-CLOSE — Close the cycle with one explicit release identity 🧑

**Objective.** Record the cycle's disposition and, if releasing, tag exactly one
commit.

**Gate.** Release only if the full definition of done holds and both Step 10
negative controls fired.

**Steps.**

1. **Decide the version number explicitly.** Default `v0.12.0`, a minor bump:
   `./run models` is new operator surface and `/ingest` failure semantics change.
   Record the reasoning, and record why the alternative (`v0.11.1` for the
   correction half alone, `v0.12.0` for the operations half) was or was not
   taken.
2. Reconcile `README.md`, `CHANGELOG.md`, `STATE.md`, `ARCHITECTURE.md`,
   `AGENTS.md`, `intel-platform-OPERATIONS.md`; run `./run version-check`,
   `cycle-check`, `checklist-audit`, `progress-check`, `invariant-scan`.
3. **State v0.11.0's disposition in the changelog**, not only in `STATE.md`: it
   remains published, and the defect it shipped is named with the task that
   corrected it.
4. **Update `ARCHITECTURE.md §6` to reflect what is now enforced** — and keep
   saying plainly what remains bypassable by a rewritten shell (A4) and, now,
   what remains bypassable by an edited controller (Step 7's L0/L1 residual).
   **Do not let this cycle's fixes be written up as closing A4.** They do not.
5. Append the **Cycle closing record**: date, disposition, release, release
   commit, annotated tag object, and per-Step implementation commits.
6. State the publication disposition as a decision with a trigger, not a default.

**Acceptance criteria.** Version choice recorded with reasoning · v0.11.0's
disposition stated in `CHANGELOG.md` · every diff path accounted for ·
`ARCHITECTURE.md` invariant table matches enforced reality · A4 and the Step 7
residual both still stated as open · checklist fully checked, retraction
reported, `checklist-audit` green · all pins match · golden 11/11.

**Done when** v0.12's disposition is a recorded, measured decision, and the record
of v0.11's is true.

---

## Cycle checklist

- [x] **E0** — entering matrix captured; dirty inventory preserved and recorded; shell-count ambiguity resolved with both numbers; C1 reproduced as a failure-capable run; C2/C5 reproduced as command output; C3/C6/C7 dispositions recorded
- [x] **INGEST-ATOMIC** — `append_new` rematerializes in-transaction; no production path splits append from assignment; non-paged failure control fails-before/passes-after on count, generation, and status; paged-durability control unchanged; `ARCHITECTURE.md` §3 item 8 corrected
- [x] **THRESHOLD-ONE** — zero production `assign_canonical_ids` call sites outside the store crate; seam disposition recorded; `DEDUP_MAX_DISTANCE` not exported; R1 registered with captured fail-before
- [x] **INVARIANT-SCAN** — `./run invariant-scan` is ci-local job 20; every rule cites its prose sentence and has a captured fail-before; a rule without `fail_before` is refused; `checklist-audit` reports checked and retracted separately; both `AGENTS.md` amendments landed
- [x] **RETRACT-0110** — retraction record validated; `PROGRESS-v0.11.md` appended not edited; `STATE.md` header reports released counts with worktree delta named; `v0.11.0` tag, commit, and 54 pins byte-identical
- [x] **INFRA-POLICY** — disclosure decision recorded in three locations with reasoning; the v0.11 clause's falsity named; R4 registered; a planted credential is refused
- [x] **OPS-AUTHORITY** — enforcement level decided and recorded; L1 allowlist tested in both directions with ≥4 planted refusals; `run` and `model_profiles.py` hash-pinned; `OPERATIONS.md §5` and `AGENTS.md` byte-identical under R6; the "what this does not do" sentence present
- [x] **OPS-ADMIT** — operations work committed in one implementation commit; 200/200 now true of HEAD; live evidence recorded with provenance and HC13 limits; three C7-augment items disposed; controller ownership stated
- [ ] **OPS-FAILCLOSED** — four fail-closed claims tested in both directions; managed socket reused never killed; hung and dead servers distinguishable; ask-first command set asserted absent from every emitted script
- [ ] **RE-MEASURE** — seven authenticated distinct-identity receipts accepted; both negative controls fired; hosted identity set still exactly seven; release-grade report pinned and re-derived
- [ ] **R-CLOSE** — version choice recorded with reasoning; v0.11.0's disposition in `CHANGELOG.md`; `ARCHITECTURE.md` matches enforced reality; A4 and the Step 7 residual both still open

---

## Standing prohibitions

- **Do not touch the `v0.11.0` release.** The tag object, its commit, its 14
  receipt/bundle files, and all 54 pins are immutable. The correction goes
  forward as a new release; it never edits a published one.
- **Do not edit `PROGRESS-v0.11.md`.** It is append-only. The errata entry is an
  append. Verify by diff that the task produced only additions.
- **Do not uncheck a box in a closed runbook.** Retraction is a record, not an
  edit.
- **Do not weaken any v0.10.3 or v0.11 guard**: the `(job, matrix)` identity set,
  the `evidence_grade` requirement, the shared classifier invariants, the
  resolving receipt paths, the pin re-hash in `validate`, the
  source-deterministic re-derivation, the loopback bind refusal, the sector
  binding, the robots `*`-merge prohibition, or the billing atomicity.
- **Do not export `DEDUP_MAX_DISTANCE`** as the fix for C2. That closes the
  instance and preserves the seam.
- **Do not broaden C1's claim.** Earlier committed pages of a paged harvest
  legitimately survive a later failure. Atomicity is per durability unit, not
  per request.
- **Do not add an `invariant-scan` rule you cannot make fire.** A rule with no
  captured fail-before is refused by the scanner, and that refusal is itself a
  required test.
- **Do not let `invariant-scan` acquire a runtime dependency.** Static analysis
  over source, config, and git only — no built binary, no protected DB, no
  network, no Docker, no SSH.
- **Do not change the hosted seven-identity set.** If job 20 would add an eighth
  hosted identity, fold it into an existing job instead.
- **Do not run a live server session in this cycle.** The 2026-07-27 matrix is
  recorded as prior measured evidence. L2 in Step 7, if chosen, is *scheduled*,
  not executed here.
- **Do not claim any task in this cycle closes A4**, and do not claim Step 7
  makes the server authorization invariant under an edited controller unless L2
  actually landed. Both remain accepted, open risks, and `ARCHITECTURE.md` must
  keep saying so.
- Do not change the public `/v1/*` JSON bodies, the SQLite schema, or the golden
  regression's 11 invariants. Golden stays 11/11 byte-identical after **every**
  task.
- Do not hand-edit `Cargo.lock` (HC12), raise the offline Rust 1.78 floor, lower
  the Python 3.11 floor, or let core call an LLM (HC3).
- Do not commit `.env`, provider keys, tokens, private key material, or raw
  secret-bearing responses. **Option A was selected in Step 6:** RFC 1918 hosts
  and loopback-forward ports may remain as documentation because they confer no
  access without the operator's network. The host/port clause in
  `TASKS-v0.11-EXECUTION.md:693-696` was false when written and had no
  executable guard during its lifetime; registered credential scan R4 replaces
  it with a rule that can fail.
- Do not batch `STATE.md` / `PROGRESS-v0.12.md` updates or combine two tasks in
  one commit, except for the operator-approved Steps 7–8 atomic implementation
  boundary recorded in `## Runbook amendments`.
- If any Step's Objective, Acceptance criteria, or "Done when" is amended after
  this file is first committed, name the amendment in a dated
  `## Runbook amendments` block in the same commit.

---

## Runbook amendments

### 2026-07-27 · Steps 7–8 atomic implementation boundary

The operator approved one narrow sequencing exception after the committed
runbook's requirements proved mutually unsatisfiable in a clean tree. Step 7
requires `tools/model_profiles.py` to be hash-pinned and executable under R6
before completion, while Step 8 exclusively admits that untracked controller,
manual, and test file. The pin validator correctly refuses a path absent from
`HEAD`; therefore an independently committed Step 7 could not satisfy its own
acceptance criteria, and an independently committed Step 8 would briefly admit
the mutable authorization surface without Step 7's guard.

Steps 7 and 8 consequently share exactly one atomic implementation commit. Both
tasks retain their complete acceptance criteria and receive separate append-only
progress entries and separate audit-record commits after that implementation
exists. No other task or status update is combined by this amendment.

---

## Provenance of this draft

C1 and C2 are the Codex post-release self-audit's two findings. Both were
**independently reproduced by reading the shipped tree** on 2026-07-27 at the
cited paths and lines, and both hold exactly as reported, including the severity
assignments. `append_new` does commit independently at `sqlite.rs:202-208`; the
handler does perform assignment in a second transaction at `main.rs:794`;
`DEDUP_MAX_DISTANCE` is module-private at `sqlite.rs:32` and the literal `16`
does appear at `main.rs:794`. The audit's positive claims also hold:
`commit_harvest_page` is genuinely atomic, `update_document` and
`delete_document` genuinely rematerialize in-transaction, and the nine
fully-verified tasks show no contrary evidence in the export.

The audit's remediation proposal — "make append + rematerialization one store
transaction, remove the second threshold literal, add the failure-capable
regression, record the corrected status" — is correct and is Steps 2, 3, and 5.

**C3-C7 are additions from independent re-verification and are not in the Codex
audit.** They were found by asking why the audit's findings survived a green
19/19, 11/11, 54/54 matrix — which is a different question from what the findings
are. C3 (the checklist proves provenance, not property) and the gate/criterion
mismatch behind C2 are the answer, and Step 4 is the only task in this file whose
absence would let the same failure recur unchanged.

Each C3-C7 row is written as a hypothesis for E0 to confirm or refute — not as a
settled fact.
