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
