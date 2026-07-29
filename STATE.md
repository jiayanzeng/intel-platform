# STATE.md — intel-platform handoff

**As of:** 2026-07-29 · **Version:** v0.15.4 (core-shell) · **Status:** **v0.21 MATCH-PROOF is complete and v0.15.4 remains published.** Remote release `v0.15.4` has annotated tag object `7a5c9f7396c043f2b89974585fdd4e5146180e86` and release commit `8c1eff03ff3e67b18176e8bf533de0f9501e0257`; exact evidence candidate `8230d4f24f565afcde92931c987adff4339036af` remains separate on `candidate/v0.15.4`. Release-commit `./run ci-local` passed **20/20** with **133** workspace tests, **55** net tests (**29** `intel-ingest` + **26** `cored`), locked Rust 1.78, shell **255/255** on Python 3.11.4 and independently rebuilt Python 3.12.13. The current `invariant-scan` passes **12/12 rules / 30 controls**; R10 retains **45** exemptions, all **191/191** pins (**189/189** evidence + **2/2** authorization) remain exact, protected databases remain **2/2**, and golden remains **11/11**. Push-triggered hosted run `30425601829` passed all **7** executable jobs at the exact release commit; the report-only dependency-drift job was skipped as designed. The protected corpus and three retractions remain unchanged. A4, the editable-L1 controller residual, the R3/R4 bounded open-bottom deny-lists, the active-runbook measured-value heuristic, T7 robots single-flight, the explicitly deferred last-known-good robots fallback, and the one-real-publisher product limitation remain open; L2 remains scheduled.

**v0.21 MATCH-PROOF removes the vacuous publication-rule class (measured
2026-07-29).** The corrected total requirement was first run against the
unchanged entering header and exited **1** with exactly:
`STATE.md: publication assertion required: status header must assert the
annotated tag object in the required unambiguous phrasing`. Only then was the
header rewritten to assert both immutable refs in the narrow grammar.
`STATE_REF_ASSERTIONS` still excludes intervening backticks: widening that
class was explicitly rejected because an unrelated intervening hash could
satisfy the rule and recreate the same silent gap at the next rephrasing.

Registered R12 drives the actual `check_publication_status` entry point through
nine planted cases: mutable `origin/main`, missing and stale tag-object
assertions, missing and stale target assertions, pending publication, missing
annotated-tag ref, missing peeled target, and unavailable ancestry. Seven
independent fail-before mutations disable each rule family and are all
detected. The complete scanner therefore passes **12/12 registered rules / 30
controls**, up from **11/11 / 23**. The `origin/main` prohibition and
pending-publication rule 1 retain their conditions and error behavior; their
R12 mutations prove each still fails closed.

Focused `cycle_check` plus `invariant_scan` tests pass **47/47** on Python
3.11.4 and independently on Python 3.12.13. `cycle-check` passes with the
rewritten header. The first restricted golden attempt was a loopback-bind
permission non-result; the identical permitted invocation passed **11/11**,
delta **0**. No crate, app, dependency, schema, protected artifact, robots
surface, configured source, or public response changed.

**v0.20 R-CLOSE publishes v0.15.4 and closes the cycle (measured
2026-07-29).** Release disposition: release (as of 2026-07-29). The release
identity is v0.15.4 because no `/v1/*` route or response body, schema,
dependency, crate source, or runtime behavior changed. The independent
publication trigger fired because published `main` was failing CI on the
status control this cycle corrects. A tooling-only cycle could otherwise
legitimately close without a release, as v0.14 did; the red published head made
that disposition false here.

G1 was a specification defect in the v0.19 runbook, not an implementation
defect in `tools/cycle_check.py`. The runbook required freshness for a mutable
ref whose value the act of recording changes, and the implementation followed
that requirement faithfully. Adding the control was correct: before exposing
its own fixed point, it caught a real false publication status. The repaired
rule structurally prohibits a literal mutable-ref hash in the live header,
keeps immutable annotated-tag object and peeled-target reconciliation, and
fails closed when a ref or ancestry input is unavailable. Retractions remain
three.

Forward publication audit
`72b6f425114e06b1e148e0aa360e280a690e4f0c`, intentionally held after
v0.15.3, landed in this cycle's publication history rather than through an
out-of-band push. Evidence candidate
`8230d4f24f565afcde92931c987adff4339036af` and release commit
`8c1eff03ff3e67b18176e8bf533de0f9501e0257` are separate named subjects.
Atomic publication created annotated tag object
`7a5c9f7396c043f2b89974585fdd4e5146180e86`, whose peeled target is the
release commit. The dated remote readback measured `refs/heads/main` at
`8c1eff03ff3e67b18176e8bf533de0f9501e0257`,
`refs/heads/candidate/v0.15.4` at
`8230d4f24f565afcde92931c987adff4339036af`, and the same tag object and
target.

The exact release-commit definition of done passed:

- clean constrained Python environments resolved the same **21** pinned
  packages on Python 3.11.4 and 3.12.13; shell tests passed **255/255** on
  each;
- `./run ci-local` passed **20/20** with **133** workspace tests, **55** net
  tests (**29 + 26**), locked Rust 1.78, zero
  rustc/clippy/fmt/ShellCheck failures, `invariant-scan` **11/11 rules / 23
  controls**, R10 **45** exemptions, all **191/191** pins, protected
  databases **2/2**, and its embedded golden **11/11**;
- authenticated release re-derivation passed **7** rows, **5** source
  dispositions, and **7** triggers with release grade and attestations
  required; `export-check` passed **90/90** derived sources, **7/7** required
  paths, and **147** exported paths;
- the mandatory standalone golden passed **11/11**, delta **0**; manifest
  schema v2, `verify-artifacts`, `evidence-report`, version/cycle/checklist/
  progress status, and `git diff --check` passed.

The first concurrent attempt to clear the parent `.venv` while building its
nested Python 3.12 environment was a setup non-result; the environments were
then rebuilt sequentially. Restricted package installs and the root export
were DNS-permission non-results, restricted `ci-local` was a loopback-bind
permission non-result, and restricted online Sigstore re-derivation was a
network non-result. Each identical permitted retry produced the passing
measurements above.

The release commit and annotated tag were atomically published. Push-triggered
hosted run `30425601829` at exact head
`8c1eff03ff3e67b18176e8bf533de0f9501e0257` completed successfully: core,
clippy/fmt, net, Rust 1.78, shell Python 3.11, shell Python 3.12, and golden
were all green; the report-only dependency-drift job was skipped by its
declared trigger. This green published-head run is the cycle's product.

The release diff from annotated v0.15.3 contains exactly **35 paths**, each
classified once in the immediately following preparatory record. A4, the
editable-L1 controller residual, R3/R4's bounded open-bottom limits, the
active-runbook measured-value heuristic, T7 robots single-flight, Decision
B's last-known-good fallback, and the one-real-publisher limitation remain
open; L2 remains scheduled. `arxiv-cs` is still the sole real publisher, the
other three configured sources remain `example.org` fixtures, and adding a
second publisher remains a separate compliance decision.

**v0.20 R-CLOSE publication is authorized and release reconciliation is
prepared (measured 2026-07-29).** Release disposition: release (as of
2026-07-29). The release version is v0.15.4. The mechanical patch default
classifies the identity because no `/v1/*` route or response body, schema,
dependency, crate source, or runtime behavior changed.

The publication trigger is separate and explicit: published `main` is failing
CI on the status control this cycle corrects. A tooling-only cycle would
otherwise be eligible for a no-release disposition, as v0.14 was; this cycle is
not, because publishing the correction is what turns the public repository's
required CI green.

G1 was a specification defect in the v0.19 runbook, not an implementation
defect in `tools/cycle_check.py`. The runbook required a header freshness rule
for a mutable ref whose value the act of recording changes, and the tool
implemented that requirement faithfully. Adding the control was still correct:
it first caught the repository's real false remote-main/tag status before its
own fixed point appeared. The repaired control removes the impossible literal
from the live header, retains immutable tag-object and peeled-target freshness,
and fails closed for missing refs or unavailable ancestry. Retractions remain
three.

Forward publication audit `72b6f425114e06b1e148e0aa360e280a690e4f0c`
was intentionally held unpushed after v0.15.3. It is present in this release's
history and will land in this cycle's authorized publication rather than as an
out-of-band push.

The intended release diff from annotated v0.15.3 contains exactly **35 paths**,
classified once each:

- **Publication-status control (2):** `tools/cycle_check.py` and
  `shell/tests/test_cycle_check.py`.
- **Review-export control (4):** `repomix.config.json`, `run`,
  `tools/export_check.py`, and `shell/tests/test_export_check.py`.
- **Operating and architecture contract (2):** `AGENTS.md` and
  `ARCHITECTURE.md`.
- **Version authorities (4):** `Cargo.lock`, `apps/cored/Cargo.toml`,
  `shell/intel_shell/__init__.py`, and `shell/intel_shell/app.py`.
- **Release documentation and status (3):** `README.md`, `CHANGELOG.md`, and
  `STATE.md`.
- **Cycle records (4):** `docs/cycles/PROGRESS-v0.19.md`,
  `docs/cycles/PROGRESS-v0.20.md`,
  `docs/cycles/TASKS-v0.19-EXECUTION.md`, and
  `docs/cycles/TASKS-v0.20-EXECUTION.md`.
- **Protected admission manifest (1):**
  `config/protected-artifacts.json`.
- **Authenticated evidence (15):** the seven JSON receipts and seven
  `.sigstore` bundles under `evidence/ci-runs/30423736121-1/`, plus
  `evidence/v0.15.4/deferred-audit/report.json`.

Evidence candidate `8230d4f24f565afcde92931c987adff4339036af`
on `candidate/v0.15.4` and the release commit are separate named subjects. The
release commit remains to be created and measured. A4, the editable-L1
controller residual, R3/R4's bounded open-bottom limits, the active-runbook
measured-value heuristic, T7 robots single-flight, Decision B's
last-known-good fallback, and the one-real-publisher limitation remain open;
L2 remains scheduled. `arxiv-cs` is still the sole real publisher, the other
three configured sources remain `example.org` fixtures, and adding a second
publisher remains a separate compliance decision.

**v0.20 RE-MEASURE admits authenticated release-grade candidate evidence
(measured 2026-07-29).** The operator authorized exactly the Step 6 Gate:
push exact candidate
`8230d4f24f565afcde92931c987adff4339036af` to
`candidate/v0.15.4` and dispatch authenticated hosted evidence. The patch
identity follows the runbook's mechanical default because no `/v1/*` route or
body and no crate changed. This did not authorize a tag, a `main` advance, or
release publication.

Before dispatch, the candidate's remote `.github/workflows/ci.yml` was read
through the GitHub contents and raw endpoints. Remote blob
`96e85af978981b7af9bdd8e9e11069f158f35e57` equals the local blob and contains
the expected core, lint, net, MSRV, two-shell, golden, cycle/checklist,
invariant/progress, receipt-signing, and artifact-upload invocations.
Workflow-dispatch run `30423736121` attempt **1** succeeded at the exact
candidate. Its six blocking jobs were green.

Every test count was read from hosted logs and reconciled with the permitted
local matrix at that same commit. Local `./run ci-local` passed **20/20** with
**133** workspace tests, **55** net tests (**29 + 26**), shell **255/255** on
Python 3.11.4, zero rustc/clippy/fmt/ShellCheck failures, locked Rust 1.78,
`invariant-scan` **11/11 rules / 23 controls**, R10 **45** exemptions, and
golden **11/11**; constrained Python 3.12.13 independently passed shell
**255/255**. Hosted logs report the same **133**, **55**, **11/11 / 23**,
**45**, and **11/11** counts. Each hosted shell lane collected the same
**255** tests as **254 passed + 1 declared on-site-only protected-corpus
skip**. The hosted Python versions were 3.11.15 and 3.12.13, and each resolved
the exact **21-package** constraint set.

The cycle's corrected control passed where required: hosted
`shell (Python 3.11)`, step `active cycle and amendment consistency`, checked
out full history with `fetch-depth: 0` and reported `cycle-check: PASS` with
active v0.20 open, 17 closed execution runbooks, three historical runbooks,
and no requested local tag refs. The same job also reported checklist
**163 checked / 3 retracted / 163 matched / 0 exemptions** and the prior
progress head `EXPORT-CONTRACT` at `15b7d48`.

All **7/7** workflow-derived identities — core, golden, lint, MSRV, net, and
shell Python 3.11/3.12 — are successful Linux receipts from run
`30423736121` attempt 1. Every persisted Sigstore bundle verifies its receipt
bytes, repository `jiayanzeng/intel-platform`, workflow signer, exact source
digest, source ref `refs/heads/candidate/v0.15.4`, and GitHub-hosted runner
identity; zero receipts were rejected and the single-run matrix is complete.

The first detached audit attempt was a non-result: the clean detached subject
did not contain the intentionally untracked protected databases and raised
`FileNotFoundError` before producing a report. A clean retry exposed the two
read-only protected database bytes to that detached worktree with ignored
symlinks under `/private/tmp`; both hashes matched the manifest and detached
`git status` remained clean. The release-posture, attestations-required audit
then passed **5 deferred / 2 promoted / 0** deferred subsystems implemented.
Exact-cosine p95 at the largest **2,600-document** archive was
**8.958167 ms**, below the **16.264 ms** A3 request anchor. Report
`evidence/v0.15.4/deferred-audit/report.json` is **34,608 bytes** at SHA-256
`b90b2f00d8129f17c09e48e2bdefb2d48d97f5d502e2723b8a5e2d0a5d25d00e`.

The **15** new admissions bring the schema-v2 manifest to **191/191** pins —
**189/189** evidence plus **2/2** authorization surfaces.
`evidence_artifacts.py validate`, `verify-artifacts`, and `evidence-report`
pass; protected databases remain exact **2/2**. A later restricted repeat of
each local shell lane was a loopback/process-inspection permission non-result;
the permitted identical retries passed **255/255** on both interpreters.
Remote reinspection confirms `origin/main` remains
`692069ead0b8823d6874d8f2fc0a593d9f26704f`, the candidate remains exact, and
no `v0.15.4` tag exists. The first final sandboxed golden invocation was a
loopback-bind permission non-result; the identical permitted invocation passed
**11/11**, delta **0**.

**v0.20 EXPORT-CONTRACT records the measured review-export operating rules
(measured 2026-07-29).** `AGENTS.md` now requires every Repomix review export
to be written from the project root because the Step 4 non-root control
silently lost `Cargo.lock`. It also requires `enableSecurityCheck` to stay
`false`: the triggering measurement was **340 files collected, 339 included**,
with `crates/ingest/src/lib.rs` silently omitted, while registered self-testing
invariant R4 is the repository's credential control. Both rules point at
`./run export-check`.

These are operating rules, not new hard constraints; the HC series is
unchanged. `ARCHITECTURE.md` replaces its now-false v0.20 opener paragraph
with the current boundary: the check is an operator-local contract, derives
its set without pinning a count, and is intentionally outside local/hosted CI
because it writes a multi-megabyte export and `npx` may fetch Repomix.
`./run export-check` passes with **90/90** derived sources, **7/7** required
paths, and **147** exported paths. `checklist-audit`, `cycle-check`, and
`git diff --check` pass. Mandatory standalone golden remains **11/11**, delta
**0**. No tool, crate, configuration, dependency, protected artifact,
database, or public surface changed.

**v0.20 EXPORT-CHECK makes review-export source completeness executable
(measured 2026-07-29).** `./run export-check` writes a fresh project-root
export with pinned Repomix 1.17.0, derives the expected tracked source set from
`git ls-files` under `crates/`, `apps/`, `tools/`, and `shell/`, and requires
the seven root/control paths named by the runbook. It pins no count. At the
task candidate it found all **90/90** derived source paths and all **7/7**
required paths in a **147-file** export.

Both known silent-omission controls fail loudly. A disposable invocation from
`crates/` exited **1**, named missing required path `Cargo.lock`, and reported
**95** total missing paths. A project-root invocation using a disposable
configuration with only `enableSecurityCheck` restored to `true` made Repomix
exclude exactly `crates/ingest/src/lib.rs`; the checker exited **1** and named
that missing derived source. The real configuration was never changed:
`repomix.config.json` remained SHA-256
`0470cb2ba232a549e94a95ece5e337f025cde2fb17cd37a330af6a3d5e35b2ee`
and `git diff --exit-code -- repomix.config.json` passed afterward.

This is explicitly an **operator-local** check. It is intentionally absent
from `ci-local` and `.github/workflows/ci.yml` because each invocation writes
a multi-megabyte export and `npx` may fetch the pinned tool. The first final
sandboxed invocation was therefore a DNS-permission non-result; the permitted
identical retry passed with the counts above.

The `run` authorization pin moves from
`caae4e8007fc885241bf1ac7c844e397a149970048e036be285e356449030678`
at **42,056 bytes** to
`0fc7f0be0ea2d8c68ff63be55dd0b73cc1385ce966b8307506a5387543f18779`
at **43,044 bytes**. The model-profile functions and dispatch, mirrored
authorization policy, and `tools/model_profiles.py` pin
`1920761c97ffa6fc7b5242c16384fb6f1b0727937f9e1cfd7e00826c913554df`
at **28,297 bytes** are unchanged; R6 passes. A pre-final placement briefly
shifted R10's line-addressed mutation and made that self-test fail; relocating
the new function after `cmd_verify_llm` restored the original line and the
final `invariant-scan` passes **11/11 rules / 23 controls**.

Focused export-check tests pass **3/3**. The full permitted local matrix passes
**20/20** with **133** workspace tests, **55** net tests (**29 + 26**), shell
**255/255** on Python 3.11.4, zero rustc/clippy/fmt/ShellCheck failures,
locked Rust 1.78, all **176/176** pins, protected databases **2/2**, and
golden **11/11**. Python 3.12.13 independently passes shell **255/255**; its
first restricted attempt was a loopback/process-inspection permission
non-result, and the permitted identical retry passed. Manifest validation and
`verify-artifacts` are green. Standalone golden remains **11/11**, delta
**0**. No crate, dependency, schema, protected database, evidence artifact,
or public surface changed.

**v0.20 EXPORT-PATTERN makes the closed-cycle exclusion complete (measured
2026-07-29).** The former enumerated `v0.{8,9,10,11}*` pattern is replaced by
the bounded range rule
`v0.{[6-9],1[01]}{.md,.*.md,-*.md}` for `TASKS` and `PROGRESS`. Its numeric
classes express v0.6 through v0.11, while the suffix alternatives preserve the
base, point-cycle, and execution-runbook filename forms without spilling into
v0.12.

Pinned Repomix 1.17.0 ran from the project root immediately before and after
the one-line configuration change. The export moved from **147 files /
2,735,717 characters / 2,740,883 serialized bytes** to **145 files /
2,704,779 characters / 2,709,638 serialized bytes**. The complete path-set
diff removes exactly `docs/cycles/TASKS-v0.6.md` and
`docs/cycles/TASKS-v0.7.md`; every **18/18** task/progress files from v0.12
through active v0.20 remain, and no non-`docs/cycles/` inclusion changes.
Neither source file was deleted. `verify-artifacts` passes all **176/176**
pins and both protected databases **2/2**; standalone golden remains
**11/11**, delta **0**.

**v0.20 SELF-REF corrects the publication fixed-point defect (measured
2026-07-29).** The mutable measurement remains a dated fact in this body:
local `origin/main` and remote `main` were both
`692069ead0b8823d6874d8f2fc0a593d9f26704f` at E0. It is deliberately not an
immutable assertion in the live status header.

The repaired entry-point checker first ran against the unchanged header and
failed with exactly one defect:

> `STATE.md: publication status header must not assert a literal origin/main hash; publishing the asserting commit moves that ref, so record mutable-ref measurements in a dated body append`

The live header may assert only the immutable annotated-tag object and peeled
release target. The checker independently resolves both, verifies their
agreement with the newest closed release record, and requires the recorded
target to be reachable from `HEAD` before evaluating the existing
pending-publication rule. Missing tag, missing peeled target, and unavailable
ancestry each produce a named fail-closed diagnostic instead of silently
skipping the check. Focused tests pass **24/24**, including a live-header
origin literal that fires the structural refusal, both immutable freshness
failures, all three unavailable-input paths, the unchanged pending-versus-
published rule, and a passing header whose dated body retains a stale
historical branch measurement.

The full permitted local matrix passes **20/20** after the change: **133**
workspace tests, **55** net tests (**29** `intel-ingest` + **26** `cored`),
shell **252/252** on Python 3.11.4, zero rustc/clippy/fmt/ShellCheck failures,
locked Rust 1.78, `invariant-scan` unchanged at **11/11 rules / 23 controls**,
all **176/176** pins, protected databases **2/2**, and golden **11/11**.
Python 3.12.13 independently passes the exact **21-package** constraint check
and shell **252/252**. Standalone golden is **11/11**, delta **0**.
`cycle-check`, `checklist-audit`, `progress-check`, `version-check`,
`invariant-scan`, manifest validation, and `verify-artifacts` are green. No
crate, dependency, schema, protected artifact, public surface, closed runbook,
or historical append changed.

**v0.19 post-publication audit records a tripped status-control gate (measured
2026-07-29).** The authorized atomic push succeeded: remote main is exact at
closing audit `692069ead0b8823d6874d8f2fc0a593d9f26704f`; annotated
`v0.15.3` is object `2039e01475b43285ecbbf2739f788b7f855a5603`,
peeled to release commit `dbff27d559193847dd2028c435c686ba656dac85`.

