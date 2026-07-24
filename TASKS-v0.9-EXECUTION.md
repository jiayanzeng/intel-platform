# TASKS-v0.9-EXECUTION.md — evidence and operations runbook for Codex

v0.9 is an **evidence-and-operations cycle**. It does not add an ingestion
source or subscriber-facing product surface. The work is deliberately narrower:
make protected live evidence self-describing, make the split local-model wire
check reproducible, measure `/view` before considering another storage shape,
and close the cycle with an explicit release decision.

**Entering state (asserted, not yet verified).** The code baseline is clean at
`091a203`, one CI-only/harness commit after annotated tag `v0.8.0` (`bfc8c5a`);
this runbook is the only expected later documentation commit when B0 begins.
Runtime version sources report 0.8.0. The measured matrix is 92 workspace Rust
tests, 20 net tests, and 88 shell tests under Python 3.11 and 3.12;
warning-denied offline/net checks, clippy, fmt, ShellCheck, Python floor
compilation, and locked Rust 1.78 are green. Golden is 11/11. Protected artifacts
are `data/core.db` (1,764 documents) and `data/live-smoke.db` (2,600 documents),
with hashes recorded in `config/protected-artifacts.sha256`. The dedicated LAN
models last passed one uninterrupted 6/6 verifier run.

**Every sentence above is a hypothesis until Step 1 measures it.** Prior
measurements are not permission to skip the entering-state run.

**How to run this file.** Execute top to bottom, one task and one commit at a
time. Follow `AGENTS.md §5` after every task: check the gate first, implement,
run and capture every acceptance criterion, run `./run golden`, update
`STATE.md`, append `PROGRESS-v0.9.md`, check the box here, and commit.

- **🤖 = Codex executes and self-verifies end to end.**
- **🧑 = one named operator decision or action is required.** Everything else
  in that task remains Codex's responsibility.

**Global definition of done.** Protected hashes exact unless a task explicitly
stops at the artifact-drift gate; golden 11/11; `./run version-check` green;
zero rustc warnings on offline and net builds; all Rust tests green; all shell
tests green under Python 3.11 and 3.12; clippy, fmt, ShellCheck, floor
byte-compilation, and locked Rust 1.78 green. No mock result is promoted to
wire evidence.

## Deferred means deferred

These triggers have **not** fired. Each task must re-measure its trigger; none
may implement the deferred design merely because v0.9 mentions it.

| Deferred item | Unchanged trigger | v0.9 action before the trigger |
|---|---|---|
| T7 robots single-flight | a second concurrent harvester | audit topology only |
| Postgres | a second writer | audit writer count only |
| pgvector | corpus scale beyond SQLite's comfort, measured | record corpus size and retrieval latency |
| Multi-host seam hardening (UDS/mTLS) | an actual core/shell host split | record bind/deployment topology |
| `/view` materialization | measured warm-up cost crossing a defined SLO | benchmark a disposable archive copy first |

---

## Step 1 · B0 — Rebuild the entering state from commands 🤖

**Objective.** Establish the actual v0.9 baseline and create
`PROGRESS-v0.9.md`. Do not inherit counts, tags, artifact facts, endpoint
availability, or tool versions from the v0.8 handoff.

**Gate.** If any entering-state claim is false, stop and correct `STATE.md`
before starting Step 2. A changed protected-artifact hash is a separate hard
stop: inspect the database and provenance; do not update the manifest to bless
unknown bytes.

**Steps.**
1. Capture `git log --oneline -5`, `git status --porcelain`,
   `git describe --tags --always --dirty`, and the commit/tag object for
   `v0.8.0`. Record that HEAD is or is not past the release tag.
2. Run `./run version-check` and read each version from its source. Confirm
   `CHANGELOG.md` describes the tag that actually exists.
3. Run the full `AGENTS.md §4` Rust matrix, including warning-denied offline/net
   checks, tests, clippy, fmt, and locked Rust 1.78 check/tests.
4. Run the shell suite independently under Python 3.11 and 3.12. Byte-compile
   every Python file with 3.11, run `shellcheck ./run`, and record interpreter
   and ShellCheck versions.
