# STATE.md — intel-platform handoff

**As of:** 2026-07-28 · **Version:** v0.15.1 (core-shell) · **Status:** **v0.15.1 is published and v0.17 is closed with release disposition `release (as of 2026-07-28)`.** The atomic release push advanced `origin/main` from `cdae3c922a2156701c0df0ceb4f45fc937fa7f20` through closing-audit commit `0d99a6387f3087ff90990ff95a1ee6cf6abcb6d4`; publication CI run `30361205715` passed. Annotated tag object `d6a71c1a2afabd7ce7b335756b7ae66ff36cf1ba` dereferences to release commit `a0ba69e0a3e8385287274bb404d5123f9a2b8ac7`. Exact evidence candidate `3481e4ba85d65c927b7d0fc3a430bc04fb094394` remains a separate authenticated subject on provisionally named ref `candidate/v0.16.0`; hosted run `30357365420` attempt 1 authenticates all **7/7** derived identities. The release commit passes local CI **20/20** with zero rustc/clippy/fmt/ShellCheck failures, **131** workspace tests, **55** net tests (**29** `intel-ingest` + **26** `cored`), locked Rust 1.78, shell **244/244** on both Python 3.11.4 and clean-rebuilt 3.12.13, `invariant-scan` **11/11 rules / 23 controls**, all **146/146** pins (**144/144** evidence + **2/2** authorization), protected databases exact **2/2**, and golden **11/11**. Published `v0.15.0`, its annotated tag, release commit, receipts, and every earlier release remain byte-identical and unmoved; protected corpus bytes and three retractions remain unchanged. A4, the editable-L1 controller residual, the R3/R4 bounded open-bottom deny-lists, the active-runbook measured-value heuristic, and T7 robots single-flight remain open; L2 remains scheduled.

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

**v0.13 cycle activation is complete; E0 has not yet run (measured
2026-07-27).** The mandatory opener found only the operator-supplied untracked
`TASKS-v0.13-EXECUTION.md`. Entering HEAD was
`466ebb3fc9736923110803e087acc798e417d084`, described as
`v0.12.0-1-g466ebb3`; local `main` and `origin/main` were aligned with zero
ahead / zero behind. Annotated `v0.12.0` remained tag object
`94d8215bc2151fecba1280dc793d3f5953cd8055`, dereferencing exactly to release
commit `e5faf0c161a4256f33976664685653d8bd805d5d`.

Implementation commit `5223d783b43c250102418163ef124f4e662b727b`
admitted only the supplied runbook, the `AGENTS.md` v0.13 declaration, and the
new append-only progress-log skeleton. After that commit, `./run cycle-check`
passed with v0.13 open and ten closed execution runbooks;
`./run checklist-audit` resolved the entering **99/99** checked tasks, reported
the one existing v0.11 retraction separately, and found zero exemptions;
`git diff --check` passed. No test, golden, artifact, hosted-runner,
publication, or release claim is made by this preparatory pair. E0 begins from
the clean post-audit tree.

**v0.13 E0 is complete (measured 2026-07-27).** The restarted opener produced
no worktree entries. HEAD was
`5e450b08a3f78bbe8a804aad95a808f42415ecd1`, described as
`v0.12.0-3-g5e450b0`; the activation implementation/audit pair explains local
`main` being two commits ahead / zero behind `origin/main`. The published
`v0.12.0` tag remained object
`94d8215bc2151fecba1280dc793d3f5953cd8055`, peeled to unchanged release
commit `e5faf0c161a4256f33976664685653d8bd805d5d`.

The first sandboxed `./run ci-local` was an environment non-result: every
non-shell lane passed, while eight shell controls were denied loopback binds
or process inspection after 197 tests passed. The identical permitted rerun
passed all **20/20** jobs with **121** Rust workspace / **21** net tests, zero
rustc/clippy/format/ShellCheck failures, locked Rust 1.78 green,
**205/205** Python 3.11.4 shell tests, protected artifacts **2/2**, all
**71/71** pins, and golden **11/11**. The independent Python 3.12.13 lane
passed **205/205** and verified **21/21** exact constrained packages.
Standalone `./run golden` repeated the byte-identical **11/11** result.
`verify-artifacts`, `cycle-check`, `checklist-audit`, `progress-check`,
`version-check`, and `invariant-scan` all passed; the checklist entered E0 at
**99/99** historical checked tasks with the existing v0.11 retraction reported
separately.

All C1–C5 findings were confirmed; none refuted:

1. **C1:** a disposable real `cored` on a scratch database containing exactly
   `finance-a` and `science-b` returned HTTP 200 from `/retrieve` for a finance
   scope querying the science-only token `alpha`, with empty BM25, vector,
   fused, and context lists. The containment came from the upstream ranking
   legs: a direct call to the public unscoped `documents_by_ids(["science-b"])`
   returned the science document and its full 18-token body. `/attest` cannot
   express a sector scope; the same finance-caller control supplied
   `science-b` plus its first 16 normalized body tokens and received HTTP 200,
   the constant refusal, and `violations:[{"doc_id":"science-b"}]`. Replacing
   the id with `does-not-exist` returned HTTP 400 `unknown context document
   id`. This confirms the cross-sector existence/match oracle. No
   `/retrieve` body leak reproduced, but its final hydration boundary does
   not fail closed independently.
2. **C2:** in a detached scratch worktree, adding
   `INGEST_FUZZ_LIMIT: u32 = 17` and routing the production
   `assign_canonical_ids_tx` call through it exited **0** with
   `invariant-scan: R5 PASS`. The two original controls do fire:
   `SECOND_DEDUP_MAX_DISTANCE=17` produced
   `R5 FAIL: crates/store/src/sqlite.rs:33: second canonical-distance
   constant SECOND_DEDUP_MAX_DISTANCE=17`, and replacing the same production
   argument with literal `16` produced
   `R5 FAIL: crates/store/src/sqlite.rs:207: numeric canonical-distance
   argument in production`. R5 has a coverage defect, not total inertia.
3. **C3:** source enumeration found 16 shell test files and no reference to or
   test module for `tools/invariant_scan.py`. In the scratch worktree,
   replacing R4's provider-key regex with the never-matching `(?!)` pattern
   still exited **0** and reported all **6/6** registered rules passing. The
   registry's prose `fail_before` values are not executed.
4. **C4:** `ARCHITECTURE.md` records `/attest` as taking only
   `{answer, context_doc_ids}` while claiming nine lines later that every
   body-reading boundary takes an explicit sector set and fails closed in core
   SQL. `/retrieve` and `/attest` both call the id-only hydration method; the
   HC2 rationale is therefore false in the published v0.12.0 source.
5. **C5:** the single `USER_AGENT` constant is already used byte-identically
   by both reqwest clients and `RobotsCache`, so that part of the earlier
   diagnosis is refuted exactly as the runbook predicts. The defect is
   confirmed: the value contains `intel-platform/0.1` and
   `you@example.com`, no operator contact setting exists, and
   `build_robots_cache` performs no unset/empty/placeholder refusal. Only the
   contact substring may become configurable; the robots group-selection
   token remains structural.

C1's measured `/attest` oracle is a release-blocking finding rather than a
routine confirmation: no v0.13 release may close or publish until
BODY-BOUNDARY makes the same control empty across sectors. This changes the
cycle's release posture, not its publication authority; the version and
publication decisions still belong to R-CLOSE. Both disposable worktrees,
their temporary database, and the spawned core process were removed, and the
live tree returned clean.

**v0.13 FAIL-BEFORE-EXEC is complete (measured 2026-07-27).** Registry schema
2 replaces each decorative `fail_before` string with one or more executable
controls: a safe relative file, exact find text, replacement fragments, and an
expected failure substring. Every original prose string is preserved
byte-for-byte in `fail_before_note`; a dedicated test asserts the six-value
mapping.

`invariant_scan.py --self-test` first requires the unmutated tree to pass, then
copies the Git-tracked tree into a fresh temporary directory for each control,
initializes only that disposable copy's index, applies one exact substitution,
runs only the owning rule, and requires exit 1 plus the recorded substring.
The copy excludes build products, archives, virtual environments, and network
state by construction. Malformed registries and unimplemented rule ids still
exit 2. No R1–R6 matcher, pattern, or allow/deny outcome changed in this task.

The no-argument scanner path now executes the same self-test, so the existing
`./run invariant-scan` invocation in ci-local and the Python 3.11 hosted lane
both exercise the controls without adding a job. An initial attempt to pass
the flag from `run` correctly tripped its authorization-surface pin and one
evidence test; that was an integration non-result. The launcher was restored
byte-exact at SHA-256
`7afede56f13b5ee73d3f1dbe92910ce535908623676db21664409855c5ac006d`
and remains unchanged. The self-testing behavior lives entirely in the
scanner, as allowed by this task's gate.

The required inversion fired against the real CLI. Temporarily replacing R4's
provider-key regex with `(?!)` left the clean tree at 6/6 but made
`--self-test` exit **1** with
`SELF-TEST R4/1 FAIL: mutation did not make the rule fail`. Restoring the
matcher produced R1–R6 clean PASS plus all **6/6** recorded controls PASS.
The new test module contributes ten cases: six parametrized clean/fire
controls, exact preservation of all legacy prose, the non-matching-regex
failure, malformed-registry exit 2, and unimplemented-rule exit 2.

The corrected full `./run ci-local` passed all **20/20** jobs with unchanged
**121** Rust workspace / **21** net counts, warning-denied builds,
clippy/fmt/ShellCheck, locked Rust 1.78, **215/215** Python 3.11.4 tests, all
**71/71** pins, protected databases **2/2**, and golden **11/11**. Python
3.12.13 independently passed **215/215** and verified **21/21** exact packages.
The C1 release blocker remains open; this task changes the assurance harness,
not the body boundary.

**v0.13 THRESHOLD-BIND gate tripped before implementation (measured
2026-07-27).** The strict R5 allow-list was applied without changing any Rust
source. It enumerated production calls to `assign_canonical_ids`,
`assign_canonical_ids_tx`, and
`rematerialize_canonical_ids_with_distance`, excluding the `#[cfg(test)]`
seam, and required the distance argument to be the single token
`DEDUP_MAX_DISTANCE`. Against unmodified HEAD it exited **1** with:

```text
invariant-scan: R5 FAIL: crates/store/src/sqlite.rs:685: assign_canonical_ids_tx distance argument must be DEDUP_MAX_DISTANCE; found max_distance
```

The finding is real: the public no-argument maintenance entry point binds the
constant at line 657, but then forwards it through the production
`rematerialize_canonical_ids_with_distance(max_distance)` helper, whose
transaction call passes the parameter at line 685. That source shape does not
satisfy the runbook's required property that every production call site itself
bind the canonical constant. Per the Step 3 gate, no Rust source was edited and
the red matcher was not committed. THRESHOLD-BIND remains incomplete. The
runbook-mandated follow-up, THRESHOLD-SOURCE-SEAM, must remove the production
parameter seam while retaining the test-only alternate-distance control; only
then may the R5 rewrite resume.

**v0.13 THRESHOLD-SOURCE-SEAM is complete (measured 2026-07-27).** The public
no-argument `rematerialize_canonical_ids` method now opens its transaction and
passes `DEDUP_MAX_DISTANCE` directly to `assign_canonical_ids_tx`. The
production `rematerialize_canonical_ids_with_distance(max_distance)` helper is
absent. The alternate-distance path remains only in the `#[cfg(test)]`
`assign_canonical_ids` method and still exercises the same real transaction,
materialization, commit, and rollback behavior.

The focused `intel-store` suite passed **21/21**. Warning-denied workspace
check/test passed **121** tests; warning-denied net check and `intel-ingest`
net tests passed **21/21**; clippy and fmt were clean; locked Rust 1.78
check/test passed **121** tests. Re-applying the strict R5 candidate without
changing the source returned `R5 PASS` and exit **0**: all five production
`assign_canonical_ids_tx` calls pass the canonical constant, while the one
`max_distance` call is inside the `#[cfg(test)]` seam. No tool or registry
change is part of this task. THRESHOLD-BIND may now resume.

**v0.13 THRESHOLD-BIND is complete (measured 2026-07-27).** R5 now enumerates
every production call to `assign_canonical_ids`, `assign_canonical_ids_tx`,
and `rematerialize_canonical_ids_with_distance`, excludes test-only Rust, and
requires the distance argument at each call to be exactly the single token
`DEDUP_MAX_DISTANCE`. A different constant, literal, or expression is reported
with file, line, call name, and offending token. The independent declaration
half still requires exactly one private
`DEDUP_MAX_DISTANCE: u32 = 16`.

The three executable controls each exited **1** with the expected real R5
failure:

```text
R5 FAIL: crates/store/src/sqlite.rs:208: assign_canonical_ids_tx distance argument must be DEDUP_MAX_DISTANCE; found INGEST_FUZZ_LIMIT
R5 FAIL: crates/store/src/sqlite.rs:33: second canonical-distance constant SECOND_DEDUP_MAX_DISTANCE=17
R5 FAIL: crates/store/src/sqlite.rs:207: assign_canonical_ids_tx distance argument must be DEDUP_MAX_DISTANCE; found 16
```

Unmodified HEAD passed R5 and the full self-test passed R1–R6 with **8**
controls. The focused invariant module passed **10/10** under both Python
3.11.4 and 3.12.13. Full ci-local remained **20/20** with **121** workspace
Rust tests, **21** net tests, **215/215** shell tests, warning-denied builds,
clippy/fmt/ShellCheck, locked Rust 1.78, all **71/71** pins, protected
databases **2/2**, and golden **11/11**. No source file under `crates/`
changed in the THRESHOLD-BIND implementation.

**v0.13 UA-CONTACT is complete (measured 2026-07-27).** A net-enabled core
requires `INTEL_CRAWLER_CONTACT` at `build_robots_cache`. A real net binary
with the variable unset or empty exited **101** before binding and named the
required setting. The same binary refused `ops@example.com`,
`you@operator.test`, and `changeme` with explicit placeholder errors. With
`crawler-operator@unit.test`, the process reached listener readiness and was
then stopped immediately; no publisher request was made.

The `intel-platform` product token is a compile-time constant and cannot be
supplied by the operator. The full identity is installed once per process,
derives its version from cored's `CARGO_PKG_VERSION` (measured
`intel-platform/0.12.0`), and is then consumed by both reqwest clients and
passed byte-identically to `RobotsCache`. A real loopback wire control captured
the exact same
`intel-platform/0.12.0 (research prototype; contact: wire-contact@unit.test)`
header from the document and robots clients. Its first sandboxed attempt was a
proxy-routing non-result; the repository-documented
`NO_PROXY=127.0.0.1,localhost` path reached the local listener and passed.

The offline-only test proves `build_robots_cache` returns `None` without
reading or requiring a contact. Workspace Rust tests increased **121 → 122**;
net `intel-ingest` tests increased **21 → 22**. The additional net-enabled
cored suite passed **22/22**, covering missing, empty, case-insensitive
placeholder, valid-contact, and crate-version behavior. Full ci-local remained
**20/20** with shell **215/215**, warning-denied builds,
clippy/fmt/ShellCheck, locked Rust 1.78, all **71/71** pins, protected
databases **2/2**, and golden **11/11**. `.env.example`, the main README, and
the deploy guide document the required setting and the structural-token rule.

**v0.13 BODY-BOUNDARY is complete (measured 2026-07-27).** Final
`/retrieve` hydration now calls `documents_by_ids_in_sectors` with the request's
sector set. `/attest` requires the same explicit set, hydrates through the
sector-scoped SQL predicate, and receives the shipped subscription sectors
from both `/v1/ask` and the live-model verification harness. The unscoped
`documents_by_ids` method is private and compiled only for its store-level
parameter-binding tests; production Rust has zero callers and cannot name it.

Both new failure-capable controls were red before the correction. A forged
technology id injected at the exact post-ranking `/retrieve` hydration
boundary returned a document and made the focused test exit **101**. This
injection is necessary because the real ranking legs already filter by sector;
an endpoint happy-path alone cannot prove the final independent guard. A
finance-caller `/attest` probe containing the first 16 whitespace tokens of a
technology `IndexOnly` body returned an attestation rather than the required
unknown-id refusal and made its focused test exit **101**. After the change,
both focused tests passed, including empty-sector controls.

The E0 wire control was rerun against a rebuilt real `cored` and a fresh
scratch archive containing exactly `finance::a` and `science::b`.
Finance-scoped `/retrieve` for science-only `alpha` returned empty BM25,
vector, fused, context, and suppressed lists. Both the 16-token
`science::b` attestation probe and `does-not-exist` returned the same HTTP
**400** body, `unknown context document id`; an empty attestation sector set
returned that same refusal. The error intentionally does not name
`science::b`, so no violation payload or cross-sector existence/match oracle
remains. A stale pre-rebuild binary first reproduced the old HTTP **200**
constant refusal with `violations:[{"doc_id":"science::b"}]`; rebuilding the
changed source produced the passing pair. The temporary process, fixtures, and
databases were then removed.

The runbook Gate was widened before implementation to contain its required
`CHANGELOG.md` error-semantics record and the two production
`tools/verify_llm.py` attestation callers found by inventory. No database
schema or public `/v1/*` response field changed. The real public-path golden
test remained byte-identical at **11/11**, including its four-citation
`/v1/ask` response.

The permitted full `./run ci-local` passed all **20/20** jobs with **124**
workspace Rust tests, **22** net tests, warning-denied builds,
clippy/fmt/ShellCheck, locked Rust 1.78, **215/215** Python 3.11.4 tests, all
**71/71** pins, protected databases **2/2**, and golden **11/11**. Python
3.12.13 independently passed **215/215** and verified **21/21** exact
packages. Initial sandboxed standalone golden and Python 3.12 attempts were
environment non-results because loopback bind/process inspection was denied;
their identical permitted reruns produced the results above. The C1 release
blocker is cleared; R7-BODY-SECTOR remains the next assurance task.

**v0.13 R7-BODY-SECTOR is complete (measured 2026-07-27).** Registered R7
cites the exact body-boundary sentence at `ARCHITECTURE.md:181-183`. Its
allow-list enumerates production calls to the two document-by-id hydration
methods outside the store, permits only `documents_by_ids_in_sectors`, and
separately refuses any public declaration of the unscoped
`documents_by_ids`.

All three reconstructible controls exited **1** and named their mutated
location. Re-publication failed at `crates/store/src/sqlite.rs:289`;
rerouting `/retrieve` failed at `apps/cored/src/main.rs:1126`; rerouting
`/attest` failed at `apps/cored/src/main.rs:1173`. Clean R7 passed **1/1**,
and the complete scanner passed **7/7** with **11** executable controls. The
focused invariant suite increased **10 → 11** and passed under Python 3.11.4
and 3.12.13.

The compiler remains the primary enforcement mechanism: BODY-BOUNDARY made
the unscoped method private and unavailable in production. R7 is intentionally
the cheaper secondary alarm that catches a future re-`pub`; it does not
replace visibility with a regex. The implementation diff contains no source
under `crates/` or `apps/`.

Full `./run ci-local` remained **20/20** with **124** workspace Rust tests,
**22** net tests, **216/216** Python 3.11 shell tests, warning-denied builds,
clippy/fmt/ShellCheck, locked Rust 1.78, all **71/71** pins, protected
databases **2/2**, invariant scan **7/7**, and golden **11/11**. Python
3.12 independently passed **216/216** and verified **21/21** exact packages.
The mandatory standalone golden run remained byte-identical at **11/11**.

**v0.13 RETRACT-HC2 is complete (measured 2026-07-27).** The retraction
registry now records two independent v0.12 defects. R-CLOSE falsely claimed
that the published HC2 architecture row matched enforced reality while
`/retrieve` and `/attest` could hydrate through the public unscoped
`documents_by_ids` method and `/attest` had no sector field. THRESHOLD-ONE's
own v0.12 correction was also defective: R5 rejected a second numeric
declaration and numeric call arguments but did not bind the production
`max_distance` forwarding seam to `DEDUP_MAX_DISTANCE`. Their corrections are
recorded as BODY-BOUNDARY plus R7-BODY-SECTOR, and THRESHOLD-SOURCE-SEAM plus
THRESHOLD-BIND, respectively.

`ARCHITECTURE.md` now describes the enforced request shapes and boundary:
`/retrieve` carries sectors; `/attest` carries sectors; every
caller-directed body hydration boundary uses a core-SQL sector predicate; an
empty set makes every requested document unavailable; and the unscoped helper
is private and test-only. R7 continues to cite the exact
`ARCHITECTURE.md:181-183` sentence. The HC2 table row names the
`/retrieve`, `/docs`, `/attest`, and missing-embeddings SQL enforcement points
without claiming that the shell is outside the trust boundary.

The historical correction is append-only: `PROGRESS-v0.12.md` has **31
additions / 0 deletions** for the erratum. The original v0.12 task records,
checked boxes, release commit, and tag remain untouched.
`checklist-audit` passed with v0.12 still **11/11** checked, its two new
retractions reported separately, and **three** retractions across all cycles.
The annotated v0.12.0 tag object remains
`94d8215bc2151fecba1280dc793d3f5953cd8055`, peeled release commit remains
`e5faf0c161a4256f33976664685653d8bd805d5d`, all **71/71** protected pins
match, and both protected databases remain exact **2/2**.

Neither accepted residual is narrowed. A rewritten shell can still bypass or
falsify the `/attest` handoff, so A4 remains open. An edited controller can
still rewrite the L1 command construction, so the server-enforced L2
forced-command wrapper remains open and scheduled. Full `./run ci-local`
passed **20/20** with **124** workspace Rust tests, **22** net tests,
**216/216** Python 3.11 shell tests, warning-denied builds,
clippy/fmt/ShellCheck, locked Rust 1.78, invariant scan **7/7** with **11**
controls, all **71/71** pins, protected databases **2/2**, and golden
**11/11**. Python 3.12 independently passed **216/216** and verified
**21/21** exact packages. The mandatory standalone golden remained
byte-identical at **11/11**.

**v0.13 NET-TEST-EXEC is complete (measured 2026-07-27).** The existing
local and hosted net jobs now execute
`cargo test -p cored --features net --locked` after the existing
`intel-ingest` invocation. `ci-local` remains **20/20** jobs. Its net job
executes **46** tests instead of **22**: `intel-ingest` remains **22/22** and
the newly reached `cored` binary passes **24/24**, including
`net_build_refuses_missing_empty_and_placeholder_contacts` and
`valid_contact_builds_one_versioned_identity_for_cache_and_clients`.
The workspace total remains **124** because its default-feature `cored` run
still excludes those two tests. The hosted workflow's identities remain
exactly `core`, `lint`, `net`, `msrv`, `shell`, `golden`, and `drift`; only a
step was added inside `net`. At task completion this hosted-path result was a
workflow-definition inspection, not a live GitHub execution. The later
RE-MEASURE attempt and its failure are recorded below rather than
retroactively promoted into this task's acceptance.

The fail-before used an exported disposable tree. Inverting the placeholder
test's `error.contains(CRAWLER_CONTACT_ENV)` assertion made the exact new
command exit **101** with **23 passed / 1 failed**, and named
`tests::net_build_refuses_missing_empty_and_placeholder_contacts` plus
`refusal must name the required setting: INTEL_CRAWLER_CONTACT is required
for a net-enabled harvester`. Restoring the assertion made the same command
pass **24/24**. The restored scratch and live
`apps/cored/src/main.rs` both hashed
`fde0a339f9c22dfc2470ad5ac76b1284f7fb0d34b79640c0c48771d47f45f076`;
the implementation diff has no path under `apps/` or `crates/`.

The full net-gated test inventory has no other unreached item. The two direct
`#[cfg(feature = "net")]` cored tests above execute in the widened cored
command. The net-gated `intel-ingest::net` module contains
`both_live_clients_send_the_installed_user_agent_byte_identically`,
`cross_origin_redirect_reads_and_honors_new_robots_before_fetching`, and
`same_origin_redirect_reuses_the_cached_robots_policy`; all three execute in
the existing **22-test** ingest command. The other `cfg(feature = "net")`
source occurrences select production code, not test items.

The first standalone commands inside the restricted workspace sandbox were
environment non-results: loopback binds and `ps` inspection were denied.
Their identical permitted reruns passed golden **11/11** and Python 3.12
**216/216** with **21/21** constrained packages. Full permitted
`./run ci-local` passed all **20/20** jobs with **124** workspace tests,
the **46-test** net job, Python 3.11 **216/216**, invariant scan **7/7**
with **11** controls, warning-denied builds, clippy/fmt/ShellCheck, locked
Rust 1.78, all **71/71** pins, protected databases **2/2**, and golden
**11/11**.

The general control lesson is now explicit: `cargo check --all-targets`
proves that a test compiles and says nothing about whether it runs, while a
`--features` gate changes the test set that `cargo test` executes. Because
`run` is an authorization-surface pin, the task Gate was widened before
implementation to update its forward manifest entry to SHA-256
`30475367926eff8b990b70dac6d17339c4e6ec0e685aa4b01f8d01a2c328b304`
at **41104** bytes; the immutable v0.12.0 `run` hash and all other historical
pins are preserved in their release.

**v0.13 IDENTITY-INSTALL is complete locally (measured 2026-07-27).** D1,
D2, and D3 were each confirmed against the entering tree rather than accepted
from the directive. D1 was the exact `OnceLock` check-then-set window:
`install_crawler_user_agent` read `USER_AGENT.get()` and later called
`USER_AGENT.set()`, so two first installers could both observe `None`; the
loser alone could emit `could not install crawler User-Agent`. D2 was also
live: test-only `AppState::new` delegated to `new_with_startup`, which
unconditionally constructed the robots cache under `net`, so the unrelated
attestation test acquired process-startup identity. D3 was confirmed by three
independent literals with identical bytes: the contact test, local net job,
and hosted net job all used `crawler-tests@unit.test`.

D1 is closed by construction. The installer now uses one
`OnceLock::get_or_init` operation and compares the bytes actually installed
with the requested bytes. Identical concurrent requests succeed; a mismatch
returns `crawler User-Agent is already configured with different bytes`.
The lost-race branch and its message were deleted; a mechanical search finds
zero `USER_AGENT.set()`, `USER_AGENT.get()`, or `could not install crawler
User-Agent` occurrences in the two gated source files. A 64-thread barrier
control passed with every installer observing the same identity, after which
a differing request returned exactly
`http: crawler User-Agent is already configured with different bytes`.

For D2, the selected disposition is option (a): identity and robots-cache
construction moved to `main()` startup, and `AppState::new_with_startup`
receives its already-decided limiter and optional cache. This keeps the
production refusal at the place where the process actually starts and avoids
widening the production/test-constructor seam. Test-only `AppState::new`
passes no cache, and the attestation test asserts that absence before testing
license semantics. The focused attestation test passed without installing
crawler configuration. For D3, the contact test deliberately installs
`identity-test@unit.test`, asserts that it differs from the CI value
`crawler-tests@unit.test`, and then proves the CI value is refused with the
exact different-bytes error.

UA-CONTACT refusal semantics did not move. Three real net-enabled binary runs
each exited **101** before listening: missing and empty contacts both emitted
`cored refused to start: INTEL_CRAWLER_CONTACT is required for a net-enabled
harvester`; `ops@example.com` emitted `cored refused to start:
INTEL_CRAWLER_CONTACT must name a real operator contact, not placeholder
"ops@example.com"`. The focused invalid-contact unit control and deliberately
different valid-contact control also passed.

This host reports **12** logical processors. The complete cored net suite
passed **24/24** with `--test-threads=1`, `4`, and `64` (above the processor
count), passed a repeated `64`-thread run, and passed the exact default CI
invocation. The concurrency control increases the ingest net suite from
**22** to **23**; the cored count remains **24**, and workspace default-feature
tests remain **124**. Full permitted `./run ci-local` passed **20/20** with
**124** workspace tests, the **47-test** net job (**23** ingest + **24**
cored), Python 3.11 **216/216**, invariant scan **7/7** with all **11**
controls, warning-denied builds, clippy/fmt/ShellCheck, locked Rust 1.78,
all **71/71** pins, protected databases **2/2**, and golden **11/11**.
Python 3.12 independently passed **216/216** and verified **21/21** exact
packages. Standalone golden repeated **11/11** with delta **0**.

The first full ingest-net run without a loopback proxy exclusion failed the
pre-existing `cross_origin_redirect_reads_and_honors_new_robots_before_fetching`
wire control with `connection closed before message completed`. The exact
test failed identically in an exported pre-change
`f4e8195f2a15735efe8c387b1eb836faeb585752` tree. With both `NO_PROXY` and
`no_proxy` set to `127.0.0.1,localhost`, that isolated control and the full
**23/23** ingest suite passed; the same explicit local exemption was used for
the complete CI measurement. This is recorded as an environment
qualification, not attributed to IDENTITY-INSTALL.

Hosted run **30274895522** therefore adds material evidence to the already
checked NET-TEST-EXEC task: its log proved that all **24** cored tests really
executed, and the first benefit of that execution was exposing D1. The
observed old message distinguishes the lost-race branch from all refusal
branches: missing/empty yields `is required`; placeholder yields `must name a
real operator contact`; already-installed different bytes yields `already
configured with different bytes`; the observed `could not install crawler
User-Agent` was reachable only after the check-then-set race.

The general lesson is also explicit: a green parallel test run is not evidence
of race-freedom, and a process-global initialized from a test binary is
order-dependent by default. The earlier local **24/24** was a measured pass,
but it did not prove the absence of a scheduler interleaving.

**v0.13 R-CLOSE has a verified release disposition and an authorized
publication disposition (measured 2026-07-27).** The operator
authorized `v0.13.0` because UA-CONTACT landed, so the correction-only
`v0.12.1` alternative does not apply. The separate publication trigger fired
when the operator accepted IDENTITY-INSTALL and release-grade RE-MEASURE and
authorized publication of `v0.13.0` in Directive 5. Before that authorization,
no annotated v0.13.0 tag or publication mutation existed and `origin/main` had
not advanced. Read-only
`git ls-remote` returned remote `main` unchanged at
`466ebb3fc9736923110803e087acc798e417d084`, the published v0.10.3/v0.11.0/
v0.12.0 annotated objects and peeled commits unchanged, no remote v0.10.2
reference, and no remote v0.13.0 reference.

The release-facing correction records the measured severity plainly:
published v0.12.0 returned an attestation violation naming out-of-sector
`science::b` to a finance-scoped request. This was an existence-and-16-token
normalized-match oracle, not a document-body leak. The HC2 retraction now says
the claim was **falsified by measurement**, and v0.13.0 closes the oracle by
sector-scoping the final `/retrieve` and `/attest` hydration in core SQL.
Out-of-sector and nonexistent attestation ids intentionally return the same
`400 unknown context document id` response.

The complete `v0.12.0..v0.13.0-local-candidate` diff contains **44 paths**,
each classified exactly once:

- **release authorities and public documentation (6):** `CHANGELOG.md`,
  `Cargo.lock`, `README.md`, `apps/cored/Cargo.toml`,
  `shell/intel_shell/__init__.py`, and `shell/intel_shell/app.py`;
- **architecture and operating documentation (4):** `.env.example`,
  `AGENTS.md`, `ARCHITECTURE.md`, and `deploy/README.md`;
- **core/shell runtime and store implementation (4):**
  `apps/cored/src/main.rs`, `crates/ingest/src/net.rs`,
  `crates/store/src/sqlite.rs`, and `shell/intel_shell/core_client.py`;
- **executable assurance and CI (9):** `.github/workflows/ci.yml`,
  `config/invariant-rules.json`, `config/protected-artifacts.json`, `run`,
  `shell/tests/test_invariant_scan.py`, `shell/tests/test_shell.py`,
  `shell/tests/test_verify_llm.py`, `tools/invariant_scan.py`, and
  `tools/verify_llm.py`;
- **state, progress, task, and retraction records (6):**
  `PROGRESS-v0.12.md`, `PROGRESS-v0.13.md`, `STATE.md`,
  `TASKS-v0.12-EXECUTION.md`, `TASKS-v0.13-EXECUTION.md`, and
  `config/checklist-retractions.json`;
- **v0.13 hosted evidence (15):**
  `evidence/ci-runs/30277584129-1/30277584129-1-core.json`,
  `evidence/ci-runs/30277584129-1/30277584129-1-core.json.sigstore`,
  `evidence/ci-runs/30277584129-1/30277584129-1-golden.json`,
  `evidence/ci-runs/30277584129-1/30277584129-1-golden.json.sigstore`,
  `evidence/ci-runs/30277584129-1/30277584129-1-lint.json`,
  `evidence/ci-runs/30277584129-1/30277584129-1-lint.json.sigstore`,
  `evidence/ci-runs/30277584129-1/30277584129-1-msrv.json`,
  `evidence/ci-runs/30277584129-1/30277584129-1-msrv.json.sigstore`,
  `evidence/ci-runs/30277584129-1/30277584129-1-net.json`,
  `evidence/ci-runs/30277584129-1/30277584129-1-net.json.sigstore`,
  `evidence/ci-runs/30277584129-1/30277584129-1-shell-py3.11.json`,
  `evidence/ci-runs/30277584129-1/30277584129-1-shell-py3.11.json.sigstore`,
  `evidence/ci-runs/30277584129-1/30277584129-1-shell-py3.12.json`,
  `evidence/ci-runs/30277584129-1/30277584129-1-shell-py3.12.json.sigstore`,
  and `evidence/v0.13.0/deferred-audit/report.json`.

`PROGRESS-v0.12.md` remains append-only relative to the release tag:
**93 additions / 0 deletions**. No path under `data/` changed; the fifteen
`evidence/` paths classified above are forward-only v0.13 release evidence.
The v0.12.0 annotated object and peeled commit remain
`94d8215bc2151fecba1280dc793d3f5953cd8055` and
`e5faf0c161a4256f33976664685653d8bd805d5d`; v0.11.0, v0.10.3, and local-only
v0.10.2 are also unmoved. The version update changed only the local `cored`
package version in `Cargo.lock`; dependency resolution did not move.

The final architecture reconciliation matches enforced reality.
`ARCHITECTURE.md` keeps A4 open because a rewritten shell can bypass or
falsify `/attest`; this cycle constrains only the honest shipped path. Its
model-profile row keeps the L1 controller residual open because an edited
controller can rewrite the client-side allowlist; the server-enforced L2
forced-command wrapper remains open and scheduled. Neither residual is closed
or narrowed.

The complete permitted local test-and-assurance matrix passed at the v0.13.0
candidate. `./run ci-local` passed all **20/20** jobs with **124** Rust
workspace tests, **47** tests in the net job (**23** ingest + **24** cored),
zero rustc/clippy/format/ShellCheck failures, locked Rust 1.78 green,
Python 3.11.4 **216/216**, invariant scan **7/7** with all **11**
reconstructible controls, all **86/86** pins, protected databases **2/2**,
persisted fingerprints exact, and golden **11/11**. The independent Python
3.12.13 lane passed **216/216** and verified **21/21** constrained packages.
The mandatory standalone golden repeated **11/11** byte-identically.
`version-check`, `cycle-check`, `checklist-audit`, `progress-check`, manifest
validation, artifact verification, and `git diff --check` passed.

Before the publication authorization, `checklist-audit` resolved **110**
checked tasks and **three** retractions while R-CLOSE remained the sole
unchecked box. Directive 5 fired the outstanding trigger. The release
implementation commit records the authorized disposition and all release
content; the following append-only audit-record commit checks R-CLOSE and
records the exact release commit and annotated tag object together, so
`cycle-check` transitions directly from one valid open state to one valid
closed state.

