//! intel-ingest: the plugin seam.
//!
//! Every connector implements `Source`. Fixture mode (a local file standing
//! in for the network body) keeps runs deterministic and testable; building
//! with `--features net` enables real HTTP fetching through the same gate.
//!
//! Cursoring (OAI-PMH resumptionToken, RSS ETag/Last-Modified) belongs in
//! each connector's state; it is stubbed here and noted in the README.

pub mod arxiv_oai;
pub mod rss;

#[cfg(feature = "net")]
pub mod net;

use async_trait::async_trait;
pub use intel_compliance::MissingPolicy;
use intel_compliance::{HostLimiters, RobotsCache, RobotsGate};
use intel_core::{Document, SectorId, SourceKind};
use std::sync::Arc;
use thiserror::Error;

#[derive(Debug, Error)]
pub enum IngestError {
    #[error("network fetch has no publisher robots cache: {0}")]
    NetworkWithoutRobotsCache(String),
    #[error("blocked by robots policy: {0}")]
    RobotsDisallowed(String),
    #[error("io: {0}")]
    Io(#[from] std::io::Error),
    #[error("parse: {0}")]
    Parse(String),
    #[error("http: {0}")]
    Http(String),
    #[error("persistence: {0}")]
    Persistence(String),
}

/// Persistence seam for paged harvests, implemented by the core store and
/// injected via `SourceContext`. A paged/incremental connector commits each
/// parsed page together with its next resumptionToken and datestamp high-water
/// candidate. Keeping those values in one transaction prevents an interruption
/// from advancing past documents that were still only held in memory.
/// Connectors that don't page simply ignore it.
///
/// Kept sync deliberately to match the core store's SQLite surface and keep the
/// trait object-safe without pulling async machinery into the seam. No handle
/// or transaction obtained here is held across a network await.
pub trait CursorStore: Send + Sync {
    /// In-flight resumptionToken to resume from, if a prior harvest was
    /// interrupted; `None` to start a fresh harvest.
    fn resume_token(&self, source_id: &str) -> Option<String>;
    /// The datestamp high-water mark from the last completed harvest, used as
    /// `from=` to request only newer records.
    fn high_water(&self, source_id: &str) -> Option<String>;
    /// Atomically persist one parsed page and its cursor state. `next_token`
    /// is `None` only for the final page; implementations then clear the
    /// in-flight cursor and promote the maximum pending datestamp to the
    /// completed high-water mark. Returns the number of genuinely new docs.
    fn commit_page(
        &self,
        source_id: &str,
        docs: &[Document],
        next_token: Option<&str>,
        page_high_water: Option<&str>,
    ) -> Result<usize, String>;
}

/// Per-run politeness context handed to every source.
pub struct SourceContext {
    /// The **configured** robots policy: the operator's own deny-list, applied
    /// to every host. It is a floor, not a substitute for the publisher's own
    /// policy — see `robots_cache`.
    pub robots: RobotsGate,
    /// Per-host politeness clocks. Keyed by host so a slow publisher's wait
    /// isn't charged to everyone else in the run.
    pub limiter: Arc<HostLimiters>,
    /// Atomic page + cursor persistence for resumable/incremental sources.
    /// `None` disables persistence (a single, non-resuming pass) — the default
    /// for tests and for connectors that never page.
    pub cursors: Option<Arc<dyn CursorStore>>,
    /// The **fetched** robots policy: the publisher's real `/robots.txt`,
    /// discovered per origin and cached (TTL + bounded).
    ///
    /// `None` is the offline/fixture path and means exactly what it says — no
    /// robots.txt is fetched, no network is touched, and the configured
    /// `robots` gate above governs alone, byte-for-byte as it did before T2.
    /// A network reach with `None` is rejected by `gate()` before any request.
    /// A fixture run must never reach out to a publisher just to be told it may
    /// read a file already sitting on disk.
    ///
    /// `Some` is the live path: **both** gates must permit the request. The
    /// operator's deny-list can only ever subtract from what the publisher
    /// allows, never add to it.
    pub robots_cache: Option<Arc<RobotsCache>>,
}

#[async_trait]
pub trait Source: Send + Sync {
    fn id(&self) -> &str;
    fn sector(&self) -> &SectorId;
    fn kind(&self) -> SourceKind;
    async fn fetch(&self, ctx: &SourceContext) -> Result<Vec<Document>, IngestError>;
}

/// Splits an absolute URL without normalizing its encoded bytes.
///
/// The returned tail starts with `/`, `?`, `#`, or is empty. Keeping the tail
/// verbatim matters because the robots matcher, not URL derivation, owns any
/// percent-encoding comparison.
fn absolute_url_parts(url: &str) -> Option<(&str, &str, &str)> {
    let (scheme, remainder) = url.split_once("://")?;
    if scheme.is_empty() || remainder.is_empty() {
        return None;
    }
    let authority_end = remainder
        .char_indices()
        .find_map(|(index, ch)| matches!(ch, '/' | '?' | '#').then_some(index))
        .unwrap_or(remainder.len());
    let authority = &remainder[..authority_end];
    if authority.is_empty() {
        return None;
    }
    Some((scheme, authority, &remainder[authority_end..]))
}

fn host_from_authority(authority: &str) -> Option<&str> {
    let host = authority
        .rsplit_once('@')
        .map_or(authority, |(_, host)| host);
    (!host.is_empty()).then_some(host)
}

/// Derives the robots comparison target from an absolute URL: path plus query,
/// with the fragment excluded. An absent path becomes `/`; a query on an
/// absent path is prefixed with `/`. Percent-encoding and repeated slashes are
/// preserved for the robots matcher.
pub(crate) fn robots_path_of(url: &str) -> String {
    let Some((_, _, tail)) = absolute_url_parts(url) else {
        return "/".to_string();
    };
    let comparison_target = tail.split_once('#').map_or(tail, |(before, _)| before);
    if comparison_target.starts_with('/') {
        comparison_target.to_string()
    } else if comparison_target.starts_with('?') {
        format!("/{comparison_target}")
    } else {
        "/".to_string()
    }
}

/// Extracts the authority's host (including an explicit port but excluding
/// userinfo), so politeness can be tracked per publisher.
pub(crate) fn host_of(url: &str) -> String {
    absolute_url_parts(url)
        .and_then(|(_, authority, _)| host_from_authority(authority))
        .unwrap_or("unknown")
        .to_string()
}

/// Extracts the origin (`scheme://host[:port]`) — the unit a `robots.txt`
/// governs. Per RFC 9309 the policy is per-origin, not per-host: `https://x`
/// and `http://x` are, strictly, allowed to publish different rules.
pub(crate) fn origin_of(url: &str) -> String {
    let Some((scheme, authority, _)) = absolute_url_parts(url) else {
        return "https://unknown".to_string();
    };
    format!(
        "{}://{}",
        scheme,
        host_from_authority(authority).unwrap_or("unknown")
    )
}

/// Where the bytes for the fetch about to happen will actually come from.
///
/// This distinction is load-bearing, not cosmetic. Reading a fixture off local
/// disk is not a request to a publisher, so it must not trigger a `robots.txt`
/// fetch — an "offline, deterministic" run that quietly phones example.org to
/// ask permission to read a file already sitting on disk would be both a
/// surprise and a lie about what offline means. The politeness *limiter* still
/// runs either way: it is a local clock, it costs nothing, and keeping it in
/// the fixture path is what lets the harvest tests assert that the limiter is
/// consulted once per page without any network at all.
#[derive(Clone, Copy, PartialEq, Eq, Debug)]
pub(crate) enum Reach {
    /// The bytes will come over the wire. The publisher gets a say.
    Network,
    /// The bytes will come from a local fixture. The publisher is not involved.
    Fixture,
}

/// The compliance gate: robots first, then the politeness wait for THIS host.
///
/// Two robots checks, deliberately, and in this order:
///
/// 1. The **publisher's** policy, fetched from their real `/robots.txt` — but
///    only on a `Reach::Network` fetch with a cache wired in. This is the check
///    that did not exist until T2: before it, "robots-compliant" meant
///    "compliant with a policy we wrote ourselves," which is not a claim worth
///    making.
/// 2. The **operator's** configured deny-list, which applies on top and can only
///    ever refuse *more*. A publisher permitting `/private` does not oblige us
///    to crawl it.
///
/// A denial from either is the same error: we do not fetch.
pub(crate) async fn gate(
    ctx: &SourceContext,
    url: &str,
    reach: Reach,
    on_missing: MissingPolicy,
) -> Result<(), IngestError> {
    let path = robots_path_of(url);

    if reach == Reach::Network {
        let cache = ctx
            .robots_cache
            .as_ref()
            .ok_or_else(|| IngestError::NetworkWithoutRobotsCache(url.to_string()))?;
        let origin = origin_of(url);
        if !cache.allowed(&origin, &path, on_missing).await {
            return Err(IngestError::RobotsDisallowed(url.to_string()));
        }
        // If the publisher published a Crawl-delay, adopt it from here on —
        // but only ever to slow down. See `RobotsCache::apply_crawl_delay`.
        cache.apply_crawl_delay(&origin).await;
    }

    if !ctx.robots.allowed(&path) {
        return Err(IngestError::RobotsDisallowed(url.to_string()));
    }
    ctx.limiter.acquire(&host_of(url)).await;
    Ok(())
}

// --- shared XML helpers (namespace-agnostic: match by local name) ----------

pub(crate) fn child_text(node: roxmltree::Node<'_, '_>, local: &str) -> Option<String> {
    node.children()
        .find(|c| c.tag_name().name() == local)
        .and_then(|c| c.text())
        .map(|t| t.trim().to_string())
        .filter(|t| !t.is_empty())
}

pub(crate) fn child_texts(node: roxmltree::Node<'_, '_>, local: &str) -> Vec<String> {
    node.children()
        .filter(|c| c.tag_name().name() == local)
        .filter_map(|c| c.text())
        .map(|t| t.trim().to_string())
        .filter(|t| !t.is_empty())
        .collect()
}

#[cfg(test)]
mod gate_tests {
    use super::*;
    use intel_compliance::{RobotsFetch, RobotsFetcher};
    use std::sync::atomic::{AtomicUsize, Ordering};
    use std::time::Duration;

