# Changelog

All notable changes to intel-platform releases are recorded here.

## Unreleased

### Fixed

- Final `/retrieve` hydration and `/attest` now bind the shell-decided sector
  set in core SQL. The internal `/attest` endpoint intentionally returns the
  same `400 unknown context document id` response for an out-of-sector id and a
  nonexistent id, removing the former cross-sector existence/match oracle.

## v0.12.0 — 2026-07-27

### Added

- A registered invariant scanner with executable R1–R6 rules, captured planted
  failures, local CI job 20, and hosted execution inside the Python 3.11 shell
  leg. The rules cover the production canonical-threshold seam, core bind path,
  core LLM-client absence, tracked credential boundary, single private distance
  constant, and mirrored model-profile authorization text.
- A guarded `./run models status|intel|athenaeum|athenaeum-bulk|stop` operator
  surface. Its L1 controller builds commands from a structured allowlist for
  exactly five named containers and the documented read-only probes.
- Pure, failure-capable model-profile guards for incomplete container
  inventories, foreign listeners, non-ready health results, and managed,
  absent, stale, or unreadable control sockets.
- Retraction-aware checklist auditing and a permanent forward correction for
  the false v0.11.0 canonical-threshold criterion.

### Changed

- Non-paged document append and corpus-wide canonical rematerialization now
  share one SQLite transaction, so a rematerialization failure returns HTTP 500
  without leaving appended rows or advancing view generation.
- Production canonical rematerialization selects its threshold only inside the
  store; the caller-supplied threshold seam remains test-only.
- Tracked infrastructure policy now treats credentials—not documented private
  LAN coordinates—as the enforceable disclosure boundary.
- Authorization-surface hashes join evidence-file hashes in protected-artifact
  manifest schema 2.

### Fixed

- v0.11.0 shipped a threshold-source defect: STORE-IDENTITY claimed one shared
  `max_distance` constant while the production ingest handler separately passed
  literal `16`. v0.12 INGEST-ATOMIC and THRESHOLD-ONE correct that claim
  forward; the published v0.11.0 tag and its evidence remain unchanged.
- A failed non-paged canonical rematerialization can no longer durably append
  documents while leaving the prior view generation in place.
- Model-profile parsing and transition decisions now fail with structured
  refusals instead of exposing bare parsing errors or silently routing around
  unsafe observed state.

### Publication and carried dispositions

- The operator selected and authorized v0.12.0 rather than a correction-only
  v0.11.1. The correction half alone could have been a patch, but the same
  release adds the `./run models` operator surface and changes `/ingest` failure
  semantics; one minor release accurately names the combined shipped change.
- Hosted run 30253646597, attempt 1, passed all seven expected jobs at exact
  evidence candidate `d664a7d3c524a3dfab932e158d9545953844b8dd`.
  The release audit accepted seven distinct authenticated receipts with zero
  rejection, measured five deferred / two promoted rows, and recorded
  exact-cosine p95 at 10.324209 ms for 2,600 documents.
- Real hosted controls rejected a persisted failed-core receipt and a duplicate
  `python=3.11`/missing-`python=3.12` shell matrix, accepting zero executions in
  each case. The admitted report, receipts, and Sigstore bundles bring immutable
  evidence to 69/69 pins; both authorization-surface pins also match.
- v0.11.0 remains published with the known threshold-source defect named above;
  its tag, release commit, receipts, report, and 54 pins are unchanged.
- A4 remains open because a rewritten shell can bypass or falsify the trusted
  `/attest` handoff. Model-profile authorization is L1 client-side defense only:
  an edited controller can rewrite it, and the L2 server forced-command wrapper
  remains scheduled for the next authorized server session.

## v0.11.0 — 2026-07-27

### Added

- Structural loopback-only startup validation for every resolved `CORE_BIND`
  address, with refusal before configuration, archive setup, or listener bind.
- Explicit sector sets on `/docs` and `/embeddings/missing`, enforced by bound
  predicates in core SQL and empty-set fail-closed behavior.
- Failure-capable coverage for duplicate robots groups, percent-equivalent
  paths, crawl-delay timing, missing publisher policy, billing rollback, and
  canonical identity after edits and takedowns.

### Changed

- Same-specificity robots groups now merge in file order while a specific
  product match remains isolated from generic `*` rules; multiple applicable
  crawl delays use the conservative maximum.
