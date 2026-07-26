#!/usr/bin/env python3
"""Executable audit for the seven deferred-design triggers."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import re
import shutil
import socket
import sqlite3
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from typing import Any, Callable


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "config" / "protected-artifacts.json"
SCHEDULE = ROOT / "config" / "schedule.json"
SCHEDULER = ROOT / "shell" / "intel_shell" / "scheduler.py"
CORE_CONFIG = ROOT / "shell" / "intel_shell" / "config.py"
CORE_MAIN = ROOT / "apps" / "cored" / "src" / "main.rs"
PUBLIC_APP = ROOT / "shell" / "intel_shell" / "app.py"
STORE = ROOT / "crates" / "store" / "src" / "sqlite.rs"
SUBSCRIPTIONS = ROOT / "shell" / "intel_shell" / "config.py"
SERVICE = ROOT / "deploy" / "intel-pipeline.service"
TIMER = ROOT / "deploy" / "intel-pipeline.timer"
DEPLOY_README = ROOT / "deploy" / "README.md"
SCALE_NOTE = ROOT / "docs" / "T8-scale-design-note.md"
VIEW_SUMMARY = ROOT / "evidence" / "v0.9" / "view-benchmark" / "summary.json"
V2_VIEW_SUMMARY = (
    ROOT / "evidence" / "v0.10" / "view-decomposition" / "summary.json"
)
V2_VIEW_DESIGN = ROOT / "docs" / "V2-VIEW-DESIGN.md"
RETRIEVE_ANCHOR_MS = 16.264
EMBEDDING_DIMENSION = 768
COSINE_SAMPLES = 30
SCHEMA_VERSION = 2
EXPECTED_RUNNER_JOB_COUNTS = {
    "core": 1,
    "golden": 1,
    "lint": 1,
    "msrv": 1,
    "net": 1,
    "shell": 2,
}
EXPECTED_RUNNER_WORKFLOW = "CI"
SOURCE_DETERMINISTIC_ROW_IDS = (
    "T7 robots single-flight",
    "Postgres",
    "Multi-host seam hardening",
    "A4 untrusted-shell attestation boundary",
    "CI-runner evidence",
)
SCHEDULER_RUNTIME_FIELDS = (
    "active_scheduler_processes",
    "scheduler_processes",
    "active_cored_processes",
    "cored_processes",
    "loopback_8788_accepting",
)


def configure_subject_root(root: Path) -> None:
    """Point every subject-side measurement at one explicit worktree."""
    global ROOT, MANIFEST, SCHEDULE, SCHEDULER, CORE_CONFIG, CORE_MAIN
    global PUBLIC_APP, STORE, SUBSCRIPTIONS, SERVICE, TIMER, DEPLOY_README
    global SCALE_NOTE, VIEW_SUMMARY, V2_VIEW_SUMMARY, V2_VIEW_DESIGN

    ROOT = root.resolve()
    MANIFEST = ROOT / "config" / "protected-artifacts.json"
    SCHEDULE = ROOT / "config" / "schedule.json"
    SCHEDULER = ROOT / "shell" / "intel_shell" / "scheduler.py"
    CORE_CONFIG = ROOT / "shell" / "intel_shell" / "config.py"
    CORE_MAIN = ROOT / "apps" / "cored" / "src" / "main.rs"
    PUBLIC_APP = ROOT / "shell" / "intel_shell" / "app.py"
    STORE = ROOT / "crates" / "store" / "src" / "sqlite.rs"
    SUBSCRIPTIONS = ROOT / "shell" / "intel_shell" / "config.py"
    SERVICE = ROOT / "deploy" / "intel-pipeline.service"
    TIMER = ROOT / "deploy" / "intel-pipeline.timer"
    DEPLOY_README = ROOT / "deploy" / "README.md"
    SCALE_NOTE = ROOT / "docs" / "T8-scale-design-note.md"
    VIEW_SUMMARY = (
        ROOT / "evidence" / "v0.9" / "view-benchmark" / "summary.json"
    )
    V2_VIEW_SUMMARY = (
        ROOT / "evidence" / "v0.10" / "view-decomposition" / "summary.json"
    )
    V2_VIEW_DESIGN = ROOT / "docs" / "V2-VIEW-DESIGN.md"


def progress_paths(root: Path | None = None) -> list[Path]:
    """Return every progress record; the active cycle must never be omitted."""
    selected = ROOT if root is None else root
    return sorted(selected.resolve().glob("PROGRESS-v*.md"))


class AuditFailure(RuntimeError):
    """The audit could not establish a required measurement."""


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def require_text(path: Path, literals: list[str]) -> str:
    text = path.read_text()
    for literal in literals:
        if literal not in text:
            raise AuditFailure(f"{path}: required evidence missing: {literal!r}")
    return text


def line_of(path: Path, literal: str) -> int:
    for number, line in enumerate(path.read_text().splitlines(), 1):
        if literal in line:
            return number
    raise AuditFailure(f"{path}: required call site missing: {literal!r}")


def source_ref(path: Path, literal: str) -> str:
    return f"{path.relative_to(ROOT)}:{line_of(path, literal)}"


def git_subject() -> dict[str, Any]:
    head = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=True,
    ).stdout.strip()
    status = subprocess.run(
        ["git", "status", "--porcelain=v1"],
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=True,
    ).stdout.splitlines()
    return {
        "head_commit": head,
        "worktree_dirty": bool(status),
        "worktree_status": status,
        "measured_source_sha256": {
            "tools/audit_deferred.py": sha256(Path(__file__).resolve()),
            "crates/store/examples/cosine_bench.rs": sha256(
                ROOT / "crates" / "store" / "examples" / "cosine_bench.rs"
            ),
            "shell/intel_shell/scheduler.py": sha256(SCHEDULER),
            "crates/store/src/sqlite.rs": sha256(STORE),
            "deploy/intel-pipeline.service": sha256(SERVICE),
            "deploy/intel-pipeline.timer": sha256(TIMER),
            "docs/T8-scale-design-note.md": sha256(SCALE_NOTE),
            "evidence/v0.9/view-benchmark/summary.json": sha256(VIEW_SUMMARY),
            "evidence/v0.10/view-decomposition/summary.json": sha256(
                V2_VIEW_SUMMARY
            ),
            "docs/V2-VIEW-DESIGN.md": sha256(V2_VIEW_DESIGN),
            "shell/intel_shell/app.py": sha256(PUBLIC_APP),
        },
    }


def require_production_subject(expected_head: str) -> str:
    """Require the exact clean Git subject before any measurement executes."""
    expected = expected_head.strip().lower()
    if re.fullmatch(r"[0-9a-f]{40,64}", expected) is None:
        raise AuditFailure(
            "expected HEAD must be a 40-64 character hexadecimal object id"
        )
    actual = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=True,
    ).stdout.strip().lower()
    if actual != expected:
        raise AuditFailure(
            f"subject HEAD mismatch: expected {expected}, actual {actual}"
        )
    status = subprocess.run(
        ["git", "status", "--porcelain=v1"],
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=True,
    ).stdout.splitlines()
    if status:
        raise AuditFailure(
            "subject worktree is dirty: " + "; ".join(status)
        )
    return actual


def expanded_schedule_jobs() -> int:
    raw = json.loads(SCHEDULE.read_text())
    jobs = raw.get("jobs")
    if not isinstance(jobs, list):
        raise AuditFailure(f"{SCHEDULE}: jobs must be a list")
    expanded = 0
    for job in jobs:
        if not isinstance(job, dict):
            raise AuditFailure(f"{SCHEDULE}: every job must be an object")
        sources = job.get("sources", {})
        sectors = job.get("sectors", {})
        if not isinstance(sources, dict) or not isinstance(sectors, dict):
            raise AuditFailure(f"{SCHEDULE}: sources/sectors must be objects")
        expanded += len(sources) + len(sectors)
        expanded += 1
    return expanded


def process_topology() -> dict[str, Any]:
    result = subprocess.run(
        ["ps", "-axo", "pid=,ppid=,command="],
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        raise AuditFailure(f"ps failed: {result.stderr.strip()}")
    scheduler_pattern = re.compile(r"\b-m\s+intel_shell\.scheduler\b")
    cored_pattern = re.compile(r"(?:^|/)(?:target/(?:debug|release)/)?cored(?:\s|$)")
    schedulers = [
        line.strip()
        for line in result.stdout.splitlines()
        if scheduler_pattern.search(line)
    ]
    cored = [
        line.strip()
        for line in result.stdout.splitlines()
        if cored_pattern.search(line)
    ]
    listener = False
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as probe:
        probe.settimeout(0.1)
        listener = probe.connect_ex(("127.0.0.1", 8788)) == 0
    return {
        "active_scheduler_processes": len(schedulers),
        "scheduler_processes": schedulers,
        "active_cored_processes": len(cored),
        "cored_processes": cored,
        "loopback_8788_accepting": listener,
    }


def scheduler_measurement(
    topology: dict[str, Any] | None = None,
) -> dict[str, Any]:
    require_text(
        SCHEDULER,
        [
            "for job in due_jobs(self.jobs, now):",
            "job.action()",
            "scheduler.run_once()",
            "scheduler.run_forever(tick_seconds=args.tick)",
        ],
    )
    require_text(
        SERVICE,
        [
            "Type=oneshot",
            "CORE_URL=http://127.0.0.1:8788",
            "intel_shell.scheduler --once",
        ],
    )
    require_text(TIMER, ["OnUnitActiveSec=15min"])
    require_text(
        DEPLOY_README,
        [
            "Pick one of two ways to drive it.",
            "## Option A — systemd timer (recommended)",
            "## Option B — in-process loop",
        ],
    )
    if topology is None:
        topology = process_topology()
    missing_topology = [
        field for field in SCHEDULER_RUNTIME_FIELDS if field not in topology
    ]
    if missing_topology:
        raise AuditFailure(
            "scheduler topology is missing fields: "
            + ", ".join(missing_topology)
        )
    return {
        "configured_jobs": len(json.loads(SCHEDULE.read_text())["jobs"]),
        "expanded_jobs": expanded_schedule_jobs(),
        "execution_within_one_scheduler": "serial for-loop",
        "documented_deployment_modes": [
            "one Type=oneshot scheduler owned by one systemd timer",
            "one long-lived in-process scheduler loop",
        ],
        "documented_modes_are_alternatives": True,
        "supported_simultaneous_harvest_callers": 1,
        "source_evidence": [
            source_ref(SCHEDULER, "for job in due_jobs(self.jobs, now):"),
            source_ref(SCHEDULER, "job.action()"),
            source_ref(SERVICE, "Type=oneshot"),
            source_ref(SERVICE, "intel_shell.scheduler --once"),
            source_ref(TIMER, "OnUnitActiveSec=15min"),
            source_ref(DEPLOY_README, "Pick one of two ways to drive it."),
        ],
        **topology,
    }


def writer_measurement() -> dict[str, Any]:
    require_text(
        STORE,
        [
            "pub fn append_new(",
            "pub fn record_signals(",
            "pub fn update_document(",
            "pub fn delete_document(",
            "pub fn assign_canonical_ids(",
            "pub fn commit_harvest_page(",
            "pub fn upsert_embeddings(",
        ],
    )
    require_text(
        CORE_MAIN,
        [
            "SqliteStore::open_with_timings(",
            ".commit_harvest_page(",
            ".append_new(",
            ".assign_canonical_ids(",
            ".upsert_embeddings(",
            ".record_signals(",
        ],
    )
    shell_core_db_hits = [
        str(path.relative_to(ROOT))
        for path in (ROOT / "shell" / "intel_shell").glob("*.py")
        if "CORE_DB" in path.read_text()
    ]
    if shell_core_db_hits:
        raise AuditFailure(
            "shell directly names CORE_DB: " + ", ".join(shell_core_db_hits)
        )
    production_core = CORE_MAIN.read_text().split(
        "\n#[cfg(test)]\nmod tests", 1
    )[0]
    if production_core.count("SqliteStore::open_with_timings(") != 1:
        raise AuditFailure(
            "production cored must construct exactly one SqliteStore"
        )
    for method in (".update_document(", ".delete_document("):
        if method in production_core:
            raise AuditFailure(
                f"maintenance method unexpectedly gained a product caller: {method}"
            )
    require_text(
        SUBSCRIPTIONS,
        [
            "class SqliteSubscriptionStore",
            'conn.execute("DELETE FROM subscriptions")',
            '"INSERT INTO subscriptions "',
        ],
    )
    return {
        "supported_archive_writer_processes": 1,
        "archive_writer": "single cored process; one Mutex<rusqlite::Connection>",
        "shell_direct_archive_writers": 0,
        "archive_write_inventory": [
            {
                "owner": "cored startup",
                "path": "SqliteStore::open_with_timings",
                "writes": "schema/FTS triggers, cursor migration, missing-fingerprint backfill",
                "source": source_ref(
                    CORE_MAIN,
                    "SqliteStore::open_with_timings(",
                ),
            },
            {
                "owner": "cored /ingest",
                "path": "append_new + assign_canonical_ids",
                "writes": "documents/FTS and corpus-derived canonical_id",
                "sources": [
                    source_ref(CORE_MAIN, ".append_new("),
                    source_ref(CORE_MAIN, ".assign_canonical_ids("),
                ],
            },
            {
                "owner": "cored paged /ingest",
                "path": "commit_harvest_page",
                "writes": "documents/FTS, canonical_id, and cursor in one transaction",
                "source": source_ref(CORE_MAIN, ".commit_harvest_page("),
            },
            {
                "owner": "cored /embeddings",
                "path": "upsert_embeddings",
                "writes": "embeddings",
                "source": source_ref(CORE_MAIN, ".upsert_embeddings("),
            },
            {
                "owner": "cored /signals/record",
                "path": "record_signals",
                "writes": "signals_history",
                "source": source_ref(CORE_MAIN, ".record_signals("),
            },
            {
                "owner": "store maintenance/test surface; no product caller",
                "path": "update_document + delete_document",
                "writes": "documents/FTS and embeddings",
                "sources": [
                    source_ref(STORE, "pub fn update_document("),
                    source_ref(STORE, "pub fn delete_document("),
                ],
            },
        ],
        "separate_shell_configuration_writers": [
            {
                "owner": "public billing handlers",
                "path": "SqliteSubscriptionStore.save",
                "database": "SUBSCRIPTIONS_PATH, never CORE_DB",
                "source": source_ref(
                    ROOT / "shell" / "intel_shell" / "app.py", "store.save()"
                ),
            },
            {
                "owner": "admin key CLI",
                "path": "SqliteSubscriptionStore.save",
                "database": "SUBSCRIPTIONS_PATH, never CORE_DB",
                "source": source_ref(ROOT / "tools" / "admin_keys.py", "store.save()"),
            },
            {
                "owner": "one-shot subscription migration",
                "path": "SqliteSubscriptionStore.save",
                "database": "destination subscription DB, never CORE_DB",
                "source": source_ref(
                    ROOT / "tools" / "migrate_subscriptions.py", "dest.save()"
                ),
            },
        ],
    }


def multi_host_measurement() -> dict[str, Any]:
    require_text(
        CORE_MAIN,
        ['unwrap_or_else(|_| "127.0.0.1:8788".into())'],
    )
    require_text(
        CORE_CONFIG,
        ['CORE_URL = os.environ.get("CORE_URL", "http://127.0.0.1:8788")'],
    )
    require_text(SERVICE, ["CORE_URL=http://127.0.0.1:8788"])
    progress = progress_paths()
    remote_core_url_hits: list[str] = []
    for path in (*progress, SERVICE, CORE_CONFIG):
        for number, line in enumerate(path.read_text().splitlines(), 1):
            if re.search(r"CORE_URL=https?://(?!127\.0\.0\.1|localhost)", line):
                remote_core_url_hits.append(
                    f"{path.relative_to(ROOT)}:{number}:{line.strip()}"
                )
    return {
        "cored_default_bind": "127.0.0.1:8788",
        "shell_default_core_url": "http://127.0.0.1:8788",
        "deployment_core_url": "http://127.0.0.1:8788",
        "deployment_core_and_shell_host": "same host",
        "recorded_remote_core_url_hits": remote_core_url_hits,
        "recorded_cross_host_core_shell_requests": len(remote_core_url_hits),
        "progress_files_scanned": [
            str(path.relative_to(ROOT)) for path in progress
        ],
        "source_evidence": [
            source_ref(
                CORE_MAIN, 'unwrap_or_else(|_| "127.0.0.1:8788".into())'
            ),
            source_ref(
                CORE_CONFIG,
                'CORE_URL = os.environ.get("CORE_URL", "http://127.0.0.1:8788")',
            ),
            source_ref(SERVICE, "CORE_URL=http://127.0.0.1:8788"),
        ],
    }


def load_manifest_records() -> list[dict[str, Any]]:
    manifest = json.loads(MANIFEST.read_text())
    records = manifest.get("artifacts")
    if not isinstance(records, list):
        raise AuditFailure(f"{MANIFEST}: artifacts must be a list")
    selected = sorted(records, key=lambda item: item["expected"]["documents"])
    counts = [item["expected"]["documents"] for item in selected]
    if counts != [1764, 2600]:
        raise AuditFailure(f"expected archive counts [1764, 2600], got {counts}")
    return selected


def read_only_embedding_count(path: Path) -> int:
    with sqlite3.connect(f"file:{path}?mode=ro", uri=True) as connection:
        return int(
            connection.execute("SELECT COUNT(*) FROM embeddings").fetchone()[0]
        )


def exact_cosine_measurement() -> dict[str, Any]:
    records = load_manifest_records()
    reports: list[dict[str, Any]] = []
    with tempfile.TemporaryDirectory(prefix="intel-d4-cosine-") as temp:
        temp_dir = Path(temp)
        for record in records:
            source = ROOT / record["path"]
            actual = sha256(source)
            if actual != record["sha256"]:
                raise AuditFailure(
                    f"{record['path']}: protected hash {actual} != "
                    f"{record['sha256']}"
                )
            copy_path = temp_dir / (
                f"archive-{record['expected']['documents']}.db"
            )
            shutil.copyfile(source, copy_path)
            if sha256(copy_path) != actual:
                raise AuditFailure(f"{copy_path}: byte copy does not match")
            original_embeddings = read_only_embedding_count(source)
            result = subprocess.run(
                [
                    "cargo",
                    "run",
                    "--quiet",
                    "--release",
                    "-p",
                    "intel-store",
                    "--example",
                    "cosine_bench",
                    "--",
                    str(copy_path),
                    str(EMBEDDING_DIMENSION),
                    str(COSINE_SAMPLES),
                    "science",
                ],
                cwd=ROOT,
                text=True,
                capture_output=True,
                check=False,
            )
            if result.returncode != 0:
                raise AuditFailure(
                    "exact-cosine benchmark failed: "
                    + (result.stderr.strip() or result.stdout.strip())
                )
            try:
                report = json.loads(result.stdout.strip().splitlines()[-1])
            except (IndexError, json.JSONDecodeError) as error:
                raise AuditFailure(
                    f"invalid exact-cosine report: {result.stdout!r}"
                ) from error
            if report.get("documents") != record["expected"]["documents"]:
                raise AuditFailure("exact-cosine report has wrong corpus count")
            report["database"] = f"disposable copy of {record['path']}"
            report["protected_archive"] = {
                "path": record["path"],
                "sha256": record["sha256"],
                "bytes": record["bytes"],
                "original_embedding_rows": original_embeddings,
                "copy_seeded_embedding_rows": record["expected"]["documents"],
            }
            reports.append(report)
    for record in records:
        if sha256(ROOT / record["path"]) != record["sha256"]:
            raise AuditFailure(
                f"{record['path']}: protected bytes changed during audit"
            )
    small, large = reports
    delta_documents = large["documents"] - small["documents"]
    delta_p95 = large["p95_ms"] - small["p95_ms"]
    return {
        "engine": "intel_store::SqliteStore::vector_search",
        "algorithm": "brute-force exact cosine over deterministic 768d vectors",
        "archive_reports": reports,
        "largest_evidenced_corpus": large["documents"],
        "largest_p95_ms": large["p95_ms"],
        "a3_retrieve_anchor_ms": RETRIEVE_ANCHOR_MS,
        "largest_p95_below_a3_anchor": large["p95_ms"]
        < RETRIEVE_ANCHOR_MS,
        "two_point_p95_ms_per_1000_documents": delta_p95
        * 1000
        / delta_documents,
        "scale_note_order_of_magnitude": "10^5–10^6 documents",
        "comparison_note": (
            "A3's 16.264 ms full-request observation is an anchor, not a "
            "retrieval SLO; the current exact-cosine component remains below "
            "even that measured request cost."
        ),
    }


def attestation_boundary_measurement() -> dict[str, Any]:
    text = require_text(
        PUBLIC_APP,
        [
            '@app.get("/v1/ask")',
            "core.attest,",
            'answer = attestation["clean_answer"]',
        ],
    )
    lines = text.splitlines()
    ask_start = next(
        index
        for index, line in enumerate(lines)
        if '@app.get("/v1/ask")' in line
    )
    ask_end = next(
        index
        for index, line in enumerate(lines[ask_start + 1 :], ask_start + 1)
        if '@app.post("/v1/billing/webhook")' in line
    )
    ask_lines = lines[ask_start:ask_end]
    shell_egress = [
        f"{PUBLIC_APP.relative_to(ROOT)}:{ask_start + offset + 1}"
        for offset, line in enumerate(ask_lines)
        if line.strip() == "return {"
    ]
    if len(shell_egress) != 1:
        raise AuditFailure(
            f"{PUBLIC_APP}: expected one /v1/ask public egress, "
            f"observed {shell_egress}"
        )
    if sum("core.attest," in line for line in ask_lines) != 1:
        raise AuditFailure(
            f"{PUBLIC_APP}: /v1/ask must call core.attest exactly once"
        )

    authority_files = [ROOT / name for name in (
        "AGENTS.md",
        "ARCHITECTURE.md",
        "README.md",
        "STATE.md",
    )]
    invariant_claims: list[str] = []
    pattern = re.compile(
        r"(?<!not )HC1 is invariant under shell replacement",
        re.IGNORECASE,
    )
    for path in authority_files:
        for number, line in enumerate(path.read_text().splitlines(), 1):
            match = pattern.search(line)
            if match is None:
                continue
            prefix = line[: match.start()].lower()
            if prefix.rstrip().endswith("or any claim that"):
                # D5's registry must quote the unchanged trigger. A quoted
                # condition is not itself an affirmative architecture claim.
                continue
            if match:
                invariant_claims.append(
                    f"{path.relative_to(ROOT)}:{number}:{line.strip()}"
                )
    return {
        "public_answer_paths": 1,
        "public_answer_paths_without_core_owned_response_boundary": 1,
        "shell_owned_public_egress_points": len(shell_egress),
        "shell_owned_public_egress_sources": shell_egress,
        "core_attest_inspection_calls": 1,
        "core_owned_public_response_boundaries": 0,
        "shipped_shell_trust": "repository-owned and operator-controlled",
        "third_party_or_untrusted_shells": 0,
        "hc1_invariant_under_shell_replacement_claims": invariant_claims,
        "risk": (
            "the shipped shell calls /attest, but public egress remains "
            "shell-owned and HC1 is not invariant under shell replacement"
        ),
    }


def _display_receipt_path(
    path: Path,
    repository: Path,
    logical_receipt_root: Path | None,
) -> str:
    if logical_receipt_root is not None:
        try:
            relative = path.resolve().relative_to(logical_receipt_root.resolve())
            return str(Path("evidence") / "ci-runs" / relative)
        except ValueError:
            pass
    try:
        return str(path.resolve().relative_to(repository.resolve()))
    except ValueError:
        return str(path.resolve())


def verify_attestation_bundle(
    receipt: Path,
    bundle: Path,
    repository: str,
    signer_workflow: str,
) -> None:
    """Verify one persisted GitHub provenance bundle against its receipt."""
    gh = shutil.which("gh")
    if gh is None:
        raise AuditFailure(
            "authenticated receipt verification requires the GitHub CLI"
        )
    verified = subprocess.run(
        [
            gh,
            "attestation",
            "verify",
            str(receipt),
            "--bundle",
            str(bundle),
            "--repo",
            repository,
            "--signer-workflow",
            signer_workflow,
            "--deny-self-hosted-runners",
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if verified.returncode != 0:
        detail = verified.stderr.strip() or verified.stdout.strip()
        raise AuditFailure(
            "GitHub attestation verification failed"
            + (f": {detail}" if detail else "")
        )


def runner_receipt_measurement(
    receipts: list[Path],
    *,
    repository: Path,
    audited_head: str,
    released_commit: str,
    logical_receipt_root: Path | None = None,
    attestation_bundles_dir: Path | None = None,
    require_attestations: bool = False,
    expected_repository: str | None = None,
    expected_workflow: str | None = None,
    attestation_verifier: Callable[[Path, Path, str, str], None] | None = None,
) -> dict[str, Any]:
    """Accept only one complete successful matrix for the released commit."""
    candidates: list[dict[str, Any]] = []
    rejected: list[dict[str, Any]] = []
    matrix_findings: list[str] = []
    released_commit = released_commit.lower()
    if re.fullmatch(r"[0-9a-f]{40,64}", released_commit) is None:
        raise AuditFailure(
            "released commit must be a 40-64 character hexadecimal object id"
        )
    if require_attestations and (
        attestation_bundles_dir is None
        or not expected_repository
        or not expected_workflow
    ):
        raise AuditFailure(
            "authenticated receipt verification requires bundle directory, "
            "expected repository, and expected workflow"
        )
    verifier = attestation_verifier or verify_attestation_bundle
    required = (
        "run_id",
        "run_attempt",
        "job",
        "sha",
        "conclusion",
        "runner_os",
        "completed_at",
    )
    for path in receipts:
        shown = _display_receipt_path(
            path,
            repository,
            logical_receipt_root,
        )
        try:
            receipt = json.loads(path.read_text())
        except (OSError, json.JSONDecodeError) as error:
            rejected.append(
                {
                    "path": shown,
                    "sha": None,
                    "reason": f"receipt is not readable JSON: {error}",
                }
            )
            continue
        if not isinstance(receipt, dict):
            rejected.append(
                {
                    "path": shown,
                    "sha": None,
                    "reason": "receipt root is not an object",
                }
            )
            continue
        missing = [
            field
            for field in required
            if not isinstance(receipt.get(field), (str, int))
            or str(receipt[field]).strip() == ""
        ]
        sha = str(receipt.get("sha", "")).lower()
        if missing:
            rejected.append(
                {
                    "path": shown,
                    "sha": sha or None,
                    "reason": "missing/invalid fields: " + ", ".join(missing),
                }
            )
            continue
        if re.fullmatch(r"[0-9a-f]{40,64}", sha) is None:
            rejected.append(
                {
                    "path": shown,
                    "sha": sha,
                    "reason": "sha is not a 40-64 character hexadecimal object id",
                }
            )
            continue
        ancestry = subprocess.run(
            ["git", "merge-base", "--is-ancestor", sha, audited_head],
            cwd=repository,
            text=True,
            capture_output=True,
            check=False,
        )
        if ancestry.returncode != 0:
            reason = (
                f"sha is not an ancestor of audited head {audited_head}"
                if ancestry.returncode == 1
                else (
                    "git ancestry check failed: "
                    + (ancestry.stderr.strip() or f"exit {ancestry.returncode}")
                )
            )
            rejected.append({"path": shown, "sha": sha, "reason": reason})
            continue
        if sha != released_commit:
            rejected.append(
                {
                    "path": shown,
                    "sha": sha,
                    "reason": (
                        f"sha does not equal released commit {released_commit}"
                    ),
                }
            )
            continue
        conclusion = str(receipt["conclusion"])
        if conclusion.lower() != "success":
            rejected.append(
                {
                    "path": shown,
                    "sha": sha,
                    "reason": f"conclusion is not success: {conclusion}",
                }
            )
            continue
        accepted = {
            "path": shown,
            **{field: receipt[field] for field in required},
        }
        if require_attestations:
            assert attestation_bundles_dir is not None
            assert expected_repository is not None
            assert expected_workflow is not None
            if receipt.get("repository") != expected_repository:
                rejected.append(
                    {
                        "path": shown,
                        "sha": sha,
                        "reason": (
                            "receipt repository does not match expected "
                            f"{expected_repository}"
                        ),
                    }
                )
                continue
            if receipt.get("workflow") != EXPECTED_RUNNER_WORKFLOW:
                rejected.append(
                    {
                        "path": shown,
                        "sha": sha,
                        "reason": (
                            "receipt workflow does not match expected "
                            f"{EXPECTED_RUNNER_WORKFLOW}"
                        ),
                    }
                )
                continue
            bundle = (
                attestation_bundles_dir.resolve()
                / f"{path.name}.sigstore"
            )
            if not bundle.is_file():
                rejected.append(
                    {
                        "path": shown,
                        "sha": sha,
                        "reason": (
                            "required attestation bundle is missing: "
                            f"{bundle.name}"
                        ),
                    }
                )
                continue
            try:
                verifier(
                    path.resolve(),
                    bundle,
                    expected_repository,
                    expected_workflow,
                )
            except AuditFailure as error:
                rejected.append(
                    {
                        "path": shown,
                        "sha": sha,
                        "reason": str(error),
                    }
                )
                continue
            accepted["attestation_bundle"] = bundle.name
            accepted["attestation_verified"] = True
        candidates.append(accepted)

    run_keys = {
        (str(receipt["run_id"]), str(receipt["run_attempt"]))
        for receipt in candidates
    }
    if candidates and len(run_keys) != 1:
        matrix_findings.append(
            "structurally valid receipts do not share a single "
            "run_id/run_attempt"
        )
    actual_counts = {
        job: sum(str(receipt["job"]) == job for receipt in candidates)
        for job in EXPECTED_RUNNER_JOB_COUNTS
    }
    unknown_jobs = sorted(
        {
            str(receipt["job"])
            for receipt in candidates
            if str(receipt["job"]) not in EXPECTED_RUNNER_JOB_COUNTS
        }
    )
    if candidates and (
        actual_counts != EXPECTED_RUNNER_JOB_COUNTS or unknown_jobs
    ):
        matrix_findings.append(
            "runner receipt job counts do not match expected matrix: "
            f"expected={EXPECTED_RUNNER_JOB_COUNTS}, "
            f"actual={actual_counts}, unknown={unknown_jobs}"
        )
    if not candidates and receipts:
        matrix_findings.append("no valid receipts remain for matrix validation")
    matrix_complete = bool(candidates) and not matrix_findings
    accepted = candidates if matrix_complete else []
    return {
        "audited_head_commit": audited_head,
        "released_commit": released_commit,
        "expected_job_counts": EXPECTED_RUNNER_JOB_COUNTS,
        "runner_receipts": [
            _display_receipt_path(path, repository, logical_receipt_root)
            for path in receipts
        ],
        "accepted_runner_receipts": accepted,
        "rejected_runner_receipts": rejected,
        "matrix_findings": matrix_findings,
        "single_run_matrix_complete": matrix_complete,
        "attestations_required": require_attestations,
        "observed_runner_executions": len(accepted),
        "workflow_configuration_counts_as_execution": False,
    }


def ci_runner_measurement(
    released_commit: str,
    runner_receipts_dir: Path | None = None,
    *,
    attestation_bundles_dir: Path | None = None,
    require_attestations: bool = False,
    expected_repository: str | None = None,
    expected_workflow: str | None = None,
) -> dict[str, Any]:
    remote = subprocess.run(
        ["git", "remote", "-v"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=True,
    )
    remote_entries = [
        line for line in remote.stdout.splitlines() if line.strip()
    ]
    receipts = sorted((ROOT / "evidence" / "ci-runs").glob("*.json"))
    if runner_receipts_dir is not None:
        receipts = sorted(runner_receipts_dir.resolve().glob("*.json"))
    head = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=True,
    ).stdout.strip()
    current_runner = os.environ.get("GITHUB_ACTIONS", "").lower() == "true"
    return {
        "git_remote_entries": remote_entries,
        "git_remote_entry_count": len(remote_entries),
        "current_process_is_github_actions": current_runner,
        "configured_workflows": [
            str(path.relative_to(ROOT))
            for path in sorted((ROOT / ".github" / "workflows").glob("*.yml"))
        ],
        **runner_receipt_measurement(
            receipts,
            repository=ROOT,
            audited_head=head,
            released_commit=released_commit,
            logical_receipt_root=runner_receipts_dir,
            attestation_bundles_dir=attestation_bundles_dir,
            require_attestations=require_attestations,
            expected_repository=expected_repository,
            expected_workflow=expected_workflow,
        ),
    }


def view_measurement() -> dict[str, Any]:
    summary = json.loads(VIEW_SUMMARY.read_text())
    decomposition = json.loads(V2_VIEW_SUMMARY.read_text())
    reports = summary.get("reports")
    gate = summary.get("gate")
    if not isinstance(reports, list) or len(reports) != 4:
        raise AuditFailure(f"{VIEW_SUMMARY}: expected four reports")
    if not isinstance(gate, dict):
        raise AuditFailure(f"{VIEW_SUMMARY}: missing gate")
    decomposed_reports = decomposition.get("reports")
    if not isinstance(decomposed_reports, list) or len(decomposed_reports) != 4:
        raise AuditFailure(f"{V2_VIEW_SUMMARY}: expected four reports")
    require_text(
        V2_VIEW_DESIGN,
        [
            "Status: design only",
            "Future implementation acceptance",
            "cold p95 ≤ **162.640 ms**",
        ],
    )
    return {
        "slo": summary["slo"],
        "reports": reports,
        "cross_corpus_slopes": summary["cross_corpus_slopes"],
        "gate": gate,
        "v2_decomposition_reports": decomposed_reports,
        "v2_design": str(V2_VIEW_DESIGN.relative_to(ROOT)),
        "v2_materialization_implemented": False,
        "promoted_task": "future /view materialization implementation",
    }


def evaluate(measurements: dict[str, Any]) -> list[dict[str, Any]]:
    scheduler = measurements["scheduler"]
    writers = measurements["writers"]
    cosine = measurements["pgvector"]
    multi_host = measurements["multi_host"]
    attestation = measurements["attestation_boundary"]
    ci_runner = measurements["ci_runner"]
    view = measurements["view"]
    rows = [
        {
            "id": "T7 robots single-flight",
            "unchanged_trigger": "a second concurrent harvester",
            "measurement": (
                f"{scheduler['supported_simultaneous_harvest_callers']} "
                "supported simultaneous harvest caller(s); "
                f"{scheduler['active_scheduler_processes']} active scheduler "
                "process(es)"
            ),
            "disposition": (
                "promote"
                if scheduler["supported_simultaneous_harvest_callers"] >= 2
                else "defer"
            ),
        },
        {
            "id": "Postgres",
            "unchanged_trigger": "a second archive writer",
            "measurement": (
                f"{writers['supported_archive_writer_processes']} supported "
                "archive writer process(es); shell direct archive writers="
                f"{writers['shell_direct_archive_writers']}"
            ),
            "disposition": (
                "promote"
                if writers["supported_archive_writer_processes"] >= 2
                else "defer"
            ),
        },
        {
            "id": "pgvector",
            "unchanged_trigger": (
                "exact cosine over the archive stops fitting the measured "
                "request budget"
            ),
            "measurement": (
                f"largest evidenced corpus={cosine['largest_evidenced_corpus']}; "
                f"exact-cosine p95={cosine['largest_p95_ms']:.6f} ms; "
                f"A3 request anchor={cosine['a3_retrieve_anchor_ms']:.3f} ms"
            ),
            "disposition": (
                "defer"
                if cosine["largest_p95_below_a3_anchor"]
                else "promote"
            ),
        },
        {
            "id": "Multi-host seam hardening",
            "unchanged_trigger": "an actual core/shell host split",
            "measurement": (
                "recorded cross-host core/shell requests="
                f"{multi_host['recorded_cross_host_core_shell_requests']}; "
                f"bind={multi_host['cored_default_bind']}; "
                f"CORE_URL={multi_host['deployment_core_url']}"
            ),
            "disposition": (
                "promote"
                if multi_host["recorded_cross_host_core_shell_requests"] > 0
                else "defer"
            ),
        },
        {
            "id": "A4 untrusted-shell attestation boundary",
            "unchanged_trigger": (
                "a third-party or untrusted shell, or any claim that HC1 is "
                "invariant under shell replacement"
            ),
            "measurement": (
                "public answer paths without a core-owned response boundary="
                f"{attestation['public_answer_paths_without_core_owned_response_boundary']}; "
                "shell-owned public egress points="
                f"{attestation['shell_owned_public_egress_points']}; "
                "third-party/untrusted shells="
                f"{attestation['third_party_or_untrusted_shells']}; "
                "invariance claims="
                f"{len(attestation['hc1_invariant_under_shell_replacement_claims'])}"
            ),
            "disposition": (
                "promote"
                if attestation["third_party_or_untrusted_shells"] > 0
                or attestation[
                    "hc1_invariant_under_shell_replacement_claims"
                ]
                else "defer"
            ),
        },
        {
            "id": "CI-runner evidence",
            "unchanged_trigger": (
                "a runner execution receipt exists for the released commit"
            ),
            "measurement": (
                "complete release-matrix runner receipts="
                f"{ci_runner['observed_runner_executions']}; rejected receipts="
                f"{len(ci_runner.get('rejected_runner_receipts', []))}; "
                "workflow config is not an execution"
            ),
            "disposition": (
                "promote"
                if ci_runner["observed_runner_executions"] > 0
                else "defer"
            ),
        },
        {
            "id": "/view materialization",
            "unchanged_trigger": (
                "cold or warm p95 crosses the predeclared V1 SLO in both runs"
            ),
            "measurement": (
                f"V1 gate={view['gate']['overall']}; V2 reports="
                f"{len(view['v2_decomposition_reports'])}; "
                "V2 materialization implemented="
                f"{view['v2_materialization_implemented']}; "
                f"promoted task={view['promoted_task']}"
            ),
            "disposition": (
                "promote"
                if view["gate"]["overall"] == "materialization-trigger-fired"
                else "defer"
            ),
        },
    ]
    for row in rows:
        row["future_task"] = (
            "future /view materialization implementation"
            if row["id"] == "/view materialization"
            and row["disposition"] == "promote"
            else None
        )
    return rows


def production_measurements(
    runner_receipts_dir: Path | None = None,
    *,
    released_commit: str,
    attestation_bundles_dir: Path | None = None,
    require_attestations: bool = False,
    expected_repository: str | None = None,
    expected_workflow: str | None = None,
) -> dict[str, Any]:
    return {
        "scheduler": scheduler_measurement(),
        "writers": writer_measurement(),
        "pgvector": exact_cosine_measurement(),
        "multi_host": multi_host_measurement(),
        "attestation_boundary": attestation_boundary_measurement(),
        "ci_runner": ci_runner_measurement(
            released_commit,
            runner_receipts_dir,
            attestation_bundles_dir=attestation_bundles_dir,
            require_attestations=require_attestations,
            expected_repository=expected_repository,
            expected_workflow=expected_workflow,
        ),
        "view": view_measurement(),
    }


def committed_rederivation_snapshot(report: dict[str, Any]) -> dict[str, Any]:
    try:
        rows = report["triggers"]
        measurements = report["measurements"]
        view = measurements["view"]
    except (KeyError, TypeError) as error:
        raise AuditFailure(
            "committed receipt is missing measurements/triggers"
        ) from error
    if not isinstance(rows, list):
        raise AuditFailure("committed receipt triggers must be an array")
    by_id = {
        row.get("id"): row
        for row in rows
        if isinstance(row, dict) and isinstance(row.get("id"), str)
    }
    if len(by_id) != len(rows):
        raise AuditFailure("committed receipt has duplicate or invalid row ids")
    missing = sorted(set(SOURCE_DETERMINISTIC_ROW_IDS) - set(by_id))
    if missing:
        raise AuditFailure(
            "committed receipt is missing source-deterministic rows: "
            + ", ".join(missing)
        )
    try:
        return {
            "row_count": len(rows),
            "source_dispositions": {
                row_id: by_id[row_id]["disposition"]
                for row_id in SOURCE_DETERMINISTIC_ROW_IDS
            },
            "trigger_texts": {
                row_id: by_id[row_id]["unchanged_trigger"]
                for row_id in sorted(by_id)
            },
            "v2_materialization_implemented": view[
                "v2_materialization_implemented"
            ],
        }
    except (KeyError, TypeError) as error:
        raise AuditFailure(
            "committed receipt is missing a re-derived field"
        ) from error


def measurements_rederivation_snapshot(
    measurements: dict[str, Any],
) -> dict[str, Any]:
    rows = evaluate(measurements)
    by_id = {row["id"]: row for row in rows}
    return {
        "row_count": len(rows),
        "source_dispositions": {
            row_id: by_id[row_id]["disposition"]
            for row_id in SOURCE_DETERMINISTIC_ROW_IDS
        },
        "trigger_texts": {
            row_id: by_id[row_id]["unchanged_trigger"]
            for row_id in sorted(by_id)
        },
        "v2_materialization_implemented": measurements["view"][
            "v2_materialization_implemented"
        ],
    }


def source_deterministic_measurements(
    report: dict[str, Any],
    runner_receipts_dir: Path | None = None,
) -> dict[str, Any]:
    """Recompute only rows whose inputs are source, config, and Git."""
    try:
        committed = report["measurements"]
        scheduler_runtime = {
            field: committed["scheduler"][field]
            for field in SCHEDULER_RUNTIME_FIELDS
        }
        view = dict(committed["view"])
        measurements = {
            "scheduler": scheduler_measurement(scheduler_runtime),
            "writers": writer_measurement(),
            "pgvector": committed["pgvector"],
            "multi_host": multi_host_measurement(),
            "attestation_boundary": attestation_boundary_measurement(),
            "ci_runner": ci_runner_measurement(
                report["subject"]["head_commit"],
                runner_receipts_dir,
            ),
            "view": view,
        }
    except (KeyError, TypeError) as error:
        raise AuditFailure(
            "committed receipt is missing a measurement needed for "
            "source-deterministic re-derivation"
        ) from error
    measurements["view"]["v2_materialization_implemented"] = (
        view_measurement()["v2_materialization_implemented"]
    )
    return measurements


def rederivation_mismatches(
    expected: dict[str, Any],
    actual: dict[str, Any],
) -> list[str]:
    mismatches: list[str] = []
    for field in (
        "row_count",
        "source_dispositions",
        "trigger_texts",
        "v2_materialization_implemented",
    ):
        if expected[field] != actual[field]:
            mismatches.append(
                f"{field}: expected={json.dumps(expected[field], sort_keys=True)} "
                f"actual={json.dumps(actual[field], sort_keys=True)}"
            )
    return mismatches


def run_rederivation(
    receipt: Path,
    *,
    runner_receipts_dir: Path | None = None,
) -> int:
    try:
        report = json.loads(receipt.read_text())
    except (OSError, json.JSONDecodeError) as error:
        raise AuditFailure(f"{receipt}: {error}") from error
    if not isinstance(report, dict):
        raise AuditFailure(f"{receipt}: receipt root must be an object")
    expected = committed_rederivation_snapshot(report)
    actual = measurements_rederivation_snapshot(
        source_deterministic_measurements(report, runner_receipts_dir)
    )
    mismatches = rederivation_mismatches(expected, actual)
    if mismatches:
        for mismatch in mismatches:
            print(f"REDERIVATION MISMATCH {mismatch}", file=sys.stderr)
        return 1
    print(
        "deferred-evidence re-derivation: PASS "
        f"(rows={actual['row_count']}, "
        f"source_dispositions={len(actual['source_dispositions'])}, "
        f"triggers={len(actual['trigger_texts'])}, "
        "v2_materialization_implemented="
        f"{str(actual['v2_materialization_implemented']).lower()})"
    )
    return 0


def control_measurements() -> dict[str, Any]:
    return {
        "scheduler": {
            "supported_simultaneous_harvest_callers": 2,
            "active_scheduler_processes": 2,
        },
        "writers": {
            "supported_archive_writer_processes": 2,
            "shell_direct_archive_writers": 1,
        },
        "pgvector": {
            "largest_evidenced_corpus": 2600,
            "largest_p95_ms": 20.0,
            "a3_retrieve_anchor_ms": RETRIEVE_ANCHOR_MS,
            "largest_p95_below_a3_anchor": False,
        },
        "multi_host": {
            "recorded_cross_host_core_shell_requests": 1,
            "cored_default_bind": "127.0.0.1:8788",
            "deployment_core_url": "http://core.example:8788",
        },
        "attestation_boundary": {
            "public_answer_paths_without_core_owned_response_boundary": 1,
            "shell_owned_public_egress_points": 1,
            "third_party_or_untrusted_shells": 1,
            "hc1_invariant_under_shell_replacement_claims": [],
        },
        "ci_runner": {
            "git_remote_entry_count": 1,
            "observed_runner_executions": 1,
        },
        "view": {
            "gate": {"overall": "materialization-trigger-fired"},
            "v2_decomposition_reports": [{}, {}, {}, {}],
            "v2_materialization_implemented": False,
            "promoted_task": "future /view materialization implementation",
        },
    }


def print_rows(rows: list[dict[str, Any]]) -> None:
    for row in rows:
        print(
            f"{row['disposition'].upper():7} {row['id']}: "
            f"trigger={row['unchanged_trigger']}; {row['measurement']}"
        )


def run_control() -> int:
    rows = evaluate(control_measurements())
    print_rows(rows)
    fired = {
        row["id"]
        for row in rows
        if row["disposition"] == "promote"
    }
    required = {
        "T7 robots single-flight",
        "Postgres",
        "pgvector",
        "Multi-host seam hardening",
        "A4 untrusted-shell attestation boundary",
        "CI-runner evidence",
        "/view materialization",
    }
    if fired != required:
        raise AuditFailure(
            "synthetic input did not fire all seven triggers; "
            f"fired={sorted(fired)}"
        )
    print(
        "CONTROL FIRED: all seven deferred triggers were promoted by "
        "synthetic measurements"
    )
    return 1


def run_production(
    output: Path,
    *,
    expected_head: str,
    runner_receipts_dir: Path | None = None,
    attestation_bundles_dir: Path | None = None,
    require_attestations: bool = False,
    expected_repository: str | None = None,
    expected_workflow: str | None = None,
) -> int:
    if output.exists():
        raise AuditFailure(f"refusing to overwrite existing evidence: {output}")
    released_commit = require_production_subject(expected_head)
    measurements = production_measurements(
        runner_receipts_dir,
        released_commit=released_commit,
        attestation_bundles_dir=attestation_bundles_dir,
        require_attestations=require_attestations,
        expected_repository=expected_repository,
        expected_workflow=expected_workflow,
    )
    rows = evaluate(measurements)
    report = {
        "schema_version": SCHEMA_VERSION,
        "task": "v0.10.1 RECEIPT",
        "measured_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "subject": git_subject(),
        "host": {
            "platform": platform.platform(),
            "machine": platform.machine(),
            "logical_cpu_count": os.cpu_count(),
            "python": platform.python_version(),
        },
        "measurements": measurements,
        "triggers": rows,
        "summary": {
            "deferred": sum(
                row["disposition"] == "defer" for row in rows
            ),
            "promoted": sum(
                row["disposition"] == "promote" for row in rows
            ),
            "implemented_deferred_subsystems": 0,
        },
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(
        "progress files scanned: "
        + ", ".join(measurements["multi_host"]["progress_files_scanned"])
    )
    print_rows(rows)
    print(
        "AUDIT COMPLETE: "
        f"{report['summary']['deferred']} deferred, "
        f"{report['summary']['promoted']} promoted, "
        "0 deferred subsystems implemented"
    )
    print(f"evidence: {output}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Audit all seven deferred v0.10 design triggers"
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--output", type=Path)
    group.add_argument(
        "--control",
        choices=("all-seven",),
    )
    group.add_argument(
        "--rederive",
        type=Path,
        help=(
            "recompute corpus-free source/config/Git fields and compare them "
            "with a committed deferred-audit receipt"
        ),
    )
    parser.add_argument(
        "--subject-root",
        type=Path,
        help=(
            "explicit clean worktree whose commit, source, config, and "
            "protected artifacts are measured"
        ),
    )
    parser.add_argument(
        "--runner-receipts-dir",
        type=Path,
        help=(
            "explicit directory containing downloaded runner-produced "
            "receipt JSON"
        ),
    )
    parser.add_argument(
        "--expected-head",
        help=(
            "exact clean subject commit required before a production audit; "
            "also required in every accepted runner receipt"
        ),
    )
    parser.add_argument(
        "--attestation-bundles-dir",
        type=Path,
        help="directory containing <receipt-name>.sigstore bundles",
    )
    parser.add_argument(
        "--require-attestations",
        action="store_true",
        help="require and verify one GitHub provenance bundle per receipt",
    )
    parser.add_argument(
        "--expected-repository",
        help="GitHub owner/repository identity required in authenticated mode",
    )
    parser.add_argument(
        "--expected-workflow",
        help="GitHub signer workflow identity required in authenticated mode",
    )
    args = parser.parse_args()
    if args.control:
        if (
            args.subject_root
            or args.runner_receipts_dir
            or args.expected_head
            or args.attestation_bundles_dir
            or args.require_attestations
            or args.expected_repository
            or args.expected_workflow
        ):
            raise AuditFailure(
                "subject/receipt overrides apply only to production audits"
            )
        return run_control()
    receipt = args.rederive.resolve() if args.rederive is not None else None
    if args.subject_root is not None:
        configure_subject_root(args.subject_root)
    runner_receipts_dir = (
        args.runner_receipts_dir.resolve()
        if args.runner_receipts_dir is not None
        else None
    )
    attestation_bundles_dir = (
        args.attestation_bundles_dir.resolve()
        if args.attestation_bundles_dir is not None
        else None
    )
    if args.require_attestations and (
        attestation_bundles_dir is None
        or not args.expected_repository
        or not args.expected_workflow
    ):
        raise AuditFailure(
            "--require-attestations also requires "
            "--attestation-bundles-dir, --expected-repository, and "
            "--expected-workflow"
        )
    if receipt is not None:
        if (
            args.expected_head
            or attestation_bundles_dir is not None
            or args.require_attestations
            or args.expected_repository
            or args.expected_workflow
        ):
            raise AuditFailure(
                "authentication/release arguments apply only to production "
                "audits"
            )
        return run_rederivation(
            receipt,
            runner_receipts_dir=runner_receipts_dir,
        )
    if not args.expected_head:
        raise AuditFailure(
            "--expected-head is required for production audits"
        )
    return run_production(
        args.output.resolve(),
        expected_head=args.expected_head,
        runner_receipts_dir=runner_receipts_dir,
        attestation_bundles_dir=attestation_bundles_dir,
        require_attestations=args.require_attestations,
        expected_repository=args.expected_repository,
        expected_workflow=args.expected_workflow,
    )


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AuditFailure as error:
        print(f"audit-deferred: FAIL: {error}", file=sys.stderr)
        raise SystemExit(2)
