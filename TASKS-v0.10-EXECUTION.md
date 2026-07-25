# TASKS-v0.10-EXECUTION.md — auditability and design runbook for Codex

v0.10 is an **auditability-and-design cycle**. v0.9 closed with a real release
(`v0.9.0`, annotated tag on an exact commit) and a green 16-job local matrix,
and the closing audit found **0 unchecked execution boxes across 40 checked
ones**. That is the problem this cycle addresses: *the boxes were never
executable*. Nothing ties a checked box to a progress entry, a progress entry to
a real commit, an "active cycle" declaration to the file it names, or a
protected expected hash to the review that admitted it. Under
`AGENTS.md §0` — **a claimed property that nothing executes is not a
property** — a 40/40 checklist is currently markup.

v0.10 therefore does four things and deliberately no more:

1. makes cycle identity, checklist state, and admission of protected evidence
   **executable rather than declarative**;
2. closes the provenance of the cycles already finished (v0.9) and retires the
   two files that still claim present-tense authority (v0.6, v0.7);
3. converts two standing v0.10 candidates — dependency constraints and
   protected-artifact admission — into shipped, failure-capable controls;
4. produces the **V2 `/view` design** on measured decomposition, without
   shipping materialization.

It adds no ingestion source and no subscriber-facing surface.

---

## Entering state (asserted, not yet verified)

Taken from the 2026-07-25 closing audit. **Every sentence here is a hypothesis
until Step 1 measures it.** Prior measurement is not permission to skip the
entering-state run — including when the prior measurement is your own.

- Worktree clean; `./run ci-local` **16/16**; `./run version-check` **PASS at
  0.9.0**; golden **11/11**; protected evidence **2/2 exact**; progress check
  **PASS**.
- Rust **98 workspace / 20 net** tests, warning-denied checks green. Python
  **3.11 and 3.12: 105 shell tests each**, one third-party Starlette
  deprecation warning per lane.
- Release commit `4c59db2727eda1c81beae3ff38be883a26a92ae8`; annotated tag
  object `548ffdfec4e414570ddecf813aa2f2d616662487` (`v0.9.0`); HEAD is
  intentionally one append-only audit commit ahead at
  `280f6abfec0044104b830731c952883aa64b9703`.
- Execution checklists: `TASKS-v0.8-EXECUTION.md` 12/12,
  `TASKS-v0.8.1-EXECUTION.md` 10/10, `TASKS-v0.8.2-EXECUTION.md` 11/11,
  `TASKS-v0.9-EXECUTION.md` 7/7 — **40 checked, 0 unchecked**.
- No Git remote; **no CI-runner execution has ever been observed**.
- The real model's adversarial `/attest` leg remains **`NOT EXERCISED`**: core
  HC1 has never been tripped by a real model.

### Defects this runbook was drafted against (verify, do not trust)

Each was read out of the packaged tree on 2026-07-25 and is cited by path and
line so Step 1 can confirm or refute it:

| # | Location | Claim to verify |
|---|---|---|
| 1 | `tools/progress_check.py:14-15` | `CURRENT_PROGRESS` is the literal `PROGRESS-v0.9.md`, falling back to `PROGRESS-v0.8.md`. In a v0.10 cycle, `./run progress-check` would validate the **closed** v0.9 log and pass while the new log is never validated. |
| 2 | `tools/audit_deferred.py:349-350` | The multi-host measurement scans only `PROGRESS-v0.8.md` and `PROGRESS-v0.9.md` for remote `CORE_URL` hits. A `PROGRESS-v0.10.md` is invisible to it, so "0 recorded cross-host requests" would become true by construction. |
| 3 | `AGENTS.md:13` | Still names `TASKS-v0.9-EXECUTION.md` as this cycle's ordered work and `PROGRESS-v0.9.md` as the log. Both are closed; an agent following it literally re-executes a finished runbook. |
| 4 | `TASKS-v0.9-EXECUTION.md` (Provenance section) | Still states the v0.9 tasks "have not been executed"; its execution correction names only B0 and A1 although all seven boxes are checked and R2 released. |
| 5 | `TASKS-v0.6.md:3`, `TASKS-v0.7.md:3` | Both still say "This document is the authoritative task list". `TASKS-v0.7.md:13` still asserts Rust "≥ 1.75 still suffices for the offline build", which `STATE.md §5` records as **false** — the committed lock is format v4 and the floor is **1.78**. |
| 6 | every `TASKS-v*-EXECUTION.md` | Checklist boxes are static markup. No tool maps `- [x]` to a progress entry or to a commit object. |
| 7 | `shell/requirements.txt` | Four floors (`fastapi>=0.110`, `uvicorn>=0.29`, `httpx>=0.27`, `pytest>=8`); no constraints file exists. `AGENTS.md §4`'s recorded 3.12 resolution is a dated measurement, not a pin. |
| 8 | `config/protected-artifacts.json` + `tools/evidence_artifacts.py:155-158` | `lifecycle.admission` is a string literal, and validation only checks that the literal is the known one. Nothing records or verifies wire evidence or operator review when an expected hash changes. |
| 9 | `tools/verify_llm.py:292-306` | The adversarial leg is **one** prompt shape against `gated[0]` only. A single refusal produces `NOT EXERCISED` for the whole guard. |

