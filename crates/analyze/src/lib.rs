//! intel-analyze: from mentions to signals. This crate is the moat.
//!
//! Three signal families, each answering a question an aggregator can't:
//!
//! - **RisingEntity** — "what changed today?" Per-entity daily document
//!   counts vs a trailing baseline; a z-score outlier is a burst. (Seed-grade
//!   z-score; production ladder: Kleinberg burst states, then per-entity
//!   Poisson/negative-binomial baselines with day-of-week seasonality.)
//!
//! - **Corroborated** — "is it real or one outlet's take?" An entity
//!   independently reported by k distinct sources is k-corroborated.
//!   De-duplication upstream is what makes this honest: syndicated copies
//!   must not count as independent confirmation.
//!
//! - **EmergingEntity** — "what don't we have a node for yet?" Recurring
//!   unknown surface forms, surfaced for gazetteer promotion.
//!
//! Plus the **association graph**: entity co-occurrence edges weighted by
//! count and PMI. Weight says "often together"; PMI says "together more than
//! their individual popularity predicts" — high-PMI low-weight edges are
//! where early, non-obvious relationships show up.
//!
//! Every signal carries evidence doc-ids. No claim without provenance.

use intel_core::{Day, Discovered, Document, Entity, Mention, Signal, SignalKind};
use std::collections::{BTreeMap, BTreeSet, HashMap, HashSet};

pub struct AnalyzeParams {
    pub z_threshold: f64,
    pub min_burst_docs: usize,
    pub min_corroborating_sources: usize,
}

impl Default for AnalyzeParams {
    fn default() -> Self {
        Self {
            z_threshold: 2.0,
            min_burst_docs: 2,
            min_corroborating_sources: 2,
        }
    }
}

pub struct Edge {
    pub a: String,
    pub b: String,
    pub weight: usize,
    pub pmi: f64,
}

pub struct Analysis {
    pub signals: Vec<Signal>,
    pub edges: Vec<Edge>,
    pub window_end: Option<Day>,
}