5. Run `./run down`; prove ports 8787, 8788, and 8899 are clear.
6. Run `./run verify-artifacts`, then independently measure both protected
   databases: SHA-256, byte size, document count, NULL `simhash` /
   `canonical_id` counts, `PRAGMA integrity_check`, and complete cursor rows.
7. Run `./run golden` and capture all eleven named assertions.
8. Run `./run config` only for its redacted resolution. Record the selected
   endpoint hosts, models, dimensions already evidenced in STATE, and timeouts;
   make no provider call in this step.
9. Create `PROGRESS-v0.9.md` with this measured baseline and the exact commands.

**Failure-capable control.** Point `./run verify-artifacts` at a disposable copy
and disposable manifest, mutate the copy, and prove the command exits non-zero
with expected and actual hashes. Restore nothing in `data/` because nothing
there may be touched.

**Acceptance criteria.** Every entering-state claim confirmed or corrected ·
artifact mismatch control fails loudly · both Python lanes and the full Rust
matrix green · version/tag relationship recorded · golden 11/11 · protected
artifacts unchanged.

**Done when** the v0.9 baseline exists as measured commands in `STATE.md` and
`PROGRESS-v0.9.md`, not as copied prose.

---

## Step 2 · A1 — Give protected evidence one executable provenance record 🤖

**Objective.** `config/protected-artifacts.sha256` proves byte identity, but not
what each database is evidence *of*. Make path, hash, corpus facts, cursor state,
and provenance one machine-checked record. Preserve one authority rather than
adding another hand-maintained hash list.

**Gate.** If either protected database differs from B0, stop. Do not regenerate
expected metadata from the changed file. If a proposed format would require
mutating either SQLite database, reject that format and keep the metadata
external.

**Steps.**
1. Define an atomic-JSON evidence manifest under `config/` with, per artifact:
   relative path, SHA-256, byte size, purpose/provenance, document count,
   integrity expectation, NULL fingerprint/identity expectations, and cursor
   rows needed to interpret the evidence.
2. Migrate `./run verify-artifacts` to that manifest and remove the old
   `.sha256` file in the same commit. There must never be two authoritative
   expected hashes.
3. Add `./run evidence-report` to print the measured values without changing
   the manifest or database. Keep output deterministic and secret-free.
4. Keep live-harvest refusal driven by the same manifest. Resolve canonical
   paths before comparing so `./data/…` and absolute aliases cannot bypass it.
5. Wire the stronger verification into `./run test` and CI.
6. Document the lifecycle: protected artifacts are immutable evidence; every
   future live harvest uses the fresh path printed by `./run harvest-arxiv`; a
   new protected artifact is admitted only by an explicit task with captured
   wire evidence and operator review.

**Failure-capable controls.** Against disposable copies only, prove separate
failures for (a) byte mutation, (b) a logically changed document count with a
fresh matching hash, and (c) a changed cursor row with a fresh matching hash.
Each failure must name the artifact and disagreeing field. This proves the
record checks meaning, not only bytes.

**Acceptance criteria.** One authoritative manifest · hash and logical metadata
checked · live-harvest refusal still covers both protected paths and aliases ·
three controls fail on their intended field · no protected bytes changed ·
golden unchanged.

**Done when** an evidence database can be understood and rejected when wrong
without relying on a paragraph in `STATE.md`.

---

## Step 3 · P2 — Make the real provider wire probe reproducible 🤖 + 🧑

**Objective.** T4 succeeded only after separating provider identity from the
command runner's transport: the deployment host reached
`192.168.0.192:8080/8081` directly, while Codex used operator-owned SSH forwards
on 18080/18081. Turn the minimal capability probe into a command while keeping
keys and machine-specific tunnel aliases uncommitted.

**Operator action, only if the direct endpoints are unreachable from the
runner.** Start the same SSH forwards used for T4 and report that they are
ready. Codex performs every subsequent probe and verification.

**Gate.** Transport failure is not provider failure. If health cannot be
reached, record the exact route and error and stop; do not rewrite the committed
profile, switch providers, or substitute the mock. If model identity or
embedding dimension differs from the last evidence, stop before a full verifier
run and treat it as a model-change decision.

