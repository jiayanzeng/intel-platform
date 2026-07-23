# intel-platform (v0.6.2 — core-shell)

A multi-sector intelligence gathering and analysis platform, split into a
**Rust core** (the engine) and a **Python shell** (the product), joined by a
minimal internal JSON API. Sources are legal, non-gatekeeper channels only
(OAI-PMH harvesting, RSS, bulk/open datasets, compliant crawling, client
uploads). Clients subscribe to sectors; the shell decides entitlements, the
core enforces them.

**The design premise is unchanged: the moat is the derived layer, not the
inputs.** What changed in v0.4 is *where things live*:

```
┌──────────────────────── SHELL (Python, hot-editable) ────────────────────────┐
│  public API (FastAPI)   auth / API keys / subscriptions   LLM chat+embed     │
│  prompts (ASK_SYSTEM…)  brief rendering & product copy    pipeline flow      │
└───────────────────────────────┬──────────────────────────────────────────────┘
                     minimal JSON API on 127.0.0.1:8788
┌───────────────────────────────┴───────────────────── CORE (Rust, stable) ────┐
│  ingest connectors + compliance gate      SimHash dedup     gazetteer scan   │
│  burst z-scores / corroboration / PMI     SQLite+FTS5       BM25+cosine+RRF  │
│  LICENSE GATING (snippets & excerpts)     sector filtering in SQL/memory     │
└───────────────────────────────────────────────────────────────────────────────┘
```

The split rule: **the core owns math, throughput, and invariants that must
be impossible to forget; the shell owns everything a product person might
want to change this afternoon.** Editing a prompt, rewording the brief,
changing the citation style, adding an endpoint, swapping the LLM provider,
restructuring subscriptions — all shell-only, no recompile. The core's ten
endpoints are the whole contract.

## Who owns what

| Concern | Layer | Why |
|---|---|---|
| Fetching, XML parsing, robots.txt discovery + rate limits | core | throughput + compliance invariant |
| SimHash dedup (before ALL statistics) | core | signal-honesty invariant |
| Gazetteer scan, discovery, bursts, PMI graph | core | CPU-bound hot loops |
| SQLite archive, FTS5 BM25, vector cosine, RRF | core | data + math |
| **License gating** (snippets, evidence excerpts) | **core** | must be unforgettable: the shell renderer never even receives gated text |
| **Entitlement decision** (key → client → sectors) | **shell** | business state (billing, tiers, trials) |
| Sector *filtering* given an explicit list | core | defense in depth: a shell bug can mis-grant sectors, never bypass filtering |
| LLM chat + embeddings, all prompts | shell | provider/prompt churn is product iteration |
| Brief rendering, API shapes, pipeline flow | shell | product voice |

## The core API contract (all of it)

`cored` binds `127.0.0.1:8788` (env `CORE_BIND`); optional shared secret via
`CORE_TOKEN` → `x-core-token` header. Sector lists are always explicit.

| Endpoint | Does |
|---|---|
| `GET /health` | liveness + archive size |
| `GET /sectors` | configured sectors/sources/licenses |
| `POST /ingest {sectors, sources?}` | fetch through the compliance gate, idempotent append; optional `sources` runs exactly those source ids (each validated against `sectors`) for true per-source cadence |
| `GET /view?sectors=` | the full intelligence view: dedup drops, signals with **license-gated hydrated evidence**, named PMI edges, discovery queue, `kept_doc_ids` |
| `GET /search?q&sectors&limit` | BM25 hits, snippets gated in the store layer |
| `POST /retrieve {q, sectors, k, model?, query_vector?}` | hybrid BM25 + cosine + RRF; near-dups suppressed at context assembly; returns full-body context docs + diagnostics |
| `GET /embeddings/missing?model` | backfill work queue |
| `POST /embeddings {model, items}` | store shell-computed vectors |
| `POST /signals/record {client, window_end, signals}` | audit trail |
| `GET /docs?ids=` | full documents (internal) |

