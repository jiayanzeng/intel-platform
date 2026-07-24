use intel_core::{Document, License, Provenance, SectorId, SourceKind};
use intel_store::SqliteStore;
use std::path::PathBuf;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let mut args = std::env::args_os().skip(1);
    let path = PathBuf::from(
        args.next()
            .ok_or("usage: fingerprint_fixture <new-database>")?,
    );
    if args.next().is_some() {
        return Err("too many arguments".into());
    }
    if path.exists() {
        return Err(format!("fixture database already exists: {}", path.display()).into());
    }

    let store = SqliteStore::open(&path)?;
    let inserted = store.append_new(&[Document {
        id: "golden::fingerprint-control".into(),
        sector: SectorId::new("technology"),
        url: None,
        title: "Persisted fingerprint verifier control".into(),
        body: "A deterministic body makes the verifier fixture failure-capable.".into(),
        published_day: None,
        published_raw: None,
        authors: vec!["intel-platform".into()],
        tags: vec!["control".into()],
        provenance: Provenance {
            source_id: "golden-fixture".into(),
            retrieved_from: "fixture".into(),
            kind: SourceKind::Rss,
            license: License::CcBy,
        },
    }])?;
    if inserted != 1 {
        return Err(format!("expected one fixture document, inserted {inserted}").into());
    }
    println!("fingerprint_fixture={}", path.display());
    println!("documents=1");
    Ok(())
}
