# TASKS-v0.24-EXECUTION.md — the population, not the number

## Runbook amendments

Step 5 — Extend the non-establishment acceptance to the live RSS wire path — 2026-07-30

Step 6 — Acceptance criteria corrected to a same-commit population-rule relation — 2026-07-29

- **2026-07-30 — operator-directed Step 5 acceptance amendment.** Step 5's
  non-establishment clause and acceptance criterion now state that the review
  establishes nothing about the live RSS wire path: live fetching, feed
  parsing, and cursor durability against a real server remain untested until
  admission. The original clause named only the multi-origin robots cache and
  per-host limiter. No objective, gate, or done condition changed.
- **2026-07-29 — activation validation correction.** The activation commit
  exposed four defects and they are corrected forward here. The declared scope
  now uses the checker's required Markdown-table schema; its Python-source
  forbid uses the v0.23-established lower-case-module glob so the only
  release-authority overlap is `shell/intel_shell/app.py`; the unchanged
  manifest re-measurement is assigned to Step 1; and Step 6's acceptance
  criterion now states same-commit invariant-count equality and execution of
  the population-equivalence rule rather than citing Step 3's measured
  increase. The last change amends one acceptance criterion; no objective,
  gate, or done condition changed.

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

| Scope class | Path or value |
|---|---|
| `scope_version` | `1` |
| `disposition_intent` | `release` |
| `allow` | `shell/tests/**` |
| `allow` | `shell/pytest.ini` |
| `allow` | `tools/test_population.py` |
| `allow` | `tools/cycle_check.py` |
| `allow` | `tools/invariant_scan.py` |
| `allow` | `config/invariant-rules.json` |
| `allow` | `config/protected-artifacts.json` |
| `allow` | `.github/workflows/ci.yml` |
| `allow` | `run` |
| `allow` | `observations/**` |
| `allow` | `AGENTS.md` |
| `allow` | `ARCHITECTURE.md` |
| `release_authority` | `Cargo.toml` |
| `release_authority` | `Cargo.lock` |
| `release_authority` | `crates/*/Cargo.toml` |
| `release_authority` | `apps/*/Cargo.toml` |
| `release_authority` | `shell/intel_shell/__init__.py` |
| `release_authority` | `shell/intel_shell/app.py` |
| `release_authority` | `CHANGELOG.md` |
| `release_authority` | `README.md` |
| `forbid` | `crates/**/*.rs` |
| `forbid` | `apps/**/*.rs` |
| `forbid` | `shell/intel_shell/[a-z]*.py` |
| `forbid` | `config/core.json` |
| `forbid` | `config/subscriptions*.json` |

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
| Second configured publisher | a completed review with an admissible recommendation for `/Archives/edgar/usgaap.rss.xml`, preserving the monitored-contact crawler identity and a total automated rate at or below the SEC's then-current published ceiling, then a separate operator admission decision | review completed 2026-07-30 with that conditional recommendation; no admission decision made | **Step 5 completed the review only; admission remains a v0.25 operator decision** |
| `v0.8.0` / `v0.10.2` publication | operator-authorized push of both exact annotated objects | not authorized | none — **no historical ref touched** |
| `--skip-local-tag-verification` removal | both historical tags published plus a passing hosted full-history `cycle-check` without the flag | tags unpublished | none — **the flag stays** |
| Manifest retention/indexing | 1 MiB manifest, or two consecutive `verify-artifacts` runs ≥1.00 s | re-measure at E0 | **Step 1 — re-measure only** |
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

## Execution records

### 2026-07-29 · E0

- **Entering matrix — PASS.** Repository-local environments were rebuilt from
  empty trees. Python **3.11.4** and **3.12.13** each resolved the exact **21**
  constrained packages and collected **275**, passed **275**, and skipped
  **0** shell tests; the skip set was empty in both local environments. The
  first sandboxed `./run ci-local` reached a denied loopback bind and was a
  non-result. The identical permitted invocation passed all **20** jobs:
  **133** workspace tests, **55** net tests (**29** ingest + **26** cored),
  warning-denied current and locked Rust 1.78 lanes, clean
  clippy/fmt/ShellCheck, `invariant-scan` **12/12 rules / 38 controls**, all
  **236** pins, protected databases **2/2**, and embedded golden **11/11**.
  Standalone golden passed **11/11**. Standalone `cycle-check`,
  `checklist-audit` (**184 checked / 3 retracted / 184 matched / 0
  exemptions**), `progress-check`, `version-check`, `invariant-scan`, manifest
  validation, and `export-check` passed. The export contains **90** derived
  sources, **7** required paths, and **155** exported paths; its first
  sandboxed `npx` DNS failure was a network non-result.
