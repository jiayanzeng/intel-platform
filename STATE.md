# STATE.md — intel-platform handoff

**As of:** 2026-08-03 · **Version:** v0.17.2 (core-shell) · **Status:** **v0.36 is active; A1r2 corrects the two author-side lifecycle contradictions and reopens AUTONOMY under an explicit interim verification path.** v0.17.2 remains closed locally and unpublished; no remote publication is authorized. Release commit `d4258883645a99f9499895bf064e453de9be1281` is the immediate parent of the locally tagged closing record. Authenticated run `30762871542` passed all **9** blocking identities; the pinned release-grade verifier accepted **9/9** signed bundles and asserted receipts bind Rust **1.78.0 / 1.86.0 / 1.85.0**. The patch restores third-party verifiability without route, response-body schema, named-surface shape, dependency resolution, protected database, golden input, entitlement/licensing outcome, or serialized `/v1/*` value-domain movement. The registered suite remains at the last measured **12 rules / 73 controls** with **0** hand-typed absolute finding-line fields; the retraction count remains **3**. Published remote `main` and v0.17.1 remain unchanged unless the operator separately authorizes the exact closing commit and annotated tag.

**v0.36 AUTONOMY stop-and-report (measured 2026-08-03).** The runbook's
pre-activation ordering was attempted first. `ci-local` rejected a v0.36 task
path while v0.35 remained declared and treated the new runbook as an incomplete
older cycle, so the explicit Step 0e exception was taken. Activation landed as
implementation `f44681c1dce0c5c2efc0d3fb4a30900fdb4163f5` with audit record
`8c798cd`. The declared retention set is exactly v0.35–v0.36, and the
permission-complete activation golden run passed **11/11**.

The Step 0 experiment then generalized R6 from its one hard-coded authority
name to the derived union of marker names. Before the Operations mirror was
added, the real scan failed on missing `CYCLE_AUTONOMY_AUTHORITY` START/END
markers. With the exact mirror present, the focused test and full self-test
passed **12/12 rules / 74 controls**, including a planted missing-START control.
Two consecutive artifact checks matched all **332** pins and both protected
databases in **0.12 s / 0.13 s real**; `run` remained exactly **45,409 bytes**
at its authorization-grade hash. Project-root `export-check` passed at
**100 derived / 7 required / 152 exported / 2,724,915 bytes / 2 retained
cycles**, exactly v0.35–v0.36, with both protected byte classes excluded.

The exact acceptance entry point `./run ci-local`, run with normal loopback and
process-inspection permissions, passed release-version consistency and then
stopped at active-cycle consistency with exactly two defects:

1. `AGENTS.md:635: stale/cycle-specific task path
   'TASKS-v0.36-EXECUTION.md' appears outside the active declaration`. The
   runbook simultaneously requires the marker block verbatim, including that
   literal, while the existing `check_contract_cycle_paths` rule rejects every
   cycle-specific task path below AGENTS §0.
2. `STATE.md: publication post-push record required: expected exactly one
   complete record for v0.17.2; found 0`. Local annotated tag `v0.17.2` points
   at closing commit `9996c6820d720160b64607575d0270d2e5393ef9`; activation makes
   HEAD its descendant, so the current R-CLOSE checker requires the record that
   the contract defines as post-publication. The tag is explicitly unpublished,
   no hosted publication run exists, and publication is the runbook's retained
   ask-first gate.

This is the runbook's stop-and-report condition for an instruction that cannot
be executed without violating another instruction. No post-push record was
fabricated, the local release tag was not deleted, publication was not
performed, the verbatim block was not weakened, and the scope-forbidden
`tools/cycle_check.py` was not changed. The unaccepted Step 0 implementation
was restored; its checkbox remains open. The restored standing self-test passes
**12/12 rules / 73 controls**, manifest schema validation passes for **2
artifacts / 332 pinned files**, and the post-restore golden pipeline passes
**11/11** with zero delta. The operator-supplied amendment remains untracked
and untouched. Because the runbook says everything requires Step 0 complete,
E0 and Steps 2–7 were not started.

**v0.36 A1r2 author-side correction (measured 2026-08-03).** Amendment
application commit `6a3c108dd19378549a503c220c8917c7b34055ea` changes only the
active runbook. It replaces the stale cycle-specific authority text, adds
Step 1A's truthful unpublished-local-close lifecycle objective, removes the
forbid-before-allow scope contradictions, records H11–H13, and gates every
later step on Step 1A. The two amendment inputs remain untracked and untouched.

The real post-amendment `cycle-check` now reports exactly the one expected
interim defect: the absent v0.17.2 post-push record. It reports no authority
literal, declared-scope, amendment-disclosure, trigger-freshness, retention, or
artifact-boundary defect. This is the amendment's deliberate A4 state until
Step 1A changes the lifecycle predicate; it is not accepted as a clean close.
The amendment-only golden run passed **11/11** with zero delta. No production
source, protected byte, dependency, tag, or remote ref changed. Corrected Step
0 is therefore reopened and runs next; this forward correction does not alter
the truthful earlier stop-and-report measurement.

**v0.35 R-CLOSE — operator-selected v0.17.2 patch release closed locally
(measured 2026-08-03).** Release disposition: release (as of 2026-08-03).
The operator overrode the declared no-release intent and selected patch
**v0.17.2**. The structural reason is a correctness repair within existing
names and shapes: published v0.17.1's release-grade verifier cannot validate
any bundle under pinned `gh` 2.96.0, while the corrected verifier, explicitly
selected 1.78 / 1.86 / 1.85 floor lanes, and receipt-bound effective toolchain
restore third-party verifiability. No route, response-body schema,
named-surface shape, or serialized `/v1/*` value domain moves, so the public
value-domain rule does not require a minor release.

The untagged release parent is
`d4258883645a99f9499895bf064e453de9be1281`, tree object
`c2ab865cf9a6cbb685554568ddf9d94354747784`. `version-check` derives
**0.17.2** from `apps/cored/Cargo.toml`,
`shell/intel_shell/__init__.py`, `shell/intel_shell/app.py`, `STATE.md`,
and `CHANGELOG.md`; it reports **3** executable offline-MSRV pins at raw
`[1.78.0]`, **22** current offline-MSRV restatements deriving 1.78, and **3**
release-version current restatements deriving 0.17.2. The lockfile movement is
only `cored 0.17.1 → 0.17.2`; it was generated by Cargo and was neither
deleted nor format-edited.

Accepted evidence is anchored to candidate
`2e5b247e348f362b1cc3fa6a9aaa393d0025fc87`, ref
`codex/v0.35-evidence-2e5b247`, and run **30762871542**, attempt 1. The
strict pinned verifier accepted **9**, rejected **0**, and independently
matched the expected workflow certificate identity per bundle. Its temporary
canonical report rehashes to **41,042 bytes**, SHA-256
`dac7de5243968096ef49049ab2b400fdb6d489a8fa17091b0654fd5d3e9858d4`.
The three receipt assertions remain exact at **1.78.0 / 1.86.0 / 1.85.0**.
The report and hosted artifacts remain outside the repository and manifest.

The release-parent project-root export passes **100 derived / 7 required / 152
exported / 2,742,486 bytes / 2 retained cycles**, exactly v0.34–v0.35, with
both protected byte classes excluded. The closing progress field binds that
figure as
`tree=d4258883645a99f9499895bf064e453de9be1281`. v0.34 proves that
`tree=` stores the **commit object**: its governed value
`1117dc6db6ec0e55e8c8f078ca8059628f9f8262` is Git type `commit`, while
its distinct tree object is `05ef0cce218ce03a69a07558c5ce25edf7d8331f`.
The latest adjacent-cycle governed delta is therefore **+215,306 bytes** from
v0.34's 2,527,180 to this 2,742,486. The **257,514-byte / 8.58%** remainder is
**1.20 cycles**, with the checker retaining its one-pair representativeness and
unobserved-structural-epoch bounds.

Immediately before the closing record, State measured **298,251 / 453,741
bytes**, leaving **155,490 bytes / 3.70 cycles** against the adjacent
same-kind v0.34 delivered-State basis of **42,033 bytes/cycle**. The unchanged
manifest measured **193,057 / 1,048,576 bytes**, leaving **855,519 bytes /
842.88 cycles** at **1,015 bytes/cycle**. Export at **1.20 cycles** is the
nearest governed byte boundary. Manifest schema validation and two complete
checks matched all **332** pins, the structural State archive, and both
protected databases in **0.11 s / 0.10 s real**. Neither byte nor timing trigger
fired.

All active deferral rows carry fresh v0.35 / 2026-08-03 observations. The
planted-control line-number subject is closed into Deferred completions:
activation had **0** `expected_anchor` values and close has **73**, so **73**
anchor values changed relative to activation; all 73 derive against a unique
constructed mutant, the real self-test passes **12/12 rules / 73 controls**,
and **0** hand-typed `expected_line` or other absolute finding-line fields
survive. The broad `app.py` trigger fired only for its declared release
literal; the package-owned-literal structural option remains deferred.

Published v0.17.1 reset the publication-epoch divergence count to zero. The
v0.17.2 distance contains verifier/toolchain evidence correction, release
literals, and lifecycle records but no measured runtime-behaviour or
public-surface change, so the count remains **0**. The local tagged close
publishes nothing; separately authorized publication of its exact closing
commit will reset and retain the count at zero.

The release close used release authorities `Cargo.lock`,
`apps/cored/Cargo.toml`, `shell/intel_shell/__init__.py`,
`shell/intel_shell/app.py`, `CHANGELOG.md`, and `README.md`. Root
`Cargo.toml`, every `crates/*/Cargo.toml`, and other app manifests are
unused authorities. The `app.py` diff is exactly the version literal admitted
by release-authority precedence. Every other production source, dependency,
schema, publisher/scheduler configuration, observation, fixture, protected
byte, historical cycle document, and historical ref remains unchanged. The
operator-supplied amendment file remains untracked and untouched.

The release-path cycle-ending export audit and dated post-push identity belong
to the first append after an authorized atomic publication, because neither
the annotated tag object nor closing-commit identity can exist inside the
closing tree. No value is predicted or fabricated locally. The closing child
cannot claim a post-commit command whose exact identity does not exist inside
its own tree. That complete entry point and standalone golden are measured
after the local commit/tag construction and reported at handoff; publication
of `main` and `v0.17.2` remains a separate exact authorization.



**v0.35 Step 5a pre-implementation MSRV measurement gate (measured
2026-08-02).** The operator-supplied r4 prompt required all three affected
jobs to be measured at the real entry point before implementation. Existing
workflow-dispatch run **30746841903**, attempt **1**, provides that measurement:

- `msrv` declared action input **1.78**. The action installed it and set it as
  the rustup default, then logged that `1.91-x86_64-unknown-linux-gnu` was
  `currently in use (overridden by .../rust-toolchain.toml)`. The job invoked
  bare `cargo check --workspace --locked` and bare `cargo test --workspace
  --locked`; both completed successfully under the active 1.91 override. The
  hosted 1.78 floor lane therefore did not execute 1.78 in this run.
- `net-msrv-1-86` declared action input **1.86.0**, emitted the same active-1.91
  override note, invoked bare package-scoped cargo, and passed. Its green is a
  **non-result** for the 1.86 floor.
- `net-msrv-1-85` declared action input **1.85.0**, emitted the same active-1.91
  override note, invoked bare package-scoped cargo, and compiled successfully;
  its wrapper then failed because it expected a declared-MSRV refusal. It is a
  measured failed lane and a **non-result** for the 1.85 floor.

This fires Step 5a decision-gate clause 4. Work stopped before classification
or correction. No inference is made here about whether a published record is
false, no retraction is proposed, and the existing `STATE.md` v0.10/G2
hosted-1.78 sentence is byte-unchanged. The locally explicit Rust 1.78 lane
remains valid local evidence and is not falsified by this hosted measurement.
Amendment r4 is recorded in the active runbook, but no selection, proof, R10,
planted-control, pin, or `AGENTS.md` implementation is permitted until the
operator adjudicates the measured 1.78 evidence history. Step 5 stays unboxed;
Step 6 and Step 7 remain ineligible and unauthorized.

**v0.35 Step 5A operator classification and derived historical boundary
(ruled and measured 2026-08-02).** The operator's classification is
**UNVERIFIABLE, not false**. There is no retraction; the repository retraction
count remains **3**. Git history derives commit
`6005a19878d72518e2f982b5859d68520a4a9503` (`feat: first commit`,
2026-07-20) as the commit that introduced `.github/workflows/ci.yml` and its
hosted `msrv` `toolchain: "1.78"` input plus unqualified cargo check/test form.
Every hosted `msrv` execution of that form from `6005a198…` through failed-
evidence candidate `d33c251d477aa4b1ee6b5b2ebd531b1fda428e99` is classified
as **NOT a measurement of 1.78** — a non-result. The offline 1.78 floor claim
survives on the explicit local `rustup run 1.78.0` evidence; only its hosted
attestation is void.

Operator rationale, recorded verbatim:

- One measurement exists (run 30746841903), and it is of the CURRENT workflow.
  No measurement of the v0.10/G2 run exists or can be obtained: its logs are
  past retention and the receipt schema carries no toolchain field.
- Unverifiable is not false. STATE.md:3634 is NOT edited.
- The 1.78 offline floor itself remains TRUE on local explicit
  `rustup run 1.78.0` evidence, which the override never touched.

The retention and receipt-schema limits are therefore part of the
classification: historical logs have expired, and historical receipts cannot
answer which Rust release executed because they record no toolchain field.
This is not a judgment that the unmeasurable v0.10/G2 run used the wrong
toolchain. Its existing sentence is unchanged. The operator authorized local
Step 5A implementation after this ruling, including new A13 receipt field
`rustc_release`; push, hosted dispatch, failed-ref movement, retraction, Step 6,
and Step 7 remain unauthorized.

**v0.35 Step 5A NET-FLOOR-CORRECTION local completion (measured
2026-08-02).** The before measurement remains hosted run **30746841903**:
all three named floor jobs executed Rust 1.91 and are non-results for their
named floors. The corrected local entry points printed and asserted their
effective Cargo and rustc releases. Explicit Rust **1.78.0** completed the
offline workspace check and test; explicit Rust **1.86.0** completed the
`cored --features net` check; explicit Rust **1.85.0** exited nonzero because
the locked `idna_adapter` and ICU packages declare `rust-version = 1.86`.
The corrected hosted commands have not run and make no hosted claim.

All three workflow jobs — `msrv`, `net-msrv-1-86`, and `net-msrv-1-85` — now
invoke `rustup run <version> cargo`, emit `cargo -V` and `rustc -vV`, and fail
if either release differs from the declared one. Their matching `run` lanes do
the same. `AGENTS.md` now states that an action `toolchain:` input is only an
installation/default request beneath a repository override and cannot itself
prove a floor lane. R10 identities carry the effective toolchain, producing
local **22 jobs / 30 checks**, hosted **8 blocking jobs / 29 checks**, and
**59** derived local-only exemptions. Its three new executable mutations emit:

- `.github/workflows/ci.yml:182: hosted job net-msrv-1-86 runs unqualified cargo under shadowed toolchain input 1.86.0; rust-toolchain.toml selects 1.91`
- `.github/workflows/ci.yml:139: blocking hosted floor lane 'net-msrv-1-86' selects 1.85.0 without an effective cargo/rustc version proof`
- `.github/workflows/ci.yml:139: blocking hosted floor lane 'net-msrv-1-86' selects 1.86.0 without an effective cargo/rustc version proof`

The registered self-test passed **12 rules / 72 controls** and the registry
contains zero absolute `expected_line` fields. No lane, decision gate,
exemption, or R10 classification was relaxed. Before and after Step 5A,
`version-check` independently reported **3** pins, **22** offline-MSRV current
restatements, and **3** release-version current restatements. New registry
floor literals are classified as control constructions; no version authority
moved.

A13 adds numeric `rustc_release` to all **9** CI-runner receipt emitters and
requires it in current receipt verification. Missing, empty, or non-numeric
values are rejected. The shell population moved **358 → 361** for exactly
these three nodes:

- `tests/test_deferred_audit.py::test_current_receipt_requires_numeric_rustc_release[None-missing/invalid fields: rustc_release]`
- `tests/test_deferred_audit.py::test_current_receipt_requires_numeric_rustc_release[1.91-rustc_release is not a numeric Rust release]`
- `tests/test_invariant_scan.py::test_r10_cargo_identity_carries_the_explicit_toolchain`

The accepted-runner assertion remains **9** and the expected receipt and
Sigstore-bundle populations remain **9 / 9**; A13 moved no deferred-audit
runner cardinality or bundle expectation. The workflow is **39,175 bytes**,
SHA-256
`600b194980231e80cce4a05a14ca043ac6a0b1adbafed747cd78b2fcdf50bd09`.

Protected-artifact validation and complete byte verification pass with exactly
the existing `run` pin updated: **44,795 bytes**, SHA-256
`1f87371243698cb60fb24c07b21caf8ce7a86f927a46443b0b89f71de978ad7b`.
The manifest is **192,703 bytes**, SHA-256
`6407d619f3f93b9d11e52b8c2de2f28ce0621ea1bcc425a8e39a8913b85dd65d`,
with **332** pins, **2** artifacts, and **2** admissions.
`tools/model_profiles.py` remains **28,297 bytes**, SHA-256
`1920761c97ffa6fc7b5242c16384fb6f1b0727937f9e1cfd7e00826c913554df`;
both protected databases and every admission record are byte-identical.

The authoritative local gate passed **22/22**, checklist
**268 / 3 / 268 / 268**, zero rustc and clippy warnings, embedded golden
**11/11**, and constrained shell **361/361**. Clean Python 3.11.4 and 3.12.13
rebuilds each resolved the same 21 packages and passed **361/361**; the
machine comparator derived `equivalent=true`, `equivalent_passed=361`, and no
skips. The mandatory standalone golden passed **11/11**, delta **0**. A first
sandboxed package install and a first sandboxed standalone golden were
permission/network non-results; their authorized reruns produced the stated
measurements. No push, hosted dispatch, remote-ref change, or acceptance of
run 30746841903 occurred. Step 6 remains a separate decision on one exact
candidate SHA and one new ref.

**v0.35 Step 6 first authorized attempt and installer-name correction
(measured 2026-08-02).** The operator authorized exact candidate
`7a444235dab5905bff6cc90a61815e31690c3a35` and fresh ref
`refs/heads/codex/v0.35-evidence-7a44423`. The ref did not exist before the
push, was pushed once, and immediate and final readback both resolved it to
that exact candidate. Workflow-dispatch run **30754728135**, attempt **1**,
authenticated the same `event_sha`, `sha`, and ref. Eight of nine blocking
identities passed: core, net, golden, lint, Python 3.11, Python 3.12, the Rust
1.86 net success, and the Rust 1.85 declared-MSRV refutation. The offline
`msrv` identity failed before either cargo command executed.

The failed proof is a construction non-result. The action input installed the
rustup name `1.78`, while the proof invoked `rustup run 1.78.0`; rustup emitted
`toolchain '1.78.0-x86_64-unknown-linux-gnu' is not installed` and stopped.
The always-run receipt recorded `conclusion=failure` and the effective fallback
`rustc_release=1.91.1`, so A13 makes the construction answerable from retained
repository-shaped evidence. All nine receipt/bundle artifacts were downloaded
and inspected locally; none was accepted as release-grade evidence. Run
**30754728135** and ref `codex/v0.35-evidence-7a44423` are immutable non-results,
just like run **30746841903** and ref `codex/v0.35-evidence-d33c251`.

The local correction changes only the offline job's action input from `1.78`
to the exact selector name `1.78.0`. R10 now rejects any explicit hosted floor
selector whose action-installed toolchain name is not exactly identical; its
seventh reconstructible control changes `1.78.0` back to `1.78` and emits
`blocking hosted floor lane 'msrv' selects toolchain 1.78.0 but action installs
1.78`. The registered self-test passes **12 rules / 73 controls**, still with
zero absolute `expected_line` fields. No gate, lane, exemption, blocking
identity, or R10 classification was relaxed. The local/hosted topology remains
**22 jobs / 30 checks**, **8 blocking jobs / 29 checks**, **59** derived
local-only exemptions, and **9** total blocking identities. Receipt emitters,
accepted-runner assertions, deferred-audit runner populations, and receipt /
bundle expectations remain **9**, **9**, **9**, and **9 / 9** respectively;
the correction moves none of them.

`version-check` measured **3** executable pins before and after the correction.
The raw authority set changed from `[1.78, 1.78.0]` to `[1.78.0]`, while both
trees normalize to offline floor **1.78** and report **22** offline-MSRV plus
**3** release-version current restatements. The workflow is now **39,177
bytes**, SHA-256
`4ebf2c2193fe3fb11e7710b20c1c000fd073103656dc0b155bce945b57bff871`.
The invariant registry is **64,886 bytes**, SHA-256
`27377b5b6326dc92be5cdba7726ce9d559dcc3076b9e653a3a230625ba7e1f3e`.

The corrected authoritative local gate passed all **22/22** jobs: explicit
Rust 1.78 offline check/test, Rust 1.86 net success, Rust 1.85 declared-MSRV
refutation, zero rustc/clippy warnings, checklist **268 / 3 / 268 / 268**,
constrained Python 3.11.4 **361/361**, embedded golden **11/11**, all protected
pins, and both protected databases. Clean Python 3.11.4 and 3.12.13 rebuilds
each resolved **21** constrained packages and passed **361/361**; the
machine-readable comparator derived `equivalent=true`, `collected=361`,
`equivalent_passed=361`, and zero skips. The mandatory standalone golden passed
the same **11/11** assertions, delta **0**. A sandbox-only first 3.11 execution
could not bind eight loopback test servers and is a permission non-result; the
permitted clean rerun produced the stated result. No corrected-candidate push
or hosted dispatch occurred. A fresh exact candidate and fresh ref require a
separate operator authorization before Step 6 can resume.

**v0.35 Step 6 second authorized attempt — hosted checks green, release-grade
attestation verification a construction non-result (measured 2026-08-03).**
The operator authorized exact candidate
`8fae40e78afee6df80133f89bbbac4a074179ff5` and only fresh ref
`refs/heads/codex/v0.35-evidence-8fae40e`. A new pre-push `git ls-remote`
exited **0** with no entry. One non-force push created the ref; immediate and
final direct readback each resolved it to the exact candidate. The candidate
tree is `06925e82b10e6706d38a9120e642898c06c25799`; its tracked worktree was
clean, with only the operator-supplied amendment untracked.

Workflow-dispatch run **30757027882**, attempt **1**, authenticated event
`workflow_dispatch`, the exact SHA/ref, and completed with `conclusion=success`.
All **9** blocking identities passed, including explicit Rust **1.78.0**
offline proof/check/test, explicit Rust **1.86.0** net proof/success, explicit
Rust **1.85.0** proof/declared-MSRV refutation, core, net, lint, golden, and
both shell jobs. The report-only dependency-drift job was structurally skipped.
The workflow is intentionally changed this cycle and remains **39,177 bytes**,
SHA-256
`4ebf2c2193fe3fb11e7710b20c1c000fd073103656dc0b155bce945b57bff871`.

Exactly **9** receipts and **9** Sigstore bundles were downloaded. Executed
`jq -e` assertions, not inspection, required and obtained these exact pairs:
`msrv=1.78.0`, `net-msrv-1-86=1.86.0`, and
`net-msrv-1-85=1.85.0`. The other six receipts record `rustc_release=1.91.1`.
Every receipt records `conclusion=success`, event and checkout SHA equal to the
exact candidate, repository `jiayanzeng/intel-platform`, workflow `CI`, and a
Linux runner.

The required production release-grade verifier then ran once from a clean
detached worktree at the exact candidate, with attestations required and exact
repository, workflow path, signer/source digest, source ref, and hosted-runner
requirements. It accepted **0** and rejected **9**. Every rejection reason was
`GitHub attestation verification failed: Error: verifying with issuer
"sigstore.dev"`; the derived matrix consequently reported all nine identities
missing. This is an attestation-verification construction failure, not a
judgment about the passed jobs or toolchain properties. The generated
non-release-grade audit report is **32,751 bytes**, SHA-256
`3d1593ace65bc76fc72bd041a8cf3a1106c013bffba23808176bf0cbe1968b94`,
and remains operator-local under `/private/tmp`; it is not repository evidence.

The operator's stop condition therefore fired. The verifier was not retried;
no receipt or bundle was accepted as release-grade evidence, and the governed
export, release-grade shell-population comparison, protected-artifact timing
record, and governed progress field were **not measured**. Those are
non-results, not passes. Mandatory local record checks passed: `cycle-check`,
`version-check`, `checklist-audit` at **268 / 3 / 268 / 268**, diff hygiene,
and standalone golden **11/11**, delta **0**. Step 6 remains unchecked and
Step 7 was not entered. No gate, lane, exemption, blocking identity, or R10
classification was relaxed.

Final direct remote readback fixed the three evidence refs at their exact
candidates, kept `main` and peeled `v0.17.1` at
`f02379f03ccdfd1b019413234f2ad014d169fb04`, and kept annotated tag object
`14912f134e45277e2b4fd10b7f5bf8b4900ca20d`. Runs **30746841903**,
**30754728135**, and **30757027882** and their refs are immutable non-results.
No receipt or bundle from any of them is release-grade evidence.

**v0.35 Step 6 attestation-verifier diagnosis — classification (a), verifier /
environment fault (measured 2026-08-03).** The decisive same-host control used
the currently installed `gh version 2.96.0 (2026-07-02)` to reverify the known-
good v0.34 **7-receipt / 7-bundle** set at authenticated candidate
`1117dc6db6ec0e55e8c8f078ca8059628f9f8262` and ref
`refs/heads/codex/v0.34-evidence-1117dc6`. All seven now exit **1**. A
representative historical bundle's complete stderr is the same **45 bytes** as
the current run's representative `msrv` bundle:

```
Error: verifying with issuer "sigstore.dev"
```

Both invocations passed `.github/workflows/ci.yml` as `--signer-workflow`.
For v0.34, `--signer-digest` and `--source-digest` were
`1117dc6db6ec0e55e8c8f078ca8059628f9f8262` and `--source-ref` was
`refs/heads/codex/v0.34-evidence-1117dc6`; for v0.35 they were respectively
`8fae40e78afee6df80133f89bbbac4a074179ff5`, the same candidate digest, and
`refs/heads/codex/v0.35-evidence-8fae40e`. Direct certificate decoding showed
that each set's signer workflow URI, signer digest, source digest, source ref,
repository, and GitHub-hosted runner claim equal the arguments supplied. The
workflow-byte change is intended: v0.34 was **26,967 bytes** / SHA-256
`5a7160f15a9eaa57daa9cc8ce666c1a1c2b8cc39728ea2308474e0d66f2b6791`,
whereas the v0.35 candidate is **39,177 bytes** / SHA-256
`4ebf2c2193fe3fb11e7710b20c1c000fd073103656dc0b155bce945b57bff871`.
`--signer-digest` correctly denotes the workflow's commit digest, not the
workflow file's SHA-256; no stale or wrongly derived verifier argument was
found.

The trust-root control also excludes a stale or expired TUF cache. No Sigstore
TUF override or no-cache environment variable is set;
`gh attestation trusted-root --verify-only` exited **0** with empty stderr.
The refreshed public-good root v15 expires 2026-11-20 and timestamp v744 expires
2026-08-08; the GitHub root v9 expires 2027-01-28, timestamp v922 expires
2026-08-08, and snapshot v75 expires 2026-08-11. All were current at the
2026-08-03 measurement. The original v0.34 successful record did not capture
its then-running `gh --version`, so no historical binary-version claim is
invented; both decisive rechecks used the same current executable.

The historical set's failure selects **(a) verifier/environment fault —
evidence content sound, chain unvalidatable on this host**. It rules out **(b)**
repository argument derivation and **(c)** a signing-side fault specific to run
30757027882. The measured property is proven separately: all **9/9** blocking
identities passed, and executed receipt assertions established
`msrv=1.78.0`, `net-msrv-1-86=1.86.0`, and
`net-msrv-1-85=1.85.0`. Only the attestation chain remains unvalidated. That
separation does not admit any receipt or bundle as release-grade evidence:
Step 6 remains unchecked, run **30757027882** and its ref remain immutable, no
hosted retry or ref mutation occurred, and Step 7 was not entered.

**v0.35 Step 6 attestation-verifier diagnosis — forward correction to
classification (b), repository argument derivation (measured 2026-08-03).**
The preceding classification (a) was premature: applying the same current
wrapper to both bundle sets entangled the wrapper with its external CLI. Three
subsequent controls separate them and supersede that classification without
editing its dated record.

Control 1 bypassed `verify_attestation_bundle` and passed one authenticated
v0.34 bundle's byte-identical contents directly to `gh` 2.96.0 under three
names. Raw `.sigstore` exited **1** with complete stderr `Error: bundle file
extension not supported, must be json or jsonl`; `.sigstore.json` and the
wrapper's `.bundle.jsonl` each reached verification and exited **1** with
complete stderr `Error: verifying with issuer "sigstore.dev"`. Thus the raw
archival suffix is unsupported and the wrapper's extension dependency is real,
but decoder selection did not cause the issuer failure.

Control 2 held the supported `.sigstore.json` input and all other arguments
constant while dropping exactly one strict policy flag at a time. Dropping
`--signer-workflow` alone exited **0**; dropping any one of
`--signer-digest`, `--source-digest`, `--source-ref`, or
`--deny-self-hosted-runners` still exited **1** at the issuer. Restoring every
strict flag while changing only the signer workflow from bare
`.github/workflows/ci.yml` to documented
`jiayanzeng/intel-platform/.github/workflows/ci.yml` exited **0**. The optional
host-qualified `github.com/jiayanzeng/intel-platform/.github/workflows/ci.yml`
also exited **0**. No policy flag was relaxed in either passing confirmation.

Control 3 captured the 2.96.0 help contract. `--repo` requires
`owner/repo`; `--signer-workflow` requires
`[host/]owner/repo/path/to/workflow`; the digest, source-ref, hosted-runner, and
JSON-output flags are accepted as used; and `--bundle` accepts a single JSON
bundle or JSON Lines. The repository's bare signer-workflow value violated that
contract. `gh auth status` exited **0** with the active `jiayanzeng` keyring
account, HTTPS Git operations, and `gist`, `read:org`, `repo`, and `workflow`
scopes; the masked token text is not recorded. Because the controls identify a
repository fault, no older CLI installation was attempted.

The explicit classification is **(b), argument-derivation fault in the
repository**. The old statement that the bare signer-workflow argument matched
the decoded certificate claim was wrong: the certificate names the fully
qualified workflow URI, while current `gh` interprets a bare path as an invalid
signer identity and collapses that mismatch into the issuer error. The current
run is not a signing-side fault, and no verifier/environment classification is
retained.

The durable local correction pins the release-grade verifier to exact `gh`
**2.96.0** and refuses version drift before examining a bundle. It canonicalizes
a repository-relative workflow into the documented owner/repository form,
validates already-qualified forms, parses each persisted `.sigstore` document,
and re-emits canonical single-bundle JSON instead of copying bytes under a
decoder-selecting `.jsonl` suffix. Future audit records include the required and
observed CLI version, canonical bundle input format, and signer-workflow format.
Executable tests prove the version mismatch refusal, workflow qualification,
canonical JSON conversion, and audit-record fields.