- Robots patterns and request paths normalize unreserved percent triplets
  without decoding reserved delimiters or turning encoded literals into
  wildcards.
- Crawl-delay changes update the existing per-host limiter in place, preserving
  its clock and acquisition counter; network ingestion without a publisher
  policy cache now fails closed.
- Billing batches validate against detached state before publishing once, and
  successful document maintenance rematerializes corpus-wide canonical identity
  in the same SQLite transaction.

### Fixed

- Non-loopback or mixed-resolution core binds can no longer expose unauthenticated
  internal endpoints.
- Internal document enumeration can no longer escape the core's sector boundary.
- A later invalid billing event can no longer leave an earlier entitlement
  mutation live in memory or persist it through an unrelated save.
- Document edits, publication-order changes, and canonical-row deletion can no
  longer leave stale or dangling `canonical_id` values.

### Publication and carried dispositions

- The operator selected a minor release because `/docs` and
  `/embeddings/missing` gain required internal query parameters and bind,
  robots, billing-failure, and maintenance-write behavior changes. Public
  `/v1/*` JSON bodies, the SQLite schema, cache representation, dependency
  resolution, and golden retrieval outputs are unchanged.
- Hosted run 30236305375 passed all seven expected jobs at exact candidate
  `17221504d0c572e2b52f8509cb720d4a7c72f47d`. The release audit authenticated
  all seven distinct receipts with zero rejection, measured five deferred /
  two promoted rows, and recorded exact-cosine p95 at 15.033417 ms for 2,600
  documents.
- Real hosted controls rejected a persisted failed-core receipt and a duplicated
  `python=3.11` matrix, accepting zero executions in each case. The admitted
  report, receipts, and Sigstore bundles bring immutable evidence to 54/54 pins.
- T7 single-flight, Postgres, pgvector, multi-host seam hardening, and the A4
  untrusted-shell boundary remain deferred. `/view` materialization remains a
  promoted future implementation; this release does not claim to close A4.
- v0.10.2 remains local and unpublished at its original annotated tag object;
  this release does not move or publish it.

## v0.10.3 — 2026-07-26

### Added

- Exact `(job, matrix)` identities for the seven-job hosted evidence set,
  including failure-capable duplicate-leg and failed-job controls.
- Run-scoped durable storage and SHA-256 pins for every accepted receipt and
  Sigstore bundle, plus a release-grade v0.10.3 production audit.
- A semantic historical-evidence registry and one active-cycle identity source
  for lifecycle, report-label, and benchmark tooling.

### Changed

- Release evidence now requires authenticated grade, a pinned workflow
  revision, exact successful single-run matrix coverage, and persisted posture
  that participates in re-derivation.
- Resumed adversarial attempts are revalidated against five one-way classifier
  invariants, their declared target/shape/model, and recorded overlap telemetry.
- Lifecycle checks distinguish strict local annotated-tag verification from
  hosted clones while retaining release-commit, contract-amendment, and stale
  source-literal enforcement.

### Fixed

- Duplicate receipt subjects or digests can no longer satisfy two matrix legs,
  and release-grade evidence cannot be produced in structural-only mode.
- A recorded receipt or bundle path must resolve to indexed, unchanged bytes
  in the named evidence worktree; lossy or fictional durable paths are refused.
- New audit labels no longer embed a stale prior cycle, and the immutable
  v0.10.2 mislabeled report is corrected by annotation without changing bytes.

### Publication and carried dispositions

- Hosted run 30202019640 passed all seven expected jobs at exact candidate
  `a1d8c958b4eaf4fe4add75cc49a7fec341c8f8a5`. The release audit authenticated
  all seven distinct receipts with zero rejection and measured two promoted /
  five deferred rows; exact-cosine p95 was 8.390958 ms.
- Real negative controls rejected the persisted failed-core run and a
  duplicated `python=3.11` shell matrix, accepting zero executions in each
  case.
- v0.10.2 remains local and unpublished at its original annotated tag object;
  this release does not move or publish it.
- This patch release changes release metadata, workflow/evidence integrity,
  lifecycle controls, tests, tools, and durable evidence only. Public and
  internal API behavior, runtime behavior, storage paths, database schema,
  cache representation, licensing outcomes, dependency resolution, and golden
  retrieval outputs are unchanged.

