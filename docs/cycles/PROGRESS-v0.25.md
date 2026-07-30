# PROGRESS-v0.25.md — append-only execution record

This file records v0.25 task and gate events after their implementation
commits exist. Each entry names the measured result, every applicable
acceptance criterion, the golden delta, and the real implementation commit.
Entries are append-only; corrections are new dated entries.

### 2026-07-30 · ACTIVATE — v0.25 admitted with a valid live contract

- owner: Codex
- commit: 822aa54
- result: PASS. Before the activation commit, the supplied runbook's declared
  scope was translated from its non-executable YAML draft into the required
  Markdown table, and the manifest-retention remeasurement was assigned to
  Step 1. No task objective, gate, acceptance criterion, or permission changed.
- worktree acceptance: PASS. Before activation the only worktree item was the
  operator-supplied untracked
  `docs/cycles/TASKS-v0.25-EXECUTION.md`. Implementation commit `822aa54`
  contains only that runbook, the `AGENTS.md` v0.25 declaration, and this
  progress-log skeleton.
- entering-ref acceptance: PASS with one entering-hypothesis correction.
  Before activation, HEAD was post-push audit
  `947822c8ff85d256f20a38f1f91f5eb85326af7c` on branch
  `codex/v0.23-action-migration`, not on local `main`; local `main` remained
  `eb2d9df8b3ffd3e0380d506e958fb5a3adb2d42e`. Read-only remote inspection
  resolved `main` and peeled `v0.15.8` to closing commit
  `64002678672a601804e5f67886c73fffb4d212c8`, with annotated tag object
  `dc5abe0690e77cef671896102382427721d97321`. No ref changed.
- lifecycle acceptance: PASS. `cycle-check` reports active v0.25 open with
  twenty-two closed execution runbooks and three historical runbooks.
  `checklist-audit` passes **191 checked / 3 retracted / 191 matched / 0
  exemptions**. `progress-check` correctly reported that the new skeleton had
  no dated entry before this audit record existed.
- scope acceptance: PASS. The activation commit is the scope anchor, so its
  `activation..HEAD` diff is empty. The static release-intent rule accepts the
  complete declared release-authority set.
- test acceptance: NOT RUN at this preparatory checkpoint; E0 owns the complete
  entering matrix and drafted-gate measurements.
- golden-E2E delta: NOT MEASURED; no claim.
- protected artifact delta: NOT MEASURED; no protected or pinned file changed.

### 2026-07-30 · ACTIVATE-CORRECTION — crate-source scope made explicit

- owner: Codex
- commit: e1512ca
- result: PASS. The first clean Python 3.11 E0 shell lane executed the active
  scope control and found three release-authority/forbid overlaps rather than
  the one documented overlap. The two crate-wide forbids now name only
  `crates/ingest/src/**` and `crates/compliance/src/**`; the effective
  release-authority permission is unchanged.
- fail-before acceptance: PASS. The clean lane resolved all **21** constrained
  packages, collected **283**, passed **282**, failed the exact active-scope
  control, and skipped **0**. The failing assertion reported
  `crates/compliance/Cargo.toml`, `crates/ingest/Cargo.toml`, and
  `shell/intel_shell/app.py` instead of the required sole `app.py` overlap.
  This was a gate finding, not a passing shell measurement.
- focused acceptance: PASS. The unchanged failure-capable
  `test_current_scope_has_exactly_one_release_forbid_overlap` passes **1/1**
  after the runbook correction.
- lifecycle acceptance: PASS. `cycle-check` accepts the corrected active scope
  and its dated amendment.
- scope acceptance: PASS. Only the active runbook changed. No crate source,
  manifest, workflow, dependency, schema, protected artifact, public surface,
  configured publisher, or ref changed.
- golden-E2E delta: NOT MEASURED; no claim.

### 2026-07-30 · E0 — entering state rebuilt and six gates settled

