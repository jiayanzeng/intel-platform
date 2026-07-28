//! intel-compliance: the gate every fetch flows through.
//!
//! Two jobs, both of which used to be seed-grade and are now honest (T9.4):
//!
//! - **`RobotsGate`** speaks the path-matching language robots.txt actually
//!   uses (RFC 9309): `*` wildcards, `$` end-anchors, and `Allow` rules that
//!   can carve exceptions out of a broader `Disallow`. Prefix-only matching
//!   was wrong in both directions — it silently ignored `Disallow: /*.pdf$`
//!   (fetching what a publisher asked us not to) and had no way to honor an
//!   `Allow` exception (refusing what a publisher explicitly permitted).
//!   Conflicts resolve the way the spec says: the longest matching pattern
//!   wins, and `Allow` breaks ties.
//!
//! - **`HostLimiters`** keys the politeness wait per host. One shared limiter
//!   meant a single slow publisher throttled every other source in the run —
//!   arXiv's ~3s spacing would have been applied to an unrelated RSS feed too.
//!   Politeness is a promise to a *publisher*, so it belongs per-publisher.
//!
//! Production swap, same interfaces: `texting_robots` for a real robots.txt
//! parser (per-UA groups, Crawl-delay, TTL cache) and `governor` for token
//! buckets. The shapes here are already the shapes those slot into.

// clippy::unnecessary_map_or wants `Option::is_none_or`, stabilized in Rust
// 1.82. This crate's floor is 1.78 (STATE §5 / rust-toolchain.toml), and
// adopting is_none_or would silently raise it. The `map_or(true, ..)` form is
// correct and MSRV-safe, so the lint is allowed here deliberately.
#![allow(clippy::unnecessary_map_or)]

use std::collections::HashMap;
use std::sync::atomic::{AtomicU64, AtomicUsize, Ordering};
use std::sync::Arc;
use std::time::Duration;
use tokio::time::{sleep, Instant};

// ---------------------------------------------------------------------------
// Robots
// ---------------------------------------------------------------------------

#[derive(Clone, Debug)]
struct Rule {
    allow: bool,
    pattern: String,
}

/// A robots policy over URL paths.
#[derive(Clone, Default)]
pub struct RobotsGate {
    rules: Vec<Rule>,
    crawl_delay: Option<Duration>,
}

impl RobotsGate {
    /// Deny-list constructor (the historical shape): every entry is a
    /// `Disallow` pattern. Plain prefixes keep behaving exactly as before,
    /// because a pattern with no wildcard *is* a prefix match.
    pub fn new(disallow: &[&str]) -> Self {
        Self {
            rules: disallow
                .iter()
                .map(|p| Rule {
                    allow: false,
                    pattern: (*p).to_string(),
                })
                .collect(),
            crawl_delay: None,
        }
    }

    /// The `Crawl-delay` this policy asked for, if any.
    ///
    /// Non-standard (it is not in RFC 9309) but widely published and widely
    /// honored; when a publisher states a cadence we prefer *their* number to
    /// our configured default, and never a faster one — see
    /// [`RobotsCache::apply_crawl_delay`].
    pub fn crawl_delay(&self) -> Option<Duration> {
        self.crawl_delay
    }

    /// Parse a real `robots.txt` body, selecting the group that applies to
    /// `user_agent`.
    ///
    /// RFC 9309 group semantics, which are easy to get subtly wrong:
    ///
    /// - A "group" is one or more consecutive `User-agent` lines followed by
    ///   that group's rules. A `User-agent` line appearing *after* a rule line
    ///   starts a **new** group; it does not extend the current one.
    /// - We first find the **longest** product-token specificity matching our
    ///   UA (case-insensitive prefix match, §2.2.1), then merge every group at
    ///   that winning specificity in file order. If no specific token matches,
    ///   every `*` group is merged. Specific beats generic: `*` rules are NOT
    ///   merged in on top of a specific match. Doing so would be a real bug: a
    ///   site that disallows `/` for `*` and allows everything for us would end
    ///   up denying us everything. Across merged groups, the most conservative
    ///   (maximum) `Crawl-delay` applies.
    /// - An empty `Disallow:` value means "nothing is disallowed" and is the
    ///   conventional way to spell allow-all. It is a no-op rule, not a
    ///   disallow of the empty path.
    /// - Unknown fields (`Sitemap`, `Host`, …) are ignored, and a body with no
    ///   applicable group is allow-all — robots is a deny-list.
    pub fn parse(text: &str, user_agent: &str) -> Self {
        Self::parse_internal(text, user_agent)
    }

    fn parse_internal(text: &str, user_agent: &str) -> Self {
        // (ua tokens, rules, crawl_delay) per group, in file order.
        let mut groups: Vec<(Vec<String>, Vec<Rule>, Option<Duration>)> = Vec::new();
        // True while we are still accumulating the UA lines of the group being
        // built; the first rule line flips it, so the next UA line opens a new
        // group rather than joining this one.
        let mut in_ua_block = false;

        for raw in text.lines() {
            // Strip comments, then whitespace. A `#` anywhere begins a comment.
            let line = raw.split('#').next().unwrap_or("").trim();
            if line.is_empty() {
                continue;
            }
            let Some((field, value)) = line.split_once(':') else {
                continue; // Not a field:value line; ignore rather than fail.
            };
            let field = field.trim().to_ascii_lowercase();
            let value = value.trim();

            match field.as_str() {
                "user-agent" => {
                    if !in_ua_block || groups.is_empty() {
                        groups.push((Vec::new(), Vec::new(), None));
                        in_ua_block = true;
                    }
                    if let Some(g) = groups.last_mut() {
                        g.0.push(value.to_ascii_lowercase());
                    }
                }
                "allow" | "disallow" => {
                    // A rule with no preceding User-agent line belongs to no
                    // group; RFC 9309 says to ignore it.
                    let Some(g) = groups.last_mut() else { continue };
                    in_ua_block = false;
                    // `Disallow:` with an empty value disallows nothing.
                    if value.is_empty() {
                        continue;
                    }
                    g.1.push(Rule {
                        allow: field == "allow",
                        pattern: value.to_string(),
                    });
                }
                "crawl-delay" => {
                    let Some(g) = groups.last_mut() else { continue };
                    in_ua_block = false;
                    if let Ok(secs) = value.parse::<f64>() {
                        if secs.is_finite() && secs > 0.0 {
                            g.2 = Some(Duration::from_secs_f64(secs));
                        }
                    }
                }
                _ => {} // Sitemap, Host, and anything else: not our business.
            }
        }

        // Find the winning specificity first, then merge every group at that
        // specificity. `*` groups are the fallback only and never join a
        // specific match.
        let ua = user_agent.to_ascii_lowercase();
        let mut best_specificity: Option<usize> = None;
        for (tokens, _, _) in &groups {
            for t in tokens {
                if t != "*" && ua.starts_with(t.as_str()) {
                    let len = t.len();
                    if best_specificity.map_or(true, |best| len > best) {
                        best_specificity = Some(len);
                    }
                }
            }
        }

        let mut rules = Vec::new();
        let mut crawl_delay: Option<Duration> = None;
        for (tokens, group_rules, group_delay) in &groups {
            let applies = match best_specificity {
                Some(best) => tokens
                    .iter()
                    .any(|t| t != "*" && t.len() == best && ua.starts_with(t.as_str())),
                None => tokens.iter().any(|t| t == "*"),
            };
            if applies {
                rules.extend(group_rules.iter().cloned());
                if let Some(delay) = group_delay {
                    crawl_delay = Some(crawl_delay.map_or(*delay, |current| current.max(*delay)));
                }
            }
        }

        Self { rules, crawl_delay }
    }

