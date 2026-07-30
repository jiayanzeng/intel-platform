# TASKS-v0.25-EXECUTION.md — admission, and the gates the model does not hold

## Runbook amendments

Declared scope — crate-wide forbids corrected to source-tree forbids — 2026-07-30

- **2026-07-30 — activation validation correction.** The first clean E0 shell
  lane executed the live active-scope control and found that the crate-wide
  `crates/ingest/**` and `crates/compliance/**` forbids overlapped their two
  enumerated Cargo release authorities in addition to the one documented
  `shell/intel_shell/app.py` overlap. The forbids now name the two source trees,
  which preserves the standing prohibition on ingest/compliance source changes
  and leaves release-authority handling explicit. Release-authority precedence
  already permitted the two manifests, so this correction broadens no
  effective path permission. No task objective, gate, acceptance criterion, or
  done condition changed.
- **2026-07-30 — G5 measured correction.** E0 confirmed that `./run golden`
  starts the core with `CORE_CONFIG=config/core.json`, but refuted the draft's
  author-side implication that any source addition therefore changes golden:
  the harness explicitly ingests and views only `science` and `technology`,
  while the proposed source is confined to `finance`. This was a runbook error,
  not an implementation defect. Step 1 item 6 and the G5 hypothesis are
  therefore narrowed to the condition golden actually executes. The existing
  11/11 definition of done and Step 5's requirement to match E0's determination
  are correct; changing either would manufacture drift rather than measure it.
- **2026-07-30 — Step 2 gate-scope correction.** Before implementation, the
  Step 2 gate was found narrower than its acceptance criteria: the task
  requires the public-value-domain criterion to be written into `AGENTS.md`,
  but the gate omitted that path. The gate now names `AGENTS.md`. The declared
  scope already allowed it, so this correction adds no repository permission
  and changes no objective, implementation condition, acceptance criterion, or
  done condition.
- **2026-07-30 — Step 5 deferral-row label correction.** Before admission, the
  active deferral row was found to say “Third configured publisher” while its
  trigger, measured state, and inherited v0.24 provenance all describe the
  reviewed **second** publisher. The row now carries its correct subject and is
  closed by Step 5; the separately deferred first live RSS harvest is added as
  Step 5 requires. No trigger, permission, objective, acceptance criterion, or
  done condition changed.
- **2026-07-30 — Step 5 trigger-test scope correction.** The first complete
  shell lanes executed the deferral-table acceptance and found the governed
  runbook-row population correctly increased from 11 to 12. Step 5 requires
  that new live-RSS deferral row but its gate did not name
  `shell/tests/test_cycle_check.py`, whose executable expectation counts it.
  The gate now names that exact test. Declared scope already permits
  `shell/tests/**`; no production, objective, acceptance, or done-condition
  permission changed.

v0.24 closed and v0.15.8 published. Release parent `696c0863…`, closing commit
`64002678…`, annotated object `dc5abe06…`, hosted run `30475988050` green on all
seven executable jobs. **The population comparator did its job on its first live
exercise**: local 283 passed, hosted 282 passed plus one named `on_site` skip,
and the two were confirmed equivalent rather than reconciled into a single
number. The false-count class was bounded to one record and corrected forward,
and retractions correctly stayed at three.

The PUBLISHER-REVIEW is the best artifact this project has produced. It fetched
a real policy through the shipped matcher — **2,622 bytes, first real robots.txt
this system has ever evaluated** — recorded a genuine `Disallow: /cgi-bin` match
on the Atom path and a default-allow on the RSS path, cited four publisher
statements verbatim by URL and date, and **contradicted the operator's own stated
expectation on the record**: the crawler identity already carries a monitored
contact. That correction is the review working.

It returned **admissible, conditional**. Admission is this cycle's subject, and
three questions have to be answered before it can happen. **None of them is
apparatus. All three are about the product.**

**The licence enum cannot express what the review found.** `License` is
`PublicDomain | CcBy | ClientOwned | IndexOnly`, and `redistributable()` is true
for the first three. The review's evidence is SEC's own statement that EDGAR
public filing content is free to access and reuse — and the review **expressly
declined** to conclude that issuer-authored filings are U.S.-government works.
So `PublicDomain` asserts a copyright-status claim the review refused to make;
`IndexOnly` is safe but forfeits the entire architectural reason for choosing
this publisher; `CcBy` and `ClientOwned` are simply false. **There is no value
meaning "the publisher expressly permits reuse under its own stated terms."**
Picking `PublicDomain` because it is closest is exactly the quiet reconciliation
this project keeps catching.

**A terms-level gate exists that the architecture does not model.** The robots
verdict for the intended path is *allow*. SEC's Internet Security Policy says it
does not allow unclassified bots or automated tools to crawl the site. Those are
two different gates. The system models robots policy and an operator deny-list;
it models nothing for a publisher's terms-level prohibition on automated access.
The review cited the statement and did not resolve it.

**And the feed has never been looked at.** No real feed was fetched, by design.
Whether `usgaap.rss.xml` contains `<item>` elements carrying the fields this
repository's RSS parser requires is unknown. Admitting a source whose
parseability has never been observed would repeat, in the ingestion path, the
mistake v0.18 corrected in the compliance path.

**Version disposition is determined by Step 2, not declared here.** `License` is
serialized into `/v1/*` response bodies as
`d.provenance.license.as_str()`. Adding a variant expands the value domain of a
public field without moving a route or a body — and the standing trigger rule
covers movement, not domain expansion. **Step 2 must decide the version, and
Step 7 must record the criterion it used.** Do not inherit a patch default; the
default has no answer for this case.

---

## Declared scope

| Scope class | Path or value |
|---|---|
| `scope_version` | `1` |
| `disposition_intent` | `release` |
| `allow` | `config/core.json` |
| `allow` | `crates/core/src/lib.rs` |
| `allow` | `crates/store/src/sqlite.rs` |
| `allow` | `shell/tests/**` |
| `allow` | `crates/**/tests/**` |
| `allow` | `observations/**` |
| `allow` | `tools/cycle_check.py` |
| `allow` | `tools/invariant_scan.py` |
| `allow` | `config/invariant-rules.json` |
| `allow` | `AGENTS.md` |
| `allow` | `ARCHITECTURE.md` |
| `release_authority` | `Cargo.toml` |
| `release_authority` | `Cargo.lock` |
| `release_authority` | `crates/*/Cargo.toml` |
| `release_authority` | `apps/*/Cargo.toml` |
| `release_authority` | `shell/intel_shell/__init__.py` |
| `release_authority` | `shell/intel_shell/app.py` |
| `release_authority` | `CHANGELOG.md` |
| `release_authority` | `README.md` |
| `forbid` | `crates/ingest/src/**` |
| `forbid` | `crates/compliance/src/**` |
| `forbid` | `apps/**/*.rs` |
| `forbid` | `shell/intel_shell/[a-z]*.py` |
| `forbid` | `config/subscriptions*.json` |

**This is the first cycle since v0.19 whose scope permits a crate source
change**, and the permission is narrow and conditional: `crates/core/src/lib.rs`
is allowed **only** if Step 2 chooses to extend the `License` enum, and
`crates/store/src/sqlite.rs` **only** if that extension requires a persistence
mapping. **If Step 2 chooses otherwise, both paths must go unmodified and Step 7
must record that the permission went unused.** The robots matcher and the
ingestion crates stay forbidden outright: nothing in this cycle touches
`crates/compliance/**` or `crates/ingest/**`.

---

## Entering state (asserted, not yet verified)

**Every sentence here is a hypothesis until Step 1 (E0) measures it.**

- `v0.15.8` is published. Release parent
  `696c0863ea684d590970902bcbbd13a7a3ccb610`, closing commit
  `64002678672a601804e5f67886c73fffb4d212c8`, annotated tag object
  `dc5abe0690e77cef671896102382427721d97321`. v0.24 is closed. **None of this is
  reopened.** Hosted run `30475988050` is the verification of record.
