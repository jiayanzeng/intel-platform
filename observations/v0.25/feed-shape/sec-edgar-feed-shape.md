# v0.25 FEED-SHAPE — SEC EDGAR US GAAP RSS

Observed on **2026-07-30** under the Step 4 single-request authorization. The
robots request completed at **2026-07-30T03:33:58Z** and the feed request at
**2026-07-30T03:34:00Z**.

## Request boundary

The disposable observer used the installed
`intel-platform/0.15.8 (research prototype; contact: [operator contact
redacted])` identity. The contact was present and had already been confirmed
monitored by the operator. Redirect following and retry behavior were disabled.

| Request | Count | Result |
|---|---:|---|
| `GET https://www.sec.gov/robots.txt` | **1** | successful policy body |
| `GET https://www.sec.gov/Archives/edgar/usgaap.rss.xml` | **1** | HTTP **200** |

No other publisher URL was requested in Step 4.

## Fresh robots decision

The robots request ran through the shipped `HttpRobotsFetcher`,
`RobotsCache`, and `RobotsGate`, with the operator deny-list applied
separately. The cache and recording wrapper each measured exactly one fetch.

- fresh body:
  [`sec-edgar-robots.txt`](sec-edgar-robots.txt)
- body size: **2,622 bytes**
- SHA-256:
  `72d6196b3f20737396e566ddeb769fb4174b44f334985a1267a59ae0f08c2f2f`
- v0.24 SHA-256:
  `72d6196b3f20737396e566ddeb769fb4174b44f334985a1267a59ae0f08c2f2f`
- byte comparison with the v0.24 policy: **identical**
- publisher verdict for `/Archives/edgar/usgaap.rss.xml`: **allow**
- operator deny-list verdict: **allow**
- effective request interval: **0.500 seconds**
- redirects followed: **0**

The unchanged policy and both allow results were checked before the feed client
was constructed.

## Feed wire result

- body:
  [`sec-edgar-usgaap.rss.xml`](sec-edgar-usgaap.rss.xml)
- request count: **1**
- HTTP status: **200**
- `Content-Type`: **`text/xml`**
- `Location` response header present: **no**
- redirects followed: **0**
- retries: **0**
- body size: **892,641 bytes**
- SHA-256:
  `154556cd81bda4fc2372386bf43aa7b4414335560dd1371c45bae09f1a8d9de3`

The observation-local `.gitattributes` marks this raw wire artifact as binary
so Git does not normalize or whitespace-clean publisher bytes. The XML remains
stored uncompressed and byte-identical to the measured response.

## Observed item and field presence

E0 found that the repository RSS parser has **zero mandatory per-item fields**.
An independent offline XPath count inspected the captured body for shape only;
the repository parser was not invoked against it. The table records direct
child presence and non-empty normalized text per `<item>`.

| E0 field | E0 requirement | Items with field | Items with non-empty field | Presence |
|---|---|---:|---:|---|
| `title` | optional | **200 / 200** | **200 / 200** | every item |
| `guid` | optional | **200 / 200** | **200 / 200** | every item |
| `pubDate` | optional | **200 / 200** | **200 / 200** | every item |
| `link` | optional | **200 / 200** | **200 / 200** | every item |
| `description` | optional | **200 / 200** | **200 / 200** | every item |
| `author` | optional | **0 / 200** | **0 / 200** | no items |

Observed `<item>` count: **200**. Because E0's mandatory-field list is empty,
the Step 4 mandatory-presence condition is satisfied. The optional-field counts
are recorded because they are still material to the documents the parser would
construct.

## Derived repository-parser behavior

This section derives behavior from E0's source enumeration; it does not execute
the repository parser or assert that the captured body parses successfully.

If the repository parser accepts the XML:

- it iterates descendant `<item>` elements, so the observed shape offers **200**
  candidates;
- the present non-empty `title`, `guid`, `link`, and `description` values take
  their ordinary branches rather than their missing-field fallbacks;
- `pubDate` is present in every item, so its raw value is retained; whether each
  value converts to `published_day` was not exercised here;
- absent `author` values yield an empty author vector for every item;
- no missing mandatory field can reject an item because the parser defines no
  mandatory per-item field.

The successful independent XPath count is not substituted for execution of the
repository parser.

## What one request does not establish

This observation establishes feed shape at one instant. It establishes nothing
about paging, any `resumptionToken` equivalent, cursor durability,
near-duplicate behavior, repeated-fetch politeness, conditional requests,
redirect handling on a different response, or a live ingest. The body remains
only under `observations/v0.25/`; it is not a fixture, protected-corpus
admission, configured source, or golden input.