    /// Add a `Disallow` pattern (`*` and trailing `$` supported).
    pub fn disallow(mut self, pattern: &str) -> Self {
        self.rules.push(Rule {
            allow: false,
            pattern: pattern.to_string(),
        });
        self
    }

    /// Add an `Allow` pattern — an exception carved out of a broader deny.
    pub fn allow(mut self, pattern: &str) -> Self {
        self.rules.push(Rule {
            allow: true,
            pattern: pattern.to_string(),
        });
        self
    }

    /// Is this path fetchable?
    ///
    /// Per RFC 9309: the most specific (longest) matching pattern decides, and
    /// when an `Allow` and a `Disallow` tie, `Allow` wins. No match at all means
    /// allowed — robots is a deny-list, not an allow-list.
    pub fn allowed(&self, path: &str) -> bool {
        self.decision_internal(path)
    }

    fn decision_internal(&self, path: &str) -> bool {
        let normalized_path = normalize_percent_encoding(path);
        let mut best: Option<(usize, bool)> = None;
        for r in &self.rules {
            let normalized_pattern = normalize_percent_encoding(&r.pattern);
            if !path_matches(&normalized_pattern, &normalized_path) {
                continue;
            }
            let len = normalized_pattern.len();
            best = match best {
                None => Some((len, r.allow)),
                Some((blen, _)) if len > blen => Some((len, r.allow)),
                // Equal specificity: Allow wins.
                Some((blen, ballow)) if len == blen => Some((blen, ballow || r.allow)),
                keep => keep,
            };
        }
        best.map_or(true, |(_, allow)| allow)
    }
}

/// Normalize the RFC 3986 unreserved octets used by robots matching.
///
/// Reserved octets deliberately stay encoded: decoding `%2F` to `/` would
/// re-segment the path and could over- or under-block. Valid encoded octets
/// that remain encoded get uppercase hex, so equivalent spellings compare
/// identically. Raw `*` and `$` remain parser metacharacters, while `%2A` and
/// `%24` remain literals.
fn normalize_percent_encoding(input: &str) -> String {
    fn hex_value(byte: u8) -> Option<u8> {
        match byte {
            b'0'..=b'9' => Some(byte - b'0'),
            b'a'..=b'f' => Some(byte - b'a' + 10),
            b'A'..=b'F' => Some(byte - b'A' + 10),
            _ => None,
        }
    }

    const HEX: &[u8; 16] = b"0123456789ABCDEF";
    let bytes = input.as_bytes();
    let mut output = Vec::with_capacity(bytes.len());
    let mut index = 0;
    while index < bytes.len() {
        if bytes[index] == b'%' && index + 2 < bytes.len() {
            if let (Some(high), Some(low)) =
                (hex_value(bytes[index + 1]), hex_value(bytes[index + 2]))
            {
                let value = (high << 4) | low;
                if value.is_ascii_alphanumeric() || matches!(value, b'-' | b'.' | b'_' | b'~') {
                    output.push(value);
                } else {
                    output.extend_from_slice(&[
                        b'%',
                        HEX[(value >> 4) as usize],
                        HEX[(value & 0x0f) as usize],
                    ]);
                }
                index += 3;
                continue;
            }
        }
        output.push(bytes[index]);
        index += 1;
    }

    String::from_utf8(output).expect("normalizing valid UTF-8 preserves valid UTF-8")
}

/// robots.txt path matching: `*` matches any run of characters, a trailing `$`
/// anchors the match to the end of the path, and everything else is literal.
/// An unanchored pattern is a prefix match, which is why plain-prefix policies
/// keep working unchanged.
fn path_matches(pattern: &str, path: &str) -> bool {
    let (pat, anchored) = match pattern.strip_suffix('$') {
        Some(p) => (p, true),
        None => (pattern, false),
    };

    let segments: Vec<&str> = pat.split('*').collect();
    let mut pos = 0usize;
    for (i, seg) in segments.iter().enumerate() {
        if seg.is_empty() {
            continue;
        }
        if i == 0 {
            // The first segment is anchored at the start of the path.
            if !path[pos..].starts_with(seg) {
                return false;
            }
            pos += seg.len();
        } else {
            match path[pos..].find(seg) {
                Some(idx) => pos += idx + seg.len(),
                None => return false,
            }
        }
    }

    if anchored {
        // `$` means the pattern must consume the path to its end — unless the
        // pattern ends in `*`, which can absorb whatever remains.
        let ends_with_wildcard = segments.last().is_some_and(|s| s.is_empty());
        if !ends_with_wildcard {
            return pos == path.len();
        }
    }
    true
}

// ---------------------------------------------------------------------------
// robots.txt discovery: fetch, cache, and the fail-closed rule
// ---------------------------------------------------------------------------

/// What came back when we asked an origin for its `/robots.txt`.
///
/// The three cases are not cosmetic — RFC 9309 §2.3.1 gives each of them a
/// *different* meaning, and conflating "the server told us there are no rules"
/// with "we could not reach the server" is how a crawler ends up either
/// refusing to fetch anything or fetching what it was asked not to.
#[derive(Clone, Debug, PartialEq, Eq)]
pub enum RobotsFetch {
    /// 2xx with a body. Parse it; the body governs. An empty body is a valid
    /// allow-all, and is NOT the same thing as `Unavailable`.
    Body(String),
    /// 4xx — "Unavailable" (§2.3.1.3). The server answered definitively: there
    /// is no policy here. The RFC permits full access.
    Unavailable,
    /// 5xx, timeout, TLS failure, DNS failure, connection refused, or a body we
    /// could not read — "Unreachable" (§2.3.1.4). We do not know the policy.
    /// The RFC says assume complete disallow, and so do we.
    Unreachable,
}

/// Fetches `/robots.txt` for an origin.
///
/// The trait exists so `intel-compliance` stays dependency-free and offline-
/// testable: the real implementation lives behind `--features net` in
/// `intel-ingest::net` (reqwest), while the tests here drive every branch —
/// 404, 500, empty file, malformed body — with a fake and no network at all.
#[async_trait::async_trait]
pub trait RobotsFetcher: Send + Sync {
    /// `robots_url` is a fully-qualified `scheme://host[:port]/robots.txt`.
    /// Implementations must not return an error type: every failure mode is
    /// already one of the `RobotsFetch` variants, which forces the caller to
    /// make the allow/deny decision explicitly instead of `?`-ing past it.
    async fn fetch(&self, robots_url: &str) -> RobotsFetch;
}

