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

> **Measured correction — 2026-07-24 (B0 `1054994`, A1 `2adf486`).**
> B0 found the tree clean at
> `d09eda8cd611c3465aaad7a828465bdb8d8de26f`, described as
> `v0.8.0-15-gd09eda8`: 15 commits past release commit `bfc8c5a` (annotated
> tag object `314c1dd`), not `091a203` plus one later documentation commit.
> It measured **98 workspace / 20 net / 88 shell** tests, not 92 workspace
> tests. A1 raised the shell count to **93** and made
> `config/protected-artifacts.json` the sole expected-hash authority while
> deleting `config/protected-artifacts.sha256`. The asserted paragraph above
> remains intact as the hypothesis B0 tested.

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

**ID note (2026-07-24).** This v0.9 A1 is the evidence-provenance manifest
task. It is distinct from v0.8.2 A1, which made the fingerprint verifier
failure-capable; the committed v0.9 id is retained because `2adf486` and its
audit record already refer to it.

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

## Step 3 · D3 — Make the v0.9 runbook true against measured state 🤖

**Objective.** Preserve the original hypotheses while adding dated corrections
for what B0 and A1 measured, remove task-id ambiguity, and make the unstarted
tasks capable of producing meaningful evidence.

**Gate.** Protected artifacts must be 2/2 exact and golden 11/11 before editing.
This step changes documentation and task metadata only: no Rust, Python,
`run`, dependency, build input, protected data, or architecture rule change,
and no implementation of P2, V1, D4, or R2.

**Steps.**
1. Banner the entering-state correction and append the closing provenance
   correction without rewriting either historical paragraph.
2. Supersede the historical P1 hash-list reference through a dated STATE
   addition; distinguish the two committed A1 tasks; rename the colliding
   deferred-audit id to D4.
3. Record the step-number citation search, insert D3, and renumber the
   uncited remaining steps.
4. Anchor V1's predeclared SLO to A3's measured cost, require both protected
   corpus sizes, and make empty-sector/cache-invalid warm runs fail.
5. Define P2's transport-block disposition and require R2 to inventory every
   carried non-result.
6. Rebuild and measure a repo-local ignored Python 3.12 lane; record that
   requirements floors are repeatable rather than pinned/reproducible.
7. Record the unexecuted manifest-admission policy as a named future risk; do
   not implement its control here.

**Failure-capable controls.** Prove the old live deferred-audit id and
unstarted id collisions are absent; enumerate every remaining historical
legacy SHA-256-manifest reference; and make a malformed commit value in the
new progress entry fail `./run progress-check` before restoring it byte-for-byte.

**Acceptance criteria.** Corrections appended, not rewritten · ids and step
numbers unambiguous · V1 threshold can fire and both corpus points are required
· P2 live non-result cannot masquerade as completion · Python 3.12 lane rebuilt
and measured · manifest-admission risk recorded · no repository command, code,
build input, architecture rule, lockfile, or protected-data change · full
matrix, golden, and artifact checks green.

**Done when** this file describes the measured cycle and every remaining gate
can still distinguish pass from non-result.

---

## Step 4 · P2 — Make the real provider wire probe reproducible 🤖 + 🧑

**Objective.** T4 succeeded only after separating provider identity from the
command runner's transport: the deployment host reached
`192.168.0.192:8080/8081` directly, while Codex used operator-owned SSH forwards
on 18080/18081. Turn the minimal capability probe into a command while keeping
keys and machine-specific tunnel aliases uncommitted.

**Operator action, only if the direct endpoints are unreachable from the
runner.** Start the same SSH forwards used for T4 and report that they are
ready. Codex performs every subsequent probe and verification.

**Gate.** Transport failure is not provider failure. If health cannot be
reached, record the exact route and error and stop the live leg; do not rewrite
the committed profile, switch providers, or substitute the mock. If model
identity or embedding dimension differs from the last evidence, stop before a
full verifier run and treat it as a model-change decision.

**Blocked-path disposition.** A transport block still ships and records the
harness half: the probe command, all four classifications, and the local-double
failure controls. Record the live leg as a non-result with its exact route and
error, then re-run that leg in this cycle once the operator confirms the route.
Do not open a new correction-cycle file. P2's checklist box remains unchecked
until both the harness and live-wire halves are recorded.