Note the embedding flow: the **shell** calls the model and POSTs vectors;
the core only stores them and does cosine. The core never talks to an LLM.

`examples/coreClient.ts` is a typed TypeScript client for the same contract
— the shell language is a free choice; this repo ships Python.

## New in v0.6: per-source ingest & resumable harvesting

Two core capabilities, both of which the sector-granular v0.5 core couldn't express.

**Per-source ingest.** `/ingest` accepts an optional `sources` list, so a single
feed can be fetched on its own clock rather than dragging its whole sector along:

```bash
curl -X POST localhost:8788/ingest -H 'content-type: application/json' \
     -d '{"sectors":["technology"],"sources":["techwire"]}'
```

Named sources are **still validated against `sectors`** — asking for a source
outside your entitlement is refused, not honored, so the source filter narrows
what runs and can never widen it. Unknown ids come back as structured per-id
errors rather than failing the batch. Omitting `sources` keeps the old behavior
exactly: every source in the sectors, in config order.

This is what makes the scheduler's cadence *genuinely* per source: in
`config/schedule.json`, a job's `sources` map is source id → interval (so
`techwire` can tick every 15 minutes while `osdaily`, in the same sector, ticks
every 30), and the `sectors` map handles whole-sector jobs.

**Resumable, incremental harvesting.** The arXiv OAI-PMH connector now follows
`resumptionToken` paging to completion, with a `cursors` table in the core store
holding two things per source:

- the **in-flight token**, checkpointed after *every* page — so a harvest killed
  halfway through a large set resumes where it stopped instead of restarting;
- a **datestamp high-water mark** from the last completed harvest, replayed as
  `from=` so the next run fetches only what's new. It advances monotonically, so
  a late-arriving old record can't drag it backward.

The compliance gate is consulted on every page request, not just the first —
the polite spacing arXiv asks of harvesters applies *between* pages, and the
live path honors `503 Retry-After` with a bounded backoff.

## Run it

One entrypoint. `./run` with no argument lists everything.

```bash
./run demo     # build, ingest fixtures, run the pipeline, print signals, clean up
./run test     # every test: Rust workspace + --features net + pytest
```

That is the whole offline story. `./run demo` is fully self-contained — it
starts `cored` and the mock model, runs an `acme-research` pipeline over the
fixtures, prints the signal table (DeepSeek RISING, the near-duplicate drop,
etc.), and tears everything down. No env vars, no leftover processes.

To poke at it by hand instead of the one-shot demo:

```bash
./run up       # cored on :8788 and mock model on :8899
./run api      # public shell on :8787; loads model settings from .env
curl -H "Authorization: Bearer ak_acme_7f3d9c"  localhost:8787/v1/signals
curl -H "Authorization: Bearer ak_acme_7f3d9c" "localhost:8787/v1/search?q=sparse+attention"
./run down     # stop everything
```

### Configure real models once

`./run` automatically loads a root `.env`. The file is ignored by Git; only the
secret-free template is committed:

```bash
test -e .env || cp .env.example .env
chmod 600 .env
${EDITOR:-vi} .env
./run config       # prints resolved URLs/models and the harvest DB; never keys
```

The chat profiles let one file hold both a LAN server and an online provider:

```dotenv
LLM_CHAT_PROFILE=lan                   # change only this line to: online

LLM_LAN_BASE_URL=http://192.168.0.192:8080/v1
LLM_LAN_API_KEY=
LLM_LAN_CHAT_MODEL=your-lan-chat-model

LLM_ONLINE_BASE_URL=https://api.deepseek.com/v1
LLM_ONLINE_API_KEY=replace-with-your-key
LLM_ONLINE_CHAT_MODEL=deepseek-chat
```

Embeddings are configured independently:

```dotenv
LLM_EMBED_BASE_URL=https://your-embedding-provider.example/v1
LLM_EMBED_API_KEY=replace-with-your-key
LLM_EMBED_MODEL=your-embedding-model
```