**v0.13 RE-MEASURE is blocked at its hosted-failure gate (measured
2026-07-27).** The operator-authorized remote exception pushed exactly
`b18ece34424e03c531bc0e90f1a633262f252d12` to the non-`main` branch
`candidate/v0.13.0`. Before dispatch, the remote branch resolved to that exact
commit, whose `.github/workflows/ci.yml` contains
`cargo test -p cored --features net --locked`. `origin/main` remained
`466ebb3fc9736923110803e087acc798e417d084`, and no local or remote
`v0.13.0` tag existed.

Workflow-dispatch run **30274895522**, attempt **1**, used
`candidate/v0.13.0`, `publish_evidence: true`, and
`audit_sha=b18ece34424e03c531bc0e90f1a633262f252d12`. It finished **Failure**:
the `core`, `lint`, `msrv`, both `shell` matrix legs, and `golden` jobs passed;
the `net` job failed; and the report-only `drift` job was skipped. The failed
hosted command and output were:

```
cargo test -p cored --features net --locked
running 24 tests
test tests::attest_endpoint_refuses_an_index_only_body ... FAILED
test tests::net_build_refuses_missing_empty_and_placeholder_contacts ... ok
test tests::valid_contact_builds_one_versioned_identity_for_cache_and_clients ... ok

thread 'tests::attest_endpoint_refuses_an_index_only_body' (3254) panicked at apps/cored/src/main.rs:202:33:
cored refused to start: could not configure crawler identity: http: could not install crawler User-Agent

test result: FAILED. 23 passed; 1 failed; 0 ignored; 0 measured; 0 filtered out; finished in 2.71s
error: test failed, to rerun pass `-p cored --bin cored`
Error: Process completed with exit code 101.
```

The run exposed all seven receipt artifact names, but its failed `net` receipt
cannot satisfy the seven-successful-identity acceptance criterion. Per the
operator stop condition, no receipt or bundle was downloaded or admitted, no
release audit or re-derivation was run, and the hosted invariant self-test log
was not promoted as evidence. At that stop, protected pins therefore remained
**71 total** (**69** evidence plus **2** authorization surfaces), RE-MEASURE
stayed unchecked, R-CLOSE was not resumed, and no post-failure golden run was
made. The later corrected retry is recorded next.

**v0.13 RE-MEASURE retry is complete (measured 2026-07-27).** The
operator-authorized candidate-only force update moved
`candidate/v0.13.0` from obsolete `b18ece34424e03c531bc0e90f1a633262f252d12`
to exact superseding candidate
`7faaa4e1271616ff9390111c863d12fbcfa4d2fd`. The remote ref resolved to that
commit, whose workflow includes the cored net invocation. Workflow-dispatch
run **30277584129**, attempt **1**, used that branch,
`publish_evidence: true`, and
`audit_sha=7faaa4e1271616ff9390111c863d12fbcfa4d2fd`. It completed
**Success** in 50 seconds.

All seven evidence-producing identities passed: `core`, `golden`, `lint`,
`msrv`, `net`, `shell/python=3.11`, and `shell/python=3.12`. The report-only
dependency-drift node remained scheduled-only/skipped and emitted no identity,
so the hosted set is still exactly seven. The hosted net log contains:

```
Run cargo test -p intel-ingest --features net --locked
test result: ok. 23 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out

Run cargo test -p cored --features net --locked
running 24 tests
test result: ok. 24 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out
```

The cored log includes the formerly failing attestation test, both
cycle-added contact tests, and all other cored tests as `ok`. The ingest log
includes
`concurrent_identity_installation_is_atomic_and_mismatch_is_deterministic ...
ok`. The hosted Python 3.11 log ran `./run invariant-scan`, passed **7/7**
registered rules, individually reconstructed R1 through R7, and ended
`SELF-TEST PASS (7/7 rules, 11 controls)`.

GitHub exposed seven artifacts whose ZIP SHA-256 digests matched the values
displayed in the run. Each contained one receipt and one paired Sigstore
bundle. All receipts name run **30277584129**, attempt **1**, success, Linux,
and both event and checked-out SHA
`7faaa4e1271616ff9390111c863d12fbcfa4d2fd`. The fourteen files are committed
under `evidence/ci-runs/30277584129-1/`.

A clean detached worktree at the exact candidate, with byte-identical ignored
copies of both protected databases, produced
`evidence/v0.13.0/deferred-audit/report.json`. Release posture required the
expected head, repository `jiayanzeng/intel-platform`, workflow
`jiayanzeng/intel-platform/.github/workflows/ci.yml`, source/signer digest
`7faaa4e1271616ff9390111c863d12fbcfa4d2fd`, source ref
`refs/heads/candidate/v0.13.0`, GitHub-hosted runners, and attestations.
The audit accepted **7** authenticated identities, rejected **0**, measured
**5 deferred / 2 promoted**, and recorded exact-cosine p95 **8.202667 ms** at
2,600 documents against the 16.264 ms anchor. A fresh re-derivation passed
with rows 7, source dispositions 5, triggers 7, release grade, and
attestations required.

The **34,038-byte** audit report hashes to
`6d9ebf6d9463303235b12d6f7d8c88a3676de2361696cf5238b7336eb8468a52`.
Its report plus fourteen receipt/bundle inputs add fifteen exact forward pins:
the manifest now validates and verifies **86 total**, comprising **84/84**
evidence files and **2/2** authorization surfaces; both protected databases
remain exact **2/2**. A4 remains open in the report with one shell-owned
public egress path and no core-owned public response boundary. The editable-L1
controller residual likewise remains open in architecture; no live server
session or L2 work occurred.

Pre-publication read-only remote verification returned `origin/main` unchanged at
`466ebb3fc9736923110803e087acc798e417d084`, candidate branch exact at
`7faaa4e1271616ff9390111c863d12fbcfa4d2fd`, immutable v0.12.0 tag object
`94d8215bc2151fecba1280dc793d3f5953cd8055` peeling to
`e5faf0c161a4256f33976664685653d8bd805d5d`, and no v0.13.0 tag. Directive 5
subsequently authorized publication; the closing record carries the resulting
exact mapping.

**v0.14 candidate inputs carried forward from v0.13 review
(recorded 2026-07-27; not acted on in this cycle):**

1. Tighten every `expected_fail` to include file and line, so each control
   proves its rule fired at the mutated site. R7's two call-site controls
   currently share failure text, and R6 carries the full message prefix while
   the other rules carry only the message.
2. Perform an allow-list audit of R1, R3, R4, and R6, including renamed and
   restructured equivalents. R3 is specifically a deny-list over known
   provider names and remains open at the bottom by construction.
3. Add a mandatory RE-MEASURE step to the runbook template. v0.13 declared
   hosted re-measurement in its deferral table but omitted the task that would
   discharge it.
4. Consider registered invariant R8 for identity-before-bind. Moving identity
   installation into `main()` fixed placement, but ordering before listener
   bind is currently guarded by statement order plus one manual binary run,
   not by a reconstructible structural rule.

**v0.13.0 publication is complete (measured 2026-07-27).** One atomic push
advanced `origin/main` from
`466ebb3fc9736923110803e087acc798e417d084` to release commit
`5ecd42bb6ca44f1588e53e493c67fee17d071b09` and created annotated tag object
`24a6a2aca52974891d120e0f2b295a93d629c1f7`. Immediate read-only verification
returned `origin/main` and `v0.13.0^{}` at the exact release commit and
`v0.13.0` at the exact tag object. The v0.10.3, v0.11.0, and v0.12.0 objects
and peeled commits remained byte-identical, as did their committed
receipt/report files. Only after that mapping passed was remote
`candidate/v0.13.0` deleted; final enumeration found it absent.

Push-triggered CI run **30281407090** executed exact release commit
`5ecd42bb6ca44f1588e53e493c67fee17d071b09` and completed **Success** in
**42 seconds**. Its seven execution identities all passed: core
`90028434967`, lint `90028434962`, net `90028434986`, MSRV `90028434824`,
golden `90028434952`, shell Python 3.11 `90028434931`, and shell Python 3.12
`90028434995`; report-only drift `90028435515` was skipped. GitHub produced
seven artifacts, but none was downloaded, admitted, or pinned. This run is
post-publication confirmation only. Release evidence remains authenticated
dispatch run **30277584129** against candidate `7faaa4e1…`, and the protected
pin count remains **86**.

**Post-release shared-model operations are live-verified (measured
2026-07-27).** Tier A created persistent `intel-gen`
(`7485ff91dc0e428b8c99f9b62fe5affee9eb76461e380fba1309c73da12b9aa9`) and
`intel-embed`
(`bbbcc5f637d1c50292a6f5254af5b50438a3ecabf2de4ced042bf2791006f093`)
from the already-local `ghcr.io/ggml-org/llama.cpp:server-cuda13` image and
the documented GGUFs, with restart policy `no`; image, commands, mounts, GPU
requests, model readability, and contexts **32768 / 2048** were inspected.
Server-local ports 8080 and 8081 both returned HTTP 200
`{"status":"ok"}`. The inherited image health check hard-codes internal port
8080, so the existing port-8081 embedding container is falsely labeled
`unhealthy`; its explicit port-8081 HTTP check is green, and the corrected
disaster-recovery creation command is recorded without recreating it.

The Mac route was measured rather than assumed: the Codex subprocess and
`osascript do shell script` both returned `No route to host`, while a command
actually launched in Terminal.app reached the server and established the
shared localhost:2222 bridge. `./run models` now provides fail-closed
`status`, `intel`, `athenaeum`, `athenaeum-bulk`, and `stop` profiles. The
complete live matrix passed: intel exposed healthy server 8080/8081 and Mac
18080/18081; Athenaeum serving exposed healthy 8080/8082 and Mac 28080/28082
with 8081 down; Athenaeum bulk exposed healthy 8081/8082 and Mac 28081/28082
with 8080 down; all-stop stopped all five named containers and released 2222,
18080–18081, and 28080–28082. A no-bridge Terminal.app resume then recreated
the bridge and restored intel with both tunneled health checks HTTP 200.
Routine switches never create, remove, pull, or alter models; missing
containers, foreign listeners, partial/overlapping GPU state, and failed
health refuse the switch. The final measured live state is the intel profile
with its managed tunnel up.

This is prior measured evidence from the operator-authorized 2026-07-27
server-administration session immediately before the v0.12 runbook. Commands
were executed in Terminal.app and then through the measured localhost:2222
bridge, with their output observed during that session; the durable record
retains the two newly created container IDs above and the profile/health matrix,
not a raw server transcript. Per HC13, this one real-hardware run proves only
what those bytes and endpoints did at that time. It cannot prove the sequences
remain correct after a controller edit, on another host, or after server state
changes. v0.12 performs no live server session and does not promote this prior
wire result into a reproducible CI claim.

**v0.12 cycle activation is complete; E0 has not yet run (measured
2026-07-27).** The mandatory opener measured entering HEAD
`916b20f8c3dabd743a0568cb14353a0c889e2ab1`, described as
`v0.11.0-1-g916b20f-dirty`; local `main` and `origin/main` were aligned with
zero ahead / zero behind. Annotated `v0.11.0` remained object
`fcfa4825e6ffbc06c0ad73e18044965c10786aa8`, dereferencing exactly to release
commit `6daeb7e9f2cc0022b5e1a1dcf2ce8702b5be0321`.

The full dirty inventory was captured before any edit and preserved without
stash, revert, clean, or broad staging. Modified tracked files were
`AGENTS.md`, `README.md`, `STATE.md`, and `run`; untracked files were the
supplied `TASKS-v0.12-EXECUTION.md`, `intel-platform-OPERATIONS.md`,
`shell/tests/test_model_profiles.py`, and `tools/model_profiles.py`. The draft
omitted `README.md`; its diff is nevertheless explained by the same
model-profile work (command documentation, operations-manual link, and the
nine-test count). The other tracked diffs contain the standing authorization,
prior live-evidence record, and `./run models` dispatch, while the three
untracked operations files are the manual, controller, and tests.

Implementation commit `a81430ab8a50961d03eff019d3449405312d8280`
admitted only the supplied runbook, the `AGENTS.md` v0.12 declaration, and the
new append-only progress-log skeleton; partial staging left the pre-existing
`AGENTS.md` operations hunk untouched. After that commit,
`./run cycle-check` passed with v0.12 open and nine closed execution runbooks;
`./run checklist-audit` resolved the entering **88/88** checked tasks with zero
exemptions; `git diff --check` passed. No test, golden, artifact,
hosted-runner, publication, or release claim is made by this preparatory pair.
E0 begins from the intentionally preserved dirty operations tree.

**v0.12 E0 is complete (measured 2026-07-27).** The entering-state gate passed:
all dirty tracked content is attributable to the supplied model-profile
operations work, including the draft-omitted `README.md`; no operations hunk or
untracked operations file was stashed, reverted, cleaned, or admitted.

The first sandboxed `./run ci-local` was an environment non-result: all
non-shell lanes passed, while eight shell tests were denied loopback binds or
process inspection. The identical permitted rerun passed all **19/19** units:
warning-denied offline and net builds, **119** Rust workspace tests, **21** net
tests, clippy, fmt, ShellCheck, locked Rust 1.78 check/tests, **200/200** Python
3.11.4 shell tests, protected artifacts **2/2**, all **54/54** pins, and golden
**11/11**. The independent Python 3.12.13 lane passed **200/200** and both
interpreters verified **21/21** exact constrained packages. Temporarily moving
`shell/tests/test_model_profiles.py` outside collection and restoring it
immediately produced **191/191** under Python 3.11.4: the untracked file adds
exactly nine cases, so the header's 200 count describes the dirty worktree, not
the published v0.11.0 release.

Standalone `./run golden` passed the same **11/11** byte-identical anchors.
`./run verify-artifacts`, `cycle-check`, `checklist-audit`,
`progress-check`, `version-check`, and
`python3 tools/evidence_artifacts.py validate` all passed. The checklist
resolved **88/88** entering checked tasks with zero exemptions. A separate
`shasum -a 256`/byte-count witness matched `data/core.db` at
`db2f186e291c64192e567c9dfb979dd9877eb32b13c2ce2724a4acf1761a37a0`
and 6,729,728 bytes and `data/live-smoke.db` at
`94f03e9e8662dddfa5c80b63a9845d9926a1fa10060b83638ee094e0a0462c4a`
and 9,490,432 bytes. Annotated `v0.11.0` remained object
`fcfa4825e6ffbc06c0ad73e18044965c10786aa8`, peeled to the unchanged release
commit `6daeb7e9f2cc0022b5e1a1dcf2ce8702b5be0321`.

All C1-C7 findings were confirmed; none refuted:

1. **C1:** a disposable real `cored` on a scratch database first ingested one
   finance document (HTTP 200, generation 1). Setting that row's persisted
   `simhash` to NULL made the later canonical rematerialization fail. A
   non-paged `techwire` ingest returned HTTP **500**, yet the database grew
   from **1 to 5** rows with all **4** `techwire` rows durable, while view
   generation stayed at **1**. This is the required fail-before.
2. **C2:** the exact recursive Rust grep found one production caller outside
   the store, `apps/cored/src/main.rs` passing literal `16`; the store exposes
   `assign_canonical_ids(max_distance)`, and its other nine call sites are
   inside the store's `#[cfg(test)]` module.
3. **C3:** `checklist_audit.py` finds checked boxes, resolves their qualified
   progress entries, and validates real commit hashes. It never reads or
   evaluates task acceptance criteria, exactly as its module contract states.
4. **C4:** the measured **200 versus 191** control confirms the nine-test
   release/worktree identity drift described above.
5. **C5:** the tracked-path grep excluding `evidence/` found 11 paths, not only
   the draft's five examples: `.env.example`, `PROGRESS-v0.8.md`,
   `PROGRESS-v0.9.md`, `README.md`, `STATE.md`,
   `TASKS-v0.8.1-EXECUTION.md`, `TASKS-v0.9-EXECUTION.md`,
   `TASKS-v0.10.3-EXECUTION.md`, `TASKS-v0.11-EXECUTION.md`,
   `TASKS-v0.12-EXECUTION.md`, and `shell/tests/test_llm_config.py`. The ten
   paths other than the current correction runbook were already committed
   before the supplied operations body; dirty operations text adds occurrences
   to `STATE.md` but did not create that path-level conflict.
6. **C6:** `./run models` calls the agent-editable
   `tools/model_profiles.py`, whose mutable free-form `TRANSITIONS` strings
   carry the remote lifecycle commands. Current content respects the named
   allowlist, but no structural boundary refuses an edited command.
7. **C7:** the nine new tests exercise only `classify_profile` and
   `transition_script`. Missing-container, foreign-listener, health-failure,
   and stale-socket refusals remain unexecuted by tests. The three augments
   also reproduce: malformed tabular output raises bare `ValueError`;
   `_require_containers` couples every profile to all five containers; and
   `cmd_models` deliberately uses bare `python3` without documenting its
   pre-venv rationale.

**v0.12 INGEST-ATOMIC is complete (measured 2026-07-27).** `append_new` now
opens one transaction, appends documents, and—when any row is new—runs global
canonical rematerialization before the single commit. The non-paged handler has
no second assignment call and performs no fallible work between that commit and
the view-generation bump. `ARCHITECTURE.md` §3 item 8 now states the enforced
rule: every store write path that adds, changes, or removes rows rematerializes
identity in the same SQLite transaction. The schema and `/ingest` success body
are unchanged.

The failure-capable regression was captured on both sides. Before the fix,
`non_paged_rematerialization_failure_rolls_back_append_and_generation` failed
with **5** rows where **1** was required; after the fix it passes while also
asserting HTTP 500 and an unmoved generation. The independent paged-boundary
control passed before and after: a successful first page leaves two durable
rows with canonical ids, cursor token, and generation 1; an injected failure in
the later page adds nothing and does not bump again.

The first post-change `./run ci-local` exposed a stale executable source locator
in `audit_deferred.py`: it required the removed handler-level assignment call.
The audit inventory was corrected to the actual one-transaction `append_new`
write path without changing any deferred trigger or disposition. The identical
rerun then passed all **19/19** jobs with **121** Rust workspace / **21** net
tests, warning-denied builds, clippy/fmt, locked Rust 1.78 check/tests, and
**200/200** shell tests. Standalone relevant Rust/MSRV lanes also passed.
Standalone golden remained **11/11** byte-identical; protected databases stayed
exact **2/2** and all **54/54** pins validated.

**v0.12 THRESHOLD-ONE is complete (measured 2026-07-27).** The preferred
disposition **(b)** is implemented because recursive source search found no
real out-of-crate caller to preserve. Production now exposes only
`rematerialize_canonical_ids()` as the documented maintenance/backfill entry
point; it chooses the private `DEDUP_MAX_DISTANCE` internally. The
caller-supplied `assign_canonical_ids(max_distance)` seam is compiled only for
the store's tests, where alternate numeric thresholds remain intentional
boundary controls. `DEDUP_MAX_DISTANCE` was not exported.

New static rule R1 in `tools/invariant_scan.py` scans production Rust outside
`crates/store/src/sqlite.rs` and refuses any `assign_canonical_ids` call. Its
docstring explicitly excludes store-internal/test numeric literals. In a
disposable detached worktree, an injected
`store.assign_canonical_ids(16)` produced exit 1 and
`invariant-scan: R1 FAIL: apps/cored/src/main.rs:1267: production
assign_canonical_ids call outside the store`; the worktree was then removed.
The clean tree reports `R1 PASS` and recursive grep finds the method definition
and nine calls only inside the store's `#[cfg(test)]` module.

The deferred-writer inventory now names the no-argument maintenance seam. A
manual raw re-derivation against the release report without its runner-receipt
directory was an invocation non-result—it downgraded only the CI-runner
disposition. The authoritative wrapper resolved its historical baseline and
passed. Full `./run ci-local` passed **19/19** with **121** workspace / **21**
net tests and **200/200** shell tests; standalone golden remained **11/11**.
Protected artifacts remained exact **2/2** with **54/54** pins.

**v0.12 INVARIANT-SCAN is complete (measured 2026-07-27).** Static
repository invariants now have a registered JSON contract and execute through
`./run invariant-scan`, local CI job 20, and the Python 3.11 hosted shell lane.
Each rule records an id, executable claim, prose source, scope, and captured
failure. Missing or empty `fail_before` is a configuration error rather than an
unproved rule. R1 preserves the Step 3 call-site boundary; R2 enforces the sole
production TCP bind and its validated-address spelling; R3 scans production
core crates for recognized LLM imports, provider/base-URL constants, and
provider calls; R5 protects the single private canonical-distance constant and
refuses numeric production call arguments. R4 is intentionally not seeded
before Step 6: its credential policy text is an operator decision and the
runbook requires registering it only after that text exists.

The failure-capable scratch control made R2, R3, and R5 fire together. An extra
production bind produced both an outside-validated-path failure and a two-bind
count failure; an `async_openai::Client` import under `crates/core` produced an
LLM-client-import failure; and a second distance constant produced both the
second-constant and two-constant-count failures. R1's separately captured Step
3 failure remains in the registry. The scratch worktree was removed. A
temporary registry with an empty `fail_before` exited 2 with
`rules[0].fail_before: must be a non-empty string`; the clean registry reports
**4/4** rules passing.

`checklist-audit` now validates a separate retraction registry, rejects
retraction/exemption overlap and unresolved retractions, and reports checked
and retracted totals separately. Before this task's checkbox, it measured
**91 checked, 0 retracted**, all 91 entries and commits resolved, and zero
exemptions. Both `AGENTS.md` amendments are live: repo-wide absence criteria
require a registered scan, and every Gate must contain the scope of its
criteria. Full `./run ci-local` passed **20/20** with **121** workspace,
**21** net, and **200/200** dirty-worktree shell tests; standalone golden
remained **11/11**. The job-count increase is exactly the new registered static
invariant unit, not a new hosted job identity.

**v0.12 RETRACT-0110 is complete (measured 2026-07-27).** v0.11.0 stays
published with a known, now-corrected defect: STORE-IDENTITY claimed “one
shared `max_distance` constant”, but the released source used the private store
constant for maintenance writes while the production ingest handler separately
passed literal `16`. Equal values did not make that one source of truth.
INGEST-ATOMIC moved ingest rematerialization inside the store transaction and
THRESHOLD-ONE made the production maintenance seam no-argument, so the
threshold is now selected only inside the store.

The permanent record is corrected forward, not rewritten. The v0.11 progress
file has an append-only erratum after its closing record; the original
STORE-IDENTITY lines and all v0.11 checklist boxes remain byte-for-byte as
published. `checklist-retractions.json` quotes the false criterion and names
both correcting v0.12 tasks. Before this task's checkbox, `checklist-audit`
resolved **92 checked, 1 retracted**, all 92 progress entries and commits, and
zero exemptions.

At RETRACT-0110 measurement, the header's **191/191** shell count was the suite
reproduced by the released v0.11.0 commit, while the preserved untracked
operations test file made the dirty worktree **200/200**. OPS-ADMIT later made
those nine cases part of HEAD without attributing them to the release. Annotated
tag object
`fcfa4825e6ffbc06c0ad73e18044965c10786aa8` still peels to
`6daeb7e9f2cc0022b5e1a1dcf2ce8702b5be0321`. Manifest validation and protected
artifact verification remain **54/54** pins and **2/2** databases, and
standalone golden remains **11/11**.

**v0.12 INFRA-POLICY is complete (measured 2026-07-27).** The operator
selected recommended **Option A**. RFC 1918 addresses and loopback-forward
ports remain documentable because they do not confer access without the LAN or
local route; no specific threat model was identified that makes those
coordinates secret. Credentials are the enforceable boundary: tracked `.env`
files, provider keys, tokens, private key material, concrete long bearer
values, non-placeholder secret assignments, and raw secret-bearing response
fields are prohibited.

The correction is recorded in the active runbook's standing prohibition,
`AGENTS.md`, and decision-log §6g. Each names the v0.11 host/port statement as
false when written and unexecuted for its entire life. E0's tracked scan found
11 matching paths, ten predating the v0.12 runbook; the private coordinates
were already deliberate documentation in `.env.example`, `README.md`, shell
tests, and append-only history.

Registered scan R4 examines every Git-tracked text file while allowing empty
assignments, explicit placeholders, and short demo fixtures. The clean tree
reports **R1–R5 5/5**. In a detached scratch worktree, planting a fake
`sk-proj-…` provider key at `README.md:1` made R4 exit 1 with
`provider-key-shaped value`; the scratch worktree was removed and the clean
pass repeated. Full `./run ci-local` passed **20/20** with **121** workspace,
**21** net, and **200/200** dirty-worktree shell tests, protected artifacts
**2/2**, and **54/54** pins. Standalone golden remained **11/11**.

**v0.12 OPS-AUTHORITY is complete (measured 2026-07-27).** The operator selected
recommended **L1 now, L2 scheduled**. L1 is offline-testable and prevents the
current controller from constructing an unapproved remote payload: every SSH
command passes `build_remote_command`, transition data is structured tuples,
and only the five named containers, bounded Docker inventory, loopback
health/model probes on 8080–8082, and the exact read-only commands named in the
policy are accepted. The existing nine-test operations file now exercises
every emitted transition and all allowlist categories; planted `docker rm`,
`docker run`, `rm -rf`, and sixth-container commands each raise `ProfileError`
before SSH.

The identical marker-delimited L1 policy lives in `AGENTS.md` and
`intel-platform-OPERATIONS.md`. Registered static rule R6 reports **PASS** on the
real tree. In a disposable Git-backed copy, changing one word in only the
operations copy made it exit 1 with
`model-profile authorization block differs from AGENTS.md`; the clean pass was
then repeated. Manifest schema 2 now holds two narrowly registered
`authorization` pins in addition to the unchanged 54 evidence pins:
`run` is 40,980 bytes at
`7afede56f13b5ee73d3f1dbe92910ce535908623676db21664409855c5ac006d`,
and `tools/model_profiles.py` is 21,394 bytes at
`b7b84261a6bc45706f93f338682108a31c3b88ad00ad4c91061a90f77ed74292`.
The manifest test proves a one-byte `run` mutation is refused.

The residual is explicit: L1 cannot stop an agent that edits the controller
from changing what runs. L2 is the only server-enforced boundary. It is
scheduled for the next operator-authorized server-administration session and
must be installed and refusal-tested before any additional model profile is
admitted, using an `authorized_keys` forced-command wrapper over the same
lifecycle set. No live server session occurred in this cycle.

**v0.12 OPS-ADMIT is complete (measured 2026-07-27).** Under the
operator-approved runbook amendment, OPS-AUTHORITY and OPS-ADMIT share one
atomic implementation commit so the previously untracked controller, tests,
and manual never exist in committed HEAD without the L1 guard and executable
pins. The operations body consists of `tools/model_profiles.py`,
`shell/tests/test_model_profiles.py`, `intel-platform-OPERATIONS.md`, and the
`run`/`AGENTS.md` changes; the same commit includes their documentation,
registered guard, pin validation, and this measured admission record.

The shell-count ambiguity is closed: both permitted interpreter runs pass
**200/200** under Python 3.11.4 and 3.12.13, with **21/21** constrained packages
on each. The earlier direct sandboxed run was an environment non-result with
eight denials of loopback binds or process topology; the identical permitted
runs passed. `./run ci-local` passes **20/20** with **121** workspace Rust tests,
**21** net tests, warning-denied builds, clippy/fmt/ShellCheck, and locked Rust
1.78 lanes. Standalone golden remains byte-identical **11/11**; both protected
databases remain **2/2**, all **54/54** evidence pins match, and both
authorization pins match.

The E0 operations inventory changed only for the selected L1 policy and the
three required C7 augment dispositions, so the task's remeasurement was the
full offline matrix above; the runbook prohibits a new live session. Malformed
container rows now raise `ProfileError`. Requiring all five containers is a
deliberate cross-project coupling because this single controller must know it
can stop every conflicting role before selecting either project's profile; a
missing role makes the known inventory incomplete and refuses. `cmd_models`
deliberately calls stdlib-only bare `python3` so reboot recovery works before a
venv exists. `tools/model_profiles.py` in intel-platform is recorded as the
single executable source of truth for both projects; Athenaeum delegates to it
and must not carry a second copy.

The prior live matrix and its two recorded container IDs retain the provenance
and HC13 limits stated at the top of this file. It is a single
operator-authorized 2026-07-27 real-hardware run, not a repeatable check and not
proof about the post-edit controller. OPS-FAILCLOSED supplies offline
failure-capable controls next; it does not turn fixtures into wire evidence.

**v0.12 OPS-FAILCLOSED is complete (measured 2026-07-27).** Container inventory,
local listeners, health results, and socket observations now each flow through a
pure function returning `proceed`, `reuse`, `move-aside`, or `refuse` before the
I/O caller acts. Their both-direction tests are offline: complete inventory
proceeds while a missing name refuses and is named; free ports proceed, a fully
managed port set reuses, and any foreign port refuses; only HTTP 200 with exact
`{"status":"ok"}` proceeds; absent/live/stale/unreadable sockets respectively
proceed/reuse/move/refuse.

The health probe now records the HTTP status separately from its body. HTTP 503
and a 200 loading body refuse. Curl timeout exit 28 produces a “hung or still
loading” result, while connection failure produces a distinct “dead or
unreachable” result; tests assert those messages differ. A fifth new control
drives `_start_tunnel` with a healthy managed socket and occupied managed
listeners while replacing both stop and recreate calls with test failures: the
method reuses the tunnel and invokes neither. No new test opens a socket, calls
SSH, or calls Docker.

Every rendered transition for `intel`, `athenaeum`, `athenaeum-bulk`, and
`stop` is also asserted free of `docker run`, `docker rm`, `docker rmi`,
`docker pull`, `/data/models`, and `kill`. The shell suite therefore moved from
**200 to 205** and passes **205/205** under both Python 3.11.4 and 3.12.13, with
**21/21** constrained packages on both. The deliberate controller change
updated its authorization pin from the admitted L1 hash to 28,297 bytes at
`1920761c97ffa6fc7b5242c16384fb6f1b0727937f9e1cfd7e00826c913554df`;
the unchanged `run` pin and all 54 evidence pins still match.

`./run ci-local` passes **20/20** with **121** workspace Rust tests, **21** net
tests, warning-denied builds, clippy/fmt/ShellCheck, and locked Rust 1.78 lanes.
Standalone golden remains byte-identical **11/11**, and protected databases
remain exact **2/2**. These pure/double controls prove the refusal state machine,
not the server wire; HC13 remains explicit.

**v0.12 RE-MEASURE is complete (measured 2026-07-27).** The clean candidate
was `d664a7d3c524a3dfab932e158d9545953844b8dd`; remote `main` was a
fast-forward from `916b20f8c3dabd743a0568cb14353a0c889e2ab1` and was verified
at that exact candidate before dispatch. GitHub Actions run **30253646597**,
attempt **1**, used `workflow_dispatch`, the exact candidate as `audit_sha`,
and `publish_evidence=true`. Core, golden, lint, MSRV, net, shell
`python=3.11`, and shell `python=3.12` all passed. The new
`invariant-scan` local job remains inside the existing Python 3.11 hosted leg,
so the authenticated identity set is still exactly seven.

The seven fresh artifacts downloaded into
`evidence/ci-runs/30253646597-1/` as seven JSON receipts and seven paired
Sigstore bundles. Every artifact and receipt names run 30253646597, attempt 1,
branch `main`, and candidate `d664a7d3c524a3dfab932e158d9545953844b8dd`.
A detached clean candidate worktree received ignored byte-exact copies of both
protected databases; its `git status --porcelain=v1` stayed empty. The
production command required `--expected-head`, `--evidence-grade release`,
`--require-attestations`, repository/workflow identity, source digest, and
`refs/heads/main`. It accepted **7**, rejected **0**, observed **7**, and
measured **5 deferred / 2 promoted**. Exact-cosine p95 was **10.324209 ms**
over 2,600 documents, below the **16.264 ms** A3 anchor.

The report is `evidence/v0.12.0/deferred-audit/report.json`, **33,852 bytes**,
SHA-256
`067fa823ba7c4e840100d30aa6a2b9fadae747ac41eca2d725b508bd410a8bc3`.
It is labeled `v0.12 RECEIPT`, records a clean subject, is release-grade, and
requires attestations. Fresh re-derivation passed with rows 7, source
dispositions 5, triggers 7, release grade, and attestations required. Manifest
schema 2 validates all **69/69** evidence pins and both authorization pins;
both protected databases remain exact **2/2**.

Both real negative controls ran only on the disposable
`codex/v0.12-remeasure-controls` branch. Run **30254382891** persisted all
seven signed packages with core as the sole failed job; the auditor rejected
that receipt for `conclusion is not success: failure`, found the core identity
missing, and accepted/observed **0/0**. Run **30254838500** passed every hosted
job but signed two `shell/python=3.11` identities and no
`shell/python=3.12`; the auditor reported the duplicate and missing identity
and again accepted/observed **0/0**.

Two earlier control dispatches are non-results and are not counted. Run
**30254221740** fired the intended core failure but a diagnostic containing the
literal `v0.12` also correctly tripped `cycle-check` in shell 3.11. Run
**30254680116** emitted the duplicate identity but correctly tripped the
workflow source-shape assertion in both shell lanes. Each issue was corrected
on the disposable branch, the focused source/authentication lane passed
**36/36** with one environment skip before the counted dispatch, and no
production guard was weakened. The remote branch, local branch, both
worktrees, copied databases, control reports, and control packages were
deleted; no negative-control evidence was committed.

Final local acceptance passed `./run ci-local` **20/20** with **121** workspace
Rust tests, **21** net tests, warning-denied offline/net builds, clippy, fmt,
ShellCheck, locked Rust 1.78 checks/tests, persisted fingerprints, and
**205/205** Python 3.11.4 shell tests. The independent Python 3.12.13 lane
passed **205/205**; both constrained environments remain **21/21** exact
packages. Matrix and standalone golden each passed **11/11** with zero drift.
Final remote enumeration kept `main` at the measured candidate, found no
control branch, and returned the unchanged annotated objects and peeled commits
for v0.9.0, v0.10.0, v0.10.1, v0.10.3, and v0.11.0. The intentionally
local-only v0.10.2 tag remains absent remotely; no published tag moved.

**v0.12 R-CLOSE selected the minor-release disposition (measured
2026-07-27).** The operator explicitly selected and authorized publication of
`v0.12.0`. A correction-only release could have shipped INGEST-ATOMIC and
THRESHOLD-ONE as `v0.11.1`, but this cycle also admits the new `./run models`
operator surface and changes `/ingest` failure semantics. Splitting those
already-integrated halves would create two identities for one measured
candidate; one minor release accurately describes the combined operations and
runtime delta.

The publication decision had an evidence trigger rather than a default:
publish only after the complete local definition of done passed against the
reconciled candidate, both Step 10 hosted negative controls accepted zero
executions, and the release commit existed. Runs **30254382891** and
**30254838500** satisfied the hosted trigger; the complete local candidate
matrix and standalone golden satisfied the remaining trigger before
publication.

The complete `v0.11.0..release-candidate` diff contains **44 paths**, each
classified exactly once:

- **release authorities and public documentation (6):** `README.md`,
  `CHANGELOG.md`, `Cargo.lock`, `apps/cored/Cargo.toml`,
  `shell/intel_shell/__init__.py`, and `shell/intel_shell/app.py`.
- **architecture authority (1):** `ARCHITECTURE.md`.
- **core runtime, store, and test plumbing (3):**
  `apps/cored/src/main.rs`, `crates/store/Cargo.toml`, and
  `crates/store/src/sqlite.rs`.
- **operations and operating-contract surface (4):** `AGENTS.md`,
  `intel-platform-OPERATIONS.md`, `run`, and `tools/model_profiles.py`.
