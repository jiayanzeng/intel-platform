#!/usr/bin/env python3
"""Verify that cycle identity, runbook lifecycle, and tool targets agree."""

from __future__ import annotations

import datetime as dt
import re
import subprocess
import sys
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools.audit_deferred import progress_paths as deferred_progress_paths
from tools.cycle_identity import CycleIdentityError, resolve_cycle
from tools.progress_check import default_progress_path


ROOT = Path(__file__).resolve().parents[1]
CHECKED_RE = re.compile(r"^- \[x\] ", re.MULTILINE)
UNCHECKED_RE = re.compile(r"^- \[ \] ", re.MULTILINE)
CLOSING_HEADING = "## Cycle closing record"
DATE_RE = re.compile(
    r"^- \*\*Cycle closed:\*\* ([0-9]{4}-[0-9]{2}-[0-9]{2})$",
    re.MULTILINE,
)
DISPOSITION_RE = re.compile(
    r"^- \*\*Release disposition:\*\* (release|no-release)$",
    re.MULTILINE,
)
RELEASE_RE = re.compile(r"^- \*\*Release:\*\* (`?)([^`\n]+)\1$", re.MULTILINE)
RELEASE_COMMIT_RE = re.compile(
    r"^- \*\*Release commit:\*\* `([0-9a-f]{40})`$", re.MULTILINE
)
TAG_OBJECT_RE = re.compile(
    r"^- \*\*Annotated tag object:\*\* `([0-9a-f]{40})`$", re.MULTILINE
)
COMMIT_RE = re.compile(r"`([0-9a-f]{40})`")
HISTORICAL_BANNER_RE = re.compile(
    r"^> \*\*(?:Superseded-cycle status|Closed-cycle status correction) — "
    r"[0-9]{4}-[0-9]{2}-[0-9]{2}\.\*\*",
    re.MULTILINE,
)
AUTHORITY_PATTERNS = (
    "This document is the authoritative task list",
    "This is the active runbook",
    "Task work for this cycle is ordered",
)
CONTRACT_CYCLE_PATH_RE = re.compile(
    r"\b(?:TASKS-v[0-9]+(?:\.[0-9]+)*-EXECUTION\.md"
    r"|PROGRESS-v[0-9]+(?:\.[0-9]+)*\.md)\b"
)


def shown(path: Path, root: Path) -> str:
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)


def strip_corrections(text: str) -> str:
    return re.sub(
        r"~~.*?~~",
        lambda match: "\n" * match.group(0).count("\n"),
        text,
        flags=re.DOTALL,
    )


def git_output(root: Path, *args: str) -> str | None:
    result = subprocess.run(
        ["git", *args],
        cwd=root,
        check=False,
        text=True,
        capture_output=True,
    )
    if result.returncode != 0:
        return None
    return result.stdout.strip()


def valid_iso_date(raw: str) -> bool:
    try:
        return dt.date.fromisoformat(raw).isoformat() == raw
    except ValueError:
        return False


def exactly_one(
    pattern: re.Pattern[str],
    text: str,
    path: Path,
    root: Path,
    label: str,
    errors: list[str],
) -> re.Match[str] | None:
    matches = list(pattern.finditer(text))
    if len(matches) != 1:
        errors.append(
            f"{shown(path, root)}: closing record must contain exactly one "
            f"{label}; found {len(matches)}"
        )
        return None
    return matches[0]