This separation is required, not cosmetic. In the 2026-07-23 operator run, the
LAN server returned **501** from `POST /v1/embeddings`, while DeepSeek returned
**404**. Both can be chat candidates, but neither tested endpoint can populate
vectors. T4 needs a provider that really implements OpenAI-compatible
`POST /embeddings`; the verifier will report failure rather than silently call
BM25-only retrieval a pass.

The old `LLM_BASE_URL`, `LLM_API_KEY`, and `LLM_MODEL` variables remain supported
for a single provider that implements both chat and embeddings. Role-specific
and selected-profile values take precedence.

### The two things `./run` cannot fake

Everything above runs against fixtures and a mock model, on purpose — it is
deterministic and needs no network. Two commands reach the real world, and each
**refuses to pretend** if it can't:

```bash
./run harvest-arxiv    # a REAL arXiv harvest into data/live-smoke.db. Checks
                       # reachability first; if
                       # arXiv is unreachable it stops with exit 2 and tells you
                       # so, rather than silently "passing" against fixtures.

./run verify-llm       # loads .env; creates and tears down an isolated fixture
                       # core; runs embeddings + fusion + public HC1 checks.
```

`harvest-arxiv` needs outbound HTTPS to the configured arXiv endpoint. A bare
run uses `data/live-smoke.db`; an intentional named override remains possible as
`CORE_DB=data/named-smoke.db ./run harvest-arxiv`. Never point a smoke run at
`data/core.db`.

`verify-llm` needs both a chat-completions endpoint and an embeddings endpoint.
It owns a fresh temporary fixture database and its `cored` process, so no
separate `./run up` is required.

### Exact test sequence

Run these from the repository root:

```bash
# 1. Make sure no stale service owns the core port.
./run down
lsof -nP -iTCP:8788 -sTCP:LISTEN       # no output is the expected result

# 2. Full deterministic test suite: workspace, net feature, and shell.
./run test

# 3. Offline golden demo. This always forces the deterministic mock even when
#    .env selects a real model.
./run demo

# 4. Confirm profile resolution without exposing keys or making requests.
./run config

# 5. Real-model verification. Requires chat + embedding settings in .env.
./run verify-llm
```

Expected real-model success includes: embeddings missing count decreases,
`retrieval.notes` is empty, hybrid retrieval returns context, `/v1/ask` returns
citations, at least one cited document is `IndexOnly`, and the public answer has
no 16-token overlap with gated source bodies. A 404/501 embeddings response,
BM25-only fallback, core disconnect, or traceback is not a pass.

For an additional interactive public-API check, use two terminals:

```bash
# terminal 1
./run up

# terminal 2
./run api
curl -H "Authorization: Bearer ak_acme_7f3d9c" \
  "http://127.0.0.1:8787/v1/ask?q=What+is+DeepSeek-V4%3F"

# cleanup
./run down
```

<details><summary>Under the hood — the raw commands <code>./run</code> wraps, if you need them</summary>

```bash
cargo run -p cored                                          # core on :8788
pip install -r shell/requirements.txt
python3 tools/mock_openai.py &                              # mock model on :8899
LLM_BASE_URL=http://127.0.0.1:8899/v1 \
  PYTHONPATH=shell python3 -m intel_shell.pipeline --client acme-research
SUBSCRIPTIONS_PATH=config/subscriptions.hashed.json \
  LLM_BASE_URL=http://127.0.0.1:8899/v1 \
  PYTHONPATH=shell uvicorn intel_shell.app:app --port 8787
curl -H "Authorization: Bearer ak_acme_7f3d9c" \
  "localhost:8787/v1/ask?q=what+is+happening+with+sparse+attention+models"
```

A live arXiv harvest is the same `cored`, built with `--features net`, pointed
at a config with the `arxiv-cs` `"fixture"` key removed (`./run harvest-arxiv`
generates that config for you, leaving `config/core.json` untouched).
</details>

Degradation is graceful and explicit in the public API: no configured chat
endpoint makes `/v1/ask` return 503; an embedding failure leaves the vector leg
empty and records the reason in `retrieval.notes`. The T4 verifier is stricter:
either condition is a failed acceptance criterion, never a pass.