The corrected wrapper, given the original bare-path input and every strict
flag, diagnostically verified one v0.34 representative and one run
**30757027882** representative, each returning its exact certificate identity,
signer/source digest, and source ref. Neither result admits a bundle: the
corrected verifier is not in candidate `8fae40e7…`, the complete nine-bundle
release-grade population remains unvalidated, and Step 6 remains unchecked.
The measured property remains separately proven by **9/9** passed hosted
identities and executed receipt assertions for **1.78.0 / 1.86.0 / 1.85.0**.
No push, ref creation or mutation, hosted retry, evidence admission, gate or
verifier-policy relaxation, or Step 7 action occurred.

**v0.35 Step 6 verifier preflight, independent certificate identity, and CLI
history control (measured 2026-08-03).** `./run attestation-preflight` is now a
standing executable prerequisite for any further hosted-evidence run. With no
directory override it downloads immutable accepted run **30726156221**; it
then requires the embedded SHA-256 authorities for all 7 receipts and 7
bundles, the exact accepted receipt/run/repository/commit/job facts, and the
current release verifier with every strict flag. Its source ref is derived from
the historical progress records rather than hard-coded as a cycle literal. The
real preflight over the already-downloaded bytes passed **7/7** on exact `gh`
**2.96.0**.

The positive preflight is paired with a separate executed negative control.
The authenticated historical `msrv` receipt/bundle was submitted with
deliberately wrong workflow
`jiayanzeng/intel-platform/.github/workflows/not-the-accepted-ci.yml`; the
current wrapper rejected it verbatim:

```text
GitHub attestation verification failed: Error: verifying with issuer "sigstore.dev"
```

The positive 7/7 result cannot prove that a verifier still rejects mismatches;
this negative construction does. A planted wrapper regression that forwards
the repository-relative workflow unqualified makes the preflight fail, and a
planted permissive verifier that accepts the wrong workflow makes the negative
control itself fail. Both constructions executed in the focused **47/47**
suite.

`verify_attestation_bundle` now independently constructs the exact expected
certificate SAN as
`https://github.com/{owner}/{repo}/{workflow-path}@{source-ref}` and requires
the verified output to contain exactly that identity. The release-audit call
site separately constructs the same expectation from its repository, workflow,
and source-ref inputs; it no longer copies `certificate_identity` out of the
verifier's return to create its own expected value. The prior mock SAN
`https://example.test/workflow` is now an executed rejection both at the
wrapper boundary and at the release-audit call site.

The exact CLI pin now fails with its admission procedure: update the pin only
after the historical 7/7 preflight, the wrong-signer negative control, and a
dated State/progress decision pass. The active deferral table carries a
trigger-bearing `gh` version/contract row assigned to **Step 6**, so an
auto-update or proposed bump stops as a decision rather than surfacing during
release verification. This changes no hosted identity, receipt, bundle, or
deferred-audit population: their required values remain **9 / 9 / 9**, and the
protected manifest remains **332** pins.

The older-CLI question was measured, not inferred. Git history introduces
`verify_attestation_bundle` at
`2863d42ff31d5c964478bee1420df221d0dbab18` on 2026-07-26. The host's current
2.96.0 executable link predates that commit; the immediately preceding
official GitHub CLI release, **2.95.0 (2026-06-17)**, was downloaded from its
release artifact and its ZIP matched the published SHA-256
`3677f9c27965825f9c7d50395473c134edaea4b484373ef6b25de653570a0489`.
Against the same authenticated historical receipt/bundle and every other
strict flag, 2.95.0 produced these results:

- bare `.github/workflows/ci.yml`: exit **1**, stdout **0 bytes**, stderr **45
  bytes**;
- qualified `jiayanzeng/intel-platform/.github/workflows/ci.yml`: exit **0**,
  stdout **14,694 bytes**, stderr **0 bytes**;
- deliberately wrong qualified workflow: exit **1**, stdout **0 bytes**,
  stderr **45 bytes**.

Both rejecting stderr streams are byte-identical: one leading newline,
`Error: verifying with issuer "sigstore.dev"`, and one trailing newline.
Thus measured 2.95.0 did **not** accept the bare form without matching. All
**20** retained committed audit reports that carry a signer-workflow identity
use the qualified `jiayanzeng/intel-platform/.github/workflows/ci.yml` form.
Repository evidence therefore shows no accepted prior cycle whose workflow
verification was weakened by a bare value; no retraction is proposed and no
historical record was edited.

The complete local entry point passed **22/22**, all **12** invariants and
**73** planted controls, warning-denied Rust lanes, all **332** pins, and
embedded golden **11/11**. Python 3.11.4 and 3.12.13 each passed **366/366**;
`tools/test_population.py` derived `collected=366`, `equivalent=true`, and
`equivalent_passed=366`. The measured hosted property remains separately proven
at **9/9** with asserted **1.78.0 / 1.86.0 / 1.85.0** toolchains. Only the
complete candidate attestation chain remains unvalidated. Step 6 stays
unchecked; no bundle is admitted, and no push, ref creation/mutation, hosted
retry, verifier relaxation, or Step 7 action occurred.

**v0.35 Step 6 RE-MEASURE — exact candidate authenticated with independent
certificate identities (measured 2026-08-03).** Candidate
`2e5b247e348f362b1cc3fa6a9aaa393d0025fc87`, tree
`5e8216fbf20614328b4f8e1e5615382cea5ef1da`, was clean in tracked content;
the operator-supplied amendment remained untracked and was not included. A
fresh pre-push `git ls-remote` exited **0** with no entry for
`refs/heads/codex/v0.35-evidence-2e5b247`. The single authorized non-force
push created that ref, and immediate readback resolved it exactly to the
candidate. No existing ref was reused, moved, forced, deleted, or repurposed.

Before dispatch, the standing `./run attestation-preflight` executed against
the immutable accepted v0.34 7-receipt / 7-bundle set. Exact pinned `gh`
**2.96.0** accepted **7/7** with every strict flag, and the deliberately wrong
signer workflow was rejected by the separate negative control. Only after that
pass, workflow-dispatch run **30762871542**, attempt **1**, was started once on
the exact candidate/ref with evidence signing. All **9/9** blocking identities
passed; every receipt emission, attestation, bundle-copy, and persistence step
passed. Dependency drift skipped only under its declared report-only
condition. The workflow is still **39,177 bytes** with unchanged SHA-256
`4ebf2c2193fe3fb11e7710b20c1c000fd073103656dc0b155bce945b57bff871`:
the correction changed `tools/audit_deferred.py`, `run`, tests, and forward
records, not `.github/workflows/ci.yml`.

Three receipt values were asserted, not merely read: `msrv` equals
`rustc_release=1.78.0`, `net-msrv-1-86` equals `1.86.0`, and
`net-msrv-1-85` equals `1.85.0`; all three `jq -e` assertions exited **0**.
The release-grade audit used canonical single-bundle JSON, qualified workflow
`jiayanzeng/intel-platform/.github/workflows/ci.yml`, exact source/signer
digest `2e5b247e348f362b1cc3fa6a9aaa393d0025fc87`, exact source ref
`refs/heads/codex/v0.35-evidence-2e5b247`, `--deny-self-hosted-runners`, and
every other strict flag. It accepted **9**, rejected **0**, and found the
complete matrix. Its operator-local **41,042-byte** report has SHA-256
`dac7de5243968096ef49049ab2b400fdb6d489a8fa17091b0654fd5d3e9858d4`;
it and the downloaded artifacts remain under `/private/tmp`, outside the
repository and protected manifest.

For every bundle, the verifier independently constructed and matched the
expected certificate identity rather than accepting a self-reported
expectation:

- `30762871542-1-core.json.sigstore` →
  `https://github.com/jiayanzeng/intel-platform/.github/workflows/ci.yml@refs/heads/codex/v0.35-evidence-2e5b247`
- `30762871542-1-golden.json.sigstore` → the same exact expected URI
- `30762871542-1-lint.json.sigstore` → the same exact expected URI
- `30762871542-1-msrv.json.sigstore` → the same exact expected URI
- `30762871542-1-net.json.sigstore` → the same exact expected URI
- `30762871542-1-net-msrv-1-85.json.sigstore` → the same exact expected URI
- `30762871542-1-net-msrv-1-86.json.sigstore` → the same exact expected URI
- `30762871542-1-shell-py3.11.json.sigstore` → the same exact expected URI
- `30762871542-1-shell-py3.12.json.sigstore` → the same exact expected URI

The earlier “no prior weakening” statement is narrowed to what repository
evidence actually retains. These **20** committed JSON reports name the
qualified value in `measurements.ci_runner.expected_workflow` (the expected
argument field) and in every accepted receipt's `certificate_identity` (the
certificate SAN): `evidence/v0.10.3`, `v0.11.0`, `v0.12.0`, `v0.13.0`,
`v0.14.0`, `v0.14.1`, `v0.15.0` through `v0.15.4`, and `v0.21` through
`v0.29`, each at `deferred-audit/report.json`. At v0.34 close, however, the
37,309-byte JSON report named in `docs/cycles/PROGRESS-v0.34.md` and this file
was temporary and is not retained. The immutable v0.34 bundles retain the
qualified `subjectAlternativeName` SAN, and the records retain the report hash
and qualified workflow summary, but repository evidence does **not** retain the
original `gh --signer-workflow` argument. Therefore the v0.34 conclusion is
only that its certificate SANs were qualified; it does not claim that the
historical CLI argument was qualified or that signer-workflow enforcement was
as strong as recorded. The measured 2.95.0 rejection of a bare value establishes
that version's behavior, not the unavailable historical invocation. No
retraction or historical edit follows.

Exact-candidate local Python 3.11.4 and 3.12.13 each passed **366/366**. Each
hosted lane collected **366**, passed **365**, and skipped the same declared
`on_site` node
`tests/test_deferred_audit.py::test_on_site_production_measurements_match_committed_receipt`
for reason `on-site production audit requires protected corpora and built
cored`. For each lane `tools/test_population.py` derived `collected=366`,
`equivalent=true`, and `equivalent_passed=366`; no count was transcribed.

The project-root exact-candidate export passed at **2,708,098 bytes / 151 files
/ 2 retained cycles**, retaining exactly the v0.34 and v0.35 task/progress
pairs, with **100** derived sources and all **7** required paths. The pinned SEC
RSS body and every `docs/state-archive/**` byte were absent. The manifest is
**193,057 bytes / 332 pins**, **+1,015 bytes** from v0.34; its only changed
entry is the existing `run` authorization pin/provenance. Two complete
candidate runs matched all pins and both protected databases in **0.13 s / 0.11
s real**. Remote `main` and peeled `v0.17.1` remain
`f02379f03ccdfd1b019413234f2ad014d169fb04`; annotated tag object
`14912f134e45277e2b4fd10b7f5bf8b4900ca20d` is unchanged.

Hosted and exact-candidate local golden each passed **11/11**, delta **0**. A
first detached-subject report setup lacked the ignored database copies and
measured no receipt identity; byte-identical copies corrected that temporary
subject. Two sandbox-only golden constructions respectively failed before
assertions on unavailable package-network access and denied loopback bind; the
permission-complete run passed. These are operator-local setup non-results,
not hosted retries or identity failures. Step 6 is complete. No gate, lane,
strict flag, exemption, or classification was relaxed; Step 7 was not entered.

**v0.35 NET-FLOOR — blocked hosted toolchain counterpart (measured
2026-08-02).** This is a forward correction to the earlier local-only
completion claim. Authorized workflow-dispatch run **30746841903**, attempt
**1**, targeted exact candidate
`d33c251d477aa4b1ee6b5b2ebd531b1fda428e99` on fresh ref
`refs/heads/codex/v0.35-evidence-d33c251`. Eight of nine blocking identities
passed, including the new named 1.86 job. The named 1.85 refutation job failed
because its `cargo check` exited **0** after compiling the complete graph.

The action installed and set default toolchain 1.85.0, but its own log then
reported: `toolchain '1.91-x86_64-unknown-linux-gnu' is currently in use
(overridden by .../rust-toolchain.toml)`. The step invoked bare `cargo`, so it
ran the repository override rather than 1.85. Its successful compilation is
therefore not a 1.85 pass and does not fire decision-gate clause 1; it proves
the hosted lane did not execute the construction it claimed. R10 nevertheless
canonicalized that bare hosted command as the counterpart of local `rustup run
1.85.0 cargo`. This is the decision-gate clause 3 classification gap. Step 5
is unboxed and blocked; Step 6 cannot authenticate this candidate. No lane was
changed, no failed run was retried, and the evidence ref was neither reused nor
moved.

The local pre-hosted measurements remain valid but are insufficient to
complete the task. The exact negative command
`RUSTFLAGS="" rustup run 1.85.0 cargo check -p cored --features net --locked
--all-targets` exited nonzero and named the declaring packages, including
`idna_adapter@1.2.2 requires rustc 1.86` plus each locked ICU 2.2.0 crate's
1.86 requirement. This was a declared-`rust-version` refutation, not a
lockfile, registry, network, or unrelated compile failure. The matching
`rustup run 1.86.0` command exited **0** after compiling the complete graph.
The local floor measurement is **1.86**; the hosted floor remains unmeasured.

`cargo tree` measured the locked edge as `cored` → `intel-ingest` →
`reqwest` 0.11.27 → `url` 2.5.8 → `idna` 1.1.0 → `idna_adapter` 1.2.2
→ `icu_collections` / `icu_normalizer` / `icu_properties` 2.2.0. The
shipped offline `intel-compliance` tree remains its seven-crate
`async-trait`/`tokio` graph with no ICU edge. `AGENTS.md` dependency clause 1
now places the chain in the net graph and retains `texting_robots` as the
explicit counterfactual reason it was not admitted into the offline graph.

The launcher adds a success lane and a failure-capable refutation lane; the
workflow adds matching blocking jobs `net-msrv-1-86` and `net-msrv-1-85`.
R10 initially found a real classification gap because redirect tokens produced
different command identities. The corrected grouping keeps redirection off the
command line seen by the canonicalizer. R10 then reported no finding at
**local_jobs=22, local_checks=24, blocking_jobs=8, hosted_checks=23**, with no
new residual exemption. The two new local and two new hosted jobs reuse the
existing canonical net check, so only job counts move. The misleading topology
test is split: one test derives exemption bases; a separate test explicitly
pins and names the four current topology figures.

The hosted identity set is now **9**: `core`, `golden`, `lint`, `msrv`, `net`,
`net-msrv-1-85`, `net-msrv-1-86`, and the two shell matrices. Therefore Step 6
expects **9 receipt JSON files / 9 Sigstore bundles**. The executable source is
`blocking_job_identities`; its exact-set assertion is in
`test_ci_workflow_parser_derives_current_blocking_identities`. The dynamic
success, rejection, and verifier population assertions in
`shell/tests/test_deferred_audit.py` now each state **9**; immutable historical
seven-job evidence remains unchanged.

Before edits, `version-check` reported **3 executable pins**, **22 offline-MSRV
current restatements**, and **3 release-version current restatements**. After
the new floor commands and present-tense corrections it reports the same
**3 / 22 / 3**. The package-scoped net `rustup run` lines do not match the
offline authority's required `--workspace --locked` shape, and no pattern edit
was needed.

Manifest validation and complete artifact verification passed before the
manifest proposal. Afterward, exactly the existing `run` entry moved from
**43,125 bytes / `44314ddf…`** to **43,907 bytes /
`a05562dd1612678aa7c78f1aa8efe09e4c2e4392175c2363b25778577f36b818`**.
The manifest is **192,370 bytes**, delta **+328**, at SHA-256
`b4b1973d8231c1e006a622741f8f84d24a148547f331c4713649a6011282a09c`;
schema remains **2 artifacts / 332 pinned files** and complete verification
matches every pin plus both protected databases. `tools/model_profiles.py`
remains byte-identical at **28,297 bytes /
`1920761c97ffa6fc7b5242c16384fb6f1b0727937f9e1cfd7e00826c913554df`**.
No `artifacts[]` entry or admission record moved. The intended workflow bytes
are **32,533** at SHA-256
`74a1dc3d690d1dfedeb3d0193d40df0df3256ba1f52ccae7751b2cb21b3fd3a8`.
R10/1's adjacent-context anchor necessarily changed after the two job-table
rows were inserted; it is now the unique planted target line itself. No
control, expected finding, or absolute finding line changed.

The focused invariant and deferred-audit suites passed **68/68**. With the
Step 5 box still open, the complete `./run ci-local` entry point passed all
derived **22/22** jobs: invariant-scan **12 rules / 69 controls**, checklist
**268 / 3 / 268 / 268**, constrained Python 3.11.4 **358/358** with the same
one accepted warning, every protected byte and both protected databases, and
embedded golden **11/11**. The separately required standalone `./run golden`
passed the same **11/11** assertions, delta **0**.

**v0.35 POST-LEVER BASIS — first two-cycle-epoch denominator (measured
2026-08-02).** Exact Step 3 audit child
`cd9a119f309096d2d715a54fde6302a5f95362d0` produced a project-root export of
**2,551,288 bytes / 151 files / 2 retained cycles**, with **100** derived and
**7** required paths and both protected byte classes excluded. The first
sandboxed invocation failed npm registry DNS and is a non-result; the identical
permission-complete invocation passed.

The complete append-only governed-field series, with the retention depth in
force at each point, is **2,464,445 [3] → 2,576,273 [3] → 2,556,451 [3]
→ 2,586,197 [3] → 2,629,379 [3] → 2,617,984 [3] → 2,706,393 [3]
→ 2,592,441 [3] → 2,527,180 [2] → 2,551,288 [2]**. The checker's
last-field-per-cycle series is **2,576,273 [3] → 2,629,379 [3] (+53,106)
→ 2,706,393 [3] (+77,014) → 2,592,441 [3] (−113,952) → 2,527,180
[2] (−65,261 across the lever) → 2,551,288 [2] (+24,108)**. Thus the
latest positive adjacent same-kind governed pair is now v0.34→v0.35 and is
wholly within the two-cycle epoch. The published **77,014**, **77,862**,
**86,946**, and **79,962 bytes/cycle** denominators are all explicitly stale:
each was measured with three-cycle retention and its recurring v0.33-era
turnover term.

At the same exact tree, controlled Repomix exports differed only in the
retention pattern. Two-cycle retention emitted **2,551,288 bytes / 151 files**;
the three-cycle counterfactual emitted **2,649,296 bytes / 153 files** and added
exactly `TASKS-v0.33-EXECUTION.md` plus `PROGRESS-v0.33.md`. The real export
reclaim is therefore **98,008 bytes**, refuting the reviewer's **97,951-byte**
figure by **57 bytes**. The raw two-file payload alone is not the export
measurement; Repomix framing is part of the delivered bytes.

The export ceiling has **448,712 bytes** remaining and is **18.61 cycles** away
on the new **24,108-byte/cycle** governed denominator. State at the same tree is
**256,218 / 453,741 bytes**. Exact delivered v0.34 State was **243,402 bytes**,
so its post-retention same-kind denominator is **12,816 bytes/cycle** and its
**197,523-byte** remainder is **15.41 cycles**. State is therefore nearer by
**3.20 cycles**. Both rates are one-pair measurements: the checker's
representativeness remains unbounded, and one v0.35 observation is not a trend.
The new basis does not indicate an immediate lever, so this step selects none;
the archive, manifest-exclusion, and depth-one tradeoffs remain unexercised.

**v0.35 ONE-RETENTION — one Git-derived retained-cycle authority (measured
2026-08-02).** Option A was feasible and selected. The formatter's
`retained_cycle_paths` parameter is now mandatory; the `None` branch and its
patch-number arithmetic are deleted. Production already obtains the set from
`tools/export_check.py::expected_retained_cycle_paths(root)`. The cycle-check
fixtures now initialize Git, commit their cycle documents, obtain that same
tracked set, and only then derive the configured pattern. The autouse fixture
that substituted a second arithmetic implementation is gone.

The skipped-cycle control no longer calls the formatter through a fallback.
It builds one consecutive Git-tracked construction to obtain the deliberately
wrong configured pattern, then proves that applying those bytes to a different
Git-tracked skipped-cycle construction is rejected. Every actual formatter
call receives the set derived for its own construction. The focused
`shell/tests/test_cycle_check.py` suite passed **85/85**.

R12 adds one failure-capable control, moving the registry from **68 to 69**
controls for a recorded reason. `r12_findings` inspects the executable callable
signature and rejects any default on `retained_cycle_paths`; the planted
optional-parameter mutation fired at the real entry point:

```text
invariant-scan: SELF-TEST R12/20 PASS: tools/cycle_check.py:1215: review-export-retention planted controls were not detected: optional-retained-set-parameter
```

R12 as a whole passed **1/1 rule / 41 controls**. This is the executable proof
that an omitted-set path cannot silently return: the property is not inferred
from a search. The full registered total is now **12 rules / 69 controls**;
the added control uses the existing unique review-retention marker anchor and
introduces no absolute line field.

The real v0.35 checker accepted the activation pattern
`docs/cycles/{TASKS,PROGRESS}-v0.{[0-9],1[0-9],2[0-9],3[0-3]}{.md,.*.md,-*.md}`.
An isolated current-tool construction replacing only that pattern with the
stale boundary emitted verbatim:

```text
cycle-check: ERROR: repomix.config.json: review-export retention pattern for v0.35 must be 'docs/cycles/{TASKS,PROGRESS}-v0.{[0-9],1[0-9],2[0-9],3[0-3]}{.md,.*.md,-*.md}' to agree with the tracked retained-cycle set; found ['docs/cycles/{TASKS,PROGRESS}-v0.{[0-9],1[0-9],2[0-9],3[0-2]}{.md,.*.md,-*.md}']
cycle-check: FAIL (1 defect(s))
```

The prior retention-fallback trigger was worded around the very branch it
governed and Step 1 truthfully measured it as satisfied. The active row is
forward-corrected to fire if the formatter again accepts an omitted set or a
live caller supplies a set not Git-derived for its root. Step 1 had already
obeyed its own mandate to replace the active v0.34 placeholder, so runbook
amendment r2 applies Step 3's “do not edit” instruction to the immutable closed
v0.34 records; none was changed.

With the Step 3 checkbox deliberately still open, `./run ci-local` passed all
**20/20** jobs: registered invariants **12 rules / 69 controls**, checklist
**268 / 3 / 268 / 268**, warning-denied current/net/MSRV Rust lanes, constrained
Python 3.11.4 **357/357** with the same one accepted warning, embedded golden
**11/11**, all **332** pins, and both protected databases. The mandatory
standalone post-task golden then passed byte-identical **11/11**, delta **0**.

**v0.35 ANCHOR — planted-control locations derive from constructed mutants
(measured 2026-08-02).** Registry schema v4 replaces every `expected_line`
integer with an authored `expected_anchor` and optional zero-based
`expected_anchor_line_offset`, defaulting to zero. The harness first copies the
tracked tree, applies the fail-before mutation, requires the literal anchor
exactly once in that mutant, derives its file-global line from the anchor start
plus the checked offset, and only then constructs the expected finding. Rule
output is never read to produce that expectation.

All **68** controls have unique mutant anchors and the control count is
unchanged. **43** anchors are one line and **25** are multi-line; **8** use a
nonzero line offset. R1/1 uses a nine-line anchor with offset **3**, retaining
the measured helper-relative target while extending beyond `replace_with` into
unchanged context. All 40 R12 controls retain their pre-existing named control-
site marker: 39 use the marker alone, while R12/39 extends it by one unchanged
line. An executable registry-wide assertion confirms no registered anchor is
wholly a substring of its own `replace_with`. The count of `expected_line`
fields or any other hand-typed absolute finding-line field in
`config/invariant-rules.json` is **0**; there are no survivors to justify.

The real entry point rejected zero- and two-occurrence anchors verbatim:

```text
invariant-scan: SELF-TEST R1/1 FAIL: crates/store/src/sqlite.rs: expected_anchor occurs 0 times in constructed mutant; expected exactly 1
invariant-scan: SELF-TEST R1/1 FAIL: crates/store/src/sqlite.rs: expected_anchor occurs 2 times in constructed mutant; expected exactly 1
```

A constructed R7 checker reporting every real finding one line late was caught
before a pass could be trusted:

```text
invariant-scan: SELF-TEST R7/1 FAIL: missing expected finding 'invariant-scan: R7 FAIL: crates/store/src/sqlite.rs:410: documents_by_ids must not be public'; observed=['invariant-scan: R7 FAIL: crates/store/src/sqlite.rs:411: documents_by_ids must not be public']
```

The mutant/original boundary is independently exercised in both directions. A
temporary R3 control anchored only on planted `use async_openai::Client;`
resolved in the mutant and passed its **1/1-rule / 1-control** self-test. A
temporary R7 control anchored on the original private
`fn documents_by_ids(...)` declaration was absent after mutation and failed
with the same zero-occurrence rejection. The focused
`shell/tests/test_invariant_scan.py` suite passed **27/27**. No control was
added, removed, or weakened.

With the Step 2 checkbox deliberately still open, `./run ci-local` passed all
**20/20** jobs, including registered invariants **12 rules / 68 controls**,
checklist **268 / 3 / 268 / 268**, warning-denied current/net/MSRV Rust lanes,
constrained Python 3.11.4 **357/357** with the same one accepted warning,
embedded golden **11/11**, all **332** pins, and both protected databases.
The mandatory standalone post-task golden passed byte-identical **11/11**,
delta **0**.

**v0.35 E0 — entering-state reconstruction and G1–G7 dispositions (measured
2026-08-02).** The entering worktree was clean apart from the operator-supplied
untracked v0.35 runbook. Exact audit child
`d8d20b81b9ea9027dada74ce047a7cd92815e9f3` had immediate parent
`6a19d31dd00143fc85a5e6c157dceb90ce40e946`. Direct remote inspection—not the
closing record—resolved `main` and peeled `v0.17.1` to closing commit
`f02379f03ccdfd1b019413234f2ad014d169fb04`, its immediate parent to release
commit `7a621e39a069a1ef26438e841e7bb1ca2f34165b`, annotated tag ref `v0.17.1` to
object `14912f134e45277e2b4fd10b7f5bf8b4900ca20d` of Git type `tag`, and evidence
ref `codex/v0.34-evidence-1117dc6` to
`1117dc6db6ec0e55e8c8f078ca8059628f9f8262`. Exact historical tags `v0.8.0`
and `v0.10.2` were absent. The project-root export at the exact audit child
measured **2,559,695 bytes / 151 files / 2 retained cycles**, confirming both
the reviewer's delivered-export figure and the audit-child identity rather
than inferring either from the 7,323-byte difference.

G1 constructed every registered mutant against repository bytes with its
trailing newline preserved. The measured geometry was:

| rule | controls | unique target lines | named control-site target lines | minimum unique widths |
|---|---:|---:|---:|---|
| R1 | 1 | 0 | 0 | 4 lines, target offset 3 |
| R2 | 1 | 1 | 0 | 1 |
| R3 | 1 | 1 | 0 | 1 |
| R4 | 1 | 1 | 0 | 1 |
| R5 | 8 | 8 | 0 | 1 for all 8 |
| R6 | 1 | 1 | 0 | 1 |
| R7 | 3 | 3 | 0 | 1 for all 3 |
| R8 | 3 | 3 | 0 | 1 for all 3 |
| R9 | 1 | 1 | 0 | 1 |
| R10 | 3 | 3 | 0 | 1 for all 3 |
| R11 | 5 | 5 | 0 | 1 for all 5 |
| R12 | 40 | 40 | 40 | 1 for all 40 |
| **total** | **68** | **67** | **40** | **67 one-line; R1/1 four-line** |

Thus all 40 R12 targets really are named control-site lines; the reviewer
hypothesis is confirmed. R1/1's expected line occurred twice, while the unique
four-line mutant anchor begins at planted `fn rebuild_identity_with_limit` and
derives the target at zero-based offset 3. `invariant-scan --self-test` then
executed and rejected every planted construction: **12/12 rules / 68 controls**.

G2 executed both retention branches. For active v0.35 the Git-derived tracked
set `{v0.34,v0.35}` and the fallback each produce the boundary through v0.33.
For a skipped v0.36 construction whose tracked set is `{v0.34,v0.36}`, the
tracked branch still ends at v0.33 while the arithmetic fallback ends at v0.34.
Production `cycle_check.py` calls the helper with the Git-derived set. The
generic fixture and deliberate skipped-cycle test in
`shell/tests/test_cycle_check.py` reach the fallback. The R12
`retention-skipped` construction deliberately relies on that divergence to
make the real checker reject the stale fallback-shaped pattern; its trigger as
written is therefore satisfied and Step 3 owns the criterion correction.

G3 found no honest post-retention trend denominator yet. The published
**77,014**, **77,862**, **86,946**, and **79,962 bytes/cycle** bases were all
measured while three execution cycles were retained and are epoch-stale after
v0.34's move to two. Exact delivered v0.34 is the sole delivered point in the
new epoch, so no adjacent same-kind post-retention pair exists and none was
synthesized. The live row stays bound to its last valid governed field; Step 4
owns the first new adjacent basis.

G4 read the executable workflow and launcher. The `net` job pins Rust **1.91**;
the `msrv` job pins Rust **1.78** and builds only the offline workspace graph.
The report-only `drift` job has `continue-on-error: true`, writes its MSRV text
only to `$GITHUB_STEP_SUMMARY`, and no job or check consumes that text. The
locked net path is `cored → intel-ingest → reqwest 0.11.27 → url 2.5.8 → idna
1.1.0 → idna_adapter 1.2.2`; locked `icu_collections`, `icu_normalizer`,
`icu_locale_core`, `icu_normalizer_data`, `icu_properties`,
`icu_properties_data`, and `icu_provider` 2.2.0 each declare Rust **1.86**.
The offline
`intel-compliance` graph remains its seven-crate `async-trait`/`tokio` graph
and contains no ICU edge. A sandboxed metadata attempt that could not download
platform packages was a network non-result, not evidence about the graph.

G5 classified, without changing any trigger, all **28** governed rows as
**21 event-shaped / 5 authorization-shaped / 2 self-discharging**. The four
Architecture rows are event-shaped. The two self-discharging rows are the
explicit Rust 1.86 net execution and historical `v0.8.0`/`v0.10.2`
publication, both assigned work in this cycle. The authorization-shaped rows
are EDGAR extension mapping, the first recurring scheduled SEC run, admission
of a third configured publisher, permission to change the public version
literal in `app.py`, and release-classification adjudication. Every remaining
deferred row is event-shaped; a row that also names authorization remains
event-shaped when an external outage, runtime topology, publisher, or other
event is independently necessary. This taxonomy describes trigger shape; it
does not claim the work or external event occurred.

G6 measured `r10_report` at **local_jobs=20, local_checks=24,
blocking_jobs=6, hosted_checks=23**, with 45 declared exemptions and no
finding. Step 5's two versioned net lanes will move only `local_jobs` from 20
to 22 and `blocking_jobs` from 6 to 8; they exercise an existing canonical net
check, so neither unique-check count moves. G7's manifest/lockfile trace
therefore refutes the dependency-gate prose that says ICU is presently in the
offline graph through `intel-compliance`; it is a rejected-dependency
counterfactual, while the real edge is net-only through `intel-ingest`.

