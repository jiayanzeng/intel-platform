# v0.38 WIRE-ADMISSION — SEC EDGAR evidence comparison

Observed on **2026-08-04** local time under the operator's initiating Grant B.
The three evidence requests ran from **2026-08-03T19:50:50Z** through
**2026-08-03T19:50:56Z**.

## Request boundary

The disposable capture used the installed version-shaped identity
`intel-platform/0.17.4 (research prototype; contact: [operator contact
redacted])`. The contact was present in the normal environment and remains the
operator-confirmed monitored contact on which the pinned v0.25 affirmative
determination depends. Redirect following and retry behavior were disabled.
Requests were sequential and separated by at least the project's 0.500-second
floor.

| Request | Count | UTC start | Result | Content type | `Location` |
|---|---:|---|---|---|---:|
| `GET https://www.sec.gov/robots.txt` | **1** | `19:50:50Z` | HTTP **200** | `text/plain` | **0** |
| `GET https://www.sec.gov/about/privacy-information` | **1** | `19:50:52Z` | HTTP **200** | `text/html; charset=UTF-8` | **0** |
| `GET https://www.sec.gov/Archives/edgar/usgaap.rss.xml` | **1** | `19:50:54Z` | HTTP **200** | `text/xml` | **0** |

No other publisher URL was requested during evidence capture. Redirects
followed: **0**. Retries: **0**.

## Per-artifact comparison

### Publisher robots policy

- fresh file: [`sec-edgar-robots.txt`](sec-edgar-robots.txt)
- fresh bytes: **2,622**
- fresh SHA-256:
  `72d6196b3f20737396e566ddeb769fb4174b44f334985a1267a59ae0f08c2f2f`
- pinned v0.25 file:
  `observations/v0.25/feed-shape/sec-edgar-robots.txt`
- direct `cmp` result: **byte-identical**
- material compatibility: **pass**

The production matcher rehearsal already proves this exact policy allows
`/Archives/edgar/usgaap.rss.xml`, preserves the publisher's `/Archives/bin`
denial, and composes with the operator deny-list. The live harvest remains
responsible for the current production-cache verdict.

### Published access terms

- fresh file:
  [`sec-edgar-privacy-information.html`](sec-edgar-privacy-information.html)
- fresh bytes: **90,192**
- fresh SHA-256:
  `2a8baabaab64002140f6707b080afe5d67a108ad84acfb67cd91f8def1c41fd1`
- pinned v0.25 determination:
  `observations/v0.25/terms-gate/sec-edgar-terms-determination.md`
- pinned determination bytes / SHA-256: **3,549** /
  `103d29edd3a9ab005981a8ccd22eb8118040d992474e6a33491a51bde9ddbb2c`
- material compatibility: **pass**

The fresh page retains all material policy facts used by the determination: it
limits users to no more than **10 requests per second**, says the SEC does not
allow **"unclassified" bots or automated tools** to crawl the site, and says
public information on `sec.gov` may be copied or further distributed without
the SEC's permission. Nothing in the fresh page contradicts the pinned
organization-and-monitored-contact determination. The old record is a dated
determination rather than a raw HTML capture, so this comparison is explicitly
fresh-file to pinned-determination-file semantics; it does not fabricate an
unavailable v0.25 raw-page byte comparison or re-determine the policy.

### US GAAP RSS feed

- fresh file: [`sec-edgar-usgaap.rss.xml`](sec-edgar-usgaap.rss.xml)
- fresh bytes: **866,188**
- fresh SHA-256:
  `1139043372f2f4340489a4fc3eaafb08b7ffb741cc9c2c6470137edf9d8b673d`
- pinned v0.25 bytes / SHA-256: **892,641** /
  `154556cd81bda4fc2372386bf43aa7b4414335560dd1371c45bae09f1a8d9de3`
- direct `cmp` result: **different current feed contents**
- material shape compatibility: **pass**

Both files contain exactly **200** `<item>` elements. In the fresh file,
`title`, `guid`, `pubDate`, `link`, and `description` are present and non-empty
for **200/200** items; `author` is absent for **200/200**, exactly matching the
v0.25 shape. All **200** fresh GUIDs are non-empty and unique, and all **200**
links use `www.sec.gov`. The repository parser has no mandatory per-item field.
Changing filing content is expected for a current feed; the parser-facing shape
did not drift.

## DR12 disposition

**Compatible; admission may proceed.** Robots bytes are identical, the current
terms page preserves the pinned determination's material conditions and reuse
basis, and the current feed preserves the parser-facing 200-item shape. This
record makes no harvest, persistence, entitlement, recurrence, concurrency,
conditional-request, or repeated-fetch claim. The evidence files were captured
before the live harvest and are never input to it.
