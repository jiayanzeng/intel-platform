# ARCHITECTURE.md — intel-platform

**This document is authoritative for invariants — what must be true of the
system. It changes rarely and never casually.** For *current status* (test
counts, what shipped last, open gaps) see `STATE.md`. For *how to work here* see
`AGENTS.md`. Where a placement below seems arbitrary, `STATE.md §2` holds the full
reasoning and is the authority.

intel-platform is a market- and technology-intelligence aggregation system built
on a **Core–Shell** split: a performance-critical, invariant-bearing Rust core
(`cored`) behind a freely-iterating Python shell (`intel_shell`).

## 1. The seam

```text
SHELL (Python, product layer — iterate freely)
  app.py        public /v1/* API, auth
  auth.py       api key -> entitled sectors
  llm.py        chat + embed  (the ONLY component that calls a model)
  prompts.py · briefing.py · pipeline.py · enrichment.py · scheduler.py
        |
        |  CoreClient (core_client.py) — the ONE door to the core.
        |  httpx, injectable transport (MockTransport in tests).
        v  minimal JSON API over 127.0.0.1:8788, optional x-core-token
CORE (Rust, engine — stable, invariant-bearing)
  apps/cored    /health /sectors /ingest /view /search /retrieve
                /attest /entities/unknown /embeddings(/missing,/stats)
                /signals/record /docs
  crates        core compliance ingest extract enrich analyze
                store registry view retrieve
```

The design intent: **source-side invariants live in the core so product-layer
iteration cannot bypass them.** `briefing.py` can be rebuilt from scratch and
still cannot leak gated text, because it never receives gated text. The
shell-owned public answer path is the recorded A4 exception: the shipped shell
attests it correctly, but an arbitrary rewrite is not constrained until public
egress crosses a core-owned boundary. That exact boundary is why the placement
decisions below are load-bearing.

## 2. Config ownership

| file | owner | holds |
|---|---|---|
| `config/core.json` | core | sectors, sources, licenses |
| `config/entities.json` | core | gazetteer |
| `config/subscriptions.json` (or `sqlite:///…`) | shell | clients, sectors, keys |
| `config/schedule.json` | shell | per-source and per-sector cadence |
| `config/protected-artifacts.json` | evidence control | immutable artifact facts and chained admissions |

Core-owned config describes *what exists and how it may be used*; shell-owned
config describes *who may see it and when to fetch it*. Do not cross these.

**HC9 — persistence scope is explicit.** HC9 governs shell-owned
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

**Manifest schema v2 has two disjoint evidence containers.**
`artifacts[]` holds protected SQLite archives, requires the SQLite corpus-fact
`expected` shape, and carries the executable append-only `admission` chain.
Every artifact's current SHA-256 equals its newest admission record; each new
record's `prior_sha256` equals the preceding record's SHA-256 and names the
admitting task/date, captured wire command and output reference, operator
approval, and retroactive status. `pinned_files[]` instead accepts immutable
bytes beneath `evidence/` or `observations/` and exact registered authorization
paths, with the applicable grade and byte facts; it forbids `admission`.
Validate the manifest with `python3 tools/evidence_artifacts.py validate`; then
prove the recorded bytes and corpus facts with `./run verify-artifacts`. The two
initial v0.10/A2 artifact records are explicitly retroactive references to
prior wire/B0 evidence, not new harvest claims.

A task requiring a byte pin names the container it intends to use. If neither
container can express the requirement, that is an author-side defect to record
and correct rather than a condition to work around. v0.26's fifth and sixth
unsatisfiable author-side rules are the two motivating data points and remain
historical dispositions; this rule does not reopen either. Executed
container-shape fixtures prove this description matches the validator today,
including the two exact v0.26 rejections: `extra=['admission']` under
`pinned_files[]` and `missing=['expected']` under `artifacts[]`. They cannot
prevent future validator drift; v0.27's prohibition on changing the validator
is what controls that limitation in this cycle.

## 3. Load-bearing placement decisions (do not move casually)

Condensed from `STATE.md §2`.

1. **License gating lives in the core.** `store.search` nulls snippets for
   `IndexOnly`; `/view` hydrates evidence with `excerpt: Option<String>` gated by
   `License::redistributable()`; `/attest` refuses a model answer that overlaps
   gated context. The shipped shell receives bodies only on the internal
   model-context seam and checks the answer before return. A4 proved that the
   shell remains in this path's trusted computing base: a receipt cannot tell
   the core which retrieval actually supplied a shell-owned prompt or force a
   rewritten shell to call `/attest`. Supporting an untrusted shell requires a
   non-bypassable, core-owned public-response boundary; HC3 still keeps the
   model call itself out of core.
2. **Entitlement *decision* in the shell; sector *filtering* also in core SQL.**
   Defense in depth: a shell bug can grant wrong sectors, never bypass the filter.
3. **The core never calls an LLM.** Embeddings round-trip through the shell;
   `/retrieve` takes `model` + `query_vector`.
4. **Full bodies are served on internal `/retrieve` and `/docs`** — model context
   is analysis, not redistribution, and these are loopback-internal, not public.
   Any model output derived from that context must pass through `/attest` before
   a public response.