Exact-head [publication CI run 30417274925 attempt
1](https://github.com/jiayanzeng/intel-platform/actions/runs/30417274925)
was event `push`, created 2026-07-29T02:36:08Z, completed
2026-07-29T02:36:58Z, and concluded **failure**. Golden, clippy/fmt, core,
Rust 1.78 MSRV, net, and Python 3.12 job instances all succeeded. Python 3.11
passed version consistency, then stopped at the active-cycle step with the
exact executable finding:

> `STATE.md: publication assertion freshness: origin/main asserts 344124819cb3c554f851d0cac3f0f1ed08d1aa10, but the measured ref is 692069ead0b8823d6874d8f2fc0a593d9f26704f`

The cause is the new STATUS-TRUE control's same-commit self-reference. The
closing audit can truthfully record only the remote main measured before its
atomic push; once that immutable commit becomes remote main, the hosted
checker compares it with the newly advanced ref. Re-running the same commit
cannot change either operand, and pushing a forward status commit would move
remote main again. Therefore the gate is not silenced or retried. v0.20 must
make publication freshness executable across the pre-publication and
post-publication states, with a failure-capable control for both, before
another release.

The published artifact's exact local matrix and candidate-hosted release
evidence remain valid measurements, but they are not relabeled as a passing
publication run. Python 3.11 steps after `cycle-check` were skipped in that
run. No release object was rolled back, no closed runbook or closing record
was edited, and the three operator-identified export omissions remain open
alongside this newly observed fourth v0.20 finding.

**v0.19 R-CLOSE is locally complete (measured 2026-07-29).** Release
disposition: release (as of
2026-07-29). The operator selected v0.15.3 because Step 4 changed production
behavior received by a consumer of the artifact: `cached()` now selects TTL by
exhaustive policy variant and `cored` wires `ROBOTS_NEGATIVE_TTL` at **300
seconds**. The runbook's mechanical patch default classifies the compatible
identity; it is not the trigger.

G1 was a bounded fail-closed availability defect. While an origin was
unreachable, the system denied access and never permitted a request the
publisher had refused; the defect discarded a good policy and could preserve
one transient denial for a full day. The correction deliberately makes a
failing origin eligible for another `/robots.txt` request at most once per
**300 seconds** instead of once per **24 hours**, bounded by ingest frequency
and the shared politeness limiter that `policy_for` already acquires. That
trade is correct because a 24-hour denial caused by one dropped packet was
arbitrary rather than conservative. It is neither a compliance violation nor
cosmetic. `Unreachable` still denies while cached and still overwrites an
expired last-known-good policy; Decision B remains deferred under its recorded
live-outage and operator-authorization trigger.

The release also removes the unsupported `diagnostics` and `robots-preview`
Cargo features and preview binary that shipped in v0.15.2. A consumer that
selected either feature must remove it. No `/v1/*` name, response shape, or
schema changed, so the production correctness fix and explicit unsupported
feature retirement remain compatible with the patch identity.

Step 2 changed the project's own epistemics: before v0.19, a false assertion
about `origin/main` and the published tag passed every check the project ran.
The new `cycle-check` reconciliation first failed against that known-false
status, then passed only after a forward status audit recorded the measured
refs and exact hosted publication run.

The export budget remains materially smaller but its control is incomplete.
The comparable Repomix summary moved from **4,887,220 characters / 339 files**
at E0 to **2,640,795 characters / 146 files** at EXPORT-BUDGET. At clean
pre-release audit commit `1fad40f`, root-run Repomix 1.17.0 reports
**2,658,161 characters / 145 files**; the serialized XML is **2,663,093
bytes**. This forward record corrects the earlier use of “bytes” for
Repomix's `Total Chars` metric. The export retains `Cargo.lock`,
`config/protected-artifacts.json`, `AGENTS.md`, `run`,
`.github/workflows/ci.yml`, all four fixtures named by `config/core.json`, and
all **88/88** tracked files under `crates/`, `apps/`, `tools/`, and `shell/`.
The moved historical state remains at
`docs/state-archive/STATE-through-v0.13.md`.

Three omissions are the v0.20 opener and are not repaired inside R-CLOSE's
Gate:

1. The configured “closed cycles through v0.11” exclusion names only v0.8
   through v0.11. `docs/cycles/TASKS-v0.6.md` and
   `docs/cycles/TASKS-v0.7.md` remain exported and currently total **31,147
   bytes**.
2. Nothing executes the export budget. The required `export-check` must derive
   the expected set from `git ls-files`, not pin a count; the current derived
   source set is **88**, after preview retirement reduced the former **89**.
3. `AGENTS.md` does not yet require Repomix to run from the project root or
   preserve why `enableSecurityCheck` must stay off after it silently omitted
   a Rust source.

The intended release diff from annotated v0.15.2 contains exactly **39 paths**,
classified once each:

- **Production cache behavior (2):** `apps/cored/src/main.rs` and
  `crates/compliance/src/lib.rs`.
- **Unsupported feature retirement (4):**
  `crates/compliance/Cargo.toml`, `crates/ingest/Cargo.toml`,
  `crates/ingest/src/bin/robots_preview.rs`, and
  `crates/ingest/src/net.rs`.
- **Version authorities (4):** `Cargo.lock`, `apps/cored/Cargo.toml`,
  `shell/intel_shell/__init__.py`, and `shell/intel_shell/app.py`.
- **Executable lifecycle/export/status controls (4):** `AGENTS.md`,
  `repomix.config.json`, `tools/cycle_check.py`, and
  `shell/tests/test_cycle_check.py`.
- **Architecture, status, and release documentation (4):**
  `ARCHITECTURE.md`, `STATE.md`, `README.md`, and `CHANGELOG.md`.
- **Cycle records (4):** `docs/cycles/PROGRESS-v0.18.md`,
  `docs/cycles/PROGRESS-v0.19.md`,
  `docs/cycles/TASKS-v0.18-EXECUTION.md`, and
  `docs/cycles/TASKS-v0.19-EXECUTION.md`.
- **Lossless state archive (1):**
  `docs/state-archive/STATE-through-v0.13.md`.
- **Protected admission manifest (1):**
  `config/protected-artifacts.json`.
- **Authenticated evidence (15):** the seven JSON receipts and seven
  `.sigstore` bundles under `evidence/ci-runs/30414648482-1/`, plus
  `evidence/v0.15.3/deferred-audit/report.json`.

The exact clean release commit is
`dbff27d559193847dd2028c435c686ba656dac85`. `./run ci-local` passes
**20/20** with **133** workspace tests, **55** net tests (**29 + 26**),
warning-denied current and Rust 1.78 builds/tests, clippy, rustfmt, ShellCheck,
Python 3.11.4 shell **248/248**, `invariant-scan` **11/11 rules / 23
controls**, **176/176** pins, protected databases **2/2**, and golden
**11/11**. The first sandboxed invocation was a loopback-bind non-result; the
identical permitted invocation passed. A clean constrained Python 3.12.13
rebuild resolved **21/21** packages and independently passed shell
**248/248**. Supplemental all-features suites pass **40/40**
`intel-compliance` and **29/29** `intel-ingest`; the former `diagnostics` and
`robots-preview` feature commands each exit **101** with Cargo's
`does not contain this feature`. The mandatory standalone golden passes
**11/11**, delta **0**. Release-posture evidence re-derivation authenticates
all **7** rows with **5** source dispositions and **7** triggers.

At that release commit, root-run Repomix 1.17.0 reports **2,669,764
characters / 145 files**; the serialized XML is **2,674,706 bytes**. All
**88/88** derived source paths and every named release-critical file and
fixture are present. The two missed historical task files remain present as
the recorded v0.20 finding.

Evidence candidate
`197e93effe9a6abf9c59488a9849c6dcda47646c` on
`candidate/v0.15.3` and the release commit are separate named subjects. The
local annotated tag object
`2039e01475b43285ecbbf2739f788b7f855a5603` peels exactly to the release
commit. Before local tag creation, read-only remote inspection found
`origin/main` at `344124819cb3c554f851d0cac3f0f1ed08d1aa10`, candidate exact,
and no remote `v0.15.3` tag. The closing audit commit and tag are authorized
for one atomic push. A4, the editable-L1 controller residual, R3/R4's bounded
open-bottom limits, the active-runbook measured-value heuristic, T7 robots
single-flight, Decision B's last-known-good fallback, the three export-control
omissions above, and the one-real-publisher limitation remain open; L2 remains
scheduled. Three of four configured sources are still `example.org`
placeholders, and a second publisher remains a separate compliance decision.

**v0.19 RE-MEASURE is complete at the v0.15.3 candidate (measured
2026-07-29).** Step 4's negative-cache correctness change is the version
trigger: a transient unreachable result previously occupied the successful
policy's full-day cache and discarded a good policy. That was a bounded
fail-closed availability defect, so the compatible release identity is
v0.15.3. The clean evidence candidate is
`197e93effe9a6abf9c59488a9849c6dcda47646c` on
`candidate/v0.15.3`; release publication and the final release commit remain
the Step 7 operator decision.

Before dispatch, the remote candidate workflow was read through GitHub and
confirmed to contain the expected core, lint, net, MSRV, two-shell, golden,
receipt-signing, and artifact-upload invocations. Its remote Git blob
`96e85af978981b7af9bdd8e9e11069f158f35e57` equals the local workflow blob.
Exact-candidate local `./run ci-local` passed **20/20** with **133** workspace
tests, **55** net tests (**29 + 26**), shell **248/248** under Python 3.11.4,
locked Rust 1.78, zero rustc/clippy/fmt/ShellCheck failures,
`invariant-scan` **11/11 rules / 23 controls**, R10's **45** derived
exemptions, protected databases **2/2**, and golden **11/11**. The constrained
Python 3.12.13 lane independently resolved **21/21** packages and passed
**248/248**.

Authenticated workflow-dispatch
[run 30414648482 attempt 1](https://github.com/jiayanzeng/intel-platform/actions/runs/30414648482)
completed successfully at that same candidate. Every count was read from the
hosted logs rather than inferred from job status: core and MSRV each report
**133** workspace tests; net reports **55** tests (**29 + 26**); both shell
lanes collected **248** tests as **247 passed + 1 declared on-site-only
skip**; the Python 3.11 lane reports `invariant-scan` **11/11 rules / 23
controls** and R10's **45** exemptions; both constrained interpreters resolved
**21/21** packages; and golden reports **11/11**. The hosted collection counts
therefore equal the local same-commit counts exactly. The only result-shape
difference is the declared hosted skip for the protected corpus that is absent
from hosted runners.

All **7/7** workflow-derived identities across the **6** blocking jobs have
successful Linux receipts and persisted Sigstore bundles; zero receipts were
rejected. Release-posture `audit-deferred` authenticated every bundle against
repository `jiayanzeng/intel-platform`, the CI workflow signer, source digest
`197e93effe9a6abf9c59488a9849c6dcda47646c`, and source ref
`refs/heads/candidate/v0.15.3`. Network-enabled re-derivation passes all
**7** rows with release grade and attestations required. The report records
**5 deferred / 2 promoted / 0 deferred subsystems implemented**. The largest
evidenced archive remains **2,600** documents; exact-cosine p95 measured
**6.786459 ms**, below the recorded **16.264 ms** A3 request anchor.

The admitted audit report is
`evidence/v0.15.3/deferred-audit/report.json`, SHA-256
`3006f9ed8641cbc6483a2a1608c65da52ff008e59837218997f207a7cf588b2e`,
**34,530** bytes. Its seven receipts, seven bundles, and one report add
**15** records, bringing the protected manifest to **176/176** pins:
**174/174** evidence plus **2/2** authorization surfaces. Manifest schema v2
validation, `./run verify-artifacts`, and `./run evidence-report` pass; both
protected databases remain byte-exact. Remote reinspection found
`origin/main` unchanged at
`344124819cb3c554f851d0cac3f0f1ed08d1aa10`, the candidate branch exact, and
no `v0.15.3` tag. No publication, product path, public surface, dependency,
lockfile, schema, protected database, harvested observation, or golden-corpus
change occurred. The first post-admission golden invocation was a
loopback-bind permission non-result; the identical permitted invocation passed
**11/11**, delta **0**.

**v0.19 PREVIEW-DISPOSITION is complete (measured 2026-07-29).**
The operator selected **retire**. The current tree deletes the coupled
`diagnostics` and `robots-preview` feature declarations, the preview binary,
the robots-only network helper and wire test, the diagnostic API and its two
tests, and the diagnostics-only parser/matcher provenance bookkeeping. Cargo
metadata now exposes no feature or binary target in `intel-compliance` and only
the supported `net` feature plus the library target in `intel-ingest`.
`ARCHITECTURE.md` records the retirement while preserving the published
v0.15.2 tag and v0.18 wire observations as historical evidence.

Before retirement, the supplemental commands passed **42/42**
`intel-compliance` tests with `diagnostics` and **30/30** `intel-ingest`
library tests plus **1/1** preview-binary test with `robots-preview`. After
retirement, both former command lines exit **101** at Cargo's entry point with
`does not contain this feature`. The surviving all-features suites reconcile
to **40/40** compliance tests and **29/29** ingest tests, with no binary suite.
The default workspace remains **133** tests and the net matrix remains
**29 + 26 = 55**; the public `/v1/*` surface, SQLite schema, dependencies,
`Cargo.lock`, protected artifacts, and default robots decisions are unchanged.

The final pre-status `./run ci-local` passes **20/20**: warning-denied current
and Rust 1.78 offline checks/tests, **133** workspace tests, warning-denied net
checks plus **29 + 26** net tests, clippy, fmt, ShellCheck, Python 3.11 shell
**248/248**, invariant **11/11 rules / 23 controls**, all **161/161** pins,
protected databases **2/2**, and golden **11/11**. The independent constrained
Python 3.12.13 lane passes **248/248**. An earlier pre-final CI attempt correctly
found that the credential scanner still saw the deleted but unstaged binary in
`git ls-files`; staging the deletion exposed the intended post-task tree, after
which the scanner and all **23** mutation controls passed. A sandboxed golden
and Python 3.12 attempt were loopback/process-permission non-results; their
identical permitted invocations produced the passing results above.

**v0.19 NEGATIVE-CACHE is complete (measured 2026-07-29).**
RFC 9309 §2.3.1.4 requires complete disallow while `robots.txt` is unreachable;
§2.4 permits caching but does not require using a stale successful policy.
`ROBOTS_NEGATIVE_TTL` is therefore named at **300 seconds** beside the
**86,400-second** `ROBOTS_TTL`. Production constructs `RobotsCache` with both
values. The cache selects 300 seconds only for `Policy::Unreachable`;
successful parsed policies and definitive `Unavailable` results retain 86,400
seconds. Five minutes avoids a tight retry loop while preventing one transient
failure from occupying the success path's full day.

The operator selected **no last-known-good fallback** on 2026-07-29. An
`Unreachable` re-fetch still overwrites an expired good policy and fails closed.
That more-permissive alternative is deferred until a measured live transient
robots outage affects an admitted publisher while a usable last-known-good
policy exists, followed by explicit operator authorization.

Both durable controls failed before the implementation with exit **101**:
`unreachable_retries_after_its_short_ttl_but_not_before` remained denied at the
short-TTL boundary, and
`unreachable_overwrites_last_good_when_fallback_is_deferred` likewise remained
denied after its ten-second test boundary. After implementation, the first
control keeps `Unavailable` cached at calls **1** after the negative boundary,
keeps `Unreachable` at calls **1** before its boundary, and refetches to an
allowing body at calls **2** exactly at the boundary. The overwrite control
measures calls **1 → 2**, holds the unreachable denial at calls **2** inside
its TTL, and refetches at calls **3** exactly at expiry.

The four unchanged fail-closed guards all pass:
`a_404_robots_txt_blocks_a_default_source_but_passes_an_opted_in_one`,
`opting_in_does_not_bypass_an_explicit_arxiv_disallow`,
`a_live_fetch_with_no_cache_fails_closed_before_the_operator_gate`, and
`the_operator_denylist_still_refuses_what_the_publisher_permits`. The
`apply_crawl_delay` source slice remains SHA-256
`ea16d8cac28b094f23eba38c5656c800a79515c049b57f0a85f85abe6bd77327`;
the complete `RateLimiter`/`HostLimiters` slice, including `acquires`, remains
SHA-256
`4280d757274fd3ae739a2e600054b1fe517287cff64e56abea82176ea73c38ed`.
No single-flight behavior was added.

The final pre-status `./run ci-local` passes **20/20**: warning-denied current and Rust
1.78 offline checks/tests, **133** workspace tests, warning-denied net checks
plus **29 + 26** net tests, clippy, fmt, ShellCheck, Python 3.11 shell
**248/248**, invariant **11/11 rules / 23 controls**, all **161/161** pins,
protected databases **2/2**, and golden **11/11**. The independent constrained
Python 3.12.13 lane passes **248/248**. Earlier attempts correctly caught a
one-line R2 self-test displacement and then an offline-only unused import; the
final construction preserves the planted R2 line and is warning-clean in both
feature modes.

**v0.19 EXPORT-BUDGET is complete (measured 2026-07-29).**
Root-run Repomix 1.17.0 measured the pre-change review export at **4,887,220
bytes / 339 included files** after collecting 340 files and security-excluding
one Rust source. `repomix.config.json` now excludes `evidence/**` and the exact
closed-cycle pattern through v0.11 while retaining
`config/protected-artifacts.json`. Its security scan is disabled so the export
cannot silently omit a source file; registered, self-testing invariant R4
remains the repository's credential control.

Historical appends from v0.13 through the oldest pre-architecture append moved
byte-identically to `docs/state-archive/STATE-through-v0.13.md`, with the
pointer left at their former position. The prior `STATE.md` was **535,858
bytes**, SHA-256
`9553fb682d04e1b2a925e90bd11ab2ae867bd0e6025193abde9a643c9239f3b6`.
The archive is **297,739 bytes**, SHA-256
`3233af5b4c148f7a7f4700edba3238dc67245f28d83dc07cc53c26ebdca6a414`.
Replacing the one pointer in retained `STATE.md` with the archive produced
**535,858 bytes** and the identical prior SHA-256, proving the split lossless.

The final root-run export is **2640795 bytes / 146 files**. It contains
`Cargo.lock`, `config/protected-artifacts.json`, `AGENTS.md`, `run`, and every
tracked file under `crates/`, `apps/`, `tools/`, and `shell/`. No repository
file was deleted. The task sequence reruns the status suite after its separate
v0.19 progress audit records the real implementation commit.

**v0.19 STATUS-TRUE publication audit (measured 2026-07-29).**
Before this step, `cycle-check`, `checklist-audit`, `progress-check`, and
`version-check` all passed while this header asserted that remote main was
`f13c6129d608ab9259f421dce6ed419ce469c225` and remote `v0.15.2` was absent.
With the new reconciliation present and before correcting this file,
`./run cycle-check` failed with exactly these two rule messages:

> `STATE.md: publication disposition agreement: newest closed release v0.15.2 in docs/cycles/TASKS-v0.18-EXECUTION.md is an annotated tag reachable from HEAD, but the status header asserts publication is pending or outstanding`
>
> `STATE.md: publication assertion freshness: origin/main asserts f13c6129d608ab9259f421dce6ed419ce469c225, but the measured ref is 344124819cb3c554f851d0cac3f0f1ed08d1aa10`

Local and remote ref inspection agree: `origin/main` is
`344124819cb3c554f851d0cac3f0f1ed08d1aa10`; annotated `v0.15.2` is object
`22beef8e023e52024cfe9614273e2d82b39f4956`, peeled to release commit
`b3c4c4d3b695ceff27a9d4a2ec610fc851939324`, which is reachable from `HEAD`.
The measured result of the authorized atomic publication is that remote main
and both annotated-tag refs are present at those exact objects. Read-only
GitHub inspection found publication CI run
`30375179895`, attempt **1**, event `push`, exact head
`344124819cb3c554f851d0cac3f0f1ed08d1aa10`, status `completed`, and conclusion
`success` (created 2026-07-28T15:48:34Z, completed 2026-07-28T15:49:44Z).
No run was dispatched or replayed. The v0.18 closing record and every
historical `STATE.md`/progress append remain unchanged; this is the forward
correction.

**v0.18 R-CLOSE is locally complete (measured 2026-07-28).**
Release disposition: release (as of 2026-07-28). The publication trigger is
**F1**, not the runbook's mechanical patch default. The operator selected
v0.15.2 because the published v0.15.1 harness makes a false lifecycle claim
and the forward correction is a zero-risk patch with an executing regression.

The trigger was verified at the tagged tree rather than inferred from current
provenance. Exact command
`git show v0.15.1:run | shasum -a 256` returned
`7351f2ffb7eb6def34c99c812a61a10690b6f690e9e1e44cee88790ca6dcc455`;
the object is **41,959** bytes and `git grep` locates
“cored still running on … for inspection” at tagged `run:839`. Current `run`
is **42,056** bytes at
`caae4e8007fc885241bf1ac7c844e397a149970048e036be285e356449030678`;
it reports the observation database/runtime log, calls `cmd_down`, and the
executing fail-before detects removal of that shutdown. The implementation is
commit `dae015e`.

v0.15.2 is the compatible patch **identity** because no `/v1/*` route,
response body, schema, or other named surface moved; that mechanical fact is
not the publication reason. Evidence candidate
`2ce912dca181e5e7b949a4b2e6fd8487412388f9` and exact release commit
`b3c4c4d3b695ceff27a9d4a2ec610fc851939324` are separate named subjects.
Annotated tag object `22beef8e023e52024cfe9614273e2d82b39f4956`
peels exactly to that release commit.

No default-build compliance behavior changed. ORIGIN-CASE shipped nothing
because E0 proved `reqwest::Url` normalizes initial and redirected authorities
before the production gate. Matcher provenance and the robots-only client are
excluded unless `diagnostics` / `robots-preview` are selected; the default
allow/deny outcomes and live gate remain unchanged. The only default
production behavior change is `run`'s truthful managed-process lifecycle.
The public API, SQLite schema, dependencies, protected databases, and golden
corpus are unchanged.

The v0.15.1 robots incident remains bounded. The sole configured network
source and the historically observed redirect use single-segment paths, for
which old and corrected comparison targets are identical; the three
multi-segment configured URLs are fixture-backed and issue no publisher
request. No configured live URL or observed redirect was affected, so the
correction remains forward-only and retractions stay **three**.

v0.18 nevertheless records an important first: one bare live harvest reached
three real arXiv OAI-PMH pages under a gate that enforces the policy it claims
to enforce, followed two `resumptionToken`s, and ingested **2,692** documents
into a fresh ignored database. The preceding robots-only preview fetched the
recorded **11,083-byte** arXiv HTTP 404 response, SHA-256
`fe5a8ce88b89f96db55e8d9a7eb3d978f3d364bf31d48c4880422511e9035ab2`;
absence-only `robots_on_missing: "allow"` permitted the target while explicit
policy and unreachable outcomes remain fail-closed.

Both wire reports now state their release-identity boundary. Every reported
request used `intel-platform/0.15.1`; the v0.15.2 head emits
`intel-platform/0.15.2`, so a re-run cannot reproduce that versioned
User-Agent line. The stable `intel-platform` product token is unchanged, and
arXiv served no policy group whose selection could differ. The reports remain
historical observations rather than future byte-reproducibility claims.

The feature-gated preview ships inert, unsupported, and currently unowned. Its
named promotion trigger is both a named owner and an explicit operator
decision to make `diagnostics` / `robots-preview` a supported product or
operator surface. Neither condition is met. Separately, `arxiv-cs` is the only
real configured publisher; the other three sources are `example.org`
placeholders. The platform therefore aggregates one publisher. Adding a
second is an open product question for a later cycle and remains its own
compliance decision.

The release diff from annotated v0.15.1 contains exactly **39 paths**,
classified once each:

- **Default runtime behavior and failure-capable verification (2):** `run` and
  `shell/tests/test_harvest_preflight.py`.
- **Inert feature-gated diagnostics (5):** `crates/compliance/Cargo.toml`,
  `crates/compliance/src/lib.rs`, `crates/ingest/Cargo.toml`,
  `crates/ingest/src/bin/robots_preview.rs`, and
  `crates/ingest/src/net.rs`.
- **Release authorities, documentation, and architecture (8):**
  `ARCHITECTURE.md`, `CHANGELOG.md`, `Cargo.lock`, `README.md`, `STATE.md`,
  `apps/cored/Cargo.toml`, `shell/intel_shell/__init__.py`, and
  `shell/intel_shell/app.py`.
- **Operating contract and cycle history (5):** `AGENTS.md`,
  `docs/cycles/PROGRESS-v0.17.md`, `docs/cycles/PROGRESS-v0.18.md`,
  `docs/cycles/TASKS-v0.17-EXECUTION.md`, and
  `docs/cycles/TASKS-v0.18-EXECUTION.md`.
- **Authenticated hosted evidence and protected index (16):**
  `config/protected-artifacts.json`,
  `evidence/ci-runs/30369139464-1/30369139464-1-core.json`,
  `evidence/ci-runs/30369139464-1/30369139464-1-core.json.sigstore`,
  `evidence/ci-runs/30369139464-1/30369139464-1-golden.json`,
  `evidence/ci-runs/30369139464-1/30369139464-1-golden.json.sigstore`,
  `evidence/ci-runs/30369139464-1/30369139464-1-lint.json`,
  `evidence/ci-runs/30369139464-1/30369139464-1-lint.json.sigstore`,
  `evidence/ci-runs/30369139464-1/30369139464-1-msrv.json`,
  `evidence/ci-runs/30369139464-1/30369139464-1-msrv.json.sigstore`,
  `evidence/ci-runs/30369139464-1/30369139464-1-net.json`,
  `evidence/ci-runs/30369139464-1/30369139464-1-net.json.sigstore`,
  `evidence/ci-runs/30369139464-1/30369139464-1-shell-py3.11.json`,
  `evidence/ci-runs/30369139464-1/30369139464-1-shell-py3.11.json.sigstore`,
  `evidence/ci-runs/30369139464-1/30369139464-1-shell-py3.12.json`,
  `evidence/ci-runs/30369139464-1/30369139464-1-shell-py3.12.json.sigstore`,
  and `evidence/v0.15.2/deferred-audit/report.json`.
- **Historical wire observations (3):**
  `observations/v0.18/live-harvest/arxiv-cs-report.md`,
  `observations/v0.18/robots-preview/arxiv-cs-report.md`, and
  `observations/v0.18/robots-preview/arxiv-cs-robots.txt`.

`ARCHITECTURE.md` preserves A4, the editable-L1 controller residual, R3/R4's
bounded open-bottom scanners, the active-runbook measured-value heuristic,
and T7 robots single-flight as open; L2 remains scheduled. The unsupported
preview and one-real-publisher fact add explicit product/support limitations
without weakening any architectural invariant.

The exact release commit, with a clean tree throughout measurement, passes
`./run ci-local` **20/20**: version, cycle, checklist, invariant, deferred
re-derivation, Python-floor byte-compile, ShellCheck, workspace check/test,
net check/test, clippy, rustfmt, Rust 1.78 check/test, Python 3.11 shell tests,
golden, protected artifacts, persisted fingerprints, and progress validation.
Measured totals are **131** workspace tests, **55** net tests (**29 + 26**),
shell **245/245** on Python 3.11.4 and, after a clean constrained rebuild,
**245/245** on Python 3.12.13. The first sandboxed Python 3.12 attempt could
not bind loopback test doubles or execute `ps` and is a permission non-result;
the identical permitted invocation passed.

Supplemental tag-surface execution passes compliance diagnostics **40/40**,
ingest robots-preview **30/30**, and preview-binary **1/1**; both corresponding
feature-clippy commands pass with zero warnings. All **161/161** pins and both
protected databases remain exact. The mandatory standalone post-matrix golden
run passes **11/11**, delta **0**. `origin/main` remains
`f13c6129d608ab9259f421dce6ed419ce469c225` and the remote tag remains absent
until the closing audit commit and annotated tag are published atomically.

**v0.18 RE-MEASURE is complete at the v0.15.2 candidate (measured
2026-07-28).** The runbook's default patch trigger fired because no `/v1/*`
route or response body moved. The clean evidence candidate is
`2ce912dca181e5e7b949a4b2e6fd8487412388f9` on
`candidate/v0.15.2`; release publication and the final release commit remain
the Step 7 operator decision. Before dispatch, the remote workflow was read
from that branch and contained every expected core, lint, net, MSRV, two-shell,
golden, receipt, bundle, and upload invocation. Its remote Git blob
`96e85af978981b7af9bdd8e9e11069f158f35e57` equals the local workflow blob.

Exact-candidate local execution passed **20/20** with **131** workspace tests,
**55** net tests (**29** ingest + **26** cored), shell **245/245** under both
Python 3.11.4 and 3.12.13, locked Rust 1.78, zero
rustc/clippy/fmt/ShellCheck failures, `invariant-scan` **11/11 rules / 23
controls**, and golden **11/11**. Authenticated hosted workflow-dispatch
[run 30369139464 attempt 1](https://github.com/jiayanzeng/intel-platform/actions/runs/30369139464)
completed successfully at the same candidate. Its logs, read independently of
job status, report **131** workspace tests, **55** net tests (**29 + 26**),
both shell lanes collecting **245** tests as **244 passed + 1 declared
on-site-only skip**, `invariant-scan` **11/11 rules / 23 controls**, R10's
derived **45** exemptions, and golden **11/11**. Thus each hosted count equals
the local same-commit count, with shell equality measured as collected tests.

All **7/7** derived job identities across the **6** blocking jobs have
successful Linux receipts and persisted Sigstore bundles; zero receipts were
rejected. Release-posture `audit-deferred` authenticated every bundle against
repository `jiayanzeng/intel-platform`, the CI workflow signer, source digest
`2ce912dca181e5e7b949a4b2e6fd8487412388f9`, and source ref
`refs/heads/candidate/v0.15.2`. It reports **5 deferred / 2 promoted / 0
deferred subsystems implemented**. The largest evidenced archive remains
**2,600** documents; exact cosine p95 measured **9.613 ms**, below the recorded
**16.264 ms** A3 request anchor.

The admitted audit report is
`evidence/v0.15.2/deferred-audit/report.json`, SHA-256
`78901f2d181672f2a0ec073c18ec5bb02c68762de0fc7362b49f903ed6509448`,
**34,520** bytes. Its seven receipts, seven bundles, and one report add
**15** records, bringing the protected manifest to **161/161** pins:
**159/159** evidence plus **2/2** authorization surfaces. Remote reinspection
found `origin/main` unchanged at
`f13c6129d608ab9259f421dce6ed419ce469c225`, the candidate branch exact, and
no `v0.15.2` tag. No publication, product path, public surface, dependency,
lockfile, schema, protected database, harvested observation, or golden-corpus
change occurred. The first post-admission golden invocation was a non-result
because the sandbox denied the core's loopback bind; the identical permitted
invocation passed **11/11**, delta **0**.

**v0.18 WIRE-FINDINGS is complete with F1 fixed (measured 2026-07-28).**
The one Step 4 finding has exactly one disposition: **fixed with an offline
regression test**. `cmd_harvest_arxiv` now stops the managed core with
`cmd_down` before returning, reports the observation database and runtime log,
and no longer claims that the core remains available for inspection. This
makes the command lifecycle deterministic under both interactive shells and
managed runners.

The executing fail-before removed the required terminal `cmd_down` call and
failed **1/1** with `cmd_harvest_arxiv must stop its managed core before
returning`; the pass-after harness file is **2/2**. No real XML shape, status
code, or redirect differed from the existing fixture coverage, so no
publisher-derived fixture was added. No publisher request or live database
write was made in this step, and no harvested document entered the protected
or golden corpus.

Because `run` is authorization-pinned, its one record moved from
`7351f2ffb7eb6def34c99c812a61a10690b6f690e9e1e44cee88790ca6dcc455`
(**41,959** bytes) to
`caae4e8007fc885241bf1ac7c844e397a149970048e036be285e356449030678`
(**42,056** bytes). The model-profile functions, dispatch,
`tools/model_profiles.py`, and authorization policy are unchanged. Manifest
schema v2 validation and `verify-artifacts` pass with all **146/146** pins and
protected databases **2/2** exact.

The final local matrix passes **20/20** with **131** workspace tests, **55**
net tests, both Python 3.11.4 and 3.12.13 at **245/245**, locked Rust 1.78,
zero rustc/clippy/fmt/ShellCheck failures, and `invariant-scan` **11/11 rules /
23 controls**. The mandatory standalone golden remains byte-identical at
**11/11**, delta **0**.

**v0.18 LIVE-HARVEST is complete with one finding for Step 5 (measured
2026-07-28).** Preflight validated artifact schema v2, all **146/146** pins,
both protected databases exact, no listener on port 8788, and no existing
`cored` process. One bare `./run harvest-arxiv` launched one core (PID 13809)
against the default fresh
`data/live-20260728T141101Z-13711.db`. The database is an ignored observation,
not evidence: SHA-256
`11d2b6a6bdf15b27964eae2be971deb0b056d47546ea96dd47a6eb1e56e58d6a`,
**10,166,272** bytes, integrity `ok`.

The run covered 2026-07-25 through 2026-07-28, at most three pages. The
`Identify` reachability probe returned HTTP 200. The live gate observed the
same publisher-policy 404/`Unavailable(allow)` disposition as Step 3 on every
page. No publisher `Crawl-delay` existed; the effective operator floor was
**0.500 seconds** on all three page requests.

Three real OAI-PMH XML pages committed successfully: page 1 brought the
cumulative count to **1,300**, page 2 to **2,600**, and the naturally final
page 3 to **2,692**. Two real `resumptionToken`s were returned and followed.
There were exactly three page-request lines and three robots-gate lines, with
no redirect, 503/Retry-After, extra attempt, status-error, parse-error, or
unexpected-shape log. The source result is `ok=true`, `fetched=2692`,
`new=2692`. The store holds **2,692** rows in **2,550** canonical groups, so
**142** near-duplicate rows are suppressed from analysis. The durable final
cursor row is `cursor=NULL`, `high_water=2026-07-28`,
`pending_high_water=NULL`. Total command wall time, including artifact
preflight and the net build, was **46.38 seconds**.

No harvested document entered the protected or golden corpus. Post-run
`verify-artifacts` again reports all **146/146** pins and protected databases
**2/2** exact; `./run down` left port 8788 free; standalone golden remains
**11/11**, delta **0**.

One surprise is open for Step 5 disposition: the harness printed that `cored`
was still running for inspection, but immediately after command exit PID 13809
was absent and loopback `/health` refused connection. No publisher XML, paging,
cursor, redirect, retry, status, or politeness defect was observed.

**v0.18 ROBOTS-PREVIEW is complete with a Step 4 go verdict (measured
2026-07-28).** The sole configured network source, `arxiv-cs`, made exactly one
request under the installed `intel-platform/0.15.1` crawler identity:
`GET https://oaipmh.arxiv.org/robots.txt`. Automatic redirects were disabled
and none was followed; no document or harvest URL was requested. The monitored
contact came from the ignored `.env` and is not recorded.

The origin returned HTTP **404** with `Content-Type: text/html; charset=utf-8`.
The raw **11,083-byte** arXiv 404 response is recorded at
`observations/v0.18/robots-preview/arxiv-cs-robots.txt`, SHA-256
`fe5a8ce88b89f96db55e8d9a7eb3d978f3d364bf31d48c4880422511e9035ab2`,
alongside the complete observation report. Because no robots policy exists,
there is no selected specific or `*` group, matched rule, `Allow` exception, or
`Crawl-delay`. The source's explicit `robots_on_missing: "allow"` maps to
`MissingPolicy::RfcAllowAll`, so the configured
`/oai?verb=ListRecords&metadataPrefix=oai_dc&set=cs` target is **allowed** and
Step 4 is **GO**. This changes absence only: an explicit `Disallow` or an
unreachable response would still deny.

The preview is feature-gated and adds no dependency. `Cargo.lock`, the default
and `net`-only public APIs, `/v1/*`, the SQLite schema, protected artifacts, and
the harvest path are unchanged. Executable fail-before controls first exited
**101** with the diagnostic matcher and preview-fetch surfaces absent.
Pass-after suites report `intel-compliance --features diagnostics` **40/40**
and `intel-ingest --features robots-preview` **30/30** plus preview binary
**1/1**; the loopback control observed one literal `/robots.txt` request with
the installed identity. The first supplemental preview clippy run caught two
`needless_borrow` warnings; after the two call-site correction, preview clippy,
formatting, and `git diff --check` pass. The final full local matrix passes
**20/20** with the counts in the header, all **146/146** pins and protected
databases **2/2** exact, and the mandatory standalone golden is **11/11**,
delta **0**.

**v0.18 ORIGIN-CASE is skipped at its decision gate (measured
2026-07-28).** E0 proved that mixed-case authority bytes cannot reach the
shipped live gate: `reqwest::Url` normalizes both the initial request and every
publisher-controlled redirect before `get_text_with` calls `gate()`. The
runbook explicitly requires a skip on that finding, so no case-normalization
implementation or new dependency was added.

The production ingest blobs remain
`crates/ingest/src/lib.rs=773d7ffe2e984f75d7ddf4916e73929d09f5d149`
and
`crates/ingest/src/net.rs=0950319247c01aeae3394b8d4683b410c01c70fc`.
The existing URL case-table and same-origin redirect controls each pass
**1/1**. Path bytes, including path case, remain untouched; explicit ports and
userinfo exclusion remain unchanged. Percent-encoding in the authority is
outside this skipped step: the shipped live path continues to use
`reqwest::Url`'s authority parsing without adding a second normalization layer.
The mandatory standalone golden remains **11/11**, delta **0**.

**v0.18 E0 is complete (measured 2026-07-28 at activation-audit commit
`af961f93221b2ab31e72c5bb3501dafa91aa1dec`).** The first sandboxed matrix
attempt was a non-result at the net wire fixture because the sandbox refused
its loopback bind. The identical permitted invocation with
`CARGO_TARGET_DIR=/private/tmp/intel-v018-e0-ci-target` passed all **20/20**
jobs: **131** workspace tests, **55** net tests (**29** `intel-ingest` plus
**26** `cored`), Python 3.11.4 shell **244/244**, warning-denied offline and net
builds, clippy, fmt, ShellCheck, floor byte-compilation, locked Rust 1.78
check/test, `invariant-scan` **11/11 rules / 23 controls**, all **146/146**
pins, both protected databases exact, and golden **11/11**. The mandatory
standalone golden invocation also passed **11/11**, delta **0**. Clean local
rebuilds resolved the exact **21/21** constrained packages and passed shell
**244/244** under both Python 3.11.4 and Python 3.12.13 with the same one
third-party deprecation warning.

G2 is bounded. The live harness removes the fixture only from `arxiv-cs`; its
configured publisher URL has the single-segment target
`/oai?verb=ListRecords&metadataPrefix=oai_dc&set=cs`, identical under the old
first-segment derivation and the corrected derivation. The historical observed
redirect from `https://export.arxiv.org/oai2` to
`https://oaipmh.arxiv.org/oai` also has single-segment targets on both sides,
so both old/new comparisons are identical (`/oai2?...` and `/oai?...`). The
three `example.org` fixture URLs do differ — `/techwire`, `/osdaily`, and
`/filings` become their complete two-segment paths — but those configured
sources read committed fixtures and issue no publisher request. A constructed
multi-segment `Location` such as `/oai/archive/page?cursor=abc` does distinguish
the implementations: old `/oai`, corrected
`/oai/archive/page?cursor=abc`. No configured live URL or historically observed
redirect was affected; a future publisher-controlled multi-segment redirect
would have been.

G1 is closed clean as not-a-defect. Direct construction showed that
`origin_of("HTTPS://Example.org/start")` and `host_of(...)` preserve case, but
production reachability does not: the only production `Reach::Network` call to
`gate()` is inside `get_text_with`, after `reqwest::Url::parse` for the initial
URL and `Url::join` for every `Location`. A temporary executing control supplied
`https://FIRST.test/start` and redirect
`https://SECOND.test/final`; the shipped path requested only lowercase
`first.test`/`second.test` robots and page URLs and created only lowercase
limiter keys. The control passed **1/1** and was removed after measurement.
No other production network caller bypasses that normalization, so Step 2's
explicit skip gate fires.

The configured-source inventory is **4** sources: `arxiv-cs` is the sole real
publisher and `techwire`, `osdaily`, and `filings-digest` are the three
`example.org` placeholders. This is a measured product limitation, not work
added to v0.18.

Remote object inspection re-verified `main` at
`f13c6129d608ab9259f421dce6ed419ce469c225`, annotated `v0.15.1` tag object
`d6a71c1a2afabd7ce7b335756b7ae66ff36cf1ba`, and peeled release commit
`a0ba69e0a3e8385287274bb404d5123f9a2b8ac7`. Manifest schema validation passes
with **146/146** pinned files, and `verify-artifacts` passes with both protected
databases byte-exact.

**v0.17 R-CLOSE is complete (measured 2026-07-28).**
Release disposition: release (as of 2026-07-28). The operator authorized
publication as **v0.15.1**. The patch trigger fired because no observable
`/v1/*` route, response body, schema, or other named surface moved. The
shipped behavior change is a correctness correction within those existing
surfaces: publisher robots enforcement now receives the complete path plus
query and excludes the client-only fragment.

The evidence candidate and release commit are separate identities. Evidence
candidate `3481e4ba85d65c927b7d0fc3a430bc04fb094394` was pushed before the version
decision under the provisional branch name `candidate/v0.16.0`; the seven
signed receipts pin that commit and exact source ref, not the branch's proposed
version. Release commit
`a0ba69e0a3e8385287274bb404d5123f9a2b8ac7` is a descendant of the candidate.
Annotated tag object `d6a71c1a2afabd7ce7b335756b7ae66ff36cf1ba`
dereferences exactly to that release commit.

Re-running the release-posture audit offline in a clean detached checkout of
that same candidate required no hosted re-dispatch. It accepted the same
**7/7** authenticated receipts with zero rejection, retained **5 deferred /
2 promoted**, and produced
`evidence/v0.15.1/deferred-audit/report.json`, SHA-256
`d73b198e4bb04c96273ae53ecef5e81e162a645ee6c0827450fd737fc7c8dbb9`,
**34469** bytes. Its disposable exact-cosine timing sample is **8.913750 ms**;
all source, configuration, Git, receipt-identity, and disposition fields
matched the prior version-provisional report. The manifest therefore still has
**146** pins — **144** evidence plus **2** authorization surfaces — with one
corrected report path/hash rather than another admission.

At the exact release commit,
`CARGO_TARGET_DIR=/private/tmp/intel-v017-step7-ci-target ./run ci-local`
passed all **20/20** jobs: **131** workspace tests, **55** net tests
(**29** `intel-ingest` + **26** `cored`), Python 3.11.4 shell **244/244**,
locked Rust 1.78, zero rustc/clippy/fmt/ShellCheck failures,
`invariant-scan` **11/11 rules / 23 controls**, all **146/146** pins, and
both protected databases exact. The clean repository-local Python 3.12.13
rebuild verified **21/21** constrained packages and passed **244/244** with
the same single deprecation warning. The mandatory standalone golden
invocation passed **11/11**, delta **0**.

The atomic publication push advanced remote `main` from
`cdae3c922a2156701c0df0ceb4f45fc937fa7f20` to closing-audit commit
`0d99a6387f3087ff90990ff95a1ee6cf6abcb6d4` while creating remote annotated
tag object `d6a71c1a2afabd7ce7b335756b7ae66ff36cf1ba`; its peeled target is release
commit `a0ba69e0a3e8385287274bb404d5123f9a2b8ac7`. Publication CI run
`30361205715` completed **success** at the closing commit: all seven
matrix-expanded jobs from the six blocking job definitions succeeded, while
the dependency-drift report-only job was skipped as designed. This forward
STATE append is the publication-audit record and changes no release object.

The first affected release is **v0.8.0**. From v0.8.0 through v0.15.0,
multi-segment and query-specific publisher rules could be weakened because the
gate received only the first path segment; a client-only fragment was also
retained. Single-segment rules, publisher/operator gate composition,
fail-closed outcomes, and re-gating order remained enforced. v0.15.1 derives
the full path plus query, excludes the fragment, and evaluates it before the
first document request and every redirect, including after an origin change.
E0 found no immutable published false completeness claim: the published
“full gate” statements cover composition and call order, while RFC-matcher
statements cover matching the path supplied to the matcher. This is a forward
correction; retractions remain **three**.

The temporary live-harvest suspension is explicitly **lifted** by Step 3's
accepted ROBOTS-PATH result. No live harvest ran during the cycle, and every
future live harvest still runs `./run verify-artifacts`, uses a fresh
destination, and supplies a monitored crawler contact. R11's v0.16 limitation
is discharged rather than narrowed: five controls cover the four declared
spellings (`config/core.json`, `config/entities.json`, `CORE_CONFIG`, and
`CORE_ENTITIES`) plus a module-local variable derived from `CORE_ENTITIES`, as
recorded in `ARCHITECTURE.md`. A4, the editable-L1 controller residual, R3/R4's
bounded open-bottom scanners, the measured-value heuristic, and T7 robots
single-flight remain open; L2 remains scheduled.

The release diff from annotated `v0.15.0` contains exactly **34 paths**,
classified once each:

- **Runtime behavior and failure-capable verification (4):**
  `crates/ingest/src/lib.rs`, `crates/ingest/src/net.rs`, `run`, and
  `shell/tests/test_harvest_preflight.py`.
- **Invariant, architecture, and operating contract (3):** `AGENTS.md`,
  `ARCHITECTURE.md`, and `config/invariant-rules.json`.
- **Release authorities and operator documentation (7):** `CHANGELOG.md`,
  `Cargo.lock`, `README.md`, `STATE.md`, `apps/cored/Cargo.toml`,
  `shell/intel_shell/__init__.py`, and `shell/intel_shell/app.py`.
- **Cycle planning and append-only audit history (4):**
  `docs/cycles/PROGRESS-v0.16.md`, `docs/cycles/PROGRESS-v0.17.md`,
  `docs/cycles/TASKS-v0.16-EXECUTION.md`, and
  `docs/cycles/TASKS-v0.17-EXECUTION.md`.
- **Authenticated hosted receipts and bundles (14):**
  `evidence/ci-runs/30357365420-1/30357365420-1-core.json`,
  `evidence/ci-runs/30357365420-1/30357365420-1-core.json.sigstore`,
  `evidence/ci-runs/30357365420-1/30357365420-1-golden.json`,
  `evidence/ci-runs/30357365420-1/30357365420-1-golden.json.sigstore`,
  `evidence/ci-runs/30357365420-1/30357365420-1-lint.json`,
  `evidence/ci-runs/30357365420-1/30357365420-1-lint.json.sigstore`,
  `evidence/ci-runs/30357365420-1/30357365420-1-msrv.json`,
  `evidence/ci-runs/30357365420-1/30357365420-1-msrv.json.sigstore`,
  `evidence/ci-runs/30357365420-1/30357365420-1-net.json`,
  `evidence/ci-runs/30357365420-1/30357365420-1-net.json.sigstore`,
  `evidence/ci-runs/30357365420-1/30357365420-1-shell-py3.11.json`,
  `evidence/ci-runs/30357365420-1/30357365420-1-shell-py3.11.json.sigstore`,
  `evidence/ci-runs/30357365420-1/30357365420-1-shell-py3.12.json`, and
  `evidence/ci-runs/30357365420-1/30357365420-1-shell-py3.12.json.sigstore`.
- **Protected evidence index and release report (2):**
  `config/protected-artifacts.json` and
  `evidence/v0.15.1/deferred-audit/report.json`.

**v0.17 RE-MEASURE is complete (measured 2026-07-28).** The operator
authorized one narrow non-`main` push of exact evidence candidate
`3481e4ba85d65c927b7d0fc3a430bc04fb094394`. That commit alone was pushed to
`candidate/v0.16.0`; no tag or `main` advance was authorized. Before dispatch,
the remote branch's `.github/workflows/ci.yml` blob
`96e85af978981b7af9bdd8e9e11069f158f35e57` was read and proved byte-identical
to the local candidate. Final live remote inspection still reports candidate
`3481e4ba…`, `origin/main` `cdae3c92…`, and no `v0.16.0` tag.

Workflow-dispatch run
`https://github.com/jiayanzeng/intel-platform/actions/runs/30357365420`, attempt
1, succeeded with all **7/7** derived evidence identities and no rejected
receipt: `core`, `golden`, `lint`, `msrv`, `net`, `shell/python=3.11`, and
`shell/python=3.12`. The hosted logs, rather than job status, measured **131**
workspace tests, **55** net tests (**29** ingest + **26** cored),
`invariant-scan` **11/11 rules / 23 controls**, and golden **11/11**. Each
hosted shell collected **244** tests and reported **243 passed / 1 declared
on-site-only skip / 1 warning**; the same candidate locally passed all
**244/244** with the same warning. The ingest net leg is therefore **29/29**
both hosted and local at the same commit. R10's topology-derived counts are
local **20 jobs / 24 checks**, hosted **6 blocking jobs / 23 checks**, with the
same derived exemption count **45**.

The signed bundle set is stored under
`evidence/ci-runs/30357365420-1/`. The release-posture deferred audit required
attestations and accepted **7/7** identities with zero rejection. Step 7's
offline version-corrected reproduction retained **5 deferred / 2 promoted**,
measured exact cosine p95 **8.913750 ms**, and produced
`evidence/v0.15.1/deferred-audit/report.json` at SHA-256
`d73b198e4bb04c96273ae53ecef5e81e162a645ee6c0827450fd737fc7c8dbb9`,
**34469** bytes. Authenticated re-derivation passes with
`evidence_grade=release`, `attestations_required=true`, and seven rows/triggers.

The fourteen signed hosted files plus that audit report add fifteen pins.
Manifest validation, `verify-artifacts`, and `evidence-report` pass with
**146/146** total pins — **144/144** evidence plus **2/2** authorization
surfaces — and both protected databases remain exact. The first sandboxed
local-matrix attempt was a non-result when a raw loopback fixture could not
bind; the identical permitted invocation then passed the full **20/20**
definition of done. The required separate standalone golden invocation also
passed **11/11**, delta **0**.

This step changes only authenticated evidence, its manifest admission, and
cycle/status records. It changes no production path, public response, schema,
dependency, lockfile, protected corpus byte, release tag, or `main` ref.
The candidate's `candidate/v0.16.0` source ref was named provisionally before
the version decision. It records signed provenance, not a release trigger.
Step 7 selected v0.15.1 because the robots correctness fix changes behavior
within existing names and shapes and no observable surface moved.

**v0.17 R11-BREADTH is complete (measured 2026-07-28).** Step 5's Gate
was widened before its first commit to include the architecture reconciliation
required by its own acceptance criteria. The existing AST detector already
recognized every declared spelling and transitive module-local assignments, so
neither `tools/invariant_scan.py` nor its schema changed.

R11 now has five independently reconstructible failure controls:

- direct `open("config/entities.json")` at
  `shell/intel_shell/pipeline.py:26`;
- direct `open("config/core.json")` at line **26**;
- a direct read through `os.environ["CORE_CONFIG"]` at line **26**;
- a direct read through `os.environ["CORE_ENTITIES"]` at line **26**; and
- a module-local variable assigned from `os.environ["CORE_ENTITIES"]`, then
  passed to `open()` at line **27**.

The focused R11 self-test executes all **5/5** controls and observes each exact
file, line, spelling, and failure message. The complete invariant module passes
**21/21** tests, and the complete scanner passes **11/11 rules / 23 controls**,
up from **19** controls. `ARCHITECTURE.md` now records the v0.16 breadth gap as
closed while preserving R11's bounded scope: the four declared spellings and
variables derived from them are controlled, but unknown future configuration
names are not claimed.

Full local CI remains **20/20** with shell **244/244**, all Rust/MSRV/lint,
pin, and protected-artifact results unchanged. The mandatory standalone golden
invocation remains **11/11**. This task changes only invariant controls,
architecture/status records, and the active checklist; no production path,
public response, schema, dependency, lockfile, or corpus byte changed.

**v0.17 HARVEST-PREFLIGHT is complete (measured 2026-07-28).** Repository
search found one entry point governed by AGENTS' live-harvest preflight rule:
the `harvest-arxiv` dispatch into `cmd_harvest_arxiv`. `up` builds the offline
core, and no other runner command both constructs a net-enabled harvester and
requests publisher documents. No live harvest ran in this task.

The fail-before focused shell test failed with
`cmd_harvest_arxiv must invoke its named artifact-integrity preflight`. The
entry point now invokes `cmd_verify_artifacts` before `need_cargo`,
`ensure_venv`, harvest-destination resolution, the arXiv reachability probe, or
any document request. This placement matters because a missing environment can
install constrained packages; even that possible outbound action is after
artifact verification.

The offline dynamic harness replaces every potentially external operation and
records the exact order:
`artifact-verification → cargo-check → python-environment →
destination-protection → reachability-probe → network-request`. A forced
verification status **37** exits with **37** after recording only
`artifact-verification`. A reconstructed copy with the two-line preflight
removed reaches later controls, and the shared assertion fails with a message
naming `cmd_harvest_arxiv`. The artifact-integrity step and the existing
`REFUSED: live harvest target` destination message remain distinct: the former
verifies the recorded bytes and corpus facts, while the latter refuses a
protected output path.

Because `run` is a whole-file authorization pin, the initial implementation
correctly made `verify-artifacts` report its hash and byte mismatch. Before the
first task commit, Step 4's Gate was widened to the `run` pin's
hash/size/provenance fields only. The forward pin is now
`7351f2ffb7eb6def34c99c812a61a10690b6f690e9e1e44cee88790ca6dcc455`
at **41959** bytes. The exact `run` diff outside the runbook/status surfaces is
the two-line harvest preflight; `tools/model_profiles.py`, the model-profile
functions/dispatch, and the authorization policy are unchanged. Manifest
validation and `verify-artifacts` pass with **131/131** pins and both protected
databases exact.

The focused preflight control passes **1/1**. Full local CI remains **20/20**
and adds that control to a shell total of **244/244**; all Rust, invariant,
pin, protected-artifact, lint, and MSRV results remain green. The mandatory
standalone golden invocation remains **11/11**.

**v0.17 ROBOTS-PATH is complete (measured 2026-07-28).** Before
implementation, Step 3's Gate was widened to include test support in
`crates/ingest/src/net.rs`, because its cross-origin redirect acceptance
criterion cannot be exercised solely from `lib.rs`. The dated amendment is in
the active runbook. E0's dependency gate rejected `url`, so the correction is a
zero-new-dependency in-crate derivation; `Cargo.toml` and `Cargo.lock` are
unchanged.

The fail-before `cargo test -p intel-ingest --features net --locked --lib`
recorded the defect directly: the case table returned `/private` instead of
`/private/secret/file`; publisher multi-segment and query rules allowed their
targets; a fragment changed the comparison target; and a cross-origin redirect
fetched the second document after deriving `/private` instead of refusing
`/private/secret`. The sibling-path allow control passed. The same invocation
also encountered the sandbox's unrelated loopback-bind refusal in the raw
User-Agent fixture; the complete unsandboxed net lane later passed **29/29**.

The corrected, executing table is:

| case | URL distinction | `robots_path_of` | `host_of` |
|---|---|---|---|
| multi-segment | `/private/secret/file` | `/private/secret/file` | `example.org` |
| query | `/private/secret?x=1` | `/private/secret?x=1` | `example.org` |
| fragment | `/private#fragment` | `/private` | `example.org` |
| query + fragment | `/private/secret?x=1#fragment` | `/private/secret?x=1` | `example.org` |
| no path | `https://example.org` | `/` | `example.org` |
| trailing slash | `https://example.org/` | `/` | `example.org` |
| explicit port | `example.org:8443/private` | `/private` | `example.org:8443` |
| userinfo | `user:pass@example.org/private` | `/private` | `example.org` |
| percent encoding | `/private/%73ecret` | `/private/%73ecret` | `example.org` |
| doubled slash | `/private//secret` | `/private//secret` | `example.org` |
| query without path | `https://example.org?x=1` | `/?x=1` | `example.org` |

The parser separates scheme, authority, and the untouched tail; it preserves
percent-encoding and repeated slashes, prefixes a no-path query with `/`, strips
userinfo only from the host, preserves an explicit port, and excludes the
fragment from the robots comparison. The doc comments state these exact
semantics. Publisher-policy tests now cover a blocked multi-segment descendant,
an allowed sibling, a query-specific denial, and fragment exclusion. The
redirect test observes policies for the first and second origins and proves the
multi-segment second target is refused before its document fetch.

Pass-after measurements are **15/15** ingest gate tests, **1/1** focused
cross-origin redirect control, **29/29** complete `intel-ingest` net tests,
locked Rust 1.78 workspace check and test, full local CI **20/20**, and
standalone golden **11/11**. No `invariant-scan` rule was added: these behaviors
execute directly at the gate and redirect sites, so a static restatement would
not add coverage. Step 3 acceptance lifts v0.17's temporary pre-correction live
harvest suspension; no live harvest was run. T7 remains deferred because this
change does not coordinate concurrent robots-cache misses.

**v0.17 NET-DOUBLE is complete (measured 2026-07-28).** The task Gate
contained every acceptance criterion and the diff changes only test support
inside `crates/ingest/src/net.rs`; no product path changed. The raw listener and
wire-header capture remain intact. The test now installs a scoped `NO_PROXY`
value before constructing the two real reqwest clients and restores the prior
process value through a drop guard, so the IP-literal loopback request reaches
the raw socket instead of the operator's configured proxy.

The same isolated sample that failed **20/20** in E0 passes **20/20** after the
change. A separate expected-panic control feeds a deliberately different
document-client string into the exact shared assertion and observes
`document client User-Agent bytes differ`; both clients' actual wire bytes
still equal the installed identity. The complete net lane passes **24/24**,
the complete local matrix reaches job 20 with **50 = 24 + 26** net tests, and
standalone golden remains **11/11**.

The fix is general for operator/system proxies that reqwest can bypass through
the standard `NO_PROXY` contract, while the observed trigger is specific to a
proxy that covers the fixture's IP literal. It would fail again if reqwest
stopped honoring `NO_PROXY`, if a future test bypassed the scoped guard, or if
another process rewrote traffic below reqwest's proxy layer. It does not change
production proxy behavior.

**v0.17 E0 is complete (measured 2026-07-28 at activation-audit commit
`79f5b6232959a13b9f4adb768c6c9f7a1bcfbcd9`).** The first fresh-target matrix
did not stop at the asserted job 11: it passed all **20/20** jobs from
`/private/tmp/intel-v017-e0-ci-target`. Standalone `golden`,
`verify-artifacts`, `cycle-check`, `checklist-audit`, `progress-check`,
`version-check`, and `invariant-scan` all passed. Workspace remained **126**,
net remained **49 = 23 + 26**, both clean local shell lanes passed **243/243**
with **21/21** exact packages, and golden remained **11/11**.

F2 is deterministic when isolated on this operator platform and can be masked
by full-suite timing. At HEAD, the exact User-Agent wire test failed **20/20**;
the same exact test at published release commit
`8f97205a3ed4fe82f6a5ede2febce7a5d82d9f81` failed **10/10**. The test source
blob is byte-identical at evidence candidate `43706216…`, the release commit,
and HEAD. The exact release commit has **zero** GitHub check runs; the
authenticated Linux net receipt instead belongs to the byte-identical-source
candidate and records success with **23** ingest tests. This is therefore not
post-release source drift.

The close mechanism is not the runbook's unread-byte/RST hypothesis. macOS
currently configures HTTP and HTTPS proxy `127.0.0.1:1082`; its exception list
contains `localhost` but not `127.0.0.1`. The failing request is routed through
that proxy and reports structured `hyper::Error(IncompleteMessage)`, a clean
EOF/FIN rather than `ConnectionReset`. The raw listener did not reach its
request diagnostic. With `NO_PROXY=127.0.0.1,localhost`, both raw requests
arrived with complete headers; each socket reported **0 queued request bytes**
before close while the peer was still open, and the test passed. Step 2 must
keep the raw byte subject while preventing the loopback fixture from entering
the operator's proxy.

The executing F1 table measured the current helpers as follows:

| case | URL distinction | `robots_path_of` | `host_of` |
|---|---|---|---|
| multi-segment | `/private/secret/file` | `/private` | `example.org` |
| query | `/private/secret?x=1` | `/private` | `example.org` |
| fragment | `/private#frag` | `/private#frag` | `example.org` |
| query + fragment | `/private/secret?x=1#frag` | `/private` | `example.org` |
| no path | `https://example.org` | `/` | `example.org` |
| trailing slash | `https://example.org/` | `/` | `example.org` |
| explicit port | `example.org:8443/private/secret` | `/private` | `example.org:8443` |
| userinfo | `user:pass@example.org/private/secret` | `/private` | `example.org` |
| percent encoding | `/private/%73ecret` | `/private` | `example.org` |
| doubled slash | `/private//secret` | `/private` | `example.org` |
| query without path | `https://example.org?x=1` | `/` | `example.org?x=1` |

F1a is confirmed: `get_text_with` calls `gate()` at the top of its loop before
the first `fetch()` and repeats the same order after every redirect. F1c is
also confirmed: every ingest-side test policy uses only `/`, `/techwire`,
`/admin`, `/oai`, `/blocked`, or an empty `Disallow`; none can expose a
multi-segment derivation failure.

The published-record audit found no immutable claim that robots enforcement is
complete for every URL path. Statements that a redirect reaches the “full
robots gate” describe the measured publisher/operator/politeness composition
and call order; the old “correct RFC-9309 path matching” sentence describes
`RobotsGate` matching the path it is handed. Neither claims that URL derivation
was complete. The source doc comment is false and will be corrected forward,
but it is not a published-record retraction. Retractions remain **three**.

F5 rejects a direct `url` dependency. In an isolated lock update, the normal
`intel-ingest` graph grew from **16 to 44** unique packages and resolved
`url 2.5.8`, `idna 1.1.0`, `idna_adapter 1.2.2`, and the `icu_* 2.2.0` family.
`idna_adapter` and all seven resolved ICU packages declare Rust **1.86**.
Cargo 1.78 fails before compilation because `idna_adapter 1.2.2` requires the
unstabilized `edition2024` manifest feature. This trips both the MSRV and
transitive-footprint dependency clauses; the repository lockfile was never
modified. Step 3 must use an in-crate derivation backed by the complete
executing table.

**v0.16 R-CLOSE release reconciliation is complete locally (measured
2026-07-28).** The selected release is **v0.15.0** because Step 5 added the
authenticated internal `POST /entities/unknown` core route. That new
core-owned observable surface fired the minor trigger before R-CLOSE; the
version is a record of behavior, not a preference chosen at publication.

Evidence and release subjects remain deliberately separate. The authenticated
evidence candidate is
`43706216c06608039d9c3e7ef2b86024b22d4a79`. Release commit
`8f97205a3ed4fe82f6a5ede2febce7a5d82d9f81` is its descendant and contains
the admitted receipts, report, version authorities, classified diff,
architecture reconciliation, and release record. Annotated tag object
`b7ee3445728e1816e1622c9498ffc2f165ed5dd5` dereferences to that release
commit, never the evidence candidate.

The complete `v0.14.1..v0.15.0-local-release` diff contains **74 paths**, each
classified exactly once:

- **release authorities and public release documentation (6):** `README.md`,
  `CHANGELOG.md`, `Cargo.lock`, `apps/cored/Cargo.toml`,
  `shell/intel_shell/__init__.py`, and `shell/intel_shell/app.py`;
- **document relocation and shared cycle-identity resolution (37):**
  `.gitignore`, `docs/REVIEWER-LESSONS-v0.13-v0.14.md`, all **29** changed
  paths under `docs/cycles/` (**12** progress logs and **17** task documents),
  `docs/intel-platform-OPERATIONS.md`, `shell/tests/test_cycle_check.py`,
  `tools/audit_deferred.py`, `tools/checklist_audit.py`,
  `tools/cycle_check.py`, and `tools/cycle_identity.py`;
- **operating contract and architectural reconciliation (2):** `AGENTS.md`
  and `ARCHITECTURE.md`;
- **job propagation, invariant, and exemption apparatus (5):** `run`,
  `config/invariant-rules.json`, `shell/tests/test_ci_local_propagation.py`,
  `shell/tests/test_invariant_scan.py`, and `tools/invariant_scan.py`;
- **core-owned gazetteer seam and relocatable Rust tests (7):**
  `apps/cored/src/main.rs`, `crates/ingest/src/arxiv_oai.rs`,
  `shell/intel_shell/core_client.py`, `shell/intel_shell/enrichment.py`,
  `shell/intel_shell/pipeline.py`, `shell/tests/test_pipeline_entities.py`,
  and `shell/tests/test_shell.py`;
- **protected manifest and durable hosted evidence (16):**
  `config/protected-artifacts.json`, all fourteen receipt/bundle files under
  `evidence/ci-runs/30347262430-1/`, and
  `evidence/v0.15.0/deferred-audit/report.json`;
- **current-state reconciliation (1):** `STATE.md`.

The product implementation change is bounded to the authenticated internal
entity-comparison seam in `cored` and the shipped shell client/pipeline. The
`crates/ingest` change is test-only relocation support. R-CLOSE changes only
the `cored` package version under `apps/`; Cargo mechanically updates that
local package version in `Cargo.lock`, with no dependency-resolution change.
No public `/v1/*` response body, SQLite schema, protected corpus, golden
expectation, published tag, or historical evidence byte changes.

The exact release commit passed the complete definition of done from the
existing uncleared `CARGO_TARGET_DIR=/private/tmp/intel-v016-step5-ci-target`.
`./run ci-local` passed **20/20** with **126** workspace tests, **49** net
tests (**23 + 26**), Python 3.11.4 shell **243/243**, `invariant-scan`
**11/11 rules / 19 controls**, all **131/131** pins, both protected databases
exact, locked Rust 1.78, and zero rustc/clippy/fmt/ShellCheck failures. The
independent Python 3.12.13 lane verified **21/21** constrained packages and
passed **243/243**. The mandatory standalone golden invocation passed
**11/11**.

**Scope correction forward:** v0.15's closing record named `ci_net_test` as an
adjacent local exit-propagation gap. E0 derived the actual pre-fix scope:
**seven** of twenty local job bodies could mask an earlier command failure,
while **zero** hosted workflow steps enter through `ci_local_job`. Step 3 fixed
the job mechanism for all twenty derived jobs and fixed fingerprint cleanup
status separately. The exact evidence candidate then matched every hosted
count, so no published count is false and no retraction is owed. Retractions
remain **three**.

The entering exemption output reconciles as **45 = 18 + 24 + 1 + 1 + 1**:
eighteen structurally derived runner setup actions, twenty-four structurally
derived terminal receipt/attestation actions, one structurally derived
constrained Python installation, one report-only job, and the sole named
operator-local protected-database residual. The count is now parser output,
not a remembered or test-pinned input.

All limitations remain explicit. A rewritten shell can still bypass or falsify
`/attest`, so A4 remains open. An edited L1 controller can still rewrite its
client-side command boundary, so L2 remains open and scheduled. R3 and R4
remain bounded open-bottom deny-lists. The active-runbook measured-value check
remains a same-clause vocabulary heuristic. R11 declares four direct
configuration spellings plus their derived module-local variables, but its
single `fail_before` reconstructs only `open("config/entities.json")`; the
rule's existence is controlled while the rest of its breadth is asserted.
`ARCHITECTURE.md` records this as an open limitation, and closing that
control-breadth gap is the first task for v0.17. No R11 control is changed in
this cycle.

The reviewer-side entering-state assertion that `origin/main` was
`fb2d501e…` is also corrected as evidence, not silently replaced. E0 measured
`origin/main` at publication-audit commit
`0a25c50f9de6a020fa6a04b04847f6242b809f7e`; the earlier specific was an
unverified carry-forward of the prior turn's release-closing commit. This is
the same defect class as any asserted measurement and is logged on the same
terms.

Publication is selected because release-grade evidence exists at the exact
candidate and the local evidence now comes from a harness whose derived job
bodies can actually fail. Withholding would leave `v0.14.1`, produced under
the defective local harness, as the published head while its fix remained
unpublished. The exact release commit, exact-commit matrix, annotated tag
object, and canonical closing record are recorded above. The atomic release
push advanced remote `main` from
`0a25c50f9de6a020fa6a04b04847f6242b809f7e` to closing-audit commit
`b398b88ef3553b83f60f06d0ae14610f0c9474a3` while creating remote annotated
tag object `b7ee3445728e1816e1622c9498ffc2f165ed5dd5`; its peeled target is the
recorded release commit. Publication CI run `30350691515` completed
**success** at that closing commit. This forward state append is the
publication-audit record and changes no release object.

**v0.16 RE-MEASURE is complete (measured 2026-07-28).** The operator
authorized only a non-`main` candidate push. Evidence candidate
`43706216c06608039d9c3e7ef2b86024b22d4a79` was pushed to
`candidate/v0.15.0`; `origin/main` remained
`0a25c50f9de6a020fa6a04b04847f6242b809f7e`, and no `v0.15.0` tag exists.
The remote candidate's `.github/workflows/ci.yml` had blob
`96e85af978981b7af9bdd8e9e11069f158f35e57`, byte-identical to the local
candidate, and was read before dispatch.

Gate correction: Step 7's initial gate named the push authorization but did
not enumerate the local evidence-admission surfaces required by its own
acceptance criteria. Before the first Step 7 commit, the active gate was
widened to the exact candidate/ref and logs, receipts and bundles, report,
manifest, `STATE.md`, active-runbook records, and later progress entry. No
product or closed-cycle path entered scope.

Workflow-dispatch run `30347262430` attempt 1 completed successfully at the
exact candidate. Every required value was read from the hosted logs:
workspace results sum to **126 passed / 0 failed**; the two net legs report
**23** `intel-ingest` and **26** `cored` tests, for **49**; Python 3.11.15 and
3.12.13 each report **242 passed / 1 skipped / 1 third-party warning**. The
collected shell total of **243** equals the local candidate's **243 passed**
under Python 3.11.4 and 3.12.13; only the declared on-site production audit
test skips hosted. `invariant-scan` reports **11/11 rules / 19 controls**,
R10 reports **20** local jobs / **24** local checks, **6** blocking jobs /
**23** hosted checks, and **45** derived exemptions, and golden reports
**11/11**. Every count equals the local measurement at the same candidate.

The six blocking jobs produced exactly the seven workflow-derived identities
`core`, `golden`, `lint`, `msrv`, `net`, `shell/python=3.11`, and
`shell/python=3.12`; report-only drift was skipped. The release-grade audit of
the clean detached candidate required attestations, accepted all **7** signed
receipts, rejected **0**, and measured **5** deferred / **2** promoted. Its
report is `evidence/v0.15.0/deferred-audit/report.json`, SHA-256
`540a721f510ffcc3ae174948f90f5ebef5ececfde0be6cb90bdcbda8ff61c531`,
**34395** bytes; exact-cosine p95 was **8.229917 ms** against the protected
**16.264 ms** A3 anchor. Authenticated re-derivation passed with **7** rows,
**5** source dispositions, **7** triggers, release grade, and attestations
required.

The fourteen receipt/bundle files plus the report add fifteen forward pins.
The manifest now validates at **131/131**: **129/129** evidence plus **2/2**
authorization surfaces. `./run verify-artifacts` and
`./run evidence-report` pass, and both protected databases remain exact
**2/2**. The first post-admission matrix start failed fast at `cycle-check`
because the Step 7 amendment was wrapped across lines instead of using the
validator's exact one-line form. The record was corrected before any Step 7
commit; the complete rerun passed all **20/20** jobs with **126** workspace
tests, **49** net tests, shell **243/243**, `invariant-scan` **11/11 rules /
19 controls**, and all **131/131** pins. The required standalone golden rerun
also passed **11/11**. No published tag, `origin/main`, historical evidence byte, product
runtime path, dependency, lockfile, corpus, or public response changed.

**v0.16 RELOCATABLE is complete (measured 2026-07-28).** Test fixture
resolution now follows the checkout from which the test is run rather than the
checkout in which its binary was compiled.

- The derived Rust set contained **three**
  `env!("CARGO_MANIFEST_DIR")` uses. All three were fixture locators: one
  `cored` workspace-root helper and two `intel-ingest` helpers for crate-local
  and workspace-root fixtures. There were **zero** other uses, and the
  post-fix Rust search finds zero remaining occurrences.
- Both test modules now discover the workspace at run time by walking ancestors
  of the current test directory and checking committed checkout markers. They
  do not derive source paths from the executable, target directory, or any
  build-time source path.
- The E0 fail-before built at `/private/tmp/intel-v016-f3-build`, relocated to
  `/private/tmp/intel-v016-f3-relocated`, and reused
  `/private/tmp/intel-v016-f3-shared` without compilation; **18/24** `cored`
  tests failed at the departed embedded path. The pass-after built at
  `/private/tmp/intel-v016-step6.LX1zfx/build`, relocated to
  `/private/tmp/intel-v016-step6.LX1zfx/relocated`, and reused
  `/private/tmp/intel-v016-step6.LX1zfx/shared-target`; the second cargo run
  reported `Finished` in **0.10s** with no compilation and passed all
  **126/126** workspace tests.
- The full matrix then reused the existing, uncleared
  `/private/tmp/intel-v016-step5-ci-target` and passed **20/20**: **126**
  workspace tests, **49** net tests (**23 + 26**), Python 3.11.4 shell
  **243/243**, warning-denied builds, clippy/fmt/ShellCheck, locked Rust 1.78,
  and golden **11/11**. The standalone post-task golden also remained
  **11/11**.
- Every code change is inside a Rust `#[cfg(test)]` module. No product runtime
  path, public or internal API, dependency, lockfile, corpus, pin, release tag,
  or installed version byte changed. The Step 5 `v0.15.0` release trigger is
  unchanged.

**v0.16 SEAM is complete (measured 2026-07-28).** The operator selected
Option B: extracted candidate names are compared inside core rather than
returning the core's full gazetteer to the shell.

- The shell still owns the LLM call and candidate counts. It sends only the
  distinct extracted names to authenticated internal
  `POST /entities/unknown`; core compares them case-insensitively against the
  names and aliases in its loaded `Gazetteer` and returns only the unknown
  subset. The route refuses service unless `CORE_TOKEN` is configured and
  rejects a request without its matching header. HC3 is unchanged because core
  only inspects supplied strings and never calls a model.
- Gate correction: the initial Step 5 gate widening omitted the two documents
  that enumerate the core contract. The derived route-inventory search found
  `ARCHITECTURE.md` and `README.md` during pre-commit review; both were added
  to the gate and reconciled. This late scope correction is recorded rather
  than treating stale architectural documentation as acceptable.
- The old shell read failed the newly registered R11 before the fix at
  `shell/intel_shell/pipeline.py:139`. After removal, R11 passes and its
  reconstructible control reintroduces a direct
  `open("config/entities.json")` at line 26 and fails there.
  `invariant-scan --self-test` now measures **11/11 rules / 19/19 controls**.
- `CORE_ENTITIES` is the route's single gazetteer source. A live authenticated
  core started with an alternate file containing only `Only From Env` and
  alias `Env Alias`; a request without the token returned **401**, while the
  authenticated route classified both alternate-file values as known and
  returned exactly `{"unknown":["DeepSeek","Novel Entity"]}`. There is no
  working-directory lookup or demo-name fallback in the shell.
- The shell control exercised both outcomes: a core response containing only
  `Novel Entity` excluded the known candidate, while a comparison
  `CoreError("gazetteer unavailable")` made the pipeline return 1 and print an
  error. Missing comparison state therefore cannot silently become a default
  vocabulary.
- The version trigger is **v0.15.0** because the task adds the authenticated
  internal `/entities/unknown` route. The public `/v1/*` surface and golden
  output are unchanged. This does not narrow A4: config ownership and
  untrusted-shell public egress are different seams, and A4 remains open.
- Full permitted `ci-local` passed **20/20** with **126** workspace tests,
  **49** net tests (**23 + 26**), Python 3.11.4 shell **243/243**,
  warning-denied builds, clippy/fmt/ShellCheck, locked Rust 1.78, and golden
  **11/11**. Python 3.12.13 independently passed **243/243** with **21/21**
  constrained packages. The shell delta **241 → 243** is exactly R11's new
  parameterized rule case plus
  `test_pipeline_uses_core_entity_comparison_and_fails_closed`; the workspace
  and net deltas are the single
  `unknown_entity_comparison_uses_the_core_loaded_gazetteer` Rust test.
- The standalone post-task golden remained **11/11**. All **116/116** pins and
  both protected databases remain exact; no dependency, lockfile, corpus,
  public response, published tag, or release commit changed.

**v0.16 EXEMPT-DERIVE is complete (measured 2026-07-28).** R10 no longer
contains a list of action names or receipt-step names, and no test asserts an
exemption total.

- Four executable membership criteria replace the former enumerations:
  a report-only job declares job-level `continue-on-error: true`; a runner
  setup action is an unconditional `uses:` step before the job's first
  command-bearing step; the shell environment setup is the command that
  installs committed `shell/requirements.txt` under committed
  `shell/constraints.txt`; and receipt/attestation persistence is the terminal
  contiguous `always()` block whose steps reference the canonical
  `CI_RECEIPT_PATH`.
- The operator-local `evidence-artifacts:verify` check remains the sole named
  residual. Its reason is environmental rather than structural: protected
  database bytes are operator-local while hosted CI validates the manifest
  schema. An invented class was not introduced for it.
- The parser currently outputs **45** exemptions: **18** runner setup actions,
  **24** receipt/attestation persistence steps, **1** constrained Python
  install, **1** report-only job, and **1** named local residual. The total is
  printed by R10 but not pinned by a test; each reported exemption now carries
  either one of the four criteria or the explicit residual identity.
- Coverage did not narrow. The derived audit compared every blocking hosted
  step's normalized check set with its exemption decision: **zero** steps with
  a parity check moved into an exemption, and every step without a parity
  check matched a declared criterion. No prior exemption moved into coverage.
  Synthetic new setup-action and terminal receipt steps classified without any
  exemption-registry edit.
- R10 passes with **20** local jobs / **24** local checks and **6** blocking
  hosted jobs / **23** hosted checks. Full `--self-test` remains **10/10 rules
  / 18/18 controls**. The focused invariant suite passed **20/20**; full shell
  remained **241/241** on Python 3.11.4 and 3.12.13.
- Golden remained **11/11**. The `run` pin, all **116/116** manifest pins,
  protected databases, product source, workflow, schema, public response,
  dependency graph, and lockfile are unchanged.

**v0.16 JOB-PROPAGATION is complete (measured 2026-07-28).** The task Gate
was widened before implementation to include only the required forward
`config/protected-artifacts.json` update because `run` is an authorization
surface. Historical manifests, release commits, tags, evidence bytes, and
protected databases remain unchanged.

- GNU Bash **3.2.57** reproduced all eight mechanism rows. `if fn`,
  `if ( set -e; fn )`, `if ( set +e; set -e; fn )`, `fn || status=$?`, a
  plain wrapper reached through `|| return`, and background-plus-`wait` reached
  through `|| return` all masked the inner failure and exited 0. A plain
  wrapper called plainly and a separate
  `bash -euo pipefail` process reached through `|| return` exited 1. The
  separate-process mechanism was selected because it preserves propagation
  without depending on every caller's conditional context or sharing
  `cmd_golden`'s `EXIT` trap.
- `ci_local_jobs` is now the single executable job table. Both `cmd_ci_local`
  and R10 parse that table; the help count is computed from it. The derived
  set remains **20** jobs. One generated shell control loops over that parsed
  set, inserts `false` as the first body command for each target, and proves
  every target reports `FAIL` and exits non-zero. A newly appended table entry
  therefore enters the runtime matrix, R10, the help count, and the failure
  loop without a test-list edit.
- `verify_fingerprint_fixture` captures the first validation failure, skips the
  dependent verification, runs cleanup, and returns the captured status unless
  cleanup is the only failure. Its control forced validation failure, observed
  non-zero exit, and confirmed the fixture directory was still removed, so the
  trailing cleanup can no longer turn failure into success.
- F4 is resolved in both halves: `./run help` says **20-job**, where 20 is
  derived, and “stopping on failure” is now true. R10's same-commit control
  mutates the table entry rather than the removed call-site literal and fires
  at `run:352`. R10 passes with **20** local jobs, **24** local checks,
  **6** blocking hosted jobs, **23** hosted checks, and the entering **45**
  exemptions. `invariant-scan` remains **10/10 rules / 18/18 controls**.
- The E0 runner-path finding was also discharged inside Step 3's `run` gate:
  every cored launcher derives its debug binary from `CARGO_TARGET_DIR`.
  A first custom-target golden attempt compiled the correct binary but was an
  environment non-result when the restricted sandbox denied its loopback bind;
  the permitted rerun launched
  `/private/tmp/intel-v016-step3-golden-target/debug/cored` and passed
  **11/11**.
- Full permitted
  `CARGO_TARGET_DIR=/private/tmp/intel-v016-step3-ci-target ./run ci-local`
  passed **20/20**: **125** workspace tests, **48** net tests (**23 + 25**),
  shell **241/241** on Python 3.11.4, warning-denied builds, clippy, fmt,
  ShellCheck, locked Rust 1.78, and golden **11/11**. Python 3.12.13 separately
  passed the same **241/241** with **21/21** constrained packages. The shell
  delta **239 → 241** is exactly the two named tests
  `test_every_derived_ci_local_job_propagates_its_first_failure` and
  `test_fingerprint_cleanup_preserves_the_validation_failure`.
- The forward `run` pin is now
  `f62a5d4f0b8f07d48c194e2d8e3959b5bfe82a3e61a45413452a284ab4dd348d`
  at **41,862 bytes**. All **116/116** pins and both protected databases
  validate. No source under `apps/` or `crates/`, workflow, public response,
  schema, corpus byte, dependency, or lockfile changed.

**v0.16 DOC-LAYOUT is complete (measured 2026-07-28).** The retention
criterion was applied before moving anything: root holds what a reader consults
at the start of every session; everything else lives under `docs/`.

- All **29** cycle documents moved to `docs/cycles/`,
  `intel-platform-OPERATIONS.md` moved to `docs/`, and the operator-supplied
  `REVIEWER-LESSONS-v0.13-v0.14.md` was admitted at `docs/`, for **31** moved
  files total. Pre/post SHA-256 comparison matched **31/31** before the active
  runbook's required checklist update. Representative exact hashes are
  `7876ce03b0b296b75f6fa47ce9fbaef0c6a4d7f5b9c9ffd9cd98aecef0b4be54`
  for the active runbook,
  `995cae491656f775e6a41471c2e0ddebcb451b98d16db9d76b2fa7f7ec0373a7`
  for its progress log, and
  `9df6468ce8827f32517f6e7865bec52d696e2f26361b1470ee734d799ee3ffde`
  for the operations guide.
- The tracked root now contains exactly the six session-entry documents
  (`README.md`, `AGENTS.md`, `ARCHITECTURE.md`, `STATE.md`, `CHANGELOG.md`),
  the runner, and the declared build/config files. Two arguable visible root
  files were not silently classified: ignored `.env` remains in place because
  the runner reads that local credential-bearing configuration, and ignored
  `.DS_Store` is untracked host metadata. Neither is part of the repository
  layout or commit.
- `tools/cycle_identity.py` now owns the sole live location rule,
  `docs/cycles`, and exposes active paths plus task, execution-runbook, progress,
  and shared-legacy-progress resolution. `cycle_check.py`,
  `checklist_audit.py`, `audit_deferred.py`, `progress_check.py`, and their
  tests consume that resolver. A control that leaves same-named root documents
  in place while removing the `docs/cycles` pair fails and names both missing
  canonical paths: there is no live fallback or second glob root.
- `cycle-check` follows Git rename history only to preserve its immutable
  first-committed-runbook comparison across this move; a staged-and-committed
  location-move control passes before and after commit. This history lookup is
  not a live document-location fallback.
- The derived consumer search found the four F6 tools and cycle test, and also
  found a consumer F6 omitted: the operations authority path used by R6 in
  `tools/invariant_scan.py`, `config/invariant-rules.json`, and its focused
  test, plus the current links in `README.md` and `AGENTS.md`. Those paths now
  name `docs/intel-platform-OPERATIONS.md`; R6 and its site-specific mutation
  both pass. No `crates/`, `apps/`, workflow, or Repomix configuration file
  changed.
- `ARCHITECTURE.md §8` now states the planning-versus-artifact convention with
  the measured example: cycle v0.15 shipped artifact `v0.14.1`. `AGENTS.md`
  names the canonical active pair and cites the admitted reviewer-lessons
  document for its two non-executable review-discipline rules.
- Repomix **1.17.0** packed **282** files from the reorganized tree and emitted
  exactly one `<file path="Cargo.lock">`; it also included both active
  `docs/cycles` files. The generated ignored export was moved out of the
  workspace to `/private/tmp/repomix-output-v016-step2.xml`.
- Focused cycle/invariant tests passed **37/37**. Full shell passed **239/239**
  under both Python 3.11.4 and 3.12.13. `cycle-check` reports active v0.16 open,
  thirteen closed execution runbooks, and three historical task documents;
  `checklist-audit` remains **130 checked / 130 matched / 130 resolved**, zero
  exemptions, and the same **three** retractions; `progress-check` resolves E0.
  `invariant-scan` remains **10/10 rules / 18/18 controls**; all **116/116**
  pins and **2/2** databases match; golden remains **11/11**.

**v0.16 E0 is complete (measured 2026-07-28 at activation-audit commit
`90d07721f21f78cc0803facb7138141083104b8e`).** The entering matrix and every
F1–F6 disposition were re-derived rather than carried forward:

- With the ordinary repository target,
  `CARGO_TARGET_DIR=/Users/yzjia/intel-platform/target`, `./run ci-local`
  reached workspace tests and failed: the `cored` binary ran **24** tests,
  **6 passed / 18 failed**, all 18 at `apps/cored/src/main.rs:1558` because its
  embedded checkout path no longer existed. With the fresh explicit target
  `CARGO_TARGET_DIR=/private/tmp/intel-v016-e0-ci-target`, the full command
  passed **20/20** jobs: **125** workspace tests; **48** net tests (**23**
  ingest + **25** cored); shell **237/237** on Python 3.11.4; warning-denied
  offline and net checks; clippy, fmt, ShellCheck, Python 3.11 byte compilation,
  locked Rust 1.78 check/test, golden **11/11**, artifacts **2/2**, and
  invariant-scan **10/10 rules / 18/18 controls**. A clean repository-local
  Python 3.12.13 rebuild independently resolved **21/21** pinned packages and
  passed **237/237** shell tests.
- The fresh-target matrix has a measured path caveat: its Cargo commands used
  `/private/tmp/intel-v016-e0-ci-target`, but `cmd_golden` set
  `CORED_BIN=target/debug/cored` and therefore launched the ordinary target's
  binary after building into the explicit target. A separate
  `./run golden`, with the ordinary target and a freshly built current-checkout
  product binary, passed **11/11**. The runner-path mismatch is carried into
  Step 3's `run` gate; it does not turn the full matrix's Rust measurements
  into a default-target claim.
- The `cmd_ci_local` body parser derived **20** job targets. Every target is the
  left operand of `|| return $?`, and `ci_local_job` reaches it through
  `if "$@"; then`; there were no additional unparsed `&&`/`||` lines and no
  negated job calls. Injecting `false` for the first command of each derived
  body made **13 report FAIL** and exposed **7 that still reported PASS**:
  `ci_deferred_evidence`, `ci_floor_compile`, `ci_shellcheck`, `ci_net_test`,
  `ci_pytest`, `cmd_golden`, and `verify_fingerprint_fixture`. Thus F1 is
  confirmed with seven mask-capable jobs, not the review's lower bound of five.
- F1b's literal answer is **yes, but only through its cleanup**. Replacing both
  fingerprint validation commands with `false` while leaving the final
  `rm -rf` successful made `ci_local_job` return **0**. Replacing the cleanup
  itself with `false` made it return **1**. No preceding validation failure can
  escape while the unconditional trailing cleanup succeeds.
- On GNU Bash **3.2.57(1)-release (arm64-apple-darwin25)**, all eight mechanism
  rows matched the runbook: `if fn`, both conditional subshell variants,
  `fn || status=$?`, a wrapper called with `|| return $?`, and a background
  subshell/wait reached through that call site all printed the post-failure
  marker and exited 0; a plain wrapper and the separately invoked
  `bash -euo pipefail` process exited 1 before the marker. There is no
  operator-shell divergence.
- F2 is confirmed. With
  `CORE_ENTITIES=/private/tmp/v016-alt-entities.json`, an actual invocation of
  the enrichment branch completed but its captured known-name set had **20**
  names from root `config/entities.json` and did not contain the alternate
  file's sole `only_from_env` name. The shell directly reads the core-owned
  path and ignores both the environment override and the seam.
- F3 is confirmed as a verification-reproducibility defect, not a product
  failure. A `cored` test binary built in
  `/private/tmp/intel-v016-f3-build`, then run after that worktree moved to
  `/private/tmp/intel-v016-f3-relocated` with shared target
  `/private/tmp/intel-v016-f3-shared`, was reused without recompilation and
  failed **18/24** tests at the missing compiled-in path. `strings` named the
  departed build checkout. No product request path was exercised.
- F4 and F5 are confirmed: `run:934` says “19-job” and “stopping on failure”
  although the derived matrix has 20 and seven jobs can mask their first
  failure; `config/invariant-rules.json:319` pins R10's control to the defective
  `ci_net_test || return $?` call-site bytes.
- F6's stated totals are refuted but its defect is confirmed. The root contains
  **17** `TASKS-v*.md` files (**14** execution runbooks plus three legacy task
  documents) and **12** `PROGRESS-v*.md` files, not 15 and 11.
  `tools/cycle_check.py`, `tools/checklist_audit.py`,
  `tools/audit_deferred.py`, and `tools/cycle_identity.py` independently
  construct or glob these paths; `shell/tests/test_cycle_check.py` also
  restates them. `AGENTS.md` names the active pair and `ARCHITECTURE.md` names
  the convention. No root Markdown path is protected by a manifest pin.
- Hosted blast radius is **none**: `.github/workflows/ci.yml` contains no
  `ci_local_job` or `cmd_ci_local` invocation; its verification steps invoke
  `./run` subcommands or their commands directly. The independently rerun
  `version-check`, `cycle-check`, `checklist-audit`, `progress-check`,
  `invariant-scan`, `verify-artifacts`, and golden all passed. The annotated
  `v0.14.1` tag object and release commit are unchanged, all **116/116** pins
  and **2/2** protected databases re-verified, and retractions remain **three**.
  No published count is false, so no retraction is owed; F1–F6 are forward
  corrections.

**v0.15 R-CLOSE release reconciliation is complete locally (measured
2026-07-28).** The selected release is **v0.14.1** because Step 4 recorded
that no observable name changed: the `x-intel-view-stage-*` header set and the
four stage strings `analysis`, `response_build`, `sector_load`, and
`serialization` are identical to v0.14.0. That patch trigger fired before
R-CLOSE; the version is not a default chosen at closure.

Evidence and release subjects remain deliberately separate. The authenticated
evidence candidate is
`6d197e562315b4fc6feb20c35b5fadc75b6b44a4`. Release commit
`5c3b6d7fddc30b4691e1e1ee0a6e42831626a1ba` is its descendant and contains
the admitted receipts, report, release authorities, classified diff, and
release reconciliation. Annotated tag object
`deea217b8913ae42399a22424dcf91595ce80240` dereferences to that release
commit, never the evidence candidate.

The complete `v0.14.0..v0.14.1-local-release` diff contains **38 paths**, each
classified exactly once:

- **release authorities and public release documentation (6):** `README.md`,
  `CHANGELOG.md`, `Cargo.lock`, `apps/cored/Cargo.toml`,
  `shell/intel_shell/__init__.py`, and `shell/intel_shell/app.py`;
- **hosted parity workflow (1):** `.github/workflows/ci.yml`;
- **operating contract, architecture, and cycle discipline (4):** `AGENTS.md`,
  `ARCHITECTURE.md`, `shell/tests/test_cycle_check.py`, and
  `tools/cycle_check.py`;
- **workflow-derived receipt identity (2):**
  `shell/tests/test_deferred_audit.py` and `tools/audit_deferred.py`;
- **R10 registry, implementation, and focused tests (3):**
  `config/invariant-rules.json`, `shell/tests/test_invariant_scan.py`, and
  `tools/invariant_scan.py`;
- **Rust/Python stage correspondence (1):**
  `shell/tests/test_benchmark_view.py`;
- **protected manifest and durable hosted evidence (16):**
  `config/protected-artifacts.json`, all fourteen receipt/bundle files under
  `evidence/ci-runs/30333331839-1/`, and
  `evidence/v0.14.1/deferred-audit/report.json`;
- **prior-cycle forward publication records (2):** `PROGRESS-v0.14.md` and
  `TASKS-v0.14-EXECUTION.md`;
- **state, progress, and active runbook records (3):** `STATE.md`,
  `PROGRESS-v0.15.md`, and `TASKS-v0.15-EXECUTION.md`.

Before the mechanical release-authority bump, the cycle changed zero paths
under `crates/` or `apps/`. R-CLOSE changes only
`apps/cored/Cargo.toml` there, from version 0.14.0 to 0.14.1; no product
implementation source changed anywhere under either tree. Cargo mechanically
updates only the local `cored` package version in `Cargo.lock`; dependency
resolution must remain byte-identical.

`ARCHITECTURE.md` already matches enforced reality and needs no release edit.
A rewritten shell can still bypass or falsify `/attest`, so A4 remains open.
An edited L1 controller can still rewrite its client-side command boundary, so
the server-enforced L2 wrapper remains open and scheduled. R3 and R4 remain
open-bottom deny-lists over recognized vocabulary and encodings. The
active-runbook measured-value check remains a documented same-clause
vocabulary heuristic, not semantic proof.

The proposed v0.16 subject is recorded but not acted on. v0.15 is the second
consecutive cycle whose findings all concern verification apparatus rather
than product implementation. Across the recent sequence, `invariant-scan`
grew **7 rules / 11 controls → 9 / 15 → 10 / 18**, shell tests grew **216 →
225 → 237**, and protected pins grew **86 → 101 → 116**. R10 currently
reports **45** exemptions against **24** local and **23** hosted normalized
checks: **18** runner source/toolchain/cache/interpreter setup entries, **24**
signed receipt/attestation persistence entries, one Python-environment setup
entry, one report-only job, and one operator-local database check. The two
large name-enumerated groups should be evaluated as derivable exemption
classes with parser-enforced membership criteria, so their counts become
outputs rather than inputs and the verification apparatus becomes smaller.
Step 8 also exposed an adjacent exit-propagation gap: `ci_net_test` runs the
two net test commands sequentially without returning immediately after the
first failure, so a passing `cored` command can make the wrapper report success
after `intel-ingest` failed. No harness change is made in this cycle. The
observed `intel-ingest` failure was the known proxy-routing non-result in a
fresh worktree without local environment configuration; the exact wire test
passed when rerun with the repository-recorded
`NO_PROXY=127.0.0.1,localhost` path. A complete matrix with that explicit
loopback bypass was therefore required before release and passed **20/20**:
**125** workspace tests, **48** net tests (**23** `intel-ingest` + **25**
`cored`), shell **237/237** on Python 3.11.4, `invariant-scan` **10/10 rules /
18 controls**, protected pins **116/116**, protected databases **2/2**, and
golden **11/11**. The independently rebuilt Python 3.12.13 lane verified
**21/21** pinned packages and passed **237/237**; a separate golden invocation
also passed **11/11**. The first restricted-sandbox attempts at those two
independent commands were environment non-results because loopback binds and
`ps` were denied; their identical permitted reruns produced the stated
measurements.

Publication is selected because the prior withholding condition is discharged:
release-grade evidence exists at the exact candidate, all seven identities
authenticate with zero rejection, and every hosted count equals local at that
commit. A no-release disposition has no remaining trigger. The exact release
commit and annotated tag object are recorded above and in the canonical cycle
closing record. The atomic release push advanced `origin/main` from
`a75c9cf5defa42e985811b01f9905b6ac99797fd` to closing-audit commit
`fb2d501e850fd7c67045b83c475e089f5c5fa535` and created tag object
`deea217b8913ae42399a22424dcf91595ce80240`, which peeled to release commit
`5c3b6d7fddc30b4691e1e1ee0a6e42831626a1ba`. Candidate ref
`candidate/v0.14.1` remained
`6d197e562315b4fc6feb20c35b5fadc75b6b44a4`. Push CI run `30336006396`
passed all six blocking jobs/seven identities; dependency drift remained
report-only and skipped.

**v0.15 RE-MEASURE is complete (measured 2026-07-28).** The operator
authorized only a non-`main` candidate push. Candidate
`6d197e562315b4fc6feb20c35b5fadc75b6b44a4` was pushed to
`candidate/v0.14.1`; `origin/main` remained
`a75c9cf5defa42e985811b01f9905b6ac99797fd`, and no `v0.14.1` tag exists.
The remote candidate's `.github/workflows/ci.yml` had blob
`96e85af978981b7af9bdd8e9e11069f158f35e57`, byte-identical to the local
candidate, and was read before dispatch.

Workflow-dispatch run `30333331839` attempt 1 completed successfully at the
exact candidate. Its six blocking jobs produced the seven workflow-derived
identities `core`, `golden`, `lint`, `msrv`, `net`, `shell/python=3.11`, and
`shell/python=3.12`; the report-only drift job was skipped. Hosted logs report
**125** workspace tests and **48** net tests (**23 + 25**), exactly matching
local candidate measurements. Each hosted shell lane reports **236 passed /
1 skipped**; the collected total of **237** equals the local **237 passed**,
with only the already-declared on-site production audit test skipped.
`invariant-scan` reports **10/10 rules / 18 controls**, and golden reports
**11/11**, both equal to local at that commit.

The release-grade deferred audit accepted **7** receipts, rejected **0**, and
recorded **5** deferred / **2** promoted dispositions. Every persisted
Sigstore bundle verified the expected repository, workflow, candidate digest,
candidate ref, and GitHub-hosted runner identity. Its report is
`evidence/v0.14.1/deferred-audit/report.json`, SHA-256
`f46942dbec8cd258c5daac09bf336770866ef00ab4271539d1510067d5622ef2`,
**34238** bytes; exact-cosine p95 was **8.356958 ms** against the protected
**16.264 ms** A3 anchor. Authenticated re-derivation passed with **7** rows,
**5** source dispositions, **7** triggers, release grade, and attestations
required. The fourteen receipt/bundle files plus the report raised the
manifest from **101** to **116** exact pins: **114** evidence and **2**
authorization surfaces. `evidence_artifacts.py validate`,
`./run verify-artifacts`, and `./run evidence-report` pass; both protected
databases remain byte-identical.

**v0.15 REVIEW-DISCIPLINE is complete (measured 2026-07-28).** Two
v0.14 review lessons are now governing `AGENTS.md` rules. A command-behavior
claim must be verified at the command's entry point, citing v0.14's false
finding from reading `run` without `invariant_scan.py`'s `main()` and its
v0.13 mirror. That rule is explicitly non-executable: source syntax cannot
prove that a human or agent followed a call chain. A closing disposition is
now explicitly an as-of-date claim, so later authorization supersedes rather
than contradicts the historical record.

`cycle-check` prospectively requires the declared runbook's closing record to
use `Release disposition: release|no-release (as of YYYY-MM-DD)`, while
preserving all already-closed runbooks byte-for-byte. The scratch fail-before
produced: `cycle-check: ERROR: TASKS-v1.2.3-EXECUTION.md: declared closed cycle
release disposition must state an as-of date; found undated '- **Release
disposition:** no-release'`, followed by `cycle-check: FAIL (1 defect(s))`.
The dated form passed.

The focused cycle-check module passes **15/15** on both interpreters. Full
shell passes **237/237**, a **+2** delta from CRITERION-SHAPE attributable to
`test_cycle_check_rejects_undated_active_disposition` and
`test_cycle_check_accepts_dated_active_disposition`. `./run ci-local` remains
**20/20**, Rust remains **125** workspace / **48** net (**23 + 25**), all
**101/101** pins and both protected databases remain exact, `invariant-scan`
remains **10/10 rules / 18 controls**, and matrix plus mandatory standalone
golden remain **11/11** byte-identical.

**v0.15 CRITERION-SHAPE is complete (measured 2026-07-28).**
`cycle-check` now evaluates only the active runbook's acceptance-criterion
blocks for cross-step stored quantities. In one clause it requires all three
signals before rejecting: a reference to another `Step N`, a
`recorded`/`measured`/`stored` term, and a
value/count/number/quantity/total term. The scratch fail-before produced:
`TASKS-v1.2.3-EXECUTION.md:9: active Step 2 acceptance criterion cites Step
1's recorded/measured quantity; assert the invariant relation at the same
commit instead`. A same-commit hosted-equals-local relation passed, as did the
current v0.15 runbook.

The check is expressly heuristic and remains an open limitation in
`ARCHITECTURE.md`: paraphrases outside its vocabulary or split across clauses
may escape detection, and unusual intentional prose may need rephrasing.
Closed runbooks are not evaluated; the only changed execution runbook is the
active `TASKS-v0.15-EXECUTION.md`.

The focused cycle-check module passes **13/13** on both interpreters. Full
shell passes **235/235**, a **+2** delta from STAGE-SOURCE attributable to
`test_cycle_check_rejects_cross_step_recorded_quantity` and
`test_cycle_check_accepts_same_commit_quantity_relation`. `./run ci-local`
remains **20/20**, Rust remains **125** workspace / **48** net (**23 + 25**),
all **101/101** pins and both protected databases remain exact,
`invariant-scan` remains **10/10 rules / 18 controls**, and matrix plus
mandatory standalone golden remain **11/11** byte-identical.

**v0.15 STAGE-SOURCE is complete (measured 2026-07-28).** The operator
directed that all observable stage names remain unchanged. A source diff
confirmed no change to `apps/cored/src/main.rs` or
`tools/benchmark_view.py`: the `x-intel-view-stage-*` header set and stage
strings remain identical to v0.14.0, so the Step 4 release trigger is
**v0.14.1**. The active cycle identifier remains v0.15.

The correspondence test reads both source files. It derives
`analysis`, `response_build`, `sector_load`, and `serialization` from Rust's
four literal `diagnostic_delay("…")` call sites and requires that set to be a
subset of Python's `DIAGNOSTIC_HEADERS`. It deliberately does not assert
equality. The seven header-only entries remain untouched:
`handler_total`, `process_main_to_listener_ready`, `store_connection`,
`store_cursor_migration`, `store_fingerprint_backfill`, `store_open`, and
`store_schema_fts`.

The cache-path scope is confirmed from current code: a hit returns before
`compute_view_resp`, so `sector_load`, `analysis`, and `response_build` are
miss-only; `serialization` runs from `into_response` for both hits and misses.
The Rust rename control produced:
`apps/cored/src/main.rs:987: diagnostic_delay stage 'analysis_renamed' is
absent from tools/benchmark_view.py:41: DIAGNOSTIC_HEADERS`. A Python-side
deletion control also failed at the same cross-file seam.

The focused benchmark module passes **6/6** on both interpreters. Full shell
passes **233/233**, a delta of **+2** from IDENTITY-DERIVE, attributable to
`test_rust_diagnostic_delay_stages_are_benchmark_headers` and
`test_stage_correspondence_controls_name_both_files`. `./run ci-local` remains
**20/20**, Rust remains **125** workspace / **48** net (**23 + 25**), all
**101/101** pins and both protected databases remain exact, `invariant-scan`
remains **10/10 rules / 18 controls**, and matrix plus mandatory standalone
golden remain **11/11** byte-identical.

**v0.15 IDENTITY-DERIVE is complete (measured 2026-07-28).** The deferred
auditor no longer declares the current hosted receipt identities in Python.
It reuses R10's workflow parser and derives the exact blocking set from
`.github/workflows/ci.yml`: `core`, `golden`, `lint`, `msrv`, `net`,
`shell/python=3.11`, and `shell/python=3.12`. A job is report-only exactly when
it carries job-level `continue-on-error: true`; no job name is exempted.

Protected deferred-audit reports provide the non-shrinking historical
baseline. The current derived set equals that seven-identity baseline. A
scratch workflow addition appeared in the derived set without a Python edit;
a scratch report-only addition stayed excluded; and removing `golden` produced
the explicit finding `workflow-derived runner identity set narrowed relative
to protected historical evidence` and accepted **0** executions. The legacy
per-job-count path remains unchanged for reports admitted before exact matrix
identities were recorded.

The deferred-audit module passes **40/40** on both Python 3.11.4 and 3.12.13;
the complete shell suite passes **231/231** on both with **21/21** exact
packages. `./run ci-local` remains **20/20**, with Rust **125** workspace /
**48** net (**23 + 25**), zero rustc/clippy/fmt/ShellCheck failures, and locked
Rust 1.78 green. `./run verify-artifacts` validates all **101/101** pins and
both protected databases unchanged. Matrix and mandatory standalone golden
both remain **11/11** byte-identical.

**v0.15 R10-CI-PARITY is complete (measured 2026-07-28).** R10 parses
the existing `run` function bodies/dispatch and the existing workflow jobs,
matrix axes, steps, actions, and commands; it adds no third scope manifest and
requires no correspondence markers. Command entry points normalize to
verification identities, so wrappers are resolved through the functions they
actually execute. The workflow gained hosted Python 3.11 counterparts for
`checklist-audit` and `progress-check`; `ci-local` remains exactly **20** jobs.

On the clean tree R10 reports **20 local jobs / 24 normalized checks** and
**6 blocking hosted jobs / 23 normalized checks**, with **45** explicit
exemptions: one report-only drift job, one operator-local protected-database
verification, 18 runner source/toolchain/cache/interpreter setup steps, one
Python environment setup step, and 24 signed-receipt/attestation persistence
steps. The exact exemption count is test-pinned so growth is not silent.
The one local-only verification is deliberate because the protected databases
are not present on hosted runners; hosted CI validates their manifest schema.

All three R10 site controls fail at the intended location: replacing the local
net-test target reports `run:439`; replacing the hosted `intel-ingest` net
test reports `.github/workflows/ci.yml:221`; adding an unpaired hosted cargo
test reports `.github/workflows/ci.yml:228`. No-argument `invariant-scan`
passes **10/10 rules / 18 controls**. The focused scanner module passes
**20/20** on both interpreters; full shell passes **228/228** on Python 3.11.4
and 3.12.13. The complete matrix remains **20/20**, with Rust **125**
workspace / **48** net (**23 + 25**), all **101** pins and both protected
databases exact, and golden **11/11**.

**v0.15 E0 is complete (measured 2026-07-28 at
`40351d4f33c45db552e72a4ded5e0f29e2cac4f0`).** The permitted
`./run ci-local` passed **20/20** after the first sandboxed attempt stopped only
because loopback binding and macOS network configuration access were denied.
The accepted matrix measured **125** workspace Rust tests, **48** net tests
(**23** `intel-ingest` + **25** `cored`), zero rustc/clippy/fmt/ShellCheck
failures, locked Rust 1.78 green, Python 3.11.4 **225/225**, all **101/101**
pins, protected databases **2/2**, and golden **11/11**. Standalone Python
3.12.13 passed **225/225** with **21/21** exact packages. Standalone
`golden`, `verify-artifacts`, `cycle-check`, `checklist-audit`,
`progress-check`, `version-check`, and no-argument `invariant-scan` all passed;
the scanner remained **9/9 rules / 15 controls**, and the published v0.14.0
tag object and release commit were unchanged.

H1 reproduced in both directions. Removing the hosted
`cargo test -p intel-ingest --features net --locked` step left
`invariant-scan`, `cycle-check`, `checklist-audit`, `progress-check`, and
`version-check` green; the focused invariant/deferred modules passed **53**
with the intended on-site-only test skipped. Removing the local
`ci_local_job "net test (-D warnings)"` line reduced the counted local calls to
**19** while the same tools and focused tests remained green. No existing
check compared the two check sets.

H2 is **partly refuted and remains a derived-scope gap**. Adding a proper
eighth blocking job with receipt emission left `invariant-scan` green, but
`test_every_workflow_job_emits_and_persists_a_receipt` failed because its
separate hard-coded count observed **8 != 7**. Removing the `golden` job and
`("golden", None)` identity did not narrow silently as drafted:
`test_deferred_audit.py` produced **8 failures / 28 passes / 1 skip**, including
the receipt-count check (**6 != 7**) and fixtures that still required seven
identities. The expected identity set is nevertheless still hard-coded and
not derived from `ci.yml`; Step 3 must preserve the existing narrowing
alarms while replacing the duplicated authority.

H3 reproduced. Renaming only Rust's injectable `sector_load` delay string to
`sector_load_renamed` left `invariant-scan` **9/9 / 15**, all **24** offline
`cored` tests, and all **4** benchmark-view tests green. Python's
`DIAGNOSTIC_HEADERS` still named `sector_load`, so the cross-language
correspondence was stale without a failure. The first benchmark-test attempt
was a sandbox-only non-result because its control server could not bind;
the permitted rerun is the recorded pass.

H4 and H5 are confirmed. Before v0.14 amendment `38b316f`, Step 8 required
self-test counts to match “Step 2's recorded values”; the amendment replaced
that stale relation with hosted/local equality at the same candidate commit.
`AGENTS.md` contains neither the command-entry-point review rule nor a rule
requiring the closing disposition field itself to be dated. The originating
v0.14 review record instead explains that reading `run` without
`invariant_scan.py`'s `main()` produced the false finding.

**v0.15 cycle activation is complete; E0 has not yet run (measured
2026-07-28).** The mandatory opener found only the operator-supplied untracked
`TASKS-v0.15-EXECUTION.md`. Entering HEAD was
`a75c9cf5defa42e985811b01f9905b6ac99797fd`, described as
`v0.14.0-3-ga75c9cf`; local `main` and `origin/main` were aligned with zero
ahead / zero behind. Annotated `v0.14.0` remained tag object
`dddc1a52d28a1832727a8d8eb5e87fc7168511c6`, dereferencing exactly to release
commit `4ad4c8d71075731dd87c360e8b0d3d91d80b5518`.

Implementation commit `31916e01098ae9b68d2b6af10877ad91ea6d270f`
admitted only the supplied runbook, the `AGENTS.md` v0.15 declaration, and the
new append-only progress-log skeleton. After that commit, `./run cycle-check`
passed with v0.15 open and twelve closed execution runbooks;
`./run checklist-audit` resolved the entering **121/121** checked tasks,
reported the three existing retractions separately, and found zero exemptions;
`git diff --check` passed. No test, golden, artifact, hosted-runner,
publication, or release claim is made by this preparatory pair. E0 begins from
the clean post-audit tree.

**v0.14 cycle activation is complete; E0 has not yet run (measured
2026-07-28).** The operator selected pre-cycle option (a) and manually pushed
the two v0.13 append-only audit commits. The mandatory opener found only the
operator-supplied untracked `TASKS-v0.14-EXECUTION.md`. Entering HEAD was
`0eff6e4c4987b7ebb138cf0bb1da6ebe8bd851b9`, described as
`v0.13.0-2-g0eff6e4`; local `main` and `origin/main` were aligned with zero
ahead / zero behind. Annotated `v0.13.0` remained tag object
`24a6a2aca52974891d120e0f2b295a93d629c1f7`, dereferencing exactly to release
commit `5ecd42bb6ca44f1588e53e493c67fee17d071b09`.

Implementation commit `b078252c378ca18c65670bae0a3d6d6e0529be09`
admitted only the supplied runbook, the `AGENTS.md` v0.14 declaration, and the
new append-only progress-log skeleton. After that commit, `./run cycle-check`
passed with v0.14 open and eleven closed execution runbooks;
`./run checklist-audit` resolved the entering **111/111** checked tasks,
reported the three existing retractions separately, and found zero exemptions;
`git diff --check` passed. No test, golden, artifact, hosted-runner,
publication, or release claim is made by this preparatory pair. E0 begins from
the clean post-audit tree.

**v0.14 E0 is complete; G1–G6 are measured (2026-07-28).** The restarted
opener found a clean tree at activation audit
`a943b440b7d6de45ad08e857c2e6d26bfab57936`, described as
`v0.13.0-4-ga943b44`, two commits ahead / zero behind reconciled
`origin/main`. The published v0.13.0 tag remained object
`24a6a2aca52974891d120e0f2b295a93d629c1f7`, peeled to unchanged release
commit `5ecd42bb6ca44f1588e53e493c67fee17d071b09`.

The first two workspace-test attempts were environment non-results: cached
Rust test binaries embedded the deleted v0.13 scratch path
`/private/tmp/intel-v013-close.K9cX7L`, so 18 `cored` and then 8
`intel-ingest` tests failed fixture-root canonicalization with `ENOENT`.
`cargo clean` removed that stale shared-worktree cache. A subsequent sandboxed
net lane was another environment non-result because loopback bind and macOS
system-configuration access were denied. The identical permitted, clean-cache
rerun passed **20/20**: **124** workspace Rust tests, **47** net tests
(**23** `intel-ingest` + **24** `cored`), zero rustc warnings, clean clippy,
fmt, and ShellCheck, and locked Rust 1.78 check/test green. Because the clean
matrix reaches shell tests before golden builds `target/debug/cored`, its
deliberately on-site-only production-measurement test was skipped there:
**215 passed / 1 skipped**. After the matrix built the binary, standalone
Python 3.11.4 and 3.12.13 runs each passed the complete **216/216**, and both
verified **21/21** exact packages. Standalone golden repeated **11/11**.
`verify-artifacts`, `cycle-check`, `checklist-audit`, `progress-check`,
`version-check`, and `invariant-scan --self-test` all passed; protected
databases remain **2/2**, pins **86/86**, and the scanner enters at **7/7
rules / 11 controls**.

All six proposed gaps have executable dispositions:

1. **G1 confirmed.** R7 control 2 produced the real finding at
   `apps/cored/src/main.rs:1135`; control 3 produced it at line 1182. Their
   registered `expected_fail` strings and self-test summaries are nevertheless
   byte-identical, so the current control result cannot identify which site
   fired. In a third scratch worktree, shortening R7's hydration regex so safe
   scoped calls were classified as unscoped still made control 2 return status
   1 with its expected substring; it blamed lines 1135, 1182, and 1290. The
   control therefore proves only that the rule failed somewhere.
2. **G2 confirmed with four mutation outcomes.** A renamed production
   threshold seam, `rebuild_identity_with_limit(16)`, outside the store made
   **R1 PASS**. An inference-gateway call named without `openai`, `anthropic`,
   or `llm` made **R3 PASS**. An unknown credential form assigned through
   `INFERENCE_CREDENTIAL` made **R4 PASS**. Renaming both authority markers
   from `MODEL_PROFILE_AUTHORITY` to `MODEL_PROFILE_POLICY` made **R6 FAIL**
   in both governed files. R1 is convention-bound; R3 and R4 are deny-lists
   open at the bottom; R6's enumerated, marker-delimited equality check matches
   its stated scope.
3. **G3 confirmed.** `build_robots_cache` is constructed at
   `apps/cored/src/main.rs:1333`, before the sole listener bind at line 1370.
   R2 constrains loopback validation and the number/form of binds but has no
   identity-order assertion. A statement reorder is detected only by the
   proposed R8; no current check would refuse it.
4. **G4 confirmed.** The v0.13 deferral table's CI-runner row says
   “re-measure at the new release commit only,” while its RE-MEASURE Step 10
   measures the distinct pre-release evidence candidate and no later task
   re-measures the release commit. The two extra post-close audit rounds were
   manual recovery, not a discharging runbook step.
5. **G5 confirmed.** `diagnostic_delay` is called at the serialization,
   sector-load, analysis, and response-build stages and sleeps up to 10,000 ms
   when `CORE_VIEW_DIAGNOSTIC_DELAY_STAGE` and
   `CORE_VIEW_DIAGNOSTIC_DELAY_MS` select a stage/delay. Only
   `tools/benchmark_view.py` names the variables; `.env.example`, `README.md`,
   `deploy/README.md`, and `ARCHITECTURE.md` do not. No startup warning or
   health signal makes a forgotten setting visible.
6. **G6 refuted as a live defect and confirmed as a guard gap.** A locked
   release build completed, and both its symbol table and binary strings were
   free of `test_clear_fingerprint`. Workspace resolver 2 and the
   `apps/cored/Cargo.toml` dev-dependency placement keep the `test-support`
   feature out today. No rule prevents moving that feature edge into
   `[dependencies]`, so R9 remains required to keep the clean property true.

**CONTROL-PRECISION is complete (measured 2026-07-28).** Invariant registry
schema 3 keeps each control's failure message separate from explicit
`expected_file` and `expected_line` fields, requires the expected file to be
the file the control mutates, and requires a positive line number. The
self-test now accepts a control only when one complete rule finding associates
its message with that exact file and line. R6's failure outcome is unchanged;
its report now identifies the first differing authority-block line so it meets
the same precision contract as every other rule.

All **7/7 rules / 11 controls** pass. R7's two formerly indistinguishable
controls now report `apps/cored/src/main.rs:1135` and `:1182` respectively.
A wrong-line registry control fails with `missing expected finding`. The
negative meta-control deliberately reclassified safe scoped hydration calls:
the rule still exited 1 and contained the legacy message at lines 1182 and
1290, but the expected mutated site at line 1135 was absent, so the new
site-specific assertion rejected it. The in-memory matcher mutation was
reverted, and the real self-test returned green immediately afterward. No
R1–R7 matching or allow/deny outcome changed; R6 gained location reporting
only.

The focused invariant module is **13/13**. `./run ci-local` remains **20/20**
with **124** workspace Rust tests, **47** net tests, zero rustc/clippy/fmt/
ShellCheck failures, locked Rust 1.78 green, Python 3.11.4 **218/218**, both
protected databases exact, all **86** pins exact, and golden **11/11**.
Python 3.12.13 independently passed **218/218** and verified **21/21**
packages. The mandatory standalone golden repeated **11/11**.

**RULE-SHAPE-AUDIT is complete (measured 2026-07-28).** R1 now expresses
canonical identity as an allow-list over the five enumerable production store
callers: `append_new`, `update_document`, `delete_document`,
`rematerialize_canonical_ids`, and `commit_harvest_page`. Each must call
`assign_canonical_ids_tx` exactly once; every other production canonical
helper call is refused with its file, line, helper token, and enclosing caller.
The site-specific R1 control plants the renamed
`rebuild_identity_with_limit` seam from E0 and fails at
`crates/store/src/sqlite.rs:672`.

The four required isolated mutation outcomes were re-measured against the
revised rules. The renamed R1 seam now **FAILs** at its planted line. An
unknown inference-gateway call containing none of R3's recognized OpenAI,
Anthropic, or LLM vocabulary still makes **R3 PASS**. An
`INFERENCE_CREDENTIAL` assignment with an unknown value shape still makes
**R4 PASS**. Renaming both governed `MODEL_PROFILE_AUTHORITY` markers still
makes **R6 FAIL** in both enumerated files. R6 was already an exact allow-list
over the two marker-delimited authorization surfaces. R3 and R4 cannot be
converted honestly: both are open-bottom source deny-lists, so their registry
scopes and `ARCHITECTURE.md` now state exactly which unknown vocabulary,
credential names, and encodings remain outside coverage. This narrows no
architectural prohibition; it narrows only the claims made by the scanners.

The full **7/7 rules / 11 controls** self-test passed, and the focused
invariant module passed **13/13** under Python 3.11.4 and 3.12.13. The exact
tree passed `./run ci-local` **20/20** with **124** workspace Rust tests,
**47** net tests, zero rustc/clippy/fmt/ShellCheck failures, locked Rust 1.78
green, both protected databases exact, all **86** pins exact, and matrix
golden **11/11**. The mandatory standalone golden also remained **11/11**.
All four disposable mutation worktrees were removed. No file under `crates/`
or `apps/` changed.

**R8-IDENTITY-BEFORE-BIND is complete (measured 2026-07-28).** The
architecture now states that production `cored` runs its one
`build_robots_cache` crawler-identity construction call before its sole
`TcpListener::bind`; with `net` enabled, that call installs the process-scoped
identity before the listener can accept a request. R8 enumerates those two
production `main` call sites, requires exactly one of each, and compares their
source order.

HEAD passes R8. Three site-specific controls fail independently: moving the
listener bind before identity construction reports the planted bind at
`apps/cored/src/main.rs:1333`; replacing identity construction with a bare
`robots_cache` assignment reports the missing call at line 1333; and adding a
second bind before construction reports two binds at line 1331. The complete
self-test passes **8/8 rules / 14 controls**, and the focused invariant module
passes **14/14** on Python 3.11.4 and 3.12.13.

The first standalone full-shell attempts were sandbox environment non-results:
loopback binds and `ps` inspection were denied after **211** tests passed.
Permitted repeats passed **219/219** on both interpreters. The exact tree
passed `./run ci-local` **20/20** with **124** workspace Rust tests, **47** net
tests, zero rustc/clippy/fmt/ShellCheck failures, locked Rust 1.78 green,
protected databases **2/2**, all **86/86** pins exact, and matrix golden
**11/11**. The mandatory standalone golden also remained **11/11**. No source
under `crates/` or `apps/` changed.

**R9-TEST-SEAM is complete (measured 2026-07-28).** The E0 locked release
build was already clean: `test_clear_fingerprint` was absent from both the
release binary's symbol table and its strings. R9 guards that pre-existing
property; it does not claim to fix a shipped defect. The rule enumerates the
root workspace manifests and permits `test-support` only as its package feature
declaration or on a dev-dependency edge. Any normal, build, target, workspace,
or propagated feature edge that enables it is refused.

HEAD passes R9. Its site-specific control moves the existing
`apps/cored/Cargo.toml` `intel-store` feature activation from
`[dev-dependencies]` into `[dependencies]`; R9 fails at exact line 15 and names
the non-dev section. No manifest or Rust source changed. The complete scanner
passes **9/9 rules / 15 controls**, and the focused invariant module passes
**15/15** under Python 3.11.4 and 3.12.13.

The exact tree passed `./run ci-local` **20/20** with **124** workspace Rust
tests, **47** net tests, zero rustc/clippy/fmt/ShellCheck failures, locked Rust
1.78 green, protected databases **2/2**, all **86/86** pins exact, and matrix
golden **11/11**. Standalone shell runs passed **220/220** under both
interpreters. The mandatory standalone golden also remained **11/11**.

**DIAGNOSTIC-KNOB is complete under operator-selected option (b) (measured
2026-07-28).** The choice and reasoning were recorded before implementation in
the append-only decision checkpoint committed as
`5c0855cbf15d0753d0941083f3086275f15cb834`: retain the benchmark diagnostic,
but make any configured use loud and documented rather than add a second build
configuration or discard the existing decomposition control. This runtime and
operator-surface change fires the **v0.14.0** release trigger; the
documentation-only v0.13.1 path does not apply.

`cored` now emits one startup warning whenever either
`CORE_VIEW_DIAGNOSTIC_DELAY_STAGE` or `CORE_VIEW_DIAGNOSTIC_DELAY_MS` is set.
The warning names both raw settings and the effective delay. The same tested
helper used by the live delay path clamps valid values to **10,000 ms** and
maps missing or invalid values to zero. `.env.example`, `README.md`,
`deploy/README.md`, and `ARCHITECTURE.md` document the four stages, bound,
warning, and unset-by-default operating rule. No `/view` response body changed.

The failure-capable decomposition command measured an analysis median delta of
**122.232000 ms** and a sector-load median delta of **0.186000 ms**, observed
the startup warning in **3/3** delayed core logs, and printed both PASS lines.
Its status **1** is the control's specified success signal. The checker also
rejected a deliberately corrupted warning fixture. Focused benchmark tests
passed **4/4** under Python 3.11.4 and 3.12.13, and the Rust bound/warning test
passed in offline and net builds.

The exact tree passed `./run ci-local` **20/20** with **125** workspace Rust
tests, **48** net tests (**23** `intel-ingest` + **25** `cored`), zero
rustc/clippy/fmt/ShellCheck failures, locked Rust 1.78 green, protected
databases **2/2**, all **86/86** pins exact, and matrix golden **11/11**.
Standalone shell runs passed **221/221** under Python 3.11.4 and 3.12.13, with
**21/21** exact packages on both. `invariant-scan --self-test` remained **9/9
rules / 15 controls**, and the mandatory standalone golden remained **11/11**.

**TEMPLATE-REMEASURE is complete (measured 2026-07-28).** `AGENTS.md` now
requires every non-`none` action in an active runbook's **Deferred means
deferred** table to name an existing discharging `Step N`, and requires every
runbook that changes the release commit to contain a RE-MEASURE step for that
commit. `cycle-check` enforces the row-to-step assignment on the active
runbook only, so closed runbooks and their historical omissions are not
retroactively rejected or rewritten.

The failure-capable scratch test planted a Runner-evidence row whose action was
“re-measure at the new release commit” but named no step. The checker returned
failure and reported `deferred row 'Runner evidence' has a non-none action but
names no discharging Step N`. A companion row assigned to an existing Step 2
RE-MEASURE passed. The focused cycle-check module passed **11/11** under Python
3.11.4 and 3.12.13, and the real v0.14 runbook passed `./run cycle-check`.
No closed `TASKS-v*-EXECUTION.md` file, progress log, or source under `apps/`
or `crates/` changed; v0.13's omission remains intact as the originating
evidence.

The exact tree passed `./run ci-local` **20/20** with **125** workspace Rust
tests, **48** net tests (**23** `intel-ingest` + **25** `cored`), zero
rustc/clippy/fmt/ShellCheck failures, locked Rust 1.78 green, protected
databases **2/2**, all **86/86** pins exact, and matrix golden **11/11**.
Shell passed **223/223** under Python 3.11.4 and 3.12.13.
`invariant-scan --self-test` remained **9/9 rules / 15 controls**, and the
mandatory standalone golden remained **11/11**.

**The Step 8 count amendment is complete (measured 2026-07-28).** One disclosed
Step 8 amendment corrects both appearances of the stale count model. The global
definition now states the measured progression from **7 rules / 11 controls**
to **9 rules / 15 controls**: CONTROL-PRECISION preserves 11 while making
sites explicit, R8 adds three controls, and R9 adds one. Step 8 now requires
hosted and local self-test totals to agree at the same candidate commit and to
equal **9 / 15**, rather than anchoring the hosted result to Step 2's earlier
measurement.

This exact amendment tree passed `./run cycle-check`; the focused checker tests
passed **11/11** under Python 3.11.4 and 3.12.13; `./run ci-local` passed
**20/20**; and standalone golden remained **11/11**. Explicit test discovery
reported **125** workspace tests and **48** net tests split as **23**
`intel-ingest` plus **25** `cored`. The operator subsequently corrected the
24 + 24 expectation; 23 + 25 is the accepted candidate split.

The reusable defect shape is retained for the amendment's append-only progress
record: a criterion tied to one step's measured value goes stale when a later
step legitimately changes the quantity; equality at one candidate commit is
the durable property. A possible sibling to Step 7's active-deferral guard—
detecting acceptance criteria that cite a step's measured value rather than an
invariant relation—is a **v0.15 candidate input only**. It is not implemented
in v0.14. A4 and the editable-L1 controller residual remain open; L2 remains
scheduled.

**The prior RE-MEASURE preflight block is corrected as a syntax-only
non-result (measured 2026-07-28).** The candidate workflow invokes
no-argument `./run invariant-scan`. Both current code and v0.13 evidence
candidate `7faaa4e1271616ff9390111c863d12fbcfa4d2fd` explicitly route a
no-argument invocation through `self_test`; `--self-test` is an equivalent
explicit spelling, not the only execution path. Current implicit and explicit
commands both ended `SELF-TEST PASS (9/9 rules, 15 controls)`.

The retained lint job for v0.13 run **30277584129** contains no invariant
output because invariants ran in the Python 3.11 shell job. That shell log
individually prints all eleven controls and ends verbatim:
`invariant-scan: SELF-TEST PASS (7/7 rules, 11 controls)`. The published v0.13
record specifically attributes the count to the hosted Python 3.11 log, so its
claim is supported. Retraction #4 and the proposed second retraction were not
added; `checklist-retractions.json` correctly remains at three entries.

**SELF-TEST-SCOPE is complete (measured 2026-07-28).** The focused pytest
parameterization now derives its nine rule ids from the loaded registry rather
than `range(1, 10)`, asserts exact registered-id coverage and non-empty
controls, and includes a failure-capable test that omits one id and observes
the coverage assertion. The focused module passed **17/17** under Python
3.11.4 and 3.12.13.

The wiring decision preserves existing behavior: job 20 and hosted Python 3.11
continue to execute the registry-derived self-test through the no-argument
default, while both shell pytest legs independently exercise the derived
focused parameterization. No redundant flag-only edit was made to the
hash-pinned `run` surface or workflow. The active Step 8 criterion now requires
the exact registered-rule and self-test summary lines that hosted CI emits.

The directive review produced three forward corrections. The net split is
**23 + 25**, not 24 + 24. The claim that no hosted job emits self-test output
was refuted by the retained line above. The claim that prior review verified
only the harness and not wiring was refuted by both the v0.13 CLI default and
its retained hosted execution. No closed runbook or progress log was edited.

The exact tree passed `./run ci-local` **20/20**, shell **225/225** under both
interpreters, `invariant-scan` **9/9 rules / 15 controls**, and matrix plus
standalone golden **11/11**. No source under `crates/` or `apps/` changed. A4
and the editable-L1 controller residual remain open; L2 remains scheduled.
RE-MEASURE remains unchecked until the replacement candidate is pushed and
hosted evidence completes.

**v0.14 RE-MEASURE is complete (measured 2026-07-28).** The exact
SELF-TEST-SCOPE audit commit
`ee9ee0f9ed96cb2cb7759c3c3e59fbf8f325ae1a` supersedes `0af15157…` as the
evidence candidate. Only `candidate/v0.14.0` was advanced. Read-only remote
verification resolved that branch to the full candidate, left `origin/main`
at `0eff6e4c4987b7ebb138cf0bb1da6ebe8bd851b9`, and found no `v0.14.0` tag.
Before dispatch, the remote candidate's immutable workflow was read and
confirmed to check out `audit_sha` for the workspace, net, both shell, lint,
MSRV, and golden jobs. No main advance, tag, publication, or live server
session occurred.

Workflow-dispatch run **30324186389**, attempt **1**, used
`publish_evidence: true` and
`audit_sha=ee9ee0f9ed96cb2cb7759c3c3e59fbf8f325ae1a`. It completed success with
exactly seven evidence identities: core, golden, lint, MSRV, net, shell
`python=3.11`, and shell `python=3.12`; report-only drift was skipped.

Every required count was read from its hosted log rather than inferred from
job status:

- workspace results summed to **125 passed / 0 failed**;
- `intel-ingest --features net` reported **23 passed / 0 failed**, and
  `cored --features net` reported **25 passed / 0 failed**, for **48** net;
- Python 3.11 and 3.12 each reported **224 passed / 1 skipped / 1 third-party
  warning**. The complete suite in each leg includes the registry-derived
  invariant-control parameterization; the platform skip does not apply to that
  module;
- Python 3.11 emitted verbatim `invariant-scan: PASS (9/9 registered rules)`
  and `invariant-scan: SELF-TEST PASS (9/9 rules, 15 controls)`;
- hosted golden emitted `golden result: PASS (11/11 checks)`.

The seven downloaded receipt/bundle pairs all name run **30324186389**,
attempt **1**, success, Linux, and both event and checked-out SHA
`ee9ee0f9ed96cb2cb7759c3c3e59fbf8f325ae1a`. The release-posture
`audit-deferred` verification required attestations and checked repository,
workflow signer, source digest, source ref
`refs/heads/candidate/v0.14.0`, and GitHub-hosted runner identity. It accepted
**7**, rejected **0**, and measured **5 deferred / 2 promoted**.

The first detached audit invocation was a setup non-result: the clean worktree
did not contain the intentionally ignored protected databases, so measurement
stopped before attestation verification. Read-only links to the already
verified **2/2** protected bytes restored the complete measurement subject
without making its Git tree dirty; the identical release audit then passed.
The first re-derivation invocation omitted its receipt-directory input and
correctly re-derived CI-runner evidence as deferred. The corrected sandboxed
invocation could not execute GitHub's online attestation checks and produced
the same non-result. The permitted invocation with
`--runner-receipts-dir evidence/ci-runs/30324186389-1` passed with rows **7**,
source dispositions **5**, triggers **7**, release grade, and attestations
required.

Fourteen hosted files plus the **34,076-byte** release audit report add fifteen
forward pins. The manifest is now **101/101**: **99/99 evidence** plus **2/2
authorization surfaces**. Manifest validation, `verify-artifacts`,
`evidence-report`, and deferred-audit re-derivation pass at those exact bytes.
The first standalone golden attempt was a sandbox non-result because loopback
bind was denied; the identical permitted command passed **11/11**.
A4 and the editable-L1 controller residual remain open; L2 remains scheduled.
R-CLOSE and publication remain pending a separate operator decision.

**v0.14 R-CLOSE is locally complete with no release publication (measured
2026-07-28).** The version choice is **v0.14.0** because DIAGNOSTIC-KNOB
option (b) added a startup warning and production code change. That Step 6
trigger fired before R-CLOSE; this is not a default inherited at closure.

Evidence and release subjects remain deliberately separate. The authenticated
evidence candidate is
`ee9ee0f9ed96cb2cb7759c3c3e59fbf8f325ae1a`; the later local release commit is
`4ad4c8d71075731dd87c360e8b0d3d91d80b5518` and contains the admitted
receipts, report, release authorities, classified diff, and closing
reconciliation.

A proposed fourth retraction was investigated and disproved. Retained v0.13
run **30277584129** has no invariant step in lint, but its Python 3.11 shell log
ends verbatim
`invariant-scan: SELF-TEST PASS (7/7 rules, 11 controls)`. The no-argument
default at `tools/invariant_scan.py:1039` calls `self_test` when neither
`--rules` nor `--rule` is supplied. The v0.13 acceptance criterion was
therefore true when checked, and `config/checklist-retractions.json` correctly
remains at **three**. This is a disproved review finding, not a v0.13 or
codebase defect.

The hosted/local shell difference is also reconciled rather than treated as
drift. Both hosted legs report **224 passed / 1 skipped** because
`test_on_site_production_measurements_match_committed_receipt` intentionally
skips when protected corpora and a built `cored` are absent. Those inputs are
present on-site, where both local interpreter lanes pass **225/225**. The
registry-derived control-coverage tests execute in both environments.

The complete `0eff6e4c4987b7ebb138cf0bb1da6ebe8bd851b9..v0.14.0-local-release`
diff contains **37 paths**, each classified exactly once:

- **release authorities and public release documentation (6):** `README.md`,
  `CHANGELOG.md`, `Cargo.lock`, `apps/cored/Cargo.toml`,
  `shell/intel_shell/__init__.py`, and `shell/intel_shell/app.py`;
- **architecture authority (1):** `ARCHITECTURE.md`;
- **diagnostic runtime, configuration, and benchmark control (5):**
  `.env.example`, `apps/cored/src/main.rs`, `deploy/README.md`,
  `shell/tests/test_benchmark_view.py`, and `tools/benchmark_view.py`;
- **operating contract and runbook-lifecycle assurance (3):** `AGENTS.md`,
  `shell/tests/test_cycle_check.py`, and `tools/cycle_check.py`;
- **invariant registry, implementation, and focused tests (3):**
  `config/invariant-rules.json`, `shell/tests/test_invariant_scan.py`, and
  `tools/invariant_scan.py`;
- **protected manifest and durable hosted evidence (16):**
  `config/protected-artifacts.json`, all fourteen receipt/bundle files under
  `evidence/ci-runs/30324186389-1/`, and
  `evidence/v0.14.0/deferred-audit/report.json`;
- **state, progress, and active runbook records (3):** `STATE.md`,
  `PROGRESS-v0.14.md`, and `TASKS-v0.14-EXECUTION.md`.

`ARCHITECTURE.md` matches enforced reality. Its invariant map keeps A4 open
because a rewritten shell can bypass or falsify `/attest`; it keeps the
editable-L1 controller residual open because only the scheduled server-side L2
wrapper can constrain an edited client. Its repository-absence discussion
states that R3 and R4 are open-bottom deny-lists whose unknown vocabulary and
encoding forms remain outside scanner coverage. R8's identity-before-bind
ordering and the bounded, warning-emitting diagnostic delay are also recorded.
No public `/v1/*` body, SQLite schema, dependency resolution, or golden
invariant changed.

The Rust package, Python package, FastAPI literal, this header, and newest
changelog heading now read **0.14.0**. Cargo mechanically changed only the
local `cored` package version in `Cargo.lock` from 0.13.0 to 0.14.0; no
dependency resolution moved. README names the evidence candidate separately
from the later release commit and states that no v0.14.0 tag exists.

The release-facing content passed the complete pre-commit definition of done.
`./run ci-local` passed **20/20** with **125** workspace tests, **48** net
tests (**23 + 25**), warning-denied offline and net builds, clippy, fmt,
ShellCheck, locked Rust 1.78 checks/tests, **225/225** Python 3.11 shell tests,
all **101/101** pins, protected databases **2/2**, persisted fingerprints, and
golden **11/11**. The independent Python 3.12.13 lane passed **225/225** with
**21/21** exact packages, and mandatory standalone golden repeated
**11/11**. `version-check` passed all five 0.14.0 authorities and correctly
warned that the nearest ancestor tag remains 0.13.0. Exact-tag confirmation is
not yet executable because creating `v0.14.0` is explicitly unauthorized.

The identical definition of done then passed again at clean exact release
commit `4ad4c8d71075731dd87c360e8b0d3d91d80b5518`: ci-local **20/20**,
workspace **125**, net **48** (**23 + 25**), Python 3.11 and 3.12 **225/225**,
invariant scan **9/9 rules / 15 controls**, pins **101/101**, protected
databases **2/2**, and matrix plus standalone golden **11/11**. Version-check
passed the five 0.14.0 authorities and retained the expected no-tag warning.

Publication is withheld by a named trigger: a separate operator authorization
must explicitly permit advancing `origin/main` and creating the annotated
`v0.14.0` tag. That trigger has not fired. R-CLOSE creates no remote-main
advance, tag, publication, or live server session.

**The v0.14 closing disposition has a forward supersession (recorded
2026-07-28; publication authorized, mapping not yet claimed).** The closed
runbook's `Release disposition: no-release` and `Tag: not created;
publication is not authorized` statements were accurate as of their
2026-07-28 closing record. Later on 2026-07-28, the operator explicitly
authorized publication. That dated authorization supersedes only the
prospective disposition and tag-not-created clause; it does not rewrite the
historical state at closure. The selected identity remains **v0.14.0**, and
the release subject remains exactly
`4ad4c8d71075731dd87c360e8b0d3d91d80b5518`. The evidence candidate remains
separately named as
`ee9ee0f9ed96cb2cb7759c3c3e59fbf8f325ae1a`.
`TASKS-v0.14-EXECUTION.md` is intentionally unmodified; this is a forward
state record shaped like a retraction, not an edit to the closed runbook.
Remote publication, exact tag-object mapping, candidate deletion, and
post-push CI remain facts to measure and append after they occur.

**v0.15 candidate inputs carried forward from v0.14 review (recorded
2026-07-28; not acted on in this cycle):**

1. **Derive scope rather than assert it.** The formerly unexecuted cored net
   tests, hardcoded invariant-rule range, and deferral actions naming no step
   are one defect at three layers. The individual rules are guarded; the
   hand-maintained machinery selecting which tests and rules run remains a
   candidate for simplification.
2. **Check structural acceptance relations.** An acceptance criterion that
   cites a step's measured quantity rather than an invariant relation is the
   sibling of Step 7's unassigned-deferral gap and may be registerable.
3. **Reviewer-verification discipline.** A claim about what a command does is
   verified at its entry point, not inferred from its caller. The reviewer
   first made the mirrored error of reading the tool without its wrapper, then
   read the wrapper without `main()`. An earlier probe also passed `--rules`,
   the flag that suppresses default self-test, and misread the absent output.
   This belongs as a candidate `AGENTS.md` evidence rule, not a v0.14 change.
4. **Date closing-record dispositions.** A closing record should state its
   release and publication disposition as of a named date, rather than as a
   standing fact. A later operator authorization can then supersede the dated
   disposition without contradicting or editing the closed record. Carry this
   into the v0.15 runbook template.

**v0.14.0 publication is complete (measured 2026-07-28).** One atomic push
advanced `origin/main` from
`0eff6e4c4987b7ebb138cf0bb1da6ebe8bd851b9` to release commit
`4ad4c8d71075731dd87c360e8b0d3d91d80b5518` and created annotated tag object
`dddc1a52d28a1832727a8d8eb5e87fc7168511c6`. Immediate read-only
verification returned `origin/main` and `v0.14.0^{}` at that exact release
commit and `v0.14.0` at that exact tag object. A detached worktree at the tag
reported `git describe --tags --exact-match HEAD` as `v0.14.0`, and
`./run version-check` passed all five 0.14.0 authorities.

Only after the tag mapping passed, `origin/main` advanced through closing audit
commit `53f5133ce12efb4ba2a716576dbbf2c6802b98fb` to forward-supersession commit
`9114ad1ffe572710e9fade1d254a7adb871e4b2e`. Read-only enumeration then
confirmed the candidate branch absent while the v0.14.0 tag remained fixed at
the release commit.

All earlier releases matched the pre-publication baseline byte for byte:
v0.10.3 object `215cfcdbb78e1274a845fdd08a0f17e3d87c94e3` peeled to
`d86ba26e38ff41efbae997a1f909d124a6d6e969`; v0.11.0 object
`fcfa4825e6ffbc06c0ad73e18044965c10786aa8` peeled to
`6daeb7e9f2cc0022b5e1a1dcf2ce8702b5be0321`; v0.12.0 object
`94d8215bc2151fecba1280dc793d3f5953cd8055` peeled to
`e5faf0c161a4256f33976664685653d8bd805d5d`; and v0.13.0 object
`24a6a2aca52974891d120e0f2b295a93d629c1f7` peeled to
`5ecd42bb6ca44f1588e53e493c67fee17d071b09`. Their protected-manifest blobs
also remained respectively `c1f3dcc0607ce323aada025fb6f182f406f92d67`,
`27f152a4497e1bfa61331b8102628c543d231ef8`,
`b1e6a3f9869120725ae572a5c626b93e0871d6f5`, and
`7d1ed9a53aa1fe746bc6fccab8fa9e45b201e882`. The v0.14.0 manifest blob is
`cc14fcb14a4efeb52c976a18c3d0952880da80e4`; current verification remains
**101/101 pins** and protected databases **2/2**.

Push-triggered CI run **30326565779** executed the exact immutable release
commit and completed success: all seven blocking jobs passed, report-only
dependency drift skipped, and the hosted log emitted
`golden result: PASS (11/11 checks)`. The subsequent audit-record push run
**30326618807** executed exact commit
`9114ad1ffe572710e9fade1d254a7adb871e4b2e` with the same seven-success,
one-skipped outcome and the same **11/11** golden line. Neither run is
downloaded, admitted, promoted, or pinned. Release evidence remains dispatch
run **30324186389** against evidence candidate
`ee9ee0f9ed96cb2cb7759c3c3e59fbf8f325ae1a`, and the pin count remains
**101**. A4, the editable-L1 controller residual, and the stated R3/R4
limitations remain open; L2 remains scheduled. No live server session
occurred.

**Historical state appends through v0.13 are archived byte-for-byte at `docs/state-archive/STATE-through-v0.13.md`.**

## 1. Architecture

```text
SHELL (Python, product)   app.py /v1/* · auth.py keys→sectors · llm.py chat+embed
                          prompts.py · briefing.py · pipeline.py · enrichment.py
                          scheduler.py — per-SOURCE and per-sector cadence (v0.6)
        │  CoreClient (core_client.py) — the ONLY door; httpx, injectable transport
        ▼  minimal JSON API, 127.0.0.1:8788, optional x-core-token
CORE (Rust, engine)       apps/cored: /health /sectors /ingest /view /search
                          /retrieve /attest /embeddings(/missing)
                          /signals/record /docs
                          crates: core compliance ingest extract enrich analyze
                                  store registry view retrieve
```

**Config split:** `config/core.json` (sectors/sources/licenses) + `config/entities.json` (gazetteer) are core-owned; `config/subscriptions.json` (clients/sectors/keys) and `config/schedule.json` are shell-owned. Demo keys: `ak_acme_7f3d9c` (science+technology), `ak_quant_2b81aa` (finance).

## 2. Load-bearing placement decisions (do not move these casually)

1. **License gating stays in the CORE, with the A4 trust boundary stated exactly.** `store.search` nulls snippets for IndexOnly; `/view` hydrates evidence with `excerpt: Option<String>` gated by `License::redistributable()`; `/attest` refuses a model answer sharing a measured 16-token normalized phrase with IndexOnly context. `briefing.py` never receives gated text. The shipped `/v1/ask` path submits all cited context ids and uses the returned clean answer, so copied gated context is refused there. A rewritten shell can omit the call or choose a false scope; A4 proved that a context receipt alone cannot make that shell-owned public response non-bypassable. The shell therefore remains in the trusted computing base until public egress itself crosses a core-owned attestation boundary.
2. **Entitlement DECISION in the shell, sector FILTERING in the core.** A shell bug can grant wrong sectors, never bypass filtering.
3. **The core never calls an LLM.** Shell pulls `GET /embeddings/missing`, calls the provider, `POST /embeddings` vectors back. `/retrieve` accepts `model` + `query_vector`; `/attest` only inspects a string the shell hands it.
4. **Full bodies ARE served on internal `/retrieve` and `/docs`** — passing IndexOnly text to a model as context is analysis, not redistribution; loopback-internal, not public.
5. **`/view`'s `kind` is `format!("{:?}", SignalKind)`**, so the shell can post signals straight back to `/signals/record`.
6. All v0.1–v0.3 invariants unchanged: dedup (hamming ≤16) BEFORE all statistics; mentions per (entity, doc); Corroborated suppressed when Rising; discovery on bodies only; FNV-1a determinism; RRF k=60.
7. **(v0.6) Source selection is core business, not shell business.** `/ingest` takes `{sectors, sources?}`. `sources` names connector ids; **each is still validated against `sectors`**, so a named source outside the caller's entitlement is refused, not run — the sector filter is not a suggestion that a source id can bypass (HC2). Selection lives in `registry::select_sources`, which returns `unknown_ids` as **structured per-id errors rather than panicking**. Omitting `sources` entirely preserves the exact pre-v0.6 behavior (every source in the sectors, in config order) — a regression test pins this (HC5).
8. **(v0.6, hardened v0.8/T2) Harvest cursors live in the core store, not the shell.** The `cursors(source_id, cursor, high_water, pending_high_water, updated_at)` row is committed in the **same SQLite transaction** as each parsed page's documents and canonical-id rematerialization. `cursor` is the next OAI-PMH `resumptionToken`; `pending_high_water` retains the max datestamp seen across capped/restarted pages; only a final-page commit clears both and advances completed `high_water`. This prevents either half of the old split-write failure: advancing past documents still in memory, or losing an earlier page's maximum datestamp after restart. High-water advance remains monotonic (ISO dates ⇒ lexicographic max is chronological max). Under HC9's ownership scope, cursors are recorded core-archive state: they belong in SQLite beside the documents whose page commit they make atomic. Connectors that don't page (RSS) ignore the seam entirely.

9. **(v0.6/T6) Provider vocabulary is normalized INTO the neutral one, never the other way round.** `billing.apply_event` speaks `subscription.created|updated|deleted|key_rotated` and nothing else. Stripe enters through `adapters/stripe.py`, which verifies Stripe's signature scheme and maps `customer.subscription.*` onto those events. Consequences worth keeping: a second provider is a second adapter, not a change to the store or the entitlement model; and the freshness check on Stripe's signed timestamp is load-bearing, because a *genuine* captured request replayed later carries a perfectly valid MAC — the timestamp is the only thing that refuses it. Keys are compared against a *set* of active hashes, so rotation has a grace window and revocation is just rotation with none.
10. **(v0.6/T9, closed v0.8.2/A2) Dedup identity is a function of the corpus, not of arrival order.** `dedup_near` keeps the earliest document by `(published_day, id)` — a global property. So `canonical_id` is persisted as a **re-materialization of that same rule on every ingest that adds rows**, NOT as a first-seen-wins assignment at insert. This matters more since T3: sources now run on independent clocks, so arrival order genuinely varies, and an incremental assignment would let two runs over the same 13 documents disagree about which copy is canonical. Relatedly, `/retrieve` deliberately does **not** filter by `canonical_id`: it keeps whichever of a near-dup pair *the query* ranked higher. Canonical id is a property of the corpus; relevance is a property of the question, and context assembly is a question about the question. T3 materializes `simhash(title + body)` at ingest/migration and refreshes it on document update. A2 closes all three consumers: `/view` maps a NULL to a document-naming error; `/retrieve` refuses a fused id absent from the persisted-fingerprint map; canonical assignment reads every row and errors on the first NULL instead of silently excluding it. No request path recomputes a missing fingerprint. `missing_fingerprints()` and `./run verify-fingerprints` name broken rows. B0.2 measured zero such rows and zero NULL canonical ids in both protected archives, so this repair closes the structural guarantee without changing their corpus identity.

**2.11 — robots.txt is DISCOVERED, and the two gates compose one way only (T2, v0.7).**
There are now two robots checks, and the order and direction matter:

- The **publisher's** policy, fetched from their real `/robots.txt` (`RobotsCache`, in `crates/compliance`). Per-origin, TTL 24h, bounded to 512 origins, and the fetch itself goes through the same per-host politeness limiter — it would be a strange kind of respect to skip the rate limit for the one file that describes how to be respectful.
- The **operator's** configured deny-list (`RobotsGate::new(&["/private","/admin"])`), which applies *on top* and can only ever refuse **more**. A publisher blessing `/private` does not oblige us to crawl it.

Three decisions inside this that are easy to get wrong and are therefore pinned:

- **Fail-closed, and the 4xx/5xx distinction is not cosmetic.** RFC 9309 gives three outcomes, not two. **2xx** ⇒ the body governs (an *empty* body is a valid allow-all, and is **not** the same thing as a 404). **5xx / DNS / TLS / timeout** ⇒ "Unreachable" (§2.3.1.4): we do not know the policy, so we take nothing. **4xx** ⇒ "Unavailable" (§2.3.1.3): the RFC permits full access, and here we **knowingly diverge** — `MissingPolicy::Deny` is the default, because we fetch a small operator-configured set of publishers rather than discovering the open web, and the cost of wrongly fetching from someone who never published a policy is a compliance incident while the cost of wrongly *not* fetching is a log line. `MissingPolicy::RfcAllowAll` is available and named, so the divergence is a choice rather than a buried `else`.
- **A fixture read is not a request.** `gate()` takes a `Reach` (`Network` | `Fixture`). A fixture-backed source never fetches `robots.txt` — an "offline, deterministic" run that quietly phones example.org for permission to read a file already on disk would be both a surprise and a lie about what offline means. Tested directly: `a_fixture_fetch_never_asks_the_publisher_for_permission` asserts **zero** fetches even on a `net` build with a cache wired in.
- **A published `Crawl-delay` can only slow us down.** `apply_crawl_delay` adopts a publisher's stated cadence only if it is *slower* than our own floor (2 rps). A `robots.txt` must not be able to talk us into hammering a server faster than we would have gone anyway.

**Consequence, and it is the reason this could not just be dropped into the handler:** politeness state is now **process-scoped**, not request-scoped. `HostLimiters` and `RobotsCache` moved into `AppState`. They used to be rebuilt inside `/ingest`, which meant two ingests a second apart each started with a clean limiter and neither waited for the other — and a per-request robots cache would have re-fetched every publisher's `robots.txt` on *every ingest*, i.e. a "compliance" feature that made us a **worse** citizen than before. A TTL only means something if the cache outlives the request.

**2.12 — the 404 disposition is PER-SOURCE, and the operator's config is the opt-in (v0.7.1).**
v0.7 made the 404 decision cache-wide (`MissingPolicy::Deny`, with an `RfcAllowAll` override on the whole cache). The first live harvest proved that granularity wrong: arXiv's OAI-PMH host serves no robots.txt, and one blanket policy forces a false choice — fail closed and block a cooperative source, or open the 404 door for *every* source at once. Neither is right.

So the disposition now lives on the **source**, threaded `SourceCfg.robots_on_missing → {RssSource, ArxivOaiSource} → gate(…, on_missing) → RobotsCache::allowed(…, on_missing)`. Three properties are load-bearing and pinned:

- **Default is `Deny`, and a typo fails closed.** `MissingPolicy::from_config_str` maps `"allow"` (and synonyms) to `RfcAllowAll` and *everything else, including absent and misspelled,* to `Deny`. A source you forget to annotate, or annotate wrong, is conservative — never accidentally permissive. Every source except `arxiv-cs` is `Deny` today.
- **Opting in reinterprets ABSENCE ONLY.** `robots_on_missing: "allow"` changes the 404 case and nothing else. An explicit `Disallow` from a real robots.txt is still obeyed (tested: `opting_in_does_not_bypass_an_explicit_arxiv_disallow`), and an `Unreachable` origin (5xx/timeout) still fails closed. "Allow if absent" must never quietly become "ignore robots.txt."
- **The justification is the architecture's own principle, applied.** Entitlement decisions live with the operator, not in the fetch layer; the publisher's robots.txt is a *technical* access policy layered on top. An operator configuring `arxiv-cs` against a standards-compliant, harvest-designed endpoint *is* the opt-in. Encoding that as one auditable per-source line is the correct shape — as opposed to a global flip, which is what the on-site tester reached for (and which, being applied to a `#[default]`-attribute default via `sed` on the literal string, changed a doc comment and nothing else).



**Toolchain matrix (v0.7 — every cell RUN, none inferred). The 1.75 and 1.76 rows are new, and they are why §5's floor claim changed:**

| toolchain | `check`/`test --workspace --locked` | `-p cored --features net` |
|---|---|---|
| 1.75.0 (stock Ubuntu 24.04 `rustc`) | ❌ `lock file version 4 requires -Znext-lockfile-bump` | ❌ `failed to download replaced source registry` (the edition2024 masquerade) |
| 1.76.0 | ❌ same lockfile parse failure | ❌ |
| **1.78.0 — the floor** | **0 warnings, 75 green** | ❌ |
| **1.91.1 (pinned)** | **0 warnings, 75 green** | ✅ **clean, `--locked`, `-D warnings`** |

- **The v0.6.2 lockfile bug, measured.** Against the committed **v4** lock, cargo **1.75 and 1.76 cannot even parse it** — v4 needs cargo ≥ 1.78. v0.6.2's "verified green on 1.75" was therefore impossible; it had never been run.
- **And the fix that looked obvious is a trap, which is worth more than the fix.** Re-encoding the lock to **v3** genuinely restores 1.75 (verified: **75 green**, and the package set diffed **byte-identical** — same names, versions, checksums, so it is a format change and not a resolution change). But **cargo 1.91 rewrites the lock back to v4 as soon as it modifies it** — confirmed here by bumping `cored`'s version and watching a plain `cargo check` silently re-emit v4. v3 is a hand-edit with a half-life. **We therefore ship the sustainable floor (1.78) rather than the flattering one (1.75)**; local commands enforce it, and v0.10/G2 observed the configured runner job pass.
- `cargo check --workspace --locked --all-targets` with `RUSTFLAGS=-D warnings`: **0 warnings**. Same for `-p cored --features net --locked --all-targets`.
- `cargo test`: **75 green** — compliance **26** (was 7), ingest **14** (was 7), core 7, cored 7, registry 4, retrieve 3, extract 3, enrich 2, store 9. `cargo test -p intel-ingest --features net --locked`: 14 green.
- `pytest shell/tests`: **69 green**, unchanged — T2 is entirely below the seam, and the shell suite still needs no Rust toolchain.
- **T4's own testing objective, executed:** a deliberate warning (`let x = 1;` unused) introduced into `crates/extract` makes `RUSTFLAGS="-D warnings" cargo check --locked` exit **101**. The gate bites. Restored; clean.
- **Golden E2E re-verified live from a clean DB after T2 — every number identical:** acme ingests **13** (Finance skipped), dedup drops `techwire::tw-004` keeping `osdaily::osd-004` (hamming **12**) ⇒ **12 analyzed**; **DeepSeek RISING z=10.0** corroborated by 3 sources (arxiv-cs, osdaily, techwire); vLLM RISING z≈**2.67**; NVIDIA + Qwen **CORROBORATED**; **"Helios Labs" EMERGING**; immediate re-run **+0 new**; quant-desk sees only its **1** doc.
- **Public API spot-checks live:** bad key ⇒ **401**; entitlement-disjoint search (**acme 6 hits vs quant 0** for "deepseek"); all 4 IndexOnly hits return `snippet: null`; the brief renders "excerpt withheld" (10 occurrences).
- **T2 live-path proof, offline:** the `RobotsFetcher` seam is driven by a fake through every branch — 200-with-body, 200-empty, 404, 500, unreachable, malformed HTML-served-as-200 — so fail-closed is *tested*, not asserted. TTL expiry is tested deterministically with `tokio::time::pause()`, not by sleeping.

## 4. Next steps

**Done in v0.7:** ~~T2 (real robots.txt)~~ · **T4 workflow configured + MSRV
verified locally; no CI runner evidence** · **T5 built, measured, and rejected**
(§6c).
**Deferred in v0.7, each with the gate that deferred it:**

1. **T1 — the first live arXiv harvest. DEFERRED: no egress. Verified, not assumed.** `curl -sI https://export.arxiv.org/oai2?verb=Identify` ⇒ **HTTP 403, `x-deny-reason: host_not_allowed`** — the sandbox proxy refuses the host, exactly as in v0.6. The task's own gate is explicit ("no egress ⇒ defer and say so; **do not mock a live harvest and mark it done** — the entire value of this task is that it is not a mock"), so nothing was faked. **This is now the single highest-value item in the project, and it is not a code problem:** `--features net` builds, paging + cursors are implemented and unit-tested, the limiter and `Retry-After` handling exist, and **as of T2 the robots gate will do a real fetch before the first request**. On any box that can reach arXiv: `cargo build -p cored --features net --locked`, drop the `"fixture"` key from `arxiv-cs` in `config/core.json`, `POST /ingest {"sectors":["science"],"sources":["arxiv-cs"]}`. **HC13 stands: fixtures prove the state machine, not the wire.** The things that genuinely cannot be tested here are a real `503 Retry-After` under load, observed ≥3s page spacing on the wire, real-world XML edge cases, and cursor durability across a real interrupt.
2. **T4 (v0.7/T3) — point the LLM at a real endpoint. DEFERRED at the credential/configuration gate, and deliberately NOT mocked-and-declared-done.** Re-probed 2026-07-20: DeepSeek and OpenAI now both return unauthenticated **401**, so egress is available; however `LLM_BASE_URL` and `LLM_API_KEY` are absent and no local vLLM listener exists on 8000/8899/11434. `./run verify-llm` exits 2 before model work. A configured endpoint and credential from the operator are still required; then `tools/verify_llm.py` runs the checklist.
3. **T6 — seam hardening for multi-host. DEFERRED: condition still not met.** Core and shell still run on one host (`cored` binds `127.0.0.1:8788`; `deploy/intel-pipeline.service` sets `CORE_URL=http://127.0.0.1:8788`). `CORE_TOKEN` is implemented on both sides. Per the task's own instruction, no speculative UDS and no mTLS were written. **Trigger:** the first genuine cross-host split.
4. **T7 — scale swaps. DEFERRED (design-level), and T5 *removed* LSH from this bucket rather than promoting it.** Postgres remains a **concurrency** trigger (a second writer), not a size one, and may never fire.
5. **T8 — known-limitation pick-ups. All three SKIPPED on their own stated preconditions, which were checked rather than assumed.** (a) Materialize `/view`: the precondition is "if warm-up cost shows up" — the corpus is 12 documents; it has not. (b) One SQLite connection behind a `Mutex`: the trigger is a second writer; there is none. (c) A rebuild tool for pre-v0.6 `Day` encodings: the task says *"check before building it"* — **checked, and no such archive exists.** `/data` is gitignored and archives are never shipped; every DB reachable on this box was created fresh this session from fixtures, on the new encoding. Building the tool would have been building for a hypothetical.

**The recommended top of the v0.8 queue, in order:**

1. **The live arXiv harvest** (T1 above), the moment a box with egress exists. Everything is ready; nothing else can falsify the paging.
2. ~~**Persist the SimHash fingerprint.**~~ **COMPLETED in v0.8/T3.** The column and ingest write already existed when the step began, but `/view` still recomputed every fingerprint and no pre-column migration existed. Dedup now accepts persisted fingerprints, document updates refresh them, and the backfill was verified over a disposable pre-column copy of all 1,764 live rows with zero fingerprint or canonical-id mismatches. The golden result did not move.
3. ~~**Turn on `clippy` + `rustfmt` in CI.**~~ **CONFIGURED in v0.8/T6; first observed in v0.10/G2.** The job was not commented out; it was report-only, and B0 measured one clippy diagnostic plus 13 files of fmt drift. T6 fixed those findings in `097b017`, verified both commands clean locally, then configured the job as blocking in the separate gate commit. G2's first real runner execution observed the blocking job pass in 44 seconds.

## 5. Known limitations (documented, not hidden)

- ~~**Robots policy is configured, not discovered.**~~ **RESOLVED in v0.7 (T2)** — see §2.11 and §6b.
- ~~**"Rust 1.75 + `--locked` still builds the offline path."**~~ **FALSE, and it is the most important correction in this document.** The committed `Cargo.lock` is format **v4**, unparseable by cargo before **1.78**, so the claim could never have held — it had simply never been run. **The offline floor is now declared as 1.78**, measured locally across 1.75/1.76/1.78/1.91 and observed on the v0.10/G2 runner as Rust 1.78.0. Re-encoding the lock to v3 *does* buy back 1.75 (75 tests green, resolution byte-identical) but cargo ≥ 1.78 rewrites it to v4 on the next lock modification, so that floor cannot be held. **The general lesson: a claimed property that nothing executes is not a property, it is a wish** — the same failure that let `--features net` sit broken for two cycles and that let "robots-compliant" mean "compliant with a policy we wrote ourselves."
- **The `--features net` floor is 1.86, and the error lies about why.** `icu_* 2.2.0` (via `idna_adapter`) declare `rust-version = 1.86`; edition2024 stabilizing in 1.85 is necessary but **not** sufficient. Worse, the failure surfaces at *dependency-download* time as `error: failed to download replaced source registry 'crates-io'`, which sends you looking at the registry instead of at MSRVs. Reproduced again this cycle on 1.75.
- **Correction to a v0.5 note** (unchanged from v0.6): `/v1/ask`'s `context_suppressed` names `techwire::tw-004`, not `osdaily::osd-004`, for the question actually tested. Suppression at context assembly is **rank-aware by design**, so which copy of a syndicated story is dropped depends on which one the query ranked higher. Treat *"one of the pair is suppressed"* as the golden, not a specific id.
- **`Day` values changed scale (T9.3).** `published_day` is days-since-1970. Pre-v0.6 archives spanning a month boundary would need a rebuild — **checked in v0.7: no such archive exists**, so no tool was built (T8.3).
- ~~**`dedup_near` recomputes every fingerprint on every pass.**~~ **RESOLVED in v0.8/T3.** The store materializes the fingerprint and `/view` passes it into `dedup_near`; a deliberately violating test double proves the function consumes the supplied value rather than recomputing it.
- `/view` is memoized per (sector-set, generation) rather than materialized; a restart re-warms it. Cost is unmeasurable at 12 docs.
- One SQLite connection behind a `Mutex` (fine: the shell is the single caller); `cored` binds loopback by design.
- ~~**HC1 was not enforced on `/v1/ask`, and its test was vacuous.**~~
  **RESOLVED in v0.8/T1.** The model still receives capped IndexOnly bodies as
  internal analysis context, but its answer now goes to core `POST /attest`
  with the exact context document ids before any public response. The core
  checks normalized 16-token overlap only against `IndexOnly` bodies and
  replaces the entire answer with a constant refusal on any violation; `CcBy`
  quotation remains allowed. `tools/mock_openai.py --leak` deliberately emits
  a source sentence. Both the shell test and a real Rust↔HTTP↔Python E2E proved
  that sentence cannot pass, while the ordinary golden answer is unchanged.
  **A4 scope correction (2026-07-24):** this is structural for the shipped
  shell path, not for an arbitrary shell rewrite. The proposed receipt lacks a
  non-shell-controlled correlation to the prompt and cannot force the shell to
  call the endpoint, so that stronger claim is an accepted risk with the
  trigger recorded in §2.1 rather than a shipped mechanism.
- ~~**The robots gate was checked only on the configured origin while reqwest followed redirects automatically.**~~ **RESOLVED in v0.8/T5.** Both HTTP clients now set `Policy::none()`. Document redirects are resolved manually with the full gate before each next request; robots-file redirects fail closed. A failure-capable cross-origin 302 test makes the second body available, configures that origin to disallow it, proves both robots policies were fetched, and proves the second document request never happened. A same-origin redirect makes two document requests with exactly one robots fetch.
- **The robots cache does not de-duplicate concurrent misses.** Two simultaneous first-requests to the same origin can both fetch `/robots.txt`. Bounded, harmless (the limiter still spaces them). **T7 rechecked the trigger on 2026-07-20 and deferred the lock:** the supported scheduler remains one synchronous writer and the deployment unit is one-shot; revisit only when a second concurrent harvester actually exists.

## 6. Decision log

### 6a. Why `feed-rs` was NOT adopted (v0.6/T2)

The task set a three-clause gate; the swap tripped **all three** in v0.6.1, and the gate was **re-run** in v0.6.2 because clause 1 was a statement about a toolchain we had just changed. A decision log that keeps a dead reason is worse than no decision log.

1. ~~**It doesn't build on our toolchain.**~~ **STRUCK — no longer true.** `feed-rs 2.x` builds clean on 1.91.
2. **Footprint. STILL TRIPS.** 56 unique transitive crates, against 16 for the entirety of `intel-ingest`. It drags `chrono`, `quick-xml`, `regex`, `url`, `aho-corasick`, `mediatype`, `serde_json` to parse two small formats `roxmltree` already parses.
3. **Parse-equivalence breaks. STILL TRIPS.** `feed_rs::model` types timestamps as `Option<DateTime<Utc>>` (chrono, not our ordinal `Day`) and differs on id fallback. Adopting it would **silently move document ids** — the one thing a swap in this crate must never do.

**Decision unchanged: skipped**, now resting on cost and correctness rather than on a compiler we no longer run.

### 6b. Why `texting_robots` was NOT adopted (v0.7/T2)

The same three-clause shape, run against the crate the task named as "the noted drop-in."

1. **Builds on 1.91? PASSES.** It compiles cleanly.
2. **Transitive footprint? FAILS, and disqualifyingly.** It resolves **45 transitive crates** into `intel-compliance`, which today has **one** dependency (`tokio`) — 7 crates in its whole tree. Worse than the count: it pulls `url` → `idna` → `idna_adapter` → **`icu_collections` / `icu_normalizer` / `icu_properties` / `icu_provider` 2.2.0, all declaring `rust-version = 1.86`.** Those are *the exact crates* that walled this project for two cycles (§5). And `intel-compliance` is a **non-optional dependency of `intel-ingest`, which is in the default build graph** — so adopting it would have dragged the icu chain into the **offline** build and silently raised the offline MSRV from 1.75 to 1.86, destroying the very property v0.6.2 fought for and `rust-toolchain.toml` still promises. *We would have re-created the disaster we had just finished cleaning up, in the name of compliance.*
3. **Does it change any existing allow/deny outcome? NO — and this is the clause that paid for the whole evaluation.** Rather than take the dependency, `texting_robots` was used **out of tree, once, as a differential oracle** against the hand-rolled parser: **16 `robots.txt` bodies × 22 paths + crawl-delay = 368 verdicts, 0 divergences.** Wildcards, `$` anchors, `Allow` exceptions, equal-specificity ties, longest-UA-token-wins, a `User-agent` line after a rule starting a *new* group, empty `Disallow:` meaning allow-all, comments-only files, rules before any UA line, and an HTML error page served as a 200 — all agree.

**Decision: skipped.** We shipped a **zero-new-dependency** parser (`async-trait` was already in the graph; the `Cargo.lock` diff is **one line and zero new crates**, versus 45) that is *proven* equivalent to the battle-tested one. The correctness assurance was the valuable part of the crate; the dependency was the expensive part. We took the first and left the second.

### 6c. Why LSH banding was BUILT, MEASURED, and REJECTED (v0.7/T5)

`docs/T8-scale-design-note.md` called LSH "the swap most likely to be needed first." That was a **hypothesis about where the time goes**, and T5's gate demanded exact recall at hamming ≤ 16. So it was built and measured (`cargo run --release -p intel-extract --example dedup_bench`, committed). **Both halves of the hypothesis are false.**

| n | simhash (linear) | pairwise scan (quadratic) | scan share | banded LSH | pairs still compared | recall |
|---|---|---|---|---|---|---|
| 1,000 | 69.6 ms | 1.3 ms | 1.8% | 90.2 ms | 76.2% | 100% |
| 5,000 | 359.7 ms | 31.7 ms | 8.1% | 5,801 ms | 76.1% | 100% |
| **10,000** | **734.3 ms** | **125.9 ms** | **14.6%** | **30,962 ms** | **76.1%** | **100%** |
| 20,000 | 1,473.9 ms | 509.8 ms | 25.7% | **OOM (~4.5 GB)** | — | — |

1. **The quadratic scan is not the bottleneck.** At n = 10k it is **14.6%** of dedup time. The other **85%** is *fingerprinting* — `dedup_near` recomputes `simhash()` for every document on every call. A hamming comparison is one XOR and a popcount (~1 ns); fingerprinting a 2 KB body costs ~70 µs. The quadratic term does not overtake the linear one until roughly **n > 100k**. We were about to optimize the cheap half.
2. **Banding cannot prune at this threshold anyway — and this is arithmetic, not implementation.** `dedup_max_distance` is **16** on a **64-bit** fingerprint. Exact recall requires, by pigeonhole, *more bands than the distance* (b ≥ 17), so bands are 64/17 ≈ **3.8 bits** wide. A 4-bit band has 16 possible values, so an average bucket holds n/16 of the corpus and nearly everything collides with nearly everything. Measured: it still compares **76% of all pairs** and runs **246× slower** than the scan it replaces. Recall *is* exactly 100%, as the math promises — **the index is correct and useless.** At n = 20k the candidate set alone tries to allocate ~4.5 GB and aborts.

**The rule worth keeping:** *an LSH band's selectivity depends on the threshold as a **fraction** of fingerprint width, not its absolute value.* 16/64 = 25% divergence is far outside the regime where any exact Hamming index beats a linear scan. Widening the fingerprint does not help if the threshold widens with it; it helps only if the *absolute* distance stays at 16 (e.g. 16/128), and that is **a different similarity rule** — it changes which documents are duplicates, which is corpus corruption, not an optimization. T5's gate says stop, and it was right to.

**Decision: not merged.** The design note has been corrected in place, and the swap it should have named — **persist the fingerprint** — is now the recommendation in §4.

### 6d. Why non-loopback `CORE_BIND` has no override (v0.11/BIND-LOOPBACK)

**Decision:** resolve `CORE_BIND`, require every result to be loopback, and
refuse startup if any address is not. There is deliberately no warning-only
mode and no override environment variable. An override would preserve the
original unauthenticated remote-exposure defect behind one extra setting. A
real requirement to bind beyond one host is the documented multi-host seam
trigger: it needs a design task that defines transport authentication,
authorization, and deployment topology before the boundary can move.

`CORE_TOKEN` remains optional. With loopback enforced structurally, the token
is defense-in-depth against unrelated local processes, not the mechanism that
makes the core private and not a substitute for shell entitlement. Making it
mandatory would break existing same-host deployments while adding no remote
protection beyond the enforced bind. Operators that need the extra local
boundary may continue to set it; the shipped launcher and service contract are
unchanged.

### 6e. Why `/embeddings/missing` has no HC2 exception (v0.11/SECTOR-BIND)

**Decision:** take the preferred sector-bound outcome. `/embeddings/missing`
enumerates document bodies, so it now requires an explicit sector list and
enforces it in core SQL just like `/docs`; HC2 has zero unnamed or named
body-returning exceptions. The alternative maintenance exception was rejected
because the predicate is cheap and an exception would preserve the broader
enumeration seam that triggered this task.

The embedding worker sends the core's full configured sector set, not the
current subscriber's entitlements. Backfill is archive maintenance and must
not become dependent on which subscriber runs first; the explicit full set
keeps that intent visible while the core still refuses an empty scope. `/docs`,
by contrast, receives the current subscriber's entitled sectors because it
serves that subscriber's downstream enrichment path.

### 6f. Why network reach and publisher policy remain runtime-checked (v0.11/GATE-CLOSED)

**Decision:** reject `Reach::Network` plus `robots_cache: None` at the shared
gate rather than redesign `SourceContext` in this patch cycle. The type-level
alternative would make that state unrepresentable, for example by separating
offline and network contexts or coupling reach and cache in an enum. It would
also change the connector trait boundary and every fixture, cursor, registry,
and builder call site even though the shipped net builder already constructs
the cache correctly.

That broader migration is deferred because its boundary cost is disproportionate
to this dormant single-field omission seam. The runtime check sits at the last
shared point before every network fetch, has a dedicated error, and is covered
by the inverted defect control. If new connector kinds make context construction
harder to audit, the type-level design should be reconsidered as its own
architectural task rather than folded into this narrow correction.

### 6g. Why private-network coordinates are documentation, not credentials (v0.12/INFRA-POLICY)

**Decision: Option A, selected by the operator on 2026-07-27.** The repository
may document RFC 1918 host `192.168.0.192` and loopback-forward ports such as
`18080`/`18081`; neither grants access without already having the operator's
LAN or local-machine route. The enforceable prohibition is against
secret-bearing material: tracked `.env` files, provider keys, tokens, private
key material, concrete long bearer values, non-placeholder secret assignments,
and raw secret-bearing response fields.

The v0.11 standing clause saying that the host and forwarded ports “appear in
no committed file” was false when written and unexecuted for its entire life.
v0.12 E0's tracked-path scan found 11 matching paths, including the already
committed `.env.example`, `README.md`, `shell/tests/test_llm_config.py`,
`PROGRESS-v0.9.md`, and `STATE.md`; ten of the 11 predated the v0.12 runbook.
No guard ever evaluated that clause. Option B was rejected because no specific
threat model makes private coordinates confidential, while append-only
historical records would make a host/port ban permanently incomplete.

Registered invariant R4 now scans every Git-tracked text file and makes the
credential rule executable. The clean tree passes. In a detached scratch
worktree, a planted fake `sk-proj-…` provider key at `README.md:1` produced
`invariant-scan: R4 FAIL: README.md:1: provider-key-shaped value`; the scratch
worktree was then removed.

### 6h. Why model-profile authority is L1 now and L2 scheduled (v0.12/OPS-AUTHORITY)

**Decision: L1 now, L2 scheduled, selected by the operator on 2026-07-27.**
Free-form remote transition strings were rejected because the standing
authorization named a narrow lifecycle while the mutable controller could
construct arbitrary shell. L1 converts transitions to structured tuples and
routes every remote payload through one compiled allowlist before SSH. It is
offline-testable, and planted lifecycle, creation, destructive-path, and
unknown-container commands prove the boundary can refuse.

Hash-pinning both executable surfaces and byte-comparing the policy copies make
edits visible, but they do not make L1 invariant under an agent that edits the
controller and its pin together. That residual is accepted temporarily and
stated without qualification. L2 is scheduled for the next
operator-authorized server-administration session, before any additional model
profile is admitted. Its forced-command `authorized_keys` wrapper must be
tested from both directions so the server, rather than the Mac controller,
enforces the lifecycle set. This is the operations analogue of A4; it neither
narrows nor closes A4's core-shell trust boundary.

## 7. Run reference

```bash
# toolchain (v0.6.2): offline needs >= 1.75; --features net needs >= 1.86.
# Ubuntu 24.04 ships both, no rustup required:
apt-get install -y rustc-1.91 cargo-1.91
export PATH=/usr/lib/rust-1.91/bin:$PATH
cargo build -p cored --features net --locked            # live HTTP; builds since v0.6.2

cargo run -p cored                                     # core on :8788
pip install -r shell/requirements.txt
PYTHONPATH=shell python3 -m intel_shell.pipeline --client acme-research
PYTHONPATH=shell uvicorn intel_shell.app:app --port 8787   # public API on :8787

# with the mock LLM (embeddings + /v1/ask):
python3 tools/mock_openai.py &
LLM_BASE_URL=http://127.0.0.1:8899/v1 PYTHONPATH=shell python3 -m intel_shell.pipeline

cargo test && PYTHONPATH=shell python3 -m pytest shell/tests   # 49 Rust + 69 shell

# v0.6 — per-source ingest (the `sources` filter is optional; omit it for whole sectors):
curl -X POST localhost:8788/ingest -H 'content-type: application/json' \
     -d '{"sectors":["technology"],"sources":["techwire"]}'
PYTHONPATH=shell python3 -m intel_shell.scheduler --dry-run   # per-source + per-sector jobs
PYTHONPATH=shell python3 -m intel_shell.scheduler --once      # run due jobs (cron/systemd)

# v0.5 — hashed keys + billing webhook:
PYTHONPATH=shell python3 tools/hash_subscriptions.py config/subscriptions.json \
  --out config/subscriptions.hashed.json
SUBSCRIPTIONS_PATH=config/subscriptions.hashed.json BILLING_WEBHOOK_SECRET=whsec_… \
  PYTHONPATH=shell uvicorn intel_shell.app:app --port 8787

# v0.6 (T6) — key rotation, Stripe, SQLite-backed subscriptions:
PYTHONPATH=shell python3 tools/admin_keys.py list
PYTHONPATH=shell python3 tools/admin_keys.py rotate \
  --client acme-research --new-key ak_NEW --grace 86400   # omit --grace = revoke now
PYTHONPATH=shell python3 tools/migrate_subscriptions.py config/subscriptions.json \
  --to sqlite:///var/lib/intel/subs.db
SUBSCRIPTIONS_PATH=sqlite:///var/lib/intel/subs.db STRIPE_WEBHOOK_SECRET=whsec_… \
  PYTHONPATH=shell uvicorn intel_shell.app:app --port 8787   # POST /v1/billing/stripe

# T7, when a real LLM endpoint exists (this is the whole deferred checklist):
LLM_BASE_URL=http://vllm-box:8000/v1 LLM_API_KEY=… \
  PYTHONPATH=shell python3 tools/verify_llm.py
```

**Env — core:** `CORE_CONFIG` `CORE_ENTITIES` `CORE_DB` `CORE_BIND` `CORE_TOKEN`.
**Env — shell:** `CORE_URL` `CORE_TOKEN` `SUBSCRIPTIONS_PATH` (a path, or `sqlite:///…`) `LLM_BASE_URL` `LLM_API_KEY` `LLM_CHAT_MODEL`/`LLM_EMBED_MODEL`, `API_KEY_PEPPER`, `BILLING_WEBHOOK_SECRET`; **new in T6:** `STRIPE_WEBHOOK_SECRET` (unset ⇒ `/v1/billing/stripe` returns 503), `STRIPE_PRICE_SECTORS` (JSON price→sectors map, so entitlements follow what was purchased).

**Note (T9.6):** the default subscriptions path is now anchored to the repo root rather than the process CWD — `uvicorn intel_shell.app:app` launched from anywhere but the repo root used to silently find zero clients and 401 every request.

**Scheduler config (`config/schedule.json`) — v0.6 shape:** a job's `sources` map is now **source id → cadence** (true per-feed clocks: `techwire` every 900s and `osdaily` every 1800s, though both live in `technology`), and the new `sectors` map is **sector id → cadence** for whole-sector jobs. A job with neither runs a single full pipeline.

## 8. v0.8 measured execution

### B0 — entering baseline (verified 2026-07-20)

Every result below was run on the pinned Rust/Cargo 1.91.1 toolchain after
`cargo clean` removed 758.4 MiB of build output; none is inferred from the prior
handoff.

- `RUSTFLAGS="-D warnings" cargo check --workspace --locked --all-targets`:
  exit 0, 0 rustc warnings.
- `RUSTFLAGS="-D warnings" cargo test --workspace --locked`: exit 0, **80
  passed** (cored 7, compliance 28, core 7, enrich 2, extract 3, ingest 17,
  registry 4, retrieve 3, store 9; analyze/view and doc-tests 0).
- `RUSTFLAGS="-D warnings" cargo check -p cored --features net --locked
  --all-targets`: exit 0, 0 rustc warnings.
- `RUSTFLAGS="-D warnings" cargo test -p intel-ingest --features net --locked`:
  exit 0, **17 passed**.
- `PYTHONPATH=shell .venv/bin/python -m pytest shell/tests -q`: exit 0, **69
  passed**, with 1 `StarletteDeprecationWarning` from FastAPI's `TestClient`.
- Clippy/fmt inventory: clippy exits 101 on the one
  `items_after_test_module` diagnostic described above; allowing only that lint
  makes the remaining workspace clippy run clean. The two intentional
  `unnecessary_map_or` allows remain. `cargo fmt --all -- --check` exits 1 with
  diffs in 13 Rust files. At this historical measurement the workflow was
  report-only, not commented out; the stale
  "commented out" descriptions elsewhere in this file and `TASKS-v0.8.md` are
  recorded as false here and remain for the ordered T6 documentation fix. T6
  owns the lint/fmt corrections and gate promotion.
- Golden E2E, run through the real Rust↔HTTP↔Python seam with the deterministic
  mock model and a fresh temporary fixture DB: initial ingest **13 new**; acme
  **13 → 12 analyzed**; `techwire::tw-004` dropped for `osdaily::osd-004` at
  hamming **12**; DeepSeek **RISING z = 10.0**, corroborated by arxiv-cs,
  osdaily, and techwire; immediate re-ingest **+0**; quant-desk **1 document**;
  `/v1/ask?q=What is DeepSeek-V4?` returned **4 citations** and suppressed
  `techwire::tw-004`. No golden delta.
- DB isolation is explicit. `./run demo` creates `$DEMO_DIR/demo.db` under
  `mktemp -d`; B0 additionally used
  `/private/tmp/intel-platform-b0-golden-20260720.db` (14 fixture documents
  after both clients). The live archive remains `data/core.db`: read-only checks
  before and after the golden run showed **1,764 documents**, 6,729,728 bytes,
  and mtime `2026-07-20 09:22:16 +0800`. All future live smoke runs use
  `CORE_DB=data/live-smoke.db` and must not write the golden fixture DB or the
  1,764-document archive.
- Environment note: at B0, port 8788 was held by a `cored` process B0 did not
  start, PID **59269**, executable from this checkout. The operator stopped it;
  T2's preflight then confirmed `./run down` followed by
  `lsof -iTCP:8788 -sTCP:LISTEN -n -P` was clear.

### T2 — live interruption-resume gate tripped (2026-07-20)

- Preflight: port 8788 clear; `data/live-smoke.db` absent; `data/core.db` at
  **1,764 documents**, 6,729,728 bytes, mtime `2026-07-20 09:22:16 +0800`,
  SHA-256 `ddb2c7fb81038b670104fb8d619e7cd15a021f3e9028ba6be59f0604fafc8f3a`.
- Run 1 command: `HARVEST_MAX_PAGES=1 CORE_DB=data/live-smoke.db ./run
  harvest-arxiv`, with the generated window `2026-07-17` through `2026-07-20`.
  The live response was `fetched=1300, new=1300, ok=true, error=null`; the log
  reported page 1 with 1,300 documents, more pages following, then cap 1.
  Real OAI-PMH XML therefore parsed without an observed error on that page.
- Gate measurement immediately after run 1:
  `source_id='arxiv-cs', cursor=NULL, high_water='2026-07-20'`. This fails the
  first acceptance criterion. A capped run was treated as completion.
- Root cause: the page loop calls `checkpoint(next)`, breaks on `max_pages`,
  then the common post-loop path calls `complete(max_datestamp)`. The test
  `max_pages_bounds_one_run_and_checkpoints_the_rest` proves only that the fake
  observed the intermediate checkpoint call; it does not assert the final
  `resume_token`, so the subsequent clear cannot make the test fail.
- Run 2: **not run by design**. With the token already cleared and high-water
  advanced, it would be an incremental request, not resume-from-interruption.
  Treating it as resume evidence would violate the task's explicit gate.
- `503 Retry-After`: not observed; no 503/retry line appeared in run 1.
- Isolation and regression: `data/live-smoke.db` contains the 1,300 live rows;
  `data/core.db` retained the exact pre-run count, size, mtime, and SHA-256.
  The full fixture golden E2E was re-run and unchanged: acme **13 → 12**,
  `techwire::tw-004` dropped for `osdaily::osd-004` at hamming **12**, DeepSeek
  **RISING z=10.0**, re-ingest **+0**, quant-desk **1 document**, and `/v1/ask`
  **4 citations** with `techwire::tw-004` suppressed.

### T2 corrective attempt — durable locally, live reproof blocked (2026-07-22)

- The old cap guard was made failure-capable before the repair. The unchanged
  production code then failed the strengthened assertion: checkpoint history
  contained `oai_page2.xml`, but final `resume_token("arxiv-cs")` was `None`
  because the common completion path cleared it.
- The persistence seam now exposes one fallible page commit. `SqliteStore`
  atomically inserts the page documents, rematerializes canonical ids, records
  the next token, and accumulates `pending_high_water`. A final page promotes
  `max(existing high_water, pending pages, final page)` and clears the in-flight
  fields. Cursor-write failures are no longer swallowed by `cored`.
- Failure controls executed: the in-memory cursor double injected a page-commit
  error and proved no token advance; a SQLite `BEFORE INSERT` trigger aborted
  the cursor upsert after the document insert and proved the transaction left
  **0 documents and 0 cursor rows**; a close/reopen test preserved the page-2
  token and a page-1 datestamp newer than page 2, then completed at the correct
  earlier maximum. An old cursor table was reopened and gained the new pending
  column.
- Local acceptance: warning-denied workspace and net checks passed; **90
  workspace tests**, **20 net ingest tests**, and **70 shell tests** passed (the
  existing one Starlette deprecation warning remains); clippy and fmt passed.
  The locked offline workspace also checked clean under Rust **1.78.0** with
  `-D warnings`, so the MSRV floor did not move.
- Live preflight: `./run down` succeeded and port 8788 was clear. The previous
  disposable smoke DB was preserved at
  `/private/tmp/intel-platform-live-smoke-before-t2r-20260722.db`; a fresh
  `data/live-smoke.db` was used. The sandboxed probe returned HTTP `000000` and
  was not counted. With network permission, arXiv's Identify endpoint returned
  200 and the real robots decision was `Unavailable(allow)` with effective
  crawl delay 0.500s, but the first `ListRecords` request for 2026-07-19 through
  2026-07-22 timed out. Result: `fetched=0`, `new=0`, `ok=false`, no parsed XML
  page, no cursor row, and every HC13 box unchecked. Run 2 was not executed;
  503/Retry-After was not observed. **T2 remains blocked, not passed.**
- Full golden E2E used fresh temporary DB
  `/private/tmp/intel-t2r-golden.gB0kZ9/golden.db` and remained exact: initial
  ingest **13**, acme re-ingest **+0**, analyzed **12**,
  `techwire::tw-004` dropped for `osdaily::osd-004` at hamming **12**, DeepSeek
  **RISING z=10.0**, quant-desk **1 document**, and ordinary `/v1/ask` with **4
  citations** and `techwire::tw-004` suppressed. The DB ended at 14 rows with 0
  NULL fingerprints/canonical ids. `data/core.db` retained **1,764 rows** and
  SHA-256 `ddb2c7fb81038b670104fb8d619e7cd15a021f3e9028ba6be59f0604fafc8f3a`.
- Verification environment note: the first sandboxed golden could not bind
  loopback; the permitted run then exposed macOS system-proxy discovery routing
  Python `httpx` loopback through `httpcore._sync.http_proxy` despite no proxy
  environment variables. Direct curl proved cored stayed healthy. The recorded
  golden set `NO_PROXY/no_proxy=127.0.0.1,localhost`; no application behavior
  was changed. Ports 8788 and 8899 were clear after teardown.

### T2 closed — interruption-resume proven on the live wire (2026-07-23)

- Preflight: the worktree was clean at `2b036d9`; `./run down` succeeded and
  port 8788 was clear. The 2026-07-22 zero-row timeout artifact was preserved at
  `/private/tmp/intel-platform-live-smoke-t2-timeout-20260722.db`, and both live
  runs used a fresh `data/live-smoke.db`. The sandboxed reachability probe again
  returned HTTP `000000` and was not counted; the permitted commands reached
  arXiv Identify with HTTP 200.
- Run 1 command: `HARVEST_MAX_PAGES=1 CORE_DB=data/live-smoke.db ./run
  harvest-arxiv`, generated window `2026-07-19` through `2026-07-22`. It fetched
  and added **1,300** real records, reported `ok=true`, parsed the page without
  an observed error, reported that more pages followed, and stopped at cap 1.
  SQLite then held 1,300 documents and the non-NULL next token
  `verb%3DListRecords%26metadataPrefix%3Doai_dc%26from%3D2026-07-21%26until%3D2026-07-22%26set%3Dcs%26skip%3D522`,
  with `high_water=NULL` and `pending_high_water=2026-07-21`.
- Run 1's logs/config were preserved under
  `/private/tmp/intel-platform-t2-run1-20260723-*`. `cored` was stopped, port
  8788 was independently confirmed clear, and the identical capped command was
  run again. **Run 2's first request carried the exact run-1 token**, so it
  resumed rather than fetching the fresh first page. It fetched and added the
  next **1,300** real records with `ok=true`; the store reached **2,600** rows
  and 2,487 analyzed documents. The next durable token advanced to
  `verb%3DListRecords%26metadataPrefix%3Doai_dc%26from%3D2026-07-22%26until%3D2026-07-22%26set%3Dcs%26skip%3D88`,
  with `high_water=NULL` and `pending_high_water=2026-07-22`. Run 2 evidence is
  preserved under `/private/tmp/intel-platform-t2-run2-20260723-*`.
- Both runs emitted the real robots verdict `Unavailable(allow)` and an
  effective crawl delay of 0.500s. Across the two live pages the harness
  reported no XML parse error. A 503/Retry-After response was **not observed**;
  it was not forced. The smoke DB has 0 NULL fingerprints and 0 NULL canonical
  ids.
- Full acceptance on the resulting tree: warning-denied offline and net checks
  passed; **90 workspace tests**, **20 net ingest tests**, and **70 shell tests**
  passed (the existing one Starlette deprecation warning remains); clippy and
  fmt passed. The locked offline workspace checked clean under Rust **1.78.0**
  with `-D warnings`.
- Full golden E2E used fresh temporary DB
  `/private/tmp/intel-platform-t2-golden.gyEOy7/golden.db` and remained exact:
  initial ingest **13**, acme re-ingest **+0**, analyzed **12**,
  `techwire::tw-004` dropped for `osdaily::osd-004` at hamming **12**, DeepSeek
  **RISING z=10.0**, quant-desk **1 document**, and ordinary `/v1/ask` with **4
  citations**, no retrieval degradation notes, and `techwire::tw-004`
  suppressed. The temporary DB ended at 14 rows with 0 NULL fingerprints or
  canonical ids. Before and after the live runs and golden, `data/core.db`
  remained **1,764 rows** with SHA-256
  `ddb2c7fb81038b670104fb8d619e7cd15a021f3e9028ba6be59f0604fafc8f3a`.
- Teardown: `cored` and the mock model were stopped; ports 8788 and 8899 were
  clear. The live gate did not trip, so T2 is complete.

### H1 — harvest evidence hardened (verified 2026-07-20)

- `RobotsCache::allowed` now emits one behavior-neutral, greppable decision line
  containing origin, exact disposition (`Body(allow|deny)`,
  `Unavailable(allow|deny)`, or `Unreachable(deny)`), path, allow/deny outcome,
  and effective crawl-delay. It performs only reads and logging; the returned
  allow/deny value and subsequent `apply_crawl_delay` path are unchanged.
- `run`'s robots evidence grep now matches only `robots:` /
  `effective-crawl-delay`; it no longer includes the broad `arxiv` alternative
  that mislabeled page progress as robots evidence.
- The HC13 checklist is computed from the captured ingest JSON, numbered page
  lines, and the SQLite cursor-row query. It has no static `[ ]` claims.
- Positive live run, fresh `data/live-smoke.db`, window 2026-07-17 through
  2026-07-20: **1,764 fetched/new**, page 1 = 1,300 and page 2 = 1,764, 0 parse
  errors. The robots section contained only the real lines
  `robots: https://oaipmh.arxiv.org -> Unavailable(allow) ...
  effective-crawl-delay=0.500s`. All four evidence boxes were checked:
  documents > 0, pages > 1, source result parse-clean, and cursor row present.
- Negative control on the disposable smoke DB: its high-water was set beyond
  the configured window, and the real endpoint returned `fetched=0, new=0,
  ok=true` with one zero-document page. The harness reported **NOT VERIFIED**
  and all four boxes were unchecked, including the cursor-row box despite a
  stale row being present. The successful 1,764-document snapshot was restored
  afterward; the T2 failure snapshot is preserved at
  `/private/tmp/intel-platform-t2-blocked-live-smoke.db`.
- Verification: `bash -n run` passed; targeted clippy for compliance + net
  ingest passed under `-D warnings`; workspace check/test passed with 0 rustc
  warnings and **80 tests**; net check/test passed with 0 rustc warnings and
  **17 tests**; shell **69 passed** with the existing 1 deprecation warning.
  Fmt's known B0 inventory remains the same 13 files; T6 still owns it.
- Golden E2E was re-run after the change and is byte-identical in every anchor:
  acme **13 → 12**, `techwire::tw-004` dropped for `osdaily::osd-004` at
  hamming **12**, DeepSeek **RISING z=10.0**, re-ingest **+0**, quant-desk **1
  document**, and `/v1/ask` **4 citations** with `techwire::tw-004` suppressed.
  `data/core.db` remained 1,764 documents with SHA-256
  `ddb2c7fb81038b670104fb8d619e7cd15a021f3e9028ba6be59f0604fafc8f3a`.
- H1 intentionally does **not** repair T2's capped-run completion bug. T2
  remains blocked exactly as recorded above.

### T6 — clippy + fmt promoted to a blocking gate (verified 2026-07-20)

- The lint fix and gate are separate as required. Commit `097b017` contains
  only Rust formatting plus relocation of `row_to_document`, the embeddings
  `impl SqliteStore`, and vector helpers before the final `#[cfg(test)] mod
  tests`; no behavior or invariant changed. The gate/status change is the
  following commit.
- `cargo clippy --workspace --locked --all-targets -- -D warnings`: exit 0.
  `items_after_test_module` no longer fires. The two deliberate
  `unnecessary_map_or` allows remain because replacing them with
  `Option::is_none_or` would require Rust 1.82, above the offline 1.78 floor.
- `cargo fmt --all -- --check`: exit 0. `.github/workflows/ci.yml` was changed
  to configure the lint job as blocking with `continue-on-error: false`; the
  prior report-only and "commented out" descriptions have been corrected. No
  runner had executed it at T6; v0.10/G2 later observed the job pass.
- Full regression matrix after the lint fix: warning-denied workspace check
  exit 0; **80 workspace tests passed**; warning-denied net check exit 0; **17
  net ingest tests passed**; shell **69 passed** with the existing single
  third-party Starlette deprecation warning.
- Golden E2E used fresh temporary DB
  `/private/tmp/intel-platform-t6-golden.VdLRbK/golden.db` and was unchanged:
  acme **13 → 12**, `techwire::tw-004` dropped for `osdaily::osd-004` at
  hamming **12**, DeepSeek **RISING z=10.0**, re-ingest **+0**, quant-desk **1
  document**, and `/v1/ask` **4 citations** with `techwire::tw-004` suppressed.
- Before and after the golden run, `data/core.db` remained **1,764 documents**,
  6,729,728 bytes, mtime `2026-07-20 09:22:16 +0800`, SHA-256
  `ddb2c7fb81038b670104fb8d619e7cd15a021f3e9028ba6be59f0604fafc8f3a`.
  Ports 8788, 8790, 8786, and 8899 were clear after teardown.

### T1 — HC1 structurally enforced on `/v1/ask` (verified 2026-07-20)

- Decision-gate corpus: read-only `data/core.db`, **1,764 IndexOnly live arXiv
  documents**. Normalization is lowercase alphanumeric token runs, matching the
  shipped Rust implementation. Clean trials comprised ten explicitly written
  analytical answers (including the normal golden mock answer) against every
  document, plus one answer per four-document context that repeats only the
  already-public citation titles. That yields **17,640 single-document clean
  trials** and **4,851 four-document clean trials**. Leak trials used one
  substantive complete sentence (at least 12 tokens, wholly visible inside the
  800-character model context) from **1,763 documents**; token lengths were min
  16, p10 25, median 33, max 76. One record,
  `arxiv-cs::oai:arXiv.org:2510.24819`, has no punctuation-delimited 12-token
  sentence in its visible prefix and was recorded rather than silently counted.
- Measured sweep (rates are hits / trials; `four-doc FPR` is the operational
  selection column):

  | n | single-doc FPR | four-doc FPR | seeded-leak TPR |
  |---:|---:|---:|---:|
  | 2 | 0.172619 | 0.490414 | 1.000000 |
  | 3 | 0.005442 | 0.109050 | 1.000000 |
  | 4 | 0.000000 | 0.078747 | 1.000000 |
  | 5 | 0.000000 | 0.053185 | 1.000000 |
  | 6 | 0.000000 | 0.030097 | 1.000000 |
  | 7 | 0.000000 | 0.018347 | 1.000000 |
  | 8 | 0.000000 | 0.010513 | 1.000000 |
  | 9 | 0.000000 | 0.006390 | 1.000000 |
  | 10 | 0.000000 | 0.004535 | 1.000000 |
  | 11 | 0.000000 | 0.002474 | 1.000000 |
  | 12 | 0.000000 | 0.001237 | 1.000000 |
  | 13 | 0.000000 | 0.001031 | 1.000000 |
  | 14 | 0.000000 | 0.000618 | 1.000000 |
  | 15 | 0.000000 | 0.000206 | 1.000000 |
  | **16** | **0.000000** | **0.000000** | **1.000000** |
  | 17 | 0.000000 | 0.000000 | 0.999433 |
  | 18 | 0.000000 | 0.000000 | 0.999433 |
  | 19 | 0.000000 | 0.000000 | 0.998298 |
  | 20 | 0.000000 | 0.000000 | 0.997731 |

- **Selected `n = 16`, measured rather than assumed.** It is the only tested
  point with zero false positives in all 4,851 operational clean trials and
  100% recall across all 1,763 seeded sentences. `n = 15` retains one false
  positive; at `n = 17`, recall begins to fall. The anticipated `n ≈ 8` would
  have falsely refused 1.0513% of the four-document clean trials and was
  rejected.
- `intel_core::attest_answer` returns the original answer byte-for-byte when
  clean, ignores redistributable licenses, and on any IndexOnly overlap returns
  the constant `Answer withheld because it reproduced non-redistributable
  source text.` plus document-id-only violations. `POST /attest` fails closed on
  unknown context ids and accepts at most the same eight documents as retrieval.
  The core still does not call an LLM.
- The failure-capable double is real: `tools/mock_openai.py --leak` extracts a
  substantive IndexOnly sentence from the exact prompt. The shell negative
  control first asserted that the sentence was present in the model answer;
  `/v1/ask` then returned only the refusal. A second E2E against real cored,
  real HTTP, the shell API, and leaking mode produced the same refusal.
- Acceptance matrix: core tests cover IndexOnly refusal, CcBy pass-through, and
  unmangled analytical output; a cored test executes the handler against a real
  store; shell executes the leaking mock. Warning-denied workspace check passed
  with **84 Rust tests**; net check passed with **17 net tests**; shell **70
  passed** with the existing one Starlette deprecation warning; clippy and fmt
  both passed.
- Normal golden E2E used fresh temporary DB
  `/private/tmp/intel-platform-t1-golden.oD23lB/golden.db` and remained exact:
  acme **13 → 12**, `techwire::tw-004` dropped for `osdaily::osd-004` at hamming
  **12**, DeepSeek **RISING z=10.0**, re-ingest **+0**, quant-desk **1 document**,
  and `/v1/ask` retained its ordinary mock answer, **4 citations**, and
  `techwire::tw-004` suppression. `data/core.db` remained 1,764 documents,
  6,729,728 bytes, mtime `2026-07-20 09:22:16 +0800`, and SHA-256
  `ddb2c7fb81038b670104fb8d619e7cd15a021f3e9028ba6be59f0604fafc8f3a`.
  All local ports were clear after teardown.

### T5 — redirects re-gated before each origin (verified 2026-07-20)

- Design 1 was selected deliberately: both reqwest clients set
  `redirect(Policy::none())`. The document path resolves `Location` manually,
  permits only HTTP(S), bounds the chain at 10 redirects, and runs the existing
  publisher-policy + operator-deny + politeness gate before every request. A
  robots-file redirect is not followed and therefore fails closed.
- Failure-capable cross-origin test: the fake page server returned
  `https://first.test/start` → 302
  `https://second.test/blocked` and had a successful second body ready. The
  robots fake returned allow for the first origin and `Disallow: /blocked` for
  the second. Measured calls were both origins' `/robots.txt`, but only the
  first document URL; result was `RobotsDisallowed` for the second URL. The
  forbidden request therefore never occurred.
- Same-origin test: `https://same.test/start` → `/final` returned `finished`;
  page calls were start + final, while the robots fake recorded exactly one
  `/robots.txt` fetch. The process-scoped cache prevented redundant policy I/O.
- Fixture gate stayed exact: the existing failure-capable
  `a_fixture_fetch_never_asks_the_publisher_for_permission` test passed with
  both the fake's call count and `RobotsCache::fetches()` at **0**. RSS and OAI
  fixture branches remain separate from `net::get_text`.
- The first full workspace test run exposed a separate pre-existing isolation
  defect and was **not counted as a pass**: store test
  `duplicate_ingest_maps_to_one_canonical_id` found 3 rows instead of 2.
  `tmp_store()` still used timestamp-only filenames; the correctly qualified
  test passed alone (1/1), confirming a parallel collision. The test helper now
  includes pid + process-global atomic sequence + timestamp, matching cored's
  proven isolation shape. A full parallel store run then passed 9/9, followed
  by the complete workspace passing 84/84. No production store code changed.
- Final acceptance matrix: warning-denied workspace and net checks passed;
  **84 workspace tests**, **19 net ingest tests**, and **70 shell tests** passed
  (the existing one third-party Starlette deprecation remains); clippy and fmt
  passed. No dependency or MSRV change.
- Golden E2E used fresh temporary DB
  `/private/tmp/intel-platform-t5-golden.qNIV2J/golden.db` and was byte-identical:
  acme **13 → 12**, `techwire::tw-004` dropped for `osdaily::osd-004` at hamming
  **12**, DeepSeek **RISING z=10.0**, re-ingest **+0**, quant-desk **1 document**,
  and `/v1/ask` retained the ordinary mock answer, **4 citations**, and
  `techwire::tw-004` suppression. `data/core.db` remained 1,764 documents,
  6,729,728 bytes, mtime `2026-07-20 09:22:16 +0800`, and SHA-256
  `ddb2c7fb81038b670104fb8d619e7cd15a021f3e9028ba6be59f0604fafc8f3a`.
  All local ports were clear after teardown.

### T3 — SimHash persisted and consumed (verified 2026-07-20)

- **Entering-state correction:** the runbook's statement that the 1,764-row
  `data/core.db` had no fingerprint column was false. Direct SQLite measurement
  returned **1,764 rows, 0 NULL `simhash`, 0 NULL `canonical_id`**, and
  `pragma_table_info` found `simhash`. The schema, ingest-time write, canonical
  assignment, and one stored-equals-fresh test were already present. What was
  actually missing was a pre-column migration, update-time fingerprint refresh,
  and use of the stored value by `/view`; `dedup_near` still recomputed it.
- `dedup_near` now accepts `(Document, u64)` pairs. Core sector filtering loads
  persisted pairs from the store, and a NULL fingerprint is an error rather than
  a fallback recompute. A deliberately violating double gives two unrelated
  documents the same supplied fingerprint: they collapse at distance 0, proving
  the consumer uses the supplied value. `update_document` now refreshes the
  fingerprint from the changed title/body.
- `SqliteStore::open` now upgrades a table without `simhash` and backfills every
  NULL from the same title-plus-body function. The backfill is transactional and
  suspends/recreates the external-content FTS update trigger so unchanged text is
  not deleted/reinserted. The first targeted compile failed on a lifetime in the
  new verifier and was fixed; the next targeted test exposed the FTS-trigger
  interaction as `database disk image is malformed`. That failure was not
  counted as a pass. The transactional trigger suspension fixed it, and the
  unchanged targeted command then passed **14/14** tests across extract/store/view.
- Migration proof used disposable copy
  `/private/tmp/intel-platform-t3.qbNTxc/precolumn.db`. Before migration it had
  **1,764 rows** and no `simhash` column. After opening it through the shipped
  migration: **1,764 stored fingerprints, 0 fresh-compute mismatches, 0 canonical
  mismatches** against `data/core.db`, the column was present, and both NULL
  counts were 0. The verifier also measured the actual archive directly:
  **1,764 stored fingerprints, 0 mismatches**.
- Final matrix: warning-denied workspace and net checks passed; **86 workspace
  tests**, **19 net ingest tests**, and **70 shell tests** passed (the existing
  third-party Starlette deprecation warning remains); clippy and fmt passed. No
  dependency, lockfile, MSRV, sector, license, or robots-policy change.
- Golden E2E used fresh temporary DB
  `/private/tmp/intel-platform-t3-golden.gYgAMo/final.db` and was unchanged:
  acme **13 → 12**, `techwire::tw-004` dropped for `osdaily::osd-004` at hamming
  **12**, DeepSeek **RISING z=10.0**, re-ingest **+0**, quant-desk **1 document**,
  and `/v1/ask` retained the ordinary mock answer, **4 citations**, and
  `techwire::tw-004` suppression. The fixture DB finished at 14 rows with 0 NULL
  fingerprints/canonical ids. `data/core.db` retained **1,764 rows**, 6,729,728
  bytes, mtime `2026-07-20 09:22:16 +0800`, and SHA-256
  `ddb2c7fb81038b670104fb8d619e7cd15a021f3e9028ba6be59f0604fafc8f3a`.
  Ports 8788, 8790, 8786, and 8899 were clear after teardown.

### T4 — real model deferred at credential gate (measured 2026-07-20)

- Environment checks returned absent for both `LLM_BASE_URL` and
  `LLM_API_KEY`; an assignment-only repository scan found no `LLM_API_KEY` value.
  `lsof` found no listeners on the documented local-model ports 8000, 8899, or
  11434.
- Fresh no-credential network probes corrected the previous cycle's egress
  result: DeepSeek `/v1/models` returned **401** and OpenAI `/v1/models` returned
  **401**. Both hosts are reachable today, but neither is usable without a key.
  `./run verify-llm` exited **2** with its request to set `LLM_BASE_URL` and
  `LLM_API_KEY`.
- Gate outcome: **DEFERRED, not passed.** `verify_llm.py` was not green against a
  real endpoint and the real-model HC1 spot-check was not run. The deterministic
  mock was used only for the mandatory regression golden; it is not T4 evidence.
- Golden E2E used fresh temporary DB
  `/private/tmp/intel-platform-t4-golden.x5mEQL/golden.db` and was unchanged:
  acme **13 → 12**, `techwire::tw-004` dropped for `osdaily::osd-004` at hamming
  **12**, DeepSeek **RISING z=10.0**, re-ingest **+0**, quant-desk **1 document**,
  and `/v1/ask` retained the ordinary mock answer, **4 citations**, and
  `techwire::tw-004` suppression. The fixture DB finished at 14 rows with 0 NULL
  fingerprints/canonical ids. `data/core.db` retained **1,764 rows**, 6,729,728
  bytes, mtime `2026-07-20 09:22:16 +0800`, and SHA-256
  `ddb2c7fb81038b670104fb8d619e7cd15a021f3e9028ba6be59f0604fafc8f3a`.
  Ports 8788, 8790, 8786, and 8899 were clear after teardown.

### T7 — robots single-flight skipped at one-writer gate (measured 2026-07-20)

- `config/schedule.json` expands to five jobs (two source ingests, one sector
  ingest, one refresh, and one full pipeline), confirmed by
  `python3 -m intel_shell.scheduler --dry-run`. They are not five workers:
  `Scheduler.tick` invokes each due `job.action()` synchronously in one `for`
  loop. Both supported drivers preserve that topology: the in-process mode is
  one loop, and `deploy/intel-pipeline.service` is one `Type=oneshot` process
  running `scheduler --once`.
- Scheduler tests passed **8/8**. `lsof data/core.db` found no active holder at
  the decision point. A separate `pgrep` diagnostic could not enumerate
  processes because this Mac lacks the queried sysmond service (exit 3); that
  failed diagnostic is recorded and is not being presented as evidence.
- Gate outcome: **SKIPPED/DEFERRED as required.** The supported deployment still
  has exactly one synchronous writer, so the second-concurrent-harvest trigger
  has not fired. No single-flight lock or concurrency test was added; either
  would be speculative and would violate the task's decision gate.
- Golden E2E used fresh temporary DB
  `/private/tmp/intel-platform-t7-golden.HPED3p/golden.db` and was unchanged:
  acme **13 → 12**, `techwire::tw-004` dropped for `osdaily::osd-004` at hamming
  **12**, DeepSeek **RISING z=10.0**, re-ingest **+0**, quant-desk **1 document**,
  and `/v1/ask` retained the ordinary mock answer, **4 citations**, and
  `techwire::tw-004` suppression. The fixture DB finished at 14 rows with 0 NULL
  fingerprints/canonical ids. `data/core.db` retained **1,764 rows**, 6,729,728
  bytes, mtime `2026-07-20 09:22:16 +0800`, and SHA-256
  `ddb2c7fb81038b670104fb8d619e7cd15a021f3e9028ba6be59f0604fafc8f3a`.
  Ports 8788, 8790, 8786, and 8899 were clear after teardown.

### T4C — reproducible split-provider configuration (verified 2026-07-23)

- `./run` now loads a root `.env`; `.env` and `.env.*` are ignored while the
  secret-free `.env.example` is committed. `LLM_CHAT_PROFILE=lan|online`
  selects independent chat settings, `LLM_EMBED_*` selects an embedding
  provider separately, and the legacy shared `LLM_BASE_URL` variables remain a
  fallback. `./run config` prints resolved endpoints/models with keys redacted.
- Failure-capable tests configured an intentionally wrong legacy endpoint and
  proved both LAN and online chat profiles plus the embedding role overrode it.
  A proxy-sensitive transport then raised unless a loopback `CoreClient` used
  `trust_env=False`; the loopback case passed and the remote control retained
  `trust_env=True`. A verifier test injected a 16-token IndexOnly overlap and
  proved the public guard detects it, while a CC-BY/short-overlap control passed.
- `./run verify-llm` now builds and starts `cored` on a fresh temporary fixture
  database, requires the 13-document ingest, runs embeddings/fusion/public HC1,
  and tears down. Missing configuration exited **2** with a concise error and no
  traceback. The real LAN retry started that isolated core and ingested all 13
  fixtures, then measured **No route to host** for embeddings and chat and
  failed honestly. A deterministic mock control then passed **6/6 required
  checks**: embeddings **13 missing → 0**, clean retrieval notes, 5 hybrid
  context documents, public ask with 5 citations including 5 IndexOnly
  documents, and no 16-token gated overlap. The mock result validates the
  harness, not T4.
- Harvest safety is now explicit: `./run config` measured a bare harvest target
  of `data/live-smoke.db`; `CORE_DB=data/named-smoke.db ./run config` measured
  the explicit override unchanged. `bash -n run` passed. The ignored local
  `.env` selects the supplied LAN URL and also stores the DeepSeek chat URL with
  both key fields blank; embeddings remain deliberately unset. `.env.example`
  matched no API-key-shaped secret.
- Final matrix: warning-denied workspace and net checks passed; **90 workspace
  tests**, **20 net ingest tests**, and **77 shell tests** passed (the existing
  third-party Starlette deprecation warning remains); clippy and fmt passed;
  locked Rust **1.78.0** offline check passed with warnings denied.
- Golden E2E used
  `/private/tmp/intel-platform-t4c-final-golden.UCwRAP/golden.db` and remained
  exact: initial fixture ingest **13**; acme re-ingest **+0**; **12** analyzed;
  `techwire::tw-004` dropped for `osdaily::osd-004` at hamming **12**; DeepSeek
  **RISING z=10.0**; a second acme run again added **0**; quant-desk saw exactly
  **1 document**; public `/v1/ask` returned the ordinary mock answer with **4
  citations**, no retrieval degradation notes, and `techwire::tw-004`
  suppressed. The temporary DB ended at **14 rows, 0 NULL fingerprints, 0 NULL
  canonical ids**, integrity `ok`; ports 8788 and 8899 were clear after
  teardown.
- Gate outcome: **T4C complete; T4 still deferred.** The operator's LAN 501 and
  DeepSeek 404 embedding responses, followed by the Codex LAN reachability
  failure, mean no real embedding backfill or real public HC1 pass occurred.
  No mock or BM25-only result was promoted to real-model evidence.

### T4W — split-provider wire gate recorded (verified 2026-07-23)

- Resolved non-secret roles were LAN chat at
  `http://192.168.0.192:8080/v1`, model `default`, and DMXAPI embeddings at
  `https://www.dmxapi.cn/v1`, model `openAI`. Keys remained redacted.
- Operator run 1 created an isolated fixture DB and ingested **13/13** fresh
  documents. Both embedding operations returned HTTP **503**, so backfill and
  hybrid retrieval failed. The real LAN chat request did complete: public
  `/v1/ask` returned **4 citations**, all 4 cited documents were `IndexOnly`,
  and the returned answer contained no 16-token gated overlap. Verifier result:
  **3/5 required checks passed**, one latency diagnostic. This is a partial
  real HC1 pass and an overall T4 failure.
- Operator run 2 independently repeated the embedding 503 at 0.14s and the
  fusion failure, then blocked in the public chat request. The operator
  interrupted it after **1m41s**; Starlette/AnyIO printed a
  `KeyboardInterrupt` traceback before cleanup stopped the core. That outcome is
  a verifier control-flow/timeout defect, not provider success and not a second
  HC1 result.
- A fresh Codex probe sourced the ignored `.env`, printed only the redacted
  endpoint/model, and made one embedding request. It independently returned
  HTTP **503 Service Unavailable** from
  `https://www.dmxapi.cn/v1/embeddings`. T4's embedding gate therefore remains
  tripped; no mock, BM25-only result, or independent chat success was promoted
  to completion.
- Documentation-only acceptance matrix: warning-denied workspace and net
  checks passed; **90 workspace tests**, **20 net ingest tests**, and **77 shell
  tests** passed (the existing Starlette deprecation warning remains); clippy,
  fmt, `bash -n run`, and the locked Rust **1.78.0** offline check passed.
- Complete golden E2E used
  `/private/tmp/intel-platform-t4w-golden.5nqKKI/golden.db` and remained exact:
  initial fixture ingest **13**; acme re-ingest **+0**; **12** analyzed;
  `techwire::tw-004` dropped for `osdaily::osd-004` at hamming **12**; DeepSeek
  **RISING z=10.0**; second acme run **+0**; quant-desk exactly **1 document**;
  public `/v1/ask` **4 citations**, no retrieval notes, and
  `techwire::tw-004` suppressed. The DB ended **14/0/0**, integrity `ok`; ports
  8788 and 8899 were clear.
- `data/core.db` remained **1,764/0/0**, integrity `ok`, and SHA-256
  `db2f186e291c64192e567c9dfb979dd9877eb32b13c2ce2724a4acf1761a37a0`.
  This step made no runtime, dependency, lockfile, policy, or protected-corpus
  change.

### T4H — verifier fail-fast and provider timeouts (verified 2026-07-23)

- The failure-capable controls were run before implementation and failed in the
  intended ways: role-specific timeout assertions observed the hard-coded
  120 seconds, malformed/non-positive timeouts were accepted, and a 503
  embedding double reached a public-API constructor wired to raise. The
  unchanged targeted command reported **6 failed, 7 passed**. Those same
  controls pass after the repair.
- `ChatClient` and `EmbedClient` now resolve positive
  `LLM_CHAT_TIMEOUT_SECONDS` / `LLM_EMBED_TIMEOUT_SECONDS`, falling back to
  `LLM_TIMEOUT_SECONDS` and then the existing 120-second library default.
  Role-specific tests override a deliberately wrong shared value; a legacy
  shared-timeout test configures both roles; `0`, `-1`, and `not-a-number` are
  refused. The local ignored `.env` and `.env.example` set both roles to
  **30 seconds**, and `./run config` prints those values with keys redacted.
- Verifier stages are strict prerequisites. A failed embedding backfill returns
  immediately before fusion and public HC1; a failed fusion returns before
  chat. The 503 negative control exposes a callable chat double and a public
  API constructor that fail the test if reached. It now exits 1 after exactly
  one embedding call. Manual interruption is also converted to exit 130 with a
  concise message at the script boundary.
- Live negative control against the still-configured DMXAPI provider: fresh
  isolated core, **13/13** fixtures, HTTP **503** at embedding stage in **0.17s**,
  then `stopping before fusion/public HC1`; summary **0/1**, no LAN chat call,
  no traceback, and clean teardown. The wrapper command completed in **2.4s**.
  This is a cleaner T4 failure, not progress through the gate.
- Deterministic success control used a separate `/dev/null` env file and the
  mock on loopback with 5-second role timeouts. It passed **6/6**: embeddings
  **13 → 0 missing**, clean retrieval notes, 5 hybrid context documents, public
  ask 5 citations, 5 IndexOnly documents, and no gated overlap. The mock remains
  harness evidence only.
- Final matrix: warning-denied workspace and net checks passed; **90 workspace
  tests**, **20 net ingest tests**, and **84 shell tests** passed (the existing
  Starlette deprecation warning remains); clippy, fmt, `bash -n run`, Python
  bytecode compilation, and the locked Rust **1.78.0** check passed.
- Complete golden E2E used
  `/private/tmp/intel-platform-t4h-final-golden.jF8Ser/golden.db` and remained exact:
  initial **13**; acme **+0**, **12 analyzed**; `techwire::tw-004` dropped for
  `osdaily::osd-004` at hamming **12**; DeepSeek **RISING z=10.0**; second acme
  **+0**; quant-desk **1**; public ask **4 citations**, no retrieval notes, and
  `techwire::tw-004` suppressed. The DB ended **14/0/0**, integrity `ok`; ports
  8787/8788/8899 were clear.
- `data/core.db` remained **1,764/0/0**, integrity `ok`, and SHA-256
  `db2f186e291c64192e567c9dfb979dd9877eb32b13c2ce2724a4acf1761a37a0`.
  T4 remains deferred; no dependency, lockfile, sector, license, robots, dedup,
  or protected-corpus invariant changed.

## 9. v0.8.1 measured execution

### B0.1 — entering baseline (verified 2026-07-24)

- **Entering-state correction recorded before proceeding:** `git log --oneline
  -5` confirmed `HEAD` at `6d42a75` (`fix: bound real-model verification`), but
  `git status --porcelain` returned
  `?? TASKS-v0.8.1-EXECUTION.md`. The runbook's clean-worktree assertion was
  therefore false: the operator-added v0.8.1 runbook was present and untracked,
  exactly as reported in the task request. No other worktree change was present.
- Toolchains measured: pinned `rustc/cargo 1.91.1`, floor
  `rustc/cargo 1.78.0`, and Python **3.11.4** in both the system interpreter and
  `.venv`.
- Full matrix: warning-denied workspace check exit 0; **90 workspace tests**
  passed; warning-denied `cored --features net` check exit 0; **20 net ingest
  tests** passed; **84 shell tests** passed with the existing one third-party
  Starlette deprecation warning; clippy and fmt exit 0; locked warning-denied
  Rust **1.78.0** workspace check exit 0.
- `./run down` completed, and `lsof -nP -iTCP:<port> -sTCP:LISTEN` confirmed
  ports **8787, 8788, and 8899 clear** before the artifact measurements.
- Protected artifact measurements:
  - `data/core.db`: **1,764 documents**, 0 NULL `simhash`, 0 NULL
    `canonical_id`, integrity `ok`; **6,729,728 bytes**; mtime
    `2026-07-23 20:08:13 +0800`; SHA-256
    `db2f186e291c64192e567c9dfb979dd9877eb32b13c2ce2724a4acf1761a37a0`;
    cursor row `arxiv-cs | NULL | 2026-07-20 | NULL |
    2026-07-23 12:08:13`.
  - `data/live-smoke.db`: **2,600 documents**, 0 NULL `simhash`, 0 NULL
    `canonical_id`, integrity `ok`; **9,490,432 bytes**; mtime
    `2026-07-23 07:45:38 +0800`; SHA-256
    `94f03e9e8662dddfa5c80b63a9845d9926a1fa10060b83638ee094e0a0462c4a`;
    cursor row `arxiv-cs |
    verb%3DListRecords%26metadataPrefix%3Doai_dc%26from%3D2026-07-22%26until%3D2026-07-22%26set%3Dcs%26skip%3D88
    | NULL | 2026-07-22 | 2026-07-22 23:45:38`.
- The golden ran on disposable database
  `/private/tmp/intel-platform-b0.1-golden.L0tF8n/full-golden.db`. The first
  sandboxed bind was refused by the execution environment (`Operation not
  permitted`) and was not counted; the permitted local-only run completed
  normally. Exact measured result: initial ingest **fetched=13, new=13**; first
  acme pipeline re-ingest **+0**; **12 documents analyzed**;
  `techwire::tw-004` dropped for `osdaily::osd-004` at hamming **12**; DeepSeek
  **RISING, z=10.0**, corroborated by **3 sources**; second acme ingest **+0**;
  quant-desk **1 document**; `/v1/ask` returned **4 citations**, suppressed
  `techwire::tw-004`, and had clean retrieval notes; acme search for `deepseek`
  returned **6 hits** versus quant-desk **0**, with every `IndexOnly` snippet
  NULL; a bad key returned **401**. The disposable DB ended at **14 rows**, 0
  NULL fingerprints/canonical ids, integrity `ok`.
- The explicit command sequence used for that golden, in order, was:

  ```bash
  export ENV_FILE=/dev/null
  export CORE_DB=/private/tmp/intel-platform-b0.1-golden.L0tF8n/full-golden.db
  export SUBSCRIPTIONS_PATH=config/subscriptions.hashed.json
  export LLM_CHAT_PROFILE=
  export LLM_CHAT_BASE_URL=http://127.0.0.1:8899/v1
  export LLM_EMBED_BASE_URL=http://127.0.0.1:8899/v1
  export LLM_BASE_URL=http://127.0.0.1:8899/v1
  export NO_PROXY=127.0.0.1,localhost
  export no_proxy=127.0.0.1,localhost
  ./run up
  curl -fsS -X POST http://127.0.0.1:8788/ingest \
    -H 'content-type: application/json' \
    -d '{"sectors":["science","technology"]}'
  PYTHONPATH=shell .venv/bin/python -m intel_shell.pipeline \
    --client acme-research
  curl -fsS 'http://127.0.0.1:8788/view?sectors=science,technology'
  PYTHONPATH=shell .venv/bin/python -m intel_shell.pipeline \
    --client acme-research
  PYTHONPATH=shell .venv/bin/python -m intel_shell.pipeline \
    --client quant-desk
  PYTHONPATH=shell .venv/bin/python -m uvicorn intel_shell.app:app \
    --host 127.0.0.1 --port 8787
  curl -fsS -H 'Authorization: Bearer ak_acme_7f3d9c' --get \
    --data-urlencode 'q=What is DeepSeek-V4?' \
    http://127.0.0.1:8787/v1/ask
  curl -fsS -H 'Authorization: Bearer ak_acme_7f3d9c' --get \
    --data-urlencode 'q=deepseek' http://127.0.0.1:8787/v1/search
  curl -fsS -H 'Authorization: Bearer ak_quant_2b81aa' --get \
    --data-urlencode 'q=deepseek' http://127.0.0.1:8787/v1/search
  curl -sS -o /dev/null -w '%{http_code}\n' \
    -H 'Authorization: Bearer bad-key' http://127.0.0.1:8787/v1/signals
  ./run down
  ```

  The API server was backgrounded solely so the four public requests could
  execute in the same captured run; teardown killed it before `./run down`.
- After the golden, both protected hashes matched the values above and all
  three local ports were clear. No source, license, robots, dedup, dependency,
  lockfile, or protected-database bytes changed.

### G1 — golden E2E made executable (verified 2026-07-24)

- `./run golden` now builds the offline core, creates a fresh `mktemp -d`
  database and brief-output directory, starts the real Rust HTTP core,
  deterministic 32-dimensional mock model, and public FastAPI shell, executes
  all subscriber flows over loopback HTTP, and tears down all three services
  plus the temporary directory on EXIT. It never points a write at `data/`.
- `tools/golden_e2e.py` prints and enforces **11 named checks**: initial
  fetched/new 13/13; acme pipeline completion; 12 analyzed; exact near-duplicate
  ids and hamming 12; DeepSeek RISING at 10.0 from three sources; second acme
  ingest +0; quant-desk 1; public ask 4 citations with `techwire::tw-004`
  suppressed; all IndexOnly search snippets NULL; acme/quant DeepSeek hits 6/0;
  and bad-key 401. The restored-tree command exited 0 with **11/11**.
- Failure-capable control executed before trusting the harness: 20 unique words
  were temporarily appended to the `techwire::tw-004` fixture body. The
  unchanged command exited **1** with **7/11** passing and explicitly named
  `near-duplicate drops techwire::tw-004, keeps osdaily::osd-004 at hamming 12`
  as failed. Dependent checks also caught 13 analyzed, no duplicate pair,
  DeepSeek z=12.0, and 5 citations/no suppression. The fixture was restored
  byte-for-byte; the next run returned 11/11.
- Mock readiness now probes a real embedding POST and remains pid-aware; public
  API readiness is also pid-aware. The first implementation run exposed a
  missing `PYTHONPATH=shell` export and failed loudly before assertions; that
  was repaired and is not counted as a pass. A later attempt to neutralize
  ambient core authentication by exporting an empty `CORE_TOKEN` correctly
  produced HTTP 401; the deterministic harness now **unsets** the token instead,
  matching the normal token-off state, and the following 11/11 run is the one
  counted.
- `AGENTS.md §5.5` now requires the command rather than a hand-reimplemented
  ritual, and §6 names its assertions as authoritative over the human summary.
  `.github/workflows/ci.yml` configures a separate `golden E2E (blocking)`
  push/PR job with `continue-on-error: false`; no runner had executed it at G1,
  and v0.10/G2 later observed it pass in 76 seconds.
- Final matrix: warning-denied offline and net checks passed; **90 workspace
  tests**, **20 net ingest tests**, and **84 shell tests** passed (the existing
  one Starlette warning remains); clippy, fmt, `bash -n run`, Python bytecode
  compilation, and the locked warning-denied Rust **1.78.0** check passed.
- Both protected hashes remained exact:
  `data/core.db`
  `db2f186e291c64192e567c9dfb979dd9877eb32b13c2ce2724a4acf1761a37a0`
  and `data/live-smoke.db`
  `94f03e9e8662dddfa5c80b63a9845d9926a1fa10060b83638ee094e0a0462c4a`.
  Ports 8787/8788/8899 were clear after teardown. No dependency, lockfile,
  source, policy, license, sector, dedup, or protected-corpus change occurred.

### P1 — live-harvest evidence paths protected (verified 2026-07-24)

- `harvest_db_path()` now gives a bare command a fresh
  `data/live-<UTC timestamp>-<pid>.db` and adds a numeric suffix if that path
  already exists. `ENV_FILE=/dev/null ./run config` measured
  `data/live-20260724T064350Z-16718.db`; an explicit
  `CORE_DB=data/named-smoke.db` remained unchanged.
- `config/protected-artifacts.sha256` records the complete B0.1 hashes for
  `data/core.db` and `data/live-smoke.db`. The live-harvest command resolves and
  prints its destination **before the reachability request**, compares
  canonicalized paths, and refuses any protected entry.
- Failure-capable path controls: `CORE_DB=data/core.db` and
  `CORE_DB=./data/live-smoke.db` both exited **2 before network access**, named
  the artifact and manifest, printed its full recorded SHA-256, and supplied an
  exact fresh `CORE_DB=data/live-…db ./run harvest-arxiv` incantation.
- `./run verify-artifacts` measured **2/2 MATCH**. A disposable byte-for-byte
  copy of `data/core.db` was then appended with `planted-mismatch`; verification
  against a disposable manifest exited **1**, reporting expected
  `db2f186e…1a37a0` versus actual
  `2223a92b24024ba80ce288e6c4550287336fdfcabf71d7db0f7701406c62e183`
  and **0/1 match**. The real manifest immediately returned 2/2 again.
- `ENV_FILE=/dev/null ./run test` now begins with the artifact check and
  measured 2/2 exact matches before **90 workspace**, **20 net**, and **84 shell
  tests** passed. The standalone final matrix also passed warning-denied
  offline/net checks, the same test counts, clippy, fmt, `bash -n run`, and the
  locked warning-denied Rust **1.78.0** check.
- `./run golden` remained **11/11**. Final real hashes are still
  `db2f186e291c64192e567c9dfb979dd9877eb32b13c2ce2724a4acf1761a37a0`
  and
  `94f03e9e8662dddfa5c80b63a9845d9926a1fa10060b83638ee094e0a0462c4a`;
  ports 8787/8788/8899 were clear. No protected bytes were deleted, renamed, or
  rewritten, and no dependency, lockfile, source, license, robots, sector, or
  dedup behavior changed.

### E1 — embedding model keys enforce one dimension (verified 2026-07-24)

- The pre-fix controls all failed in the intended way. Store accepted a
  1,024-dimensional vector after a 32-dimensional vector under
  `shared-model` (`Ok(1)`); `/retrieve` returned `notes: []` for a planted
  32-versus-1,024 mismatch; and a freshly ingested but pre-embedded verifier
  database printed a green `0 missing -> 0` backfill before reaching a
  failure-capable later-stage double. Those are the three silent-success paths
  E1 was required to remove.
- `SqliteStore::upsert_embeddings` now validates an entire write against the
  dimension already stored for its model key before inserting anything. Its
  structured `DimensionMismatch` error names the model plus existing and
  received dimensions. The 32→1,024 control now fails the write, reports
  `shared-model`, `32`, and `1024`, and leaves the count at one.
- Vector search filters rows whose recorded/blob dimension differs from the
  query and returns a mismatch count. `/retrieve` turns that count into a
  visible note; the planted control reports one ignored stored embedding for
  `shared-model` against query dimension 1,024 and returns no vector hits.
  `GET /embeddings/stats?model=` reports count, common dimension, and whether
  legacy rows contain inconsistent dimensions.
- The mock roles now use reserved explicit names (`mock-chat` and
  `mock-embed-32`). `verify-llm` exits **2 before starting services** when a
  non-loopback embedding endpoint has no `LLM_EMBED_MODEL`; the measured
  control named the ambiguous model-key risk. `.env.example` requires an
  explicit embedding model.
- A fresh verifier database now passes backfill only after at least one provider
  request, zero remaining missing documents, and stored statistics matching the
  returned dimension. The pre-embedded control now prints **FAIL**, reports
  zero real requests, and stops before fusion/public HC1. A corrected isolated
  mock success control (with ambient proxy bypassed for loopback) passed **6/6**:
  13 missing → 0, one request, provider/stored dimension 32, clean retrieval
  notes, five hybrid context documents, five public citations, five IndexOnly
  citation documents, and no gated overlap. This is harness evidence only, not
  real-provider evidence.
- `./run golden` remained exactly **11/11**, so E1's strict dimension guard did
  not trip its decision gate. Final matrix: warning-denied offline and net
  checks passed; **92 workspace tests**, **20 net tests**, and **85 shell
  tests** passed; clippy, fmt, `bash -n run`, Python bytecode compilation, and
  locked warning-denied Rust **1.78.0** check passed.
- `./run verify-artifacts` remained **2/2 MATCH**. Final hashes are
  `db2f186e291c64192e567c9dfb979dd9877eb32b13c2ce2724a4acf1761a37a0`
  and
  `94f03e9e8662dddfa5c80b63a9845d9926a1fa10060b83638ee094e0a0462c4a`;
  port 8788 was clear. HC3 is intact: core only stores and compares vectors and
  makes no provider calls. No dependency, lockfile, source, license, robots,
  sector, dedup, or protected-corpus behavior changed.

### T4L — local embedding attempt deferred at transport gate (measured 2026-07-24)

- The operator supplied two distinct Docker launch commands: chat on
  `192.168.0.192:8080` using
  `gemma-4-26B-A4B-it-UD-IQ4_XS.gguf` without `--embeddings`, and a dedicated
  embedding process on port 8081 using
  `embeddinggemma-300M-Q8_0.gguf` with the required `--embeddings` CLI flag.
  These are operator-supplied launch parameters, not evidence that either API
  served a request.
- Four live probes were executed. `POST :8080/v1/embeddings`,
  `GET :8081/v1/models`, and `POST :8081/v1/embeddings` each returned curl
  exit **7**, status **000**, `Couldn't connect to server`, in 1–2 ms. A
  separate bounded `GET :8081/health` retry returned the same exit 7/status
  000. No HTTP response body existed. Therefore the historical 501
  `--embeddings` diagnosis was neither confirmed nor refuted in this attempt,
  and the embedding endpoint's API-reported model name and vector dimension
  remain unmeasured.
- A later operator-requested LAN retry ruled out an address/proxy mistake. The
  Codex host's active `en0` address measured **192.168.0.105/24**, and ARP
  resolved `192.168.0.192` to `5c:b4:7e:cd:45:92` on that interface. Requests
  to both `/health` and `/v1/models` were repeated with `curl --noproxy '*'`;
  ports 8080 and 8081 still returned exit **7** / status **000** immediately.
  ICMP reported `No route to host`, while the ARP entry proves the target was
  visible at layer 2. The remaining evidence is therefore server-side: neither
  published TCP port accepted a connection during the retry window.
- The T4L decision gate is **tripped and the step is deferred**. No fallback
  provider or mock was tried. `./run config` still resolves LAN chat
  `http://192.168.0.192:8080/v1`, model `default`, but retains the previously
  configured DMXAPI embedding role `https://www.dmxapi.cn/v1`, model `openAI`;
  that provider's measured 503 evidence above is preserved. The local role was
  not written into configuration because its endpoint never became reachable.
- Output-preserving checks remained green: `./run golden` passed **11/11**;
  `./run verify-artifacts` passed **2/2**; warning-denied offline and net checks
  passed; **92 workspace**, **20 net**, and **85 shell** tests passed; clippy,
  fmt, and locked warning-denied Rust **1.78.0** check passed. The first
  sandboxed MSRV attempt could not write rustup metadata and was not counted;
  the permitted rerun completed successfully.
- Final protected hashes remained
  `db2f186e291c64192e567c9dfb979dd9877eb32b13c2ce2724a4acf1761a37a0`
  and
  `94f03e9e8662dddfa5c80b63a9845d9926a1fa10060b83638ee094e0a0462c4a`;
  local ports 8787/8788/8899 were clear. Documentation only; no runtime,
  dependency, lockfile, policy, provider configuration, or protected-corpus
  change occurred.

### T4P — adversarial HC1 verifier built; live exercise deferred (measured 2026-07-24)

- `tools/verify_llm.py` now wraps the resolved chat client while the real public
  `/v1/ask` handler runs, capturing the exact raw model answer passed to core
  `/attest` without adding raw or gated text to the public response. The
  verifier then calls `/attest` directly with that raw answer and the same
  citation document ids, and reports the returned `violations` ids.
- The adversarial question targets a retrieved IndexOnly document by title and
  asks for its opening sentence verbatim. Classification is exactly
  `GUARD FIRED` (raw overlap, violations present, and both direct/public clean
  answers equal the constant refusal), `NOT EXERCISED` (the model declined or
  paraphrased), or `LEAK` (overlap reached the public answer or the raw overlap
  was not consistently refused). `LEAK` is a required-check failure. The
  Python overlap oracle remains deliberately independent from core `/attest`,
  so it can expose a core regression rather than merely repeat it.
- Failure-capable control: before the implementation, the targeted test failed
  collection because the adversarial classifier did not exist. Afterward, a
  canned answer containing a real 20-token IndexOnly span, paired with a
  deliberately broken no-violation attestation result, reported **LEAK**,
  named `source::gated`, and made `_finish()` exit **1**. Separate controls
  report `GUARD FIRED` with `violations: ['source::gated']` and
  `NOT EXERCISED` as a warning.
- Full-path deterministic controls used isolated fixture databases. The normal
  mock passed **6/6 required checks** and reported `NOT EXERCISED`, zero
  violations. The deliberately leaking mock passed **7/7 required checks**:
  public `/v1/ask` returned the core refusal and the adversarial leg reported
  **GUARD FIRED**, with violation
  `arxiv-cs::oai:arXiv.org:2607.01455`. Both are failure-capable harness
  evidence only, not evidence about a real model.
- The real-model acceptance remains **deferred**. Fresh `GET /v1/models`
  probes to LAN chat port 8080 and embedding port 8081 both returned curl exit
  **7**, status **000**, `Couldn't connect to server`, with no HTTP body.
  Therefore no real model received the adversarial prompt, and the record
  cannot yet say that core HC1 has been tripped by a real model.
- `./run golden` remained exactly **11/11** and protected artifacts remained
  **2/2**. Final matrix: warning-denied offline/net checks passed; **92
  workspace**, **20 net**, and **88 shell** tests passed; clippy, fmt,
  `bash -n run`, Python bytecode compilation, and locked warning-denied Rust
  **1.78.0** check passed. Protected hashes stayed
  `db2f186e291c64192e567c9dfb979dd9877eb32b13c2ce2724a4acf1761a37a0`
  and
  `94f03e9e8662dddfa5c80b63a9845d9926a1fa10060b83638ee094e0a0462c4a`;
  ports 8787/8788/8899 were clear. No dependency, lockfile, policy, public
  response shape, or protected-corpus change occurred.

### T4 — uninterrupted closure run deferred at embedding backfill (measured 2026-07-24)

- Preflight completed in order: `./run down`; ports 8787/8788/8899 clear;
  protected artifacts **2/2 MATCH**; and `./run config` resolved LAN chat at
  `http://192.168.0.192:8080/v1`, model `default`, timeout 30s, plus DMXAPI
  embeddings at `https://www.dmxapi.cn/v1`, model `openAI`, timeout 30s. Keys
  remained redacted.
- One `./run verify-llm` run was executed without interruption. Its isolated
  database ingested **13 fetched / 13 new** fixtures. The first and only
  provider stage returned `503 Service Unavailable` from
  `https://www.dmxapi.cn/v1/embeddings` after **0.16s**. The verifier reported
  embedding backfill **FAIL**, stopped with **0/1 required checks** and one
  latency warning, tore down its core, and exited 1.
- The T4 gate is **tripped and T4 remains deferred**. In this run there was no
  successful embedding request or measured dimension, no zero-missing result,
  no fusion/retrieval result, no chat latency, no public `/v1/ask`, no
  IndexOnly context check, and no adversarial `GUARD FIRED` /
  `NOT EXERCISED` outcome. Earlier partial LAN-chat evidence and mock controls
  do not carry forward into this run.
- The provider's HTTP response body was **not exposed by the current
  `EmbedClient` error path**; the captured output contains the exact status,
  URL, and httpx status reference, but no body. No second provider request was
  made after the gate tripped. Therefore the runbook's requested body evidence
  is explicitly absent rather than inferred or fabricated.
- Mandatory post-task regression checks remained green: `./run golden`
  **11/11**, protected artifacts **2/2**, warning-denied offline/net checks,
  **92 workspace**, **20 net**, and **88 shell** tests, clippy, fmt,
  `bash -n run`, Python bytecode compilation, and locked warning-denied Rust
  **1.78.0** check. Protected hashes remained
  `db2f186e291c64192e567c9dfb979dd9877eb32b13c2ce2724a4acf1761a37a0`
  and
  `94f03e9e8662dddfa5c80b63a9845d9926a1fa10060b83638ee094e0a0462c4a`.
  No runtime, dependency, lockfile, provider configuration, or
  protected-corpus change occurred.

### T4L — local embedding role confirmed over live SSH-forwarded wire (verified 2026-07-24)

- The operator demonstrated both LAN health endpoints returning HTTP 200 from
  `192.168.0.105`, while Codex's command runner and in-app browser remained
  unable to route private-LAN addresses. A user-owned SSH local forward mapped
  chat to `127.0.0.1:18080` and embeddings to `127.0.0.1:18081`; these are
  transport-only aliases for the real servers, not mock endpoints.
- Both forwarded `/health` and `/v1/models` endpoints returned HTTP **200**.
  Chat reported `gemma-4-26B-A4B-it-UD-IQ4_XS.gguf`, completion capability,
  context 32,768. Embeddings reported
  `embeddinggemma-300M-Q8_0.gguf`, context 2,048, metadata width 768.
- The required diagnosis is now confirmed from the body, not inferred:
  `POST :18080/v1/embeddings` returned HTTP **501** and
  `{"error":{"code":501,"message":"This server does not support embeddings. Start it with \`--embeddings\`","type":"not_supported_error"}}`.
  The dedicated `POST :18081/v1/embeddings` returned HTTP **200**, one item at
  index 0, model `embeddinggemma-300M-Q8_0.gguf`, and an actually measured
  vector length of **768**.
- The ignored `.env` now resolves the production roles directly:
  LAN chat `http://192.168.0.192:8080/v1` with the reported Gemma model, and
  LAN embeddings `http://192.168.0.192:8081/v1` with the reported
  EmbeddingGemma model; both timeouts remain 30s. `./run config` printed these
  exact non-secret values. DMXAPI's prior 503 evidence remains above.
- HC13 boundary at this step: the short one-item wire request proved endpoint,
  shape, index, and dimension. Full-document context-window behavior, a
  13-document batch, short/out-of-order responses, and load stalls were not
  exercised here and remain for the uninterrupted T4 verifier; they are not
  inferred from the one-item success.
- Post-task verification remained green: `./run golden` **11/11**, protected
  artifacts **2/2**, warning-denied offline/net checks, **92 workspace**,
  **20 net**, and **88 shell** tests, clippy, fmt, `bash -n run`, and locked
  warning-denied Rust **1.78.0** check. Protected hashes remained exact.

### T4P — real-model adversarial outcome measured (verified 2026-07-24)

- A fresh isolated run used the real models through the operator-owned SSH
  forward: chat `gemma-4-26B-A4B-it-UD-IQ4_XS.gguf` and embeddings
  `embeddinggemma-300M-Q8_0.gguf`, both with 30s timeouts. It ingested **13/13**
  fresh fixtures and passed **6/6 required checks**.
- The real embedding server accepted all 13 full fixture bodies in one request,
  returned 13 usable **768-dimensional** vectors, reached **13 missing → 0**,
  and matched core stats `{count: 13, dim: 768,
  inconsistent_dimensions: false}` in **0.50s**. No context-window rejection,
  short response, or stall was observed. Silent truncation cannot be determined
  from the OpenAI-compatible response; raw server return order was not captured
  because `EmbedClient` deliberately sorts by index.
- Hybrid retrieval had clean notes and five context documents. Ordinary real
  `/v1/ask` returned four citations, all four cited documents were IndexOnly,
  and the independent oracle found no 16-token gated overlap.
- The real adversarial leg targeted an IndexOnly document through the public
  path and reported **NOT EXERCISED**, `violations: []`, across seven IndexOnly
  context documents. This is exactly the runbook's model-declined/paraphrased
  outcome: not a guard pass and not a leak. Core HC1 has therefore still not
  been tripped by a real model. The prior leaking-double `GUARD FIRED` evidence
  and canned broken-attestation `LEAK`/exit-1 control remain the positive and
  emergency wiring evidence.
- Post-task verification remained green: golden **11/11**, artifacts **2/2**,
  warning-denied offline/net checks, **92 workspace**, **20 net**, and
  **88 shell** tests, clippy, fmt, `bash -n run`, and locked Rust **1.78.0**.

### T4 — closed in one uninterrupted real-model run (verified 2026-07-24)

- Preflight ran in the required order: local services stopped; ports
  8787/8788/8899 clear; protected artifacts **2/2 MATCH**; direct production
  config resolved chat `gemma-4-26B-A4B-it-UD-IQ4_XS.gguf` at LAN `:8080/v1`
  and embeddings `embeddinggemma-300M-Q8_0.gguf` at LAN `:8081/v1`, both with
  30s timeouts. The command runner used the operator's loopback SSH aliases
  `:18080/:18081` for those same servers because its private-LAN route is
  isolated.
- One separate `./run verify-llm` execution ran without interruption on a
  fresh database, ingested **13 fetched / 13 new**, and passed **6/6 required
  checks** with five diagnostics:
  - embedding backfill: one real 13-document request, **13 missing → 0**,
    provider/stored dimension **768**, stats count 13 and consistent,
    **0.16s**;
  - fusion: clean notes, five hybrid context documents, **0.02s**;
  - ordinary public `/v1/ask`: **12.97s**, four citations, all four IndexOnly,
    no independent-oracle 16-token overlap;
  - adversarial public `/v1/ask`: **6.00s**, **NOT EXERCISED**,
    `violations: []`, seven IndexOnly context documents, and never `LEAK`.
- This satisfies T4's three-way gate: `NOT EXERCISED` is an allowed completed
  outcome, while remaining explicitly not evidence that a real model tripped
  `/attest`. Earlier real or mock checks were not carried into the closure
  result; every required check above comes from this single run.
- `tools/verify_llm.py` now prints per-stage fusion, ordinary-ask, and
  adversarial-ask latencies in addition to its existing embedding latency, so
  this evidence is executable rather than reconstructed from a wall clock.
- Post-run verification passed: golden **11/11**, protected artifacts **2/2**,
  warning-denied offline/net checks, **92 workspace**, **20 net**, and
  **88 shell** tests, clippy, fmt, `bash -n run`, Python bytecode compilation,
  and locked warning-denied Rust **1.78.0** check. Protected hashes remained
  `db2f186e291c64192e567c9dfb979dd9877eb32b13c2ce2724a4acf1761a37a0`
  and
  `94f03e9e8662dddfa5c80b63a9845d9926a1fa10060b83638ee094e0a0462c4a`;
  ports 8787/8788/8899 were clear after teardown.

> **Closed-cycle status correction — 2026-07-26.** The immutable
> `evidence/v0.10.2/deferred-audit/report.json` carries the task field
> `v0.10.1 RECEIPT`. That label is wrong: the artifact records the v0.10.2
> deferred audit. Its bytes remain immutable and correctly pinned at SHA-256
> `4e11a8b3a3a64b5519469289f5cdf246bf13a0045954aa22c38703bbe6d29d9b`;
> this annotation does not move the pin. The v0.10.3 auditor derives new task
> labels from the active-cycle declaration.
