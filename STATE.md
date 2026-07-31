# STATE.md — intel-platform handoff

**As of:** 2026-07-31 · **Version:** v0.17.0 (core-shell) · **Status:** **v0.29 is active; RE-MEASURE is complete and R-CLOSE awaits the operator's separate disposition.** Annotated tag object `df4fc3b044ca12335e773dcc0b9bdd4e0db90afd` still targets published closing commit `4af2841816dd3e43fb8423153b91aa22ccb87537`, whose immediate parent is release commit `d5969207835c9f27f461d292b169ccb8d6ae5a46`. Authenticated v0.29 evidence candidate `9059ecab338eaaccfd6376ec7ba5e5e22e18c6f4` on neutral ref `refs/heads/codex/v0.29-evidence-9059eca` passed hosted run **30600284114**, attempt **1**: all seven executable jobs passed, dependency drift skipped under its report-only condition, attestations were required, **7** signed identities were accepted, **0** rejected, and the complete matrix was found. The completed evidence tree's local CI passed **20/20** jobs with warning-denied **146** workspace tests and **62** net tests (**32** `intel-ingest`, including three replay tests, + **30** `cored`), locked Rust 1.78, clean rustc/clippy/fmt/ShellCheck, shell **306/306**, `invariant-scan` **12 rules / 51 controls**, and embedded golden **11/11**. Fresh candidate Python 3.11 and 3.12 populations each collected/passed **306** with **0** skips; each comparator against its hosted lane derived `collected=306`, `equivalent=true`, and `equivalent_passed=306`. Standalone golden passed **11/11**. The evidence manifest contains **331** `pinned_files[]` and measures **191,395 bytes**; two consecutive complete verifications took **0.10 s / 0.10 s real**, and both protected SQLite archives remain byte-identical. The completed RE-MEASURE implementation-tree review export measures **2,500,164 bytes / 152 files**, leaving **499,836 bytes / 16.66%** against its **3,000,000-byte** executable ceiling and retaining exactly v0.27–v0.29 without either excluded byte class. No publisher request or scheduler run occurred; remote `main` and every release tag remain unchanged.

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

**v0.28 R-CLOSE records the operator-selected no-release disposition (measured
2026-07-31).** The operator selected `no-release`. The measured cycle diff adds
no route, response shape, `/v1/*` value domain, dependency, schema, or public
surface. The one runtime correction changes only the value of the internal
`/ingest` diagnostic for a misordered window and leaves its response shape
untouched. v0.17.0 remains the current published release; no version authority,
tag, remote `main`, or release ref moved.

Immediately before closure, remote `main` and the peeled v0.17.0 tag both
resolved to `4af2841816dd3e43fb8423153b91aa22ccb87537`; the neutral evidence ref
resolved to authenticated candidate
`47bb77c19420bf513b53b228e473d4accedc6cc9`. The exact project-root export
passed **99 derived / 7 required / 152 exported** at **2,526,556 bytes**,
below the **3,000,000-byte** ceiling. Step 4's archival control held
`checklist-audit` at **219 → 219** before its mandatory workflow records. Step
5 measured **220** before its mandatory increment. The pre-closure audit
passed **223 checked / 223 matched / 223 commits resolved**; this distinguishes
the unchanged detector populations from their ordinary task-record increments.

Every declared permission was reconciled. Used `allow` paths were
`tools/cycle_check.py`, `tools/export_check.py`,
`crates/store/src/sqlite.rs`, `shell/tests/**`,
`config/invariant-rules.json`, `tools/invariant_scan.py`,
`repomix.config.json`, `docs/state-archive/**`, the exact hosted evidence
directory and report, the explicitly authorized manifest registration,
`AGENTS.md`, and `ARCHITECTURE.md`. The unused `allow` paths were
`crates/store/src/lib.rs` and `crates/**/tests/**`; every `forbid` path was
unused. No release authority was declared or used.

G1's blank-cell and G3's all-`none` constructions both executed and exposed
their vacuous controls; G5's executed historical-cycle move reduced audited
coverage while both prior checkers still passed. G2 measured the inadequate
day-resolution identity, G4 measured the unbounded near-limit export, G6
reproduced and then corrected the positional raw-boundary assumption, and G7
enumerated both semantic release criteria with no implementation because the
current authorities provide no bounded historical surface/value-domain
detector. The drafted T7/NEGATIVE-CACHE accusation is preserved as a
**reviewer error**, not a finding: both subjects were already governed in the
active deferred table with dated observations.

The closing local suite passed **20/20** jobs with warning-denied **146**
workspace tests, **62** net tests, shell **303/303**, locked Rust 1.78, clean
rustc/clippy/fmt/ShellCheck, registered invariant self-test **12 rules / 49
controls**, protected-artifact validation at **2 artifacts / 316 pinned
files**, and embedded golden **11/11**. The separately required standalone
golden also passed **11/11**, delta **0**.

**v0.28 RE-MEASURE authenticates the exact neutral evidence candidate without
publishing (authorized and measured 2026-07-31).** Candidate
`47bb77c19420bf513b53b228e473d4accedc6cc9` was pushed only to
`refs/heads/codex/v0.28-evidence-47bb77c`. Hosted workflow-dispatch run
**30561513204**, attempt **1**, executed that exact candidate and ref. Core,
golden, lint, MSRV, net, shell 3.11, and shell 3.12 all passed; the
report-only dependency-drift job skipped under its declared condition. Remote
`main` and the peeled v0.17.0 tag both remained
`4af2841816dd3e43fb8423153b91aa22ccb87537`; no release tag was created or
moved. Earlier run **30561374600** omitted `publish_evidence`, could not supply
the required attestations, and was cancelled; it is a dispatch non-result and
is not cited as evidence.

Both fresh local shell lanes collected and passed **303** with zero skips.
For each hosted lane, `tools/test_population.py` independently derived
`{"collected":303,"equivalent":true,"equivalent_passed":303,"hosted":{"on_site_skipped":1,"passed":302,"skipped":[{"node_id":"tests/test_deferred_audit.py::test_on_site_production_measurements_match_committed_receipt","reason":"on-site production audit requires protected corpora and built cored"}]},"local":{"passed":303,"skipped":0},"schema_version":1}`.
The one hosted skip is named, carries the declared reason, and is marked
`on_site`.

All seven receipts and their seven paired Sigstore bundles are registered
under `evidence/ci-runs/30561513204-1/` as `pinned_files[]` with `supporting`
grade and no `admission` key. Each bundle verified the exact receipt bytes,
repository, CI workflow signer, candidate digest, neutral source ref, and
GitHub-hosted runner identity. The release-grade report at
`evidence/v0.28/deferred-audit/report.json` is **35,070 bytes**, SHA-256
`1e72a50061a31e84fbc7e38fadb60036ea86f5afd1b3cdff480c2e3f21695227`,
requires attestations, accepted all **7** identities, rejected **0**, found no
matrix finding, and recorded **5 deferred / 2 promoted / 0 implemented
deferred subsystems**. Clean-candidate re-derivation passed **7** rows, **5**
source-determined dispositions, and **7** trigger texts.

The first production-report invocation was an environment non-result because
the sandbox denied its required local process inspection; the identical
permission-complete entry point passed. The first re-derivation lacked the new
logical receipt paths in its detached subject and was a construction
non-result. A later wrapper lost a completed process's exit status and was
also not counted. After the authenticated bytes were mirrored to their exact
temporary logical paths, a fully captured re-derivation passed.

The candidate itself verified the pre-registration **301** pins and golden
**11/11**. The operator explicitly authorized the dated amendment and fifteen
new `pinned_files[]` records on 2026-07-31; manifest validation now reports
schema 2, **2 artifacts / 316 pinned files**. `verify-artifacts` and
`evidence-report` pass, and both protected SQLite artifacts remain
byte-identical. The exact evidence paths and manifest allowance are scoped
only to this registration; no validator, production source, protected
database, publisher configuration, schedule, or identity changed.

Complete workflow and hosted-log searches found no SEC or arXiv publisher URL,
no `harvest-arxiv`, and no publisher-directed ingest command. The two
`usgaap.rss` occurrences were local `PIN MATCH` output for the committed SEC
observation. Every `curl` command was the pinned Rust toolchain action's
`https://sh.rustup.rs` installer. No hosted publisher request occurred.

Full local `ci-local` passed **20/20** jobs with warning-denied **146**
workspace tests, **62** net tests (**32 ingest + 30 cored**), locked Rust
1.78, clean clippy/fmt/ShellCheck, shell **303/303**, registered invariants
**12 rules / 49 controls**, protected evidence, and embedded golden **11/11**.
The separately required standalone golden also passed **11/11**, delta **0**.
Step 8 remains behind its separate operator-only disposition decision.

**v0.28 COVERAGE-ORDER removes the coverage detector's positional assumption
(measured 2026-07-30).** The decision gate remained open: the implementation is
contained in `crates/store/src/sqlite.rs` and its unit test; forbidden
`apps/cored/src/main.rs` and `crates/ingest/src/**` are byte-unchanged.
Enforcement was selected because the store already owns the archive ordering,
so a second handler contract would add ambiguity without adding assurance.

Both boundary selections now use the archive's known-day, day, raw-byte, and id
ordering. Incoming documents without a raw publisher timestamp do not supply a
raw boundary; among those that do, the minimum archive-order document supplies
`incoming_oldest_published_raw`. The input need not be sorted. The new test
constructs a middle/oldest/newest sequence and measures `2026-07-05` as the
boundary even though the last element is `2026-07-09`; it never consults
`incoming.last()`.

The blast radius remains one observational diagnostic string. Gap detection
continues the poll and commits the incoming window; it does not discard a
filing or alter identity. The pinned SEC replay tests remained green, including
the measured **200 items / zero ascending timestamp inversions** premise. The
shipped identity control kept the **200** SEC documents plus the separate
filings-digest document: **201/201 total kept, zero dropped**.

The focused misordered-window test passed **1/1**. Warning-denied workspace
tests passed **146/146**, comprising **29** `cored`, **23** store unit tests,
and the unchanged remaining population. Clippy, fmt, and warning-denied
`cored --features net --all-targets` check passed. Registered invariant scan
passed **12/12 rules / 49 controls** after its R1, R5, and R7 exact store-line
locators were re-measured. Standalone golden passed **11/11**, delta **0**.

The internal `/ingest` response shape did not change: its route, response type,
field names, field types, and serialization are untouched. The corrected edge
case may change only the value of `incoming_oldest_published_raw`; no `/v1/*`
route, response shape, or serialized value domain moved. No dependency, schema,
protected artifact, publisher request, scheduler run, tag, or branch ref
changed.

**v0.28 EXPORT-BOUND makes reviewability an executable property (measured
2026-07-30).** `tools/export_check.py` now rejects exports above a declared
**3,000,000-byte** ceiling. The Step 4 implementation-tree measurement was
**2,469,697 bytes**, so the bound deliberately left **530,303 bytes / 21.47%**
for the remaining cycle records while staying far below the former
**4,975,987-byte** near-limit corpus. The first Step 5 implementation-tree
export passed at **2,481,041 bytes / 152 files**, leaving **518,959 bytes /
20.92%**.

The one retention-depth constant is **3**. From the active declaration and
cycle registry, the checker derives the active execution runbook plus its two
immediately prior runbooks and their matching progress records, then compares
that set exactly with every exported TASKS/PROGRESS path. It also discovers the
unique pinned SEC RSS capture from the repository and rejects its exact export
path, while separately rejecting any `docs/state-archive/**` path. Existing
coverage remained **99** Git-derived sources and **7** required paths.

Five planted violation constructions exercised the over-ceiling, retained
missing, older-cycle present, pinned-body present, and State-archive present
failures before the valid fixture passed. Focused tests passed **8/8**. The
permission-complete full shell entry point collected and passed **303/303** with
zero skips; a preceding sandbox-denied loopback/process-table attempt was not
treated as a result. `cycle-check` passed with the architecture governed-row
population now **3**; `invariant-scan` passed **12/12 rules / 49 controls**;
and standalone golden passed **11/11**, delta **0**.

`checklist-audit` remained **220 checked / 220 matched / 220 commits resolved**
before the mandatory task checkbox, with three retractions and zero exemptions.
The final implementation-tree export including the required status and
completion records passed at **2,485,846 bytes / 152 files**, leaving
**514,154 bytes / 20.68%** headroom beneath the declared ceiling.
No historical cycle document, production runtime source, dependency, schema,
protected artifact, golden input, publisher request, scheduler run, public
route, serialized value domain, tag, or branch ref changed.

**v0.28 DOC-SLIM reduces review-export scope without reducing executable
coverage (measured 2026-07-30).** The mechanical State split began from
**462,196 bytes**. It moved **185,680** bytes of v0.21→v0.14 history and
**66,557** bytes of reference §8/§9 into a new archive surrounding the existing
**297,739-byte** through-v0.13 archive. The new archive is **549,976 bytes**;
the immediate post-split live State was **209,959 bytes** and retains
v0.22-forward plus reference §1–§7.

The moved historical segment matched its destination at SHA-256
`c2535b16bdec70a4fc3551a3ebfc3bfbc3f02ef337a33aaa47f1942cacad6d6c`;
the existing archive matched its embedded destination at
`3233af5b4c148f7a7f4700edba3238dc67245f28d83dc07cc53c26ebdca6a414`;
and reference §8/§9 matched at
`beca80003f472db3c22aca1fb54d2eb5777a13b66568ab8c3f996d47a3538c98`.
Independent whole-output comparisons returned `state_exact=True` and
`archive_exact=True`; these are byte comparisons, not a reading-based claim.

The archival control measured `checklist-audit` **219 → 219** before the
mandatory task-record checkbox, with three retractions, zero exemptions, and
every entry/commit resolved. `cycle-check`, `progress-check`, manifest
validation, all **301** pins plus both protected databases, and registered
`invariant-scan` **12/12 rules / 49 controls** passed. The publication-status
entry point found exactly **one** complete post-push record for current tag
v0.17.0 and returned zero errors. No historical cycle document was moved,
edited, or deleted.

The first post-reduction export passed the exact project-root entry point with
**99** derived sources, **7** required paths, and **152** exported files. It
measured **2,465,363 bytes**, **49.31%** of decimal 5 MB. Its raw source
composition was cycle docs **6 / 342,530 bytes**; observations **12 / 56,703**;
root **12 / 469,902**; state archive **0 / 0**; and other reviewed paths
**122 / 1,582,306**. The cycle set was exactly the TASKS/PROGRESS pairs for
v0.26, v0.27, and v0.28; all eight observation Markdown files remained; the
pinned SEC body and both State archives were absent. A final export after the
mandatory status/checklist record passed the same exact entry point at **99
derived / 7 required / 152 exported** and measured **2,469,697 bytes / 49.39%
of decimal 5 MB**. Its final raw composition is cycle docs **6 / 343,965
bytes**; observations **12 / 56,703**; root **12 / 472,800**; state archive
**0 / 0**; and other reviewed paths **122 / 1,582,306**. Final live
`STATE.md` is **212,857 bytes**.

Standalone golden passed **11/11**, delta **0**. No production runtime source,
dependency, schema, protected artifact, golden input, publisher request,
scheduler run, public route, serialized value domain, tag, or branch ref
changed.

**v0.28 TRIGGER-FLOOR makes governed populations and carry-forward executable
(measured 2026-07-30).** The active call site now binds the freshness result and
rejects a zero population by naming the architecture or active-deferral table.
The focused test derives its expected `(architecture, deferral)` counts from
the table rows rather than a literal; the real tree derived **(2, 15)**.
Planting `none` in every trigger cell made the checker report both named
zero-population errors.

The immediately prior runbook is selected by version from
`execution_runbooks()`. Its governed subjects must remain active or be listed
under an active **Deferred completions** table with a valid ISO-dated
completion. The real v0.27 → v0.28 comparison measured **14 → 15**, **zero
dropped**, and one addition, “Release-classification criteria with no executed
control.” This corrects the runbook draft: “First live SEC RSS harvest” and
“Observation-byte manifest coverage” were the two drops in v0.26 → v0.27,
whose measured populations were **14 → 14** with two different additions.
Executing fixtures use those exact two subjects to prove dated completions are
expressible without changing a closed runbook.

Focused lifecycle tests passed **50/50**; real `cycle-check` passed; registered
self-test derived **12/12 rules / 49 controls**, with R12 control 18 disabling
the carry-forward rejection and detecting a silently dropped planted subject.
Standalone golden passed **11/11**, delta **0**. No production runtime source,
dependency, schema, protected artifact, golden input, publisher request,
scheduler run, public route, serialized value domain, tag, or branch ref
changed.

**v0.28 TRIGGER-IDENTITY binds governed observations to their owning cycle
(measured 2026-07-30).** The mandatory data-first commit
`5342663f89e3e2b499bfc1bf42b15c44705de58b` re-measured and rewrote only the
two trigger-bearing architecture rows with their own `v0.28` and ISO-date
tokens; the pre-tightening checker passed that commit. The rule then removed
the measured-column header fallback, retained v0.23-forward own-cell date
freshness, and added v0.28-forward exact active-cycle identity resolved through
`resolve_cycle(root)`. No closed runbook changed.

The focused lifecycle suite passed **46/46** and the real `cycle-check` passed
with active v0.28, 25 closed execution runbooks, and three historical runbooks.
Registered `invariant-scan --self-test` derived **12/12 rules / 48 controls**.
R12 control 16 disabled the v0.28 own-cell date branch and caught a row whose
cell had no date even though its header carried `2026-07-30`; control 17
disabled active-cycle identity and caught a `v0.27` observation presented to
the v0.28 checker. The prior generic missing-date control remains independently
executable as control 15. The real checker accepts both live tables in their
new format, and neither tests nor tooling hardcode the aggregate control count.

The first sandboxed standalone golden invocation was an environment non-result:
the core could not bind its isolated loopback port. The permission-complete
execution of that exact `./run golden` entry point passed **11/11**, delta
**0**. No production runtime source, dependency, schema, protected artifact,
golden input, publisher request, scheduler run, model-server session, public
route, serialized value domain, tag, or branch ref changed.

**v0.28 E0 rebuilds the entering state and settles G1–G7 (measured
2026-07-30).** After the separately committed activation compatibility
corrections, `./run ci-local` passed all **20/20** jobs: warning-denied
**145** workspace tests and **62** net tests, clean clippy/fmt/ShellCheck,
locked Rust 1.78, `invariant-scan` **12 rules / 46 planted controls**, shell
pytest, embedded golden, protected artifacts, and lifecycle checks.
Standalone golden remained byte-identical at **11/11**. Clean Python 3.11.4
and 3.12.13 environments resolved all 21 constrained packages and each
collected/passed **293**, failed zero, and skipped zero.
`tools/test_population.py` derived `collected=293`, `equivalent=true`, and
`equivalent_passed=293`.

Both full artifact verifications matched **301** pins plus both protected
SQLite archives and took **0.10 s / 0.10 s real**. The manifest is **174,152
bytes**, below its 1 MiB bound. `checklist-audit` passed **216 checked / 3
retracted / 216 matched / 0 exemptions**. The architecture table contains
**11** data rows with **2** governed triggers; the active deferred table
contains **15**, correcting the drafted 14. The entering `STATE.md` was
**6,984 lines / 453,741 bytes**. Its seven drafted regions measured, in the
runbook's order, **12,540 / 17,273 / 127,922 / 185,799 / 43,650 / 38,748 /
27,809 bytes**. The declared `docs/state-archive` consumer search returned no
match across `tools/*.py`, `run`, `AGENTS.md`, `ARCHITECTURE.md`, or
`config/*.json`, and the manifest contains no pin for that directory.

G1's throwaway runbook blanked every deferred measured cell while retaining a
dated measured-column header; `cycle-check` exited **0**. Every real governed
row currently has its own valid date, so removing a header token from the real
tables would reject zero rows. G2 confirmed that v0.24 through v0.27 all closed
on `2026-07-30`; a date-only discriminator distinguishes at most one cycle on
that date, leaving three of those four later measurements indistinguishable
from copied tokens. G3 confirmed the checker discarded its returned `(2, 15)`
population and had no floor: an all-`none` throwaway construction derived
`(0, 0)` and `cycle-check` exited **0**.

G4 confirmed that `tools/export_check.py` enforced inclusion only: four source
roots and seven required paths, with no byte or retention bound. The exact
project-root entry point passed **99 derived sources / 7 required / 182
exported files**. Its retained export measured **4,975,987 bytes**, **99.52%**
of decimal 5 MB with **24,013 bytes** headroom. Raw exported-file composition
was `docs/cycles` **34 files / 1,435,284 bytes**; observations **13 /
949,344**; repository root **12 / 713,006**; `docs/state-archive` **1 /
297,739**; and all other reviewed paths **122 / 1,564,264**. The external
project-knowledge observation remains **2,067 chunks against a 2,000 limit**
on 2026-07-30.