/// What to do when the server says, definitively, that it has no `robots.txt`
/// (a 4xx — `RobotsFetch::Unavailable`).
///
/// This is the one place where we knowingly diverge from RFC 9309, so it is a
/// named, explicit choice rather than a buried `else`:
///
/// - The RFC ([`MissingPolicy::RfcAllowAll`]) says a 404 means the crawler MAY
///   access anything. That is the right default for a *general-purpose* web
///   crawler discovering the open web.
/// - We are not that. We fetch a small, operator-configured set of publishers,
///   and the cost of wrongly fetching from a publisher who never published a
///   policy is a compliance incident, while the cost of wrongly *not* fetching
///   is a log line. So the default here is [`MissingPolicy::Deny`]: absence of
///   a stated permission is not permission.
///
/// `Unreachable` is not covered by this knob — it always denies, because there
/// the RFC and the conservative reading already agree.
#[derive(Clone, Copy, Debug, PartialEq, Eq, Default)]
pub enum MissingPolicy {
    /// No robots.txt ⇒ deny. The project default; see above.
    #[default]
    Deny,
    /// No robots.txt ⇒ allow all, per RFC 9309 §2.3.1.3.
    RfcAllowAll,
}

impl MissingPolicy {
    /// Parse the per-source config string. Unknown / absent ⇒ the conservative
    /// default (`Deny`), so a typo fails *closed*, never open.
    ///
    /// `"allow"` opts a specific, operator-vetted source into RFC-9309 behavior
    /// (a 404 robots.txt ⇒ crawl permitted). This is the right knob for a
    /// cooperative endpoint that publishes no robots.txt but exists expressly to
    /// be harvested — arXiv's OAI-PMH interface being the canonical case. It
    /// does **not** override an explicit `Disallow`, and it does **not** touch
    /// the `Unreachable` (5xx/timeout) path: both still fail closed.
    pub fn from_config_str(s: &str) -> Self {
        match s.trim().to_ascii_lowercase().as_str() {
            "allow" | "rfc" | "rfc_allow_all" | "allow_if_absent" => Self::RfcAllowAll,
            _ => Self::Deny,
        }
    }

    fn allows_when_absent(self) -> bool {
        matches!(self, Self::RfcAllowAll)
    }
}

/// The disposition of one origin, as cached.
#[derive(Clone)]
enum Policy {
    /// We have a parsed policy from the origin.
    Gate(RobotsGate),
    /// 4xx: no policy exists. Interpretation depends on `MissingPolicy`.
    Unavailable,
    /// 5xx/network: we do not know the policy. Always denies.
    Unreachable,
}

struct Entry {
    policy: Policy,
    fetched_at: Instant,
}

/// Cache lifetimes for definitive policy results and transient failures.
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub struct RobotsCacheTtls {
    policy: Duration,
    unreachable: Duration,
}

impl RobotsCacheTtls {
    pub const fn new(policy: Duration, unreachable: Duration) -> Self {
        Self {
            policy,
            unreachable,
        }
    }
}

/// Per-origin `robots.txt` cache: fetches once, honors a TTL, and is bounded.
///
/// Bounded because a cache keyed by a value an *outside party* influences (the
/// origin we were pointed at) is an unbounded-growth bug waiting to happen.
/// Eviction is oldest-fetch-first, which is the right policy for entries whose
/// only reason to exist is a TTL anyway.
///
/// The politeness limiter is shared with the harvest: fetching `/robots.txt` is
/// itself a request to the publisher, and it would be a strange kind of respect
/// to skip the rate limit for the one file that describes how to be respectful.
pub struct RobotsCache {
    fetcher: Arc<dyn RobotsFetcher>,
    limiters: Arc<HostLimiters>,
    user_agent: String,
    ttl: Duration,
    negative_ttl: Duration,
    capacity: usize,
    entries: std::sync::Mutex<HashMap<String, Entry>>,
    fetches: AtomicUsize,
}

impl RobotsCache {
    pub fn new(
        fetcher: Arc<dyn RobotsFetcher>,
        limiters: Arc<HostLimiters>,
        user_agent: impl Into<String>,
        ttl: Duration,
        capacity: usize,
    ) -> Self {
        Self::new_with_ttls(
            fetcher,
            limiters,
            user_agent,
            RobotsCacheTtls::new(ttl, ttl),
            capacity,
        )
    }

    /// Construct a cache with a distinct TTL for `Unreachable` results.
    ///
    /// Successful policies and definitive `Unavailable` results use `ttl`.
    /// Only transient 5xx/network failures use `negative_ttl`; they continue to
    /// deny while cached, as required by RFC 9309 §2.3.1.4.
    pub fn new_with_ttls(
        fetcher: Arc<dyn RobotsFetcher>,
        limiters: Arc<HostLimiters>,
        user_agent: impl Into<String>,
        ttls: RobotsCacheTtls,
        capacity: usize,
    ) -> Self {
        Self {
            fetcher,
            limiters,
            user_agent: user_agent.into(),
            ttl: ttls.policy,
            negative_ttl: ttls.unreachable,
            capacity: capacity.max(1),
            entries: std::sync::Mutex::new(HashMap::new()),
            fetches: AtomicUsize::new(0),
        }
    }

    /// How many live fetches this cache has issued — lets a test assert that a
    /// second request for the same origin was served from cache, and that the
    /// offline path issued *zero*.
    pub fn fetches(&self) -> usize {
        self.fetches.load(Ordering::Relaxed)
    }