5. **Source selection is core business.** `/ingest` takes `{sectors, sources?}`;
   every named source is validated against `sectors` (a source outside
   entitlement is refused, not run). Omitting `sources` preserves pre-v0.6
   behavior; a regression test pins this.
6. **Harvest pages and cursors are one core-store transaction.**
   `cursors(source_id, cursor, high_water, pending_high_water, updated_at)`:
   each parsed page's documents, sector-scoped canonical-id rematerialization,
   next `resumptionToken`, and pending max datestamp commit atomically. An
   interruption can therefore neither advance past documents still in memory
   nor forget a prior page's newer datestamp. Only a final-page commit clears
   the token/pending value and advances completed `high_water`, which remains
   monotonic (ISO dates ⇒ lexicographic max is chronological max).
7. **Provider vocabulary normalizes *into* the neutral event set, never out.**
   Billing speaks `subscription.created|updated|deleted|key_rotated`; Stripe
   enters through `adapters/stripe.py`. A second provider is a second adapter, not
   a change to the store or entitlement model.
8. **Dedup identity is a corpus property within a sector.** `canonical_id` is
   re-materialized from the global-within-a-sector rule (earliest by
   `(published_day, id)` inside each sector) inside the same SQLite transaction
   on every store write path that adds, changes, or removes rows. The sector
   axis is part of identity because independently configured domains can carry
   identical wording without denoting one archival object; cross-sector text
   equality must therefore never collapse entitlement-visible corpus members.
   The 64-bit `simhash(title + body)` is materialized at ingest or
   migration and refreshed on document updates; `/view` and canonical
   assignment consume that persisted value, and a missing value is an error
   rather than an invitation to hide a failed migration by recomputing.
   `/retrieve` keeps whichever near-dup the *query* ranked higher — relevance is
   a property of the question, not the corpus. Only the persisted fingerprint
   is reused there.

   **Shared identity seam — selected 2026-08-03.** The earlier
   threshold-authority limitation's trigger fired when v0.36 re-measured the
   graph and found that store and view already share `intel-extract`; no new
   crate, manifest edge, type-boundary dependency, or MSRV movement is needed.
   `assign_dedup_identity` now owns candidate ordering, sector partitioning,
   feature eligibility, radius comparison, and canonical selection. Store
   persistence and view collapse translate their boundary types into that one
   rule. Registered R14 requires both call sites and the shared sector key, with
   independent planted failures for removing either consumer and for replacing
   the sector key. This closes the prior two-implementation scope divergence.

   The numeric radius remains boundary-local: the store's private constant and
   `ViewParams::default` are still synchronized by registered R5. Static
   equality is not a shared compiled constant; a coordinated radius change
   still requires its own behavioral evidence and release decision.

   **Feature eligibility — selected 2026-07-30.** Radius 16 applies only when
   both documents have at least 26 three-token SimHash features. Twenty-six is
   the smallest feature count measured in the calibrated golden news corpus;
   the measured SEC corpus had at most 10, so the unmeasured 11–25 range is
   deliberately ineligible rather than extrapolated. `intel-extract` owns the
   one compiled `DEDUP_MIN_FEATURES` authority and the shared two-sided guard;
   the one shared identity implementation invokes it for both consumers. R5
   statically observes the floor, guard body, and call site with planted
   failures. R1 remains the durability-caller topology control and R14 owns the
   store/view identity seam. The explicit cost is that sparse documents,
   including byte-identical ones, remain separate identities until another
   measured rule is admitted.

## 4. The robots subsystem (two gates, one direction)

- **Publisher policy** — fetched from the real `/robots.txt` (`RobotsCache`,
  `crates/compliance`): per-origin, bounded to 512 origins, and the fetch itself
  goes through the per-host politeness limiter. Successful `Gate(_)` and
  definitive `Unavailable` results use the 24-hour policy TTL; transient
  `Unreachable` results use the production five-minute negative TTL.
- **Operator deny-list** — `RobotsGate::new(&["/private","/admin"])`, applied on
  top; can only ever refuse **more**.

Pinned dispositions:
- **Fail-closed, and the 4xx/5xx distinction is not cosmetic.** 2xx ⇒ the body
  governs (empty body = valid allow-all ≠ 404). 5xx / DNS / TLS / timeout ⇒
  Unreachable ⇒ take nothing. 4xx ⇒ Unavailable ⇒ **per-source**
  `robots_on_missing` decides, defaulting to Deny; a typo or omission fails
  closed.
- **Opting in reinterprets ABSENCE ONLY.** `robots_on_missing: "allow"` changes
  the 404 case and nothing else; an explicit `Disallow` is still obeyed, and an
  Unreachable origin still fails closed.
- **A fixture read is not a request.** `gate()` takes a `Reach`; a fixture-backed
  source never fetches `robots.txt`. Pinned by test.
- **The policy target is the complete request path plus query, never the
  fragment.** This exact target is derived before the first document request
  and again before every redirected request. A rule for `/a/b?mode=full`
  therefore cannot be weakened to `/a`, and a client-only `#fragment` can
  never affect a publisher verdict.
- **A published `Crawl-delay` can only slow us down**, never speed us past our own
  floor (2 rps).
- **Politeness is process-scoped (HC8):** `HostLimiters` and `RobotsCache` in
  `AppState`.