## v0.10.2 — 2026-07-26

### Added

- Authenticated GitHub build-provenance bundles for the complete seven-job
  released-commit matrix, plus a pinned production audit that accepts only
  exact, successful, single-run receipts.
- Cycle-contract regression coverage that rejects stale concrete task or
  progress paths in `AGENTS.md`.

### Changed

- Production deferred audits require an explicit expected HEAD, a clean
  worktree, exact receipt subjects, and the complete hosted job matrix before
  runner execution can be promoted.
- Adversarial-report resume accepts only internally consistent HTTP 200
  completions with the full current schema and stops immediately on any reused
  `LEAK`.
- The operating contract now derives active task and progress paths from its
  declared cycle instead of embedding stale cycle literals in the workflow.

### Fixed

- Receipt ancestry can no longer substitute for exact released-commit
  identity, and failed, partial, hand-authored, or unauthenticated receipt sets
  cannot promote execution evidence.
- Dirty or wrong-subject production measurements now abort before corpus work,
  and malformed or leaking resumed attempts cannot be silently trusted.
- Sigstore bundles persisted with a neutral extension are presented to the
  GitHub verifier through an ephemeral compatible filename without changing
  their authenticated bytes.

### Publication and carried dispositions

- v0.10.1 was published unchanged: remote `main` reached the reviewed Step 5
  audit record, the immutable v0.10.1 tag stayed on its release commit, and
  hosted CI produced seven authenticated successful receipts.
- The fresh v0.10.2 deferred audit records two promoted and five deferred rows,
  accepts all seven authenticated receipts with zero rejection, and measures
  exact-cosine p95 at 8.962542 ms for 2,600 documents.
- The fresh real-model matrix remains 45/45 valid cells as `NOT EXERCISED`,
  with zero `LEAK` and an independent `GUARD FIRED` positive control. T7
  single-flight, Postgres, pgvector, multi-host seam hardening, and the A4
  untrusted-shell boundary remain deferred.
- This patch release changes workflow, evidence integrity, lifecycle controls,
  tests, and release metadata only. Public and internal API behavior, runtime
  behavior, storage paths, database schema, cache representation, licensing
  outcomes, dependencies, and retrieval outputs are unchanged.

## v0.10.1 — 2026-07-26

### Added

- Runner-produced, persisted CI receipts whose commit ancestry is checked
  before they can promote the released-commit execution trigger.
- Corpus-free SHA-256 pins for the corrected deferred-audit receipt and fresh
  real-model adversarial report, plus a blocking source/config/Git
  re-derivation job.
- A guarded on-site test that executes the complete deferred-design production
  audit without requiring protected corpora on hosted runners.

### Changed

- Adversarial evidence counts only target-valid, model-completed attempts,
  retries transport failures without counting them, records graduated
  `n=8/12/16` telemetry, and requires a real-handler positive control.
- The local CI matrix has 19 tracked jobs; the workflow mirrors its new
  evidence re-derivation gate.
- Python constraint drift tests use an explicit synthetic distribution
  inventory while the product verifier continues to inspect the real
  interpreter and reject duplicates.

### Fixed

- The v0.10.1 deferred receipt now measures a clean detached v0.10.0 release
  tree and accepts seven real runner receipts instead of inferring execution
  from Git-remote presence.
- Finder `.DS_Store` files are ignored and the previously tracked copies were
  removed from version control.
- The real-model battery can no longer call a timeout a completed adversarial
  attempt, and the FastAPI pin-drift test cannot be masked by an unrelated
  ambient duplicate distribution.

### Carried dispositions

- The fresh real-model matrix completed 45/45 valid cells as
  `NOT EXERCISED`, with zero `LEAK`; the deployed-path positive control fired
  `GUARD FIRED`. This is an observed resistance result, not a proof that no
  model can reproduce gated text.
- T7 single-flight, Postgres, pgvector, multi-host seam hardening, and the A4
  untrusted-shell boundary remain deferred. CI-runner evidence and future
  `/view` materialization remain the two promoted deferred-audit rows.
- This patch release changes operations, evidence, and tests only. The public
  API, runtime behavior, database schema, cache representation, licensing
  boundary, and retrieval outputs are unchanged.

## v0.10.0 — 2026-07-25

### Added