- owner: Codex
- commit: cf092ad0209a952f55aaeb8221f82c578dbe1cfc
- result: PASS. The complete entering matrix, both clean shell lanes, every
  standalone control, G1–G6, artifact scale, published objects, and all pins
  were re-measured. The active runbook contains the command-backed record.
- entering-matrix acceptance: PASS. `./run ci-local` passed all **20** jobs:
  workspace **133**, net **55** (**29** ingest + **26** cored), warning-denied
  current and locked Rust 1.78 builds, clean clippy/fmt/ShellCheck, shell
  **283 / 283 / 0 skipped**, protected databases **2/2**, and embedded golden
  **11/11**. Standalone golden passed **11/11**. Standalone `cycle-check`,
  `checklist-audit` (**191 checked / 3 retracted / 191 matched / 0
  exemptions**), `progress-check`, `version-check`, `invariant-scan` (**12/12
  rules / 39 controls**), manifest validation, and root `export-check` (**94**
  derived / **7** required / **163** exported) passed.
- population acceptance: PASS. Clean Python **3.11.4** and **3.12.13** each
  collected **283**, passed **283**, failed **0**, and skipped **0**. The
  machine-readable comparator derived `equivalent=true` and
  `equivalent_passed=283`; its second input was the local 3.12 lane, not a
  hosted run.
- G1 acceptance: PASS. `PublicDomain` would make the unsupported
  government-work/public-domain claim, `CcBy` would invent a CC licence,
  `ClientOwned` would falsely assert subscriber ownership, and `IndexOnly`
  would be safe only by forfeiting the publisher's express reuse permission.
  No existing variant expresses publisher-granted reuse under the publisher's
  own terms.
- G2 acceptance: PASS. The executable model was enumerated as publisher
  `robots.txt` plus the operator deny-list, with no terms component. The SEC
  privacy, webmaster FAQ, and developer-resource texts were recorded by URL and
  2026-07-30 read date: the publisher disallows “unclassified” automation and
  operationally directs programmatic downloaders to declare an
  organization-and-contact User-Agent. No broader definition was inferred.
- G3 acceptance: PASS. The parser requires well-formed XML but treats every
  per-item field—`title`, `guid`, `pubDate`, `link`, `description`, and
  `author`—as optional; zero `item` elements succeeds with an empty result. No
  feed request was made.
- G4 acceptance: PASS. Public licence carriers were enumerated for
  `/v1/signals`, `/v1/search`, `/v1/ask`, and the conditional plaintext branch
  of `/v1/brief`. The standing rule does not explicitly classify a compatible
  expansion of a string enum's value domain.
- G5 acceptance: PASS after a dated runbook correction. Golden does read
  `config/core.json`, but explicitly selects only `science` and `technology`;
  the proposed source is confined to `finance`. Its measured expected outcome
  therefore remains **11/11**.
- G6 acceptance: PASS. The crawler identity derives its version from
  `CARGO_PKG_VERSION`; every net startup structurally requires a non-empty,
  non-placeholder contact before bind. Whether the contact is monitored remains
  an operator fact.
- evidence acceptance: PASS. The protected manifest remains **145,541 bytes**.
  Two consecutive `verify-artifacts` entry-point runs passed in **0.09 s** each,
  all **251** pins and both protected databases matched, and the v0.15.8
  annotated object, peeled closing commit, release parent, and live remote refs
  were re-verified.
- boundary acceptance: PASS. E0 made no publisher-origin request, no feed
  request, no working-repository ref mutation, and no change to `STATE.md`,
  `config/core.json`, production source, protected corpus, schema, or public
  surface.
- golden-E2E delta: **0**.

### 2026-07-30 · LICENSE-SEMANTICS — PublisherPermitted selects v0.16.0

- owner: Codex
- commit: ad029da80f9e5c0a463b9f0aa38eff95eb151ef2
- result: PASS. The operator selected `extend/minor`.
  `PublisherPermitted` records that a publisher expressly permits reuse under
  its own stated terms while making no claim about underlying copyright.
  `PublicDomain` remains excluded because the measured SEC evidence does not
  establish that issuer-authored filings are government works. `CcBy`,
  `ClientOwned`, and `IndexOnly` would each make a different false or
  unnecessarily restrictive claim.
