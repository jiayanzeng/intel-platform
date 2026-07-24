from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

from tools.benchmark_view import BenchmarkFailure, percentile_95


ROOT = Path(__file__).resolve().parents[2]
TOOL = ROOT / "tools" / "benchmark_view.py"


def control_command(name: str) -> list[str]:
    return [
        sys.executable,
        str(TOOL),
        "--anchor-ms",
        "16.264",
        "--anchor-source",
        "A3 retrieve measurement",
        "--cold-factor",
        "10",
        "--cold-reason",
        "process and SQLite startup headroom",
        "--warm-factor",
        "2",
        "--warm-reason",
        "local cache-hit headroom",
        "--cold-slo-ms",
        "162.640",
        "--warm-slo-ms",
        "32.528",
        "--physically-plausible",
        "yes",
        "--sector",
        "science",
        "--control",
        name,
    ]


def test_p95_is_nearest_rank() -> None:
    assert percentile_95([float(value) for value in range(1, 101)]) == 95.0
    assert percentile_95([float(value) for value in range(1, 11)]) == 10.0
    with pytest.raises(BenchmarkFailure, match="zero samples"):
        percentile_95([])


def test_delayed_control_fires_cold_and_warm() -> None:
    result = subprocess.run(
        control_command("delayed"),
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
        timeout=20,
    )
    assert result.returncode != 0
    assert "cold" in result.stdout
    assert "warm" in result.stdout
    assert result.stdout.count("FIRED") == 2
    assert "both cold and warm checks fail" in result.stdout


def test_empty_sector_control_rejects_warm_empty_path() -> None:
    result = subprocess.run(
        control_command("empty-sector"),
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
        timeout=20,
    )
    assert result.returncode != 0
    assert "empty-sector warm control failed benchmark" in result.stdout
    assert "non-positive documents_analyzed=0" in result.stdout