All four Architecture rows and all 24 active deferral rows now carry dated
v0.35 measurements, with trigger text unchanged. Version checking derived
0.17.1 with **22** offline-MSRV and **3** release-version current
restatements. The unchanged **192,042-byte / 332-pin** manifest passed schema
validation and two complete artifact checks in **0.11 s / 0.10 s real**. Clean
constrained Python 3.11.4 and 3.12.13 lanes each collected/passed **352**,
failed **0**, skipped **0**, and emitted the same one accepted warning;
`tools/test_population.py` derived `collected=352`, `equivalent=true`, and
`equivalent_passed=352`. The initial sandboxed 3.11 lane failed only on denied
loopback/`ps` access and the then-stale observations, so it is recorded as an
environment/pre-refresh non-result. No dependency declaration or constraint
changed.

With the Step 1 checkbox deliberately still open, the real `./run ci-local`
entry point passed all **20/20** jobs: version and cycle consistency, checklist
audit **268 / 3 / 268 / 268**, all **12 rules / 68 controls**, deferred
re-derivation, Python-floor compile, ShellCheck, warning-denied current/net/MSRV
Rust lanes, clippy, rustfmt, constrained Python 3.11.4 **352/352**, embedded
golden **11/11**, all pins and both databases, persisted fingerprints, and the
activation progress record. No gate was waived or interpreted from a partial
runner. The mandatory standalone post-task golden then passed byte-identical
**11/11**, delta **0**.

**v0.34 R-CLOSE — operator-selected no-release closure (measured
2026-08-02).** The operator explicitly selected `no-release`. The measured
distance from published v0.17.1 contains lifecycle controls, focused lifecycle
tests, cycle and architecture records, and the two-cycle review-export
retention configuration selected in Step 5. It contains no production source,
workflow, dependency, release value, measured runtime-behaviour difference,
public route, response shape, or serialized `/v1/*` value-domain change. That
structural distance is the reason for the disposition; “nothing shipped” is
not substituted for it.

Final direct remote inspection resolved `main` and peeled `v0.17.1` to
published closing commit `f02379f03ccdfd1b019413234f2ad014d169fb04`, the
annotated tag ref to object
`14912f134e45277e2b4fd10b7f5bf8b4900ca20d`, and fresh evidence ref
`codex/v0.34-evidence-1117dc6` to exact candidate
`1117dc6db6ec0e55e8c8f078ca8059628f9f8262`. `version-check` derives 0.17.1
from every authority with 22 offline-MSRV and 3 release-version current
restatements. All eight declared release-authority paths are unchanged from
activation. No tag, `main`, release ref, version source, or publication
identity moved during close.

The last governed field visible to the closing tree is the authenticated
candidate at **2,527,180 bytes / 151 files / 2 retained cycles**, excluding
both protected byte classes. Its **472,820-byte / 15.76%** remainder is **6.14
cycles** on the corrected latest-positive-adjacent same-kind governed basis,
v0.31→v0.32 at **77,014 bytes/cycle**. The full governed series is **2,576,273
→ 2,629,379 (+53,106) → 2,706,393 (+77,014) → 2,592,441 (−113,952) →
2,527,180 (−65,261)**. The two negative transitions are not used as fictional
growth denominators, and the entry point states that its chosen single pair
has no representativeness guarantee and may predate an undetectable structural
change. The closing implementation tree's own export is reserved for the
audit child's non-governing `cycle-ending review-export audit` field.

Immediately before drafting the closing record, State measured **236,944 /
453,741 bytes**, leaving **216,797 bytes / 6.95 cycles** at the latest positive
same-kind **31,177-byte/cycle** denominator. The unchanged manifest measured
**192,042 / 1,048,576 bytes**, leaving **856,534 bytes / 1,323.85 cycles** at
its **647-byte/cycle** denominator. The governed export at **6.14 cycles** is
therefore the nearest byte boundary. Manifest schema validation reported **2
artifacts / 332 pinned files**; two complete checks took **0.10 s / 0.09 s
real** and matched all pins plus both databases. The forbidden structural
archive remains **178,125 bytes** at SHA-256
`b9442f7bedf9024351ef0bafe0e6f7a4d58a0883e9c2f81bbbadebfb476d5886`;
the forbidden manifest remains at SHA-256
`a5d990462ba59a252c9228db2c4d4532670debbcb7422c8771ef68fc22a0dd2b`.
Both are byte-unchanged from activation. Pre-close `checklist-audit` passed
**267 checked / 3 retracted / 267 matched / 267 commits resolved**.

Over activation commit `bb4257000cd6a752e807af9f48d0fe871e20d216`
exclusive through the closing worktree, used declared allowances are
`tools/cycle_check.py`, `tools/invariant_scan.py`,
`config/invariant-rules.json`, `shell/tests/**`, `AGENTS.md`,
`ARCHITECTURE.md`, `tools/export_check.py`, and `repomix.config.json`;
`tools/version_check.py` is the sole unused allowance. Every release authority
and `forbid` path is unused. Standing status precedence accounts for
`STATE.md` and the active runbook/progress pair. The exact path diff confirms
no closed-cycle, protected, production, workflow, dependency, publisher,
scheduler, observation, or fixture path changed.

The pre-commit closing matrix passed all **19** executable `ci-local` jobs that
do not require the not-yet-possible R-CLOSE progress mapping: version and
closed-cycle checks, registered invariants **12 rules / 68 controls** with all
failure-capable self-tests, deferred-evidence re-derivation, Python floor
compile, ShellCheck, warning-denied current workspace and net checks/tests,
clippy, rustfmt, both Rust 1.78 locked lanes, shell, golden, protected
artifacts, fingerprints, and the existing append-only progress record. The
Python 3.11.4 and 3.12.13 acceptance lanes each reported **352 collected / 352
passed / 0 failed / 0 skipped** and the same one accepted warning. Standalone
golden passed byte-identical **11/11**, delta **0**. The sandboxed net lane and
Python 3.11 lane were environment non-results: the former had one denied
loopback bind, and the latter reported **344 passed / 8 failed** solely on
denied loopback and `ps` access. Their identical permission-complete reruns are
the passing results. The append-only audit child will add the real closing
commit mapping and cycle-ending export measurement, then run the complete
**20/20** entry point.

The first closing-record draft was intentionally submitted to the real
checker before acceptance. It rejected three record-shape defects: the heading
did not contain the exact `Intentionally unreleased implementation commits:`
token, a full annotated-tag-object hash was parsed as a purported no-release
commit, and the governed row said `exported` rather than carrying exactly one
visible `export of **N bytes` value. The final draft uses the canonical heading,
abbreviates the non-commit tag object in the no-release record, and carries the
required visible/machine values. The unchanged checker then passed with
`state=closed` and `governed_export=bound`.

Published v0.17.1 reset the divergence count to zero. The v0.34 closing
distance contains no runtime-behaviour difference and no public-surface
change, so the count remains zero and no fresh count starts. Across the cycle,
the invariant registry remains **68 controls** and **27 / 68** existing
`expected_line` values differ from activation; all were re-derived from real
emitted output. G5's retained trend is controls **58 → 61 → 68**,
shifted-existing expectations **36 → 12 → 25**, combined checker bytes
**192,695 → 208,356 → 243,494**, and ratios **62.07% → 19.67% → 36.76%**.
The non-monotonic series supports no defensible linear approach rate, and the
cycle-wide count is 41 below the controls protected. The one reviewer error
remains at the runbook header where readers encounter it first.

**v0.34 RE-MEASURE — exact candidate authenticated on a fresh evidence ref
(measured 2026-08-02).** The worktree was clean at exact candidate
`1117dc6db6ec0e55e8c8f078ca8059628f9f8262`, tree
`05ef0cce218ce03a69a07558c5ce25edf7d8331f`. Before any push, direct
`git ls-remote` exited zero with no entry for
`refs/heads/codex/v0.34-evidence-1117dc6`. The operator then explicitly
authorized publication of that exact candidate to that one fresh ref. The
single push created it, and immediate plus final readback each resolved it to
the candidate. No existing ref was reused, forced, moved, or repurposed.

Workflow-dispatch run **30726156221**, attempt **1**, used branch
`codex/v0.34-evidence-1117dc6`, exact candidate SHA, and evidence signing.
`core`, `golden`, `lint`, `msrv`, `net`, `shell/python=3.11`, and
`shell/python=3.12` all passed. Every receipt emission, attestation, bundle-copy,
and artifact-persistence step passed; dependency drift skipped under its
declared report-only condition. The workflow remained byte-unchanged at
SHA-256 `5a7160f15a9eaa57daa9cc8ce666c1a1c2b8cc39728ea2308474e0d66f2b6791`.
The repository's release-grade verifier consumed the downloaded ephemeral
**7-receipt / 7-bundle** set, accepted **7**, rejected **0**, and found the
complete runner matrix. Every accepted certificate binds repository
`jiayanzeng/intel-platform`, workflow
`jiayanzeng/intel-platform/.github/workflows/ci.yml`, source and signer digest
`1117dc6db6ec0e55e8c8f078ca8059628f9f8262`, and source ref
`refs/heads/codex/v0.34-evidence-1117dc6`. The temporary **37,309-byte** report
has SHA-256
`52580016656c9e5fa686b16ecf7f3afdadea47a7892070eeb2ec744d9f68b68c`
and remains outside the repository and protected manifest. An earlier tool-
orchestration attempt produced neither a report nor captured exit evidence and
is a non-result; the identical interactive rerun exited zero and is the
measurement reported here.

The first post-record `cycle-check` stopped because the draft Architecture row
named `docs/cycles/PROGRESS-v0.34.md` as its evaluated source before that
progress file could legally contain the post-implementation governed field. It
emitted `governed export margin source docs/cycles/PROGRESS-v0.34.md has no
valid governed measurement series`. The implementation record therefore stays
bound to the last governed field already visible in v0.33. After this commit
exists, the separate append-only Step 6 progress entry adds the v0.34 candidate
measurement; the open-cycle exemption then applies until Step 7 forward-updates
the live row. The checker and historical field were not weakened or invented.

Exact-candidate local Python 3.11.4 and 3.12.13 each collected/passed **352**,
failed **0**, and skipped **0**. Each hosted lane collected **352**, passed
**351**, and skipped the same named `on_site` node
`tests/test_deferred_audit.py::test_on_site_production_measurements_match_committed_receipt`
for reason `on-site production audit requires protected corpora and built
cored`. For each lane `tools/test_population.py` emitted `collected=352`,
`equivalent=true`, and `equivalent_passed=352`; no count was transcribed from a
runner log. The exact candidate locally matched all **332** pins and both
protected databases, passed `cycle-check`, and exported **2,527,180 bytes /
151 files / 2 retained cycles** with both protected byte classes excluded.
Golden passed **11/11** on the exact candidate locally and hosted, delta **0**.

Final direct remote measurement left the fresh evidence ref exact, remote
`main` and peeled `v0.17.1` at closing commit
`f02379f03ccdfd1b019413234f2ad014d169fb04`, and the annotated tag ref at
object `14912f134e45277e2b4fd10b7f5bf8b4900ca20d` of Git type `tag`. The
candidate distance contains lifecycle documentation, tests, controls, and
retained-cycle configuration, but no production source, workflow, dependency,
release value, measured runtime-behaviour difference, or public-surface change.
Step 6 issued no publisher request, ran no scheduler, service, or model-profile
command, and performed no manifest registration or protected-byte write. Its
only remote mutation was the explicitly authorized fresh evidence ref.

**v0.34 BUDGET-LEVER — operator-selected Option A reduces review retention
from three cycles to two (measured 2026-08-02).** The operator explicitly
selected Option A after the required construction measurement. Exact baseline
commit `e8bf31f225f1cb977dd6a1ee45c6e062e62b96a4`, tree
`8fe4225fb7c53c8d146fb5a0725bdc19983d16de`, exported **2,629,024 bytes /
153 files / 3 retained cycles**. A throwaway construction changing only
`CYCLE_RETENTION_DEPTH` from 3 to 2 and the matching Repomix exclusion through
v0.32 produced tree `c19876d08502a8aa4eb33e35d25ce2b7d67f32e5` and exported
**2,520,904 bytes / 151 files / 2 retained cycles**. The exact one-time reclaim
is therefore **108,120 bytes**. At the same unchanged post-retention steady
denominator of **77,862 bytes/cycle**, the available margin moves from
**370,976 / 77,862 = 4.76 cycles** to **479,096 / 77,862 = 6.15 cycles**, an
increase of **1.39 cycles**. The corroborating same-basis calculations are
**4.27 → 5.51 (+1.24)** at the **86,946-byte** persistent-component
denominator and **4.64 → 5.99 (+1.35)** at the **79,962-byte** positive
delivered denominator. These retain Step 3's representativeness and structural-
epoch bounds and are projections, not forecasts.

The stale-pattern construction changed the executable depth while leaving the
three-cycle Repomix pattern in place. The real `./run cycle-check` entry point
rejected it verbatim:

```text
cycle-check: ERROR: repomix.config.json: review-export retention pattern for v0.34 must be 'docs/cycles/{TASKS,PROGRESS}-v0.{[0-9],1[0-9],2[0-9],3[0-2]}{.md,.*.md,-*.md}' to agree with the tracked retained-cycle set; found ['docs/cycles/{TASKS,PROGRESS}-v0.{[0-9],1[0-9],2[0-9],3[0-1]}{.md,.*.md,-*.md}']
cycle-check: FAIL (1 defect(s))
```

The implementation moves the sole executable depth authority and tracked
Repomix pattern together. The contributor contract and live Architecture
trigger now describe exactly the active cycle plus one prior; dated historical
three-cycle measurements remain unchanged. No boundary or ceiling moved,
Option E was not selected, and no additional exclusion beyond the derived
two-cycle policy was added. The real project-root export passed at **2,524,284
bytes / 151 files / 2 retained cycles** on the implementation worktree over
baseline tree `8fe4225fb7c53c8d146fb5a0725bdc19983d16de`. With the task box still
open, the complete entry point passed **20/20** jobs, checklist **265 / 3 / 265
/ 265**, registered invariants **12/12 rules / 68 controls**, clean constrained
Python 3.11.4 **352/352**, warning-denied current/net/MSRV Rust lanes, all
**332** pins, both protected databases, and embedded golden **11/11**. The
mandatory standalone `./run golden` also passed **11/11**, delta **0**.

**v0.34 REGION-FLOOR — State structural admission no longer depends on the
tail it protects (measured 2026-08-02).** E0's exact delivered-tree
construction deleted the marker and all numbered State sections. Before this
change, the real entry point emitted `state_regions=not-measured` and passed;
only the separate semantic `version-check` zero-restatement rule failed in the
composite lane. With the REGION-FLOOR implementation copied into the same
full-tail construction, the real entry point now emits verbatim:

```text
cycle-check: ERROR: STATE.md: State archival structural permanent-tail marker required exactly once; found 0; semantic current-restatement state=absent remains delegated to version-check
cycle-check: FAIL (1 defect(s))
```

The structural family now admits only a recognized status header and exactly
one permanent-tail marker before proceeding to marker adjacency, region
overlap, top-level headings, unique/increasing anchors, live external-reference
resolution, and ordinal reporting. None of those structural decisions depends
on the semantic restatement result. The existing delegation to
`version_check.offline_msrv_report` remains: successful output reports
`structural=bound semantic_current_restatement=present
semantic_owner=version-check`, and a missing semantic restatement remains that
tool's responsibility. Thus the duplicate semantic reader was not recreated.

G1's other silent publication-status exits are now visible bounds in the
entry-point output. With no reachable closed release, reconciliation reports
`not-applicable` because no release ref exists. Portable hosted mode reports
`not-requested`, names missing historical local tag objects as the bound, and
states that State/header admission and closed-runbook structure remain
enforced. A verified legacy release reports that R-CLOSE post-push records do
not apply to its protocol. Current local output reports
`local-tag-reconciliation=verified protocol=tagged-closing release=v0.17.1`.
All error-bearing early returns remain named defects rather than bounds.

Focused lifecycle tests passed **85/85**, including new full-tail, missing
structural-header, no-release, portable-hosted, and legacy-protocol cases. R12
now plants complete tail deletion through `cycle_check.run`; disabling the
structural marker branch makes that construction disappear, proving the test
double can violate the property. The registered suite passed **12/12 rules /
68 controls**. The first self-test stopped on its expected stale location.
Replaying every R12 mutation emitted the actual findings; **27** shifted
existing `expected_line` values were copied from those outputs, and the final
self-test passed all 68 controls. No location was offset-computed. No
production source, workflow, dependency, publisher request, scheduler,
service, model-profile command, release authority, protected artifact, public
surface, or runtime behaviour changed.

The complete Step 2 acceptance gate passed **20/20** local jobs, including
checklist **262 / 3 / 262 / 262**, registered invariants **12/12 rules / 68
controls**, the clean Python 3.11.4 shell population **352/352**, warning-denied
current/net/MSRV Rust lanes, both protected databases and all **332** pins.
Golden remained byte-stable at **11/11** inside `ci-local` and at the required
standalone `./run golden` entry point.

**v0.34 BASIS-BOUND — the margin entry point states what its denominator
cannot prove (measured 2026-08-02).** The executable selection remains the
latest positive adjacent same-kind governed pair, because it binds the recorded
values and arithmetic without mixing delivered and governed kinds. The check
now emits this successful-path bound verbatim:

```text
cycle-check: governed-export-margin-basis: selected=latest-positive-adjacent-governed-pair representativeness=unbounded(single adjacent pair carries no representativeness guarantee) structural_epoch=unobserved(checker cannot detect a basis predating a structural change)
```

A constraint was not selected because the repository evidence cannot support
one. The governed series contains only two positive adjacent deltas, **53,106**
and **77,014 bytes**, so a floor derived from them would be arbitrary rather
than a representativeness guarantee. A trailing window would combine the
v0.33 **−113,952-byte** one-time archive transition with steady growth, exactly
the denominator error this cycle forbids. An epoch constraint would require an
independent machine-readable archival event aligned to the progress series;
none exists, and parsing the prose that makes the claim would turn the bound
into self-attestation. The truthful outcome is therefore an emitted bound until
future evidence supplies a defensible constraint. No dated historical margin
figure was edited.

The first complete gate correctly stopped at R12 control 37 because the new
emitted-bound path shifted its stored source location. Replaying that exact
mutation through `exercise_fail_before` emitted
`tools/cycle_check.py:2935: ... silently-dropped-trigger-subject`; the one
shifted existing `expected_line` was copied from that output. This step adds no
control and changes no control construction, so the registered population
remains **68** and the deferred control-schema trigger did not fire.

After that named stopped attempt, the complete entry point passed **20/20**
with BASIS-BOUND's task box still open: checklist **263 / 3 / 263 / 263**,
registered invariants **12/12 rules / 68 controls**, warning-denied
current/net/MSRV Rust lanes, clean Python 3.11.4 shell **352/352**, all **332**
pins, both protected databases, and embedded golden **11/11**. The required
standalone `./run golden` also passed **11/11**, for delta **0**. Focused
lifecycle tests remained **85/85**.

**v0.34 BUDGET-DERIVE — every supported export pair, with reclaims separated
(measured 2026-08-02).** Three independently recorded series cover all adjacent
pairs their tracked records support. “Governed” means the last machine-readable
field in each progress record; “closing audit” means its non-governing
cycle-ending field; “delivered audit child” means E0's exact export of the
append-only child actually delivered to the next cycle.

| record class | v0.30→v0.31 | v0.31→v0.32 | v0.32→v0.33 |
|---|---:|---:|---:|
| governed last-per-progress | 2,576,273→2,629,379 = **+53,106** | 2,629,379→2,706,393 = **+77,014** | 2,706,393→2,592,441 = **−113,952** |
| closing-tree cycle-ending audits | not recorded for v0.30 | 2,649,103→2,729,387 = **+80,284** | 2,729,387→2,628,346 = **−101,041** |
| exact delivered audit children | not retained as an E0 export pair | 2,654,404→2,734,366 = **+79,962** | 2,734,366→2,634,692 = **−99,674** |

Only the exact delivered audit-child exports retain enough serialized content
to support component attribution. For those two supported pairs, persistent
components are shown before either recurring retention turnover or the one-time
State archive. Each percentage is the component's share of that column's named
persistent net, **67,805** then **86,946 bytes/cycle**.

| persistent component | v0.31→v0.32 bytes / share of 67,805 | v0.32→v0.33 bytes / share of 86,946 | reclaim mechanism |
|---|---:|---:|---|
| `cycle_check.py` + `invariant_scan.py` | +15,661 / 23.10% | +35,138 / 40.41% | none automatic; deliberate simplification only |
| `version_check.py` | +7,715 / 11.38% | 0 / 0% | none automatic |
| control tests, fixtures, and registry | +11,580 / 17.08% | +15,416 / 17.73% | none automatic; deliberate control retirement only |
| live `STATE.md`, before archive | +28,605 / 42.19% | +31,177 / 35.86% | governed structural archive, shown separately below |
| `ARCHITECTURE.md` + `AGENTS.md` | +4,244 / 6.26% | +4,568 / 5.25% | none automatic |
| protected manifest | 0 / 0% | +647 / 0.74% | no deletion; append-only pins make growth effectively permanent |
| **persistent net** | **+67,805 / 100%** | **+86,946 / 100%** | — |

Reclaim and turnover are not growth denominators. The retention row is the net
effect visible in the exact exports after adding the new retained cycle and
evicting the oldest; the records do not preserve a serialized gross-add versus
gross-eviction split, so none is invented.

| separate reclaim or turnover | v0.31→v0.32 | v0.32→v0.33 | share denominator |
|---|---:|---:|---|
| three-cycle document turnover | +12,157 | −9,084 | 15.20% of +79,962 delivered net; −11.67% of +77,862 post-retention steady net |
| one-time State archival reclaim | 0 | **−177,542** | 178.12% of the −99,674 delivered net |
| retention-pattern / serialization movement | 0 | +6 | −0.006% of the −99,674 delivered net |

The reconciliations are exact: **67,805 + 12,157 = 79,962** for v0.31→v0.32,
and **86,946 − 9,084 − 177,542 + 6 = −99,674** for v0.32→v0.33. The second
transition's gross persistent growth is therefore positive; its negative
delivered result is a one-time archive effect, not a negative growth rate.

Against the exact delivered v0.33 export remainder of **365,308 bytes**, the
latest persistent-component denominator projects **4.20 cycles**
(365,308 / 86,946), the latest post-retention steady denominator projects
**4.69** (365,308 / 77,862), the positive delivered denominator projects
**4.57** (365,308 / 79,962), and their two-transition steady mean of **78,912**
projects **4.63**. The same delivered tree's State remainder is **247,211
bytes**: its latest positive **31,177-byte** denominator projects **7.93
cycles**, and its two-transition **29,891-byte** mean projects **8.27**. Thus
the fuller series confirms, rather than contradicts, the reviewer's ordering:
the export ceiling arrives first under every named denominator. These are
projections with the Step 3 representativeness/epoch bounds, not forecasts.
This step selects no lever, changes no ceiling or retention depth, and adds no
exclusion.

The real measurement-only `./run cycle-check` passed with the task box open,
State at **229,486 / 453,741 bytes**, manifest **192,042 / 1,048,576**, the
margin basis's two emitted bounds, and governed export
`exempt-open-empty-progress`. The mandatory standalone golden anchor passed
**11/11**, delta **0**. Only `STATE.md` and the active runbook were written;
the progress record remains reserved for the separate post-implementation
audit commit.

**v0.34 E0 entering-state reconstruction and G1–G6 dispositions (measured
2026-08-02).** The sole pre-activation worktree item was the operator-supplied
untracked v0.34 runbook. Exact delivered v0.33 HEAD was audit child
`e0ab6964f76b0a919c5214607ef141eb5b118deb`, whose immediate parent was
closing implementation `70781081abd42ed9a49e22ed100efdb039a9b762`.
Activation implementation `bb4257000cd6a752e807af9f48d0fe871e20d216`
and audit `5e91545da0dcce215a019ea4dea7c1415fd2d6f6` established the declared
v0.34 cycle and exact v0.32–v0.34 retained set without production or protected
artifact changes. Direct `git ls-remote`, rather than the closing record,
resolved remote `main` and peeled `v0.17.1` to
`f02379f03ccdfd1b019413234f2ad014d169fb04`, the tag ref to annotated object
`14912f134e45277e2b4fd10b7f5bf8b4900ca20d`, and local Git identified that
object as `tag`; the published closing commit's immediate parent remains
release commit `7a621e39a069a1ef26438e841e7bb1ca2f34165b`.

An isolated clone of exact audit child `e0ab6964f76b0a919c5214607ef141eb5b118deb`
passed all **20/20** `ci-local` jobs after two named environment non-results: a
DNS-denied dependency bootstrap and the empty environment that bootstrap left
behind. The passing run measured checklist **261 checked / 3 retracted / 261
matched / 261 commits resolved**, registered invariants **12 rules / 68
controls**, warning-denied current/net/MSRV lanes, shell **348 collected / 347
passed / one named `on_site` skip**, and embedded golden **11/11**. The exact
tree's project-root `./run export-check` passed at **100 derived / 7 required /
153 exported / 2,634,692 bytes**, confirming both the reviewer figure and the
audit-child identity. Two independent real-workspace artifact verifications
matched **332 pins / 2 artifacts**, the exact structural State archive, and
both protected databases in **0.12 s / 0.10 s real**. No publisher request,
scheduler, service, model-profile command, protected database write, remote
ref mutation, or production-source change occurred.

After all **four** Architecture trigger rows and **24** active deferred rows
were refreshed to v0.34, the real active-tree `./run cycle-check` passed with
the exact activation state `governed_export=exempt-open-empty-progress` and
directly measured State at **218,338 / 453,741 bytes** and the manifest at
**192,042 / 1,048,576 bytes**. Clean constrained Python 3.11.4 and 3.12.13
lanes each emitted **348 collected / 348 passed / 0 failed / 0 skipped** and
the same one accepted `StarletteDeprecationWarning`; the repository comparator
emitted exactly `collected=348`, `equivalent=true`, and
`equivalent_passed=348`. With E0's box still open, the complete active-tree
entry point then passed all **20/20** jobs and checklist **261 / 3 / 261 /
261**. The required standalone post-task golden run passed **11/11**, delta
**0**. An earlier active-tree 3.11 attempt, before trigger freshness was
rewritten, failed only the test that requires those v0.34 observations and is
not the passing result.

**G1 — the State-region guard has a circular floor.** Four throwaway copies of
the exact delivered tree were passed to the real `./run cycle-check` entry
point. Renaming `## 5.` to `## 50.` emitted verbatim:

```text
cycle-check: ERROR: STATE.md: external State section references do not resolve: crates/compliance/src/lib.rs:24=§5, crates/ingest/src/arxiv_oai.rs:28=§5, rust-toolchain.toml:31=§5, tools/version_check.py:261=§5, tools/version_check.py:270=§5
cycle-check: FAIL (1 defect(s))
```

Deleting the marker and full permanent tail emitted verbatim:

```text
cycle-check: artifact-boundary: path=STATE.md bytes=162672 boundary=453741 state=bound checked_tree=worktree-over-HEAD-tree:d0fd5bcff81cbdba6111671f415c68ae07f0eb5d timing=not-applicable
cycle-check: artifact-boundary: path=config/protected-artifacts.json bytes=192042 boundary=1048576 state=bound checked_tree=worktree-over-HEAD-tree:d0fd5bcff81cbdba6111671f415c68ae07f0eb5d timing=out-of-scope
cycle-check: PASS (active=v0.33, state=closed, local_tag_refs=verified, runbook=docs/cycles/TASKS-v0.33-EXECUTION.md, progress=docs/cycles/PROGRESS-v0.33.md, artifact_boundaries=bound, state_regions=not-measured, governed_export=bound-with-cycle-ending-audit, closed_execution=31, historical=3)
```

Keeping the marker and §7 while removing §§1–6 emitted verbatim:

```text
cycle-check: ERROR: STATE.md: external State section references do not resolve: .github/workflows/ci.yml:293=§6b, AGENTS.md:149=§6, ARCHITECTURE.md:6=§2, ARCHITECTURE.md:94=§2, ARCHITECTURE.md:510=§6, README.md:640=§6b, crates/compliance/Cargo.toml:7=§6, crates/compliance/src/lib.rs:24=§5, crates/compliance/src/lib.rs:897=§6, crates/ingest/src/arxiv_oai.rs:28=§5, rust-toolchain.toml:31=§5, tools/version_check.py:261=§5, tools/version_check.py:270=§5
cycle-check: FAIL (1 defect(s))
```

Duplicating the permanent-tail marker emitted verbatim:

```text
cycle-check: ERROR: STATE.md: State archival permanent-tail marker required exactly once; found 2
cycle-check: FAIL (1 defect(s))
```

The full-tail deletion separately made `./run version-check` emit exactly
`version-check: ERROR: STATE.md: current run-reference correction yielded zero
extracted current restatements`. That semantic zero-extraction rule is the only
composite floor; the State-region family itself examined nothing and passed.

Every silent early return in the two named functions was enumerated at its
entry point. `check_state_archival_region_contract` has two: an absent status
header returns `None` silently inside this family, although the independent
publication admission check rejects that construction on the delivered repo;
and no marker plus no numbered top-level heading returns `None` silently and is
reachable exactly as the full-tail construction demonstrates. Its other early
returns all append named defects. `check_publication_status` has three silent
early returns: no reachable closed release (reachable in a repository with no
closed runbook, but impossible with the delivered 31); hosted
`verify_local_tag_refs=False` (reachable deliberately after State/header family
admission and bounded to skipping local historical-ref reconciliation); and a
legacy newest release after legacy assertions (reachable for the historical
pre-R-CLOSE protocol, but not when v0.17.1 is newest). Its remaining early
returns append a named defect directly or return only after a called helper has
done so. G1 therefore confirms the finding and authorizes Step 2; it does not
trip the decision gate.

**G2 — a tiny denominator is accepted and the basis has no epoch awareness.**
The complete field-level governed sequence is **2,464,445 → 2,576,273
(+111,828) → 2,556,451 (−19,822) → 2,586,197 (+29,746) → 2,629,379
(+43,182) → 2,617,984 (−11,395) → 2,706,393 (+88,409) → 2,592,441
(−113,952)**. Taking the last field in each tracked progress record—the series
the checker governs—gives **2,576,273 → 2,629,379 (+53,106) → 2,706,393
(+77,014) → 2,592,441 (−113,952)** for v0.30–v0.33. The selected latest
positive pair, v0.31→v0.32, predates the v0.33 State archival; neither the
progress fields nor `cycle-check` carry an archival epoch, so the check cannot
know that.

In a delivered-tree construction, v0.33's governed field was set to
**2,709,393**, making the latest adjacent delta **+3,000**, and the row stated
the exact **290,607 / 3,000 = 96.87-cycle** margin. The real entry point
accepted it verbatim:

```text
cycle-check: PASS (active=v0.33, state=closed, local_tag_refs=verified, runbook=docs/cycles/TASKS-v0.33-EXECUTION.md, progress=docs/cycles/PROGRESS-v0.33.md, artifact_boundaries=bound, state_regions=bound, governed_export=bound-with-cycle-ending-audit, closed_execution=31, historical=3)
```

The rule proves source identity, adjacency, sign selection, and arithmetic; it
does not prove that one adjacent positive delta represents future growth. G2
confirms the finding and authorizes Step 3.

**G3 — two delivered transitions separate steady growth from reclaim.** Exact
delivered exports at v0.31 post-push audit `9625fb1f…`, v0.32 audit child
`70b7f93c…`, and v0.33 audit child `e0ab6964…` measured respectively
**2,654,404**, **2,734,366**, and **2,634,692 bytes**. Repomix file-content
deltas reconcile both delivered transitions:

