//! arXiv OAI-PMH connector.
//!
//! OAI-PMH is the harvesting protocol arXiv (and thousands of institutional
//! repositories) offer explicitly for programmatic bulk access — an official
//! free channel, not a commercial gatekeeper. This parses the standard
//! `ListRecords` response with `oai_dc` metadata and follows `resumptionToken`
//! paging to completion.
//!
//! Resumability & incrementality (T4):
//! - **Paging.** Each page may end with a `<resumptionToken>`; the harvest
//!   re-requests with that token until an empty/absent token terminates it.
//!   The token is checkpointed (via `CursorStore`) after every page, so an
//!   interrupted harvest resumes from exactly where it stopped rather than
//!   restarting the whole set.
//! - **High-water mark.** On a completed harvest the max `datestamp` seen is
//!   stored and replayed as `from=` on the next run, so we fetch only records
//!   newer than last time.
//! - **Compliance.** The shared limiter is consulted on every page request
//!   (arXiv asks harvesters to space requests ~3s apart); the `net` path also
//!   honors `503 Retry-After`.
//!
//! Offline/fixture mode is the default and drives the tests: the first page is
//! the configured fixture, and a `resumptionToken` names the next fixture file
//! (resolved relative to the first page), so a fixture chain exercises the full
//! paging/cursor path with no network.

// clippy::unnecessary_map_or wants `Option::is_none_or`, stabilized in Rust
// 1.82. This crate's floor is 1.78 (STATE §5 / rust-toolchain.toml), and
// adopting is_none_or would silently raise it. The `map_or(true, ..)` form is
// correct and MSRV-safe, so the lint is allowed here deliberately.
#![allow(clippy::unnecessary_map_or)]

use crate::{child_text, child_texts, gate, IngestError, Reach, Source, SourceContext};
use async_trait::async_trait;
use intel_compliance::MissingPolicy;
use intel_core::{Day, Document, License, Provenance, SectorId, SourceKind};

pub struct ArxivOaiSource {
    pub id: String,
    pub sector: SectorId,
    /// e.g. "https://export.arxiv.org/oai2?verb=ListRecords&metadataPrefix=oai_dc&set=cs"
    pub endpoint_url: String,
    pub fixture_path: Option<String>,
    pub license: License,
    /// Per-source disposition for a 404 robots.txt. arXiv's OAI-PMH host serves
    /// no robots.txt (404) yet exists expressly to be harvested, so the operator
    /// sets this to `RfcAllowAll` for arxiv-cs; the global default stays `Deny`.
    pub robots_on_missing: MissingPolicy,
    /// Optional hard cap on pages fetched in one harvest. `None` = follow the
    /// resumptionToken to exhaustion (the historical behavior, right for an
    /// incremental catch-up harvest). `Some(n)` bounds a run — essential for a
    /// smoke test against a huge set like `set=cs`, which is otherwise hundreds
    /// of pages and tens of minutes. A capped run still checkpoints its cursor,
    /// so a later run resumes exactly where the cap stopped: bounded, not lossy.
    pub max_pages: Option<u32>,
}

/// One parsed OAI-PMH page.
struct PageParse {
    docs: Vec<Document>,
    /// Max `datestamp` on this page (for the high-water mark).
    max_datestamp: Option<String>,
    /// The `resumptionToken` text: `None` if the element is absent, `Some("")`
    /// if present but empty. Both mean "final page".
    resumption_token: Option<String>,
}

