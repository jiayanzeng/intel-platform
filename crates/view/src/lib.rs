//! intel-view: the shared "corpus -> intelligence view" pass.
//!
//! This is the single place where a raw entitled corpus becomes deduplicated
//! documents, resolved mentions, discovery candidates, and signals. Every
//! consumer of the core (the /view endpoint, and through it every shell
//! surface — briefs, /v1/signals, dashboards) goes through this one
//! function, so no two renderings of the intelligence can drift apart.
//!
//! Core-shell note: this crate is the old `intel-brief` minus `render.rs`.
//! RENDERING LEFT THE CORE — markdown copy, section ordering, and product
//! voice are shell business (`shell/intel_shell/briefing.py`). What stays
//! here is the computation, because it is the hot path (near-duplicate scans
//! over persisted SimHashes, alias scans over every body) and because its
//! outputs are product invariants (dedup-before-statistics, evidence-linking).
//!
//! At seed scale this recomputes per call (instant on hundreds of docs).
//! At product scale: materialize per-sector views on an ingestion schedule
//! and serve from the store; the function signature stays the same.

use intel_analyze::{analyze, Analysis, AnalyzeParams};
use intel_core::{Discovered, Document, Entity, Mention};
use intel_enrich::{discover_candidates, Gazetteer};
use intel_extract::{dedup_near, DedupResult};

pub struct View {
    pub dd: DedupResult,
    pub mentions: Vec<Mention>,
    pub discovered: Vec<Discovered>,
    pub analysis: Analysis,
}

pub struct ViewParams {
    /// Near-dup hamming threshold. Calibrated for title+abstract texts and
    /// guarded in intel-extract so both documents must first meet the measured
    /// minimum feature count.
    pub dedup_max_distance: u32,
    pub discovery_min_docs: usize,
    pub analyze: AnalyzeParams,
}

impl Default for ViewParams {
    fn default() -> Self {
        Self {
            dedup_max_distance: 16,
            discovery_min_docs: 2,
            analyze: AnalyzeParams::default(),
        }
    }
}

pub fn compute_view(corpus: Vec<(Document, u64)>, gaz: &Gazetteer, p: &ViewParams) -> View {
    let dd = dedup_near(corpus, p.dedup_max_distance);
    let mentions = gaz.extract(&dd.kept);
    let discovered = discover_candidates(&dd.kept, gaz, p.discovery_min_docs);
    let analysis = analyze(&dd.kept, &gaz.entities, &mentions, &discovered, &p.analyze);
    View {
        dd,
        mentions,
        discovered,
        analysis,
    }
}

/// Convenience: name lookup used by serializers.
pub fn entity_names(entities: &[Entity]) -> std::collections::HashMap<&str, &str> {
    entities
        .iter()
        .map(|e| (e.id.as_str(), e.name.as_str()))
        .collect()
}