| component | v0.31→v0.32 | v0.32→v0.33 before archival reclaim | share of latest 77,862-byte steady growth | reclaim mechanism |
|---|---:|---:|---:|---|
| `cycle_check.py` + `invariant_scan.py` | +15,661 | +35,138 | 45.12% | none automatic; only deliberate simplification/removal |
| `version_check.py` | +7,715 | 0 | 0% | none automatic |
| control tests, fixtures, and registry | +11,580 | +15,416 | 19.80% | none automatic; deliberate control retirement only |
| live `STATE.md` before archive | +28,605 | +31,177 | 40.04% | yes, the governed structural archive operation |
| `ARCHITECTURE.md` + `AGENTS.md` | +4,244 | +4,568 | 5.87% | none automatic |
| protected manifest | 0 | +647 | 0.83% | no deletion; append-only pins make growth effectively permanent |
| retained cycle documents | +12,157 | −9,084 | −11.67% | yes, three-cycle retention turns over the oldest pair |

The first pair sums to its exact **+79,962-byte** delivered delta. In the
second pair, the listed components sum to **+77,862 bytes** before reclaim;
the archive removed **177,542 net live-State bytes**, and a **+6-byte**
retention-pattern/serialization change reconciles the exact delivered
**−99,674-byte** transition. Gross growth was not negative; archival reclaim
temporarily hid it.

Against delivered v0.33's **365,308-byte** export margin, the latest positive
delivered denominator gives **365,308 / 79,962 = 4.57 cycles** and the latest
post-archive steady-growth decomposition gives **365,308 / 77,862 = 4.69
cycles**. Current State is **206,530 / 453,741 bytes**; at its latest positive
same-kind **31,177-byte/cycle** growth, the **247,211-byte** remainder is
**7.93 cycles** from the next archive. Averaging the two measured positive
State deltas gives 8.27 cycles, while averaging the two steady export deltas
gives 4.63. Under every named denominator the export ceiling arrives first.
G3 confirms the reviewer order and authorizes Step 4's measurement-only budget
derivation.

**G4 — the ceiling is an internally enforced but externally uncalibrated
proxy.** Exhaustive tracked search found the referent only in the dated v0.28
runbook and progress record: external project-knowledge indexing reported
**2,067 chunks against a 2,000 limit on 2026-07-30** beside a
**4,975,987-byte** export. The live Architecture row retained the 3,000,000-byte
ceiling but no longer stated that referent. `tools/export_check.py` can measure
export bytes, path retention, and exclusions; no repository tool implements
the external chunker, reads a current project-knowledge index, or maps bytes to
chunks. The ceiling is therefore a conservative executable proxy, not a
repository-measurable current capacity fact. G4 records that bound without
moving the number; Step 5 alone owns any operator-selected lever.

**G5 — control churn is material but not approaching its second trigger at a
stable rate.** Across delivered v0.31–v0.33, registered controls are **58 → 61
→ 68**, shifted-existing `expected_line` totals are **36 → 12 → 25**, and the
physical combined sizes of `cycle_check.py` plus `invariant_scan.py` are
**192,695 → 208,356 → 243,494 bytes** (**+15,661**, then **+35,138**). Shifted
counts as a share of controls are **62.07% → 19.67% → 36.76%**. The latest
count is **43 below** the 68 controls it protects; the observed changes are
−24 then +13 rather than a monotonic approach, and even repeating the latest
+13 once would leave 38 below the contemporaneous control count before any new
controls. The schema-change clause fired in prior cycles and was discharged by
emitted mutations; the second clause did not fire and has no defensible linear
arrival rate from these three observations.

**G6 — the export is now the nearest governed byte boundary.** Exact delivered
State leaves **247,211 bytes / 7.93 cycles** on the latest 31,177-byte positive
State denominator. The delivered export leaves **365,308 bytes / 4.69 cycles**
on the latest 77,862-byte pre-reclaim denominator. The manifest leaves
**856,534 bytes / 1,323.85 cycles** on its latest 647-byte positive denominator.
The ranking is therefore export, State, manifest. Exhaustive live-row search
found no current Architecture disposition asserting the old order; the
statement that State is nearest remains only in dated v0.32 State/runbook
history and is not rewritten. This v0.34 observation supersedes it forward.

**v0.33 R-CLOSE — operator-selected governed no-release closure (measured
2026-08-01).** Release disposition: no-release (as of 2026-08-01). The
operator selected `no-release` after the activation-exclusive and published
diffs showed lifecycle/publication controls, focused tests, cycle and
architecture records, retained-cycle configuration, the operator-selected
State archival, and its exact structural manifest pin. No production source,
workflow, dependency, release value, measured runtime behaviour, public route,
response shape, or serialized `/v1/*` value-domain changed. That structural
and archival distance is the reason for the disposition; it is not weakened to
the statement that “nothing shipped.”

The closing runbook binds its governed export row to the last field already
visible in its tree: authenticated candidate
`2edb7694c2c6c1498b3903382c37aef68329150d` at **2,592,441 bytes / 153
files**. The remaining **407,559 bytes / 13.59%** equals **5.29 cycles** on the
latest positive adjacent same-kind basis, v0.31→v0.32 at **77,014
bytes/cycle**. The actual post-archive v0.32→v0.33 transition is **−113,952
bytes**, so the corrected executable format separates the denominator basis
from the v0.33 evaluation field and rejects both a misstated measurement and an
older positive pair. The real closing-tree export is deliberately absent from
the closing record and belongs only in the audit child's non-governing
`cycle-ending review-export audit` field.

Immediately before the close record, `STATE.md` measured **201,569 /
453,741 bytes**, leaving **252,172 bytes**, or **8.09 cycles** at its latest
positive same-kind **31,177-byte/cycle** denominator. The manifest measured
**192,042 / 1,048,576 bytes**, leaving **856,534 bytes**, or **1,323.85
cycles** at **647 bytes/cycle**. Manifest validation reported schema 2 / **2
artifacts / 332 pinned files**; the exact **178,125-byte** State archive
remained pinned at SHA-256
`b9442f7bedf9024351ef0bafe0e6f7a4d58a0883e9c2f81bbbadebfb476d5886`.
Two final complete verifications took **0.12 s / 0.10 s real** and matched all
pins plus both protected databases, so neither manifest trigger fired. The
pre-close checklist passed **260 / 3 / 260 / 260** and did not fall.

Final direct remote readback left evidence ref
`codex/v0.33-evidence-2edb769` at the exact candidate, remote `main` and peeled
`v0.17.1` at published closing commit
`f02379f03ccdfd1b019413234f2ad014d169fb04`, and annotated tag object
`14912f134e45277e2b4fd10b7f5bf8b4900ca20d` unchanged. `version-check`
derived **0.17.1** from every release source, **22** current offline-MSRV
restatements at 1.78, and **3** current release-version restatements. No version
source, tag, `main`, or release ref changed.

Permission reconciliation over activation
`353a17e67c3cac5699f43dd65b15725e3e35d5e1..R-CLOSE` used
`tools/cycle_check.py`, `tools/invariant_scan.py`,
`config/invariant-rules.json`, `shell/tests/**`, `docs/state-archive/**`,
`AGENTS.md`, `ARCHITECTURE.md`, `tools/evidence_artifacts.py`, and the
conditionally authorized `config/protected-artifacts.json`. The conditional
manifest permission activated only for selected Fidelity B. Unused allowances
are `tools/version_check.py`, `tools/export_check.py`, and
`repomix.config.json`. Every release-authority and `forbid` path is unused;
standing status precedence accounts for `STATE.md` and the active
runbook/progress pair. No publisher request, scheduler, service, model-profile
command, protected database write, production-source change, or publication
mutation occurred during close.

Published v0.17.1 reset the divergence count to zero. The measured v0.33
distance contains no runtime-behaviour difference and no public-surface
change, so the count remains zero and no fresh publication-epoch count starts.
This remains a dated operator adjudication whose record shape, freshness, and
cycle identity are executable.

The full pre-commit closing gates passed where the closing protocol permits
them: `cycle-check` reported `state=closed` and governed export `bound`;
`invariant-scan --self-test` passed **12 rules / 68 controls**; constrained
Python 3.11.4 and 3.12.13 each collected/passed **348**, failed 0, skipped 0,
with the same one accepted warning; and golden passed **11/11**. The first
sandboxed Python runs failed eight tests only because loopback binds and `ps`
were denied, and the first sandboxed golden could not bind; those attempts are
`not measured`, while the identical permitted reruns supply the passing
results. The closing box cannot acquire its matching real commit in the
progress record until the closing commit exists; the append-only audit child
resolves that protocol edge and reruns the complete entry point.

Across the final tree, **25** of the **61** activation `expected_line` values
differ and **7** controls were added, for **68 controls protected**. Step 7's
last schema change re-derived **12** shifted existing values plus new emitted
line **2683**. No expected line was calculated by offset. The four author
defects remain visible in the active runbook header. The fourth is the Step 3
format's inability to encode a truthful post-archive decrease while keeping a
positive margin denominator; its real-entrypoint rejection is corrected by
separating the evaluation source from the latest positive adjacent same-kind
basis, without weakening the ceiling or latest-at-close binding.

**v0.33 E0 entering-state reconstruction and G1–G6 dispositions (measured
2026-08-01).** The sole pre-activation worktree item was the operator-supplied
untracked v0.33 runbook. Exact delivered v0.32 HEAD was audit child
`70b7f93c94c67e43f6f4a29ede5823081955f3fa`, whose immediate parent was
closing implementation `86b8db0b4026c23371317c7881dcc9497806c20b`.
Direct `git ls-remote`, rather than a closing-record transcription, resolved
remote `main` and peeled `v0.17.1` to
`f02379f03ccdfd1b019413234f2ad014d169fb04`, the tag ref to annotated object
`14912f134e45277e2b4fd10b7f5bf8b4900ca20d`, and local Git identified that
object as `tag`; the published closing commit's immediate parent is release
commit `7a621e39a069a1ef26438e841e7bb1ca2f34165b`. An isolated clone of the exact
delivered tree measured checklist **254 / 3 / 254 / 254**, rather than the
entering hypothesis's 253, and registered invariants **12 rules / 61
controls**. Its first sandboxed net lane was `not measured` because loopback
bind was denied; the permitted rerun passed. Its protected-artifact lane was
also `not measured` because the intentionally local databases were absent from
the isolated clone; the real workspace supplied the two passing **0.09 s /
0.10 s** measurements. A clean project-root `./run export-check` at exact
audit child `70b7f93c94c67e43f6f4a29ede5823081955f3fa` measured **2,734,366
bytes / 153 files**, confirming the reviewer's inferred tree identity and the
exact **4,979-byte** increase over the recorded 2,729,387-byte closing-tree
export. The activation checker named the governed-export state
`exempt-open-empty-progress`. After all trigger rows were refreshed, the real
complete entry point passed **20/20** with E0's task box still open and
`invariant-scan --self-test` emitted **12/12 rules / 61 controls**. Python
3.11.4 and 3.12.13 each emitted `collected=336`, `passed=336`, `failed=0`, and
`skipped=[]`; the repository comparator, rather than a transcribed total,
emitted `collected=336`, `equivalent=true`, and `equivalent_passed=336`.
The required standalone post-task golden run passed **11/11**, delta **0**.

**G1 — publication-family admission fails open.** At the real delivered-tree
`./run cycle-check` entry point, the absent-header construction emitted:

```text
cycle-check: artifact-boundary: path=STATE.md bytes=350530 boundary=453741 state=bound checked_tree=worktree-over-HEAD-tree:b08c54cfe5b171b504c1a21e9b119db69798f629 timing=not-applicable
cycle-check: artifact-boundary: path=config/protected-artifacts.json bytes=191395 boundary=1048576 state=bound checked_tree=worktree-over-HEAD-tree:b08c54cfe5b171b504c1a21e9b119db69798f629 timing=out-of-scope
cycle-check: PASS (active=v0.32, state=closed, local_tag_refs=verified, runbook=docs/cycles/TASKS-v0.32-EXECUTION.md, progress=docs/cycles/PROGRESS-v0.32.md, artifact_boundaries=bound, governed_export=bound-with-cycle-ending-audit, closed_execution=30, historical=3)
```

The renamed-header construction emitted the same PASS with `STATE.md
bytes=352904`. The absent-file construction emitted:

```text
cycle-check: ERROR: STATE.md: governed artifact is not a file
cycle-check: FAIL (1 defect(s))
cycle-check: artifact-boundary: path=config/protected-artifacts.json bytes=191395 boundary=1048576 state=bound checked_tree=worktree-over-HEAD-tree:b08c54cfe5b171b504c1a21e9b119db69798f629 timing=out-of-scope
```

Thus the publication family itself admits all three empty constructions. The
complete checker rejects the absent file only through the independent governed-
artifact boundary; it borrows no publication-family floor. The composite
`ci-local` entry point rejects absent and renamed headers through
`version-check`, which emitted `STATE.md: expected exactly one versioned As-of
header, found 0`; its absent-file case emitted the filesystem error. That is a
borrowed floor, not `cycle-check`'s own admission rule. `git log -G` measured
the overstating Architecture sentence's introduction in v0.21 release commit
`b7c4b10eb506923e3ea854a32d1dc3f4c83b0eaa` and its later wording change in
v0.22 release commit `a83db73aac3d5ef1e9a427662340eb1eb8a49df1`.
The introducing commit, v0.21 activation
`df9abb939b81a24c038d30522ba63538cc1014e3`, and the current runbook share
the same reviewer identity, so the overstatement is classified as a reviewer
error rather than attributed elsewhere.

**G2 — export margins by measurement kind.** The three comparable series are:

- governed→governed: 2,629,379 → 2,706,393, a **77,014-byte** denominator;
  **293,607 / 77,014 = 3.81 cycles**;
- closing-tree→closing-tree: 2,649,103 → 2,729,387, an **80,284-byte**
  denominator; **270,613 / 80,284 = 3.37 cycles**;
- delivered→delivered: 2,654,404 → measured 2,734,366, a **79,962-byte**
  denominator; **265,634 / 79,962 = 3.32 cycles**.

The governed row can honestly carry governed→governed at close because the
closing tree can see the latest governed progress field but cannot see its own
closing-tree or delivered export. The historical **5.65** calculation performs
its arithmetic correctly on a **51,989-byte mixed-kind subtraction**; it is a
criterion/evaluation-point error, not a raw arithmetic or measurement error.
The dated v0.32 record remains historical evidence and is corrected forward.

**G3 — live and movable regions.** Exact delivered `STATE.md` was **5,368
lines / 352,895 bytes**: immutable status header lines 1–4 were **2,405
bytes**, the only archival-eligible dated append region at lines 5–4,982 was
**306,676 bytes**, and permanent numbered tail lines 4,983–5,368 were
**43,814 bytes**. The only registered current-restatement binding inside the
tail was delivered line 5,320, read by `tools/version_check.py:291–299`.
Derived live, non-historical `STATE §N` consumers were
`.github/workflows/ci.yml:293` (§6b), `AGENTS.md:149` (§6),
`ARCHITECTURE.md:6,94,458` (§2, §2, §6), `README.md:640` (§6b),
`crates/compliance/Cargo.toml:7` (§6),
`crates/compliance/src/lib.rs:24,897` (§5, §6),
`crates/ingest/src/arxiv_oai.rs:28` (§5), `rust-toolchain.toml:31` (§5), and
`tools/version_check.py:261,270` (§5). This corrects the reviewer inventory,
which omitted the workflow and compliance-manifest consumers. There is no
`## 3.` heading and exhaustive search found no live §3 consumer. Historical
cycle and prior-archive references are evidence, not current consumers, and
must be structurally excluded from the live derivation rather than silently
treated as current bindings.

At complete delivered-tree entry points, the over-cut and removed-restatement
constructions made `version-check` reject with `STATE.md: current run-reference
correction yielded zero extracted current restatements`; renamed `## 5.` and
removal of §1, §2, §4, §5, and §6 both made it PASS at 0.17.1. In contrast,
`cycle-check` PASSed all four constructions, reporting only their reduced
artifact bytes. The existing restatement reader therefore protects its own
line, incidentally catches this particular over-cut, and does not define an
eligible archival region or protect section anchors. Step 4 must derive the
header, append, and permanent-tail boundaries from live structure and derive
current external references from tracked files; only then is “dated appends
only” executable rather than asserted.

**G4 — archive fidelity has no reader.** Exhaustive tracked search found
`docs/state-archive/**` only in exclusion/retention prose and in the export and
version-check historical-family exclusions. No tool, test, config, or manifest
pin reads an archive's expected digest, complement, ordering, or truncation.
Git detects an uncommitted mutation and retains history, but after a corrupt
archive is committed no repository check detects that corruption against the
claimed source bytes. The v0.21 archive's recorded SHA-256 and complement are
one-time evidence, not a standing control. A second archive therefore needs
either the same honestly bounded one-time verification or an executable pin;
neither may be described as the other.

**G5 — executable `STATE.md` readers.** `cycle_check.py` reads the publication
header/post-push records and artifact bytes; a valid archival must preserve the
header and newest publication evidence while reducing the byte count.
`version_check.py` reads the versioned header, registered current MSRV
restatement, and tracked floor partition; it permits removal of dated historical
occurrences but requires those live authorities. `audit_deferred.py` scans
`AGENTS.md`, `ARCHITECTURE.md`, `README.md`, and live `STATE.md` for the
forbidden HC1-under-shell-replacement assertion; the proposed dated-region cut
does not change its result. `export_check.py` and Repomix include live
`STATE.md` while excluding `docs/state-archive/**`, so every archived byte is
removed from the export. `invariant_scan.py` creates synthetic State fixtures
for lifecycle controls and its credential scan still sees tracked archive
bytes; it has no archive-fidelity reader. `checklist_audit.py` enumerates cycle
runbooks and does not read `STATE.md`. Executing its real entry point before and
after the measured Option B throwaway cut returned the identical **254 checked
/ 3 retracted / 254 matched / 254 commits resolved**. The same throwaway cut
left `version-check` PASS at 0.17.1 with **22** current MSRV restatements and
**3** release restatements.

**G6 — the two boundaries share one operation.** Live `STATE.md` closing-tree
growth was 289,117 → 321,718 → 352,895 bytes; at the latest same-kind
**31,177-byte** denominator its **100,846-byte** headroom is **3.23 cycles**.
The delivered series 324,290 → 352,895 gives a 28,605-byte denominator and
**3.53 cycles**. Export margins are the G2 same-kind **3.81 governed / 3.37
closing / 3.32 delivered cycles**. The State archival trigger's first clause
explicitly depends on the export-ceiling trigger, and archives are excluded
from the export; therefore one cut disposes pressure on both. The measured
Option B counterfactual removed **178,125 bytes** from each boundary, leaving
live State at **174,770 bytes** and the exact delivered-tree export at
**2,556,241 bytes**. The other measured cut points remain operator choices;
no archive was created or selected during E0.

**v0.33 Step 2 — publication-family admission is fail-closed (measured
2026-08-01).** E0's required fail-before constructions remain recorded above:
the old real `cycle-check` PASSed absent and renamed headers, while an absent
State file was rejected only by the independent artifact reader. Entry-point
tracing then exposed an additional cause: `newest_closed_release()` selected
the newest closed cycle first and returned `None` when that cycle was
`no-release`, instead of continuing to the newest actual release. On the
delivered v0.32 baseline the publication family therefore stopped even before
its State-file and header early returns. The selector now skips later
no-release records and reconciles the newest actual release.

With the fix installed in the same exact three delivered-tree throwaway
constructions, the real entry point emitted these distinct family defects:

```text
cycle-check: ERROR: STATE.md: publication admission header required: STATE.md has no '**As of:**' status header
cycle-check: FAIL (1 defect(s))

cycle-check: ERROR: STATE.md: publication admission header shape: the leading as-of status header is present but does not match STATE_HEADER_RE's required '**As of:**' form
cycle-check: FAIL (1 defect(s))

cycle-check: ERROR: STATE.md: governed artifact is not a file
cycle-check: ERROR: STATE.md: publication admission file required: STATE.md is absent or is not a regular file
cycle-check: FAIL (2 defect(s))
```

The absent-file construction correctly retains the independent artifact defect
and adds its own named publication-admission defect. The check-site comment
records why this parser does not delegate to `version_check.state_version()`:
the latter independently binds the release version, while this family binds
publication status, and either hand-written regex may reject text the other
accepts.

Registered R12 now runs the real `cycle_check.run` entry point over all three
admission constructions, disables each distinct branch, and separately
disables the newest-release selector. Its focused mutation self-test passed
**37/37 R12 controls**; the full registry has **65 controls**. Emitted
self-test findings, not hand arithmetic, re-derived **25 shifted existing
`tools/cycle_check.py` `expected_line` values** and the four new values: the
three admission branches resolve to line **603**, the selector to line **562**.
The shifted-existing count remains below the 65 controls protected. The
Architecture overstatement introduced by the same reviewer in v0.21 is
corrected forward; its dated historical text is not rewritten.

Focused lifecycle tests passed **74/74** on constrained Python 3.11.4 and
independently on 3.12.13. The complete Step 2 `./run ci-local` entry point,
executed with the task box still open, passed all **20/20** jobs and emitted
`invariant-scan` **12/12 rules / 65 controls**. The independently constrained
Python 3.12.13 shell lane and the Python 3.11.4 lane embedded in `ci-local`
each collected/passed **340**, failed **0**, and skipped **0**; the repository
comparator emitted `collected=340`, `equivalent=true`, and
`equivalent_passed=340`. Golden passed **11/11**, delta **0**. No production
source, workflow, dependency, schema, manifest, protected byte, public
response/value-domain state, publication ref, publisher, scheduler, or model
profile changed.

**v0.33 Step 3 — the export margin is a progress-backed same-kind series
(measured 2026-08-01).** The live Architecture row now carries one executable
`governed→governed` series. Its prior term is the last governed field in
`PROGRESS-v0.31.md`, **2,629,379 bytes**; its current term is the last governed
field in `PROGRESS-v0.32.md`, **2,706,393 bytes**. The lifecycle checker reads
both files, requires the current term to equal the row's governed byte marker,
and re-derives **77,014 denominator bytes/cycle**, **293,607 numerator bytes**
under the single 3,000,000-byte ceiling, and **3.81 cycles** after two-decimal
rounding. Closing→closing and delivered→delivered remain legitimate operator
measurements, but cannot occupy the executable row marker because they have no
common in-repository progress authority. The dated v0.32 **5.65** record remains
unchanged historical evidence and the live row corrects it forward.

R12 plants a row whose declared prior term no longer matches its named governed
progress series, runs the real `cycle_check.run` entry point, and disables the
comparison to prove the plant would otherwise be missed. Focused R12 self-test
passed **38/38 controls** and the complete registry now passes **12 rules / 66
controls**. Each mutation's emitted finding re-derived **29 shifted existing
`expected_line` values** and the one new same-kind value at line **2401**; no
line was offset-calculated. The shifted-existing count remains below the 66
controls protected.

Focused lifecycle tests passed **76/76** on Python 3.11.4. The complete Step 3
entry point passed **20/20** with its task box open. Its Python 3.11.4 lane and
the independently permitted Python 3.12.13 lane each collected/passed **342**,
failed **0**, and skipped **0**; the repository comparator emitted
`collected=342`, `equivalent=true`, and `equivalent_passed=342`. An initial
Python 3.12 command without `PYTHONPATH=shell` and a later sandboxed invocation
whose loopback binds and `ps` call were denied are invocation non-results; the
correct, permitted repository command supplies the passing measurement. Golden
passed **11/11**, delta **0**. No production source, workflow, dependency,
schema, manifest, protected byte, public response/value-domain state,
publication ref, publisher, scheduler, service, or model profile changed.

**v0.33 Step 4 — State archival eligibility and external anchors are
executable (measured 2026-08-01).** Before any archive byte moved, the live
State acquired one structural permanent-tail marker. The lifecycle checker now
derives the immutable header from the status paragraph, the eligible dated
append from the bytes between that header and the marker, and the permanent
numbered tail from the marker through EOF. It requires the marker exactly once,
immediately before the first numbered top-level heading, forbids a numbered
top-level heading in the eligible region, and derives headings and gaps without
a hardcoded line, byte figure, or section-number list. With the task box open,
the real entry point reported:

```text
cycle-check: state-region-contract: header_bytes=1933 eligible_bytes=322653 tail_bytes=43858 top_sections=1,2,4,5,6,7 numbering_gaps=3 referenced_sections=2,5,6,6b referenced_gaps=none reference_sites=.github/workflows/ci.yml:293=§6b,AGENTS.md:149=§6,ARCHITECTURE.md:6=§2,ARCHITECTURE.md:94=§2,ARCHITECTURE.md:500=§6,README.md:640=§6b,crates/compliance/Cargo.toml:7=§6,crates/compliance/src/lib.rs:24=§5,crates/compliance/src/lib.rs:897=§6,crates/ingest/src/arxiv_oai.rs:28=§5,rust-toolchain.toml:31=§5,tools/version_check.py:261=§5,tools/version_check.py:270=§5
```

Thus the tracked live inventory resolves every derived reference; `## 3.` is
absent and is referenced by nothing. Cycle records, prior State archives, and
test/control constructions are structurally excluded from this live inventory.
The marker check delegates only the already-owned missing-restatement condition
to `version-check`, so its permanent-tail floor is independently executable
without duplicating the registered MSRV reader.

The four required complete-entry-point constructions were first reproduced
against Step 3. Before the fix, the over-cut and removed-restatement cases each
made `version-check` reject with exactly:

```text
version-check: ERROR: STATE.md: current run-reference correction yielded zero extracted current restatements
```

while `cycle-check` passed both. Renaming `## 5.` and removing §1, §2, §4, §5,
and §6 each made both `version-check` and `cycle-check` pass. After the fix, the
over-cut retained the same sole `version-check` error and `cycle-check` passed
with `state_regions=not-measured`; the removed-restatement construction retained
the same sole error while `cycle-check` passed with `state_regions=bound`. No
duplicate error was added to either existing rejection. Renaming `## 5.` kept
`version-check: PASS (0.17.1)` and made the real lifecycle entry point emit:

```text
cycle-check: ERROR: STATE.md: external State section references do not resolve: crates/compliance/src/lib.rs:24=§5, crates/ingest/src/arxiv_oai.rs:28=§5, rust-toolchain.toml:31=§5, tools/version_check.py:261=§5, tools/version_check.py:270=§5
cycle-check: FAIL (1 defect(s))
```

Removing §1, §2, §4, §5, and §6 kept `version-check: PASS (0.17.1)` and made
the lifecycle entry point emit:

```text
cycle-check: ERROR: STATE.md: State archival permanent-tail marker required exactly once; found 0
cycle-check: FAIL (1 defect(s))
```

R12 removes the marker through the real lifecycle entry point and disables the
new branch. Focused R12 self-test passed **39/39 controls** and the complete
registry now passes **12 rules / 67 controls**. Mutation output re-derived
**30 shifted existing `expected_line` values** plus the new State-region value
at line **2213**; the shifted-existing count remains fewer than the 67 controls
protected. Focused lifecycle tests passed **79/79** on Python 3.11.4. The
complete entry point passed **20/20** with the task box open; constrained Python
3.11.4 and 3.12.13 each collected/passed **345**, failed **0**, and skipped
**0**, and the repository comparator emitted `collected=345`,
`equivalent=true`, and `equivalent_passed=345`. Checklist audit remained fully
matched at **257 / 3 / 257 / 257**. Golden passed **11/11**, delta **0**. No
byte was written under `docs/state-archive/**`, and no production source,
workflow, dependency, schema, manifest, protected byte, public
response/value-domain state, publication ref, publisher, scheduler, service,
or model profile changed.

**v0.33 Step 5 — operator-selected Cut B and Fidelity B completed ahead of the
trigger (measured 2026-08-01).** The operator explicitly selected Cut B through
v0.28 and Fidelity B. Clean pre-cut HEAD was
`1121e90055f2fb189bb71404e8bd93f5b55e0a8b`; its State was **5,679 lines /
372,667 bytes**, SHA-256
`d4af6dda99fded542c19de222df02e3878dbb15c44043b8f7be30092f0c6d248`.
The structural cut began at the v0.28 R-CLOSE block at byte **150,684** and
ended at the permanent-tail marker at byte **328,809**. The resulting
`docs/state-archive/STATE-through-v0.28.md` is **2,888 lines / 178,125 bytes**
at SHA-256
`b9442f7bedf9024351ef0bafe0e6f7a4d58a0883e9c2f81bbbadebfb476d5886`;
the pre-record live State is **2,791 lines / 194,542 bytes** at SHA-256
`4e95f3beed3164610054dfd14df1b5b35a24d31c881b348c53146e250395d0c1`.
Executed byte comparison reported archive plus live **372,667**, prefix equal,
suffix equal, the **1,895-byte** header equal, and full reconstruction equal.

Fidelity B exposed one author-side schema defect before the cut: both required
pre-manifest validators passed, but a synthetic archive pin made the real entry
point exit 2 with:

```text
evidence-manifest: ERROR: pinned_files[331].path: pinned files must live beneath evidence/, observations/, or be an exact registered authorization surface
```

The runbook had offered Fidelity B while forbidding the validator needed to
express it. Its r4 amendment records the reviewer error and narrowly registers
this exact structural archive path; sibling paths and a wrong grade both fail.
Focused manifest tests passed **20/20**, including a one-byte mutation of every
committed pin. The real validator then emitted `schema=2, artifacts=2,
pinned_files=332`; the manifest is **192,042 bytes**, SHA-256
`a5d990462ba59a252c9228db2c4d4532670debbcb7422c8771ef68fc22a0dd2b`.
Two complete `./run verify-artifacts` runs matched all **332** pins and both
protected databases in **0.11 s / 0.10 s real**.

Post-cut lifecycle reported State **194,542 / 453,741 bytes**, eligible region
**148,789 bytes**, permanent tail **43,858 bytes**, and manifest **192,042 /
1,048,576 bytes**, both `bound`. All derived external references still resolved
to §§2, 5, 6, and 6b; §3 remained unreferenced. `version-check` passed exact
**0.17.1** with **22** current offline-MSRV restatements at 1.78 and **3**
release restatements. Checklist remained **258 / 3 / 258 / 258** before and
after the cut with the task box open.

The exact staged post-cut pre-record tree is
`91be7ac3b7c90f5407353136cde8e647f7af2f2f`. The first sandboxed project-root
export attempt was a DNS non-result; the permitted rerun against that unchanged
tree passed at **2,584,353 bytes / 153 files**, retained three cycles, and
excluded the archive and pinned SEC body. The complete entry point passed
**20/20**; Python 3.11.4 and 3.12.13 each collected/passed **346**, failed **0**,
and skipped **0**, and the comparator emitted `collected=346`,
`equivalent=true`, and `equivalent_passed=346`. Golden passed **11/11**, delta
**0**. The archival was performed ahead of its unchanged recurrence trigger
under explicit operator authorization. No production source, workflow,
dependency, runtime behavior, protected database byte, public surface,
publisher, scheduler, service, model profile, publication version, or ref
changed.

**v0.33 Step 6 — exact candidate authenticated on a fresh evidence ref
(measured 2026-08-01).** With the worktree clean at exact candidate
`2edb7694c2c6c1498b3903382c37aef68329150d` and tree
`916db4b88ec9086222913da33fdb3c06a17a5e40`, the operator explicitly
authorized publication to `refs/heads/codex/v0.33-evidence-2edb769`.
The first sandboxed `git ls-remote` was a DNS non-result. Before any push, the
permitted authoritative query exited zero with no matching ref. The one
authorized push created only that fresh ref, and immediate plus final remote
readback each resolved it to the exact candidate.