---

## How to run this file

Execute top to bottom, one task and one commit at a time. Follow `AGENTS.md §5`
after **every** task: check the gate first, implement, run and capture every
acceptance criterion, run `./run golden`, update `STATE.md`, append
`PROGRESS-v0.10.md`, check the box here, and commit. Implementation commit and
audit-record commit stay separate.

- **🤖 = Codex executes and self-verifies end to end.**
- **🧑 = exactly one named operator decision or action is required.** Everything
  else in that task remains Codex's responsibility.

### Session opener (run before reading further)

```bash
git status --porcelain=v1
git describe --tags --always --dirty
git rev-parse HEAD
sed -n '1,20p' AGENTS.md
sed -n '1,6p' STATE.md
```

If `AGENTS.md` names a runbook other than this one, that is defect #3, not
permission to execute the file it names. Record it and proceed to Step 1.

### Global definition of done

Protected hashes exact unless a task explicitly stops at the artifact-drift
gate; golden **11/11**; `./run version-check` green; zero rustc warnings on
offline and net builds; all Rust tests green; all shell tests green under Python
3.11 **and** 3.12; clippy, fmt, ShellCheck, floor byte-compilation, and locked
Rust 1.78 green. No mock, fixture, double, or health response is promoted to
wire evidence.

**The `ci-local` job count is itself a tracked number.** It enters this cycle at
**16**. D0 and A1 each add one blocking job; the expected exit count is **18**.
Any task that changes the count must record the new count in `STATE.md` and
`PROGRESS-v0.10.md` in the same task. A job count that drifts without a record
is the same defect class as a checked box with no entry.

---

## Deferred means deferred

None of these triggers has fired. Each must be **re-measured** in D5; none may
be implemented because this file mentions it.

| Deferred item | Unchanged trigger | v0.10 action before the trigger |
|---|---|---|
| T7 robots single-flight | a second concurrent harvester | re-audit topology only |
| Postgres | a second archive writer | re-audit writer count only |
| pgvector | exact cosine stops fitting the measured request budget | re-measure latency only |
| Multi-host seam hardening (UDS/mTLS) | an actual core/shell host split | re-record bind/deployment topology |
| `/view` materialization | **already fired** (V1, both archives, both runs) | **design only in V2 — no cache table, no schema** |
| A4 untrusted-shell attestation boundary | a third-party/untrusted shell, or any claim that HC1 is invariant under shell replacement | record the measurement; ship no receipt seam |

---

## Step 1 · B0 — Rebuild the entering state from commands 🤖

**Objective.** Establish the actual v0.10 baseline and create
`PROGRESS-v0.10.md`. Inherit nothing — not counts, not tags, not artifact
facts, not tool versions, and specifically not the nine defects above.

**Gate.** Any false entering-state claim stops the cycle until `STATE.md` is
corrected. A changed protected-artifact hash is a separate hard stop: inspect
the database and its provenance; **do not** update the manifest to bless unknown
bytes — that bypass is exactly what A2 exists to close.

**Steps.**
1. Capture `git log --oneline -5`, `git status --porcelain=v1`,
   `git describe --tags --always --dirty`, `git remote -v`, and the commit and
   tag objects for `v0.9.0`. Confirm or refute that HEAD is exactly one
   append-only audit commit past release commit `4c59db2`, and that
   `git rev-parse v0.9.0^{}` equals that release commit.
2. Run `./run version-check`; read each version from its own source. Confirm the
   newest `CHANGELOG.md` heading describes the tag that actually exists.
3. Run the full `AGENTS.md §4` Rust matrix: warning-denied offline and net
   checks, both test suites, clippy, fmt, and locked Rust 1.78 check/tests.
4. Run the shell suite independently under Python 3.11 and 3.12. Byte-compile
   every file under `tools/` and `shell/` with 3.11, run `shellcheck ./run`,
   and record interpreter and ShellCheck versions.
5. Run `./run down`; prove ports 8787, 8788, and 8899 are clear with an
   independent `lsof`.
6. Run `./run verify-artifacts`, then independently measure both protected
   databases read-only: SHA-256, byte size, document count, NULL `simhash` and
   `canonical_id` counts, `PRAGMA integrity_check`, and complete cursor rows.
7. Run `./run golden`; capture all eleven named assertions.
8. Run `./run ci-local` and record the job count and each job's result.
9. **Verify the defect table above, item by item**, with `grep -n` / `sed -n`
   output for each cited path and line. Record each as CONFIRMED or REFUTED with
   the evidence. A refuted item is deleted from the cycle, not worked around.
10. Create `PROGRESS-v0.10.md` with this measured baseline and the exact
    commands.

