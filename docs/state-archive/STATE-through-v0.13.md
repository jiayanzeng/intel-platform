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