G5 moved closed v0.24 out of `docs/cycles` in a throwaway clone.
`cycle-check` exited **0** before and after while its closed count fell **25 →
24**; `checklist-audit` exited **0** before and after while checked/matched
coverage fell **216 → 209**. The `audit_deferred` complete-progress-glob
assertion still passed. Closed cycle documents therefore remain in their sole
audited directory; only export scope may change.

G6 confirmed the coverage detector's doc comment states source partition and
before-insert preconditions but no incoming ordering premise.
`incoming.iter().rev().find_map(...)` returns the last positional non-null raw
timestamp, so a misordered window can report a middle timestamp as
`incoming_oldest_published_raw`. The existing handler test compares against
`incoming.last()` and encodes the same assumption. The blast radius is one
observational diagnostic string: detection still commits the poll, and no
filing or identity is dropped. G7 enumerated the public value-domain and named
response-shape release criteria. Both honestly declare semantic R-CLOSE
adjudication; no bounded detector exists from current authorities without
first materializing a machine-readable historical surface/value-domain
contract, so no implementation was added.

The first sandboxed loopback test and dependency-install attempts were
environment non-results; their exact entry points passed with the needed
permissions. The operator explicitly authorized Repomix 1.17.0 after its
direct networked execution was rejected for repository-egress risk. It was
installed with lifecycle scripts disabled in an isolated temporary directory
containing no repository data, then executed against the repository only in
the network-restricted sandbox; the real `./run export-check` passed. No
publisher request, scheduler run, model-server session, historical ref
movement, protected-byte change, dependency change, route change, or public
value-domain change occurred.

**Active v0.27 continuation:** CADENCE-CRITERION, COVERAGE-DETECTION,
ADMISSION-LANGUAGE, MULTI-ORIGIN, and RE-MEASURE are also complete.
Current constrained Python 3.11.4 and 3.12.13 lanes each collected and passed
**293** with zero skips; their comparator derived `collected=293`,
`equivalent=true`, and `equivalent_passed=293`. The architecture now records
window advance, not the ten-minute rebuild description, as the governing
cadence criterion; the configured value remains 600 seconds. The manifest
contract now names the disjoint `artifacts[]` and `pinned_files[]` capabilities,
and executing fixtures prove both valid shapes and both exact prohibited shapes.

**v0.27 R-CLOSE selects v0.17.0 and closes on authenticated candidate evidence
(operator decision and measurement 2026-07-30).** Release disposition: release
(as of 2026-07-30). Untagged release commit
`d5969207835c9f27f461d292b169ccb8d6ae5a46` is the immediate parent of the
closing tree. Published v0.16.1 remains unchanged until that closing tree and
its annotated v0.17.0 tag move atomically.

G7 is settled as a reusable criterion. `ARCHITECTURE.md §8`'s shape rule
covers every observable route and response body named in the architecture,
including internal loopback surfaces. Internal classification constrains
access and redistribution; it does not make the named JSON contract
unversioned. Adding the per-source coverage field to `/ingest` therefore
requires the minor release **v0.17.0**. Future additions, removals, renames,
or incompatible reshapes of fields on named internal responses are minor
under the same rule unless the surface is first explicitly removed from the
contract. The separate public value-domain criterion does **not** fire: no
field serialized in a `/v1/*` body gains, loses, or redefines a value.

No corrective trigger was visible at entry: published v0.16.1 is green and
its records remain true. The publication trigger is the operator's explicit
decision to ship the authenticated coverage detector, corrected cadence
criterion, executable admission-language contract, and bounded
mixed-disposition measurement.

Authenticated evidence candidate
`f2b5f7a9ded1b21f3815752cc9e310bd29c1478e` and hosted run
**30545771070**, attempt **1**, are the closing evidence and remain separate
from the untagged release parent. All seven executable jobs passed. The
release-grade audit required paired Sigstore attestations, observed and
accepted **7** identities, rejected **0**, and found no matrix defect. Both
shell comparators derived `collected=293`, `equivalent=true`, and
`equivalent_passed=293`: local passed 293 / skipped 0, while hosted passed 292
plus the one named, reasoned, `on_site` skip.

The coverage determination is overlap/id-only Option 1. For consecutive
successful fixed windows, a shared stable id proves the publication-order
intervals abut only when the publisher's window is contiguous and ids remain
stable across polls. The pinned body derives the measured premises available
at capture: **200 items / zero ascending timestamp inversions**, **200 unique
GUIDs / 200 distinct accession numbers**, and one SEC host. A first window
does not misfire; an identical window reports overlap; a genuinely disjoint
67-held / 66-omitted / 67-incoming pair fires with raw publisher boundary
strings `16:26:17 EDT` / `17:00:13 EDT` and still commits the incoming rows.
Post-insert reassessment returns overlap, independently proving the surfaced
field was computed before insertion. A combined batch reports independently
per source, and cursor-paged OAI-PMH is `not_applicable_paged`. Publisher
re-issue or GUID-form change can produce a visible false positive; zero false
positives and a quantified loss size are not claimed.

The cadence criterion is window advance, not the publisher's ten-minute
rebuild description. The pinned latest-200 sample spans **4,650 seconds /
77.5 minutes** against the unchanged **600-second** interval: **7.75×**
span/poll margin and **12.90%** of the observed span consumed per poll. This
single post-close Wednesday sample does not establish peak-season,
deadline-day, or uncovered-hour density, so it does not imply a number
change. The v0.26 architecture row remains intact; the v0.27 correction is
appended after it. The 600-second schedule has never run, and neither this
cycle nor publication authorizes it to run.

The admission-language change addresses the generator of the fifth and sixth
author-side unsatisfiable requirements without reopening either historical
record. SQLite `artifacts[]` require corpus facts and carry the append-only
admission chain; immutable `pinned_files[]` carry graded evidence,
observation, and exact authorization bytes and forbid `admission`. Executing
fixtures prove both valid containers and the two exact prohibited
cross-container shapes.

The bounded two-origin runtime did occur: exactly four application request
starts evaluated arXiv's source-local HTTP-404 `RfcAllowAll` and SEC's
independent fetched `Body(allow)` in one process-scoped cache. arXiv content
timed out before a page/cursor committed; SEC returned and stored 200
documents. This is opposing-disposition coexistence plus wire-integration
corroboration, not first proof of cache keying or per-host independence. The
origins were sequential, not concurrent harvesters, so T7 did not fire and is
not nearer its trigger.

Of the five conditional production permissions, **three were used**:
`crates/store/src/lib.rs`, `crates/store/src/sqlite.rs`, and
`apps/cored/src/main.rs` implement and surface pre-insert per-source coverage.
**Two were unused:** `crates/ingest/src/lib.rs` and
`crates/ingest/src/rss.rs`. No `edgar:*` extension field was mapped; no
conditional GET was implemented; `config/core.json`, `config/schedule.json`,
the 600-second value, dependencies, schema, protected databases, fixtures,
golden inputs, `crates/extract`, and `crates/view` did not change. Document
identity remains 200 SEC kept / 0 dropped with the shared 26-feature floor and
radius 16 unchanged.

The release-parent changed-path classification is reconciled in eight disjoint
groups against the exact
`v0.16.1..d5969207835c9f27f461d292b169ccb8d6ae5a46` set of **38** paths:

- **Operating contract, architecture, release notes, and status:** `AGENTS.md`,
  `ARCHITECTURE.md`, `CHANGELOG.md`, `README.md`, and `STATE.md`.
- **Release version authorities:** `Cargo.lock`, `apps/cored/Cargo.toml`,
  `shell/intel_shell/__init__.py`, and `shell/intel_shell/app.py`.
- **Product behavior:** `apps/cored/src/main.rs`,
  `crates/store/src/lib.rs`, and `crates/store/src/sqlite.rs`.
- **Executing controls:** `config/invariant-rules.json`,
  `crates/ingest/tests/sec_observation_replay.rs`,
  `shell/tests/test_evidence_artifacts.py`,
  `shell/tests/test_invariant_scan.py`, `shell/tests/test_scheduler.py`, and
  `tools/invariant_scan.py`.
- **Cycle and forward-publication records:**
  `docs/cycles/PROGRESS-v0.26.md`, `docs/cycles/PROGRESS-v0.27.md`, and
  `docs/cycles/TASKS-v0.27-EXECUTION.md`.
- **Window measurement:** `observations/v0.27/sec-latest-window-margin.md`.
- **Append-only provenance authority:** `config/protected-artifacts.json`.
- **Authenticated hosted evidence:** all fourteen files under
  `evidence/ci-runs/30545771070-1/` and
  `evidence/v0.27/deferred-audit/report.json`.

The exact release parent passed all **20/20** local jobs with
warning-denied **145** workspace tests and **62** net tests (**32 ingest + 30
cored**), locked Rust 1.78, clean rustc/clippy/fmt/ShellCheck, and
`invariant-scan` **12 rules / 46 planted controls**. Constrained Python 3.11.4
and 3.12.13 each collected and passed **293** with zero skips. Embedded and
standalone golden both passed **11/11** without changing the expected bytes.
`version-check`, `cycle-check`, `checklist-audit`, `progress-check`,
manifest validation, protected-artifact verification, and evidence reporting
all passed. Project-root `export-check` passed **99** derived sources, **7**
required paths, and **180** exported files. No publisher request or scheduler
run occurred.

**v0.17.0 post-push forward verification (measured 2026-07-30).** The atomic
push moved remote `main` and annotated `v0.17.0` together. Remote inspection
resolves `main` and the peeled tag to closing commit
`4af2841816dd3e43fb8423153b91aa22ccb87537`, while the annotated tag object is
`df4fc3b044ca12335e773dcc0b9bdd4e0db90afd`; the closing commit's immediate
parent remains release commit
`d5969207835c9f27f461d292b169ccb8d6ae5a46`.

- **Post-push verification date:** 2026-07-30
- **Post-push release:** `v0.17.0`
- **Post-push annotated tag object:** `df4fc3b044ca12335e773dcc0b9bdd4e0db90afd`
- **Post-push closing commit:** `4af2841816dd3e43fb8423153b91aa22ccb87537`
- **Post-push hosted run:** `30550582370`

Post-push run **30550582370**, attempt **1**, passed all seven executable jobs
at the exact closing commit; the dependency-drift job skipped under its
declared report-only condition. Fresh local Python 3.11.4 and 3.12.13 lanes
each collected and passed **293** with zero skips. For each hosted lane,
`tools/test_population.py` derived
`{"collected":293,"equivalent":true,"equivalent_passed":293,"hosted":{"on_site_skipped":1,"passed":292,"skipped":[{"node_id":"tests/test_deferred_audit.py::test_on_site_production_measurements_match_committed_receipt","reason":"on-site production audit requires protected corpora and built cored"}]},"local":{"passed":293,"skipped":0},"schema_version":1}`.
The complete hosted-log search found no SEC or arXiv URL and no harvest
command. Its `usgaap.rss` matches were local `PIN MATCH` lines for the
committed observation; its `curl` matches were the pinned rustup action's
installer command, not publisher traffic. Closing-tree standalone golden
remained **11/11**.

The protected manifest remains below its accepted bounds: **301** pins,
**174,152 bytes**, and two consecutive complete verifications at **0.16 s /
0.10 s real**. A4, editable L1, the R3/R4 open-bottom limitations, the
active-runbook measured-value heuristic, T7, robots negative-cache Decision B,
scheduled L2, FastAPI version-literal relocation, and terms-gate operator
responsibility remain open or unchanged.

## v0.27 active execution

**WINDOW-MEASURE derives the SEC latest-window margin and corrects its authored
elapsed-time premise (measured 2026-07-30).** The committed test
`derives_sec_latest_window_timing_from_pinned_body` first enforces the pinned
892,641-byte body and SHA-256, then parses all item timestamps and derives 200
items from `Wed, 29 Jul 2026 16:13:52 EDT` through
`Wed, 29 Jul 2026 17:31:22 EDT`: **4,650 seconds / 77.5 minutes**, 199
consecutive gaps, **11 seconds median**, **215 seconds maximum**, and EDT hour
counts `{16: 133, 17: 67}`. It also confirms channel `lastBuildDate` and
`pubDate` at `Wed, 29 Jul 2026 21:50:03 EDT`.

The general safety criterion is: for consecutive successful polls over a
stable fixed latest-N identity set, the window is covered if and only if the
poll interval is shorter than the time the window takes to advance by N items.
The two terms measured here are the committed **600-second poll interval** and
this sample's **4,650-second latest-200 span**. Their observed ratio is `4,650
/ 600 = 7.75`; equivalently, one poll consumes **12.90%** of the measured
span. This is one post-close window on one Wednesday. It does not establish
peak-season density, deadline-day density, or density during hours neither live
sample covered.

The committed capture timestamps also correct the runbook's drafted **7h28m**
idle interval. `2026-07-30T03:34:00Z` to
`2026-07-30T09:18:39.680936Z` is **5h44m39.680936s / 20,679.680936
seconds**. Both observations fell outside filing hours; their bodies,
SHA-256, and `lastBuildDate` were unchanged. That refutes “updated every 10
minutes” as a description of observable behavior during the idle interval,
while simultaneously failing to test window velocity because no filing
arrived.

Focused replay passed **2/2**; warning-denied workspace passed **140**, and
warning-denied net lanes passed **31 ingest + 26 cored = 57**. Clippy and fmt
passed. The identity control remained **200 SEC kept / 0 dropped**, and golden
remained byte-identical at **11/11**. `config/schedule.json` did not change,
the scheduler did not run, no production source changed, and no publisher
request was made.

**CADENCE-CRITERION corrects the architectural reason while retaining the
measured value (measured 2026-07-30).** A new dated operational-disposition row
follows the byte-identical v0.26 cadence row. It records window advance time as
the governing loss quantity, the unchanged 600-second poll against the
4,650-second sample span, the **7.75× / 12.90%** margin, and the peak-season,
deadline-day, and uncovered-hour evidence gaps. The positive sample margin does
not imply a cadence change, so no number change is recommended from this
measurement. The terms determination and coverage objective remain separate and
unsatisfied by this correction.

The executing scheduler test reads the v0.27 architecture row, resolves the
committed SEC job to 600 seconds through `load_schedule` and `build_jobs`, and
compares the values. Its planted architecture value of 601 seconds raises the
expected mismatch, so the check can fail and is not vacuous. The focused test
passed **10/10** under both interpreters; the complete constrained Python 3.11
and 3.12 lanes each collected and passed **292** with zero skips, and their
comparator derived `equivalent=true` / `equivalent_passed=292`. Golden remained
**11/11**. Hash comparison proves both the v0.25 terms row and v0.26 cadence row
are byte-unchanged; `config/schedule.json` is byte-unchanged. No publisher
request or scheduler run occurred.

**ADMISSION-LANGUAGE makes the manifest-container contract executable
(measured 2026-07-30).** `AGENTS.md` and `ARCHITECTURE.md` now name schema v2's
disjoint containers: `artifacts[]` requires the SQLite `expected` shape and
carries the chained `admission` record; `pinned_files[]` carries graded
immutable bytes under `evidence/` or `observations/`, plus exact registered
authorization paths, and forbids `admission`. The operating contract now
requires every pinning task to name its container and classifies a requirement
expressible by neither container as an author-side defect. The fifth and sixth
v0.26 instances are recorded only as motivating data and are not reopened.

The executing fixture validates one SQLite artifact and three pins covering
evidence, observation, and authorization grades. It then proves the two exact
rejections: `extra=['admission']` under `pinned_files[]` and
`missing=['expected']` under `artifacts[]`. This proves the documentation
matches the validator today; it cannot prevent future validator drift, while
v0.27's explicit prohibition on editing the validator controls that limitation
for this cycle. Full constrained Python 3.11 and 3.12 lanes each collected and
passed **293** with zero skips; their comparator derived `collected=293`,
`equivalent=true`, and `equivalent_passed=293`. `invariant-scan` remained
**12 rules / 44 controls**, and golden remained **11/11**.
`tools/evidence_artifacts.py` remained SHA-256
`3e5e0c5ff6e12c25180833124faaaf91dc43b5171e893e83500e029d04e99af5`;
`config/protected-artifacts.json` remained SHA-256
`8711aa1b95d6071c6492594aa20a3c4ab8a1756ffe4b5ed72b5208f39ed9a3da`.
No production source changed and no publisher request was made.

**COVERAGE-DETECTION makes a fixed-window rollover visible without failing the
poll (measured and authorized 2026-07-30).** The operator selected the id-only
overlap watermark. Its exact no-gap claim is conditional: when each fetched
window is a contiguous interval in publication order and document ids remain
stable across polls, any id shared with the source's stored corpus proves the
old and new covered intervals abut. The pinned SEC body re-derives both measured
premises available in this sample: **200 items with zero ascending inversions**
in document order and **200 unique SEC GUIDs containing 200 distinct accession
numbers**, with each parsed id derived from its source id and GUID. Accession
immutability supports id stability; stability across an actual publisher
re-issue remains a dependency rather than a property this single body executes.

For every successful non-paged source, cored now asks the store about overlap
**before** the combined tail `append_new`, passing that source's id and its own
document slice. The resulting per-source field is computed pre-commit and
carried into `IngestSourceResult`; it is not populated by a default or
back-filled after insertion. A fresh source reports `first_window`, an
identical window reports `overlap`, and an empty incoming window reports
`empty_window`. An empty overlap against a non-empty source reports
`gap_detected` in the response and human-readable log, with the publisher's raw
`held_newest_published_raw` and `incoming_oldest_published_raw` strings. It
still commits the incoming documents. This is deliberately a conservative
visible finding, not proof that a filing was lost: a publisher re-issue or a
change in GUID form can cause a false positive. The implementation neither
claims zero false positives nor quantifies the gap. Cursor-paged OAI-PMH
reports `not_applicable_paged`, because page-to-page id overlap is not a valid
coverage condition there.

Execution against the pinned body proved the fresh **200-document** poll reports
`first_window`, then the identical poll reports `overlap` with **0 new**. A
genuinely disjoint pair kept 67 older documents, omitted the 66 intervening
items, then ingested 67 newer documents; it reported `gap_detected`,
`held_newest_published_raw="Wed, 29 Jul 2026 16:26:17 EDT"`, and
`incoming_oldest_published_raw="Wed, 29 Jul 2026 17:00:13 EDT"`, while committing
all 67 incoming rows. Re-assessing after insertion returned `overlap`, proving
the surfaced result came from the pre-insert check. A combined two-source
non-paged ingest independently reported overlap for one source and a gap for
the other; an OAI-PMH fixture reported `not_applicable_paged` while committing
its cursor.

R12 now carries **18 planted controls**, and the repository total is **12 rules
/ 46 controls**. The two new mutations move an insert before assessment and
replace the per-source document slice with the combined fetched batch; both
produced their expected failures. Full local CI passed **20/20** jobs:
warning-denied **145** workspace tests and **62** net tests (**32 ingest + 30
cored**), clean locked Rust 1.78, clippy, fmt, ShellCheck, and both constrained
Python lanes at **293/293** with zero skips. The first sandboxed Python 3.12
attempt could not perform its loopback/process checks and was a non-result; the
same entry point passed with the required local permissions. The identity
fixture still measured the 200 SEC documents as **200 kept / 0 dropped**
(alongside one separately kept filings-digest document), and standalone golden
remained byte-identical at **11/11** with its Hamming-12 collapse.
`crates/extract`, `crates/view`, `config/schedule.json`, `config/core.json`, and
the protected-artifact manifest are byte-unchanged. The allowed
`crates/ingest/src/lib.rs` and `crates/ingest/src/rss.rs` production permissions
were unused. No publisher request was made.

**MULTI-ORIGIN confirms source-local missing-policy isolation in one bounded
runtime (authorized and measured 2026-07-30).** The authorization basis was
corrected before execution: focused tests already prove per-origin robots
keying/reuse and per-host limiter independence. The live question was whether
arXiv's permissive missing-policy and SEC's restrictive missing-policy could
coexist in the same process-scoped cache without bleeding across origins.

Before network, exact focused tests proved `max_pages: 1` bounds OAI-PMH to one
content request and checkpoints a non-terminal page's next token plus
`pending_high_water` without advancing completed `high_water`; a terminal
first page advances `high_water`. The first incorrectly filtered zero-test
invocation was a vacuous non-result, and the exact test then passed **1/1**.
The exact store cursor lifecycle test also passed **1/1**. Artifact validation
and `./run verify-artifacts` passed before and after with all **286** pins and
both protected databases exact. A `data/core.db` harvest attempt exited **2**
before network, proving the protected-target refusal stood.

The plaintext-observable construction used a disposable, out-of-tree copy of
the current runtime. The `/ingest`, source registry, gate, cursor adapter, and
store logic were current production bytes; only its net transport was wrapped
to write plaintext observations and refuse any repeated or fifth request
before `send`. The formatted observer source SHA-256 was
`72783cb5e1b6848d1675bd3bcf608872676781bf39520b394f9af027d91baa33`,
and its two-source config SHA-256 was
`7646cff12d6c9df9e9727cdae94bb0957c3e168fcaa2ead1f7893b66138f26c0`.
A planted pre-existing request marker made a separate attempted run refuse
before network and emit no response file, so the quota control can fail. A
sandboxed macOS proxy-config panic was an environment non-result and made no
request.

One authorized `/ingest` selected `arxiv-cs` then
`sec-edgar-usgaap` in the same runtime. Exactly **4** application-level request
starts crossed the observer's `send` boundary, **2 per origin**: one robots and
one content attempt. There was no redirect, retry, second page, fifth request,
or scheduler.

| derived origin key | robots response | effective missing-policy | outcome |
|---|---|---|---|
| `https://oaipmh.arxiv.org` | 404; 11,083 bytes; SHA-256 `fe5a8ce88b89f96db55e8d9a7eb3d978f3d364bf31d48c4880422511e9035ab2` | `allow` → `RfcAllowAll` for absence only | allowed |
| `https://www.sec.gov` | 200; 2,622 bytes; SHA-256 `72d6196b3f20737396e566ddeb769fb4174b44f334985a1267a59ae0f08c2f2f` | `deny` | `Body(allow)` |