- Executable active-cycle and checked-task auditors, plus failure-capable
  protected-artifact admission that rejects both byte drift and logical
  provenance drift.
- Reproducible Python 3.11/3.12 constraints, verified locally and on the first
  observed GitHub Actions executions.
- A decomposed `/view` cold-path benchmark and restart-invalidation verifier
  covering every mutation class without adding materialized storage.
- A resumable 45-cell real-model adversarial battery with separate
  failure-capable guard and leak controls.

### Changed

- The internal loopback `/view` response now exposes startup, SQLite-open,
  analysis, response-build, and serialization timing headers. Its JSON body,
  cache representation, public API, and database schema are unchanged.
- Deferred-design auditing now derives every progress input, measures seven
  triggers, and records CI-runner and `/view` promotions without implementing
  the five still-deferred subsystems.
- CI installs from the reproduced Python constraints and verifies that the
  resolved environment matches them before testing.

### Fixed

- The run harness is compatible with both local ShellCheck 0.11.0 and the
  runner's ShellCheck 0.9.0 diagnostics.
- The declared cycle checker accepts the current runbook's explicit closed
  state after release while continuing to reject a zero-unchecked runbook that
  has no valid closing record.

### Carried dispositions

- X1's real-model aggregate remains `NOT EXERCISED`, not a no-leak claim;
  failure-capable controls independently observed both `GUARD FIRED` and
  deliberate raw overlap without public overlap.
- T7 single-flight, Postgres, pgvector, multi-host seam hardening, and the A4
  untrusted-shell boundary remain deferred under their measured triggers.
- `/view` materialization remains a future implementation task; v0.10.0 ships
  only its measured design and internal diagnostic seam.

## v0.9.0 — 2026-07-25

### Added

- One executable JSON authority for protected-artifact hashes and logical
  provenance, with deterministic evidence reports and failure-capable controls.
- Bounded, secret-redacted provider capability probing that distinguishes
  transport blocks, identity drift, and capability failures before a full live
  verifier run.
- Reproducible `/view` and exact-cosine benchmarks plus an executable audit of
  every deferred scale and deployment trigger.
- A local 16-job release matrix, Python 3.11/3.12 lanes, and append-only
  progress-record validation.

### Changed

- Missing persisted fingerprints now fail closed at `/view`, `/retrieve`, and
  canonical-id materialization instead of being recomputed or skipped.
- Core document reads are sector- and id-scoped in SQL, and the process-scoped
  `/view` cache is bounded, validates configured sectors, and exposes internal
  hit/generation diagnostics without changing its JSON response.
- Provider identity is independent from a per-command transport route, allowing
  the same configured LAN models to be probed through operator-owned forwards.
- Execution-cycle names and artifact-release identities are now explicitly
  separate; the annotated tag and agreeing version sources define a release.

### Deferred

- `/view` restart materialization is promoted to future design task V2 after
  both protected archive sizes missed the predeclared cold p95 SLO twice; every
  warm distribution passed.
- T7 single-flight, Postgres, pgvector, and multi-host hardening remain deferred
  by measured triggers. Manifest-admission enforcement, dependency constraints,
  and a real-model `GUARD FIRED` observation remain named future work.

## v0.8.0 — 2026-07-24

### Added

- Core `/attest` enforcement for every public `/v1/ask` answer, with
  failure-capable controls for blocked and deliberately leaking model output.
- A protected-artifact manifest, disposable eleven-assertion golden E2E, and
  blocking CI coverage for lint, the net feature, MSRV 1.78, and release-version
  consistency.
- Strict per-model embedding dimensions, retrieval diagnostics for mismatched
  legacy vectors, and real-model verification against separately hosted Gemma
  chat and EmbeddingGemma embedding services.

### Changed

- Harvest pages now commit documents and continuation state atomically, and two
  live arXiv runs proved interruption-resume on the wire.
- Cross-origin redirects are followed manually only after the destination
  origin passes the full robots gate.
- SimHash fingerprints and corpus-global canonical identities are persisted and
  re-materialized deterministically rather than derived from arrival order.
- Bare live harvests use fresh databases and refuse the two protected evidence
  databases as targets.

### Deferred

- T7 scheduler single-flight remains deferred: the shipped scheduler is one
  synchronous writer, so no concurrent trigger exists to guard. The gate must
  be revisited if a concurrent scheduler is introduced.