pub fn analyze(
    docs: &[Document],
    entities: &[Entity],
    mentions: &[Mention],
    discovered: &[Discovered],
    p: &AnalyzeParams,
) -> Analysis {
    let name_of: HashMap<&str, &str> = entities
        .iter()
        .map(|e| (e.id.as_str(), e.name.as_str()))
        .collect();
    let source_of: HashMap<&str, &str> = docs
        .iter()
        .map(|d| (d.id.as_str(), d.provenance.source_id.as_str()))
        .collect();

    let all_days: BTreeSet<Day> = docs.iter().filter_map(|d| d.published_day).collect();
    let window_end = all_days.iter().next_back().copied();
    let window_start = all_days.iter().next().copied();

    // --- per-entity indexes -------------------------------------------------
    let mut per_entity_day: HashMap<&str, BTreeMap<Day, BTreeSet<&str>>> = HashMap::new();
    let mut per_entity_sources: HashMap<&str, BTreeSet<&str>> = HashMap::new();
    let mut per_entity_docs: HashMap<&str, BTreeSet<&str>> = HashMap::new();
    let mut per_doc_entities: HashMap<&str, BTreeSet<&str>> = HashMap::new();

    for m in mentions {
        if let Some(day) = m.day {
            per_entity_day
                .entry(m.entity_id.as_str())
                .or_default()
                .entry(day)
                .or_default()
                .insert(m.doc_id.as_str());
        }
        per_entity_sources
            .entry(m.entity_id.as_str())
            .or_default()
            .insert(m.source_id.as_str());
        per_entity_docs
            .entry(m.entity_id.as_str())
            .or_default()
            .insert(m.doc_id.as_str());
        per_doc_entities
            .entry(m.doc_id.as_str())
            .or_default()
            .insert(m.entity_id.as_str());
    }

    let mut signals: Vec<Signal> = Vec::new();
    let mut burst_entities: HashSet<&str> = HashSet::new();

    // --- RisingEntity -------------------------------------------------------
    if let (Some(min_d), Some(max_d)) = (window_start, window_end) {
        for (eid, daymap) in &per_entity_day {
            let today: Vec<&str> = daymap
                .get(&max_d)
                .map(|s| s.iter().copied().collect())
                .unwrap_or_default();
            if today.len() < p.min_burst_docs {
                continue;
            }
            // Baseline: every ordinal day in [min, max), zero-filled.
            let mut base: Vec<f64> = Vec::new();
            let mut o = min_d.0;
            while o < max_d.0 {
                base.push(daymap.get(&Day(o)).map(|s| s.len()).unwrap_or(0) as f64);
                o += 1;
            }
            if base.is_empty() {
                continue; // single-day corpus: no baseline, no burst claims
            }
            let mean = base.iter().sum::<f64>() / base.len() as f64;
            let var = base.iter().map(|x| (x - mean).powi(2)).sum::<f64>() / base.len() as f64;
            let std = var.sqrt().max(0.5); // floor prevents div-by-~0 on quiet baselines
            let z = (today.len() as f64 - mean) / std;
            if z < p.z_threshold {
                continue;
            }

            burst_entities.insert(eid);
            let name = name_of.get(eid).copied().unwrap_or(eid);
            let mut srcs: BTreeSet<&str> = today
                .iter()
                .filter_map(|d| source_of.get(d).copied())
                .collect();
            let n_src = srcs.len();
            let src_list: Vec<&str> = srcs.iter().copied().collect();
            srcs.clear();

            let corroboration_note = if n_src >= p.min_corroborating_sources {
                format!(
                    "; independently corroborated by {n_src} sources: {}",
                    src_list.join(", ")
                )
            } else {
                format!("; single-source so far ({})", src_list.join(", "))
            };

            signals.push(Signal {
                kind: SignalKind::RisingEntity,
                headline: format!(
                    "{name}: {} documents on {max_d} vs baseline {mean:.1}/day",
                    today.len()
                ),
                score: z,
                entity_ids: vec![eid.to_string()],
                evidence: today.iter().map(|s| s.to_string()).collect(),
                detail: format!("burst z-score {z:.1}{corroboration_note}"),
            });
        }
    }

    // --- Corroborated (suppressed for entities already reported as rising) --
    for (eid, sources) in &per_entity_sources {
        if burst_entities.contains(eid) || sources.len() < p.min_corroborating_sources {
            continue;
        }
        let name = name_of.get(eid).copied().unwrap_or(eid);
        let docs_for: Vec<String> = per_entity_docs
            .get(eid)
            .map(|s| s.iter().map(|x| x.to_string()).collect())
            .unwrap_or_default();
        let src_list: Vec<&str> = sources.iter().copied().collect();
        signals.push(Signal {
            kind: SignalKind::Corroborated,
            headline: format!("{name} reported by {} independent sources", sources.len()),
            score: sources.len() as f64,
            entity_ids: vec![eid.to_string()],
            evidence: docs_for,
            detail: format!("sources: {}", src_list.join(", ")),
        });
    }

    // --- EmergingEntity ------------------------------------------------------
    for d in discovered {
        let srcs: BTreeSet<&str> = d
            .doc_ids
            .iter()
            .filter_map(|id| source_of.get(id.as_str()).copied())
            .collect();
        let src_list: Vec<&str> = srcs.iter().copied().collect();
        signals.push(Signal {
            kind: SignalKind::EmergingEntity,
            headline: format!(
                "unrecognized entity \"{}\" recurring in {} documents",
                d.surface,
                d.doc_ids.len()
            ),
            score: d.doc_ids.len() as f64,
            entity_ids: Vec::new(),
            evidence: d.doc_ids.clone(),
            detail: format!(
                "candidate for gazetteer promotion; seen in: {}",
                src_list.join(", ")
            ),
        });
    }

    signals.sort_by(|a, b| {
        b.score
            .partial_cmp(&a.score)
            .unwrap_or(std::cmp::Ordering::Equal)
            .then_with(|| a.headline.cmp(&b.headline))
    });

    // --- association graph ----------------------------------------------------
    let n_docs = docs.len().max(1);
    let entity_doc_count: HashMap<&str, usize> =
        per_entity_docs.iter().map(|(k, v)| (*k, v.len())).collect();

    let mut pair_weight: BTreeMap<(String, String), usize> = BTreeMap::new();
    for ents in per_doc_entities.values() {
        let v: Vec<&str> = ents.iter().copied().collect();
        for i in 0..v.len() {
            for j in (i + 1)..v.len() {
                *pair_weight
                    .entry((v[i].to_string(), v[j].to_string()))
                    .or_insert(0) += 1;
            }
        }
    }

    let mut edges: Vec<Edge> = pair_weight
        .into_iter()
        .map(|((a, b), weight)| {
            let ca = *entity_doc_count.get(a.as_str()).unwrap_or(&1) as f64;
            let cb = *entity_doc_count.get(b.as_str()).unwrap_or(&1) as f64;
            let pmi = ((weight as f64 * n_docs as f64) / (ca * cb)).ln();
            Edge { a, b, weight, pmi }
        })
        .collect();
    edges.sort_by(|x, y| {
        y.weight.cmp(&x.weight).then_with(|| {
            y.pmi
                .partial_cmp(&x.pmi)
                .unwrap_or(std::cmp::Ordering::Equal)
        })
    });

    Analysis {
        signals,
        edges,
        window_end,
    }
}
