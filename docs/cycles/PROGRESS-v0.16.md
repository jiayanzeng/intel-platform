# PROGRESS-v0.16.md — append-only execution record

This file records v0.16 task and gate events after their implementation
commits exist. Each entry names the measured result, every applicable
acceptance criterion, the golden delta, and the real implementation commit.
Entries are append-only; corrections are new dated entries.

### 2026-07-28 · E0-GATE — v0.16 admitted

- owner: Codex
- commit: e8ed83c
- result: PASS for cycle activation only; E0 remains unchecked. The session
  opener measured local `main` and `origin/main` aligned at
  `0a25c50f9de6a020fa6a04b04847f6242b809f7e`, zero ahead and zero behind.
  This refuted the runbook's stale `fb2d501…` activation base; the operator
  explicitly authorized `0a25c50…` as the corrected base. Commit `0a25c50…`
  is the later append-only publication audit and does not move the published
  `v0.14.1` tag or release commit.
- worktree acceptance: PASS under the operator-approved preparation. The
  pre-existing `repomix-output.xml` ignore rule was preserved in its own
  preparatory commit `8516401`; it was not combined with cycle activation.
  The operator-supplied reviewer-lessons file remains untracked for Step 2.
- published-tag acceptance: PASS. Annotated `v0.14.1` remains tag object
  `deea217b8913ae42399a22424dcf91595ce80240`, dereferencing exactly to release
  commit `5c3b6d7fddc30b4691e1e1ee0a6e42831626a1ba`.
- activation acceptance: PASS. Implementation commit `e8ed83c` contains only
  the supplied runbook, the `AGENTS.md` v0.16 declaration, and the new
  append-only progress log.
- lifecycle acceptance: PASS. `./run cycle-check` reports active v0.16 open
  with thirteen closed execution runbooks. `./run checklist-audit` resolves
  the entering 129/129 checked tasks, reports the same three retractions, and
  finds zero exemptions. `git diff --check` passed.
- test acceptance: NOT RUN at this preparatory checkpoint; E0 owns the full
  entering matrix and F1–F6 reproduction.
- golden-E2E delta: NOT MEASURED; no claim.
- protected artifact delta: NOT MEASURED; no protected or pinned file was
  touched.

### 2026-07-28 · E0 — entering state and F1–F6 measured

- owner: Codex
- commit: 1960626
- result: PASS. Every entering claim was executed at activation-audit commit
  `90d07721f21f78cc0803facb7138141083104b8e`; F1, F2, F3, F4, and F5 were
  confirmed, while F6's location defect was confirmed with its stated file
  totals corrected from 15/11 to **17 TASKS / 12 PROGRESS**.
- entering-matrix acceptance: PASS with target provenance recorded. Ordinary
  `CARGO_TARGET_DIR=/Users/yzjia/intel-platform/target` reproduced F3 at the
  workspace-test job (**6/24 cored passed, 18 failed**). Fresh
  `CARGO_TARGET_DIR=/private/tmp/intel-v016-e0-ci-target ./run ci-local`
  passed **20/20**: **125** workspace tests, **48** net tests (**23 + 25**),
  shell **237/237** on Python 3.11.4, warning-denied offline/net builds,
  clippy, fmt, ShellCheck, Python-floor compile, locked Rust 1.78 check/test,
  invariant-scan **10/10 rules / 18/18 controls**, artifacts **2/2**, and
  golden **11/11**. A clean Python 3.12.13 rebuild resolved **21/21** exact
  packages and passed **237/237**.
- target-path finding: RECORDED. Cargo jobs in the fresh-target matrix used the
  named target, but `cmd_golden` still launched ordinary
  `target/debug/cored`; standalone ordinary-target `./run golden` rebuilt the
  current product binary and passed **11/11**. This `run`-scoped mismatch is
  assigned to Step 3's gate.
- F1 acceptance: PASS by derivation. Parsing `cmd_ci_local` produced all
  **20** targets, each reached through both an `if "$@"` condition and an
  `|| return $?` left operand, with no unparsed logical or negated job call.
  First-command failure injection made **13 fail** and **7 falsely pass**:
  `ci_deferred_evidence`, `ci_floor_compile`, `ci_shellcheck`, `ci_net_test`,
  `ci_pytest`, `cmd_golden`, and `verify_fingerprint_fixture`.
