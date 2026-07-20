use intel_store::SqliteStore;
use rusqlite::Connection;
use std::collections::BTreeMap;
use std::path::{Path, PathBuf};

fn canonical_ids(path: &Path) -> rusqlite::Result<BTreeMap<String, Option<String>>> {
    let conn = Connection::open(path)?;
    let mut stmt = conn.prepare("SELECT id, canonical_id FROM documents ORDER BY id")?;
    let rows = stmt.query_map([], |row| Ok((row.get(0)?, row.get(1)?)))?;
    rows.collect()
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let mut args = std::env::args_os().skip(1);
    let path = PathBuf::from(
        args.next()
            .ok_or("usage: verify_fingerprints <database> [canonical-reference-database]")?,
    );
    let reference = args.next().map(PathBuf::from);
    if args.next().is_some() {
        return Err("too many arguments".into());
    }

    let store = SqliteStore::open(&path)?;
    let documents = store.load_all()?;
    let stored = store.fingerprints()?;
    let mut mismatches = Vec::new();
    for document in &documents {
        let fresh = intel_extract::simhash(&format!("{} {}", document.title, document.body));
        if stored.get(&document.id).copied() != Some(fresh) {
            mismatches.push(document.id.clone());
        }
    }

    println!("database={}", path.display());
    println!("documents={}", documents.len());
    println!("stored_fingerprints={}", stored.len());
    println!("fingerprint_mismatches={}", mismatches.len());
    for id in mismatches.iter().take(10) {
        println!("mismatch={id}");
    }

    let mut canonical_mismatches = 0usize;
    if let Some(reference) = reference {
        let actual = canonical_ids(&path)?;
        let expected = canonical_ids(&reference)?;
        canonical_mismatches = actual
            .iter()
            .filter(|(id, canonical)| expected.get(*id) != Some(*canonical))
            .count()
            + expected
                .keys()
                .filter(|id| !actual.contains_key(*id))
                .count();
        println!("canonical_reference={}", reference.display());
        println!("canonical_mismatches={canonical_mismatches}");
    }

    if documents.len() != stored.len() || !mismatches.is_empty() || canonical_mismatches != 0 {
        return Err("fingerprint verification failed".into());
    }
    Ok(())
}