Both fresh robots bodies were byte-identical to the committed captures. arXiv
therefore still exercised the missing-policy branch; SEC was evaluated after
arXiv occupied the same cache and retained its own `Body(allow)` result. This
independently asserts that arXiv's `RfcAllowAll` did not affect SEC.

Request-start intervals were **1.827372 seconds** within arXiv, **60.004385
seconds** from arXiv content to SEC robots, **1.313344 seconds** within SEC,
and **61.831757 seconds** between robots requests. The arXiv content request
timed out at the shipped 60-second limit, so this run did not display a
cross-origin interval below the 0.5-second per-host floor. Such a shorter
cross-origin interval would be expected and correct because the host clocks
are independent. The focused cache-reuse, per-host limiter, and slow-host/
fast-host tests each passed **1/1**; the live novelty is opposing-disposition
coexistence, while keying and spacing are wire-integration corroboration.

The response was **200 fetched / 200 new**. ArXiv reported `ok:false`, zero
documents, `coverage:not_applicable_paged`, and the content timeout; because no
page parsed, it committed no cursor, pending high-water, completed high-water,
or document. Publisher receipt is not claimed from the absent response. SEC
reported `ok:true`, 200 documents, and `coverage:first_window`. The successful
arXiv page/cursor and SEC `overlap` hoped for as secondary corroboration were
therefore not observed and were not relabeled as successes; the request budget
was not expanded to retry or pre-seed.

The fresh, ignored, unadmitted archive
`data/live-20260730T125247Z-99839.db` is **253,952 bytes**, SHA-256
`47f64b7ebe690b0987b17af404b384cad2abdea7eb0e4b83e9dc54534a8d422c`,
with integrity `ok`, **200** SEC documents, **200** distinct non-null
canonical ids, and zero cursor rows. T7 did not fire and is not nearer its
trigger: two sequential sources are not concurrent harvesters. A successful
live arXiv checkpoint, a sub-floor cross-origin interval, and the 600-second
schedule remain unexercised.

Full local CI passed **20/20** jobs: warning-denied **145** workspace tests,
**62** net tests (**32 ingest + 30 cored**), locked Rust 1.78,
invariant-scan **12 rules / 46 controls**, clippy, fmt, and ShellCheck. Both
constrained Python lanes collected and passed **293** with zero skips.
Standalone golden remained byte-identical at **11/11**.
`config/core.json`, `run`, `config/protected-artifacts.json`, both protected
databases, and production compliance, ingest, extract, view, and shell source
are byte-unchanged. The archive was not admitted to protected evidence or
golden.

**v0.27 RE-MEASURE authenticates the neutral evidence candidate before any
publication decision (authorized and measured 2026-07-30).** Exact candidate
`f2b5f7a9ded1b21f3815752cc9e310bd29c1478e` was pushed only to
`refs/heads/codex/v0.27-evidence-f2b5f7a`. Remote `main`, the historical
candidate refs, and the annotated `v0.16.1` tag remained unchanged. Hosted
workflow-dispatch run **30545771070**, attempt **1**, executed that exact
candidate/ref and passed all seven executable jobs: core, golden, lint, MSRV,
net, shell 3.11, and shell 3.12. Report-only dependency drift skipped as
designed.

Fresh local Python 3.11.4 and 3.12.13 lanes each collected and passed **293**
with zero skips. For each hosted lane, `tools/test_population.py` derived
`{"collected":293,"equivalent":true,"equivalent_passed":293,"hosted":{"on_site_skipped":1,"passed":292,"skipped":[{"node_id":"tests/test_deferred_audit.py::test_on_site_production_measurements_match_committed_receipt","reason":"on-site production audit requires protected corpora and built cored"}]},"local":{"passed":293,"skipped":0},"schema_version":1}`.
The single hosted skip is named, carries the declared reason, and is marked
`on_site`; no unnamed or unmarked skip was accepted.

All seven receipts and seven paired Sigstore bundles are exact `pinned_files[]`
with `supporting` grade and no `admission` key. Each bundle verified its paired
receipt bytes, repository, CI workflow, candidate digest, source ref, and
GitHub-hosted runner policy. The generated release-posture report is **34,995
bytes**, SHA-256
`67b0c7a5488293cba8bc38e410bd24c748af6f1598481a23a37eeb623ec8dc64`,
grade `release`, with attestations required. It accepted all **7** observed
runner identities, rejected **0**, found no matrix finding, and recorded **5
deferred / 2 promoted / 0 implemented deferred subsystems**. These fifteen
new pins move the manifest from **286** to **301**; both protected databases
remain byte-unchanged. Manifest validation, `verify-artifacts`,
`evidence-report`, and authenticated clean-subject re-derivation passed.

No hosted publisher request occurred. The candidate workflow contains no
publisher URL or publisher-directed ingest command. Complete hosted-log search
found only two `usgaap.rss` occurrences, both local `PIN MATCH` output for the
committed SEC observation; the broader `curl` search found only the rustup
installer URL. A sandboxed `ci-local` rerun could not bind its loopback
wire-test socket and was a non-result; the exact command passed all **20/20**
jobs with its required local permissions. Hosted and standalone golden both
remained **11/11**. The exact evidence directory and manifest pins are the
only Step 7 evidence admissions; no production source, protected database,
publisher configuration, schedule, or identity changed.

## v0.16.1 post-push verification

- **Post-push verification date:** 2026-07-30
- **Post-push release:** `v0.16.1`
- **Post-push annotated tag object:** `ae593e882898b9c49d5e91e2d50b6ca1f02ac49b`
- **Post-push closing commit:** `397d100ae425d5d059cef8a8ddb2ac13cfde52f5`
- **Post-push hosted run:** `30535121730`

Remote `main` and the peeled `v0.16.1` tag both resolve to closing commit
`397d100ae425d5d059cef8a8ddb2ac13cfde52f5`; annotated tag object
`ae593e882898b9c49d5e91e2d50b6ca1f02ac49b` names that closing commit, whose
immediate parent is release commit
`b9af84b8785bcd52c16ab0225d66386ecd872c4d`. Historical
`refs/heads/candidate/v0.16.0` remains v0.15.1 evidence at
`3481e4ba85d65c927b7d0fc3a430bc04fb094394`.

Post-push CI run **30535121730**, attempt **1**, executed at the exact closing
commit and passed all seven executable jobs: core, lint, golden, net, shell
3.11, shell 3.12, and MSRV; the report-only dependency-drift job was skipped
as designed. Hosted execution reported **139** workspace tests and **56** net
tests (**30** `intel-ingest`, including replay, plus **26** `cored`);
checklist-audit reported **208 checked / 3 retracted / 208 matched / 0
exemptions**; invariant-scan reported **12/12 rules / 44 controls**;
manifest validation reported **286** pins; and golden passed **11/11**.

Both post-push machine-readable population comparisons returned:
`{"collected":291,"equivalent":true,"equivalent_passed":291,"hosted":{"on_site_skipped":1,"passed":290,"skipped":[{"node_id":"tests/test_deferred_audit.py::test_on_site_production_measurements_match_committed_receipt","reason":"on-site production audit requires protected corpora and built cored"}]},"local":{"passed":291,"skipped":0},"schema_version":1}`.
The one hosted skip is named, reasoned, and marked `on_site`; both Python lanes
therefore match the local population exactly under the registered comparator.

Authenticated candidate run **30531390933**, attempt **1**, remains the
closing evidence because it supplied the required signed attestations.
Post-push run **30535121730** is forward confirmation of the published closing
commit and does not replace that evidence. Complete hosted-log inspection found
no publisher URL or publisher-directed request command; its only two
`usgaap.rss` matches were local `PIN MATCH` output. No publisher request was
made by publication or verification.

This post-push record is the first commit after the tagged closing commit. It
is supported by the required local gates but is intentionally hosted-unverified
until the following publication, when it becomes an ancestor of the next
candidate and release commit.

**v0.26 R-CLOSE selects v0.16.1 and closes on authenticated candidate evidence
(operator decision and measurement 2026-07-30).** Release disposition: release
(as of 2026-07-30). Untagged release commit
`b9af84b8785bcd52c16ab0225d66386ecd872c4d` is the immediate parent of the
closing tree.

The patch criterion fires because this cycle corrects near-duplicate behavior
within existing routes, fields, types, body shapes, and public value sets. The
public value-domain criterion added at v0.25 does **not** fire: no serialized
`/v1/*` field gains, loses, or redefines a value. No corrective trigger was
visible at entry; published v0.16.0 is green and its records are true. The
publication trigger is the operator's explicit decision to ship the
authenticated identity correction, explicit SEC cadence, and bounded
first-contact validation.

Authenticated evidence candidate
`1cd88acd99704cc76c866331e505db446936e469` and hosted run
**30531390933**, attempt **1**, are the closing evidence and remain separate
from the untagged release parent. All seven executable jobs passed. The
release-grade audit required paired Sigstore attestations, accepted **7**
identities, rejected **0**, and confirmed the complete matrix. Its protected
report is 34,937 bytes at SHA-256
`267c23c676b0e227584d0eb9647d0ce8c4595804fb39e6ac5047691d066d0f25`.

The identity determination is the operator-selected feature-floor option.
Under the shipped radius 16, the parser-produced 200 SEC documents yielded
172 kept / 28 dropped: 8 same-issuer and **20 cross-issuer false collapses**.
The mechanism was a fixed 64-bit Hamming radius over fingerprints built from
only 4–10 three-token features, compared with the calibrated news corpus's
26–42. `intel-extract` now owns one `DEDUP_MIN_FEATURES = 26` two-sided guard,
and both store canonicalization and view collapse invoke it. Both shipped
paths keep all 200 SEC documents; the independently fetched live sample also
kept **200 / dropped 0**. Golden remains byte-identical at **11/11** and still
drops `techwire::tw-004` for `osdaily::osd-004` at Hamming 12, proving the
change did not overshoot. The measured cost is intentional under-collapse:
sparse documents, including two distance-zero pairs in the SEC sample, remain
visible.

The committed replay executed shipped `RssSource::fetch` over the exact
892,641-byte observation and constructed **200** documents. The XML declares
`windows-1252`, but the response is ASCII-only: reqwest's charset-less string
path decoded those bytes as UTF-8 and roxmltree accepted them losslessly. No
general non-UTF-8 decoder branch executed or was established. All 15 observed
`edgar:*` extension local names remain enumerated but unmapped.

G3 found zero observation paths in the manifest. Authorized Step 2B therefore
added the `observations/` prefix and `observation` grade and pinned all five
v0.25 files without an admission key, increasing 266 pins to 271. Step 7's
authenticated receipt/bundle set and release report raised the final total to
**286**. A pin detects later byte change; only the v0.25 wire record
establishes what the publisher served.

The bounded live SEC ingest did occur: **200 fetched / 200 new**, followed by
one separately authorized corrective robots request and one feed request. No
scheduler ran, no scheduled SEC run has occurred, and no production runtime
has exercised both publisher origins together. No `edgar:*` field was mapped;
no ingest or compliance production source, `config/core.json`, dependency,
schema, protected database, fixture, or golden input changed.

Every conditional source permission was used. `crates/extract/src/lib.rs`
owns the feature-floor authority and guard; `crates/store/src/sqlite.rs` and
`crates/view/src/lib.rs` invoke it while retaining their synchronized
boundary-local radius declarations. Authorized Step 2B used
`tools/evidence_artifacts.py`. No conditional source permission is unused.
The only R-CLOSE change to `shell/intel_shell/app.py` is the mechanical public
version literal; the recorded relocation option remains unused.

Two v0.26 blockers retain their distinct dispositions. Step 2's original
pin-first rule is the fifth author-side rule with no satisfying assignment:
`artifacts[]` requires SQLite-only expected facts, while `pinned_files[]`
originally rejected an observation path and cannot carry `admission`. The
CADENCE retrieval is a cycle-execution gate violation with an author-side
ambiguity; its content remains quarantined and uncited, and **retractions
remain three**. Step 7 later exposed the sixth author-side unsatisfiable rule:
receipts cannot truthfully enter `artifacts[]`, while `pinned_files[]` rejects
an `admission` key. Its operator-approved replacement uses immutable pins plus
paired authenticated provenance without weakening either schema.

The release-parent changed-path classification is exact in eight disjoint
groups and matches the committed
`v0.16.0..b9af84b8785bcd52c16ab0225d66386ecd872c4d` set of **44** paths:

- **Operating contract, architecture, release notes, and status:** `AGENTS.md`,
  `ARCHITECTURE.md`, `CHANGELOG.md`, `README.md`, and `STATE.md`.
- **Release version authorities:** `Cargo.lock`, `apps/cored/Cargo.toml`,
  `shell/intel_shell/__init__.py`, and `shell/intel_shell/app.py`.
- **Product behavior and cadence:** `config/schedule.json`,
  `crates/extract/src/lib.rs`, `crates/store/src/sqlite.rs`, and
  `crates/view/src/lib.rs`.
- **Executing controls:** `config/invariant-rules.json`,
  `crates/ingest/tests/sec_observation_replay.rs`,
  `crates/store/tests/sec_identity_measure.rs`,
  `shell/tests/test_cycle_check.py`,
  `shell/tests/test_evidence_artifacts.py`,
  `shell/tests/test_offline_fixtureless_ingest.py`,
  `shell/tests/test_scheduler.py`, `tools/cycle_check.py`,
  `tools/evidence_artifacts.py`, and `tools/invariant_scan.py`.
- **Cycle and forward-publication records:**
  `docs/cycles/PROGRESS-v0.25.md`, `docs/cycles/PROGRESS-v0.26.md`, and
  `docs/cycles/TASKS-v0.26-EXECUTION.md`.
- **Replay and identity measurements:** both files under
  `observations/v0.26/`.
- **Append-only provenance authority:** `config/protected-artifacts.json`.
- **Authenticated hosted evidence:** all fourteen files under
  `evidence/ci-runs/30531390933-1/` and
  `evidence/v0.26/deferred-audit/report.json`.

The protected manifest remains below its accepted bounds: **286** pins,
**165,488 bytes**, and two consecutive complete verifications at **0.11 s /
0.10 s real**. A4, editable L1, the R3/R4 open-bottom limitations, the
active-runbook measured-value heuristic, T7, robots negative-cache Decision B,
scheduled L2, FastAPI version-literal relocation, terms-gate operator
responsibility, and live multi-publisher behavior all remain open or
unchanged. The one supported SEC harvest caller and zero running schedulers do
not move T7 nearer its trigger.

**v0.26 RE-MEASURE admits authenticated hosted evidence after the approved
schema-2 correction (measured 2026-07-30).**

The operator approved replacing the impossible chained-receipt clause with
immutable `pinned_files` registration plus paired Sigstore verification. The
seven receipt JSON files and seven bundles from run **30531390933**, attempt
**1**, are registered under `evidence/ci-runs/30531390933-1/` with grade
`supporting`; no `admission` key was added and no receipt was misclassified as
a SQLite artifact.

Release-posture audit
`evidence/v0.26/deferred-audit/report.json` is **34,937 bytes**, SHA-256
`267c23c676b0e227584d0eb9647d0ce8c4595804fb39e6ac5047691d066d0f25`.
It measured a clean detached subject at exact hosted candidate
`1cd88acd99704cc76c866331e505db446936e469`, required attestations, accepted
**7** distinct successful identities, rejected **0**, and confirmed the
single-run matrix complete. The authenticated boundary is repository
`jiayanzeng/intel-platform`, workflow
`jiayanzeng/intel-platform/.github/workflows/ci.yml`, source digest
`1cd88acd99704cc76c866331e505db446936e469`, and source ref
`refs/heads/codex/v0.26-evidence-1cd88ac`.

The report recorded **5 deferred / 2 promoted / 0 implemented deferred
subsystems**. Its exact-cosine p95 over the 2,600-document protected archive
was **9.289042 ms**, still below the 16.264 ms A3 anchor. T7 remains deferred:
one supported simultaneous harvest caller was measured and zero schedulers were
active; the v0.26 SEC work did not move that trigger nearer.

Manifest schema validation, `verify-artifacts`, and `evidence-report` pass with
**286** pinned files and both protected databases exact. This supersedes the
blocked disposition below without deleting it: the blocked attempt correctly
records why the original runbook wording could not be satisfied, and the dated
operator amendment records why the replacement is valid.

**v0.26 RE-MEASURE passed hosted execution but its admission clause has no
satisfying schema-2 form (measured 2026-07-30).**

The operator authorized the one Step 7 neutral-branch push. Exact candidate
`1cd88acd99704cc76c866331e505db446936e469` was pushed only to
`refs/heads/codex/v0.26-evidence-1cd88ac`; remote `main` remained
`c66c2b02191e3ca3126dddc3c004b175899b414e`, the historical
`refs/heads/candidate/v0.16.0` remained
`3481e4ba85d65c927b7d0fc3a430bc04fb094394`, and no tag was created. The
remote and local CI workflow blobs were byte-identical at
`48ea726b798f1049e0b29cce1f0c64588861c2dd`.

Authenticated hosted run **30531390933**, attempt **1**, passed all seven
executable jobs at that exact candidate. For each of Python 3.11 and 3.12,
`tools/test_population.py` derived `collected=291`, `equivalent=true`, and
`equivalent_passed=291`: local passed **291 / skipped 0**, while hosted passed
**290** plus one named `on_site` skip,
`tests/test_deferred_audit.py::test_on_site_production_measurements_match_committed_receipt`,
with reason “on-site production audit requires protected corpora and built
cored”. Hosted golden passed **11/11** and `invariant-scan` passed **12/12
rules / 44 controls**.

No hosted publisher request occurred. The workflow contains no harvest or
ingest command. A case-insensitive search of the complete hosted log found
zero `sec.gov`, `harvest-arxiv`, `POST /ingest`, publisher URL, or
publisher-directed HTTP command. Its two `usgaap.rss` matches were both
`PIN MATCH` messages for the committed local observation path, not network
commands. Dependency setup did fetch Rust tooling from `sh.rustup.rs`; that is
not a publisher request and is not being hidden by the publisher-specific
audit.

Step 7 step 3 nevertheless requires the receipt/bundle set to carry “a chained
admission record.” Executed schema 2 has no container for that combination.
Submitting a receipt as `pinned_files[271]` with `admission` failed:
`keys differ; missing=[], extra=['admission']`. Submitting it as
`artifacts[2]` failed: `keys differ; missing=['expected'], extra=[]`; supplying
that `expected` object would assert SQLite document, integrity, fingerprint,
canonical-id, and cursor facts about a JSON receipt. The valid evidence
container is `pinned_files`, but it deliberately has no chain because a new
receipt is admitted at a new immutable path rather than by changing an
artifact's expected hash.

This is the sixth author-side rule with no satisfying assignment under the
operator's Amendment 1 criterion, not an implementation or hosted-CI defect.
The fourteen downloaded receipt/bundle files remain outside the repository;
none is pinned, the exact evidence-directory scope amendment has not been
claimed, and the manifest remains at **271** pins. RE-MEASURE stays unchecked
and R-CLOSE stays blocked pending an operator amendment that withdraws or
replaces the impossible chain clause.

That disposition was true at the stop. The operator subsequently approved the
schema-2 replacement recorded immediately above; the evidence is now admitted
without rewriting this historical finding.

**v0.26 HARVEST crossed the SEC wire and the corrective observation closed its
evidence gap (measured 2026-07-30).**

The operator authorized Step 6 under seven stated conditions. The authorization
covered one bounded SEC harvest, not the 600-second scheduler. No scheduled run
occurred, and that larger traffic commitment remains unexercised.

Preflight passed all **271** pins and both protected databases. An explicit
`CORE_DB=data/core.db ./run harvest-arxiv` invocation was refused before its
reachability step, and the harness printed the fresh absent destination
`data/live-20260730T084234Z-16401.db`. A `-D warnings` net build then started
the committed core configuration on unused loopback port 8788 with the
monitored `.env` contact. The exact ingest body selected only
`finance` / `sec-edgar-usgaap`; no scheduler or arXiv source ran.