- F1b acceptance: PASS with literal answer **yes, cleanup-only**. Two failed
  validation commands followed by successful `rm -rf` returned 0 through
  `ci_local_job`; a failed cleanup returned 1. Validation failures themselves
  cannot escape the current function.
- mechanism-table acceptance: PASS on GNU Bash
  **3.2.57(1)-release (arm64-apple-darwin25)**. All eight rows matched the
  runbook: six suppressing forms continued after failure; a plain wrapper and
  a separate `bash -euo pipefail` process stopped with exit 1.
- F2 acceptance: PASS as a reproduced defect. An enrichment invocation with
  `CORE_ENTITIES=/private/tmp/v016-alt-entities.json` returned 0 but captured
  the **20** root-config names and omitted the alternate file's sole name,
  proving the shell ignores the configured core-owned path.
- F3 acceptance: PASS as a verification-only reproduction. A cored test binary
  built at `/private/tmp/intel-v016-f3-build` and run after relocation to
  `/private/tmp/intel-v016-f3-relocated`, sharing
  `/private/tmp/intel-v016-f3-shared`, was reused without compilation and
  failed **18/24** at the departed embedded path. No product path changed.
- F4/F5/F6 acceptance: PASS. Help says 19 jobs and stopping on failure despite
  the measured 20/seven result; R10 pins the defective `ci_net_test` call-site
  literal; four production tools and one shell test independently derive root
  cycle paths. The root has **17/12** cycle Markdown files and zero root
  Markdown manifest pins.
- hosted/published acceptance: PASS. The workflow contains no
  `ci_local_job`/`cmd_ci_local` path, so the local propagation defect does not
  reach hosted evidence. Standalone version, cycle, checklist, progress,
  invariant, artifact, and golden checks passed; annotated tag object
  `deea217b8913ae42399a22424dcf91595ce80240` still dereferences to
  `5c3b6d7fddc30b4691e1e1ee0a6e42831626a1ba`; **116/116** pins and **2/2**
  databases re-verified; retractions remain **three**. No retraction is owed.
- golden-E2E delta: **0**; standalone post-task result remained **11/11**.
- protected artifact delta: **0**; no protected artifact, manifest pin, release
  tag, release commit, product source, schema, or public response changed.

### 2026-07-28 · DOC-LAYOUT — cycle documents have one location

- owner: Codex
- commit: 0403fbd
- result: PASS. The pre-move retention criterion was: root holds what a reader
  consults at the start of every session; everything else lives under `docs/`.
  The tracked root now contains only those session-entry documents plus the
  declared runner/build/config files. Ignored local `.env` and `.DS_Store`
  remain untracked and were not classified as repository content.
- byte-identity acceptance: PASS. SHA-256 captured before and immediately after
  relocation matched **31/31** files: **17** task documents, **12** progress
  records, the operations guide, and the supplied reviewer-lessons document.
  Git recorded every previously tracked historical document as a 100% rename;
  only the active runbook subsequently changed for its required checkbox.
- layout acceptance: PASS. All **29** cycle documents are under `docs/cycles/`;
  the operations and reviewer-lessons documents are under `docs/`.
  `AGENTS.md`, `README.md`, R6's registry/implementation/control, and current
  architecture citations name the new paths.
- resolver acceptance: PASS. `tools/cycle_identity.py` is the only live
  `docs/cycles` location rule. Cycle, checklist, deferred-audit, and progress
  consumers import it. A derived no-fallback control leaves root files present
  and proves the canonical pair is still required; a separate control proves
  first-committed-runbook history survives both staged and committed renames.
- consumer-search acceptance: PASS. F6's four tools and cycle test were found.
  The search also found F6's omitted operations-path consumer in R6's scanner,
  registry, and test, plus `README.md`/`AGENTS.md`; all were updated. No source
  under `crates/` or `apps/`, workflow, or Repomix configuration changed.
