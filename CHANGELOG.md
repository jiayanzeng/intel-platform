# Changelog

All notable changes to intel-platform releases are recorded here.

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