At **2026-07-30T08:47:16.394914Z** a target-restricted CONNECT observer accepted
the first `www.sec.gov:443` TLS connection, and at
**2026-07-30T08:47:17.646652Z** it accepted the second: **2** SEC-origin TLS
connections, **1.251746 seconds** apart. The shipped log recorded
`Body(allow)` for `/Archives/edgar/usgaap.rss.xml` with a 0.500-second effective
floor. The ingest returned **200 fetched / 200 new**, source `ok:true`, and the
process was stopped. The observer recorded 594 / 9,318 encrypted bytes on the
first connection and 706 / 902,479 on the second. No second origin was
exercised, so the per-origin cache/limiter result is SEC-only and cannot claim
two-origin runtime behavior.

The fresh unadmitted archive is **253,952 bytes**, SHA-256
`00b221483d58870f7841582f5afa9f0e3f6d19818e0c9cae1212d8bf6bfc8035`,
and passes SQLite integrity with 200 documents, 200 distinct canonical ids,
zero canonical drops, and zero cursor rows. Executing the shipped guard over
the fresh rows kept **200 / dropped 0** at radius 16 and floor 26. The exact
feature distribution is `{4:40, 5:86, 6:48, 7:20, 8:5, 10:1}`: all 200 remain
below 11, none enters the 11–25 calibration gap, and none is eligible. Two
distance-zero pairs, at 8/8 and 6/6 features, are both kept. This is the
measured under-collapse cost and moves the failure direction from hiding
distinct filings to showing duplicate filings.

All 200 fresh normalized rows have the same ids, titles, descriptions, links,
and raw publication dates as the pinned observation; all 200 descriptions
still equal the pinned `edgar:formType`. The pinned body declares
`windows-1252`, but the fresh declaration was **not measured**. The configured
User-Agent bytes were captured locally without printing the contact: **73
bytes**, SHA-256
`2fc0ac45a37a1c604d0f01d5039fffd0d734857b613de87cb6c848f29acec495`.
The shipped raw-wire control passed for both HTTP clients and its deliberate
mismatch control fired, but the publisher-received plaintext header was not
visible through the TLS relay.

This is an agent-side observation-design failure, not an implementation defect
and not a false wire claim. A CONNECT count is not an HTTP request count:
because TLS remained opaque, the record cannot prove exact publisher statuses,
redirects, retries, the fresh robots body hash, the fresh XML declaration, or
the publisher-received User-Agent bytes. No second feed or robots request was
made to repair the missing evidence. HARVEST remains unchecked pending a
separate operator authorization for a corrective observable replay. The fresh
database remains ignored and unadmitted; no protected byte changed.

The operator then separately authorized that corrective replay. Before any
request, a disposable observer compiled offline against the repository's exact
locked `reqwest 0.11.27`, `tokio 1.52.3`, and shipped ingest/compliance crates.
Its pre-existing-output control was executed and refused before client
construction. All 271 pins and both protected databases matched again.

At **2026-07-30T09:18:38.296998Z**, the observer's recording wrapper issued
exactly one request through the shipped `HttpRobotsFetcher`. `RobotsCache`
and the wrapper each counted **1**, and the shipped cache returned
`Body(allow)` for the SEC feed path. The 2,622-byte body has SHA-256
`72d6196b3f20737396e566ddeb769fb4174b44f334985a1267a59ae0f08c2f2f`
and is byte-identical to the pinned v0.25 policy. The cored operator deny-list
also allowed the path, and the effective host rate remained 2 requests/second.

At **2026-07-30T09:18:39.680936Z**, after both gates and the shared limiter,
the same installed identity issued exactly one feed request. The measured
request-start interval was **1.383946 seconds**. Redirect following and retry
behavior were disabled by construction; the response was HTTP **200**,
`Content-Type: text/xml`, with no `Location` or `Retry-After` header. Its
892,641-byte body has SHA-256
`154556cd81bda4fc2372386bf43aa7b4414335560dd1371c45bae09f1a8d9de3`
and is byte-identical to the pinned v0.25 feed. It therefore still declares
`windows-1252`, contains 200 items, and has description equal to
`edgar:formType` in 200/200 items.

The assigned User-Agent was captured byte-for-byte before the clients ran:
**73 bytes**, SHA-256
`2fc0ac45a37a1c604d0f01d5039fffd0d734857b613de87cb6c848f29acec495`,
and exactly equal to the value installed for the two clients. The contact was
not printed, and the temporary raw contact-bearing file was removed after the
comparison. The corrective phase made one robots plus one feed request to SEC
and no request to any other origin. It did not run the scheduler, touch the
archive, or mutate production configuration. Combined with the original
shipped-core archive and identity measurements above, this closes all seven
operator conditions without rewriting the original opaque attempt as evidence
it did not contain.

HARVEST is complete. The fresh database remains ignored and unadmitted; no
protected artifact changed. No scheduled live run has occurred, the
600-second cadence remains unexercised, and the larger recurring traffic
commitment is not implied by either bounded authorization.

**v0.26 CADENCE chooses the SEC feed's per-source clock and covers the
offline partial failure (measured 2026-07-30).**

The effective pre-change cadence came from executed scheduler resolution:
`quant-desk` had neither a source nor sector map, so it resolved to one full
job every 7,200 seconds and selected every entitled finance source. The chosen
replacement gives `sec-edgar-usgaap` an explicit **600-second** source clock,
keeps `filings-digest` at 7,200 seconds, and keeps the finance refresh at 7,200
seconds. A committed test loads the real schedule, resolves those three jobs,
executes the SEC action, and fails if the source is absent or its cadence
moves.

Every publisher fact came from committed evidence. The Developer Resources URL
and 2026-07-30 read date are in
`observations/v0.25/terms-gate/sec-edgar-terms-determination.md`. The current
process floor of 2 requests/second, the cited publisher ceiling of 10
requests/second, and the absence of publisher `Crawl-delay` are in
`observations/v0.24/publisher-review/sec-edgar-report.md`. The `<description>`
in `observations/v0.25/feed-shape/sec-edgar-usgaap.rss.xml` says the feed
updates every ten minutes. Matching that committed update interval is the
reason for 600 seconds. This scheduling choice is separate from the unchanged
terms determination.

G4 now has an executing shell regression. A failure-capable HTTP transport
returns the exact measured offline finance response: fixture-backed
`filings-digest` is `ok:true`; fixtureless `sec-edgar-usgaap` is `ok:false`
with the absent-`net` error. The full `quant-desk` pipeline prints the
per-source error, continues through view and audit, writes the brief, and
returns 0. Focused tests pass 10/10 in both Python versions. The quarantined
retrieval was not cited, and no publisher request or harvest occurred.

**v0.26 IDENTITY-DECISION guards radius 16 at the measured feature
boundary (selected and measured 2026-07-30).**

The operator selected Option 1, guard by feature count. The claim is narrow:
radius 16 is eligible only when both documents have at least 26 three-token
SimHash features. Twenty-six is the smallest count measured in the calibrated
golden news corpus. The SEC maximum was 10, so 11–25 remains deliberately
ineligible rather than being treated as measured. The cost is explicit:
sparse documents, even identical ones, remain separate identities.

`intel-extract` now owns one compiled `DEDUP_MIN_FEATURES` value and the shared
two-sided eligibility guard. Both `dedup_near` and store
`assign_canonical_ids_tx` compute feature counts from the same title-plus-body
input as SimHash and call that guard before comparing distance. Step 4A's two
boundary-local radius declarations remain 16; the shared guard is applied to
both boundaries. R1 is unchanged because no canonical-identity caller was
added. R5 now observes the floor fixed at 26, the guard's two-sided comparison,
and both production call sites in addition to its prior distance checks.

The parser-produced finance test sent 201 documents through the public store
append path and shipped view dedup. Both paths kept 201 and dropped 0; all 200
SEC rows stayed distinct, so the previously measured 20 cross-issuer drops are
gone. Separate sparse-identical tests prove the guard refuses distance zero.
Golden still drops `techwire::tw-004` for `osdaily::osd-004` at hamming 12,
so the calibrated true positive remains.

Four new R5 planted failures changed the floor, severed one side of the shared
guard, removed the view-side call, and removed the store-side call. All were
detected at their exact production locations. Counts remain **12 rules** and
rise from 40 to **44 controls**. The focused invariant suites passed 22/22 in
both Python versions; full self-test passed 12/12 rules and all 44 controls.
The `-D warnings` workspace passed **139** tests; both full constrained Python
lanes passed **289/289**; clippy and fmt were clean; and golden passed
**11/11** byte-identically. The first sandboxed golden and shell invocations
could not bind loopback ports (and the shell lane could not inspect `ps`);
their approved reruns executed those controls and passed. `config/core.json`
and `config/schedule.json` did not change, and no publisher request was made.

**v0.26 THRESHOLD-AUTHORITY synchronizes the boundary-local declarations
(measured 2026-07-30).**

Store canonicalization and view collapse retain two numeric declarations. This
is deliberate: neither production crate depends on the other, and Step 4A's
allowed scope contains neither a common dependency module nor a manifest edge.
The limitation is explicit in `ARCHITECTURE.md` and R5's registered scope:
this is static equality enforced across two declarations, not one shared
compiled constant. A coordinated change to both still needs separate
behavioral evidence and the Step 4 decision.

R5 now claims exactly what it checks. Every production store identity caller
must bind to the private `DEDUP_MAX_DISTANCE`; exactly one store declaration
must exist; exactly one `ViewParams` default must exist; and the two numeric
values must match. Its new planted failure moves only the view default from 16
to 17 and leaves the store at 16. The real scanner rejected it at
`crates/view/src/lib.rs:44`. No new rule was registered: counts remain **12
rules** and rise from 39 to **40 controls**.

Both declarations remain 16, so product behavior did not move. Python 3.11
and 3.12 focused invariant suites each passed **22/22**; full
`invariant-scan` passed 12/12 rules and all 40 controls; `cycle-check` passed;
and golden remained byte-identical at **11/11**, including the hamming-12
collapse. No store or view production byte, configuration, fixture, protected
artifact, database, dependency, or publisher changed.

**v0.26 IDENTITY-MEASURE finds 20 cross-issuer false collapses
(measured 2026-07-30).**

A committed integration test passed parser-produced `Document` values through
the public store append path, which executed private
`assign_canonical_ids_tx`, then executed `dedup_near` over the store-persisted
fingerprints. Both shipped implementations returned the same 28 drops at
radius 16 from 201 finance inputs: the existing finance fixture stayed kept,
172/200 SEC documents stayed kept, 8 drops joined the same issuer CIK, and
**20 joined a different issuer CIK**. Every dropped id, kept id, distance, and
CIK classification is in the committed measurement record.

The sweep measured total kept / dropped / same-issuer / cross-issuer as
16: 173/28/8/20; 15: 187/14/6/8; 14: 196/5/5/0; 13: 197/4/4/0;
12: 197/4/4/0; 10: 199/2/2/0; and 8: 199/2/2/0. These are corpus facts, not a
recommendation. The fixture's minimum SEC distance is 23 and it participates
in no collapse.

The mechanism is measured. SEC inputs carry 4–10 three-token features with
median 5; the seven golden news RSS documents carry 26–42 with median 40. SEC
has 198 distinct fingerprints and 35/19,900 pairs within radius 16; first-match
canonical selection produces 28 drops. News has one of 21 pairs within radius
16, the intended hamming-12 golden near-duplicate. Sparse feature count is
therefore confirmed as the mechanism on this corpus, without claiming a
general calibration.

All 200 SEC rows share 2026-07-29; after dedup 172 remain beside the
2026-07-03 fixture. The committed gazetteer resolves zero entities, so shipped
analyze observes the 26-day corpus window but constructs no per-entity
baseline, computes no z-score, and emits zero signals or edges. This
concentration is recorded and not acted on.

The draft prediction is confirmed except for its news-feature “28–36”
comparison. Executed news features span **26–42**, median 40. That is an
author-side prediction error, not an implementation defect. The focused
measurement passed 1/1; the `-D warnings` workspace suite passed **137**,
clippy and fmt passed, and golden remained **11/11**. No production source,
configuration, fixture, protected artifact, golden input, database, ref, or
publisher changed.

**v0.26 OBSERVATION-PIN makes observation changes repository-visible
(operator-authorized and measured 2026-07-30).**

`pinned_files` now accepts exactly one third prefix, `observations/`, with
exactly one new grade, `observation`. The existing evidence grades remain
confined to `evidence/`; `observation` is rejected there, and unregistered
prefixes remain rejected. No `admission` key was added: observations are not
procedurally replaceable artifacts.

Three failure controls executed the real validator and captured distinct
rejections: `observations/body.xml` with `supporting`, an
`evidence/report.json` path with `observation`, and
`outside/body.xml` with `observation`. A fourth control copied the committed
manifest and pinned files into a disposable directory, flipped one byte of the
SEC RSS observation without changing its length, and captured the expected
SHA mismatch
`154556cd…` versus
`feb138bb…`.

All five v0.25 observation files are now manifest-pinned, raising the pin count
from 266 to **271**. `python3 tools/evidence_artifacts.py validate` passed
schema 2 with 2 artifacts / 271 pins, and `./run verify-artifacts` matched all
271 files and both databases. Both constrained Python lanes collected and
passed **289** with no skip, and golden remained **11/11**. The limitation is
explicit: a pin detects changed repository bytes; it does not establish that
those bytes are what the publisher served. Only the v0.25 wire record supports
that claim. No publisher request occurred.

**v0.26 REPLAY constructs and records the real document set (measured
2026-07-30).**

The committed `sec_observation_replay` integration test reads the v0.25 SEC
body at its observation path. Before the shipped parser runs, the test asserts
**892,641 bytes** and SHA-256
`154556cd81bda4fc2372386bf43aa7b4414335560dd1371c45bae09f1a8d9de3`.
The same assertion rejected a disposable one-byte mutation at hash
`feb138bb57e12466321c5db5a8f2a6ab1ea51ee59c9b94d355e7eaf65c9be748`;
the temporary directory was removed and no manifest change was proposed.

Shipped `RssSource::fetch` constructed **200** documents and the test compared
every field against the asserted XML items. There are 200 distinct ids in
`sec-edgar-usgaap::<guid>` form (maximum 114 bytes), titles span 30–80
characters, bodies have the exact distribution 3:108 / 4:64 / 5:5 / 6:4 /
7:19 with mean **3.810**, all 200 raw dates are retained (191 distinct), zero
authors are populated, and all 200 URLs are present and distinct. Every
document is `finance`, `PublisherPermitted`, and `Rss`.

`Day::parse_rfc822ish` ignores the clock and zone after finding a three-token
day/month/year window. All 200 EDT values therefore record the publisher-local
day `2026-07-29`; an executed EDT-to-UTC comparison found **0** items crossing
a UTC day boundary. The committed observation record enumerates all 15
namespaced `edgar:*` local names with item and element counts, including 2,339
`xbrlFile` occurrences; none reaches a `Document` field. The declared
`windows-1252` path executed successfully because these committed bytes are
ASCII-only, not because the connector implements a general Windows-1252
decoder.

This proves shipped parser behavior against this real response only. Paging,
cursor durability, repeated fetches, on-wire politeness, redirects,
conditional requests, and the publisher's next response remain unmeasured.
The `-D warnings` workspace suite passed **136**, the focused replay passed
**1/1** with its rejection output captured, clippy and fmt passed, and golden
remained **11/11**. No publisher request, fixture change, protected-corpus
change, golden-input change, core-config change, production-source change, or
manifest change occurred.

**v0.26 Amendment 01 disposes both blockers and authorizes observation pins
(operator decision and local verification 2026-07-30).**

The Step 2 pin-first rule was an author-side rule with no satisfying assignment,
the fifth on this project's record. Executed schema 2 proved both failures:
`artifacts[]` carries an admission chain but demands SQLite-only expected facts,
while `pinned_files[]` fits ordinary files but rejects `observations/` paths and
an `admission` key. Amendment 01 replaces that precondition with a
failure-demonstrated SHA-256 and byte-length assertion at replay use. The
operator separately authorized Step 2B to add exactly the `observations/`
prefix and `observation` grade without making observations procedurally
replaceable through an admission chain.

The CADENCE retrieval remains a cycle-execution gate violation. Its content is
quarantined and no cycle measurement may cite it. Step 5 is eligible again
because every required publisher fact now names its already committed source.
The original progress record stands, including its conservative “at least one”
request wording; **retractions remain three**. No new invariant rule claims to
observe an agent's out-of-band retrieval.

The amendment also adds Step 4A so the measured store/view threshold divergence
cannot be left behind by a later “record and defer” identity decision, and adds
the missing G4 offline fixtureless-source disposition test to CADENCE. The
lifecycle checker now recognizes one uppercase step suffix, keeping `Step 2B`
and `Step 4A` contract fields and deferred references distinct. Two new focused
tests pass; the active trigger population is **2 architecture / 14 runbook**.
Full constrained Python 3.11.4 and 3.12.13 lanes each collected and passed
**286**, failed **0**, and skipped **0**. `invariant-scan` remains **12/12
rules / 39 controls**, including all R12 planted failures after its two
line-location pins were advanced with the checker edit. Golden remains
**11/11**. Amendment execution made no publisher request and changed no
publisher, schedule, core, protected artifact, database, or ref.

**v0.26 REPLAY pin gate blocked before measurement (measured 2026-07-30).**

The required pre-proposal `evidence_artifacts.py validate` and
`verify-artifacts` entries passed schema 2 with **2 artifacts**, **266 pinned
files**, and both protected databases exact. All five v0.25 observation files
were then re-hashed at **903,679 bytes** total. The feed body's SHA-256 remains
`154556cd81bda4fc2372386bf43aa7b4414335560dd1371c45bae09f1a8d9de3`;
the other four exact hashes are in the active execution record.

Two disposable manifest constructions were executed through the real
validator. An otherwise valid pinned-file object at the original
`observations/v0.25/` path failed because non-authorization pins must live
beneath `evidence/`. Adding the runbook-required `admission` object failed the
pinned-file exact-key check because schema 2 permits that chain only on the two
database artifacts. Extending the validator/schema is outside REPLAY's Gate;
copying the body beneath `evidence/` would violate the runbook's no-copy
boundary. No manifest edit was proposed, no measurement was derived from the
unchecked bytes, and REPLAY is blocked. Consequently IDENTITY-MEASURE and
IDENTITY-DECISION remain blocked; CADENCE remains independently eligible.
The mandatory permitted golden rerun passed **11/11** after a sandbox-only
loopback-bind refusal was discarded as a non-result. No publisher request was
made.

**v0.26 CADENCE stopped at a publisher-request gate violation (measured
2026-07-30).**

Codex directly opened
<https://www.sec.gov/about/developer-resources> with the web retrieval tool
while beginning CADENCE. That instruction path was wrong: although Step 5 asks
for the publisher guidance with a read date, the active runbook separately
prohibits every publisher request before Step 6. The retrieval exposed the
exact URL but not the connector's underlying wire method, redirects, or
request count; the safe statement is therefore that at least one
publisher-origin request occurred. It was not a product-runtime request and it
did not touch robots, the RSS feed, a connector, or a harvest, but those facts
do not cure the gate violation.

The returned official page said it was last reviewed or updated 2025-03-10 and
gave the fair-access ceiling as no more than 10 requests per second total. The
already committed v0.25 terms record had cited the same page on 2026-07-30, so
the direct read was unnecessary. Execution stopped immediately: no cadence
decision, schedule edit, scheduler test, or architecture disposition was made,
and the existing terms row is unchanged. CADENCE remains unchecked; Step 6 is
ineligible both here and because REPLAY is blocked. Local golden passed
**11/11** after the stop. This is an agent-side procedural failure, not an
implementation defect or live-harvest evidence.

**v0.16.0 post-push confirmation (measured 2026-07-30).**

- **Post-push verification date:** 2026-07-30
- **Post-push release:** `v0.16.0`
- **Post-push annotated tag object:** `54f8cb2f89ed53d9e0b485f6cd46924a51e41813`
- **Post-push closing commit:** `c66c2b02191e3ca3126dddc3c004b175899b414e`
- **Post-push hosted run:** `30516010035`

Atomic remote readback resolves `main` and the peeled v0.16.0 tag to closing
commit `c66c2b02191e3ca3126dddc3c004b175899b414e`; its immediate parent is
release commit `7baddb305a4357ec2dc2a35757528c1a6dc13f1e`, and the tag ref resolves
to annotated object `54f8cb2f89ed53d9e0b485f6cd46924a51e41813`. The pre-existing
`refs/heads/candidate/v0.16.0` remains untouched at
`3481e4ba85d65c927b7d0fc3a430bc04fb094394`.

Push run `30516010035` attempt **1** completed successfully at the exact
closing commit. All seven executable jobs passed: core, lint, MSRV, net, shell
Python 3.11, shell Python 3.12, and golden; report-only dependency drift was
skipped by its declared trigger.

