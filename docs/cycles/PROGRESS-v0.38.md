# PROGRESS-v0.38.md — append-only execution record

This file records v0.38 task and gate events after their implementation
commits exist. Each entry names the measured result, every applicable
acceptance criterion, the golden delta, and the real implementation commit.
Entries are append-only; corrections are new dated entries.

## Operator grants recorded before execution

The operator issued both dormant-step grants in the initiating request. The
grant text is recorded verbatim before either gated step runs:

> Please read agents.md and ARCHITECTURE.md first, then read the newly added file "docs/cycles/TASKS-v0.38-EXECUTION.md" and execute it strictly in accordance with the architectural design and constraints. Before the task begins, I will first authorize you to "publish v0.17.4" and "SEC EDGAR wire and admission."

Under the exact scopes defined by the runbook, the quoted labels activate
Grant A and Grant B; neither is generalized beyond those written bounds.

### 2026-08-04 · ACTIVATE — v0.38 cycle activation

- owner: Codex
- runbook: `TASKS-v0.38-EXECUTION.md`
- commit: e6d68c89aa1cf018c10ad289a42674350e3d7d1e
- result: PASS under the measured ordering fallback. Direct pre-activation
  `cycle-check` treated the untracked v0.38 runbook as an older open cycle and
  failed with exactly **7 unchecked boxes** plus **1 missing closing record**.
  Activation therefore precedes P1's repository record, while Grant A's exact
  remote actions remained the first milestone execution.
- author-contract correction: PASS. The supplied short deferral table omitted
  the prior trigger-bearing population and both governed artifact byte
  authorities; its non-none actions named `Step W1`, which the entry point
  cannot resolve as Step N. The committed runbook restores the derived
  carry-forward population and authorities and renames that heading to
  structurally equivalent **Step 2A**.
- declaration acceptance: PASS. Post-commit `cycle-check` resolves v0.38 from
  the declaration and reports `state=open`, with publication reconciliation,
  scope, trigger freshness, artifact boundaries, State regions, and prior
  closed cycles all accepted.
- retention acceptance: PASS. The pre-change configuration excluded through
  v0.35 and retained v0.36–v0.37. The derived v0.38 boundary excludes through
  v0.36 and the exact retained set is the v0.37–v0.38 task/progress pairs.
  Project-root `export-check` passed at **104 derived / 7 required / 158
  exported / 2,596,652 bytes / 2 retained cycles**.
- governed review-export measurement: tree=`e6d68c89aa1cf018c10ad289a42674350e3d7d1e`; bytes=`2596652`
- artifact acceptance: PASS. Two complete checks matched **2 artifacts / 333
  pinned files** in **0.11 s / 0.11 s real**; neither governed trigger fired.
- protected-input acceptance: PASS. The three historical amendment inputs
  remain untouched and untracked. No dependency, production source, protected
  byte, observation, fixture, or unauthorized ref moved during activation.
- golden-E2E delta: **0**. The first loopback-bind attempt was a sandbox-denied
  non-result; the permission-complete identical command passed **11/11**.

### 2026-08-04 · PUBLISH-V17-4 — exact Grant A publication

- owner: Codex
- runbook: `TASKS-v0.38-EXECUTION.md`
- commit: 36f94c77a2d6e47130f342f7ffa2476bc280ab62
- grant: PASS. The initiating request's verbatim grant is recorded above
  before the gated action; its `publish v0.17.4` label activates only the exact
  Grant A scope stated in the runbook.
- precondition acceptance: PASS immediately before push. Remote `main` was
  exact `e068cacc76685791c54ab47c84be6abbd592271d`; v0.17.4 was absent; the
  ancestor check exited 0; and local annotated object
  `902d30f046c7e9f493fe3a18eefd5275ca5c5afe` peeled to exact closing commit
  `f4f2690a442d7a77f1dabb53fb3a120a2c987e97`.