    /// Counts fetches so a test can assert the *absence* of network traffic —
    /// which is the whole point of the fixture path.
    struct CountingFetcher {
        body: RobotsFetch,
        calls: AtomicUsize,
    }

    impl CountingFetcher {
        fn new(body: RobotsFetch) -> Arc<Self> {
            Arc::new(Self {
                body,
                calls: AtomicUsize::new(0),
            })
        }
        fn calls(&self) -> usize {
            self.calls.load(Ordering::Relaxed)
        }
    }

    #[async_trait]
    impl RobotsFetcher for CountingFetcher {
        async fn fetch(&self, _url: &str) -> RobotsFetch {
            self.calls.fetch_add(1, Ordering::Relaxed);
            self.body.clone()
        }
    }

    fn ctx_with(fetcher: Arc<CountingFetcher>, configured_denies: &[&str]) -> SourceContext {
        let limiter = Arc::new(HostLimiters::per_second(1000.0));
        SourceContext {
            robots: RobotsGate::new(configured_denies),
            limiter: limiter.clone(),
            cursors: None,
            robots_cache: Some(Arc::new(RobotsCache::new(
                fetcher,
                limiter,
                "intel-platform/0.1",
                Duration::from_secs(3600),
                64,
            ))),
        }
    }

    #[test]
    fn origin_is_scheme_plus_host() {
        assert_eq!(
            origin_of("https://export.arxiv.org/oai2?verb=x"),
            "https://export.arxiv.org"
        );
        assert_eq!(
            origin_of("http://example.org:8080/a/b"),
            "http://example.org:8080"
        );
    }

