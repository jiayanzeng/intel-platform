//! intel-store: the archive. Sources come and go; the archive accumulates.
//!
//! Seed-grade: append-only JSONL with id-based idempotency (re-running the
//! pipeline never duplicates documents; the corpus only grows with genuinely
//! new material — this is the "historical archive as moat" property in its
//! simplest possible form).
//!
//! Production swap, behind this same surface:
//! - Postgres via `sqlx` for documents, entities, mentions, signals;
//! - `pgvector` for embeddings (semantic retrieval / RAG over YOUR archive);
//! - `tantivy` for full-text search — pure Rust, embedded, no external
//!   service, which fits the no-gatekeeper constraint nicely.

pub mod sqlite;
pub use sqlite::{
    Cursor, EmbeddingStats, EmbeddingWriteError, SearchHit, SqliteStore, StoreOpenTimings,
    VectorSearchResult,
};

use intel_core::Document;
use std::collections::HashSet;
use std::fs::{self, OpenOptions};
use std::io::{BufRead, BufReader, Write};
use std::path::{Path, PathBuf};

pub struct JsonlStore {
    docs_path: PathBuf,
}

impl JsonlStore {
    pub fn open(dir: &Path) -> std::io::Result<Self> {
        fs::create_dir_all(dir)?;
        Ok(Self {
            docs_path: dir.join("docs.jsonl"),
        })
    }

    pub fn load(&self) -> std::io::Result<Vec<Document>> {
        if !self.docs_path.exists() {
            return Ok(Vec::new());
        }
        let f = fs::File::open(&self.docs_path)?;
        let mut out = Vec::new();
        for line in BufReader::new(f).lines() {
            let line = line?;
            if line.trim().is_empty() {
                continue;
            }
            match serde_json::from_str::<Document>(&line) {
                Ok(d) => out.push(d),
                Err(e) => eprintln!("store: skipping corrupt line: {e}"),
            }
        }
        Ok(out)
    }

    /// Appends only documents whose ids are not already present.
    /// Returns how many were actually new.
    pub fn append_new(&self, docs: &[Document]) -> std::io::Result<usize> {
        let existing: HashSet<String> = self.load()?.into_iter().map(|d| d.id).collect();
        let mut f = OpenOptions::new()
            .create(true)
            .append(true)
            .open(&self.docs_path)?;
        let mut n = 0;
        for d in docs {
            if existing.contains(&d.id) {
                continue;
            }
            let line = serde_json::to_string(d)
                .map_err(|e| std::io::Error::new(std::io::ErrorKind::InvalidData, e))?;
            writeln!(f, "{line}")?;
            n += 1;
        }
        Ok(n)
    }
}