- In production `cored`, the single `build_robots_cache` crawler-identity
  construction call precedes the sole `TcpListener::bind`; with the `net`
  feature enabled, this installs the process-scoped identity before the
  listener can accept a request.

The shorter negative TTL deliberately permits more `/robots.txt` attempts
against a failing origin: at most one attempt per 300 seconds instead of one
per 24 hours, bounded by ingest frequency and the same process-scoped
politeness limiter acquired by `policy_for`. The cached verdict remains
fail-closed throughout. An unreachable refresh still overwrites an expired
successful policy; retaining a last-known-good policy is Decision B, deferred
until a measured transient robots outage affects an admitted publisher while a
usable stale policy exists and the operator explicitly authorizes that change.

**v0.18 wire / v0.19 support boundary.** v0.18 changed no default-build
compliance verdict or robots-policy behavior. ORIGIN-CASE shipped nothing
because the production network path normalizes authority bytes through
`reqwest::Url` before the gate. The published v0.15.2 tag contained an inert
robots-only observation client and matcher provenance; its v0.18 observations
remain historical evidence. On 2026-07-29 the operator selected retirement:
the current tree contains neither feature declaration, diagnostic API,
robots-only network helper/test, nor preview binary. The default product gate
remains the only supported robots-policy surface.

The live evidence remains bounded. `arxiv-cs` and `sec-edgar-usgaap` are the
two configured network sources, while the other three configured sources are
`example.org` fixtures. On 2026-07-30 one operator-authorized, plaintext-
observable runtime exercised both origins sequentially with four
application-level request starts: one robots and one content attempt per
origin, with no retry, redirect, second OAI-PMH page, scheduler, or fifth
request. Fresh robots bytes remained exact to the committed captures. arXiv's
HTTP 404 became `RfcAllowAll` under that source's `robots_on_missing: allow`;
SEC's real body independently produced `Body(allow)` under
`robots_on_missing: deny` after arXiv already occupied the same process-scoped
cache. The permissive absence policy therefore did not bleed across origin
keys. arXiv's content request timed out before a page or cursor committed,
while SEC returned 200 documents to the fresh archive. Unit tests already
execute cache keying/reuse and per-host limiter independence; this live run
adds wire integration for those properties and the first mixed-disposition
coexistence measurement. It does not exercise concurrent-harvester
single-flight (T7), a successful live arXiv cursor checkpoint, or the
600-second schedule.

**Terms-policy boundary — operator disposition 2026-07-30.** The executable
two-gate model does not claim to decide publisher terms compliance. Publisher
terms are reviewed as a dated, publisher-specific operator responsibility
before admission because the reviewed SEC requirement is natural-language
policy with no stable machine-readable classification or registration state.
For the reviewed SEC path, the publisher's operational direction is an
organization-and-contact User-Agent; the operator affirmed on 2026-07-30 that
the structurally required contact is monitored. This does not add a third
runtime gate or generalize the determination to another publisher.

**Redirects are re-gated before the next request (v0.8/T5).** Both
`reqwest::Client`s in `crates/ingest/src/net.rs` use `Policy::none()`. Document
redirects are resolved manually (maximum 10 hops), and the full publisher +
operator gate runs before each hop. A cross-origin `Location` therefore causes
the new origin's robots policy to be fetched and honored before document bytes
are requested; a same-origin hop reuses the process-scoped cache. Robots-file
redirects fail closed rather than silently moving to another origin.

## 5. Endpoints (core, loopback 127.0.0.1:8788)

| endpoint | method | purpose | gated? |
|---|---|---|---|
| `/health` | GET | liveness | — |
| `/sectors` | GET | sector list | — |
| `/ingest` | POST | harvest `{sectors, sources?}` | internal |
| `/view` | GET | analyzed corpus; excerpts gated by license | **excerpt gated** |
| `/search` | GET | ranked docs; snippets nulled for IndexOnly | **snippet gated** |
| `/retrieve` | POST | `{q, sectors, k, model?, query_vector?}`; full-body model context | internal |
| `/entities/unknown` | POST | requires `CORE_TOKEN`; compares shell-extracted names against the core-loaded gazetteer and returns only the unknown subset | internal |
| `/embeddings/missing` | GET | sector-filtered backfill work queue | internal |
| `/embeddings/stats` | GET | stored vector count/dimension for one model key | internal |
| `/embeddings` | POST | vectors posted back by the shell | internal |
| `/signals/record` | POST | shell posts signals back | internal |
| `/docs` | GET | sector-filtered full documents | internal |
| `/attest` | POST | `{answer, context_doc_ids, sectors}` ⇒ `{clean_answer, violations[]}` | **enforces HC1** |

`CORE_VIEW_DIAGNOSTIC_DELAY_STAGE` plus
`CORE_VIEW_DIAGNOSTIC_DELAY_MS` form a deliberate benchmark-only timing knob
for the `sector_load`, `analysis`, `response_build`, and `serialization`
stages. The delay is bounded to 10,000 ms. If either variable is set, startup
warns with both raw settings and the effective bounded delay; normal operation
leaves both unset. The knob changes timing only and never changes a `/view`
response body.

