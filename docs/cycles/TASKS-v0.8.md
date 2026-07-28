# TASKS-v0.8 — work order

> **Closed-cycle status correction — 2026-07-24.** The body below is preserved
> as historical v0.8 rationale, not live status or instructions. T4 later
> closed with a 6/6 uninterrupted real-model run; T1 shipped core `/attest` for
> the trusted shell path (A4 subsequently recorded that an arbitrary shell
> rewrite can still bypass it); and the protected archives now contain 1,764
> and 2,600 documents. The golden fixture still analyzes 12 documents. Those
> facts supersede the body's deferred-T4, stale-HC1, and
> 12-document-corpus statements without rewriting the closed rationale.

**Entering state:** v0.7.0. 75 Rust tests, 69 shell tests, 0 warnings on both
build configurations. `robots.txt` is fetched for real (v0.7/T2); CI exists and
enforces `--locked`, `-D warnings`, the `--features net` path, and the 1.78 MSRV
floor (v0.7/T4). Golden E2E unchanged since v0.5.

**The one sentence that matters:** *this platform has never touched the outside
world.* Every document it has ever ingested came from a fixture on disk; every
model response it has ever seen came from a mock we wrote ourselves. The code is
well tested against itself. It is **unfalsified against reality**, and the two
places that hurt most are a licensing invariant (T1) and the harvest (T2).

Tasks are dependency-ordered. Each carries a **decision gate**: a condition that,
if tripped, means *stop and record*, not *push through*. The gates have earned
their keep — they are why `feed-rs`, `texting_robots`, and LSH are all correctly
*not* in this codebase.

---

## T1 — Enforce HC1 on `/v1/ask` structurally, not by prompt [P0, core + shell]

**This is the highest-priority item in the project and it is not the harvest.**
It is a licensing exposure that is live today, in code that already ships.

**The problem.** STATE §2.1's headline claim is that license gating lives in the
Rust core, so *no shell rewrite can leak gated text*. That is true for `/view`,
`/search`, and `/brief`. It is **false for `/v1/ask`**:

- The model is deliberately handed the **full bodies** of IndexOnly documents
  (`prompts.BODY_CAP = 800` chars each). This is defensible and should stay —
  reading gated text as analysis context is not redistribution.
- The model's answer is then returned to the caller **verbatim and uninspected**
  (`app.py`: `"answer": answer`).
- The only thing between a gated source sentence and a public API response is
  **one sentence in a system prompt** (`ASK_SYSTEM`). A prompt is not an
  invariant. The leak vector is not a shell rewrite — it is the model's own
  output, and no core invariant touches it.

**And the existing test cannot fail.** The only model in the suite is
`tools/mock_openai.py`, a deterministic double *we wrote*, which returns a
templated answer and is structurally incapable of reproducing source text. The
HC1 spot-check on `/v1/ask` has never been run against anything able to violate
it. That is the project's recurring failure — *a claimed property that nothing
executes* — except that this time the property is a licensing one.

**Where it lands, and why there.** In **core**, behind a new endpoint (suggested:
`POST /attest` → `{answer, context_doc_ids}` ⇒ `{clean_answer, violations[]}`).
Not in the shell, for exactly the reason §2.1 gives: the shell is the freely
rewritable layer, and an invariant that a rewrite can delete is not an invariant.
Core already holds the gated bodies in SQLite, so it needs nothing new to do
this. **The core still never calls an LLM** — it inspects a string it is handed.
That prohibition is not weakened.

**Mechanism.** Normalized token n-gram overlap: shingle the answer and every
IndexOnly context body, and treat any shared n-gram as a violation. Then either
redact the span or refuse the answer — pick one and make it structural.

**Decision gate — `n` must be MEASURED, not chosen.** Too small and every answer
trips on ordinary phrasing ("the model was trained on"); too large and a leaked
sentence slips through. Sweep `n` over the real corpus: for each `n`, measure the
false-positive rate on answers known to be clean and the true-positive rate on
answers seeded with verbatim source sentences. **If no `n` gives a clean
separation, stop** — do not ship a check with a false-positive rate that will
train operators to disable it. Report the curve either way. (Anticipate `n` ≈ 8;
do not assume it.)

**Testing objectives:**
- **Give the test double the ability to fail.** Add a `--leak` mode to
  `tools/mock_openai.py` that deliberately reproduces a verbatim sentence from
  the context it was given. A guard tested only against a double that cannot
  violate it is not tested.
- A core unit test: an answer containing an IndexOnly sentence ⇒ violation.
- A core unit test: an answer containing a *CcBy* sentence ⇒ **no** violation
  (the gate is about license, not about quoting).
- A core unit test: a legitimate analytical answer is passed through unmangled.
- A shell test: `/v1/ask` with the leaking mock ⇒ the public response does **not**
  contain the gated text.
- Golden E2E: `/v1/ask` output on the existing question is **unchanged** (4
  citations, one of the near-dup pair suppressed).

**Done when** a model that *tries* to leak gated text cannot get it through the
public API, and the test proving that runs in CI.

---

## T2 — The first live arXiv harvest [P0, ops — COMPLETE]