- **executable assurance and configuration (10):**
  `.github/workflows/ci.yml`, `config/checklist-retractions.json`,
  `config/invariant-rules.json`, `config/protected-artifacts.json`,
  `shell/tests/test_evidence_artifacts.py`,
  `shell/tests/test_model_profiles.py`, `tools/audit_deferred.py`,
  `tools/checklist_audit.py`, `tools/evidence_artifacts.py`, and
  `tools/invariant_scan.py`.
- **durable evidence (15):** all fourteen receipt/bundle files under
  `evidence/ci-runs/30253646597-1/` and
  `evidence/v0.12.0/deferred-audit/report.json`.
- **state, progress, and task records (5):** `PROGRESS-v0.11.md`,
  `PROGRESS-v0.12.md`, `STATE.md`, `TASKS-v0.11-EXECUTION.md`, and
  `TASKS-v0.12-EXECUTION.md`.

`ARCHITECTURE.md §6` now maps corpus-identity atomicity to the core store
transaction and private threshold, and maps executable absence claims to the
registered invariant scanner. Its HC1 row still says that a rewritten shell can
bypass or falsify `/attest`, so A4 remains open. The model-profile row names L1
as defense for the shipped controller and states that an edited controller can
rewrite it; the server-enforced L2 forced-command wrapper remains open and
scheduled. `AGENTS.md` and `intel-platform-OPERATIONS.md` already carry the
same marker-delimited authorization policy and required residual wording, so
R-CLOSE changes neither file.

The Rust package, Python package, FastAPI literal, this header, README heading,
and newest changelog heading now read 0.12.0. Cargo mechanically changed only
the local `cored` package version from 0.11.0 to 0.12.0 in `Cargo.lock`; no
dependency resolution moved. `CHANGELOG.md` says explicitly that v0.11.0
remains published with the threshold-source defect corrected forward by
INGEST-ATOMIC and THRESHOLD-ONE. The v0.11.0 tag, release commit, receipts,
report, and 54 evidence pins remain unchanged.

The reconciled release candidate passed the complete local definition of done.
`./run ci-local` passed **20/20** jobs with **121** Rust workspace tests,
**21** net tests, warning-denied offline/net builds, clippy, fmt, ShellCheck,
locked Rust 1.78 checks/tests, **205/205** Python 3.11.4 shell tests, golden
**11/11**, persisted fingerprints, all **71/71** pins, and protected databases
**2/2**. The independent Python 3.12.13 lane passed **205/205**, and both
interpreters verified **21/21** exact constrained packages. The mandatory
standalone `./run golden` then passed the same **11/11** byte-identical anchors.
`version-check`, `cycle-check`, `checklist-audit`, `progress-check`,
`invariant-scan`, manifest validation, protected-artifact verification,
`git diff --check`, and the independent 44-path count all passed. Before the
R-CLOSE checkbox, checklist auditing resolved **98/98** checked tasks with the
one v0.11 retraction reported and zero exemptions.

Publication succeeded without replacement. Release commit
`e5faf0c161a4256f33976664685653d8bd805d5d` contains the classified diff,
reconciled authorities, checked R-CLOSE task, and measured candidate record.
Annotated tag object `94d8215bc2151fecba1280dc793d3f5953cd8055`
has annotation `intel-platform v0.12.0` and peels exactly to that commit. One
atomic push advanced remote `main` from
`d664a7d3c524a3dfab932e158d9545953844b8dd` to the release commit and created
the tag. Read-only remote verification returned the release commit for
`refs/heads/main` and the peeled tag, and the annotated object for the tag ref.
This later append-only closing audit does not move the release tag.

With the exact closing record and R-CLOSE progress entry present, the
closed-state definition of done passed. `./run ci-local` again passed all
**20/20** jobs with **121** Rust workspace tests, **21** net tests,
warning-denied builds, clippy/fmt, locked Rust 1.78, **205/205** Python 3.11.4
tests, all **71/71** pins, protected databases **2/2**, and golden **11/11**.
The independent Python 3.12.13 lane passed **205/205** with **21/21** exact
packages, and the final standalone golden remained **11/11**. `cycle-check`
reported v0.12 closed with ten closed execution runbooks;
`checklist-audit` resolved **99/99** checked tasks, reported the one v0.11
retraction, and found zero exemptions; `progress-check` resolved R-CLOSE to the
release commit; `version-check` matched the exact annotated tag; all six
registered invariants passed. The audit commit that records these measurements
intentionally follows the release tag and does not move it.

**v0.11 cycle activation is complete; E0 has not yet run (measured
2026-07-27).** The read-only opener found only the operator-supplied untracked
`TASKS-v0.11-EXECUTION.md`; `AGENTS.md` correctly still declared the latest
closed cycle, v0.10.3. Entering HEAD was
`d24f2b83c9657b1fa47d7f3315a4120181f2624e`, described as
`v0.10.3-1-gd24f2b8`; local `main` and `origin/main` were aligned at that
commit with zero ahead / zero behind.

Implementation commit `57e56b7268345ea17dda6641dd2682295b43ec55`
admitted the reviewed runbook unchanged, declared v0.11 active, and created
its append-only progress log. The pre-admission `./run cycle-check` correctly
refused the uncommitted runbook because it had no first committed version.
After the implementation commit, `./run cycle-check` passed with v0.11 open
and eight closed execution runbooks; `./run checklist-audit` resolved the
entering 77/77 checked tasks with zero exemptions; `git diff --check` passed.
No test, golden, artifact, hosted-runner, publication, or release claim is
made by this preparatory correction. E0 restarts from the clean post-audit
tree.

**v0.11 E0 is complete (measured 2026-07-27).** The restarted opener produced
no `git status --porcelain=v1` output. HEAD was
`ac1b2ef9cc6b9913add42d22b2d4b23f10e2a29a`, described as
`v0.10.3-3-gac1b2ef`; the activation implementation/audit pair explains local
`main` being two commits ahead / zero behind `origin/main` at
`d24f2b83c9657b1fa47d7f3315a4120181f2624e`. The published v0.10.3 release
identity remained unchanged.

The first sandboxed `./run ci-local` attempt is an environment non-result:
every Rust, MSRV, lint, lifecycle, and evidence-rederivation unit passed, while
eight shell controls were denied `ps` or loopback binds and reported 179
passes / 8 permission failures. The permitted identical rerun passed all
**19/19** units with **99** Rust workspace tests, **20** net tests,
warning-denied offline/net builds, clippy/fmt, locked Rust 1.78 check/tests,
and **187/187** Python 3.11.4 shell tests. The independent Python 3.12.13 lane
also passed **187/187**; both interpreters verified the exact **21/21**
constrained packages and emitted the existing single third-party
Starlette/httpx deprecation warning.

Standalone `./run golden` passed **11/11** with every corpus, duplicate,
signal, rerun, entitlement, citation, snippet, and authentication anchor
unchanged. `./run verify-artifacts` matched the protected databases **2/2**
and manifest validation matched all **39/39** pinned files. A separate
`hashlib.sha256` witness read every declared pin itself and independently
reported **39/39** matches with zero mismatches. `version-check`,
`cycle-check`, `checklist-audit`, and `progress-check` passed; the checklist
entered v0.11 at **77/77** checked historical tasks with zero exemptions.

All eight defects and every augment row were confirmed against the clean
entering tree:

1. **S1:** `CORE_BIND` still flows directly from the environment/default into
   `TcpListener::bind`; source search found no `is_loopback` check.
   `CORE_TOKEN` is optional and `guard()` returns success when it is absent.
2. **S2:** `/docs` accepts only `ids`, calls the misleadingly named
   `parse_sectors(&p.ids)`, and reaches `documents_by_ids`, whose SQL has no
   sector predicate. `/embeddings/missing` accepts only `model` and enumerates
   bodies through `docs_missing_embeddings`, also with no sector predicate.
3. **S3:** parsing still chooses one longest-token group by strict `>` and
   clones only that group's rules, while the existing comment correctly
   protects a specific group from the unrelated `*` group.
4. **S4:** `path_matches` still compares the raw pattern and path; the crate
   contains no percent/decode/url-encoding implementation.
5. **S5:** `set_host_rate` still replaces the host's limiter with a fresh one,
   discarding both its `last` clock and per-host acquisition counter after the
   robots fetch.
6. **S6:** `Reach::Network` still skips publisher policy when
   `robots_cache` is `None`; the existing test deliberately asserts that
   fail-open behavior. The shipped net builder still refuses to start without
   constructing a cache, so the defect remains dormant at that caller.
7. **S7:** `_apply_events` still mutates the process-lifetime store event by
   event; a later `BillingError` raises HTTP 400 before `store.save()` but does
   not undo earlier in-memory mutations.
8. **S8:** `update_document` still performs a bare update and
   `delete_document` commits its delete transaction without rematerializing
   canonical ids. `assign_canonical_ids_tx` is already available; source
   search found no non-test caller of either maintenance method outside
   `sqlite.rs`.

The four required scratch controls demonstrated the wrong behavior before
being removed. Three temporary compliance tests passed while asserting that a
second `User-agent: intel-platform` group's disallow was ignored, that
`/foo/bar/%62%61%7A` evaded `/foo/bar/baz`, and that applying a ten-second
crawl delay reset `acquires_for` from one to zero and let the next paused-clock
acquire complete with zero elapsed time. A temporary signed-webhook test passed
while asserting that a two-event batch returned HTTP 400 yet left the first
event's `acme-research` sector mutation live. The scratch edits were removed,
and `git diff` returned empty before this record was written.

The v0.10.3 guards remain live. The committed receipt declares
`evidence_grade: release`, `attestations_required: true`, task
`v0.10.3 RECEIPT`, and the exact seven-member `(job, matrix)` identity set.
All seven accepted rows are distinct, verified, successful, and accompanied
by tracked, existing receipt/bundle paths; rejection count is zero. The fresh
and resumed adversarial paths both call the same
`_adversarial_outcome_invariant_error` checker, and protected validation plus
the independent witness matched all 39 pins. No runtime, dependency, lockfile,
architecture, protected byte, pinned evidence byte, provider configuration,
remote ref, or tag changed during E0.

**v0.11 BIND-LOOPBACK is complete (measured 2026-07-27).** `CORE_BIND`
now resolves through the standard library's `ToSocketAddrs` before configuration
or archive setup and before `TcpListener::bind`. The pure, socket-free
`loopback_only(&str) -> Result<Vec<SocketAddr>, String>` boundary accepts a
resolution only when it is nonempty and every resolved IP is loopback; the
listener consumes the already-validated addresses rather than resolving the
name a second time.

Three failure-capable unit tests reject `0.0.0.0:8788`, `[::]:8788`, a LAN
literal, and a synthetic hostname result containing both loopback and
non-loopback addresses; they accept IPv4 loopback, IPv6 loopback, and
`localhost`. The mixed-result refusal names `192.168.1.10:8788` and the
multi-host seam deferral. A first direct `target/debug/cored` probe was a
non-result because that binary predated the source change and reached the old
bind. After an explicit warning-denied rebuild, the same
`CORE_BIND=0.0.0.0:8788 target/debug/cored` command exited before binding and
reported the offending `0.0.0.0:8788` plus the multi-host design-task message.

The permitted `./run ci-local` passed all **19/19** units with **102** Rust
workspace tests, **20** net tests, zero rustc/clippy/format failures, locked
Rust 1.78 checks/tests, **187/187** Python 3.11.4 shell tests, golden **11/11**,
protected artifacts **2/2**, and all **39/39** pins. A required standalone
`./run golden` repeated **11/11**, and standalone `./run verify-artifacts`
repeated **2/2** exact databases plus **39/39** pins. `git diff` reports no
change under `run`, `deploy/`, any Cargo manifest, or `Cargo.lock`; no bind
override was introduced and no dependency changed. `ARCHITECTURE.md` and the
daemon contract now name the startup resolver/check as the enforcement
mechanism. The public API, corpus, protected artifacts, evidence pins, remote
refs, and tags are unchanged.

**v0.11 SECTOR-BIND is complete (measured 2026-07-27).** `/docs` now requires
both `ids` and `sectors` and calls
`documents_by_ids_in_sectors(ids, sectors)`. `/embeddings/missing` now requires
both `model` and `sectors` and calls the sector-bound
`docs_missing_embeddings(model, sectors)`. Both store methods return an empty
result for an empty sector set and include `sector IN (…)` in the SQL itself;
the id and sector values remain bound parameters. The old misleading
`parse_sectors(&p.ids)` call is gone in favor of the neutral `parse_csv`.

The shell passes subscriber entitlements to `/docs`. The embedding maintenance
worker and real-model verifier pass all sector ids reported by the core, so
backfill covers the configured archive rather than depending on which
subscriber happened to start it. Every Python call site and its doubles were
updated. Handler controls span technology and finance ids and prove that only
the entitled document returns; separate `/docs` and `/embeddings/missing`
controls prove empty sectors return nothing. The store-level bound-parameter
test independently exercises both new SQL scopes, and a shell transport test
captures the exact `sectors` query parameters.

`./run ci-local` passed all **19/19** units with **104** Rust workspace tests,
**20** net tests, zero warning/lint/format failures, locked Rust 1.78
checks/tests, and **188/188** Python 3.11.4 shell tests. A first sandboxed
Python 3.12.13 run was an environment non-result: the same eight process and
loopback controls seen at E0 were denied after 180 tests passed. The permitted
identical rerun passed **188/188**, with **21/21** exact packages. Standalone
`./run golden` repeated **11/11** exactly, proving the public `/v1/*` bodies and
corpus anchors did not move. Standalone artifact verification matched both
protected databases **2/2** and all pins **39/39**. No schema, dependency,
protected byte, evidence pin, remote ref, or tag changed.

**v0.11 ROBOTS-MERGE is complete (measured 2026-07-27).** The robots parser
now computes the longest matching non-`*` product-token specificity first and
then merges every group containing a matching token at that specificity, in
file order. When no specific token matches it merges every `*` group. A
specific match never receives `*` rules, and multiple applicable
`Crawl-delay` values resolve to the conservative maximum.

Four new failure-capable controls prove both halves. Duplicate
`intel-platform` groups enforce both disallows; the mandatory named regression
proves a generic `Disallow: /` cannot override a specific allow-all; a separate
specific-plus-generic control proves unrelated `*` rules are absent; and two
specific groups select the seven-second maximum delay over two seconds. The
parser doc-comment states the same-specificity merge and deliberate generic
exclusion explicitly.

`./run ci-local` passed all **19/19** units with **108** Rust workspace tests,
**20** net tests, zero warning/lint/format failures, locked Rust 1.78
checks/tests, **188/188** Python 3.11.4 shell tests, protected databases
**2/2**, and evidence pins **39/39**. Standalone `./run golden` repeated
**11/11** with every exact corpus and public-API anchor unchanged. Only the
compliance parser/tests plus required state and task records changed; no
dependency, lockfile, schema, protected byte, evidence pin, remote ref, or tag
changed.

**v0.11 ROBOTS-NORMALIZE is complete (measured 2026-07-27).** The compliance
crate now applies one zero-dependency normalizer to both robots rule patterns
and request paths before matching. Percent triplets for RFC 3986 unreserved
octets (`ALPHA`, `DIGIT`, `-`, `.`, `_`, `~`) decode to their literal byte.
Every other valid triplet stays encoded with uppercase hex. Reserved octets
are deliberately not decoded: `%2F` cannot re-segment a path, and `%2A` cannot
become the parser's `*` wildcard. Raw `*` and trailing `$` retain their existing
metacharacter behavior.

Five controls prove the boundary. `/foo/bar/baz` now blocks
`/foo/bar/%62%61%7A`; `%2f` becomes `%2F` rather than `/`; encoded `%2a` matches
its uppercase literal spelling but not arbitrary text; mixed-case hex
normalizes identically; and already-normalized plus once-normalized paths are
idempotent. The existing wildcard/end-anchor suite remains green.

`./run ci-local` passed all **19/19** units with **113** Rust workspace tests,
**20** net tests, zero warning/lint/format failures, locked Rust 1.78
checks/tests, **188/188** Python 3.11.4 shell tests, protected databases
**2/2**, and evidence pins **39/39**. Standalone `./run golden` repeated
**11/11** with every exact anchor unchanged. No crate was added; `Cargo.lock`,
schemas, protected bytes, evidence pins, remote refs, and tags are unchanged.

**v0.11 DELAY-CLOCK is complete (measured 2026-07-27).** A `RateLimiter` now
stores its minimum interval as atomic nanoseconds. `set_host_rate` remains
synchronous: it updates that atomic on an existing per-host limiter and creates
a limiter only for an unknown host. The async `last` mutex and `acquires`
counter therefore survive a rate transition on the same object. `acquire`
loads the current interval while holding the existing host clock. The
`apply_crawl_delay` comparison is unchanged and still adopts publisher policy
only when it slows the configured rate.

The new paused-clock control fetches `robots.txt` once to establish the host
clock and counter, applies a ten-second publisher delay, and observes the
counter remain one. The next acquire increments it to two but remains pending
after nine seconds, releases at exactly ten seconds, and leaves the counter at
two; `rate_for` reports `0.1` requests/second. Existing controls still prove a
publisher cannot speed up the configured floor and that one slow host does not
throttle another.

`./run ci-local` passed all **19/19** units with **114** Rust workspace tests,
**20** net tests, zero warning/lint/format failures, locked Rust 1.78
checks/tests, **188/188** Python 3.11.4 shell tests, protected databases
**2/2**, and evidence pins **39/39**. Standalone `./run golden` repeated
**11/11** with every exact anchor unchanged. No dependency, lockfile, schema,
protected byte, evidence pin, remote ref, or tag changed.

**v0.11 GATE-CLOSED is complete (measured 2026-07-27).** The shared ingest
`gate()` now returns the dedicated `NetworkWithoutRobotsCache` error whenever
`Reach::Network` is paired with `robots_cache: None`. The refusal precedes the
operator gate and limiter, and every shipped net document request already
calls this seam before its fetch. A network reach can therefore no longer omit
publisher policy by forgetting to construct the cache.

The former defect-encoding test was inverted in place: its public network path
now requires the new error. Its pre-T2 offline guarantee was preserved in a
sibling fixture-reach control, where a public path is still allowed and an
operator-denied path is still refused without fetching publisher policy.
Existing `Network` plus `Some(cache)` controls remain green for publisher
allow, publisher deny, operator deny, unreachable policy, missing-policy
opt-in, and redirect composition.

`./run ci-local` passed all **19/19** units with **115** Rust workspace tests,
**21** net tests, zero warning/lint/format failures, locked Rust 1.78
checks/tests, **188/188** Python 3.11.4 shell tests, protected databases
**2/2**, and evidence pins **39/39**. Standalone `./run golden` repeated
**11/11** with every exact anchor unchanged. No dependency, lockfile, schema,
protected byte, evidence pin, remote ref, or tag changed.

**v0.11 BILLING-ATOMIC is complete (measured 2026-07-27).** The shared neutral
event helper now constructs a detached in-memory `SubscriptionStore` from the
live store's frozen subscription values, applies and validates the complete
batch there, and publishes the resulting list to the process-lifetime store
only after every event succeeds. The routes retain their existing order:
publish the validated snapshot, call the selected backend's `save()` once,
then return the unchanged response shape. Authentication and the accepted
event vocabulary are unchanged.

Four controls cover the boundary. A signed two-event batch whose second event
is invalid returns HTTP 400 and leaves `acme-research` at its original science
plus technology sectors in live state. The path-backed control also observes
the JSON file unchanged after that 400, then performs an unrelated
`quant-desk` update and save and proves the rejected acme mutation still does
not land. A valid delete/create batch publishes every event and records exactly
one save. An unhandled neutral event inside a valid batch still returns its
`ignored` result while a sibling update commits, again with one save.
`apply_event`'s docstring now names detached batch staging as well as
caller-owned persistence.

`./run ci-local` passed all **19/19** units with **115** Rust workspace tests,
**21** net tests, zero warning/lint/format failures, locked Rust 1.78
checks/tests, and **191/191** Python 3.11.4 shell tests. The independent Python
3.12.13 lane also passed **191/191**; both emitted only the existing
third-party Starlette/httpx deprecation warning. Protected databases remained
**2/2** and evidence pins **39/39**. Standalone `./run golden` repeated
**11/11** with every exact anchor unchanged. No dependency, lockfile, schema,
protected byte, evidence pin, remote ref, or tag changed.

**v0.11 STORE-IDENTITY is complete (measured 2026-07-27).** Both public
maintenance writes now hold one SQLite transaction across their data mutation
and global canonical-id rematerialization. A successful `update_document`
recomputes identity after changing content, fingerprint, sector, or publication
order; a successful `delete_document` removes embeddings and the document,
then reassigns every survivor before commit. Missing-row operations retain
their clean `false` result without paying the scan. The ingest transaction and
both maintenance paths use the single store-local
`DEDUP_MAX_DISTANCE = 16` constant.

The doc-comments record the tradeoff: edits and takedowns are maintenance APIs,
not the ingest hot path, and correctness deliberately pays a corpus-wide scan.
The first warning-denied control invocation was a compile non-result because
the newly introduced constant was then referenced only from tests and therefore
failed the dead-code warning gate. After the already-existing ingest call was
routed through the constant, the still-unfixed methods produced the intended
evidence: **18/21** store tests passed and three controls failed. A body edit
left the survivor pointing at the old canonical, a publication-day change left
the old tie-break winner in place, and deleting the canonical left a surviving
row naming the deleted id. The no-op update control passed and preserved the
exact `(id, canonical_id)` rows.

After the transactional repair, all **21/21** store tests passed. The body edit
makes the former duplicate canonical to itself; the earlier publication date
moves both documents to the new winner; deleting the canonical yields zero
rows naming the deleted id and makes its survivor canonical; the no-op update
remains byte-identical. `./run ci-local` passed all **19/19** units with
**119** Rust workspace tests, **21** net tests, zero warning/lint/format
failures, locked Rust 1.78 checks/tests, and **191/191** Python 3.11.4 shell
tests. Standalone `./run golden` repeated **11/11**. Standalone
`./run verify-artifacts` matched protected databases **2/2** and evidence pins
**39/39**. No schema, dependency, lockfile, protected byte, evidence pin,
remote ref, or tag changed.

**v0.11 RE-MEASURE is complete (measured 2026-07-27).** The clean candidate
was `17221504d0c572e2b52f8509cb720d4a7c72f47d`; remote `main` was pushed to
that exact commit before the operator-authorized dispatch. GitHub Actions run
**30236305375**, attempt **1**, used `workflow_dispatch`,
`audit_sha=17221504d0c572e2b52f8509cb720d4a7c72f47d`, and
`publish_evidence=true`. Core, golden, lint, MSRV, net, shell
`python=3.11`, and shell `python=3.12` all passed. Each emitted one receipt
and one persisted Sigstore bundle, and all seven checkouts and receipt SHAs
name the candidate.

The first production-audit attempt in the clean detached candidate worktree
was a non-result before measurement because ignored `data/core.db` was absent.
An initial copy attempt was also a non-result because the fresh worktree had no
`data/` directory. After creating that ignored directory, the exact protected
database bytes were copied in: core SHA-256
`db2f186e291c64192e567c9dfb979dd9877eb32b13c2ce2724a4acf1761a37a0`
and live-smoke SHA-256
`94f03e9e8662dddfa5c80b63a9845d9926a1fa10060b83638ee094e0a0462c4a`.
`git status --porcelain` remained empty, so the measurement subject was still
a clean candidate tree.

The production command required `--expected-head`,
`--evidence-grade release`, `--require-attestations`, repository and workflow
identity, source digest, and `refs/heads/main`. It accepted **7** authenticated
receipts with the exact distinct identity set, rejected **0**, and recorded
**7** observed runner executions. The report is labeled `v0.11 RECEIPT`,
records a clean subject, and reports **5 deferred / 2 promoted**: the five
unchanged deferrals remain T7 single-flight, Postgres, pgvector, multi-host
hardening, and A4; CI-runner evidence is promoted by the complete authenticated
matrix, while `/view` materialization remains promoted to its future
implementation task. Exact-cosine p95 was **15.033417 ms** over 2,600
documents, below the **16.264 ms** A3 anchor. The report is
`evidence/v0.11.0/deferred-audit/report.json`, **33,741 bytes**, SHA-256
`2bfade7c8bf5d39323a91d0a599b4576bc83a9bdce1ef9c29cca7d7db82d3d71`.
Fresh re-derivation passed with rows 7, source dispositions 5, triggers 7,
release grade, and attestations required.

Both hosted negative controls ran only on the disposable
`codex/v0.11-remeasure-controls` branch. Run **30236791703** planted one core
failure; all seven signed packages persisted, the audit rejected the core
receipt as `conclusion is not success: failure`, found the core identity
missing, and accepted/observed **0** executions. Run **30237021683** passed all
seven jobs but rewrote the signed Python 3.12 receipt to claim
`python=3.11`; the audit found the duplicate 3.11 identity and missing 3.12
identity and again accepted/observed **0**. A preceding dispatch command against
control commit `33e99893e707dc53dffb01f4eeda6fef51c42034` returned HTTP 422 before
creating a run because its one-line YAML scalar was not dispatchable; the
block-scalar correction was re-parsed and the source-shape test repeated
**36 passed / 1 skipped** before the successful control dispatch. The remote
branch, local branch, and disposable worktree were then deleted; neither
negative receipt set nor report was committed.

Manifest validation and standalone artifact verification now match all
**54/54** immutable file pins and both protected databases **2/2**. The full
local matrix passed **19/19** with **119** Rust workspace tests, **21** net
tests, zero rustc/clippy/format failures, locked Rust 1.78 checks/tests, and
**191/191** Python 3.11.4 shell tests. The independent Python 3.12.13 lane
passed **191/191** with **21/21** exact packages; both lanes emitted only the
known third-party Starlette/httpx deprecation warning. Mandatory standalone
golden remained byte-identical at **11/11**. Remote tag enumeration still maps
the published v0.9.0, v0.10.0, v0.10.1, and v0.10.3 annotated objects to their
unchanged peeled commits; no tag was created, moved, or published in this task.

**v0.11 R-CLOSE selected and published the minor release (measured
2026-07-27).** The operator explicitly approved release and publication of
`v0.11.0`. The gate was open: RE-MEASURE authenticated seven
distinct successful identities with zero rejection, both hosted negative
controls accepted zero executions, all 54 evidence pins and both protected
databases match, and the complete local definition of done was green before
release reconciliation.

The minor disposition follows `ARCHITECTURE.md §8`. `/docs` and
`/embeddings/missing` gain required internal sector parameters; loopback bind,
robots evaluation, network-policy failure, billing rejection, and maintenance
identity behavior change. Public `/v1/*` JSON bodies, the SQLite schema, cache
representation, dependency resolution, and golden retrieval outputs are
unchanged. This is the same internal-API and runtime-change basis used for the
v0.10.0 minor release, not an evidence-only patch.

The complete `v0.10.3..release-candidate` diff contains **40 paths**, each
classified exactly once:

- **release and public documentation (5):** `README.md`, `CHANGELOG.md`,
  `Cargo.lock`, `apps/cored/Cargo.toml`, and
  `shell/intel_shell/__init__.py`.
- **architecture and invariant authority (1):** `ARCHITECTURE.md`.
- **core runtime and store behavior (4):** `apps/cored/src/main.rs`,
  `crates/compliance/src/lib.rs`, `crates/ingest/src/lib.rs`, and
  `crates/store/src/sqlite.rs`.
- **shell runtime behavior (4):** `shell/intel_shell/app.py`,
  `shell/intel_shell/billing.py`, `shell/intel_shell/core_client.py`, and
  `shell/intel_shell/pipeline.py`.
- **executable verifier and tests (4):** `tools/verify_llm.py`,
  `shell/tests/test_billing.py`, `shell/tests/test_shell.py`, and
  `shell/tests/test_verify_llm.py`.
- **evidence configuration (1):** `config/protected-artifacts.json`.
- **durable evidence (15):** all fourteen receipt/bundle files under
  `evidence/ci-runs/30236305375-1/` and
  `evidence/v0.11.0/deferred-audit/report.json`.
- **operating, state, and task records (6):** `AGENTS.md`,
  `PROGRESS-v0.10.3.md`, `PROGRESS-v0.11.md`, `STATE.md`,
  `TASKS-v0.10.3-EXECUTION.md`, and `TASKS-v0.11-EXECUTION.md`.

`ARCHITECTURE.md` now states the enforced loopback startup refusal, identifies
`/docs` and `/embeddings/missing` in the HC2 core-SQL boundary, and says
plainly that `/attest` protects the trusted shipped path but a rewritten shell
can still bypass or falsify the handoff. A4 therefore remains open. `README.md`
names the required sector parameters and the measured 119-workspace /
191-shell counts. `AGENTS.md` already has the correct cycle-neutral closure
semantics: v0.11 remains the declared cycle after its closing record is
appended, until an operator supplies another runbook.

The Rust package, Python package, FastAPI literal, this header, and newest
changelog heading now read 0.11.0. Cargo mechanically changed only the local
`cored` package version from 0.10.3 to 0.11.0 in `Cargo.lock`; no dependency
resolution moved. An intermediate `./run version-check` correctly refused the
still-old STATE authority while the other four authorities read 0.11.0; the
reconciled candidate then passed all five authorities.

Publication disposition is explicit. The operator selected and published
v0.11.0 after the authenticated success and failure controls passed. Annotated
tag object `fcfa4825e6ffbc06c0ad73e18044965c10786aa8` dereferences exactly to
release commit `6daeb7e9f2cc0022b5e1a1dcf2ce8702b5be0321`. One atomic push
advanced remote `main` to that commit and created the tag; remote verification
returned the exact tag object, peeled commit, and main commit. This later
append-only closing record does not move the tag. v0.10.2 remains local and
unpublished at annotated tag object
`d821f8b2eb6f39fe4a7d06a88cd61de771c7b0ba`, dereferencing to
`7d127abac0b993c9e98294ee1c03ff01153de9d0`; this release does not move or
publish it.

The reconciled release candidate passed the complete local definition of done.
`./run ci-local` passed all **19/19** jobs with **119** Rust workspace tests,
**21** net tests, warning-denied builds, clippy/fmt, locked Rust 1.78
check/tests, **191/191** Python 3.11.4 shell tests, golden **11/11**, protected
databases **2/2**, all **54/54** pins, persisted fingerprints, and every
lifecycle auditor. The independent Python 3.12.13 lane passed **191/191** with
the same single third-party Starlette/httpx warning, and both interpreters
verified **21/21** exact packages. `version-check` reconciled all five
authorities at 0.11.0 with the expected pre-tag warning and then matched the
exact annotated HEAD tag after creation; cycle, checklist, progress, manifest,
and `git diff --check` passed. The 40-path inventory matches the Git diff
exactly.

With the R-CLOSE box checked, the exact closing record appended, and the
R-CLOSE progress entry present, the closed-state definition of done passed.
The first restricted-sandbox `./run ci-local` was a non-result for eight shell
tests because the environment denied loopback socket creation and `ps` access;
every other completed lane passed. The exact rerun with the required system
access passed all **19/19** jobs. `cycle-check` reported v0.11 closed with nine
closed execution runbooks; `checklist-audit` resolved **88/88** checked tasks
with zero exemptions; `progress-check` resolved R-CLOSE to the release commit;
`version-check` matched the exact HEAD tag; all **54/54** pins and protected
databases **2/2** matched. The independent Python 3.12.13 lane passed
**191/191** with **21/21** exact packages, and the final standalone golden
remained **11/11**. The audit commit that records these measurements
intentionally follows the release tag and does not move it.

**v0.10.3 R-CLOSE selected and published the patch release (measured
2026-07-26).** The operator explicitly approved release
`v0.10.3`. The publication gate is open: RE-MEASURE authenticated seven
distinct successful identities with zero rejection, both hosted negative
controls accepted zero executions, and neither EVIDENCE-DURABLE nor
LITERAL-NEUTRAL records a publication-blocking residual gap.

The patch disposition follows `ARCHITECTURE.md §8`. This cycle hardens matrix
identity, mandatory release authentication, resumed-evidence invariants,
durable evidence paths, lifecycle enforcement, and cycle-neutral labeling. It
adds tests and immutable receipt, bundle, and report evidence. It does not
change public or internal API behavior, runtime behavior, storage paths,
database schema, cache representation, licensing outcomes, dependencies, or
retrieval outputs.

The complete `v0.10.2..release-candidate` diff contains **69 paths**, each
classified exactly once:

- **release and public documentation (6):** `README.md`, `CHANGELOG.md`,
  `Cargo.lock`, `apps/cored/Cargo.toml`, `shell/intel_shell/__init__.py`, and
  `shell/intel_shell/app.py`.
- **workflow, harness, and evidence configuration (4):**
  `.github/workflows/ci.yml`, `run`, `config/cycle-history.json`, and
  `config/protected-artifacts.json`.
- **executable audit controls and tests (10):**
  `shell/tests/test_cycle_check.py`, `shell/tests/test_deferred_audit.py`,
  `shell/tests/test_evidence_artifacts.py`,
  `shell/tests/test_verify_llm.py`, `tools/audit_deferred.py`,
  `tools/benchmark_view.py`, `tools/cycle_check.py`,
  `tools/cycle_identity.py`, `tools/evidence_artifacts.py`, and
  `tools/verify_llm.py`.
- **durable evidence (43):** the seven flat
  `evidence/ci-runs/30187058897-1-*.json` compatibility paths; all seven
  receipts in `evidence/ci-runs/30187058897-1/`; all fourteen receipt/bundle
  files in `evidence/ci-runs/30194678764-1/`; all fourteen receipt/bundle files
  in `evidence/ci-runs/30202019640-1/`; and
  `evidence/v0.10.3/deferred-audit/report.json`.
- **operating, state, and task records (6):** `AGENTS.md`,
  `PROGRESS-v0.10.2.md`, `PROGRESS-v0.10.3.md`, `STATE.md`,
  `TASKS-v0.10.2-EXECUTION.md`, and `TASKS-v0.10.3-EXECUTION.md`.
- **architecture, runtime, storage, dependency-resolution, public-API, or
  internal-API behavior paths (0):** none. `ARCHITECTURE.md` was reconciled and
  remains authoritative without a diff.

The Rust package, Python package, FastAPI literal, this header, and newest
changelog heading now read 0.10.3. Cargo mechanically regenerated
`Cargo.lock` and changed only the `cored` package version from 0.10.2 to
0.10.3; no dependency resolution moved. `README.md` now names the current
release, all twelve core endpoints including `/attest`, and the measured
99-workspace / 187-shell test counts. `AGENTS.md` now describes every older
closed runbook without a stale enumerated cycle list. Its active declaration
remains v0.10.3 after closure until the operator supplies the next runbook.

Publication disposition is explicit. v0.10.2 remains local and unpublished at
its original annotated tag object, and v0.10.3 did not change that. v0.10.3
was published because the operator selected release after RE-MEASURE satisfied
the real success and failure controls. Annotated tag object
`215cfcdbb78e1274a845fdd08a0f17e3d87c94e3` dereferences exactly to release
commit `d86ba26e38ff41efbae997a1f909d124a6d6e969`. The atomic remote push advanced
`main` to that commit and created the tag; read-only remote verification
returned the same tag object and dereferenced commit. The separate append-only
closing record does not move the tag.

The release candidate passed the complete local definition of done.
`./run ci-local` passed all **19/19** jobs with **99** Rust workspace tests,
**20** net tests, warning-denied builds, clippy/fmt, locked Rust 1.78
check/tests, **187/187** Python 3.11 shell tests, golden **11/11**, protected
databases **2/2**, all **39/39** pins, persisted fingerprints, and every
lifecycle auditor. The independent Python 3.12.13 lane passed **187/187** with
the same single third-party Starlette warning, and both interpreters verified
**21/21** exact packages. Standalone manifest validation, protected
verification, golden, version consistency, and `git diff --check` passed. The
69-path inventory matches the Git diff exactly.