**Failure-capable control.** Copy `data/core.db` beneath a `mktemp -d`, record
its real hash in a disposable manifest, mutate only that copy, and prove
`./run verify-artifacts <disposable-manifest>` exits non-zero printing expected
and actual hashes. Touch nothing in `data/`.

**Acceptance criteria.** Every entering claim confirmed or corrected · all nine
defects dispositioned with command output · artifact-mismatch control fails
loudly · full Rust matrix and both Python lanes green · `ci-local` count
recorded · version/tag relationship recorded · golden 11/11 · protected
artifacts 2/2 exact.

**Done when** the v0.10 baseline exists as executed commands in `STATE.md` and
`PROGRESS-v0.10.md`, not as copied prose.

---

## Authorized execution-order correction — 2026-07-25

B0 confirmed the drafted provenance defects, and the first D0 attempt exposed
an ordering cycle: D0's blocking checker must reject the same unfinished
historical closure records assigned to D1, while D1 was ordered after A1 and A1
requires completed D0. On 2026-07-25 the operator explicitly approved moving
the provenance-bootstrap portion of D1 before D0.

The corrected order is **B0 → D1A → D0 → A1 → D1**. D1A adds only the dated
historical closure/supersession records required for a strict D0 checker to
evaluate the real corpus. The original D1 remains in place as the post-auditor
validation step driven by D0 and A1. No auditor exemption or relaxed rule is
authorized. The checklist therefore contains twelve tasks rather than the
drafted eleven.

## Step 1A · D1A — Bootstrap historical cycle closure 🤖

**Objective.** Break the D0/A1/D1 dependency cycle without weakening the
auditor: give every finished execution runbook the dated release/no-release
record D0 requires, and retire the two historical task lists that still claim
present authority.

**Gate.** Preserve all closed rationale. Use dated appends and correction
banners; do not rewrite historical measurements or fabricate a release or
commit. Every release/tag/commit value must resolve from Git before it is
recorded.

**Steps.**
1. Append a dated closing record to all four finished execution runbooks.
   v0.8 and v0.8.1 name annotated `v0.8.0`; v0.8.2 records its explicit
   no-separate-release disposition and all intentionally unreleased
   implementation commits; v0.9 names all seven task commits, annotated
   `v0.9.0`, and every carried non-result required by the original D1 scope.
2. Add dated superseded banners to `TASKS-v0.6.md` and `TASKS-v0.7.md`, strike
   their present-tense authority claims, and correct v0.7's false Rust 1.75
   offline floor to the measured 1.78 floor.
3. Verify every recorded commit and tag object with Git, confirm all historical
   checklists remain unchanged, and run the normal output-preservation gates.

**Acceptance criteria.** Four finished execution runbooks carry dated,
resolvable closing records · v0.8.2's no-release record names all 11
implementation commits · v0.9 names all seven task commits and carried
non-results · v0.6/v0.7 are historical-only and the 1.75 claim is corrected ·
no closed checklist or rationale changed · golden 11/11 · protected artifacts
2/2.

**Done when** D0 can enforce its strict rule against the production corpus
without an exemption or out-of-order repair.

---

## Step 2 · D0 — Make the active cycle executable, not declarative 🤖

