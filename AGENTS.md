# AGENTS.md — operating contract for autonomous agents on intel-platform

This file governs how an autonomous coding agent (Codex, or any successor) works
in this repository. It is not a style guide; it is a set of constraints that
exist because each one was learned the expensive way. Read it before touching
anything, and re-read the two documents it points at:

- **`ARCHITECTURE.md`** — authoritative for *invariants* (what must be true of
  the system). These change rarely and never casually.
- **`STATE.md`** — authoritative for *current status* (what is true right now).
  You update this after every task; see §5.

**Active cycle:** v0.36

Task work for this declared cycle is ordered in
**`docs/cycles/TASKS-v0.36-EXECUTION.md`**. Every completed step is logged in
**`docs/cycles/PROGRESS-v0.36.md`**. The declaration points at the open cycle
while work remains and at the latest closed cycle after its release record is
appended, until the operator supplies the next runbook. Every older execution
runbook appends its dated closing record; its progress log and full original
task document remain preserved as historical rationale. `./run cycle-check`
enforces that the declared runbook is either open with an unchecked task or
closed with one valid release record, and that every older runbook is closed.

## 0. The one rule the others serve

**A claimed property that nothing executes is not a property.** This project has
been bitten by that exact failure three times on record: `--features net` sat
broken for two cycles because no CI job compiled it; "robots-compliant" meant
"compliant with a policy we wrote ourselves" because nothing ever fetched a real
`robots.txt`; and an MSRV floor of 1.75 was asserted in a document while the
committed lockfile could not be parsed below 1.78. Every sentence you add to
`STATE.md` must be backed by a command you ran and whose output you captured. If
you did not run it, do not claim it.

Corollaries, each earned:

- **A test double that cannot fail is not a test.** Before trusting a guard,
  give the double the ability to violate it and confirm the guard catches it.
  Every registered invariant rule carries a reconstructible `fail_before`
  mutation whose expected failure is executed by `invariant-scan --self-test`;
  prose saying a rule fired is not a control.
- **A zero exit on a construction the checked entry point did not examine is
  not a negative result.** It is `not measured`. Before interpreting a planted
  construction's success, demonstrate that the rule under test read that
  construction; this is the v0.21 vacuous-pattern lesson applied to controls.
- **Fixtures prove the state machine, not the wire (HC13).** A green fixture test
  is evidence about parsing and control flow, never about what a real server
  does. Live-path claims require a live run.
- **Report what the wire actually did.** "Blocked", "should work", and "reached
  the endpoint" are non-results until documents land and you can count them.
- **Verify command claims at the command's entry point, not its caller.** In
  v0.14, reading `run`'s wrapper without `invariant_scan.py`'s `main()` produced
  a false self-test finding; this mirrored v0.13, when the tool was read and its
  wrapper was not. This is deliberately a non-executable review discipline for
  humans and agents: syntax cannot prove that a reviewer followed the call
  chain. This rule and the dated-disposition rule immediately below preserve
  their review provenance in
  `docs/REVIEWER-LESSONS-v0.13-v0.14.md`.
- **A closing disposition is true as of a date, not forever.** v0.14's later
  publication authorization superseded its accurate-at-close `no-release`
  disposition without making the historical record false. Every cycle closed
  under this contract records `Release disposition: release|no-release (as of
  YYYY-MM-DD)`. `cycle-check` enforces the dated form prospectively when the
  declared runbook closes; already-closed runbooks remain immutable historical
  evidence.
- **Verify the entering state; trust no summary.** At cycle start, rebuild and
  re-run rather than believing the header of the last handoff — including this
  one.

## 1. Decision gates: stop and record, do not push through

Every task in the runbook carries a **decision gate** — a condition that, if
tripped, means *stop, write down what you found, and do not proceed*. Gates are
not obstacles to route around; they are the mechanism that has correctly kept
`feed-rs`, `texting_robots`, and LSH banding out of this codebase after each was
built or evaluated and measured. When a gate trips:

1. Do **not** implement a workaround that defeats the gate's purpose.
2. Record the measurement that tripped it in `STATE.md` and the active cycle's
   progress log named in the declaration above.
3. Mark the task blocked/deferred with the gate cited, and move on.

A gate you silence is worse than a task you skip.

## 2. Hard constraints (never violate these)

These are the load-bearing invariants. `ARCHITECTURE.md` explains why each lives
where it does; here is what you must never do.

- **HC1 — no gated text on a public path.** `IndexOnly` document text must never
  reach a public API response. It may be handed to a model as *analysis context*
  on internal loopback endpoints (`/retrieve`, `/docs`) — that is not
  redistribution — but the public surface must not carry it. `/v1/ask` model
  output must pass through the core's `/attest` license check before return;
  never bypass or move that check into the shell.
- **HC2 — entitlement is decided in the shell; sector filtering is *also*
  enforced in core SQL.** A shell bug may grant the wrong sectors; it must never
  be able to bypass the core's filter. Never move the sector filter out of core.
- **HC3 — the core never calls an LLM.** The shell pulls `GET /embeddings/missing`,
  calls the provider, and posts vectors back to `POST /embeddings`. The core
  inspects strings it is handed; it does not generate them. T1's `/attest`
  endpoint inspects a string — it does **not** weaken this.
- **HC8 — politeness is process-scoped, not request-scoped.** `HostLimiters` and
  `RobotsCache` live in `AppState`. Never rebuild them per request; a per-request
  robots cache re-fetches every publisher's `robots.txt` on every ingest, which
  makes "compliance" a worse citizen than none.
- **HC9 — persistence scope is explicit.** HC9 governs shell-owned
  configuration: atomic JSON is the default, and any new SQLite-backed shell
  configuration needs a recorded reason. The core archive is SQLite by design.
  The recorded SQLite scopes are:
  - **Harvest cursors:** live beside documents so a page and its continuation
    state commit in one transaction.
  - **Subscriptions:** shell-owned configuration may explicitly select
    `sqlite:///…` for transactional billing, key rotation, and revocation;
    atomic JSON remains the default.
  - **Core store tables:** `documents`, `embeddings`, and `signals_history`
    are archive/query state, not shell-owned configuration.
- **HC12 — never delete `Cargo.lock` to "fix" a resolution error; understand it.
  The lockfile *format* is part of the MSRV surface, not just the dependency
  graph.** A format-v4 lock cannot be parsed below Rust 1.78. Re-encoding to v3
  is not stable (cargo rewrites it to v4 on the next modification), so do not
  hand-edit the format as a fix.
- **HC13 — fixtures prove the state machine, not the wire.** (See §0.)
- **Credential disclosure is forbidden; private-network documentation is
  not.** Never commit `.env`, provider keys, tokens, private key material, or
  raw secret-bearing responses. RFC 1918 hosts and loopback-forward ports may
  be documented because they convey no access without the operator's network.
  The v0.11 host/port prohibition was false when written and had no executable
  guard during its lifetime; v0.12 replaces it with registered credential scan
  R4.
- **The robots gate composes one way only.** The publisher's fetched policy and
  the operator's configured deny-list both apply; the operator list can only ever
  refuse *more*. Fail-closed on unreachable (5xx / DNS / TLS / timeout ⇒ take
  nothing). The 404 disposition is **per-source** (`robots_on_missing`), defaults
  to deny, and opting in reinterprets *absence only* — it must never become
  "ignore robots.txt". Never replace this with a global flip. Automatic HTTP
  redirects stay disabled; every document redirect is followed manually and the
  full gate is re-run before requesting the next origin.
- **Dedup identity is a function of the corpus, not arrival order.** `canonical_id`
  is re-materialized from the global rule (earliest by `(published_day, id)`) on
  every ingest that adds rows — never assigned first-seen-wins at insert.
  `/retrieve` deliberately does *not* filter by `canonical_id`; it keeps whichever
  of a near-dup pair the query ranked higher. Do not "simplify" either of these.