Workflow-dispatch run **30705340282**, attempt **1**, used branch
`codex/v0.33-evidence-2edb769`, exact candidate SHA, and evidence signing.
`core`, `golden`, `lint`, `msrv`, `net`, `shell/python=3.11`, and
`shell/python=3.12` all passed. Every receipt emission, attestation, bundle
copy, and artifact-persistence step passed; dependency drift skipped under its
declared report-only condition. The unchanged workflow SHA-256 is
`5a7160f15a9eaa57daa9cc8ce666c1a1c2b8cc39728ea2308474e0d66f2b6791`.
The repository's release-grade verifier consumed the downloaded ephemeral
**7-receipt / 7-bundle** set, accepted **7**, rejected **0**, and found the
complete runner matrix. Every accepted certificate binds repository
`jiayanzeng/intel-platform`, workflow
`jiayanzeng/intel-platform/.github/workflows/ci.yml`, source and signer digest
`2edb7694c2c6c1498b3903382c37aef68329150d`, and source ref
`refs/heads/codex/v0.33-evidence-2edb769`. Its temporary **37,297-byte** report
has SHA-256
`6c96a0e04749459e752bef21bc4d4f7781dbc050929dbbb5f76782acd7981196`
and remains outside the repository and protected manifest.

Local Python 3.11.4 and 3.12.13 each collected/passed **346**, failed **0**,
and skipped **0**. Each hosted lane collected **346**, passed **345**, and
skipped the same named `on_site` node
`tests/test_deferred_audit.py::test_on_site_production_measurements_match_committed_receipt`
for reason `on-site production audit requires protected corpora and built
cored`. For each lane the repository comparator emitted `collected=346`,
`equivalent=true`, and `equivalent_passed=346`; no count was transcribed from a
log. The exact candidate passed local `ci-local` **20/20**, all **332** pins and
both protected databases, and golden **11/11** locally and hosted. The first
sandboxed local golden could not bind loopback and was not measured; its
identical permitted rerun passed. The first sandboxed project-root export was
also a DNS non-result; the permitted run measured **2,592,441 bytes / 153
files**, retained exactly three cycles, and excluded the archive and pinned SEC
body.

Final direct remote measurement left the fresh evidence ref exact, remote
`main` and peeled `v0.17.1` at closing commit
`f02379f03ccdfd1b019413234f2ad014d169fb04`, and the annotated tag ref at
object `14912f134e45277e2b4fd10b7f5bf8b4900ca20d`. The published-distance file
list contains only lifecycle documentation, tests, controls, retained-cycle
configuration, and the structural archive pin: no production source, workflow,
dependency, release value, runtime-behaviour, or public-surface change. Step 6
issued no publisher request, ran no scheduler, service, or model-profile
command, and performed no manifest registration.

**v0.32 E0 entering-state reconstruction and gate dispositions (measured
2026-08-01).** The worktree was clean apart from the operator-supplied untracked
v0.32 runbook before activation. The v0.31 post-push audit, closing, release,
and annotated-tag objects were where the runbook placed them. Direct remote
inspection—not the prior closing record—resolved `main` and peeled `v0.17.1`
to closing commit `f02379f03ccdfd1b019413234f2ad014d169fb04`; annotated
object `14912f134e45277e2b4fd10b7f5bf8b4900ca20d` has Git type `tag`, and
the closing commit's immediate parent is release commit
`7a621e39a069a1ef26438e841e7bb1ca2f34165b`.

The clean constrained Python 3.11.4 and 3.12.13 rebuilds each resolved all 21
constraint packages and reported `collected=325`, `passed=325`, `failed=0`,
and `skipped=[]`. Their machine comparison was:

```text
test-population-compare: {"collected":325,"equivalent":true,"equivalent_passed":325,"hosted":{"on_site_skipped":0,"passed":325,"skipped":[]},"local":{"passed":325,"skipped":0},"schema_version":1}
```

The complete `./run ci-local` entry point then passed all **20/20** jobs,
including the loopback-dependent net tests, the same **325** shell population,
and golden **11/11**. A first sandboxed invocation could not bind the net
suite's loopback wire server and was `not measured`; the exact rerun with
loopback permission is the passing gate result. `invariant-scan --self-test`
executed **12/12 rules / 58 controls**. Two independent protected-artifact
verifications measured **331** pins, both protected databases exact, and
complete real times of **0.17 s / 0.10 s**.

**G1 — governed byte facts.** Exhaustive search found no lifecycle comparison
of `STATE.md` against 453,741 bytes or the protected manifest against 1 MiB;
the only executable byte ceiling is the review export's 3,000,000-byte check.
At the activation-audit tree:

- `STATE.md` was **324,290 bytes**, leaving **129,451 bytes**. At the latest
  delivered **+35,173 bytes/cycle** denominator this is **3.68 cycles**; the
  estimate worsened from v0.31 activation's 5.19 cycles.
- `config/protected-artifacts.json` was **191,395 bytes**, leaving **857,181
  bytes** to 1 MiB. Its latest cycle delta is zero, so no finite exhaustion
  follows from that denominator; at the last positive **8,621 bytes/cycle**
  denominator the margin is **99.43 cycles**.
- Exact activation-audit tree
  `7ba89795403b2b8fab84ff53abeba6ad4a220d23` exported **2,617,984 bytes**,
  leaving **382,016 bytes / 12.73%**. At the latest delivered **+70,780
  bytes/cycle** denominator the margin is **5.40 cycles**. v0.31's delivered
  **2,654,404-byte** export had **345,596 bytes / 4.88 cycles** remaining;
  advancing retention reduced the activation export by **36,420 bytes**.

`STATE.md` is therefore the nearest governed byte boundary and is getting
closer. `cycle-check` reported the activation state by the exact exemption name
`exempt-open-empty-progress`.

**G2 — floor-domain closure.** `rust_floor_partition_report` builds its search
alternatives only from the already-derived 1.78 and 1.86 values. In a throwaway
tracked clone, a staged `wrong-floor.md` containing `offline needs >= 1.75`
produced the real function result
`'wrong_floor_rows': [], 'wrong_floor_occurrences': 0` and the real
`./run version-check` still emitted `version-check: PASS (0.17.1)`. A detector
that catches an unknown wrong value without enumerating wrong values needs a
contextual floor-shaped candidate recognizer followed by an explicit accepted
value/classification decision; that widens maintenance to phrasing contexts
and false-positive adjudication. The current bound names only file-level and
within-file history separation, so it does not name its value-closure limit.

**G3 — release-version completeness.** Exhaustive search placed current-version
literals in `ARCHITECTURE.md`, `CHANGELOG.md`, `Cargo.lock`, `README.md`,
`STATE.md`, `apps/cored/Cargo.toml`, the v0.31/v0.32 runbooks and progress
records, `shell/intel_shell/__init__.py`, and `shell/intel_shell/app.py`.
`version-check` directly binds the Cargo manifest, both shell values, the
`STATE.md` header, and newest changelog entry; locked Cargo lanes bind the
package stanza. Dated cycle/State instances are historical or evidence, while
README lines 1, 10, and 14 are unchecked present-tense restatements. In a
throwaway clone of exact v0.31 post-push tree
`9625fb1f7a7af2e85bad8418480b5b89093b707b`, changing README line 1 alone to
`v9.9.9` left `./run version-check`, `./run cycle-check`, and
`./run invariant-scan --self-test` green. Those are every lifecycle entry point
present in both local and hosted shell lanes. The Rust-floor file partition
does not transfer directly to release versions: release values change and live
in heterogeneous contexts, so Step 4 owns a registered present-tense
restatement reader rather than a bare-literal partition.

**G4 — hosted ref convention.** Every observed `codex/*` ref and target was:

- local `codex/v0.23-action-migration`:
  `7ba89795403b2b8fab84ff53abeba6ad4a220d23`;
- remote `codex/v0.23-action-migration`:
  `9625fb1f7a7af2e85bad8418480b5b89093b707b`;
- remote evidence refs v0.24 through v0.30 respectively:
  `a73c042068a367aea22e63e28dfd2f754b65ef9c`,
  `779fbe55ba33dd5d196df391cc9a9eeb3ce0bbb3`,
  `1cd88acd99704cc76c866331e505db446936e469`,
  `f2b5f7a9ded1b21f3815752cc9e310bd29c1478e`,
  `47bb77c19420bf513b53b228e473d4accedc6cc9`,
  `9059ecab338eaaccfd6376ec7ba5e5e22e18c6f4`, and
  `2528498ba7bdce3f280fa1a9c4d6fe266cac05ab`.

There is no v0.31 evidence ref. Downloaded run **30685356489** supplied seven
receipts and seven Sigstore bundles. Executing the repository verifier over all
seven accepted **7/7** with signed source digest
`7a621e39a069a1ef26438e841e7bb1ca2f34165b` and signed source ref
`refs/heads/codex/v0.23-action-migration`. Those signed values are load-bearing;
the branch's current mutable target is not. Fresh-ref nonexistence and readback
can be executed at the Step 6 operation, but no in-tree or hosted checker can
make a mutable remote ref's prior absence durable. The convention therefore
remains an explicit operation-time acceptance criterion; its cycle-qualified
name is human readability, not cryptographic identity.

**G5 — post-closing export reconciliation.** Direct Git blob measurement from
v0.31 release parent to post-push audit found progress growth of **2,729 bytes**
and `STATE.md` growth of **2,572 bytes**. Their exact **5,301-byte** sum equals
the export movement from **2,649,103** to **2,654,404** bytes. This corrects the
entering hypothesis: the tracked progress delta is +2,729 bytes; no separate
two-newline correction is needed at repository-byte level. The cycle-ending
audit should be required whenever a closed cycle's delivered export differs
from its governed figure. A record cannot measure its own tree, so the latest
append's self-contribution remains necessarily undisclosed: for a release that
is the post-push record; for a no-release close it is the audit child itself.
Adding another named field would only recreate the fixed point.

**G6 — divergence firing and reset.** Exhaustive search found freshness,
cycle-identity, population, and carry-forward syntax checks, but no control that
distinguishes a fired trigger from an unfired one or gives the three-cycle
counter a post-publication restart point. v0.32's live observation therefore
says that the trigger fired at v0.31, v0.17.1 publication disposed it, no new
runtime or public-surface difference exists, and reset is undefined pending
Step 5. Firing truth and reset semantics are irreducibly operator adjudications;
the checker can enforce only their dated/cycle-identified record shape.

The activation stale-retention construction produced the predicted rejection
byte-for-byte:

```text
cycle-check: ERROR: repomix.config.json: review-export retention pattern for v0.32 must be 'docs/cycles/{TASKS,PROGRESS}-v0.{[0-9],1[0-9],2[0-9]}{.md,.*.md,-*.md}' to agree with the tracked retained-cycle set; found ['docs/cycles/{TASKS,PROGRESS}-v0.{[0-9],1[0-9],2[0-8]}{.md,.*.md,-*.md}']
```

An earlier invocation while the runbook was untracked stopped before examining
that construction and was `not measured`, not a prediction mismatch. No
publisher request, scheduled process, service, or model-profile command ran;
port 8788 had no listener. Direct remote query found neither historical
`v0.8.0` nor `v0.10.2` tag.

**v0.32 Step 2 — governed artifact byte boundaries (measured 2026-08-01).**
The operator selected crossing as a named reported state requiring a dated
disposition. The active runbook now contains the single machine-readable
authority for both governed paths: `STATE.md` at 453,741 bytes and
`config/protected-artifacts.json` at 1,048,576 bytes. The current governed rows
refer to that authority and no longer restate either numeric boundary;
historical measurements remain dated evidence, not live declarations.

The preimplementation rejection proof used committed construction
`43945ffdb958fcebcfe44141758f99725dd7f2f2` with both boundaries set to one
byte. The old real `./run cycle-check` still returned `PASS`, proving that it
read neither artifact for this purpose. After implementation, the real entry
point read the files directly and reported this below-boundary state against
the named worktree/tree reference:

```text
cycle-check: artifact-boundary: path=STATE.md bytes=332554 boundary=453741 state=bound checked_tree=worktree-over-HEAD-tree:f399244157fd5dba99f6c72e50b6d5c2c99305b6 timing=not-applicable
cycle-check: artifact-boundary: path=config/protected-artifacts.json bytes=191395 boundary=1048576 state=bound checked_tree=worktree-over-HEAD-tree:f399244157fd5dba99f6c72e50b6d5c2c99305b6 timing=out-of-scope
```

The rejection was demonstrated before acceptance. With both authorities
temporarily set to one byte and neither governed row disposed, the same real
entry point rejected both artifacts:

```text
cycle-check: ERROR: STATE.md: measured 332554 bytes at checked_tree=worktree-over-HEAD-tree:f399244157fd5dba99f6c72e50b6d5c2c99305b6, meeting or exceeding governed boundary 1; row 'Second STATE.md archival' requires a dated 'trigger-fired disposition:'
cycle-check: ERROR: config/protected-artifacts.json: measured 191395 bytes at checked_tree=worktree-over-HEAD-tree:f399244157fd5dba99f6c72e50b6d5c2c99305b6, meeting or exceeding governed boundary 1; row 'protected evidence-manifest growth' requires a dated 'trigger-fired disposition:'
cycle-check: FAIL (2 defect(s))
```

Adding explicit dated `trigger-fired disposition:` text to both governed rows
made that same crossed construction pass while reporting
`trigger-fired-disposed` for each artifact. Both constructions were then
restored; the committed manifest bytes were never edited. Focused lifecycle
tests passed **70/70**, including below-boundary, duplicate-authority,
missing-row, crossed-undisposed, and crossed-disposed cases. The constrained
Python 3.11.4 and 3.12.13 suites each reported `collected=330`, `passed=330`,
`failed=0`, and `skipped=[]`; the machine comparator derived
`equivalent=true` and `equivalent_passed=330`. An earlier sandboxed 3.11 run
could not bind loopback servers or execute `ps` and was `not measured`; the
exact permission-enabled rerun is the passing result.

Registered R12 now plants the one-byte crossed-undisposed construction. The
real self-test passed **12/12 rules / 59 controls**. Nine existing
`expected_line` values shifted and were re-derived from the emitted production
locations; the new control resolves to `tools/cycle_check.py:2016`. The change
adds no archive, manifest edit, dependency, production source, or local/hosted
lane job. The manifest timing trigger remains governed by its dated row and is
explicitly outside this byte check's scope.

After the code, tests, live rows, and State record were present, the complete
`./run ci-local` entry point passed all **20/20** jobs. Its measurements include
warning-denied **146** workspace tests, **32** net ingest tests plus **30** net
`cored` tests, clean clippy/fmt/ShellCheck, locked Rust 1.78, shell **330/330**,
registered self-test **12 rules / 59 controls**, protected artifacts exact, and
embedded golden **11/11**. The standalone post-task `./run golden` also passed
the same **11/11** assertions with no document, id, distance, signal, citation,
license, or entitlement delta.

**v0.32 Step 3 — Rust-floor contextual value closure (measured
2026-08-01).** The E0 construction proved that the old exact-value detector
could not see a newly tracked refuted floor statement. The shipped detector now
unions its existing derived-value literal scan with two registered line-local
context predicates: a minimum claim after a Rust/offline subject, and a floor
followed by a value. Those predicates contain the general Rust-version grammar
and no list of refuted answers. The check's own emitted bound now names both
limits: classification remains file-level, so identical text cannot distinguish
current prose from dated history inside one classified file; value closure is
the derived floor literals plus the registered contexts, with arbitrary version
numerals outside those contexts excluded.

The rejection preceded acceptance. A tracked-file override under
`tools/export_check.py` carrying E0's refuted figure in the registered minimum
context failed with a `floor-shaped context value(s)` / zero-classification
error. The same file carrying that numeral only as a release version remained
outside the detector, demonstrating that the context construction was read and
that arbitrary numerals were not swept in. The exact current tracked-set run
recognized eleven context-only occurrences, but they occurred only in files
the prior derived-value detector already matched: newly matched files **0**,
new classification decisions **0**. Historical records retaining refuted
figures stayed byte-unchanged and remained classified by the existing dated
historical families.

Focused version-check tests passed **10/10**. The previous zero-extraction,
normalized pin-disagreement, stale registered-restatement, and unclassified
derived-literal tests continued to reject. R12 gained a distinct contextual
value-closure construction; its real mutation self-test passed **12/12 rules /
60 controls**. Three existing `tools/version_check.py` `expected_line` values
shifted and were re-derived from the successive emitted failures to **449,
449, and 583**; the new context control resolves to **568**. The binding remains
inside `./run version-check`, already executed by both local and hosted shell
lanes. No toolchain pin, workflow, harness, evidence topology, dependency,
production source, dated historical record, or release value changed.

The clean constrained Python 3.11.4 and 3.12.13 suites each collected and
passed **333**, with no failures or skips; the machine comparator derived
`equivalent=true` and `equivalent_passed=333`. The complete local entry point
passed all **20/20** jobs, including registered self-test **12 rules / 60
controls** and embedded golden **11/11**. The standalone post-task
`./run golden` also passed the same **11/11** assertions with no corpus or
public-response delta.

**v0.32 Step 4 — present-tense release-version completeness (measured
2026-08-01).** G3 established that heterogeneous release-version prose cannot
be derived honestly from bare literals: the same value appears in current
headings and tag descriptions as well as dated historical evidence. The shipped
shape therefore retains the five syntax-derived executable authority readers
and adds the named `RELEASE_VERSION_RESTATEMENTS` semantic registry with an
executed reader. It extracts exactly the three current README statements and
requires each to equal the canonical executable value. `ARCHITECTURE.md` §8
now delegates authority and restatement membership to `./run version-check`
instead of maintaining a second hand-written source list.

The disagreement rejection preceded acceptance. Replacing only the README
project-heading value with `9.9.9` made the focused lane pass its planted test
by observing the production error `README.md: project heading states 9.9.9,
but executable release authorities derive 0.17.1`. A separate zero-extraction
test proves the registry is read rather than merely declared. The real current
entry point reports **3** registered restatements, all deriving **0.17.1**, and
focused version tests passed **13/13**. README and every executable version
authority remained byte-unchanged; dated older releases were not rewritten.

Registered R12 now disables the production mismatch branch and catches the
resulting missed `stale-readme-version` plant. No existing control site moved;
the new site's expected line **695** was derived from the emitted self-test
failure. An initial population comparison exposed two invalid expected-line
records—the deliberate new placeholder and an accidentally edited R3 value—and
failed with two tests in both lanes. Restoring R3 to its emitted line **1** and
binding the new site to **695** made the real self-test pass **12/12 rules / 61
controls**. The clean constrained Python 3.11.4 and 3.12.13 populations then
each collected and passed **336**, with zero failures or skips; the repository
comparator derived exact equivalence at **336**. No shell source, release value,
tag, dependency, workflow, toolchain pin, or evidence topology changed.

With the task box still open, the complete `./run ci-local` entry point passed
all **20/20** jobs: warning-denied Rust remained **146** workspace tests plus
the focused SEC diagnostic and **32 + 30** net tests, locked Rust 1.78,
clippy/fmt/ShellCheck, shell **336/336**, registered self-test **12 rules / 61
controls**, protected artifacts exact, and embedded golden **11/11**. The
standalone post-task `./run golden` then passed the same **11/11** assertions
with no document, id, distance, signal, citation, license, entitlement, or
public-response delta. An earlier `ci-local` invocation after prematurely
checking the task box stopped at the expected missing-progress-entry defect and
was not the acceptance run; the successful run used the runbook-prescribed
open-box state before the implementation commit existed.

**v0.32 Step 5 — publication-epoch reset and honest non-controls (measured
2026-08-01).** G6's decision gate tripped for executable trigger truth: the
published-release row is the only artifact asserting whether a runtime
difference exists, so a checker reading that row has no independent fact with
which to contradict it. Building a firing/reset check would therefore be a
self-report dressed as a control. Step 2 already supplies the executable half
for the two direct byte boundaries. Step 5 adds no code or R12 control and
records that limit explicitly.

The contract now defines the missing reset symmetrically. Successful authorized
publication resets the consecutive closed-cycle count to zero at its published
closing commit. Only a measured runtime-behaviour difference in the subsequent
unpublished distance starts a fresh count at the first later closed cycle that
carries it. Pre-publication cycles, a difference already shipped, documentation,
evidence, lifecycle-only changes, and a closed cycle without a measured runtime
difference do not start or continue the count; any public-surface change still
fires immediately. v0.17.1 publication therefore reset the v0.31 count to zero,
and v0.32 has not started a new count.

The general cycle-ending export audit remains deliberately zero-or-one. When an
operator measures the closing tree and finds a difference, the field truthfully
discloses it; absence claims neither a zero delta nor that measurement occurred.
`cycle-check` cannot create the operator-local export, so requiring the field
only on a self-reported difference would be vacuous, while requiring it always
would claim a measurement the entry point never performed. v0.32's own runbook
independently requires its closing-tree audit. The audit append's own byte
contribution remains necessarily undisclosed; another field would recreate the
self-measurement fixed point. No executable control exists under this ruling,
no `expected_line` moved, and the registered total remains **12 rules / 61
controls**.

With the task box open, `./run ci-local` passed all **20/20** jobs, including
warning-denied **146** workspace tests, the focused SEC diagnostic, **32 + 30**
net tests, locked Rust 1.78, clean clippy/fmt/ShellCheck, shell **336/336**,
registered self-test **12 rules / 61 controls**, protected artifacts exact, and
embedded golden **11/11**. Clean constrained Python 3.11.4 and 3.12.13 runs each
collected/passed **336**, failed **0**, and skipped **0**; the direct repository
comparison derived `equivalent=true` and `equivalent_passed=336`. The standalone
post-task `./run golden` passed the same **11/11** assertions with delta zero.

**v0.32 Step 6 — exact-candidate hosted authentication on a fresh neutral ref
(measured 2026-08-01).** The clean candidate was
`1caace6e2470b51c371d67598b756a48f93d7968`. Before any ref movement,
`git ls-remote` returned no entry for
`refs/heads/codex/v0.32-evidence-1caace6`; remote `main` and peeled
`v0.17.1` both resolved to closing commit
`f02379f03ccdfd1b019413234f2ad014d169fb04`, while annotated tag object
`14912f134e45277e2b4fd10b7f5bf8b4900ca20d` remained distinct. The operator
explicitly approved publishing the measured candidate to that new ref. The
post-push readback resolved it to the exact candidate, with the three published
identities unchanged.

Workflow-dispatch run **30693555131**, attempt **1**, executed at that exact
branch and SHA. All seven executable jobs passed; dependency drift was the sole
skip under its unchanged report-only condition. The workflow SHA-256 remained
`5a7160f15a9eaa57daa9cc8ce666c1a1c2b8cc39728ea2308474e0d66f2b6791`,
and its job/matrix and receipt populations remained the prior cycle's seven
identities: `core`, `golden`, `lint`, `msrv`, `net`, `shell/python=3.11`, and
`shell/python=3.12`. Every receipt, attestation, bundle, and persistence step
passed.

The repository's release-grade verifier consumed the downloaded ephemeral
**7 receipts / 7 Sigstore bundles**, required attestations, accepted **7**
signed identities, rejected **0**, and found no matrix defect. Every accepted
identity binds repository `jiayanzeng/intel-platform`, workflow
`jiayanzeng/intel-platform/.github/workflows/ci.yml`, source digest
`1caace6e2470b51c371d67598b756a48f93d7968`, and source ref
`refs/heads/codex/v0.32-evidence-1caace6`. Its temporary **37,235-byte** report
had SHA-256
`c374b139010343c35ea96d233634b0566675ca967d7a7c88774377cb8b504fcb`;
it and the downloaded artifacts remain outside the repository and manifest.

The exact candidate's local Python 3.11.4 and 3.12.13 lanes each collected and
passed **336**, with zero failures and skips. Each hosted lane collected
**336**, passed **335**, and skipped the same named, reasoned `on_site` node
`tests/test_deferred_audit.py::test_on_site_production_measurements_match_committed_receipt`.
For both lanes the executed repository comparator derived `collected=336`,
`equivalent=true`, and `equivalent_passed=336`; no figure was transcribed from
the runner log.

The candidate passed local `ci-local` **20/20**, all **331** pins and both
protected archives matched, and golden passed **11/11** locally and hosted.
Its project-root export measured **2,706,393 bytes / 153 files**, leaving
**293,607 bytes / 9.79%** and retaining exactly v0.30–v0.32. A final post-run
remote query again found the evidence ref at the candidate, `main` and peeled
`v0.17.1` at the published closing commit, and the annotated object unchanged.
No manifest registration occurred.

**v0.32 R-CLOSE — governed no-release closure (operator authorization and
measurement 2026-08-01).** Release disposition: no-release (as of 2026-08-01).
The operator selected `no-release` after the activation-exclusive and published
release diffs showed only documentation, lifecycle controls, focused control
tests, and cycle records. No production source, workflow, manifest, dependency,
schema, version value, public route, response shape, serialized value domain,
or runtime behaviour changed. This measured structural distance is the reason
for the disposition; it is not restated as the weaker claim that “nothing
shipped.” Published v0.17.1 remains current, and all v0.32 implementation and
audit commits are intentionally unreleased.

The closing tree keeps the Architecture governed-export row bound to the last
field it can already see: authenticated candidate
`1caace6e2470b51c371d67598b756a48f93d7968` at **2,706,393 bytes / 153
files**, **293,607 bytes / 9.79%** below the ceiling. It does not project or
backfill its own export. The closing tree's real export is measured only after
that tree exists and belongs in the distinct non-governing cycle-ending audit
field in the append-only child. Immediately before closure, `STATE.md` measured
**352895 bytes**, leaving **100846 bytes** to its
453,741-byte governed archival boundary, and `checklist-audit` passed **253
checked / 3 retracted / 253 matched / 253 commits resolved**.

Close-time artifact validation again found schema 2 / **2 artifacts / 331
pinned files** in the byte-unchanged **191,395-byte** manifest. Two complete
verifications took **0.19 s / 0.11 s real** and matched both protected
databases, so neither manifest trigger fired. Direct remote inspection resolved
the fresh evidence ref to the authenticated candidate, remote `main` and peeled
`v0.17.1` to published closing commit
`f02379f03ccdfd1b019413234f2ad014d169fb04`, and the annotated tag object
unchanged. Neither deferred historical tag was present. No publication ref was
moved.

Every declared permission is reconciled over activation commit
`9ecc8c17ffe5349a38f41df78a02acf7c46bd9ca` exclusive through R-CLOSE. Used
`allow` paths are `tools/cycle_check.py`, `tools/version_check.py`,
`tools/invariant_scan.py`, `config/invariant-rules.json`, `shell/tests/**`,
`AGENTS.md`, and `ARCHITECTURE.md`. Unused `allow` paths are
`tools/export_check.py` and `repomix.config.json`. All eight declared
`release_authority` patterns are unused and every actual version value is
unchanged. Every `forbid` path is unused; standing precedence admits only
`STATE.md` and the active runbook/progress pair. In particular, every closed
cycle document, `.github/workflows/**`, `run`, `tools/model_profiles.py`,
`config/protected-artifacts.json`, every production source family, and every
publisher/scheduler configuration path is byte-unchanged across the governed
range.

G1 directly measured all three governed byte quantities and identified
`STATE.md` as nearest. G2 executed contextual Rust-floor recognition against a
wrong value before accepting an explicit value-closure bound. G3 executed the
registered present-tense release-version reader and its disagreement/zero-match
rejections. G4 classified fresh-ref absence as an operation-time criterion and
Step 6 satisfied it with signed digest and source-ref identity. G5 reconciled
the prior closing delta and preserved the non-governing audit-child boundary.
G6 defined the publication-epoch reset and correctly declined to present
runtime classification self-report as an executable control. The live reading
is that v0.17.1 publication reset the divergence count to zero and the
documentation/lifecycle-only v0.32 distance starts no fresh count; no public
surface change exists.

The runbook's three draft defects remain classified as **reviewer errors**:
(1) v0.31 specified a partition without specifying the Rust-floor detector's
domain; (2) it hand-enumerated release authorities and omitted README's current
restatement; and (3) it dropped the fresh evidence-ref requirement and allowed
release evidence to bind a reused v0.23-named branch. They are not findings and
are not silently dropped. Across Steps 2–4, **12** existing `expected_line`
values were re-derived from real emitted self-test output—nine in Step 2 and
three in Step 3. Step 4 shifted zero existing sites; Step 5 shipped no control.

**v0.31 R-CLOSE publishes the authenticated v0.17.1 correction under the
two-commit tagged-close protocol (operator authorization and measurement
2026-08-01).** Release disposition: release (as of 2026-08-01). Exact release
commit `7a621e39a069a1ef26438e841e7bb1ca2f34165b` is the immediate parent of the
closing tree. The annotated `v0.17.1` tag targets that closing tree and moves
atomically with remote `main`; the tag-object identity and closing-commit hash
are deliberately absent from this tree and belong in the first dated post-push
append.

**v0.17.1 post-push forward verification (measured 2026-08-01).** Atomic
publication moved remote `main` and annotated `v0.17.1` together. Remote
inspection resolves `main` and the peeled tag to closing commit
`f02379f03ccdfd1b019413234f2ad014d169fb04`; annotated tag object
`14912f134e45277e2b4fd10b7f5bf8b4900ca20d` has Git type `tag`, and the
closing commit's immediate parent is release commit
`7a621e39a069a1ef26438e841e7bb1ca2f34165b`.

- **Post-push verification date:** 2026-08-01
- **Post-push release:** `v0.17.1`
- **Post-push annotated tag object:** `14912f134e45277e2b4fd10b7f5bf8b4900ca20d`
- **Post-push closing commit:** `f02379f03ccdfd1b019413234f2ad014d169fb04`
- **Post-push hosted run:** `30686179773`

Post-push run **30686179773**, attempt **1**, completed successfully on remote
`main` at exact closing commit `f02379f03ccdfd1b019413234f2ad014d169fb04`.
All seven executable jobs passed; dependency drift skipped under its declared
report-only condition. Every receipt, attestation, bundle, and persistence step
passed. The core job validated schema 2 / 2 artifacts / 331 pinned files;
golden passed **11/11**; net passed **32 ingest + 30 cored**; current and locked
Rust 1.78 builds/tests, clippy, fmt, and the complete shell lifecycle gates all
passed.

Each hosted shell lane collected **325**, passed **324**, and skipped the same
one named, reasoned `on_site` test. Against exact-closing-tree local **325
passed / 0 skipped**, `tools/test_population.py` independently derived this
output for both Python 3.11 and 3.12:

```text
test-population-compare: {"collected":325,"equivalent":true,"equivalent_passed":325,"hosted":{"on_site_skipped":1,"passed":324,"skipped":[{"node_id":"tests/test_deferred_audit.py::test_on_site_production_measurements_match_committed_receipt","reason":"on-site production audit requires protected corpora and built cored"}]},"local":{"passed":325,"skipped":0},"schema_version":1}
```

The exact published closing tree produced an operator-local review export of
**2,649,103 bytes / 153 files**, retained exactly v0.29–v0.31, and passed **100
derived / 7 required** plus both excluded-content controls. That is **+19,724
bytes** from the governed release-parent measurement of 2,629,379 bytes. This
is the distinct non-governing cycle-ending audit; it does not supersede the
architecture row or its exact-tree governed progress field. The audit child is
locally gated and deliberately not part of post-push run 30686179773; under the
accepted cycle-ending rhythm it becomes hosted-verified at the next
publication.