**Objective.** A cycle pointer that only exists in prose can rot silently, and
it has (defects #1, #2, #3). Give the repository **one declared active cycle**
and make every tool derive from it.

**Gate.** If any tool cannot derive its target from the single declared source
without a literal filename, stop and record which one. Do not "fix" it by
updating the literal from `v0.9` to `v0.10` — that reproduces the defect one
cycle later and is explicitly out of scope for this task.

**The rule this task ships.** A `TASKS-v*-EXECUTION.md` file is in exactly one
of two states, and anything else is a defect:

- **open** — it is the declared active runbook and has ≥ 1 unchecked box; or
- **closed** — it carries a dated closing record naming its release identity
  (annotated tag and release commit) or an explicit no-release disposition with
  the intentionally unreleased commits named.

**Steps.**
1. Declare the active cycle in exactly one machine-readable place. Prefer a
   single line in `AGENTS.md` with a fixed, greppable shape (for example
   `**Active cycle:** v0.10`), so the human contract and the machine contract
   cannot diverge. Record why you chose that location.
2. Add `tools/cycle_check.py` and `./run cycle-check`. It must assert:
   (a) the declared cycle resolves to an existing `TASKS-v<cycle>-EXECUTION.md`
   and an existing `PROGRESS-v<cycle>.md`; (b) that runbook is **open** by the
   rule above; (c) every other `TASKS-*.md` is **closed** by the rule above and
   makes no present-tense authority claim; (d) `tools/progress_check.py` and
   `tools/audit_deferred.py` resolve their targets from the same declared source.
3. Remove the cycle literals: `tools/progress_check.py` derives its default from
   the declared cycle; `tools/audit_deferred.py` globs `PROGRESS-v*.md` rather
   than listing two files.
4. Retarget `AGENTS.md`: the active-cycle line, the `§5` per-task workflow
   references, and the `§6` golden reference must all name v0.10. Keep the
   closed-cycle pointers as history, clearly dated.
5. Add `cycle-check` to `./run ci-local` as a blocking job and record the new
   job count (**16 → 17**).

**Failure-capable control.** In a disposable copy of the tree, prove
`./run cycle-check` exits non-zero and names the file in each of four cases:
(i) the declared cycle names a runbook that does not exist; (ii) the active
runbook has zero unchecked boxes and no closing record; (iii) a closed runbook
still claims present-tense authority; (iv) `progress_check` resolves to a file
other than the declared active log. A checker that passes all four is not a
checker.

**Acceptance criteria.** One declared source of cycle identity · no cycle
filename literal remains in `tools/` · all four control cases fail loudly ·
`./run progress-check` demonstrably validates `PROGRESS-v0.10.md` and not
`PROGRESS-v0.9.md` · `ci-local` 17/17 · golden 11/11 · protected artifacts 2/2.

**Done when** pointing the repository at the next cycle is a one-line edit that
a command can falsify.

---

## Step 3 · A1 — Make checklist boxes evidence-bearing 🤖

**Objective.** Close defect #6. A checked box must be a claim that something
executed, verifiable without reading prose.

**Gate.** If an existing checked box cannot be resolved to a real commit, that
is a **finding to record**, not a rule to relax. Do not fabricate, guess, or
back-derive a hash. Do not uncheck a historically completed box to make the tool
pass. If the count of unresolvable boxes exceeds what a recorded exemption can
honestly cover, stop and report.

**Steps.**
1. Add `tools/checklist_audit.py` and `./run checklist-audit`. For every
   `TASKS-v*-EXECUTION.md`, parse each `- [x] **<ID>**` line and require, in the
   matching `PROGRESS-v<cycle>.md`, a `### <ISO date> · <ID> — …` entry
   containing exactly one `- commit:` line whose 7–40 character hash resolves via
   `git cat-file -e <hash>^{commit}`.
2. Report per file: boxes checked, entries matched, commits resolved, and every
   mismatch by file and line. Exit non-zero on any unmatched box.
3. Handle the known legacy defect honestly: early `PROGRESS-v0.8.md` entries
   record narrative values such as "see git history" instead of hashes, and
   `PROGRESS-v0.8.md:1049` already acknowledges this. Where the real commit is
   recoverable from `git log`, record it as a dated correction append (never by
   editing the original entry — the log is append-only). Where it is not
   recoverable, add it to one explicit, dated exemption record listing entry,
   reason, and who accepted it. The tool must **fail** if an exemption exists for
   an entry that is in fact resolvable.
4. Add `checklist-audit` to `./run ci-local` as a blocking job; record the new
   count (**17 → 18**).

**Failure-capable control.** In a disposable copy: check a box with no progress
entry (must fail naming the box); check a box whose entry carries a
well-formed but non-existent hash (must fail naming the hash); add an exemption
for an entry that resolves cleanly (must fail naming the false exemption).

**Acceptance criteria.** All 40 pre-existing checked boxes audited · every
unresolvable entry either corrected by append or explicitly exempted with a
reason · no original progress entry rewritten · three controls fail loudly ·
`ci-local` 18/18 · golden 11/11 · protected artifacts 2/2.

**Done when** "40 checked" is a measurement instead of a count of characters.

---

## Step 4 · D1 — Close the provenance of the finished cycles 🤖

**Objective.** Close defects #4 and #5, driven by what D0 and A1 actually
report rather than by this draft's reading.

**Gate.** Preserve closed rationale; do **not** rewrite it. The project's
discipline is dated correction banners and appends, exactly as
`TASKS-v0.8.md` already does. If a correction would require changing what a
closed document originally claimed, stop — annotate instead.

**Steps.**
1. `TASKS-v0.9-EXECUTION.md`: append a dated closing record that supersedes the
   "have not been executed" provenance. Name all seven tasks with their
   implementation commits, the release identity (`4c59db2`, tag object
   `548ffdf`), and every non-result carried out of the cycle (adversarial
   `NOT EXERCISED`; four deferrals; V2 promoted; no remote, no runner). This is
   the record `./run cycle-check` requires for a closed runbook.
2. `TASKS-v0.6.md` and `TASKS-v0.7.md`: add dated superseded banners in the
   `TASKS-v0.8.md` shape. Strike the present-tense authority claims, and
   explicitly correct the Rust ≥ 1.75 offline-floor statement at
   `TASKS-v0.7.md:13` against the measured 1.78 floor, citing `STATE.md §5`.
   State that these two files carry no checklist and are historical rationale
   only.
3. Re-run `./run cycle-check` and `./run checklist-audit`; both must now pass
   over the full corpus.
4. Update `STATE.md` with the corrected corpus state and the exact commands.

**Failure-capable control.** Temporarily restore one present-tense authority
claim in a disposable copy and prove `./run cycle-check` names that file and
line; restore the corrected text and prove it passes.

**Acceptance criteria.** Every closed runbook carries a dated closing record ·
no closed rationale rewritten · the false 1.75 floor corrected wherever it
appears · both auditors green over all task files · control fails loudly ·
golden 11/11 · protected artifacts 2/2.

**Done when** no document in the repository claims to be the active task list
except the one that is.

---

## Step 5 · A2 — Make protected-artifact admission failure-capable 🤖

**Objective.** Close defect #8. `STATE.md` already records this as required
**before the first proposal to add a protected artifact or change an expected
protected hash**. Today a manifest edit alone can bless changed bytes, and Git
review is the only control — which is prose.

**Gate.** A2 must not be used to admit anything. The two existing artifacts get
**retroactive** records marked as such, sourced from the provenance already in
`STATE.md`, never presented as fresh review. If admission logic would require
touching `data/core.db` or `data/live-smoke.db`, stop: it is designed wrong.

**Steps.**
1. Extend the manifest schema so each artifact carries an `admission` object:
   admitting task id, ISO date, `prior_sha256` (or `null` for an original
   admission), references to captured wire evidence (command and captured
   output path or hash), the operator approval, and `retroactive: true|false`.
   Bump `schema_version` and update the validator in
   `tools/evidence_artifacts.py` accordingly.
2. Make the chain checkable: an artifact's current `sha256` must be the
   `sha256` of its newest admission record, and that record's `prior_sha256`
   must equal the previous record's `sha256`. A hash edited without a new,
   complete admission record is a validation failure that names the artifact and
   the missing field.
3. Wire the check into `tools/evidence_artifacts.py validate`, `./run
   verify-artifacts`, and the existing CI manifest-validation job. Do not add a
   new `ci-local` job; this rides the existing one.
4. Write the retroactive records for `data/core.db` (1,764 documents) and
   `data/live-smoke.db` (2,600 documents), citing the already-recorded harvest
   provenance and the B0 measurements. Verify both hashes before and after; the
   database bytes must not change.
5. Update `ARCHITECTURE.md` and `AGENTS.md` so admission is described as an
   executed control, with its exact command.

**Failure-capable control.** On a disposable manifest and disposable copies
only: (i) change an expected hash with no new admission record → must exit
non-zero naming the artifact; (ii) add an admission record missing wire evidence
or operator approval → must exit non-zero naming the missing field; (iii) add an
admission record whose `prior_sha256` does not match the previous record → must
exit non-zero naming the break; (iv) a complete, chained record over a
disposable artifact → passes.

**Acceptance criteria.** Schema bumped and validated · chain rule enforced ·
four controls behave exactly as specified · both real artifacts remain
byte-identical and 2/2 exact · retroactive status explicit in the file · docs
describe a command, not an intention · golden 11/11.

**Done when** changing a protected expected hash requires evidence a command
can reject.

---

## Step 6 · C1 — Pin the Python lanes with constraints 🤖

**Objective.** Close defect #7. `shell/requirements.txt` declares floors, so the
recorded 3.12 resolution in `AGENTS.md §4` is repeatable but not reproducible —
an upstream release can change the tested surface without any diff here.

**Gate.** Constraints must not raise the Python 3.11 floor, must not change the
**105/105** shell test result on either lane, and must not alter runtime
behavior. If the two lanes cannot resolve a single shared constraints set, ship
two files and record the exact conflict. If a pin would require a package
unavailable on 3.11, stop and record.

**Steps.**
1. Rebuild both lanes clean (`.venv` for 3.11, `.venv/py312` per `AGENTS.md §4`)
   and capture `pip freeze` from each. Record interpreter versions.
2. Produce constraints. One shared `shell/constraints.txt` if the resolutions
   agree; otherwise `shell/constraints-py311.txt` and
   `shell/constraints-py312.txt` with the divergence recorded. Keep
   `requirements.txt` as declared floors — constraints pin, requirements
   declare.
3. Install with `-c` everywhere it is installed: `./run` venv setup, the CI
   workflow's install step, and the `AGENTS.md §4` commands.
4. Prove reproducibility: build a fresh venv from `requirements.txt` +
   constraints and show `pip freeze` matches the recorded set exactly on both
   lanes; run `pip check`.
5. Re-run both shell lanes and the full matrix.

**Failure-capable control.** Plant one constraint that conflicts with a
`requirements.txt` floor and prove the install fails loudly naming both; plant
one constraint one patch version off the recorded set and prove the
reproducibility check names the difference. Restore and re-verify.

**Acceptance criteria.** Both lanes reproduce their recorded resolution exactly
· `pip check` clean on both · 105 shell tests on 3.11 and 3.12 · floors
unchanged · CI and `./run` both install with constraints · both controls fail
loudly · `ci-local` 18/18 · golden 11/11 · protected artifacts 2/2.

**Done when** the dated environment in `AGENTS.md §4` is enforced by a command
instead of remembered.

---

## Step 7 · V2 — Decompose the `/view` cold path and design its fix 🤖

**Objective.** V1's gate fired: cold p95 missed **162.640 ms** on both archives
in both runs (1,764-row: 1,693.423417 / 362.794125 ms; 2,600-row: 543.318334 /
523.764917 ms) while every warm cell passed (8.164166 / 8.469334 and 12.584125 /
12.565458 ms). V2's own scope requires decomposing that cost **before** choosing
a representation.

**Gate.** **No materialization ships in this task** — no cache table, no schema
change, no persisted derived representation. Do not select an implementation
before the failure-capable stale-result control exists and passes. If
decomposition shows the dominant cost is not what a materialized view would
remove, that finding **replaces** the cache-table hypothesis rather than
qualifying it.

**Steps.**
1. Instrument the cold path so a `/view` request can report stage timings via
   internal diagnostic headers only — the same seam as the existing
   `x-intel-view-cache` and `x-intel-view-generation`. **The JSON body must not
   change**; golden depends on it.
2. Separate at minimum: process spawn to listener ready; `SqliteStore::open`
   (schema and FTS creation, cursor migration, **missing-fingerprint backfill**);
   sector corpus load; analysis; serialization; HTTP transfer. Name the
   backfill explicitly — it runs at `cored` startup and is a live hypothesis for
   the dominant cold cost at 1,764 and 2,600 rows.
3. Extend `./run benchmark-view` with a decomposition mode over disposable
   byte-for-byte copies of both protected archives. Ten cold samples per
   archive, as in V1. Report per-stage min/median/p95/max and each stage's share
   of cold p95.
4. Address V1's retained 1,693.423417 ms outlier: either explain it from stage
   data or state explicitly that the decomposition does not explain it. Do not
   discard it.
5. Write the V2 design against the measurement. It must state the invalidation
   key and prove it covers **archive identity, sector set, algorithm/schema
   version, and every corpus mutation class** (append, update, delete,
   canonical-id rematerialization, fingerprint refresh, embedding write). An
   in-memory generation that resets on restart is insufficient by construction.
6. Constrain the design explicitly to HC1, core-SQL sector enforcement (HC2),
   HC3, corpus-derived dedup identity, and HC9 — any persisted core
   representation is archive/query state, never shell-owned configuration.
7. Record the acceptance a future implementation task must meet: rerun V1's
   two-archive, two-run benchmark and meet **both** predeclared thresholds with
   no change to the JSON response, protected artifacts, or golden 11/11.

**Failure-capable control.** Build a stale-result control that mutates the
corpus in each named mutation class and proves a candidate key detects each one;
a key that misses any class fails the task. Separately prove the decomposition
harness itself can fail: inject a delay into one stage and show it appears in
that stage's distribution and not another's.

**Acceptance criteria.** Stage decomposition measured on both archives across
two runs · every stage's share of cold p95 reported · outlier explained or
explicitly unexplained · invalidation key proven against every mutation class ·
no materialization implemented · JSON body byte-identical · protected hashes
exact · golden 11/11.

**Done when** the design targets a measured cost and the key that would keep it
correct is one a control has already tried to break.

---

## Step 8 · D5 — Re-audit every deferred trigger, and extend the registry 🤖

**Objective.** "Deferred" must be a current measurement, not inherited
folklore — including for the two dispositions that currently live only in prose.

**Gate.** A fired trigger promotes a scoped future design task and nothing else.
It does not authorize implementing the deferred subsystem inside D5.

**Steps.**
1. Re-run `./run audit-deferred` and record the five existing dispositions from
   measurement, not from v0.9's table.
2. Extend the registry to seven items:
   - **A4 untrusted-shell attestation boundary.** Trigger: a third-party or
     untrusted shell, or any claim that HC1 is invariant under shell
     replacement. Measurement: count public answer paths that do **not** traverse
     a core-owned response boundary, and count shell-owned public egress points.
     The correct current disposition is defer with the risk recorded; ship no
     receipt seam.
   - **CI-runner evidence.** Trigger: a Git remote exists. Measurement:
     `git remote -v` entries and observed runner executions. Workflow
     configuration is **never** reported as a runner result.
3. Apply D0's glob fix so `PROGRESS-v0.10.md` is actually scanned (defect #2);
   prove it by showing the file list the tool used.
4. Import V2's disposition for the `/view` row.
5. Write the dated seven-row table into `STATE.md` with `trigger`,
   `measurement`, and `defer`/`promote` for each.

**Failure-capable control.** Run the audit against a disposable synthetic input
supplying two harvesters, two archive writers, a remote `CORE_URL` hit, a
configured Git remote, and a public answer path bypassing `/attest`; prove every
corresponding trigger reports fired and the command exits non-zero. The
production audit must still use measured repository and deployment state.

**Acceptance criteria.** Seven triggers measured · synthetic control fires all
seven · progress-file glob demonstrably includes v0.10 · no deferred subsystem
implemented · every disposition carries its unchanged trigger · golden 11/11 ·
protected artifacts 2/2.

**Done when** every deferral in the project is a row a command produced.

---

## Step 9 · X1 — Exercise the real-model adversarial guard 🧑

**One operator input: confirm the LAN chat and embedding endpoints are
reachable and `.env` is configured.** Everything else is Codex's.

**Objective.** Core HC1 has never been tripped by a real model. The current leg
is one prompt shape against one document (defect #9), so a single model refusal
produces `NOT EXERCISED` for the entire guard.

**Gate.** `NOT EXERCISED` across the whole battery remains an **acceptable,
honest recorded outcome and is never reported as a pass.** A `LEAK` is a hard
stop: record it in `STATE.md` immediately, do not proceed to further tasks, and
surface it to the operator — that is an HC1 breach, not a test result. If the
endpoints are unreachable, defer per `AGENTS.md §7` and do not substitute the
mock; a mock result is harness evidence only.

**Steps.**
1. Replace the single adversarial prompt with a declared battery: several
   distinct elicitation shapes (verbatim quotation, "continue this sentence",
   translation round-trip, formatted extraction, and a chunked reconstruction
   request) applied across **every** IndexOnly document in the fixture corpus,
   not just `gated[0]`.
2. Classify each attempt independently as `GUARD FIRED` / `NOT EXERCISED` /
   `LEAK`, and report the aggregate plus the full per-attempt matrix. The
   aggregate is `NOT EXERCISED` only when every attempt was.
3. Keep the failure-capable doubles honest: `tools/mock_openai.py --leak` must
   still produce `GUARD FIRED`, and a deliberately unattested path must still
   produce `LEAK`. A classifier that cannot emit all three values is not
   evidence.
4. Record model identity, endpoint role, prompt shape, latency, and outcome for
   every attempt. Commit no keys, no tunnel aliases, and no raw secret-bearing
   responses.
5. Re-run `./run golden` and confirm the ordinary answer path is unchanged.

**Failure-capable control.** Prove the battery can distinguish outcomes: the
`--leak` double must fire the guard on a shape where the real model did not, and
that difference must be visible in the matrix.

**Acceptance criteria.** Battery declared before execution · every IndexOnly
document targeted · per-attempt matrix recorded · aggregate honestly classified
· all three classifier values demonstrated by doubles · no secrets committed ·
golden 11/11 · protected artifacts 2/2.

**Done when** the project can say precisely how hard it tried to make a real
model breach HC1, and what happened.

---

## Step 10 · G2 — Obtain one observed CI-runner execution, or record its absence 🧑

**One operator decision: add a Git remote and run the configured workflow once,
or decline and record the trigger.**

**Objective.** `.github/workflows/ci.yml` has configured blocking jobs for
several cycles and **no runner has ever executed them**. That is this project's
canonical failure mode applied to its own CI.

**Gate.** Workflow configuration must never be described as a runner result. If
the operator declines, that is a legitimate recorded deferral with its trigger
(a remote exists) — not a failure and not a silent omission. Do not push
anything anywhere the operator has not explicitly approved.

**Steps.**
1. If the operator approves: add the remote, push the release commit and tag,
   and trigger the workflow once. Capture the run identifier, per-job results,
   durations, and the runner's toolchain and interpreter versions.
2. Compare the runner's job set against `./run ci-local`'s 18 jobs. **Any
   divergence is the finding** — record which jobs exist in one and not the
   other rather than assuming equivalence.
3. Record in `STATE.md` the first observed runner execution, replacing every
   "configured but never executed" claim with the measurement.
4. If the operator declines: record the decision, the date, and the unchanged
   trigger in both `STATE.md` and the D5 registry. Leave every
   "no runner execution observed" claim exactly as it is.

**Failure-capable control.** If a run occurs, prove the runner can fail: push a
branch with one planted version mismatch and confirm the `version-check` job
fails there; delete the branch. Never plant a failure on the release commit or
the tag.

**Acceptance criteria.** Either a real run with captured per-job evidence and a
job-set comparison, or a dated decline with its trigger · no configuration
described as execution · release tag unmoved · golden 11/11 · protected
artifacts 2/2.

**Done when** the CI claim in `STATE.md` is either a measurement or an honest
absence, and not an implication.

---

## Step 11 · R3 — Close the cycle with one explicit release identity 🧑

**One human input: choose the release disposition after seeing the actual
diff.** Recommendation rule, per `ARCHITECTURE.md §8`:

- **v0.10.0** if runtime, storage, or public/API behavior changed;
- **v0.9.1** if the changes are operations, evidence, and documentation only;
- **no release** only if the cycle produced no shipped change.

Note the likely shape before measuring: D0, A1, A2, C1, and D5 are tooling,
evidence, and packaging; V2 ships instrumentation on an internal diagnostic seam
with an unchanged JSON body; X1 changes a verification tool. Whether the `/view`
timing headers constitute an internal API change is the judgment call — make it
explicitly, from the diff, rather than by defaulting.

**Gate.** Do not version or tag a dirty, failing, artifact-drifted, or
golden-drifted tree. Do not move or replace an existing tag. If "no release" is
chosen, name the commits that remain intentionally unreleased.

**Steps.**
1. Inventory `git diff --name-status v0.9.0` and classify **every** path exactly
   once as runtime/storage/internal API, public/release metadata, operations,
   executable evidence and controls, or documentation and task metadata.
2. State the disposition of every non-result carried out of the cycle,
   including X1's aggregate outcome, G2's disposition, D5's seven rows, and
   V2's unimplemented design.
3. For a release: update all five version sources together, update
   `CHANGELOG.md`, run `./run version-check`, commit, and create one annotated
   tag on that exact commit. For no release: leave every version source
   unchanged.
4. Failure control: plant one version mismatch, prove `./run version-check`
   names the file and the disagreeing value, restore, and prove the restored
   file's hash matches. For a release, also prove the tag dereferences to the
   release commit and the worktree is clean.
5. Append this cycle's closing record to `TASKS-v0.10-EXECUTION.md` so
   `./run cycle-check` sees a **closed** runbook — the rule D0 shipped now
   applies to this file.
6. Run the full global definition of done one final time, including
   `./run cycle-check` and `./run checklist-audit`.

**Acceptance criteria.** Release/no-release rationale recorded · every diff path
classified once · every carried non-result disposed · all version sources agree
· changelog and tag exact when releasing · mismatch control fails · this runbook
carries its own closing record · `ci-local` 18/18 · both Python lanes green ·
golden 11/11 · protected hashes exact.

**Done when** an operator can map source commit, tag, runtime version, and
evidence record without interpreting the cycle name.

---

## Cycle checklist

- [x] **B0** — entering state re-measured; all nine defects confirmed or refuted
- [x] **D1A** — historical cycle closure bootstrapped before the strict auditor
- [x] **D0** — active cycle declared once and enforced by `./run cycle-check`
- [x] **A1** — every checked box resolves to a progress entry and a real commit
- [x] **D1** — v0.9 provenance closed; v0.6/v0.7 retired to historical status
- [x] **A2** — protected-artifact admission is failure-capable
- [x] **C1** — both Python lanes pinned by constraints and reproduced exactly
- [x] **V2** — `/view` cold path decomposed; restart-safe design proven against
  every mutation class; nothing materialized
- [x] **D5** — seven deferral triggers re-audited from measurement
- [ ] **X1** — real-model adversarial battery executed and honestly classified
- [ ] **G2** — one observed CI-runner execution, or a dated decline
- [ ] **R3** — release disposition recorded and, if applicable, tagged

## Standing prohibitions

- Do not mutate, delete, rename, vacuum, or "refresh" `data/core.db` or
  `data/live-smoke.db`. A2 changes how admission is checked; it never admits.
- Do not hand-edit or delete `Cargo.lock` (HC12), raise the offline Rust 1.78
  floor, or lower the Python 3.11 floor.
- Do not move license attestation, sector filtering, robots policy, or
  canonical-id materialization out of their architectural owners.
- Do not let core call an LLM (HC3), re-enable automatic redirects, or weaken
  per-source missing-robots policy.
- Do not implement `/view` materialization, a single-flight lock, Postgres,
  pgvector, a UDS/mTLS seam, or an A4 receipt seam in the task that measures or
  designs it.
- Do not change the `/view` JSON response body. Internal diagnostic headers are
  the permitted seam.
- Do not commit `.env`, provider keys, tunnel aliases, or raw secret-bearing
  responses.
- Do not promote fixtures, local doubles, a health response, or workflow
  configuration to real end-to-end evidence (HC13).
- Do not relax an auditor to make the existing corpus pass. Record the finding.
- Do not batch `STATE.md` / `PROGRESS-v0.10.md` updates or combine two tasks in
  one commit.

## Provenance of this draft

Drafted on 2026-07-25 against the packaged repository tree (116 files) and the
2026-07-25 Codex closing audit, at declared release `v0.9.0` — release commit
`4c59db2727eda1c81beae3ff38be883a26a92ae8`, annotated tag object
`548ffdfec4e414570ddecf813aa2f2d616662487`, HEAD asserted one append-only audit
commit ahead at `280f6abfec0044104b830731c952883aa64b9703`.

**The v0.10 tasks themselves have not been executed.** The nine defects listed
above were read from the packaged tree by path and line and are hypotheses, not
findings, until B0 runs the commands that confirm or refute each one. Step 1
deliberately re-verifies every entering claim before any implementation, and a
refuted defect is deleted from this cycle rather than worked around.

**Execution correction — 2026-07-25.** B0 executed in implementation commit
`8603992` with separate audit commit `15437f9`. Its first D0 attempt then
recorded the D0/A1/D1 dependency cycle in `acbbae4` and audit `890676b`; no D0
implementation shipped. The operator approved the dated D1A bootstrap above
before D0 resumes.