**Execution status — 2026-07-24.** The harness half is implemented and its
failure-capable controls are green. The configured direct health routes
`http://192.168.0.192:8080/health` and `:8081/health` each returned curl exit 7,
HTTP 000, `Couldn't connect to server`; the command classified the direct chat
route `TRANSPORT BLOCKED` with `[Errno 65] No route to host`. The prior
transport-only aliases are not currently present: chat
`http://127.0.0.1:18080/health` returned `[Errno 61] Connection refused`, and
embedding `:18081/health` returned curl exit 7 / HTTP 000. The live leg is
therefore a non-result awaiting the named operator tunnel action and an
in-cycle rerun. P2 remains unchecked.

**Live completion — 2026-07-24.** After the operator confirmed the SSH
forwards, the exact transport-override probe passed: both health/model routes
returned HTTP 200, chat returned the required HTTP 501 unsupported-embeddings
diagnosis, and embedding returned one index-0 vector from the configured
EmbeddingGemma model at the predeclared **768** dimensions. One fresh,
uninterrupted `./run verify-llm` then passed **6/6** required checks with
13 missing → 0 embeddings in one request, consistent stored dimension 768,
clean five-document hybrid retrieval, four attested IndexOnly citations with
no public overlap, and adversarial `NOT EXERCISED` / no violations. Both
harness and live halves are now recorded; P2 is complete.

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

**Acceptance criteria.** Harness half shipped even if transport is blocked ·
minimal provider probe is executable and bounded · transport and provider
failures are distinct · model/dimension drift stops the run · keys absent from
output · live leg records one uninterrupted real verifier result, or remains an
explicit unchecked non-result awaiting an in-cycle rerun · protected artifacts
unchanged · golden unchanged.

**Done when** both halves are recorded: the failure-capable harness, and live
LAN capability evidence from one command plus, only when necessary, the named
tunnel action.

---

## Step 5 · V1 — Measure `/view`; do not materialize it yet 🤖 + 🧑

**One human input: approve or replace the anchored SLO before measurement.**
A3 measured one post-change `POST /retrieve` on a disposable copy of the
2,600-row archive at **0.016264 s** for `learning`, sector `science`, `k=8`.
That one-shot value is a cost anchor, not an SLO. The recommended reference-host
rule is cold p95 ≤ **10 × anchor = 162.640 ms** across ten process restarts and
warm p95 ≤ **2 × anchor = 32.528 ms** across 100 requests. Ten-fold cold
headroom accommodates process startup, SQLite open, sector-scoped load, and
analysis absent from the retrieval anchor; two-fold warm headroom requires a
real cache hit to remain close to the already-measured local HTTP/store cost.
The operator may approve or replace the factors and values, but before the
first sample V1 must record (a) this source measurement, (b) each chosen
headroom factor and its reason, (c) the exact p95 value whose breach fires the
trigger, and (d) whether that value is physically plausible on this host. An
implausibly high threshold must be rejected before timing.

**Objective.** Measure restart warm-up against disposable copies of both
protected archives—1,764 and 2,600 rows—so the evidence has two corpus points
and a slope. This task is a benchmark and decision, not permission to implement
materialization.

**Gate.** If both archives' cold and warm p95 meet the predeclared SLO in two
independent runs, `/view` materialization remains deferred. If either archive's
cold or warm p95 misses in both runs, the trigger fires: stop and write a design
task with the measurements. Do not implement a cache table inside V1. A one-off
outlier is rerun and reported, not silently discarded. An SLO that cannot fire
is a defect, not a pass.

**Steps.**
1. Verify both protected hashes, create one byte-for-byte copy of each archive
   below `mktemp -d`, and point `CORE_DB` only at the active copy.
2. Add a standard-library benchmark tool and `./run benchmark-view`. It must
   record commit, hardware/OS summary, archive identity, corpus count, sector
   query, iteration count, cold samples, warm samples, min/median/p95/max,
   failures, and the two-point size/latency slope.
3. Draw the requested sector set from `config/core.json`; both protected
   archives use `science`. Every sample must assert a non-zero document count.