- Local `main` is one commit ahead at post-push audit `947822c8…`, unpushed,
  under the accepted cycle-ending rhythm.
- Local shell lanes are **283 collected / 283 passed / 0 skips**; hosted is
  **282 passed + 1 named `on_site` skip**; the comparator confirmed equivalence.
- `invariant-scan` is **39 controls**, R12 at **16**. Golden is **11/11**.
  `ci-local` is 20/20.
- `config/core.json` declares sectors `science`, `technology`, `finance`, with
  exactly one live source — `arxiv-cs`, `arxiv_oai`, `IndexOnly`,
  `robots_on_missing: allow`. The three `rss` sources all point at
  `example.org` and all have fixtures.
- The SEC review is recorded at
  `observations/v0.24/publisher-review/sec-edgar-report.md` with policy bytes at
  `sec-edgar-robots.txt`, SHA-256
  `72d6196b3f20737396e566ddeb769fb4174b44f334985a1267a59ae0f08c2f2f`.
  Recommendation: **admissible, conditional**.
- A4, the editable-L1 controller residual, the R3/R4 open-bottom deny-lists, the
  active-runbook measured-value heuristic, T7 robots single-flight, and
  NEGATIVE-CACHE Decision B remain open. L2 remains scheduled. `v0.8.0` and
  `v0.10.2` remain local-only under A/A/E. **No step in this file closes or
  narrows any of them** — **and note that admitting a second origin does not fire
  T7's trigger, which is a second concurrent *harvester*, not a second source.**

---

## Drafted gates

| Gate | Where | Hypothesis |
|---|---|---|
| **G1** [P1] | `crates/core/src/lib.rs` `License`; the review's licence section | **The enum has no value for the evidence found.** `redistributable()` is true for `PublicDomain \| CcBy \| ClientOwned`. SEC's statement is a permission to access and reuse; the review declined to assert that issuer-authored filings are government works. Confirm that no existing variant expresses "publisher-granted reuse under its own terms" without asserting a copyright status the evidence does not support. |
| **G2** [P1] | SEC Internet Security Policy; `crates/ingest`, `crates/compliance` | **A terms-level automated-access gate exists outside the model.** Robots says allow; the publisher's policy says unclassified bots are not allowed. Confirm the architecture represents only robots policy and the operator deny-list, and that no component consults publisher terms. **Then determine, with cited evidence, whether the declared contact-bearing identity satisfies the publisher's classification requirement.** A robots allow does not answer this. |
| **G3** [P1] | `https://www.sec.gov/Archives/edgar/usgaap.rss.xml`; the repository's RSS parser | **The feed's shape is unobserved.** Locate the RSS parser, enumerate the elements and fields it requires from each `<item>`, and state which are mandatory. **The feed itself is not fetched in E0** — Step 4 owns that, under a single request. |
| **G4** [P1] | `apps/cored/src/main.rs`; the version-trigger rule | **The version rule covers movement, not domain expansion.** `license` is serialized into `/v1/*` bodies from `as_str()`. Confirm every public response field carrying it, and confirm the standing rule speaks only to a route or body moving. **The gap is the finding; Step 2 decides the version and Step 7 records the criterion.** |
| **G5** [P2] | golden corpus configuration | **Whether admission perturbs golden is unknown.** Determine whether the golden E2E reads `config/core.json` or a separate fixture configuration. **If golden reads the live config, adding a source changes golden, and the global definition of done in this file is wrong and must be amended before Step 5 rather than after.** |
| **G6** [P2] | the review's recorded condition | **The condition is stated as a string, not a property.** It says to preserve the existing monitored-contact crawler identity, but the identity embeds the version — it was measured as `intel-platform/0.15.7 (…)` and the head now emits `0.15.8`. Restate the condition as the invariant it means: **a monitored contact is present**, version-independent. Confirm the identity is derived rather than literal, so a release cannot silently drop the contact. |

---

## How to run this file

Execute top to bottom, one task and one commit at a time. Follow `AGENTS.md §5`
after **every** task. Implementation and audit-record commits stay separate.

- **🤖 = Codex executes and self-verifies end to end** — no publication, no push
  to `main`, no ref creation or deletion **in the working repository**.
- **🧑 = exactly one named operator action or decision.**

**Interpretive rules, binding throughout.** An exit code of 0 from a construction
the checker never examined is **not measured**. A measurement that disagrees with
an acceptance criterion is **reported as measured**; the criterion is what gets
corrected. And **a licence classification is a claim about someone else's
rights**: where the evidence supports a narrower claim than a variant asserts,
the narrower claim wins.

**Dependency gates.** Steps 2, 3, and 4 are independent of each other and all
three block Step 5. **Step 5 runs only if all three return affirmative
determinations.** Any undetermined outcome defers admission to v0.26 — **and a
deferred admission is a complete cycle**, because the three determinations are
the substance. Step 6 is blocked by every preceding implementation step; Step 7
by Step 6.

### Cycle activation (before E0)

In a separate preparatory implementation/audit pair: confirm the worktree is
clean and record the measured refs **without asserting a literal `origin/main`
hash in `STATE.md`'s header**. Commit **only** this runbook at
`docs/cycles/TASKS-v0.25-EXECUTION.md` — including its `## Declared scope` block
— the `AGENTS.md` header moving the active declaration from v0.24 to v0.25, and
a new `docs/cycles/PROGRESS-v0.25.md`. **Local `main` already carries the
unpushed audit `947822c8…`; activation sits on top of it and does not amend,
rebase, or squash it.**

### Global definition of done

Protected hashes exact; all pins match until Step 6 adds more; **golden 11/11 —
byte-identical unless G5 shows the golden corpus reads the live configuration,
in which case Step 1 amends this line before Step 5 runs and Step 7 records the
amendment**; `./run version-check` green; zero rustc warnings on offline and net
builds; all Rust tests green; all shell tests green under Python 3.11 **and**
3.12; shell results recorded as collected / passed / skipped with every skip
named and compared by the comparator, never as a bare `N/N`; clippy, fmt,
ShellCheck, floor byte-compilation, and locked Rust 1.78 green.

---

## Deferred means deferred

| Deferred item | Unchanged trigger | Measured 2026-07-30 | v0.25 action |
|---|---|---|---|
| T7 robots single-flight | a second concurrent harvester | one harvester; ingest is sequential | **none — a second *source* does not fire this** |
| NEGATIVE-CACHE Decision B | a live transient robots outage for an admitted publisher while a usable last-known-good policy exists, plus operator authorization | no such outage observed | none |
| Postgres / pgvector / multi-host seam | unchanged | single writer, single host | none |
| A4 untrusted-shell boundary | a third-party/untrusted shell, or any claim HC1 is invariant under shell replacement | one first-party shell; no such claim made | none |
| L2 forced-command wrapper | an operator server session | no operator server session has occurred | none — remains scheduled |
| R3/R4 open-bottom coverage | a spelling outside registered vocabulary | none observed | none |
| Second configured publisher | a completed compliance review, then a separate admission decision | review complete; licence, terms, and shape gates affirmative; admission approved | **Completed by Step 5 — 2026-07-30: `sec-edgar-usgaap` admitted under `finance` without a harvest** |
| First live RSS harvest | an operator-authorized v0.26 runbook with declared live-RSS scope and fresh publisher gates | no live RSS harvest has occurred; Step 4 was observation-only | none — deferred to v0.26 |
| `v0.8.0` / `v0.10.2` publication | operator-authorized push of both exact annotated objects | not authorized | none — **no historical ref touched** |
| `--skip-local-tag-verification` removal | both historical tags published plus a passing hosted full-history `cycle-check` without the flag | tags unpublished | none — **the flag stays** |
| Manifest retention/indexing | 1 MiB manifest, or two consecutive `verify-artifacts` runs ≥1.00 s | re-measure at E0 | **Step 1 — re-measure only** |
| Version literal in `app.py` | a cycle whose declared scope permits shell source changes | literal present in production source | none — recorded, not acted on |

---

## Step 1 · E0 — Rebuild the entering state and settle six gates 🤖

