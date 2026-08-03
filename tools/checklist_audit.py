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
# Invariant R13 control site: bold and plain checked task boxes.
CHECKED_RE = re.compile(
    r"^- \[x\] (?:\*\*([^*]+)\*\*(?: — .*)?|(.+))$"
)
UNCHECKED_RE = re.compile(
    r"^- \[ \] (?:\*\*([^*]+)\*\*(?: — .*)?|(.+))$"
)
STEP_HEADING_RE = re.compile(
    r"^## (?P<full>Step (?P<number>[0-9]+[A-Z]?) · (?P<title>.+))$"
)
TRAILING_ROLE_MARKERS_RE = re.compile(
    r"(?:\s*(?:[🤖🧑✅+]|DONE))+\s*$"
)
TRAILING_ANNOTATION_RE = re.compile(r"\s+\([^()]*\)$")
DRAFT_RUNBOOK_RE = re.compile(
    r"^Draft `TASKS-(v[0-9]+(?:\.[0-9]+)*)-EXECUTION\.md`$"
)
RUNBOOK_VERSION_RE = re.compile(
    r"^TASKS-v([0-9]+(?:\.[0-9]+)*)-EXECUTION\.md$"
)
HEADER_RE = re.compile(
    r"^### ([0-9]{4}-[0-9]{2}-[0-9]{2}) · (.+?) — (.+)$"
)
COMMIT_RE = re.compile(r"^[0-9a-f]{7,40}$")
RUNBOOK_FIELD_RE = re.compile(r"^- runbook: `?([^`]+)`?$")


@dataclass(frozen=True)
class Box:
    task_id: str
    line: int
    checked: bool
    bold: bool


@dataclass(frozen=True)
class Step:
    task_id: str
    aliases: frozenset[str]
    line: int
    end_line: int


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


def runbook_version(path: Path) -> tuple[int, ...]:
    match = RUNBOOK_VERSION_RE.fullmatch(path.name)
    if match is None:
        raise ValueError(f"not an execution runbook: {path.name}")
    return tuple(int(part) for part in match.group(1).split("."))


def _box_from_match(
    match: re.Match[str], number: int, checked: bool
) -> Box:
    bold = match.group(1) is not None
    raw = match.group(1) if bold else match.group(2)
    assert raw is not None
    return Box(normalize_task_id(raw), number, checked, bold)


def task_boxes(path: Path) -> list[Box]:
    boxes: list[Box] = []
    for number, line in enumerate(path.read_text().splitlines(), 1):
        if (match := CHECKED_RE.fullmatch(line)) is not None:
            boxes.append(_box_from_match(match, number, True))
        elif (match := UNCHECKED_RE.fullmatch(line)) is not None:
            boxes.append(_box_from_match(match, number, False))
    return boxes


def checked_boxes(path: Path) -> list[Box]:
    return [box for box in task_boxes(path) if box.checked]


def derived_steps(path: Path) -> list[Step]:
    lines = path.read_text().splitlines()
    level_two = [
        index + 1 for index, line in enumerate(lines) if line.startswith("## ")
    ]
    steps: list[Step] = []
    for number, line in enumerate(lines, 1):
        match = STEP_HEADING_RE.fullmatch(line)
        if match is None:
            continue
        raw = TRAILING_ROLE_MARKERS_RE.sub("", match.group("full")).strip()
        full_task_id = normalize_task_id(raw)
        label = full_task_id.split(" · ", 1)[1]
        while TRAILING_ANNOTATION_RE.search(label) is not None:
            label = TRAILING_ANNOTATION_RE.sub("", label).strip()
        aliases = {full_task_id, label}
        if (draft := DRAFT_RUNBOOK_RE.fullmatch(label)) is not None:
            aliases.add(draft.group(1))
        end_line = next(
            (heading for heading in level_two if heading > number),
            len(lines) + 1,
        )
        steps.append(
            Step(
                task_id=full_task_id,
                aliases=frozenset(aliases),
                line=number,
                end_line=end_line,
            )
        )
    return steps