The public surface is the shell's `/v1/*`. The core is structurally loopback-only:
startup resolves `CORE_BIND`, checks every resulting address, and refuses before
binding if any address is not loopback. `/retrieve` and `/docs` carry full bodies
only for analysis, and the shipped shell sends model output through `/attest`
before `/v1/ask` returns it. This prevents copied IndexOnly context on the shipped
path, but does not constrain an arbitrary rewrite that omits the call or supplies
a false scope (A4 accepted risk). Every caller-directed boundary that reads or
returns document bodies takes an explicit sector set whose predicate is enforced
in core SQL; an empty set makes every requested document unavailable.

## 6. Invariant map (which invariant lives where, and why)

| invariant | enforced in | why there |
|---|---|---|
| HC1 no gated text public | core (`/search`, `/view`); core + trusted shipped shell (`/attest` for `/v1/ask`) | source gating is unconditional; answer attestation is enforced on the shipped path, but a rewritten shell can still bypass or falsify that handoff until public egress crosses a core-owned boundary (A4 remains open) |
| HC2 sector filtering | core SQL at `/retrieve`, `/docs`, `/attest`, and `/embeddings/missing`; private unscoped store seam; R7 | every caller-directed body hydration requires an explicit sector set, an empty set makes requested documents unavailable, and production callers cannot select the unscoped id lookup, so a shell bug may grant wrong sectors but cannot bypass the filter mechanism |
| HC3 no LLM in core | core (by omission) | keeps the engine deterministic and offline-testable |
| HC8 politeness | core `AppState` | a TTL / limiter that doesn't outlive the request is theatre |
| HC9 persistence scope | shell configuration + core store | shell config defaults to atomic JSON; the three recorded SQLite scopes above are explicit |
| HC12 lock discipline | CI (`--locked`, MSRV job) | the lock *is* the build; its format is part of MSRV |
| HC13 fixtures ≠ wire | tests + live-run policy | three bugs came from believing otherwise |
| corpus identity atomicity, scope, and eligibility | core store transaction + R1 production-caller allow-list + R5 synchronized distance/feature declarations + R14 shared identity seam | each of the five enumerated production durability paths rematerializes canonical identity exactly once before its commit; store and view both consume one implementation that partitions candidates by sector; the two boundary-local radius declarations remain synchronized; and the one identity implementation invokes the two-sided 26-feature eligibility authority, so sparse fingerprints cannot exercise a radius calibrated on denser text |
| repository absence claims | registered `invariant-scan` rules in local/hosted CI | each scoped claim has executable source coverage and a captured planted failure; prose-only absence is not accepted |
| local/hosted check parity | R10 over `run` and `.github/workflows/ci.yml` | the local `ci-local` jobs and non-report-only hosted verification steps are derived from their entry-point commands in both directions; runner setup, release-evidence plumbing, report-only jobs, and operator-local protected database bytes are explicit, counted exemptions |
| active-runbook measured-value references | `cycle-check` acceptance-criterion heuristic | explicit cross-step references to a recorded, measured, or stored value/count/number/quantity/total are rejected; acceptance must state the invariant relation at the same commit |
| routine model-profile authorization | shipped L1 controller allowlist + pure fail-closed guards + repository pins | the current controller can construct only the five-container/read-only command set and refuses unsafe observed state, but an edited controller can rewrite this client-side boundary; the server-enforced L2 forced-command wrapper remains open and scheduled |

The last row is defense for the shipped controller, not a server-side security
invariant. L1 and its repository pins detect or refuse the current implementation;
they do not authorize future controller edits. Likewise, the HC1 row still
describes the trusted shipped shell and does not close A4.

The repository-absence row is deliberately scoped rather than universal. R3 is
an open-bottom deny-list over recognized OpenAI, Anthropic, and LLM vocabulary;
an unknown provider or inference-gateway spelling is outside its coverage, so
R3 does not prove HC3 against arbitrary new vocabulary. R4 is likewise an
open-bottom deny-list over registered credential names and value shapes;
unknown names or encodings are outside its coverage, so R4 does not prove that
every possible secret form is absent. These scanner limits do not weaken HC3 or
the credential-disclosure prohibition; they prevent the checks from claiming
more than their source detectors establish.

R11's v0.16 control-breadth limitation is closed. Its declared source scope
still covers direct reads of `config/core.json`, `config/entities.json`,
`CORE_CONFIG`, and `CORE_ENTITIES`, plus module-local variables derived from
those spellings. Five independently reconstructible `fail_before` controls now
exercise both direct path spellings, both environment-name spellings, and an
`open()` call through a module-local variable tainted from `CORE_ENTITIES`.
`invariant-scan --self-test` requires each mutation to fail at its recorded file
and line. This closes the recorded mismatch between R11's scope and its failure
controls; it does not turn the four-spelling rule into a universal detector for
unknown future configuration names.

The active-runbook measured-value check is deliberately heuristic, not a
semantic proof. It recognizes explicit same-clause combinations of a
cross-step `Step N` reference, a recorded/measured/stored term, and a
value/count/number/quantity/total term. A paraphrase outside that vocabulary or
split across clauses can escape it, while an unusual intentional sentence may
need rephrasing. Closed runbooks remain historical evidence and are not
retroactively evaluated by this check.