### Hashed API keys

Keys no longer need to live in plaintext on disk. `subscriptions.json` may
store a `key_hash` (HMAC-SHA256 of the key) instead of `api_key`; auth compares
digests in constant time. Migrate a plaintext file once and keep only the hashed
output:

```bash
PYTHONPATH=shell python3 tools/hash_subscriptions.py \
  config/subscriptions.json --out config/subscriptions.hashed.json
SUBSCRIPTIONS_PATH=config/subscriptions.hashed.json \
  PYTHONPATH=shell uvicorn intel_shell.app:app --port 8787
```

Set `API_KEY_PEPPER` to mix a server-side secret into every hash (regenerate
the file if you change it). Legacy records that still carry a raw `api_key`
keep working — they're hashed on the fly — and any `save()` rewrites them to
the hashed form.

### Key rotation & revocation

A client record can carry several active hashes, so a key can be rolled without
a flag-day cutover: the new key becomes primary, the old one keeps working until
a deadline, and is refused the moment it passes. Revocation is just rotation
with no grace period — which is what you want for a leaked key.

```bash
# roll a key; the old one keeps working for 24h
PYTHONPATH=shell python3 tools/admin_keys.py rotate \
  --client acme-research --new-key ak_acme_NEW --grace 86400

# leaked key: cut it off now
PYTHONPATH=shell python3 tools/admin_keys.py rotate \
  --client acme-research --new-key ak_acme_NEW

PYTHONPATH=shell python3 tools/admin_keys.py list      # who holds what
PYTHONPATH=shell python3 tools/admin_keys.py revoke --client acme-research --hash <hex>
```

The new key is hashed at the CLI and only the hash is stored — print it once,
hand it over, and it's gone. A provider can drive the same change through the
webhook with a `subscription.key_rotated` event (carrying `key_hash`, never the
key itself, plus an optional `retire_after` deadline).

### Billing webhook

A payment provider can flip a client's entitled sectors without a redeploy.
`POST /v1/billing/webhook` verifies an HMAC-SHA256 signature over the raw body
(`x-signature: sha256=…`) against `BILLING_WEBHOOK_SECRET`, then applies
`subscription.created|updated|deleted|key_rotated` events and persists the
change. Unset secret → 503; bad signature → 401. The core is never touched, so a
forged event can at most misgrant sectors the core still filters against its own
config.

```bash
BILLING_WEBHOOK_SECRET=whsec_… PYTHONPATH=shell uvicorn intel_shell.app:app --port 8787
# body signed with: hmac_sha256(secret, raw_body)
```

**Real providers** enter through an adapter, not through a second entitlement
model. `POST /v1/billing/stripe` (`STRIPE_WEBHOOK_SECRET`) verifies Stripe's own
scheme — `Stripe-Signature: t=…,v1=…`, HMAC over `{t}.{body}` — and normalizes
`customer.subscription.*` into the neutral events above. The timestamp is inside
the signed material and is checked for freshness, so a genuine-but-replayed
request is refused rather than re-applied. Stripe event types we don't handle
are acknowledged and ignored (a 500 on an uninteresting event is how a provider
decides to disable your endpoint). Sectors come from `metadata.sectors`, or from
a price→sector map (`STRIPE_PRICE_SECTORS`) so entitlements follow what the
customer actually bought. Swapping to Paddle means writing a second adapter —
`billing.py`, the store, and the entitlement model stay put.

### Subscription storage

`SUBSCRIPTIONS_PATH` selects the backend. A plain path is the JSON file; a
`sqlite://` URL is the SQLite store. Both implement one interface and commit
atomically (temp-file-and-rename / one transaction), so nothing else in the
shell knows which is in use.

```bash
PYTHONPATH=shell python3 tools/migrate_subscriptions.py \
  config/subscriptions.json --to sqlite:///var/lib/intel/subs.db
SUBSCRIPTIONS_PATH=sqlite:///var/lib/intel/subs.db \
  PYTHONPATH=shell uvicorn intel_shell.app:app --port 8787
```

