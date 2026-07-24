# Changelog

All notable changes to intel-platform releases are recorded here.

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
