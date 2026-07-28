from __future__ import annotations

import os
import shlex
import subprocess
from pathlib import Path

from tools import invariant_scan


ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / "run"


def _control_script(tmp_path: Path, target: str) -> Path:
    text = RUN.read_text()
    function_header = f"{target}() {{\n"
    assert text.count(function_header) == 1
    text = text.replace(function_header, function_header + "  false\n", 1)
    text = text.replace(
        'cd "$(dirname "$0")"\n',
        f"cd {shlex.quote(str(ROOT))}\n",
        1,
    )
    dispatch = 'cmd="${1:-help}"; shift || true\n'
    assert text.count(dispatch) == 1
    text = text.replace(
        dispatch,
        """
if [ "${1:-}" = "__ci-local-control" ]; then
  control_target="${2:-}"
  CI_LOCAL_RESULTS=()
  ci_local_job "failure control: $control_target" "$control_target" || exit $?
  exit 0
fi
"""
        + dispatch,
        1,
    )
    script = tmp_path / f"run-{target}"
    script.write_text(text)
    return script


def test_every_derived_ci_local_job_propagates_its_first_failure(
    tmp_path: Path,
) -> None:
    jobs = invariant_scan.parse_ci_local_jobs(RUN.read_text())
    failures: list[str] = []
    for job in jobs:
        script = _control_script(tmp_path, job.target)
        result = subprocess.run(
            [
                "bash",
                "-euo",
                "pipefail",
                str(script),
                "__ci-local-control",
                job.target,
            ],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        output = result.stdout + result.stderr
        expected = f"FAIL  failure control: {job.target}"
        if result.returncode == 0 or expected not in output:
            failures.append(
                f"{job.label}|{job.target}: exit={result.returncode}; "
                f"expected={expected!r}; output={output!r}"
            )

    assert not failures, "\n".join(failures)
    help_result = subprocess.run(
        ["bash", str(RUN), "help"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=True,
    )
    assert (
        f"configured {len(jobs)}-job CI matrix, stopping on failure"
        in help_result.stdout
    )
    first_failure = subprocess.run(
        ["bash", str(_control_script(tmp_path, jobs[0].target)), "ci-local"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    first_output = first_failure.stdout + first_failure.stderr
    assert first_failure.returncode != 0
    assert f"FAIL  {jobs[0].label}" in first_output
    assert f"ci-local: {jobs[1].label}" not in first_output


def test_fingerprint_cleanup_preserves_the_validation_failure(
    tmp_path: Path,
) -> None:
    text = RUN.read_text()
    fixture_dir = tmp_path / "fingerprint-fixture"
    fixture_dir.mkdir()
    text = text.replace(
        'cd "$(dirname "$0")"\n',
        f"cd {shlex.quote(str(ROOT))}\n",
        1,
    )
    text = text.replace(
        '  fixture_dir="$(mktemp -d)"\n',
        '  fixture_dir="${FINGERPRINT_CONTROL_DIR:?}"\n',
        1,
    )
    validation = (
        "  cargo run --quiet -p intel-store --example fingerprint_fixture -- \\\n"
        '    "$fixture_db" || status=$?\n'
    )
    assert text.count(validation) == 1
    text = text.replace(validation, "  false || status=$?\n", 1)
    script = tmp_path / "run-fingerprint-cleanup"
    script.write_text(text)

    env = os.environ.copy()
    env["FINGERPRINT_CONTROL_DIR"] = str(fixture_dir)
    result = subprocess.run(
        [
            "bash",
            "-euo",
            "pipefail",
            str(script),
            "__ci-local-job",
            "verify_fingerprint_fixture",
        ],
        cwd=ROOT,
        env=env,
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode != 0
    assert not fixture_dir.exists()
