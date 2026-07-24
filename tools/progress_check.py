#!/usr/bin/env python3
"""Validate the newest append-only progress entry."""

from __future__ import annotations

import datetime as dt
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PROGRESS = ROOT / "PROGRESS-v0.8.md"
HEADER_RE = re.compile(
    r"^### ([0-9]{4}-[0-9]{2}-[0-9]{2}) · ([^·\n]+?) — (.+)$"
)
COMMIT_RE = re.compile(r"^[0-9a-f]{7,40}$")


def fail(path: Path, line: int, message: str) -> int:
    try:
        shown = path.relative_to(ROOT)
    except ValueError:
        shown = path
    print(f"progress-check: ERROR: {shown}:{line}: {message}", file=sys.stderr)
    return 1


def parse_date(path: Path, line: int, raw: str) -> dt.date | None:
    try:
        parsed = dt.date.fromisoformat(raw)
    except ValueError:
        return None
    if parsed.isoformat() != raw:
        return None
    return parsed


def commit_exists(commit: str) -> bool:
    checked = subprocess.run(
        ["git", "cat-file", "-e", f"{commit}^{{commit}}"],
        cwd=ROOT,
        check=False,
        capture_output=True,
    )
    return checked.returncode == 0


def check(path: Path) -> int:
    try:
        lines = path.read_text().splitlines()
    except OSError as error:
        print(f"progress-check: ERROR: {error}", file=sys.stderr)
        return 1

    headers = [
        (index, line)
        for index, line in enumerate(lines)
        if line.startswith("### ") and not line.startswith("### <date>")
    ]
    if len(headers) < 2:
        return fail(path, 1, "expected at least two dated progress entries")

    latest_index, latest_header = headers[-1]
    latest_match = HEADER_RE.fullmatch(latest_header)
    if latest_match is None:
        return fail(
            path,
            latest_index + 1,
            "newest header must match '### <ISO date> · <task id> — <text>'",
        )
    latest_date = parse_date(path, latest_index + 1, latest_match.group(1))
    if latest_date is None:
        return fail(path, latest_index + 1, "newest header has an invalid ISO date")

    previous_index, previous_header = headers[-2]
    previous_match = HEADER_RE.fullmatch(previous_header)
    if previous_match is None:
        return fail(
            path,
            previous_index + 1,
            "previous header does not match the progress-entry format",
        )
    previous_date = parse_date(path, previous_index + 1, previous_match.group(1))
    if previous_date is None:
        return fail(path, previous_index + 1, "previous header has an invalid ISO date")
    if latest_date < previous_date:
        return fail(
            path,
            latest_index + 1,
            f"date {latest_date} precedes previous entry date {previous_date} "
            f"(line {previous_index + 1})",
        )

    section = lines[latest_index + 1 :]
    owners = [
        (latest_index + offset + 2, line.removeprefix("- owner:").strip())
        for offset, line in enumerate(section)
        if line.startswith("- owner:")
    ]
    if len(owners) != 1 or not owners[0][1]:
        return fail(
            path,
            latest_index + 1,
            f"newest entry must contain exactly one non-empty '- owner:' line; "
            f"found {len(owners)}",
        )

    commits = [
        (latest_index + offset + 2, line.removeprefix("- commit:").strip())
        for offset, line in enumerate(section)
        if line.startswith("- commit:")
    ]
    if len(commits) != 1:
        return fail(
            path,
            latest_index + 1,
            f"newest entry must contain exactly one '- commit:' line; "
            f"found {len(commits)}",
        )
    commit_line, commit = commits[0]
    if COMMIT_RE.fullmatch(commit) is None:
        return fail(
            path,
            commit_line,
            "commit must be 7-40 lowercase hexadecimal characters; "
            f"found {commit!r}",
        )
    if not commit_exists(commit):
        return fail(
            path,
            commit_line,
            f"commit {commit} is not a commit object in this repository",
        )

    print(
        "progress-check: PASS "
        f"({latest_match.group(1)} · {latest_match.group(2)} · {commit})"
    )
    return 0


def main() -> int:
    if len(sys.argv) > 2:
        print("usage: progress_check.py [progress-file]", file=sys.stderr)
        return 2
    path = Path(sys.argv[1]).resolve() if len(sys.argv) == 2 else DEFAULT_PROGRESS
    return check(path)


if __name__ == "__main__":
    raise SystemExit(main())