- publication acceptance: PASS. One non-force branch push advanced only
  `origin/main` to `a7d6c80e7e5ccd963e8ebb46ee054b30af88abb0`; one non-force
  tag push created only v0.17.4. Fresh readback matched the branch, annotated
  object, and peeled target exactly. No ref was forced, deleted, or moved
  beyond Grant A.
- hosted acceptance: PASS. Push-triggered run **30841505130**, attempt **1**,
  concluded `success` on the exact published head; all **9/9** blocking job
  identities passed and dependency drift was the sole report-only skip.
- lifecycle acceptance: PASS. The current header says published, the exact
  five-field post-push record is at column zero, and the historical absence
  observation remains untouched. Direct `cycle-check` passes on the published
  path and reports exact v0.17.4 local-tag reconciliation.
- planted-control acceptance: PASS unmodified at **15/15 rules / 84
  controls**, including required/fresh post-push fields, unpublished-observation
  precedence, and published-descendant missing-record refusal.
- divergence acceptance: PASS. Publication resets the publication-epoch count
  to **0** at closing commit `f4f2690a…`; activation adds no runtime or public
  surface difference.
- stop conditions: none. No grant precondition, hosted identity, record truth,
  entitlement/licensing outcome, protected byte, dependency, payload, or
  accepted boundary condition failed.
- golden-E2E delta: **0**. The permission-complete P1 worktree passed
  **11/11**.

### 2026-08-04 · E0 — entering-state reconstruction

- owner: Codex
- runbook: `TASKS-v0.38-EXECUTION.md`
- commit: 2be2b36fb4d2fcc0ec3729772b95e4c47db0b747
- hypothesis acceptance: PASS. Every H1–H7 row carries a dated confirmed,
  refuted, partly confirmed, or deliberately-unmeasured verdict backed by its
  named entry point. H1's local graph and H4's configuration/replay claims are
  confirmed; publication superseded H1's remote state; H2/H3 counts and units,
  H6 scheduling, and H7 export/retention were corrected from measurements; H5
  remains owned exclusively by Step 2 as required.
- entering-gate acceptance: PASS. Initial porcelain named exactly the three
  historical untracked amendment inputs. Permission-complete `ci-local` passed
  **22/22** identities, including Python 3.11 **370/370**, Rust 1.78 offline,
  Rust 1.86 net success, Rust 1.85 refusal, focused SEC replay **3/3**, artifact
  verification, and golden **11/11**. A separate Python 3.12 run passed the
  identical **370/370** population with no skips.
- control acceptance: PASS. Fresh direct `invariant-scan --self-test` passes
  **15/15 rules / 84 planted controls**. R15's added-enum, removed-field, and
  changed-type mutations fail at the executing serialization control, so the
  G6 row is truthfully moved to the dated Deferred completions table. Direct
  `cycle-check` passes the disclosed Step 1 record amendment.
- domain/version acceptance: PASS. The exact **47,135-byte** v0.17.4 baseline
  covers **6 routes / 31 status-media response variants / 112 recursive field
  occurrences**. Version derivation reports **3** offline pins, **22**
  offline-floor current restatements, **3** release-version restatements, and
  all **579** tracked files classified.
- boundary acceptance: PASS. Pre-record State is **110,556 / 453,741** bytes;
  the manifest is **193,830 / 1,048,576**; and exact activation export
  **2,596,652 / 3,000,000** leaves **403,348 bytes / 13.44% / 2.81 cycles**.
  Neither trigger fired.
- protected-input acceptance: PASS. No dependency, production source,
  protected byte, fixture, observation, entitlement/licensing outcome, or
  unauthorized ref moved. The three amendment inputs remain untouched.
- stop conditions: none.
- golden-E2E delta: **0**. The final permission-complete E0 worktree passed
  **11/11**.

### 2026-08-04 · REHEARSAL-COMPLETE — lifecycle checklist and wire partition

- owner: Codex
- runbook: `TASKS-v0.38-EXECUTION.md`
- commit: 65b9a3af9d50ee33594bf44264cc1445b23e47f6
- checklist acceptance: PASS. The active runbook derives the admission clauses
  from the protected-artifact lifecycle, configured source/cadence, HC1/HC2/
  HC8/HC13, and the robots/redirect/dedup invariants. Every clause names either
  an executing fixture witness or an irreducible current-wire fact; W1 is now
  exactly that residue.