The review-export budget is an executable **operator-local contract**, not a
hosted repository invariant. `./run export-check` writes the export from the
project root, derives its tracked source set from `git ls-files`, and checks the
required root/control paths without pinning a count. `AGENTS.md` records the two
measured operating rules: non-root generation silently dropped `Cargo.lock`,
and Repomix's security pass included 339 of 340 collected files while omitting
`crates/ingest/src/lib.rs`; registered self-testing invariant R4 remains the
credential control. The check is intentionally absent from local/hosted CI
because it writes a multi-megabyte export and `npx` may fetch its pinned
toolchain. This does not add or renumber an HC invariant.

The governed review-export content binding is evaluated at the exact tree
`cycle-check` is checking. Every closed tree binds the architecture row to the
last governed measurement already visible in that same tree. A release closing
child may add its already-existing release parent's measurement beside the
agreeing row. A later audit measurement uses the distinct
`cycle-ending review-export audit` field after the last governed field; it is
parsed and reported but cannot supersede the closed comparison. The checker
also compares the written row against `export_check.py`'s single ceiling
authority while stating that this does not measure an export. Actual bytes,
retention, and excluded content remain owned by operator-local
`./run export-check`. Registered R12 makes the stale-row, over-ceiling, and
misordered-audit constructions fail.

The cycle-margin estimate beside that bound value is independently executable.
Its measured cell names a governed→governed kind, the two progress records that
supply the last governed values at those evaluation points, the same-kind byte
delta, the ceiling remainder, and the two-decimal quotient. `cycle-check`
re-reads the last governed measurement in both named records, requires the
current term to equal the row's governed byte marker, and recomputes every
derived term. Closing→closing and delivered→delivered remain legitimate
operator measurements, but they are not accepted in this machine field because
the repository has no common closing/delivered progress authority comparable to
the governed fields. R12 plants a mixed-kind row through the real lifecycle
entry point and disables this comparison.

`STATE.md` archival eligibility is structural rather than a line or byte
constant. The status paragraph supplies the immutable header boundary;
`STATE_ARCHIVE_PERMANENT_TAIL:START` supplies the permanent-tail boundary; the
bytes strictly between them are the only archival-eligible region. The marker
must occur exactly once and immediately precede the first numbered top-level
heading, and no numbered top-level heading may occur in the eligible region.
The checker derives every numbered heading and numbering gap from the live
State text; it carries no enumerated section list.

The same check derives live external `STATE §N` and `STATE.md §N` consumers
from the Git-tracked set, structurally excluding cycle records, prior State
archives, and test/control constructions. Every derived anchor must resolve to
a permanent-tail heading. Its entry-point report names all three byte regions,
top-level sections, gaps, referenced sections, referenced gaps, and source
sites; the present `3` gap is therefore reported with no reference rather than
encoded as an exception. Structural admission requires the status header and
exactly one permanent-tail marker before any semantic result can affect the
outcome. Missing-restatement cases remain delegated to `version_check`'s
existing current-restatement reader, and the region report explicitly names
that semantic state as `present` or `absent` with `version-check` as owner.
Header, marker cardinality, headings, adjacency, overlap, anchors, external
references, and ordinal order are structural; none depends on the semantic
restatement. Complete tail removal therefore fails on the missing structural
marker even though the delegated semantic state is absent. R12 removes the
full tail through the real lifecycle entry point and disables the structural
marker branch, proving that the planted construction would otherwise pass.

Archive fidelity is a separate property from archival eligibility. Manifest
schema v2 admits the v0.33 archive through an exact structural-archive registry,
not through the evidence, observation, SQLite-artifact, or authorization
classes. The registered path is
`docs/state-archive/STATE-through-v0.28.md`; a different archive name or a
non-structural grade fails schema validation. `./run verify-artifacts` reads the
registered bytes and compares both SHA-256 and byte length on every run. The
older through-v0.21 archive retains its honestly bounded one-time verification
and is not silently upgraded into this standing claim.

The cycle-ending audit's zero-or-one cardinality is deliberately optional in
the general lifecycle checker. When a closing-tree export was actually measured
and differs from the governed figure, the audit field is the truthful place to
disclose that result. Its absence asserts neither a zero delta nor a performed
measurement: the lifecycle checker does not create an export and therefore has
no independent fact that could make a conditional requirement non-vacuous. A
cycle may impose a stronger runbook-specific requirement. The latest
append-only audit record's own byte contribution is necessarily undisclosed;
another field would recreate the self-measurement fixed point.

The governed export margin's executable denominator is the latest positive
adjacent same-kind governed pair. That selection and its arithmetic are bound,
but its representativeness and structural epoch are not: one adjacent pair
cannot establish a representative rate, and the checker has no independent
machine-readable event that identifies an archival or other structural change.
The entry point therefore emits both limits beside every successful basis
selection. A numeric floor would be an unsupported inference from only two
positive pairs; a trailing window would mix the measured v0.33 one-time archive
reclaim into steady growth; and an epoch rule would merely trust prose until an
independent epoch authority exists. This is an explicit bound, not a claim that
the selected pair predicts future growth.

Published-release divergence is counted within a publication epoch. A
successful authorized publication resets the consecutive closed-cycle count to
zero at the published closing commit. Only a measured runtime-behaviour
difference in the later unpublished distance starts a fresh count, at the first
subsequent closed cycle carrying that difference. Pre-publication cycles, a
difference already shipped by the publication, documentation/evidence/lifecycle
changes, and a cycle with no measured runtime difference do not start or
continue the count. A public-surface change still fires immediately. These
classifications and the reset event are dated operator adjudications because no
repository check can independently infer runtime meaning or remote publication
truth from the row that reports them; executable freshness and identity checks
do not pretend otherwise.