**Objective.** Confirm HEAD is green and settle G1–G6, including whether this
file's own definition of done is correct.

**Gate.** Read-only repository, object, disposable-clone, and local execution
measurements plus `PROGRESS-v0.25.md` and this runbook's status records — **and
one amendment to this file's global definition of done if G5 requires it**. **No
publisher request of any kind is made in this step.** No ref created, moved, or
deleted in the working repository; `STATE.md` and `config/core.json` unedited.

**Steps.**

1. Run the full entering matrix and standalone `./run golden`, plus
   `verify-artifacts`, `cycle-check`, `checklist-audit`, `progress-check`,
   `version-check`, `invariant-scan`, and `export-check`. **Record shell as
   collected / passed / skipped and cite the comparator.**
2. **Confirm G1.** Quote `License`'s variants and `redistributable()`, and for
   each variant state what claim admitting SEC under it would assert. Set that
   against the review's cited SEC statement and its explicit refusal to treat
   issuer filings as government works.
3. **Confirm G2 in two parts.** First, show by enumeration that no component
   consults publisher terms — only robots policy and the operator deny-list.
   Second, **read the SEC Internet Security Policy and any linked classification
   or registration procedure, and record what "unclassified" means in the
   publisher's own words with URL and date.** Do not infer it.
4. **Confirm G3 without fetching the feed.** Locate the RSS parser, enumerate the
   `<item>` elements and fields it requires, and mark each mandatory or optional.
   **Step 4 owns the single request.**
5. **Confirm G4.** Enumerate every `/v1/*` response field carrying a licence
   string, and quote the standing version-trigger rule to show it speaks to
   route or body movement only.
6. **Settle G5 and act on it.** Determine whether the golden E2E reads
   `config/core.json`. **If it does, amend this file's global definition of done
   in the same commit, under a dated `## Runbook amendments` block**, and state
   what golden's expected outcome becomes. **Do not carry a known-wrong
   acceptance line into Step 5.**
7. **Confirm G6.** Show whether the crawler identity is derived from the version
   authority or written literally, and whether the contact is structurally
   guaranteed or merely present today.
8. Re-measure manifest size and `verify-artifacts` wall time. Re-verify the
   published `v0.15.8` objects and all pins.

**Acceptance criteria.** Entering matrix with both interpreters and comparator
citation · G1 stated per variant as a claim about rights · G2's model gap
enumerated **and** the publisher's own definition of "unclassified" recorded with
URL and date · G3's required `<item>` fields enumerated with no feed request
made · G4's response fields enumerated and the rule quoted · **G5 settled and the
definition of done amended in the same commit if required** · G6 answered
structurally, not by inspection of today's string · manifest and verify time
freshly measured · published objects and all pins re-verified · golden 11/11 or
the amended expectation · no publisher request made.

---

## Execution records

### E0 measured result — 2026-07-30

**Entering objects and refs.** The activation commit is `822aa54`; its scope
correction is `e1512ca`, and the correction's audit child was the measured HEAD,
`07e64626e2c79404c685d928a371138763af78f7`. The draft's entering assertion
about `main` was false: `947822c8…` is carried by the working branch, while the
local `refs/heads/main` remained
`eb2d9df8b3ffd3e0380d506e958fb5a3adb2d42e`. A live `git ls-remote` measured
`origin/main=64002678672a601804e5f67886c73fffb4d212c8`,
`refs/tags/v0.15.8=dc5abe0690e77cef671896102382427721d97321`, and
`refs/tags/v0.15.8^{}` equal to that remote-main commit. Local object inspection
confirmed that the tag ref is an annotated `tag`, peels to closing commit
`64002678672a601804e5f67886c73fffb4d212c8`, and that closing commit's parent is
release commit `696c0863ea684d590970902bcbbd13a7a3ccb610`. No ref was
created, moved, or deleted.

**Clean shell populations and comparator.** Both repository-local environments
were deleted and rebuilt from the constraints before measurement:

- Python 3.11.4: collected 283, passed 283, failed 0, skipped 0.
- Python 3.12.13: collected 283, passed 283, failed 0, skipped 0.
- `python3 tools/test_population.py compare
  /private/tmp/intel-v025-e0-py311.log
  /private/tmp/intel-v025-e0-py312.log` returned
  `collected=283`, `equivalent=true`, `equivalent_passed=283`, local passed 283
  and skipped 0, comparison passed 283 and skipped 0. The tool's
  machine-readable field is named `hosted`, but this E0 comparison input was
  the local Python 3.12 lane, not a hosted run. Both lanes emitted the same one
  accepted `StarletteDeprecationWarning`; neither emitted a test skip.

The first 3.11 lane exposed the declared-scope overlap described in the
activation-validation amendment above. After the scope correction, a sandboxed
run also produced eight loopback/process-inspection failures and was treated as
not measured; the clean unsandboxed entry-point run above is the recorded lane.

**Entering command matrix.**

| Command | Measured result |
|---|---|
| `./run ci-local` | PASS, all 20 jobs |
| workspace locked check/test with `-D warnings` | PASS, 0 rustc warnings; 133 tests passed |
| net locked check/test with `-D warnings` | PASS, 0 rustc warnings; ingest 29 and cored 26 tests passed |
| `cargo clippy ... -D warnings`; `cargo fmt --check` | PASS; PASS |
| Rust 1.78 locked check/test | PASS; PASS |
| shell pytest | 283 collected / 283 passed / 0 skipped |
| `./run golden` inside the matrix | PASS, 11/11 |
| protected artifacts; persisted fingerprints | 2/2 match; 1/1 stored fingerprint matches |
| `./run golden` standalone | PASS, 11/11, byte-identical expected outcome |
| `./run cycle-check` | PASS, active v0.25 open, 22 closed execution cycles and 3 historical cycles |
| `./run checklist-audit` | PASS, 191 checked, 3 retracted, 191 matched/resolved, 0 exemptions |
| `./run progress-check` | PASS, latest entry `ACTIVATE-CORRECTION` cites `e1512ca` |
| `./run version-check` | PASS at 0.15.8, with the expected ahead-of-tag warning |
| `./run invariant-scan` | PASS, 12/12 rules and 39/39 planted controls |
| `./run export-check` from the project root | PASS, 94 derived sources, 7 required, 163 exported |

**G1 — licence claims.** `License` is exactly `PublicDomain | CcBy |
ClientOwned | IndexOnly`; `redistributable()` is true only for the first three.
Admitting the reviewed SEC feed under each value would assert:

| Variant | Rights claim admission would make | Fit to evidence |
|---|---|---|
| `PublicDomain` | the issuer-authored filing text is public-domain material | Rejected: the v0.24 review expressly declined to turn the SEC's reuse permission into a government-authorship/public-domain claim |
| `CcBy` | the text is offered under a Creative Commons Attribution licence | Unsupported: the cited SEC statement names no CC licence |
| `ClientOwned` | the subscriber owns the text | False for public issuer filings |
| `IndexOnly` | analysis/indexing is allowed but raw text must not be redistributed | Safe as a restriction, but it deliberately forfeits the publisher's express statement that EDGAR public filing content is free to access and reuse |

The cited evidence says that government-created SEC content **and EDGAR public
filing content** are free to access and reuse; it does not say all filing text
is government-authored. G1 is confirmed: no existing variant expresses
publisher-granted reuse under the publisher's own terms without inventing a
copyright status.

**G2 — the terms-model gap and the publisher's wording.** Production has exactly
two policy inputs at this boundary:

1. `RobotsCache` fetches, parses, caches, and evaluates the publisher's
   `robots.txt`.
2. `RobotsGate` applies the operator-configured deny-list on top, subtracting
   from the publisher result.

`intel_ingest::gate` composes those two decisions. No production component
fetches, parses, stores, accepts, registers against, or evaluates publisher
terms. `SourceKind::CompliantCrawl`'s “ToS-compliant” comment is a label, not an
executed terms gate.