The exact-release-parent local Python 3.11.4 and 3.12.13 summaries each
collected **284**, passed **284**, failed **0**, and skipped **0**. Both hosted
summaries collected **284**, passed **283**, failed **0**, and skipped the one
`tests/test_deferred_audit.py::test_on_site_production_measurements_match_committed_receipt`
node, marked `on_site`, for “on-site production audit requires protected
corpora and built cored”. `tools/test_population.py` verified the claimed
hosted counts and emitted this byte-identical result for both lanes:

`test-population-compare: {"collected":284,"equivalent":true,"equivalent_passed":284,"hosted":{"on_site_skipped":1,"passed":283,"skipped":[{"node_id":"tests/test_deferred_audit.py::test_on_site_production_measurements_match_committed_receipt","reason":"on-site production audit requires protected corpora and built cored"}]},"local":{"passed":284,"skipped":0},"schema_version":1}`

The hosted-zero-skip stop condition did not fire. Hosted measurements were
workspace **135**, net **55** (**29 + 26**), lifecycle **198** checked / **3**
retracted / **198** matched / **0** exemptions, `invariant-scan` **12/12
rules / 39 controls**, protected pins **266**, and golden **11/11**. Ordinary
push verification did not request attestations; candidate run **30513561141**
remains the authenticated closing evidence. The published result confirms
rather than creates the already-valid close.

This first descendant carries the protocol-required post-push fields. Per the
accepted cycle-ending audit rhythm, it is locally verified and remains
hosted-unverified until the following publication. No manifest, evidence file,
source, schema, dependency, protected database, public surface, configured
publisher, or golden-corpus fact changed.

**v0.25 R-CLOSE selects v0.16.0 and closes on authenticated candidate evidence
(operator decision and measurement 2026-07-30).** Release disposition: release
(as of 2026-07-30). Untagged release commit
`7baddb305a4357ec2dc2a35757528c1a6dc13f1e` is the immediate parent of the
closing tree.

The minor identity follows the operator's dated public-value-domain criterion,
not the standing surface-movement default. `license` is already serialized in
`/v1/signals`, `/v1/search`, `/v1/ask`, and the conditional plaintext branch
of `/v1/brief`. Adding `PublisherPermitted` expands that field's value set even
though route, field name, field type, and body shape do not move. The prior
surface rule had no answer for this case; that gap was the Step 2 finding.
`AGENTS.md` now states symmetrically that adding, removing, or redefining a
public serialized value requires a minor release because exhaustive consumer
handling is part of the contract. No invariant rule was added: this is prose
adjudicated at R-CLOSE, and counts remain **12 rules / 39 controls**.

No corrective trigger was visible at entry: published v0.15.8 is green and its
records are true. The publication trigger is the operator's explicit decision
to ship the authenticated product change—the missing publisher-permission
rights ground and the reviewed SEC source that uses it. Authenticated candidate
`779fbe55ba33dd5d196df391cc9a9eeb3ce0bbb3` and run **30513561141** attempt
**1** are the closing evidence, deliberately separate from the untagged release
parent `7baddb305a4357ec2dc2a35757528c1a6dc13f1e`. The exact release parent
passed `./run ci-local` all **20** jobs: workspace **135**, net **55** (**29 +
26**), warning-denied current and locked Rust 1.78 lanes, clean
clippy/fmt/ShellCheck, Python 3.11 collected/passed **284/284** with no skip,
embedded golden **11/11**, protected pins **266/266**, both databases, and
persisted fingerprints. Independent Python 3.12 collected/passed **284/284**
with no skip; `tools/test_population.py` derived `collected=284`,
`equivalent=true`, and `equivalent_passed=284` across the local interpreters.
Standalone golden passed **11/11**. Root `export-check` passed **96** derived
sources, **7** required, and **170** exported. Release-posture
`./run audit-deferred --rederive
evidence/v0.25/deferred-audit/report.json` required attestations and reproduced
all **7** rows. The tag object and closing-commit identity remain unknowable
until their protocol-defined points and are not predicted in this tree.

The three product determinations are affirmative and bounded:

- **Licence.** `PublisherPermitted` claims only that the publisher expressly
  permits reuse under its own stated terms; it makes no claim that
  issuer-authored filings are government works or public domain. The spelling
  is exact across config, archive, and `/v1/*`; redistribution is true.
- **Terms.** SEC's Privacy Information page says it does not allow
  “unclassified” automated tools, while its Webmaster FAQ directs
  programmatic downloaders to declare an organization-and-contact User-Agent.
  On 2026-07-30 the operator affirmed that the structurally required contact is
  monitored. Terms remain a dated publisher-specific operator responsibility
  outside the executable robots-plus-deny-list model.
- **Feed shape.** After a fresh allowed robots decision, the one authorized
  RSS request returned HTTP 200 with **200** items. `title`, `guid`, `pubDate`,
  `link`, and `description` were non-empty in **200/200**; optional `author`
  was present in **0/200**. E0 found zero mandatory per-item fields. The
  repository parser was deliberately not executed against the body, so the
  record does not claim parser success.

Admission configured the reviewed path under `finance` with
`PublisherPermitted` and `robots_on_missing: "deny"` but performed no live
harvest. It did not exercise the production origin-keyed robots cache or
per-host limiter with both origins in one runtime, live RSS ingestion, paging,
repeated-fetch behavior, near-duplicate behavior, or cursor durability. Two
publisher origins are configured and only `arxiv-cs` has ever been fetched.
The first live SEC RSS harvest remains deferred to a separately authorized and
scoped v0.26 runbook.

E0's G5 author-side implication was corrected on 2026-07-30 as a runbook error,
not an implementation defect. Golden reads `config/core.json` but explicitly
selects only `science` and `technology`; the new source is confined to
`finance`. The definition of done therefore stayed **11/11**, and admission
produced delta **0**.

The exact
`v0.15.8..7baddb305a4357ec2dc2a35757528c1a6dc13f1e`
release-parent changed-path set contains **38** paths, each classified exactly
once in seven disjoint groups:

- **Operating contract, architecture, release notes, and status:** `AGENTS.md`,
  `ARCHITECTURE.md`, `CHANGELOG.md`, `README.md`, and `STATE.md`.
- **Release version authorities:** `Cargo.lock`, `apps/cored/Cargo.toml`,
  `shell/intel_shell/__init__.py`, and `shell/intel_shell/app.py`.
- **Product configuration, licence implementation, and focused controls:**
  `config/core.json`, `crates/core/src/lib.rs`,
  `crates/store/tests/license_compat.rs`,
  `shell/tests/test_core_config_admission.py`, and
  `shell/tests/test_cycle_check.py`.
- **Cycle and forward-publication records:**
  `docs/cycles/PROGRESS-v0.24.md`, `docs/cycles/PROGRESS-v0.25.md`, and
  `docs/cycles/TASKS-v0.25-EXECUTION.md`.
- **Append-only provenance authority:** `config/protected-artifacts.json`.
- **Publisher determinations and wire observations:** all five files under
  `observations/v0.25/`.
- **Authenticated evidence:** all fourteen files under
  `evidence/ci-runs/30513561141-1/` and
  `evidence/v0.25/deferred-audit/report.json`.

The `crates/core/src/lib.rs` permission was used for the new enum value and its
exhaustive redistribution decision. The conditional permission to edit
`crates/store/src/sqlite.rs` was unused: the existing unconstrained text column
and `as_str`/`parse` boundary already persist the value. The new store
integration control records the older-reader fallback without changing
production storage code. The only `shell/intel_shell/app.py` change at
R-CLOSE is the mechanical public version literal; the recorded relocation
option remains unused. Cargo changes only the local `cored` version in
`Cargo.lock`; dependency resolution is unchanged.

The protected manifest remains below its accepted bounds: **266** pins,
**154,205 bytes**, and two consecutive complete verifications at **0.14 s /
0.09 s real**. A4, editable L1, the R3/R4 open-bottom limitations, the
active-runbook measured-value heuristic, T7, robots negative-cache Decision B,
scheduled L2, and live multi-publisher behavior all remain open. A second
configured source is not T7's second-concurrent-harvester trigger, and no
transient robots outage fired Decision B.

**v0.25 RE-MEASURE admits authenticated release-posture evidence without
publishing (hosted and local measurement 2026-07-30).**

The operator authorized the Step 6 narrow remote mutation. Exact candidate
`779fbe55ba33dd5d196df391cc9a9eeb3ce0bbb3` was pushed to the neutral ref
`refs/heads/codex/v0.25-evidence-779fbe5`; the name encodes neither the selected
version nor a patch assumption. Before dispatch, the remote
`.github/workflows/ci.yml` blob was
`48ea726b798f1049e0b29cce1f0c64588861c2dd`, byte-identical to the local
candidate blob. Authenticated hosted run
<https://github.com/jiayanzeng/intel-platform/actions/runs/30513561141>,
attempt **1**, completed successfully with all seven executable jobs green.

The hosted log reports workspace **135** and net **55**
(`intel-ingest` **29** + `cored` **26**), locked Rust 1.78, clean
rustc/clippy/fmt/ShellCheck gates, lifecycle **196 checked / 3 retracted / 196
matched / 0 exemptions**, `invariant-scan` **12/12 rules / 39 controls** with
R10 **45** exemptions, and golden **11/11**. Both exact
`tools/test_population.py` comparisons returned
`collected=284`, `equivalent=true`, and `equivalent_passed=284`: each local
lane passed **284 / skipped 0**, while its hosted lane passed **283** plus the
single named `on_site` skip
`tests/test_deferred_audit.py::test_on_site_production_measurements_match_committed_receipt`
with reason “on-site production audit requires protected corpora and built
cored”. The run's workflow commands contained no harvest, and a case-insensitive
search of the complete hosted log for `sec.gov`, `usgaap.rss`,
`harvest-arxiv`, `POST /ingest`, or an HTTP GET returned no matches. No hosted
job made a publisher request.

The seven authenticated receipt JSON files and their seven persisted Sigstore
bundles are under `evidence/ci-runs/30513561141-1/`. Release-posture
`./run audit-deferred` measured a clean detached copy of the exact candidate,
required attestations, accepted **7 / rejected 0** identities, confirmed the
single-run matrix complete, and recorded **5 deferred / 2 promoted / 0
implemented deferred subsystems**. The largest measured archive remains
**2,600 documents**; exact-cosine p95 was **8.640 ms**, below the **16.264 ms**
A3 request anchor. The **34,881-byte** report is
`evidence/v0.25/deferred-audit/report.json`, SHA-256
`9d7c367060d2c9f28aaf17586f7e54ab782f6f8113b64326d730cccb05cfb342`.
`./run audit-deferred --rederive` reproduced it with attestations required.

Those fourteen signed hosted files plus the report add fifteen records to the
schema-v2 protected manifest, taking it from **251** to **266** pins.
`python3 tools/evidence_artifacts.py validate`, `./run verify-artifacts`, and
`./run evidence-report` passed; both protected databases remained exact.
Standalone `./run golden` passed **11/11**, delta **0**, and
`invariant-scan` again passed **12/12 rules / 39 controls**.

Read-only post-dispatch resolution found remote `main` unchanged at
`64002678672a601804e5f67886c73fffb4d212c8`, the historical
`refs/heads/candidate/v0.16.0` unchanged at
`3481e4ba85d65c927b7d0fc3a430bc04fb094394`, and the neutral Step 6 branch
still at the exact candidate. No `v0.16.0` tag exists. Step 6 created no tag,
advanced no release ref, and changed no source, public surface, dependency,
lockfile, schema, or protected database. Step 7 remains behind its separate
operator publication decision.

The declared-scope diff sub-rule first became applicable after the changed
Step 6 commit and rejected the evidence directory, exact report, and protected
manifest because the runbook table omitted them even though the Step 6 gate
and steps explicitly require all three. The dated runbook correction adds only
the exact run `30513561141` directory, exact v0.25 report path, and manifest
path. The corrected `cycle-check` passes; no task authority was broadened.

**v0.25 ADMIT configures the reviewed SEC source without claiming a harvest
(operator decision and measurement 2026-07-30).**

The operator approved admission of `sec-edgar-usgaap` in the `finance` sector
at `https://www.sec.gov/Archives/edgar/usgaap.rss.xml`, classified
`PublisherPermitted`. The binding review conditions are unchanged: use that
exact path; preserve the monitored-contact crawler identity; re-evaluate and
obey the publisher's current `robots.txt` plus the operator deny-list before
requests; and keep total automated traffic at or below the SEC's then-current
published ceiling. `robots_on_missing` is explicitly `"deny"` because SEC
serves a policy today: absence is not the reviewed condition and must fail
closed rather than borrowing arXiv's publisher-specific 404 exception.

The admission test reads the release configuration and pins the source's exact
sector, id, type, URL, licence, conservative missing-policy value, and global id
uniqueness. Its fail-before execution found no matching source and failed; after
the config change it passed. The first complete rebuilt shell lanes exposed one
runbook-control count that correctly rose with the required new deferral row:
both initially collected **284**, passed **283**, and failed the exact
trigger-freshness population assertion. The Step 5 gate was corrected to name
that already-declared test path, its expected governed runbook-row count moved
from 11 to 12, and focused controls passed **2/2**. Clean Python 3.11 and 3.12
lanes then each passed **284/284** with zero skips and the same one accepted
third-party warning. `tools/test_population.py` derived
`collected=284`, `equivalent=true`, and `equivalent_passed=284`; its second
input was the local Python 3.12 lane, not a hosted run.

Admission performed no live harvest and made no publisher request. It proves
only that two reviewed publisher origins are now represented in configuration
and that the exact new source declaration is controlled. Only `arxiv-cs` has
ever been harvested. The origin-keyed robots cache and per-host limiter have
never handled the two origins in one production runtime, and live RSS fetching,
repository parsing of the observed SEC body, paging, repeated-fetch behavior,
near-duplicate behavior, and cursor durability remain unmeasured. The first
live RSS harvest is explicitly deferred to an operator-authorized v0.26
runbook with its own declared scope.

The mandatory standalone `./run golden` passed **11/11**, delta **0**, matching
E0's finding that its science-and-technology selection excludes this finance
source. `python3 tools/evidence_artifacts.py validate` passed; `./run
verify-artifacts` found all **251** pins and both protected databases exact.
The complete `./run ci-local` then passed all **20** jobs at the admitted
configuration, including 135 workspace tests, 55 net tests, the locked Rust
1.78 lanes, clean warning/lint/format gates, 284 shell tests, and embedded
golden **11/11**. No protected corpus, pin, database, schema, dependency,
lockfile, ingest source, compliance source, shell production source, public
response, tag, or branch moved. Counts remain **12 invariant rules / 39
controls**.

**v0.25 FEED-SHAPE observes 200 SEC items in one authorized request without
claiming parser execution (wire and offline measurement 2026-07-30).**

Preflight passed `python3 tools/evidence_artifacts.py validate` and
`./run verify-artifacts`; all **251** protected pins and both protected
databases matched, port 8788 was free, and the destination observation files
did not exist. The ignored `.env` supplied the monitored contact without
printing it. A disposable out-of-tree observer compiled offline before any
wire action and refused existing output paths, policy change, or either robots
denial before constructing the feed client.

At **2026-07-30T03:33:58Z**, exactly one shipped
`HttpRobotsFetcher` request fetched `https://www.sec.gov/robots.txt`.
`RobotsCache` and the recording wrapper each counted **1** fetch.
The body is **2,622 bytes** with SHA-256
`72d6196b3f20737396e566ddeb769fb4174b44f334985a1267a59ae0f08c2f2f`,
byte-identical to the v0.24 policy. The shipped matcher returned
`Body(allow)` for `/Archives/edgar/usgaap.rss.xml`; the operator deny-list also
allowed it, the effective interval was **0.500 seconds**, and redirects were
disabled.

Only after those checks, at **2026-07-30T03:34:00Z**, the same
contact-bearing `intel-platform/0.15.8` identity made exactly one
redirect-disabled, no-retry GET of
`https://www.sec.gov/Archives/edgar/usgaap.rss.xml`. It returned HTTP **200**,
`Content-Type: text/xml`, no `Location` header, and **892,641 bytes** with
SHA-256
`154556cd81bda4fc2372386bf43aa7b4414335560dd1371c45bae09f1a8d9de3`.
No other publisher URL was requested by Step 4.

Independent offline XPath counts found **200** `<item>` elements.
`title`, `guid`, `pubDate`, `link`, and `description` are present and non-empty
in **200/200**; optional `author` is present in **0/200**. E0 proved that all six
fields are optional, so the mandatory-field list is empty and the Step 4 shape
condition is satisfied. The repository parser was deliberately not invoked
against the body. Derived only from E0's source enumeration: if it accepts the
XML, it sees 200 candidate items, uses the five present-value branches, retains
each raw `pubDate` while conditionally deriving its day, and emits an empty
author vector for every item. This is not a claim that the repository parser
succeeded.

The wire body, fresh robots body, and report live only in
`observations/v0.25/feed-shape/`. They are not fixtures, protected-corpus
admissions, configured-source inputs, or golden inputs. One request establishes
nothing about paging, resumption-token equivalents, cursor durability,
near-duplicate behavior, repeated-fetch politeness, conditional requests, or a
live ingest. No code, config, schema, protected artifact, database, public
surface, or ref changed. Mandatory standalone golden passed **11/11**, delta
**0**. Step 5 is now eligible but remains behind its separate operator
admission decision.

**v0.25 TERMS-GATE is affirmative for the reviewed SEC path and leaves terms
as a dated operator responsibility (operator decision and measurement
2026-07-30).**

The measured publisher gates remain distinct. The shipped matcher returned
**allow** for `/Archives/edgar/usgaap.rss.xml` against the captured SEC
`robots.txt`. The SEC Privacy Information page, read on 2026-07-30 at
<https://www.sec.gov/about/privacy-information>, states that the SEC does not
allow “unclassified” bots or automated tools to crawl the site. The Webmaster
FAQ, read on the same date at
<https://www.sec.gov/about/webmaster-frequently-asked-questions>, directs
programmatic EDGAR downloaders to declare their User-Agent and supplies an
organization-and-administrative-contact example. The publisher supplies no
separate glossary or registration transaction defining “unclassified”; the
organization-and-contact declaration is the operational procedure the
publisher actually publishes.

The operator accepted the recommended affirmative determination on 2026-07-30,
including its premise that the configured contact is monitored. The
version-independent property is: **a monitored contact is present in the
crawler identity**. Source construction guarantees before bind that a
net-enabled process has a trimmed, non-empty, non-placeholder contact and
derives its version from the package authority. Monitoring is not
source-observable; it is the operator fact confirmed here. E0 therefore found
no structural contact defect to fix or assign forward.

`ARCHITECTURE.md` now records the dated disposition that publisher terms remain
a publisher-specific operator responsibility outside the executable model.
The SEC condition is natural-language policy with no stable machine-readable
classification or registration state; encoding a third boolean gate would
claim an automation the evidence cannot support. The runtime continues to
enforce publisher `robots.txt` plus the operator deny-list, while a dated
operator review decides the separate terms question before admission.

This result binds one publisher, the reviewed path, the cited texts, and
2026-07-30. It is not a general finding about government or regulatory sources,
does not establish another publisher's compliance, and says nothing about the
feed's shape. The dated observation is
`observations/v0.25/terms-gate/sec-edgar-terms-determination.md`. Step 3 made
**zero publisher requests**, no code change, and no source/config/schema/ref
change. Its first sandboxed golden attempt exited before startup because the
loopback bind was denied with `Operation not permitted`; the permitted rerun of
the same `./run golden` entry point passed **11/11**, delta **0**. Step 4 remains
behind its separate authorization for exactly one live feed GET.

**v0.25 LICENSE-SEMANTICS adds the missing rights ground and selects v0.16.0
(operator decision and measurement 2026-07-30).**

The operator chose `extend/minor`. `PublisherPermitted` means that the publisher
expressly permits reuse under its own stated terms; it asserts nothing about
underlying copyright. `PublicDomain` remains excluded because the SEC evidence
does not establish that issuer-authored filings are government works. `CcBy`
would invent a Creative Commons grant, `ClientOwned` would falsely assert
subscriber ownership, and `IndexOnly` would assert the opposite operational
restriction from the publisher's measured reuse permission.

`PublisherPermitted` serializes and persists as exactly
`"PublisherPermitted"`. `redistributable()` is now an exhaustive match:
`PublicDomain`, `CcBy`, `ClientOwned`, and `PublisherPermitted` are true, while
`IndexOnly` is false. The compiler will therefore require an explicit decision
when a later enum variant is added. The focused core control exercised every
variant's spelling, parse result, redistribution result, and `/attest` outcome;
only `IndexOnly` produced a refusal and violation.

SQLite required no production edit and no schema change. The existing
`license TEXT NOT NULL` column has no `CHECK`; writes already use `as_str()`,
and both document hydration and search already use `License::parse`. A new
integration control wrote and reopened `PublisherPermitted`, observed the exact
stored text, and returned a redistributable search snippet. It then planted
`FutureLicense` directly in the temporary archive; the unchanged older-reader
fallback reclassified it as `IndexOnly` and suppressed the snippet. The
conditional permission to edit `crates/store/src/sqlite.rs` was therefore
unused.

