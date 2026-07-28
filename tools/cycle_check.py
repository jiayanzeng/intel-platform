#!/usr/bin/env python3
"""Verify that cycle identity, runbook lifecycle, and tool targets agree."""

from __future__ import annotations

import argparse
import datetime as dt
import re
import subprocess
import sys
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools.audit_deferred import progress_paths as deferred_progress_paths
from tools.cycle_identity import (
    CycleIdentityError,
    historical_artifacts,
    resolve_cycle,
)
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
CYCLE_LITERAL_RE = re.compile(
    r"(?<![A-Za-z0-9_.-])v[0-9]+\.[0-9]+(?:\.[0-9]+)?"
    r"(?![A-Za-z0-9_.-])"
)
STEP_HEADING_RE = re.compile(r"^## Step ([0-9]+)\b[^\n]*$", re.MULTILINE)
DEFERRED_HEADING = "## Deferred means deferred"
MARKDOWN_TABLE_SEPARATOR_RE = re.compile(r"^:?-{3,}:?$")
STEP_REFERENCE_RE = re.compile(r"\bStep ([0-9]+)\b", re.IGNORECASE)
MEASURED_VALUE_TERM_RE = re.compile(
    r"\b(?:recorded|measured|stored)\b",
    re.IGNORECASE,
)
QUANTITY_TERM_RE = re.compile(
    r"\b(?:values?|counts?|numbers?|quantit(?:y|ies)|totals?)\b",
    re.IGNORECASE,
)
CRITERION_CLAUSE_RE = re.compile(r"[^.;\n·]+")
BOLD_BLOCK_RE = re.compile(
    r"^\*\*([^*\n]+)\*\*(.*?)"
    r"(?=^\*\*[^*\n]+\*\*|^## |\Z)",
    re.MULTILINE | re.DOTALL,
)
AMENDMENTS_HEADING = "## Runbook amendments"
AMENDMENT_ENTRY_RE = re.compile(
    r"^Step ([0-9]+) — .+ — ([0-9]{4}-[0-9]{2}-[0-9]{2})$",
    re.MULTILINE,
)
CONTRACT_FIELD_LABELS = {
    "Objective": "Objective",
    "Acceptance criteria": "Acceptance criteria",
    "Done when": "Done when",
}


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
    verify_local_tag_refs: bool = True,
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
        commit_type = git_output(root, "cat-file", "-t", commit)
        if commit_type != "commit":
            errors.append(
                f"{shown(path, root)}: recorded release commit {commit} "
                "is not a commit object"
            )
        if verify_local_tag_refs:
            resolved_tag = git_output(root, "rev-parse", release)
            resolved_commit = git_output(root, "rev-parse", f"{release}^{{}}")
            object_type = git_output(root, "cat-file", "-t", tag_object)
            if resolved_tag != tag_object or object_type != "tag":
                errors.append(
                    f"{shown(path, root)}: annotated tag {release!r} does not "
                    f"resolve to recorded tag object {tag_object}"
                )
            if resolved_commit != commit:
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
    path: Path,
    text: str,
    root: Path,
    errors: list[str],
    verify_local_tag_refs: bool = True,
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
    check_release_record(
        path,
        section,
        root,
        checked,
        errors,
        verify_local_tag_refs,
    )


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


def source_cycle_scan_paths(root: Path) -> list[Path]:
    paths = sorted((root / "tools").glob("*.py"))
    harness = root / "run"
    if harness.is_file():
        paths.append(harness)
    workflows = root / ".github" / "workflows"
    if workflows.is_dir():
        paths.extend(sorted(workflows.glob("*.yml")))
        paths.extend(sorted(workflows.glob("*.yaml")))
    return paths


def check_source_cycle_literals(root: Path, errors: list[str]) -> None:
    try:
        historical_artifacts(root)
    except CycleIdentityError as error:
        errors.append(str(error))
    for path in source_cycle_scan_paths(root):
        for number, line in enumerate(path.read_text().splitlines(), 1):
            matches = {
                match.group(0)
                for pattern in (CONTRACT_CYCLE_PATH_RE, CYCLE_LITERAL_RE)
                for match in pattern.finditer(line)
            }
            for literal in sorted(matches):
                errors.append(
                    f"{shown(path, root)}:{number}: cycle-specific literal "
                    f"{literal!r} must be derived from the active declaration "
                    "or historical registry"
                )