**Steps.**
1. Document environment precedence for direct LAN settings and per-command
   transport overrides. `./run config` must print the effective, redacted
   endpoints and models; it must never print keys.
2. Add `./run probe-providers`, using the already resolved chat and embedding
   roles. Bound every request by the configured role timeout.
3. Capture chat `/health` and `/v1/models`; send the intentional chat
   `/v1/embeddings` request and require the known 501 capability diagnosis
   without treating it as overall failure.
4. Capture embedding `/health` and `/v1/models`; send one short embedding
   request; assert exactly one index-0 vector and report its measured dimension.
5. The command must distinguish `PASS`, `TRANSPORT BLOCKED`, `IDENTITY CHANGED`,
   and `CAPABILITY FAILED`, exit non-zero for the latter three, and include
   status/body with secrets redacted.
6. After the minimal probe passes, run one fresh `./run verify-llm`; do not carry
   forward any T4 stage. Record models, request count, dimension, citations,
   attestation outcome, and every stage latency.

**Failure-capable controls.** Use a local double that can return a wrong model,
short embedding data, wrong vector dimension, and a stalled response. Prove
each classification and timeout. These controls validate the harness only;
the real endpoint run is still required by HC13.

**Acceptance criteria.** Minimal provider probe is executable and bounded ·
transport and provider failures are distinct · model/dimension drift stops the
run · keys absent from output · one uninterrupted real verifier result recorded
or an exact gate failure recorded · protected artifacts unchanged · golden
unchanged.

**Done when** repeating the LAN capability evidence is one command plus, only
when necessary, the named tunnel action.

---

## Step 4 · V1 — Measure `/view`; do not materialize it yet 🧑

**One human input: approve or replace the SLO before measurement.** Recommended
reference-host SLO: cold `/view` p95 ≤ **1,000 ms** across ten process restarts,
and warm `/view` p95 ≤ **100 ms** across 100 requests. Record the chosen values
before the first timing so the threshold cannot move to fit the result.

**Objective.** Measure restart warm-up against a disposable copy of the
1,764-row archive. This task is a benchmark and decision, not permission to
implement materialization.

**Gate.** If both cold and warm p95 meet the predeclared SLO in two independent
runs, `/view` materialization remains deferred. If either misses in both runs,
the trigger fires: stop and write a design task with the measurements. Do not
implement a cache table inside V1. A one-off outlier is rerun and reported, not
silently discarded.

**Steps.**
1. Verify the protected hash, create a byte-for-byte copy below `mktemp -d`,
   and point `CORE_DB` only at that copy.
2. Add a standard-library benchmark tool and `./run benchmark-view`. It must
   record commit, hardware/OS summary, corpus count, sector query, iteration
   count, cold samples, warm samples, min/median/p95/max, and failures.
3. Cold measurement means a new `cored` process and first `/view` request for
   every sample. Warm measurement reuses one process and the same sector set so
   it exercises the generation cache.
4. Run the complete benchmark twice. Store the reports under a documented
   evidence path; do not store the disposable database.
5. Re-hash both protected databases after the benchmark and run golden.

**Failure-capable control.** Give the benchmark a local delayed endpoint and
prove the declared SLO produces a non-zero exit naming `cold`, `warm`, or both.

**Acceptance criteria.** SLO fixed before timing · disposable 1,764-row copy
used · two complete reports with distributions, not one stopwatch value · slow
control fails · materialization explicitly deferred or promoted to a separate
design task by the gate · protected hashes exact · golden unchanged.

**Done when** `/view` has a measured threshold and disposition rather than
"we'll know when it matters."

---

## Step 5 · D1 — Re-audit every deferred trigger, without implementing it 🤖

**Objective.** Make the defer table at the top executable as an audit. The
result is allowed—and expected—to be "all still deferred."

**Gate.** A fired trigger promotes only a future design task. It does not grant
permission to implement the deferred subsystem inside D1.

**Steps.**
1. T7: inspect scheduler code, deployment units, and live process topology.
   Count potential simultaneous harvest callers; do not infer concurrency from
   the number of configured jobs.
2. Postgres: count supported writers and document the ownership path for every
   SQLite write.