    /// May we fetch `path` from `origin` (`scheme://host[:port]`)?
    ///
    /// `on_missing` is the **per-source** disposition for a 404 robots.txt,
    /// supplied by the caller from the source's own config. It exists because
    /// the right answer to "no robots.txt" is not global: for an unknown host
    /// the conservative `Deny` is correct, but for a cooperative, operator-
    /// configured endpoint that serves no robots.txt on purpose (arXiv OAI-PMH),
    /// `Deny` is a false positive that blocks exactly the access the publisher
    /// built the endpoint to provide. The operator's decision to configure the
    /// source *is* the opt-in; this threads that decision to the 404 case.
    ///
    /// It changes nothing else. An explicit `Disallow` is still honored (the
    /// publisher said no), and an `Unreachable` origin still fails closed (we do
    /// not know the policy). Only genuine *absence* is reinterpreted.
    pub async fn allowed(&self, origin: &str, path: &str, on_missing: MissingPolicy) -> bool {
        let policy = self.policy_for(origin).await;
        let (allowed, disposition, published_delay) = match policy {
            Policy::Gate(g) => {
                let allowed = g.allowed(path);
                (
                    allowed,
                    if allowed { "Body(allow)" } else { "Body(deny)" },
                    g.crawl_delay(),
                )
            }
            Policy::Unavailable => {
                let allowed = on_missing.allows_when_absent();
                (
                    allowed,
                    if allowed {
                        "Unavailable(allow)"
                    } else {
                        "Unavailable(deny)"
                    },
                    None,
                )
            }
            // We could not reach the origin's policy. RFC 9309 §2.3.1.4.
            Policy::Unreachable => (false, "Unreachable(deny)", None),
        };

        // This line is operational evidence, not decoration: the live harness
        // greps it to report the publisher disposition actually taken. The
        // effective delay is the slower of our current per-host floor and any
        // Crawl-delay the publisher supplied; apply_crawl_delay() below adopts
        // that same slower value before the document request.
        let host = host_of_origin(origin);
        let own_delay =
            Duration::from_secs_f64(1.0 / self.limiters.rate_for(&host).max(f64::MIN_POSITIVE));
        let effective_delay = published_delay.map_or(own_delay, |d| d.max(own_delay));
        eprintln!(
            "robots: {origin} -> {disposition}; path={path}; allowed={allowed}; effective-crawl-delay={:.3}s",
            effective_delay.as_secs_f64()
        );
        allowed
    }

    /// The `Crawl-delay` this origin published, if any.
    pub async fn crawl_delay(&self, origin: &str) -> Option<Duration> {
        match self.policy_for(origin).await {
            Policy::Gate(g) => g.crawl_delay(),
            _ => None,
        }
    }

    /// Adopt the origin's published `Crawl-delay` for its host's limiter — but
    /// only ever to slow *down*. A robots.txt that asks for a 0.1s delay must
    /// not be able to talk us into hammering a server faster than our own
    /// configured politeness floor; publisher policy is a lower bound on our
    /// courtesy, not a licence.
    pub async fn apply_crawl_delay(&self, origin: &str) {
        let Some(delay) = self.crawl_delay(origin).await else {
            return;
        };
        let host = host_of_origin(origin);
        let requested_rps = 1.0 / delay.as_secs_f64().max(0.001);
        if requested_rps < self.limiters.rate_for(&host) {
            self.limiters.set_host_rate(&host, requested_rps);
        }
    }

    /// Returns the cached policy for `origin`, fetching it if we have never
    /// seen it or the TTL has expired.
    async fn policy_for(&self, origin: &str) -> Policy {
        if let Some(p) = self.cached(origin) {
            return p;
        }

        // Be polite about the politeness file, too.
        let host = host_of_origin(origin);
        self.limiters.acquire(&host).await;

        self.fetches.fetch_add(1, Ordering::Relaxed);
        let url = format!("{}/robots.txt", origin.trim_end_matches('/'));
        let policy = match self.fetcher.fetch(&url).await {
            RobotsFetch::Body(body) => Policy::Gate(RobotsGate::parse(&body, &self.user_agent)),
            RobotsFetch::Unavailable => Policy::Unavailable,
            RobotsFetch::Unreachable => Policy::Unreachable,
        };

        self.store(origin, policy.clone());
        policy
    }

    /// Cache read. The std mutex is taken and dropped here and never held
    /// across an await.
    fn cached(&self, origin: &str) -> Option<Policy> {
        let map = self.entries.lock().unwrap();
        let e = map.get(origin)?;
        let ttl = match &e.policy {
            Policy::Unreachable => self.negative_ttl,
            Policy::Gate(_) | Policy::Unavailable => self.ttl,
        };
        if e.fetched_at.elapsed() >= ttl {
            return None; // Stale: re-fetch.
        }
        Some(e.policy.clone())
    }

    fn store(&self, origin: &str, policy: Policy) {
        let mut map = self.entries.lock().unwrap();
        map.insert(
            origin.to_string(),
            Entry {
                policy,
                fetched_at: Instant::now(),
            },
        );
        // Bounded: evict the oldest fetch until we are back under capacity.
        while map.len() > self.capacity {
            let Some(oldest) = map
                .iter()
                .min_by_key(|(_, e)| e.fetched_at)
                .map(|(k, _)| k.clone())
            else {
                break;
            };
            map.remove(&oldest);
        }
    }
}

/// `scheme://host[:port]` -> `host[:port]`, to key the shared host limiter.
fn host_of_origin(origin: &str) -> String {
    origin
        .split_once("://")
        .map(|(_, rest)| rest)
        .unwrap_or(origin)
        .trim_end_matches('/')
        .to_string()
}

// ---------------------------------------------------------------------------
// Rate limiting
// ---------------------------------------------------------------------------

/// Enforces a minimum interval between requests to ONE host.
pub struct RateLimiter {
    min_interval_ns: AtomicU64,
    last: tokio::sync::Mutex<Option<Instant>>,
    acquires: AtomicUsize,
}

impl RateLimiter {
    pub fn per_second(rps: f64) -> Self {
        Self {
            min_interval_ns: AtomicU64::new(Self::interval_ns(rps)),
            last: tokio::sync::Mutex::new(None),
            acquires: AtomicUsize::new(0),
        }
    }

    fn interval_ns(rps: f64) -> u64 {
        Duration::from_secs_f64(1.0 / rps.max(0.001))
            .as_nanos()
            .try_into()
            .unwrap_or(u64::MAX)
    }

    fn min_interval(&self) -> Duration {
        Duration::from_nanos(self.min_interval_ns.load(Ordering::Relaxed))
    }

    fn set_rate(&self, rps: f64) {
        self.min_interval_ns
            .store(Self::interval_ns(rps), Ordering::Relaxed);
    }

    pub async fn acquire(&self) {
        self.acquires.fetch_add(1, Ordering::Relaxed);
        let mut last = self.last.lock().await;
        if let Some(prev) = *last {
            let elapsed = prev.elapsed();
            let min_interval = self.min_interval();
            if elapsed < min_interval {
                sleep(min_interval - elapsed).await;
            }
        }
        *last = Some(Instant::now());
    }

    /// How many times `acquire` has been called — lets a harvest test confirm
    /// the limiter is consulted once per page without timing the actual waits.
    pub fn acquires(&self) -> usize {
        self.acquires.load(Ordering::Relaxed)
    }

    /// Requests per second this limiter currently enforces.
    pub fn rate(&self) -> f64 {
        1.0 / self.min_interval().as_secs_f64().max(f64::MIN_POSITIVE)
    }
}

/// A registry of per-host rate limiters.
///
/// Politeness is a promise made to a publisher, so the clock has to be kept per
/// publisher: waiting on arXiv must not make us wait on an unrelated RSS feed.
pub struct HostLimiters {
    rps: f64,
    limiters: std::sync::Mutex<HashMap<String, Arc<RateLimiter>>>,
    acquires: AtomicUsize,
}

impl HostLimiters {
    pub fn per_second(rps: f64) -> Self {
        Self {
            rps,
            limiters: std::sync::Mutex::new(HashMap::new()),
            acquires: AtomicUsize::new(0),
        }
    }