The release commit and evidence candidate are the same object. Hosted
workflow-dispatch run **30685356489**, attempt **1**, executed the unchanged
workflow at exact SHA `7a621e39a069a1ef26438e841e7bb1ca2f34165b` on
`refs/heads/codex/v0.23-action-migration`. All seven executable jobs passed;
dependency drift skipped under its report-only condition. Release-grade
verification required paired attestations, accepted **7** signed identities,
rejected **0**, and found the complete runner matrix. The temporary verifier
report was **37,157 bytes**, SHA-256
`0ab408757fa870fac8629b24607c59e2092533e60a45af66f6f648fa514b4e6b`,
and was not registered or committed.

Each hosted Python 3.11 and 3.12 lane collected **325**, passed **324**, and
skipped exactly
`tests/test_deferred_audit.py::test_on_site_production_measurements_match_committed_receipt`
under the `on_site` marker with reason `on-site production audit requires
protected corpora and built cored`. Against local **325 passed / 0 skipped**,
the repository comparator independently reported for both lanes:

```text
test-population-compare: {"collected":325,"equivalent":true,"equivalent_passed":325,"hosted":{"on_site_skipped":1,"passed":324,"skipped":[{"node_id":"tests/test_deferred_audit.py::test_on_site_production_measurements_match_committed_receipt","reason":"on-site production audit requires protected corpora and built cored"}]},"local":{"passed":325,"skipped":0},"schema_version":1}
```

The exact release parent also passed local `ci-local` **20/20**, clean
constrained Python 3.11.4 and 3.12.13 at **325/325**, standalone golden
**11/11**, and the focused threshold-16/feature-floor-26 identity diagnostic at
**201 input / 201 kept / 0 dropped**, including **200 SEC kept / 0 dropped**.
The hosted workflow SHA-256 remained
`5a7160f15a9eaa57daa9cc8ce666c1a1c2b8cc39728ea2308474e0d66f2b6791`.
Hosted and local evidence checks found schema 2, 2 protected archives, and 331
unchanged pinned files; local exact-byte verification matched both archives.
Golden remained byte-identical at **11/11**. No publisher request or harvest
command appeared in the complete hosted log search.

The operator-local export at exact release parent
`7a621e39a069a1ef26438e841e7bb1ca2f34165b` passed **100 derived / 7 required /
153 exported / 2,629,379 bytes**, retained exactly v0.29–v0.31, and rejected
both excluded byte classes. It leaves **370,621 bytes / 12.35%** beneath the
ceiling. The movement from the prior governed CLOSE-POINT tree is **+43,182
bytes**; v0.30 delivered to the v0.31 release parent moved **+45,755 bytes**.
The machine-readable governed progress field binds the written architecture
figure to that exact release tree. The later exact closing-tree export is a
different measurement and belongs only in the non-governing cycle-ending audit
child.

The divergence trigger fires at the close because the corrected internal
`/ingest` raw-boundary behavior is still absent from the published v0.17.0 tree
and v0.31 becomes the third consecutive post-correction closed cycle after
v0.29 and v0.30. No public-surface change exists. The operator selected patch
v0.17.1 before implementation and separately authorized publication after the
exact release commit passed hosted evidence. The authorized atomic publication
therefore disposes the fired trigger rather than projecting a fourth
unpublished cycle.

Every G1–G6 answer remains measured. G1 executed both commits of the real
v0.30 closing pair and Step 3 repaired the impossible comparison by binding a
release close to its already-existing parent measurement and separating the
closing-tree audit. G2 exhaustively classified the tracked Rust-floor set and
Step 4 made the previously unread historical exclusion a consumed path-family
authority. G3 executed the skipped-cycle real-Git construction and Step 5 made
the configured pattern consume the one tracked retained set without an export
or brace-glob matcher. G4 constrains the written figure against the single
ceiling authority while correctly leaving real-byte and excluded-content
measurement operator-local. G5 enumerated and preserved satisfying assignments
for no-release and tagged-release shapes. G6 retains exactly **two**
delivered-to-delivered observations with opposite signs, **−8,342** and
**+61,837**, while the later **+45,755** release-parent movement remains a
separately named point. Retention can return bytes to the export; live State
still has no reclaim mechanism.

The three runbook-header errors remain reviewer errors. The first authored an
unsatisfiable closing equality and is corrected by CLOSE-POINT. The second
accepted a declaration with no reader and is corrected by EXCLUSION-READ. The
third placed disposition after hosted evidence and is corrected by selecting
v0.17.1 before implementation, then authenticating the release commit itself.
They are neither product findings nor retraction proposals. The accepted
retraction count remains **3**. Planted-control line numbers were re-derived
only from emitted mutated-tree output: Step 3 **9**, Step 4 **3**, and Step 5
**24**, for **36 total**.

Scope use is reconciled by path. Lifecycle implementation used
`tools/cycle_check.py`, `tools/export_check.py`, `tools/version_check.py`,
`tools/invariant_scan.py`, `config/invariant-rules.json`,
`shell/tests/test_cycle_check.py`, `shell/tests/test_version_check.py`,
`repomix.config.json`, `AGENTS.md`, and `ARCHITECTURE.md`. Release-authority
use was `Cargo.lock`, `apps/cored/Cargo.toml`,
`shell/intel_shell/__init__.py`, `shell/intel_shell/app.py`, `CHANGELOG.md`, and
`README.md`. Root `Cargo.toml`, every `crates/*/Cargo.toml`, and every other
`apps/*/Cargo.toml` were unused. Standing record paths were `STATE.md` and the
active TASKS/PROGRESS pair. Every forbid remained unchanged; the two shell
version files are reachable through the declared release-authority precedence.
No closed cycle document was edited, moved, renamed, or deleted.

The cycle changed no route, response shape, public value domain, dependency
resolution beyond cored's workspace version, schema, entitlement or licensing
outcome, publisher configuration, scheduler configuration, cadence, model
profile, manifest, protected byte, observation, fixture, golden input, or
production behavior source. No publisher request, scheduler run, model-profile
command, manifest registration, historical tag movement, or publication-ref
movement occurred before the authorized closing action.

**v0.31 VERSION-SET prepares the exact v0.17.1 release commit
(measured 2026-08-01).** The gate did not trip because Step 2 selected release
v0.17.1. `version-check` read one agreeing value from each of its five
authorities:

```text
apps/cored/Cargo.toml: 0.17.1
shell/intel_shell/__init__.py: 0.17.1
shell/intel_shell/app.py: 0.17.1
STATE.md: 0.17.1
CHANGELOG.md: 0.17.1
```

README's release identity and active-cycle links also moved to v0.17.1/v0.31.
The toolchain command `cargo check --workspace` regenerated `Cargo.lock`; its
only lockfile diff is cored **0.17.0 → 0.17.1**. The command compiled cored
0.17.1 successfully. The lockfile was neither deleted nor hand-edited, and all
subsequent locked current and Rust 1.78 checks/tests passed.

The product-surface classification is measured against annotated v0.17.0's
tree. `apps/cored/src/main.rs` and `crates/core/src/lib.rs` are byte-unchanged.
The FastAPI source changes only its declared version literal. The sole
behavioural production diff is the already-measured
`crates/store/src/sqlite.rs` coverage-boundary correction: held-newest and
incoming-oldest raw strings now use the same archive recency ordering even for
a misordered slice. `/ingest` keeps the same route, response shape, fields,
types, and outcome domain. Every `/v1/*` route, response shape, serialized
field, and value domain is unchanged. Dependency resolution beyond the
workspace cored version, schema, entitlements, licensing outcomes, and archive
rows are unchanged, so patch classification remains correct.

The focused shipped identity diagnostic printed threshold **16**, feature
floor **26**, **201 input / 201 kept / 0 dropped**, including **200 SEC kept /
0 dropped**. The permission-complete full matrix passed **20/20** with **146**
workspace and **62** net tests, both warning-denied Rust lanes, clean
clippy/fmt/ShellCheck, registered self-test **12 rules / 58 controls**, shell
**325/325**, protected artifacts, and embedded golden **11/11**. Clean
constrained Python 3.11.4 and 3.12.13 rebuilds each passed **325**, failed **0**,
skipped **0**, and retained the same one warning. The comparator reported:

```text
test-population-compare: {"collected":325,"equivalent":true,"equivalent_passed":325,"hosted":{"on_site_skipped":0,"passed":325,"skipped":[]},"local":{"passed":325,"skipped":0},"schema_version":1}
```

Standalone golden passed **11/11**, delta **0**. No tag or local/remote release
ref was created, moved, or deleted, and nothing was pushed. The Step 6 checkbox
and progress entry deliberately do not appear in the release tree: Step 7 must
measure this exact commit, and the specific R-CLOSE protocol requires the
closing record to be its immediate child. Those lifecycle records therefore
land in that closing child, not in an intervening audit commit.

**v0.31 RETENTION-ONE binds the configured pattern to one tracked retained set
(measured 2026-08-01).** The decision gate did not trip. G3's cheap shape is
achievable without parsing or matching the brace glob: `export-check` now
derives cycle-document membership once from `git ls-files`, and
`cycle-check` imports that same retained-path authority and formats the one
configured exclusion boundary from its earliest retained execution runbook.
No export exists or is read in either automated rejection fixture. The task
gate therefore contains every acceptance criterion.

Rejection ran before acceptance. The new skipped-cycle test executed against
the old checker with active synthetic cycle `v1.2.4`; the old entry point
returned **0** and the test failed its required `1` assertion. The construction
tracks retained execution/progress pairs for `v1.2.1`, `v1.2.2`, and
`v1.2.4`, deliberately omitting `v1.2.3`, while configuring the old arithmetic
pattern. After implementation, the skipped-cycle case and the existing stale
pattern case passed **2/2**. The new diagnostic names the corrective boundary:

```text
must be <derived pattern> to agree with the tracked retained-cycle set; found <configured patterns>
```

The throwaway test asserts that no `repomix-output-*.xml` exists. It uses a
real initialized Git index for the retained-set derivation. A deliberately
explicit synthetic authority remains confined to generic Gitless unit
fixtures; the skipped-cycle test carries a sentinel that selects production
Git derivation, so the acceptance construction cannot pass through the test
double. Full focused cycle/export/invariant tests passed **95/95**.

Registered R12's existing retention control now plants both
`stale-retention-pattern` and `skipped-cycle-retained-set`; suppressing the
guard exposes both names. This expands the reconstructible failure covered by
the existing control rather than adding a duplicate control, so the full
self-test remains **12 rules / 58 controls**. Every shifted line was derived
from emitted mutated-tree output: **24** R12 `cycle_check.py` controls moved,
including the joint retention failure at line **1151**. No expected line was
advanced arithmetically.

The permission-complete `./run ci-local` passed **20/20**, including **146**
workspace tests, **62** net tests, warning-denied and Rust 1.78 lanes, clean
clippy/fmt/ShellCheck, shell **325/325**, protected artifacts, and embedded
golden **11/11**. Clean constrained Python 3.11.4 and 3.12.13 rebuilds each
passed **325**, failed **0**, skipped **0**, and retained the same one warning.
The executed comparator reported:

```text
test-population-compare: {"collected":325,"equivalent":true,"equivalent_passed":325,"hosted":{"on_site_skipped":0,"passed":325,"skipped":[]},"local":{"passed":325,"skipped":0},"schema_version":1}
```

Standalone golden passed **11/11**, for delta **0**. G3's earlier statement
that only operator-local `export-check` caught the skipped-cycle construction
is now superseded prospectively: `cycle-check` rejects it before any export is
created. The task changes no route, public value domain, dependency, schema,
manifest, protected byte, production source, publisher state, scheduler state,
version authority, tag, or ref.

**v0.31 EXCLUSION-READ makes the historical-floor declaration load-bearing
(measured 2026-08-01).** The decision gate did not trip. The implementation
does not add a local or hosted job, change either executable offline pin, alter
a toolchain file, or change evidence topology. It lives in `version-check`,
which the existing local matrix and hosted shell job already execute. The task
gate therefore contains every acceptance criterion.

Rejection ran before acceptance. With the two acceptance tests present against
the old module, the focused file reported **5 passed / 2 failed** because no
partition reader existed. After implementation, the focused file passed
**7/7**, and an explicit planted tracked `tools/export_check.py` floor
statement was rejected with:

```text
tools/export_check.py: Rust floor literal(s) yielded zero file-level classifications
```

The implemented reader derives **559 tracked paths** from `git ls-files`. It
derives the literal values from the three existing normalized offline pins and
the already-declared, explicitly unexecuted net-floor source; neither is
written. The implementation-tree scan found **75 literal-bearing files / 662
bounded literal occurrences**, **0 unclassified files**, and **6
multiply-classified files**. The six remain `.github/workflows/ci.yml`, `run`,
`AGENTS.md`, `README.md`, `STATE.md`, and `rust-toolchain.toml`, exactly the
E0 file set.

The declared precedence is executable authority → registered current
restatement → derived Python control construction → historical family.
Authority and restatement paths come from their existing registries; control
construction is derived from executable Python use of `offline_msrv_report`;
and `OFFLINE_MSRV_HISTORICAL_EXCLUSIONS` is now a tuple of real path patterns
read by the partition. The check's own emitted bound is:

```text
file-level only; within-file current restatements cannot be separated from dated historical quotations by identical literal text
```

That residual is deliberate: the six mixed files are classified at file
granularity, and no claim is made about identical lines within them. No dated
historical cycle, State archive, evidence, or observation file was rewritten.
Tests added no hard-coded expected floor value.

Registered R12 now plants an unclassified tracked file and proves the guard
rejects it. The full self-test passed **12 rules / 58 controls**. Real mutated
tree output re-derived **3** shifted `expected_line` values: the two existing
offline controls now emit at line **397**, and the new partition control emits
at line **484**. Combined focused version/invariant tests passed **29/29**.

The permission-complete `./run ci-local` passed **20/20**, including **146**
workspace tests, **62** net tests, warning-denied and Rust 1.78 lanes, clean
clippy/fmt/ShellCheck, shell **324/324**, protected artifacts, and embedded
golden **11/11**. Clean constrained Python 3.11.4 and 3.12.13 rebuilds each
passed **324**, failed **0**, skipped **0**, and retained the same one warning.
The first sandboxed Python 3.11 install was a DNS-denied non-result; its
permission-complete retry passed. The executed comparator reported:

```text
test-population-compare: {"collected":324,"equivalent":true,"equivalent_passed":324,"hosted":{"on_site_skipped":0,"passed":324,"skipped":[]},"local":{"passed":324,"skipped":0},"schema_version":1}
```

Golden delta is **0**. The task changes no route, public value domain,
dependency, schema, manifest, protected byte, production source, publisher
state, scheduler state, version authority, tag, or ref.

**v0.31 CLOSE-POINT binds the governed export at the exact checked tree
(measured 2026-07-31).** The decision gate did not trip: E0 executed the
v0.30 closing implementation commit failing while its audit child passed, so
the finding remains the unsatisfiable two-commit rule and requires a checker
correction. The task gate covers every acceptance criterion because it governs
that complete closing sequence, both reported open exemptions, the closed
comparison and its ceiling, the cycle-ending audit path, and the registered
rejection controls.

Rejection ran before acceptance. With the new expectations planted against the
old checker, the focused governed-margin suite reported **5 passed / 3 failed**:
the old function returned `bound` instead of
`bound-with-cycle-ending-audit`, returned `bound` for an audit placed before
the governed measurement, and exposed no `MAX_EXPORT_BYTES` authority. After
the implementation, the same family passed **8/8**. The complete real-fixture
release construction then passed **9/9** focused tests and exercised these
four points:

- release commit `R`: active/open,
  `governed_export=exempt-open-latest-at-close`;
- closing child `C`: closed, `governed_export=bound`;
- annotated-tag checkout of the same `C`: closed,
  `governed_export=bound`;
- first post-push descendant: closed,
  `governed_export=bound-with-cycle-ending-audit`.

The fixed point uses no closed exemption. At each closed tree the architecture
row equals the last governed measurement already visible in that exact tree.
A release `C` may add the measurement of its already-existing parent `R`
beside the agreeing row. A later audit records the closing-tree export only
under the distinct exact field
`cycle-ending review-export audit`, after the last governed field, so it does
not supersede the comparison. The existing closed-empty construction still
fails, the existing stale-row construction still fails, and both existing
open states retain their named exemptions. There is therefore no closed commit
at which a figure is unbound and no later-tree value a cycle may select
opportunistically.

The same entry point now imports the sole 3,000,000-byte
`MAX_EXPORT_BYTES` authority and rejects a written governed figure above it.
Its emitted error says explicitly that the comparison constrains the written
figure at the checked tree and does not measure an export. Operator-local
`export-check` remains the only control over actual Repomix bytes, retained
paths, and excluded content.

Registered R12 now executes the superseded figure, written-figure ceiling, and
misordered cycle-ending-audit failures. The self-test passed **12 rules / 57
controls**, with R12 at **29** controls. Real fail-before output re-derived
**9** expected-line values: **7 shifted existing values** and the **2 new
registered values**. The emitted mappings were trigger-boundary controls
`1519 → 1526` twice; governed latest-at-tree `1863 → 1913`; new ceiling
`1869`; new audit ordering `1898`; trigger freshness `1665 → 1672` three
times; and deferred carry-forward `2041 → 2093`.

Focused lifecycle tests passed **64/64** and invariant-scanner tests passed
**22/22**. Full `ci-local` passed **20/20** with the Rust populations and
warning gates named in the header. Both constrained shell lanes collected and
passed **322**, skipped **0**, and the comparator emitted:

```text
test-population-compare: {"collected":322,"equivalent":true,"equivalent_passed":322,"hosted":{"on_site_skipped":0,"passed":322,"skipped":[]},"local":{"passed":322,"skipped":0},"schema_version":1}
```

Embedded golden passed **11/11**, delta **0**. The workflow, manifest,
production source, protected bytes, version authorities, and publication refs
remain unchanged.

**v0.31 DISPOSITION-FIRST selects patch release v0.17.1 before implementation
(operator-selected 2026-07-31).** The operator selected `release v0.17.1`.
The recorded reason is to ship the order-independent internal boundary
derivation together with three cycles of executable binding corrections, not
merely because the gates are green. The selection makes the release-shaped
Step 6–Step 8 ordering available; it does not itself authorize Step 8's
separate publication act.

The classification was remeasured rather than inherited. The unpublished
distance was compared with the published v0.17.0 tree for routes, response
shapes, serialized `/v1/*` value domains, dependencies, and schema. None
moved. The measured runtime difference remains bounded to which raw boundary
string can appear in one internal loopback `/ingest` diagnostic for a
misordered window. Therefore neither the named-surface rule nor the public
value-domain criterion fires, and **patch** is the correct class.

At the decision tree, `./run version-check` reported all five authorities still
at **0.17.0**:

```text
apps/cored/Cargo.toml: 0.17.0
shell/intel_shell/__init__.py: 0.17.0
shell/intel_shell/app.py: 0.17.0
STATE.md: 0.17.0
CHANGELOG.md: 0.17.0
```

The release-authority diff from E0 audit commit
`46e22f20ad1f87f7c7f4f2369fc16898cbdb3bdf` was empty. Remote-tracking
`origin/main` and the peeled v0.17.0 tag both remained
`4af2841816dd3e43fb8423153b91aa22ccb87537`; annotated tag object
`df4fc3b044ca12335e773dcc0b9bdd4e0db90afd` was unchanged. No version
authority, version value, tag, `main`, release ref, or publication ref moved in
this decision step.

**v0.31 E0 rebuilds the entering state and settles G1–G6 (measured
2026-07-31).** The pre-activation tracked tree was clean apart from the
operator-supplied untracked v0.31 runbook. HEAD was v0.30 audit commit
`5af3209bbab4116f15bfdef10c1e17befbf27e63`; its immediate parent was closing
commit `00ad3fe1390bac5d6b848581550c88d12dd2ea8e`. Remote `origin/main` and the
peeled v0.17.0 tag both resolved to
`4af2841816dd3e43fb8423153b91aa22ccb87537`; local `main` was
`eb2d9df...`, and HEAD was 60 commits ahead of and zero behind remote main.
Activation implementation commit
`f8141496c571da85b8dd7a5e022534b95bf561d8` contains only the supplied
runbook, the active declaration, its progress skeleton, and the retention
pattern correction. Audit commit
`9ed9f9e8086f703d9d349878e6fe14320e5e7b9d` records it. E0 began from a
clean worktree, and the task gate covers every acceptance criterion because
all are entering-state or local-gate measurements.

Before correcting the stale retention pattern, the real entry point emitted
the predicted line byte-for-byte:

```text
cycle-check: ERROR: repomix.config.json: review-export retention pattern for v0.31 must be 'docs/cycles/{TASKS,PROGRESS}-v0.{[0-9],1[0-9],2[0-8]}{.md,.*.md,-*.md}'; found ['docs/cycles/{TASKS,PROGRESS}-v0.{[0-9],1[0-9],2[0-7]}{.md,.*.md,-*.md}']
```

There was no prediction mismatch. The activated real entry point then
reported `governed_export=exempt-open-empty-progress`. That is exactly the
open-cycle branch required when the active progress record has no governed
measurement; it is an exemption, not a closed-cycle pass.

**G1 — the v0.30 latest-at-close construction is unsatisfiable across its real
two-commit close.** A no-hardlink throwaway clone ran the real checker at each
commit. At closing implementation commit
`00ad3fe1390bac5d6b848581550c88d12dd2ea8e`, it exited 1 and emitted:

```text
cycle-check: ERROR: ARCHITECTURE.md: governed review-export row is superseded: row=2576273, latest_progress=2464445, tree=e7b2c58814e2223d9899b83b3f3491344ce85337
cycle-check: FAIL (1 defect(s))
```

At audit child `5af3209bbab4116f15bfdef10c1e17befbf27e63`, it exited 0 and
emitted:

```text
cycle-check: PASS (active=v0.30, state=closed, local_tag_refs=verified, runbook=docs/cycles/TASKS-v0.30-EXECUTION.md, progress=docs/cycles/PROGRESS-v0.30.md, governed_export=bound, closed_execution=28, historical=3)
```

`ARCHITECTURE.md` is byte-identical across the pair. The later progress append
alone makes the 2,576,273-byte field visible. Therefore the closing value
cannot satisfy the implementation commit, the earlier value cannot satisfy
the audit child after its current measurement lands, and neither truthful
value satisfies both evaluation points.

**G2 — E0 found the unused exclusion tuple was not a rule; EXCLUSION-READ now
executes the available file-level partition with explicit precedence.**
Exhaustive `git ls-files` search at
activation audit tree `9ed9f9e8086f703d9d349878e6fe14320e5e7b9d` found **75
tracked files / 683 occurrences** of `1.78` or `1.86`.
`OFFLINE_MSRV_HISTORICAL_EXCLUSIONS` has exactly one occurrence, its
declaration at `tools/version_check.py:270`; no importer or reader exists.
The complete classes are:

- executable authorities: `run` and `.github/workflows/ci.yml`;
- registered current restatements: those two files plus `AGENTS.md`,
  `README.md`, `STATE.md`, `rust-toolchain.toml`,
  `crates/compliance/Cargo.toml`, `crates/compliance/src/lib.rs`,
  `crates/ingest/src/arxiv_oai.rs`, and
  `crates/store/examples/cosine_bench.rs`;
- control constructions: `shell/tests/test_version_check.py` and
  `tools/invariant_scan.py`;
- dated historical families: all literal-bearing `docs/cycles/**`,
  `docs/state-archive/**`, `CHANGELOG.md`, the two literal-bearing
  `evidence/**` reports, the literal-bearing `observations/**` report, and the
  historical clauses within `.github/workflows/ci.yml`, `AGENTS.md`,
  `README.md`, `STATE.md`, and `rust-toolchain.toml`.

There are **0 unclassified files**. Six files are multiply classified:
`.github/workflows/ci.yml` is authority, current restatement, and history;
`run` is authority and current restatement; `AGENTS.md`, `README.md`,
`STATE.md`, and `rust-toolchain.toml` are current restatement and history.
Authority → current restatement → control construction → historical family is
a complete deterministic file-level partition. Within those six mixed files,
present-tense versus dated-history membership is not decidable from the
identical literals alone. That within-file residual is distinct from, and does
not reopen, the zero-gap file-level result. EXCLUSION-READ later made this
classification executable in `version-check`: the historical tuple is now
read as real path patterns, control constructions are derived from executable
Python use, an unclassified tracked file raises, and the same six mixed files
remain under the declared precedence.

**G3 — arithmetic retention and the real runbook set can diverge inside
`v0.x`.** A distinct-seed full Git construction made v0.33 active with no
v0.32 and a closed synthetic v0.31. The real checker exited 0:

```text
cycle-check: PASS (active=v0.33, state=open, local_tag_refs=verified, runbook=docs/cycles/TASKS-v0.33-EXECUTION.md, progress=docs/cycles/PROGRESS-v0.33.md, governed_export=exempt-open-empty-progress, closed_execution=29, historical=3)
```

The real operator-local export entry point reached its checks and exited 1:

```text
export-check: ERROR: missing retained cycle document: docs/cycles/PROGRESS-v0.30.md
export-check: ERROR: missing retained cycle document: docs/cycles/TASKS-v0.30-EXECUTION.md
export-check: FAIL (2 defect(s); derived_sources=100, exported=151)
```

An initial sandboxed Repomix attempt failed DNS resolution and is explicitly a
non-result; the permission-complete rerun above is the measurement. Only
operator-local `export-check` catches this reachable skipped-cycle
construction. `cycle-check` passes, and neither local nor hosted automated
matrix contains `export-check`.

**G4 — a figure-level ceiling check is implementable but deliberately
narrow.** Exhaustive search found four `export-check` command/usage occurrences
in `run`, zero in `ci_local_jobs`, zero in the workflow, and the sole
`MAX_EXPORT_BYTES` authority in `tools/export_check.py` (definition,
comparison, and result formatting). `tools/cycle_check.py` does not currently
read it. An already-automated `cycle-check` can import that one authority and
reject a recorded governed figure over the ceiling. Such a check constrains
what the repository claims at the exact checked tree. It does **not** create or
measure a Repomix export, enumerate exported paths, test retained documents,
or detect excluded pinned SEC/state-archive bytes. The operator-local
`export-check` remains the only real-byte control.

**G5 — evaluation points in both closing shapes are now explicit.** Under the
current rule, a no-release closing implementation commit is closed and runs
the comparison against the last pre-existing progress field; for the truthful
new closing figure it is unsatisfiable, as G1 executed. Its audit child is also
closed and runs the comparison after the new field appears; it is satisfiable
with the new row value. No single truthful row value satisfies both points.

For a release, the untagged release commit `R` is still open, so the comparison
is exempt (`exempt-open-latest-at-close` once prior measurements exist).
Closing child `C` is closed and compares the row with the closing record's
last visible governed field; assigning both to the export measured on `R` is
satisfiable. The annotated-tag checkout reads the same `C` tree and remains
satisfiable. The first post-push descendant again evaluates the closed active
cycle and remains satisfiable while its required State/progress append adds no
new governed-export field. A different later governed field would supersede
the unchanged row and fail. The Step 3 correction must therefore repair the
no-release implementation point without breaking `R`, `C`, tagged `C`, or the
post-push descendant.

**G6 — the export has a reclaiming mechanism; State does not.** The exact
activation audit tree
`9ed9f9e8086f703d9d349878e6fe14320e5e7b9d` exported **153 files /
2,544,715 bytes**, retained exactly v0.29–v0.31, reported **100 derived / 7
required**, and left **455,285 bytes / 15.18%** headroom. The delivered series
is v0.28 **2,530,129**, v0.29 **2,521,787** (−8,342), and v0.30
**2,583,624** (+61,837): three points but only **two**
delivered-to-delivered observations, with opposite signs. Activation is a
separate v0.30-delivered-to-v0.31-activation observation of **−38,909**.
Those observations do not establish one monotonic growth rate.

Using the latest positive delivered export delta, the export ceiling is
455,285 / 61,837 = **7.36 cycles** away. Activation `STATE.md` was **289,117
bytes** against its **453,741-byte** archival boundary; using the latest State
growth of 31,695 bytes, that boundary is 164,624 / 31,695 = **5.19 cycles**
away and is nearer under those explicitly named denominators. Three-cycle
retention returns old cycle-document bytes to every new export; no mechanism
returns bytes to live `STATE.md` before another archive.

The entering gates are green. `./run ci-local` passed **20/20** with **146**
workspace and **62** net tests, clean warning-denied builds, locked Rust 1.78,
clippy, fmt, ShellCheck, byte-compile, embedded golden **11/11**, and all
artifact checks. Standalone golden passed **11/11**, delta **0**.
`invariant-scan --self-test` passed **12 rules / 55 controls**. Focused SEC
identity measured **201 input / 201 kept / 0 dropped**, including **200 SEC
kept / 0 dropped**. Clean constrained Python 3.11.4 and 3.12.13 lanes each
collected/passed **317**, failed **0**, skipped **0**, and retained the same one
warning. The executed comparator reported:

```text
test-population-compare: {"collected":317,"equivalent":true,"equivalent_passed":317,"hosted":{"on_site_skipped":0,"passed":317,"skipped":[]},"local":{"passed":317,"skipped":0},"schema_version":1}
```

Schema validation reported **2 artifacts / 331 pinned files** in the unchanged
**191,395-byte** manifest. Two permission-complete
`./run verify-artifacts` executions took **0.10 s / 0.10 s real** and matched
both databases. `checklist-audit` passed **239 checked / 3 retracted / 239
matched / 239 commits resolved** before E0's checkbox. The four governed
architecture rows and all 22 deferred rows now carry v0.31 measurements. E0
changed no checker, so **0** planted-control expected-line values were
re-derived.

**v0.30 R-CLOSE records the operator-selected governed no-release disposition
(authorized and measured 2026-07-31).** The operator selected `no-release` and
placed the published-to-working-head difference under a new governed trigger:
**the unpublished distance contains a measured runtime behaviour difference
persisting across three consecutive closed cycles, or acquires any
public-surface change**. The dated v0.30 observation is **persisted two of three
(v0.29, v0.30) since the v0.28 correction; no public-surface change is present;
the trigger has not fired**.

The bounded difference is real. For a misordered incoming window, published
v0.17.0 can place the wrong raw boundary string in one internal `/ingest`
diagnostic field. No route, response shape, `/v1/*` value domain, dependency,
schema, or public surface moved, so patch classification would apply if the
implementation were released. Publication is nevertheless not authorized:
the authenticated candidate is a no-release tree, every actual version
authority and value is byte-unchanged, and no RE-MEASURE ran at a release
commit. One declared `release_authority` path is not byte-identical:
`crates/compliance/Cargo.toml` corrects only its explanatory offline-floor
comment from the refuted 1.75 to the executable 1.78 value.

Immediately before closure, remote `main` and the peeled v0.17.0 tag both
resolved to `4af2841816dd3e43fb8423153b91aa22ccb87537`, annotated tag object
`df4fc3b044ca12335e773dcc0b9bdd4e0db90afd` was unchanged, and neutral ref
`refs/heads/codex/v0.30-evidence-2528498` resolved to
`2528498ba7bdce3f280fa1a9c4d6fe266cac05ab`. No tag, `main`, release ref,
publisher request, scheduler run, cadence change, or model-profile command
occurred.

