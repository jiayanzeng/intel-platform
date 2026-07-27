//! Real HTTP fetching (enabled with `--features net`).
//!
//! Identify yourself: a descriptive User-Agent with contact info is both
//! polite and, for endpoints like arXiv OAI, expected of harvesters. OAI-PMH
//! endpoints throttle harvesters with `503 Retry-After`; we honor it with a
//! bounded backoff (HC8). Production additions: conditional GET (ETag /
//! If-Modified-Since) and a per-host client pool.

use crate::{gate, IngestError, Reach, SourceContext};
use intel_compliance::{MissingPolicy, RobotsFetch, RobotsFetcher};
use reqwest::redirect::Policy;
use std::sync::OnceLock;
use std::time::Duration;

/// Structural product token used for publisher `robots.txt` group selection.
///
/// This is deliberately not operator-configurable: the full User-Agent handed
/// to `RobotsCache` must start with the same stable token sent on the wire. A
/// typo here would select one publisher policy while presenting another
/// identity (the group-selection reason documented at lines 14–18).
pub const PRODUCT_TOKEN: &str = "intel-platform";

static USER_AGENT: OnceLock<String> = OnceLock::new();

/// Construct the one process identity from the product crate's version and the
/// operator-supplied contact substring.
pub fn crawler_user_agent(version: &str, contact: &str) -> String {
    format!("{PRODUCT_TOKEN}/{version} (research prototype; contact: {contact})")
}

/// Install the exact identity shared by both HTTP clients and `RobotsCache`.
///
/// A process cannot change identity after it has begun fetching. Reinstalling
/// the same bytes is harmless; a different identity is refused.
pub fn install_crawler_user_agent(
    version: &str,
    contact: &str,
) -> Result<&'static str, IngestError> {
    let user_agent = crawler_user_agent(version, contact);
    let installed = USER_AGENT.get_or_init(|| user_agent.clone());
    if installed == &user_agent {
        return Ok(installed.as_str());
    }
    Err(IngestError::Http(
        "crawler User-Agent is already configured with different bytes".to_string(),
    ))
}

