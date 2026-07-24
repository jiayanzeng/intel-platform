# Changelog

All notable changes to intel-platform releases are recorded here.

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