## 3. The dependency gate (three clauses, all must pass)

Before adding any crate, evaluate it against all three and record the result in
the decision log (`STATE.md §6`). A crate is **rejected** if it:

1. **raises either MSRV floor** (the offline build must stay ≥ 1.78; the
   live-fetch `net` graph is separately pinned at 1.86 by `cored` →
   `intel-ingest` → `reqwest` 0.11.27 → `url` 2.5.8 → `idna` 1.1.0 →
   `idna_adapter` 1.2.2 → `icu_*` 2.2.0, whose locked crates declare 1.86).
   The earlier `intel-compliance` warning was a counterfactual: adding
   `texting_robots` would have pulled that expensive chain into the offline
   graph, which is one reason it was rejected; the shipped seven-crate
   `intel-compliance` graph does not contain ICU, or
2. **adds excessive transitive dependencies** (compare against the receiving
   crate's current tree — `intel-compliance` has 7 crates total; `intel-ingest`
   has 16), or
3. **changes any existing type boundary or allow/deny outcome** (e.g. returns
   `chrono::DateTime` where the project uses the ordinal `Day`, which would
   silently move document ids).

When the *correctness assurance* of a crate is the valuable part but the
*dependency* is the expensive part, use it **out of tree as a differential
oracle** (as `texting_robots` was: 368 verdicts, 0 divergences) and ship your own
zero-dependency implementation.

## 4. Build, test, and toolchain

Toolchain is pinned by `rust-toolchain.toml`. This MacBook runs 1.91.1, which
satisfies both floors, so nothing in this cycle is toolchain-blocked here.
Python 3.11 is the supported shell and harness minimum; CI also exercises 3.12.

```
# offline path (MSRV floor 1.78) — everything except live fetching
cargo check --workspace --locked --all-targets
cargo test  --workspace --locked

# the live-fetch path (MSRV floor 1.86) — the path that sat broken unwatched
cargo check -p cored --features net --locked --all-targets
cargo test  -p intel-ingest --features net --locked

# the live-fetch floor itself — success at 1.86, declared-MSRV refusal at 1.85
RUSTFLAGS="" rustup run 1.86.0 cargo check -p cored --features net --locked --all-targets
RUSTFLAGS="" rustup run 1.85.0 cargo check -p cored --features net --locked --all-targets

# lint (clean and blocking in CI since T6)
cargo clippy --workspace --locked --all-targets -- -D warnings
cargo fmt --all -- --check

# shell (holds the entitlement/licensing invariants the Rust tests do not)
python3 -m venv --clear .venv
.venv/bin/python -m pip install \
  -c shell/constraints.txt -r shell/requirements.txt
.venv/bin/python tools/python_constraints.py shell/constraints.txt
PYTHONPATH=shell .venv/bin/python -m pytest shell/tests -q
```

Rebuild the local Python 3.12 lane in the repository's already-ignored
`.venv/` tree; do not inherit a random `/private/tmp` environment:

```
python3.12 -m venv --clear .venv/py312
.venv/py312/bin/python -m pip install \
  -c shell/constraints.txt -r shell/requirements.txt
.venv/py312/bin/python tools/python_constraints.py shell/constraints.txt
PYTHONPATH=shell .venv/py312/bin/python -m pytest shell/tests -q
```

An MSRV floor lane must select its toolchain at a precedence level above
`rust-toolchain.toml`, for example with `rustup run <version> cargo ...`, and
must prove the effective `cargo -V` and `rustc -vV` release before compiling.
A `dtolnay/rust-toolchain` action `toolchain:` input only installs and selects
the rustup default; it does not override the tracked toolchain file and is not
by itself a floor selection.

