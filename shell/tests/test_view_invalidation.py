from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TOOL = ROOT / "tools" / "view_invalidation.py"


def _run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(TOOL), "control", *args],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )


def test_candidate_key_detects_every_required_input() -> None:
    result = _run()

    assert result.returncode == 0, result.stdout + result.stderr
    assert "PASS (9/9 invalidation inputs detected)" in result.stdout


def test_key_that_omits_embeddings_fails_the_control() -> None:
    result = _run("--omit-component", "embeddings")

    assert result.returncode != 0
    assert "embedding-write: STALE-RESULT RISK" in result.stdout
    assert "view-key control: FAIL: missed embedding-write" in result.stdout