- **G1 — CONFIRMED.** `rg` found exactly **1**
  `@pytest.mark.skipif` and **0** `pytest.skip(` calls under `shell/tests/**`.
  The sole decorator guards
  `test_on_site_production_measurements_match_committed_receipt`; its reason is
  `on-site production audit requires protected corpora and built cored`.
  Repository enumeration found **0** `pytest.ini`, `pyproject.toml`,
  `setup.cfg`, `tox.ini`, or `conftest.py` files. `ci_pytest()` and the hosted
  shell job both execute `pytest shell/tests -q`; no JUnit, JSON, report-log, or
  other machine-readable output is requested or consumed.
- **G2 — CONFIRMED.** v0.19's RE-MEASURE acceptance says that where a hosted
  count differs by a declared on-site-only skip, the record must state the
  skip. The corresponding v0.21, v0.22, and v0.23 acceptance criteria instead
  say every count must be read from the log and equal to local, with no
  environment clause. v0.22 resolved that impossible shell condition by
  recording **266 collected / 265 passed / 1 declared on-site skip** per hosted
  lane against **266 collected / 266 passed / 0 skipped** locally. v0.23
  resolved the same condition in the opposite direction by claiming **275
  collected / 275 passed / 0 skipped** for hosted and local even though the
  hosted log says **275 collected / 274 passed / 1 skipped**. The divergent
  resolutions, not either choice, confirm the authored defect.
- **G3 — CONFIRMED and bounded.** `git log -S` places the conditional test's
  introduction at commit `edd77a4835057fb0a0836b39600cbe54a88b5092`,
  v0.10.1 PIN. That cycle's earlier G-RUN `30187058897` predates the test and
  reports **120 collected / 120 passed / 0 skipped** in each hosted lane.
  v0.10.2 PUBLISH run `30194678764`, which is outside the requested
  RE-MEASURE/POST-PUSH record set, is the first hosted run to contain it and
  reports **138 collected / 137 passed / 1 skipped**. Every requested retained
  log was available; there is **no retention gap**:

  | record | hosted run | each hosted Python lane: collected / passed / skipped | comparison with the record |
  |---|---:|---:|---|
  | v0.10.3 RE-MEASURE | `30202019640` | 187 / 186 / 1 on-site† | no hosted shell-number claim |
  | v0.11 RE-MEASURE | `30236305375` | 191 / 190 / 1 on-site† | no hosted shell-number claim |
  | v0.12 RE-MEASURE | `30253646597` | 205 / 204 / 1 on-site† | no hosted shell-number claim |
  | v0.13 failed RE-MEASURE | `30274895522` | 216 / 215 / 1 on-site† | stopped on net; no shell-number pass claim |
  | v0.13 RE-MEASURE retry | `30277584129` | 216 / 215 / 1 on-site† | no hosted shell-number claim |
  | v0.14 RE-MEASURE | `30324186389` | 225 / 224 / 1 on-site† | matches |
  | v0.15 RE-MEASURE | `30333331839` | 237 / 236 / 1 on-site† | matches |
  | v0.16 RE-MEASURE | `30347262430` | 243 / 242 / 1 on-site† | matches |
  | v0.17 RE-MEASURE | `30357365420` | 244 / 243 / 1 on-site† | matches |
  | v0.18 RE-MEASURE | `30369139464` | 245 / 244 / 1 on-site† | matches |
  | v0.19 RE-MEASURE | `30414648482` | 248 / 247 / 1 on-site† | matches |
  | v0.20 RE-MEASURE | `30423736121` | 255 / 254 / 1 on-site† | matches |
  | v0.21 RE-MEASURE | `30432249637` | 258 / 257 / 1 on-site† | matches |
  | v0.22 RE-MEASURE | `30443692105` | 266 / 265 / 1 on-site† | matches |
  | v0.22 POST-PUSH | `30446796322` | 266 / 265 / 1 on-site† | no hosted shell-number claim |
  | v0.23 RE-MEASURE | `30459746825` | 275 / 274 / 1 on-site† | **false 275-passed/no-skip claim** |
  | v0.23 POST-PUSH | `30462710258` | 275 / 274 / 1 on-site† | matches and supersedes the prior claim |

  † The sole on-site member is
  `test_on_site_production_measurements_match_committed_receipt`, skipped for
  the declared protected-corpora-and-built-`cored` reason above. The exact
  affected set is therefore **one record**:
  `PROGRESS-v0.23.md`'s RE-MEASURE entry for run `30459746825` (and the same
  false number copied into the v0.23 closed execution record). No other
  RE-MEASURE or POST-PUSH progress claim in the measured range omitted a hosted
  skip it purported to count.