Both clean rebuilds were executed on 2026-07-25 with Python 3.11.4 and
3.12.13. Their application/test resolutions were byte-identical and are
enforced by `shell/constraints.txt`; `shell/requirements.txt` remains the
declaration of floors.

```
annotated-doc==0.0.4
annotated-types==0.8.0
anyio==4.14.2
certifi==2026.7.22
click==8.4.2
fastapi==0.140.0
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

`RUSTFLAGS="-D warnings"` is the standing rule for the offline and net builds:
**0 warnings is a gate, not an aspiration.** ("0 warnings" means *rustc*
warnings; clippy is an independent blocking gate.)

### Review-export operating rules

- **Write every Repomix review export from the project root.** A measured
  non-root invocation did not load `repomix.config.json` and silently dropped
  `Cargo.lock`, recreating the lockfile-review gap this project has already paid
  for. Use `./run export-check`; it generates from the root and derives the
  expected source set from `git ls-files`.
- **Keep Repomix `enableSecurityCheck` set to `false`.** The measured security
  pass reported **340 files collected, 339 included** and silently omitted
  `crates/ingest/src/lib.rs`. Registered, self-testing invariant R4 is this
  repository's credential control. `./run export-check` fails if the omitted
  source is absent from the generated review export.
- **Keep the review export within its executable bound.** `export-check`
  rejects an export above 3,000,000 bytes, derives exactly two retained
  execution cycles (the active cycle plus one prior) from the cycle declaration,
  and rejects the pinned SEC RSS body or any `docs/state-archive/**` content in
  the export. Repository bytes and protected pins remain untouched by these
  review-scope exclusions.

These are review-export operating rules, not additions to the HC series.

## 5. The per-task workflow — status is updated in real time

You do **not** batch status updates. After each task, in order, before starting
the next:

Before implementation, verify that the task's Gate contains the scope of every
acceptance criterion. A Gate may not be narrower than its criteria: widen the
Gate or move an out-of-scope criterion to a task whose Gate contains it.

Beginning with v0.23, every active execution runbook carries one
machine-readable declared-scope table. `cycle-check` applies two distinct
sub-rules and their evidence must not be conflated:

- The **static sub-rule fires at activation**. A release disposition must
  declare patterns covering every enumerated release-authority path.
- The **diff sub-rule first fires at the per-task gate after a changed commit**.
  Its range is the activation commit **exclusive** through `HEAD` **inclusive**
  (`activation..HEAD`), so the activation diff itself is empty. The exact
  standing always-allowed set is `STATE.md`, the active progress record, and
  the active runbook. `AGENTS.md` is deliberately not standing and must be
  declared by any cycle that changes it.

The matcher is repository-relative and glob-based. A declared release authority
wins over `forbid` so R-CLOSE can change version authorities; in v0.23 this
weakens the production-source prohibition for exactly
`shell/intel_shell/app.py`, whose non-version diff therefore still requires
human classification. Closed runbooks before v0.23 are immutable and are never
retrofitted with a scope table.

Beginning with v0.23, trigger freshness is executable over exactly two live
tables: `ARCHITECTURE.md`'s **Dated operational-residual dispositions** and the
active runbook's **Deferred means deferred** table. Only rows whose trigger cell
is neither empty nor `none` are governed. Each such row must carry a valid
ISO-date in its own measured-observation cell. Beginning with v0.28, that cell
must also name the literal active cycle resolved from the active declaration.
A dated negative observation is sufficient for an event-shaped condition (for
example, no operator server session occurred); the checker verifies the
presence, date, and active-cycle identity of the measurement, not the truth of
an external event. Date freshness is v0.23-forward, cycle identity is
v0.28-forward, and neither retrofits closed historical runbooks.

Beginning with v0.29, a trigger-bearing governed row's measured cell carries
the latest measurement available when the cycle closes, not whichever earlier
task first wrote the row. If a later measurement exists, an earlier value is
not current; if no later measurement exists, do not invent or project one.
Preserve the earlier measurement in its dated task or progress record and
forward-correct the live row explicitly, so neither an increase nor a decrease
can be selected opportunistically.

Beginning with v0.32, the published-release divergence count is scoped to a
publication epoch. A successful authorized publication resets the consecutive
closed-cycle count to zero at that published closing commit. A later measured
runtime-behaviour difference starts a fresh count at the first subsequent
closed cycle whose unpublished distance carries that difference; it never
inherits cycles from before the publication. Documentation, evidence, and
lifecycle-only changes, a difference already included in the published commit,
and a closed cycle with no measured runtime-behaviour difference neither start
nor continue the count. A public-surface change still fires the trigger
immediately, independent of the consecutive-cycle count. Runtime classification,
trigger firing, and the publication-reset fact remain dated operator
adjudications: `cycle-check` enforces their record freshness and identity, not a
self-reported truth it has no independent artifact to contradict.

Beginning with v0.30, the content binding is deliberately narrower than the
date/cycle-identity rule. It covers only the `ARCHITECTURE.md` subject beginning
`review-export size and retention bound`; every other governed row remains
explicitly out of content-binding scope because its heterogeneous external
measurement has no common repository authority. The covered row carries
`Governed review-export bytes: \`<digits>\`` and its visible `export of **N
bytes**` figure must agree. The active cycle's progress record supplies the
independent authority through append-only fields of this exact form:

```
- governed review-export measurement: tree=`<40 hex>`; bytes=`<digits>`
```

At every closed tree checked by `cycle-check`, the row must equal the last such
governed progress field already visible in that exact tree, regardless of
whether the value increased or decreased. This is symmetric: neither a later
audit child nor an earlier implementation parent may be selected
opportunistically as the evaluation point. While the cycle is open, a missing
field takes the named `exempt-open-empty-progress` path because no
latest-at-close referent exists yet; a present field takes
`exempt-open-latest-at-close` because later measurements may still arrive.
These exemptions are reported by `cycle-check` and expire at close. A closed
cycle with no governed field is an error, not a vacuous pass.

The governed figure is measured on the last tree measurable when the covered
row is written. Under a release close, closing child `C` may carry a governed
measurement of its already-existing release parent `R`, and the row in `C`
must agree with that field. Under a no-release close, the closing implementation
tree keeps the row bound to the latest governed field it can already see. The
separate append-only audit child records the later closing-tree measurement
under this exact non-governing form:

```
- cycle-ending review-export audit: closing_tree=`<40 hex>`; bytes=`<digits>`; audit_delta=`<signed digits>`
```

Exactly zero or one such audit field may exist, only after the last governed
field and only once the cycle is closed. That optionality is deliberate. When
an operator actually measures the closing tree and its delivered export differs
from the governed figure, the audit field is the truthful disclosure and its
`bytes` value and `audit_delta` are backed by the operator-local command and
captured output. An absent field makes no claim that the delta was zero or that
the tree was measured: `cycle-check` cannot generate the export, so it has no
independent fact with which to distinguish an unmeasured omission from a true
zero. Requiring the field only when a self-reported difference exists would be
a self-report dressed as a control; requiring it unconditionally would claim a
measurement the lifecycle entry point does not perform. A cycle runbook may
independently require its own audit, as v0.32 does. When present,
`cycle-check` parses the field, enforces its position, reports
`bound-with-cycle-ending-audit`, and deliberately does not treat it as a newer
governed measurement. This avoids asking a record to measure a tree containing
itself while keeping both the closing implementation tree and its audit child
bound. The append-only audit record's own byte contribution remains the one
necessarily undisclosed delta; adding another field would recreate the fixed
point.

At every checked tree, `cycle-check` also compares the row's written figure
against the single `MAX_EXPORT_BYTES` authority imported from
`tools/export_check.py`. That automated check constrains the repository's
written claim and explicitly does **not** create or measure an export.
Operator-local `./run export-check` remains the real-byte, retained-set, and
excluded-content control.

Beginning with v0.28, both governed tables must contain at least one
trigger-bearing row. Every trigger-bearing subject in the immediately prior
execution runbook must remain in the active deferral table or appear in an
active **Deferred completions** table with a valid ISO-dated completion. The
prior runbook is derived from the versioned execution-runbook set; it is never
named as a fixed cycle in the checker.

Every active runbook's **Deferred means deferred** table must assign each
non-`none` action to a named, existing `Step N`; an asserted action without its
discharging step is invalid. Every runbook that changes the release commit must
contain a **RE-MEASURE** step that measures that release commit.

Every RE-MEASURE comparison between local and hosted shell tests uses the
machine-readable population summaries and `tools/test_population.py`.
Equivalence means equal collected populations, local passed equal to hosted
passed plus hosted `on_site` skips, and every skip named with its node id,
declared reason, and `on_site` marker. An unmarked or unnamed skip is a failure.
The number written in a record must be the comparator's derived output, never a
figure transcribed from a log.

1. **Read** the task's objective and decision gate in
   the active cycle's execution runbook named in the declaration above.
2. **Check the gate first.** If it trips, record and stop (§1).
3. **Implement** the change.
4. **Run every acceptance criterion** listed for the task and **capture the
   output** — command text and result. Self-verify; do not ask the operator to
   run anything you can run yourself. An acceptance criterion phrased as a
   repo-wide absence must be discharged by a registered, self-testing
   `invariant-scan` rule with an executable `fail_before`, not by inspection.
5. **Run `./run golden`** (§6). Its exit code defines whether the regression
   anchor held. If it moves by even one document / id / distance on a task meant
   to preserve it, **stop** — that is corpus corruption, not progress.
6. **Update `STATE.md`**: the header line (test counts, warning status, golden
   E2E status) and the relevant section, with what you **measured**, not what you
   hoped. Correct any prior claim you found to be false.
7. **Check the box** for the task in the active cycle's execution runbook.
8. **Commit the task implementation** — one task per implementation commit.
   Never combine a lint gate with a lint fix, or a formatting diff with a
   behavior change; that is how a real change hides inside noise.
9. **Append the active progress-log entry after that commit exists**: date,
   task id, owner, measured result, each acceptance criterion pass/fail,
   golden-E2E delta, and the real 7–40 character implementation commit hash.
   Run `./run progress-check`, then commit that append-only entry in a separate
   audit-record commit before starting the next task. Do not amend an entry to
   contain its own commit hash: changing commit contents changes the hash, so
   that proposed self-reference cannot be true.

**Public value-domain change (2026-07-30).** A release that adds a value to, removes a value from, or redefines a value in the domain of any field already serialized in a `/v1/*` response body takes a **minor** version, even when no route, field name, field type, or body shape moves. Patch is available only when the set of values every public field can take is unchanged. A consumer's exhaustive handling of a field's values is part of the contract it was given. Stated symmetrically so a later contraction is not argued again. This criterion is prose adjudicated at R-CLOSE; no executed control enforces it.

### Cycle-ending hosted-verification rhythm — accepted 2026-07-29

The operator accepts that the final append-only audit record of each cycle is
written after publication and therefore is hosted-unverified when written. It
is verified at the following publication, when it becomes an ancestor of the
candidate and release commit exercised by hosted CI. This is the intended
rhythm, not a defect to route around; the consequence is that the latest
cycle-ending audit commit remains supported by its required local gates and
append-only evidence until that following publication occurs.

### R-CLOSE — tagged-closing release protocol selected 2026-07-29

Releases through v0.15.5 used the prior closing-record shape and retain its
historical validation semantics. v0.15.6 and every later release use R-CLOSE's
two-commit tagged-closing protocol. The release commit `R` carries the release
edits and version authorities but is not tagged. Its immediate child `C` checks
R-CLOSE's box and carries the complete closing record. That record names
`Cycle closed`, the dated `Release disposition`, `Release`, and `Release commit:
R`; it must not contain an `Annotated tag object` field. The closing record
cites already-authenticated candidate hosted evidence, because evidence from
publishing `C` cannot exist in `C`.

The annotated release tag targets `C`, not `R`. Before any ref movement,
`cycle-check` verifies that `R` is `C`'s immediate parent and that `C`'s tree
contains the closed runbook with the same release name and release-commit hash
and no tag-object field. `STATE.md`'s live header in `C` asserts the knowable
release commit `R`; neither the tag-object hash nor `C`'s own hash may be
required in that tree. `C` and its annotated tag are pushed atomically.

The first commit after `C` records the post-push result in a dated `STATE.md`
body append with these exact contiguous fields:

```
- **Post-push verification date:** YYYY-MM-DD
- **Post-push release:** `vX.Y.Z`
- **Post-push annotated tag object:** `<40 hex>`
- **Post-push closing commit:** `<40 hex>`
- **Post-push hosted run:** `<digits>`
```

At the tagged `C` checkout, `cycle-check` accepts the release-commit assertion
while directly verifying the annotated tag, parent, and tagged tree. On every
descendant of `C`, it additionally requires exactly one complete post-push
record for that release and checks the recorded tag object and closing commit
against Git. The post-push run confirms the published head; it is forward
evidence and is not what closes the cycle.

## 6. Golden end-to-end (run after every task; it must not drift silently)

The v0.10 golden pipeline is the regression anchor. **`./run golden` is the
authoritative, executable definition; the prose below is a human summary. If
they ever disagree, the command's named assertion failure is the finding — do
not edit the assertion to bless the drift.** Its current eleven-check expected
outcome:

> acme corpus 13 → 12 analyzed; `techwire::tw-004` dropped for `osdaily::osd-004`
> at hamming 12; DeepSeek RISING z = 10.0; a re-run adds 0; quant-desk sees 1
> document; `/v1/ask` yields 4 citations with one of the near-dup pair suppressed.

A task meant to be output-preserving (T3, T6, the harness work) must leave this
**byte-identical**. A task meant to change it (T1's `/attest` may redact) must
state the new expected value and update this section. Either way: the number in
`STATE.md` is the one you measured this run.

## 7. When you are blocked

Two blocks are legitimate and cannot be engineered away; everything else you
handle yourself:

- **No reachable LLM endpoint / no key (T4).** Defer per its gate. Do not declare
  it done against the mock.
- **Port 8788 held by a foreign process.** macOS has bitten this repo before (an
  orphaned `cored` in `.Trash` ate 34 minutes). The harness now detects it and
  prints the exact `lsof` / `kill` command; surface that to the operator rather
  than guessing. Run `./run down` and check `lsof -i :8788` before a harvest.

Before any live harvest, run `./run verify-artifacts`. A bare
`./run harvest-arxiv` resolves to a fresh
`data/live-<UTC-timestamp>-<pid>.db` and prints it before the first request.
`config/protected-artifacts.json` is the single provenance authority for
`data/core.db` and `data/live-smoke.db`; the harness must refuse both as
live-harvest targets. Protected artifacts are immutable evidence. Do not bypass
that refusal—choose the fresh path it prints.

Manifest schema v2 has two disjoint containers:

- **`artifacts[]`** is for protected SQLite archives. Each entry requires the
  SQLite corpus-fact `expected` shape and carries the executable append-only
  `admission` chain. A new artifact hash requires a newly appended record whose
  `prior_sha256` chains to the preceding record and whose fields name the task,
  date, captured wire command/output reference, operator approval, and
  retroactive status. Never edit or replace an earlier admission record.
- **`pinned_files[]`** is for immutable bytes beneath `evidence/` or
  `observations/`, plus exact registered structural-archive and authorization
  paths. Each entry carries its applicable grade and byte facts, and **forbids
  `admission`**. The structural-archive registry is exact rather than a prefix:
  v0.33 registers only `docs/state-archive/STATE-through-v0.28.md`, so another
  archive name cannot silently inherit its pin grade.

A task that requires a byte to be pinned must name `artifacts[]` or
`pinned_files[]`. A requirement that neither container can express is an
author-side defect to record and correct, not a condition to work around. The
fifth and sixth unsatisfiable author-side rules recorded in v0.26 are the two
data points that caused this rule; neither historical disposition is reopened.

Run both commands before proposing a manifest change:

```
python3 tools/evidence_artifacts.py validate
./run verify-artifacts
```

The first command rejects incomplete or broken admission chains; the second
also measures the actual artifact bytes and corpus facts. CI runs the schema
validation independently. The two existing v0.10/A2 records are explicitly
retroactive and cite the already-recorded wire and B0 evidence; they are not
fresh admissions or fresh wire runs.

The container-shape fixtures prove that this description matches the validator
today, including rejection of `admission` under `pinned_files[]` and rejection
of an `artifacts[]` entry without `expected`. They do not prevent a later
validator change from drifting away from the description; a cycle changing the
validator must update and re-execute the contract. v0.27 forbids changing
`tools/evidence_artifacts.py`, so that limitation is controlled for this cycle.

Record every block precisely. A block is a non-result, never a pass.

## 8. Server model profiles — standing operator authorization

The marker-delimited policy below is byte-identically mirrored in
`docs/intel-platform-OPERATIONS.md` and enforced by invariant R6.

<!-- MODEL_PROFILE_AUTHORITY:START -->
**Server model-profile authority — L1 now, L2 scheduled.** The operator selected
L1 on 2026-07-27 because it is offline-testable and makes the current controller
refuse remote commands outside a compiled construction allowlist. Codex may run
`./run models status|intel|athenaeum|athenaeum-bulk|stop` without a per-command
authorization request, including launching that exact command in Terminal.app
when the Mac-created port-2222 bridge is absent.

Every remote command produced by `tools/model_profiles.py` passes one allowlist
before SSH. `docker start|stop|restart` may name only `intel-gen`,
`intel-embed`, `athenaeum-gen`, `athenaeum-embed-gpu`, and
`athenaeum-embed-cpu`; `docker ps` and `docker ps -a` may inspect inventory;
`curl` may query only `/health` or `/v1/models` on loopback ports 8080–8082;
and the remaining exact read-only commands are `nvidia-smi`, `ip -br address`,
and `git status`. Anything else raises `ProfileError` before SSH. The `run` and
`tools/model_profiles.py` bytes are hash-pinned in
`config/protected-artifacts.json`.

The authorization also covers creating, checking, reusing, and cleanly exiting
the documented shared SSH bridge and intel/Athenaeum model-tunnel control
sockets, plus local `lsof` inspection of their documented forwards. Before a
switch, Codex inspects and reports the actual named-container state. After a
switch, it reports server-local and forwarded health. A missing named container,
foreign listener, health failure, or partial/overlapping GPU state is a refusal;
`models stop` is the authorized safe recovery for the last state and may stop
all five named containers plus close only the managed tunnels and bridge.

Everything else on the server remains ask-first, especially `docker run`,
`docker rm`, `docker rmi`, `docker pull`, any image or tag change, edits under
`/data/models`, package installation, reboots, and irreversible actions. The
routine controller never creates, removes, or recreates a container, and never
removes an image, model, repository, or configuration.

L1 cannot prevent an agent that edits `tools/model_profiles.py` from changing
what runs; only L2 can make the server authorization survive an edited
controller. L2 is scheduled for the next operator-authorized
server-administration session and must be installed and refusal-tested before
any additional model profile is admitted: an `authorized_keys`
forced-command wrapper will make the server reject commands outside the same
lifecycle set.
<!-- MODEL_PROFILE_AUTHORITY:END -->
