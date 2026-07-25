#!/usr/bin/env python3
"""Executable audit for the five deferred-design triggers."""

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
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "config" / "protected-artifacts.json"
SCHEDULE = ROOT / "config" / "schedule.json"
SCHEDULER = ROOT / "shell" / "intel_shell" / "scheduler.py"
CORE_CONFIG = ROOT / "shell" / "intel_shell" / "config.py"
CORE_MAIN = ROOT / "apps" / "cored" / "src" / "main.rs"
STORE = ROOT / "crates" / "store" / "src" / "sqlite.rs"
SUBSCRIPTIONS = ROOT / "shell" / "intel_shell" / "config.py"
SERVICE = ROOT / "deploy" / "intel-pipeline.service"
TIMER = ROOT / "deploy" / "intel-pipeline.timer"
DEPLOY_README = ROOT / "deploy" / "README.md"
SCALE_NOTE = ROOT / "docs" / "T8-scale-design-note.md"
VIEW_SUMMARY = ROOT / "evidence" / "v0.9" / "view-benchmark" / "summary.json"
RETRIEVE_ANCHOR_MS = 16.264
EMBEDDING_DIMENSION = 768
COSINE_SAMPLES = 30
SCHEMA_VERSION = 1


def progress_paths(root: Path = ROOT) -> list[Path]:
    """Return every progress record; the active cycle must never be omitted."""
    return sorted(root.resolve().glob("PROGRESS-v*.md"))


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
        ["git", "status", "--porcelain"],
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
        },
    }


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


def scheduler_measurement() -> dict[str, Any]:
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
    topology = process_topology()
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
            "SqliteStore::open(",
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
    if production_core.count("SqliteStore::open(") != 1:
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
                "path": "SqliteStore::open",
                "writes": "schema/FTS triggers, cursor migration, missing-fingerprint backfill",
                "source": source_ref(CORE_MAIN, "SqliteStore::open("),
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
    remote_core_url_hits: list[str] = []
    for path in (*progress_paths(), SERVICE, CORE_CONFIG):
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


def view_measurement() -> dict[str, Any]:
    summary = json.loads(VIEW_SUMMARY.read_text())
    reports = summary.get("reports")
    gate = summary.get("gate")
    if not isinstance(reports, list) or len(reports) != 4:
        raise AuditFailure(f"{VIEW_SUMMARY}: expected four reports")
    if not isinstance(gate, dict):
        raise AuditFailure(f"{VIEW_SUMMARY}: missing gate")
    return {
        "slo": summary["slo"],
        "reports": reports,
        "cross_corpus_slopes": summary["cross_corpus_slopes"],
        "gate": gate,
        "promoted_task": "V2",
    }


def evaluate(measurements: dict[str, Any]) -> list[dict[str, Any]]:
    scheduler = measurements["scheduler"]
    writers = measurements["writers"]
    cosine = measurements["pgvector"]
    multi_host = measurements["multi_host"]
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
            "id": "/view materialization",
            "unchanged_trigger": (
                "cold or warm p95 crosses the predeclared V1 SLO in both runs"
            ),
            "measurement": (
                f"V1 gate={view['gate']['overall']}; "
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
            "V2"
            if row["id"] == "/view materialization"
            and row["disposition"] == "promote"
            else None
        )
    return rows


def production_measurements() -> dict[str, Any]:
    return {
        "scheduler": scheduler_measurement(),
        "writers": writer_measurement(),
        "pgvector": exact_cosine_measurement(),
        "multi_host": multi_host_measurement(),
        "view": view_measurement(),
    }


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
            "largest_p95_ms": 8.0,
            "a3_retrieve_anchor_ms": RETRIEVE_ANCHOR_MS,
            "largest_p95_below_a3_anchor": True,
        },
        "multi_host": {
            "recorded_cross_host_core_shell_requests": 0,
            "cored_default_bind": "127.0.0.1:8788",
            "deployment_core_url": "http://127.0.0.1:8788",
        },
        "view": {
            "gate": {"overall": "materialization-deferred"},
            "promoted_task": None,
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
    required = {"T7 robots single-flight", "Postgres"}
    if not required.issubset(fired):
        raise AuditFailure(
            "synthetic two-harvester/two-writer input did not fire both triggers"
        )
    print("CONTROL FIRED: two harvesters and two archive writers were promoted")
    return 1


def run_production(output: Path) -> int:
    if output.exists():
        raise AuditFailure(f"refusing to overwrite existing evidence: {output}")
    measurements = production_measurements()
    rows = evaluate(measurements)
    report = {
        "schema_version": SCHEMA_VERSION,
        "task": "v0.9 D4",
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
        description="Audit all five deferred v0.9 design triggers"
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--output", type=Path)
    group.add_argument(
        "--control",
        choices=("two-harvesters-two-writers",),
    )
    args = parser.parse_args()
    if args.control:
        return run_control()
    return run_production(args.output.resolve())


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AuditFailure as error:
        print(f"audit-deferred: FAIL: {error}", file=sys.stderr)
        raise SystemExit(2)