- convention acceptance: PASS. `ARCHITECTURE.md §8` now states in one sentence
  that cycle v0.15 shipped artifact `v0.14.1`, so cycle and release identifiers
  may intentionally differ. The operator-supplied lessons are committed at
  `docs/REVIEWER-LESSONS-v0.13-v0.14.md` and cited by `AGENTS.md`.
- tool acceptance: PASS. `cycle-check` reports active v0.16 open, thirteen
  closed execution runbooks, and three historical documents. `checklist-audit`
  remains **130 checked / 130 matched / 130 resolved**, zero exemptions, and
  **three** retractions. `progress-check` resolves E0 before this append.
  Invariant scan remains **10/10 rules / 18/18 controls**.
- test acceptance: PASS. Focused cycle/invariant tests passed **37/37**; full
  shell passed **239/239** under Python 3.11.4 and 3.12.13.
- protected/pack acceptance: PASS. All **116/116** pins and **2/2** databases
  match. Repomix **1.17.0** packed **282** files, included `Cargo.lock` exactly
  once, and included both active cycle documents from `docs/cycles/`.
- golden-E2E delta: **0**; post-task `./run golden` remained **11/11**.
- protected artifact delta: **0**; no pin, protected byte, product source,
  schema, release tag, release commit, or public response changed.

### 2026-07-28 · JOB-PROPAGATION — failing jobs cannot pass

- owner: Codex
- commit: a251415
- result: PASS. `ci-local` now runs each target in a separate
  `bash -euo pipefail` process, preserves the per-job summary, and returns at
  the first failed job. The executable job table remains **20** entries and is
  the common source for runtime iteration, R10, the derived help count, and the
  failure controls.
- gate acceptance: PASS after a disclosed pre-implementation widening.
  Changing the authorization-pinned `run` required only its forward
  `config/protected-artifacts.json` pin to remain in scope. The pin moved from
  `30475367926eff8b990b70dac6d17339c4e6ec0e685aa4b01f8d01a2c328b304`
  at 41,104 bytes to
  `f62a5d4f0b8f07d48c194e2d8e3959b5bfe82a3e61a45413452a284ab4dd348d`
  at **41,862 bytes**. Every historical manifest remains unchanged.
- mechanism acceptance: PASS on GNU Bash **3.2.57**. The operator-shell rerun
  reproduced all eight table rows: the six conditional/in-process forms
  masked the internal failure, while only a plain wrapper called plainly and
  the selected separate Bash process exited 1. The selected process boundary
  survives the retained `|| return` caller context and does not share or
  replace `cmd_golden`'s `EXIT` trap.
- derived-control acceptance: PASS. One test parses the production job table
  and loops over all **20** targets. Inserting `false` as the first body command
  made every target report `FAIL` and exit non-zero; a matrix-level control
  also proved the second job is not entered after the first fails. A newly
  appended table job is therefore covered without a test-list edit.
- F1b/help acceptance: PASS. `verify_fingerprint_fixture` captures validation
  status before cleanup; its forced failure returned non-zero while still
  removing the fixture directory. Help prints the derived **20-job** count,
  and its stopping claim is now exercised and true.
- R10 acceptance: PASS. Its coupled control now mutates
  `net test (-D warnings)|ci_net_test` in the job table and fires at `run:352`.
  HEAD measures **20** local jobs / **24** local checks against **6** blocking
  hosted jobs / **23** hosted checks, with the entering **45** exemptions.
  `invariant-scan` remains **10/10 rules / 18/18 controls**.
- runner-path acceptance: PASS. All cored launchers now resolve their debug
  binary from `CARGO_TARGET_DIR`. A permitted custom-target golden launched
  `/private/tmp/intel-v016-step3-golden-target/debug/cored` and passed
  **11/11**; its preceding restricted attempt was an environment non-result
  because loopback bind was denied.
- matrix acceptance: PASS. Permitted
  `CARGO_TARGET_DIR=/private/tmp/intel-v016-step3-ci-target ./run ci-local`
  passed **20/20** with **125** workspace tests, **48** net tests (**23**
  ingest + **25** cored), Python 3.11.4 shell **241/241**, warning-denied
  builds, clippy/fmt/ShellCheck, locked Rust 1.78, and golden **11/11**.
  Python 3.12.13 independently passed **241/241** with **21/21** packages.
  The shell delta **239 → 241** is exactly the two named propagation and
  fingerprint-cleanup tests.
