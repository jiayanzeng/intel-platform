#!/usr/bin/env python3
"""Resolve every checked execution-runbook task to progress and a Git commit."""

from __future__ import annotations

import datetime as dt
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools.cycle_identity import execution_runbooks, progress_for_runbook


ROOT = Path(__file__).resolve().parents[1]
EXEMPTIONS_FILE = Path("config/checklist-exemptions.json")
RETRACTIONS_FILE = Path("config/checklist-retractions.json")
CHECKED_RE = re.compile(r"^- \[x\] \*\*([^*]+)\*\*")
HEADER_RE = re.compile(
    r"^### ([0-9]{4}-[0-9]{2}-[0-9]{2}) · (.+?) — (.+)$"
)
COMMIT_RE = re.compile(r"^[0-9a-f]{7,40}$")
RUNBOOK_FIELD_RE = re.compile(r"^- runbook: `?([^`]+)`?$")


@dataclass(frozen=True)
class Box:
    task_id: str
    line: int


@dataclass(frozen=True)
class Entry:
    task_id: str
    line: int
    lines: list[str]
    runbook: str | None


@dataclass(frozen=True)
class Exemption:
    runbook: str
    task_id: str
    date: str
    reason: str
    accepted_by: str


@dataclass(frozen=True)
class Retraction:
    runbook: str
    task_id: str
    date: str
    reason: str
    accepted_by: str
    corrected_by: str


def normalize_task_id(raw: str) -> str:
    return raw.split(" — ", 1)[0].strip()


def checked_boxes(path: Path) -> list[Box]:
    boxes: list[Box] = []
    for number, line in enumerate(path.read_text().splitlines(), 1):
        match = CHECKED_RE.match(line)
        if match is not None:
            boxes.append(Box(normalize_task_id(match.group(1)), number))
    return boxes


def progress_entries(path: Path) -> list[Entry]:
    lines = path.read_text().splitlines()
    headers = [
        (index, match)
        for index, line in enumerate(lines)
        if (match := HEADER_RE.fullmatch(line)) is not None
    ]
    entries: list[Entry] = []
    for position, (index, match) in enumerate(headers):
        end = headers[position + 1][0] if position + 1 < len(headers) else len(lines)
        section = lines[index + 1 : end]
        runbooks = [
            field.group(1)
            for line in section
            if (field := RUNBOOK_FIELD_RE.fullmatch(line)) is not None
        ]
        entries.append(
            Entry(
                task_id=normalize_task_id(match.group(2)),
                line=index + 1,
                lines=section,
                runbook=runbooks[0] if len(runbooks) == 1 else None,
            )
        )
    return entries


def commit_exists(root: Path, commit: str) -> bool:
    result = subprocess.run(
        ["git", "cat-file", "-e", f"{commit}^{{commit}}"],
        cwd=root,
        check=False,
        capture_output=True,
    )
    return result.returncode == 0


def entry_commit(
    root: Path, progress: Path, entry: Entry
) -> tuple[str | None, str]:
    fields = [
        line.removeprefix("- commit:").strip()
        for line in entry.lines
        if line.startswith("- commit:")
    ]
    location = f"{progress.name}:{entry.line}"
    if len(fields) != 1:
        return None, (
            f"{location}: entry {entry.task_id!r} must contain exactly one "
            f"'- commit:' line; found {len(fields)}"
        )
    commit = fields[0]
    if COMMIT_RE.fullmatch(commit) is None:
        return None, (
            f"{location}: entry {entry.task_id!r} has non-hash commit "
            f"value {commit!r}"
        )
    if not commit_exists(root, commit):
        return None, (
            f"{location}: entry {entry.task_id!r} names non-existent "
            f"commit {commit}"
        )
    return commit, ""


def exact_object(
    raw: Any, expected: set[str], location: str, errors: list[str]
) -> dict[str, Any] | None:
    if not isinstance(raw, dict):
        errors.append(f"{location}: expected an object")
        return None
    keys = set(raw)
    if keys != expected:
        errors.append(
            f"{location}: expected keys {sorted(expected)}, found {sorted(keys)}"
        )
        return None
    return raw


def valid_date(raw: Any) -> bool:
    if not isinstance(raw, str):
        return False
    try:
        return dt.date.fromisoformat(raw).isoformat() == raw
    except ValueError:
        return False


