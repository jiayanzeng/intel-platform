//! intel-retrieve: hybrid retrieval with reciprocal-rank fusion.
//!
//! Two legs, fused:
//! - **BM25** (SQLite FTS5): exact-term precision — finds "sparse attention"
//!   when you say "sparse attention";
//! - **vector cosine** (embeddings): recall on paraphrase — finds it when
//!   you say "efficient long-context transformer techniques".
//!
//! RRF (score = sum over lists of 1/(k + rank)) fuses the legs without any
//! score calibration between them, which is exactly why it is the standard
//! first choice for hybrid retrieval. k=60 is the conventional constant.
//!
//! Core-shell note: the embedding CALL left this crate. Embedding a query is
//! an LLM-provider interaction — prompt/provider business that belongs to
//! the shell. The core accepts an optional precomputed `(model, vector)`
//! pair and does the math: BM25, cosine, RRF. Degradation stays graceful
//! and *explicit*: no vector supplied -> the vector leg is empty, fusion
//! reduces to BM25 ranking, and a note in the diagnostics says so.

use intel_store::SqliteStore;
use std::collections::HashMap;

pub struct Retrieval {
    /// doc ids by BM25 rank (best first)
    pub bm25: Vec<String>,
    /// doc ids by cosine rank (best first)
    pub vector: Vec<String>,
    /// fused (doc id, rrf score), best first
    pub fused: Vec<(String, f64)>,
    /// honest operational notes (e.g. "vector leg disabled")
    pub notes: Vec<String>,
}

/// Reciprocal-rank fusion over ranked id lists.
pub fn rrf(lists: &[&[String]], k: f64) -> Vec<(String, f64)> {
    let mut scores: HashMap<&str, f64> = HashMap::new();
    for list in lists {
        for (rank, id) in list.iter().enumerate() {
            *scores.entry(id.as_str()).or_insert(0.0) += 1.0 / (k + rank as f64 + 1.0);
        }
    }
    let mut out: Vec<(String, f64)> = scores
        .into_iter()
        .map(|(id, s)| (id.to_string(), s))
        .collect();
    out.sort_by(|a, b| {
        b.1.partial_cmp(&a.1)
            .unwrap_or(std::cmp::Ordering::Equal)
            .then_with(|| a.0.cmp(&b.0))
    });
    out
}

/// Hybrid retrieval over the given sectors. `query_vector` is an optional
/// `(model, embedding)` pair the SHELL computed by calling its LLM provider;
/// the core never talks to a model.
pub fn hybrid(
    store: &SqliteStore,
    query: &str,
    sectors: &[String],
    top_k: usize,
    query_vector: Option<(&str, &[f32])>,
) -> Result<Retrieval, String> {
    let mut notes = Vec::new();

    // BM25 leg. Natural-language questions are converted to an OR query:
    // FTS5 ANDs terms by default, so "what is happening with X" would demand
    // the literal word "happening" in every hit and return nothing. OR-ing
    // quoted tokens restores recall; BM25's IDF then downweights the filler
    // words naturally. (/search keeps raw FTS5 syntax for power users.)
    let fts_query = natural_to_fts_or(query);
    let bm25: Vec<String> = match store.search(&fts_query, sectors, top_k) {
        Ok(hits) => hits.into_iter().map(|h| h.doc_id).collect(),
        Err(_) => {
            notes.push("bm25 leg skipped: query is not valid FTS5 syntax".into());
            Vec::new()
        }
    };

    // Vector leg — only if the shell supplied a query embedding.
    let vector: Vec<String> = match query_vector {
        Some((model, qv)) if !qv.is_empty() => store
            .vector_search(model, qv, sectors, top_k)
            .map_err(|e| e.to_string())?
            .into_iter()
            .map(|(id, _)| id)
            .collect(),
        Some(_) => {
            notes.push("vector leg skipped: empty query vector supplied".into());
            Vec::new()
        }
        None => {
            notes.push(
                "vector leg disabled: no query embedding supplied (shell has no embed client)"
                    .into(),
            );
            Vec::new()
        }
    };

    let mut fused = rrf(&[bm25.as_slice(), vector.as_slice()], 60.0);
    fused.truncate(top_k);

    Ok(Retrieval {
        bm25,
        vector,
        fused,
        notes,
    })
}

/// "what is happening with sparse attention" -> "\"what\" OR \"is\" OR ..."
pub fn natural_to_fts_or(q: &str) -> String {
    let tokens: Vec<String> = q
        .split(|c: char| !c.is_alphanumeric())
        .filter(|t| !t.is_empty())
        .map(|t| format!("\"{}\"", t.to_lowercase()))
        .collect();
    if tokens.is_empty() {
        q.to_string()
    } else {
        tokens.join(" OR ")
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn rrf_rewards_agreement() {
        let a = vec!["x".to_string(), "y".to_string(), "z".to_string()];
        let b = vec!["y".to_string(), "x".to_string(), "w".to_string()];
        let fused = rrf(&[a.as_slice(), b.as_slice()], 60.0);
        // x and y appear in both lists; they must outrank z and w.
        let top2: Vec<&str> = fused.iter().take(2).map(|(id, _)| id.as_str()).collect();
        assert!(top2.contains(&"x") && top2.contains(&"y"), "{fused:?}");
    }

    #[test]
    fn natural_query_becomes_or_of_quoted_tokens() {
        assert_eq!(
            natural_to_fts_or("sparse attention?"),
            "\"sparse\" OR \"attention\""
        );
    }

    #[test]
    fn rrf_single_list_preserves_order() {
        let a = vec!["p".to_string(), "q".to_string()];
        let fused = rrf(&[a.as_slice(), &[]], 60.0);
        assert_eq!(fused[0].0, "p");
        assert_eq!(fused[1].0, "q");
    }
}
