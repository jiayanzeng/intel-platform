# SEC EDGAR observation replay — 2026-07-30

## Inputs and command

The committed test
`crates/ingest/tests/sec_observation_replay.rs` read
`observations/v0.25/feed-shape/sec-edgar-usgaap.rss.xml` in place and cited
`observations/v0.25/feed-shape/sec-edgar-feed-shape.md` as the record that
states its expected bytes. No copy was added to fixtures, the protected
corpus, or golden.

Executed from the repository root:

```text
cargo test -p intel-ingest --test sec_observation_replay --locked -- --nocapture
```

Result: **1 passed; 0 failed**.

## Point-of-use byte assertion and failure control

Before calling `RssSource::fetch`, the test measured:

- bytes: **892,641**
- SHA-256:
  `154556cd81bda4fc2372386bf43aa7b4414335560dd1371c45bae09f1a8d9de3`

The same assertion then read a disposable copy whose final byte was XORed with
one. Its length remained 892,641 and the assertion rejected it with:

```text
SHA-256 mismatch for observations/v0.25/feed-shape/sec-edgar-feed-shape.md:
expected 154556cd81bda4fc2372386bf43aa7b4414335560dd1371c45bae09f1a8d9de3,
observed feb138bb57e12466321c5db5a8f2a6ab1ea51ee59c9b94d355e7eaf65c9be748
```

The disposable directory was removed by the test. This step proposed no
manifest change; repository-wide manifest coverage is the separately
authorized Step 2B.

## Constructed `Document` set

The shipped RSS connector returned **200** documents from **200** XML `item`
elements. The committed test independently read each direct RSS child and
compared every constructed `Document` field with the shipped result.

| Field or population | Executed result |
|---|---|
| `Document.id` | 200 distinct; `sec-edgar-usgaap::<guid>`; maximum 114 bytes |
| `title` | 30–80 Unicode scalar values |
| `body` | 3 chars: 108; 4: 64; 5: 5; 6: 4; 7: 19 |
| `body` summary | min 3; p25 3; median 3; p75 4; max 7; mean **3.810** chars |
| `published_day` | `2026-07-29`: 200 |
| `published_raw` | present 200; 191 distinct strings |
| `authors` | 0 documents populated; 0 values; 0 distinct |
| `url` | present 200; 200 distinct |
| `tags` | empty on all 200 |
| `sector` | `finance` on all 200 |
| `License` | `PublisherPermitted` on all 200 |
| `SourceKind` | `Rss` on all 200 |
| provenance source | `sec-edgar-usgaap` on all 200 |
| provenance retrieval URL | committed SEC RSS URL on all 200 |

The observation declares `windows-1252`. The shipped fixture path executed
`read_to_string`, handed a Rust `&str` to roxmltree, and roxmltree accepted the
declaration. This response is lossless through that path because the committed
body is ASCII-only, not because the connector implements a general
Windows-1252 decoder.

## Day semantics

All 200 raw dates ended in `EDT`. `Day::parse_rfc822ish` slides a three-token
window to find day, month, and year and ignores the zone and clock. The
constructed value is therefore the publisher's local calendar day. An
independent EDT-to-UTC conversion in the executing test found **0 of 200**
items whose UTC calendar day differs from the recorded local day.

## Discarded `edgar:*` elements

The test enumerated descendants in the committed EDGAR namespace. “Items”
means the number of the 200 RSS items containing at least one such element;
“elements” counts all occurrences, including nested `xbrlFile` entries.

| Local name | Items | Elements |
|---|---:|---:|
| `acceptanceDatetime` | 200 | 200 |
| `accessionNumber` | 200 | 200 |
| `assignedSic` | 170 | 170 |
| `assistantDirector` | 170 | 170 |
| `cikNumber` | 200 | 200 |
| `companyName` | 200 | 200 |
| `fileNumber` | 200 | 200 |
| `filingDate` | 200 | 200 |
| `fiscalYearEnd` | 194 | 194 |
| `formType` | 200 | 200 |
| `otherCikNumbers` | 7 | 7 |
| `period` | 200 | 200 |
| `xbrlFile` | 200 | 2,339 |
| `xbrlFiles` | 200 | 200 |
| `xbrlFiling` | 200 | 200 |

None reaches a `Document` field. The test proves that by comparing all
constructed fields with only the direct RSS children plus configured
provenance values. No extension mapping was added.

## Establishment boundary

Asserted real publisher bytes replayed through shipped code establish parser
behavior for this one committed response. They establish nothing about paging,
cursor durability, repeated fetches, politeness on the wire, redirects,
conditional requests, or what the publisher serves next. No publisher request
was made during this replay.