Publication reconciliation is likewise a lifecycle control, not a new HC
invariant. Legacy release headers through v0.15.5 carry immutable annotated-tag
object and peeled-target facts; a tagged-closing header carries the already
known release-commit parent and leaves the later tag object and closing target
to its dated forward record. Neither form predicts a mutable branch ref whose
value publishing the same commit creates. Exact branch measurements therefore
live in dated body records. `cycle-check` requires the applicable immutable
assertions to exist and agree with the newest closed release record; zero
matches are a defect, not a conditional skip. The tag must also be reachable
from `HEAD`; missing tag, target, or ancestry inputs fail closed. The older rule
that rejects a reachable release while the live header calls publication
pending is unchanged. Registered R12 executes the actual publication-status
entry point over planted cases. It independently disables selection of the
newest actual release, each of the three family-admission outcomes, and every
rule within the admitted family. `cycle-check` itself now distinguishes an
absent State file, an absent `**As of:**` status header, and a leading as-of
header whose shape does not match `STATE_HEADER_RE`; no later no-release cycle
can hide the newest earlier release from reconciliation. The separate
`version_check.state_version()` regex binds a version for a different reason
and is not this family's admission floor. Thus neither an empty selector nor a
rule that examines nothing can report clean merely because its pattern found
nothing.

Hosted lifecycle checks deliberately use `--skip-local-tag-verification`; they
can validate cycle structure without possessing every historical tag, but they
cannot prove remote historical release identity. v0.22 established that local
`v0.8.0` and `v0.10.2` resolve to valid annotated tag objects and existing
commit targets while complete remote enumeration contains neither name nor
object. The records are therefore correct and the remote is incomplete.
Remove the hosted skip only after both exact objects are published and a
full-history hosted `cycle-check` passes without it, or after contrary evidence
causes the identities and affected claims to be forward-corrected.
The checker makes each intentional non-reconciliation branch visible: no
reachable closed release reports a `not-applicable` bound, portable hosted mode
reports `not-requested` and names the admission and structure checks it retains,
and a verified legacy release reports that R-CLOSE post-push records do not
apply. These are explicit bounds, not silent successes.

### Dated operational-residual dispositions

