//! intel-registry: config-driven sectors and the source factory.
//!
//! Adding a sector or a source is a JSON edit; adding a source *type* is a
//! new `Source` impl plus one arm in `build_sources`. Core never changes.
//!
//! Core-shell note: SUBSCRIPTIONS LEFT THIS CRATE. Clients, API keys, tiers,
//! quotas, and billing are business logic and live in the shell
//! (`config/subscriptions.json` + `shell/intel_shell/auth.py`). The core
//! deliberately does not know that clients exist — every core endpoint takes
//! an explicit sector list, and the shell decides who gets which sectors.
//! That keeps the core's contract stable while the entitlement model
//! (billing webhooks, trials, tier upgrades) iterates freely outside.

use intel_core::{License, SectorId};
use intel_ingest::MissingPolicy;
use intel_ingest::arxiv_oai::ArxivOaiSource;
use intel_ingest::rss::RssSource;
use intel_ingest::Source;
use serde::Deserialize;
use std::collections::HashSet;

#[derive(Deserialize)]
pub struct CoreConfig {
    pub sectors: Vec<SectorCfg>,
}

#[derive(Deserialize)]
pub struct SectorCfg {
    pub id: String,
    pub display_name: String,
    pub sources: Vec<SourceCfg>,
}

#[derive(Deserialize)]
pub struct SourceCfg {
    #[serde(rename = "type")]
    pub source_type: String,
    pub id: String,
    pub url: String,
    /// Local file standing in for the network body (omit + build with
    /// `--features net` for live fetching).
    pub fixture: Option<String>,
    pub license: License,
    /// Optional per-source disposition when the publisher serves NO robots.txt
    /// (a 404). Absent or unrecognized ⇒ the conservative default (`"deny"`), so
    /// a typo fails closed. Set to `"allow"` for an operator-vetted cooperative
    /// endpoint that publishes no robots.txt on purpose — arXiv's OAI-PMH host
    /// being the canonical case. This never overrides an explicit `Disallow`,
    /// and never affects the unreachable (5xx/timeout) path.
    #[serde(default)]
    pub robots_on_missing: Option<String>,
    /// Optional cap on pages fetched per harvest (arxiv_oai only). Absent =
    /// unbounded (follow resumptionToken to exhaustion). Set this for a huge set
    /// like `set=cs` so one run is bounded; the cursor still checkpoints, so a
    /// later run resumes from the cap.
    #[serde(default)]
    pub max_pages: Option<u32>,
}

pub fn build_sources(sec: &SectorCfg) -> Vec<Box<dyn Source>> {
    let sid = SectorId::new(&sec.id);
    let mut out: Vec<Box<dyn Source>> = Vec::new();
    for s in &sec.sources {
        // Absent / unrecognized ⇒ Deny (fail closed on a typo).
        let on_missing = s
            .robots_on_missing
            .as_deref()
            .map(MissingPolicy::from_config_str)
            .unwrap_or_default();
        match s.source_type.as_str() {
            "rss" => out.push(Box::new(RssSource {
                id: s.id.clone(),
                sector: sid.clone(),
                feed_url: s.url.clone(),
                fixture_path: s.fixture.clone(),
                license: s.license,
                robots_on_missing: on_missing,
            })),
            "arxiv_oai" => out.push(Box::new(ArxivOaiSource {
                id: s.id.clone(),
                sector: sid.clone(),
                endpoint_url: s.url.clone(),
                fixture_path: s.fixture.clone(),
                license: s.license,
                robots_on_missing: on_missing,
                max_pages: s.max_pages,
            })),
            other => eprintln!(
                "registry: unknown source type '{other}' for source '{}' (skipped)",
                s.id
            ),
        }
    }
    out
}

/// A connector chosen to run, tagged with the sector it belongs to.
pub struct SelectedSource {
    pub sector_id: String,
    pub source: Box<dyn Source>,
}

/// The outcome of resolving an ingest request to concrete connectors.
pub struct SourceSelection {
    /// The connectors to run, in config order (sector order, then source
    /// order within each sector) — so a sector-only selection is byte-for-byte
    /// the pre-per-source behavior.
    pub selected: Vec<SelectedSource>,
    /// Requested source ids that matched no eligible connector — either
    /// unknown entirely, or belonging to a sector the caller isn't entitled
    /// to. Surfaced as data (never a panic) so the handler can report a
    /// structured per-id error.
    pub unknown_ids: Vec<String>,
}