The migration carries hashes across byte-exact and verifies it did — re-hashing
would invalidate every client's key.

### Scheduler

Automate pipeline runs on a per-source cadence — either an in-process loop or a
systemd timer (see `deploy/`). Because `/ingest` accepts a `sources` filter,
cadence is genuinely per source: a spec's `sources` map (source id → interval)
fans out one ingest job per feed — so two feeds in the same sector can run on
independent clocks — and an optional `sectors` map (sector id → interval) still
does whole-sector jobs, plus a client refresh job. A spec with neither runs a
single full job.

```bash
PYTHONPATH=shell python3 -m intel_shell.scheduler --dry-run   # preview
PYTHONPATH=shell python3 -m intel_shell.scheduler --once      # run due jobs, exit (cron/systemd)
PYTHONPATH=shell python3 -m intel_shell.scheduler --tick 60   # long-lived loop
```

### Tests

```bash
cargo test                                    # core: 49 tests
PYTHONPATH=shell python3 -m pytest shell/tests # shell: 69 tests, FAKE core via
                                              # httpx.MockTransport — no Rust needed
```

## Layout

```
crates/core        shared model: Document, License, Provenance, Entity, Signal, Day
crates/compliance  robots.txt fetch/parse/cache (RFC 9309) + polite per-host rate limiter
crates/ingest      Source trait + connectors (arxiv_oai, rss); net.rs behind --features net
crates/extract     SimHash near-duplicate collapse
crates/enrich      gazetteer resolution + discovery (LLM enrichment moved to shell)
crates/analyze     bursts (z-score), corroboration, co-occurrence graph (weight + PMI)
crates/store       SQLite archive: FTS5, embeddings BLOBs, signals_history audit
crates/view        compute_view: the shared dedup->enrich->analyze pass
crates/retrieve    BM25 + vector + RRF (sync; query vector supplied by the shell)
apps/cored         the core daemon: the ten-endpoint internal API
shell/intel_shell  config, core_client, auth, llm, prompts, briefing,
                   enrichment, app (FastAPI), pipeline (CLI),
                   security (key hashing + webhook sigs), billing (webhook),
                   scheduler (per-source cadence, in-loop or systemd)
shell/tests        shell test suite against a mocked core
examples/          coreClient.ts — typed TS client for the same contract
config/            core.json + entities.json (core-owned),
                   subscriptions.json / subscriptions.hashed.json (shell-owned),
                   schedule.json (shell-owned scheduler config)
deploy/            systemd service + timer for the scheduler
fixtures/          deterministic stand-ins for network bodies
tools/             mock_openai.py — OpenAI-compatible test double
                   hash_subscriptions.py — raw-key -> hashed-key migration
```

Adding a sector = a JSON edit. Adding a source type = one `Source` impl +
one match arm in the registry. Adding a *product feature* = Python only.

## Config split