    /// Per-host override, for a publisher that asks for a slower cadence than
    /// the default (arXiv's ~3s between harvester requests, say).
    pub fn set_host_rate(&self, host: &str, rps: f64) {
        let mut map = self.limiters.lock().unwrap();
        match map.get(host) {
            Some(limiter) => limiter.set_rate(rps),
            None => {
                map.insert(host.to_string(), Arc::new(RateLimiter::per_second(rps)));
            }
        }
    }

    /// The rate currently in force for `host` — the default unless a publisher
    /// (or an operator) has asked for something slower.
    pub fn rate_for(&self, host: &str) -> f64 {
        let map = self.limiters.lock().unwrap();
        map.get(host).map_or(self.rps, |l| l.rate())
    }

    fn limiter_for(&self, host: &str) -> Arc<RateLimiter> {
        let mut map = self.limiters.lock().unwrap();
        map.entry(host.to_string())
            .or_insert_with(|| Arc::new(RateLimiter::per_second(self.rps)))
            .clone()
    }

    /// Wait until it is polite to hit `host`. The std Mutex is released before
    /// the await — only the per-host limiter's async mutex is held across it,
    /// so two different hosts never block each other.
    pub async fn acquire(&self, host: &str) {
        self.acquires.fetch_add(1, Ordering::Relaxed);
        let limiter = self.limiter_for(host);
        limiter.acquire().await;
    }

    /// Total acquisitions across all hosts.
    pub fn acquires(&self) -> usize {
        self.acquires.load(Ordering::Relaxed)
    }

    /// Acquisitions for one host.
    pub fn acquires_for(&self, host: &str) -> usize {
        let map = self.limiters.lock().unwrap();
        map.get(host).map_or(0, |l| l.acquires())
    }