| subject | disposition | trigger | dated measured observation and reason |
|---|---|---|---|
| review-export operator-local status (v0.22 G3) | **REFUTED as a missing-contract claim — 2026-07-29** | none | 2026-07-29 — The contributor-facing paragraph above and `AGENTS.md` already state that `./run export-check` is operator-local, why it is absent from local/hosted CI, and what it verifies. No duplicate rule or hosted workaround is added. |
| review-export size and retention bound (v0.28) | **Accepted at a 3,000,000-byte ceiling and two-cycle retention depth — operator selected 2026-08-02** | the project-root review export exceeds **3,000,000 bytes**, its cycle-document set differs from the active cycle plus the immediately prior execution cycle, the pinned SEC RSS body reappears, or any `docs/state-archive/**` byte reappears | v0.36 · 2026-08-03 — Step 5 measured implementation tree `9dea180cb872c6fa5c28b09907e2b452a7904952` at an export of **2,850,622 bytes / 153 files / 2 retained cycles**, with exactly the v0.35–v0.36 task/progress pairs retained and both protected byte classes excluded. The distinct-cycle progress-backed governed series is **2,742,486 → 2,850,622 (+108,136)**. Its **149,378-byte / 4.98%** remainder is **1.38 cycles** at that latest adjacent-cycle denominator. Review-export margin: kind=`governed→governed`; prior_progress=`docs/cycles/PROGRESS-v0.35.md`; prior_bytes=`2742486`; current_progress=`docs/cycles/PROGRESS-v0.36.md`; current_bytes=`2850622`; evaluated_progress=`docs/cycles/PROGRESS-v0.36.md`; evaluated_bytes=`2850622`; denominator_bytes_per_cycle=`108136`; numerator_bytes=`149378`; cycles=`1.38`. Exact historical E0/Step 5 remeasurement also corrected the v0.17.2 release-parent/closing pair to **2,725,527 → 2,737,957 bytes at 151 files**, a +12,430-byte delta, and exposed the closing export's **−4,529-byte** difference from its 2,742,486-byte governed field. Neither byte nor retention trigger fired. Governed review-export bytes: `2850622`. |
| protected evidence-manifest growth (v0.22 G4) | **Accepted with bounds — 2026-07-30** | the manifest reaches its governed artifact byte boundary, or two consecutive clean `./run verify-artifacts` runs each take **≥1.00 s real** | v0.36 · 2026-08-03 — E0 measured the unchanged manifest at **193,057 bytes / 332 pins**, leaving **855,519 bytes** to its governed boundary, and matched the State archive plus both protected databases. The latest duration-bearing complete checks remain **0.12 s / 0.13 s real**, leaving **0.88 s / 0.87 s** to the timing trigger; E0 did not capture a newer duration and makes no such claim. No manifest or protected byte changed and neither trigger fired. |
| shell `StarletteDeprecationWarning` (v0.22 G5) | **Accepted until trigger — 2026-07-30** | the warning becomes an error/failure, or the next authorized constraints refresh changes FastAPI, Starlette, `httpx`, or `httpx2` | v0.36 · 2026-08-03 — Step 6's exact-candidate local Python 3.11 and 3.12 populations each collected and passed **368/368** and emitted the existing single warning. Each hosted lane collected **368**, passed **367**, and skipped only the declared `on_site` production-audit node; the comparator derived equivalent **368** populations. No dependency declaration, constraint, FastAPI, Starlette, `httpx`, or `httpx2` value changed; neither warning trigger fired. |
| published-release divergence | **Accepted under the operator-selected bound; publication-epoch reset defined — 2026-08-01** | the unpublished distance contains a measured runtime behaviour difference persisting across three consecutive closed cycles within the current publication epoch, or acquires any public-surface change | v0.36 · 2026-08-03 — Step 4 changes reachable runtime behavior for a cross-sector near-duplicate corpus: view now preserves sector-local identities. The cycle remains open, so no closed-cycle count is added yet and published v0.17.1's epoch count remains **0**. Separate Step 3/Step 4 builds produced byte-identical **15,719-byte** canonical public payloads across both configured subscribers and every `/v1/*` route exercised, SHA-256 `0c2ec212b9e398eddd38053c7157b8dd283f35f3908ad1b8c2f6481a912f09ea`; no route, response-body schema, named surface, serialized value domain, licensing outcome, or entitlement outcome moved. The public-surface trigger did not fire. |
| hosted GitHub Actions Node-runtime deprecation annotation (v0.22 G5) | **Completed by v0.23 Step 3 — 2026-07-29** | none | 2026-07-29 — Run `30456330833` passed **7/7** executable jobs on the migrated actions; all eight check runs had annotation count **0**, and the new **7-receipt / 7-bundle** set verified **7 accepted / 0 rejected**. |
| hosted action immutability (`dtolnay/rust-toolchain@master`) | **Completed by v0.23 Step 3 — 2026-07-29** | none | 2026-07-29 — All **6/6** workflow uses are pinned to immutable commit `2c7215f132e9ebf062739d9130488b56d53c060c`, dated **2026-07-16T09:35:07-07:00**, and the same hosted evidence run verified. |
| recorded-trigger freshness discipline | **Completed by v0.23 Step 5 — 2026-07-29** | none | 2026-07-29 — `cycle-check` now requires a valid dated measured observation for each trigger-bearing row in this table and the active v0.23-forward deferral table; registered R12 mutation **15** proves a missing date is rejected. |
| SEC automated-access terms (v0.25 TERMS-GATE) | **Operator responsibility outside the executable model — 2026-07-30** | none | 2026-07-30 — The SEC privacy policy prohibits “unclassified” automated tools while its webmaster FAQ directs programmatic downloaders to declare an organization-and-contact User-Agent. The operator affirmed that the structurally required contact is monitored. The terms condition is publisher-specific natural-language policy with no stable machine-readable classification or registration state, so a dated operator review—not a pretend third runtime gate—owns it. |
| SEC US GAAP RSS cadence | **Explicit per-source cadence: 600 seconds — 2026-07-30** | none | 2026-07-30 — The `<description>` in committed `observations/v0.25/feed-shape/sec-edgar-usgaap.rss.xml` says the feed updates every 10 minutes. `observations/v0.24/publisher-review/sec-edgar-report.md` records the process floor at 2 requests/second, the publisher's cited ceiling at 10 requests/second, and no publisher `Crawl-delay`; `observations/v0.25/terms-gate/sec-edgar-terms-determination.md` records the cited Developer Resources URL and 2026-07-30 read date. The scheduler therefore gives only `sec-edgar-usgaap` a 600-second ingest clock while retaining `filings-digest` and the finance refresh at 7,200 seconds. This cadence decision is separate from, and does not satisfy, the terms determination above. |
| SEC US GAAP RSS cadence criterion correction (v0.27) | **Explicit per-source cadence remains 600 seconds — criterion corrected 2026-07-30** | none | 2026-07-30 — The governing loss quantity is latest-window advance time, not the publisher's ten-minute rebuild description. The pinned latest-200 sample spans **4,650 seconds / 77.5 minutes**, so the unchanged **600-second poll interval** consumes **12.90%** of that observed span and the span/poll margin is **7.75×**. This sample is one post-close window on one Wednesday and does not establish peak-season density, deadline-day density, or density during hours neither live sample covered. Its positive measured margin does not imply a cadence change, so 600 seconds remains declared; it also does not satisfy the separate terms condition or the coverage-detection objective. |
| Non-paged fixed-window coverage detection (v0.27) | **Overlap/id-only Option 1 authorized — 2026-07-30** | none | 2026-07-30 — For each non-paged source separately, the store assesses the incoming id window before the combined `append_new` call. An empty store is `first_window`; a non-empty id intersection is `overlap`; a non-empty store plus an empty intersection is the conservative `gap_detected` outcome. The incoming window is still committed, because discarding it would compound the loss. Exact no-gap proof from an overlap depends on a contiguous publication-ordered window and stable ids. The pinned SEC body executes the observed premises at capture: 200 items, zero ascending timestamp inversions, 200 unique GUIDs carrying 200 distinct matching accession numbers, and one `www.sec.gov` host; cross-poll identifier immutability remains a stated dependency rather than a fact one snapshot can prove. Empty overlap can false-positive after a publisher re-issue or GUID-form change, so the system does not claim zero false positives or quantify loss. On a detected gap it reports the held-newest and incoming-oldest `published_raw` boundary strings without instant parsing; eight timestamp values in the pinned body are tied (seven pairs and one triple, maximum multiplicity three), which is why timestamps are not the identity watermark. Cursor-paged OAI-PMH is explicitly `not_applicable_paged`, because consecutive committed pages legitimately need not overlap. The response and log are observational: detection never fails the poll. |
| Mixed robots dispositions in one runtime (v0.27) | **Confirmed without cross-origin policy bleed — 2026-07-30** | none | 2026-07-30 — One bounded sequential runtime evaluated fresh, byte-identical robots captures for both configured publisher origins. `https://oaipmh.arxiv.org` returned HTTP 404 and used that source's `allow` missing-policy as `RfcAllowAll`; `https://www.sec.gov` returned its real policy and independently produced `Body(allow)` under its `deny` missing-policy after arXiv occupied the same cache. Exactly four application-level request starts occurred, two per origin. arXiv content timed out before a page/cursor committed; SEC returned 200 documents. Cache keying/reuse and per-host independence were already unit-tested, so the live novelty is opposing-disposition coexistence and wire integration, not first state-machine proof. Sequential origins do not fire T7, and the scheduler did not run. |