- fixture-gap acceptance: PASS. Exact pinned robots bytes run through production
  `RobotsGate` with publisher allow, publisher denial, operator composition,
  missing-policy denial, and a planted target-path denial. Exact pinned terms
  bytes require the affirmative determination, three reviewed pages,
  monitored-contact condition, and operator responsibility; a planted
  `Undetermined` mutation fails. Focused replay passes **4/4** and compliance
  passes **40/40**.
- persistence/license acceptance: PASS. The parser-produced SEC corpus measures
  **201 input / 201 kept / 0 dropped**. Finance retrieval returns a
  `PublisherPermitted` SEC hit with a snippet, a disjoint sector is empty, and
  the independent unknown-license negative remains `IndexOnly`; focused store
  identity passes **3/3**.
- operational-path acceptance: PASS. The new bounded `./run harvest-sec`
  performs artifact preflight before startup, selects and protects a fresh
  archive, requires the declared monitored contact, posts only
  `finance/sec-edgar-usgaap`, requires a nonempty `first_window`, derives
  license/integrity/fingerprint facts, consumes no fixture or observation file,
  and owns deterministic cleanup. Its structural control carries failing
  missing-preflight and wrong-source mutations; the shell harvest/config/
  scheduler group passes **14/14**, `bash -n` and `shellcheck` pass, and net
  ingest passes **29/29**.
- artifact acceptance: PASS. The changed `run` entry point is pinned at
  **50,378 bytes** and SHA-256
  `e436d59b05f060a8ce78dd3fb23282ad99fbc8bd263abd73224978c74afeeadb`.
  Artifact fixtures pass **21/21**; schema validation and two consecutive
  complete checks match **2 artifacts / 333 pinned files** at **0.09 s / 0.09
  s real**. The manifest is **194,717 / 1,048,576 bytes**.
- wire-residue acceptance: PASS. Only current robots/terms/RSS responses,
  outbound identity/request behavior, live parser consumption, fresh database
  and entitlement/license facts, and their Grant-B-bound admission remain.
  Recurrence, concurrency, 304, backfill, and a second fetch remain deferred.
  No publisher request or new observation byte occurred in this step.
- full-gate acceptance: PASS. Permission-complete `ci-local` passes **22/22**
  identities with Python 3.11 **371/371**, both Rust floors, zero rustc/clippy/
  format findings, registered scan **15/15 rules / 84 controls**, and protected
  artifacts. Permission-complete Python 3.12 passes the identical **371/371**
  population with no skips. The earlier sandboxed 3.12 attempt is a non-result:
  all eight failures were explicit loopback-bind or `ps` permission denials.
- review-boundary acceptance: PASS. Exact pre-record project-root export is
  **2,638,292 bytes / 158 files / 2 retained cycles**, leaving **361,708 bytes /
  12.06% / 2.52 cycles** below the ceiling at +143,456 bytes/cycle.
- protected-input acceptance: PASS. The three historical untracked amendment
  inputs remain untouched. No dependency, production publisher configuration,
  protected database, prior observation, schedule, unauthorized ref, or public
  response domain moved.
- stop conditions: none. The initial full-gate attempt stopped only at the
  intended pre-progress checked-box control; the workflow-valid pre-implementation
  rerun passed, the box was checked in the implementation commit above, and
  this separate append-only record supplies its commit witness.
- golden-E2E delta: **0**. The permission-complete full gate passed **11/11**.

### 2026-08-04 · WIRE-ADMISSION — SEC EDGAR live admission