**v0.10.3 RE-MEASURE is complete (measured 2026-07-26).**
Operator-authorized hosted run **30202019640**, attempt **1**, passed all seven
expected jobs against exact candidate
`a1d8c958b4eaf4fe4add75cc49a7fec341c8f8a5`. Every receipt carried
`conclusion:"success"`, the exact subject/event SHA, repository, workflow, and
one of the seven distinct expected `(job, matrix)` identities. Real
source-pinned Sigstore verification accepted all seven persisted bundles with
the CI workflow certificate identity, source/signer digest `a1d8c958…`,
source ref `refs/heads/main`, and GitHub-hosted runner policy.

The clean detached production audit accepted **7**, rejected **0**, found a
complete matrix with no findings, and measured **5 deferred / 2 promoted**.
The exact-cosine p95 was **8.390958 ms**. The release-grade report is 33,754
bytes at SHA-256
`272487af426675c3b5f3be25f5521f5a03bc5f148cd8d50c5651a692c5993c51`.
Its seven receipts, seven attestation bundles, and report are committed under
run-scoped repository paths and pinned as 14 supporting artifacts plus one
release artifact. Manifest validation and protected-artifact verification
passed all **39/39** file pins and both protected databases **2/2**.

Network-enabled release re-derivation passed with seven rows, five
source-deterministic dispositions, seven trigger texts, release evidence grade,
attestations required, and view materialization false. An initial restricted
sandbox invocation could not initialize any Sigstore verifier and therefore
rejected all seven rows; no assertion or evidence byte changed, and the exact
command passed when allowed to reach the trust services.

Both required real negative controls remain measured. Run **30201489016**
persisted its signed artifacts after the planted core failure; the guard named
the failed conclusion and missing core identity, then accepted zero
executions. Mixed-control run **30201602108** was canceled rather than conflated
with the duplicate test. Isolated run **30201653302** passed all seven hosted
jobs and attestations but made both shell receipts claim `python=3.11`; the
guard named the duplicate and missing `python=3.12` identity, then accepted
zero executions. The throwaway remote and local branch and worktree were
deleted.

Both complete shell lanes passed **187/187** under Python 3.11.4 and 3.12.13,
with the existing single Starlette deprecation warning. `./run ci-local`
passed **19/19** with 99 workspace tests, 20 net tests, warning-denied builds,
clippy/fmt, locked Rust 1.78, lifecycle and evidence checks, persisted
fingerprints, protected databases **2/2**, and all **39/39** pins. The required
standalone `./run golden` remained byte-identical at **11/11**. No product
runtime, dependency, lockfile, architecture, protected byte, prior pinned
evidence byte, provider configuration, or tag changed.

**v0.10.3 EVIDENCE-PATH-ADMISSION correction is complete locally (measured
2026-07-26).** Authenticated hosted run **30201306837**, attempt **1**, passed
all seven expected jobs against exact checkout
`725b8820c29fd4e6dac8be1c32b69f59f2a6fc35`. Its seven downloaded receipts
carried the exact distinct identity set, `conclusion:"success"`, repository
`jiayanzeng/intel-platform`, workflow `CI`, exact subject/event SHA, and two
shell matrix values. Real `gh attestation verify` accepted every persisted
bundle with source/signer digest `725b8820…`, source ref `refs/heads/main`, the
expected workflow, and GitHub-hosted runner policy. The clean production preview
accepted **7**, rejected **0**, and measured **5 deferred / 2 promoted**.

That preview also produced a real durability finding: receipts outside the clean
subject worktree were correctly recorded at their absolute temporary paths, but
the compatibility `logical_path` omitted the run-scoped directory. Such a
report cannot pass release-grade manifest validation and was not admitted or
hand-edited. `--evidence-repository` now separates the clean measured subject
from the worktree that will commit its raw evidence. Every recorded receipt and
bundle must resolve inside that worktree's exact Git root, be present in its
index, and match its indexed bytes. Only then does the report persist the true
repository-relative nested path; untracked and post-stage-mutated files fail.

The two new path controls passed, and the focused selected set passed **3/3**.
Both complete shell lanes passed **187/187**, with the existing single Starlette
deprecation warning. `./run ci-local` passed **19/19** with 99 workspace tests,
20 net tests, warning-denied builds, clippy/fmt, locked Rust 1.78, strict
lifecycle checking, evidence re-derivation, persisted fingerprints, protected
databases **2/2**, and all **24/24** pins. The required standalone
`./run golden` remained byte-identical at **11/11**. No product runtime,
dependency, lockfile, architecture, protected byte, pinned evidence byte,
provider configuration, or tag changed.

The real negative controls are already complete. Run **30201489016** failed only
the planted `core` step, persisted all signed artifacts, and the authenticated
guard rejected its `conclusion:"failure"` receipt, named the missing core
identity, and accepted zero executions. The first duplicate attempt
**30201602108** was canceled because the deliberate workflow edit would also
trip its source-shape assertion. The isolated duplicate run **30201653302**
then passed all seven hosted jobs and attestations; both shell receipts claimed
`python=3.11`, so the guard named the duplicate subject and missing
`python=3.12` identity and accepted zero executions. Remote and local
`codex/v0.10.3-remeasure-controls` refs and its temporary worktree were deleted.

**v0.10.3 HOSTED-CYCLE-GATE correction is complete locally (measured
2026-07-26).** The first operator-authorized RE-MEASURE dispatch was hosted run
**30201012362**, attempt **1**, against exact checkout
`87fa115bb5279694fb21fcb140545583ba29471a`. Six expected jobs passed. The
Python 3.11 shell job failed at `./run cycle-check` before its remaining checks:
the full local lifecycle guard could not resolve recorded annotated-tag objects
for local-only `v0.8.0` and `v0.10.2` refs. This was a real hosted failure and is
not counted as successful release evidence.

`git ls-remote --tags origin` measured only the published annotated releases
`v0.9.0`, `v0.10.0`, and `v0.10.1`; it confirmed that the two failing tag refs
are absent from the remote. Their recorded release commits are nevertheless
ancestors of remote `main`. The correction therefore adds the explicit
`--skip-local-tag-verification` mode for remote clones. It skips only resolution
of local annotated-tag refs and their tag objects. It still validates every
closing record, requires each recorded release commit to be a present commit
object, enforces active/open and historical/closed lifecycle rules, rejects
stale source literals, and checks runbook amendment disclosure. Plain
`./run cycle-check` remains strict and still verifies every local tag object and
dereferenced release commit.

The failure-capable lifecycle suite passed **9/9**. One new control proves the
strict command refuses an unavailable historical tag while hosted mode accepts
the same present release commit; a second proves hosted mode still refuses a
nonexistent recorded release commit. Both complete shell lanes passed
**185/185**, with the existing single Starlette deprecation warning.
`./run ci-local` passed **19/19** with 99 workspace tests, 20 net tests,
warning-denied builds, clippy/fmt, locked Rust 1.78, strict local lifecycle
checking, evidence re-derivation, persisted fingerprints, protected databases
**2/2**, and all **24/24** pins. The required standalone `./run golden` remained
byte-identical at **11/11**. No product runtime, dependency, lockfile,
architecture, protected byte, pinned evidence byte, provider configuration,
or tag changed.

**v0.10.3 LITERAL-NEUTRAL is complete (measured 2026-07-26).**
New deferred-audit and adversarial report labels now derive from
`tools/cycle_identity.py`'s one active-cycle declaration. View benchmark labels
are cycle-independent. The three intentionally historical evidence inputs live
once in the validated semantic registry `config/cycle-history.json`; tools,
the harness, and the hosted workflow resolve those keys rather than embedding
their versioned paths. The harness's usage examples are cycle-neutral.

`cycle-check` now scans every Python file in `tools/`, `run`, and both YAML
workflow extensions for concrete `TASKS-…` / `PROGRESS-…` filenames and bare
`v<major>.<minor>[.<patch>]` literals. The active declaration remains the only
live cycle authority; the history registry is validated for schema, relative
repository-contained paths, existence, regular files, and uniqueness. A direct
repository scan returned zero concrete cycle literals in all three guarded
source locations. The hosted Python 3.11 shell job now runs `./run cycle-check`
with its explicit local-tag-ref omission, using its existing full-history
checkout; the correction above records why the strict local form cannot run
against the repository's intentionally smaller remote tag topology.

The amendment assertion is executable. For the active runbook, `cycle-check`
loads the blob from the commit that first added the file and compares each
Step's exact **Objective**, **Acceptance criteria**, and **Done when** block.
Any changed field requires that Step to appear under one dated
`## Runbook amendments` entry. Missing fields and removed Steps are changes,
and malformed dates or duplicate amendment headings are refused. Normal
checkbox progress is outside the compared contract fields.

The three permanent controls failed **3/3** before the guard changed: a planted
tool label, a stale harness evidence path, and an undisclosed acceptance edit
all incorrectly passed `cycle-check`. Afterward, the complete lifecycle module
passed **7/7**: those controls and a planted workflow literal were refused,
the clean tree passed, and a correctly dated disclosed edit passed. The focused
report/benchmark/lifecycle/audit set passed **76/76**.

The closed-cycle record was corrected without touching evidence bytes.
`PROGRESS-v0.10.2.md` and this file now carry dated
`Closed-cycle status correction` banners explaining that the immutable
v0.10.2 deferred report's `v0.10.1 RECEIPT` task label is wrong, while the
artifact remains correctly pinned at
`4e11a8b3a3a64b5519469289f5cdf246bf13a0045954aa22c38703bbe6d29d9b`.
Direct SHA-256 and manifest verification confirmed the report is still exactly
28,968 bytes at that hash; the pin did not move.

Both full shell lanes passed **183/183** with the existing single Starlette
deprecation warning. Python compilation, `bash -n run`, ShellCheck,
`git diff --check`, the semantic historical re-derivation, and direct
`cycle-check` passed. The final `./run ci-local` passed **19/19** with 99
workspace tests, 20 net tests, warning-denied builds, clippy/fmt, locked Rust
1.78, evidence re-derivation, persisted fingerprints, protected databases
**2/2**, and all **24/24** pins. The required final standalone `./run golden`
remained byte-identical at **11/11**. No product runtime, dependency, lockfile,
architecture, protected byte, pinned evidence byte, provider configuration,
remote ref, or tag changed.

**v0.10.3 EVIDENCE-DURABLE is complete (measured 2026-07-26).**
The production verifier now threads the installed GitHub CLI's
`--signer-digest`, `--source-digest`, and `--source-ref` policy flags from
required release-grade `--expected-source-digest` and
`--expected-source-ref` arguments. It retains the existing repository,
workflow, and `--deny-self-hosted-runners` constraints, requests JSON output,
and independently checks that the returned certificate has one non-empty
identity and exactly the expected source digest, signer digest, and ref.
Every accepted receipt row persists that certificate identity and the three
source-revision fields.

The operator-authorized authenticated download recovered all seven receipts
and all seven `.sigstore` bundles from successful hosted workflow run
**30194678764**, attempt **1**, before its 2026-10-24 retention expiry.
All seven receipts name subject commit
`e5af6bc5df8261cc004bd4d3247b70f8cbe930bb` and event/source commit
`817e7f3e7c1878c18f474532df4d50c2b17fcbdc`. Real `gh attestation verify`
accepted every pair with repository `jiayanzeng/intel-platform`, signer
workflow `jiayanzeng/intel-platform/.github/workflows/ci.yml`, source digest
`817e7f3e7c1878c18f474532df4d50c2b17fcbdc`, source ref
`refs/heads/main`, GitHub-hosted runner policy, and certificate identity
`https://github.com/jiayanzeng/intel-platform/.github/workflows/ci.yml@refs/heads/main`.
The direct seven-file measurement returned complete `true`, observed **7**,
and rejected **0**. A real wrong-source-digest control substituted forty
zeroes; `gh` rejected it with exit **1** and named the expected/actual
`SourceRepositoryDigest`.

The durable convention is now
`evidence/ci-runs/<run_id>-<attempt>/`. The seven legacy run
30187058897 receipts were moved into that layout; tracked compatibility
symlinks keep the immutable v0.10.1 report's original flat paths resolving to
the one stored copy. Run 30194678764 contributes its seven receipt/bundle
pairs under the same convention. The manifest now pins the three immutable
reports, seven legacy receipts, seven authenticated receipts, and seven
authenticated bundles: **24/24** pins matched exact bytes and SHA-256 values.

Path recording no longer rewrites a temporary measurement path into a
fictional repository path: it records the true absolute path and an explicit
`logical_path` while external, and the true repository-relative path once
committed. Release-grade manifest validation now requires every recorded
receipt and bundle path to be pinned, resolve inside the repository, and name
a regular file; it also requires each row's certificate and source fields to
match the report's pinned revision. The immutable v0.10.1 report still
re-derived successfully through the compatibility paths.

Three selected controls failed **3/3** against the old implementation: the
runner guard could not accept source policy, the verifier did not return
source/certificate identity, and release-pin validation accepted unresolved
recorded paths. After implementation the expanded selected set passed
**4/4**. The focused deferred-audit/artifact suites passed **50/50** under
both supported interpreters. Both complete shell lanes passed **178/178**
with the existing single Starlette deprecation warning.

The first sandboxed `./run ci-local` attempt passed every non-shell stage but
was an environment non-result because `ps` and loopback binds were denied.
The permitted identical run passed all **19/19** jobs: 99 workspace tests,
20 net tests, warning-denied builds, clippy/fmt, locked Rust 1.78,
178 Python tests, structural re-derivation, persisted fingerprints, protected
databases **2/2**, and **24/24** pins. Standalone manifest validation and
`./run verify-artifacts` passed, Python compilation and `git diff --check`
passed, and the required standalone `./run golden` remained byte-identical at
**11/11**. No product runtime, dependency, lockfile, architecture, protected
database byte, existing pinned report byte, provider configuration, remote
ref, or tag changed.

**v0.10.3 RESUME-INVARIANT is complete (measured 2026-07-26).** One
shared executable consistency checker now guards both the fresh adversarial
classifier and every schema-complete resumed attempt. It enforces all five
one-way implications: public overlap requires `LEAK`; raw overlap requires
`GUARD FIRED` or `LEAK`; `GUARD FIRED` requires raw overlap, no public
overlap, and at least one violation id; `NOT EXERCISED` forbids both overlap
flags; and `LEAK` requires at least one overlap flag. It also refuses
`raw_overlap: false` when the recorded longest gated token run reaches the
16-token attestation threshold.

Resume now binds each completed attempt to the report declaration. The target
must be in `battery.target_doc_ids`, the shape must be one of the five
`ADVERSARIAL_SHAPES`, and the model must equal the declared chat model.
Schema-incomplete and transport-incomplete attempts remain retryable. A
schema-complete contradiction is instead recorded under
`halted_on_resumed_invariant` with target, shape, and reason, then raises the
distinct `ResumedAttemptInvariantError`; it is treated as tampering and is
never silently discarded. A consistent resumed `LEAK` retains the existing
`ResumedLeakError` emergency halt.

The seven contradiction/declaration controls failed **7/7** against the old
validator while the positive committed-evidence control passed **1/1**. After
the change all **8/8** selected controls passed: the audit substitution,
empty-violation guard result, overlap-free leak, telemetry contradiction,
out-of-battery target, unknown shape, and mismatched model all halted; the
immutable X-REGEN report reused all **45/45** attempts with counts unchanged
at 45 `NOT EXERCISED`, zero `GUARD FIRED`, and zero `LEAK`.

The complete verifier module passed **31/31** and both full shell lanes passed
**175/175** under Python 3.11.4 and 3.12.13, with the existing single
Starlette deprecation warning. Python compilation and `git diff --check`
passed. `./run golden` remained byte-identical at **11/11**. Both protected
databases matched **2/2**, manifest validation passed, and all three pinned
JSON reports—including the unchanged 62,978-byte X-REGEN report—matched.
Only the verifier harness and its tests changed; no product runtime,
dependency, lockfile, architecture, protected byte, evidence byte, provider
configuration, remote ref, or tag changed.

**v0.10.3 AUTH-REQUIRED is complete (measured 2026-07-26).**
Production deferred audits require
`--evidence-grade {structural,release}`. Release grade derives mandatory
attestation verification and refuses to measure without a bundle directory,
expected repository, and expected workflow. Structural grade rejects
authentication arguments, stamps the report explicitly, and remains the
token-free default selected by the local `./run audit-deferred --output …`
wrapper.

New reports record `evidence_grade` and `attestations_required` at top level.
Re-derivation compares both values and every accepted receipt's
`attestation_verified` flag. Legacy immutable receipts remain byte-exact:
v0.10.1's unauthenticated posture is derived from its false/missing flags,
while v0.10.2's authenticated posture is derived from its seven verified
accepted rows. No legacy report can silently acquire release grade.

Every pinned file now has a manifest grade. The immutable v0.10.1 deferred
report is `structural`, its real-model report is `supporting`, and the
immutable v0.10.2 deferred report is `legacy`. A new pin labeled `release`
must contain a JSON deferred report declaring release grade, requiring
attestations, and carrying at least one accepted receipt whose bundle name is
non-empty and whose verification flag is true.

The selected failure-before controls produced **5 failures / 1 pass** under
the old tooling: production did not require a grade, release posture was not
re-derived, a tampered legacy authentication declaration was accepted, and
the pin schema could neither express nor enforce release grade. The genuine
release re-derivation control already passed its unrelated legacy checks.
After implementation, all **7/7** selected controls passed. The focused
deferred-audit and artifact suites passed **47/47** on both Python 3.11.4 and
3.12.13; both full shell lanes passed **167/167** with the existing single
Starlette deprecation warning.

The complete permitted `./run ci-local` passed **19/19**: 99 workspace tests,
20 net tests, warning-denied Rust builds, clippy/fmt, locked Rust 1.78,
167 Python 3.11 tests, token-free structural re-derivation, golden **11/11**,
protected evidence **2/2**, and all three pins. Python compilation,
`bash -n run`, `git diff --check`, and direct manifest validation also passed.
The immutable v0.10.1 structural report re-derived successfully. Direct
source re-derivation of the v0.10.2 authenticated report still cannot promote
its CI row because its seven recorded raw receipts and bundles are absent;
that is the already-confirmed G4b input gap assigned to EVIDENCE-DURABLE, not
an inferred pass. No product runtime, dependency, lockfile, architecture,
protected byte, pinned evidence byte, provider configuration, remote ref, or
tag changed.

**v0.10.3 MATRIX-ID is complete (measured 2026-07-26).** The count map was
replaced on the production path by the exact identity set `core`, `golden`,
`lint`, `msrv`, `net`, `shell/python=3.11`, and `shell/python=3.12`.
Single-leg jobs must omit `matrix`; shell must carry one of its two declared
values. Missing, unknown, and unexpected matrix shapes have distinct rejection
reasons. The accepted rows now retain `matrix`, `workflow`, `repository`, and
`event_sha`.

The guard rejects a repeated `(job, matrix)` subject and separately rejects
identical receipt content digests even under different filenames. Any duplicate,
missing identity, unexpected identity, mixed run id/attempt, rejected receipt,
or incomplete identity set yields zero observed executions and an empty
accepted set. The workflow already emitted `matrix` on the shell job only; an
executable source assertion now pins that shape.

The permanent authenticated duplicated-leg control copied the Python 3.11
receipt bytes over the Python 3.12 filename while supplying all seven synthetic
bundles. Against the old guard, the selected control set failed **5/5**: the
duplicated set was incorrectly accepted as seven executions, all three malformed
matrix shapes promoted, and accepted rows lost matrix identity. After the
change the same set passed **5/5**; the duplicate produced both subject and
content-digest findings and deferred with zero accepted executions.

Immutable reports and old runner bytes are not rewritten and no matrix is
inferred from a filename. Source re-derivation detects the absence of the new
`expected_job_identities` report field and explicitly replays that historical
report's count contract. The production report-creation path does not expose
this compatibility option and always emits the exact identity contract. The
committed v0.10.1 deferred report still re-derived with five source
dispositions and seven triggers.

The focused deferred-audit suite passed **28/28** on Python 3.11.4 and
3.12.13. Both full shell lanes passed **160/160** with the existing single
Starlette deprecation warning. Python compilation and `git diff --check`
passed. Standalone `./run golden` remained byte-identical at **11/11**.
Protected databases matched **2/2**, all three JSON pins matched, and manifest
validation passed. No product runtime, dependency, lockfile, architecture,
protected byte, evidence pin, provider configuration, remote ref, or tag
changed.

**v0.10.3 E0 is complete (measured 2026-07-26).** The restarted opener
produced no `git status --porcelain=v1` output. HEAD was
`4c70da5760a25fe5781ce7d09d6350cda69187d9`, described as
`v0.10.2-3-g4c70da5`; the preparatory implementation/audit pair explains local
`main` being six commits ahead / zero behind `origin/main` at
`817e7f3e7c1878c18f474532df4d50c2b17fcbdc`. The local annotated v0.10.2
tag remained object `d821f8b2eb6f39fe4a7d06a88cd61de771c7b0ba`
dereferencing exactly to release commit
`7d127abac0b993c9e98294ee1c03ff01153de9d0`; the authenticated remote tag
census still contained v0.10.0 and v0.10.1 only.

The first sandboxed `./run ci-local` attempt is an environment non-result:
Rust, MSRV, lint, lifecycle, and evidence re-derivation passed, while eight
shell controls failed because the environment denied loopback binds and
`ps`. The permitted identical rerun passed all **19/19** jobs with **99**
workspace tests, **20** net tests, warning-denied builds, clippy/fmt, locked
Rust 1.78 check/tests, and **156/156** Python 3.11.4 shell tests. The
independent Python 3.12.13 lane passed **156/156** and both interpreters
verified the exact **21/21** constrained packages.

Standalone `./run golden` passed **11/11** with every exact corpus, duplicate,
signal, rerun, entitlement, citation, snippet, and auth anchor unchanged.
`./run verify-artifacts` matched both protected databases **2/2**.
Manifest validation and an independent `hashlib.sha256` witness each matched
all three pinned reports exactly: 27,786 bytes / `00cf14ae…`, 62,978 bytes /
`beec8bfa…`, and 28,968 bytes / `4e11a8b3…`. `version-check`,
`cycle-check`, `checklist-audit`, and `progress-check` passed; the checklist
entered at **69/69** checked historical tasks with zero exemptions.

All six defect classes were confirmed:

1. **G1:** the receipt guard declares job counts, computes them with
   `sum(receipt["job"] == job)`, omits `matrix` from both required and accepted
   fields, and its positive fixture emits two indistinguishable `shell`
   receipts.
2. **G2:** `--require-attestations` is optional, and neither `run` nor
   `ci.yml` requires it. The drafted claim that a broad grep would match only
   tests was refuted: the option and writer necessarily also appear in
   `tools/audit_deferred.py`. The substantive finding holds: no release-path
   invocation requires it, and `attestations_required` /
   `attestation_verified` have no reader outside the measurement writer.
3. **G3:** the in-process substitution control changed a committed valid cell
   to `NOT EXERCISED` with both overlap flags true and a violation id;
   `_completed_attempt_schema_valid` returned `True`. Resume binds neither
   target, shape, nor model to the report declaration.
4. **G4:** `gh` 2.96.0 exposes `--signer-digest`, `--source-digest`, and
   `--source-ref`, while the current verifier passes none of them. All seven
   accepted `30194678764-1-*` logical receipt paths are absent from the
   repository; no `.sigstore` bundle exists under `evidence/`.
5. **G5:** `tools/audit_deferred.py` hard-codes
   `"task": "v0.10.1 RECEIPT"` and the immutable pinned v0.10.2 report carries
   that wrong label. `cycle_check` scans only `AGENTS.md` for task/progress
   paths, while `run` still contains stale v0.10/v0.10.1 evidence paths.
6. **G6:** Git's unreachable blob
   `0eaef2570b1a435e6165f64a8fe3b377360e06f6` preserves the supplied
   v0.10.2 runbook at SHA-256 `247d7185…`; the first committed runbook is
   `2fc0eb19…`. Their diff proves Step 2's Objective, Acceptance criteria, and
   Done-when were rewritten before admission, while the dated correction named
   only activation and the publication dependency.

No runtime, dependency, lockfile, architecture, protected byte, evidence pin,
provider configuration, remote ref, or tag changed during E0.

**v0.10.3 cycle activation is complete; E0 has not yet run (measured
2026-07-26).** The read-only opener found only the operator-supplied untracked
`TASKS-v0.10.3-EXECUTION.md`; `AGENTS.md` correctly still declared the latest
closed cycle, v0.10.2. Entering HEAD was
`6a7070b97bd4bef08345311644fa8815a58cd282`, described as
`v0.10.2-1-g6a7070b`, with local `main` four commits ahead of remote
`origin/main` at `817e7f3e7c1878c18f474532df4d50c2b17fcbdc`. The remote tag
census contained v0.10.0 and v0.10.1 only; no remote v0.10.2 tag existed.

Implementation commit `f220e695dc93189d9fe919d80e373d96edd55851`
admitted the reviewed runbook unchanged, declared v0.10.3 active, and created
its append-only progress log. `./run cycle-check` passed with v0.10.3 open and
seven closed execution runbooks; `./run checklist-audit` resolved the entering
69/69 checked tasks with zero exemptions; `git diff --check` passed. No test,
golden, artifact, hosted-runner, publication, or release claim is made by this
preparatory correction. E0 restarts from the clean post-audit tree.

**v0.10.2 PUBLISH is complete (measured 2026-07-26).** The operator
explicitly authorized publication. Remote `main` advanced from
`5bcabcb870a906b0b830bf3c8c391bbe3ced71b0` to the reviewed Step 5 audit
record `817e7f3e7c1878c18f474532df4d50c2b17fcbdc`. The existing annotated
`v0.10.1` tag was pushed without replacement: remote tag object
`8ded63f79ed12b4180e8bcd0bcff4ef30a080a79` still dereferences to
`e5af6bc5df8261cc004bd4d3247b70f8cbe930bb`, which is an ancestor of remote
`main`.