3. pgvector: record current and largest evidenced corpus sizes plus measured
   exact-cosine latency. Compare to the existing scale design note; do not use a
   round document threshold without a latency measurement.
4. Multi-host: record core bind address, shell `CORE_URL`, deployment hosts, and
   whether any real core/shell request crosses a host boundary.
5. `/view`: import V1's chosen SLO and both measured reports.
6. Write a dated table in STATE with `trigger`, `measurement`, and
   `defer/promote`. If promoted, create a scoped v0.10 candidate—no code here.

**Failure-capable control.** Run the audit against a disposable synthetic input
showing two harvesters/two writers and prove it reports the relevant triggers as
fired. The production audit must still use measured repository/deployment state.

**Acceptance criteria.** All five triggers measured · synthetic audit can fire ·
no deferred implementation added · every disposition includes its unchanged
trigger · golden and protected artifacts unchanged.

**Done when** "deferred" is a current measurement, not inherited folklore.

---

## Step 6 · R2 — Close the cycle with one explicit release identity 🧑

**One human input: choose the release disposition after seeing the actual
diff.** Recommendation rule:

- choose **v0.9.0** if runtime/storage/API behavior changed;
- choose **v0.8.1** if changes are operational tooling and evidence only;
- choose **no release** only if the cycle produced no shipped change.

Record the rationale. A cycle name is not silently treated as an artifact
version.

**Gate.** Do not version or tag a dirty, failing, artifact-drifted, or
golden-drifted tree. Do not move or replace an existing tag. If "no release" is
chosen, document which commits remain intentionally unreleased.

**Steps.**
1. Inventory the diff since `v0.8.0` and classify each change as runtime,
   storage, public API, operations, evidence, or documentation.
2. Record in `ARCHITECTURE.md` the durable relationship between execution-cycle
   names and artifact releases.
3. For a release, update all version sources together, update `CHANGELOG.md`,
   run `./run version-check`, commit, and create one annotated tag on that exact
   commit. For no release, leave every version source unchanged.
4. Failure control: plant one version mismatch and prove the checker names it;
   restore. For a release, also prove the tag resolves to the release commit and
   the worktree is clean.
5. Run the full global definition of done one final time.

**Acceptance criteria.** Release/no-release rationale recorded · cycle/release
policy durable · all version sources agree · changelog/tag exact when releasing
· mismatch control fails · full matrix and golden green · protected hashes
exact.

**Done when** an operator can map source commit, tag, runtime version, and
evidence record without interpreting the cycle name.

---

## Cycle checklist

- [x] **B0** — entering state re-measured; v0.8.0 tag/HEAD relationship recorded
- [x] **A1** — protected evidence has one executable provenance manifest
- [ ] **P2** — provider capability probe reproducible; real wire disposition recorded
- [ ] **V1** — `/view` cold/warm measured against a predeclared SLO
- [ ] **D1** — all deferred triggers re-audited; no gate bypassed
- [ ] **R2** — release disposition recorded and, if applicable, tagged

## Standing prohibitions

- Do not mutate, delete, rename, vacuum, or "refresh"
  `data/core.db` or `data/live-smoke.db`.
- Do not hand-edit or delete `Cargo.lock` (HC12), raise the offline Rust 1.78
  floor, or lower the Python 3.11 floor.
- Do not move license attestation, sector filtering, robots policy, or
  canonical-id materialization out of their architectural owners.
- Do not let core call an LLM (HC3), re-enable automatic redirects, or weaken
  per-source missing-robots policy.
- Do not commit `.env`, provider keys, tunnel aliases, or raw secret-bearing
  responses.
- Do not promote fixtures, local doubles, or a health response to real
  end-to-end evidence (HC13).
- Do not implement a deferred subsystem in the task that audits or benchmarks
  its trigger.
- Do not batch STATE/PROGRESS updates or combine tasks in one commit.

## Provenance of this draft

Drafted against `main` at `091a203`, `v0.8.0` at `bfc8c5a`, and the measured
v0.8.1 handoff through C1 on 2026-07-24. The v0.9 tasks themselves have not been
executed. Step B0 deliberately re-verifies every entering claim before any
implementation.
