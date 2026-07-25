# AGENTS.md — operating contract for autonomous agents on intel-platform

This file governs how an autonomous coding agent (Codex, or any successor) works
in this repository. It is not a style guide; it is a set of constraints that
exist because each one was learned the expensive way. Read it before touching
anything, and re-read the two documents it points at:

- **`ARCHITECTURE.md`** — authoritative for *invariants* (what must be true of
  the system). These change rarely and never casually.
- **`STATE.md`** — authoritative for *current status* (what is true right now).
  You update this after every task; see §5.

**Active cycle:** v0.10

Task work for this cycle is ordered in **`TASKS-v0.10-EXECUTION.md`**. Every
completed step is logged in **`PROGRESS-v0.10.md`**. The finished v0.8,
v0.8.1, v0.8.2, and v0.9 execution runbooks append their dated closing records;
their progress logs and the full original task documents remain preserved as
historical rationale. `./run cycle-check` enforces this declaration and those
closed-cycle records.

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
- **Fixtures prove the state machine, not the wire (HC13).** A green fixture test
  is evidence about parsing and control flow, never about what a real server
  does. Live-path claims require a live run.
- **Report what the wire actually did.** "Blocked", "should work", and "reached
  the endpoint" are non-results until documents land and you can count them.
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
2. Record the measurement that tripped it in `STATE.md` and `PROGRESS-v0.10.md`.
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

1. **raises the MSRV floor** (offline build must stay ≥ 1.78; watch for the
   `icu_*` 2.2.0 chain via `idna` / `idna_adapter`, which declares 1.86 and lives
   in the *offline* graph through `intel-compliance`), or
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

# lint (clean and blocking in CI since T6)
cargo clippy --workspace --locked --all-targets -- -D warnings
cargo fmt --all -- --check

# shell (holds the entitlement/licensing invariants the Rust tests do not)
pip install -r shell/requirements.txt
PYTHONPATH=shell python3 -m pytest shell/tests -q
```

Rebuild the local Python 3.12 lane in the repository's already-ignored
`.venv/` tree; do not inherit a random `/private/tmp` environment:

```
python3.12 -m venv --clear .venv/py312
.venv/py312/bin/python -m pip install -r shell/requirements.txt
PYTHONPATH=shell .venv/py312/bin/python -m pytest shell/tests -q
```

This command was executed on 2026-07-24 with Python 3.12.13 and resolved the
following environment. It is a dated measurement, not a guarantee:
`shell/requirements.txt` declares floors rather than pins.

```
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

`RUSTFLAGS="-D warnings"` is the standing rule for the offline and net builds:
**0 warnings is a gate, not an aspiration.** ("0 warnings" means *rustc*
warnings; clippy is an independent blocking gate.)

## 5. The per-task workflow — status is updated in real time

You do **not** batch status updates. After each task, in order, before starting
the next:

1. **Read** the task's objective and decision gate in
   `TASKS-v0.10-EXECUTION.md`.
2. **Check the gate first.** If it trips, record and stop (§1).
3. **Implement** the change.
4. **Run every acceptance criterion** listed for the task and **capture the
   output** — command text and result. Self-verify; do not ask the operator to
   run anything you can run yourself.
5. **Run `./run golden`** (§6). Its exit code defines whether the regression
   anchor held. If it moves by even one document / id / distance on a task meant
   to preserve it, **stop** — that is corpus corruption, not progress.
6. **Update `STATE.md`**: the header line (test counts, warning status, golden
   E2E status) and the relevant section, with what you **measured**, not what you
   hoped. Correct any prior claim you found to be false.
7. **Check the box** for the task in `TASKS-v0.10-EXECUTION.md`.
8. **Commit the task implementation** — one task per implementation commit.
   Never combine a lint gate with a lint fix, or a formatting diff with a
   behavior change; that is how a real change hides inside noise.
9. **Append the `PROGRESS-v0.10.md` entry after that commit exists**: date, task
   id, owner, measured result, each acceptance criterion pass/fail, golden-E2E
   delta, and the real 7–40 character implementation commit hash. Run
   `./run progress-check`, then commit that append-only entry in a separate
   audit-record commit before starting the next task. Do not amend an entry to
   contain its own commit hash: changing commit contents changes the hash, so
   that proposed self-reference cannot be true.

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
that refusal—choose the fresh path it prints. Admit a new protected artifact
only through an explicit task with captured wire evidence and operator review.

Record every block precisely. A block is a non-result, never a pass.
