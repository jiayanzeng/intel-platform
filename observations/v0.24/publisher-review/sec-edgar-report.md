# v0.24 PUBLISHER-REVIEW — SEC EDGAR structured-disclosure RSS

Observed on **2026-07-30** local time (**2026-07-29T16:41Z** on the wire).
This is a compliance review against the `finance` sector. It is not a source
admission.

## Candidate and measured reason

The operator selected the SEC EDGAR filings feeds. The intended source is the
SEC's official US GAAP structured-disclosure RSS feed:

- publisher: U.S. Securities and Exchange Commission
- source page:
  <https://www.sec.gov/data-research/structured-data/structured-disclosure-rss-feeds>
- intended URL: <https://www.sec.gov/Archives/edgar/usgaap.rss.xml>
- intended path: `/Archives/edgar/usgaap.rss.xml`
- proposed sector: `finance`

The selection rationale was checked against `config/core.json`. It contains
three `rss` sources and all three have fixtures. `technology` has two fixture
RSS sources and `finance` has one; each points to `example.org`. The sole
existing live-publisher observation is the v0.18 `arxiv-cs` OAI-PMH harvest
under `IndexOnly`. The configured `CcBy` and `PublicDomain` cases have therefore
met only fixtures. The v0.18 publisher returned HTTP 404 for `robots.txt`, so
its observation exercised no real policy group, wildcard, anchor, exception,
or `Crawl-delay`.

Those facts make SEC's real RSS publisher, real reuse statement, and real
robots policy a more informative review than another OAI-PMH source. The
operator's prior description was candidate rationale, not evidence; the
publisher fetch and cited publisher statements below govern this result.

## Robots wire evidence

The robots-only preview used the repository's shipped
`intel_ingest::net::HttpRobotsFetcher`, installed crawler identity,
`intel_compliance::RobotsCache`, and `RobotsGate`. It made no feed or document
request.

- robots origin: `https://www.sec.gov`
- request: `GET https://www.sec.gov/robots.txt`
- final preview request count: **1**
- automatic redirects followed: **0**
- fetch result: `Body` (the shipped fetcher returns this only for a successful
  HTTP status)
- raw policy:
  [`sec-edgar-robots.txt`](sec-edgar-robots.txt)
- body size: **2,622 UTF-8 bytes**
- SHA-256:
  `72d6196b3f20737396e566ddeb769fb4174b44f334985a1267a59ae0f08c2f2f`
- crawler identity:
  `intel-platform/0.15.7 (research prototype; contact: [operator contact redacted])`
- monitored contact present on the actual request: **yes**
- selected group: `User-agent: *`
- matching rule for `/Archives/edgar/usgaap.rss.xml`: **none**
- `Allow` exception used: **none**
- publisher `Crawl-delay`: **none**
- configured missing-policy input to the preview: `Deny` (not reached because a
  policy body was served)
- shipped-matcher verdict for the intended path: **allow**

The absence of a matching rule is material: the feed does not inherit the
nearby `Allow: /Archives/edgar/data`, and none of the policy's `Disallow`
patterns matches it. The matcher therefore takes the selected wildcard group's
default allow outcome.

One earlier robots-only preview in the same review tested the SEC "Latest
Filings" Atom path,
`/cgi-bin/browse-edgar?action=getcurrent&output=atom`. The shipped matcher
returned **deny**, matching `Disallow: /cgi-bin`. That Atom path is also not the
RSS `item` input implemented by this repository. It is a measured excluded
endpoint, not an alternate admission route. Across the two preview processes,
the only publisher URL requested was `/robots.txt`; neither feed was requested.

## Licence and terms — verbatim publisher references

Each reference was read on **2026-07-30**. The quoted text is the publisher's;
no project paraphrase substitutes for it.

- Reuse permission — SEC Webmaster Frequently Asked Questions,
  <https://www.sec.gov/about/webmaster-frequently-asked-questions>,
  “Is content on sec.gov free? Do I need permission to reuse EDGAR content?”:
  “All Government-created content on sec.gov and EDGAR public filing content
  are free to access and reuse.”
- Crawler identity — the same FAQ, “I want to programmatically download EDGAR
  filings”: “Please declare your user agent in request headers:”
- Rate ceiling — SEC Developer Resources,
  <https://www.sec.gov/about/developer-resources>, “Fair Access”:
  “Current guidelines limit each user to a total of no more than 10 requests
  per second”
- Automated-access classification — SEC Privacy Information,
  <https://www.sec.gov/about/privacy-information>, “Internet Security Policy”:
  “The SEC does not allow "unclassified" bots or automated tools to crawl the
  site.”

The reuse evidence is the SEC's express statement about both
government-created content and EDGAR public filing content. This review does
not replace that statement with the broader and inaccurate proposition that
every issuer-authored filing is itself a U.S.-government-authored work.

## Reviewed recommendation

**Admissible, conditional.** The condition for any later admission is that it
use the reviewed `/Archives/edgar/usgaap.rss.xml` path, preserve the existing
monitored-contact crawler identity, and keep the total automated request rate
at or below the SEC's then-current published ceiling. A separate operator
admission decision remains required in v0.25.

The wire evidence contradicts the prior expectation that
`intel-platform/<version>` carries no contact: current production construction
requires a contact, and the actual preview request carried it. The condition is
therefore to preserve the measured contact-bearing identity, not to claim that
a missing contact was observed or corrected in this review. The current
process floor is 2 requests per second and is below the cited 10-request ceiling;
no publisher `Crawl-delay` was present.

## What this review does not establish

This review establishes nothing about multi-origin behaviour of the
origin-keyed robots cache or per-host limiter. It also establishes nothing
about the **live RSS wire path**: no real feed was fetched, so live RSS
fetching, feed parsing, and cursor durability against a real server remain
untested until admission. It establishes no production source, license enum,
sector mapping, schema, public response, protected corpus, or golden-corpus
change.

`config/core.json` is unchanged and no source has been added.