The committed v0.24 publisher review records the SEC Privacy Information page's
Internet Security Policy on 2026-07-30:
<https://www.sec.gov/about/privacy-information>. Its own operative sentence is
that the SEC does not allow “unclassified” bots or automated tools to crawl the
site. The SEC Webmaster FAQ, read and cited on the same date,
<https://www.sec.gov/about/webmaster-frequently-asked-questions>, separately
directs programmatic downloaders to declare their User-Agent in request
headers; its published sample identifies the organization and an administrative
contact at that organization's domain. The Developer Resources “Fair Access”
page, <https://www.sec.gov/about/developer-resources>, separately publishes the
ten-requests-per-second ceiling.

Those publisher texts do not supply a separate glossary definition or a
registration transaction explicitly equating “unclassified” with a named
state. E0 therefore records the publisher's own operational classification
procedure—declare an organization-and-contact User-Agent—and does not infer a
broader definition. Step 3 must determine whether the existing construction
satisfies that published direction; there is no executed project control that
can decide it. E0 re-read committed evidence and search-indexed publisher text
only and made no request to a publisher origin.

**G3 — RSS parser contract, without a feed request.** The parser requires
well-formed XML to return successfully and iterates descendant elements whose
local name is `item`. Zero `<item>` elements is a successful empty result. No
per-item field is syntactically mandatory:

| `<item>` child | Parser treatment |
|---|---|
| `title` | optional; absent becomes the empty string |
| `guid` | optional; absent falls back to `title`, so both absent yield source id plus an empty suffix |
| `pubDate` | optional; absent or unparsable yields no `published_day`, while the raw value is retained when present |
| `link` | optional; absent yields no URL |
| `description` | optional; absent becomes an empty body |
| `author` | optional; absent yields an empty author vector, present yields one value |

Thus the Step 4 “mandatory fields” list is empty; item count and the presence
counts for these optional fields are still material observations. No feed URL
was requested.

**G4 — public licence-string carriers and version gap.** The public shell
surfaces are:

- `/v1/signals`: each `signals[].evidence[].license`;
- `/v1/search`: each `hits[].license`;
- `/v1/ask`: each `citations[].license`;
- `/v1/brief`: the plaintext withheld-excerpt line can include the licence
  string, although a newly redistributable variant normally takes the
  excerpt-present branch.

The billing routes carry no licence string. Core-internal `/sectors`,
`/retrieve`, and `/docs` also serialize licence strings across the loopback
seam but are not public `/v1/*` response fields.

`ARCHITECTURE.md §8` says that adding, removing, renaming, or incompatibly
reshaping an observable route, response body, schema, or other named surface
requires the corresponding minor release; a correctness or behavior fix within
existing names and shapes uses a patch. It does not classify a compatible
expansion of an existing string enum's value domain. G4 is confirmed: Step 2
must write that criterion before choosing the release class.

**G5 — golden reads live config but excludes this sector.** `./run golden`
exports `CORE_CONFIG=config/core.json`. Its executable ingest and view calls
then name only `science` and `technology`; the proposed source is under
`finance`. A finance-only admission therefore cannot enter the golden corpus.
The measured expectation remains exactly 11/11. The dated amendment above
corrects the draft's false implication; no golden definition-of-done change is
required.

**G6 — identity construction.** `crawler_user_agent(version, contact)` formats
the structural product token, its `version` argument, and the contact.
Net-enabled `cored` passes `env!("CARGO_PKG_VERSION")`, so the identity follows
the package version authority rather than a written version literal.
`required_crawler_contact` trims and requires the environment value, rejects an
empty value and the registered `example.com`, `you@`, and `changeme`
placeholders, and a net-enabled startup panics before bind if construction
fails. A non-placeholder contact-bearing identity is therefore structural for
every live process. Whether that address is actively monitored is an operator
fact, not something source can prove; v0.24 measured it for that preview.

**Artifact scale and integrity.** `config/protected-artifacts.json` is 145,541
bytes. Two consecutive `/usr/bin/time -p ./run verify-artifacts` invocations
both passed at 0.09 seconds, below both retention triggers. Manifest schema 2
validated with 251/251 pinned files, and protected `data/core.db` and
`data/live-smoke.db` matched byte hashes and corpus facts (2/2). The published
objects above and every pin were re-verified. `STATE.md`, `config/core.json`,
the protected corpus, and refs remained untouched. No publisher request of any
kind was made by E0.

### LICENSE-SEMANTICS measured result — 2026-07-30

**Decision and rights claim.** The operator selected `extend/minor`.
`PublisherPermitted` means the publisher expressly permits reuse under its own
stated terms and makes no claim about underlying copyright. `PublicDomain`
remains excluded because the SEC evidence does not establish that
issuer-authored filings are government works. `CcBy` would invent a Creative
Commons grant, `ClientOwned` would falsely assert subscriber ownership, and
`IndexOnly` would record a restriction opposite to the publisher's measured
reuse permission. The selected variant fills a missing ground in the existing
licensing taxonomy rather than adding a new axis.

**Version and criterion.** The operator selected minor, making the release
identity **v0.16.0** independently of whether later terms or feed-shape gates
defer admission. The exact operator-supplied symmetric public-value-domain
criterion is now in `AGENTS.md`; `ARCHITECTURE.md §8` reconciles it. Adding,
removing, or redefining a value of a field already serialized in a `/v1/*`
response takes a minor release even when route, field name, field type, and body
shape do not move, because exhaustive value handling is part of the consumer's
contract. Patch is available only when every public field's value set is
unchanged.

The criterion is prose adjudicated at R-CLOSE. Step 2 step 5 produced **no new
invariant rule** because the registered scanners cannot observe that semantic
release-classification judgment. Counts remain exactly **12 rules / 39
controls** here, in `STATE.md`, and in the Step 2 progress entry; no R12
mutation was added.

**Implementation and existing behavior.** `PublisherPermitted` is
redistributable, and `as_str()` returns exactly `"PublisherPermitted"`;
`parse()` accepts that same spelling. `redistributable()` is now an exhaustive
match, so a future variant cannot silently inherit a false outcome. The focused
core control enumerates all five values and proves every spelling, parse result,
redistribution result, and attestation result: the existing three
redistributable values remain true and unblocked, `IndexOnly` remains false and
refused, and the new value is true and unblocked.

**Persistence and compatibility.** Inspection confirmed that SQLite's
`license TEXT NOT NULL` has no `CHECK`, writes already use `as_str()`, and
document/search hydration already uses `License::parse`. No production mapping
or schema edit was required; `crates/store/src/sqlite.rs` is byte-unchanged and
its conditional scope permission is recorded as unused. A new integration test
under `crates/store/tests/**` writes, reads, and searches
`PublisherPermitted`, confirms the raw stored text, then plants
`FutureLicense`. The unchanged fallback reads that unknown value as
`IndexOnly` and suppresses its search snippet.

The opposite boundary was exercised through the actual offline `cored` entry
point. A temporary config using `PublisherPermitted` reached successful server
startup. The same config with `FutureLicense` exited 101 at deserialization,
naming the five accepted variants. Config unknowns are therefore loud; stored
unknowns are silent and safely restrictive. This means an older binary reading
a newer archive can silently reclassify publisher-permitted documents as
`IndexOnly`, and the property is now recorded in both directions.

**Release-name collision.** Live remote inspection measured the pre-existing
`refs/heads/candidate/v0.16.0` at
`3481e4ba85d65c927b7d0fc3a430bc04fb094394` and no `v0.16.0` tag. The branch
predates this release and is the v0.15.1 evidence candidate. Seven immutable
Sigstore-bundle provenance entries and the pinned v0.15.1 deferred-audit report
preserve that source ref across eight evidence subjects. It was not renamed,
deleted, or moved; Step 7 must state explicitly that it does not belong to this
release.

**Deferred release documentation and admission independence.** `README.md`'s
four-value config-schema enumeration became stale when the variant landed. It
is a release authority outside this step's gate and remains assigned to Step 7
step 10. `config/core.json` is unchanged, so zero configured sources currently
produce `PublisherPermitted` and no `/v1/*` response can carry it. If Step 3 or
Step 4 defers admission, that is the close-time fact rather than a shortfall;
the enum and minor release still ship.