- **G4 — answered only after stating the criterion.** The existing registry
  uses a retraction for a resolved checked task whose accepted
  product/invariant or task-acceptance property was later proved false and
  whose retraction and correction were explicitly accepted by the operator.
  Its three entries each name the checked task, falsified acceptance property,
  operator acceptance, and correcting task. An incorrect measurement inside
  an append-only progress entry instead has an established instrument:
  a dated superseding entry, demonstrated by v0.23 POST-PUSH. Applying that
  existing distinction, this measurement correction does **not** itself meet
  the checklist-retraction criterion and the registry remains at **three**;
  Step 4 preserves the named operator decision on that application.
- **G5 — CONFIRMED after a measured activation correction.** The first
  activation attempt did not pass and did not exercise the static rule because
  its YAML construction was outside the parser's Markdown schema; that result
  remains recorded as NOT MEASURED. Correction commit `6c5ca4c` supplied the
  accepted table, after which `cycle-check` passed the live `release` intent
  with all **17** release-authority paths covered and exactly the declared
  `shell/intel_shell/app.py` authority/forbid overlap. The focused
  release-authority rejection construction and current-scope test both passed
  (**2 tests**): the former detects missing authority coverage and the latter
  verifies the current 17-path population. The static sub-rule therefore
  examined and accepted this corrected live construction.
- **G6 — CONFIRMED and named.** Both rebuilt local lanes report exactly one
  `starlette.testclient.StarletteDeprecationWarning`: using `httpx` with
  `starlette.testclient` is deprecated and `httpx2` is recommended. It is the
  previously accepted warning, not a new warning. Neither trigger fired:
  it remains a warning rather than an error/failure, and
  `shell/constraints.txt` plus `shell/requirements.txt` are byte-unchanged from
  `v0.15.7`.
- **Manifest retention — unchanged.** The manifest is freshly measured at
  **136,625 bytes**, below **1 MiB**. Two consecutive complete
  `verify-artifacts` executions took **0.10 s** and **0.09 s** real, both below
  **1.00 s**, and each verified all **236** pins and protected databases
  **2/2**. Neither retention/indexing trigger fired.
- **Published identity and repository immutability — PASS.** Annotated
  `v0.15.7` object
  `b579c2c18e4eeb549617ea20a9175b0c26dc621d` peels locally and remotely to
  closing commit `e7715fb97b86b91a2a58bc7b73bf99308c2aae9b`, whose first parent
  is release parent `8bb6a71446b043b10ce16077499fdc07abb91b98`.
  Remote `main` remains that closing commit. The working repository's
  pre-implementation refs were unchanged; no auxiliary ref was created, moved,
  or deleted. `STATE.md`, `run`, and `.github/workflows/ci.yml` remain entering
  blobs `344d92a123cee58e81a6f6d7f159b8eb44748204`,
  `daeace0bf5c652fd79ee08a6aff9d11e8904371e`, and
  `48ea726b798f1049e0b29cce1f0c64588861c2dd`.
- **Golden-E2E delta: 0.** Mandatory standalone execution passed **11/11**.

### 2026-07-29 · POPULATION-EXPLICIT

- **Gate — PASS.** E0 confirmed the sole existing conditional test and the
  absence of pytest population configuration. Changes are confined to the
  declared pytest/test, `run` authorization-pin, manifest, and status paths;
  `.github/workflows/ci.yml` remains byte-unchanged.