Unknown values are intentionally asymmetric and both directions were executed.
At the config boundary, a temporary configuration using
`PublisherPermitted` started the actual offline `cored` entry point; replacing
it with `FutureLicense` exited **101** with a hard Serde error naming the five
accepted variants. At the stored-row boundary, the integration control above
showed the silent `License::parse(...).unwrap_or(License::IndexOnly)` fallback.
Both fail safely, but an older binary reading a newer archive can silently
reclassify publisher-permitted documents as `IndexOnly`; this compatibility
behavior is now explicit rather than inferred.

The operator's exact dated public-value-domain criterion is in `AGENTS.md`, and
`ARCHITECTURE.md §8` now reconciles the same rule: adding, removing, or
redefining any value of a field already serialized in a `/v1/*` response
requires a minor release even when route, field name, field type, and body shape
do not move. Patch is available only when every public field's value set is
unchanged. The criterion is prose adjudicated at R-CLOSE. No invariant rule was
added because no registered rule can observe that release-classification
judgment; counts remain exactly **12 rules / 39 controls** in the runbook,
progress record, and this state record.

Minor classification selects **v0.16.0** even if later terms or feed-shape
determinations defer source admission. In that outcome, closure will state that
the value exists, zero configured sources produce it, and no `/v1/*` response
can carry it as of the closing date. `README.md`'s four-value config-schema
block is now known stale and is deliberately assigned to Step 7 step 10, whose
gate contains that release authority.

Live remote inspection measured the pre-existing
`refs/heads/candidate/v0.16.0` at
`3481e4ba85d65c927b7d0fc3a430bc04fb094394` and found no `v0.16.0` tag. That
branch predates this release identity and belongs to the v0.15.1 evidence run.
Seven immutable Sigstore-bundle provenance entries and the pinned v0.15.1
deferred-audit report preserve that source ref across eight evidence subjects.
The ref was not renamed, deleted, or moved. Step 7 must explicitly disambiguate
it from this release.

The author-side G5 implication was also corrected as a runbook error, not an
implementation defect: golden reads `config/core.json` but explicitly selects
only `science` and `technology`, so a future `finance` source cannot enter that
corpus. The complete matrix passed **20/20** with workspace **135**, net **55**,
both warning-denied Rust lanes, clean clippy/fmt/ShellCheck, shell Python 3.11
**283 / 283 / 0 skipped**, `invariant-scan` **12/12 / 39 controls**, all
**251** pins, and embedded golden **11/11**. Independent Python 3.12 passed
**283 / 283 / 0 skipped**, and mandatory standalone golden passed **11/11**,
delta **0**. No configured source, publisher request, feed request, dependency,
lockfile, protected database, protected pin, schema, shell source, or ref
changed.

**v0.24 R-CLOSE selects v0.15.8 and closes on authenticated candidate evidence
(operator decision and measurement 2026-07-30).** Release disposition: release
(as of 2026-07-30). Untagged release commit
`696c0863ea684d590970902bcbbd13a7a3ccb610` is the immediate parent of the
closing tree. The
patch identity applies because the cycle changes test-comparison apparatus,
documentation, evidence, and lifecycle records without adding, removing,
renaming, or incompatibly reshaping any `/v1/*` route or response body, schema,
dependency, configured source, robots-policy behavior, runtime behavior, or
protected database.

The publication trigger is the false hosted shell count in the published
v0.15.7 tree. Its correction is present only in unpublished descendants of the
tagged closing commit. Publishing v0.15.8 makes the correction and the
executable population comparator visible together; the release identity is not
an inherited patch default.

Authenticated run `30472740314` attempt **1** at exact candidate
`a73c042068a367aea22e63e28dfd2f754b65ef9c` is the closing evidence. The
candidate is deliberately separate from release parent
`696c0863ea684d590970902bcbbd13a7a3ccb610`.
All seven executable hosted jobs passed, and the release-grade verifier
accepted **7 / rejected 0** signed identities with attestations required.
For both Python lanes, the exact comparator output already recorded under
RE-MEASURE derives equivalent populations from local collected **283**, passed
**283**, skipped **0** and hosted collected **283**, passed **282**, plus the
one named `on_site` skip. The release-parent definition of done, exact release
commit, and closing evidence are measured. The closing commit, annotated tag
object, and post-push run are recorded only at their protocol-defined forward
points rather than predicted in this tree.

The false-measurement class is **isolated** under HISTORY-BOUND's measured
criterion: exactly one hosted RE-MEASURE event was false, represented once in
the v0.23 progress entry and copied into its closed execution record. The
v0.23 POST-PUSH entry and this cycle correct that measurement forward without
rewriting either historical record.

The author-side population contains **5** members under v0.23's criterion of
one distinct normative runbook requirement with no outcome satisfying both the
requirement and its governed action. The measured members are v0.19 mutable-main
freshness, v0.20 post-push-before-close ordering, v0.22's closing field set,
v0.22's source prohibition, and the bare local/hosted equality requirement
first authored in v0.21. This fifth member is the first whose consequence was a
false number in a published record; the earlier four produced unmeetable
criteria without that published measurement consequence.

PUBLISHER-REVIEW completed with a conditional recommendation rather than an
admission. The shipped matcher fetched SEC's **2,622-byte** policy, SHA-256
`72d6196b3f20737396e566ddeb769fb4174b44f334985a1267a59ae0f08c2f2f`,
and allowed `/Archives/edgar/usgaap.rss.xml` under the wildcard group; the
separate latest-filings Atom path matched `Disallow: /cgi-bin`. Admission
requires a separate v0.25 operator decision and preservation of the reviewed
RSS path, monitored-contact crawler identity, and then-current publisher rate
ceiling. No feed was fetched and no source was configured, so live RSS
fetching, parsing, cursor durability, multi-origin robots-cache behavior, and
multi-host limiter behavior remain unestablished.

The exact `v0.15.7..696c0863ea684d590970902bcbbd13a7a3ccb610`
release-parent changed-path set contains **38** paths, each classified exactly
once in seven disjoint groups:

- **Operating contract, architecture, release notes, and status:** `AGENTS.md`,
  `ARCHITECTURE.md`, `CHANGELOG.md`, `README.md`, and `STATE.md`.
- **Release version authorities:** `Cargo.lock`, `apps/cored/Cargo.toml`,
  `shell/intel_shell/__init__.py`, and `shell/intel_shell/app.py`.
- **Lifecycle controls and tests:** `config/invariant-rules.json`, `run`,
  `tools/invariant_scan.py`, `tools/test_population.py`, `shell/pytest.ini`,
  `shell/tests/conftest.py`, `shell/tests/test_deferred_audit.py`, and
  `shell/tests/test_test_population.py`.
- **Cycle records:** `docs/cycles/PROGRESS-v0.23.md`,
  `docs/cycles/PROGRESS-v0.24.md`, and
  `docs/cycles/TASKS-v0.24-EXECUTION.md`.
- **Append-only provenance authority:** `config/protected-artifacts.json`.
- **Publisher-review observations:** both files under
  `observations/v0.24/publisher-review/`.
- **Authenticated evidence:** all fourteen files under
  `evidence/ci-runs/30472740314-1/` and
  `evidence/v0.24/deferred-audit/report.json`.

The exact release parent passed the complete definition of done:
`./run ci-local` passed all **20** jobs with **133** workspace tests, **55**
net tests (**29** `intel-ingest` + **26** `cored`), warning-denied current and
locked Rust 1.78 builds, clean clippy/fmt/ShellCheck gates, both Python 3.11
and independently rebuilt Python 3.12 populations collected **283**, passed
**283**, failed **0**, and skipped **0**, `invariant-scan` **12/12 rules / 39
controls** with R12 control **16** and R10 **45** exemptions, and embedded
golden **11/11**. The separately invoked mandatory golden also passed all
**11** checks. Root `export-check` passed **94** derived sources, **7**
required, and **161** exported. Release-posture deferred-evidence
re-derivation required attestations and accepted all **7** rows. All **251**
protected pins and both protected databases remained exact.

The product boundary remains unchanged: `arxiv-cs` is the sole configured real
publisher and the other three sources remain fixtures. The SEC review is a
document, not an admission. A4, editable L1, the R3/R4 open-bottom limits, the
active-runbook measured-value heuristic, T7 robots single-flight, robots
negative-cache Decision B, scheduled L2, and the FastAPI version-literal
relocation remain open. The A/A/E disposition and hosted
`--skip-local-tag-verification` trigger remain unchanged.

**v0.15.8 post-push confirmation (measured 2026-07-30).**

- **Post-push verification date:** 2026-07-30
- **Post-push release:** `v0.15.8`
- **Post-push annotated tag object:** `dc5abe0690e77cef671896102382427721d97321`
- **Post-push closing commit:** `64002678672a601804e5f67886c73fffb4d212c8`
- **Post-push hosted run:** `30475988050`

Atomic remote readback resolves `main` and the peeled v0.15.8 tag to closing
commit `64002678672a601804e5f67886c73fffb4d212c8`; its first parent is release
commit `696c0863ea684d590970902bcbbd13a7a3ccb610`, and the tag ref resolves to
annotated object `dc5abe0690e77cef671896102382427721d97321`.
Push run `30475988050` attempt **1** completed successfully at that exact
closing commit. All seven executable jobs passed: core, lint, MSRV, net, shell
Python 3.11, shell Python 3.12, and golden; report-only dependency drift was
skipped by its declared trigger.

Fresh local Python 3.11.4 and 3.12.13 summaries each collected **283**, passed
**283**, failed **0**, and skipped **0**. Both hosted summaries collected
**283**, passed **282**, failed **0**, and skipped the one
`tests/test_deferred_audit.py::test_on_site_production_measurements_match_committed_receipt`
node, marked `on_site` and `skipif`, for
`on-site production audit requires protected corpora and built cored`.
`tools/test_population.py` verified the claimed hosted counts and emitted this
byte-identical result for both lanes:

`test-population-compare: {"collected":283,"equivalent":true,"equivalent_passed":283,"hosted":{"on_site_skipped":1,"passed":282,"skipped":[{"node_id":"tests/test_deferred_audit.py::test_on_site_production_measurements_match_committed_receipt","reason":"on-site production audit requires protected corpora and built cored"}]},"local":{"passed":283,"skipped":0},"schema_version":1}`

The hosted-zero-skip stop condition did not fire. Hosted measurements were
workspace **133**, net **55** (**29 + 26**), lifecycle **191** checked / **3**
retracted / **191** matched / **0** exemptions, `invariant-scan` **12/12
rules / 39 controls** with all **16** R12 planted failures detected, protected
pins **251**, and golden **11/11**. Ordinary push verification did not request
attestations; candidate run `30472740314` remains the authenticated closing
evidence. The published result confirms rather than creates the already-valid
close.

This first descendant carries the protocol-required post-push fields. Per the
accepted cycle-ending audit rhythm, it is locally verified and remains
hosted-unverified until the following publication. No manifest, evidence file,
source, schema, dependency, protected database, public surface, or configured
publisher changed.

**v0.24 POPULATION-EXPLICIT names and reports the environment-conditional
test population (measured 2026-07-29).**

The sole conditional test,
`tests/test_deferred_audit.py::test_on_site_production_measurements_match_committed_receipt`,
now carries the registered `on_site` marker immediately alongside its unchanged
`skipif`. `pytest shell/tests --collect-only -m on_site -q` enumerated exactly
that one node. The full-suite plugin emits a stable, sorted JSON object containing
`schema_version`, `collected`, `passed`, `failed`, the complete `on_site` node
set, and each skip's node id, marker set, and reason.

Repository-local Python 3.11.4 and 3.12.13 each collected **275**, passed
**275**, failed **0**, and skipped **0**. A disposable clean checkout without
the protected databases or built `cored` produced the same format in both
lanes: collected **275**, passed **274**, failed **0**, and skipped **1**. The
skip was the exact node above, carried markers `on_site` and `skipif`, and named
the reason `on-site production audit requires protected corpora and built
cored`. The selected test populations and outcomes are unchanged from E0; this
task only makes the distinction explicit and machine-readable.

An initial construction that added an explicit pytest CLI option to `run` and
the workflow was rejected by the authorization pin and R10's hosted-command
classification. The accepted construction instead places the shared option in
`shell/pytest.ini`, leaving both invocations as
`pytest shell/tests -q`. `run` changed only by one explanatory comment, from
SHA-256 `0fc7f0be0ea2d8c68ff63be55dd0b73cc1385ce966b8307506a5387543f18779`
at **43,044 bytes** to
`44314ddfc182de68d4aaa444f2c6bd074fe08858d8d46f98aafa461dd6672397`
at **43,125 bytes**. Its commands, dispatch, model-profile functions, and
authorization boundary are unchanged; `tools/model_profiles.py` and
`.github/workflows/ci.yml` are byte-unchanged.

The complete current `./run ci-local` passed all **20** jobs: workspace
**133**, net **55** (**29 + 26**), both warning-denied Rust lanes, clean
clippy/fmt/ShellCheck, `invariant-scan` **12 rules / 38 controls**, all **236**
pins, protected databases **2**, and embedded golden **11 checks**. Standalone
golden passed all **11** checks with delta **0**. No runtime source, crate,
dependency, schema, protected database, configured source, or public surface
changed.

**v0.24 POPULATION-COMPARE derives equivalent populations and rejects
unclassified differences (measured 2026-07-29).**

`tools/test_population.py` reads either the JSON summary itself or exactly one
summary embedded in a pytest log. It validates the schema and accounting, then
requires equal collected populations, zero failures, and local passed equal to
hosted passed plus hosted `on_site` skips. Every skip must name its node id and
non-empty reason, carry the `on_site` marker, and belong to the declared
`on_site` population. Its output is stable sorted JSON, including the raw local
and hosted passed values, the named hosted skip set, and the derived equivalent
passed population.

All three fail-before constructions were executed and rejected: an unmarked
hosted skip with `is not marked on_site`, a collected difference with
`collected mismatch`, and an empty reason with `reason must be present`. The
v0.23 replay produced comparator output with collected **275**, equivalent
passed **275**, local passed **275**, hosted passed **274**, and hosted
`on_site` skips **1**, naming the conditional node and protected-input reason.
Claim verification rejected passed **275** / skipped **0** because the
comparator derived passed **274** / skipped **1**, then accepted the latter.

`AGENTS.md` now requires every local/hosted shell comparison in RE-MEASURE to
use these summaries and this comparator, and forbids numbers transcribed from a
log. R12 exercises the real parser and comparator with an unmarked-skip
construction. Its registered mutation removes that rejection; self-test then
detects `test-population planted controls were not detected: unmarked-skip` at
the comparator's control site. The invariant result is **12 rules / 39
controls**, with R12 **16** controls.

The focused comparator and invariant tests passed **30** tests. Full local
Python 3.11.4 and 3.12.13 each collected **283**, passed **283**, failed **0**,
and skipped **0**, retaining the one accepted
`StarletteDeprecationWarning`. `./run ci-local` passed all **20** jobs with
workspace **133**, net **55** (**29 + 26**), clean warning-denied Rust,
clippy/fmt/ShellCheck, all **236** pins, protected databases **2**, and embedded
golden **11 checks**. No runtime source, crate, dependency, schema, protected
database, configured source, public surface, or ref changed.

**v0.24 HISTORY-BOUND corrects one isolated measurement record forward
(measured and operator-decided 2026-07-30).**

This is the dated superseding entry for the exact affected measurement event.
The `2026-07-29 · RE-MEASURE` entry in
`docs/cycles/PROGRESS-v0.23.md`, with the same figure copied into v0.23's closed
execution record, claimed each hosted shell lane passed **275** tests with no
skip and equalled local. Hosted run `30459746825` attempt **1** instead
collected **275**, passed **274**, and skipped **1**, retaining one accepted
warning in each lane. The skipped node was
`test_on_site_production_measurements_match_committed_receipt`, for the declared
protected-corpora-and-built-`cored` reason. The v0.23 POST-PUSH append for run
`30462710258` first recorded that correction; this entry confirms its exact
scope without rewriting either historical location.

The affected class is **isolated**: measurement found exactly **one** false
RE-MEASURE record, represented by its append-only progress entry and the same
copied statement in the closed runbook. The operator applied E0's existing
criterion on 2026-07-30: checklist retractions govern a resolved checked task's
later-falsified accepted product, invariant, or task property, while an
incorrect figure inside an append-only audit record uses a dated superseding
entry when the underlying executed result remains valid. The operator selected
the latter classification, so `config/checklist-retractions.json` remains
byte-identical and the retraction count remains **3**.

The defect is specifically the recorded hosted measurement. It changed no
published runtime, signed identity, protected pin, protected database, green
job conclusion, release graph, or public surface. Readback still finds the
annotated tag object peeling to closing commit
`e7715fb97b86b91a2a58bc7b73bf99308c2aae9b`, whose first parent is release
commit `8bb6a71446b043b10ce16077499fdc07abb91b98`, and all **236** pins plus both
protected databases remain exact.

The fifth-instance count is measured against v0.23's criterion: one distinct
normative runbook requirement for which no sequence or outcome can satisfy
both the requirement and its governed task or release action. v0.23 enumerated
**4** prior members: v0.19 mutable-main freshness, v0.20
post-push-before-close ordering, v0.22's release-commit/tag-object field set,
and v0.22's no-`crates/`/`apps/` prohibition. The bare hosted/local equality
criterion first authored into v0.21 Step 6 by dropping v0.19's declared
on-site-skip clause is one distinct additional member: the clean hosted
checkout must skip the protected-input test while the on-site local checkout
runs it. The measured author-side population is therefore **5**. This fifth
member is the first in that population whose consequence was a false number in
a published record rather than only an unmeetable criterion.

The preserved historical blobs are
`94745d813072ded5f04ad4193d91c23c040b5232` for the v0.23 closed runbook and
`bea2851a059dcd5f73c501f657b3c0a844fb5296` for its progress log. The unchanged
retraction registry blob is
`9e13d2d89276eaf9279ec66bc4955313b117557d`.

**v0.24 PUBLISHER-REVIEW conditionally admits a review, not a source
(measured and operator-authorized 2026-07-30).**

The operator selected SEC EDGAR filings feeds for the `finance` sector after
measuring `config/core.json`: its three RSS sources all carry fixtures, its
`technology` and `finance` publishers are `example.org`, and its configured
`CcBy` and `PublicDomain` branches have no real-content observation. v0.18
`arxiv-cs` remains the sole live-publisher corpus and is `IndexOnly`; its
`robots.txt` result was 404 and supplied no real policy group. The reviewed SEC
endpoint is the official US GAAP structured-disclosure RSS feed,
`https://www.sec.gov/Archives/edgar/usgaap.rss.xml`.

At **2026-07-29T16:41Z**, a robots-only preview ran the shipped
`HttpRobotsFetcher`, installed crawler identity, `RobotsCache`, and
`RobotsGate`. Its one final request was
`GET https://www.sec.gov/robots.txt`, with no redirect and no feed or document
request. The served policy is **2,622 UTF-8 bytes**, SHA-256
`72d6196b3f20737396e566ddeb769fb4174b44f334985a1267a59ae0f08c2f2f`,
preserved under `observations/v0.24/publisher-review/`. `User-agent: *`
applied; no rule matched `/Archives/edgar/usgaap.rss.xml`, no `Allow`
exception was used, no `Crawl-delay` existed, and the matcher returned
**allow**. An earlier robots-only pass in the same review excluded
`/cgi-bin/browse-edgar?action=getcurrent&output=atom`: it matched
`Disallow: /cgi-bin` and returned **deny**. The two processes requested only
`/robots.txt`; no feed was fetched.

The actual identity was
`intel-platform/0.15.7 (research prototype; contact: [operator contact
redacted])`, with a monitored contact present. This contradicts the prior
expectation that the versioned identity carried no contact; current production
construction requires one. The report cites the publisher's exact reuse and
automated-access statements by SEC URL and 2026-07-30 read date. In particular,
the SEC expressly states reuse permission for EDGAR public filing content; the
review does not substitute the broader claim that every issuer-authored filing
is a government-authored work.

The reviewed recommendation is **admissible, conditional**: a later admission
must use `/Archives/edgar/usgaap.rss.xml`, preserve the existing
monitored-contact identity, and keep total automated traffic at or below the
SEC's then-current published ceiling. The deferral trigger carries these
conditions and still requires a separate v0.25 operator admission decision.
`config/core.json` remains blob
`0ef1dcb4dde5f3cbd7b9112a405efb64d80e4914`; no source was added.

This review establishes neither multi-origin robots-cache/per-host-limiter
behaviour nor the **live RSS wire path**. Because it fetched no feed, it proves
nothing about live RSS fetching, feed parsing, or cursor durability against a
real server. No production source, tool, workflow, schema, protected artifact,
public surface, protected corpus, or golden-corpus fact changed.