**Acceptance matrix.** The complete `./run ci-local` passed all **20** jobs:
workspace **135**, net **55** (**29** ingest + **26** cored), warning-denied
current and locked Rust 1.78 lanes, clean clippy/fmt/ShellCheck, shell Python
3.11 **283 collected / 283 passed / 0 skipped**, `invariant-scan` **12/12
rules / 39 controls**, all **251** pins, protected databases **2/2**, and
embedded golden **11/11**. Independent Python 3.12 passed **283 collected /
283 passed / 0 skipped** with the same accepted third-party warning. Mandatory
standalone golden passed **11/11**, delta **0**. No dependency, lockfile,
configured source, shell source, schema, protected artifact, publisher request,
feed request, or ref changed.

### TERMS-GATE measured result — 2026-07-30

**Gate coverage.** Before the determination was recorded, every acceptance
criterion was mapped to the existing gate: the dated publisher observation is
under `observations/v0.25/**`, the terms-model disposition is in
`ARCHITECTURE.md`, and this execution record, `STATE.md`, and the progress log
are status records. No criterion required code, config, schema, or a widened
path.

**Publisher text and robots result.** The committed v0.24 wire evidence records
the shipped matcher's **allow** verdict for
`/Archives/edgar/usgaap.rss.xml`. The SEC Privacy Information page, read on
2026-07-30 at <https://www.sec.gov/about/privacy-information>, states that the
SEC does not allow “unclassified” bots or automated tools to crawl the site.
The SEC Webmaster FAQ, read and cited on the same date at
<https://www.sec.gov/about/webmaster-frequently-asked-questions>, directs
programmatic downloaders to declare their User-Agent and supplies an
organization-and-administrative-contact example. The publisher supplies no
separate glossary or registration transaction; its published operational
classification procedure is the organization-and-contact declaration. A
robots allow is not treated as the answer to this terms question.

**Determination and property.** **Affirmative.** On 2026-07-30 the operator
accepted the recommended affirmative determination and its premise that the
configured contact is monitored. The version-independent condition is: **a
monitored contact is present in the crawler identity**. E0 proved that every
net-enabled startup structurally requires a trimmed, non-empty,
non-placeholder contact before bind and derives the identity version from the
package authority. Monitoring is operator evidence, not source evidence; the
operator confirmed it. There is therefore no structural contact defect to fix
or assign forward.

**Terms-model disposition.** `ARCHITECTURE.md` records the dated disposition:
publisher terms compliance remains a publisher-specific operator
responsibility outside the executable model. The SEC condition is
natural-language policy with no stable machine-readable classification or
registration state, so a third runtime boolean would pretend to automate a
judgment the system cannot observe. Runtime continues to enforce the
publisher's fetched `robots.txt` and the operator deny-list; dated operator
review owns the separate terms decision before admission.

**Limits and boundary.** This determination binds the SEC, the reviewed
`/Archives/edgar/usgaap.rss.xml` path, the cited texts, and 2026-07-30. It is
not a general finding about government or regulatory sources and does not
establish feed shape. Step 3 made **zero publisher requests**, made no code,
config, schema, protected-artifact, or ref change, and leaves Step 4's single
live feed GET separately gated.

**Acceptance execution.** `cycle-check` passed with the new dated architecture
row. Diff inspection found only `ARCHITECTURE.md`, the v0.25 observation, and
status records; all code and config paths were byte-unchanged. The first
sandboxed `./run golden` attempt could not bind loopback and exited before
startup with `Operation not permitted`. The authorized rerun of the identical
entry point passed **11/11**, delta **0**.

### FEED-SHAPE measured result — 2026-07-30

**Gate coverage and preflight.** Every acceptance criterion fits the existing
gate: the raw policy, feed body, and report are under
`observations/v0.25/**`; this record, `STATE.md`, and the progress log are
status records. No criterion requires code, config, schema, protected database,
or public-surface changes. E0 confirmed G3 and Step 3 was affirmative. Before
the wire action, `python3 tools/evidence_artifacts.py validate` and
`./run verify-artifacts` passed with all **251** pins and both protected
databases exact, port 8788 was free, the worktree was clean, and neither output
file existed.

**Fresh robots decision.** At **2026-07-30T03:33:58Z**, exactly one
`GET https://www.sec.gov/robots.txt` ran through the shipped
`HttpRobotsFetcher`, `RobotsCache`, and `RobotsGate`; the cache and recording
wrapper both counted **1**. The fresh **2,622-byte** body has SHA-256
`72d6196b3f20737396e566ddeb769fb4174b44f334985a1267a59ae0f08c2f2f`
and is byte-identical to v0.24. Publisher and operator gates both allowed
`/Archives/edgar/usgaap.rss.xml`, with a **0.500-second** effective interval
and redirects disabled.

**Single feed request.** Only after the policy comparison and allow decisions,
at **2026-07-30T03:34:00Z**, the monitored-contact
`intel-platform/0.15.8` identity made exactly one redirect-disabled, no-retry
GET of `https://www.sec.gov/Archives/edgar/usgaap.rss.xml`. Request count was
**1**. The response was HTTP **200**, `Content-Type: text/xml`, with no
`Location` header and a **892,641-byte** body. SHA-256 is
`154556cd81bda4fc2372386bf43aa7b4414335560dd1371c45bae09f1a8d9de3`.
Step 4 made no other publisher request.

**Item and field presence.** Independent offline XPath inspection counted
**200** `<item>` elements. E0's mandatory-field list is empty. For completeness,
the six optional parser fields measured:

| Field | Items with field | Non-empty | Presence |
|---|---:|---:|---|
| `title` | **200/200** | **200/200** | every |
| `guid` | **200/200** | **200/200** | every |
| `pubDate` | **200/200** | **200/200** | every |
| `link` | **200/200** | **200/200** | every |
| `description` | **200/200** | **200/200** | every |
| `author` | **0/200** | **0/200** | none |

The empty mandatory set is satisfied, so FEED-SHAPE is affirmative and Step 5
may reach its separate admission decision.

**Derived parser behavior, not execution.** The repository parser was not run
against the body. Derived from E0's source enumeration only: if the XML is
accepted, the parser sees 200 candidate items, uses present values for
`title`, `guid`, `link`, and `description`, retains each raw `pubDate` while
conditionally deriving its day, and emits an empty author vector for every
item. Independent counting is not reported as repository-parser success.

**Storage, limits, and golden.** The body, fresh policy, and report remain only
under `observations/v0.25/feed-shape/`; they are not fixtures, protected-corpus
admissions, configured-source inputs, or golden inputs. One request establishes
nothing about paging, resumption-token equivalents, cursor durability,
near-duplicate behavior, repeated-fetch politeness, conditional requests, or a
live ingest. No code, config, schema, protected artifact, database, public
surface, or ref changed. Mandatory standalone `./run golden` passed **11/11**,
delta **0**.

### ADMIT measured result — 2026-07-30

**Admission decision and binding conditions.** The operator approved
`sec-edgar-usgaap` under `finance`, at the reviewed
`https://www.sec.gov/Archives/edgar/usgaap.rss.xml` path, classified
`PublisherPermitted`. The source remains bound to the reviewed path, the
monitored-contact crawler identity, fresh publisher-robots plus operator
deny-list enforcement, and total automated traffic at or below the SEC's
then-current published ceiling.

`robots_on_missing` is explicitly `"deny"`. SEC serves a policy today, so
policy absence is not the reviewed condition and fails closed; arXiv's
publisher-specific 404 exception was not copied. The focused config control
pins the exact sector, id, RSS type, URL, licence, conservative missing-policy
value, and global source-id uniqueness. Its fail-before run found no matching
source and failed; after admission it passed.

