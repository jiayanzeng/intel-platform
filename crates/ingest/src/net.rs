//! Real HTTP fetching (enabled with `--features net`).
//!
//! Identify yourself: a descriptive User-Agent with contact info is both
//! polite and, for endpoints like arXiv OAI, expected of harvesters. OAI-PMH
//! endpoints throttle harvesters with `503 Retry-After`; we honor it with a
//! bounded backoff (HC8). Production additions: conditional GET (ETag /
//! If-Modified-Since) and a per-host client pool.

use crate::IngestError;
use intel_compliance::{RobotsFetch, RobotsFetcher};
use std::time::Duration;

/// The User-Agent we identify ourselves with — and, necessarily, the same token
/// a publisher's `robots.txt` will name if they want to address us
/// specifically. It is passed to `RobotsCache` so group selection matches the
/// identity we actually send on the wire; a crawler that obeys the rules
/// written for a *different* UA than the one it presents is not obeying them.
pub const USER_AGENT: &str = "intel-platform/0.1 (research prototype; contact: you@example.com)";

/// How long a fetched `robots.txt` stays authoritative before we re-ask.
pub const ROBOTS_TTL: Duration = Duration::from_secs(24 * 3600);
/// Bound on the number of origins cached, so a config pointing at many hosts
/// cannot grow the cache without limit.
pub const ROBOTS_CAPACITY: usize = 512;

/// Live `robots.txt` fetcher.
///
/// Note what this does NOT do: it never returns `Err`. Every failure is mapped
/// onto a `RobotsFetch` variant, because the difference between "404, no policy
/// exists" and "500, we could not learn the policy" is a *compliance* decision,
/// not an I/O detail — and an `Err` type invites a caller to `?` past it.
/// Making the caller match on the outcome is the point.
pub struct HttpRobotsFetcher {
    client: reqwest::Client,
}

impl HttpRobotsFetcher {
    pub fn new() -> Result<Self, IngestError> {
        Ok(Self {
            client: reqwest::Client::builder()
                .user_agent(USER_AGENT)
                .timeout(Duration::from_secs(15))
                .build()
                .map_err(|e| IngestError::Http(e.to_string()))?,
        })
    }
}

#[async_trait::async_trait]
impl RobotsFetcher for HttpRobotsFetcher {
    async fn fetch(&self, robots_url: &str) -> RobotsFetch {
        let resp = match self.client.get(robots_url).send().await {
            Ok(r) => r,
            // DNS failure, TLS failure, connection refused, timeout: we do not
            // know this publisher's policy. RFC 9309 §2.3.1.4 ⇒ Unreachable.
            Err(_) => return RobotsFetch::Unreachable,
        };
        let status = resp.status();
        if status.is_success() {
            return match resp.text().await {
                Ok(body) => RobotsFetch::Body(body),
                // Answered, but we could not read it — same epistemic position
                // as never having asked.
                Err(_) => RobotsFetch::Unreachable,
            };
        }
        if status.is_client_error() {
            // 404 and friends: the server is telling us there is no policy here.
            return RobotsFetch::Unavailable;
        }
        // 5xx (and anything else odd): unreachable, so deny.
        RobotsFetch::Unreachable
    }
}

/// Bound on `503 Retry-After` retries before giving up, so a wedged endpoint
/// can't hang a harvest indefinitely.
const MAX_RETRIES: u32 = 5;
/// Fallback wait when a 503 omits a parseable `Retry-After` (arXiv's suggested
/// spacing).
const DEFAULT_RETRY_SECS: u64 = 3;

pub async fn get_text(url: &str) -> Result<String, IngestError> {
    let client = reqwest::Client::builder()
        .user_agent(USER_AGENT)
        // A per-request timeout is not optional on a live harvester. Without it,
        // a server that accepts the connection and then stalls holds the whole
        // ingest open indefinitely — which is exactly what "hung for 26 minutes
        // with no output" looks like from the outside. 60s is generous for a
        // 1000-record OAI page yet bounds the worst case. The 503/Retry-After
        // sleep below is separate and deliberate; this only catches a dead
        // connection, not a server politely asking us to wait.
        .timeout(Duration::from_secs(60))
        .connect_timeout(Duration::from_secs(15))
        .build()
        .map_err(|e| IngestError::Http(e.to_string()))?;

    for attempt in 0..=MAX_RETRIES {
        let resp = client
            .get(url)
            .send()
            .await
            .map_err(|e| IngestError::Http(e.to_string()))?;
        let status = resp.status();
        if status.is_success() {
            return resp.text().await.map_err(|e| IngestError::Http(e.to_string()));
        }
        // Honor 503 Retry-After (seconds form) with bounded retries.
        if status.as_u16() == 503 && attempt < MAX_RETRIES {
            let wait = resp
                .headers()
                .get(reqwest::header::RETRY_AFTER)
                .and_then(|v| v.to_str().ok())
                .and_then(|s| s.trim().parse::<u64>().ok())
                .unwrap_or(DEFAULT_RETRY_SECS);
            tokio::time::sleep(Duration::from_secs(wait)).await;
            continue;
        }
        return Err(IngestError::Http(format!("{status} for {url}")));
    }
    Err(IngestError::Http(format!(
        "giving up after {MAX_RETRIES} retries (503) for {url}"
    )))
}