def runbook_contract_fields(text: str) -> dict[tuple[str, str], str]:
    headings = list(STEP_HEADING_RE.finditer(text))
    fields: dict[tuple[str, str], str] = {}
    for index, heading in enumerate(headings):
        step = heading.group(1)
        end = headings[index + 1].start() if index + 1 < len(headings) else len(text)
        section = text[heading.end():end]
        for block in BOLD_BLOCK_RE.finditer(section):
            raw_label = block.group(1).strip().removesuffix(".")
            label = CONTRACT_FIELD_LABELS.get(raw_label)
            if label is not None:
                fields[(step, label)] = block.group(2).strip()
    return fields


def first_committed_runbook_text(root: Path, path: Path) -> str | None:
    relative = shown(path, root)
    additions = git_output(
        root,
        "log",
        "--diff-filter=A",
        "--format=%H",
        "--",
        relative,
    )
    if not additions:
        return None
    first_commit = additions.splitlines()[-1]
    return git_output(root, "show", f"{first_commit}:{relative}")


def disclosed_amendment_steps(
    text: str,
    path: Path,
    root: Path,
    errors: list[str],
) -> set[str]:
    heading_matches = list(
        re.finditer(
            rf"^{re.escape(AMENDMENTS_HEADING)}$",
            text,
            re.MULTILINE,
        )
    )
    count = len(heading_matches)
    if count == 0:
        return set()
    if count != 1:
        errors.append(
            f"{shown(path, root)}: expected at most one "
            f"{AMENDMENTS_HEADING!r}; found {count}"
        )
        return set()
    section = text[heading_matches[0].end():]
    next_heading = re.search(r"^## ", section, re.MULTILINE)
    if next_heading is not None:
        section = section[: next_heading.start()]
    disclosed: set[str] = set()
    for match in AMENDMENT_ENTRY_RE.finditer(section):
        step, date = match.groups()
        if not valid_iso_date(date):
            errors.append(
                f"{shown(path, root)}: invalid runbook amendment date "
                f"{date!r}"
            )
            continue
        disclosed.add(step)
    return disclosed


def check_runbook_amendments(
    path: Path,
    text: str,
    root: Path,
    errors: list[str],
) -> None:
    original = first_committed_runbook_text(root, path)
    if original is None:
        if (root / ".git").exists():
            errors.append(
                f"{shown(path, root)}: cannot locate the runbook's first "
                "committed version for amendment disclosure"
            )
        return
    original_fields = runbook_contract_fields(original)
    current_fields = runbook_contract_fields(text)
    changed = {
        field
        for field in set(original_fields) | set(current_fields)
        if original_fields.get(field) != current_fields.get(field)
    }
    disclosed = disclosed_amendment_steps(text, path, root, errors)
    for step, label in sorted(changed, key=lambda item: (int(item[0]), item[1])):
        if step not in disclosed:
            errors.append(
                f"{shown(path, root)}: undisclosed runbook amendment: "
                f"Step {step} {label} differs from its first committed text"
            )


def markdown_table_cells(line: str) -> list[str]:
    stripped = line.strip()
    if not stripped.startswith("|") or not stripped.endswith("|"):
        return []
    return [cell.strip() for cell in stripped[1:-1].split("|")]


def normalized_table_cell(cell: str) -> str:
    return re.sub(r"\s+", " ", cell.replace("*", "").replace("`", "")).strip()


def check_active_deferral_assignments(
    path: Path,
    text: str,
    root: Path,
    errors: list[str],
) -> None:
    heading_matches = list(
        re.finditer(rf"^{re.escape(DEFERRED_HEADING)}$", text, re.MULTILINE)
    )
    if not heading_matches:
        return
    if len(heading_matches) != 1:
        errors.append(
            f"{shown(path, root)}: expected at most one "
            f"{DEFERRED_HEADING!r}; found {len(heading_matches)}"
        )
        return

    section_start = heading_matches[0].end()
    section = text[section_start:]
    next_heading = re.search(r"^## ", section, re.MULTILINE)
    if next_heading is not None:
        section = section[: next_heading.start()]

    lines = section.splitlines()
    header_index: int | None = None
    action_index: int | None = None
    for index, line in enumerate(lines):
        cells = markdown_table_cells(line)
        normalized = [normalized_table_cell(cell).casefold() for cell in cells]
        if "deferred item" not in normalized:
            continue
        header_index = index
        action_index = next(
            (
                cell_index
                for cell_index, cell in enumerate(normalized)
                if "action" in cell
            ),
            None,
        )
        break
    if header_index is None or action_index is None:
        errors.append(
            f"{shown(path, root)}: {DEFERRED_HEADING!r} must contain a "
            "markdown table with Deferred item and action columns"
        )
        return

    steps = set(STEP_HEADING_RE.findall(text))
    for offset, line in enumerate(lines[header_index + 1 :], header_index + 1):
        cells = markdown_table_cells(line)
        if not cells or action_index >= len(cells):
            continue
        normalized = [normalized_table_cell(cell) for cell in cells]
        if normalized and all(
            MARKDOWN_TABLE_SEPARATOR_RE.fullmatch(cell) for cell in normalized
        ):
            continue
        item = normalized[0] if normalized else "<unnamed>"
        action = normalized[action_index]
        if not action or action.casefold().startswith("none"):
            continue
        references = STEP_REFERENCE_RE.findall(action)
        line_number = (
            text[:section_start].count("\n")
            + offset
            + 1
        )
        if not references:
            errors.append(
                f"{shown(path, root)}:{line_number}: deferred row {item!r} "
                "has a non-none action but names no discharging Step N"
            )
            continue
        for step in references:
            if step not in steps:
                errors.append(
                    f"{shown(path, root)}:{line_number}: deferred row {item!r} "
                    f"names missing discharging Step {step}"
                )