- owner: Codex
- runbook: `TASKS-v0.38-EXECUTION.md`
- commit: b73413da17736f2db4db841fbdf564cb913bbcb3
- grant acceptance: PASS. The initiating request's verbatim `SEC EDGAR wire
  and admission` grant is recorded before execution and spent only on the
  three bounded evidence requests, one manual live harvest, and the
  conditional append-only admission authorized by Grant B.
- wire/DR12 acceptance: PASS. One sequential no-redirect/no-retry request each
  returned HTTP 200 for SEC robots, published access terms, and the configured
  RSS feed. Robots are byte-identical to v0.25; terms preserve every material
  condition in the affirmative determination; and the changing feed preserves
  the measured **200-item** parser-facing shape. The comparison and admission
  reports plus all four raw/metadata files are exact observation-grade pins.
- harvest acceptance: PASS. Production `./run harvest-sec` consumed the live
  configured URL, not any observation file, and reported `first_window`,
  **200 fetched / 200 new / 200 stored**, robots `Body(allow)`, a **0.500 s**
  effective delay, and deterministic shutdown. Fresh archive
  `data/live-20260803T195324Z-37051.db` is **253,952 bytes** at SHA-256
  `fb1046b79e7501d51e2dde3fd89fb7dfe0094defa6205b12afb39a21dff06044`;
  integrity is `ok`, all **200** rows are exact
  `finance/sec-edgar-usgaap/PublisherPermitted`, identity nulls and
  noncanonical rows are zero, and cursors are zero.
- entitlement/license acceptance: PASS. The actual public shell/core boundary
  returns **0** documents to science/technology-only `acme-research` and
  **200** finance documents to `quant-desk`, with zero duplicate collapses.
  The only entitlement movement is that named finance addition; no public
  route, field, serialized value domain, subscription, schedule, or source
  configuration changed.
- lifecycle acceptance: PASS. A non-retroactive initial `artifacts[]` record
  binds the fresh archive, exact wire/report hashes, and Grant B citation.
  Both artifact entry points accept **3 artifacts / 339 pins**; the manifest is
  **200,440 / 1,048,576 bytes**, and two complete verifications take **0.09 s /
  0.09 s real**. The prior two admission records and all protected bytes remain
  unchanged.
- author-contract corrections: PASS without acceptance weakening. The first
  full gate exposed `tools/audit_deferred.py` selecting every admitted archive
  for a historical two-input cosine measurement; it now selects exact
  `data/core.db` and `data/live-smoke.db`, and a planted third-record regression
  passes. The first export attempt exposed a one-RSS assumption; the exact
  Repomix registry and `tools/export_check.py` now require and exclude both
  pinned raw RSS bodies, and a missing-capture regression fails as intended.
  Both paths are disclosed in the runbook's exact declared scope.
- review-boundary acceptance: PASS. Final pre-commit project-root
  `export-check` reports **104 derived / 7 required / 163 exported / 2,766,436
  bytes / 2 retained cycles**, leaving **233,564 bytes / 7.79% / 1.63 cycles**
  below the ceiling at +143,456 bytes/cycle. Sources and evidence records
  remain included; only the two independently pinned raw RSS bodies and the
  structural archives are excluded.
- full-gate acceptance: PASS. The final permission-complete `ci-local` passes
  **22/22** identities, including Python 3.11 **373/373**, registered scan
  **15/15 rules / 84 controls**, both Rust floors and warning gates, artifact
  verification, and golden **11/11**. The independent permission-complete
  Python 3.12 lane passes the identical **373/373** population with no skips.
  The earlier 370/371 attempt and inspection-unavailable export attempt remain
  recorded findings rather than acceptance evidence.
- deferred-limit acceptance: PASS. This was one manual single-source harvest;
  recurrence, concurrency, conditional GET/304, repeated fetch, parser retry/
  redirect behavior, and backfill remain unmeasured and unclaimed.
- protected-input acceptance: PASS. The three historical untracked amendment
  inputs remain untouched and outside the implementation commit. No
  dependency, fixture, historical observation, protected database byte,
  unauthorized ref, or public response domain moved.
- stop conditions: none after the two author-contract defects were corrected
  within the acceptance criteria and disclosed scope; DR12 did not trip.
- golden-E2E delta: **0**. The final permission-complete full gate passed
  **11/11**.