**Completed on the live wire 2026-07-23.** The v0.7.1 per-source robots fix
cleared the gate, v0.7.2 made the run bounded and observable, and the v0.8
atomic-page repair made interruption durable. Two capped real arXiv runs now
prove that a process restart resumes from the stored token instead of restarting
page 1.

History, retained so the closure remains auditable:

- **v0.7.0 → blocked at reachability:** arXiv had migrated `export.arxiv.org/oai2`
  → `oaipmh.arxiv.org/oai` (301). Config now points at the canonical host.
- **v0.7.1 → blocked at robots:** `oaipmh.arxiv.org` serves no robots.txt (404);
  the fail-closed default blocked a cooperative source. Per-source
  `robots_on_missing: "allow"` fixed it (STATE §2.12).
- **v0.7.2 → reached the wire, then ran 26 minutes silent:** unbounded harvest of
  the entire `set=cs`, no request timeout, no progress output. All three fixed —
  `max_pages` cap, 60s/15s timeouts, per-page progress (STATE header). The smoke
  test now injects a 3-day window + 3-page cap and streams progress.

**Completion evidence:** run 1 fetched 1,300 real records and left a non-NULL
token ending in `skip%3D522`. After stopping and restarting `cored`, run 2's
first request carried that exact token, added the next 1,300 records, and left a
new token ending in `skip%3D88`. Both pages parsed without an observed error.
The real robots disposition was captured; arXiv did not issue a 503/Retry-After.

**2026-07-22 correction:** the capped-run path itself was defective: it
checkpointed the next token and then unconditionally completed, clearing it.
That direct bug and the deeper split-write window are repaired. Each parsed
page now commits documents, canonical ids, next token, and pending high-water in
one SQLite transaction; injected-failure and reopen tests execute those guards.
The first permitted live reproof timed out with zero documents and no cursor
row, so it was correctly recorded as blocked. The later 2026-07-23 two-run wire
evidence in the execution runbook closes that gate without weakening it.

**Closure:** exact commands, tokens, counts, regression results, and preserved
log locations are recorded in `STATE.md §8` and `PROGRESS-v0.8.md`. The decision
gate remains the rule for future changes: "reached the wire" is not resume
evidence unless the stored token is observed in the next process's first request.

---

## T3 — Persist the SimHash fingerprint [P1, core — measured, output-preserving]

The swap v0.7/T5's measurements actually justify, and the one that **replaced**
LSH on the T8 trigger table after LSH was built and rejected (STATE §6c).

`simhash(title + body)` is a pure function of the document, and `dedup_near`
recomputes it for **every document on every call** — while T9.1 runs that pass on
every ingest that adds rows. Measured (`cargo run --release -p intel-extract
--example dedup_bench`): it is **85% of dedup cost at n = 10k**, versus **14.6%**
for the quadratic scan everyone assumed was the problem.

Store it as a column at ingest; have `dedup_near` *take* fingerprints rather than
compute them.

**Decision gate — the output must not move, at all.** Same fingerprints ⇒ same
drops ⇒ same canonical ids. If the golden E2E changes by one document, one
`kept_id`, or one hamming distance, **stop**: a faster dedup that silently
changes which document is canonical is corpus corruption, not an optimization.
(That is the same gate that correctly killed LSH.)

**Testing objectives:** golden E2E byte-identical; a test that a stored
fingerprint equals a freshly computed one; a migration path for archives written
before the column existed (**check whether such an archive exists before building
the migration** — in v0.7 the equivalent tool was correctly *not* built because
no such archive did).

---

## T4 — Point the LLM at a real endpoint [P1, shell — DEFERRED: embeddings unavailable]

Carried from v0.7/T3. `tools/verify_llm.py` already runs the whole checklist in
one command: embeddings backfill, fusion no longer BM25-only, `retrieval.notes`
clean. T4C made the command self-contained on a fresh fixture core and split
chat from embedding configuration.

**Decision gate:** no reachable OpenAI-compatible embedding endpoint ⇒
**defer**; do not declare it done against the mock or BM25-only retrieval. On
2026-07-23 the operator's LAN server returned 501 from `POST /v1/embeddings`,
DeepSeek returned 404, and a later LAN retry returned `No route to host`. No
real embedding backfill passed, so T4 remains deferred. A subsequent
split-provider run used DMXAPI for embeddings: that role returned 503 twice,
while the independent LAN-chat/public-HC1 leg passed once with 4 IndexOnly
citations and no gated overlap. The verifier correctly reported 3/5, not a
pass. Chat and embeddings may use different providers through `LLM_CHAT_*` and
`LLM_EMBED_*`; every required leg must pass in the same run. T4H makes that
ordering executable: embedding backfill and fusion are prerequisites, so either
failure stops before chat/public HC1. Per-role positive timeouts bound each
provider call; a faster, cleaner 503 is still a T4 failure.

**This task and T1 are worth far more together than apart.** T1 builds the guard;
T4 supplies the first model capable of tripping it. Once both are done, run the
HC1 spot-check for real: ask a question whose best evidence is an IndexOnly
document and confirm the public answer never reproduces gated text — with a model
that *could* have.