/// Resolve which connectors an `/ingest` call should run.
///
/// `entitled_sectors` is the sector allow-list the shell computed for the
/// caller; only sources *inside* these sectors are ever eligible — this is the
/// defense-in-depth sector filter (a shell bug can mis-grant sectors, never
/// bypass this gate).
///
/// `only_sources`:
/// - `None` — run every source in the entitled sectors (the original
///   sector-granular behavior, unchanged).
/// - `Some(ids)` — run exactly the named source ids, each still validated
///   against `entitled_sectors`. Ids not matching an eligible source are
///   returned in `unknown_ids`.
pub fn select_sources(
    cfg: &CoreConfig,
    entitled_sectors: &HashSet<&str>,
    only_sources: Option<&HashSet<&str>>,
) -> SourceSelection {
    let mut selected = Vec::new();
    let mut matched: HashSet<String> = HashSet::new();

    for sec in &cfg.sectors {
        if !entitled_sectors.contains(sec.id.as_str()) {
            continue;
        }
        for source in build_sources(sec) {
            if let Some(only) = only_sources {
                if !only.contains(source.id()) {
                    continue;
                }
                matched.insert(source.id().to_string());
            }
            selected.push(SelectedSource {
                sector_id: sec.id.clone(),
                source,
            });
        }
    }

    let unknown_ids = match only_sources {
        Some(only) => only
            .iter()
            .filter(|id| !matched.contains(**id))
            .map(|id| id.to_string())
            .collect(),
        None => Vec::new(),
    };

    SourceSelection {
        selected,
        unknown_ids,
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    fn cfg() -> CoreConfig {
        // Two sectors; three sources. Fixtures are irrelevant here — selection
        // never fetches, it only inspects ids — so `fixture` is None.
        let src = |t: &str, id: &str| SourceCfg {
            source_type: t.into(),
            id: id.into(),
            url: "https://example.org/x".into(),
            fixture: None,
            license: License::CcBy,
            robots_on_missing: None,
            max_pages: None,
        };
        CoreConfig {
            sectors: vec![
                SectorCfg {
                    id: "technology".into(),
                    display_name: "Technology".into(),
                    sources: vec![src("rss", "techwire"), src("rss", "osdaily")],
                },
                SectorCfg {
                    id: "finance".into(),
                    display_name: "Finance".into(),
                    sources: vec![src("rss", "filings-digest")],
                },
            ],
        }
    }

    fn ids(sel: &SourceSelection) -> Vec<&str> {
        sel.selected.iter().map(|s| s.source.id()).collect()
    }

    #[test]
    fn sector_only_selects_every_source_in_entitled_sectors() {
        let c = cfg();
        let entitled: HashSet<&str> = ["technology"].into_iter().collect();
        let sel = select_sources(&c, &entitled, None);
        assert_eq!(ids(&sel), vec!["techwire", "osdaily"]); // config order preserved
        assert!(sel.unknown_ids.is_empty());
    }

    #[test]
    fn source_filter_selects_exactly_named_connectors() {
        let c = cfg();
        let entitled: HashSet<&str> = ["technology", "finance"].into_iter().collect();
        let only: HashSet<&str> = ["techwire", "filings-digest"].into_iter().collect();
        let sel = select_sources(&c, &entitled, Some(&only));
        let mut got = ids(&sel);
        got.sort();
        assert_eq!(got, vec!["filings-digest", "techwire"]);
        assert!(sel.unknown_ids.is_empty());
    }

    #[test]
    fn unknown_source_id_is_reported_not_panicked() {
        let c = cfg();
        let entitled: HashSet<&str> = ["technology"].into_iter().collect();
        let only: HashSet<&str> = ["techwire", "does-not-exist"].into_iter().collect();
        let sel = select_sources(&c, &entitled, Some(&only));
        assert_eq!(ids(&sel), vec!["techwire"]);
        assert_eq!(sel.unknown_ids, vec!["does-not-exist".to_string()]);
    }

    #[test]
    fn source_outside_entitled_sector_is_rejected() {
        let c = cfg();
        // Caller entitled to technology only; asks for a finance source.
        let entitled: HashSet<&str> = ["technology"].into_iter().collect();
        let only: HashSet<&str> = ["filings-digest"].into_iter().collect();
        let sel = select_sources(&c, &entitled, Some(&only));
        assert!(sel.selected.is_empty());
        assert_eq!(sel.unknown_ids, vec!["filings-digest".to_string()]);
    }
}
