//! intel-enrich: turning text into entities.
//!
//! Two mechanisms, deliberately layered:
//!
//! 1. **Gazetteer resolution** (deterministic, free, fast): an alias table
//!    maps surface forms to canonical entities. This is the backbone —
//!    entity RESOLUTION (many names -> one node) matters more than entity
//!    *recognition*, because signals are computed per canonical node.
//!
//! 2. **Discovery** (the growth loop): recurring capitalized surface forms
//!    that resolve to nothing become `Discovered` candidates. Reviewed and
//!    promoted into the gazetteer, they close the loop the gazetteer alone
//!    can't: catching things that didn't exist yesterday.
//!
//! Core-shell note: the OLD optional LLM enricher (llm.rs) moved to the
//! shell (`shell/intel_shell/enrichment.py`) — an LLM call is prompt +
//! provider business, exactly the kind of thing the shell iterates on
//! freely. This crate stays deterministic and dependency-light: it is the
//! hot loop that scans every document body on every view computation.

use intel_core::{Discovered, Document, Entity, Mention};
use serde::Deserialize;
use std::collections::{HashMap, HashSet};

#[derive(Deserialize)]
struct GazetteerFile {
    entities: Vec<Entity>,
}

pub struct Gazetteer {
    pub entities: Vec<Entity>,
}

impl Gazetteer {
    pub fn from_json(s: &str) -> Result<Self, serde_json::Error> {
        let f: GazetteerFile = serde_json::from_str(s)?;
        Ok(Self { entities: f.entities })
    }

    /// Resolves mentions per document (presence-based: one mention per
    /// (entity, doc), robust to in-article keyword repetition).
    pub fn extract(&self, docs: &[Document]) -> Vec<Mention> {
        let mut out = Vec::new();
        for d in docs {
            let hay = format!("{} {}", d.title, d.body).to_lowercase();
            for e in &self.entities {
                let hit = e
                    .aliases
                    .iter()
                    .chain(std::iter::once(&e.name))
                    .any(|n| contains_word(&hay, &n.to_lowercase()));
                if hit {
                    out.push(Mention {
                        entity_id: e.id.clone(),
                        doc_id: d.id.clone(),
                        day: d.published_day,
                        source_id: d.provenance.source_id.clone(),
                        sector: d.sector.clone(),
                    });
                }
            }
        }
        out
    }
}

/// Word-boundary substring search (both sides of a match must be
/// non-alphanumeric or string edges). Prevents "rust" matching "trust".
pub fn contains_word(hay: &str, needle: &str) -> bool {
    if needle.is_empty() {
        return false;
    }
    let hb = hay.as_bytes();
    let mut start = 0;
    while let Some(pos) = hay[start..].find(needle) {
        let i = start + pos;
        let j = i + needle.len();
        let pre_ok = i == 0 || !(hb[i - 1] as char).is_alphanumeric();
        let post_ok = j >= hb.len() || !(hb[j] as char).is_alphanumeric();
        if pre_ok && post_ok {
            return true;
        }
        start = j;
    }
    false
}

/// Finds recurring capitalized runs in document *bodies* (titles are Title
/// Case and would drown discovery in noise) that match no known alias.
///
/// Heuristics: each token must start uppercase AND contain a lowercase
/// letter (drops "V4", "GPU", "AI"); runs of 2-4 tokens; a leading stopword
/// is trimmed; the run must recur in `min_docs` distinct documents.
pub fn discover_candidates(
    docs: &[Document],
    gaz: &Gazetteer,
    min_docs: usize,
) -> Vec<Discovered> {
    let stop: HashSet<&str> = [
        "the", "a", "an", "in", "on", "at", "for", "and", "but", "it", "this", "that", "with",
        "from", "after", "before", "new", "its", "their",
    ]
    .into_iter()
    .collect();

    let known: Vec<String> = gaz
        .entities
        .iter()
        .flat_map(|e| e.aliases.iter().chain(std::iter::once(&e.name)))
        .map(|s| s.to_lowercase())
        .collect();

    let mut seen: HashMap<String, HashSet<String>> = HashMap::new();

    for d in docs {
        let mut runs: Vec<Vec<String>> = Vec::new();
        let mut cur: Vec<String> = Vec::new();
        for raw in d.body.split_whitespace() {
            let t = raw.trim_matches(|c: char| !c.is_alphanumeric());
            if qualifies(t) {
                cur.push(t.to_string());
            } else {
                if cur.len() >= 2 {
                    runs.push(cur.clone());
                }
                cur.clear();
            }
        }
        if cur.len() >= 2 {
            runs.push(cur);
        }

        for mut r in runs {
            while !r.is_empty() && stop.contains(r[0].to_lowercase().as_str()) {
                r.remove(0);
            }
            if r.len() < 2 || r.len() > 4 {
                continue;
            }
            let surface = r.join(" ");
            let lower = surface.to_lowercase();
            if known.iter().any(|k| lower.contains(k.as_str())) {
                continue;
            }
            seen.entry(surface).or_default().insert(d.id.clone());
        }
    }

    let mut out: Vec<Discovered> = seen
        .into_iter()
        .filter(|(_, ids)| ids.len() >= min_docs)
        .map(|(surface, ids)| {
            let mut doc_ids: Vec<String> = ids.into_iter().collect();
            doc_ids.sort();
            Discovered { surface, doc_ids }
        })
        .collect();
    out.sort_by(|a, b| b.doc_ids.len().cmp(&a.doc_ids.len()).then_with(|| a.surface.cmp(&b.surface)));
    out
}

fn qualifies(t: &str) -> bool {
    if t.len() < 2 {
        return false;
    }
    let mut chars = t.chars();
    match chars.next() {
        Some(c) if c.is_uppercase() => {}
        _ => return false,
    }
    t.chars().any(|c| c.is_lowercase())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn word_boundaries_hold() {
        assert!(contains_word("served through vllm.", "vllm"));
        assert!(!contains_word("a matter of trust.", "rust"));
        assert!(contains_word("uses llama.cpp today", "llama.cpp"));
    }

    #[test]
    fn qualifies_filters_acronyms_and_versions() {
        assert!(qualifies("Helios"));
        assert!(qualifies("Labs"));
        assert!(!qualifies("V4"));
        assert!(!qualifies("GPU"));
        assert!(!qualifies("a"));
    }
}