---

## T5 — Re-gate robots on the final origin after redirects [P1, core — CONFIRMED LIVE]

**No longer hypothetical.** The 2026-07-19 on-site harvest hit this directly:
`export.arxiv.org/oai2` **301-redirects** to `oaipmh.arxiv.org/oai`, so a request
gated against `export.arxiv.org`'s robots.txt would fetch documents from
`oaipmh.arxiv.org`, whose policy was never read. reqwest follows up to 10
redirects silently (no redirect policy is set on either `Client` in
`crates/ingest/src/net.rs`), and RFC 9309 scopes policy per-origin, so this is a
real compliance gap.

**Worked around for arXiv in v0.7.1** by pointing config at the canonical
`oaipmh.arxiv.org/oai` (no redirect), which is why it is P1 and not P0 — but the
gap is live for any *other* source that redirects cross-origin, so it must be
fixed before a second live source goes up.

**Two viable designs — pick deliberately, do not default:**
1. `.redirect(Policy::none())` and follow redirects *manually*, re-running the
   robots gate on each hop. Explicit, more code, no surprises.
2. Keep automatic redirects, then compare the response's final URL against the
   requested one and, if the origin changed, re-gate and **discard the body** if
   the new origin disallows it. Simpler, but it means we have already made a
   request the new origin's policy might have forbidden.

Design 1 is the honest one. Design 2 fetches first and asks permission second,
which is the thing this whole subsystem exists to avoid.

**Testing objectives:** a fake fetcher that 302s cross-origin, asserting the
second origin's `robots.txt` is fetched and honored; a same-origin redirect that
does **not** trigger a redundant fetch; the fixture path still issues **zero**
fetches.

---

## T6 — Turn on `clippy` + `rustfmt` in CI [P2, ci — cheap, 20 minutes]

Entering v0.8, this was already a real CI job, but it was **report-only** via
`continue-on-error: true`; the earlier claim that it was commented out was
false. B0 ran both tools and found one `items_after_test_module` diagnostic plus
rustfmt diffs in 13 files. T6 fixed those findings in commit `097b017`, then
promoted the now-clean job to blocking in a separate commit.

```
rustup component add clippy rustfmt
cargo clippy --workspace --locked --all-targets -- -D warnings
cargo fmt --all -- --check
```

**Decision gate:** if either reports findings, **fix them in a separate commit
first**, then promote the job. Do not land a lint gate and a lint fix together —
that is how a formatting diff hides a behavior change. **Satisfied in T6:** both
commands pass on pinned Rust 1.91.1; the two intentional
`unnecessary_map_or` allows remain because their replacement requires Rust 1.82,
above the offline 1.78 floor.

---

## T7 — Robots cache: single-flight concurrent misses [P2, core — small]

Two simultaneous first-requests to the same origin can both fetch
`/robots.txt` (STATE §5). Bounded and harmless today — the limiter still spaces
them — and it stays that way until there is a second concurrent harvest.

**Decision gate:** same trigger as Postgres. If there is still exactly one writer,
**skip it and say so.** Do not add a single-flight lock to a system with no
concurrency.

---

## Still deferred, with the gate that defers them

- **Multi-host seam hardening (UDS / mTLS).** Core and shell still run on one
  host (`cored` binds `127.0.0.1:8788`). `CORE_TOKEN` exists on both sides. Do
  not build speculative mTLS.
- **Postgres / pgvector / tantivy.** Postgres is a **concurrency** trigger (a
  second writer), not a size one, and may never fire. pgvector is worth it only
  above ~10⁵ docs — below that, brute-force cosine is *faster* and exactly
  correct. See `docs/T8-scale-design-note.md`.
- **Materialize `/view`.** Precondition is measurable warm-up cost. The corpus is
  12 documents.

---

## Hard constraints (carried; HC1 and HC13 are the ones this cycle turns on)

- **HC1 — no gated text on a public path.** *Currently violated in principle on
  `/v1/ask`.* T1 exists to make this structural rather than aspirational.
- **HC2** — entitlements decided in shell, sector filter *also* in core SQL.
- **HC3** — the core never calls an LLM. T1 does not weaken this: core inspects a
  string it is handed; it does not generate one.
- **HC8** — politeness is process-scoped, not request-scoped (v0.7 moved
  `HostLimiters` and `RobotsCache` into `AppState` for exactly this reason).
- **HC12** — never delete the lock to "fix" a resolution error; understand it.
  And: **the lockfile format is part of the MSRV surface.**
- **HC13 — fixtures prove the state machine, not the wire.** Three separate bugs
  have now come from believing otherwise.
- **A test double that cannot fail is not a test.** New, and earned: see T1.

## Global definition of done

Golden E2E unchanged (acme 13 → 12 analyzed, `techwire::tw-004` dropped for
`osdaily::osd-004` at hamming 12, DeepSeek RISING z=10.0, re-run +0, quant-desk
1 doc); 0 warnings on `--workspace` **and** `--features net`; all Rust and shell
tests green; MSRV floor still 1.78; `STATE.md` updated with what was *measured*,
not what was hoped.