impl ArxivOaiSource {
    fn parse_page(&self, tree: &roxmltree::Document<'_>) -> PageParse {
        let mut docs = Vec::new();
        let mut max_datestamp: Option<String> = None;

        for rec in tree
            .descendants()
            .filter(|n| n.tag_name().name() == "record")
        {
            let header = rec.children().find(|c| c.tag_name().name() == "header");
            let identifier = header
                .and_then(|h| child_text(h, "identifier"))
                .unwrap_or_default();
            let datestamp = header.and_then(|h| child_text(h, "datestamp"));
            if let Some(ds) = &datestamp {
                if max_datestamp.as_deref().map_or(true, |m| ds.as_str() > m) {
                    max_datestamp = Some(ds.clone());
                }
            }

            // <metadata><oai_dc:dc> ... Dublin Core fields ... </oai_dc:dc>
            let dc = rec.descendants().find(|n| n.tag_name().name() == "dc");
            let Some(dc) = dc else { continue };

            let title = child_text(dc, "title").unwrap_or_default();
            let creators = child_texts(dc, "creator");
            let subjects = child_texts(dc, "subject");
            let description = child_text(dc, "description").unwrap_or_default();
            let dc_date = child_text(dc, "date");
            let url = child_texts(dc, "identifier")
                .into_iter()
                .find(|s| s.starts_with("http"));

            let raw_date = datestamp.clone().or(dc_date);
            docs.push(Document {
                id: format!("{}::{}", self.id, identifier),
                sector: self.sector.clone(),
                url,
                title,
                body: description,
                published_day: raw_date.as_deref().and_then(Day::parse_iso),
                published_raw: raw_date,
                authors: creators,
                tags: subjects,
                provenance: Provenance {
                    source_id: self.id.clone(),
                    retrieved_from: self.endpoint_url.clone(),
                    kind: SourceKind::OaiPmh,
                    license: self.license,
                },
            });
        }

        let resumption_token = tree
            .descendants()
            .find(|n| n.tag_name().name() == "resumptionToken")
            .map(|n| n.text().unwrap_or("").trim().to_string());

        PageParse {
            docs,
            max_datestamp,
            resumption_token,
        }
    }

    /// Fetch one page's XML. In fixture mode a `resume` token names the next
    /// fixture file (relative to the first page); in net mode it becomes the
    /// OAI-PMH resume request.
    async fn fetch_page_text(
        &self,
        resume: Option<&str>,
        _from: Option<&str>,
    ) -> Result<String, IngestError> {
        if let Some(base) = &self.fixture_path {
            let path = match resume {
                None => std::path::PathBuf::from(base),
                Some(tok) => std::path::Path::new(base)
                    .parent()
                    .unwrap_or_else(|| std::path::Path::new("."))
                    .join(tok),
            };
            return Ok(std::fs::read_to_string(path)?);
        }
        #[cfg(feature = "net")]
        {
            let url = oai_request_url(&self.endpoint_url, resume, _from);
            crate::net::get_text(&url).await
        }
        #[cfg(not(feature = "net"))]
        {
            Err(IngestError::Http(
                "no fixture configured and binary built without the 'net' feature".into(),
            ))
        }
    }
}

/// Build the URL for one OAI-PMH request.
///
/// - Resuming: the spec requires `verb` + `resumptionToken` ONLY (no other
///   args), so we strip the endpoint's query and rebuild it.
/// - Fresh with a high-water mark: append `from=` for an incremental harvest.
/// - Fresh cold start: the endpoint as configured.
#[cfg(any(feature = "net", test))]
fn oai_request_url(endpoint: &str, resume: Option<&str>, from: Option<&str>) -> String {
    match resume {
        Some(tok) => {
            let base = endpoint.split('?').next().unwrap_or(endpoint);
            format!(
                "{base}?verb=ListRecords&resumptionToken={}",
                percent_encode(tok)
            )
        }
        None => match from {
            Some(f) => format!("{endpoint}&from={}", percent_encode(f)),
            None => endpoint.to_string(),
        },
    }
}

/// Percent-encode a query value (encode everything outside the RFC 3986
/// unreserved set). Small and dependency-free; resumptionTokens can carry
/// `:`, `|`, `/`, etc.
#[cfg(any(feature = "net", test))]
fn percent_encode(s: &str) -> String {
    let mut out = String::with_capacity(s.len());
    for b in s.bytes() {
        match b {
            b'A'..=b'Z' | b'a'..=b'z' | b'0'..=b'9' | b'-' | b'.' | b'_' | b'~' => {
                out.push(b as char)
            }
            _ => out.push_str(&format!("%{b:02X}")),
        }
    }
    out
}

#[async_trait]
impl Source for ArxivOaiSource {
    fn id(&self) -> &str {
        &self.id
    }
    fn sector(&self) -> &SectorId {
        &self.sector
    }
    fn kind(&self) -> SourceKind {
        SourceKind::OaiPmh
    }

