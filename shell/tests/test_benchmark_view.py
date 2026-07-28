from __future__ import annotations

import ast
import re
import subprocess
import sys
from pathlib import Path

import pytest

from tools.benchmark_view import (
    BenchmarkFailure,
    percentile_95,
    verify_diagnostic_delay_warnings,
)


ROOT = Path(__file__).resolve().parents[2]
TOOL = ROOT / "tools" / "benchmark_view.py"
CORE_MAIN = ROOT / "apps" / "cored" / "src" / "main.rs"
DIAGNOSTIC_DELAY_CALL = re.compile(
    r'diagnostic_delay\(\s*"(?P<stage>[^"]+)"\s*\)'
)


def _rust_diagnostic_delay_stages(
    source: str,
) -> dict[str, int]:
    stages: dict[str, int] = {}
    for line_number, line in enumerate(source.splitlines(), 1):
        for match in DIAGNOSTIC_DELAY_CALL.finditer(line):
            stage = match.group("stage")
            assert stage not in stages, (
                f"{CORE_MAIN.relative_to(ROOT)}:{line_number}: duplicate "
                f"diagnostic_delay stage {stage!r}"
            )
            stages[stage] = line_number
    return stages


def _python_diagnostic_headers(
    source: str,
) -> tuple[set[str], int]:
    tree = ast.parse(source, filename=str(TOOL))
    assignments = [
        node
        for node in tree.body
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name)
            and target.id == "DIAGNOSTIC_HEADERS"
            for target in node.targets
        )
    ]
    assert len(assignments) == 1, (
        f"{TOOL.relative_to(ROOT)}: expected exactly one "
        f"DIAGNOSTIC_HEADERS assignment; found {len(assignments)}"
    )
    assignment = assignments[0]
    assert isinstance(assignment.value, ast.Dict), (
        f"{TOOL.relative_to(ROOT)}:{assignment.lineno}: "
        "DIAGNOSTIC_HEADERS must be a dictionary literal"
    )
    keys = {
        key.value
        for key in assignment.value.keys
        if isinstance(key, ast.Constant) and isinstance(key.value, str)
    }
    assert len(keys) == len(assignment.value.keys), (
        f"{TOOL.relative_to(ROOT)}:{assignment.lineno}: "
        "DIAGNOSTIC_HEADERS keys must be string literals"
    )
    return keys, assignment.lineno


def _assert_diagnostic_stage_correspondence(
    rust_source: str,
    python_source: str,
) -> tuple[set[str], set[str]]:
    rust_stages = _rust_diagnostic_delay_stages(rust_source)
    python_headers, map_line = _python_diagnostic_headers(python_source)
    missing = sorted(set(rust_stages) - python_headers)
    if missing:
        details = "; ".join(
            f"{CORE_MAIN.relative_to(ROOT)}:{rust_stages[stage]}: "
            f"diagnostic_delay stage {stage!r} is absent from "
            f"{TOOL.relative_to(ROOT)}:{map_line}: DIAGNOSTIC_HEADERS"
            for stage in missing
        )
        raise AssertionError(details)
    return set(rust_stages), python_headers


def test_rust_diagnostic_delay_stages_are_benchmark_headers() -> None:
    rust_stages, python_headers = _assert_diagnostic_stage_correspondence(
        CORE_MAIN.read_text(),
        TOOL.read_text(),
    )

    assert rust_stages <= python_headers


def test_stage_correspondence_controls_name_both_files() -> None:
    rust_source = CORE_MAIN.read_text()
    python_source = TOOL.read_text()
    renamed_rust = rust_source.replace(
        'diagnostic_delay("analysis");',
        'diagnostic_delay("analysis_renamed");',
        1,
    )
    with pytest.raises(
        AssertionError,
        match=(
            r"apps/cored/src/main\.rs:\d+: diagnostic_delay stage "
            r"'analysis_renamed' is absent from "
            r"tools/benchmark_view\.py:\d+: DIAGNOSTIC_HEADERS"
        ),
    ):
        _assert_diagnostic_stage_correspondence(
            renamed_rust,
            python_source,
        )

    deleted_python = python_source.replace(
        '    "analysis": "x-intel-view-stage-analysis-us",\n',
        "",
        1,
    )
    with pytest.raises(
        AssertionError,
        match=(
            r"apps/cored/src/main\.rs:\d+: diagnostic_delay stage "
            r"'analysis' is absent from "
            r"tools/benchmark_view\.py:\d+: DIAGNOSTIC_HEADERS"
        ),
    ):
        _assert_diagnostic_stage_correspondence(
            rust_source,
            deleted_python,
        )


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


def test_diagnostic_delay_warning_control_can_fail(tmp_path: Path) -> None:
    first = tmp_path / "first.log"
    second = tmp_path / "second.log"
    warning = (
        'WARNING: /view diagnostic delay configured: '
        'CORE_VIEW_DIAGNOSTIC_DELAY_STAGE="analysis"; '
        'CORE_VIEW_DIAGNOSTIC_DELAY_MS="100"; '
        "configured delay=100 ms (maximum 10000 ms)\n"
    )
    first.write_text(warning)
    second.write_text(warning)
    assert (
        verify_diagnostic_delay_warnings(
            [first, second],
            stage="analysis",
            delay_ms=100,
        )
        == 2
    )

    second.write_text(warning.replace("maximum 10000 ms", "maximum unknown"))
    with pytest.raises(BenchmarkFailure, match="maximum 10000 ms"):
        verify_diagnostic_delay_warnings(
            [first, second],
            stage="analysis",
            delay_ms=100,
        )


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