    #[test]
    fn url_derivation_matches_the_e0_case_table() {
        let cases = [
            (
                "https://example.org/private/secret/file",
                "/private/secret/file",
                "example.org",
            ),
            (
                "https://example.org/private/secret?x=1",
                "/private/secret?x=1",
                "example.org",
            ),
            (
                "https://example.org/private#fragment",
                "/private",
                "example.org",
            ),
            (
                "https://example.org/private/secret?x=1#fragment",
                "/private/secret?x=1",
                "example.org",
            ),
            ("https://example.org", "/", "example.org"),
            ("https://example.org/", "/", "example.org"),
            (
                "https://example.org:8443/private",
                "/private",
                "example.org:8443",
            ),
            (
                "https://user:pass@example.org/private",
                "/private",
                "example.org",
            ),
            (
                "https://example.org/private/%73ecret",
                "/private/%73ecret",
                "example.org",
            ),
            (
                "https://example.org/private//secret",
                "/private//secret",
                "example.org",
            ),
            ("https://example.org?x=1", "/?x=1", "example.org"),
        ];

        for (url, expected_path, expected_host) in cases {
            assert_eq!(robots_path_of(url), expected_path, "path for {url}");
            assert_eq!(host_of(url), expected_host, "host for {url}");
        }
    }

    #[tokio::test]
    async fn publisher_multi_segment_rule_blocks_a_descendant_path() {
        let f = CountingFetcher::new(RobotsFetch::Body(
            "User-agent: *\nDisallow: /private/secret\n".into(),
        ));
        let ctx = ctx_with(f, &[]);

        let err = gate(
            &ctx,
            "https://example.org/private/secret/file",
            Reach::Network,
            MissingPolicy::Deny,
        )
        .await
        .expect_err("the publisher's multi-segment rule must block");
        assert!(matches!(err, IngestError::RobotsDisallowed(_)));
    }