def derived_task_box_lines(
    path: Path,
    boxes: list[Box],
    steps: list[Step],
    errors: list[str],
) -> set[int]:
    selected: set[int] = set()
    for step in steps:
        section = [
            box
            for box in boxes
            if step.line < box.line < step.end_line
        ]
        candidates = section or [
            box for box in boxes if box.task_id in step.aliases
        ]
        # Invariant R13 control site: derived step-to-box coverage.
        if len(candidates) != 1:
            detail = "no" if not candidates else f"{len(candidates)}"
            errors.append(
                f"{path.name}:{step.line}: derived step {step.task_id!r} "
                f"has {detail} task box; expected exactly one"
            )
            continue
        selected.add(candidates[0].line)
    return selected


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
    qualification_required: bool,
) -> tuple[str | None, list[str]]:
    same_id = [entry for entry in entries if entry.task_id == box.task_id]
    qualified = [
        entry for entry in same_id if entry.runbook == runbook.name
    ]
    # Invariant R13 control site: forward runbook qualification.
    if qualification_required and not qualified:
        return None, [
            f"{runbook.name}:{box.line}: checked box {box.task_id!r} requires "
            f"one runbook-qualified entry in {progress.name}"
        ]
    candidates = qualified or [
        entry for entry in same_id if entry.runbook is None
    ]
    # Invariant R13 control site: progress-entry correspondence.
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
    parsed: dict[Path, tuple[Path | None, list[Entry], list[Box], list[Step]]] = {}
    plain_task_box_runbooks: list[Path] = []
    for runbook in runbooks:
        progress = progress_for_runbook(root, runbook)
        entries = progress_entries(progress) if progress is not None else []
        boxes = task_boxes(runbook)
        steps = derived_steps(runbook)
        coverage_errors: list[str] = []
        derived_lines = derived_task_box_lines(
            runbook,
            boxes,
            steps,
            coverage_errors,
        )
        errors.extend(coverage_errors)
        declared_ids = {
            task_id
            for named_runbook, task_id in set(exemption_map) | set(retraction_map)
            if named_runbook == runbook.name
        }
        progress_ids = {entry.task_id for entry in entries}
        selected = [
            box
            for box in boxes
            if box.line in derived_lines
            or box.task_id in progress_ids
            or box.task_id in declared_ids
        ]
        if any(not box.bold for box in selected):
            plain_task_box_runbooks.append(runbook)
        parsed[runbook] = (progress, entries, selected, steps)

    # The first execution runbook that uses a plain task-box form establishes a
    # forward-only qualification epoch. The boundary is derived from the corpus,
    # not a declared cycle list or minimum version. This keeps immutable earlier
    # records under their original contract while preventing a new unqualified
    # namespace from silently depending on entry order.
    qualification_epoch = (
        min(runbook_version(path) for path in plain_task_box_runbooks)
        if plain_task_box_runbooks
        else None
    )

    for runbook in runbooks:
        progress, entries, all_selected_boxes, steps = parsed[runbook]
        boxes = [box for box in all_selected_boxes if box.checked]
        total_checked += len(boxes)
        if progress is None:
            errors.append(
                f"{runbook.name}: cannot resolve a progress log from its cycle"
            )
            print(
                f"checklist-audit: {runbook.name} steps={len(steps)} "
                f"task_boxes={len(all_selected_boxes)} checked={len(boxes)} "
                "entries_matched=0 commits_resolved=0 exemptions=0 "
                "retractions=0 progress=missing"
            )
            continue
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
                root,
                runbook,
                progress,
                entries,
                box,
                qualification_epoch is not None
                and runbook_version(runbook) >= qualification_epoch,
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
            f"checklist-audit: {runbook.name} steps={len(steps)} "
            f"task_boxes={len(all_selected_boxes)} checked={len(boxes)} "
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
