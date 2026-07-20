//! RSS 2.0 connector.
//!
//! Production notes: swap the parser for `feed-rs` (RSS 1/2, Atom, JSON Feed,
//! robust dates/encodings) and add conditional-GET cursors (send ETag /
//! Last-Modified from the previous run; a 304 means zero new work).

use crate::{child_text, gate, IngestError, Reach, Source, SourceContext};
use async_trait::async_trait;
use intel_compliance::MissingPolicy;
use intel_core::{Day, Document, License, Provenance, SectorId, SourceKind};

pub struct RssSource {
    pub id: String,
    pub sector: SectorId,
    pub feed_url: String,
    /// When set, the file's bytes stand in for the HTTP body (deterministic
    /// runs, offline tests). When None, requires the `net` feature.
    pub fixture_path: Option<String>,
    pub license: License,
    /// Per-source 404-robots.txt disposition (see `ArxivOaiSource`). Defaults to
    /// the conservative `Deny` for every RSS source unless config opts in.
    pub robots_on_missing: MissingPolicy,
}

impl RssSource {
    async fn fetch_text(&self, ctx: &SourceContext) -> Result<String, IngestError> {
        // Fixture-configured sources never touch the network, so they must not
        // trigger a robots.txt fetch either.
        let reach = if self.fixture_path.is_some() {
            Reach::Fixture
        } else {
            Reach::Network
        };
        gate(ctx, &self.feed_url, reach, self.robots_on_missing).await?;
        if let Some(p) = &self.fixture_path {
            return Ok(std::fs::read_to_string(p)?);
        }
        #[cfg(feature = "net")]
        {
            crate::net::get_text(&self.feed_url).await
        }
        #[cfg(not(feature = "net"))]
        {
            Err(IngestError::Http(
                "no fixture configured and binary built without the 'net' feature".into(),
            ))
        }
    }
}

#[async_trait]
impl Source for RssSource {
    fn id(&self) -> &str {
        &self.id
    }
    fn sector(&self) -> &SectorId {
        &self.sector
    }
    fn kind(&self) -> SourceKind {
        SourceKind::Rss
    }

    async fn fetch(&self, ctx: &SourceContext) -> Result<Vec<Document>, IngestError> {
        let xml = self.fetch_text(ctx).await?;
        let tree =
            roxmltree::Document::parse(&xml).map_err(|e| IngestError::Parse(e.to_string()))?;

        let mut out = Vec::new();
        for item in tree.descendants().filter(|n| n.tag_name().name() == "item") {
            let title = child_text(item, "title").unwrap_or_default();
            let guid = child_text(item, "guid").unwrap_or_else(|| title.clone());
            let raw_date = child_text(item, "pubDate");
            out.push(Document {
                id: format!("{}::{}", self.id, guid),
                sector: self.sector.clone(),
                url: child_text(item, "link"),
                title,
                body: child_text(item, "description").unwrap_or_default(),
                published_day: raw_date.as_deref().and_then(Day::parse_rfc822ish),
                published_raw: raw_date,
                authors: child_text(item, "author").into_iter().collect(),
                tags: Vec::new(),
                provenance: Provenance {
                    source_id: self.id.clone(),
                    retrieved_from: self.feed_url.clone(),
                    kind: SourceKind::Rss,
                    license: self.license,
                },
            });
        }
        Ok(out)
    }
}