    #[tokio::test]
    async fn publisher_multi_segment_rule_does_not_block_a_sibling_path() {
        let f = CountingFetcher::new(RobotsFetch::Body(
            "User-agent: *\nDisallow: /private/secret\n".into(),
        ));
        let ctx = ctx_with(f, &[]);

        gate(
            &ctx,
            "https://example.org/private/public",
            Reach::Network,
            MissingPolicy::Deny,
        )
        .await
        .expect("a sibling path is outside the publisher's rule");
    }

    #[tokio::test]
    async fn publisher_rule_can_match_a_path_query_pair() {
        let f = CountingFetcher::new(RobotsFetch::Body(
            "User-agent: *\nDisallow: /private/secret?token=blocked$\n".into(),
        ));
        let ctx = ctx_with(f, &[]);

        let err = gate(
            &ctx,
            "https://example.org/private/secret?token=blocked",
            Reach::Network,
            MissingPolicy::Deny,
        )
        .await
        .expect_err("the query is part of the robots comparison target");
        assert!(matches!(err, IngestError::RobotsDisallowed(_)));
    }

    #[tokio::test]
    async fn url_fragment_is_excluded_from_the_publisher_rule_target() {
        let f = CountingFetcher::new(RobotsFetch::Body(
            "User-agent: *\nDisallow: /private$\n".into(),
        ));
        let ctx = ctx_with(f, &[]);

        let err = gate(
            &ctx,
            "https://example.org/private#operator-view",
            Reach::Network,
            MissingPolicy::Deny,
        )
        .await
        .expect_err("a fragment must not alter the robots comparison target");
        assert!(matches!(err, IngestError::RobotsDisallowed(_)));
    }

    #[tokio::test]
    async fn a_fixture_fetch_never_asks_the_publisher_for_permission() {
        // THE offline-determinism guarantee. Even on a build that *can* fetch,
        // and even with a cache wired in, reading a local file must not put a
        // single packet on the wire. If this test ever regresses, every
        // "deterministic offline run" claim in this repo becomes false.
        let f = CountingFetcher::new(RobotsFetch::Body("User-agent: *\nDisallow: /\n".into()));
        let ctx = ctx_with(f.clone(), &[]);

        gate(
            &ctx,
            "https://example.org/techwire/feed.xml",
            Reach::Fixture,
            MissingPolicy::Deny,
        )
        .await
        .expect("a fixture read must not be gated on a publisher's robots.txt");

        assert_eq!(f.calls(), 0, "a fixture run fetched robots.txt");
        assert_eq!(ctx.robots_cache.as_ref().unwrap().fetches(), 0);
    }

    #[tokio::test]
    async fn a_live_fetch_is_refused_when_the_publisher_refuses() {
        let f = CountingFetcher::new(RobotsFetch::Body(
            "User-agent: *\nDisallow: /techwire\n".into(),
        ));
        let ctx = ctx_with(f.clone(), &[]);

        let err = gate(
            &ctx,
            "https://example.org/techwire/feed.xml",
            Reach::Network,
            MissingPolicy::Deny,
        )
        .await
        .expect_err("publisher said no");
        assert!(matches!(err, IngestError::RobotsDisallowed(_)));
        assert_eq!(
            f.calls(),
            1,
            "the publisher's policy must actually be fetched"
        );
    }

    #[tokio::test]
    async fn a_live_fetch_is_allowed_when_the_publisher_allows() {
        let f = CountingFetcher::new(RobotsFetch::Body(
            "User-agent: *\nDisallow: /admin\n".into(),
        ));
        let ctx = ctx_with(f.clone(), &[]);
        gate(
            &ctx,
            "https://example.org/techwire/feed.xml",
            Reach::Network,
            MissingPolicy::Deny,
        )
        .await
        .expect("publisher allows this path");
        assert_eq!(f.calls(), 1);
    }

    #[tokio::test]
    async fn an_unreachable_robots_txt_fails_closed_on_the_live_path() {
        // 5xx / DNS / TLS / timeout. We do not know what this publisher permits,
        // so we take nothing — even though nothing explicitly forbade us.
        let f = CountingFetcher::new(RobotsFetch::Unreachable);
        let ctx = ctx_with(f, &[]);
        let err = gate(
            &ctx,
            "https://example.org/anything",
            Reach::Network,
            MissingPolicy::Deny,
        )
        .await
        .expect_err("unknown policy must deny");
        assert!(matches!(err, IngestError::RobotsDisallowed(_)));
    }