The exact fixed-point R-CLOSE implementation-tree export passed **100 derived /
7 required / 153 exported** at **2,576,273 bytes**, leaving **423,727 bytes /
14.12%** below the **3,000,000-byte** ceiling. It retained exactly v0.28,
v0.29, and v0.30 TASKS/PROGRESS pairs and excluded both the pinned SEC RSS body
and every `docs/state-archive/**` byte. The R-CLOSE implementation State file
measures **289,117 bytes**, below its **453,741-byte** second-archive boundary
with **164,624 bytes** remaining.

The export history now contains four measured points and **three derived
observations**: v0.28 delivered **2,530,129**, v0.29 delivered **2,521,787**
(**−8,342**), v0.30 activation audit
`e7b2c58814e2223d9899b83b3f3491344ce85337` measured **2,464,445**
(**−57,342**), and the R-CLOSE implementation tree measured **2,576,273**
(**+111,828** intra-cycle). The first two observations are
delivered-to-next-activation intervals; the third is activation-to-close.
Their differing scope and signs do not support treating them as one growth
rate.

Every declared scope path is reconciled. Used `allow` paths are
`tools/cycle_check.py`, `tools/version_check.py`, `tools/invariant_scan.py`,
`config/invariant-rules.json`, `crates/store/src/sqlite.rs`,
`shell/tests/**`, `AGENTS.md`, `ARCHITECTURE.md`, and
`rust-toolchain.toml`. Unused `allow` paths are `tools/export_check.py`,
`crates/**/tests/**`, and `repomix.config.json`. Only the
`crates/*/Cargo.toml` release-authority pattern is used, for the comment
correction above; the other seven release-authority patterns and every actual
version value are unchanged. Every forbidden path is unused.
`.github/workflows/**` stayed byte-identical. The wholesale `docs/cycles/**`
forbid protected every closed cycle document; standing precedence admitted
only the active runbook and progress record. `STATE.md` is the remaining used
standing lifecycle path.

G1–G6 retain measured answers. G1 executed and bound the derived forward-
boundary family. G2 executed the 1.78 extraction and false-restatement
rejection; operator outcome 1 leaves the unexecuted 1.86 claim deferred. G3
executed the real v1.0/v1.3 checker/export matrix. G4 bound the governed export
row to the append-only progress authority and named its fixed-point audit
delta. G5 produced three entry points and two interval observations rather
than a rate; the closing measurement adds one separately identified
activation-to-close observation. G6 consolidated the two byte-identical SQL
clauses into one compile-time declaration after proving the shared
construction can reject drift.

The four draft defects remain reviewer errors: the unenumerated nine-MSRV-site
claim, calling a reconstruction the real retention checker, declaring no
latest-at-close control after reading only two assertions, and claiming the
complete checker ran against a construction without its required evidence or
Git history. Across MARGIN-BIND and ORDER-CONST, **11** existing
`expected_line` values were re-derived from real self-test output: six in
`tools/cycle_check.py` and five in `crates/store/src/sqlite.rs`.

Immediately before closure, `checklist-audit` passed **238 checked / 3
retracted / 238 matched / 238 commits resolved**. Close-time artifact
validation passed schema 2 with **2 artifacts / 331 pinned files** in the
unchanged **191,395-byte** manifest; two complete checks took **0.12 s / 0.09 s
real** and matched both protected databases. The final local lane passed
**20/20**, both constrained Python lanes passed **317 collected / 317 passed /
0 skipped** with the same one accepted warning, `invariant-scan` passed **12
rules / 55 controls**, and standalone plus embedded golden passed **11/11**,
delta **0**.

**v0.30 RE-MEASURE authenticates the exact candidate on a neutral ref without
publishing (measured 2026-07-31).** Steps 2–5 were complete, so the decision
gate did not trip. Candidate
`2528498ba7bdce3f280fa1a9c4d6fe266cac05ab` had an empty worktree and passed
the complete **20/20** local entry point before push. Its workflow SHA-256,
`5a7160f15a9eaa57daa9cc8ce666c1a1c2b8cc39728ea2308474e0d66f2b6791`,
was byte-identical to v0.29's authenticated workflow. It was pushed only to
`refs/heads/codex/v0.30-evidence-2528498`.

Workflow-dispatch run **30611170866**, attempt **1**, used that exact head SHA
and branch. Core, golden, lint, MSRV, net, shell 3.11, and shell 3.12 passed;
dependency drift skipped under the unchanged report-only condition. The hosted
core job verified schema 2 with **2 artifacts / 331 pinned files**, and hosted
golden passed **11/11**.

The release-grade audit required attestations and verified seven receipt/bundle
pairs. It accepted **7** identities, rejected **0**, found an empty matrix
finding set, and marked the single-run matrix complete across core, golden,
lint, MSRV, net, and both shell matrices. Every receipt bound the repository,
workflow signer, candidate digest, neutral source ref, and GitHub-hosted runner
policy. The temporary report measured **37,000 bytes**, SHA-256
`3a0f54257029b7299d4ff699278b2fda34f56fb5ae64eb378646f54e28d8fada`,
and recorded **5 deferred / 2 promoted / 0 implemented deferred subsystems**.
Exact-path re-derivation passed **7** rows, **5** source dispositions, and
**7** triggers with release-grade attestations required.

For each shell lane, `tools/test_population.py` independently derived:

```
{"collected":317,"equivalent":true,"equivalent_passed":317,"hosted":{"on_site_skipped":1,"passed":316,"skipped":[{"node_id":"tests/test_deferred_audit.py::test_on_site_production_measurements_match_committed_receipt","reason":"on-site production audit requires protected corpora and built cored"}]},"local":{"passed":317,"skipped":0},"schema_version":1}
```

The one hosted skip is named, reasoned, and marked `on_site`; each local lane
passed 317 with zero skips. The candidate's two complete artifact
verifications passed in **0.11 s / 0.10 s real**. The manifest remains exactly
**331 pins / 191,395 bytes**. In accordance with this cycle's scope, the
downloaded receipts, bundles, and generated report stayed outside the
repository: **no manifest registration occurred**. Post-run remote inspection
found only the neutral ref at the candidate; remote `main` and the peeled
v0.17.0 tag remained
`4af2841816dd3e43fb8423153b91aa22ccb87537`, and annotated tag object
`df4fc3b044ca12335e773dcc0b9bdd4e0db90afd` remained unchanged. No publisher
request, scheduler execution, production source, dependency, public contract,
schema, manifest, protected byte, version authority, release tag, or
publication ref changed.

**v0.30 ORDER-CONST states the archive SQL order once at compile time
(measured 2026-07-31).** The decision gate did not trip. A `macro_rules!`
construction expands one literal ordering clause into the production
coverage-boundary query and the test-side SQL derivation with `concat!`; it
performs no runtime formatting or allocation and changes no query predicate,
parameter, ordering term, or limit. Exact search found the clause once and two
macro call sites. The task diff contains no `apps/cored/src/main.rs` or
`crates/ingest/src/**` path.

Rejection ran before acceptance. An initial focused `--exact` spelling matched
zero tests and is explicitly a non-result. The corrected focused test passed
**1/1**; changing only the shared SQL clause's `published_raw` direction from
descending to ascending then failed **0/1**, with the SQL-derived id order on
the left and Rust-derived order on the right. Restoring descending made the
same cross-implementation test pass **1/1**. The unchanged
`coverage_boundary_uses_archive_order_for_a_misordered_window` test also passed
**1/1**.

The SEC identity-guard diagnostic measured **201** aggregate inputs, **201
kept**, and **0 dropped**: the required **200 SEC kept / 0 dropped** plus the
one non-SEC fixture document. The refactor shifted five existing
`sqlite.rs` planted-control positions, all re-derived from real self-test
output: R1 `780 → 793`; R5 `230 → 242`, `229 → 241`, and `829 → 842`; and R7
`397 → 410`. The R5 line-33 control did not move. All six store controls
re-executed, R12 remained **27** controls, and the complete self-test passed
**12 rules / 55 controls**. Across MARGIN-BIND and ORDER-CONST, **11** existing
expected-line values have now been re-derived.

The first complete local gate stopped at lifecycle validation because the
deferred action said `Steps 4 and 5`, which did not contain a literal
discharging `Step N`. Correcting it to `Step 4 and Step 5` made the complete
result pass all **20/20** jobs. The first sandboxed Python 3.12 run passed 309
and failed eight solely because loopback binds and `ps` inspection were denied;
the authorized rerun passed **317/317**. Python 3.11 passed **317/317**.
Standalone golden passed **11/11**, delta **0**. The `/ingest` response shape
and every `/v1/*` value domain are unchanged. No production behavior,
dependency, public route, schema, manifest, protected byte, publisher
configuration, scheduler state, version authority, tag, or ref changed.

**v0.30 MARGIN-BIND makes latest-at-close executable and names its residual
(measured 2026-07-31).** The decision gate did not trip:
`docs/state-archive/**` and `config/protected-artifacts.json` are absent from
the task diff. This step changes how one live row is bound; it archives and
registers nothing.

The content rule is deliberately narrower than trigger freshness. Only the
`ARCHITECTURE.md` subject beginning `review-export size and retention bound`
is content-bound. Every other governed subject remains explicitly outside
content-binding scope because its heterogeneous external fact has no common
repository authority; its date and active-cycle identity checks remain in
force. The covered row now carries a machine byte marker, and the checker
first binds that marker to the row's visible `export of **N bytes**` value.
At close it independently binds the row to the last append-only progress field
of the form `tree=<40 hex>; bytes=<digits>`. One implementation cannot satisfy
both sides by merely restating the row.

The empty-record state is explicit. Before the task audit entry existed, the
real active entry point passed with
`governed_export=exempt-open-empty-progress`; an open cycle can still acquire a
later close-time measurement. A focused construction with the same empty
record in closed state produced the required error because the exemption
expires at close. A present open-cycle field takes the separately named
`exempt-open-latest-at-close` path, while closed state requires and compares
the last field. The required workflow assigns the first machine-readable field
to the separate audit append written only after the implementation commit
exists. It is deliberately absent from this implementation tree and is not
claimed as current here; that append records the already measured activation
audit tree `e7b2c58814e2223d9899b83b3f3491344ce85337` at **2,464,445 bytes**.

The operating contract now states the fixed point symmetrically. The governed
figure is measured on the last tree measurable when the row is written,
regardless of whether it increased or decreased. The one progress entry
appended after the closing commit is the named **cycle-ending audit delta**;
it is recorded separately and is not a newer governed measurement. v0.29's
measured instance was **+4,965 export bytes**, exactly the size contribution
of that one audit append. A later negative or positive delta must be disclosed
with its sign rather than used to choose a preferred direction.

Rejection ran before acceptance. Focused tests rejected both a superseded
figure and a closed empty record **2/2**. R12 then rejected its
`superseded-export-figure` mutation at the new line-1863 marker. The new fifth
module-global forward boundary depends on trigger identity and remains
automatically covered by the derived boundary registry. The edit shifted
**six existing** `cycle_check.py` control values, all re-derived from real
self-test output: two boundary controls `1500 → 1519`, three freshness
controls `1646 → 1665`, and the carry-forward control `1873 → 2041`.
The new margin control is registered at 1863. The resulting distribution is
**22** controls into `cycle_check.py` and **6** into `sqlite.rs`; R12 passed
**27** and the full self-test passed **12 rules / 55 controls**.

The first complete lifecycle-test run passed 57 and failed two old fixture
assumptions: the identity-order fixture had not initialized the fifth boundary,
and the zero-population fixture did not clear the new export trigger. The first
correction attempt contained an indentation error and did not collect tests.
After correcting both fixtures and the indentation, the complete file passed
**59/59**. The complete result passed all **20/20** local jobs and Python
3.11.4 plus 3.12.13 at **317/317** each. Standalone golden passed **11/11**,
delta **0**. No dependency, production behavior, public contract, route,
schema, protected byte, publisher configuration, scheduler state, version
authority, tag, or ref changed.

**v0.30 FLOOR-BIND derives the offline floor and records the net-floor
residual (measured 2026-07-31).** The operator selected outcome 1 on
2026-07-31: bind the executable offline 1.78 floor and retain the net 1.86
floor as an explicitly unexecuted claim. This is the cheapest honest outcome:
it binds the evidence already authorized in both lanes without changing a
toolchain pin, adding a hosted job, or altering evidence topology. The decision
gate did not trip. `run` and `.github/workflows/**` were read but are absent
from the task diff.

The existing `version-check` entry point extracted three executable offline
pins: two raw `1.78.0` strings from `run` and one raw `1.78` string from the
hosted MSRV job. Explicit normalization produced one derived value, `1.78`.
Each authority is independently nonempty or the check fails. A named,
hand-maintained registry binds **22** current restatements to that value.
There is no honest general-purpose text derivation that can distinguish
present authority from dated quotation, so
`OFFLINE_MSRV_HISTORICAL_EXCLUSIONS` permanently names the excluded historical
families: cycle documents, State archives, `CHANGELOG.md`, evidence and
observations, dated `STATE.md` narrative outside the current run-reference
correction, and historical clauses inside current `AGENTS.md`, `README.md`,
`rust-toolchain.toml`, and workflow commentary. Maintaining that registry and
exclusion list is a manual obligation.

The stale run-reference claim remains visible in its original
`offline needs >= 1.75` form and is followed by a current correction to 1.78;
it was not erased or silently rewritten. The current rejected-dependency
comment now uses the derived 1.78 baseline. The same run-reference block
preserves its `49 Rust + 69 shell` v0.6 baseline and appends the measured
v0.30 population, **146 Rust + 313 shell**.

The rejection controls executed before acceptance. Removing every match from
either authority file produced an explicit zero-extraction error, normalized
pin disagreement was rejected, and changing the registered README
restatement to 1.77 was rejected against derived 1.78. R12's two registered
constructions independently disabled the zero-authority and stale-restatement
branches and found the planted violations at the one line-354 control site.
R12 passed **26** controls; the full self-test passed **12 rules / 54
controls**. The first lifecycle run also rejected two production-checker
metadata strings that hard-coded the active cycle; replacing them with
lifecycle-neutral labels made the real checker pass.

Exact searches found zero `rustup run 1.86`, `cargo +1.86`, or workflow
`toolchain: 1.86` constructions. The `--features net` 1.86 statement is
therefore in the active deferred table with the trigger selected by the
operator; it is not reported as a project guarantee. The complete result
passed all **20/20** local jobs, Python 3.11.4 and 3.12.13 at **313/313** each,
and standalone golden **11/11**, delta **0**. No dependency, production
behavior, public contract, route, schema, protected byte, publisher
configuration, scheduler state, release authority, tag, or ref changed.

**v0.30 BOUNDARY-COVER binds every module-global forward boundary (measured
2026-07-31).** G1's decision gate did not trip: lowering identity made its
declaration silently always-on inside the freshness gate, not a reachable
runtime defect, so the finding remains latent rather than P1.

`module_forward_boundaries()` now derives every
`tools/cycle_check.py` module-global name ending in `_FORWARD_BOUNDARY`.
The completeness check compares that derived set with one semantic registry.
The measured derived and registered sets are byte-for-byte the same four
names: `SCOPE_FORWARD_BOUNDARY`, `TRIGGER_FRESHNESS_FORWARD_BOUNDARY`,
`TRIGGER_IDENTITY_FORWARD_BOUNDARY`, and `TRIGGER_FLOOR_FORWARD_BOUNDARY`.
Scope and freshness are explicitly registered as independent with reasons;
identity and floor each declare freshness as a prerequisite. The generic
relationship evaluator therefore enforces both
`TRIGGER_IDENTITY_FORWARD_BOUNDARY >=
TRIGGER_FRESHNESS_FORWARD_BOUNDARY` and the existing floor relation without
hand-writing either comparison.

The derivation bound is deliberately and explicitly **module-scoped to
`tools/cycle_check.py` globals**. An exhaustive declaration search under
`tools/` found exactly the same four names and none outside that module today.
A future `_FORWARD_BOUNDARY` constant in another tools module remains outside
this binding; that namespace boundary is the named residual, not an assertion
that every tools module is covered.

The rejection constructions ran before the complete acceptance run. Injecting
`PLANTED_UNREGISTERED_FORWARD_BOUNDARY` produced exactly:

```
tools/cycle_check.py module-scoped forward-boundary registry is missing PLANTED_UNREGISTERED_FORWARD_BOUNDARY
```

Moving identity to `(1, 2, 2)` while freshness and floor were `(1, 2, 4)`
produced only:

```
TRIGGER_IDENTITY_FORWARD_BOUNDARY must be greater than or equal to TRIGGER_FRESHNESS_FORWARD_BOUNDARY
```

R12 now has **24** controls and the registry has **52** controls total.
Disabling the generic ordering branch makes the existing
`floor-before-freshness` construction fail; disabling the derived
unregistered-name branch makes the new `unregistered-forward-boundary`
construction fail. Both findings point to the one production marker at line
1500. The edit shifted **five existing** `cycle_check.py` control locations:
the boundary marker `1467 → 1500`, three freshness controls `1569 → 1646`,
and the carry-forward control `1796 → 1873`. All five were re-derived from
the real self-test failure/output; the new completeness control was registered
at the derived line 1500.

The four focused boundary/date tests passed **4/4**, including the prior
initialized-population reproduction and the exhaustive missing-date
`required_cycle_name` pair. The complete result passed Python 3.11.4 and
3.12.13 at **308/308** each and all **20/20** local jobs. The first sandboxed
local run failed only when its net wire test was denied a loopback bind; the
authorized rerun passed that same test and the full matrix. The first sandboxed
Python 3.12 run likewise measured eight permission failures from loopback binds
and process-topology inspection; the authorized rerun passed **308/308**.
Standalone golden passed **11/11**, delta **0**. No production source, route,
public value domain, dependency, schema, manifest, protected byte, publisher
configuration, scheduler state, version authority, tag, or ref changed.

**v0.30 E0 rebuilds the entering state and settles G1–G6 (measured
2026-07-31).** The preparatory activation began with exactly one worktree item:
the operator-supplied v0.30 runbook. HEAD was v0.29 audit commit
`d824be06582dfb76b9fe4b5d70ff33f4a505d6cc`, immediately after closure
`20ddf90bb2b1d8654b410cdafe8f67e6d006a115`, exactly as drafted. The
activation pair is `bea40e64849015fdfc9b471f2adb7ab3ce4fcbf7` plus audit
`e7b2c58814e2223d9899b83b3f3491344ce85337`. Before the retention edit,
the real checker emitted:
`cycle-check: ERROR: repomix.config.json: review-export retention pattern for v0.30 must be 'docs/cycles/{TASKS,PROGRESS}-v0.{[0-9],1[0-9],2[0-7]}{.md,.*.md,-*.md}'; found ['docs/cycles/{TASKS,PROGRESS}-v0.{[0-9],1[0-9],2[0-6]}{.md,.*.md,-*.md}']`.
That is the first new-cycle execution of v0.29's retention binding.

The activation checker then rejected exactly the three architecture governed
rows that still named v0.29. The first clean-rebuilt Python 3.11 run therefore
collected 306, passed 305, failed that one current-table test, and skipped zero.
It is a measured non-pass, not a green result. E0 rewrote all three rows with
measured v0.30 observations as the activation section requires; the same clean
environment then passed 306/306. Python 3.12 passed 306/306, and the full local
entry point passed 20/20. The expected pre-rewrite identity rejection was the
activation control being exercised, not an undisclosed product failure; after
its required rewrite, no E0 decision gate remained tripped.

**G1 — boundary-family membership is incomplete.** Exhaustive module search
finds exactly four `*_FORWARD_BOUNDARY` declarations in `cycle_check.py`.
All six pair dispositions are:

- `SCOPE` versus each of `TRIGGER_FRESHNESS`, `TRIGGER_IDENTITY`, and
  `TRIGGER_FLOOR`: independent; scope governs declared-diff enforcement and
  shares no trigger-table population.
- `TRIGGER_FRESHNESS <= TRIGGER_IDENTITY`: load-bearing. Identity is evaluated
  only inside the freshness call, so identity must not precede the function
  that can observe it.
- `TRIGGER_FRESHNESS <= TRIGGER_FLOOR`: load-bearing and already asserted.
  Floor consumes the populations initialized by freshness.
- `TRIGGER_IDENTITY` versus `TRIGGER_FLOOR`: independent. Both depend on
  freshness, but identity changes required cell content while floor changes
  population/carry-forward enforcement.

A no-hardlink throwaway clone first passed the real checker at the committed
boundaries. Changing only
`TRIGGER_IDENTITY_FORWARD_BOUNDARY = (0, 28)` to `(0, 22)` left the real
checker green at active v0.30. Replacing one v0.30 governed cell with v0.29
still produced the exact identity rejection at `ARCHITECTURE.md:385`. The
lowered cutoff is therefore **silently always-on whenever freshness is
reachable**: no v0.22 input can reach the identity branch, and every v0.23+
input already exceeds the lowered value. The declaration itself is
unobservable, and no completeness rule notices it. This is latent rather than
a reachable product defect; BOUNDARY-COVER owns it.

**G2 — one enforced floor is falsely restated; the second is not enforced.**
Executed extraction found three offline pins: `run:452` and `run:456` each
carry `1.78.0`, and `.github/workflows/ci.yml:305` carries `1.78`; explicit
normalization produced one value, `1.78`, with multiplicity three. The live
`STATE.md` run-reference line instead said offline `>= 1.75`, so it is false.
The net entry points use ambient/pinned 1.91: `run:430-440` has no toolchain
selection and the hosted net job selects `1.91`. Exact searches for
`rustup ... 1.86`, `cargo +1.86`, or a workflow `toolchain: 1.86` returned
zero. The 1.86 floor is stated but not executed.

The exhaustive tracked-text inventory contains **582** exact 1.78/1.86 lines:
**300** in execution-cycle documents, **205** in the two State archives,
**24** in live `STATE.md`, and **53** elsewhere. The present authorities and
restatements are explicitly enumerable: the three executable pins above;
`run:118,355-356,1020`; workflow current comments/job labels at
`:49,133,203,267,282,294,297,309-315`; `rust-toolchain.toml:5-10,22,27,29`;
`README.md:604,619-623,642`; `AGENTS.md:32,121,151-152,173,177`; the four
current Rust/manifest compatibility comments; and live State reference
sections at `:3489,3492-3493,3524-3525,3565,3763`. The remaining State
matches are dated execution records; cycle documents, State archives,
`CHANGELOG.md`, the v0.18 observation, and the v0.10 evidence report are
historical records.

No general text scan can distinguish current authority from historical
quotation without encoded metadata: identical “1.78” syntax occurs in both,
and several single lines intentionally contain a refuted 1.75 beside the
current 1.78. Any binding must therefore carry a named, hand-maintained
current-restatement registry and treat the historical set as a permanent
exclusion obligation. Presenting that membership as derived would repeat this
cycle's root defect. FLOOR-BIND owns the registry and the operator-only 1.86
disposition.

**G3 — retention derivations disagree across the version-family boundary.**
Two real no-hardlink Git trees replaced the active v0.30 pair with synthetic
runbook-add commits and ran both entry points:

- At `v1.0`, `cycle-check` exited 1 with
  `cannot retain depth 3 at 'v1.0'`; `export-check` passed at
  **2,524,391 bytes / 152 files** with three retained cycles. The automated
  local and hosted lifecycle lanes catch this loud activation block.
- At `v1.3`, `cycle-check` passed. The real export grew to
  **4,605,031 bytes / 203 files** and `export-check` rejected the ceiling plus
  **51** cycle documents outside the derived last-three set. `export-check` is
  operator-local, absent from `ci-local`, and absent from the workflow, so no
  automated lane catches the silent under-exclusion.

This confirms both reviewer-harness results against full Git trees. The
version-family condition remains unreachable for every existing `v0.<n>`
cycle and is recorded rather than fixed in this scope.

**G4 — latest-at-close content has no executing control and has a fixed-point
residual.** An exhaustive tracked-code search for the governed heading,
trigger-row parser, latest-at-close wording, and export-row subject found only
`tools/cycle_check.py`, `shell/tests/test_cycle_check.py`, and
`tools/invariant_scan.py`. Production validates row population, own-cell ISO
date, active-cycle literal, and carry-forward subject; the other two files
exercise those same properties. No checker reads a governed row's numeric
measurement or compares it with any cycle record.

The v0.29 R-CLOSE implementation tree recorded a 2,516,822-byte export. Its
audit child increased `PROGRESS-v0.29.md` from **33,185** to **38,150**
repository bytes, exactly **4,965 bytes**. The delivered export is likewise
2,521,787, exactly **4,965** above the recorded figure; the entry is 4,964
export bytes plus its stripped trailing newline. A closing tree cannot record
the size of a later tree containing that record. The bounded residual is
therefore the repository-byte size of the one appended audit entry, measured
against the named audit child—not an undisclosed promise of equality.
MARGIN-BIND owns binding the live row to the latest export figure actually
present in its own cycle progress record and naming the empty-record state.

**G5 — three comparable points yield two observations, not a rate.** The exact
sequence is v0.28 delivered **2,530,129**, v0.29 delivered **2,521,787**
(delta **−8,342**), and v0.30 activation audit tree
`e7b2c58814e2223d9899b83b3f3491344ce85337` **2,464,445** (delta
**−57,342**). There are three points and only two delivered-to-next-activation
interval observations; both are negative and neither supports a growth rate.
The existing planning denominators are not observations: at 31,147 bytes/cycle
the export has **17.19** cycles of headroom, while State at **257,422** has
**196,319 bytes / 8.72 cycles** to its 453,741 boundary at 22,525
bytes/cycle. State's archival boundary is nearer under those explicit
denominators; neither trigger fired.

**G6 — one compile-time SQL declaration is achievable.** Extracting the two
ordering clause bodies produced byte-identical **123-byte** values with
SHA-256
`47c5f7d45b5b92974f3f33de54be41cfeb06305db8221c7877f1c0a944f453aa`.
A `macro_rules!` query constructor can hold that clause once and expand two
different select/tail literals through `concat!` at compile time. That requires
neither runtime formatting nor allocation and preserves the two distinct
queries, so ORDER-CONST is not skipped. Its blast radius remains one raw
boundary string in an internal diagnostic.

**Entering-state result.** Clean Python 3.11.4 and 3.12.13 environments each
resolved all 21 constraints and passed **306 collected / 306 passed / 0
skipped** with one warning. Their comparator derived
`collected=306`, `equivalent=true`, and `equivalent_passed=306`. Full local CI
passed **20/20**: warning-denied **146** workspace tests, **62** net tests
(**32 ingest + 30 cored**), clean clippy/fmt/ShellCheck, locked Rust 1.78
check/test, `invariant-scan` **12/51**, and embedded golden **11/11**.
Standalone golden passed **11/11**, delta **0**. Focused SEC identity retained
all **200 SEC** rows with **0 dropped** (201/201 including the separate
filings-digest fixture).

Manifest validation passed schema 2 with **2 artifacts / 331 pinned files**.
Two complete checks took **0.09 s / 0.10 s real**, matched both databases, and
left the **191,395-byte** manifest unchanged. `checklist-audit` passed
**232/232** with three retractions and zero exemptions. Activation State was
**3,811 lines / 257,422 bytes**. E0 re-derived **0** planted-control line
numbers because it edited neither checker nor store. No publisher request,
scheduler, model-profile command, cadence, dependency, schema, production
source, manifest, protected byte, version authority, tag, or working-repository
ref changed.

**v0.29 R-CLOSE records the operator-selected no-release disposition (measured
2026-07-31).** The operator selected `no-release`. The measured cycle diff adds
no route, response shape, `/v1/*` value domain, dependency, schema, or public
surface. The published v0.17.0 defect remains precisely bounded: for a
misordered incoming window, one internal `/ingest` diagnostic can report the
wrong raw boundary string; no filing or archive row is lost, and no public
field or serialized value domain changes. The correction and this cycle's
bindings remain intentionally unpublished for a later release.

Immediately before closure, remote `main` and the peeled v0.17.0 tag both
resolved to `4af2841816dd3e43fb8423153b91aa22ccb87537`; annotated tag object
`df4fc3b044ca12335e773dcc0b9bdd4e0db90afd` was unchanged, and the neutral
evidence ref resolved to candidate
`9059ecab338eaaccfd6376ec7ba5e5e22e18c6f4`. No version authority, tag,
remote `main`, or release ref moved.

Every declared permission is reconciled against activation-exclusive
`1cf49cf8e1574b7ac6ac1c43ca16ee8794da7e38..R-CLOSE`. Used `allow` paths are
`tools/cycle_check.py`, `crates/store/src/sqlite.rs`, `shell/tests/**`,
`config/invariant-rules.json`, `tools/invariant_scan.py`,
`repomix.config.json`, the exact `evidence/ci-runs/30600284114-1/**` receipt
set, `evidence/v0.29/deferred-audit/report.json`, the explicitly authorized
`config/protected-artifacts.json` registration, `AGENTS.md`, and
`ARCHITECTURE.md`. Unused `allow` paths are `tools/export_check.py` and
`crates/**/tests/**`. Every declared release authority and every `forbid` path
is unused. The standing always-allowed `STATE.md`, active progress record, and
active runbook are used only for their declared lifecycle records.

G1 executed the stale retained-cycle glob and obtained the exact two-path
`export-check` rejection. G2 measured a different object: the automatic check
binds tracked retention intent without creating or inspecting the
operator-local export. G3 reversed the two trigger-boundary constants and
reproduced `UnboundLocalError` before the new binding produced a named
configuration failure. G4 executed known-day, NULL-day, day-tie, raw-tie, and
id-tie cases across SQL and Rust, then ORDER-BIND made either declaration's
solo drift fail. G5 measured the stale-but-labelled v0.28 margin, selected the
latest-at-close rule, and refreshed both governed tables. G6 produced a bounded
later-cycle design of 1,260 seconds, at most three loopback ingests and four
publisher requests; v0.29 executed no scheduler, sent no publisher traffic,
and changed no cadence. G7 confirmed the published positional defect and its
exact internal-diagnostic-only consequence stated above.

The six draft defects remain explicitly classified as **reviewer errors**:
(1) the supplied v0.28 draft used the reserved closing heading before closure;
(2) it asserted 14 governed deferred rows while containing 15; (3) it placed
`ddf08d20…` on local `main` when that commit was on the working branch and
local `main` was 102 commits behind `origin/main`; (4) its State-region sizes
were about seven bytes low because the review export strips trailing newlines;
(5) the supplied v0.29 draft repeated the reserved closing token in prose and
failed activation; and (6) it refreshed the runbook governed table but left
all three trigger-bearing architecture rows identified as v0.28. These are
preserved as reviewer errors, not promoted into product findings.

The exact R-CLOSE implementation-tree export passes **99 derived / 7 required /
152 exported** at **2,516,822 bytes**, leaving **483,178 bytes / 16.11%** below
the **3,000,000-byte** ceiling while retaining exactly v0.27–v0.29 and excluding
the pinned SEC RSS body and `docs/state-archive/**`. `checklist-audit` passed
before closure at **231 checked / 3 retracted / 231 matched / 231 commits
resolved**. The closing task is the one ordinary mandatory audit increment;
the seventeen cycle-control boxes are closure proofs that `cycle-check`
requires commit mappings for, but `checklist-audit` does not count them.