The v0.13 sector-boundary correction narrows neither residual: a rewritten
shell can still bypass or falsify the `/attest` handoff, so A4 remains open;
an edited controller can still rewrite the L1 command construction, so the
server-enforced L2 forced-command wrapper remains open and scheduled. The R3/R4
open-bottom limits, active-runbook measured-value heuristic, T7 robots
single-flight, and robots negative-cache Decision B also remain open. Both
configured publisher origins have now been fetched together sequentially in
one bounded production-path runtime. That run confirms source-local opposing
robots dispositions without policy bleed; it does not create two concurrent
harvesters. The bounded runtime used one supported simultaneous harvest caller
and no scheduler, so it did not move T7 nearer its second-concurrent-harvester
trigger. The 600-second SEC schedule has not executed, and neither this cycle
nor its publication authorizes that clock to issue traffic. The
publisher-specific terms responsibility above is unchanged.

Moving the public FastAPI version literal from
`shell/intel_shell/app.py` to the package-owned
`shell/intel_shell/__init__.py` remains a recorded forward option for removing
the one release-authority/production-source scope overlap; it is not
implemented here. The v0.17.0 release changes none of these residual
dispositions, and no transient robots outage supplied Decision B's trigger.

## 7. The decision-log discipline

Non-trivial "why not X" decisions are recorded in `STATE.md §6` with the
measurement that settled them, and a struck reason is *removed* rather than kept
(a dead reason is worse than none). `feed-rs`, `texting_robots`, and LSH banding
are all *correctly absent*, and the log says why, with numbers. New dependency or
scale decisions follow the three-clause gate in `AGENTS.md §3`.

## 8. Execution cycles and artifact releases

An execution-cycle name is a planning and evidence namespace, not an artifact
version. Completing `docs/cycles/TASKS-vX.Y-EXECUTION.md` does not by itself
create, imply, or move a `vX.Y.Z` release. Cycle v0.15 shipped artifact
`v0.14.1`, so differing cycle and release identifiers are intentional.

Release identity is chosen explicitly at the cycle-closing release task after
the measured diff is classified:

- adding, removing, renaming, or incompatibly reshaping an observable route,
  response body, schema, or other named surface requires the corresponding
  minor release;
- a correctness or behavior fix within existing names and shapes uses a patch
  release, including a compliance correction that should propagate under patch
  semantics;
- operations and evidence-only changes may also use a patch release;
- a cycle with no shipped change may close with no release.

The named-surface shape rule covers every route and response body explicitly
named as an observable contract in this architecture, including internal
loopback routes. “Internal” constrains access and redistribution; it does not
make a named JSON shape unversioned. Adding the per-source coverage field to
the named `/ingest` response therefore takes a minor release. This criterion
is reusable: a future addition, removal, rename, or incompatible reshape of a
field on any named internal response is minor unless that surface is first
explicitly removed from the contract.

The dated public-value-domain criterion in `AGENTS.md §5` also classifies adding,
removing, or redefining any value a field already serialized in a `/v1/*`
response can take as a minor release. A consumer's exhaustive handling of that
set is part of the public contract even when route, field name, field type, and
body shape stay fixed. This is a prose R-CLOSE adjudication, not an executable
invariant rule.

For an actual release, `./run version-check` owns the executable authority and
registered present-tense restatement sets and requires every member to agree on
the chosen version. This section deliberately delegates membership to that
executed check instead of restating a second source list. Dated historical
records are outside the current-restatement set and keep their original release
identities. A no-release close instead names the intentionally unreleased
commits and leaves every version source and tag unchanged. Tag creation, target
selection, closing-record sequencing, the historical boundary, and post-push
evidence are defined only by `AGENTS.md`'s R-CLOSE contract.