- protected/source acceptance: PASS. All **116/116** pins and **2/2**
  protected databases match. No `apps/`, `crates/`, workflow, public response,
  schema, dependency, lockfile, corpus, release tag, or release commit changed.
- golden-E2E delta: **0**; final post-task result remained **11/11**.

### 2026-07-28 · EXEMPT-DERIVE — exemption count is parser output

- owner: Codex
- commit: 523dc10
- result: PASS. R10's action-name and receipt-step-name enumerations are gone.
  Every exemption now records one declared structural criterion or the sole
  explicitly named environmental residual.
- criterion acceptance: PASS. The four criteria are job-level
  `continue-on-error: true`; an unconditional `uses:` action before the first
  command-bearing step; the exact constrained shell-requirements installation
  command; and membership in the terminal contiguous `always()` block that
  references `CI_RECEIPT_PATH`.
- residual acceptance: PASS. Only local `evidence-artifacts:verify` remains
  named, because protected database bytes are operator-local and its reason is
  environmental rather than a structural property of a workflow step.
- measured-count acceptance: PASS. The parser outputs **45** current
  exemptions: **18** runner setup actions + **24** receipt/attestation
  persistence steps + **1** constrained Python install + **1** report-only job
  + **1** named local residual. No test asserts 45; the test instead requires
  every output basis to resolve to a declared criterion or that residual.
- coverage acceptance: PASS. Across all blocking hosted steps, **zero**
  normalized parity checks matched an exemption, and every step with no
  normalized check matched a criterion. No prior exemption moved into
  coverage, and no check silently left coverage. Synthetic newly added setup
  and terminal receipt steps classified without an exemption-list edit.
- R10/control acceptance: PASS. HEAD remains **20** local jobs / **24** local
  checks against **6** blocking hosted jobs / **23** hosted checks.
  `invariant-scan --self-test` remains **10/10 rules / 18/18 controls**;
  focused invariant tests passed **20/20**.
- shell/golden acceptance: PASS. Full shell remained **241/241** under Python
  3.11.4 and 3.12.13, so the Step 4 shell delta is **0**. Golden remained
  **11/11**.
- protected/source acceptance: PASS. The unchanged `run` authorization pin,
  all **116/116** manifest pins, and **2/2** databases remain exact. No product
  source, workflow, schema, public response, corpus, dependency, lockfile,
  release tag, or release commit changed.

### 2026-07-28 · SEAM — gazetteer comparison is core-owned

- owner: Codex
- commit: 850d3ab
- result: PASS. The operator selected Option B. The shell still extracts and
  counts model candidates, but authenticated internal
  `POST /entities/unknown` now compares those names against the gazetteer
  loaded by core and returns only the unknown subset.
- gate acceptance: PASS with one recorded late correction. Before product
  implementation, Step 5's gate was widened to include shell enrichment/tests
  and the invariant scanner, registry, and controls needed by the repo-wide
  absence criterion. Pre-commit route-inventory review then found that the
  gate had omitted `ARCHITECTURE.md` and `README.md`, both of which enumerate
  the core contract. They were added to the gate and reconciled; the late
  scope correction is recorded in `STATE.md` rather than leaving the
  architectural authority stale.
- ownership acceptance: PASS. The production shell has no filesystem read of
  `config/entities.json`, `config/core.json`, `CORE_ENTITIES`, or
  `CORE_CONFIG`. It sends only extracted names through `CoreClient`; core
  compares case-insensitive names and aliases from its loaded `Gazetteer`.
  Core receives strings but makes no model call, so HC3 is unchanged.
- authentication/config acceptance: PASS. `/entities/unknown` refuses service
  if `CORE_TOKEN` is not configured and uses the existing header guard when it
  is. A live alternate-`CORE_ENTITIES` core returned **401** without the
  configured token. With the token it treated `Only From Env` and `Env Alias`
  as known and returned exactly
  `{"unknown":["DeepSeek","Novel Entity"]}`. This proves the route and core
  startup use the same selected gazetteer.