def check_release_record(
    path: Path,
    section: str,
    root: Path,
    checked: int,
    errors: list[str],
) -> None:
    date_match = exactly_one(
        DATE_RE, section, path, root, "cycle-close date", errors
    )
    if date_match is not None and not valid_iso_date(date_match.group(1)):
        errors.append(
            f"{shown(path, root)}: invalid cycle-close date "
            f"{date_match.group(1)!r}"
        )

    disposition_match = exactly_one(
        DISPOSITION_RE, section, path, root, "release disposition", errors
    )
    if disposition_match is None:
        return

    disposition = disposition_match.group(1)
    if disposition == "release":
        release_match = exactly_one(
            RELEASE_RE, section, path, root, "release tag", errors
        )
        commit_match = exactly_one(
            RELEASE_COMMIT_RE,
            section,
            path,
            root,
            "release commit",
            errors,
        )
        tag_match = exactly_one(
            TAG_OBJECT_RE,
            section,
            path,
            root,
            "annotated tag object",
            errors,
        )
        if release_match is None or commit_match is None or tag_match is None:
            return
        release = release_match.group(2)
        commit = commit_match.group(1)
        tag_object = tag_match.group(1)
        resolved_tag = git_output(root, "rev-parse", release)
        resolved_commit = git_output(root, "rev-parse", f"{release}^{{}}")
        object_type = git_output(root, "cat-file", "-t", tag_object)
        commit_type = git_output(root, "cat-file", "-t", commit)
        if resolved_tag != tag_object or object_type != "tag":
            errors.append(
                f"{shown(path, root)}: annotated tag {release!r} does not "
                f"resolve to recorded tag object {tag_object}"
            )
        if resolved_commit != commit or commit_type != "commit":
            errors.append(
                f"{shown(path, root)}: release {release!r} does not "
                f"dereference to recorded commit {commit}"
            )
        return

    if "Intentionally unreleased implementation commits:" not in section:
        errors.append(
            f"{shown(path, root)}: no-release record does not name its "
            "intentionally unreleased implementation commits"
        )
    commits = COMMIT_RE.findall(section)
    if len(commits) < checked:
        errors.append(
            f"{shown(path, root)}: no-release record names {len(commits)} "
            f"commit(s) for {checked} checked task(s)"
        )
    for commit in commits:
        if git_output(root, "cat-file", "-t", commit) != "commit":
            errors.append(
                f"{shown(path, root)}: recorded no-release commit {commit} "
                "is not a commit object"
            )


def check_closed_execution(
    path: Path, text: str, root: Path, errors: list[str]
) -> None:
    checked = len(CHECKED_RE.findall(text))
    unchecked = len(UNCHECKED_RE.findall(text))
    if unchecked:
        errors.append(
            f"{shown(path, root)}: closed runbook has {unchecked} unchecked "
            "box(es)"
        )
    if text.count(CLOSING_HEADING) != 1:
        errors.append(
            f"{shown(path, root)}: closed runbook must have exactly one "
            f"{CLOSING_HEADING!r}; found {text.count(CLOSING_HEADING)}"
        )
        return
    section = text.split(CLOSING_HEADING, 1)[1]
    check_release_record(path, section, root, checked, errors)


def check_authority(
    path: Path, text: str, root: Path, errors: list[str]
) -> None:
    for number, line in enumerate(strip_corrections(text).splitlines(), 1):
        for phrase in AUTHORITY_PATTERNS:
            if phrase in line:
                errors.append(
                    f"{shown(path, root)}:{number}: inactive task file retains "
                    f"present-tense authority claim {phrase!r}"
                )


def check_contract_cycle_paths(
    identity,
    root: Path,
    errors: list[str],
) -> None:
    path = identity.declaration
    lines = path.read_text().splitlines()
    section_zero = next(
        (
            number
            for number, line in enumerate(lines, 1)
            if line.startswith("## 0.")
        ),
        None,
    )
    if section_zero is None:
        errors.append(
            f"{shown(path, root)}: missing §0 boundary after active-cycle "
            "declaration"
        )
        return
    allowed = {identity.runbook.name, identity.progress.name}
    for number, line in enumerate(lines, 1):
        for match in CONTRACT_CYCLE_PATH_RE.finditer(line):
            literal = match.group(0)
            if number < section_zero and literal in allowed:
                continue
            kind = "task" if literal.startswith("TASKS-") else "progress"
            errors.append(
                f"{shown(path, root)}:{number}: stale/cycle-specific {kind} "
                f"path {literal!r} appears outside the active declaration"
            )