- **Marker and enumeration — PASS.** The registered `on_site` marker sits
  immediately alongside the existing, unchanged `skipif`.
  `pytest shell/tests --collect-only -m on_site -q` enumerated exactly
  `tests/test_deferred_audit.py::test_on_site_production_measurements_match_committed_receipt`.
- **Machine summary and population preservation — PASS.** Both full-suite
  invocations retain the exact `pytest shell/tests -q` command and obtain the
  same option from `shell/pytest.ini`. The stable JSON record contains
  collected, passed, failed, the enumerated `on_site` set, and every skip's
  node id, markers, and reason. Local Python 3.11.4 and 3.12.13 each collected
  **275**, passed **275**, failed **0**, and skipped **0**. A disposable clean
  checkout under each interpreter collected **275**, passed **274**, failed
  **0**, and skipped **1**: the enumerated node, marked `on_site` and `skipif`,
  for `on-site production audit requires protected corpora and built cored`.
  These are the same populations and results measured at E0.
- **Planted command-shape failure — PASS.** A construction that added an
  explicit pytest option to `run` and the workflow was rejected by the
  authorization pin and R10's hosted-command classifier. The accepted
  configuration preserves the command shape. `run` changes by one explanatory
  comment only; its pin moves from
  `0fc7f0be0ea2d8c68ff63be55dd0b73cc1385ce966b8307506a5387543f18779`
  (**43,044 bytes**) to
  `44314ddfc182de68d4aaa444f2c6bd074fe08858d8d46f98aafa461dd6672397`
  (**43,125 bytes**). Its commands, dispatch, model-profile functions, and
  authorization boundary are unchanged.
- **Acceptance — PASS.** Full `./run ci-local` passed all **20** jobs with
  workspace **133**, net **55** (**29 + 26**), both warning-denied Rust lanes,
  clean clippy/fmt/ShellCheck, `invariant-scan` **12 rules / 38 controls**, all
  **236** pins, protected databases **2**, and embedded golden **11 checks**.
  Standalone golden passed all **11** checks; delta **0**. No test selection,
  runtime source, dependency, schema, protected database, configured source, or
  public surface changed.

### 2026-07-29 · POPULATION-COMPARE

- **Gate — PASS.** POPULATION-EXPLICIT is committed and audited. Changes stay
  within the comparator, invariant tooling/registry/tests, `AGENTS.md`, and
  status paths declared for this task; no runtime source, crate, dependency,
  schema, protected database, configured source, public surface, or ref
  changed.
- **Comparator — PASS.** The tool accepts a JSON summary or one summary
  embedded in a log, validates exact schema and result accounting, requires
  equal collected populations and zero failures, and derives equivalence only
  when local passed equals hosted passed plus hosted `on_site` skips. Every
  skip must have a node id, non-empty reason, `on_site` marker, and membership
  in the declared conditional set. Output is stable sorted JSON.
- **RE-MEASURE contract — PASS.** `AGENTS.md` now requires local/hosted shell
  comparisons to use the machine summaries and comparator, defines the same
  population-equivalence relation, treats unnamed or unmarked skips as
  failures, and requires the record's number to be comparator-derived rather
  than transcribed from a log.
- **Three fail-befores — PASS.** The focused tests captured all required
  rejections: unmarked hosted skip (`is not marked on_site`), collected
  mismatch (`collected mismatch`), and absent reason (`reason must be
  present`).
- **v0.23 replay — PASS.** The comparator derived collected **275**,
  equivalent passed **275**, local passed **275**, hosted passed **274**, and
  hosted `on_site` skips **1**, naming the conditional node and protected-input
  reason. Claim verification rejected the false hosted passed **275** /
  skipped **0** assertion because it derived passed **274** / skipped **1**,
  and accepted the measured assertion.
- **R12 mutation — PASS.** R12 now exercises the real parser/comparator with an
  unmarked skip. Mutating away that exact guard produced
  `test-population planted controls were not detected: unmarked-skip`.
  `invariant-scan` passes **12 rules / 39 controls**, with R12 **16**
  controls. The focused comparator/invariant suite passed **30** tests.
