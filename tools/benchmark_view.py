#!/usr/bin/env python3
"""Failure-capable `/view` latency benchmark over disposable archive copies."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import platform
import shutil
import socket
import sqlite3
import subprocess
import sys
import tempfile
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any, Callable


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "config" / "protected-artifacts.json"
CORE_CONFIG = ROOT / "config" / "core.json"
CORE_ENTITIES = ROOT / "config" / "entities.json"
CORED = ROOT / "target" / "debug" / "cored"
EXPECTED_ARCHIVES = (1764, 2600)
REPORT_SCHEMA = 1
V2_BODY_BASELINES = {
    1764: "43af73a081eca3d0e57f646b54129df2a27550b129a56729683fd7c0c413784f",
    2600: "5685e69aafe006ef2cfaf33836a99d36310b9a314594edbd9163ee25bbc8af81",
}
V2_ANALYZED_DOCUMENTS = {1764: 1708, 2600: 2487}
DIAGNOSTIC_HEADERS = {
    "process_main_to_listener_ready": (
        "x-intel-view-stage-process-main-to-listener-ready-us"
    ),
    "store_open": "x-intel-view-stage-store-open-us",
    "store_connection": "x-intel-view-stage-store-connection-us",
    "store_schema_fts": "x-intel-view-stage-store-schema-fts-us",
    "store_cursor_migration": (
        "x-intel-view-stage-store-cursor-migration-us"
    ),
    "store_fingerprint_backfill": (
        "x-intel-view-stage-store-fingerprint-backfill-us"
    ),
    "sector_load": "x-intel-view-stage-sector-load-us",
    "analysis": "x-intel-view-stage-analysis-us",
    "response_build": "x-intel-view-stage-response-build-us",
    "serialization": "x-intel-view-stage-serialization-us",
    "handler_total": "x-intel-view-stage-handler-total-us",
}


class BenchmarkFailure(RuntimeError):
    """A benchmark validity invariant failed."""


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def percentile_95(samples: list[float]) -> float:
    if not samples:
        raise BenchmarkFailure("cannot calculate p95 from zero samples")
    ordered = sorted(samples)
    return ordered[math.ceil(0.95 * len(ordered)) - 1]


def distribution(samples: list[float]) -> dict[str, Any]:
    ordered = sorted(samples)
    middle = len(ordered) // 2
    if len(ordered) % 2:
        median = ordered[middle]
    else:
        median = (ordered[middle - 1] + ordered[middle]) / 2
    return {
        "samples_ms": [round(value, 6) for value in samples],
        "minimum_ms": round(ordered[0], 6),
        "median_ms": round(median, 6),
        "p95_ms": round(percentile_95(samples), 6),
        "maximum_ms": round(ordered[-1], 6),
        "p95_method": "nearest-rank: sorted_samples[ceil(0.95*n)-1]",
    }


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
    tracked_diff = subprocess.run(
        ["git", "diff", "--binary", "HEAD"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    ).stdout
    return {
        "head_commit": head,
        "worktree_dirty": bool(status),
        "worktree_status": status,
        "tracked_diff_sha256": hashlib.sha256(tracked_diff).hexdigest(),
        "measured_source_sha256": {
            "apps/cored/src/main.rs": sha256(
                ROOT / "apps" / "cored" / "src" / "main.rs"
            ),
            "tools/benchmark_view.py": sha256(Path(__file__).resolve()),
            "run": sha256(ROOT / "run"),
        },
    }


def host_summary() -> dict[str, Any]:
    summary: dict[str, Any] = {
        "platform": platform.platform(),
        "system": platform.system(),
        "release": platform.release(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "logical_cpu_count": os.cpu_count(),
        "python": platform.python_version(),
    }
    if platform.system() == "Darwin":
        for key, label in (
            ("hw.model", "hardware_model"),
            ("hw.memsize", "memory_bytes"),
            ("machdep.cpu.brand_string", "cpu_brand"),
        ):
            result = subprocess.run(
                ["sysctl", "-n", key],
                text=True,
                capture_output=True,
                check=False,
            )
            if result.returncode == 0 and result.stdout.strip():
                summary[label] = result.stdout.strip()
    return summary


def configured_sector_ids(path: Path) -> list[str]:
    config = json.loads(path.read_text())
    sectors = config.get("sectors")
    if not isinstance(sectors, list):
        raise BenchmarkFailure(f"{path}: sectors must be a list")
    ids = [
        sector.get("id")
        for sector in sectors
        if isinstance(sector, dict) and isinstance(sector.get("id"), str)
    ]
    if len(ids) != len(sectors) or len(ids) != len(set(ids)):
        raise BenchmarkFailure(f"{path}: sector ids are missing or duplicated")
    return ids


def archive_records(path: Path) -> list[dict[str, Any]]:
    manifest = json.loads(path.read_text())
    artifacts = manifest.get("artifacts")
    if not isinstance(artifacts, list):
        raise BenchmarkFailure(f"{path}: artifacts must be a list")
    records = [
        artifact
        for artifact in artifacts
        if isinstance(artifact, dict)
        and isinstance(artifact.get("expected"), dict)
        and artifact["expected"].get("documents") in EXPECTED_ARCHIVES
    ]
    counts = sorted(
        int(artifact["expected"]["documents"]) for artifact in records
    )
    if counts != list(EXPECTED_ARCHIVES):
        raise BenchmarkFailure(
            f"{path}: expected protected archive counts "
            f"{list(EXPECTED_ARCHIVES)}, observed {counts}"
        )
    return sorted(records, key=lambda item: item["expected"]["documents"])


def archive_facts(path: Path, sector: str) -> dict[str, Any]:
    with sqlite3.connect(f"file:{path}?mode=ro", uri=True) as connection:
        total = int(
            connection.execute("SELECT COUNT(*) FROM documents").fetchone()[0]
        )
        sector_count = int(
            connection.execute(
                "SELECT COUNT(*) FROM documents WHERE sector = ?", (sector,)
            ).fetchone()[0]
        )
        integrity = str(
            connection.execute("PRAGMA integrity_check").fetchone()[0]
        )
    return {
        "documents": total,
        "sector_documents": sector_count,
        "integrity_check": integrity,
    }


def opener() -> urllib.request.OpenerDirector:
    return urllib.request.build_opener(urllib.request.ProxyHandler({}))


def get_json(
    url: str, *, measured: bool, timeout: float = 180.0
) -> tuple[float, dict[str, Any], dict[str, str]]:
    elapsed_ms, payload, headers, _ = get_json_with_body(
        url,
        measured=measured,
        timeout=timeout,
    )
    return elapsed_ms, payload, headers


def get_json_with_body(
    url: str, *, measured: bool, timeout: float = 180.0
) -> tuple[float, dict[str, Any], dict[str, str], bytes]:
    started = time.perf_counter_ns()
    with opener().open(url, timeout=timeout) as response:
        body = response.read()
        payload = json.loads(body)
        headers = {key.lower(): value for key, value in response.headers.items()}
    elapsed_ms = (time.perf_counter_ns() - started) / 1_000_000
    if not isinstance(payload, dict):
        raise BenchmarkFailure(f"{url}: JSON response was not an object")
    return (elapsed_ms if measured else 0.0), payload, headers, body


def get_json_diagnostic(
    url: str, timeout: float = 180.0
) -> tuple[float, float, dict[str, Any], dict[str, str], bytes]:
    started = time.perf_counter_ns()
    with opener().open(url, timeout=timeout) as response:
        body = response.read()
        headers = {key.lower(): value for key, value in response.headers.items()}
    wire_elapsed_ms = (time.perf_counter_ns() - started) / 1_000_000
    decode_started = time.perf_counter_ns()
    payload = json.loads(body)
    decode_ms = (time.perf_counter_ns() - decode_started) / 1_000_000
    if not isinstance(payload, dict):
        raise BenchmarkFailure(f"{url}: JSON response was not an object")
    return wire_elapsed_ms, decode_ms, payload, headers, body


def wait_until_ready(server: "Server", timeout: float = 15.0) -> None:
    deadline = time.monotonic() + timeout
    last_error = "no response"
    while time.monotonic() < deadline:
        if not server.alive():
            raise BenchmarkFailure(
                f"benchmark server exited before readiness: {server.diagnosis()}"
            )
        try:
            get_json(f"{server.base_url}/health", measured=False, timeout=0.5)
            return
        except (OSError, urllib.error.URLError, json.JSONDecodeError) as error:
            last_error = f"{type(error).__name__}: {error}"
            time.sleep(0.025)
    raise BenchmarkFailure(
        f"benchmark server did not become ready: {last_error}; "
        f"{server.diagnosis()}"
    )


def inspect_view(
    payload: dict[str, Any],
    headers: dict[str, str],
    expected_cache: str,
    expected_generation: int | None = None,
) -> tuple[int, int]:
    documents = payload.get("documents_analyzed")
    if type(documents) is not int or documents <= 0:
        raise BenchmarkFailure(
            f"{expected_cache} /view sample returned non-positive "
            f"documents_analyzed={documents!r}"
        )
    cache = headers.get("x-intel-view-cache")
    if cache != expected_cache:
        raise BenchmarkFailure(
            f"expected /view cache={expected_cache}, observed {cache!r}"
        )
    raw_generation = headers.get("x-intel-view-generation")
    try:
        generation = int(raw_generation)  # type: ignore[arg-type]
    except (TypeError, ValueError) as error:
        raise BenchmarkFailure(
            f"invalid /view generation header {raw_generation!r}"
        ) from error
    if expected_generation is not None and generation != expected_generation:
        raise BenchmarkFailure(
            "warm /view generation moved: "
            f"expected {expected_generation}, observed {generation}"
        )
    return documents, generation


class Server:
    base_url: str

    def start(self) -> None:
        raise NotImplementedError

    def stop(self) -> None:
        raise NotImplementedError

    def alive(self) -> bool:
        raise NotImplementedError

    def diagnosis(self) -> str:
        raise NotImplementedError


class CoreServer(Server):
    def __init__(
        self,
        database: Path,
        log_path: Path,
        *,
        diagnostic_delay_stage: str | None = None,
        diagnostic_delay_ms: int = 0,
    ):
        self.database = database
        self.log_path = log_path
        self.diagnostic_delay_stage = diagnostic_delay_stage
        self.diagnostic_delay_ms = diagnostic_delay_ms
        self.process: subprocess.Popen[bytes] | None = None
        self.log_handle: Any = None
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as candidate:
            candidate.bind(("127.0.0.1", 0))
            self.port = int(candidate.getsockname()[1])
        self.base_url = f"http://127.0.0.1:{self.port}"

    def start(self) -> None:
        environment = os.environ.copy()
        environment.update(
            {
                "CORE_DB": str(self.database),
                "CORE_BIND": f"127.0.0.1:{self.port}",
                "CORE_CONFIG": str(CORE_CONFIG),
                "CORE_ENTITIES": str(CORE_ENTITIES),
            }
        )
        environment.pop("CORE_TOKEN", None)
        environment.pop("CORE_VIEW_DIAGNOSTIC_DELAY_STAGE", None)
        environment.pop("CORE_VIEW_DIAGNOSTIC_DELAY_MS", None)
        if self.diagnostic_delay_stage is not None:
            environment["CORE_VIEW_DIAGNOSTIC_DELAY_STAGE"] = (
                self.diagnostic_delay_stage
            )
            environment["CORE_VIEW_DIAGNOSTIC_DELAY_MS"] = str(
                self.diagnostic_delay_ms
            )
        self.log_handle = self.log_path.open("wb")
        self.process = subprocess.Popen(
            [str(CORED)],
            cwd=ROOT,
            env=environment,
            stdin=subprocess.DEVNULL,
            stdout=self.log_handle,
            stderr=subprocess.STDOUT,
        )

    def stop(self) -> None:
        if self.process is not None and self.process.poll() is None:
            self.process.terminate()
            try:
                self.process.wait(timeout=3)
            except subprocess.TimeoutExpired:
                self.process.kill()
                self.process.wait(timeout=3)
        if self.log_handle is not None:
            self.log_handle.close()

    def alive(self) -> bool:
        return self.process is not None and self.process.poll() is None

    def diagnosis(self) -> str:
        if not self.log_path.exists():
            return "no process log"
        return self.log_path.read_text(errors="replace")[-2000:]


class ControlHandler(BaseHTTPRequestHandler):
    server: "ControlHttpServer"

    def do_GET(self) -> None:  # noqa: N802 - BaseHTTPRequestHandler API
        parsed = urllib.parse.urlsplit(self.path)
        if parsed.path == "/health":
            self._write({"ok": True})
            return
        if parsed.path != "/view":
            self.send_error(404)
            return
        self.server.view_requests += 1
        if self.server.delay_seconds:
            time.sleep(self.server.delay_seconds)
        first = self.server.view_requests == 1
        documents = 0 if self.server.empty_after_prime and not first else 1
        self._write(
            {"documents_analyzed": documents},
            {
                "x-intel-view-cache": "miss" if first else "hit",
                "x-intel-view-generation": "0",
            },
        )

    def log_message(self, format: str, *args: object) -> None:
        return

    def _write(
        self, payload: dict[str, Any], headers: dict[str, str] | None = None
    ) -> None:
        body = json.dumps(payload).encode()
        self.send_response(200)
        self.send_header("content-type", "application/json")
        for key, value in (headers or {}).items():
            self.send_header(key, value)
        self.send_header("content-length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


class ControlHttpServer(ThreadingHTTPServer):
    daemon_threads = True

    def __init__(
        self,
        address: tuple[str, int],
        *,
        delay_seconds: float,
        empty_after_prime: bool,
    ):
        super().__init__(address, ControlHandler)
        self.delay_seconds = delay_seconds
        self.empty_after_prime = empty_after_prime
        self.view_requests = 0


class ControlServer(Server):
    def __init__(self, delay_seconds: float, empty_after_prime: bool):
        self.httpd = ControlHttpServer(
            ("127.0.0.1", 0),
            delay_seconds=delay_seconds,
            empty_after_prime=empty_after_prime,
        )
        self.thread: threading.Thread | None = None
        self.base_url = (
            f"http://127.0.0.1:{self.httpd.server_address[1]}"
        )

    def start(self) -> None:
        self.thread = threading.Thread(target=self.httpd.serve_forever)
        self.thread.start()

    def stop(self) -> None:
        self.httpd.shutdown()
        self.httpd.server_close()
        if self.thread is not None:
            self.thread.join(timeout=3)

    def alive(self) -> bool:
        return self.thread is not None and self.thread.is_alive()

    def diagnosis(self) -> str:
        return "local benchmark control"


ServerFactory = Callable[[], Server]


def view_url(server: Server, sector: str) -> str:
    query = urllib.parse.urlencode({"sectors": sector})
    return f"{server.base_url}/view?{query}"


def cold_samples(
    factory: ServerFactory, sector: str, iterations: int
) -> tuple[list[float], list[int], list[int]]:
    samples: list[float] = []
    documents: list[int] = []
    generations: list[int] = []
    for _ in range(iterations):
        server = factory()
        started = time.perf_counter_ns()
        try:
            server.start()
            wait_until_ready(server)
            _, payload, headers = get_json(
                view_url(server, sector), measured=False
            )
            elapsed = (time.perf_counter_ns() - started) / 1_000_000
            count, generation = inspect_view(payload, headers, "miss")
            samples.append(elapsed)
            documents.append(count)
            generations.append(generation)
        finally:
            server.stop()
    return samples, documents, generations


def warm_samples(
    factory: ServerFactory, sector: str, iterations: int
) -> tuple[list[float], list[int], int]:
    server = factory()
    try:
        server.start()
        wait_until_ready(server)
        _, prime_payload, prime_headers = get_json(
            view_url(server, sector), measured=False
        )
        _, generation = inspect_view(prime_payload, prime_headers, "miss")
        samples: list[float] = []
        documents: list[int] = []
        for _ in range(iterations):
            elapsed, payload, headers = get_json(
                view_url(server, sector), measured=True
            )
            count, observed_generation = inspect_view(
                payload, headers, "hit", generation
            )
            if observed_generation != generation:
                raise BenchmarkFailure("warm generation changed")
            samples.append(elapsed)
            documents.append(count)
        return samples, documents, generation
    finally:
        server.stop()


def threshold_record(args: argparse.Namespace) -> dict[str, Any]:
    derived_cold = args.anchor_ms * args.cold_factor
    derived_warm = args.anchor_ms * args.warm_factor
    for name, supplied, derived in (
        ("cold", args.cold_slo_ms, derived_cold),
        ("warm", args.warm_slo_ms, derived_warm),
    ):
        if not math.isclose(supplied, derived, rel_tol=0, abs_tol=0.0005):
            raise BenchmarkFailure(
                f"{name} SLO {supplied:.6f} ms does not equal "
                f"anchor×factor {derived:.6f} ms"
            )
    return {
        "anchor": {
            "milliseconds": args.anchor_ms,
            "source": args.anchor_source,
        },
        "cold": {
            "headroom_factor": args.cold_factor,
            "reason": args.cold_reason,
            "fires_at_ms": args.cold_slo_ms,
        },
        "warm": {
            "headroom_factor": args.warm_factor,
            "reason": args.warm_reason,
            "fires_at_ms": args.warm_slo_ms,
        },
        "physically_plausible_on_host": args.physically_plausible,
        "predeclared_before_timing": True,
    }


def safe_output_paths(output_dir: Path) -> list[Path]:
    names = [
        f"run-{run_number}-{label}.json"
        for run_number in (1, 2)
        for label in ("core-1764", "live-smoke-2600")
    ]
    paths = [output_dir / name for name in names]
    paths.append(output_dir / "summary.json")
    existing = [path for path in paths if path.exists()]
    if existing:
        raise BenchmarkFailure(
            "refusing to overwrite benchmark evidence: "
            + ", ".join(str(path) for path in existing)
        )
    output_dir.mkdir(parents=True, exist_ok=True)
    return paths


def make_core_factory(
    database: Path, log_dir: Path, label: str
) -> ServerFactory:
    counter = 0

    def factory() -> Server:
        nonlocal counter
        counter += 1
        return CoreServer(database, log_dir / f"{label}-{counter}.log")

    return factory


def diagnostic_header_ms(headers: dict[str, str], stage: str) -> float:
    name = DIAGNOSTIC_HEADERS[stage]
    raw = headers.get(name)
    try:
        value = int(raw)  # type: ignore[arg-type]
    except (TypeError, ValueError) as error:
        raise BenchmarkFailure(
            f"missing or invalid diagnostic header {name}: {raw!r}"
        ) from error
    if value < 0:
        raise BenchmarkFailure(f"negative diagnostic header {name}: {value}")
    return value / 1000


def decomposition_cold_samples(
    factory: ServerFactory,
    sector: str,
    iterations: int,
    expected_documents: int,
) -> list[dict[str, Any]]:
    samples: list[dict[str, Any]] = []
    expected_body_hash = V2_BODY_BASELINES[expected_documents]
    for _ in range(iterations):
        server = factory()
        cold_started = time.perf_counter_ns()
        try:
            server.start()
            wait_until_ready(server)
            spawn_ready_ms = (
                time.perf_counter_ns() - cold_started
            ) / 1_000_000
            (
                wire_ms,
                decode_ms,
                payload,
                headers,
                body,
            ) = get_json_diagnostic(view_url(server, sector))
            cold_total_ms = (
                time.perf_counter_ns() - cold_started
            ) / 1_000_000
            documents, generation = inspect_view(
                payload,
                headers,
                "miss",
            )
            expected_analyzed = V2_ANALYZED_DOCUMENTS[expected_documents]
            if documents != expected_analyzed:
                raise BenchmarkFailure(
                    f"decomposition expected {expected_analyzed} analyzed "
                    f"documents, observed {documents}"
                )
            body_hash = hashlib.sha256(body).hexdigest()
            if body_hash != expected_body_hash:
                raise BenchmarkFailure(
                    f"{expected_documents}-document /view body changed: "
                    f"expected {expected_body_hash}, observed {body_hash}"
                )

            measured = {
                stage: diagnostic_header_ms(headers, stage)
                for stage in DIAGNOSTIC_HEADERS
            }
            handler_components = sum(
                measured[stage]
                for stage in (
                    "sector_load",
                    "analysis",
                    "response_build",
                    "serialization",
                )
            )
            handler_other_ms = max(
                measured["handler_total"] - handler_components,
                0.0,
            )
            http_transfer_ms = max(
                wire_ms - measured["handler_total"],
                0.0,
            )
            startup_other_ms = max(
                spawn_ready_ms - measured["store_open"],
                0.0,
            )
            attributed = (
                spawn_ready_ms
                + handler_components
                + handler_other_ms
                + http_transfer_ms
                + decode_ms
            )
            samples.append(
                {
                    "cold_total": cold_total_ms,
                    "process_spawn_to_listener_ready": spawn_ready_ms,
                    "process_main_to_listener_ready": measured[
                        "process_main_to_listener_ready"
                    ],
                    "store_open": measured["store_open"],
                    "store_connection": measured["store_connection"],
                    "store_schema_fts": measured["store_schema_fts"],
                    "store_cursor_migration": measured[
                        "store_cursor_migration"
                    ],
                    "store_fingerprint_backfill": measured[
                        "store_fingerprint_backfill"
                    ],
                    "startup_other_residual": startup_other_ms,
                    "sector_load": measured["sector_load"],
                    "analysis": measured["analysis"],
                    "response_build": measured["response_build"],
                    "serialization": measured["serialization"],
                    "handler_other_residual": handler_other_ms,
                    "http_transfer": http_transfer_ms,
                    "client_json_decode": decode_ms,
                    "unattributed_residual": max(
                        cold_total_ms - attributed,
                        0.0,
                    ),
                    "handler_total": measured["handler_total"],
                    "wire_request_total": wire_ms,
                    "generation": generation,
                    "body_sha256": body_hash,
                    "fingerprints_backfilled": int(
                        headers.get(
                            "x-intel-view-fingerprints-backfilled",
                            "-1",
                        )
                    ),
                }
            )
        finally:
            server.stop()
    return samples


def decomposition_stage_report(
    samples: list[dict[str, Any]],
) -> dict[str, Any]:
    cold = distribution([float(sample["cold_total"]) for sample in samples])
    cold_p95 = float(cold["p95_ms"])
    stages: dict[str, Any] = {}
    excluded = {
        "generation",
        "body_sha256",
        "fingerprints_backfilled",
        "cold_total",
    }
    for stage in sorted(samples[0].keys() - excluded):
        values = [float(sample[stage]) for sample in samples]
        measured = distribution(values)
        measured["share_of_cold_p95_percent"] = round(
            float(measured["p95_ms"]) * 100 / cold_p95,
            6,
        )
        stages[stage] = measured
    return {
        "cold": cold,
        "stages": stages,
        "body_sha256": sorted(
            {str(sample["body_sha256"]) for sample in samples}
        ),
        "generations": [
            int(sample["generation"]) for sample in samples
        ],
        "fingerprints_backfilled": [
            int(sample["fingerprints_backfilled"]) for sample in samples
        ],
        "stage_relationships": {
            "process_spawn_to_listener_ready": (
                "inclusive startup parent measured by the harness"
            ),
            "store_open": (
                "nested within process startup; connection, schema/FTS, "
                "cursor migration, and fingerprint backfill are nested within it"
            ),
            "request_path": (
                "sector_load + analysis + response_build + serialization + "
                "handler_other_residual + http_transfer + client_json_decode"
            ),
        },
    }


def decomposition_output_paths(output_dir: Path) -> list[Path]:
    paths = [
        output_dir
        / f"run-{run_number}-{label}.json"
        for run_number in (1, 2)
        for label in ("core-1764", "live-smoke-2600")
    ]
    paths.append(output_dir / "summary.json")
    existing = [path for path in paths if path.exists()]
    if existing:
        raise BenchmarkFailure(
            "refusing to overwrite decomposition evidence: "
            + ", ".join(str(path) for path in existing)
        )
    output_dir.mkdir(parents=True, exist_ok=True)
    return paths


def run_decomposition(args: argparse.Namespace) -> int:
    if not CORED.is_file():
        raise BenchmarkFailure(
            f"{CORED} does not exist; build cored before benchmarking"
        )
    if args.cold_iterations != 10:
        raise BenchmarkFailure(
            "V2 decomposition evidence requires exactly 10 cold samples"
        )
    configured = configured_sector_ids(CORE_CONFIG)
    if args.sector not in configured:
        raise BenchmarkFailure(
            f"sector {args.sector!r} is absent from {CORE_CONFIG}"
        )
    output_dir = Path(args.output_dir).resolve()
    report_paths = decomposition_output_paths(output_dir)
    records = archive_records(MANIFEST)
    subject = git_subject()
    host = host_summary()
    reports: list[dict[str, Any]] = []

    with tempfile.TemporaryDirectory(
        prefix="intel-view-decomposition-"
    ) as temp:
        temp_dir = Path(temp)
        log_dir = temp_dir / "logs"
        log_dir.mkdir()
        report_index = 0
        for run_number in (1, 2):
            for record in records:
                documents = int(record["expected"]["documents"])
                source = ROOT / str(record["path"])
                if sha256(source) != record["sha256"]:
                    raise BenchmarkFailure(
                        f"{record['path']}: protected hash mismatch"
                    )
                copy_path = (
                    temp_dir
                    / f"run-{run_number}-archive-{documents}.db"
                )
                shutil.copyfile(source, copy_path)
                copy_before = sha256(copy_path)
                factory = make_core_factory(
                    copy_path,
                    log_dir,
                    f"run-{run_number}-{documents}",
                )
                samples = decomposition_cold_samples(
                    factory,
                    args.sector,
                    args.cold_iterations,
                    documents,
                )
                copy_after = sha256(copy_path)
                if copy_after != copy_before:
                    raise BenchmarkFailure(
                        f"{copy_path}: disposable archive bytes changed"
                    )
                measured = decomposition_stage_report(samples)
                if any(
                    count != 0
                    for count in measured["fingerprints_backfilled"]
                ):
                    raise BenchmarkFailure(
                        f"{documents}: protected copy unexpectedly backfilled "
                        "one or more fingerprints"
                    )
                report = {
                    "schema_version": 1,
                    "task": "v0.10 V2",
                    "run": run_number,
                    "measured_at": time.strftime(
                        "%Y-%m-%dT%H:%M:%SZ",
                        time.gmtime(),
                    ),
                    "subject": subject,
                    "host": host,
                    "query": {"sector": args.sector},
                    "archive": {
                        "protected_path": record["path"],
                        "documents": documents,
                        "protected_sha256": record["sha256"],
                        "copy_sha256_before": copy_before,
                        "copy_sha256_after": copy_after,
                    },
                    "iterations": args.cold_iterations,
                    **measured,
                }
                report_paths[report_index].write_text(
                    json.dumps(report, indent=2, sort_keys=True) + "\n"
                )
                report_index += 1
                reports.append(report)
                print(
                    f"V2 run {run_number} archive {documents}: "
                    f"cold p95={report['cold']['p95_ms']:.6f} ms; "
                    f"startup={report['stages']['process_spawn_to_listener_ready']['p95_ms']:.6f} ms; "
                    f"load={report['stages']['sector_load']['p95_ms']:.6f} ms; "
                    f"analysis={report['stages']['analysis']['p95_ms']:.6f} ms"
                )

    summary = {
        "schema_version": 1,
        "task": "v0.10 V2",
        "measured_at": time.strftime(
            "%Y-%m-%dT%H:%M:%SZ",
            time.gmtime(),
        ),
        "subject": subject,
        "host": host,
        "prior_v1_outlier_ms": 1693.423417,
        "prior_v1_outlier_disposition": {
            "reproduced_cold_p95_ms": reports[0]["cold"]["p95_ms"],
            "localized_stage": "process_spawn_to_listener_ready",
            "localized_stage_p95_ms": reports[0]["stages"][
                "process_spawn_to_listener_ready"
            ]["p95_ms"],
            "core_main_to_listener_ready_p95_ms": reports[0]["stages"][
                "process_main_to_listener_ready"
            ]["p95_ms"],
            "store_open_p95_ms": reports[0]["stages"]["store_open"][
                "p95_ms"
            ],
            "finding": (
                "reproduced and localized outside timed core startup; "
                "host scheduling/process-observation cause not further explained"
            ),
        },
        "reports": [
            {
                "run": report["run"],
                "documents": report["archive"]["documents"],
                "cold_p95_ms": report["cold"]["p95_ms"],
                "stage_p95_ms": {
                    name: stage["p95_ms"]
                    for name, stage in report["stages"].items()
                },
                "stage_share_of_cold_p95_percent": {
                    name: stage["share_of_cold_p95_percent"]
                    for name, stage in report["stages"].items()
                },
                "body_sha256": report["body_sha256"],
            }
            for report in reports
        ],
    }
    report_paths[-1].write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n"
    )
    for record in records:
        if sha256(ROOT / str(record["path"])) != record["sha256"]:
            raise BenchmarkFailure(
                f"{record['path']}: protected bytes changed during decomposition"
            )
    print(f"V2 decomposition: PASS; evidence={output_dir}")
    return 0


def run_decomposition_control(args: argparse.Namespace) -> int:
    if not CORED.is_file():
        raise BenchmarkFailure(
            f"{CORED} does not exist; build cored before control"
        )
    record = archive_records(MANIFEST)[0]
    documents = int(record["expected"]["documents"])
    with tempfile.TemporaryDirectory(
        prefix="intel-view-decomposition-control-"
    ) as temp:
        temp_dir = Path(temp)
        database = temp_dir / "control.db"
        shutil.copyfile(ROOT / str(record["path"]), database)
        log_dir = temp_dir / "logs"
        log_dir.mkdir()

        baseline_factory = make_core_factory(
            database,
            log_dir,
            "baseline",
        )
        baseline = decomposition_cold_samples(
            baseline_factory,
            args.sector,
            3,
            documents,
        )

        counter = 0

        def delayed_factory() -> Server:
            nonlocal counter
            counter += 1
            return CoreServer(
                database,
                log_dir / f"delayed-{counter}.log",
                diagnostic_delay_stage="analysis",
                diagnostic_delay_ms=100,
            )

        delayed = decomposition_cold_samples(
            delayed_factory,
            args.sector,
            3,
            documents,
        )

    baseline_report = decomposition_stage_report(baseline)
    delayed_report = decomposition_stage_report(delayed)
    analysis_delta = (
        float(delayed_report["stages"]["analysis"]["median_ms"])
        - float(baseline_report["stages"]["analysis"]["median_ms"])
    )
    load_delta = abs(
        float(delayed_report["stages"]["sector_load"]["median_ms"])
        - float(baseline_report["stages"]["sector_load"]["median_ms"])
    )
    print(
        "decomposition control: "
        f"analysis median delta={analysis_delta:.6f} ms; "
        f"sector_load median delta={load_delta:.6f} ms"
    )
    if analysis_delta >= 80.0 and load_delta < 40.0:
        print(
            "PASS: injected analysis delay appeared in analysis and not "
            "sector_load"
        )
        return 1
    raise BenchmarkFailure(
        "decomposition delay control was not isolated to the named stage"
    )


def benchmark_archive(
    *,
    args: argparse.Namespace,
    run_number: int,
    source_record: dict[str, Any],
    copy_path: Path,
    log_dir: Path,
    subject: dict[str, Any],
    host: dict[str, Any],
    thresholds: dict[str, Any],
) -> dict[str, Any]:
    expected = source_record["expected"]
    expected_hash = str(source_record["sha256"])
    copy_hash_before = sha256(copy_path)
    if copy_hash_before != expected_hash:
        raise BenchmarkFailure(
            f"{copy_path}: copied hash {copy_hash_before} != {expected_hash}"
        )
    facts = archive_facts(copy_path, args.sector)
    if facts["documents"] != expected["documents"]:
        raise BenchmarkFailure(
            f"{copy_path}: expected {expected['documents']} documents, "
            f"observed {facts['documents']}"
        )
    if facts["sector_documents"] <= 0:
        raise BenchmarkFailure(
            f"{copy_path}: sector {args.sector!r} has no documents"
        )
    if facts["integrity_check"] != "ok":
        raise BenchmarkFailure(
            f"{copy_path}: integrity_check={facts['integrity_check']!r}"
        )

    label = (
        f"run-{run_number}-{Path(source_record['path']).stem}-"
        f"{facts['documents']}"
    )
    factory = make_core_factory(copy_path, log_dir, label)
    cold, cold_documents, cold_generations = cold_samples(
        factory, args.sector, args.cold_iterations
    )
    warm, warm_documents, warm_generation = warm_samples(
        factory, args.sector, args.warm_iterations
    )
    copy_hash_after = sha256(copy_path)
    if copy_hash_after != copy_hash_before:
        raise BenchmarkFailure(
            f"{copy_path}: disposable archive bytes changed during benchmark"
        )

    cold_result = distribution(cold)
    warm_result = distribution(warm)
    cold_result.update(
        {
            "process_restart_per_sample": True,
            "cache_status_asserted": "miss",
            "document_counts": cold_documents,
            "generations": cold_generations,
            "slo_ms": args.cold_slo_ms,
            "passed": cold_result["p95_ms"] <= args.cold_slo_ms,
        }
    )
    warm_result.update(
        {
            "prime_request_measured": False,
            "cache_status_asserted": "hit",
            "document_counts": warm_documents,
            "generation": warm_generation,
            "unmoved_generation_asserted": True,
            "slo_ms": args.warm_slo_ms,
            "passed": warm_result["p95_ms"] <= args.warm_slo_ms,
        }
    )
    return {
        "schema_version": REPORT_SCHEMA,
        "task": "v0.9 V1",
        "run": run_number,
        "measured_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "subject": subject,
        "host": host,
        "slo": thresholds,
        "query": {
            "sector": args.sector,
            "sector_source": "config/core.json",
            "configured_sector_asserted": True,
        },
        "archive": {
            "protected_path": source_record["path"],
            "manifest": "config/protected-artifacts.json",
            "expected_sha256": expected_hash,
            "expected_bytes": source_record["bytes"],
            "expected_documents": expected["documents"],
            "disposable_copy": str(copy_path),
            "copy_sha256_before": copy_hash_before,
            "copy_sha256_after": copy_hash_after,
            **facts,
        },
        "iterations": {
            "cold": args.cold_iterations,
            "warm": args.warm_iterations,
        },
        "cold": cold_result,
        "warm": warm_result,
    }


def slope(
    small_report: dict[str, Any],
    large_report: dict[str, Any],
    path: str,
) -> dict[str, Any]:
    small_documents = int(small_report["archive"]["documents"])
    large_documents = int(large_report["archive"]["documents"])
    small_p95 = float(small_report[path]["p95_ms"])
    large_p95 = float(large_report[path]["p95_ms"])
    delta_documents = large_documents - small_documents
    delta_ms = large_p95 - small_p95
    return {
        "path": path,
        "small_documents": small_documents,
        "large_documents": large_documents,
        "delta_documents": delta_documents,
        "small_p95_ms": small_p95,
        "large_p95_ms": large_p95,
        "delta_p95_ms": round(delta_ms, 6),
        "p95_ms_per_1000_documents": round(
            delta_ms * 1000 / delta_documents, 6
        ),
    }


def gate(reports: list[dict[str, Any]]) -> dict[str, Any]:
    outcomes: list[dict[str, Any]] = []
    for documents in EXPECTED_ARCHIVES:
        archive_reports = [
            report
            for report in reports
            if report["archive"]["documents"] == documents
        ]
        if len(archive_reports) != 2:
            raise BenchmarkFailure(
                f"gate expected two runs for {documents} documents"
            )
        for path in ("cold", "warm"):
            misses = sum(
                not bool(report[path]["passed"]) for report in archive_reports
            )
            if misses == 0:
                disposition = "pass"
            elif misses == 1:
                disposition = "single-run-outlier-rerun-required"
            else:
                disposition = "design-trigger-fired"
            outcomes.append(
                {
                    "documents": documents,
                    "path": path,
                    "misses": misses,
                    "runs": 2,
                    "disposition": disposition,
                }
            )
    if any(item["misses"] == 2 for item in outcomes):
        overall = "materialization-trigger-fired"
        exit_code = 1
    elif any(item["misses"] == 1 for item in outcomes):
        overall = "inconclusive-rerun-required"
        exit_code = 1
    else:
        overall = "materialization-deferred"
        exit_code = 0
    return {
        "rule": (
            "two misses for the same archive/path fire the design trigger; "
            "one miss requires another recorded run"
        ),
        "outcomes": outcomes,
        "overall": overall,
        "exit_code": exit_code,
    }


def run_actual(args: argparse.Namespace) -> int:
    if not CORED.is_file():
        raise BenchmarkFailure(
            f"{CORED} does not exist; build cored before benchmarking"
        )
    threshold = threshold_record(args)
    configured = configured_sector_ids(CORE_CONFIG)
    if args.sector not in configured:
        raise BenchmarkFailure(
            f"sector {args.sector!r} is absent from {CORE_CONFIG}; "
            f"configured={configured}"
        )
    output_dir = Path(args.output_dir).resolve()
    report_paths = safe_output_paths(output_dir)
    records = archive_records(MANIFEST)
    subject = git_subject()
    host = host_summary()

    reports: list[dict[str, Any]] = []
    with tempfile.TemporaryDirectory(prefix="intel-view-benchmark-") as temp:
        temp_dir = Path(temp)
        log_dir = temp_dir / "logs"
        log_dir.mkdir()
        copies: dict[int, Path] = {}
        for record in records:
            source = ROOT / record["path"]
            observed_hash = sha256(source)
            if observed_hash != record["sha256"]:
                raise BenchmarkFailure(
                    f"{record['path']}: protected hash {observed_hash} "
                    f"!= manifest {record['sha256']}"
                )
            destination = (
                temp_dir
                / f"archive-{record['expected']['documents']}.db"
            )
            shutil.copyfile(source, destination)
            copies[int(record["expected"]["documents"])] = destination

        report_index = 0
        for run_number in (1, 2):
            for record in records:
                report = benchmark_archive(
                    args=args,
                    run_number=run_number,
                    source_record=record,
                    copy_path=copies[int(record["expected"]["documents"])],
                    log_dir=log_dir,
                    subject=subject,
                    host=host,
                    thresholds=threshold,
                )
                report_path = report_paths[report_index]
                report_index += 1
                report_path.write_text(
                    json.dumps(report, indent=2, sort_keys=True) + "\n"
                )
                reports.append(report)
                print(
                    f"run {run_number} archive "
                    f"{report['archive']['documents']}: "
                    f"cold p95={report['cold']['p95_ms']:.6f} ms "
                    f"({'PASS' if report['cold']['passed'] else 'MISS'}), "
                    f"warm p95={report['warm']['p95_ms']:.6f} ms "
                    f"({'PASS' if report['warm']['passed'] else 'MISS'})"
                )

        slopes = []
        for run_number in (1, 2):
            run_reports = [
                report for report in reports if report["run"] == run_number
            ]
            run_reports.sort(key=lambda report: report["archive"]["documents"])
            slopes.extend(
                slope(run_reports[0], run_reports[1], path)
                for path in ("cold", "warm")
            )
        decision = gate(reports)
        summary = {
            "schema_version": REPORT_SCHEMA,
            "task": "v0.9 V1",
            "measured_at": time.strftime(
                "%Y-%m-%dT%H:%M:%SZ", time.gmtime()
            ),
            "subject": subject,
            "host": host,
            "slo": threshold,
            "reports": [
                {
                    "run": report["run"],
                    "documents": report["archive"]["documents"],
                    "protected_path": report["archive"]["protected_path"],
                    "cold_p95_ms": report["cold"]["p95_ms"],
                    "warm_p95_ms": report["warm"]["p95_ms"],
                    "cold_passed": report["cold"]["passed"],
                    "warm_passed": report["warm"]["passed"],
                }
                for report in reports
            ],
            "cross_corpus_slopes": slopes,
            "gate": decision,
        }
        report_paths[-1].write_text(
            json.dumps(summary, indent=2, sort_keys=True) + "\n"
        )

    for record in records:
        source = ROOT / record["path"]
        if sha256(source) != record["sha256"]:
            raise BenchmarkFailure(
                f"{record['path']}: protected bytes changed during benchmark"
            )
    print(f"V1 gate: {decision['overall']}")
    print(f"evidence: {output_dir}")
    return int(decision["exit_code"])


def run_control(args: argparse.Namespace) -> int:
    threshold_record(args)
    if args.control == "delayed":
        delay = max(args.cold_slo_ms, args.warm_slo_ms) / 1000 + 0.050
        factory = lambda: ControlServer(delay, False)
        cold, _, _ = cold_samples(factory, args.sector, 2)
        warm, _, _ = warm_samples(factory, args.sector, 2)
        cold_p95 = percentile_95(cold)
        warm_p95 = percentile_95(warm)
        cold_failed = cold_p95 > args.cold_slo_ms
        warm_failed = warm_p95 > args.warm_slo_ms
        print(
            f"delayed control cold p95={cold_p95:.6f} ms "
            f"threshold={args.cold_slo_ms:.6f} ms: "
            f"{'FIRED' if cold_failed else 'DID NOT FIRE'}"
        )
        print(
            f"delayed control warm p95={warm_p95:.6f} ms "
            f"threshold={args.warm_slo_ms:.6f} ms: "
            f"{'FIRED' if warm_failed else 'DID NOT FIRE'}"
        )
        if cold_failed and warm_failed:
            print("PASS: delayed control made both cold and warm checks fail")
            return 1
        raise BenchmarkFailure(
            "SLO is defective: delayed control did not fire both cold and warm"
        )

    factory = lambda: ControlServer(0.0, True)
    try:
        warm_samples(factory, args.sector, 2)
    except BenchmarkFailure as error:
        print(f"PASS: empty-sector warm control failed benchmark: {error}")
        return 1
    raise BenchmarkFailure(
        "empty-sector warm control was incorrectly accepted"
    )


def parser() -> argparse.ArgumentParser:
    value = argparse.ArgumentParser(
        description="Benchmark cored /view over disposable protected archives"
    )
    value.add_argument("--anchor-ms", type=float, required=True)
    value.add_argument("--anchor-source", required=True)
    value.add_argument("--cold-factor", type=float, required=True)
    value.add_argument("--cold-reason", required=True)
    value.add_argument("--warm-factor", type=float, required=True)
    value.add_argument("--warm-reason", required=True)
    value.add_argument("--cold-slo-ms", type=float, required=True)
    value.add_argument("--warm-slo-ms", type=float, required=True)
    value.add_argument(
        "--physically-plausible",
        choices=("yes", "no"),
        required=True,
    )
    value.add_argument("--sector", required=True)
    value.add_argument("--cold-iterations", type=int, default=10)
    value.add_argument("--warm-iterations", type=int, default=100)
    value.add_argument("--output-dir")
    value.add_argument(
        "--decompose",
        action="store_true",
        help="run the v0.10 V2 cold-stage decomposition",
    )
    value.add_argument(
        "--decomposition-control",
        action="store_true",
        help="inject an analysis delay and exit non-zero when detected",
    )
    value.add_argument(
        "--control", choices=("delayed", "empty-sector")
    )
    return value


def main() -> int:
    args = parser().parse_args()
    if args.anchor_ms <= 0 or args.cold_factor <= 0 or args.warm_factor <= 0:
        raise BenchmarkFailure("anchor and headroom factors must be positive")
    if args.cold_slo_ms <= 0 or args.warm_slo_ms <= 0:
        raise BenchmarkFailure("SLO values must be positive")
    if args.cold_iterations <= 0 or args.warm_iterations <= 0:
        raise BenchmarkFailure("iteration counts must be positive")
    if args.decompose and args.decomposition_control:
        raise BenchmarkFailure(
            "--decompose and --decomposition-control are mutually exclusive"
        )
    if args.control and (args.decompose or args.decomposition_control):
        raise BenchmarkFailure(
            "V1 controls cannot be combined with V2 decomposition modes"
        )
    if args.control:
        return run_control(args)
    if args.decomposition_control:
        return run_decomposition_control(args)
    if not args.output_dir:
        raise BenchmarkFailure("--output-dir is required outside control mode")
    if args.decompose:
        return run_decomposition(args)
    if args.cold_iterations != 10 or args.warm_iterations != 100:
        raise BenchmarkFailure(
            "V1 evidence requires exactly 10 cold and 100 warm samples"
        )
    return run_actual(args)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except BenchmarkFailure as error:
        print(f"benchmark-view: FAIL: {error}", file=sys.stderr)
        raise SystemExit(2)
