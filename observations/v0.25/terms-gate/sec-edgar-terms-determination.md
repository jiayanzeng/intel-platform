# v0.25 TERMS-GATE — SEC EDGAR automated-access determination

Determined on **2026-07-30**. This record decides one publisher's
automated-access condition for the reviewed US GAAP RSS path. It does not admit
or request the feed.

## Evidence basis

Step 3 made **zero publisher requests**. It uses the publisher text read and
recorded on 2026-07-30 by E0 and the committed v0.24 review:

- The shipped matcher evaluated the publisher's fetched `robots.txt` for
  `/Archives/edgar/usgaap.rss.xml` as **allow**. The captured policy is
  `observations/v0.24/publisher-review/sec-edgar-robots.txt`, SHA-256
  `72d6196b3f20737396e566ddeb769fb4174b44f334985a1267a59ae0f08c2f2f`.
- The SEC Privacy Information page's Internet Security Policy says that the SEC
  does not allow “unclassified” bots or automated tools to crawl the site:
  <https://www.sec.gov/about/privacy-information>.
- The SEC Webmaster Frequently Asked Questions directs programmatic EDGAR
  downloaders to declare their User-Agent in request headers, and its sample
  identifies an organization and an administrative contact at that
  organization's domain:
  <https://www.sec.gov/about/webmaster-frequently-asked-questions>.
- The SEC Developer Resources page separately publishes the applicable fair
  access rate ceiling:
  <https://www.sec.gov/about/developer-resources>.

The publisher supplies no separate glossary definition or registration
transaction for “unclassified.” Its published operational classification
procedure is to declare an organization-and-contact User-Agent. A robots allow
does not by itself answer that terms-level direction.

## Operator determination

**Affirmative.** On 2026-07-30 the operator accepted the affirmative
determination and confirmed its prerequisite: the configured crawler contact
is monitored. The installed identity names the stable `intel-platform` product,
the package-derived version, and that contact. It therefore satisfies the
publisher's published organization-and-contact declaration procedure for this
reviewed path.

The version-independent property is:

> A monitored contact is present in the crawler identity.

The source structurally requires a trimmed, non-empty, non-placeholder contact
before a net-enabled process binds, and derives the version rather than fixing
it in the identity. Monitoring is not source-observable; it is the operator
fact confirmed above. E0 therefore found no structural contact defect to assign
forward.

## Architecture disposition

Publisher terms compliance remains a **dated operator responsibility outside
the executable model**. The reason is epistemic rather than expedient: this
publisher's condition is natural-language policy with no stable
machine-readable classification or registration state for the system to fetch
and enforce. Encoding a third boolean gate would claim an automation the
available evidence cannot support. The executable model continues to enforce
publisher `robots.txt` plus the operator deny-list; admission additionally
requires a dated publisher-specific operator review like this one.

## Limits

This affirmative determination binds the SEC, the reviewed
`/Archives/edgar/usgaap.rss.xml` path, the cited texts, and **2026-07-30**. It is
not a general finding about government or regulatory publishers, does not
establish that another publisher's terms are satisfied, does not convert terms
into a robots rule, and does not establish the feed's shape or parseability.
Step 4 remains responsible for the separately authorized single feed request.