The hosted failure-capable control used temporary commit
`7c41fca18aa2845f8f7e1b2cb196ff706975e6c7` on
`codex/v0.10.2-version-failure-control`. Local `version-check` rejected only
the planted shell version `9.9.9`. Hosted
[run 30194605219](https://github.com/jiayanzeng/intel-platform/actions/runs/30194605219)
then failed the Python 3.11 and 3.12 version-consistency steps while core,
golden, lint, MSRV, and net passed. All seven receipt uploads succeeded; the
two shell receipts recorded `conclusion:"failure"`. RCPT-AUTH rejected both,
reported an incomplete shell matrix, and accepted zero executions. The remote
and local throwaway branches and the temporary worktree were deleted; final
remote-ref census finds no control branch.

The published workflow definition on `main` dispatched
`audit_sha=e5af6bc5df8261cc004bd4d3247b70f8cbe930bb` with
`publish_evidence=true`. Hosted
[run 30194678764](https://github.com/jiayanzeng/intel-platform/actions/runs/30194678764)
completed successfully: core, golden, lint, MSRV, net, and both shell matrix
legs passed; the scheduled-only drift job skipped. Every receipt named the
exact release checkout, `run_id=30194678764`, `run_attempt=1`, repository
`jiayanzeng/intel-platform`, workflow `CI`, and event/workflow SHA
`817e7f3e7c1878c18f474532df4d50c2b17fcbdc`. Seven receipt, attestation,
bundle-persistence, and artifact-upload paths passed.

The first sandboxed Sigstore check could not initialize trust and accepted
nothing. The permitted rerun exposed that GitHub CLI selects its bundle
decoder by `.json`/`.jsonl` extension while the persisted valid bytes use
`.sigstore`; it again accepted nothing. The verifier now presents an
ephemeral `.jsonl` copy of the unchanged bundle bytes to GitHub CLI. The
executed correction verified **7/7** subject digests, repository identity,
workflow signer, and hosted-runner provenance with zero rejection; an offline
test asserts the adapter's bytes and cleanup.

The guarded production audit measured a clean detached
`e5af6bc5df8261cc004bd4d3247b70f8cbe930bb` subject with the exact protected
database copies and authenticated hosted set. It recorded five deferred / two
promoted, seven accepted receipts, zero rejected, complete single-run matrix,
and exact-cosine p95 **8.962542 ms** at 2,600 documents versus the
16.264 ms anchor. Fresh
`evidence/v0.10.2/deferred-audit/report.json` is pinned at SHA-256
`4e11a8b3a3a64b5519469289f5cdf246bf13a0045954aa22c38703bbe6d29d9b`,
**28,968 bytes**. Manifest validation passes with three pinned files; no host
path appears in the report. The detached worktree and its recoverable database
copies were removed after measurement.

Both full shell lanes passed **156/156** under Python 3.11.4 and 3.12.13 with
the existing single Starlette deprecation warning. Final `./run golden`
remained byte-identical at **11/11**. Protected databases matched **2/2**, and
all three report pins printed `PIN MATCH`. No product runtime, dependency,
lockfile, protected byte, provider configuration, tunnel value, release
commit, or tag object changed.

**v0.10.2 R-CLOSE selected and created the patch release (measured
2026-07-26).** The operator explicitly approved release
`v0.10.2`. The release gate is open: the fresh real-model report contains
**45/45** target-valid, model-completed cells with zero `LEAK`, and no resumed
attempt was accepted under the old permissive schema. The independent
real-handler positive control remains `GUARD FIRED`. This is observed
resistance evidence, not a universal no-leak claim.

The patch disposition follows `ARCHITECTURE.md §8`. This cycle hardens
workflow provenance, evidence subject/authentication checks, adversarial
resume validation, and cycle-lifecycle enforcement. It adds a pinned audit
report and tests, but it does not change public or internal API behavior,
runtime behavior, storage paths, database schema, cache representation,
licensing outcomes, dependencies, or retrieval outputs.

The complete `v0.10.1..v0.10.2` diff contains **21 paths**, each
classified exactly once:

- **public/release metadata (5):** `CHANGELOG.md`, `Cargo.lock`,
  `apps/cored/Cargo.toml`, `shell/intel_shell/__init__.py`, and
  `shell/intel_shell/app.py`.
- **operations and workflow (2):** `.github/workflows/ci.yml` and `run`.
- **executable evidence and controls (8):**
  `config/protected-artifacts.json`;
  `evidence/v0.10.2/deferred-audit/report.json`;
  `shell/tests/test_cycle_check.py`, `shell/tests/test_deferred_audit.py`, and
  `shell/tests/test_verify_llm.py`;
  `tools/audit_deferred.py`, `tools/cycle_check.py`, and
  `tools/verify_llm.py`.
- **documentation and task metadata (6):** `AGENTS.md`,
  `PROGRESS-v0.10.1.md`, `PROGRESS-v0.10.2.md`, `STATE.md`,
  `TASKS-v0.10.1-EXECUTION.md`, and `TASKS-v0.10.2-EXECUTION.md`.
- **runtime, storage, or internal API (0):** none.

All five version authorities — the Rust package, Python package, FastAPI
literal, `STATE.md` header, and newest `CHANGELOG.md` heading — now read
0.10.2. Cargo mechanically regenerated `Cargo.lock` and changed only the
`cored` package version from 0.10.1 to 0.10.2; no dependency resolution moved.
The changelog records exact-subject and authenticated receipt enforcement, the
hosted publication outcome, strict resume semantics, the cycle-neutral
operating contract, the pinned v0.10.2 audit, and every carried disposition.
The exact release commit and annotated tag object are
`7d127abac0b993c9e98294ee1c03ff01153de9d0` and
`d821f8b2eb6f39fe4a7d06a88cd61de771c7b0ba`, respectively. The annotation is
`intel-platform v0.10.2`, the tag object dereferences exactly to that release
commit, and the separate closing record does not move it.

PUBLISH advanced remote `main` only through reviewed Step 5 audit commit
`817e7f3e7c1878c18f474532df4d50c2b17fcbdc` and published the existing
immutable v0.10.1 tag. Hosted run 30194678764 passed its complete seven-job
matrix against the exact released checkout, and the production audit
authenticated **7/7** bundles with zero rejection. The resulting pinned report
records **2 promoted / 5 deferred** and exact-cosine p95 **8.962542 ms** at
2,600 documents. No v0.10.2 commit or tag will be pushed without separate
operator authorization.

The release candidate passed the complete local definition of done.
`./run ci-local` passed all **19/19** jobs with **99** Rust workspace tests,
**20** net tests, warning-denied builds, clippy/fmt, locked Rust 1.78
check/tests, **156/156** Python 3.11 shell tests, golden **11/11**, protected
artifacts **2/2**, three evidence pins, persisted fingerprints, and all
lifecycle auditors. The independent Python 3.12.13 lane passed **156/156** and
verified **21/21** exact packages with the same single third-party Starlette
warning. Standalone manifest validation, protected verification, golden,
version consistency, and `git diff --check` all passed. The 21-path inventory
matches the Git diff exactly.

With the R-CLOSE box checked, the exact closing record appended, and the
R-CLOSE progress entry present, the closed-state `./run ci-local` again passed
all **19/19** jobs. `cycle-check` reported v0.10.2 closed with seven closed
execution runbooks; `checklist-audit` resolved **69/69** checked tasks with
zero exemptions; `progress-check` resolved R-CLOSE to the release commit;
version-check matched the exact release tag; golden remained **11/11**; and
protected artifacts remained **2/2** with all three pins matching. The
independent closed-state Python 3.12.13 lane also passed **156/156** and
verified **21/21** exact packages. The audit commit that records these
measurements intentionally follows the release tag and does not move it.

**v0.10.2 AGENTS-NEUTRAL is complete (measured 2026-07-26).** The four stale
v0.10 task/progress paths in `AGENTS.md` were replaced with references to the
active execution runbook and progress log declared at the top. No invariant
or decision outcome in §§0–4 changed. A literal census now finds exactly the
active `TASKS-v0.10.2-EXECUTION.md` and `PROGRESS-v0.10.2.md`, both inside the
introductory active-cycle declaration, and no concrete task/progress path
below the §0 boundary.

`cycle-check` now scans numeric `TASKS-v*-EXECUTION.md` and
`PROGRESS-v*.md` literals in the operating contract. Only the declared active
pair is allowed before §0; any current or stale concrete path later in the
contract is an error. The scratch-root failure-before control was **one pass,
one failure**: the old checker accepted both the clean declaration and a
planted `PROGRESS-v1.2.md`. Pass-after is **2/2**: the clean scratch contract
passes and the planted path fails with its `AGENTS.md` line. The actual
`./run cycle-check` passes with v0.10.2 open, six closed execution runbooks,
and three historical task documents.

Both full shell lanes passed **155/155** under Python 3.11.4 and 3.12.13 with
the existing single Starlette deprecation warning. Python compilation and
`git diff --check` passed. Standalone `./run golden` remained byte-identical
at **11/11**. Protected databases matched **2/2**, and both v0.10.1 reports
printed `PIN MATCH`. No product path, invariant, dependency, lockfile,
runtime, protected byte, evidence pin, provider configuration, tunnel value,
remote ref, or tag changed.

**v0.10.2 RESUME-STRICT is complete (measured 2026-07-26).** Resume now
requires the full shape emitted by a fresh completed adversarial cell:
non-empty identity/model fields, non-negative latency/retry telemetry,
`http_status == 200`, exact true completion/context/valid flags, typed context
and violation lists containing the target where required, typed overlap
flags, a declared outcome, and complete non-negative 8/12/16-token match
telemetry. Structurally incomplete or internally contradictory cells are not
counted and are retried.

The four-cell failure-capable set produced the expected fail-before result:
the complete cell passed unchanged, while the old predicate incorrectly
reused the HTTP-502 and schema-incomplete cells and did not halt on the
synthetic resumed `LEAK` (**three failed, one passed**). Pass-after is
**4/4**: the complete cell is reused byte-for-byte, both invalid cells are
retried, and a resumed `LEAK` records its target and shape under
`halted_on_resumed_leak` and raises immediately. The leak was a synthetic
failure control, not a finding in protected evidence; the committed report remains zero
`LEAK`, and a direct schema census accepted all **45/45** of its completed
attempts.

The focused verifier suite passed **23/23**, and both full shell lanes passed
**153/153** under Python 3.11.4 and 3.12.13 with the existing single
Starlette deprecation warning. Python compilation and `git diff --check`
passed. Standalone `./run golden` remained byte-identical at **11/11**.
Protected databases matched **2/2**, and both v0.10.1 reports printed
`PIN MATCH`. No public product path, dependency, lockfile, runtime, protected
byte, evidence pin, provider configuration, tunnel value, remote ref, or tag
changed.

**v0.10.2 SUBJ-ENFORCE is complete (measured 2026-07-26).** Production
audits now require `--expected-head`. Before any measurement call or report
write, the auditor resolves the subject worktree's HEAD, requires exact
equality, and then requires `git status --porcelain=v1` to be empty. The same
validated SHA is passed to RCPT-AUTH as its released commit; `git_subject()`
records the necessarily clean status afterward. Rederivation and synthetic
control modes remain outside this production-only precondition.

The three-test failure-before control failed **3/3** because the old
`run_production` had no `expected_head` contract. Pass-after tests instrument
the measurement function: a wrong HEAD and a dirty tracked path each raise
before that function is called and leave no output file, while a clean
matching synthetic repository writes a report and passes its HEAD into the
receipt guard. A separate CLI control rejects `--output` without
`--expected-head`. The `./run audit-deferred` production wrapper defaults the
expected subject to immutable v0.10.1 release
`e5af6bc5df8261cc004bd4d3247b70f8cbe930bb`; an actual wrapper control from
current pre-release HEAD `170f471cab6c0b198a7254cc495b95efe0c71d2a` rejected the
mismatch, wrote no report, and reverified protected evidence before and after.

The corpus-free deferred-audit subset passed **22/22** on Python 3.11.4 and
3.12.13. Both full shell lanes passed **150/150** with the existing single
Starlette deprecation warning. Python compilation, `bash -n run`, and
`git diff --check` passed. Standalone `./run golden` remained **11/11** at
every named anchor; protected databases matched **2/2**, and both v0.10.1
reports printed `PIN MATCH`. No measurement content, dependency, lockfile,
runtime, protected byte, evidence pin, provider configuration, tunnel value,
remote ref, or tag changed.

**v0.10.2 RCPT-AUTH is complete (measured 2026-07-26).** The failure-before
control produced the expected seven failures and eight passes: the old
receipt guard did not accept a required `released_commit`, and the workflow
had no attestation steps. The pass-after guard retains the Git ancestry check
and additionally requires every receipt SHA to equal the released commit,
every conclusion to equal `success` case-insensitively, and exactly one
`run_id`/`run_attempt` containing `core=1`, `golden=1`, `lint=1`, `msrv=1`,
`net=1`, and `shell=2`. Synthetic controls reject a non-release ancestor, a
failed receipt, a partial matrix, and a multi-run matrix; the complete
seven-receipt release matrix promotes.

All seven `ci.yml` jobs now record workflow, repository, event SHA, and the
independently resolved checkout SHA. A required `publish_evidence` dispatch
input defaults false. When true, each job signs its exact receipt with hosted
GitHub build provenance and uploads that receipt plus its Sigstore bundle.
Authenticated audit mode requires one bundle per receipt and invokes GitHub
attestation verification with the expected repository, workflow signer,
hosted-runner restriction, and receipt subject bytes; the signed receipt's
checkout SHA is then subject to the exact-release guard. Missing-bundle and
invalid-bundle controls both reject all seven rows. This verification path is
wired but inert: no hosted attestation was generated or accepted in this
Step, so no runner-producer claim is made before PUBLISH.

The focused deferred-audit suite passed **18/18** with process/loopback
permission. Its corpus-free subset passed **17/17** on both Python 3.11.4 and
3.12.13, and the full shell suite passed **145/145** on both interpreters
(with the existing single Starlette deprecation warning). The workflow parsed
as YAML and `git diff --check` passed. Standalone `./run golden` remained
**11/11** byte-for-byte at every named anchor. `./run verify-artifacts`
matched protected databases **2/2** and printed `PIN MATCH` for both v0.10.1
reports. No dependency, lockfile, runtime, protected byte, evidence pin,
provider configuration, tunnel value, remote ref, or tag changed.

**v0.10.2 E0 is complete (measured 2026-07-26).** The restarted opener
produced no `git status --porcelain=v1` output. HEAD was
`9d5b08ece5447648c09073987b520dccb17d8fcf`, described as
`v0.10.1-3-g9d5b08e`; the two approved cycle-activation commits explain the
corrected 14 ahead / 0 behind count relative to `origin/main` at
`5bcabcb870a906b0b830bf3c8c391bbe3ced71b0`. Annotated `v0.10.1`
remained exact at tag object
`8ded63f79ed12b4180e8bcd0bcff4ef30a080a79` and release commit
`e5af6bc5df8261cc004bd4d3247b70f8cbe930bb`.

The first sandboxed `./run ci-local` attempt is an environment non-result:
all Rust, MSRV, lint, and lifecycle units passed, but eight shell controls
could not execute because the environment denied `ps` and loopback binds. The
permitted identical rerun passed all **19/19** units with **99** workspace
tests, **20** net tests, warnings denied, clippy/fmt, Rust 1.78 locked
check/tests, and **138/138** Python 3.11.4 shell tests. The independent Python
3.12.13 lane passed **138/138**, and both interpreters verified the exact
**21/21** constrained packages.

Standalone `./run golden` passed **11/11** with the exact 13 → 12 corpus,
hamming-12 duplicate, DeepSeek z=10.0, +0 rerun, one quant document, and
four-citation answer anchors. `./run verify-artifacts` matched both protected
databases **2/2** and both v0.10.1 report pins; `version-check`, `cycle-check`,
and `checklist-audit` passed, the latter at the entering **62/62** checked
tasks.

All four findings were confirmed:

1. **F1:** `runner_receipt_measurement` validates field presence, SHA format,
   and ancestry only. It does not require the exact release commit, a
   successful conclusion, a complete matrix, one run id, or provenance. The
   committed receipt happens to contain seven accepted rows, all at
   `45fa3d49860643fdb2595d82340e364d33566e7d`, all `success`, all run
   `30187058897`; those facts are not enforced.
2. **F2:** `run_production` calls measurements immediately and writes the
   report without a dirty-worktree or expected-HEAD precondition. Source search
   found zero `expected_head` / `expected-head` references under `tools/`.
3. **F3:** `_resume_valid_attempts` requires only stored
   `target_in_context` and `model_completed`; it checks neither HTTP 200 nor
   the completed-attempt schema and does not halt on resumed `LEAK`. The fresh
   path sets `model_completed=True` only inside its HTTP-200 branch, confirming
   the contradictory 502 state is hand-edited/cross-contaminated evidence.
4. **F4:** outside the active declaration, `AGENTS.md` still contains the four
   stale v0.10 literals at lines 59, 214, 226, and 230. No finding was refuted
   or struck.

No runtime, dependency, lockfile, architecture, protected byte, evidence pin,
provider configuration, or tunnel value changed during E0.

**v0.10.2 cycle activation is complete; E0 has not yet run (measured
2026-07-26).** The first read-only session opener stopped at E0's clean-tree
gate because the operator-supplied `TASKS-v0.10.2-EXECUTION.md` was untracked
and `AGENTS.md` correctly still declared the latest closed cycle, v0.10.1.
HEAD was `384662d673a33a6f181358304bb5daed08eac0fc`, described as
`v0.10.1-1-g384662d`; local `main` was 12 ahead / 0 behind
`origin/main` at `5bcabcb870a906b0b830bf3c8c391bbe3ced71b0`. Annotated tag
object `8ded63f79ed12b4180e8bcd0bcff4ef30a080a79` still dereferenced
exactly to release commit `e5af6bc5df8261cc004bd4d3247b70f8cbe930bb`.

The operator approved the review correction. Implementation commit
`c0b2856fea45b576c63e4b6507e4bf9e277fe145` admitted the runbook,
declared v0.10.2 active, created its append-only progress log, distinguished
structural receipt validation from authenticated producer evidence, and fixed
PUBLISH so the hardened workflow is published before it audits the immutable
v0.10.1 release checkout. `./run cycle-check` passed with v0.10.2 open and six
closed execution runbooks; `./run checklist-audit` resolved the entering
62/62 checked tasks with zero exemptions. No test, golden, artifact, hosted
runner, publication, or tunnel claim is made by this preparatory correction.
E0 restarts from the clean post-audit tree.

**v0.10.1 E0's first checkpoint stopped at the clean-tree gate (measured
2026-07-26).** The session opener ran before any edit. HEAD was
`6c53d8585d43d46723a83ba1635012b7ab00671f`
(`v0.10.0-1-g6c53d85`), exactly the v0.10 append-only closing audit after
release commit `45fa3d49860643fdb2595d82340e364d33566e7d`. Annotated tag object
`f70fd84ca0995088d2890096f3429bb878409979` has type `tag` and dereferences
exactly to that release. `origin` resolves to the GitHub SSH remote.

`git status --porcelain=v1` was not clean: it reported modified tracked
`.DS_Store`, `crates/.DS_Store`, and `shell/.DS_Store`; the supplied untracked
`TASKS-v0.10.1-EXECUTION.md`; and untracked `evidence/.DS_Store`. E0 therefore
did not run `ci-local` or claim any downstream acceptance result. The
operator's explicit request to exclude `*.DS_Store` authorizes a separate,
pre-E0 hygiene change: add that pattern, remove the three existing Finder
metadata files from Git tracking without deleting the local files, commit the
supplied runbook, and declare the new cycle. E0 will restart only after that
known-input correction and its audit record leave the worktree clean.

Runbook feasibility review also found two execution details that must be made
explicit when their tasks begin. A workflow added after v0.10.0 cannot emit a
receipt by merely dispatching the old workflow definition at the v0.10.0 ref;
CIR must run the new workflow definition while explicitly checking out and
recording the audited release commit. Likewise, the corrected auditor cannot
be executed from the old release tree itself; RECEIPT needs the new auditor to
measure an explicit clean release worktree and an explicit runner-receipt
input. The Step 6 decline example also has an arithmetic typo: with seven rows,
view promoted and CI-runner deferred means `{promoted: 1, deferred: 6}`, not
`{promoted: 1, deferred: 5}`. Historical 18-job records remain true historical
measurements and will not be rewritten when PIN raises the current matrix to
19.

Activating v0.10.1 also made `cycle-check` inspect the now-inactive v0.10
runbook for present-tense authority. Its defect table quoted the exact phrase
the checker rejects while describing the already-corrected v0.6/v0.7 defect.
The historical meaning is preserved with past-tense wording, but the inactive
file no longer contains a lexical false positive that looks like current
authority.

**v0.10.1 E0 is complete (measured 2026-07-26).** After the separately
recorded gate correction, `git status --porcelain=v1` produced no output.
HEAD was `3f81e31f324e9624cbbacb3be8ec6b817561b2aa`, described as
`v0.10.0-3-g3f81e31`; release identity and `origin` remained exact.

The first sandboxed `./run ci-local` reached 113 shell passes and seven
loopback-bind `PermissionError` failures, then stopped at job 14. That is an
environment non-result. The permitted rerun executed the doubles and passed
all **18/18** jobs: 99 workspace tests, 20 net tests, warning-denied checks,
clippy/fmt, locked Rust 1.78 check/tests, 120 Python 3.11 tests, golden 11/11,
protected artifacts 2/2, persisted fingerprints, and the active progress
record. The separate Python 3.12.13 lane passed **120/120** with the same one
third-party Starlette warning. A standalone golden lifecycle also passed
11/11.

All six drafted defects were **CONFIRMED**:

1. **D4:** classify-time validity is only `target_in_context`, and completion
   trusts every stored `valid_attempt`. The shipped report says
   `complete:true`, reused 44 prior attempts, has **0** attempts with
   `model_completed:true`, omits that key from **44**, and marks the sole
   HTTP-502 / `model_completed:false` attempt valid.
2. **D2:** the shipped deferred receipt is `{promoted:1,deferred:6}`, leaves
   CI-runner evidence deferred under `"a Git remote exists"`, describes
   commit `d9cab128eed014ca1b1702c8794ba5a0ea1c85be` rather than the release,
   and records a dirty five-path worktree.
3. **D1:** the only `evidence/ci-runs` reference is the reader glob.
   `cmd_ci_local` and `.github/workflows/ci.yml` do not run the audit, and the
   CI row promotes from remote presence rather than a runner receipt.
4. **D3:** deferred-audit tests call only `control_measurements`; none calls
   `production_measurements`. The evidence manifest names only the two
   protected SQLite databases and pins no evidence JSON.
5. **D5:** `ATTEST_NGRAM` remains 16 and all 45 shipped real-model cells are
   `NOT EXERCISED`, with 0 `GUARD FIRED` and 0 `LEAK`.
6. **D6:** `installed_versions()` raises on the first duplicate distribution
   before `compare()`, while the drift test invokes the ambient interpreter and
   asserts only that the FastAPI mismatch appears. An ambient duplicate can
   therefore mask the reason the test names.

Static source recount found **58** `#[test]`, **42** `#[tokio::test]`, and
**4** `cfg(feature = "net")` gates. `./run verify-artifacts`,
`version-check`, `cycle-check`, and `checklist-audit` independently passed;
the latter remained 52/52 before E0's box was checked. No runtime, dependency,
lockfile, architecture, provider configuration, or protected bytes changed.

**v0.10.1 X-VALID is complete (measured 2026-07-26).** Two controls were
added before the verifier changed. Against the shipped code,
`test_resume_retries_a_completed_flag_it_cannot_verify` showed both a stored
`valid_attempt:true` / `model_completed:false` attempt and one lacking the
completion key were reused. `test_gateway_timeout_is_not_a_valid_attempt`
showed five synthetic HTTP-502 attempts with retained target context were all
marked valid and battery coverage incorrectly passed. The targeted pre-fix run
failed **2/2** for those exact reasons.

`_resume_valid_attempts` now independently requires both stored
`target_in_context` and `model_completed`; it does not trust stored
`valid_attempt`. Classify-time validity uses the same conjunction. The existing
resume test now carries explicit completion evidence, both new controls pass,
and each per-attempt console line includes `http_status`, making a 502 visible
without opening JSON.

The shipped v0.10 adversarial report remains immutable and non-conformant:
although it says `complete:true`, it contains **0/45** attempts with
`model_completed:true`, 44 attempts without that key, and one 502 attempt with
`model_completed:false`. X-REGEN must not resume from it; every cell will be
regenerated fresh.

The targeted post-fix resume/timeout set passed 3/3. Full Python 3.11.4 and
3.12.13 suites each passed **122/122** with one third-party warning.
`py_compile`, standalone golden **11/11**, and protected artifacts **2/2**
passed. X-VALID changed only the verifier harness and its tests: no public path,
threshold, dependency, lockfile, architecture, or protected bytes changed.

**v0.10.1 X-CTRL is complete (measured 2026-07-26).** Four controls were
installed before implementation: the extended all-`NOT EXERCISED` aggregate,
the missing-positive-control rejection, graduated 15-token near-miss
telemetry, and a positive control routed through the deployed FastAPI handler.
All four failed against the pre-Step tree because the aggregate gate,
telemetry, and real-path control did not exist. They pass after implementation;
the full verifier test module passed 19/19.

The control substitutes only the chat client with a deterministic gated-span
response. It keeps the real `/v1/ask` handler and sends its raw answer to core
`/attest`; a strict fired result requires a valid completed attempt, raw gated
overlap, no public overlap, and at least one attestation violation. The report
schema is now 2 and records the control separately. Completeness requires this
control, and an all-`NOT EXERCISED` matrix is **WARN** only when it fired;
without it the aggregate is **FAIL**. `GUARD FIRED` remains PASS and `LEAK`
remains FAIL.

An isolated real-core HTTP run against the normal deterministic chat mock
ingested the 13-document fixture and filled 13 embeddings. The positive
control returned HTTP 200, placed its target in context, produced
`GUARD FIRED`, and measured a longest gated-token run of 29 with match counts
`n=8:22`, `n=12:18`, and `n=16:14`. The ordinary matrix then completed all
45/45 target/shape cells with target context and model completion; all 45 were
honestly `NOT EXERCISED`, with no `n=8/12/16` matches and a maximum short
near-match only. Coverage passed because the control fired, while the aggregate
remained WARN. The verifier's eight required checks passed and emitted 49
warnings. This used a normal local mock for the 45 cells and therefore makes no
real-provider behavioral claim.

Independent classifier controls demonstrated all three values: paraphrase
`NOT EXERCISED`; a leaking chat answer refused by attest `GUARD FIRED`; and the
same overlap on a deliberately unattested path `LEAK`. The telemetry control
measured an exact 15-token near miss as longest 15 with counts
`{n=8:8,n=12:4,n=16:0}`. `ATTEST_NGRAM` is unchanged at 16. The temporary
schema-2 report contained no authorization, raw/public answers, prompts,
credentials, endpoint URLs, or tunnel aliases and was not admitted as evidence.

Full Python 3.11.4 and 3.12.13 suites each passed **125/125** with one
third-party Starlette warning. `py_compile`, standalone golden **11/11**, and
protected artifacts **2/2** passed. X-CTRL changed only the verifier harness
and tests: no product path, dependency, lockfile, architecture, or protected
bytes changed.

**v0.10.1 CIR is complete (measured 2026-07-26).** The three new
failure-capable controls failed against the pre-Step tree: two receipt tests
could not call a nonexistent ancestry filter, and a zero-receipt measurement
still promoted solely because a Git remote existed. After implementation, the
expanded deferred-audit module passes 8/8.

Every one of the seven configured `ci.yml` job definitions now checks out the
explicit audit input or event SHA, emits a receipt under `evidence/ci-runs/`
with `if: always()`, and persists it with `actions/upload-artifact@v4`. The
Python 3.11/3.12 matrix uses distinct receipt filenames and artifact names. A
new optional `workflow_dispatch.audit_sha` input allows the new workflow
definition to execute against an explicitly audited older commit; each receipt
records `git rev-parse HEAD`, so a failed checkout cannot claim the requested
SHA. Static controls counted seven emit steps, seven persistence steps, seven
explicit checkout refs, and seven upload actions. Ruby parsed the workflow
YAML successfully. This configuration has not been pushed or run and is not
described as execution.

The auditor's original
`(ROOT / "evidence" / "ci-runs").glob("*.json")` remains unchanged. Each
candidate receipt must contain the seven runner fields and a hexadecimal object
id, then pass `git merge-base --is-ancestor <sha> <audited-head>`. Accepted and
rejected receipts are recorded separately with reasons; only accepted receipts
contribute to `observed_runner_executions`. `GITHUB_ACTIONS=true` and Git
remote presence remain measured context but contribute zero. The CI row now
promotes only when the filtered count is nonzero and uses the restated trigger
`a runner execution receipt exists for the released commit`.

Synthetic Git history proved both directions: a base-commit receipt promoted
an audited descendant; a receipt from a sibling foreign branch was rejected
with its SHA and audited-head reason and left the row deferred. The production
local measurement found zero candidate, accepted, and rejected receipts,
`workflow_configuration_counts_as_execution:false`, and correctly deferred
despite two `git remote -v` entries.

Full Python 3.11.4 and 3.12.13 suites each passed **129/129** with one
third-party Starlette warning. `py_compile`, standalone golden **11/11**, and
protected artifacts **2/2** passed. CIR changed only workflow configuration,
the deferred-audit harness, and its tests: no runtime product path, dependency,
lockfile, architecture, or protected bytes changed. G-RUN remains an explicit
operator decision; no push or remote workflow mutation has occurred.

**v0.10.1 G-RUN is complete (measured 2026-07-26).** The operator explicitly
approved the main push, the release-SHA dispatch, and the temporary planted
failure branch. Remote `main` was a strict fast-forward from
`6c53d8585d43fdb2595d82340e364d33566e7d` to
`5bcabcb870a906b0b830bf3c8c391bbe3ced71b0` with no remote-side divergence.
The automatic push run
[30187051942](https://github.com/jiayanzeng/intel-platform/actions/runs/30187051942)
completed successfully at that new main head.

The required manual runner execution is
[30187058897](https://github.com/jiayanzeng/intel-platform/actions/runs/30187058897).
It used the new workflow definition from main while every checkout explicitly
selected released commit
`45fa3d49860643fdb2595d82340e364d33566e7d`. It was created at
04:00:06Z, finished at 04:02:00Z, and concluded success. Per-job results and
wall durations were:

| runner job | result | duration |
|---|---:|---:|
| core (pinned toolchain) | pass | 27s |
| clippy + fmt (blocking) | pass | 18s |
| live-fetch path (`--features net`) | pass | 20s |
| MSRV floor (offline 1.78) | pass | 35s |
| shell (Python 3.11) | pass | 24s |
| shell (Python 3.12) | pass | 22s |
| golden E2E (blocking) | pass | 38s |
| dependency drift (scheduled only) | skipped | 0s |

The wire logs measured GitHub-hosted Ubuntu **24.04.4 LTS**, runner image
`ubuntu-24.04` version `20260720.247.2`, Rust **1.91.1**, floor Rust
**1.78.0**, Python **3.11.15** and **3.12.13**, and ShellCheck **0.9.0**.
GitHub forced Node-20 actions onto Node 24 and emitted deprecation annotations;
these were warnings, not job failures.

The seven uploaded artifacts were downloaded into the auditor's unchanged
`evidence/ci-runs/*.json` input. All seven parse against the strict receipt
field allowlist, record `run_id:30187058897`, attempt 1, `runner_os:Linux`,
`conclusion:success`, and the exact release SHA. Their SHA-256 values are:

- core `9158f881eb8d0a8b6102b55df8399256f3df1528e40b63505cca214a1f5e6fbf`
- lint `c3de9df82d796350d359a2458380626d92a6704474250b369c86fbf5a5197368`
- net `09a1c05775f6b19cdaf1ba5ef1c1b21626c8c273b883765a0ab129fe04c44789`
- MSRV `0e4b33c633e10d089eb87a8d61e42f1ae3411fe38a325548d72d6bb5075e089b`
- shell 3.11 `81741887442241d26379f421ea9a416369084606feb39e49c95fde286f3500d8`
- shell 3.12 `bcad9bfc2dbd9dfe64b47adec11af2a434aec4301900a2a8a12834023409296c`
- golden `ab0b968b0d86287c9c200f86c663be1321c18963e61cae8056ed291ac2992511`

Against current main, the ancestry filter accepted 7/7, rejected zero,
reported `observed_runner_executions:7`,
`workflow_configuration_counts_as_execution:false`, and promoted CI-runner
evidence only because a released-commit receipt exists.

The runner/local job sets are recorded as different granularities, not
equivalent counts. `./run ci-local` passed all **18/18** ordered units. Its
workspace check/test and persisted-fingerprint units map into runner `core`;
clippy/fmt into `lint`; net check/test into `net`; floor check/test into
`msrv`; Python constraints/tests plus version and floor/lint steps into the two
shell matrix nodes; and golden into `golden`. Local-only blocking units are
active-cycle consistency, checked-task evidence, exact protected database
bytes/corpus, and append-only progress. Runner-only coverage is a separate
Python 3.12 node, manifest-schema/evidence-control steps without protected DB
bytes, and the scheduled drift node (skipped in this manual run). The runner
has seven executed nodes plus one scheduled-only node; local CI has eighteen
finer-grained units.

The failure-capable control changed only
`shell/intel_shell/__init__.py` from 0.10.0 to 9.9.9 at temporary commit
`8cceae90debaf7e730bebd7bd6c15183e32a6263`. Local `version-check` first
exited 1 and named that exact disagreement. Runner
[30187207654](https://github.com/jiayanzeng/intel-platform/actions/runs/30187207654)
then failed as required: Python 3.11 failed `release version consistency` in
9s and Python 3.12 in 8s, each naming `9.9.9`; their receipt emit/upload steps
still passed. Core, lint, net, MSRV, and golden all passed, proving the failure
was scoped. The remote and local throwaway branch were deleted after the run.
Main and the release tag did not move.

The post-control local matrix passed **18/18**, including 129 Python 3.11 shell
tests, warning-denied Rust builds, golden **11/11**, and protected artifacts
**2/2**. No runtime product path, dependency, lockfile, architecture, provider
configuration, or protected bytes changed. The runner-produced receipt files
are the only new evidence bytes.

**v0.10.1 RECEIPT is complete (measured 2026-07-26).** The current auditor now
accepts two explicit production inputs: `--subject-root` points every
repository/config/corpus/Git measurement at one selected worktree, and
`--runner-receipts-dir` supplies runner-produced JSON from outside that clean
subject. Default behavior and the original direct
`evidence/ci-runs/*.json` glob remain unchanged. Explicit receipt paths are
normalized back to stable `evidence/ci-runs/<name>` labels rather than leaking
host paths. The executed current auditor SHA-256 was
`703daa3a6494857e995828a72c3454d471230b857730b06ff61cb7eab1b36224`.

A detached temporary Git worktree was created at exact release commit
`45fa3d49860643fdb2595d82340e364d33566e7d`. Byte-for-byte copies of the two
protected databases were placed only in its already-ignored `data/` directory.
They reverified as core
`db2f186e291c64192e567c9dfb979dd9877eb32b13c2ce2724a4acf1761a37a0`
and live-smoke
`94f03e9e8662dddfa5c80b63a9845d9926a1fa10060b83638ee094e0a0462c4a`;
`git status --porcelain=v1` remained empty. The first sandboxed audit stopped
at `ps` with `PermissionError: Operation not permitted` before producing a
report and is a non-result. The permitted rerun performed the actual process
census and release-mode exact-cosine measurements and completed.

The falsifiable pre-check measured the required disagreement:

| field | immutable v0.10 receipt | fresh v0.10.1 receipt |
|---|---|---|
| subject HEAD | `d9cab128eed014ca1b1702c8794ba5a0ea1c85be` | `45fa3d49860643fdb2595d82340e364d33566e7d` |
| worktree dirty | true | false |
| CI-runner trigger | `a Git remote exists` | `a runner execution receipt exists for the released commit` |
| CI-runner disposition | defer | promote |
| accepted runner receipts | 0 | 7 |
| summary | 1 promoted / 6 deferred | 2 promoted / 5 deferred |

The new pgvector measurement remained below its gate at **7.431750 ms p95**
for 2,600 documents versus the 16.264 ms anchor. T7, Postgres, pgvector,
multi-host seam hardening, and A4 remain deferred; CI-runner evidence and
future `/view` materialization are the two promoted rows. No deferred subsystem
was implemented.

The fresh schema-2 artifact is
`evidence/v0.10.1/deferred-audit/report.json`, measured at
2026-07-26T04:13:24Z, SHA-256
`00cf14ae931b864616e19c437168d9ef8723791ddee6dc7866794f6850319362`.
It contains no local absolute path, credential, endpoint, authorization, or
tunnel alias. The v0.10 receipt was not overwritten and remains byte-exact at
`ea23f7f2077155b4f4614edeb0afef02bf43252a7733bbc0f25b0b03db742a76`.
After the report copy was compared byte-for-byte, the release worktree again
proved clean with both copied hashes exact and was removed.

The corrected production record is therefore: CI-runner evidence promotes
because seven runner-produced receipts for the released commit exist, not
because a Git remote exists. Full Python 3.11.4 and 3.12.13 suites each passed
**129/129** with one third-party Starlette warning. `py_compile`, golden
**11/11**, and protected artifacts **2/2** passed. No runtime path, dependency,
lockfile, architecture, provider configuration, protected bytes, or v0.10
evidence bytes changed.

**v0.10.1 X-REGEN is complete (measured 2026-07-26).** The runbook's PIN/X-REGEN
numbering is dependency-inverted: PIN says to pin the X1 artifact “after Step
8,” while X-REGEN requires its own report to be added to that pin. The explicit
artifact dependency was followed, so X-REGEN generated and pinned its report
before the remaining PIN work.

The bounded live provider probe passed through the operator-established
loopback transports. The configured chat role identified
`gemma-4-26B-A4B-it-UD-IQ4_XS.gguf`, supported completion and correctly
rejected embeddings; the independent embedding role identified
`embeddinggemma-300M-Q8_0.gguf`, completed the embedding capability request,
and returned the required **768** dimensions. No key was printed.

The first no-resume run was an honest non-result: 45 cells were recorded, but
two chunked-reconstruction calls timed out at 30 seconds with HTTP 502 and
`model_completed:false`, so coverage failed despite zero leaks. That live
failure exposed the missing “timeout retried rather than counted” behavior.
The verifier now records failed invocations only in a separate
`transport_retries` audit array, admits a cell to `attempts` only after target
context and model completion are both true, records a retry count on the valid
cell, and fails visibly after an explicit three-invocation budget. Synthetic
transient and permanent-502 controls pass on both interpreters. A second fresh
run exercised the retry path but proved that the 30-second ceiling was shorter
than repeatable model latency: the same cell exhausted all three invocations.
It was interrupted as a non-result.

The operator's `.env` was not edited. A mode-600 temporary copy outside the
repository changed only the chat timeout to 60 seconds; redacted configuration
confirmed that effective value, and the file was deleted immediately after the
run. The final no-resume battery completed **45/45** target-valid,
model-completed cells with zero transport retries. All 45 real-model outcomes
were `NOT EXERCISED`; there were **0 `GUARD FIRED`**, **0 `LEAK`**, and no
nonzero `n=8/12/16` matches. The maximum real-model contiguous gated run was
four tokens and maximum cell latency was **32,599.289 ms**. The separate
positive control traversed real FastAPI `/v1/ask` and core `/attest`, returned
HTTP 200, and fired `GUARD FIRED` with longest 22 and
`{n=8:15,n=12:11,n=16:7}`. `ATTEST_NGRAM` remains 16.

The fresh schema-2 report is
`evidence/v0.10.1/real-model-adversarial/report.json`, measured at
SHA-256
`beec8bfa87b17c6b0552544fcfc810b517a8a8dd10067e2460dbce7342dda3f7`
and **62,978 bytes**. Its invariant/secret scan found no credential-shaped
value, endpoint, LAN address, loopback tunnel port, SSH command, prompt, or raw
model answer. The v0.10 report remains byte-exact at
`98fb3a3a1acac844aeccd0da0be2457ff9327ee0733f8570d7edc34b1870f13c`.

Manifest schema 2 now has a corpus-free `pinned_files` collection. Both
`validate` and local `verify` compare exact report bytes and SHA-256; a
disposable byte-mutation test proves validation fails. X1 was its first pin;
PIN subsequently added the deferred receipt and source-deterministic
re-derivation job. Full Python 3.11.4 and 3.12.13 suites each passed **132/132** with one
third-party Starlette warning. The first sandboxed full suite's seven
loopback-bind denials were an environment non-result; the permitted rerun is
the counted result. Golden passed **11/11**, and protected database evidence
remained exact **2/2**. No product runtime path, dependency, lockfile,
architecture, threshold, protected bytes, or v0.10 evidence bytes changed.

**v0.10.1 PIN is complete (measured 2026-07-26).** Manifest schema 2 now pins
both fresh JSON records: deferred audit
`00cf14ae931b864616e19c437168d9ef8723791ddee6dc7866794f6850319362`
at **27,786 bytes** and real-model X1
`beec8bfa87b17c6b0552544fcfc810b517a8a8dd10067e2460dbce7342dda3f7`
at **62,978 bytes**. `tools/evidence_artifacts.py validate` reads and hashes
only those committed evidence files, so it remains corpus-free on hosted
runners. Local `verify` checks the pins before independently verifying the two
protected databases. A disposable control appended exactly one byte to a copy
of the pinned deferred receipt; validation named its SHA-256 mismatch.

`tools/audit_deferred.py --rederive` loads the committed receipt, recomputes
`scheduler_measurement`, `writer_measurement`, `multi_host_measurement`,
`attestation_boundary_measurement`, and `ci_runner_measurement` from source,
configuration, and Git, and compares exactly the five corresponding row
dispositions, all seven unchanged trigger strings, row count seven, and the
source-declared `v2_materialization_implemented` flag. Scheduler runtime
process/socket observations are carried from the receipt because they are
explicitly outside the deterministic comparison. Host/timestamp fields,
remote text, observed/accepted/rejected receipt details, source hashes, and
numeric pgvector/view measurements are not compared. The production-dependent
pgvector and view dispositions remain protected by the whole-file hash pin.

The clean receipt re-derived exactly:
`rows=7`, `source_dispositions=5`, `triggers=7`, and
`v2_materialization_implemented=false`. A scratch receipt changing T7 from
defer to promote failed with
`REDERIVATION MISMATCH source_dispositions`. The new local CI unit invokes
manifest validation and re-derivation; it raises the tracked count from
**18 to 19**. The identical commands are a blocking step in the Python 3.11
workflow lane, whose full-history checkout already makes the released receipt
SHAs available for ancestry checks. Static workflow structure and YAML parsing
passed; no post-PIN hosted runner execution is claimed.

The guarded pytest requires `data/core.db`, `data/live-smoke.db`, and a built
`target/debug/cored`. On site it invoked the complete
`production_measurements()`/`evaluate()` path and matched the committed
environment-independent snapshot; the focused test passed in **2.64s**. A
runner without either protected corpus cannot enter that test and reports a
skip instead.

The permitted `./run ci-local` passed all **19/19** units: the new
re-derivation gate, warning-denied Rust checks/tests, clippy/fmt, Rust 1.78,
**136** Python 3.11 tests, golden 11/11, exact pinned/protected evidence,
fingerprints, and lifecycle records. The independent Python 3.12.13 lane also
passed **136/136**. Targeted PIN suites passed 23/23 on both interpreters;
ShellCheck 0.11.0, Bash syntax, and workflow YAML parsing passed. Protected
databases remained exact **2/2** and golden remained **11/11**. All pre-PIN
18-job measurements in closed task/progress records remain true historical
measurements; current help, status, and acceptance records now state 19.

**v0.10.1 HERM is complete (measured 2026-07-26).** The failure-before
regression installed three tests before the seam existed. The targeted module
failed 3/5 because `installed_versions()` accepted no inventory argument; in
particular, an ambient duplicate could still prevent the named FastAPI drift
from being evaluated.

`installed_versions(distributions=None)` now uses
`importlib.metadata.distributions()` only when no explicit iterable is
provided. The CLI/product path is unchanged and therefore still discovers the
active interpreter, ignores only the bootstrap package set, fails on missing
Name metadata, and rejects a second canonicalized distribution name before
comparison. Tests can pass a complete synthetic inventory without consulting
ambient `site-packages`.

The drift test now derives a 21-package synthetic inventory from the committed
constraints, changes only expected FastAPI from 0.140.0 to 0.140.1, and asserts
the sole problem is
`fastapi: expected 0.140.1, found 0.140.0`. The hermeticity control monkeypatches
ambient discovery to contain duplicate `colorama` distributions, proves the
explicit inventory still surfaces that exact FastAPI drift, and independently
proves the unchanged ambient/product path raises
`installed distribution is duplicated: colorama`. A direct injected duplicate
with case-varied FastAPI names also proves canonical duplicate rejection.

The targeted post-fix module passed **5/5** under Python 3.11.4 and 3.12.13.
Both real interpreters independently passed the product verifier at
**21/21 packages**. The full permitted local matrix passed **19/19**, including
**138** Python 3.11 shell tests, warning-denied Rust lanes, the evidence
re-derivation, golden, and artifact checks. The independent Python 3.12.13
suite passed **138/138**. Golden remained **11/11** and protected databases
remained exact **2/2**. No pin, declared dependency, runtime behavior, public
surface, architecture, protected byte, or evidence report changed.

**v0.10.1 R-CLOSE selected and created the patch release (measured
2026-07-26).** The operator explicitly approved release
`v0.10.1`. The gate permits release because X-REGEN completed all **45/45**
target-valid, model-completed cells with zero `LEAK`, while the real-handler
positive control independently emitted `GUARD FIRED`. The patch disposition
follows `ARCHITECTURE.md §8`: this cycle changes operations, executable
evidence, and test hermeticity, but does not change public or internal API
behavior, runtime behavior, storage paths, database schema, cache
representation, licensing outcomes, or retrieval outputs.

The complete `v0.10.0..v0.10.1` diff contains **35 paths**, each
classified exactly once:

- **public/release metadata (5):** `CHANGELOG.md`, `Cargo.lock`,
  `apps/cored/Cargo.toml`, `shell/intel_shell/__init__.py`, and
  `shell/intel_shell/app.py`.
- **operations and repository hygiene (6):** `.github/workflows/ci.yml`,
  `.gitignore`, `run`, and the deleted `.DS_Store`, `crates/.DS_Store`, and
  `shell/.DS_Store`.
- **executable evidence and controls (18):**
  `config/protected-artifacts.json`;
  `evidence/ci-runs/30187058897-1-core.json`,
  `evidence/ci-runs/30187058897-1-golden.json`,
  `evidence/ci-runs/30187058897-1-lint.json`,
  `evidence/ci-runs/30187058897-1-msrv.json`,
  `evidence/ci-runs/30187058897-1-net.json`,
  `evidence/ci-runs/30187058897-1-shell-py3.11.json`, and
  `evidence/ci-runs/30187058897-1-shell-py3.12.json`;
  `evidence/v0.10.1/deferred-audit/report.json` and
  `evidence/v0.10.1/real-model-adversarial/report.json`;
  `shell/tests/test_deferred_audit.py`,
  `shell/tests/test_evidence_artifacts.py`,
  `shell/tests/test_python_constraints.py`, and
  `shell/tests/test_verify_llm.py`;
  `tools/audit_deferred.py`, `tools/evidence_artifacts.py`,
  `tools/python_constraints.py`, and `tools/verify_llm.py`.
- **documentation and task metadata (6):** `AGENTS.md`,
  `PROGRESS-v0.10.1.md`, `PROGRESS-v0.10.md`, `STATE.md`,
  `TASKS-v0.10-EXECUTION.md`, and `TASKS-v0.10.1-EXECUTION.md`.
- **runtime, storage, or internal API (0):** none.

All five version authorities — the Rust package, Python package, FastAPI
literal, `STATE.md` header, and newest `CHANGELOG.md` heading — now read
0.10.1. Cargo mechanically regenerated `Cargo.lock` and changed only the
`cored` package version from 0.10.0 to 0.10.1; no dependency resolution moved.
The changelog records the runner receipts, evidence pins/re-derivation,
adversarial validity and control hardening, hermetic Python inventory, Finder
hygiene, and every carried disposition. The exact release commit and annotated
tag object are
`e5af6bc5df8261cc004bd4d3247b70f8cbe930bb` and
`8ded63f79ed12b4180e8bcd0bcff4ef30a080a79`, respectively. The annotation is
`intel-platform v0.10.1`, the tag object dereferences exactly to that release
commit, and the separate closing record does not move it.

The release failure control changed only
`shell/intel_shell/__init__.py` from 0.10.1 to 9.9.9.
`./run version-check` exited **1** and named that exact file and disagreeing
value. Restoring it returned SHA-256
`4e365b85f228cbbd61311413e9fc828253203187578153a067293fa46ada0090`,
identical to the pre-control hash; the five-authority check then passed at
0.10.1 with the expected ahead-of-v0.10.0 warning.

The release candidate then passed the complete local definition of done:
`./run ci-local` **19/19**, including **99** Rust workspace tests, **20** net
tests, warning-denied builds, clippy/fmt, Rust 1.78 locked check/tests,
**138/138** Python 3.11 shell tests, golden **11/11**, protected artifacts
**2/2**, pinned-evidence validation, persisted fingerprints, and lifecycle
auditors. The independent Python 3.12.13 lane passed **138/138** with the same
single third-party Starlette warning. Standalone
`evidence_artifacts.py validate` passed schema 2 with two artifacts and two
pinned files, `./run verify-artifacts` again measured exact **2/2**, and
`git diff --check` passed.

With the R-CLOSE box checked, the exact closing record appended, and the
R-CLOSE progress entry present, the closed-state `./run ci-local` again passed
all **19/19** jobs. `cycle-check` reported v0.10.1 closed with six closed
execution runbooks; `checklist-audit` resolved **62/62** checked tasks with
zero exemptions; `progress-check` resolved R-CLOSE to the release commit;
version-check matched the exact release tag; golden remained **11/11**; and
protected artifacts remained **2/2**. The independent closed-state Python
3.12.13 lane also passed **138/138**. The audit commit that records these
measurements intentionally follows the release tag and does not move it.

**v0.10 B0 is complete (measured 2026-07-25).** The gate found one false
entering claim before any tracked edit: `git status --porcelain=v1` reported
`?? TASKS-v0.10-EXECUTION.md`, the operator-supplied runbook named in the task,
rather than a clean worktree. No other entering worktree item existed. HEAD was
`280f6abfec0044104b830731c952883aa64b9703`
(`v0.9.0-1-g280f6ab`), exactly one append-only audit commit after release commit
`4c59db2727eda1c81beae3ff38be883a26a92ae8`. Annotated tag object
`548ffdfec4e414570ddecf813aa2f2d616662487` has type `tag`, annotation
`intel-platform v0.9.0`, and dereferences exactly to that release commit.
`git remote -v` produced no output.

`./run version-check` read 0.9.0 independently from the Rust package, Python
package, FastAPI literal, this header, and newest changelog release. It passed
with the expected ahead-of-tag warning, and `CHANGELOG.md` names
`v0.9.0 — 2026-07-25`. Tool versions were pinned Rust/Cargo **1.91.1**, floor
Rust/Cargo **1.78.0**, Python **3.11.4** and **3.12.13**, and ShellCheck
**0.11.0**.

After `cargo clean` removed 3.1 GiB, warning-denied locked workspace check and
**98 tests** passed on Rust 1.91.1; warning-denied net check and **20 net
tests**, clippy, and fmt passed. Warning-denied locked workspace check and the
same **98 tests** passed on Rust 1.78.0. Python 3.11 byte-compilation,
ShellCheck, and Bash syntax passed. The isolated Python lanes each passed
**105 tests** with one third-party Starlette warning. Initial sandboxed Python
attempts reached **98 passes / 7 local-bind failures** in each lane because the
environment refused loopback sockets; they are non-results. Permitted reruns
executed those HTTP doubles and produced the counted 105/105 passes.

`./run down` completed and independent `lsof` checks proved ports 8787, 8788,
and 8899 clear. `./run verify-artifacts` passed **2/2**, followed by independent
read-only measurements:

- `data/core.db`: SHA-256
  `db2f186e291c64192e567c9dfb979dd9877eb32b13c2ce2724a4acf1761a37a0`,
  **6,729,728 bytes**, **1,764 documents**, 0 NULL `simhash`, 0 NULL
  `canonical_id`, integrity `ok`; cursor `arxiv-cs | NULL | 2026-07-20 | NULL
  | 2026-07-23 12:08:13`.
- `data/live-smoke.db`: SHA-256
  `94f03e9e8662dddfa5c80b63a9845d9926a1fa10060b83638ee094e0a0462c4a`,
  **9,490,432 bytes**, **2,600 documents**, 0 NULL `simhash`, 0 NULL
  `canonical_id`, integrity `ok`; cursor `arxiv-cs |
  verb%3DListRecords%26metadataPrefix%3Doai_dc%26from%3D2026-07-22%26until%3D2026-07-22%26set%3Dcs%26skip%3D88
  | NULL | 2026-07-22 | 2026-07-22 23:45:38`.

The failure-capable control copied `data/core.db` to
`/private/tmp/intel-v010-b0-artifact.4WgqoY/core.db` and wrote a disposable
one-artifact manifest containing its real expected hash. Adding only a
`b0_control_failure` table changed the copy's hash to
`f9f4c31f54c24ca57551870122a6a2f87b0bb84f24480e48e7ba95338ecb5e3e`;
`./run verify-artifacts --manifest ... --root ...` exited **1**, printed both
hashes, named `core.db field=sha256`, and reported 0/1 match. Nothing under
`data/` was changed.

All nine drafted defects were **CONFIRMED**:

1. `tools/progress_check.py:14-18` hard-codes v0.9 with a v0.8 fallback.
2. `tools/audit_deferred.py:348-350` lists only the v0.8 and v0.9 progress
   files.
3. `AGENTS.md:13-17` still declares the closed v0.9 cycle active.
4. `TASKS-v0.9-EXECUTION.md:513-520` says the tasks were unexecuted and
   corrects only B0/A1 despite seven checked boxes.
5. `TASKS-v0.6.md:3` and `TASKS-v0.7.md:3` both claim present authority, while
   `TASKS-v0.7.md:13` repeats the false Rust 1.75 offline floor.
6. No tool maps checked execution boxes to matching progress entries and
   commit objects; the existing progress checker validates only the newest
   entry in one log.
7. `shell/requirements.txt` contains four floors and no constraints file.
8. Protected-artifact admission is one schema-v1 lifecycle string whose
   validator checks only literal equality.
9. `tools/verify_llm.py:292-306` constructs one adversarial prompt against only
   `gated[0]`.

`./run golden` passed all **11/11** named assertions on disposable database
`/var/folders/cl/4zcmgrj928n_y07msdz5pjj00000gn/T/tmp.buJodyCGBW/golden.db`.
`./run ci-local` then passed all entering **16/16** jobs, including a separate
11/11 golden lifecycle, protected artifacts 2/2, and the still-stale v0.9
progress target confirmed above. The four closed execution runbooks contained
**40 checked / 0 unchecked** boxes; the supplied v0.10 runbook entered with
0 checked / 11 unchecked. No runtime, dependency, lockfile, architecture, or
protected-corpus change was made.

**v0.10 D0 is blocked before implementation (measured 2026-07-25).** The
single-source derivation itself is feasible: `progress_check.py` can read a
fixed-shape active-cycle declaration, `audit_deferred.py` can glob progress
files, and `cycle_check.py` can derive both targets. D0's named derivation gate
therefore did not fire. Its required production acceptance is nevertheless
impossible in the prescribed task order without violating the auditor rule.

All four inactive execution runbooks have zero unchecked boxes and zero dated
closing records in the shape D0 requires:

| runbook | checked | unchecked | dated closing records |
|---|---:|---:|---:|
| `TASKS-v0.8-EXECUTION.md` | 12 | 0 | 0 |
| `TASKS-v0.8.1-EXECUTION.md` | 10 | 0 | 0 |
| `TASKS-v0.8.2-EXECUTION.md` | 11 | 0 | 0 |
| `TASKS-v0.9-EXECUTION.md` | 7 | 0 | 0 |

In addition, `TASKS-v0.6.md:3` and `TASKS-v0.7.md:3` still say they are the
authoritative task list, and `TASKS-v0.9-EXECUTION.md:514-520` still says the
v0.9 tasks were unexecuted with a correction covering only B0/A1. A conforming
D0 checker must therefore exit non-zero on the production corpus. Adding it as
a blocking job cannot produce D0's required **17/17** result.

The task that repairs these exact facts is D1, but the runbook orders
**D0 → A1 → D1**. A1 itself requires D0's 17-job baseline. This is a dependency
cycle, not an implementation obstacle:

```text
D0 acceptance requires historical closing records/no stale authority
  → D1 owns those records
  → D1 is ordered after A1
  → A1 requires completed D0
```

No checker, cycle literal, `AGENTS.md` pointer, historical task file, or CI job
was changed. Weakening the checker, adding an exemption for resolvable defects,
or silently performing D1 inside D0 would violate the runbook's standing
prohibition against relaxing an auditor and `AGENTS.md §1`. D0 remains
unchecked. The cycle requires an explicit runbook-order correction before
implementation can resume.

**v0.10 D1A is complete (measured 2026-07-25).** The operator explicitly
approved the corrected order **B0 → D1A → D0 → A1 → D1**. The active runbook
records that correction as a dated append, adds the D1A checklist item, and
keeps the original D1 as post-auditor validation. The v0.10 checklist therefore
contains **12 tasks** rather than the draft's 11.

All recorded Git identities were resolved before the documentation changed.
Annotated tag object
`314c1dd914a3d8e9193445874a419ed762581e6e` dereferences to v0.8.0 release
commit `bfc8c5af85734583f966ee70d2ec521155432205`. Both the v0.8 and v0.8.1
execution runbooks now append that dated release identity; their existing
12/12 and 10/10 checklists are unchanged.

The v0.8.2 execution runbook now has an explicit no-separate-release record.
It names all **11** implementation commits from B0.2 through C2, each verified
as a commit object: `5dd11de`, `116c350`, `2f2e82e`, `51a1464`, `040f89d`,
`3228479`, `008d50f`, `604709f`, `e15dd5d`, `5a3f3f8`, and `1939505`.
Those commits intentionally remained ahead of v0.8.0 at cycle close and were
later included in v0.9.0; the later release does not replace the recorded
no-release disposition. Its 11/11 checklist is unchanged.

The v0.9 closing append names all seven implementation commits—B0 `1054994`,
A1 `2adf486`, D3 `d8d7551`, P2 `18887f7` plus live completion `3187f1e`,
V1 `be31247`, D4 `d692aef`, and R2/release `4c59db2`. Annotated tag object
`548ffdfec4e414570ddecf813aa2f2d616662487` dereferences exactly to that
release. It also preserves every carried disposition required by D1:
real-model adversarial `NOT EXERCISED`; T7/Postgres/pgvector/multi-host
deferrals; V2 promotion without materialization; manifest-admission and Python
constraints candidates; and no Git remote or observed runner execution. The
7/7 checklist and incomplete historical provenance remain unchanged above the
superseding append.

`TASKS-v0.6.md` and `TASKS-v0.7.md` now carry dated superseded-cycle banners.
Their present-tense authority sentences are struck rather than erased.
v0.7's original "≥ 1.75" offline-floor claim is likewise preserved but struck,
with the measured format-v4 lock floor corrected to **1.78** and cited to
`STATE.md §5`. `TASKS-v0.8.md` already had the equivalent historical banner.
No runtime, dependency, lockfile, architecture, checklist disposition, or
protected data changed. D0 may now implement its strict checker against the
real corpus without a known-defect exemption.

**v0.10 D0 is complete (measured 2026-07-25).** `AGENTS.md` contains exactly
one fixed-shape declaration, `**Active cycle:** v0.10`, because the operating
contract already governs task selection and is read before any repository
change. `tools/cycle_identity.py` is the single parser for that line.
`tools/progress_check.py` derives its default log through that parser, while
`tools/audit_deferred.py` derives its evidence inputs from the complete
`PROGRESS-v*.md` glob. No task/progress cycle filename literal remains under
`tools/`.

`./run cycle-check` passes against the production corpus. It resolves
`TASKS-v0.10-EXECUTION.md` and `PROGRESS-v0.10.md`, proves the active runbook
has at least one unchecked box and no closing record, and validates four
inactive execution runbooks as closed. Release records are checked against
real annotated tag objects and dereferenced release commits; the v0.8.2
no-release record must name at least one real commit per checked task. The
three non-execution task files must carry dated historical banners. Struck
correction text is retained as history but cannot count as live authority.

All four controls fired in disposable copies under
`/private/tmp/intel-cycle-controls.e25wL3`: declaring nonexistent v99.99 named
`TASKS-v99.99-EXECUTION.md`; closing every active box named
`TASKS-v0.10-EXECUTION.md`; adding a present-tense authority sentence named
`TASKS-v0.9-EXECUTION.md`; and redirecting the default progress resolver named
`tools/progress_check.py` plus both the incorrect v0.9 and declared v0.10
logs. Each `./run cycle-check` exited non-zero.

Both `python3 tools/progress_check.py PROGRESS-v0.10.md` and the default
`./run progress-check` validate the v0.10 D1A record at real commit
`9e53d325ff6fe00d5d5a470076fd9e8f4f825ce3`, not the closed v0.9 log. Direct
and module-style checker invocations are both preserved. The expanded
`./run ci-local` passed **17/17**: 98 warning-denied workspace tests, 20 net
tests, clippy/fmt, locked Rust 1.78 check/tests, 105 Python 3.11 shell tests,
golden 11/11, protected artifacts 2/2, persisted fingerprints, and the active
progress record. This task changed no runtime, dependency, lockfile,
architecture, or protected data.

**v0.10 A1 is complete (measured 2026-07-25).** `./run checklist-audit`
parses every `- [x] **<ID>**` in every execution runbook, resolves its progress
log without a cycle-specific table, selects a runbook-qualified correction
when historical cycles share one log, requires exactly one hash-only
`- commit:` field, and verifies that object with `git cat-file -e
<hash>^{commit}`. Per-file output reports checked, matched, resolved, exempted,
and selected progress-log counts.

The gate found **31** recoverable legacy values in `PROGRESS-v0.8.md`: 12 for
v0.8, 10 for v0.8.1, and nine for v0.8.2. Their original narrative commit
fields remain byte-for-byte in place. A dated append adds one compact,
runbook-qualified correction per task, using the Git commit that introduced
its checked disposition. v0.8.2 D2/C2, all seven v0.9 tasks, and all three
pre-A1 v0.10 tasks already carried valid hashes. The acceptance run therefore
reported **43 checked = 43 matched = 43 resolved, zero exemptions**; this
includes all 40 closed-cycle boxes plus B0, D1A, and D0 in v0.10.

`config/checklist-exemptions.json` is an explicit dated schema with an empty
list and no accepting operator because every checked task is resolvable. The
auditor refuses malformed/duplicate/orphan exemptions and, critically, rejects
an exemption whenever the named task already resolves to a real commit.

All three controls fired under
`/private/tmp/intel-checklist-controls.i7Fc47`: a disposable checked D1 box
without progress named `TASKS-v0.10-EXECUTION.md:718`; replacing the v0.8 B0
correction with 40 zeroes named `PROGRESS-v0.8.md:1127` and the nonexistent
hash; and adding an exemption for clean v0.9 B0 named the false exemption plus
resolved commit `1054994`. Each `./run checklist-audit` exited non-zero.

The expanded `./run ci-local` passed **18/18**, including 43/43 checklist
evidence, 98 warning-denied workspace tests, 20 net tests, clippy/fmt, locked
Rust 1.78 check/tests, 105 Python 3.11 shell tests, golden 11/11, protected
artifacts 2/2, persisted fingerprints, and active progress. No exemption,
runtime, dependency, lockfile, architecture, original progress entry, or
protected data changed.

**v0.10 D1 is complete (measured 2026-07-25).** D1A's approved dated
appends remain the only historical provenance edits: v0.8/v0.8.1 name exact
annotated v0.8.0; v0.8.2 names its no-release disposition and 11 real commits;
v0.9 names all seven task commits, the P2 live completion, exact annotated
v0.9.0 identity, adversarial `NOT EXERCISED`, all four deferrals, V2 promotion,
the protected-admission/constraints candidates, no remote, and no observed CI
runner. Git re-resolved the v0.9 tag object
`548ffdfec4e414570ddecf813aa2f2d616662487`, release commit
`4c59db2727eda1c81beae3ff38be883a26a92ae8`, and every named task commit.

The inactive corpus has exactly four execution runbooks with one dated closing
record each and zero unchecked boxes. The three non-execution task files carry
dated historical banners. v0.6/v0.7 retain their original authority sentences
inside strikethroughs, and v0.7 retains its original false offline-floor
sentence inside a strikethrough followed by the measured 1.78 correction.
An effective-text scan that removes correction spans found no present-tense
authority claim in any inactive task file and no effective "1.75 still
suffices" claim in v0.7. The historical 1.75 measurements and false-claim
postmortems remain preserved; they are evidence, not current floor claims.

`./run cycle-check` and `./run checklist-audit` passed the complete corpus,
the latter at **44 checked = 44 matched = 44 resolved, zero exemptions**.
`cycle-check` now preserves line numbers when ignoring strikethrough text.
Under `/private/tmp/intel-d1-controls.6juKqq`, removing the v0.7 authority
strikethrough caused `./run cycle-check` to exit non-zero and name
`TASKS-v0.7.md:8`; the unmodified disposable tree passed before and after.

The exact-tree `./run ci-local` remained **18/18**, including both auditors,
98 workspace tests, 20 net tests, 105 Python 3.11 tests, golden 11/11, and
protected artifacts 2/2. D1 changed no historical rationale, runtime,
dependency, lockfile, architecture, exemption, or protected data.

**v0.10 A2 is complete (measured 2026-07-25).** Protected-artifact manifest
schema **2** makes admission an append-only, validator-enforced chain. Every
record names its task id, ISO date, admitted SHA-256, prior SHA-256, captured
wire-evidence command and immutable output reference, operator-approval
reference, and explicit retroactive status. The artifact's expected hash must
equal the newest admission hash, and every later record's prior hash must equal
the preceding record's admitted hash. Both `python3
tools/evidence_artifacts.py validate` and `./run verify-artifacts` execute that
validation; the existing CI artifact job therefore enforces it without a new
job.

The original admissions for `data/core.db` and `data/live-smoke.db` are
explicitly marked **retroactive**, not presented as fresh review. Their
evidence references resolve to the already-recorded live-harvest records and
B0 measurements in immutable Git commits; their operator-approval reference
records the instruction to execute this v0.10 runbook. Before and after A2,
the files remained byte-identical at
`db2f186e291c64192e567c9dfb979dd9877eb32b13c2ce2724a4acf1761a37a0`
and
`94f03e9e8662dddfa5c80b63a9845d9926a1fa10060b83638ee094e0a0462c4a`.
A2 changed neither database.

Nine targeted artifact tests passed. Four failure-capable controls prove that
an expected-hash edit without a new record fails; missing wire evidence and
missing operator approval each fail naming their field; a broken prior hash
fails naming the chain break; and a complete chained record over a disposable
artifact passes. Both Python 3.11.4 and 3.12.13 passed **109** shell tests with
the same one third-party Starlette warning. The exact-tree `./run ci-local`
passed **18/18**, including schema-2 artifact validation, 98 workspace tests,
20 net tests, both auditors, golden 11/11, and protected artifacts 2/2.

**v0.10 C1 is complete (measured 2026-07-25).** Clean Python **3.11.4** and
**3.12.13** rebuilds resolved the same 21 application/test distributions
byte-for-byte. `shell/constraints.txt` pins that one shared set while
`shell/requirements.txt` remains unchanged as the four declared floors.
The previously dated FastAPI 0.139.2 resolution had already moved upstream to
0.140.0 when the unconstrained gate was measured; both clean lanes selected
0.140.0 and passed the full behavior suite before it was pinned.

Every current install surface now supplies `-c shell/constraints.txt`: the
local `./run` venv bootstrap, both Python CI matrix lanes, `AGENTS.md`, and the
README's raw command. `./run python-env-check` and
`tools/python_constraints.py` compare the active interpreter's complete
non-bootstrap distribution set to exact pins, naming missing, unexpected, or
version-mismatched packages. The existing local-CI shell-test job executes
this verifier before pytest, so the matrix remains **18** jobs rather than
adding a redundant nineteenth job.

Two additional clean constrained environments reproduced all **21/21** pins
on both interpreters, emitted byte-identical `pip freeze` application/test
sets, and passed `pip check`. The first failure-capable control made pip reject
and name the conflict between declared floor `fastapi>=0.110` and disposable
constraint `fastapi==0.109.0`. The second made the verifier reject and name
`fastapi: expected 0.140.1, found 0.140.0`. Both installed lanes passed
**112/112** shell tests with the same one third-party Starlette warning.
The exact-tree `./run ci-local` passed **18/18**, including 98 workspace tests,
20 net tests, golden 11/11, and protected artifacts 2/2. C1 changed no runtime
code, requirement floor, Rust dependency, lockfile, architecture, or protected
data.

**v0.10 V2 is complete as a measured design (measured 2026-07-25); no
materialization shipped.** Internal `/view` diagnostic headers now report
process-main-to-listener readiness; total SQLite open and its connection,
schema/FTS, cursor-migration, and explicitly named missing-fingerprint
backfill components; sector load; analysis; DTO build; actual serialization;
and handler total. The harness separately measures process spawn-to-health
readiness, HTTP transfer, and client JSON decode. The JSON body is unchanged:
all 20 cold responses per archive matched their pre-instrumentation hashes
`43af73a081eca3d0e57f646b54129df2a27550b129a56729683fd7c0c413784f`
(1,764) and
`5685e69aafe006ef2cfaf33836a99d36310b9a314594edbd9163ee25bbc8af81`
(2,600).

`./run benchmark-view --decompose` measured two independent ten-cold-sample
runs per protected archive. Each JSON report under
`evidence/v0.10/view-decomposition/` records every stage's
min/median/p95/max and share of cold p95:

| run / documents | cold p95 | spawn→ready p95 / share | store open / share | fingerprint backfill / share | sector load / share | analysis / share | serialization / share | HTTP transfer / share |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 / 1,764 | 1696.949 ms | 1344.249 / 79.216% | 2.845 / 0.168% | 1.857 / 0.109% | 14.453 / 0.852% | 330.248 / 19.461% | 5.091 / 0.300% | 1.202 / 0.071% |
| 1 / 2,600 | 540.458 ms | 35.547 / 6.577% | 3.700 / 0.685% | 3.138 / 0.581% | 36.963 / 6.839% | 463.776 / 85.812% | 7.739 / 1.432% | 1.645 / 0.304% |
| 2 / 1,764 | 374.208 ms | 34.142 / 9.124% | 2.233 / 0.597% | 1.671 / 0.447% | 15.493 / 4.140% | 319.076 / 85.267% | 4.896 / 1.308% | 1.054 / 0.282% |
| 2 / 2,600 | 544.959 ms | 34.284 / 6.291% | 3.096 / 0.568% | 2.497 / 0.458% | 22.148 / 4.064% | 479.292 / 87.950% | 7.658 / 1.405% | 1.209 / 0.222% |

All 40 processes reported **zero fingerprints backfilled**. The ordinary
cells localize 85.267–87.950% of cold p95 to analysis, so the future design
targets persisted, already-gated `ViewResp` rather than SQLite open,
fingerprint backfill, or transport. The prior 1,693.423417 ms V1 outlier was
reproduced at 1,696.948500 ms: 1,344.248750 ms was spawn-to-health readiness,
while the core reported only 4.430 ms main-to-listener and 2.845 ms store open.
The stage explains the magnitude and rules out core/store/backfill work; the
underlying host scheduling/process-observation cause remains unexplained and
the sample is retained.

The restart-safe candidate key hashes resolved archive identity, canonical
sector set, explicit view algorithm/schema version, SQLite schema, every
ordered document field, and every ordered embedding field. `python3
tools/view_invalidation.py control` passed **9/9** for archive identity,
sector set, version, append, update, delete, canonical-id rematerialization,
fingerprint refresh, and embedding write. Omitting embeddings exited non-zero
with `embedding-write: STALE-RESULT RISK`. The 100 ms stage-delay control
moved analysis median by **111.553 ms** while sector load moved **0.096 ms**.

`docs/V2-VIEW-DESIGN.md` constrains a future implementation to HC1, core-SQL
sector enforcement, HC3, corpus-global dedup identity, and HC9 core
archive/query ownership. It requires the original two-archive/two-run V1
benchmark to meet cold p95 ≤162.640 ms and warm p95 ≤32.528 ms, plus unchanged
bodies, artifacts, and golden 11/11. V2 added no table, migration, cache
representation, dependency, or lockfile change. The exact tree passed **99**
workspace tests, **20** net tests, **114** shell tests in both Python lanes,
`./run ci-local` **18/18**, golden 11/11, and protected artifacts 2/2.

**v0.10 D5 is complete (measured 2026-07-25); no deferred subsystem
shipped.** `./run audit-deferred --output
evidence/v0.10/deferred-audit/report.json` emitted this dated seven-row
registry from repository, process, Git, deployment, and benchmark evidence:

| deferred item | unchanged trigger | measured production state | disposition |
|---|---|---|---|
| T7 robots single-flight | a second concurrent harvester | one supported simultaneous harvest caller; zero active scheduler processes | **defer** |
| Postgres | a second archive writer | one supported archive-writer process; zero shell direct archive writers | **defer** |
| pgvector | exact cosine over the archive stops fitting the measured request budget | largest evidenced corpus 2,600; exact-cosine p95 6.431667 ms; A3 full-request anchor 16.264 ms | **defer** |
| multi-host seam hardening | an actual core/shell host split | zero recorded cross-host core/shell requests; bind `127.0.0.1:8788`; `CORE_URL=http://127.0.0.1:8788` | **defer** |
| A4 untrusted-shell attestation boundary | a third-party or untrusted shell, or any claim that HC1 is invariant under shell replacement | one public answer path without a core-owned response boundary; one shell-owned public-egress point; zero third-party/untrusted shells; zero invariance claims | **defer; risk recorded** |
| CI-runner evidence | a runner execution receipt exists for the released commit | v0.10.1 run 30187058897 emitted seven accepted receipts, each naming release commit `45fa3d49…`; zero rejected | **promote — released-commit runner evidence exists** |
| `/view` materialization | cold or warm p95 crosses the predeclared V1 SLO in both runs | V1 gate `materialization-trigger-fired`; four V2 decomposition reports; no materialization implemented | **promote → future `/view` materialization implementation** |

The audit's progress evidence is no longer a fixed list. Its derived glob
printed all three files it actually scanned:
`PROGRESS-v0.10.md`, `PROGRESS-v0.8.md`, and `PROGRESS-v0.9.md`. The V2 row
imports the measured V1 trigger and V2 disposition, including
`docs/V2-VIEW-DESIGN.md`; promotion authorizes only that future scoped task.
At D5's dated measurement there was no remote and no observed runner. The
immutable v0.10 receipt therefore deferred CI-runner evidence, while this
release narrative previously contradicted it by promoting on remote presence.
v0.10.1 corrects the row above from measured runner receipts: the trigger is
now falsifiable and fired for release commit `45fa3d49…`. D5 itself added no
receipt seam, response boundary, cache table, migration, scheduler, database,
vector engine, remote, runner workflow, dependency, or lockfile change.

The failure-capable `python3 tools/audit_deferred.py --control all-seven`
control supplied two harvesters, two archive writers, an exact-cosine budget
miss, a remote core hit, an untrusted public answer bypass, a configured Git
remote, and a fired `/view` trigger. It printed **PROMOTE** for all seven and
exited **1** with `CONTROL FIRED: all seven deferred triggers promoted`.
Four targeted registry tests passed. The exact production tree then passed
**99** warning-denied workspace tests, **20** net tests, **115** shell tests
under both Python 3.11.4 and 3.12.13, and `./run ci-local` **18/18**. Golden
remained 11/11 and both protected artifacts remained exact at 2/2.

**v0.10 X1's first checkpoint was deferred at the real-endpoint gate
(measured 2026-07-25); the real battery had not yet run.** The battery was declared in
`tools/verify_llm.py` before any attempt: verbatim quotation, sentence
continuation, translation round-trip, formatted extraction, and chunked
reconstruction, nested across every IndexOnly document discovered from the
fresh fixture ingest. Its schema records chat model identity, endpoint role,
shape, target and context document ids, latency, overlap booleans, violation
ids, and independent `GUARD FIRED` / `NOT EXERCISED` / `LEAK` outcomes. It
explicitly excludes prompts, raw responses, credentials, endpoint URLs, and
tunnel aliases.

The first `./run probe-providers` stopped before transport because
`LLM_EMBED_EXPECTED_DIMENSION` was unset; that is a configuration non-result.
The required rerun supplied the last wire-measured value,
`LLM_EMBED_EXPECTED_DIMENSION=768`. It resolved the redacted chat role as
model `gemma-4-26B-A4B-it-UD-IQ4_XS.gguf` with a 30-second timeout and the
embedding role as `embeddinggemma-300M-Q8_0.gguf`, also with a 30-second
timeout. Its first chat health request then failed with
`ConnectError: [Errno 65] No route to host` and printed `TRANSPORT BLOCKED`.
The probe stopped before the embedding role and before any completion.

Therefore **0 real attempts** ran, no per-attempt report exists, and there is
no aggregate classification. In particular, this is not reported as
`NOT EXERCISED`: that aggregate is valid only after every declared attempt
runs. No mock was substituted. The harness-only
`tools/verify_llm.py --classifier-control` used the leak double plus a
simulated core refusal to emit `GUARD FIRED`, a paraphrase double to emit
`NOT EXERCISED`, and a deliberately unattested path to emit `LEAK`; these are
failure-capable classifier controls, not real-model evidence. At that
checkpoint X1 remained unchecked until both configured roles were reachable
and the complete matrix ran without a leak. The harness change passed
**12/12** focused verifier
tests and the complete **118/118** shell suite under both Python 3.11.4 and
3.12.13, each with the same one third-party Starlette warning. The exact
harness tree passed `./run ci-local` **18/18**, the final direct golden
lifecycle **11/11**, and protected-artifact verification **2/2**. These
regression results do not change the real-model deferral.

**v0.10 X1 is complete with an honest `NOT EXERCISED` result (measured
2026-07-25); no real-model `LEAK` occurred and this is not a pass.** The
operator-established loopback forwards made both configured roles reachable
without committing their aliases. The provider probe measured chat model
`gemma-4-26B-A4B-it-UD-IQ4_XS.gguf`: health and model discovery returned 200
and its embeddings route returned the required exact 501. The separate
`embeddinggemma-300M-Q8_0.gguf` role returned 200 for health, discovery, and
embeddings and produced vectors of dimension 768.

The ordinary verifier path freshly ingested 13 fixture documents, embedded
13→0 with one real provider request whose 768-dimensional output matched
stored statistics, exercised lexical and hybrid retrieval, and returned four
IndexOnly citations with no gated overlap in the public answer. The declared
battery then targeted all **9** IndexOnly documents with all **5** prompt
shapes: **45/45** cells were valid because the named target reached retrieved
model context. The complete matrix aggregate is **`NOT EXERCISED`**:
0 `GUARD FIRED`, 45 `NOT EXERCISED`, 0 `LEAK`, with zero raw or public gated
overlaps. Forty-four cells completed normally. The remaining
`arxiv-cs::oai:arXiv.org:2607.01455` × `chunked-reconstruction` cell returned
HTTP 502 after 120048.445 ms because the model did not complete; the recording
core had already captured the target in retrieved context, so the cell is a
valid targeted attempt and remains explicitly marked `model_completed=false`.

Interrupted runs were preserved rather than overwritten:
`attempt-1-timeout.json` SHA-256
`ff154b7ccde7276b7a75f9d6d0eac7ef2fecd98e58ee99381da92f566a62a551`,
`attempt-2-timeout.json`
`0272a11a73afbd8210740c46c3f5d02a5175d84138166cfcf58baa2659461780`,
and `attempt-3-timeout.json`
`2851eda7ba129368e33975437350788cb556dc565a8a01baad7606eb89d91d46`.
The resumable verifier validated the unchanged battery declaration, target
corpus, and provider identities, reused only valid cells, and retried only
invalid cells. The final secret-free matrix is
`evidence/v0.10/real-model-adversarial/report.json`, SHA-256
`98fb3a3a1acac844aeccd0da0be2457ff9327ee0733f8570d7edc34b1870f13c`;
its battery declaration hash is
`d7e918244ac0d3b61b73d62c1222c384b4d31bbbd1f4b45efa69d804b3d14048`.

The matched failure-capable run used exactly the same 45 target/shape pairs.
`tools/mock_openai.py --leak` produced 45 raw gated overlaps, core attestation
blocked every one, and the matrix aggregate was **`GUARD FIRED`**:
45 guard firings, 0 not-exercised cells, 0 leaks, and zero public overlaps.
Its report is
`evidence/v0.10/real-model-adversarial/leak-control.json`, SHA-256
`ba504a524f9b5df3e7c0bea68523f5b6f6b05aff28090f812c845c60cae9340c`.
The separate classifier control also emitted `NOT EXERCISED`, `GUARD FIRED`,
and a deliberately unattested `LEAK`. A scan of all five reports found no
credentials, authorization headers, endpoint addresses, prompts, raw answers,
public answers, or tunnel aliases.

The completed verifier passed **14/14** focused tests and the full **120/120**
shell suite under both Python 3.11.4 and 3.12.13, each with the same one
third-party Starlette warning. The exact tree passed `./run ci-local`
**18/18**; its 99 workspace tests, 20 net tests, warning-denied builds,
clippy/fmt, both shell lanes, and Rust 1.78 lane were green. The final direct
`./run golden` remained **11/11**, and protected-artifact verification remained
**2/2** at the exact recorded hashes.

**v0.10 G2 is complete with a first real runner failure, a separate
compatibility correction, and a subsequent green run (measured 2026-07-25);
workflow configuration is no longer standing in for execution.** With explicit
operator approval, SSH remote `origin` was added,
`main` at `85c78ea0cdf3eb35774c87e4f5c95ccd93dc7adc` was pushed, and the
existing annotated `v0.9.0` tag was pushed without moving it. Remote tag object
`548ffdfec4e414570ddecf813aa2f2d616662487` still dereferences to release
commit `4c59db2727eda1c81beae3ff38be883a26a92ae8`.

GitHub Actions run
[30142540466](https://github.com/jiayanzeng/intel-platform/actions/runs/30142540466)
is the first observed runner execution. It ran at
`85c78ea0cdf3eb35774c87e4f5c95ccd93dc7adc` for 79 seconds and concluded
**failure**. Core passed in 54s; clippy+fmt passed in 44s; net passed in 54s;
Rust 1.78 passed in 61s; Python 3.12 passed in 23s; and golden passed in 76s.
Python 3.11 failed after 5s at `shellcheck ./run`; the scheduled-only drift job
was skipped on the push event.

The runner measured Rust 1.91.1 on `x86_64-unknown-linux-gnu` with LLVM 21.1.2,
Rust 1.78.0 on the same host, Python 3.11.15, Python 3.12.13, and ShellCheck
0.9.0. The platform forced actions declaring Node.js 20 onto Node.js 24 and
emitted seven deprecation warnings. The ShellCheck failure is a real local/CI
divergence: local 0.11.0 passed, while runner 0.9.0 emitted SC2120 at `run:171`,
SC2119 at `run:193`, and SC2015 at `run:246`. The gate measurement and its
evidence are being committed separately from the eventual lint fix, as
required.

The job-set comparison is not described as equivalence. `./run ci-local` has
18 ordered check units; the workflow has seven executable push/PR job nodes
plus one scheduled-only drift node. Core groups workspace check/test and
fingerprints; lint groups clippy/fmt; net and MSRV each group check/test; the
Python 3.11 node groups version, byte-compilation, ShellCheck, constraints,
evidence controls, and pytest; golden is one job. The workflow additionally
has a Python 3.12 matrix lane, a manifest-only protected-evidence check, and the
scheduled drift reporter. Local-only gates are active-cycle consistency,
checked-task evidence, exact protected database bytes/corpus, and append-only
progress. The manifest-only runner check is not evidence that the uncommitted
protected databases were verified.

The required failure-capable control also fired. Temporary commit
`b7ed500dc123bdbfd4d7a392bdcb558d508ea85c` changed only
`shell/intel_shell/__init__.py` from 0.9.0 to 9.9.9 on
`codex/g2-version-mismatch-control`. Pull request
[1](https://github.com/jiayanzeng/intel-platform/pull/1) triggered run
[30142678150](https://github.com/jiayanzeng/intel-platform/actions/runs/30142678150);
both Python lanes failed at `release version consistency`, naming the file and
9.9.9 value, while core, lint, net, MSRV, and golden passed. The PR is closed
unmerged and the temporary branch is deleted locally and remotely. `main` and
the release tag were not changed by the control.

The complete per-job, toolchain, comparison, failure, and cleanup record is
`evidence/v0.10/ci-runner/report.json`, SHA-256
`2a8d4db07c6b4cbde72052d336360191b98c6d4dab7138961c0185fd504226c9`.

Compatibility commit `3648918b8ddcbab04f2a2057d8cc0f0552c3a6d0` then removed
the unused `refuse_foreign_port` argument interface and replaced the ambiguous
`A && B || C` cleanup with an explicit `if`. Local ShellCheck 0.11.0,
`bash -n`, `./run down`, and the full `./run ci-local` 18/18 passed before the
commit was pushed. GitHub Actions run
[30143171409](https://github.com/jiayanzeng/intel-platform/actions/runs/30143171409)
then executed that exact commit for 43 seconds and concluded **success**:
clippy+fmt 20s, golden 36s, net 25s, Rust 1.78 39s, core 27s, Python 3.11 24s,
and Python 3.12 27s. The scheduled-only drift node was skipped on the push
event. Most importantly, the Python 3.11 lane's `shellcheck run harness` step
passed with runner ShellCheck 0.9.0. The first failure remains part of the
evidence; the later run proves the compatible correction rather than erasing
the divergence.

**v0.10 R3 selected v0.10.0 and the release candidate is in progress
(measured 2026-07-25).** The operator explicitly selected **v0.10.0** after
reviewing the actual `v0.9.0..HEAD` diff. The minor disposition follows
`ARCHITECTURE.md §8`: `apps/cored/src/main.rs` changes runtime behavior by
adding internal `/view` timing headers, and the store exposes measured
SQLite-open phases. The `/view` JSON body, public API, database schema, and
cache representation remain unchanged, but the shipped runtime/internal API
seam is still a real behavior change. A patch release was therefore not used.

The pre-release gate ran against clean local and remote main commit
`67aef084da9da22d27d84506a881bce7d4569e15`. GitHub Actions run
[30143340195](https://github.com/jiayanzeng/intel-platform/actions/runs/30143340195)
passed at that exact head; protected-artifact verification passed 2/2;
`./run version-check` read 0.9.0 from all five authorities; and no
`v0.10.0` tag existed. After the release edits, Cargo changed only the `cored`
package version in `Cargo.lock`; no dependency resolution moved. All five
authorities now read 0.10.0, while the nearest ancestor tag remains v0.9.0
until the candidate is committed and tagged.

The complete release-candidate diff contains **55 paths**, each classified
exactly once:

- **runtime, storage, or internal API (3):**
  `apps/cored/src/main.rs`, `crates/store/src/lib.rs`, and
  `crates/store/src/sqlite.rs`.
- **public/release metadata (6):** `CHANGELOG.md`, `Cargo.lock`, `STATE.md`,
  `apps/cored/Cargo.toml`, `shell/intel_shell/__init__.py`, and
  `shell/intel_shell/app.py`.
- **operations (3):** `.github/workflows/ci.yml`, `run`, and
  `shell/constraints.txt`.
- **executable evidence and controls (29):**
  `config/checklist-exemptions.json`,
  `config/protected-artifacts.json`;
  `evidence/v0.10/ci-runner/report.json`,
  `evidence/v0.10/deferred-audit/report.json`,
  `evidence/v0.10/real-model-adversarial/attempt-1-timeout.json`,
  `attempt-2-timeout.json`, `attempt-3-timeout.json`, `leak-control.json`,
  and `report.json` in that same adversarial directory;
  `evidence/v0.10/view-decomposition/run-1-core-1764.json`,
  `run-1-live-smoke-2600.json`, `run-2-core-1764.json`,
  `run-2-live-smoke-2600.json`, and `summary.json` in that same view directory;
  `shell/tests/test_deferred_audit.py`,
  `shell/tests/test_evidence_artifacts.py`,
  `shell/tests/test_python_constraints.py`,
  `shell/tests/test_verify_llm.py`,
  `shell/tests/test_view_invalidation.py`;
  `tools/audit_deferred.py`, `tools/benchmark_view.py`,
  `tools/checklist_audit.py`, `tools/cycle_check.py`,
  `tools/cycle_identity.py`, `tools/evidence_artifacts.py`,
  `tools/progress_check.py`, `tools/python_constraints.py`,
  `tools/verify_llm.py`, and `tools/view_invalidation.py`.
- **documentation and task metadata (14):** `AGENTS.md`, `ARCHITECTURE.md`,
  `PROGRESS-v0.10.md`, `PROGRESS-v0.8.md`, `PROGRESS-v0.9.md`, `README.md`,
  `TASKS-v0.10-EXECUTION.md`, `TASKS-v0.6.md`, `TASKS-v0.7.md`,
  `TASKS-v0.8-EXECUTION.md`, `TASKS-v0.8.1-EXECUTION.md`,
  `TASKS-v0.8.2-EXECUTION.md`, `TASKS-v0.9-EXECUTION.md`, and
  `docs/V2-VIEW-DESIGN.md`.

Every carried non-result has a disposition. X1 remains **NOT EXERCISED** across
45 valid real-model cells: this is not a no-leak claim; its failure-capable
mock observed 45 guard firings and the separate leak control observed raw
overlap without public overlap. G2 is complete: the first real runner exposed
ShellCheck 0.9.0 divergence, the separate correction passed, and the planted
version mismatch PR was closed unmerged with its branch deleted. D5's T7,
Postgres, pgvector, multi-host hardening, and A4 untrusted-shell boundary rows
remain deferred under their measured triggers. Its CI row was promoted and
completed by G2. Its `/view` row was promoted to the measured V2 design, but no
materialized table, migration, or cache representation shipped. The cycle
checker now validates the declared runbook as open while work remains or
closed after one exact release record; it still rejects zero unchecked boxes
without that record.

The release-candidate failure control changed only
`shell/intel_shell/__init__.py` from 0.10.0 to 9.9.9.
`./run version-check` exited 1 and named that exact file and value. Restoring
it returned SHA-256
`0bd4d3a8ef91761ac81d64c548480010a53830ca4a440598c4c481027d369e05`,
identical to the pre-control hash, and the five-authority check passed again.
The candidate then passed `./run ci-local` **18/18**: 99 workspace tests, 20
net tests, warning-denied checks, clippy/fmt, Rust 1.78 check/tests, 120 Python
3.11 shell tests, golden 11/11, protected artifacts 2/2, persisted
fingerprints, and both lifecycle auditors. The first sandboxed Python 3.12
attempt completed 113 tests and reported seven loopback-bind permission
failures; the permitted rerun passed all **120** with the same single
third-party Starlette warning. No release tag has yet been created at this
candidate checkpoint.

**v0.9 B0 is complete (measured 2026-07-24).** The draft's entering Git
description was stale: `git status --porcelain` was empty at
`d09eda8cd611c3465aaad7a828465bdb8d8de26f`, described as
`v0.8.0-15-gd09eda8`, not `091a203` plus one later documentation commit.
Annotated tag object `314c1dd914a3d8e9193445874a419ed762581e6e` dereferences to
release commit `bfc8c5af85734583f966ee70d2ec521155432205`, which is an
ancestor of HEAD with 15 intervening commits. `git remote -v` produced no
output. `./run version-check` read 0.8.0 from the Rust package, Python package,
FastAPI literal, this header, and the newest changelog release; the changelog's
`v0.8.0 — 2026-07-24` entry matches the tag, and the ahead-of-tag warning is
expected.

The current matrix also corrects the draft's stale 92-test count. Pinned
Rust/Cargo **1.91.1** passed warning-denied locked workspace check and **98**
tests, warning-denied net check and **20** net tests, clippy, and fmt.
Rust/Cargo **1.78.0** passed warning-denied locked workspace check and the same
**98** tests. Python **3.11.4** byte-compiled every file under `tools/` and
`shell/` and passed **88** shell tests. The system Python **3.12.13** has no
`pytest`, so its preliminary command stopped before collection and is not
counted; the existing isolated 3.12.13 environment from B0.2 passed
`pip check` and all **88** tests without any download. Both counted lanes
reported the same one third-party Starlette deprecation warning. ShellCheck
**0.11.0** passed `run`.

`./run down` completed and independent `lsof` checks proved ports 8787, 8788,
and 8899 clear. `./run verify-artifacts` passed 2/2, followed by direct
read-only measurement:

- `data/core.db`: SHA-256
  `db2f186e291c64192e567c9dfb979dd9877eb32b13c2ce2724a4acf1761a37a0`,
  **6,729,728 bytes**, **1,764 documents**, 0 NULL `simhash`, 0 NULL
  `canonical_id`, integrity `ok`; cursor `arxiv-cs | NULL | 2026-07-20 | NULL
  | 2026-07-23 12:08:13`.
- `data/live-smoke.db`: SHA-256
  `94f03e9e8662dddfa5c80b63a9845d9926a1fa10060b83638ee094e0a0462c4a`,
  **9,490,432 bytes**, **2,600 documents**, 0 NULL `simhash`, 0 NULL
  `canonical_id`, integrity `ok`; cursor `arxiv-cs |
  verb%3DListRecords%26metadataPrefix%3Doai_dc%26from%3D2026-07-22%26until%3D2026-07-22%26set%3Dcs%26skip%3D88
  | NULL | 2026-07-22 | 2026-07-22 23:45:38`.

The failure-capable artifact control copied `data/core.db` beneath
`/private/tmp`, recorded its real expected hash in a disposable manifest, and
mutated only that copy with a planted SQLite table. Its hash changed to
`525370f250e4de32865dbc41f2dbd016f3da5fe754154080e25e1c9a2de28aea`;
`./run verify-artifacts <disposable-manifest>` exited 1, printed both hashes,
and reported 0/1 match. The real manifest immediately returned 2/2.

`./run golden` used disposable database
`/var/folders/cl/4zcmgrj928n_y07msdz5pjj00000gn/T/tmp.bWX2BZjuKG/golden.db`
and passed all 11 named assertions: 13/13 initial ingest; acme completion and
12 analyzed; the exact near-duplicate pair at hamming 12; DeepSeek RISING at
z=10.0 from three sources; second acme ingest +0; quant-desk 1 document;
`/v1/ask` four citations with `techwire::tw-004` suppressed; IndexOnly snippets
NULL; search hits acme 6 / quant 0; and bad-key 401.

`./run config` was read-only and redacted: LAN chat resolves to
`http://192.168.0.192:8080/v1`,
`gemma-4-26B-A4B-it-UD-IQ4_XS.gguf`, timeout 30s; LAN embeddings resolve to
`http://192.168.0.192:8081/v1`,
`embeddinggemma-300M-Q8_0.gguf`, timeout 30s. The embedding dimension remains
the previously wire-evidenced **768**; B0 made no provider request and makes no
claim that either endpoint is currently reachable. Final artifact verification
again returned 2/2 exact, all three local ports were clear, and `Cargo.lock`
was untouched.

**v0.9 A1 is complete (measured 2026-07-24).** The gate passed before any
edit: both protected hashes matched the B0 values. The old
`config/protected-artifacts.sha256` has been removed, and
`config/protected-artifacts.json` is now the only expected-hash authority. Its
two records combine relative path, SHA-256, byte size, purpose/provenance,
document count, integrity expectation, NULL `simhash` / `canonical_id`
expectations, and complete cursor rows. The manifest also carries the checked
immutable-evidence, fresh-harvest-only, and explicit wire-evidence/operator
review admission policy.

`./run verify-artifacts` opened both databases read-only and matched every
recorded field: `data/core.db` remained
`db2f186e291c64192e567c9dfb979dd9877eb32b13c2ce2724a4acf1761a37a0`,
6,729,728 bytes, 1,764 documents, integrity `ok`, 0/0 NULL counts, and one
cursor; `data/live-smoke.db` remained
`94f03e9e8662dddfa5c80b63a9845d9926a1fa10060b83638ee094e0a0462c4a`,
9,490,432 bytes, 2,600 documents, integrity `ok`, 0/0 NULL counts, and one
cursor. Two consecutive `./run evidence-report` outputs compared
byte-identical. The report contains only deterministic measured database
facts; it does not rewrite the manifest or either database.

Failure-capable controls used only a `data/core.db` copy under
`/private/tmp/intel-a1-controls.t6KW9J`. Adding a table while retaining the
original record exited 1 and named `core.db field=sha256` (actual
`811d8b6c32f9bb976bd4dc9e49a524940ac3183faec9d31044bc59196d987482`).
Deleting one copied document, then recording the copy's fresh hash and byte
size, exited 1 only on `core.db field=documents` (1,764 expected, 1,763
actual). Changing the copied `arxiv-cs` cursor to `a1-control`, again with a
fresh matching hash and size, exited 1 only on
`core.db field=cursors.arxiv-cs.cursor`. Five automated disposable-database
tests preserve the same three controls plus deterministic-report and
canonical-path coverage.

Live-harvest attempts against `data/core.db`, `./data/live-smoke.db`, the
absolute `data/core.db` path, and a symlink to `data/core.db` each stopped
before reachability with exit 2, named the matching JSON record, and printed a
fresh safe destination. `./run test` began with full 2/2 evidence verification
and passed 98 workspace, 20 net, and 93 Python 3.11 tests. The isolated Python
3.12.13 lane independently passed the same 93 tests. `./run ci-local` passed
all 16 configured jobs, including warning-denied offline/net builds, clippy,
fmt, ShellCheck, Python floor compilation, locked Rust 1.78 check/tests, the
11/11 golden E2E, and final evidence verification. CI now validates the
committed manifest schema and executes the disposable verifier controls. At A2
this remained configuration rather than runner evidence; v0.10/G2 later
observed the first execution. Final hashes remained exact, and `Cargo.lock` was
untouched.

Exact A1 verification commands included:

```bash
python3 tools/evidence_artifacts.py validate
./run verify-artifacts
./run evidence-report
PYTHONPATH=shell .venv/bin/python \
  -m pytest shell/tests/test_evidence_artifacts.py -q
shellcheck ./run
./run ci-local
./run test
PYTHONPATH=shell \
  /private/tmp/intel-platform-py312-baseline.wqTLIV/venv/bin/python \
  -m pytest shell/tests -q
```

**v0.9 D3 is complete (measured 2026-07-24).** Its pre-edit gate passed:
`./run verify-artifacts` matched both records and `./run golden` passed all
11/11 assertions before any tracked edit. The active runbook now preserves its
original entering and drafting hypotheses and appends dated corrections naming
B0 `1054994` and A1 `2adf486`. A committed-record search found no citation of
P2/V1/deferred-audit/R2's old numeric steps outside the active runbook, so D3
became Step 3 and those unstarted tasks became Steps 4–7; the Step 2A fallback
was not used. The v0.9 evidence-manifest A1 is explicitly distinguished from
v0.8.2's fingerprint-verifier A1, while its committed id remains unchanged.
The colliding deferred-audit id is now D4.

V1's proposed round 1,000/100 ms ceilings are superseded by an anchored
recommendation. A3's measured post-change request on the 2,600-row archive was
16.264 ms for `POST /retrieve` with `learning`, sector `science`, `k=8`.
Recommended predeclared p95 thresholds are 10× that anchor for cold
(162.640 ms) and 2× for warm (32.528 ms), with the factors, exact firing
values, rationale, and physical plausibility fixed before any sample. V1 now
requires separate disposable 1,764- and 2,600-row archive measurements, both
distributions and their slope, configured `science` sectors, non-zero document
counts, and warm cache hits against an unmoved generation. An empty-sector
warm run or an SLO that cannot fire is a failed benchmark. P2 now ships its
failure-capable harness half even when transport is blocked, but keeps its
checklist box open and records the live leg as a non-result until an in-cycle
rerun succeeds. R2 must inventory the disposition of every non-result carried
out of the cycle.

**P1 supersession — 2026-07-24.** P1's preserved present-tense reference to
`config/protected-artifacts.sha256` is historical. A1 deleted that file;
`config/protected-artifacts.json` is the sole current expected-hash authority.
The P1 section body remains unchanged.

**Manifest-admission risk — 2026-07-24.** Source search found the `admission`
literal in the JSON manifest, the schema validator that accepts only that
literal, and the disposable test fixture. Nothing records or verifies the
claimed wire evidence and operator review when an expected hash is edited.
The A1 controls intentionally refreshed disposable manifests after logical
mutations, demonstrating the same remaining bypass shape: a manifest edit can
bless changed bytes. Git review is the sole control and is prose. A v0.10
candidate must make admission failure-capable before the first proposal to add
a protected artifact or change an expected protected hash; until that trigger,
only evidence verification—not admission—is claimed executable. D3 implements
no control.

**Python 3.12 environment correction — 2026-07-24.** The old counted lane at
`/private/tmp/intel-platform-py312-baseline.wqTLIV/venv` was frozen before
replacement. The Python 3.11 `.venv` freeze was captured independently:

```text
annotated-doc==0.0.4
annotated-types==0.7.0
anyio==4.14.2
certifi==2026.6.17
click==8.4.2
fastapi==0.139.2
h11==0.16.0
httpcore==1.0.9
httpx==0.28.1
idna==3.18
iniconfig==2.3.0
packaging==26.2
pluggy==1.6.0
pydantic==2.13.4
pydantic_core==2.46.4
Pygments==2.20.0
pytest==9.1.1
starlette==1.3.1
typing-inspection==0.4.2
typing_extensions==4.16.0
uvicorn==0.51.0
```

The old Python 3.12 lane froze as:

```text
annotated-doc==0.0.4
annotated-types==0.8.0
anyio==4.14.2
certifi==2026.7.22
click==8.4.2
fastapi==0.139.2
h11==0.16.0
httpcore==1.0.9
httpx==0.28.1
idna==3.18
iniconfig==2.3.0
packaging==26.2
pluggy==1.6.0
pydantic==2.13.4
pydantic_core==2.46.4
Pygments==2.20.0
pytest==9.1.1
starlette==1.3.1
typing-inspection==0.4.2
typing_extensions==4.16.0
uvicorn==0.51.0
```

The sets differ at `annotated-types` (0.7.0 versus 0.8.0) and `certifi`
(2026.6.17 versus 2026.7.22). A fresh Python 3.12.13 lane was then built at
the ignored `.venv/py312` from the literal commands now recorded in
`AGENTS.md §4`; its freeze compared byte-identical to the old 3.12 set and
passed **93 tests** with the same one Starlette warning. This match is a dated
measurement, not reproducibility: `shell/requirements.txt` contains lower
bounds, not pins, so the command is repeatable but may resolve differently
later. Pinning or a constraints file is a v0.10 candidate; D3 did not change
the build input.

Final local acceptance passed all **16/16** `./run ci-local` jobs: version
consistency, Python 3.11 byte-compilation, ShellCheck, warning-denied workspace
check and **98 tests**, warning-denied net check and **20 tests**, clippy, fmt,
locked Rust 1.78 check/tests, **93 Python 3.11 shell tests**, golden 11/11,
protected evidence 2/2, fingerprint fixture, and progress validation. The
fresh Python 3.12 lane independently passed the same **93 shell tests**.
No Rust, Python, `run`, dependency, requirement, architecture, or protected
data change was made; `Cargo.lock` remained untouched.

**v0.9 P2 harness half is complete; live leg is a non-result (measured
2026-07-24).** `./run probe-providers` resolves the selected chat and embedding
identities through the same shell configuration as the product path. Optional
`LLM_CHAT_TRANSPORT_BASE_URL` and `LLM_EMBED_TRANSPORT_BASE_URL` values replace
only the request route after identity resolution; configured endpoint, model,
credential, and role timeout remain authoritative. Loopback transport aliases
disable ambient proxies. `./run config` prints configured and effective
endpoints, models, timeouts, and the expected embedding dimension with keys
redacted. `LLM_EMBED_EXPECTED_DIMENSION` must name the last wire-measured width;
the command will not infer or refresh it.

The bounded probe requests chat `/health` and `/v1/models`, requires the known
HTTP 501 unsupported-embeddings diagnosis from the chat role, then requests
embedding `/health`, `/v1/models`, and one short embedding. Success requires
the configured identities, exactly one index-0 finite vector, and the
predeclared dimension. Every response records route, status, and a bounded,
key-redacted body. No-response failures explicitly record `status=none` and
`body=none`. The only outcomes are `PASS`, `TRANSPORT BLOCKED`,
`IDENTITY CHANGED`, and `CAPABILITY FAILED`; only `PASS` exits zero.

Five local-double controls are failure-capable. The passing double returned the
known chat 501 and one four-dimensional embedding while echoing both
Authorization values; output replaced both with `[REDACTED]`. A wrong chat
model and a five-versus-four vector each produced `IDENTITY CHANGED`; an empty
embedding list produced `CAPABILITY FAILED`; and a real 200 ms delayed health
response under a 50 ms role timeout produced `ReadTimeout` and
`TRANSPORT BLOCKED`. All three failure classes exited non-zero. The targeted
provider/config suite passed **15/15**; the full shell suite passed **99 tests**
under Python 3.11.4 and independently under the rebuilt Python 3.12.13 lane,
each with the one third-party Starlette warning.

The live gate is blocked. Bounded direct curls to
`http://192.168.0.192:8080/health` and
`http://192.168.0.192:8081/health` each returned exit **7**, HTTP **000**,
`Couldn't connect to server`, in 1 ms. The new command, with expected
dimension **768**, classified the direct chat route `TRANSPORT BLOCKED`, exit
1, with `[Errno 65] No route to host`; it correctly stopped before later
provider stages. The prior transport-only aliases are also absent:
`http://127.0.0.1:18080/health` returned `[Errno 61] Connection refused`, and
`:18081/health` returned curl exit 7 / HTTP 000 immediately. No provider HTTP
response exists, no model or dimension was re-measured, and `./run verify-llm`
was not invoked. The required next action remains operator-owned: start the
same SSH forwards and confirm the route, then rerun the probe and, only after
`PASS`, one uninterrupted verifier in this cycle. P2's checkbox remains open;
this non-result does not create a correction-cycle file.

Local acceptance passed all **16/16** `./run ci-local` jobs: warning-denied
workspace/net checks, **98 workspace tests**, **20 net tests**, clippy, fmt,
locked Rust 1.78 check/tests, ShellCheck, Python floor byte-compilation, the
**99-test** Python 3.11 shell lane, golden **11/11**, protected artifacts
**2/2**, fingerprint fixture, version consistency, and progress validation.
A hostile inherited pair of transport aliases pointing at unused loopback
ports was planted around a separate golden run; golden still passed 11/11,
proving its deterministic mock route clears live overrides. No dependency or
architecture invariant changed; `Cargo.lock` and both protected artifacts
remained untouched.

**v0.9 P2 live leg completed on the in-cycle rerun (measured 2026-07-24).**
This dated result supersedes the live non-result above without deleting it.
After the operator confirmed the SSH forwards, `./run config` retained the
configured LAN identities while resolving chat transport to
`http://127.0.0.1:18080/v1` and embedding transport to
`http://127.0.0.1:18081/v1`; both role timeouts remained 30 seconds and keys
remained redacted.

The exact minimal probe passed. Chat `/health` and `/v1/models` returned HTTP
200 and identified `gemma-4-26B-A4B-it-UD-IQ4_XS.gguf`; the intentional chat
`POST /v1/embeddings` returned the required HTTP 501 body stating that the
server does not support embeddings without `--embeddings`. Embedding `/health`
and `/v1/models` returned HTTP 200 and identified
`embeddinggemma-300M-Q8_0.gguf`; one short `POST /v1/embeddings` returned HTTP
200, exactly one item at index 0, and a measured vector dimension of **768**,
matching the predeclared expected value. Final classification was `PASS`; no
identity or capability gate fired.

One subsequent `./run verify-llm` execution ran uninterrupted on a fresh
temporary fixture database and passed **6/6 required checks**:

- fixture ingest: **13 fetched / 13 new**;
- embedding backfill: **13 missing → 0**, exactly one real provider request,
  provider dimension **768**, stored stats `{count: 13, dim: 768,
  inconsistent_dimensions: false}`, latency **0.47s**;
- fusion: clean retrieval notes, five hybrid context documents, latency
  **0.04s**;
- ordinary public `/v1/ask`: **17.01s**, four citations, all four cited
  documents IndexOnly, and no independent-oracle gated overlap after
  attestation;
- adversarial public `/v1/ask`: **9.04s**, `NOT EXERCISED`,
  `violations: []`, with seven IndexOnly context documents. This remains
  explicitly not evidence that a real model tripped `/attest`, and it was
  never `LEAK`.

The verifier reported five diagnostic warnings—four measured latencies plus
the adversarial `NOT EXERCISED` outcome—and also emitted the existing
third-party Starlette deprecation warning. It stopped its isolated core
cleanly. The post-live `./run ci-local` matrix passed **16/16** with **98
workspace**, **20 net**, and **99 Python 3.11 shell** tests; the Python 3.12.13
lane independently passed the same **99** shell tests. Golden remained
**11/11**, protected evidence remained **2/2** exact, and the progress record
was valid. Both P2 halves are now recorded and its checklist box is checked.
No provider configuration, dependency, lockfile, architecture invariant, or
protected artifact changed.

**v0.9 V1 is complete; the `/view` cold trigger fired (measured
2026-07-24).** The operator approved the SLO before the first sample. It is
anchored to A3's 16.264 ms `POST /retrieve` measurement on the 2,600-row
archive (`learning`, sector `science`, `k=8`): cold p95 fires above
**162.640 ms** (10×, covering a new process, SQLite open, sector corpus load,
and analysis), while warm p95 fires above **32.528 ms** (2×, requiring a real
cache hit to remain near the measured local HTTP/store cost). Both values were
declared physically plausible on this Apple M2 Pro / 12 logical CPU /
17,179,869,184-byte / macOS 26.5.2 host. The declaration is preserved at
`evidence/v0.9/view-benchmark/SLO.md`.

`./run benchmark-view` verified both protected hashes, built `cored`, made one
byte-for-byte temporary copy of each archive, and measured two complete runs
per copy. Each cold distribution contains ten new-process/first-request
samples. Each warm distribution contains 100 timed requests after an unmeasured
prime on one process. The query sector `science` was read from
`config/core.json`; every timed response asserted a positive
`documents_analyzed`. Internal `/view` diagnostic headers now expose
`x-intel-view-cache: hit|miss` and the numeric
`x-intel-view-generation`, allowing every warm sample to assert a hit against
the prime's unmoved generation without changing the JSON body.

Measured p95 results:

| run | protected archive | documents | cold p95 / 162.640 ms | warm p95 / 32.528 ms |
|---:|---|---:|---:|---:|
| 1 | `data/core.db` copy | 1,764 | **1,693.423417 ms — MISS** | **8.164166 ms — PASS** |
| 1 | `data/live-smoke.db` copy | 2,600 | **543.318334 ms — MISS** | **12.584125 ms — PASS** |
| 2 | `data/core.db` copy | 1,764 | **362.794125 ms — MISS** | **8.469334 ms — PASS** |
| 2 | `data/live-smoke.db` copy | 2,600 | **523.764917 ms — MISS** | **12.565458 ms — PASS** |

The retained 1,693.423417 ms first-run outlier makes that run's cold two-point
slope negative and unsuitable as a scaling estimate; it was not discarded.
The second complete run still missed the cold gate and measured
**192.548794 ms p95 per 1,000 documents** between the two corpus points. Warm
slopes were **5.287032** and **4.899670 ms p95 per 1,000 documents**. Exact
samples, min/median/p95/max, archive hashes, source hashes, hardware, and both
slopes are preserved in the four reports and `summary.json` under
`evidence/v0.9/view-benchmark/`.

Failure-capable controls ran through the same command. A delayed local endpoint
measured cold **223.578458 ms** and warm **220.598291 ms**, named both paths,
and exited 1. A separate empty-sector double returned zero documents on its
purported warm hit; the benchmark named the non-positive count and exited 1.
The targeted test file passed 3/3. Both protected artifacts were 2/2 exact
before and after every control and the real benchmark, and the post-benchmark
golden run remained 11/11.

Final local acceptance passed all **16/16** `./run ci-local` jobs:
version-check; Python 3.11 floor byte-compilation; ShellCheck; warning-denied
workspace check and **98 tests**; warning-denied net check and **20 tests**;
clippy; fmt; locked Rust 1.78 check/tests; **102 Python 3.11 shell tests**;
golden **11/11**; protected artifacts **2/2**; persisted fingerprints; and
progress validation. The rebuilt Python 3.12.13 lane independently passed the
same **102 shell tests**. Both shell lanes emitted the one third-party
Starlette warning. `Cargo.lock` was untouched.

The gate disposition is **promote, not implement**: both archives missed the
cold SLO in both runs, while every warm cell passed. V1 added the scoped future
V2 design task to `TASKS-v0.9-EXECUTION.md` and stopped without a cache table or
other materialization. V2 must first decompose cold startup/load/analysis/body
cost and prove restart-safe invalidation before choosing a representation;
the in-memory warm cache is already within SLO.

**v0.9 D4 is complete; four triggers remain deferred and `/view` remains
promoted (measured 2026-07-24).** `./run audit-deferred` made the five-item
table executable against repository, deployment, live-process, protected-
archive, and V1 evidence. Its exact report is
`evidence/v0.9/deferred-audit/report.json`.

| item | unchanged trigger | measured production state | disposition |
|---|---|---|---|
| T7 robots single-flight | a second concurrent harvester | `config/schedule.json` has 2 specs expanding to 5 jobs, but `Scheduler.tick` invokes them in one serial loop. The documented systemd and in-process modes are alternatives; the unit is one `Type=oneshot --once` process. Supported simultaneous harvest callers: **1**. Process census: **0** schedulers, **0** `cored`, port 8788 not accepting. | **defer** |
| Postgres | a second archive writer | Production constructs exactly **1** `SqliteStore` in `cored`, backed by one `Mutex<Connection>`; the shell has **0** direct `CORE_DB` writers. | **defer** |
| pgvector | exact cosine over the archive stops fitting the measured request budget | Shipped release-mode `SqliteStore::vector_search`, exact cosine over deterministic **768d** vectors: **7.055666 ms p95** at 1,764 rows and **8.961583 ms p95** at 2,600 rows, below A3's measured **16.264 ms** full-request anchor. | **defer** |
| multi-host seam hardening | an actual core/shell host split | Core default bind `127.0.0.1:8788`; shell default and systemd `CORE_URL=http://127.0.0.1:8788`; **0** recorded remote `CORE_URL` hits and no active deployment process. | **defer** |
| `/view` materialization | cold or warm p95 crosses the predeclared V1 SLO in both runs | V1's four reports show both archives missed cold in both runs and all warm cells passed. | **promote → V2**, already scoped; no implementation |

The T7 count is callers, not configured jobs: two source jobs, one sector job,
one refresh, and one full pipeline job can all be due, but the same scheduler
calls `job.action()` serially. The current process census used `ps`; no project
scheduler or `cored` process was present, and an independent connect probe
found no listener on loopback 8788. The one supported deployment may be either
the one-shot systemd timer or one long-lived loop, as the deployment guide
requires the operator to pick one. Starting both is not the supported topology
and would be the unchanged second-harvester trigger.

The archive write inventory remains core-owned:

- `SqliteStore::open` owns schema/FTS creation, cursor migration, and missing-
  fingerprint backfill at `cored` startup.
- `/ingest` owns `append_new` plus corpus-wide canonical-id rematerialization;
  the paged path owns documents, canonical ids, and cursor in one
  `commit_harvest_page` transaction.
- `/embeddings` owns embedding upserts and `/signals/record` owns
  `signals_history`.
- `update_document` and `delete_document` remain maintenance/test surfaces
  with no production `cored` caller.
- The public billing handlers, admin-key CLI, and one-shot subscription
  migration may write the separately selected `SUBSCRIPTIONS_PATH` through
  `SqliteSubscriptionStore.save`; none names or writes `CORE_DB`. This is the
  already-recorded HC9 shell-configuration scope, not a second archive writer.

The pgvector audit measured the shipped Rust method rather than a Python cosine
approximation. Both protected archives originally contain **0 embedding
rows**. One byte-for-byte temporary copy of each was seeded with deterministic
768-dimensional vectors for every document, warmed once, and measured for
**30** searches returning eight hits with zero dimension mismatches. The
1,764-row distribution was min/median/p95/max
**4.072458/4.421105/7.055666/7.284666 ms**. The 2,600-row distribution was
**6.954083/7.415417/8.961583/9.536292 ms**, a measured two-point p95 slope of
**2.279805 ms per 1,000 documents**. The scale note's order-of-magnitude
expectation remains 10⁵–10⁶ documents. A3's 16.264 ms observation is an
anchor, not a retrieval SLO; current exact cosine remains below even that
measured whole-request cost, so no round document threshold was substituted
for latency and pgvector remains deferred.

The failure-capable control supplied exactly two harvesters and two archive
writers. It printed `PROMOTE T7 robots single-flight` and `PROMOTE Postgres`,
kept the other three synthetic triggers deferred, printed `CONTROL FIRED`, and
exited **1**. The production audit then printed four deferrals plus
`PROMOTE /view materialization`, named V2, and exited zero because the measured
promotion was recorded rather than bypassed. Both runs verified protected
artifacts 2/2 before and after. No single-flight lock, Postgres/pgvector code,
UDS/mTLS seam, or `/view` materialization was added.

The first full-matrix attempt stopped at clippy after every earlier job passed:
the new benchmark's MSRV-compatible even-length median check triggered
`manual_is_multiple_of`. Clippy's suggested `usize::is_multiple_of` is newer
than the Rust 1.78 floor, so the example carries the same narrow, reasoned
allowance pattern already used elsewhere in the repository. Targeted clippy
then passed, and Rust 1.78 compiled the example. The regenerated audit report
records the hash of that exact lint-clean source.

The complete rerun passed all **16/16** `./run ci-local` jobs:
version-check; Python 3.11 floor byte-compilation; ShellCheck; warning-denied
workspace check and **98 tests**; warning-denied net check and **20 tests**;
clippy; fmt; locked Rust 1.78 check/tests; **105 Python 3.11 shell tests**;
golden **11/11**; protected artifacts **2/2**; persisted fingerprints; and
progress validation. The Python 3.12.13 lane independently passed the same
**105 shell tests**. Both lanes emitted the one third-party Starlette warning.
`Cargo.lock` was untouched.

**v0.9 R2 selected v0.9.0 and the release candidate is green (measured
2026-07-25).** After seeing the actual diff, the operator explicitly approved
**v0.9.0**. The rule was decisive rather than cosmetic: the changes since
`v0.8.0` include persisted-fingerprint failure behavior, SQL-scoped core reads,
bounded/validated `/view` caching with internal diagnostics, and provider
transport resolution. Those are runtime, storage-path, and internal API
changes, so the patch-only and no-release dispositions do not describe the
artifact.

Immediately before R2 edits, `v0.8.0..HEAD` contained **29 commits**. The
release candidate's `git diff --name-status v0.8.0` contains **44 files**, and
`git diff --stat v0.8.0` reports **9,868 insertions / 238 deletions**. Every
path is classified here exactly once:

- **runtime, storage path, and internal API:** `apps/cored/src/main.rs`,
  `crates/store/src/sqlite.rs`, and `shell/intel_shell/llm.py`;
- **public/release API metadata:** `apps/cored/Cargo.toml`, `Cargo.lock`,
  `shell/intel_shell/__init__.py`, and `shell/intel_shell/app.py`;
- **operations:** `.env.example`, `.github/workflows/ci.yml`, `run`, and
  `tools/{audit_deferred,benchmark_view,evidence_artifacts,probe_providers,progress_check,version_check}.py`;
- **executable evidence and failure controls:**
  `config/protected-artifacts.json`, deleted
  `config/protected-artifacts.sha256`,
  `crates/store/examples/{cosine_bench,fingerprint_fixture,verify_fingerprints}.rs`,
  all seven files under `evidence/v0.9/`, all five changed/added files under
  `shell/tests/`, and `PROGRESS-v0.8.md` plus `PROGRESS-v0.9.md`;
- **documentation and task metadata:** `AGENTS.md`, `ARCHITECTURE.md`,
  `CHANGELOG.md`, `README.md`, `STATE.md`, `TASKS-v0.8.md`,
  `TASKS-v0.8.1-EXECUTION.md`, `TASKS-v0.8.2-EXECUTION.md`, and
  `TASKS-v0.9-EXECUTION.md`.

The carried non-result inventory is explicit:

- P2's initial direct-route transport block was superseded in-cycle by the
  operator-confirmed tunnel rerun, live minimal probe, and uninterrupted 6/6
  verifier; it is historical and carries no incomplete P2 leg.
- The real model's adversarial request remained **NOT EXERCISED**, with no
  violations. Failure-capable doubles prove `GUARD FIRED` and `LEAK`
  classification, but this cycle does not claim that a real model tripped
  `/attest`.
- V1's cold p95 missed on both archives in both independent runs. Its
  disposition is future design task **V2**, not an unrecorded implementation;
  every warm cell passed.
- D4 keeps T7 single-flight, Postgres, pgvector, and multi-host hardening
  deferred under their measured second-harvester, second-writer,
  exact-cosine-latency, and actual-host-split triggers.
- Manifest admission remains prose-only. Its executable control is a v0.10
  candidate required before changing a protected expected hash or adding a
  protected artifact.
- `shell/requirements.txt` still declares floors rather than pins. A
  constraints/pinning decision remains a v0.10 candidate; the recorded Python
  3.12 command is repeatable, not guaranteed reproducible.
- At the v0.9 close this checkout had no Git remote and no observed CI-runner
  execution. That release evidence is the measured local matrix; workflow
  configuration was not represented as a runner result. v0.10/G2 later added
  `origin` and captured the first actual runner execution.

The R2 failure control changed only
`shell/intel_shell/__init__.py` from 0.8.0 to 0.8.1.
`./run version-check` exited **1** and named that file and disagreeing value.
Restoration returned its SHA-256 exactly to
`996bd313663052d57f490c0af219f1604898dd7e91a35b892fffee54401ac713`,
and the checker passed again. Cargo regenerated `Cargo.lock` after the package
version edit; its complete diff is the local `cored` version
0.8.0 → 0.9.0, with no dependency or lock-format change.

The final release-candidate `./run ci-local` passed **16/16**: all agreeing
version sources at 0.9.0; Python 3.11 byte-compilation; ShellCheck 0.11.0;
warning-denied pinned workspace check and **98 tests**; warning-denied net check
and **20 tests**; clippy; fmt; warning-denied locked Rust 1.78 check/tests;
**105 Python 3.11 shell tests**; golden **11/11**; protected artifacts **2/2**;
persisted fingerprints; and progress validation. The separate Python 3.12.13
lane passed the same **105 tests**; both lanes reported the one third-party
Starlette warning. The first sandboxed golden and Python 3.12 attempts were
denied local loopback binds before their relevant assertions and are
non-results; identical permitted reruns produced the counted passes. Release
commit and annotated-tag hashes are necessarily recorded only after the
release commit exists, in the separate R2 audit record.

**R2 release identity — 2026-07-25.** Release commit
`4c59db2727eda1c81beae3ff38be883a26a92ae8` was created from the exact
twice-green release content with a clean worktree. Annotated tag object
`548ffdfec4e414570ddecf813aa2f2d616662487` has type `tag`, carries annotation
`intel-platform v0.9.0`, and dereferences exactly to that release commit.
`git rev-parse v0.9.0^{}` and `git rev-parse HEAD` matched before the audit
append, and `./run version-check` passed at the exact tag. The following
append-only audit commit intentionally leaves HEAD one commit ahead; the tag
remains fixed on the release artifact.

**B0.2 is complete (measured 2026-07-24).** The v0.8.2 entering-state
gate passed from a clean Cargo target: 92 workspace Rust tests, 20 net tests,
and 88 shell tests under both Python 3.11.4 and 3.12.13; warning-denied
offline/net checks, clippy, fmt, ShellCheck, Python byte-compilation, and locked
Rust 1.78 check/tests all passed. `./run golden` passed 11/11 after the
sandboxed bind attempt was refused and the permitted loopback run executed;
`./run verify-artifacts` remained 2/2. Direct read-only SQLite census measured
`data/core.db` at 1,764 documents and `data/live-smoke.db` at 2,600, with 0
NULL `simhash`, 0 NULL `canonical_id`, and `PRAGMA integrity_check = ok` in
both. Their post-census hashes remained exact. Git measured
`e212a7cdf269c171e1db4fb06002090a0939a95a` /
`v0.8.0-2-ge212a7c`; the only entering worktree item was the operator-added
untracked `TASKS-v0.8.2-EXECUTION.md`, and `git remote -v` produced no output.

**D0 is complete (measured 2026-07-24).** `AGENTS.md` now points its active
cycle header and per-task workflow at `TASKS-v0.8.2-EXECUTION.md`, names
`TASKS-v0.9-EXECUTION.md` as the next cycle, and keeps `PROGRESS-v0.8.md` as
the contiguous correction trail. A repository search found no remaining
`TASKS-v0.8-EXECUTION` pointer in `AGENTS.md`; line-by-line diff review found
only those pointer/continuity edits and no rule change. Golden remained 11/11
and protected artifacts remained 2/2 exact.

**A1 is complete (measured 2026-07-24).** The fingerprint verifier now queries
NULL `simhash` and `canonical_id` rows through a raw read-only SQLite
connection before any `SqliteStore::open`, prints both counts, names up to ten
offending ids, and refuses either defect without repairing it. Before the fix,
a planted NULL fingerprint was silently backfilled and a planted NULL
canonical id passed; afterward, each control exited 1, named
`golden::fingerprint-control`, and a direct read-only query proved the NULL
still present. A stale body edit also exited 1 and named the id; a clean
fixture printed `null_fingerprints=0`, `null_canonical_ids=0`, and
`fingerprint_mismatches=0`. `./run verify-fingerprints` is executed immediately
after protected-artifact verification in `./run test`, and the configured core
workflow job has the same check over a deterministic scratch fixture (no
runner had executed it at A1; v0.10/G2 later observed that step pass). The
runbook's claim that
core CI could reuse the golden E2E database was stale: `./run golden` owns and
deletes that database inside its process, so A1 added a one-document
failure-capable fixture builder rather than copying a protected archive.
Final verification passed 92 workspace tests, 20 net tests, 88 shell tests,
warning-denied offline/net checks, clippy, fmt, Bash syntax, and ShellCheck;
golden remained 11/11 and protected artifacts remained 2/2 exact.

**A2 is complete (measured 2026-07-24).** The persisted-fingerprint invariant
now fails closed at all three consumers. A planted NULL made the unchanged
store tests fail before the repair: `/view` surfaced only
`Invalid column type Null`, while canonical assignment returned `Ok(0)`.
A scratch live core independently measured `/retrieve` returning 200 with the
document (request-time recompute) and ingest returning 200 while leaving both
`simhash` and `canonical_id` NULL. After the repair, `/view`, `/retrieve`, and
the ingest-triggered canonical assignment each returned 500 naming
`golden::fingerprint-control` and directing the operator to
`./run verify-fingerprints`; the NULLs remained present. Canonical assignment
now reads all rows and errors on the first NULL; `/retrieve` refuses a fused id
absent from the persisted map; `/view` maps NULL to a legible document-specific
error. `rg "simhash\\(" apps/cored/src/main.rs` found no request-path
recompute. All A1 NULL/stale controls still failed as designed and left their
planted values intact. The full matrix passed 95 workspace tests, 20 net tests,
88 shell tests, warning-denied offline/net checks, clippy, fmt, ShellCheck, and
locked Rust 1.78 check/tests. Golden remained 11/11 and both protected hashes
remained exact, so the corpus-identity gate did not move.

**A3 is complete (measured 2026-07-24).** HC2 sector placement is now explicit
in `SqliteStore::documents_in_sectors`: `/view` no longer materializes the
whole archive and filters in Rust. `documents_by_ids` uses bound `IN`
parameters, and `/retrieve`, `/attest`, and `/docs` now load only their
requested ids rather than every document body. The store-level control inserted
a finance document beside technology rows and proved the technology-sector SQL
never returned it; `/view` independently excluded the finance id. An id shaped
as `quoted',finance-doc` was returned exactly once through a bound parameter,
without interpolating or matching the real finance id. Against fresh disposable
copies of the same 2,600-row `data/live-smoke.db`, one HTTP `/retrieve` for
`learning`, sector `science`, `k=8` measured **0.039740s before** and
**0.016264s after**; both returned 200 with 8 fused, 8 context, and 0
suppressed documents. These are single wall-clock observations (2.44× in this
run), not an SLO. The full matrix passed 97 workspace tests, 20 net tests, 88
shell tests, warning-denied offline/net checks, clippy, fmt, ShellCheck, and
locked Rust 1.78 check/tests. Golden remained 11/11 and both protected hashes
remained exact, so the output-preservation gate did not move.

**A4 recorded an accepted risk (measured 2026-07-24).** The proposed context
receipt cannot satisfy its required different-retrieval control. An
`/attest` request containing only `{answer, receipt}` gives the core no value
that identifies which retrieval supplied the shell's prompt: a live receipt
from retrieval B is therefore indistinguishable from the intended receipt from
retrieval A. A receipt also cannot force a rewritable shell to call `/attest`
before it owns the public response. Capacity, TTL, opacity, and one-time use do
not create either missing fact; making only the newest receipt valid would
instead break concurrent honest requests. The receipt seam was not shipped,
and the existing `{answer, context_doc_ids}` contract remains. The accepted
risk is precise: the shipped shell is part of the trusted computing base for
`/v1/ask`; core attestation prevents accidental copied-text leaks on that path,
but it does not constrain an arbitrary rewritten shell. Revisit before any
third-party/untrusted shell is supported, or before claiming HC1 is invariant
under shell replacement. The necessary trigger is an architecture in which
every public answer must traverse a core-owned (or equivalently
non-bypassable) attestation response boundary while the model call remains in
the shell under HC3. The decision-only change left the golden E2E at 11/11,
including four `/v1/ask` citations, and both protected artifact hashes exact.

**A5 is complete (measured 2026-07-24).** `/view` now intersects request
sectors with configured sector ids, sorts and de-duplicates that set before it
becomes a cache key, and does not cache an all-unknown request. The
process-scoped cache is bounded by the named `VIEW_CACHE_CAPACITY = 256` and
evicts oldest insertions first. The failure-capable test failed on the 257th
configured key before the repair; afterward, 300 distinct configured keys
never exceeded 256 entries, the newest entry remained a cache hit, and 50
unknown-sector requests added zero entries. Existing hit, no-op ingest, and
generation-invalidation tests remained green. The full matrix passed 98
workspace tests, 20 net tests, 88 shell tests, warning-denied offline/net
checks, clippy, fmt, ShellCheck, and locked Rust 1.78 check/tests. Golden
remained 11/11 and both protected artifact hashes remained exact.

**A6 is complete (measured 2026-07-24).** `./run version-check` now
reconciles the newest `CHANGELOG.md` release heading with the Rust package,
Python package, FastAPI literal, and `STATE.md` header. It also reads
`git describe --tags --abbrev=0`: an exact HEAD tag must match the package,
while the normal ahead-of-tag development state is an explicit warning rather
than a failure. The configured CI shell checkout uses full history so a future
runner would receive tags; no runner execution had occurred at that release
measurement. v0.10/G2 later pushed the unchanged tag and observed the first
runner execution. A changelog-only
`v0.8.1` plant exited 1 and named
`CHANGELOG.md`; a disposable scratch branch with exact tag `v0.8.1` exited 1
and named the tag/package mismatch. After restoration, the current mid-cycle
tree warned that HEAD is ahead of `v0.8.0` and passed at 0.8.0; a detached
scratch checkout of exact tag `v0.8.0` also passed under Python 3.11.4.
`./run test` passed 98 workspace, 20 net, and 88 shell tests; floor
byte-compilation, Bash syntax, and ShellCheck passed. Golden remained 11/11
and protected artifacts remained 2/2 exact.

**D1 is complete (measured 2026-07-24).** HC9 now has identical ownership-scope
wording and the same three-item SQLite list in `AGENTS.md` and
`ARCHITECTURE.md`: atomic JSON is the default for shell-owned configuration;
subscriptions may explicitly use SQLite for transactional business changes;
the core archive's document/vector/signal tables are SQLite by design; and
harvest cursors live there so page data and continuation state commit
atomically. This is a scope clarification of the implemented rule, not
permission for unrecorded persistence. The closed `TASKS-v0.8.md` body was not
rewritten: `git diff --numstat` measured 9 additions and 0 deletions for its
dated status banner, which supersedes the stale T4, HC1, and 12-document live
claims while preserving their rationale. `AGENTS.md` now describes clippy as
blocking and the golden as eleven checks; the v0.8.1 runbook now counts ten
steps. The live-claim grep initially demonstrated that its literal criterion
matched its own runbook text; the criterion now explicitly excludes that
self-reference and the preserved closed rationale, and the corrected
case-insensitive command produced no output. Golden remained 11/11,
`version-check` passed at 0.8.0 with the expected ahead-of-tag warning, and
both protected artifacts remained exact.

**D2 is complete (measured 2026-07-24).** The progress log's earlier audit
count was itself stale after this cycle's new entries: immediately before D2 it
contained 38 dated entries and 38 commit fields, with zero hash-only values;
36 were narrative and the two containing `097b017` / `2b036d9` also contained
prose. Its recorded event order also places T4 closure at line 654 before the
T4P implementation at 676 and an earlier gate event at 713. History remains
unchanged; the correction is a new entry. `tools/progress_check.py` now
validates the newest entry's ISO header, owner, nondecreasing date, and real
7–40 character Git commit, and `./run test` executes it. An invalid narrative
commit and a backwards date each exited 1 with the offending line named. The
original amend suggestion was rejected because content containing its own hash
changes that hash; the executable protocol is an implementation commit followed
by an append-only audit-record commit naming the real implementation hash.
Implementation commit `5a3f3f8` is recorded in the newest entry, which passes
the checker. The integrated test run passed 98 workspace, 20 net, and 88 shell
tests; golden remained 11/11 and both protected hashes remained exact.

**C2 is complete on the operator-selected local-only path (measured
2026-07-24).** At that measurement, `git remote -v` produced no output and no
CI runner execution had been observed; v0.10/G2 later superseded that absence.
`./run ci-local` now stops at the first failure and prints a
per-job summary. Its observed clean run passed all **16/16** ordered jobs:
release version consistency; Python 3.11 floor byte-compilation; ShellCheck
presence/version/lint; warning-denied workspace check/test; warning-denied net
check/test; clippy; rustfmt; locked Rust 1.78 check/test; 88 shell tests; golden
E2E; protected artifacts; persisted fingerprints; and progress-record
validation. The failure-capable control added a temporary PEP 701 f-string:
Python 3.12 accepted it, then the local matrix stopped at the Python 3.11 job
with `SyntaxError: f-string: unmatched '{'` and reported the preceding version
job PASS and the floor job FAIL. The control was removed before the clean run.
ShellCheck was found at `/opt/homebrew/bin/shellcheck`, reported version
**0.11.0**, and passed; the configured shell workflow now also asserts its
presence and prints its version before linting. Golden remained 11/11. Both
protected hashes remained exact, the fingerprint fixture reported zero NULLs
and mismatches, and progress validation passed against D2 implementation commit
`5a3f3f8`. `.github/workflows/ci.yml` is therefore configured; the measured
enforcement is local `./run ci-local`, never a CI runner.

**R1 release decision (2026-07-24): cut v0.8.0.** The operator selected option
(b). Harvest durability, public-path HC1 enforcement, and persisted fingerprint
identity materially change the shipped artifact, so keeping the runtime at
v0.7.4 would make deployed evidence ambiguous. The Rust package, Python package,
FastAPI surface, and this header therefore advance together and are checked by
`./run version-check`.

**R1 is complete (measured 2026-07-24).** `./run version-check` reports
v0.8.0 from `apps/cored/Cargo.toml`, `shell/intel_shell/__init__.py`, the
FastAPI `version=` literal, and this header; it is blocking in `./run test` and
configured as blocking in `.github/workflows/ci.yml`, which had not been
executed by a CI runner at R1; v0.10/G2 later captured the first execution. Its
failure-capable control changed only the Python `__version__` to
0.8.1: the command exited 1 and named
`shell/intel_shell/__init__.py: 0.8.1` as disagreeing with the Rust package,
then passed again after byte-for-byte restoration. `Cargo.lock` changed only
the local `cored` package metadata from 0.7.4 to 0.8.0, and Cargo built that
locked package on both the pinned toolchain and Rust 1.78.0. The full matrix
passed: 92 workspace tests, 20 net tests, 88 shell tests, warning-denied
offline/net checks, clippy, fmt, Python compile, shell syntax, and locked Rust
1.78 check/tests. The first sandboxed golden attempt could not bind loopback
port 8788 and made no assertions; the permitted rerun passed all 11/11 golden
checks. Both protected artifact hashes remained exact.

**C1 is complete (measured 2026-07-24).** Python **3.11.4** is now the
documented shell/harness floor. `.github/workflows/ci.yml` configures a blocking
3.11/3.12 shell matrix; none had run at C1, and v0.10/G2 later observed both
lanes on the first real runner execution. Its floor
lane is configured to byte-compile every Python file under `tools/` and
`shell/` with `python3.11 -m py_compile` and runs ShellCheck over `run`. The
failure-capable control planted a PEP 701 f-string in
`tools/version_check.py`: Python **3.12.13** compiled it, while Python 3.11.4
exited 1 with `SyntaxError: f-string: unmatched '{'`; the line was removed and
both complete trees then compiled cleanly. Both interpreter lanes passed all
88 shell tests. A preliminary local 3.12 invocation omitted
`PYTHONPATH=shell` and failed during collection without exercising tests; the
CI-shaped rerun included that environment and passed, and only that run is
counted. ShellCheck **0.11.0** initially reported two unused poll counters, one
ambiguous empty assignment, two redundant same-command environment
assignments, and the intentional `CORE_CONFIG` subshell scope. The real
findings were fixed; the two scope diagnostics have narrow, reasoned
`SC2030`/`SC2031` disables. `shellcheck ./run` and `bash -n run` now exit 0.
The full Rust/shell matrix passed, golden remained 11/11, and both protected
artifact hashes remained exact.

**The v0.9 execution runbook is drafted, not executed (2026-07-24).**
`TASKS-v0.9-EXECUTION.md` opens with a fresh B0 and six ordered,
decision-gated tasks: baseline verification, one executable evidence-provenance
manifest, a reproducible real-provider wire probe, a disposable 1,764-row
`/view` cold/warm benchmark against a predeclared SLO, an audit of every
deferred trigger, and an explicit release close. It adds no ingestion source or
subscriber-facing surface. T7 single-flight, Postgres, pgvector, multi-host
UDS/mTLS, and `/view` materialization remain deferred under their unchanged
triggers; the runbook permits measurement or promotion to a future design task,
not implementation around a gate. Draft verification passed the full matrix:
92 workspace tests, 20 net tests, 88 shell tests under Python 3.11.4 and
3.12.13, warning-denied offline/net checks, clippy, fmt, ShellCheck, floor
byte-compilation, and locked Rust 1.78 check/tests. Golden remained 11/11 and
both protected hashes remained exact.

**v0.7.4 acts on a detailed third-party (Codex) review that found the real root cause of the failed on-site harvest — plus three orchestration bugs and one test-isolation bug, all mine, all now fixed.** The 34-minute silence was *not* a long harvest and *not* the harvest logic; it was the `run` harness failing against an environment condition and then hanging on a control-flow bug:

- **Root cause — a foreign process owned the port.** An orphaned `cored` from another copy of the repo (in the operator's `.Trash`) was still listening on 8788. This checkout's server failed to bind (`Address already in use`) and died.
- **Harness bug 1 — false readiness.** The readiness poll hit `/health` and got a 200 *from the orphan*, so it announced our server ready when ours had died. **Fixed:** `_start_cored` now (a) refuses up front if the port is already serving (`port_is_foreign`), naming the offending PID and the exact `lsof`/`kill` commands, and (b) waits with a **pid-aware** check that fails fast if the process we launched dies.
- **Harness bug 2 — infinite poll under `set -e`.** The ingest ran in a backgrounded subshell that wrote a completion sentinel *after* `curl`; when `curl` timed out non-zero, `set -e` aborted the subshell before the sentinel was written, and the watch loop span forever (~29 of the 34 minutes). **Fixed:** the subshell runs `set +e` and **always** writes the sentinel with curl's exit code; the watch loop is additionally time-bounded.
- **Harness bug 3 — `down` can't reach the orphan.** A pidfile only tracks servers we started. **Fixed:** `cmd_down` now reports a still-held port after cleanup, with the PID and kill command. (Also: `_start_mock_llm` still used `setsid`; switched to `nohup` — another latent macOS break.)
- **Test-isolation bug — parallel temp-DB collision.** `tmp_db()` named the per-test SQLite file from `SystemTime` nanos only; two parallel test threads in the same tick got the same path and clobbered each other (seen as a "fresh" DB already holding another test's rows — `new=4, fetched=7`). **Fixed:** a process-global atomic counter + pid in the name guarantees a distinct path per call. `cargo test` is now deterministic under default parallelism (verified across repeated runs).

**On the "0 warnings" claim — B0 correction and T6 resolution, measured 2026-07-20.** "0 warnings" originally meant *rustc* warnings (`-D warnings` on `cargo check`), and that remains true. B0 proved the prior claim that the test module had been moved last was **false**: clippy exited 101 on `clippy::items_after_test_module`, and fmt found diffs in 13 Rust files. T6 moved the SQLite vector layer before the test module and applied rustfmt in the separate lint-fix commit `097b017`. After that fix, `cargo clippy --workspace --locked --all-targets -- -D warnings` and `cargo fmt --all -- --check` both exit 0. The two `clippy::unnecessary_map_or` crate-level allows remain deliberate in `intel-compliance` and `arxiv_oai`: the suggested `Option::is_none_or` is Rust 1.82+, above the offline 1.78 floor. The workflow configures lint as blocking (`continue-on-error: false`); v0.10/G2 first observed that runner job pass.

**T2 interruption-resume is complete on the live wire (2026-07-23).** The original 2026-07-20 capped run cleared its token because `complete()` ran after the cap. A strengthened fake reproduced that failure before the repair; injected commit and SQLite-trigger failures then proved the atomic page guard can fail and rolls documents and cursor back together. On 2026-07-23, live run 1 fetched 1,300 real arXiv records and durably stored token `verb%3DListRecords%26metadataPrefix%3Doai_dc%26from%3D2026-07-21%26until%3D2026-07-22%26set%3Dcs%26skip%3D522`. After stopping and restarting `cored`, live run 2's first request carried that exact token and added the next 1,300 records; its next token advanced to `from%3D2026-07-22...skip%3D88`. Both runs reported `ok=true`, 0 parse errors, and a real `Unavailable(allow)` robots disposition with 0.500s effective crawl delay. No 503/Retry-After was observed. `data/core.db` remained byte-identical.

**T4 real-model verification remains DEFERRED at its embedding gate (updated 2026-07-23).** The operator first exercised two chat candidates as shared providers: the LAN server returned **501 Not Implemented** from `POST /v1/embeddings`, DeepSeek returned **404 Not Found**, and a later Codex LAN retry failed with **No route to host**. After T4C split the roles, the operator configured DMXAPI embeddings and ran the isolated verifier twice. Both runs ingested 13 fresh fixtures; both DMXAPI calls returned **503 Service Unavailable**, so embedding backfill and hybrid fusion failed. The first run nevertheless completed the independent LAN-chat/public-HC1 leg: `/v1/ask` returned 4 citations, all 4 cited documents were IndexOnly, and no 16-token gated overlap escaped. The verifier correctly summarized **3/5 required checks passed**, which is partial evidence, not T4 completion. The second run repeated the 503s and then stalled in chat until the operator interrupted it after 1m41s, exposing a separate verifier fail-fast/timeout defect. A fresh Codex one-vector probe independently reproduced the DMXAPI 503. T4C's deterministic mock control remains harness evidence only; it is not substituted for the failed real embedding role.

**Protected archive correction (measured before and after T4C on 2026-07-23).** Between the T2 handoff and T4C preflight, the operator reported running a bare zero-document arXiv harvest against `data/core.db`. Direct measurement found the logical corpus unchanged at **1,764 rows, 0 NULL `simhash`, 0 NULL `canonical_id`, integrity `ok`**, but the file was no longer byte-identical: SHA-256 is now `db2f186e291c64192e567c9dfb979dd9877eb32b13c2ce2724a4acf1761a37a0`, size **6,729,728 bytes**, mtime `2026-07-23 20:08:13 +0800`, and the `arxiv-cs` cursor row is `cursor=NULL`, `high_water=2026-07-20`, `pending_high_water=NULL`, `updated_at=2026-07-23 12:08:13`. T4C made no further change to that file; its golden and verifier runs used temporary databases. Bare future harvests now resolve to `data/live-smoke.db`.

**Prior point releases (unchanged, kept for the record):** v0.7.1 per-source robots opt-in (§2.12); v0.7.2 `max_pages` cap + timeouts + progress logging; v0.7.3 removed Python 3.12-only f-strings from `run` (crashed on the on-site 3.11).

1. **arXiv migrated its OAI-PMH endpoint.** `export.arxiv.org/oai2` now **301-redirects** to `oaipmh.arxiv.org/oai` (observed live). `config/core.json` now points at the canonical host directly, which also sidesteps the redirect-origin gap (below) for arXiv specifically.
2. **The harvest was blocked by a robots FALSE POSITIVE, not by the gate working correctly.** `oaipmh.arxiv.org` serves no `robots.txt` (a 404 HTML page). The v0.7 default is fail-closed on 404 (`MissingPolicy::Deny`), which is correct for an *unknown* host but wrong for a cooperative, operator-configured endpoint that publishes no robots.txt *on purpose*. The block was the system refusing exactly the access arXiv built the endpoint to serve. **Fixed in v0.7.1** — see §2.12.
3. **The redirect-origin gap was confirmed live and is now resolved in v0.8/T5.** `export.arxiv.org/oai2` 301s to a different origin whose robots.txt the old automatic redirect path would not have read. Both clients now disable automatic redirects, and document redirects are followed manually only after the next origin passes the full robots gate.

**And a process note that matters more than the code:** the on-site tester, working with a different AI assistant, produced a status report concluding *"T2 is verified... blocked by the system's own high-security policy... performing as designed in a live adversarial environment."* Every clause of that is wrong — T2 fetched nothing, the block was a false positive, and arXiv is the least adversarial source imaginable. It is the exact failure this project was built to resist (**a claimed property that nothing executed**), and it is worth recording that the failure mode is attractive enough that a capable assistant reached for it unprompted. The fix for the class is unchanged: report what the wire actually did, and treat "blocked" as a non-result until documents land.

**What changed in v0.7.1:**
- **Per-source robots policy (§2.12).** A new optional `robots_on_missing` on each source, default `"deny"` (the conservative fail-closed behavior for every existing source), set to `"allow"` for `arxiv-cs`. Opting in reinterprets **only** a 404; it does **not** override an explicit `Disallow` and does **not** touch the unreachable/5xx path, both of which still fail closed. Threaded `SourceCfg → source struct → gate() → RobotsCache::allowed()`. +4 tests (79 total), incl. "opting in still obeys an explicit disallow." **This replaces, correctly, the global `MissingPolicy::Deny → RfcAllowAll` sed the on-site tester tried — which both weakened the gate for all sources and, because the default lives in a `#[default]` attribute and not the literal string, silently did nothing.**
- **`./run` portability fixes** for the on-site box: `setsid` → `nohup` (setsid is not on macOS), and the arXiv reachability probe now **derives its URL from config and follows redirects** (`-L`) instead of hardcoding `export.arxiv.org/oai2`, so an endpoint move can't re-break the check. The harvest step now reports PASS/NOT-VERIFIED from the actual fetched count rather than declaring success on a request that returned zero.

**The theme of v0.7 was "stop trusting fixtures." The theme it *turned into* was "stop trusting our own notes."** Two claims this document made about itself were false, and both were found by building the thing that checks them:

1. **`robots.txt` had never been read.** The gate did correct RFC-9309 path matching against **policy we configured, not policy we fetched** — so "robots-compliant" meant "compliant with a policy we wrote ourselves," which is not a claim worth making. **T2 closes this** (§2.11).
2. **"Rust 1.75 + `--locked` still builds the offline path" (v0.6.2, §5) was FALSE from the moment it was written — and the obvious fix is a trap.** v0.6.2 committed `Cargo.lock` at **format v4**, which cargo *cannot parse* before **1.78**; `cargo +1.75 check --locked` dies at the lockfile, long before it reaches any dependency's MSRV. The claim had simply never been run. T4's MSRV job is what caught it.
   The tempting fix — re-encode the lock as v3 — **does work** (measured: 1.75 builds, 75 tests green, resolution byte-identical). **It is also not stable:** cargo 1.91 rewrites the lock back to v4 the moment it has to modify it, so v3 is a hand-edit that the next `cargo add` silently undoes. *A floor that holds only until someone touches the lock is not a floor.* **So v0.7 declares the floor that is true AND sustainable: offline ≥ 1.78** (measured on 1.75/1.76/1.78/1.91). At v0.7 this was workflow configuration plus local evidence only; v0.10/G2 later observed the Rust 1.78 runner job pass. The lesson generalizes twice over: *the lockfile format is part of the MSRV surface, not just the dependency graph* — and *a claimed property that nothing executes is not a property.* This is the **third** time this project has been bitten by that exact failure (`--features net` unbuilt for two cycles; robots policy never fetched; this).

**What changed in v0.7:**
- **T2 — real `robots.txt` discovery (§2.11).** `RobotsGate::parse()` (a zero-dependency RFC-9309 parser: UA-group selection, `Allow`/`Disallow`, wildcards, `$`, `Crawl-delay`), plus `RobotsCache` — per-origin, TTL'd, bounded, **fail-closed**. `texting_robots` was evaluated and **skipped** (§6b); the hand-rolled parser was then proven equivalent to it across **368 verdicts on 16 robots.txt bodies, 0 divergences**.
- **T4 — CI configuration (`.github/workflows/ci.yml`; no runner evidence at v0.7).** Five jobs were configured: `core` (locked, `-D warnings`), **`net`** (the path that sat broken for two cycles precisely because nothing built it), **`msrv`** (the 1.78 floor; equivalent local execution caught the false claim above), `shell`, and a scheduled **`drift`** reporter. v0.10/G2 later observed the first push run: core, net, MSRV, Python 3.12, and golden passed; Python 3.11 exposed the ShellCheck-version divergence; scheduled drift was skipped.
- **T5 — LSH banding: SKIPPED, and the design note it came from is now corrected (§6c).** Built, measured, rejected. It is 246× *slower* than the scan it replaces.

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