def load_exemptions(root: Path, errors: list[str]) -> list[Exemption]:
    path = root / EXEMPTIONS_FILE
    try:
        raw = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as error:
        errors.append(f"{EXEMPTIONS_FILE}: {error}")
        return []
    record = exact_object(
        raw,
        {"schema_version", "record_date", "accepted_by", "exemptions"},
        str(EXEMPTIONS_FILE),
        errors,
    )
    if record is None:
        return []
    if record["schema_version"] != 1:
        errors.append(f"{EXEMPTIONS_FILE}: schema_version must be 1")
    if not valid_date(record["record_date"]):
        errors.append(f"{EXEMPTIONS_FILE}: record_date must be an ISO date")
    if not isinstance(record["accepted_by"], str) or not record["accepted_by"]:
        errors.append(f"{EXEMPTIONS_FILE}: accepted_by must be non-empty")
    raw_items = record["exemptions"]
    if not isinstance(raw_items, list):
        errors.append(f"{EXEMPTIONS_FILE}: exemptions must be a list")
        return []

    exemptions: list[Exemption] = []
    seen: set[tuple[str, str]] = set()
    expected = {"runbook", "task_id", "date", "reason", "accepted_by"}
    for index, raw_item in enumerate(raw_items):
        location = f"{EXEMPTIONS_FILE}:exemptions[{index}]"
        item = exact_object(raw_item, expected, location, errors)
        if item is None:
            continue
        if not valid_date(item["date"]):
            errors.append(f"{location}: date must be an ISO date")
            continue
        if any(
            not isinstance(item[field], str) or not item[field]
            for field in ("runbook", "task_id", "reason", "accepted_by")
        ):
            errors.append(f"{location}: string fields must be non-empty")
            continue
        key = (item["runbook"], item["task_id"])
        if key in seen:
            errors.append(
                f"{location}: duplicate exemption for {key[0]} {key[1]}"
            )
            continue
        seen.add(key)
        exemptions.append(
            Exemption(
                runbook=item["runbook"],
                task_id=item["task_id"],
                date=item["date"],
                reason=item["reason"],
                accepted_by=item["accepted_by"],
            )
        )
    return exemptions


def load_retractions(root: Path, errors: list[str]) -> list[Retraction]:
    path = root / RETRACTIONS_FILE
    try:
        raw = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as error:
        errors.append(f"{RETRACTIONS_FILE}: {error}")
        return []
    record = exact_object(
        raw,
        {"schema_version", "record_date", "accepted_by", "retractions"},
        str(RETRACTIONS_FILE),
        errors,
    )
    if record is None:
        return []
    if record["schema_version"] != 1:
        errors.append(f"{RETRACTIONS_FILE}: schema_version must be 1")
    if not valid_date(record["record_date"]):
        errors.append(f"{RETRACTIONS_FILE}: record_date must be an ISO date")
    if not isinstance(record["accepted_by"], str) or not record["accepted_by"]:
        errors.append(f"{RETRACTIONS_FILE}: accepted_by must be non-empty")
    raw_items = record["retractions"]
    if not isinstance(raw_items, list):
        errors.append(f"{RETRACTIONS_FILE}: retractions must be a list")
        return []

    retractions: list[Retraction] = []
    seen: set[tuple[str, str]] = set()
    expected = {
        "runbook",
        "task_id",
        "date",
        "reason",
        "accepted_by",
        "corrected_by",
    }
    for index, raw_item in enumerate(raw_items):
        location = f"{RETRACTIONS_FILE}:retractions[{index}]"
        item = exact_object(raw_item, expected, location, errors)
        if item is None:
            continue
        if not valid_date(item["date"]):
            errors.append(f"{location}: date must be an ISO date")
            continue
        if any(
            not isinstance(item[field], str) or not item[field]
            for field in (
                "runbook",
                "task_id",
                "reason",
                "accepted_by",
                "corrected_by",
            )
        ):
            errors.append(f"{location}: string fields must be non-empty")
            continue
        key = (item["runbook"], item["task_id"])
        if key in seen:
            errors.append(
                f"{location}: duplicate retraction for {key[0]} {key[1]}"
            )
            continue
        seen.add(key)
        retractions.append(Retraction(**item))
    return retractions