    #[tokio::test]
    async fn the_operator_denylist_still_refuses_what_the_publisher_permits() {
        // The two gates compose one way only: the operator can subtract, never
        // add. A publisher blessing /private does not oblige us to crawl it.
        let f = CountingFetcher::new(RobotsFetch::Body("User-agent: *\nDisallow:\n".into()));
        let ctx = ctx_with(f, &["/private"]);

        gate(
            &ctx,
            "https://example.org/public/feed.xml",
            Reach::Network,
            MissingPolicy::Deny,
        )
        .await
        .expect("allowed by both");
        let err = gate(
            &ctx,
            "https://example.org/private/feed.xml",
            Reach::Network,
            MissingPolicy::Deny,
        )
        .await
        .expect_err("configured deny-list must still apply");
        assert!(matches!(err, IngestError::RobotsDisallowed(_)));
    }

    #[tokio::test]
    async fn a_404_robots_txt_blocks_a_default_source_but_passes_an_opted_in_one() {
        // THE arXiv scenario, reproduced offline. oaipmh.arxiv.org serves no
        // robots.txt (404). A source left at the conservative default is blocked
        // (fail closed); a source the operator has vetted with
        // robots_on_missing="allow" proceeds — because the operator configuring
        // a cooperative harvest endpoint *is* the opt-in. Same 404 both times.
        let f = CountingFetcher::new(RobotsFetch::Unavailable);
        let ctx = ctx_with(f.clone(), &[]);

        let blocked = gate(
            &ctx,
            "https://oaipmh.arxiv.org/oai?verb=ListRecords",
            Reach::Network,
            MissingPolicy::Deny,
        )
        .await;
        assert!(
            matches!(blocked, Err(IngestError::RobotsDisallowed(_))),
            "a 404 must fail closed for a default source"
        );

        // Same origin, cached 404, but this source opted in.
        gate(
            &ctx,
            "https://oaipmh.arxiv.org/oai?verb=ListRecords",
            Reach::Network,
            MissingPolicy::RfcAllowAll,
        )
        .await
        .expect("an operator-vetted source may harvest an endpoint with no robots.txt");
    }

    #[tokio::test]
    async fn opting_in_does_not_bypass_an_explicit_arxiv_disallow() {
        // Guard against the knob quietly becoming "ignore robots.txt": if arXiv
        // *did* publish a robots.txt that forbade /oai, even the opted-in source
        // is refused. allow-on-missing reinterprets absence, nothing more.
        let f = CountingFetcher::new(RobotsFetch::Body("User-agent: *\nDisallow: /oai\n".into()));
        let ctx = ctx_with(f, &[]);
        let err = gate(
            &ctx,
            "https://oaipmh.arxiv.org/oai?verb=ListRecords",
            Reach::Network,
            MissingPolicy::RfcAllowAll,
        )
        .await
        .expect_err("an explicit Disallow is obeyed even for an opted-in source");
        assert!(matches!(err, IngestError::RobotsDisallowed(_)));
    }

    #[tokio::test]
    async fn a_live_fetch_with_no_cache_fails_closed_before_the_operator_gate() {
        let ctx = SourceContext {
            robots: RobotsGate::new(&["/private", "/admin"]),
            limiter: Arc::new(HostLimiters::per_second(1000.0)),
            cursors: None,
            robots_cache: None,
        };
        let err = gate(
            &ctx,
            "https://example.org/public/x",
            Reach::Network,
            MissingPolicy::Deny,
        )
        .await
        .expect_err("a network fetch without publisher policy must fail closed");
        assert!(matches!(
            err,
            IngestError::NetworkWithoutRobotsCache(url)
                if url == "https://example.org/public/x"
        ));
    }

    #[tokio::test]
    async fn with_no_cache_the_offline_configured_policy_is_unchanged() {
        // The pre-T2 offline world, preserved bit for bit: no cache wired in ⇒
        // the configured RobotsGate is the only gate, and no fetch is attempted.
        let ctx = SourceContext {
            robots: RobotsGate::new(&["/private", "/admin"]),
            limiter: Arc::new(HostLimiters::per_second(1000.0)),
            cursors: None,
            robots_cache: None,
        };
        gate(
            &ctx,
            "https://example.org/public/x",
            Reach::Fixture,
            MissingPolicy::Deny,
        )
        .await
        .expect("offline public path remains allowed");
        let err = gate(
            &ctx,
            "https://example.org/private/x",
            Reach::Fixture,
            MissingPolicy::Deny,
        )
        .await
        .expect_err("offline configured deny-list remains enforced");
        assert!(matches!(err, IngestError::RobotsDisallowed(_)));
    }
}