def check_active_step_value_criteria(
    path: Path,
    text: str,
    root: Path,
    errors: list[str],
) -> None:
    """Heuristically reject cross-step stored quantities in acceptance text."""
    headings = list(STEP_HEADING_RE.finditer(text))
    for index, heading in enumerate(headings):
        current_step = heading.group(1)
        end = (
            headings[index + 1].start()
            if index + 1 < len(headings)
            else len(text)
        )
        section = text[heading.end():end]
        for block in BOLD_BLOCK_RE.finditer(section):
            raw_label = block.group(1).strip().removesuffix(".")
            if CONTRACT_FIELD_LABELS.get(raw_label) != "Acceptance criteria":
                continue
            body = block.group(2)
            body_start = heading.end() + block.start(2)
            for clause in CRITERION_CLAUSE_RE.finditer(body):
                referenced_steps = set(
                    STEP_REFERENCE_RE.findall(clause.group(0))
                ) - {current_step}
                if (
                    not referenced_steps
                    or MEASURED_VALUE_TERM_RE.search(clause.group(0)) is None
                    or QUANTITY_TERM_RE.search(clause.group(0)) is None
                ):
                    continue
                line_number = (
                    text.count("\n", 0, body_start + clause.start()) + 1
                )
                errors.append(
                    f"{shown(path, root)}:{line_number}: active Step "
                    f"{current_step} acceptance criterion cites Step "
                    f"{', '.join(sorted(referenced_steps, key=int))}'s "
                    "recorded/measured quantity; assert the invariant relation "
                    "at the same commit instead"
                )


def run(
    root: Path = ROOT,
    *,
    verify_local_tag_refs: bool = True,
) -> int:
    root = root.resolve()
    errors: list[str] = []
    try:
        identity = resolve_cycle(root)
    except CycleIdentityError as error:
        print(f"cycle-check: ERROR: {error}", file=sys.stderr)
        return 1
    check_contract_cycle_paths(identity, root, errors)
    check_source_cycle_literals(root, errors)

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
        check_runbook_amendments(
            identity.runbook,
            active_text,
            root,
            errors,
        )
        check_active_deferral_assignments(
            identity.runbook,
            active_text,
            root,
            errors,
        )
        check_active_step_value_criteria(
            identity.runbook,
            active_text,
            root,
            errors,
        )
        unchecked = len(UNCHECKED_RE.findall(active_text))
        closing = active_text.count(CLOSING_HEADING)
        if unchecked >= 1 and closing == 0:
            active_state = "open"
        elif unchecked == 0 and closing == 1:
            active_state = "closed"
            check_closed_execution(
                identity.runbook,
                active_text,
                root,
                errors,
                verify_local_tag_refs,
            )
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
        check_closed_execution(
            path,
            text,
            root,
            errors,
            verify_local_tag_refs,
        )
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
        f"local_tag_refs={'verified' if verify_local_tag_refs else 'not-requested'}, "
        f"runbook={shown(identity.runbook, root)}, "
        f"progress={shown(identity.progress, root)}, "
        f"closed_execution={closed}, historical={len(plain_task_files)})"
    )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Verify active-cycle identity, runbook lifecycle, and tool targets."
        )
    )
    parser.add_argument(
        "--skip-local-tag-verification",
        action="store_true",
        help=(
            "skip resolution of local annotated-tag refs while retaining "
            "release-record structure and commit-object checks"
        ),
    )
    args = parser.parse_args()
    return run(
        verify_local_tag_refs=not args.skip_local_tag_verification,
    )


if __name__ == "__main__":
    raise SystemExit(main())