**v0.24 RE-MEASURE admits authenticated release-posture evidence without
publishing (measured 2026-07-30).**

Exact candidate `a73c042068a367aea22e63e28dfd2f754b65ef9c` was pushed only
to neutral branch `codex/v0.24-evidence-a73c042`. Before dispatch, the remote
and local `.github/workflows/ci.yml` both resolved to Git blob
`48ea726b798f1049e0b29cce1f0c64588861c2dd`. Workflow-dispatch run
**`30472740314`**, attempt **1**, used the candidate as `audit_sha` with
`publish_evidence: true`. All seven executable jobs passed; report-only
dependency drift was skipped.

Both fresh local Python summaries reported collected **283**, passed **283**,
failed **0**, and skipped **0**. Both hosted summaries reported collected
**283**, passed **282**, failed **0**, and skipped **1**. The sole skip was
`tests/test_deferred_audit.py::test_on_site_production_measurements_match_committed_receipt`,
marked `on_site` and `skipif`, for
`on-site production audit requires protected corpora and built cored`.
`tools/test_population.py` produced this same result for Python 3.11 and 3.12:

`test-population-compare: {"collected":283,"equivalent":true,"equivalent_passed":283,"hosted":{"on_site_skipped":1,"passed":282,"skipped":[{"node_id":"tests/test_deferred_audit.py::test_on_site_production_measurements_match_committed_receipt","reason":"on-site production audit requires protected corpora and built cored"}]},"local":{"passed":283,"skipped":0},"schema_version":1}`

The operator's hosted-zero-skip stop condition therefore did not fire. Counts
read directly from the same hosted logs were workspace **133**, net **55**
(**29 + 26**), lifecycle **189 checked / 3 retracted / 189 matched / 0
exemptions**, `invariant-scan` **12/12 rules / 39 controls** with R12 control
**16** and R10 **45** exemptions, and golden **11/11**. Fresh local
`./run ci-local` passed all **20** jobs with the same non-shell and invariant
counts, warning-denied current and Rust 1.78 lanes, and clean
clippy/fmt/ShellCheck.

The hosted run produced seven receipt artifacts containing **7 receipts / 7
Sigstore bundles**. Release-posture verification required attestations and
accepted **7 / rejected 0**, with the complete job/matrix set and exact
bindings to repository `jiayanzeng/intel-platform`, workflow
`jiayanzeng/intel-platform/.github/workflows/ci.yml`, candidate digest,
neutral source ref, and GitHub-hosted runner identity. The clean disposable
audit subject was the exact candidate with an empty worktree. Its deferred
result was **5 deferred / 2 promoted / 0 implemented**; exact cosine at the
largest protected corpus of **2,600** documents measured p95 **8.955917 ms**,
below the A3 **16.264 ms** request anchor.

The fourteen signed files under `evidence/ci-runs/30472740314-1/` and
release report `evidence/v0.24/deferred-audit/report.json` increase the
protected manifest from **236** to **251** pins. The report is **34,899
bytes**, SHA-256
`8bcd4136c15619b554f2eae292d1de81c694d38b10bf48be382194173ebce0e7`.
Manifest validation, `verify-artifacts`, `evidence-report`, and report
re-derivation pass with all new and prior bytes exact. Remote `main` remains
`e7715fb97b86b91a2a58bc7b73bf99308c2aae9b`; no release tag or publication
ref was created. No source, public surface, dependency, lockfile, schema,
protected database, or golden-corpus fact changed. Mandatory standalone golden
remains **11/11**, delta **0**.

**v0.15.7 post-push confirmation and v0.23 exact-count correction (measured
2026-07-29).**

- **Post-push verification date:** 2026-07-29
- **Post-push release:** `v0.15.7`
- **Post-push annotated tag object:** `b579c2c18e4eeb549617ea20a9175b0c26dc621d`
- **Post-push closing commit:** `e7715fb97b86b91a2a58bc7b73bf99308c2aae9b`
- **Post-push hosted run:** `30462710258`

Atomic remote readback resolves `main` and the peeled v0.15.7 tag to closing
commit `e7715fb97b86b91a2a58bc7b73bf99308c2aae9b`; its first parent is release
commit `8bb6a71446b043b10ce16077499fdc07abb91b98`, and tag ref v0.15.7 resolves
to annotated object `b579c2c18e4eeb549617ea20a9175b0c26dc621d`.
Push run `30462710258` attempt **1** completed successfully at that exact
closing commit. All **7/7** executable jobs passed: core, lint, MSRV, net,
shell Python 3.11, shell Python 3.12, and golden; report-only dependency drift
was skipped. Hosted measurements include workspace **133**, net **55** (**29 +
26**), lifecycle **184** checked / **3** retracted / **184** matched /
**0** exemptions, `invariant-scan` **12/12 rules / 38 controls**, protected
pins **236**, and golden **11/11**.

The hosted shell logs expose a correction to the closing record. Candidate run
`30459746825` and forward run `30462710258` each report **274 passed / 1
skipped / 1 warning** on both Python lanes, not the recorded hosted
**275/275**. The skipped test is
`test_on_site_production_measurements_match_committed_receipt`, whose declared
condition requires the protected databases and a built local `cored`; those
on-site inputs are deliberately absent from a clean GitHub checkout. Local
release-parent Python 3.11.4 and 3.12.13 each did run and pass that test,
yielding **275/275**.

The candidate's seven job conclusions and authenticated identities remain
valid, and the published-head result is green, so this does not retroactively
invalidate the R-CLOSE Git graph or release. It does mean Step 6's literal
acceptance that every hosted count equal local was not met, and its runbook and
append-only progress claims of hosted **275/275** were false. Those historical
records remain preserved; this dated correction supersedes the count claim.
The new v0.24 apparatus input is to make environment-specific test populations
explicit or compare only equivalent populations. It also supersedes the
close-time observation that the scheduled apparatus queue was empty.

**v0.23 R-CLOSE selects v0.15.7 and closes on authenticated candidate evidence
(operator decision and measurement 2026-07-29).** Release disposition: release
(as of 2026-07-29). The
patch identity applies because the cycle changes workflow operations,
documentation, evidence, and lifecycle controls without changing any `/v1/*`
route or response body, schema, dependency graph, runtime behavior, robots
policy, configured source, or protected database.

Both publication triggers visible at entry fired. Published `main` still uses
checkout v4, upload-artifact v4, and setup-python v5, whose action declarations
target the obsolete Node 20 runtime even though hosted runners force Node 24.
Published `ARCHITECTURE.md` also still instructs a future releaser to map the
annotated tag to release parent `R`, while the executed R-CLOSE protocol tags
closing child `C`. Publishing v0.15.7 carries both measured corrections; a
no-release close would leave the stale operating workflow and stale release
instruction published.

Authenticated run `30459746825` attempt **1** at exact candidate
`5b075dfc87e789aa34c07b94a9a80f2f10af89f2` is the closing evidence. The
candidate is deliberately separate from release parent
`8bb6a71446b043b10ce16077499fdc07abb91b98`.
All **7/7** executable hosted jobs passed, and the release-grade verifier
accepted **7 / rejected 0** signed identities with attestations required. The
release parent is the untagged immediate parent of this closing tree. The
post-push hosted run is forward confirmation and belongs in the first dated
append after publication; a red result there would be a v0.24 finding, not
retroactive invalidation of this close.

The release-parent definition of done passed exactly: `./run ci-local`
**20/20**; workspace **133**; net **55** (**29 + 26**); shell **275/275** on
Python 3.11.4 and independently on Python 3.12.13; warning-denied current and
Rust 1.78 lanes; clean clippy, fmt, and ShellCheck; `invariant-scan` **12/12
rules / 38 controls** with R12 **15/15** and R10 **45**; protected evidence
**236/236** and databases **2/2**; root review export **90** derived sources,
**7** required, **153** exported; standalone golden **11/11**, delta **0**.

G1 is settled at **P2 by construction**, not by argument. E0 cloned the local
repository with its local tag namespace, forcibly retagged recorded v0.15.6
over release parent `a83db73aac3d5ef1e9a427662340eb1eb8a49df1`, and ran the
real `cycle-check` entry point. It rejected all four parent/tree agreement
violations against the constructed identity. The stale duplicate prose could
misdirect a releaser, but the executable checker already rejects the resulting
state; Step 2 therefore deleted the duplicate mechanics without adding a
redundant literal-scan rule.

G6 measured two populations under separate criteria, each **4**, with **2**
overlapping members:

- A checker-obligation member is one distinct accepted checker behavior family
  that can falsely pass, falsely fail, or omit a required result despite a
  completed invocation. The four are: v0.19 mutable-`origin/main` freshness,
  exposed by hosted run `30417274925` and the fixed-point construction in
  `PROGRESS-v0.20.md` E0; v0.20 unavailable tag/ancestry inputs silently
  succeeding, constructed in `PROGRESS-v0.20.md` E0; v0.21's vacuous
  tag-object pattern, constructed in `PROGRESS-v0.21.md` E0; and v0.22's
  self-referential closing field set, constructed in
  `PROGRESS-v0.22.md` E0.
- An author-side member is one normative runbook requirement for which no
  sequence can satisfy both the requirement and its governed release action.
  The four are: v0.19 `STATUS-TRUE` mutable-main freshness in v0.19 Step 2,
  exposed by the v0.20 hosted firing and E0 construction; v0.20's
  post-push-before-close ordering in v0.20 Step 7, found after publication and
  recorded by v0.21 R-CLOSE; v0.22's release-commit/tag-object field set in
  v0.22 G1, found by v0.22 E0's field enumeration; and v0.22's no-`crates/`/
  `apps/` prohibition, found by independent human review of the v0.23 draft and
  reproduced by v0.23 G4.

The exact overlap is v0.19 mutable-main freshness and v0.22's closing field
set. The unavailable-input and vacuous-pattern members are checker-only; the
R-CLOSE ordering and crate prohibition are author-only. The scope prohibition
is the first author-side member found only by human review because no tool read
prose scope. Step 4's declared-scope control is this cycle's product response
to that asymmetry.

The activation-committed scope block itself required correction: it omitted
`shell/tests/test_deferred_audit.py`, which Step 3 necessarily changed, and
its `shell/intel_shell/**` forbid overlapped two Python release authorities.
The final table adds the test path, uses `shell/intel_shell/[a-z]*.py`, and
names the exact Step 6 evidence locations. Its only authority/forbid overlap is
`shell/intel_shell/app.py`; moving that version literal to `__init__.py` is the
recorded v0.24 option, not a production-source edit hidden in this release.

Step 3 exercised the upgraded signing chain rather than inferring from old
pins. Hosted run `30456330833` produced **7 receipts / 7 Sigstore bundles**
under the migrated actions; the release-grade verifier accepted **7 / rejected
0** with the complete identity matrix. The same GitHub CLI also re-derived the
prior v0.22 set, so there was no action-side or CLI-side failure to classify
and no pin was reverted. That set remained verification-only. Step 6 separately
produced and admitted the authenticated closing set from run `30459746825`.

Step 5 freshly re-evaluated **14** trigger-bearing rows: **3** architecture
rows from E0 and **11** active deferrals. Exactly **2** had fired. The
Node-runtime condition was discharged by Step 3; the `app.py` scope overlap
created exactly **1** additional v0.24 assignment. No production-source work
was absorbed. The remaining live tables validate all **13/13** governed rows,
and `invariant-scan` passes **12/12 rules / 38 controls** with R12 **15/15**.

The exact committed `v0.15.6..8bb6a71446b043b10ce16077499fdc07abb91b98`
release-parent diff contains **34** paths classified once in seven disjoint
groups:

- **Workflow:** `.github/workflows/ci.yml`.
- **Operating contract, architecture, release notes, and status:** `AGENTS.md`,
  `ARCHITECTURE.md`, `CHANGELOG.md`, `README.md`, and `STATE.md`.
- **Release version authorities:** `Cargo.lock`, `apps/cored/Cargo.toml`,
  `shell/intel_shell/__init__.py`, and `shell/intel_shell/app.py`.
- **Cycle records:** `docs/cycles/PROGRESS-v0.22.md`,
  `docs/cycles/PROGRESS-v0.23.md`, and
  `docs/cycles/TASKS-v0.23-EXECUTION.md`.
- **Lifecycle controls and tests:** `config/invariant-rules.json`,
  `tools/cycle_check.py`, `tools/invariant_scan.py`,
  `shell/tests/test_cycle_check.py`, and
  `shell/tests/test_deferred_audit.py`.
- **Append-only provenance authority:** `config/protected-artifacts.json`.
- **Authenticated evidence:** all fourteen files under
  `evidence/ci-runs/30459746825-1/` and
  `evidence/v0.23/deferred-audit/report.json`.

The product boundary remains unchanged: `arxiv-cs` is the sole real publisher
and the other three configured sources remain fixtures. A4, editable L1, the
R3/R4 open-bottom limits, active-runbook measured-value heuristic, T7, and
NEGATIVE-CACHE Decision B remain open. After three consecutive cycles whose
entire defect population lived in the apparatus, the scheduled apparatus queue
is empty; v0.24 is the natural place to observe whether that debt repayment
makes product work cheap. This is a forward observation, not a scheduled task.

**v0.23 RE-MEASURE produced release-grade hosted evidence without publishing
(measured 2026-07-29).** Candidate
`5b075dfc87e789aa34c07b94a9a80f2f10af89f2` was pushed only to the neutral
branch `candidate/v0.23-remeasure`. Before dispatch, remote and local
`.github/workflows/ci.yml` both resolved to Git blob
`48ea726b798f1049e0b29cce1f0c64588861c2dd`. Workflow-dispatch run
`30459746825` attempt **1** used `audit_sha` equal to the candidate and
`publish_evidence: true`.

Every executable hosted job passed: core, golden, lint, MSRV, net, and shell
Python 3.11/3.12. Counts read from the hosted logs were **133** workspace
tests; **55** net tests (**29 + 26**); shell **274 passed / 1 on-site-only
skip** on both hosted interpreters and **275/275** locally on Python 3.11;
`invariant-scan` **12/12 rules / 38 controls** with R12 **15/15** and R10
**45** exemptions; lifecycle **182** checked, **3** retracted, **182**
matched, **0** exemptions; golden **11/11**. The hosted/local shell totals
therefore did not match; the dated post-push correction above records the
false closing claim. Local `./run ci-local` passed all **20/20** stages,
including warning-denied Rust, locked MSRV, clippy, fmt, and ShellCheck.

The hosted run produced exactly **7** receipt artifacts containing **7**
receipts and **7** Sigstore bundles. Release-posture verification required
attestations and accepted **7 / rejected 0**, with the complete job/matrix set
and exact bindings to repository `jiayanzeng/intel-platform`, workflow
`jiayanzeng/intel-platform/.github/workflows/ci.yml`, candidate digest, neutral
source ref, and GitHub-hosted runner identity. The clean detached audit subject
was the exact candidate with an empty worktree. Its deferred result was **5
deferred / 2 promoted / 0 implemented**; exact cosine at the largest evidenced
corpus of **2,600** documents measured p95 **7.777583 ms**, below the A3
**16.264 ms** request anchor. The report is pinned at SHA-256
`850fcefa7314d1b31bf85f3939275c89aa9d0d48ebedf38ae7d49309590a1317`,
**34,825 bytes**.

The manifest grew for the first time in v0.23, from **221** to **236** pins:
**234** evidence plus the unchanged **2** authorization pins. Manifest schema
validation, `verify-artifacts`, and `evidence-report` passed; both protected
databases remained byte-exact and integrity-clean. Remote `main` remained
`15b6d28973058c833a77e9600741d29eda02cdc1`, and no tag or publication ref was
created or moved. Mandatory standalone golden remains **11/11**, delta **0**.

**v0.23 TRIGGER-FRESHNESS makes dated re-evaluation executable over a bounded
live document set (measured 2026-07-29).** The rule applies only to
`ARCHITECTURE.md`'s live dated operational-residual dispositions and the active
runbook's **Deferred means deferred** table, v0.23-forward. A row is governed
only when its trigger cell is neither empty nor `none`. A valid ISO date may
live in its measured-observation cell or that column's header. This admits
event-shaped negative evidence such as “no operator server session has
occurred”; the checker establishes that the dated measurement clause exists,
not that the external statement is true.

E0 re-evaluated **3** trigger-bearing architecture dispositions. Step 5
re-evaluated the active table's **11** trigger-bearing deferrals, for exactly
**14** governed rows. Exactly **2** triggers had fired: the Node-runtime
condition discharged by Step 3 and the `app.py` scope condition exposed by Step
4. The latter produced the one additional forward assignment: evaluate moving
the version literal in **v0.24**, without absorbing a production-source change
into v0.23. After the completed Node row changed to trigger `none`, the two live
tables contain **2 + 11 = 13** governed rows and `cycle-check` accepts all
**13/13**. Architecture observations are freshly dated at **221 pins**,
**127,982 bytes**, two clean verification times of **0.10 s / 0.09 s real**,
and constrained Python 3.11.4/3.12.13 at **266/266** with one warning and no
relevant constraints refresh.

The planted construction was examined as one trigger-bearing row and rejected
for lacking a valid date. Registered R12 mutation **15** disables that exact
conditional and is detected as `missing-trigger-measurement-date` at
`tools/cycle_check.py:1474`. `AGENTS.md` now records the exact two-document
scope, row predicate, date placement, negative-event semantics, presence/date
limit, and forward boundary. Measured `invariant-scan` is **12/12 rules / 38
controls**, R12 **15/15**. Focused lifecycle tests pass **43/43**, invariant
tests **22/22**, and the combined run passes **65/65**. The first full shell
attempt was a sandbox permission non-result for loopback and `ps`; the
identical permitted Python 3.11 command passes **275/275** with one accepted
third-party warning. Mandatory standalone golden remains **11/11**, delta
**0**.

**v0.23 SCOPE-DECLARED makes cycle scope executable at two distinct firing
times (measured 2026-07-29).** The small schema is one markdown row per scope
class and path/value, parsed with the same cell and separator conventions as
the active deferral table. It is required only for the active v0.23-forward
runbook; no closed historical runbook was edited or retrofitted.

The static sub-rule fires at activation when disposition intent or the recorded
disposition is `release` and requires declared coverage for all **17** release
authorities. The diff sub-rule fires after later commits and measures activation
commit `09cb119ba4237f99f652327d8babd51d95517cd7` **exclusive** through
`HEAD` **inclusive**. Activation therefore has an empty diff. A disposable Git
fixture passed at its activation commit, then rejected `outside.txt` after the
next commit. The exact standing always-allowed paths live in the checker:
`STATE.md`, the active runbook, and the active progress record. `AGENTS.md` is
not standing and must be declared.

Validation found the activation draft was **not correct as committed**. Its
classes fit the table schema, but it omitted
`shell/tests/test_deferred_audit.py`, necessarily changed by Step 3, and the
draft `shell/intel_shell/**` forbid overlapped both Python release authorities
instead of the asserted one. The corrected glob
`shell/intel_shell/[a-z]*.py` covers lower-case production modules without
matching `shell/tests/**` or the version-only `__init__.py`; the measured
release-authority/forbid intersection is now exactly
`shell/intel_shell/app.py`. Release-authority precedence permits that file's
R-CLOSE version change and therefore weakens path-level enforcement for exactly
one file. Its complete diff still requires human classification. Moving the
FastAPI version literal into `__init__.py` is the recorded forward option, not
an in-scope source change.

The v0.22-shaped fail-before fixture produced all four required findings:
release-authority and diff rejection each named `apps/cored/Cargo.toml` and
`Cargo.lock`. It modified no closed runbook. Registered R12 mutation **14**
disabled the shared rejection site; self-test detected
`v0.22-release-paths`. `AGENTS.md` now states both firing times, the exact
endpoints and standing set, glob/precedence semantics, the v0.23-forward
boundary, and E0's interpretive rule that zero from an unexamined construction
means `not measured`.

Measured `invariant-scan` is **12/12 rules / 37 controls**, with R12
**14/14**. Focused lifecycle tests pass **39/39**, invariant tests **22/22**,
and the complete constrained Python 3.11 shell lane passes **271/271** with its
one accepted third-party warning. `cycle-check` accepts the corrected active
table. Mandatory standalone golden remains **11/11**, delta **0**.

**v0.23 ACTION-MIGRATION moves the evidence workflow to Node 24 and verifies
the new signing path (measured 2026-07-29).** Before implementation, the Gate
was widened narrowly because
`test_every_workflow_job_emits_and_persists_a_receipt` named
`actions/upload-artifact@v4`; without its one version-string update, the
mandated v6 migration would make the repository's receipt control false. No
production source was admitted. The one attributable workflow edit changed all
**7** checkout uses from v4 to v5, all **7** upload-artifact uses from v4 to v6,
and both setup-python uses from v5 to v6. E0 already measured rust-cache v2 and
attest-build-provenance v4 on Node 24 implementations, so their majors did not
move. The three upgraded majors preserve the inputs and outputs this workflow
uses; their migration note is the internal Node 24 runtime and minimum Actions
Runner **v2.327.1**.