Growth is derived from repository bytes, not the newline-stripping export.
The activation tree's State was **224,029 bytes** and its manifest **182,774
bytes**; R-CLOSE measures State at **257,422 bytes** and the manifest at
**191,395 bytes**. Thus observed v0.29 State growth is **33,393 bytes/cycle**
and manifest growth is **8,621 bytes/cycle**. The activation export was
**2,411,393 bytes**, so the R-CLOSE export's observed retained-scope growth is
**105,429 bytes**. State remains below its **453,741-byte** second-archive
boundary with **196,319 bytes** remaining, or **5.88 cycles** if this cycle's
State growth repeated; the independent export ceiling remains the executable
gate.

**v0.29 RE-MEASURE authenticates the exact neutral evidence candidate without
publishing (authorized and measured 2026-07-31).** Candidate
`9059ecab338eaaccfd6376ec7ba5e5e22e18c6f4` was pushed only to
`refs/heads/codex/v0.29-evidence-9059eca`. Hosted workflow-dispatch run
**30600284114**, attempt **1**, executed that exact candidate and ref. Core,
golden, lint, MSRV, net, shell 3.11, and shell 3.12 all passed; the report-only
dependency-drift job skipped under its declared condition. Remote `main` and
the peeled v0.17.0 tag both remained
`4af2841816dd3e43fb8423153b91aa22ccb87537`; no release tag was created or
moved.

Both fresh local shell lanes collected and passed **306** with zero skips.
For each hosted lane, `tools/test_population.py` independently derived
`{"collected":306,"equivalent":true,"equivalent_passed":306,"hosted":{"on_site_skipped":1,"passed":305,"skipped":[{"node_id":"tests/test_deferred_audit.py::test_on_site_production_measurements_match_committed_receipt","reason":"on-site production audit requires protected corpora and built cored"}]},"local":{"passed":306,"skipped":0},"schema_version":1}`.
The one hosted skip was named, carried that declared reason, and was marked
`on_site`.

All seven receipts and their seven paired Sigstore bundles are registered under
`evidence/ci-runs/30600284114-1/` as `pinned_files[]` with `supporting` grade
and no `admission` key. Each bundle verified the exact receipt bytes,
repository, CI workflow signer, candidate digest, neutral source ref, and
GitHub-hosted runner identity. The release-grade report at
`evidence/v0.29/deferred-audit/report.json` is **35,166 bytes**, SHA-256
`91f1907ffdabfc46f7f46cebe41d85d9613a32440d78213ff1d96b987797de6e`,
requires attestations, accepted all **7** identities, rejected **0**, found no
matrix finding, and recorded **5 deferred / 2 promoted / 0 implemented
deferred subsystems**. A fully captured exact-path re-derivation passed **7**
rows, **5** source-determined dispositions, and **7** trigger texts.

The candidate itself verified the pre-registration **316** pins and hosted and
standalone golden **11/11**. The operator explicitly authorized the dated
amendment and fifteen new `pinned_files[]` records on 2026-07-31; manifest
validation now reports schema 2, **2 artifacts / 331 pinned files**. The
manifest is **191,395 bytes**, leaving **857,181 bytes** to 1 MiB, and two
consecutive complete `verify-artifacts` runs passed at **0.10 s / 0.10 s
real**, leaving **0.90 s / 0.90 s** to the timing trigger. Both protected
SQLite artifacts remained byte-identical. The exact evidence paths and
manifest allowance are scoped only to this registration; no validator,
production source, protected database, publisher configuration, schedule, or
identity changed.

Complete workflow and hosted-log searches found no SEC or arXiv publisher URL,
no `harvest-arxiv`, and no publisher-directed ingest command. The two
`usgaap.rss` occurrences were local `PIN MATCH` output for the committed SEC
observation. Every `curl` command was the immutable Rust toolchain action's
`https://sh.rustup.rs` installer. No hosted or local publisher request or
scheduler execution occurred.

The completed evidence tree's permission-complete `ci-local` passed **20/20**
jobs with warning-denied **146** workspace tests and **62** net tests (**32
ingest + 30 cored**), locked Rust 1.78, clean clippy/fmt/ShellCheck, shell
**306/306**, registered invariant self-test **12 rules / 51 controls**,
protected evidence, and embedded golden **11/11**. The separately required
standalone golden also passed **11/11**, delta **0**. Step 8 remains behind its
separate operator-only disposition decision.

**v0.29 SCHEDULE-DESIGN authorizes a bounded later-cycle experiment, not
traffic now (operator decision and measurement 2026-07-31).** The operator
selected outcome **1** on 2026-07-31: authorize a bounded scheduled SEC window
in a later cycle. The reason carried by that selection is to measure the
recurring 600-second clock in the mode for which the existing cadence and
coverage controls were built, because that mode has never run. This decision
approves the design posture only. The later execution still requires a cycle
whose declared scope admits it and a separate explicit operator authorization;
it does not authorize a request in v0.29.

**Exact bound.** The future experiment is one continuous **1,260-second**
window with one cored process, one scheduler process, a fresh absent
unprotected SQLite path, a fresh absent scheduler-state path, and an isolated
schedule copy containing only
`quant-desk:ingest-source:sec-edgar-usgaap` at exactly **600 seconds**. A fresh
state makes the job due at approximately `t+0`, then at `t+600` and `t+1200`:
at most **3** loopback `/ingest` requests. With one process-scoped
`RobotsCache` and its **86,400-second** positive TTL, the publisher-side maximum
is **4 HTTP requests**: one `/robots.txt` request before the first document
request and at most three SEC feed requests. Redirects and retries are not
budgeted; observing either is a refusal. An external watchdog ends the process
at 1,260 seconds even if fewer than three invocations complete.

The future evidence set must capture monotonic scheduler start/end and each due
job; the scheduler state before/after; each loopback `/ingest` start and
response; each publisher request's origin, path class, start time, status, and
redirect/retry disposition; assigned User-Agent byte hash without the contact
value; robots body hash and gate outcome; fetched/new/per-source `ok`; every
coverage outcome and raw boundary pair; and database before/after document,
distinct-id, canonical-id, and cursor counts. Counts must agree across the
scheduler log, loopback observer, publisher-request observer, responses, state
file, and database.

**Executable preflight/refusal checks.**

- `tools/evidence_artifacts.py validate` and two complete
  `./run verify-artifacts` passes must precede the window.
  `tools/evidence_artifacts.py protected` must reject either proposed data
  target if it aliases a protected artifact; both fresh paths must be absent.
- The existing process-topology measurement and `lsof` must find no foreign
  port-8788 owner or concurrent scheduler. The isolated schedule must parse to
  exactly one SEC source job at 600 seconds, and its dry-run inventory must
  name no refresh, sector, full, or other-source job.
- The admitted-source configuration, terms record, operator deny-list,
  fetched robots policy, configured identity, process-scoped cache, and
  per-host limiter must all pass before the first feed request. DNS, TLS,
  timeout, robots, redirect, HTTP-status, identity, or rate-policy failure
  refuses the result.
- A client-side request observer must reject any origin other than the admitted
  SEC origin, any redirect or retry, a fifth publisher request, or a fourth
  `/ingest` invocation. The watchdog rejects elapsed time above 1,260 seconds.
- The first successful non-empty window may report `first_window`. Every later
  non-empty poll must report `overlap`; `gap_detected`, `empty_window`, a
  source error, or a missing coverage record refuses the result. The coverage
  observation still commits incoming documents by design; refusal means the
  experiment is not evidence for recurring operation, not that committed rows
  are rolled back.
- Any `[scheduler] job ... failed:` line is a refusal even though the current
  scheduler catches that exception, advances the clock, and records the
  attempt. Any disagreement among request, response, state, log, or database
  counts is also a refusal.

**Named observation boundary.** Existing controls observe only parts of the
future run. `test_admitted_sec_source_has_an_explicit_resolvable_cadence` and
`test_architecture_sec_cadence_matches_schedule_and_rejects_mismatch` bind the
committed 600-second source job and its architecture record.
`Scheduler.tick`, `test_tick_runs_due_jobs_and_reschedules`, and
`test_state_persists_and_reseeds` observe due ordering and attempted-run state.
The artifact validator and harvest preflight controls protect the database
target. `test_sec_edgar_usgaap_admission_is_exact_and_fail_closed_on_missing_robots`,
the live-path robots/redirect/limiter controls, and HC8 observe admission and
politeness. R12's coverage-topology controls, the two cored pinned-window tests,
and ORDER-BIND's SQL/Rust test observe pre-insert per-source classification and
boundary ordering. `audit_deferred.scheduler_measurement` observes process
topology, not scheduler success.

No existing control enforces the whole 1,260-second envelope, reconciles all
five evidence channels, or counts actual publisher requests; the later-cycle
controller/observer must do that. No client-side evidence can prove what the
publisher received after TLS termination or how it processed a request.
Success also cannot prove peak-season density, deadline-day density, or any
hour covered by neither live sample. Whether the terms determination is still
current at execution time, whether the chosen wall-clock window is appropriate,
and whether a successful bounded sample justifies recurring deployment remain
explicit operator judgements rather than executable checks.

Step 6 itself executed only fixture/pure controls: **13/13** focused shell
tests passed under each constrained Python lane, and the two named cored
coverage tests passed **2/2**. An initial incorrectly exact-filtered Rust
command executed **0 tests** and is a non-result; the corrected commands
executed the named tests. The permission-complete deferred-audit topology
measurement found **0** scheduler processes, **0** cored processes, port 8788
not accepting, one supported simultaneous harvest caller, two configured /
seven expanded ordinary jobs, and serial execution. The default scheduler
state path is absent, and the activation-to-Step-6 diff leaves
`config/schedule.json` byte-identical. A complete audit of this Codex session's
function and custom-tool call transcript found no invocation of the scheduler,
`harvest-arxiv`, a publisher endpoint, or a publisher-directed HTTP client.
Every suspicious-string match was a documentation patch or an `rg`/`jq`
inspection of those names; no web tool was called. Step 6 therefore sent
nothing and changed no cadence. The exact SCHEDULE-DESIGN implementation-tree
export measures **2,481,321 bytes**, leaving **518,679 bytes / 17.29%**
headroom; it openly supersedes MARGIN-TRUTH's 2,471,012-byte observation.

**v0.29 MARGIN-TRUTH makes governed observations current and records the next
State boundary (measured 2026-07-31).** G5 held exactly. The v0.28 live row
carried its correctly labelled Step 5 measurement of **2,485,846 bytes** and
**514,154 bytes / 20.68%** headroom. The v0.28 closing implementation tree later
measured **2,526,556**, and the delivered reviewer export measured
**2,530,129**. The earlier row was historical truth about its named tree but was
not the latest observation available to a reader deciding whether its trigger
was near.

`AGENTS.md §5` now states the rule symmetrically: at close, a governed row uses
the latest measurement actually available; it may not retain an earlier value
when a later measurement exists, and it may not invent a later value when none
exists. Earlier observations stay in their dated task/progress records and the
live row forward-corrects explicitly, whether the margin rises or falls.

All three trigger-bearing architecture rows are current as of this tree. The
export row records the exact MARGIN-TRUTH tree and openly supersedes E0. The
manifest row retains E0 because it remains the latest complete measurement:
**316 pins / 182,774 bytes**, **865,802 bytes** below 1 MiB, and **0.11 s /
0.10 s real**, leaving **0.89 s / 0.90 s** to the timing trigger. The warning
row now carries BOUNDARY-BIND's later permission-complete **306 collected / 306
passed / 0 skipped** result; the dependency bytes remain unchanged.

The next live-State archival boundary is **453,741 bytes**, the measured
pre-archive State size at v0.28 entry. That is a reasoned byte boundary: it is
the prior demonstrated point at which review scope required the successful
mechanical archive, not a line count or a round invented limit. The current
State is **241,866 bytes**, leaving **211,875 bytes**; at E0's normalized
**22,525 bytes/cycle** rate that is **9.41 cycles** of State-only headroom. The
independent 3,000,000-byte export ceiling may fire sooner and remains an equal
trigger. This task records the boundary only: no byte under
`docs/state-archive/**` moved or changed.

**v0.29 ORDER-BIND makes SQL/Rust recency drift fail in the store test suite
(measured 2026-07-31).** The permanent fixture lives entirely below
`#[cfg(test)]`; no production byte changed. Held and incoming sets each contain
known-day and NULL-day documents plus day, raw-byte, and id ties. The held set
is inserted into SQLite and independently ordered by the production comparator;
the full SQL id order must equal the Rust order. The production coverage call's
SQL-selected held boundary must equal the Rust-derived first row. The incoming
set is separately inserted and independently SQL-ordered; its last row must
equal the production comparator's incoming-oldest boundary.

That binds the terms in both directions. SQL's `published_day IS NULL`
ascending corresponds to Rust `Option::cmp` placing `None` below `Some`; SQL
then orders day, raw byte, and id descending, exactly the reverse of the
comparator's ascending order. Changing either statement alone cannot satisfy
both comparisons by construction.

The failure was executed before acceptance. With only the production held
query changed to `published_day IS NULL DESC`, the focused test executed and
failed:

```
left: Some("z-null")
right: Some("z-raw")
```

The mutation was then removed. The same focused test passed **1/1**, the
unchanged v0.28 misordered-window test passed **1/1**, and the full store suite
passed **24 unit + 2 integration** tests. The SEC measurement reported
**201 aggregate kept / 0 dropped**, comprising the **200 SEC** documents plus
the one news baseline; the SEC pair population remained 19,900 and no
cross-issuer drop occurred.

The blast radius is exactly the one G4 measured: a divergence can produce a
wrong raw boundary string in one internal observational diagnostic. Detection
does not fail the poll, and this task changes no runtime output at all. The
internal `/ingest` response shape is unchanged; every `/v1/*` field and
serialized value domain is unchanged. No filing, schema, dependency, protected
byte, publisher configuration, or scheduler behavior changed.

**v0.29 BOUNDARY-BIND turns a latent traceback into a named configuration
defect (measured 2026-07-31).** G3 classified the defect as latent: the live
floor `(0, 28)` does not precede freshness `(0, 23)`. The implementation uses
both defenses appropriate to the two different properties. It initializes the
architecture and deferral populations to zero before either version gate, so no
ordering can read an unbound local. It also executes an explicit
`TRIGGER_FLOOR_FORWARD_BOUNDARY >= TRIGGER_FRESHNESS_FORWARD_BOUNDARY` check,
because the floor's semantic population requirement depends on freshness having
performed the measurements.

The reproduction test sets freshness to `(1, 2, 4)`, floor to `(1, 2, 2)`, and
runs the real checker against active cycle v1.2.3 between them. It exits **1**
with:

```
TRIGGER_FLOOR_FORWARD_BOUNDARY must be greater than or equal to TRIGGER_FRESHNESS_FORWARD_BOUNDARY
```

The output contains no `UnboundLocalError`; the initialized zero populations
also reach the existing named floor errors rather than a traceback. The
registered R12 construction independently reverses the constants and confirms
the same relationship check; disabling it produces the named
`floor-before-freshness` failure.

The two exhaustive missing-date branches collapsed to `if not valid_dates`.
A direct test invokes the same `check_trigger_table` entry point with
`required_cycle_name=None` and with an active-cycle name. Each still produces
exactly one missing-date error; the active-cycle case also preserves its
separate missing-cycle-identity error. This is a readability correction, not a
behavioral change.

Focused lifecycle/invariant tests passed **75/75**. The permission-complete
shell entry point collected and passed **306/306** with zero skips and the one
governed Starlette warning. Registered invariants pass **12/12 rules / 51
controls**, with R12 at **23**. No production source, public route or value
domain, dependency, schema, protected byte, publisher configuration, or
scheduler behavior changed.

**v0.29 RETENTION-BIND makes a stale Repomix cycle glob fail in automatic
lanes (measured 2026-07-31).** `cycle-check` now imports the sole
`CYCLE_RETENTION_DEPTH` authority from `tools/export_check.py`, parses the
active declaration, and independently generates the Repomix brace pattern. For
active v0.29 and depth 3, the derived exclusion ends at v0.26. The pattern's
lower range now starts at zero rather than six; matching nonexistent v0.0–v0.5
paths changes no exported path but removes an unrelated lower-bound literal
from the derivation.

The rejection ran before the acceptance. With the checker implemented and the
tracked config still carrying its activation-era `[6-9]` range, the real
`./run cycle-check` exited **1** with:

```
repomix.config.json: review-export retention pattern for v0.29 must be 'docs/cycles/{TASKS,PROGRESS}-v0.{[0-9],1[0-9],2[0-6]}{.md,.*.md,-*.md}'; found ['docs/cycles/{TASKS,PROGRESS}-v0.{[6-9],1[0-9],2[0-6]}{.md,.*.md,-*.md}']
```

After the config moved to the derived form, the same entry point passed.
The fixture explicitly verified that no `repomix-output-*.xml` existed, then
corrupted the tracked pattern and observed the named failure. The registered
R12 construction independently appends a stale suffix to the active-cycle
derivation and executes the production checker; disabling the mismatch branch
produces the named `stale-retention-pattern` self-test failure. R12 therefore
moved from **21** to **22** controls and the whole registered scanner passes
**12/12 rules / 50 controls**. Focused lifecycle/invariant tests passed
**73/73**, and the permission-complete shell suite passed **304/304**. Its
first sandboxed invocation passed 296 and failed eight only because loopback
binding and process-table inspection were denied; that environment attempt is
a non-result.

This is not v0.22 G3's rejected hosted export duplication. The automatic rule
reads only the tracked config, active declaration, and one depth authority; it
does not create or inspect an export, measure bytes, enumerate exported paths,
or enforce the ceiling and excluded-byte classes. The project-root
`./run export-check` still owns those artifact properties and passes unchanged
on the completed implementation tree at **99 derived / 7 required / 152
exported / 2,446,347 bytes**, depth 3. No production source,
public route or value domain, dependency, schema, protected byte, publisher
configuration, or scheduler behavior changed.

**v0.29 E0 rebuilds the entering state and settles G1–G7 (measured
2026-07-31).** The clean permission-complete `./run ci-local` rerun passed all
**20/20** jobs. It executed warning-denied **146** offline workspace tests and
**62** net tests, clean clippy, rustfmt, ShellCheck, locked Rust 1.78 checks and
tests, `invariant-scan` **12 rules / 49 controls**, protected-artifact and
fingerprint verification, shell **303/303**, and embedded golden **11/11**.
The separately invoked `./run golden` also passed **11/11**, delta **0**.

Both Python lanes were rebuilt rather than inherited. Python **3.11.4** and
**3.12.13** each resolved the exact **21-package** constraint set and each
reported `collected=303`, `passed=303`, `failed=0`, and `skipped=[]`.
`tools/test_population.py` derived
`{"collected":303,"equivalent":true,"equivalent_passed":303,"hosted":{"on_site_skipped":0,"passed":303,"skipped":[]},"local":{"passed":303,"skipped":0},"schema_version":1}`.
Both lanes emitted the same accepted
`StarletteDeprecationWarning`; it neither became an error nor followed any
dependency-byte change.

Manifest validation reported schema 2, **2 artifacts / 316 pinned files**.
Two complete `./run verify-artifacts` executions matched all 316 pins and both
databases in **0.11 s / 0.10 s real**. The actual manifest byte count is
**182,774**. The preparatory progress record's **182,780** was a transcription
error against an unchanged file and is forward-corrected here; its claimed pin
population, database result, and timing disposition remain true.

The entering ref hypothesis was corrected at activation and held at E0:
pre-activation `d9ecea493d3bc254051a0fa87fafe0b244cb0d19` is the v0.28
audit record whose parent is closing commit
`ec8eaa2ab7c8c23d5a923a08ae36ab7692b4b664`; the published v0.17.0
closing commit remains its ancestor. The E0 entry tree after the committed
scope-fixture amendment was clean. No ref moved.

**G1 — CONFIRMED by execution.** `run` declares **20** local CI jobs and none
is `export-check`; `.github/workflows/ci.yml` contains zero `export`
occurrences. In a no-hardlink throwaway clone with active v0.29 and the
retention glob changed back from `2[0-6]` to the supplied `2[0-5]`,
`./run export-check` exited **1** after generating the real export and printed
exactly:

```
export-check: ERROR: unexpected cycle document outside retention depth 3: docs/cycles/PROGRESS-v0.26.md
export-check: ERROR: unexpected cycle document outside retention depth 3: docs/cycles/TASKS-v0.26-EXECUTION.md
export-check: FAIL (2 defect(s); derived_sources=99, exported=154)
```

**G2 — DIFFERENT OBJECT; v0.22 G3 is not reopened.** The proposed automatic
control parses the tracked `repomix.config.json` pattern, independently derives
the retained cycle range from the active declaration and
`CYCLE_RETENTION_DEPTH`, and compares those two facts without creating or
reading a Repomix export. `export-check` instead compares the paths in an
operator-created export with the repository-derived expected path set and
enforces the size and excluded-byte constraints. The proposed control therefore
binds configuration intent; it does not duplicate the operator-local artifact
check or add a hosted export. Step 2's decision gate remains open.

**G3 — CONFIRMED latent by reproduction.** In a throwaway clone,
`TRIGGER_FRESHNESS_FORWARD_BOUNDARY` was changed from `(0, 23)` to `(0, 28)`,
`TRIGGER_FLOOR_FORWARD_BOUNDARY` from `(0, 28)` to `(0, 23)`, and the active
declaration was set to intervening cycle v0.25. The real `./run cycle-check`
exited **1** with:

```
UnboundLocalError: cannot access local variable 'architecture_trigger_rows' where it is not associated with a value
```

The live constants are freshness `(0, 23)` and floor `(0, 28)`, so the defect
is unreachable today. The load is safe only while
`TRIGGER_FLOOR_FORWARD_BOUNDARY >= TRIGGER_FRESHNESS_FORWARD_BOUNDARY`;
nothing currently binds that relationship, so Step 3 remains required.

**G4 — ordering agrees today, but is unbound.** A throwaway store test inserted
one known-day and one NULL-day row into the held archive, then supplied one
known-day and one NULL-day incoming row. The SQL path selected held raw boundary
`2026-07-10`, while the Rust comparator selected incoming raw boundary
`incoming-null-raw`; the focused test executed **1 passed / 0 failed**. This
confirms the terms agree: SQL's `published_day IS NULL` ascending puts known
days before NULL in its newest-first result, while Rust's ascending
`Option::cmp` makes `None` the minimum for its oldest result; day, raw byte,
and id then use the same lexical tie-breaks in opposite newest/oldest
directions. An earlier command with an incorrectly combined filter and
`--exact` ran **0 tests** and is explicitly not the result. Today the SQL and
Rust statements are bound only by prose and reviewer attention; no permanent
cross-implementation test fails when one changes alone.

**G5 — CONFIRMED and rule selected.** The live v0.28 architecture row recorded
its labelled Step 5 tree at **2,485,846 bytes**, **514,154 bytes / 20.68%**
headroom. The closing implementation tree measured **2,526,556**, and the
delivered review export measured **2,530,129**. A governed row must carry the
latest measurement available at cycle close, regardless of which earlier step
first wrote the row; an earlier measurement remains as openly superseded
history rather than being rewritten as though it had never been true. Step 5
will put this symmetric rule in the operating contract.

**G6 — design only; no traffic.** Proven before this design: coverage is
assessed per non-paged source before insertion; an empty id intersection on a
non-empty held corpus produces the conservative `gap_detected` observation
without discarding the incoming window; the boundary derivation is independent
of incoming slice order; the governing cadence quantity is latest-window
advance rather than feed rebuild wording; and the one pinned latest-200
Wednesday sample spans **4,650 seconds**, giving the unchanged **600-second**
clock a measured **7.75×** span/poll margin (**12.90%** consumed per poll).
Still unproven are recurring scheduler execution, peak-season density,
deadline-day density, and every hour covered by neither live sample.

The bounded later-cycle design is one isolated **1,260-second** scheduler
window, enough for at most three due SEC invocations at seconds 0, 600, and
1,200. It uses a fresh unprotected SQLite target, a fresh scheduler-state path,
an isolated schedule copy containing only the admitted
`sec-edgar-usgaap` source at exactly 600 seconds, and captured scheduler,
`/ingest`, coverage-outcome, request-count, and database evidence. It begins
only after `evidence_artifacts.py validate`, two protected-artifact
verifications, port ownership, source-registry/terms/robots configuration, and
a dry-run job inventory all pass. It stops and refuses any result if a target
resolves to a protected artifact; a foreign listener exists; the dry run names
another ingest source or a cadence other than 600; redirect, robots, DNS, TLS,
timeout, or HTTP policy fails; any publisher other than the admitted SEC origin
is contacted; more than three SEC invocations occur; a post-first poll is not
an overlap or reports `gap_detected`; the scheduler swallows a job exception;
the database or captured request/log counts disagree; or the 1,260-second bound
is exceeded. A gap remains committed and reported, per the existing
observational contract, but makes the scheduled-window outcome a refusal rather
than a pass. This is a design, not authorization; E0 executed no scheduler and
made no publisher request.

**G7 — CONFIRMED.** At annotated v0.17.0's peeled commit
`4af2841816dd3e43fb8423153b91aa22ccb87537`,
`incoming_oldest_published_raw` is still derived positionally with
`.iter().rev().find_map(...)`. Commit
`e6b3c1e` in unpublished descendants replaces that with the archive comparator
and adds the misordered-window test; the published tag is an ancestor of the
current tree. The exact user-visible consequence is a wrong raw boundary
string in one internal `/ingest` diagnostic for a misordered incoming window.
It drops no filing, loses no archive row, changes no response shape, and changes
no `/v1/*` field or serialized value domain.

**Growth and headroom are derived, not estimated.** v0.28 began with a
**453,741-byte** State. Normalizing that start for the later mechanical removal
of the **185,680-byte** historical slice and **66,557-byte** reference slice
gives **201,504 bytes**; the v0.28 final State is **224,029 bytes**, so normalized
one-cycle live-State growth was **22,525 bytes**. The manifest moved from
**174,152** to **182,774 bytes**, or **8,622 bytes**. The actual delivered-v0.28
to v0.29-activation export rollover moved from **2,530,129** to **2,411,393
bytes**, a **118,736-byte decrease**, principally because the **160,726-byte**
v0.26 cycle pair left retention while the then-current v0.29 pair was smaller.
A negative observed export rate gives no finite exhaustion projection. For a
positive planning denominator only, repeating normalized State plus manifest
growth is **31,147 bytes/cycle**. The measured E0 implementation tree leaves
**569,322 bytes** of export headroom, or **18.28 cycles** at that deliberately
narrow denominator. The figure is a planning observation, not an allowance for
unmeasured code or document growth; the executable 3,000,000-byte check remains
the gate.

<!-- STATE_ARCHIVE_PERMANENT_TAIL:START -->
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
- ~~**The `--features net` 1.86 floor had no executable lane.**~~ **RESOLVED in v0.35 Step 5.** The locked net graph is `cored` → `intel-ingest` → `reqwest` 0.11.27 → `url` 2.5.8 → `idna` 1.1.0 → `idna_adapter` 1.2.2 → `icu_*` 2.2.0. Rust 1.86 builds it; Rust 1.85 exits on the dependencies' explicit `requires rustc 1.86` declarations, including `idna_adapter@1.2.2`. Local and hosted lane pairs execute both sides. The older registry-download failure was a non-result, not evidence of the floor.
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

### 6i. Why publisher-granted reuse is `PublisherPermitted` and a minor release (v0.25/LICENSE-SEMANTICS)

**Decision: extend/minor, selected by the operator on 2026-07-30.** The
licensing enum names the ground for redistribution: public domain, a CC grant,
client ownership, or a publisher's own express permission. SEC's measured
statement supports the fourth ground without establishing any of the first
three. `IndexOnly` was rejected as a supposedly conservative default because it
would record a restriction opposite to the measured permission and would
forfeit the only prospective real-content exercise of the redistributable
branch.

`PublisherPermitted` is redistributable and makes no underlying-copyright
claim. Its config, public, and SQLite spelling is exactly the Rust identifier.
The core control enumerates all five variants and proves the existing four
spellings, redistribution outcomes, and attestation outcomes did not move.
SQLite's existing unconstrained text mapping required no production edit; its
integration control proves both the new round trip and the safe
unknown-row-to-`IndexOnly` fallback.

The release is minor because adding a value to an existing public field changes
the contract seen by exhaustive consumers even when the route and body shape
stay fixed. The symmetric dated rule now lives in `AGENTS.md §5` and is
reconciled in `ARCHITECTURE.md §8`. It is intentionally prose adjudicated at
R-CLOSE: no source scan can decide whether a semantic value was added, removed,
or redefined, so no new invariant rule or vacuous planted control was created.

### 6j. Why SEC terms stay operator-adjudicated (v0.25/TERMS-GATE)

**Decision: affirmative identity; operator-owned terms review, selected
2026-07-30.** The SEC publishes two separate facts: its Internet Security
Policy refuses “unclassified” automated tools, while its Webmaster FAQ directs
programmatic EDGAR downloaders to declare an organization-and-contact
User-Agent. It publishes no glossary or registration state that the product can
query. The operator confirmed that the structurally required contact is
monitored and therefore determined that the current identity satisfies the
published direction for the reviewed SEC path.

A runtime terms boolean was rejected because it would turn publisher-specific
natural-language judgment into an asserted machine decision without a
machine-readable input. The executable boundary remains the fetched
`robots.txt` plus the operator deny-list; a dated publisher-specific operator
review owns the additional terms determination before admission. This is
narrower and more truthful than calling robots permission terms permission, and
it generalizes nothing from the SEC to another publisher.

### 6k. Why observed feed shape is affirmative without a parser-success claim (v0.25/FEED-SHAPE)

**Decision: the shape gate is affirmative; parser success remains unmeasured.**
E0 found no mandatory per-item field in the repository RSS parser. The one
authorized feed response contained 200 items; every optional field except
`author` was present and non-empty in all 200, and `author` was absent in all
200. The empty mandatory set is therefore satisfied, and Step 5 may reach its
separate admission decision.

That result does not turn an independent XPath count into a repository-parser
test. Step 4 deliberately did not run the parser against the body. Its behavior
record is conditional and derived from the already-measured source branches;
parser execution belongs to admission testing. Keeping those claims separate
preserves HC13's distinction between observed wire shape and program behavior.

### 6l. Why the admitted SEC source fails closed when robots policy is absent (v0.25/ADMIT)

**Decision: admit with `robots_on_missing: "deny"`, selected by the operator
on 2026-07-30.** The reviewed publisher serves a `robots.txt`, and both v0.24
and the fresh v0.25 Step 4 request measured the intended path as allowed.
Admission therefore binds to the presence and evaluation of that policy.
Treating a future 404 as permission would introduce a new condition never
reviewed; it does not follow from today's allow verdict.

The arXiv `allow` setting is a narrow absence-only exception for a
standards-designed harvesting endpoint that served no policy. It is not a
default for network sources. SEC remains on the conservative branch: missing
policy denies, an explicit disallow denies, and an unreachable origin denies.
The configured source establishes none of those live outcomes by itself; the
first live RSS harvest remains separately deferred to v0.26.

## 7. Run reference

```bash
# toolchain (v0.6.2 claim, retained): offline needs >= 1.75; --features net needs >= 1.86.
# current correction: offline needs >= 1.78; net >= 1.86 is executed by paired 1.86-pass / 1.85-declared-MSRV-refute lanes.
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

cargo test && PYTHONPATH=shell python3 -m pytest shell/tests   # v0.6 baseline: 49 Rust + 69 shell; v0.30 measured: 146 Rust + 317 shell

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