fn configured_user_agent() -> Result<&'static str, IngestError> {
    USER_AGENT
        .get()
        .map(String::as_str)
        .ok_or_else(|| IngestError::Http("crawler User-Agent is not configured".to_string()))
}

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
        let user_agent = configured_user_agent()?;
        Ok(Self {
            client: reqwest::Client::builder()
                .user_agent(user_agent)
                .timeout(Duration::from_secs(15))
                // A robots request must never follow silently to a different
                // origin. A redirect is treated as unreachable (fail closed),
                // while document redirects are followed manually below.
                .redirect(Policy::none())
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
/// Match reqwest's former default bound while making every hop explicit.
const MAX_REDIRECTS: u32 = 10;

#[derive(Clone, Debug)]
struct PageResponse {
    status: u16,
    location: Option<String>,
    retry_after_secs: Option<u64>,
    body: Option<String>,
}

#[async_trait::async_trait]
trait PageFetcher: Send + Sync {
    async fn fetch(&self, url: &str) -> Result<PageResponse, IngestError>;
}

struct ReqwestPageFetcher {
    client: reqwest::Client,
}

impl ReqwestPageFetcher {
    fn new() -> Result<Self, IngestError> {
        let user_agent = configured_user_agent()?;
        Ok(Self {
            client: reqwest::Client::builder()
                .user_agent(user_agent)
                // Every Location is resolved below, and the robots gate runs
                // before the next request. Automatic redirects would ask the
                // new origin for content before asking it for permission.
                .redirect(Policy::none())
                // A per-request timeout is not optional on a live harvester.
                // 60s is generous for a 1000-record OAI page yet bounds a dead
                // connection; Retry-After sleeping remains separate.
                .timeout(Duration::from_secs(60))
                .connect_timeout(Duration::from_secs(15))
                .build()
                .map_err(|e| IngestError::Http(e.to_string()))?,
        })
    }
}

#[async_trait::async_trait]
impl PageFetcher for ReqwestPageFetcher {
    async fn fetch(&self, url: &str) -> Result<PageResponse, IngestError> {
        let response = self
            .client
            .get(url)
            .send()
            .await
            .map_err(|e| IngestError::Http(e.to_string()))?;
        let status = response.status();
        let location = response
            .headers()
            .get(reqwest::header::LOCATION)
            .and_then(|value| value.to_str().ok())
            .map(str::to_string);
        let retry_after_secs = response
            .headers()
            .get(reqwest::header::RETRY_AFTER)
            .and_then(|value| value.to_str().ok())
            .and_then(|value| value.trim().parse::<u64>().ok());
        let body = if status.is_success() {
            Some(
                response
                    .text()
                    .await
                    .map_err(|e| IngestError::Http(e.to_string()))?,
            )
        } else {
            None
        };

        Ok(PageResponse {
            status: status.as_u16(),
            location,
            retry_after_secs,
            body,
        })
    }
}

pub async fn get_text(
    ctx: &SourceContext,
    url: &str,
    on_missing: MissingPolicy,
) -> Result<String, IngestError> {
    let fetcher = ReqwestPageFetcher::new()?;
    get_text_with(ctx, url, on_missing, &fetcher).await
}

async fn get_text_with(
    ctx: &SourceContext,
    url: &str,
    on_missing: MissingPolicy,
    fetcher: &dyn PageFetcher,
) -> Result<String, IngestError> {
    let mut current = reqwest::Url::parse(url)
        .map_err(|error| IngestError::Http(format!("invalid URL {url}: {error}")))?;
    let mut redirects = 0_u32;
    let mut retries = 0_u32;

    loop {
        // This is deliberately before fetch(). On a cross-origin Location, the
        // new origin's robots.txt is read and honored before any document
        // request reaches that origin.
        gate(ctx, current.as_str(), Reach::Network, on_missing).await?;
        let response = fetcher.fetch(current.as_str()).await?;

        if (200..300).contains(&response.status) {
            return response.body.ok_or_else(|| {
                IngestError::Http(format!("empty successful response for {current}"))
            });
        }

        if matches!(response.status, 301 | 302 | 303 | 307 | 308) {
            if redirects >= MAX_REDIRECTS {
                return Err(IngestError::Http(format!(
                    "giving up after {MAX_REDIRECTS} redirects for {url}"
                )));
            }
            let location = response.location.ok_or_else(|| {
                IngestError::Http(format!(
                    "redirect {} without Location for {current}",
                    response.status
                ))
            })?;
            let next = current.join(&location).map_err(|error| {
                IngestError::Http(format!(
                    "invalid redirect from {current} to {location}: {error}"
                ))
            })?;
            if !matches!(next.scheme(), "http" | "https") {
                return Err(IngestError::Http(format!(
                    "refusing non-HTTP redirect from {current} to {next}"
                )));
            }
            current = next;
            redirects += 1;
            retries = 0;
            continue;
        }

        // Honor 503 Retry-After (seconds form) with bounded retries.
        if response.status == 503 && retries < MAX_RETRIES {
            tokio::time::sleep(Duration::from_secs(
                response.retry_after_secs.unwrap_or(DEFAULT_RETRY_SECS),
            ))
            .await;
            retries += 1;
            continue;
        }

        return Err(IngestError::Http(format!(
            "HTTP {} for {current}",
            response.status
        )));
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use intel_compliance::{HostLimiters, RobotsCache, RobotsGate};
    use std::collections::HashMap;
    use std::io::{Read, Write};
    use std::net::{Shutdown, TcpListener};
    use std::sync::mpsc;
    use std::sync::{Arc, Mutex};
    use std::thread;

    struct FakePageFetcher {
        responses: HashMap<String, PageResponse>,
        calls: Mutex<Vec<String>>,
    }

    impl FakePageFetcher {
        fn new(responses: impl IntoIterator<Item = (&'static str, PageResponse)>) -> Self {
            Self {
                responses: responses
                    .into_iter()
                    .map(|(url, response)| (url.to_string(), response))
                    .collect(),
                calls: Mutex::new(Vec::new()),
            }
        }

        fn calls(&self) -> Vec<String> {
            self.calls.lock().unwrap().clone()
        }
    }

    #[async_trait::async_trait]
    impl PageFetcher for FakePageFetcher {
        async fn fetch(&self, url: &str) -> Result<PageResponse, IngestError> {
            self.calls.lock().unwrap().push(url.to_string());
            self.responses
                .get(url)
                .cloned()
                .ok_or_else(|| IngestError::Http(format!("unexpected page fetch: {url}")))
        }
    }

    struct PolicyRobotsFetcher {
        responses: HashMap<String, RobotsFetch>,
        calls: Mutex<Vec<String>>,
    }

    impl PolicyRobotsFetcher {
        fn new(responses: impl IntoIterator<Item = (&'static str, RobotsFetch)>) -> Arc<Self> {
            Arc::new(Self {
                responses: responses
                    .into_iter()
                    .map(|(url, response)| (url.to_string(), response))
                    .collect(),
                calls: Mutex::new(Vec::new()),
            })
        }

        fn calls(&self) -> Vec<String> {
            self.calls.lock().unwrap().clone()
        }
    }

    #[async_trait::async_trait]
    impl RobotsFetcher for PolicyRobotsFetcher {
        async fn fetch(&self, robots_url: &str) -> RobotsFetch {
            self.calls.lock().unwrap().push(robots_url.to_string());
            self.responses
                .get(robots_url)
                .cloned()
                .unwrap_or(RobotsFetch::Unreachable)
        }
    }

    fn context(fetcher: Arc<PolicyRobotsFetcher>) -> SourceContext {
        let limiter = Arc::new(HostLimiters::per_second(1000.0));
        let user_agent = crawler_user_agent("test", "crawler-tests@unit.test");
        SourceContext {
            robots: RobotsGate::new(&[]),
            limiter: limiter.clone(),
            cursors: None,
            robots_cache: Some(Arc::new(RobotsCache::new(
                fetcher,
                limiter,
                user_agent,
                Duration::from_secs(3600),
                16,
            ))),
        }
    }

    fn redirect(location: &str) -> PageResponse {
        PageResponse {
            status: 302,
            location: Some(location.to_string()),
            retry_after_secs: None,
            body: None,
        }
    }

    fn ok(body: &str) -> PageResponse {
        PageResponse {
            status: 200,
            location: None,
            retry_after_secs: None,
            body: Some(body.to_string()),
        }
    }

    fn user_agent_wire_server(
        requests: usize,
    ) -> (String, mpsc::Receiver<String>, thread::JoinHandle<()>) {
        let listener = TcpListener::bind("127.0.0.1:0").expect("bind wire server");
        let address = listener.local_addr().expect("wire server address");
        let (sender, receiver) = mpsc::channel();
        let handle = thread::spawn(move || {
            for stream in listener.incoming().take(requests) {
                let mut stream = stream.expect("accept wire request");
                let mut request = Vec::new();
                let mut buffer = [0_u8; 1024];
                while !request.windows(4).any(|window| window == b"\r\n\r\n") {
                    let read = stream.read(&mut buffer).expect("read wire request");
                    if read == 0 {
                        break;
                    }
                    request.extend_from_slice(&buffer[..read]);
                }
                let headers = String::from_utf8(request).expect("HTTP headers are UTF-8");
                let user_agent = headers
                    .lines()
                    .find_map(|line| {
                        let (name, value) = line.split_once(':')?;
                        name.eq_ignore_ascii_case("user-agent")
                            .then(|| value.trim().to_string())
                    })
                    .expect("wire request carries User-Agent");
                sender.send(user_agent).expect("record User-Agent");
                stream
                    .write_all(
                        b"HTTP/1.1 200 OK\r\nContent-Length: 2\r\nConnection: close\r\n\r\nok",
                    )
                    .expect("write wire response");
                stream.flush().expect("flush wire response");
                stream
                    .shutdown(Shutdown::Write)
                    .expect("finish wire response");
            }
        });
        (format!("http://{address}"), receiver, handle)
    }

    #[tokio::test]
    async fn both_live_clients_send_the_installed_user_agent_byte_identically() {
        let expected = crawler_user_agent("0.12.0", "wire-contact@unit.test");
        let installed = install_crawler_user_agent("0.12.0", "wire-contact@unit.test")
            .expect("install identity");
        assert_eq!(installed, expected);

        let (base_url, receiver, server) = user_agent_wire_server(2);
        let pages = ReqwestPageFetcher::new().expect("build page client");
        let page = pages
            .fetch(&format!("{base_url}/document"))
            .await
            .expect("fetch document");
        assert_eq!(page.status, 200);
        let robots = HttpRobotsFetcher::new().expect("build robots client");
        let robots_result = robots.fetch(&format!("{base_url}/robots.txt")).await;
        assert_eq!(robots_result, RobotsFetch::Body("ok".to_string()));

        let page_user_agent = receiver
            .recv_timeout(Duration::from_secs(2))
            .expect("document User-Agent");
        let robots_user_agent = receiver
            .recv_timeout(Duration::from_secs(2))
            .expect("robots User-Agent");
        server.join().expect("wire server exits");
        assert_eq!(page_user_agent, expected);
        assert_eq!(robots_user_agent, expected);
    }

    #[test]
    fn concurrent_identity_installation_is_atomic_and_mismatch_is_deterministic() {
        const INSTALLERS: usize = 64;
        let barrier = Arc::new(std::sync::Barrier::new(INSTALLERS));
        let installers = (0..INSTALLERS)
            .map(|_| {
                let barrier = barrier.clone();
                thread::spawn(move || {
                    barrier.wait();
                    install_crawler_user_agent("0.12.0", "wire-contact@unit.test")
                })
            })
            .collect::<Vec<_>>();

        let expected = crawler_user_agent("0.12.0", "wire-contact@unit.test");
        for installer in installers {
            let installed = installer
                .join()
                .expect("identity installer thread")
                .expect("identical identity installation");
            assert_eq!(installed, expected);
        }

        let error = install_crawler_user_agent("0.12.0", "different-contact@unit.test")
            .expect_err("different identity bytes must be refused");
        assert_eq!(
            error.to_string(),
            "http: crawler User-Agent is already configured with different bytes"
        );
    }

    #[tokio::test]
    async fn cross_origin_redirect_reads_and_honors_new_robots_before_fetching() {
        let robots = PolicyRobotsFetcher::new([
            (
                "https://first.test/robots.txt",
                RobotsFetch::Body("User-agent: *\nAllow: /\n".to_string()),
            ),
            (
                "https://second.test/robots.txt",
                RobotsFetch::Body("User-agent: *\nDisallow: /blocked\n".to_string()),
            ),
        ]);
        let ctx = context(robots.clone());
        let pages = FakePageFetcher::new([
            (
                "https://first.test/start",
                redirect("https://second.test/blocked"),
            ),
            (
                "https://second.test/blocked",
                ok("this body must never be requested"),
            ),
        ]);

        let error = get_text_with(
            &ctx,
            "https://first.test/start",
            MissingPolicy::Deny,
            &pages,
        )
        .await
        .expect_err("second origin denies the redirected path");

        assert!(matches!(
            error,
            IngestError::RobotsDisallowed(url)
                if url == "https://second.test/blocked"
        ));
        assert_eq!(
            robots.calls(),
            vec![
                "https://first.test/robots.txt",
                "https://second.test/robots.txt"
            ]
        );
        assert_eq!(pages.calls(), vec!["https://first.test/start"]);
    }

    #[tokio::test]
    async fn same_origin_redirect_reuses_the_cached_robots_policy() {
        let robots = PolicyRobotsFetcher::new([(
            "https://same.test/robots.txt",
            RobotsFetch::Body("User-agent: *\nAllow: /\n".to_string()),
        )]);
        let ctx = context(robots.clone());
        let pages = FakePageFetcher::new([
            ("https://same.test/start", redirect("/final")),
            ("https://same.test/final", ok("finished")),
        ]);

        let body = get_text_with(&ctx, "https://same.test/start", MissingPolicy::Deny, &pages)
            .await
            .expect("same-origin redirect allowed");

        assert_eq!(body, "finished");
        assert_eq!(robots.calls(), vec!["https://same.test/robots.txt"]);
        assert_eq!(
            pages.calls(),
            vec!["https://same.test/start", "https://same.test/final"]
        );
    }
}