4. Cold measurement means a new `cored` process and first `/view` request for
   every sample. Warm measurement reuses one process and the same valid sector
   set, asserts a cache hit, and proves the backing generation did not move.
5. Run the complete benchmark twice for each archive. Store all four reports
   and the cross-corpus slope under a documented evidence path; do not store
   either disposable database.
6. Re-hash both protected databases after the benchmark and run golden.

**Failure-capable control.** Give the benchmark a local delayed endpoint and
prove the declared SLO produces a non-zero exit naming `cold`, `warm`, or both.

**Acceptance criteria.** Anchor, factors, firing values, and host plausibility
fixed before timing · an SLO that cannot fire is a defect, not a pass ·
disposable 1,764-row and 2,600-row copies used · both distributions and their
slope reported · sectors come from `config/core.json` · every sample has a
non-zero document count · every warm sample is a cache hit against an unmoved
generation · an empty-sector warm path fails the benchmark · slow control
fails · materialization explicitly deferred or promoted to a separate design
task by the gate · protected hashes exact · golden unchanged.

**Done when** `/view` has a measured threshold and disposition rather than
"we'll know when it matters."

**Gate disposition — measured 2026-07-24.** The approved 162.640 ms cold p95
was missed by both archives in both independent runs; the 32.528 ms warm p95
passed in all four cells. The design trigger therefore fired. V1 stopped
without implementing materialization and promoted V2 below. Exact samples,
distributions, host identity, source hashes, and both run-specific slopes are
preserved under `evidence/v0.9/view-benchmark/`.

### Promoted future design task · V2 — Design restart-safe `/view` materialization

**Status.** v0.10 candidate created by V1's fired gate; this is not an
additional v0.9 execution step.

**Measured input.** With a 16.264 ms A3 anchor and a predeclared 162.640 ms
cold / 32.528 ms warm p95 SLO, the 1,764-row archive measured cold p95
1,693.423417 ms and 362.794125 ms, while the 2,600-row archive measured
543.318334 ms and 523.764917 ms. Their warm p95 values were respectively
8.164166/8.469334 ms and 12.584125/12.565458 ms. The 1,693.423417 ms sample is
retained as an outlier; the second complete run still missed, so discarding it
cannot reverse the gate.

**Objective.** Design—not yet implement—a restart-safe derived representation
that addresses the cold path while preserving the already-passing in-process
generation cache. First separate process/SQLite startup from sector corpus
load, analysis, serialization, and response transfer so the design targets the
measured cost rather than assuming a cache table is the answer.

**Constraints.** The design must preserve HC1, core-SQL sector enforcement
(HC2), core's no-LLM boundary (HC3), and corpus-derived dedup identity. Any
persisted core representation is archive/query state under HC9, never
shell-owned configuration. Its key and invalidation proof must cover archive
identity, sector set, algorithm/schema version, and every corpus mutation; an
in-memory generation that resets on restart is not sufficient.

**Gate and acceptance.** Do not select an implementation until a
failure-capable stale-result control proves invalidation requirements. Any
later implementation must rerun V1's two-archive, two-run benchmark and meet
both predeclared thresholds without changing the JSON response, protected
artifacts, or golden 11/11 result.

---

## Step 6 · D4 — Re-audit every deferred trigger, without implementing it 🤖

**Objective.** Make the defer table at the top executable as an audit. The
result is allowed—and expected—to be "all still deferred."

**Gate.** A fired trigger promotes only a future design task. It does not grant
permission to implement the deferred subsystem inside D4.

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

## Step 7 · R2 — Close the cycle with one explicit release identity 🧑

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
   storage, public API, operations, evidence, or documentation. State the
   disposition of every non-result carried out of the cycle.
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
- [x] **D3** — v0.9 runbook corrected against measured B0/A1 state
- [x] **P2** — provider capability probe reproducible; real wire disposition recorded
- [x] **V1** — `/view` cold/warm measured against a predeclared SLO; cold
  trigger promoted to future V2
- [ ] **D4** — all deferred triggers re-audited; no gate bypassed
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

**Execution correction — 2026-07-24.** B0 and A1 were executed on
2026-07-24 and are recorded by implementation commits `1054994` and
`2adf486` plus their separate audit commits.