    async fn fetch(&self, ctx: &SourceContext) -> Result<Vec<Document>, IngestError> {
        let cursors = ctx.cursors.as_ref();
        // Incremental start point (only meaningful on the net path).
        let from = cursors.and_then(|c| c.high_water(&self.id));
        // Resume an interrupted harvest if a token was checkpointed.
        let mut resume: Option<String> = cursors.and_then(|c| c.resume_token(&self.id));

        let mut out: Vec<Document> = Vec::new();
        let mut max_datestamp: Option<String> = None;
        let mut page_num: u32 = 0;

        loop {
            // Compliance gate (robots + polite wait) on EVERY page request —
            // the between-pages spacing arXiv asks for. A fixture-backed harvest
            // is not a request to arXiv, so it does not fetch their robots.txt.
            let reach = if self.fixture_path.is_some() {
                Reach::Fixture
            } else {
                Reach::Network
            };
            gate(ctx, &self.endpoint_url, reach, self.robots_on_missing).await?;

            let xml = self
                .fetch_page_text(resume.as_deref(), from.as_deref())
                .await?;
            let tree =
                roxmltree::Document::parse(&xml).map_err(|e| IngestError::Parse(e.to_string()))?;
            let page = self.parse_page(&tree);
            page_num += 1;

            if let Some(ds) = page.max_datestamp {
                if max_datestamp.as_deref().map_or(true, |m| ds.as_str() > m) {
                    max_datestamp = Some(ds);
                }
            }
            out.extend(page.docs);
            let total = out.len();

            // Empty or absent token terminates the harvest.
            let next = page.resumption_token.filter(|t| !t.is_empty());

            // A live harvest of a large set is otherwise a silent black box: the
            // difference between "working" and "hung" is invisible without this.
            // Only chatter on the network path — fixture runs must stay quiet so
            // the golden pipeline output does not change.
            if reach == Reach::Network {
                eprintln!(
                    "  [{}] page {page_num}: total {total} docs so far, {}",
                    self.id,
                    if next.is_some() {
                        "more pages follow"
                    } else {
                        "last page"
                    }
                );
            }

            // Checkpoint after each page so an interrupt resumes here, not at
            // the start of the set.
            if let Some(c) = cursors {
                c.checkpoint(&self.id, next.as_deref());
            }

            match next {
                Some(t) => {
                    // Hard page cap: stop a bounded run cleanly. The cursor is
                    // already checkpointed above, so the *next* harvest picks up
                    // from this token — the cap bounds one run, it does not drop
                    // records.
                    if let Some(cap) = self.max_pages {
                        if page_num >= cap {
                            if reach == Reach::Network {
                                eprintln!(
                                    "  [{}] page cap {cap} reached; stopping. Re-run to continue from the checkpoint.",
                                    self.id
                                );
                            }
                            break;
                        }
                    }
                    resume = Some(t);
                }
                None => break,
            }
        }

        // Harvest complete: clear the in-flight token, advance the high-water
        // mark to the newest datestamp seen this run.
        if let Some(c) = cursors {
            c.complete(&self.id, max_datestamp.as_deref());
        }
        Ok(out)
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::CursorStore;
    use intel_compliance::{HostLimiters, RobotsGate};
    use std::collections::HashMap;
    use std::sync::{Arc, Mutex};

    // --- an in-memory CursorStore that records every checkpoint ------------------

    #[derive(Default)]
    struct FakeCursors {
        resume: Mutex<HashMap<String, String>>,
        high_water: Mutex<HashMap<String, String>>,
        checkpoints: Mutex<Vec<Option<String>>>,
        completes: Mutex<Vec<Option<String>>>,
    }

    impl FakeCursors {
        fn seed_resume(&self, source_id: &str, token: &str) {
            self.resume
                .lock()
                .unwrap()
                .insert(source_id.to_string(), token.to_string());
        }
    }

    impl CursorStore for FakeCursors {
        fn resume_token(&self, source_id: &str) -> Option<String> {
            self.resume.lock().unwrap().get(source_id).cloned()
        }
        fn high_water(&self, source_id: &str) -> Option<String> {
            self.high_water.lock().unwrap().get(source_id).cloned()
        }
        fn checkpoint(&self, source_id: &str, token: Option<&str>) {
            self.checkpoints
                .lock()
                .unwrap()
                .push(token.map(str::to_string));
            match token {
                Some(t) => {
                    self.resume
                        .lock()
                        .unwrap()
                        .insert(source_id.to_string(), t.to_string());
                }
                None => {
                    self.resume.lock().unwrap().remove(source_id);
                }
            }
        }
        fn complete(&self, source_id: &str, high_water: Option<&str>) {
            self.completes
                .lock()
                .unwrap()
                .push(high_water.map(str::to_string));
            self.resume.lock().unwrap().remove(source_id);
            if let Some(hw) = high_water {
                self.high_water
                    .lock()
                    .unwrap()
                    .insert(source_id.to_string(), hw.to_string());
            }
        }
    }

    fn fixture(name: &str) -> String {
        format!("{}/tests/fixtures/{}", env!("CARGO_MANIFEST_DIR"), name)
    }

    // The single-page fixture committed at the workspace root (crates/ingest ->
    // ../.. is the repo root).
    fn repo_fixture(name: &str) -> String {
        format!("{}/../../fixtures/{}", env!("CARGO_MANIFEST_DIR"), name)
    }

    fn source_at(path: String) -> ArxivOaiSource {
        ArxivOaiSource {
            id: "arxiv-cs".into(),
            sector: SectorId::new("science"),
            endpoint_url:
                "https://export.arxiv.org/oai2?verb=ListRecords&metadataPrefix=oai_dc&set=cs".into(),
            fixture_path: Some(path),
            robots_on_missing: MissingPolicy::default(),
            max_pages: None,
            license: License::IndexOnly,
        }
    }

    fn ctx(limiter: Arc<HostLimiters>, cursors: Arc<dyn CursorStore>) -> SourceContext {
        SourceContext {
            robots: RobotsGate::new(&[]),
            robots_cache: None,
            limiter,
            cursors: Some(cursors),
        }
    }

    fn source(fixture_name: &str) -> ArxivOaiSource {
        ArxivOaiSource {
            id: "arxiv-cs".into(),
            sector: SectorId::new("science"),
            endpoint_url:
                "https://export.arxiv.org/oai2?verb=ListRecords&metadataPrefix=oai_dc&set=cs".into(),
            fixture_path: Some(fixture(fixture_name)),
            robots_on_missing: MissingPolicy::default(),
            max_pages: None,
            license: License::IndexOnly,
        }
    }

    fn doc_ids(docs: &[Document]) -> Vec<String> {
        docs.iter().map(|d| d.id.clone()).collect()
    }

    // (a) pagination follows page1 -> token -> page2 -> empty; ingests the union.
    #[tokio::test]
    async fn paging_follows_chain_and_ingests_union() {
        let cur: Arc<FakeCursors> = Arc::new(FakeCursors::default());
        let lim = Arc::new(HostLimiters::per_second(1000.0));
        let docs = source("oai_page1.xml")
            .fetch(&ctx(lim, cur.clone()))
            .await
            .unwrap();
        // 2 from page1 + 2 from page2.
        assert_eq!(docs.len(), 4);
        let ids = doc_ids(&docs);
        assert!(ids.iter().any(|i| i.ends_with("2607.00101"))); // page1
        assert!(ids.iter().any(|i| i.ends_with("2607.02201"))); // page2
    }

    // (a') a page cap bounds ONE run without dropping records: it stops after
    // the cap and checkpoints the next token, so a later run resumes there.
    // This is the guard against an unbounded `set=cs` harvest running for tens
    // of minutes — a real behavior only the first live run exposed.
    #[tokio::test]
    async fn max_pages_bounds_one_run_and_checkpoints_the_rest() {
        let cur: Arc<FakeCursors> = Arc::new(FakeCursors::default());
        let lim = Arc::new(HostLimiters::per_second(1000.0));
        let mut s = source("oai_page1.xml");
        s.max_pages = Some(1); // stop after the first page

        let docs = s.fetch(&ctx(lim, cur.clone())).await.unwrap();
        // Only page1's 2 docs — page2 was not fetched.
        assert_eq!(docs.len(), 2, "cap should stop the harvest after one page");
        let ids = doc_ids(&docs);
        assert!(
            ids.iter().any(|i| i.ends_with("2607.00101")),
            "page1 doc present"
        );
        assert!(
            !ids.iter().any(|i| i.ends_with("2607.02201")),
            "page2 doc must be absent"
        );

        // The next token is checkpointed, NOT the terminal None — so a resume
        // continues from page2. A cap bounds a run; it does not lose records.
        let checkpoints = cur.checkpoints.lock().unwrap().clone();
        assert_eq!(checkpoints, vec![Some("oai_page2.xml".to_string())]);
    }

    // (b) the in-flight token is checkpointed after each page...
    #[tokio::test]
    async fn token_is_checkpointed_mid_harvest() {
        let cur: Arc<FakeCursors> = Arc::new(FakeCursors::default());
        let lim = Arc::new(HostLimiters::per_second(1000.0));
        source("oai_page1.xml")
            .fetch(&ctx(lim, cur.clone()))
            .await
            .unwrap();
        // After page1 the next token (page2 file) is checkpointed; after page2
        // the terminal None is checkpointed.
        let checkpoints = cur.checkpoints.lock().unwrap().clone();
        assert_eq!(checkpoints, vec![Some("oai_page2.xml".to_string()), None]);
    }

    // (b) ...and a harvest resumes from a checkpoint rather than restarting.
    #[tokio::test]
    async fn harvest_resumes_from_checkpoint() {
        let cur: Arc<FakeCursors> = Arc::new(FakeCursors::default());
        // Simulate a crash that left us mid-set, checkpointed at page2.
        cur.seed_resume("arxiv-cs", "oai_page2.xml");
        let lim = Arc::new(HostLimiters::per_second(1000.0));
        let docs = source("oai_page1.xml")
            .fetch(&ctx(lim, cur.clone()))
            .await
            .unwrap();
        // Only page2's 2 records — page1 was NOT refetched.
        assert_eq!(docs.len(), 2);
        assert!(doc_ids(&docs)
            .iter()
            .all(|i| i.ends_with("2607.02201") || i.ends_with("2607.02377")));
    }

    // (c) an empty resumptionToken terminates cleanly (no infinite loop).
    #[tokio::test]
    async fn empty_token_terminates() {
        let cur: Arc<FakeCursors> = Arc::new(FakeCursors::default());
        let lim = Arc::new(HostLimiters::per_second(1000.0));
        // The committed single-page fixture ends with an empty token.
        let docs = source_at(repo_fixture("arxiv_oai_cs.xml"))
            .fetch(&ctx(lim, cur.clone()))
            .await
            .unwrap();
        assert_eq!(docs.len(), 6);
        // Terminal checkpoint is None, and completion cleared any resume token.
        assert_eq!(cur.checkpoints.lock().unwrap().clone(), vec![None]);
        assert_eq!(cur.resume_token("arxiv-cs"), None);
    }

    // (d) completing a harvest stores the max datestamp; the next request
    //     replays it as `from=`.
    #[tokio::test]
    async fn high_water_stored_and_replayed_as_from() {
        let cur: Arc<FakeCursors> = Arc::new(FakeCursors::default());
        let lim = Arc::new(HostLimiters::per_second(1000.0));
        source("oai_page1.xml")
            .fetch(&ctx(lim, cur.clone()))
            .await
            .unwrap();
        // Max datestamp across both pages is 2026-07-04.
        assert_eq!(cur.high_water("arxiv-cs").as_deref(), Some("2026-07-04"));

        // The subsequent request would carry from=<high-water>.
        let endpoint =
            "https://export.arxiv.org/oai2?verb=ListRecords&metadataPrefix=oai_dc&set=cs";
        let url = oai_request_url(endpoint, None, cur.high_water("arxiv-cs").as_deref());
        assert_eq!(url, format!("{endpoint}&from=2026-07-04"));
    }

    // resume requests carry ONLY verb + resumptionToken (spec), url-encoded.
    #[test]
    fn resume_url_is_spec_shaped() {
        let endpoint =
            "https://export.arxiv.org/oai2?verb=ListRecords&metadataPrefix=oai_dc&set=cs";
        let url = oai_request_url(endpoint, Some("cursor|123:cs"), None);
        assert_eq!(
            url,
            "https://export.arxiv.org/oai2?verb=ListRecords&resumptionToken=cursor%7C123%3Acs"
        );
    }

    // (e) the rate limiter is consulted once per page.
    #[tokio::test]
    async fn rate_limiter_consulted_between_pages() {
        let cur: Arc<FakeCursors> = Arc::new(FakeCursors::default());
        let lim = Arc::new(HostLimiters::per_second(1000.0));
        source("oai_page1.xml")
            .fetch(&ctx(lim.clone(), cur))
            .await
            .unwrap();
        // Two pages fetched => two gate acquisitions.
        assert_eq!(lim.acquires(), 2);
    }
}