    pub fn hosts(&self) -> Vec<String> {
        let map = self.limiters.lock().unwrap();
        let mut v: Vec<String> = map.keys().cloned().collect();
        v.sort();
        v
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn plain_prefixes_behave_exactly_as_before() {
        let g = RobotsGate::new(&["/private", "/admin"]);
        assert!(!g.allowed("/private/thing"));
        assert!(!g.allowed("/admin"));
        assert!(g.allowed("/public/thing"));
        assert!(g.allowed("/"));
    }

    #[test]
    fn wildcards_and_end_anchors_are_honored() {
        // The case prefix-matching silently ignored: we would have fetched it.
        let g = RobotsGate::default().disallow("/*.pdf$");
        assert!(!g.allowed("/papers/2026/report.pdf"));
        assert!(g.allowed("/papers/2026/report.pdf.html")); // $ anchors the end
        assert!(g.allowed("/papers/report.html"));

        let g = RobotsGate::default().disallow("/tmp/*/private");
        assert!(!g.allowed("/tmp/a/private"));
        assert!(!g.allowed("/tmp/a/b/c/private"));
        assert!(g.allowed("/tmp/a/public"));
    }

    #[test]
    fn allow_carves_an_exception_out_of_a_broader_disallow() {
        // The other thing prefix-matching couldn't do: honor an explicit
        // permission. Longest match wins, so the Allow governs.
        let g = RobotsGate::default().disallow("/data").allow("/data/open");
        assert!(!g.allowed("/data/secret"));
        assert!(g.allowed("/data/open/corpus.xml"));
    }

    #[test]
    fn allow_wins_a_tie_of_equal_specificity() {
        let g = RobotsGate::default().disallow("/x").allow("/x");
        assert!(g.allowed("/x/y"));
    }

    #[test]
    fn unmatched_paths_are_allowed_by_default() {
        assert!(RobotsGate::default().allowed("/anything"));
    }

    #[test]
    fn unreserved_percent_encoding_cannot_evade_a_rule() {
        let gate = RobotsGate::default().disallow("/foo/bar/baz");
        assert!(!gate.allowed("/foo/bar/%62%61%7A"));
    }

    #[test]
    fn encoded_reserved_slash_is_not_decoded() {
        assert_eq!(normalize_percent_encoding("/foo%2fbar"), "/foo%2Fbar");
        let gate = RobotsGate::default().disallow("/foo/bar");
        assert!(gate.allowed("/foo%2Fbar"));
    }

    #[test]
    fn encoded_star_is_literal_and_never_becomes_a_wildcard() {
        let gate = RobotsGate::default().disallow("/foo/%2a/private");
        assert!(!gate.allowed("/foo/%2A/private"));
        assert!(gate.allowed("/foo/anything/private"));
    }

    #[test]
    fn mixed_case_hex_normalizes_identically() {
        assert_eq!(
            normalize_percent_encoding("/%7euser/%2fdata"),
            normalize_percent_encoding("/%7Euser/%2Fdata")
        );
        assert_eq!(
            normalize_percent_encoding("/%7euser/%2fdata"),
            "/~user/%2Fdata"
        );
    }

    #[test]
    fn normalized_path_is_unchanged_and_normalization_is_idempotent() {
        let normalized = "/foo/bar-._~/*/report.pdf$";
        assert_eq!(normalize_percent_encoding(normalized), normalized);
        let once = normalize_percent_encoding("/foo/%62ar/%2fdata/%7e");
        assert_eq!(normalize_percent_encoding(&once), once);
    }

    // -- robots.txt parsing ------------------------------------------------
    //
    // The corpus below is also the input to the out-of-tree differential run
    // against `texting_robots` recorded in STATE.md §6: every expectation here
    // was confirmed to match that crate's verdict before we chose not to take
    // it as a dependency.

    /// A representative real-world file: a `*` group, a more specific group for
    /// us, wildcards, an `Allow` exception, a `Crawl-delay`, comments, and a
    /// `Sitemap` line we must ignore.
    const FIXTURE: &str = r#"
# Welcome, robots.
User-agent: *
Disallow: /private
Disallow: /*.pdf$
Crawl-delay: 10

User-agent: intel-platform
Disallow: /data
Allow: /data/open
Crawl-delay: 3

Sitemap: https://example.org/sitemap.xml
"#;

    #[test]
    fn parses_the_group_that_applies_to_us_and_not_the_star_group() {
        let g = RobotsGate::parse(FIXTURE, "intel-platform/0.1 (research)");
        // Our group's rules.
        assert!(!g.allowed("/data/secret"));
        assert!(
            g.allowed("/data/open/corpus.xml"),
            "Allow must carve the exception"
        );
        assert_eq!(g.crawl_delay(), Some(Duration::from_secs(3)));
        // The `*` group's rules must NOT be merged on top of our own. A site
        // that restricts everyone else and trusts us is a site we may crawl.
        assert!(
            g.allowed("/private/thing"),
            "star-group rule leaked into our group"
        );
        assert!(
            g.allowed("/papers/report.pdf"),
            "star-group rule leaked into our group"
        );
    }

    #[test]
    fn an_unmatched_agent_falls_back_to_the_star_group() {
        let g = RobotsGate::parse(FIXTURE, "some-other-bot/2.0");
        assert!(!g.allowed("/private/thing"));
        assert!(
            !g.allowed("/papers/2026/report.pdf"),
            "wildcard + $ from robots.txt"
        );
        assert!(
            g.allowed("/data/secret"),
            "our group's rule leaked into the star group"
        );
        assert_eq!(g.crawl_delay(), Some(Duration::from_secs(10)));
    }

    #[test]
    fn a_user_agent_line_after_a_rule_starts_a_new_group() {
        // The classic parser bug: treating this as one group with two UAs would
        // apply `Disallow: /a` to bot-b as well.
        let txt = "User-agent: bot-a\nDisallow: /a\nUser-agent: bot-b\nDisallow: /b\n";
        let a = RobotsGate::parse(txt, "bot-a");
        assert!(!a.allowed("/a"));
        assert!(a.allowed("/b"));
        let b = RobotsGate::parse(txt, "bot-b");
        assert!(b.allowed("/a"));
        assert!(!b.allowed("/b"));
    }

    #[test]
    fn consecutive_user_agent_lines_share_one_group() {
        let txt = "User-agent: bot-a\nUser-agent: bot-b\nDisallow: /x\n";
        assert!(!RobotsGate::parse(txt, "bot-a").allowed("/x"));
        assert!(!RobotsGate::parse(txt, "bot-b").allowed("/x"));
        assert!(RobotsGate::parse(txt, "bot-c").allowed("/x"));
    }

    #[test]
    fn the_longest_matching_agent_token_wins() {
        let txt = "User-agent: *\nDisallow: /\n\nUser-agent: intel\nDisallow: /deep\n\nUser-agent: intel-platform\nDisallow: /deeper\n";
        let g = RobotsGate::parse(txt, "intel-platform/0.1");
        assert!(
            g.allowed("/deep"),
            "the shorter `intel` token should have lost"
        );
        assert!(!g.allowed("/deeper"));
        assert!(
            g.allowed("/anything-else"),
            "the `*` group should not apply"
        );
    }

    #[test]
    fn duplicate_specific_groups_are_merged_in_file_order() {
        let txt = "User-agent: intel-platform\nDisallow: /first\n\
                   User-agent: intel-platform\nDisallow: /second\n";
        let gate = RobotsGate::parse(txt, "intel-platform/0.1");

        assert!(!gate.allowed("/first/private"));
        assert!(!gate.allowed("/second/private"));
    }

    #[test]
    fn star_disallow_root_is_not_merged_into_specific_allow_all_regression() {
        let txt = "User-agent: *\nDisallow: /\n\
                   User-agent: intel-platform\nDisallow:\n";
        let gate = RobotsGate::parse(txt, "intel-platform/0.1");

        assert!(
            gate.allowed("/anything"),
            "the generic root deny must not leak into a specific allow-all"
        );
    }

    #[test]
    fn unrelated_star_rules_are_absent_from_a_specific_match() {
        let txt = "User-agent: *\nDisallow: /generic\n\
                   User-agent: intel-platform\nDisallow: /specific\n";
        let gate = RobotsGate::parse(txt, "intel-platform/0.1");

        assert!(gate.allowed("/generic/private"));
        assert!(!gate.allowed("/specific/private"));
    }

    #[test]
    fn merged_groups_use_the_maximum_crawl_delay() {
        let txt = "User-agent: intel-platform\nCrawl-delay: 2\n\
                   User-agent: intel-platform\nCrawl-delay: 7\n";
        let gate = RobotsGate::parse(txt, "intel-platform/0.1");

        assert_eq!(gate.crawl_delay(), Some(Duration::from_secs(7)));
    }

    #[test]
    fn an_empty_disallow_value_means_allow_all() {
        // The conventional spelling of "you may crawl everything."
        let g = RobotsGate::parse("User-agent: *\nDisallow:\n", "anyone");
        assert!(g.allowed("/"));
        assert!(g.allowed("/anything/at/all"));
    }

    #[test]
    fn an_empty_file_allows_everything() {
        assert!(RobotsGate::parse("", "anyone").allowed("/anything"));
        assert!(RobotsGate::parse("\n\n# just a comment\n", "anyone").allowed("/anything"));
    }

    #[test]
    fn field_names_are_case_insensitive_and_comments_are_stripped() {
        let g = RobotsGate::parse(
            "USER-AGENT: *\nDISALLOW: /x  # trailing comment\n",
            "anyone",
        );
        assert!(!g.allowed("/x/y"));
    }

    #[test]
    fn rules_before_any_user_agent_line_are_ignored() {
        // Junk at the top of the file must not become a global deny.
        let g = RobotsGate::parse("Disallow: /\nUser-agent: *\nDisallow: /private\n", "anyone");
        assert!(g.allowed("/public"));
        assert!(!g.allowed("/private"));
    }

    #[test]
    fn a_malformed_body_does_not_panic_and_yields_no_rules() {
        // e.g. an HTML error page served with a 200, which is depressingly common.
        let g = RobotsGate::parse(
            "<!DOCTYPE html><html><body>404 not found</body></html>",
            "anyone",
        );
        assert!(g.allowed("/anything"));
    }

    // -- fetch, cache, and the fail-closed rule -----------------------------

    /// A fetcher that answers from a script and counts calls. No network.
    struct FakeFetcher {
        reply: std::sync::Mutex<RobotsFetch>,
        calls: AtomicUsize,
    }

    impl FakeFetcher {
        fn new(reply: RobotsFetch) -> Arc<Self> {
            Arc::new(Self {
                reply: std::sync::Mutex::new(reply),
                calls: AtomicUsize::new(0),
            })
        }
        fn calls(&self) -> usize {
            self.calls.load(Ordering::Relaxed)
        }
        fn set(&self, r: RobotsFetch) {
            *self.reply.lock().unwrap() = r;
        }
    }

    #[async_trait::async_trait]
    impl RobotsFetcher for FakeFetcher {
        async fn fetch(&self, _url: &str) -> RobotsFetch {
            self.calls.fetch_add(1, Ordering::Relaxed);
            self.reply.lock().unwrap().clone()
        }
    }

    fn cache_with(f: Arc<FakeFetcher>) -> RobotsCache {
        RobotsCache::new(
            f,
            Arc::new(HostLimiters::per_second(1000.0)),
            "intel-platform/0.1",
            Duration::from_secs(3600),
            64,
        )
    }

    fn cache_with_ttls(f: Arc<FakeFetcher>, ttl: Duration, negative_ttl: Duration) -> RobotsCache {
        RobotsCache::new_with_ttls(
            f,
            Arc::new(HostLimiters::per_second(1000.0)),
            "intel-platform/0.1",
            RobotsCacheTtls::new(ttl, negative_ttl),
            64,
        )
    }

    #[tokio::test]
    async fn a_fetched_policy_governs_the_gate() {
        let c = cache_with(FakeFetcher::new(RobotsFetch::Body(FIXTURE.into())));
        assert!(
            !c.allowed("https://example.org", "/data/secret", MissingPolicy::Deny)
                .await
        );
        assert!(
            c.allowed(
                "https://example.org",
                "/data/open/x.xml",
                MissingPolicy::Deny
            )
            .await
        );
    }

    #[tokio::test]
    async fn a_500_denies_rather_than_permits() {
        // RFC 9309 §2.3.1.4: unreachable ⇒ assume complete disallow. We do not
        // know what this publisher permits, so we take nothing.
        let c = cache_with(FakeFetcher::new(RobotsFetch::Unreachable));
        assert!(
            !c.allowed("https://example.org", "/anything", MissingPolicy::Deny)
                .await
        );
        assert!(
            !c.allowed("https://example.org", "/", MissingPolicy::Deny)
                .await
        );
    }

    #[tokio::test(start_paused = true)]
    async fn unreachable_retries_after_its_short_ttl_but_not_before() {
        let unavailable_fetcher = FakeFetcher::new(RobotsFetch::Unavailable);
        let unavailable = cache_with_ttls(
            unavailable_fetcher.clone(),
            Duration::from_secs(600),
            Duration::from_secs(60),
        );
        assert!(
            unavailable
                .allowed(
                    "https://unavailable.example",
                    "/anything",
                    MissingPolicy::RfcAllowAll
                )
                .await
        );
        unavailable_fetcher.set(RobotsFetch::Body(
            "User-agent: *\nDisallow: /anything\n".into(),
        ));
        tokio::time::advance(Duration::from_secs(60)).await;
        assert!(
            unavailable
                .allowed(
                    "https://unavailable.example",
                    "/anything",
                    MissingPolicy::RfcAllowAll
                )
                .await,
            "the negative TTL leaked onto a definitive unavailable result"
        );
        assert_eq!(
            unavailable_fetcher.calls(),
            1,
            "unavailable must retain the successful-policy TTL"
        );

        let f = FakeFetcher::new(RobotsFetch::Unreachable);
        let c = cache_with_ttls(f.clone(), Duration::from_secs(600), Duration::from_secs(60));

        assert!(
            !c.allowed("https://example.org", "/anything", MissingPolicy::Deny)
                .await
        );
        assert_eq!(f.calls(), 1);

        f.set(RobotsFetch::Body(String::new()));
        tokio::time::advance(Duration::from_secs(59)).await;
        assert!(
            !c.allowed("https://example.org", "/anything", MissingPolicy::Deny)
                .await
        );
        assert_eq!(f.calls(), 1, "negative result re-fetched before its TTL");

        tokio::time::advance(Duration::from_secs(1)).await;
        assert!(
            c.allowed("https://example.org", "/anything", MissingPolicy::Deny)
                .await
        );
        assert_eq!(f.calls(), 2, "negative result was not retried at its TTL");
    }

    #[tokio::test(start_paused = true)]
    async fn unreachable_overwrites_last_good_when_fallback_is_deferred() {
        let f = FakeFetcher::new(RobotsFetch::Body(String::new()));
        let c = cache_with_ttls(f.clone(), Duration::from_secs(60), Duration::from_secs(10));

        assert!(
            c.allowed("https://example.org", "/anything", MissingPolicy::Deny)
                .await
        );
        assert_eq!(f.calls(), 1);

        tokio::time::advance(Duration::from_secs(60)).await;
        f.set(RobotsFetch::Unreachable);
        assert!(
            !c.allowed("https://example.org", "/anything", MissingPolicy::Deny)
                .await
        );
        assert_eq!(f.calls(), 2, "expired good policy was not re-fetched");

        f.set(RobotsFetch::Body(String::new()));
        tokio::time::advance(Duration::from_secs(9)).await;
        assert!(
            !c.allowed("https://example.org", "/anything", MissingPolicy::Deny)
                .await
        );
        assert_eq!(
            f.calls(),
            2,
            "overwriting unreachable result re-fetched before its TTL"
        );

        tokio::time::advance(Duration::from_secs(1)).await;
        assert!(
            c.allowed("https://example.org", "/anything", MissingPolicy::Deny)
                .await
        );
        assert_eq!(
            f.calls(),
            3,
            "overwriting unreachable result was not retried at its TTL"
        );
    }

    #[tokio::test]
    async fn a_404_denies_by_default_but_a_source_can_opt_into_the_rfc_reading() {
        // Default (the conservative per-source value): absence of a stated
        // permission is not permission.
        let c = cache_with(FakeFetcher::new(RobotsFetch::Unavailable));
        assert!(
            !c.allowed("https://example.org", "/anything", MissingPolicy::Deny)
                .await
        );

        // A source the operator has explicitly vetted (arXiv OAI-PMH is the real
        // case) opts into RFC-9309 behavior: a 404 robots.txt ⇒ crawl allowed.
        // Same cache, same origin — only the per-source disposition changes.
        assert!(
            c.allowed(
                "https://example.org",
                "/anything",
                MissingPolicy::RfcAllowAll
            )
            .await
        );
    }

    #[tokio::test]
    async fn opting_into_allow_on_missing_does_not_override_an_explicit_disallow() {
        // The knob only reinterprets *absence*. A publisher who actually
        // published a Disallow is still obeyed, even for an opted-in source —
        // otherwise "allow if absent" would silently become "ignore robots.txt".
        let c = cache_with(FakeFetcher::new(RobotsFetch::Body(
            "User-agent: *\nDisallow: /secret\n".into(),
        )));
        assert!(
            !c.allowed(
                "https://example.org",
                "/secret/x",
                MissingPolicy::RfcAllowAll
            )
            .await
        );
        assert!(
            c.allowed(
                "https://example.org",
                "/public/x",
                MissingPolicy::RfcAllowAll
            )
            .await
        );
    }

    #[tokio::test]
    async fn opting_into_allow_on_missing_does_not_override_unreachable() {
        // 5xx / timeout still fails closed regardless of the per-source knob:
        // we do not know the policy, so we take nothing.
        let c = cache_with(FakeFetcher::new(RobotsFetch::Unreachable));
        assert!(
            !c.allowed(
                "https://example.org",
                "/anything",
                MissingPolicy::RfcAllowAll
            )
            .await
        );
    }

    #[tokio::test]
    async fn an_empty_body_is_allow_all_and_is_not_confused_with_a_404() {
        // The distinction that matters: the server *did* answer, and said
        // "no restrictions". That is a permission; a 404 is not.
        let c = cache_with(FakeFetcher::new(RobotsFetch::Body(String::new())));
        assert!(
            c.allowed("https://example.org", "/anything", MissingPolicy::Deny)
                .await
        );
    }

    #[tokio::test]
    async fn a_policy_is_fetched_once_per_origin_and_then_cached() {
        let f = FakeFetcher::new(RobotsFetch::Body(FIXTURE.into()));
        let c = cache_with(f.clone());
        for _ in 0..5 {
            c.allowed("https://example.org", "/data/open", MissingPolicy::Deny)
                .await;
        }
        c.allowed("https://other.example", "/x", MissingPolicy::Deny)
            .await;
        assert_eq!(f.calls(), 2, "one fetch per origin, not per request");
        assert_eq!(c.fetches(), 2);
    }

    #[tokio::test(start_paused = true)]
    async fn the_cache_honors_its_ttl() {
        let f = FakeFetcher::new(RobotsFetch::Body("User-agent: *\nDisallow: /x\n".into()));
        let c = RobotsCache::new(
            f.clone(),
            Arc::new(HostLimiters::per_second(1000.0)),
            "intel-platform/0.1",
            Duration::from_secs(600),
            64,
        );
        assert!(
            !c.allowed("https://example.org", "/x", MissingPolicy::Deny)
                .await
        );
        assert_eq!(f.calls(), 1);

        // Within the TTL: served from cache, and a changed upstream is NOT seen.
        f.set(RobotsFetch::Body(String::new()));
        tokio::time::advance(Duration::from_secs(300)).await;
        assert!(
            !c.allowed("https://example.org", "/x", MissingPolicy::Deny)
                .await
        );
        assert_eq!(f.calls(), 1);

        // Past the TTL: re-fetched, and the new policy takes effect.
        tokio::time::advance(Duration::from_secs(400)).await;
        assert!(
            c.allowed("https://example.org", "/x", MissingPolicy::Deny)
                .await
        );
        assert_eq!(f.calls(), 2);
    }

    #[tokio::test]
    async fn the_cache_is_bounded() {
        let f = FakeFetcher::new(RobotsFetch::Body(String::new()));
        let c = RobotsCache::new(
            f.clone(),
            Arc::new(HostLimiters::per_second(1000.0)),
            "intel-platform/0.1",
            Duration::from_secs(3600),
            2,
        );
        for i in 0..10 {
            c.allowed(&format!("https://h{i}.example"), "/x", MissingPolicy::Deny)
                .await;
        }
        assert_eq!(
            c.entries.lock().unwrap().len(),
            2,
            "cache grew past its capacity"
        );
    }

    #[tokio::test]
    async fn fetching_robots_txt_is_itself_rate_limited() {
        // Asking for the politeness file is still asking. It goes through the
        // same per-host clock as everything else.
        let lim = Arc::new(HostLimiters::per_second(1000.0));
        let c = RobotsCache::new(
            FakeFetcher::new(RobotsFetch::Body(String::new())),
            lim.clone(),
            "intel-platform/0.1",
            Duration::from_secs(3600),
            64,
        );
        c.allowed("https://example.org", "/x", MissingPolicy::Deny)
            .await;
        assert_eq!(lim.acquires_for("example.org"), 1);
    }

    #[tokio::test]
    async fn a_published_crawl_delay_can_slow_us_down_but_never_speed_us_up() {
        let lim = Arc::new(HostLimiters::per_second(2.0)); // our floor: 0.5s
        let c = RobotsCache::new(
            FakeFetcher::new(RobotsFetch::Body("User-agent: *\nCrawl-delay: 10\n".into())),
            lim.clone(),
            "intel-platform/0.1",
            Duration::from_secs(3600),
            64,
        );
        c.apply_crawl_delay("https://slow.example").await;
        assert!(
            (lim.rate_for("slow.example") - 0.1).abs() < 1e-9,
            "10s delay not adopted"
        );

        // Now a publisher who says "go faster than our floor". We do not.
        let c = RobotsCache::new(
            FakeFetcher::new(RobotsFetch::Body(
                "User-agent: *\nCrawl-delay: 0.01\n".into(),
            )),
            lim.clone(),
            "intel-platform/0.1",
            Duration::from_secs(3600),
            64,
        );
        c.apply_crawl_delay("https://fast.example").await;
        assert!(
            lim.rate_for("fast.example") <= 2.0,
            "a robots.txt talked us into exceeding our own politeness floor"
        );
    }

    #[tokio::test(start_paused = true)]
    async fn crawl_delay_update_preserves_clock_counter_and_waits_new_interval() {
        let limiters = Arc::new(HostLimiters::per_second(2.0));
        let cache = RobotsCache::new(
            FakeFetcher::new(RobotsFetch::Body("User-agent: *\nCrawl-delay: 10\n".into())),
            limiters.clone(),
            "intel-platform/0.1",
            Duration::from_secs(3600),
            64,
        );
        let origin = "https://clock.example";
        let host = "clock.example";

        // Fetching robots.txt is the first acquisition and sets the host clock.
        assert!(
            cache
                .allowed(origin, "/document", MissingPolicy::Deny)
                .await
        );
        assert_eq!(limiters.acquires_for(host), 1);

        // The synchronous rate transition must mutate the existing limiter,
        // preserving both that clock and its acquisition counter.
        cache.apply_crawl_delay(origin).await;
        assert!((limiters.rate_for(host) - 0.1).abs() < 1e-9);
        assert_eq!(limiters.acquires_for(host), 1);

        let started = Instant::now();
        let waiting_limiters = limiters.clone();
        let waiter = tokio::spawn(async move {
            waiting_limiters.acquire(host).await;
        });
        tokio::task::yield_now().await;
        assert_eq!(limiters.acquires_for(host), 2);
        assert!(!waiter.is_finished(), "the new delay was not applied");

        tokio::time::advance(Duration::from_secs(9)).await;
        tokio::task::yield_now().await;
        assert!(
            !waiter.is_finished(),
            "the limiter released before 10 seconds"
        );

        tokio::time::advance(Duration::from_secs(1)).await;
        waiter.await.unwrap();
        assert_eq!(started.elapsed(), Duration::from_secs(10));
        assert_eq!(limiters.acquires_for(host), 2);
    }

    #[tokio::test]
    async fn limiters_are_per_host() {
        let l = HostLimiters::per_second(1000.0);
        l.acquire("a.example").await;
        l.acquire("a.example").await;
        l.acquire("b.example").await;

        assert_eq!(l.acquires(), 3);
        assert_eq!(l.acquires_for("a.example"), 2);
        assert_eq!(l.acquires_for("b.example"), 1);
        assert_eq!(l.hosts(), vec!["a.example", "b.example"]);
    }

    #[tokio::test]
    async fn a_slow_host_does_not_throttle_a_fast_one() {
        let l = HostLimiters::per_second(1000.0);
        l.set_host_rate("slow.example", 0.5); // 2s between requests

        // Prime the slow host, then hit the fast host twice. If the limiters
        // were shared, the second fast call would wait on the slow host's clock.
        l.acquire("slow.example").await;
        let t0 = std::time::Instant::now();
        l.acquire("fast.example").await;
        l.acquire("fast.example").await;
        assert!(
            t0.elapsed() < Duration::from_millis(500),
            "fast host was throttled by the slow host's clock"
        );
    }
}