- **Full acceptance — PASS.** Local Python 3.11.4 and 3.12.13 each collected
  **283**, passed **283**, failed **0**, and skipped **0**, retaining the one
  accepted third-party warning. Full `./run ci-local` passed all **20** jobs:
  workspace **133**, net **55** (**29 + 26**), both warning-denied Rust lanes,
  clean clippy/fmt/ShellCheck, all **236** pins, protected databases **2**, and
  embedded golden **11 checks**. Mandatory standalone golden passed all **11**
  checks; delta **0**.

### 2026-07-30 · HISTORY-BOUND

- **Gate and operator decision — PASS.** E0 bounded the affected set to one
  false RE-MEASURE record, with the same figure copied into the closed
  execution record; POPULATION-COMPARE is committed and audited. On 2026-07-30
  the operator approved applying the established dated-supersession instrument
  rather than adding a checklist retraction.
- **Dated supersession — PASS.** The v0.23 `2026-07-29 · RE-MEASURE` progress
  entry and its closed-runbook copy claimed each hosted shell lane passed
  **275** tests with no skip and equalled local. Run `30459746825` attempt
  **1** actually collected **275**, passed **274**, and skipped **1** named
  `on_site` node for the protected-corpora-and-built-`cored` reason. The
  v0.23 POST-PUSH append for run `30462710258` already introduced this
  correction; the new dated forward entry confirms the exact boundary.
- **Class size — PASS.** The class is **isolated**: exactly **one** false
  RE-MEASURE record, represented in two historical locations by the progress
  entry and copied closed-runbook statement.
- **G4 criterion — DECIDED.** Retractions govern later-falsified accepted
  product, invariant, or task properties of resolved checked tasks. An
  incorrect append-only audit figure instead uses a dated superseding entry
  when the underlying execution remains valid. The operator classified this
  event as the latter; `config/checklist-retractions.json` stays byte-identical
  and the count remains **3**.
- **Non-impact — PASS.** The defect is the recorded measurement only. It
  changed no runtime, signed identity, protected pin, protected database, green
  job conclusion, release graph, or public surface. The annotated tag still
  peels to closing commit `e7715fb9…`, whose first parent is release commit
  `8bb6a714…`; all **236** pins and both protected databases match.
- **Fifth instance — PASS by measurement.** v0.23's author-side criterion is
  one distinct normative runbook requirement for which no sequence or outcome
  can satisfy the requirement and governed action. Its measured four members
  are v0.19 mutable-main freshness, v0.20 post-push-before-close ordering,
  v0.22's closing field set, and v0.22's source prohibition. The bare equality
  requirement first authored in v0.21 Step 6 after v0.19's skip clause was
  dropped is one distinct additional member, for **5** total. This is the first
  whose consequence was a false published number rather than only an
  unmeetable criterion.
- **Historical immutability — PASS.** The v0.23 runbook and progress blobs
  remain `94745d8…` and `bea2851…`; the unchanged retraction-registry blob is
  `9e13d2d…`. No closed runbook or historical progress entry was edited.
  Mandatory standalone golden passed all **11** checks; delta **0**.

### 2026-07-30 · PUBLISHER-REVIEW

- **Gate and operator judgement — PASS.** Step 4's affected set is one record,
  so the conditional step is eligible. The operator selected SEC EDGAR filings
  feeds for `finance`, authorized the review outcomes, and kept admission
  explicitly separate. The review changes only `observations/v0.24/**` and
  status records; no configured source is added.
- **Candidate reason — PASS by configuration and retained wire evidence.**
  `config/core.json` contains three RSS sources and all three carry fixtures;
  the two `technology` sources and one `finance` source point to `example.org`.
  The sole live-publisher corpus is v0.18 `arxiv-cs` under `IndexOnly`; the
  configured `CcBy` and `PublicDomain` cases remain fixture-only. arXiv's
  `robots.txt` result was 404 and exercised no real policy group. The reviewed
  endpoint is SEC's official US GAAP structured-disclosure RSS feed,
  `/Archives/edgar/usgaap.rss.xml`.