**No live harvest and exact limits.** Step 5 made no publisher request.
Admission proves that two publisher origins are configured and that the exact
SEC declaration is controlled. Only `arxiv-cs` has ever been harvested. The
production origin-keyed robots cache and per-host limiter have never handled
both origins in one runtime. Live RSS fetching, repository parsing of the
observed SEC body, paging, repeated-fetch behavior, near-duplicate behavior,
and cursor durability remain unmeasured. The first live RSS harvest is a new
deferral row whose trigger requires an operator-authorized v0.26 runbook with
declared live-RSS scope; the second-publisher admission row closed on
2026-07-30.

**Shell population and scope finding.** The first complete rebuilt shell lanes
each collected **284**, passed **283**, and failed the same trigger-freshness
control because the Step 5-required deferral row correctly increased the
governed runbook-row population from 11 to 12. That acceptance criterion
therefore required `shell/tests/test_cycle_check.py`, which the original Step 5
gate did not name. The dated amendment above widened the gate to that exact
already-declared test path before its expected count changed. Focused config and
trigger controls passed **2/2**; clean Python 3.11 and 3.12 lanes then each
passed **284/284**, with zero skips and the same one accepted third-party
warning. `python3 tools/test_population.py
/private/tmp/intel-v025-admit-py311.log
/private/tmp/intel-v025-admit-py312.log` derived `collected=284`,
`equivalent=true`, `equivalent_passed=284`, local passed 284/skipped 0 and
comparison passed 284/`on_site` skipped 0. The machine field is named `hosted`,
but the second input here is the local Python 3.12 lane, not hosted evidence.
The draft command's nonexistent `compare` subcommand failed argument parsing;
the recorded successful invocation is the tool's actual entry point.

**Regression and protected evidence.** Mandatory standalone `./run golden`
passed **11/11**, delta **0**, as E0 predicted for the finance-only source.
Manifest schema 2 validated; `./run verify-artifacts` found all **251** pins and
both protected databases exact. `invariant-scan` remains **12/12 rules and
39/39 planted controls**. The complete `./run ci-local` passed all **20** jobs
at the admitted configuration: workspace 135, net 55 (ingest 29 + cored 26),
warning-denied current and locked Rust 1.78 lanes, clean
clippy/fmt/ShellCheck, shell 284/284, and embedded golden 11/11. No protected
corpus, pin, database, schema, dependency, lockfile, ingest source, compliance
source, shell production source, public response, tag, or branch moved.

### RE-MEASURE measured result — 2026-07-30

**Neutral candidate and hosted identity.** The operator authorized the Step 6
gate. Exact candidate
`779fbe55ba33dd5d196df391cc9a9eeb3ce0bbb3` was pushed to neutral ref
`refs/heads/codex/v0.25-evidence-779fbe5`; the name encodes neither a version
identity nor a patch assumption. The remote branch's
`.github/workflows/ci.yml` blob
`48ea726b798f1049e0b29cce1f0c64588861c2dd` matched the local candidate
blob before dispatch. Authenticated hosted run **30513561141**, attempt **1**,
then passed all seven executable jobs at that exact candidate.

**Measured populations and absence of a publisher request.** Hosted counts
were workspace **135**, net **55** (`intel-ingest` **29** + `cored` **26**),
locked Rust 1.78, clean rustc/clippy/fmt/ShellCheck, lifecycle **196 checked /
3 retracted / 196 matched / 0 exemptions**, `invariant-scan` **12/12 rules /
39 controls** with R10 **45** exemptions, and golden **11/11**. The comparator
derived the same exact result for Python 3.11 and 3.12:
`collected=284`, `equivalent=true`, `equivalent_passed=284`, local passed
**284 / skipped 0**, hosted passed **283** plus one named `on_site` skip. The
skip node was
`tests/test_deferred_audit.py::test_on_site_production_measurements_match_committed_receipt`;
its reason was “on-site production audit requires protected corpora and built
cored”. The workflow contained no harvest command, and a case-insensitive
search of the complete hosted log for `sec.gov`, `usgaap.rss`,
`harvest-arxiv`, `POST /ingest`, or an HTTP GET returned no matches. No hosted
job made a publisher request.

**Authenticated admission and release posture.** The seven receipt JSON files
and seven Sigstore bundles are committed under
`evidence/ci-runs/30513561141-1/`. Release-posture
`./run audit-deferred` required attestations, accepted **7 / rejected 0**
identities, confirmed the single-run matrix complete, and recorded **5 deferred
/ 2 promoted / 0 implemented deferred subsystems**. The largest evidenced
archive remains **2,600 documents**; exact-cosine p95 was **8.640 ms**, below
the **16.264 ms** A3 request anchor. The **34,881-byte** report at
`evidence/v0.25/deferred-audit/report.json` has SHA-256
`9d7c367060d2c9f28aaf17586f7e54ab782f6f8113b64326d730cccb05cfb342`.
`./run audit-deferred --rederive` reproduced it with attestations required.

The fourteen signed hosted files plus the report add fifteen schema-v2
manifest records, moving the protected count from **251** to **266** pins.
`python3 tools/evidence_artifacts.py validate`, `./run verify-artifacts`, and
`./run evidence-report` passed; both protected databases remained exact.
Standalone `./run golden` passed **11/11**, delta **0**, and local
`invariant-scan` passed **12/12 rules / 39 controls**.

**Remote disposition.** Read-only post-dispatch resolution found remote
`main` unchanged at `64002678672a601804e5f67886c73fffb4d212c8`, the
pre-existing `refs/heads/candidate/v0.16.0` unchanged at
`3481e4ba85d65c927b7d0fc3a430bc04fb094394`, and the neutral evidence ref
still at the exact candidate. No `v0.16.0` tag exists. Step 6 created no tag,
advanced no release ref, and changed no source, public surface, dependency,
lockfile, schema, or protected database. Step 7 remains behind its separate
operator publication decision.

---

## Step 2 · LICENSE-SEMANTICS (G1, G4) — Say only what the evidence supports 🧑🤖

**Objective.** Decide how SEC content would be classified, and what version that
decision implies.

**Gate.** 🧑 **One operator decision, at step 1.** Scope is
`crates/core/src/lib.rs` and `crates/store/src/sqlite.rs` **only if the decision
requires them**, their tests, `AGENTS.md`, `ARCHITECTURE.md`, and status
records. **Blocked on E0 confirming G1.** No ingest, compliance, shell source,
`config/core.json`, schema-breaking, or protected-database changes.

**Steps.**

1. **🧑 Choose exactly one, and record the claim each would make:**
   - **Extend the enum** with a variant meaning *the publisher expressly permits
     reuse under its own stated terms*, redistributable, asserting nothing about
     underlying copyright. **Cost:** a new value in a public response field, a
     persistence mapping, and a version question — and every downstream consumer
     switching on licence must handle it.
   - **Admit under `IndexOnly`.** **Cost:** forfeits the permissive branch of
     HC1 against real content, which was the measured reason this publisher was
     chosen over another OAI-PMH source. Say so plainly rather than treating it
     as the conservative default.
   - **Do not admit.** A complete outcome, and the right one if neither of the
     above can be justified from the cited evidence.
   **`PublicDomain` is not on this list.** The review declined to assert that
   issuer-authored filings are government works, and a classification may not
   assert what the review refused to.
2. **Decide the version and state the criterion.** If the enum is extended, the
   value domain of a public field expands without any route or body moving. The
   standing rule does not cover this. **Choose minor or patch, write the
   criterion into `AGENTS.md` so the next value-domain change is not
   re-litigated, and register it.**
3. If extending: add the variant, its `as_str`/`parse` mappings, its
   `redistributable()` membership, and the persistence mapping — **and prove by
   test that every existing licence's gating behaviour is unchanged.** A new
   variant must not perturb `IndexOnly` suppression or `PublicDomain`
   redistribution.
4. **Do not change `config/core.json` in this step.** The enum and the admission
   are separate decisions and separate commits.
5. Register any new rule as an R12 planted-failure mutation and report counts in
   three places.