def matching_commit(
    root: Path,
    runbook: Path,
    progress: Path,
    entries: list[Entry],
    box: Box,
) -> tuple[str | None, list[str]]:
    same_id = [entry for entry in entries if entry.task_id == box.task_id]
    qualified = [
        entry for entry in same_id if entry.runbook == runbook.name
    ]
    candidates = qualified or [
        entry for entry in same_id if entry.runbook is None
    ]
    if not candidates:
        return None, [
            f"{runbook.name}:{box.line}: checked box {box.task_id!r} has no "
            f"matching entry in {progress.name}"
        ]

    valid: list[tuple[Entry, str]] = []
    failures: list[str] = []
    for entry in candidates:
        commit, failure = entry_commit(root, progress, entry)
        if commit is None:
            failures.append(failure)
        else:
            valid.append((entry, commit))
    if qualified and len(valid) > 1:
        locations = ", ".join(
            f"{progress.name}:{entry.line}" for entry, _ in valid
        )
        return None, [
            f"{runbook.name}:{box.line}: checked box {box.task_id!r} has "
            f"multiple valid runbook-qualified entries: {locations}"
        ]
    if valid:
        return valid[0][1], []
    return None, failures


def run(root: Path = ROOT) -> int:
    root = root.resolve()
    errors: list[str] = []
    exemptions = load_exemptions(root, errors)
    retractions = load_retractions(root, errors)
    exemption_map = {
        (item.runbook, item.task_id): item for item in exemptions
    }
    retraction_map = {
        (item.runbook, item.task_id): item for item in retractions
    }
    for key in sorted(set(exemption_map) & set(retraction_map)):
        errors.append(
            f"{RETRACTIONS_FILE}: retraction also has an exemption: "
            f"{key[0]} {key[1]}"
        )
    seen_exemptions: set[tuple[str, str]] = set()
    seen_retractions: set[tuple[str, str]] = set()
    total_checked = 0
    total_matched = 0
    total_resolved = 0
    total_exempted = 0
    total_retracted = 0

    runbooks = execution_runbooks(root)
    for runbook in runbooks:
        boxes = checked_boxes(runbook)
        total_checked += len(boxes)
        progress = progress_for_runbook(root, runbook)
        if progress is None:
            errors.append(
                f"{runbook.name}: cannot resolve a progress log from its cycle"
            )
            continue
        entries = progress_entries(progress)
        matched = 0
        resolved = 0
        exempted = 0
        retracted = 0
        seen_ids: set[str] = set()
        for box in boxes:
            if box.task_id in seen_ids:
                errors.append(
                    f"{runbook.name}:{box.line}: duplicate checked task id "
                    f"{box.task_id!r}"
                )
                continue
            seen_ids.add(box.task_id)
            key = (runbook.name, box.task_id)
            commit, failures = matching_commit(
                root, runbook, progress, entries, box
            )
            exemption = exemption_map.get(key)
            retraction = retraction_map.get(key)
            if commit is not None:
                matched += 1
                resolved += 1
                if exemption is not None:
                    seen_exemptions.add(key)
                    errors.append(
                        f"{EXEMPTIONS_FILE}: false exemption for "
                        f"{runbook.name} {box.task_id}: commit {commit} "
                        "resolves cleanly"
                    )
                if retraction is not None:
                    seen_retractions.add(key)
                    retracted += 1
                continue
            if exemption is not None:
                seen_exemptions.add(key)
                exempted += 1
                continue
            errors.extend(failures)
        total_matched += matched
        total_resolved += resolved
        total_exempted += exempted
        total_retracted += retracted
        print(
            f"checklist-audit: {runbook.name} checked={len(boxes)} "
            f"entries_matched={matched} commits_resolved={resolved} "
            f"exemptions={exempted} retractions={retracted} "
            f"progress={progress.name}"
        )

    for key in sorted(exemption_map):
        if key not in seen_exemptions:
            errors.append(
                f"{EXEMPTIONS_FILE}: exemption names no checked box: "
                f"{key[0]} {key[1]}"
            )
    for key in sorted(retraction_map):
        if key not in seen_retractions:
            errors.append(
                f"{RETRACTIONS_FILE}: retraction names no resolved checked "
                f"box: {key[0]} {key[1]}"
            )

    if errors:
        for error in errors:
            print(f"checklist-audit: ERROR: {error}", file=sys.stderr)
        print(
            f"checklist-audit: FAIL ({len(errors)} defect(s))",
            file=sys.stderr,
        )
        return 1

    print(
        f"checklist-audit: PASS (checked={total_checked}, "
        f"retracted={total_retracted}, "
        f"entries_matched={total_matched}, commits_resolved={total_resolved}, "
        f"exemptions={total_exempted})"
    )
    return 0


def main() -> int:
    if len(sys.argv) != 1:
        print("usage: python3 tools/checklist_audit.py", file=sys.stderr)
        return 2
    return run()


if __name__ == "__main__":
    raise SystemExit(main())