- **Robots wire evidence — PASS.** A robots-only preview used the shipped
  `HttpRobotsFetcher`, installed crawler identity, `RobotsCache`, and
  `RobotsGate`. Its one final request was
  `GET https://www.sec.gov/robots.txt`, with zero redirects and no feed or
  document request. The served policy is **2,622 UTF-8 bytes**, SHA-256
  `72d6196b3f20737396e566ddeb769fb4174b44f334985a1267a59ae0f08c2f2f`.
  The wildcard group applied, no rule matched the RSS path, no `Allow`
  exception applied, no `Crawl-delay` existed, and the shipped verdict was
  **allow**. An earlier robots-only pass excluded the latest-filings Atom path:
  `/cgi-bin/browse-edgar?action=getcurrent&output=atom` matched
  `Disallow: /cgi-bin` and was denied.
- **Identity finding — PASS and contradicts the prior expectation.** The actual
  request used
  `intel-platform/0.15.7 (research prototype; contact: [operator contact
  redacted])`; a monitored contact was present. Current production construction
  refuses a missing contact, so the review does not claim that contact needs to
  be newly added.
- **Licence and terms — PASS.** The observation cites the SEC Webmaster FAQ,
  Developer Resources, and Privacy Information by URL and **2026-07-30** read
  date, with the publisher's exact statements for EDGAR reuse, declared User
  Agent, the 10-request-per-second ceiling, and unclassified automated tools.
  It distinguishes the SEC's express reuse permission for EDGAR public filing
  content from the broader, unsupported claim that every issuer-authored filing
  is government-authored.
- **Recommendation — admissible, conditional.** Any later admission must use
  `/Archives/edgar/usgaap.rss.xml`, preserve the existing monitored-contact
  crawler identity, and remain at or below the SEC's then-current published
  total request ceiling. The deferral trigger now carries those conditions and
  still requires a separate v0.25 operator admission decision.
- **Non-establishment and non-impact — PASS.** The review establishes neither
  multi-origin robots-cache/per-host-limiter behaviour nor the **live RSS wire
  path**. No feed was requested, so live RSS fetching, parsing, and cursor
  durability remain untested. `config/core.json` remains byte-unchanged at blob
  `0ef1dcb4dde5f3cbd7b9112a405efb64d80e4914`; no source, production code,
  tool, workflow, schema, protected artifact, public surface, or ref changed.
- **Golden-E2E delta: 0.** Mandatory standalone execution passed all **11**
  checks.

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
   never seen two origins and will not until a source is admitted; and nothing
   about the **live RSS wire path**, because no real feed is fetched and live
   fetching, feed parsing, and cursor durability against a real server remain
   untested until admission.
6. Update the deferral row: the trigger for admission becomes "a completed review
   with an admissible recommendation, plus a separate operator admission
   decision."

**Acceptance criteria.** One candidate named with its reason · policy fetched
through the shipped matcher with bytes, hash, verdict, and identity recorded ·
licence and terms cited by URL and date · one recommendation recorded, including
undetermined as a complete outcome · non-establishment of the multi-origin
cache/limiter and the **live RSS wire path** (live fetching, parsing, and cursor
durability) stated explicitly · no source added and `config/core.json`
unchanged · deferral row updated · golden 11/11.

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
at that commit · hosted `invariant-scan` counts recorded and equal to local at
the same candidate commit, with the population-equivalence rule executing ·
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

- [x] **E0** — entering matrix with shell recorded as collected/passed/skipped;
  G1 confirmed; G2's clause presence/absence and the two opposite resolutions
  recorded; **G3 bounded to an exact set** with retention gaps stated; G4's
  criterion stated before its answer; G5 recorded; G6 named or refuted; manifest
  and verify time freshly measured
- [x] **POPULATION-EXPLICIT** — marker registered alongside the `skipif`, not
  replacing it; `--collect-only -m on_site` enumeration recorded; identical
  machine-readable summary from both lanes; no change to which tests run, shown;
  `run` pin updated
- [x] **POPULATION-COMPARE** — comparator asserts collected equality, passed +
  marked-skip equivalence, and named reasons; unmarked skip is a failure; three
  fail-befores; **v0.23's figures replayed with the false claim rejected**;
  `AGENTS.md` acceptance rewritten; planted failure detected
- [x] **HISTORY-BOUND** — one dated superseding entry per affected record; class
  size stated with a supported adjective; G4 decided with its criterion; scope of
  non-impact stated; fifth-instance count measured; no closed record edited
- [x] **PUBLISHER-REVIEW** — complete, or deleted with the measurement that made
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