**Acceptance criteria.** Exactly one option chosen and dated, with the rights
claim it makes recorded · `PublicDomain` excluded with its reason · version
decided with a written criterion added to `AGENTS.md` · if extended: mappings,
`redistributable()` membership, persistence, and a test proving existing gating
unchanged · `config/core.json` untouched · if not extended, the scope permission
recorded as unused · counts in three places · golden 11/11 or the amended
expectation.

---

## Step 3 · TERMS-GATE (G2, G6) — A robots allow is not a terms allow 🧑🤖

**Objective.** Determine whether the publisher's automated-access terms permit
this crawler, and decide whether the architecture should represent terms-level
gates at all.

**Gate.** 🧑 **One operator determination, at step 2.** Scope is
`observations/v0.25/**`, `ARCHITECTURE.md`, and status records. **Blocked on E0
confirming G2.** **No code change of any kind, and no publisher request beyond
reading published policy pages.**

**Steps.**

1. Restate E0's finding: robots verdict *allow* for the intended path, publisher
   policy prohibiting unclassified automated tools, and the publisher's own
   definition of the term with its citation.
2. **🧑 Determine whether the declared contact-bearing identity satisfies the
   publisher's requirement**, citing the publisher's text. **An honest
   undetermined is a complete outcome and defers admission** — do not resolve an
   ambiguity in the project's own favour because admission is the cycle's goal.
3. **Restate the review's condition as a property, per G6**: a monitored contact
   is present in the crawler identity, version-independent. If E0 found the
   contact is not structurally guaranteed, **name that as a defect and assign it
   forward** — do not fix it here, because `crates/ingest/**` is out of scope.
4. **Decide whether terms-level gates belong in the model.** Options: record it
   as an operator responsibility outside the system with a stated reason; or name
   a trigger under which the architecture would represent it. **Do not build it
   in this cycle.** Whichever is chosen goes in `ARCHITECTURE.md` as a dated
   disposition with a measured observation, per v0.23's rule.
5. Record what this determination does not establish: it binds one publisher on
   one date, and it is not a general finding about government or regulatory
   sources.

**Acceptance criteria.** Publisher text cited with URL and date, not inferred ·
determination recorded as affirmative, negative, or undetermined, with
undetermined accepted as complete · condition restated as a version-independent
property · any structural contact defect named and assigned forward, not fixed ·
terms-level-gate disposition dated with a measured observation in
`ARCHITECTURE.md` · no code change · golden 11/11 or the amended expectation.

---

## Step 4 · FEED-SHAPE (G3) — Look at it once, before admitting it 🤖🧑

**Objective.** Observe the feed's actual structure against the parser's stated
requirements, without ingesting anything.

**Gate.** 🧑 **One narrow authorization: a single live GET of the intended feed
URL.** Scope is `observations/v0.25/**` and status records. **Blocked on E0
confirming G3 and on Step 3's determination being affirmative** — **do not
request the feed if the terms determination is negative or undetermined.** No
code, config, schema, protected-database, or public surface changes.

**Steps.**

1. **Re-evaluate the robots policy first**, through the shipped matcher, exactly
   as the v0.24 review did. **A policy fetched on 2026-07-30 does not authorize a
   request on a later date.** Record the fresh bytes, hash, and verdict, and
   compare the hash to `72d6196b…`. **If the policy changed, stop and record
   it** — a changed policy is a finding, not a formality.
2. Issue **exactly one** GET of `/Archives/edgar/usgaap.rss.xml`, with the
   contact-bearing identity, within the operator rate floor. **One request. Not a
   paging walk, not a cursor test, not a second attempt on a non-error
   response.**
3. Record: HTTP status, content type, byte size, SHA-256, and the count of
   `<item>` elements. **For each field E0 marked mandatory, record whether it is
   present in every item, some items, or none** — with the counts.
4. **Record what the parser would do**, derived from E0's enumeration, **without
   running it against the body.** Whether the feed parses is a claim for
   admission to test, not for this step to assert.
5. Store the body under `observations/v0.25/`. **Do not add it to
   `fixtures/`, do not admit it to the protected corpus, and do not let it
   influence golden.** It is an observation.
6. Record what this does not establish: nothing about paging, `resumptionToken`
   equivalents, cursor durability, near-duplicate behaviour, or repeated-fetch
   politeness. **One request measures shape and nothing else.**

**Acceptance criteria.** Robots re-evaluated fresh with hash compared to the
v0.24 policy and any change recorded as a finding · exactly one feed request,
evidenced by a request count · status, type, size, hash, and item count recorded
· per-field presence recorded with counts against E0's mandatory list · parser
behaviour derived, not executed · body stored as an observation and excluded from
fixtures, corpus, and golden · non-establishment stated · golden 11/11 or the
amended expectation.

---

## Step 5 · ADMIT — The second publisher 🧑🤖

**Conditional. Runs only if Step 2 chose a redistributable-or-IndexOnly
classification, Step 3's determination is affirmative, and Step 4 found the
mandatory fields present. If any is otherwise, delete this step, record the
deferral with the determination that caused it, and close the cycle on the three
determinations — which is a complete outcome.**

**Objective.** Add the first second publisher this system has ever configured.

**Gate.** 🧑 **One operator admission decision.** Scope is `config/core.json`,
tests covering the new source's configuration,
`shell/tests/test_cycle_check.py`, `ARCHITECTURE.md`, and status records. **No
ingest, compliance, or shell source change. No live harvest.**

**Steps.**

1. 🧑 Record the admission decision, naming the reviewed path, the classification
   Step 2 chose, the sector, and the conditions from the review that now bind.
2. Add the source to `config/core.json` under `finance`, with the reviewed URL,
   the chosen licence, and an explicit `robots_on_missing` value. **State why
   that value was chosen** — SEC serves a policy today, so the missing-policy
   branch should be the conservative one and the record must say so rather than
   copying `arxiv-cs`'s `allow`.
3. **Do not run a live harvest.** Admission configures the source; it does not
   fetch it. **The first live RSS harvest is v0.26's subject and needs its own
   declared scope**, exactly as the first live OAI-PMH harvest got v0.18.
4. **Record precisely what admission has and has not exercised.** Two origins are
   now *configured*; the origin-keyed robots cache and the per-host limiter have
   still never seen two origins **at runtime**, because nothing has run. Live RSS
   fetching, feed parsing, and cursor durability remain untested.
5. Confirm golden's outcome matches E0's G5 finding — unchanged, or the amended
   expectation — and that no protected corpus or pin moved.
6. Update the deferral table: the live-RSS-harvest row appears with its trigger,
   and the second-publisher row closes with its date.

**Acceptance criteria.** Admission decision recorded with path, classification,
sector, and binding conditions · source added with an explicitly reasoned
`robots_on_missing` · **no live harvest performed** · what admission does and
does not exercise stated precisely · golden matches E0's determination · no
protected corpus or pin moved · deferral table updated both ways · shell recorded
by the comparator.

---

## Step 6 · RE-MEASURE 🤖🧑

**Objective.** Produce release-grade hosted evidence for the v0.25 candidate.

**Gate.** 🧑 **One narrow authorization: a non-`main` branch push.** Remote
mutation is limited to the exact candidate branch and its authenticated hosted
evidence dispatch. Repository admission is limited to that run's signed
receipt/bundle pairs, the release-posture deferred-audit report,
`config/protected-artifacts.json`, and status records. No tag, `main` advance,
publication, source, public surface, dependency, lockfile, schema, or protected
database changes.

**Steps.**

1. Push the candidate to a **neutral branch name that does not prejudge Step 7's
   disposition** — and note that Step 2 may have set a minor version, so the name
   must not encode a patch assumption either.
2. **Read the remote branch's `ci.yml` and confirm its blob equals the local
   one before dispatching.**
3. Dispatch with `publish_evidence: true` and `audit_sha` set to the candidate.
4. **Cite the comparator's output for the shell lanes**; read every other count
   from the log and compare at the same commit. **Never transcribe.**
5. **Confirm the hosted run makes no publisher request.** The admitted source is
   configured, not harvested; a hosted job reaching `sec.gov` would be a
   compliance event and must stop the step.