def run(root: Path = ROOT) -> int:
    root = root.resolve()
    errors: list[str] = []
    try:
        identity = resolve_cycle(root)
    except CycleIdentityError as error:
        print(f"cycle-check: ERROR: {error}", file=sys.stderr)
        return 1
    check_contract_cycle_paths(identity, root, errors)

    for required in (identity.runbook, identity.progress):
        if not required.is_file():
            errors.append(
                f"{shown(required, root)}: declared {identity.name} target "
                "does not exist"
            )

    execution_files = sorted(root.glob("TASKS-v*-EXECUTION.md"))
    active_state = "missing"
    if identity.runbook.is_file():
        active_text = identity.runbook.read_text()
        unchecked = len(UNCHECKED_RE.findall(active_text))
        closing = active_text.count(CLOSING_HEADING)
        if unchecked >= 1 and closing == 0:
            active_state = "open"
        elif unchecked == 0 and closing == 1:
            active_state = "closed"
            check_closed_execution(identity.runbook, active_text, root, errors)
        elif unchecked < 1:
            errors.append(
                f"{shown(identity.runbook, root)}: declared runbook must be "
                "open with at least one unchecked box or carry one valid "
                "closing record"
            )
        if closing and unchecked:
            errors.append(
                f"{shown(identity.runbook, root)}: declared runbook cannot "
                f"mix unchecked boxes with {CLOSING_HEADING!r}"
            )

    for path in execution_files:
        if path == identity.runbook:
            continue
        text = path.read_text()
        check_closed_execution(path, text, root, errors)
        check_authority(path, text, root, errors)

    plain_task_files = sorted(
        path
        for path in root.glob("TASKS-v*.md")
        if not path.name.endswith("-EXECUTION.md")
    )
    for path in plain_task_files:
        text = path.read_text()
        if HISTORICAL_BANNER_RE.search(text) is None:
            errors.append(
                f"{shown(path, root)}: inactive task rationale lacks a "
                "dated superseded/closed-cycle banner"
            )
        check_authority(path, text, root, errors)

    progress_target = default_progress_path(root)
    if progress_target != identity.progress:
        errors.append(
            f"{shown(Path(__file__).resolve().parent / 'progress_check.py', root)}: "
            f"default resolves to {shown(progress_target, root)}, not declared "
            f"{shown(identity.progress, root)}"
        )

    deferred_targets = deferred_progress_paths(root)
    expected_deferred = sorted(root.glob("PROGRESS-v*.md"))
    if deferred_targets != expected_deferred:
        errors.append(
            f"{shown(Path(__file__).resolve().parent / 'audit_deferred.py', root)}: "
            "deferred-audit progress inputs are not the complete progress glob"
        )
    if identity.progress not in deferred_targets:
        errors.append(
            f"{shown(Path(__file__).resolve().parent / 'audit_deferred.py', root)}: "
            f"inputs omit declared {shown(identity.progress, root)}"
        )

    if errors:
        for error in errors:
            print(f"cycle-check: ERROR: {error}", file=sys.stderr)
        print(
            f"cycle-check: FAIL ({len(errors)} defect(s))", file=sys.stderr
        )
        return 1

    closed = len(execution_files) - (active_state == "open")
    print(
        f"cycle-check: PASS (active={identity.name}, "
        f"state={active_state}, "
        f"runbook={shown(identity.runbook, root)}, "
        f"progress={shown(identity.progress, root)}, "
        f"closed_execution={closed}, historical={len(plain_task_files)})"
    )
    return 0


def main() -> int:
    if len(sys.argv) != 1:
        print("usage: python3 -m tools.cycle_check", file=sys.stderr)
        return 2
    return run()


if __name__ == "__main__":
    raise SystemExit(main())
