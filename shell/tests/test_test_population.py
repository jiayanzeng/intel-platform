from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
import test_population  # noqa: E402


NODE = (
    "tests/test_deferred_audit.py::"
    "test_on_site_production_measurements_match_committed_receipt"
)
REASON = "on-site production audit requires protected corpora and built cored"


def local_summary() -> dict[str, object]:
    return {
        "schema_version": 1,
        "collected": 275,
        "passed": 275,
        "failed": 0,
        "on_site": [NODE],
        "skipped": [],
    }


def hosted_summary() -> dict[str, object]:
    return {
        "schema_version": 1,
        "collected": 275,
        "passed": 274,
        "failed": 0,
        "on_site": [NODE],
        "skipped": [
            {
                "node_id": NODE,
                "reason": REASON,
                "markers": ["on_site", "skipif"],
            }
        ],
    }


def compare(
    local: dict[str, object],
    hosted: dict[str, object],
) -> dict[str, object]:
    return test_population.compare_populations(
        test_population.parse_summary(local, "local"),
        test_population.parse_summary(hosted, "hosted"),
    )


def test_v023_population_is_equivalent_with_one_named_on_site_skip() -> None:
    result = compare(local_summary(), hosted_summary())

    assert result == {
        "collected": 275,
        "equivalent": True,
        "equivalent_passed": 275,
        "hosted": {
            "on_site_skipped": 1,
            "passed": 274,
            "skipped": [{"node_id": NODE, "reason": REASON}],
        },
        "local": {"passed": 275, "skipped": 0},
        "schema_version": 1,
    }


def test_fail_before_rejects_unmarked_hosted_skip() -> None:
    hosted = hosted_summary()
    hosted["skipped"][0]["markers"] = ["skipif"]  # type: ignore[index]

    with pytest.raises(test_population.PopulationError, match="not marked on_site"):
        compare(local_summary(), hosted)


def test_fail_before_rejects_collected_mismatch() -> None:
    hosted = hosted_summary()
    hosted["collected"] = 276
    hosted["passed"] = 275

    with pytest.raises(test_population.PopulationError, match="collected mismatch"):
        compare(local_summary(), hosted)


def test_fail_before_rejects_missing_skip_reason() -> None:
    hosted = hosted_summary()
    hosted["skipped"][0]["reason"] = ""  # type: ignore[index]

    with pytest.raises(test_population.PopulationError, match="reason must be present"):
        compare(local_summary(), hosted)


def test_v023_false_hosted_claim_is_rejected() -> None:
    result = compare(local_summary(), hosted_summary())

    with pytest.raises(test_population.PopulationError, match="claim mismatch"):
        test_population.verify_hosted_claim(result, 275, 0)


def test_v023_true_hosted_claim_is_accepted() -> None:
    result = compare(local_summary(), hosted_summary())

    test_population.verify_hosted_claim(result, 274, 1)


def test_cli_reads_prefixed_logs_and_prints_derived_result(
    tmp_path: Path,
) -> None:
    local = tmp_path / "local.log"
    hosted = tmp_path / "hosted.log"
    local.write_text(
        "pytest output\n"
        + test_population.SUMMARY_PREFIX
        + json.dumps(local_summary())
        + "\n"
    )
    hosted.write_text(
        "hosted output\n"
        + test_population.SUMMARY_PREFIX
        + json.dumps(hosted_summary())
        + "\n"
    )

    result = subprocess.run(
        [
            sys.executable,
            str(ROOT / "tools" / "test_population.py"),
            str(local),
            str(hosted),
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 0
    assert result.stderr == ""
    payload = json.loads(result.stdout.removeprefix(test_population.COMPARE_PREFIX))
    assert payload["equivalent"] is True
    assert payload["hosted"]["passed"] == 274
    assert payload["hosted"]["on_site_skipped"] == 1


def test_cli_rejects_false_recorded_claim(tmp_path: Path) -> None:
    local = tmp_path / "local.json"
    hosted = tmp_path / "hosted.json"
    local.write_text(json.dumps(local_summary()))
    hosted.write_text(json.dumps(hosted_summary()))

    result = subprocess.run(
        [
            sys.executable,
            str(ROOT / "tools" / "test_population.py"),
            str(local),
            str(hosted),
            "--claim-hosted-passed",
            "275",
            "--claim-hosted-skipped",
            "0",
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 1
    assert "claimed passed 275, skipped 0" in result.stderr
    assert "comparator derived passed 274, skipped 1" in result.stderr