6. Record the hosted `invariant-scan` rule and control counts; any rule Step 2 or
   3 added must be detected here.
7. **Record this run id prominently** — under the tagged close it is the evidence
   the closing record cites.
8. Commit the signed receipt/bundle set, re-run `./run verify-artifacts` and
   `./run evidence-report`, and record the new pin count in three places.
9. Run `./run audit-deferred` in release posture with attestations required.

**Acceptance criteria.** Hosted run on a neutral branch not encoding a version
assumption · remote `ci.yml` blob confirmed · shell compared by comparator, all
other counts equal at that commit · **no publisher request made by any hosted
job, confirmed** · hosted `invariant-scan` counts recorded · run id recorded as
citable closing evidence · signed set committed and re-derived · pin count in
three places · `origin/main` unchanged, no tag · golden per E0's determination.

---

## Step 7 · R-CLOSE 🧑🤖

**Objective.** Close the cycle under the tagged-close protocol.

**Gate.** Steps 1–6 complete and boxed, with Step 5 either complete or recorded
as conditionally deferred. Worktree clean. **🧑 One operator decision:
publication.**

**Steps.**

1. **Follow the Option C tagged-close protocol as `AGENTS.md` states it.**
2. Re-run the complete definition of done at the release parent and capture it.
3. **Record the version and the criterion Step 2 wrote**, not the standing
   default — and record that the standing rule had no answer for value-domain
   expansion, which is itself the finding.
4. Name the publication trigger, or record a no-release close as complete.
   **No trigger is visible at entry**: the published head is green and its
   records are true.
5. Record evidence candidate and release parent as **separate named fields**, and
   the disposition **as of a date**.
6. **Record each of the three determinations with its evidence** — the licence
   classification and the rights claim it makes, the terms determination and the
   publisher text it cites, and the feed shape against the parser's requirements.
   **If any was undetermined, record that as the cycle's result rather than as a
   shortfall.**
7. **Record what admission did not exercise**, if Step 5 ran: no runtime
   multi-origin behaviour, no live RSS path, no paging, no cursor durability.
8. Record E0's G5 finding and any amendment it forced to this file's definition
   of done, with its date.
9. Record whether the scope permission for `crates/core/**` was used, and if not,
   that it went unused.
10. Classify every diff path exactly once in `STATE.md`; update `CHANGELOG.md`,
    `README.md`, and the release authorities.
11. Reconcile `ARCHITECTURE.md`. **A4, the L1 residual, the R3/R4 open-bottom
    limitations, the measured-value heuristic, T7, and NEGATIVE-CACHE Decision B
    must all still read as open**, and **T7 must not be described as closer to
    its trigger** — a second configured source is not a second concurrent
    harvester.
12. Record the post-push hosted result as a **dated forward append**; a red
    post-push run is a finding for v0.26 and does not invalidate the close.
13. **State the publisher count precisely.** If Step 5 ran, two sources are
    configured and one has ever been fetched.

---

## Cycle checklist

- [x] **E0** — entering matrix with comparator citation; G1 stated per variant as
  a rights claim; G2's model gap enumerated and the publisher's own definition of
  "unclassified" cited; G3's mandatory fields enumerated with no feed request;
  G4's response fields and the rule quoted; **G5 settled and the definition of
  done amended in the same commit if required**; G6 answered structurally
- [x] **LICENSE-SEMANTICS** — one option chosen with its rights claim;
  `PublicDomain` excluded with reason; version decided with a criterion written
  into `AGENTS.md`; existing gating proven unchanged if extended;
  `config/core.json` untouched
- [x] **TERMS-GATE** — publisher text cited with URL and date; determination
  recorded with undetermined accepted as complete; condition restated as a
  version-independent property; terms-gate disposition dated in
  `ARCHITECTURE.md`; no code change
- [x] **FEED-SHAPE** — robots re-evaluated fresh with hash compared; exactly one
  feed request evidenced by count; shape and per-field presence recorded; parser
  behaviour derived not executed; body kept out of fixtures, corpus, and golden
- [x] **ADMIT** — complete, or deleted with the determination that deferred it.
  Decision recorded; `robots_on_missing` explicitly reasoned; **no live harvest**;
  non-exercise stated; deferral table updated both ways
- [x] **RE-MEASURE** — hosted run on a neutral branch; comparator cited; **no
  publisher request by any hosted job**; run id recorded
- [ ] **R-CLOSE** — version and its written criterion recorded; three
  determinations recorded with evidence; non-exercise stated; G5 amendment
  recorded; scope permission usage recorded; T7 not described as nearer its
  trigger

---

## Standing prohibitions

- **Do not classify SEC content as `PublicDomain`.** The review declined to
  assert that issuer-authored filings are government works, and a licence
  classification may not assert what the review refused to.
- **Do not resolve a terms ambiguity in the project's favour** because admission
  is this cycle's goal. Undetermined defers admission and is a complete outcome.
- **Do not request the feed if Step 3's determination is negative or
  undetermined.**
- **Do not issue more than one feed request in Step 4**, and do not re-request on
  a non-error response.
- **Do not re-use v0.24's robots verdict to authorize a request on a later
  date.** Re-evaluate the policy first and compare the hash.
- **Do not run a live harvest in this cycle.** Admission configures; v0.26
  harvests.
- **Do not add the observed feed body to `fixtures/`, the protected corpus, or
  golden.**
- **Do not copy `arxiv-cs`'s `robots_on_missing: allow`.** SEC serves a policy;
  the missing-policy branch is a separate decision requiring its own reason.
- **Do not modify `crates/ingest/**` or `crates/compliance/**`.** The scope
  permission covers `crates/core` and `crates/store` only, and only if Step 2
  requires it.
- **Do not carry a known-wrong definition of done past E0.** If G5 shows golden
  reads the live config, amend it in the same commit.
- **Do not describe T7 as nearer its trigger.** A second configured source is not
  a second concurrent harvester.
- **Do not create, move, or delete any ref in the working repository**; refs in a
  disposable clone are not repository refs.
- **Do not remove `--skip-local-tag-verification`.**
- **Do not add a rule without an R12 planted-failure control**, and do not add a
  rule that evaluates a condition it cannot observe.
- **Do not write a rule with no satisfying assignment for a case it governs.**
- **Do not amend, rebase, or squash `947822c8…`.**
- **Do not batch `STATE.md` / `PROGRESS-v0.25.md` updates or combine two tasks in
  one commit.**
- If any Step's Objective, Acceptance criteria, or "Done when" is amended after
  this file is committed at activation, name the amendment in a dated
  `## Runbook amendments` block in the same commit.

---

## Provenance of this draft

Every gate was read out of the repomix export of the v0.15.8 tree on 2026-07-30
by path, and each is a hypothesis for E0 to confirm or refute.

**Three claims here were verified against the export rather than reasoned to.**
`crates/core/src/lib.rs` declares `License` as
`PublicDomain | CcBy | ClientOwned | IndexOnly` with `redistributable()` true for
the first three, and its own comment states the dimension governs redistributing
someone else's full text verbatim in a paid product — which is exactly the claim
SEC's evidence does and does not support. `apps/cored/src/main.rs` serializes
`d.provenance.license.as_str()` into response bodies and gates `excerpt` on
`redistributable()`, so a new variant expands a public field's value domain.
And `config/core.json` still declares one live source, three `example.org`
fixtures, and `robots_on_missing: allow` on `arxiv-cs` only.

**The v0.24 review is the reason this cycle can be about the product.** It
produced the first real robots.txt this system has evaluated, a genuine
`Disallow` match on the excluded Atom path, four verbatim publisher citations,
and — most valuably — a correction of the operator's own stated expectation about
the crawler identity. **A review that only confirmed what was expected would have
been worth much less.** Its refusal to assert public-domain status for
issuer-authored filings is what makes G1 a real question rather than a
formality, and G1 is the one thing in this cycle that a reasonable person could
get wrong by being helpful.
