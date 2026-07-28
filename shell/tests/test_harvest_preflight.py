from __future__ import annotations

import os
import shlex
import subprocess
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / "run"
DISPATCH = 'cmd="${1:-help}"; shift || true\n'
PREFLIGHT = (
    '  step "artifact-integrity preflight — verify protected evidence bytes"\n'
    "  cmd_verify_artifacts\n"
)


def _control_script(tmp_path: Path, text: str, name: str) -> Path:
    assert text.count(DISPATCH) == 1
    text = text.replace(
        'cd "$(dirname "$0")"\n',
        f"cd {shlex.quote(str(ROOT))}\n",
        1,
    )
    control = r'''
if [ "${1:-}" = "__harvest-preflight-control" ]; then
  control_log="${HARVEST_CONTROL_LOG:?}"
  record_control() { printf '%s\n' "$1" >> "$control_log"; }
  cmd_verify_artifacts() {
    record_control "artifact-verification"
    return "${HARVEST_CONTROL_VERIFY_STATUS:-0}"
  }
  need_cargo() { record_control "cargo-check"; }
  ensure_venv() { record_control "python-environment"; }
  cored_debug_bin() { printf '/tmp/not-used-cored\n'; }
  harvest_db_path() { printf 'data/preflight-control.db\n'; }
  refuse_protected_harvest() {
    record_control "destination-protection"
    return 0
  }
  py() {
    record_control "reachability-probe"
    printf 'https://example.invalid/oai?verb=Identify\n'
  }
  curl() {
    record_control "network-request"
    printf '000'
  }
  cmd_harvest_arxiv
  exit $?
fi
'''
    text = text.replace(DISPATCH, control + DISPATCH, 1)
    script = tmp_path / f"run-{name}"
    script.write_text(text)
    return script


def _run_control(
    tmp_path: Path,
    text: str,
    name: str,
    *,
    verify_status: int = 0,
) -> tuple[subprocess.CompletedProcess[str], list[str]]:
    log = tmp_path / f"{name}.log"
    script = _control_script(tmp_path, text, name)
    env = os.environ.copy()
    env["ENV_FILE"] = str(tmp_path / "absent.env")
    env["HARVEST_CONTROL_LOG"] = str(log)
    env["HARVEST_CONTROL_VERIFY_STATUS"] = str(verify_status)
    result = subprocess.run(
        ["bash", "-euo", "pipefail", str(script), "__harvest-preflight-control"],
        cwd=ROOT,
        env=env,
        text=True,
        capture_output=True,
        check=False,
    )
    return result, log.read_text().splitlines()


def _assert_entry_point_order(events: list[str]) -> None:
    assert events == [
        "artifact-verification",
        "cargo-check",
        "python-environment",
        "destination-protection",
        "reachability-probe",
        "network-request",
    ], (
        "cmd_harvest_arxiv must verify protected artifact bytes before "
        "environment setup, destination protection, reachability, or harvest"
    )


def test_cmd_harvest_arxiv_enforces_artifact_preflight_before_network(
    tmp_path: Path,
) -> None:
    text = RUN.read_text()
    assert text.count(PREFLIGHT) == 1, (
        "cmd_harvest_arxiv must invoke its named artifact-integrity preflight"
    )
    assert "REFUSED: live harvest target" in text

    reached_probe, events = _run_control(tmp_path, text, "ordered")
    assert reached_probe.returncode == 2
    _assert_entry_point_order(events)

    failed_verify, failed_events = _run_control(
        tmp_path,
        text,
        "verification-failure",
        verify_status=37,
    )
    assert failed_verify.returncode == 37
    assert failed_events == ["artifact-verification"]

    without_preflight = text.replace(PREFLIGHT, "", 1)
    removed_result, removed_events = _run_control(
        tmp_path,
        without_preflight,
        "removed-preflight",
    )
    assert removed_result.returncode == 2
    with pytest.raises(AssertionError, match="cmd_harvest_arxiv"):
        _assert_entry_point_order(removed_events)