- gate acceptance: PASS after a pre-implementation scope correction. The task's
  acceptance criteria required an `AGENTS.md` edit while its gate omitted that
  path; the dated amendment added the path already permitted by declared scope
  without changing the objective, implementation, or done condition. E0 had
  confirmed G1. No ingest, compliance, shell source, configured source,
  schema-breaking, or protected-database change occurred.
- version acceptance: PASS. The operator's exact symmetric public-value-domain
  criterion is now in `AGENTS.md` and reconciled in `ARCHITECTURE.md §8`.
  Adding, removing, or redefining a value of a field already serialized in a
  `/v1/*` response takes a minor release because exhaustive value handling is
  part of the consumer contract. The selected identity is **v0.16.0**
  independently of later source-admission gates.
- mapping acceptance: PASS. `PublisherPermitted`, `as_str()`, and `parse()` use
  exactly the same spelling. `redistributable()` is an exhaustive match and
  returns true for the new value. The focused core test enumerated all five
  licences and proved the existing spellings, parse outcomes, redistribution
  outcomes, and `/attest` behavior unchanged: only `IndexOnly` is
  non-redistributable and refused.
- persistence acceptance: PASS. The new store integration test round-tripped
  `PublisherPermitted`, observed the exact SQLite text, and returned a
  redistributable search snippet. SQLite's existing `license TEXT NOT NULL`
  column has no `CHECK`; writes already use `as_str()` and reads already route
  through `License::parse`. `crates/store/src/sqlite.rs` therefore required no
  edit, and that half of the conditional scope permission was unused.
- unknown-value acceptance: PASS in both directions. The actual offline `cored`
  entry point started from a temporary config containing
  `PublisherPermitted`; a temporary `FutureLicense` value exited **101** with a
  hard Serde error. A planted SQLite `FutureLicense` row silently fell back to
  `IndexOnly` and suppressed its snippet. Both directions fail safely, while
  the archive path means an older binary can silently reclassify a newer
  value.
- invariant acceptance: PASS. Step 2 produced no new invariant rule because a
  release-classification judgment is not observable by a registered source
  scan. `invariant-scan` remains exactly **12 rules / 39 controls**, recorded
  here, in `STATE.md`, and in the active runbook; no R12 mutation was added.
- complete-matrix acceptance: PASS. `./run ci-local` passed all **20** jobs:
  workspace **135**, net **55** (**29** ingest + **26** cored),
  warning-denied current and locked Rust 1.78 lanes, clean
  clippy/fmt/ShellCheck, Python 3.11 **283 collected / 283 passed / 0 skipped**,
  protected databases **2/2**, all **251** pins, and embedded golden **11/11**.
  Independent Python 3.12 passed **283 collected / 283 passed / 0 skipped**.
  `cycle-check`, formatting, and diff hygiene passed.
- release-boundary acceptance: PASS. `config/core.json` is unchanged, so zero
  configured sources produce the value and no `/v1/*` response can yet carry
  it. `README.md`'s now-stale four-value enumeration is explicitly assigned to
  Step 7, whose gate contains that release authority. Live remote inspection
  found no v0.16.0 tag and left the pre-existing
  `candidate/v0.16.0` branch at the v0.15.1 evidence commit
  `3481e4ba85d65c927b7d0fc3a430bc04fb094394`; its seven immutable receipt
  provenance entries plus pinned report remain disambiguated as eight
  historical evidence subjects. No publisher/feed request or ref mutation
  occurred.
- runbook-correction acceptance: PASS. The false author-side G5 implication was
  recorded as a runbook error: golden uses only `science` and `technology`, so
  a future `finance` source does not enter it.
- golden-E2E delta: **0**; mandatory standalone `./run golden` passed
  **11/11**.