Primary `git ls-remote` resolution pinned all **6** composite
`dtolnay/rust-toolchain` uses to
`2c7215f132e9ebf062739d9130488b56d53c060c`; E0's disposable clone dated that
commit **2026-07-16T09:35:07-07:00**. The cost and revisit rule are coupled:
an immutable pin receives no upstream fixes automatically, so re-resolve and
re-measure it when `rust-toolchain.toml` changes or upstream publishes an
applicable security or correctness fix, and at the next authorized workflow
maintenance pass if neither occurs first.

Static verification found all existing **221/221** pins and both protected
databases byte-exact. This proves only that the manifest and recorded bytes are
intact; it does **not** exercise the upgraded signer. Separately, GitHub CLI
**2.96.0 (2026-07-02)** re-derived the prior v0.22 release-grade evidence as
**7** authenticated receipts, then verified Step 3's newly produced set from
run `30456330833` attempt 1. That disposable set contains **7** receipts and
**7** Sigstore bundles; the release-grade verifier accepted **7**, rejected
**0**, required attestations, denied self-hosted runners, and derived exactly
`core`, `golden`, `lint`, `msrv`, `net`, `shell/python=3.11`, and
`shell/python=3.12`. Every item binds repository
`jiayanzeng/intel-platform`, workflow
`jiayanzeng/intel-platform/.github/workflows/ci.yml`, source digest
`81ca6498c825e52c2c2604eec169bd4a4898b6e3`, and source ref
`refs/heads/codex/v0.23-action-migration`. Verification succeeded, so there is
no action-side or CLI-side failure to classify and no pin to revert.

Direct check-run inspection found annotation count **0** on all seven
successful executable jobs and the one skipped report-only job. The old Node
runtime annotation is absent and no replacement annotation exists. The hosted
set and its temporary audit report stayed under `/private/tmp`; neither the
repository nor `config/protected-artifacts.json` contains them. Local
`cycle-check`, the targeted receipt control, shell **266/266**, and
`invariant-scan` **12/12 rules / 36 controls** passed. The first sandboxed
shell and golden attempts were permission non-results; identical permitted
runs passed, with standalone golden **11/11**, delta **0**.

**v0.23 RELEASE-PROSE makes R-CLOSE mechanics single-source (measured
2026-07-29).** E0 forced the recorded `v0.15.6` identity onto the wrong commit
and the existing checker rejected all four parent/tree agreement violations;
G1 is therefore P2 by construction, and no duplicate literal-scan rule was
added. `ARCHITECTURE.md` §8 retains the minor/patch/no-release classification
and version-agreement semantics, then points to `AGENTS.md` as the sole
authority for tag creation, target selection, closing order, historical
boundary, and forward evidence. `AGENTS.md` now states the boundary directly:
releases through v0.15.5 keep the prior validation shape, while v0.15.6 onward
uses the two-commit tagged close.

The one-time mechanical-mapping scan
`grep -Eni 'tag (targets|points|maps)( to)? (the )?(release|closing|tagged)? ?commit|mapping is the annotated Git tag|tagged commit' ARCHITECTURE.md`
returned exit **1** with empty stdout: zero mapping sentences remain. This grep
reduces the duplicate-prose class but is not a persistent invariant. If a
duplicate mechanical mapping recurs, the forward option is a registered
literal-scan rule with a detected R12 planted failure; adding that apparatus
now would duplicate a checker that E0 measured clean. `cycle-check`,
`progress-check`, and the pre-box `checklist-audit` passed; the mandatory
standalone golden remained **11/11**, delta **0**. No workflow, crate, source,
dependency, schema, protected artifact, public surface, or ref changed.

**v0.22 R-CLOSE selects release v0.15.6 and closes on authenticated candidate
evidence (operator decision and measurement 2026-07-29).** Release disposition:
release (as of 2026-07-29). The patch identity is v0.15.6 because no `/v1/*`
route or response body, schema, dependency, runtime behavior, robots policy,
configured source, or protected database changed.

The publication trigger is Option C itself. Its **13** R12 mutations prove the
checker detects protocol violations, but do not prove that release parent `R`,
immediate closing child `C`, an annotated tag over `C`, an atomic main/tag push,
and the dated forward append compose against a real remote. A no-release close
would leave both that property and G3 unexecuted. Publication makes the closed
v0.22 runbook part of the published tree for the first time in project history.

Authenticated run `30443692105` attempt **1** at exact candidate
`10c78119cd10eeb17a01152de6b6f0c322b2b91e` is the closing event. The release
parent is `a83db73aac3d5ef1e9a427662340eb1eb8a49df1`; it is distinct from the
evidence candidate. Published-head CI is forward confirmation and will be
recorded in the first dated append after the closing commit. A red result there
would be a v0.23 finding, not retroactive invalidation of this close.

The release-parent definition of done passed exactly: `./run ci-local` **20/20**;
workspace **133**; net **55** (**29 + 26**); shell **266/266** on Python 3.11.4
and independently on Python 3.12.13; warning-denied current and Rust 1.78
lanes; clean clippy, fmt, and ShellCheck; `invariant-scan` **12/12 rules / 36
controls** with all **13** R12 mutations detected; R10 **45**; protected
evidence **221/221** and databases **2/2**; root review export **90** derived
sources, **7** required, **151** exported; standalone golden **11/11**, delta
**0**.

G1 is the fourth instance of one failure family and its second fixed point.
v0.19 shipped an unsatisfiable rule, v0.20 two silent no-op inputs, v0.21 a
vacuous pattern, and v0.22 a self-referential closing field set. The v0.21
record misdiagnosed the defect as step ordering; E0's enumeration proved that
candidate evidence was necessary but insufficient because the tag-object value
remained unknowable in every ordering. Option C removes only that field from
`C`, binds the tag and parent through Git, and requires the later exact forward
record.

G2 remains **A / A / E**: local annotated v0.8.0 and v0.10.2 identities are
valid, the remote is incomplete, and hosted local-tag verification remains
skipped until its recorded correction trigger fires. The retraction count is
still **three**. The exact historical tag objects were not published or moved
in this release.

Step 4's dated dispositions carry forward with one measured correction. G3 is
refuted because the operator-local export contract already exists. G4 remains
accepted at **119,353 bytes / 206 pins / +15 per cycle** and **0.10 s** against
its **1 MiB** and two-run **1.00 s** triggers. The shell warning remains
accepted until error/failure or a relevant constraints refresh. The hosted
warning's named-date trigger was already satisfied when its pending
disposition was written: GitHub's 2025-09-19 announcement named 2026-06-16,
and the candidate run measured all seven jobs green while forced onto Node 24.
This is scheduled v0.23 work, not a scope expansion here. The same workflow
pass must upgrade the affected actions, replace
`dtolnay/rust-toolchain@master`, re-measure hosted provenance, and add the
operating-contract requirement that every recorded trigger state the
measurement proving it has not already fired.

Every path in `v0.15.5..C` is classified exactly once:

- **Operating contract, architecture, release notes, and status:** `AGENTS.md`,
  `ARCHITECTURE.md`, `CHANGELOG.md`, `README.md`, and `STATE.md`.
- **Release version authorities:** `Cargo.lock`, `apps/cored/Cargo.toml`,
  `shell/intel_shell/__init__.py`, and `shell/intel_shell/app.py`.
- **Cycle records and forward corrections:**
  `docs/cycles/PROGRESS-v0.21.md`, `docs/cycles/PROGRESS-v0.22.md`,
  `docs/cycles/TASKS-v0.21-EXECUTION.md`, and
  `docs/cycles/TASKS-v0.22-EXECUTION.md`.
- **Failure-capable lifecycle controls:** `config/invariant-rules.json`,
  `shell/tests/test_cycle_check.py`, `tools/cycle_check.py`, and
  `tools/invariant_scan.py`.
- **Append-only provenance authority:** `config/protected-artifacts.json`.
- **Authenticated hosted receipts and bundles:**
  `evidence/ci-runs/30443692105-1/30443692105-1-core.json`,
  `evidence/ci-runs/30443692105-1/30443692105-1-core.json.sigstore`,
  `evidence/ci-runs/30443692105-1/30443692105-1-golden.json`,
  `evidence/ci-runs/30443692105-1/30443692105-1-golden.json.sigstore`,
  `evidence/ci-runs/30443692105-1/30443692105-1-lint.json`,
  `evidence/ci-runs/30443692105-1/30443692105-1-lint.json.sigstore`,
  `evidence/ci-runs/30443692105-1/30443692105-1-msrv.json`,
  `evidence/ci-runs/30443692105-1/30443692105-1-msrv.json.sigstore`,
  `evidence/ci-runs/30443692105-1/30443692105-1-net.json`,
  `evidence/ci-runs/30443692105-1/30443692105-1-net.json.sigstore`,
  `evidence/ci-runs/30443692105-1/30443692105-1-shell-py3.11.json`,
  `evidence/ci-runs/30443692105-1/30443692105-1-shell-py3.11.json.sigstore`,
  `evidence/ci-runs/30443692105-1/30443692105-1-shell-py3.12.json`, and
  `evidence/ci-runs/30443692105-1/30443692105-1-shell-py3.12.json.sigstore`.
- **Release-posture deferred evidence:**
  `evidence/v0.22/deferred-audit/report.json`.

The product boundary is unchanged: `arxiv-cs` remains the sole real publisher;
the other three configured sources remain fixtures. No crate source under
`crates/` or `apps/`, dependency graph, CI workflow, schema, protected
database, robots behavior, configured source, or public API surface changed.

- **Post-push verification date:** 2026-07-29
- **Post-push release:** `v0.15.6`
- **Post-push annotated tag object:** `47c5b314acd6f7fb42bba2f90312bf1185277c5c`
- **Post-push closing commit:** `15b6d28973058c833a77e9600741d29eda02cdc1`
- **Post-push hosted run:** `30446796322`

**v0.15.6 post-push forward confirmation passes (measured 2026-07-29).**
The atomic remote operation moved `main` from
`b7c4b10eb506923e3ea854a32d1dc3f4c83b0eaa` to closing commit
`15b6d28973058c833a77e9600741d29eda02cdc1` and created annotated v0.15.6
object `47c5b314acd6f7fb42bba2f90312bf1185277c5c`, which peels to that same
commit. The closing commit's first parent is release commit
`a83db73aac3d5ef1e9a427662340eb1eb8a49df1`. Remote readback confirmed all
three identities after the atomic push.

Push run `30446796322` executed at the exact closing commit and passed all
**7/7** executable jobs: core, lint, net, MSRV, shell Python 3.11, shell Python
3.12, and golden. The report-only dependency-drift job was skipped by its
declared trigger. Receipt attestations were intentionally absent because this
ordinary push was forward confirmation, not the evidence-publishing candidate
dispatch. The Node runtime annotations repeated without causing a failure and
remain the measured v0.23 finding already recorded above.

This dated append is the first commit after the tag target. Under the accepted
cycle-ending hosted-verification rhythm it is locally gate-backed and remains
hosted-unverified until the following publication; that is the protocol's
recorded cost, not a missing v0.22 release check.

**v0.22 RE-MEASURE admits authenticated release-posture evidence without
prejudging publication (measured 2026-07-29).** The operator authorized the
Gate's exact non-`main` branch push and authenticated hosted dispatch. Candidate
`10c78119cd10eeb17a01152de6b6f0c322b2b91e` was pushed only to
`candidate/v0.15.5-v0.22`; remote `main` remained
`b7c4b10eb506923e3ea854a32d1dc3f4c83b0eaa`. No tag, publication, product
path, public surface, dependency, lockfile, schema, protected database, or
release authority changed.

Before dispatch, the remote candidate's `.github/workflows/ci.yml` was read
through the GitHub contents endpoint. Its blob
`96e85af978981b7af9bdd8e9e11069f158f35e57` exactly equals the local workflow
blob and contains the expected core, lint, net, MSRV, two-shell, lifecycle,
invariant, golden, receipt, provenance-signing, and artifact-upload invocations.
Workflow-dispatch run `30443692105` attempt **1** completed successfully at
that exact candidate. All **7/7** executable job instances were green; the
report-only dependency-drift job was skipped by its declared trigger. This is
the authenticated candidate evidence that Option C's Step 6 closing record
must cite.

Every count was read from the hosted log and reconciled with local execution at
the same commit. Local `./run ci-local` passed **20/20** with **133** workspace
tests, **55** net tests (**29 + 26**), locked Rust 1.78, zero
rustc/clippy/fmt/ShellCheck failures, shell **266/266** on Python 3.11.4,
`invariant-scan` **12/12 rules / 36 controls**, R10 **45** exemptions, and
embedded golden **11/11**. The independently rebuilt Python 3.12.13 lane also
passed **266/266**. Hosted logs report the same **133**, **55**, **12/12 / 36**,
**45**, and **11/11** counts. Hosted Python 3.11.15 and 3.12.13 each collected
the same **266** shell tests as **265 passed + 1 declared on-site-only protected
corpus skip**, after resolving the exact **21-package** constraints.

Hosted lifecycle output found active v0.22 open with **19** closed execution
runbooks and **3** historical runbooks; checklist audit reported **175 checked /
3 retracted / 175 matched / 0 exemptions**; progress-check resolved
`RESIDUALS · d38030e`. The hosted **12/12 rules / 36 controls** measurement is
the required proof that Step 2's expanded R12 planted failures execute outside
the local harness.

The seven successful Linux receipts — core, golden, lint, MSRV, net, and shell
Python 3.11/3.12 — came from the one run and exact candidate. All seven
persisted Sigstore bundles verify their receipt bytes, repository
`jiayanzeng/intel-platform`, workflow signer, source digest, neutral candidate
source ref, and GitHub-hosted runner identity. Zero receipts were rejected and
the derived identity matrix is complete.

The release-posture deferred audit measured a clean detached candidate with
byte-identical ignored protected databases. It records **5 deferred / 2
promoted / 0** deferred subsystems implemented; exact-cosine p95 at the largest
**2,600-document** archive is **6.966708 ms**, below the **16.264 ms** A3
request anchor. Report `evidence/v0.22/deferred-audit/report.json` is **34,816
bytes** at SHA-256
`7fc1b09004d1cb8e835cf90bd3d11bf68e856c4d56bb2c9564a7fdbf77abced0`.

The **15** append-only admissions bring the schema-v2 manifest to **221/221**
pins — **219/219** evidence plus **2/2** authorization surfaces. Manifest
validation, `verify-artifacts`, and `evidence-report` pass; protected databases
remain exact **2/2**. Standalone golden remains **11/11**, delta **0**.

The hosted logs also repeat one annotation in every executable job: pinned
actions still target Node 20 and are being forced to run on Node 24. The linked
GitHub announcement names **2026-06-16** as the migration date and says Node 20
removal follows in fall 2026. Step 4's “when GitHub names an enforcement date”
trigger was therefore already true when that disposition was written. Step 5
does not silently upgrade action pins because doing so would change the exact
candidate whose evidence it admits. This is a measured forward-correction
subject for Step 6's required `ARCHITECTURE.md` reconciliation, not a renewed
acceptance of the expired trigger.

**v0.22 CLOSE-FIELDS adopts tagged-closing Option C (operator decision and
measurement 2026-07-29).** The operator answered `C`, accepting its stated
coverage cost: the annotated-tag object is no longer stored in the runbook, and
the closing record cites authenticated candidate evidence rather than a
published-head run. That cost is acceptable because the closing tree can now
state only facts that exist when it is committed, while Git identity checks
bind the later annotated tag to that tree and the next dated `STATE.md` append
pins the tag object, closing commit, and post-push hosted run. Published-head CI
is therefore forward confirmation, not the event that closes the cycle.

The implemented two-commit protocol leaves release commit `R` untagged. Its
immediate child `C` checks R-CLOSE and records `R` with no annotated-tag-object
field; the annotated release tag targets `C`. At the tagged checkout,
`cycle-check` requires an annotated tag, verifies `R` as `C`'s first parent,
and reads `C`'s runbook tree to confirm the closed release record. After `HEAD`
advances beyond `C`, the checker requires one exact dated forward record and
reconciles its tag object and closing commit with Git. Legacy releases through
v0.15.5 retain their prior validation semantics.

The corrected checker rejects the pre-change active closing shape verbatim:

```
docs/cycles/TASKS-v0.22-EXECUTION.md: declared closed cycle must use the tagged-closing protocol and omit the Annotated tag object field; record that object in the dated post-push append
```

The old checker also rejected the selected no-tag-object shape with
`closing record must contain exactly one annotated tag object; found 0`,
establishing fail-before on both sides of the protocol change. R12 now has
**13** registered fail-before mutations covering the active protocol shape,
annotated-tag type, release parent, tagged tree, three legacy publication
families, release-commit header assertion, pending status, unavailable tag and
target, ancestry, and the complete dated post-push record. All are detected;
the repository total is **12/12 rules / 36 controls**.

Focused `cycle_check` tests pass **34/34** on constrained Python 3.11.4 and
3.12.13. The complete local matrix passes **20/20** with **133** workspace
tests, **55** net tests (**29 + 26**), shell **266/266**, warning-denied current
and locked Rust lanes, and clean clippy/fmt/ShellCheck gates; the independent
Python 3.12.13 shell lane also passes **266/266**. Golden passes **11/11** with
delta **0**. No ref, closed runbook, published tree, crate, dependency, schema,
protected artifact, database, or public surface changed.

**v0.22 TAG-IDENTITY retains both historical release claims and gives hosted
tag verification a removal trigger (operator decision and measurement
2026-07-29).** The operator accepted the recommended `A / A / E`
disposition. The record is right and the remote is incomplete for both tags:

- Local `refs/tags/v0.8.0` is annotated tag object
  `314c1dd914a3d8e9193445874a419ed762581e6e`, which targets existing commit
  `bfc8c5af85734583f966ee70d2ec521155432205`.
- Local `refs/tags/v0.10.2` is annotated tag object
  `d821f8b2eb6f39fe4a7d06a88cd61de771c7b0ba`, which targets existing commit
  `7d127abac0b993c9e98294ee1c03ff01153de9d0`.

Fresh local type checks return `tag` for both objects and `commit` for both
targets. Fresh complete remote enumeration returns neither tag name nor any of
the four object ids. These are therefore valid local-only release identities,
not false historical publication records. Publishing the exact existing tags
is the eventual corrective action, but it is a separate operator-authorized
ref operation and was not performed here.

The retraction count remains **three**: neither release record is retracted and
no closed runbook or retraction registry changes. Hosted CI deliberately
retains `cycle-check --skip-local-tag-verification` for now because the remote
does not supply the two historical refs. The removal trigger is concrete:
remove the flag only after either the exact existing annotated objects are
published under both recorded tag names and a hosted full-history checkout
passes `cycle-check` without the flag, or contrary evidence causes both
tag identities and all affected release claims to be forward-corrected through
the existing closed-cycle correction mechanism. No tag, remote ref, closed
runbook, published tree, crate, dependency, schema, protected artifact,
database, or public surface changed. Golden remains **11/11**, delta **0**.

**v0.22 RESIDUALS gives G3, G4, and both G5 warnings one dated disposition
(decided and measured 2026-07-29).** G3 is **REFUTED** and its implementation
half is deleted: `ARCHITECTURE.md` and `AGENTS.md` already say
`./run export-check` is operator-local, what it checks, why local and hosted CI
omit it, and what an operator invocation catches. No duplicate rule, CI job, or
hosted-workaround trigger is added.

G4 is **accepted with bounds**. The protected manifest is **119,353 bytes** at
**206** pins; release totals are **161 → 176 → 191 → 206**, exactly **+15 per
cycle**. E0 measured the complete re-hash at **0.10 s real / 0.05 s user / 0.04
s sys**. Immutable append-only provenance is worth that currently negligible
cost. Retention/indexing becomes work when the manifest first reaches **1 MiB**
or two consecutive clean `./run verify-artifacts` runs each take **≥1.00 s
real**, whichever occurs first.

G5 is **accepted until named triggers**, separately per warning. The one
third-party `StarletteDeprecationWarning` becomes work if it becomes an
error/failure or at the next authorized constraints refresh touching FastAPI,
Starlette, `httpx`, or `httpx2`; both constrained lanes must then be
re-measured. The hosted GitHub Actions Node-runtime annotation becomes work
when GitHub names an enforcement date, a blocking job warns as an error or
fails for that runtime, or an affected `actions/*` pin changes; that work must
upgrade or replace the action and re-measure hosted CI.

All three dated outcomes are in `ARCHITECTURE.md`'s operational-residual table.
Manifest validation still passes **206/206** pins. `cycle-check`,
`checklist-audit`, and `progress-check` pass; golden remains **11/11**, delta
**0**. No tool logic, crate, dependency, schema, protected artifact, database,
or public surface changed.

**Historical state appends through v0.21 are archived byte-for-byte at `docs/state-archive/STATE-through-v0.21.md`.**

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