`config/core.json` (core-owned — the engine's inputs):

```json
{ "sectors": [{ "id": "science", "display_name": "Science",
    "sources": [{ "type": "arxiv_oai" | "rss", "id": "...", "url": "...",
                  "fixture": "fixtures/...",  // omit for live fetch (net)
                  "license": "PublicDomain" | "CcBy" | "ClientOwned" | "IndexOnly" }] }] }
```

`config/entities.json` (core-owned data, shell-managed workflow): the
gazetteer. The EMERGING signal queue is its growth loop.

`config/subscriptions.json` (shell-owned — pure business state):

```json
{ "subscriptions": [{ "client": "acme-research",
                      "sectors": ["science", "technology"],
                      "api_key": "ak_acme_7f3d9c" }] }
```

## Live fetching

```bash
cargo build -p cored --features net      # requires rustc >= 1.86 (see below)
```

enables real HTTP (reqwest + rustls) behind the same robots + rate-limit
gate. Remove a source's `"fixture"` key in `config/core.json` to fetch its
`"url"` live. The arXiv connector speaks real OAI-PMH, **including
`resumptionToken` paging and datestamp high-water marks** (v0.6/T4): tokens
are checkpointed to the `cursors` table after every page, so an interrupted
harvest resumes mid-set, and the next run replays the high-water mark as
`from=`.

### Toolchain floor (read this before enabling `net`)

| build | needs |
|---|---|
| default / offline (fixtures) | rustc **1.78+** — set by the **lockfile format**, not the dependency graph: `Cargo.lock` is v4, and cargo cannot parse v4 before 1.78. (Deps alone would still permit 1.75; re-encoding the lock to v3 restores it, but cargo ≥1.78 rewrites v4 on the next lock change, so it does not hold.) Verified 75 tests green on 1.78 and 1.91; CI's `msrv` job enforces it. |
| `--features net` (live HTTP) | rustc **1.86+** |

`net` pulls `reqwest → url → idna → idna_adapter`, whose `icu_*` crates
declare an MSRV of 1.86 — and they are `edition = "2024"`, which Cargo only
understands from 1.85. On 1.75 this surfaces as the memorable non-sequitur
`feature 'edition2024' is required`, at *dependency-download* time, which is
why it reads like a registry failure rather than a compiler one.

**`Cargo.lock` is committed on purpose.** `cored` ships as a binary, and an
unlocked workspace re-resolves to the newest semver-compatible dependencies on
every clean checkout — which is exactly how an edition2024 crate walked into a
1.75 build unannounced. The lock pins it. Build with `--locked` in CI.

## Seed-grade choices and their production swaps

| Here (deliberately simple) | Production |
|---|---|
| SQLite + FTS5 (embedded, BM25) | Postgres (`sqlx`) + `pgvector`; `tantivy` if search outgrows FTS5 |
| static API keys in subscriptions.json | hashed keys, OAuth/JWT, billing webhook flipping sectors — **shell-only change** |
| per-request view recompute | materialized per-sector views on the ingestion schedule |
| z-score bursts, ordinal `Day` | Kleinberg burst states; `chrono`; seasonality |
| O(n²) SimHash pairwise | LSH banding |
| ~~prefix robots gate, shared rate limiter~~ **done (v0.6 T9.4 + v0.7 T2)**: RFC-9309 matching, per-host limiters, and a real per-origin `robots.txt` fetch+cache (TTL, bounded, fail-closed) | `governor` for token buckets if the hand-rolled limiter ever needs to be. **`texting_robots` was evaluated and skipped** — 45 transitive crates incl. the `icu_*` MSRV-1.86 chain, which would have raised the *offline* floor. Our parser was proven equivalent to it across 368 verdicts (STATE §6b). |
| context-time near-dup suppression | canonical-id marking at ingestion, filtered in retrieval SQL |
| shell↔core over localhost HTTP | same contract over a Unix socket, or gRPC if the payloads grow |
| brute-force cosine over BLOB vectors | `pgvector` HNSW/IVFFlat behind the same store methods |

The dedup threshold (16) was calibrated empirically on short title+abstract
texts: syndicated rewordings ~12 bits apart, related-but-distinct ~26,
unrelated ~36. Long-document corpora want ~3; make it per-source-class.

## Legal notes (not legal advice)

- Redistribution is the gated act, not analysis: `License::redistributable()`
  is enforced in the CORE (store snippets + view-evidence hydration), so no
  shell iteration can leak gated text. Passing IndexOnly text to a model as
  *context* is analysis; the shell's `ASK_SYSTEM` prompt forbids verbatim
  reproduction and citations point subscribers at the original. Before
  charging for anything that redistributes text, talk to an IP lawyer.
- arXiv: metadata is broadly reusable, but abstracts can carry author
  copyright; the fixture marks the source IndexOnly, the safe default.
- Compliant crawling means robots.txt, ToS, rate limits, and an identifying
  User-Agent — all of which have hooks in this codebase already.