- fail-before/fallback acceptance: PASS. R11 reported the removed production
  read at `shell/intel_shell/pipeline.py:139` before the fix. Its registered
  control now reintroduces `open("config/entities.json")` and fails at line
  26. The pipeline test proves a comparison error returns status 1 and prints
  the error instead of substituting demo names.
- invariant/version acceptance: PASS. `invariant-scan --self-test` measures
  **11/11 rules / 19/19 controls**. The **v0.15.0** trigger fired because the
  authenticated internal route is a new observable core surface. Installed
  version bytes remain v0.14.1 pending the release commit. No `/v1/*` body
  changed. A4 remains open because config ownership is not the
  untrusted-shell public-egress boundary.
- matrix acceptance: PASS. Permitted
  `CARGO_TARGET_DIR=/private/tmp/intel-v016-step5-ci-target ./run ci-local`
  passed **20/20** with **126** workspace tests, **49** net tests (**23**
  ingest + **26** cored), Python 3.11.4 shell **243/243**, warning-denied
  builds, clippy/fmt/ShellCheck, locked Rust 1.78, and golden **11/11**.
  Python 3.12.13 independently passed **243/243** with **21/21** constrained
  packages.
- test-delta acceptance: PASS. Shell **241 → 243** is exactly R11's new
  parameterized rule case plus
  `test_pipeline_uses_core_entity_comparison_and_fails_closed`. Workspace
  **125 → 126** and net **48 → 49** are the single
  `unknown_entity_comparison_uses_the_core_loaded_gazetteer` test.
- golden/protected acceptance: PASS. The final standalone `./run golden`
  remained **11/11**. All **116/116** pins and both protected databases remain
  exact. No dependency, lockfile, corpus, public response, published tag,
  release commit, or historical evidence byte changed.

### 2026-07-28 · RELOCATABLE — fixture paths follow the runtime checkout

- owner: Codex
- commit: ca76ec4
- result: PASS. Test fixture resolution no longer embeds the checkout used to
  compile the binary; it discovers the checkout from which the tests run.
- classification acceptance: PASS. The derived Rust set was **three**
  `env!("CARGO_MANIFEST_DIR")` uses, all fixture-locating: one `cored`
  workspace-root helper and two `intel-ingest` helpers for crate-local and
  workspace-root fixtures. There were zero other uses, and the post-fix Rust
  search finds zero remaining occurrences.
- relocation acceptance: PASS. The recorded E0 fail-before built at
  `/private/tmp/intel-v016-f3-build`, moved to
  `/private/tmp/intel-v016-f3-relocated`, and reused
  `/private/tmp/intel-v016-f3-shared` without compilation; **18/24** `cored`
  tests failed at the departed embedded path. The pass-after built at
  `/private/tmp/intel-v016-step6.LX1zfx/build`, moved to
  `/private/tmp/intel-v016-step6.LX1zfx/relocated`, and reused
  `/private/tmp/intel-v016-step6.LX1zfx/shared-target`; its second cargo run
  reported `Finished` in **0.10s** without compilation and passed all
  **126/126** workspace tests.
- runtime-scope acceptance: PASS. Both resolvers walk ancestors of the current
  test directory and validate committed checkout markers. They do not derive
  paths from the executable, target directory, or build-time checkout. Every
  code change is inside a Rust `#[cfg(test)]` module, so no product runtime
  path or API changed.
- matrix acceptance: PASS. The existing, uncleared
  `CARGO_TARGET_DIR=/private/tmp/intel-v016-step5-ci-target` was reused;
  `./run ci-local` passed **20/20** with **126** workspace tests, **49** net
  tests (**23** ingest + **26** cored), Python 3.11.4 shell **243/243**,
  warning-denied builds, clippy/fmt/ShellCheck, locked Rust 1.78, and golden
  **11/11**.
- golden/source acceptance: PASS. The final standalone `./run golden` remained
  **11/11**. The Rust and shell test-count deltas are both **0**. All
  **116/116** pins and both protected databases remain exact. No product
  runtime code, dependency, lockfile, corpus, release tag, installed version,
  or historical evidence byte changed.
