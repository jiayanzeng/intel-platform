#!/usr/bin/env python3
"""Verify that cycle identity, runbook lifecycle, and tool targets agree."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import subprocess
import sys
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path
from typing import Callable, NamedTuple

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools.audit_deferred import progress_paths as deferred_progress_paths
from tools.cycle_identity import (
    CycleIdentityError,
    execution_runbooks,
    historical_artifacts,
    progress_records,
    resolve_cycle,
    task_documents,
)
from tools.export_check import (
    CYCLE_RETENTION_DEPTH,
    MAX_EXPORT_BYTES,
    ExportCheckError,
    export_attention_boundary,
    export_attention_errors,
    expected_retained_cycle_paths,
    governed_export_measured_cell,
)
from tools.progress_check import default_progress_path
from tools import version_check


ROOT = Path(__file__).resolve().parents[1]
CHECKED_RE = re.compile(r"^- \[x\] ", re.MULTILINE)
UNCHECKED_RE = re.compile(r"^- \[ \] ", re.MULTILINE)
CLOSING_HEADING = "## Cycle closing record"
DATE_RE = re.compile(
    r"^- \*\*Cycle closed:\*\* ([0-9]{4}-[0-9]{2}-[0-9]{2})$",
    re.MULTILINE,
)
DATED_DISPOSITION_RE = re.compile(
    r"^- \*\*Release disposition:\*\* (release|no-release) "
    r"\(as of ([0-9]{4}-[0-9]{2}-[0-9]{2})\)$",
    re.MULTILINE,
)
LEGACY_DISPOSITION_RE = re.compile(
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
STEP_HEADING_RE = re.compile(r"^## Step ([0-9]+[A-Z]?)\b[^\n]*$", re.MULTILINE)
DEFERRED_HEADING = "## Deferred means deferred"
MARKDOWN_TABLE_SEPARATOR_RE = re.compile(r"^:?-{3,}:?$")
STEP_REFERENCE_RE = re.compile(r"\bStep ([0-9]+[A-Z]?)\b", re.IGNORECASE)
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
    r"^Step ([0-9]+[A-Z]?) — .+ — ([0-9]{4}-[0-9]{2}-[0-9]{2})$",
    re.MULTILINE,
)
CONTRACT_FIELD_LABELS = {
    "Objective": "Objective",
    "Acceptance criteria": "Acceptance criteria",
    "Done when": "Done when",
}
EXECUTION_CYCLE_RE = re.compile(
    r"^TASKS-v([0-9]+(?:\.[0-9]+)*)-EXECUTION\.md$"
)
STATE_HEADER_RE = re.compile(
    r"^\*\*As of:\*\*.*?(?=\n\n|\Z)",
    re.MULTILINE | re.DOTALL,
)
STATE_LEADING_PARAGRAPH_RE = re.compile(
    r"\A#[^\n]*\n\n(?P<paragraph>.*?)(?=\n\n|\Z)",
    re.DOTALL,
)
STATE_AS_OF_HEADER_CANDIDATE_RE = re.compile(
    r"^\*\*[^*\n]*\bas of\b[^*\n]*:\*\*",
    re.IGNORECASE | re.MULTILINE,
)
PENDING_PUBLICATION_RE = re.compile(
    r"\bpublication\b[^\n]{0,240}?\b(?:pending|outstanding)\b",
    re.IGNORECASE,
)
ORIGIN_MAIN_LITERAL_RE = re.compile(
    r"(?:`origin/main`|(?<!`)origin/main(?!`)|Remote `main`)"
    r"(?:\s+and\s+(?:remote\s+)?`?main`?)?\s*"
    r"(?:is|are|was|were|remains?|points?\s+to|resolves?\s+to|at|=|:)"
    r"\s*`?([0-9a-f]{40})`?",
    re.IGNORECASE,
)
LEGACY_STATE_REF_ASSERTIONS = (
    # These required header assertions deliberately use a phrasing in which no
    # backtick appears between the named ref and its hash. Do not widen
    # ``[^`\n]`` to admit backticks: that would let an unrelated intervening
    # hash satisfy the assertion instead of making a missing assertion fail.
    (
        "annotated tag object",
        re.compile(
            r"annotated (?:tag )?object[^`\n]{0,120}"
            r"`([0-9a-f]{40})`",
            re.IGNORECASE,
        ),
    ),
    (
        "tag target",
        re.compile(
            r"(?:tag target|release commit)[^`\n]{0,120}"
            r"`([0-9a-f]{40})`",
            re.IGNORECASE,
        ),
    ),
)
TAGGED_CLOSING_STATE_REF_ASSERTIONS = (
    (
        "release commit",
        re.compile(
            r"release commit[^`\n]{0,120}`([0-9a-f]{40})`",
            re.IGNORECASE,
        ),
    ),
)
POST_PUSH_RECORD_RE = re.compile(
    r"^- \*\*Post-push verification date:\*\* "
    r"([0-9]{4}-[0-9]{2}-[0-9]{2})\n"
    r"- \*\*Post-push release:\*\* (`?)([^`\n]+)\2\n"
    r"- \*\*Post-push annotated tag object:\*\* `([0-9a-f]{40})`\n"
    r"- \*\*Post-push closing commit:\*\* `([0-9a-f]{40})`\n"
    r"- \*\*Post-push hosted run:\*\* `([0-9]+)`$",
    re.MULTILINE,
)
UNPUBLISHED_LOCAL_CLOSE_RE = re.compile(
    r"^- \*\*Publication observation date:\*\* "
    r"([0-9]{4}-[0-9]{2}-[0-9]{2})\n"
    r"- \*\*Publication observation release:\*\* (`?)([^`\n]+)\2\n"
    r"- \*\*Publication observation status:\*\* "
    r"`unpublished-local-close`\n"
    r"- \*\*Publication observation remote:\*\* `origin`\n"
    r"- \*\*Publication observation tag ref:\*\* `absent`$",
    re.MULTILINE,
)
UNPUBLISHED_LOCAL_CLOSE_HEADER_RE = re.compile(
    r"\bclosed locally and unpublished\b",
    re.IGNORECASE,
)
WITHHELD_RELEASE_CANDIDATE_RE = re.compile(
    r"^- \*\*Withheld release decision date:\*\* "
    r"([0-9]{4}-[0-9]{2}-[0-9]{2})\n"
    r"- \*\*Withheld release:\*\* (`?)([^`\n]+)\2\n"
    r"- \*\*Withheld release status:\*\* `permanently-withheld`$",
    re.MULTILINE,
)
WITHHELD_RELEASE_RE = re.compile(
    r"^- \*\*Withheld release decision date:\*\* "
    r"([0-9]{4}-[0-9]{2}-[0-9]{2})\n"
    r"- \*\*Withheld release:\*\* (`?)([^`\n]+)\2\n"
    r"- \*\*Withheld release status:\*\* `permanently-withheld`\n"
    r"- \*\*Withheld release reason:\*\* ([^\n]*\S[^\n]*)\n"
    r"- \*\*Withheld release tag expectation:\*\* "
    r"`local-only-never-remote`$",
    re.MULTILINE,
)
WITHHELD_RELEASE_HEADER_RE = re.compile(
    r"\bpermanently withheld\b",
    re.IGNORECASE,
)


class ClosedRelease(NamedTuple):
    runbook: Path
    tag: str
    release_commit: str
    recorded_tag_object: str | None

    @property
    def uses_tagged_closing_commit(self) -> bool:
        return self.recorded_tag_object is None


def shown(path: Path, root: Path) -> str:
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)


def check_required_state_ref_assertions(
    state_path: Path,
    root: Path,
    header: str,
    assertions_to_check: tuple[tuple[str, re.Pattern[str]], ...],
    expected: dict[str, str],
    errors: list[str],
) -> None:
    """Require each admitted immutable header assertion to be current."""
    # Invariant R12 control site: required and fresh immutable assertions.
    for label, pattern in assertions_to_check:
        measured = expected[label]
        assertions = list(pattern.finditer(header))
        if not assertions:
            errors.append(
                f"{shown(state_path, root)}: publication assertion required: "
                f"status header must assert the {label} in the required "
                "unambiguous phrasing"
            )
            continue
        for assertion in assertions:
            asserted = assertion.group(1)
            if asserted != measured:
                errors.append(
                    f"{shown(state_path, root)}: publication assertion "
                    f"freshness: {label} asserts {asserted}, but the measured "
                    f"ref is {measured}"
                )


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


def git_status(root: Path, *args: str) -> tuple[int, str]:
    result = subprocess.run(
        ["git", *args],
        cwd=root,
        check=False,
        text=True,
        capture_output=True,
    )
    return result.returncode, result.stderr.strip()


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


def tagged_closing_record_matches(
    text: str,
    release: str,
    release_commit: str,
) -> bool:
    if UNCHECKED_RE.search(text) is not None:
        return False
    if text.count(CLOSING_HEADING) != 1:
        return False
    section = text.split(CLOSING_HEADING, 1)[1]
    releases = list(RELEASE_RE.finditer(section))
    commits = list(RELEASE_COMMIT_RE.finditer(section))
    dispositions = (
        list(DATED_DISPOSITION_RE.finditer(section))
        + list(LEGACY_DISPOSITION_RE.finditer(section))
    )
    return (
        len(releases) == 1
        and releases[0].group(2) == release
        and len(commits) == 1
        and commits[0].group(1) == release_commit
        and len(TAG_OBJECT_RE.findall(section)) == 0
        and len(dispositions) == 1
        and dispositions[0].group(1) == "release"
    )


def check_annotated_tag_type(
    root: Path,
    path: Path,
    release: str,
    tag_object: str,
    errors: list[str],
) -> bool:
    tag_type = git_output(root, "cat-file", "-t", tag_object)
    # Invariant R12 control site: annotated closing-tag type.
    if tag_type != "tag":
        errors.append(
            f"{shown(path, root)}: release {release!r} must resolve to an "
            f"annotated tag object; measured object {tag_object} has type "
            f"{tag_type!r}"
        )
        return False
    return True


def check_tagged_closing_identity(
    root: Path,
    path: Path,
    release: str,
    release_commit: str,
    tag_object: str,
    closing_commit: str,
    errors: list[str],
) -> bool:
    valid = check_annotated_tag_type(
        root,
        path,
        release,
        tag_object,
        errors,
    )

    parent = git_output(root, "rev-parse", f"{closing_commit}^")
    # Invariant R12 control site: tagged-closing parent agreement.
    if parent != release_commit:
        errors.append(
            f"{shown(path, root)}: tagged-closing parent agreement: "
            f"{release!r} peels to {closing_commit}, whose first parent is "
            f"{parent!r}, not recorded release commit {release_commit}"
        )
        valid = False

    target_text = git_output(
        root,
        "show",
        f"{closing_commit}:{shown(path, root)}",
    )
    # Invariant R12 control site: tagged-closing tree agreement.
    if target_text is None or not tagged_closing_record_matches(
        target_text,
        release,
        release_commit,
    ):
        errors.append(
            f"{shown(path, root)}: tagged-closing tree agreement: "
            f"{release!r} target {closing_commit} does not contain the closed "
            "runbook with its recorded release commit and no tag-object field"
        )
        valid = False
    return valid


def check_release_record(
    path: Path,
    section: str,
    root: Path,
    checked: int,
    errors: list[str],
    verify_local_tag_refs: bool = True,
    require_dated_disposition: bool = False,
    require_tagged_closing_commit: bool = False,
    withheld_releases: frozenset[str] = frozenset(),
    hosted_ref_topology: bool = False,
) -> None:
    date_match = exactly_one(
        DATE_RE, section, path, root, "cycle-close date", errors
    )
    if date_match is not None and not valid_iso_date(date_match.group(1)):
        errors.append(
            f"{shown(path, root)}: invalid cycle-close date "
            f"{date_match.group(1)!r}"
        )

    dated_dispositions = list(DATED_DISPOSITION_RE.finditer(section))
    legacy_dispositions = list(LEGACY_DISPOSITION_RE.finditer(section))
    if require_dated_disposition:
        if len(dated_dispositions) != 1:
            if len(dated_dispositions) == 0 and len(legacy_dispositions) == 1:
                errors.append(
                    f"{shown(path, root)}: declared closed cycle release "
                    "disposition must state an as-of date; found undated "
                    f"{legacy_dispositions[0].group(0)!r}"
                )
            else:
                errors.append(
                    f"{shown(path, root)}: closing record must contain "
                    "exactly one dated release disposition; found "
                    f"{len(dated_dispositions)}"
                )
            return
        if legacy_dispositions:
            errors.append(
                f"{shown(path, root)}: closing record contains both dated "
                "and legacy release dispositions"
            )
            return
        disposition_match = dated_dispositions[0]
    else:
        disposition_matches = dated_dispositions + legacy_dispositions
        if len(disposition_matches) != 1:
            errors.append(
                f"{shown(path, root)}: closing record must contain exactly "
                "one release disposition; found "
                f"{len(disposition_matches)}"
            )
            return
        disposition_match = disposition_matches[0]

    if disposition_match.re is DATED_DISPOSITION_RE:
        disposition_date = disposition_match.group(2)
        if not valid_iso_date(disposition_date):
            errors.append(
                f"{shown(path, root)}: invalid release-disposition date "
                f"{disposition_date!r}"
            )

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
        tag_matches = list(TAG_OBJECT_RE.finditer(section))
        # Invariant R12 control site: tagged-closing protocol.
        if require_tagged_closing_commit and tag_matches:
            errors.append(
                f"{shown(path, root)}: declared closed cycle must use the "
                "tagged-closing protocol and omit the Annotated tag object "
                "field; record that object in the dated post-push append"
            )
            return
        if len(tag_matches) > 1:
            errors.append(
                f"{shown(path, root)}: closing record must contain at most one "
                f"annotated tag object; found {len(tag_matches)}"
            )
            return
        if release_match is None or commit_match is None:
            return
        release = release_match.group(2)
        commit = commit_match.group(1)
        commit_type = git_output(root, "cat-file", "-t", commit)
        if commit_type != "commit":
            errors.append(
                f"{shown(path, root)}: recorded release commit {commit} "
                "is not a commit object"
            )
        if verify_local_tag_refs:
            resolved_tag = git_output(root, "rev-parse", release)
            resolved_commit = git_output(root, "rev-parse", f"{release}^{{}}")
            if len(tag_matches) == 1:
                tag_object = tag_matches[0].group(1)
                object_type = git_output(root, "cat-file", "-t", tag_object)
                if resolved_tag != tag_object or object_type != "tag":
                    errors.append(
                        f"{shown(path, root)}: annotated tag {release!r} does "
                        f"not resolve to recorded tag object {tag_object}"
                    )
                if resolved_commit != commit:
                    errors.append(
                        f"{shown(path, root)}: release {release!r} does not "
                        f"dereference to recorded commit {commit}"
                    )
                return
            if resolved_tag is None:
                # Invariant R12 control site: hosted withheld-tag admission.
                if release in withheld_releases and hosted_ref_topology:
                    return
                # Invariant R12 control site: tagged-closing pre-tag record admission.
                if (
                    len(tag_matches) == 0
                    and git_output(root, "rev-parse", "HEAD") == commit
                ):
                    # The assembled tagged-closing worktree is intentionally
                    # one commit ahead of the release parent it records. The
                    # tag cannot exist until that closing commit exists.
                    return
                errors.append(
                    f"{shown(path, root)}: annotated tag {release!r} cannot "
                    "be resolved for the tagged-closing protocol"
                )
                return
            if resolved_commit is None:
                errors.append(
                    f"{shown(path, root)}: annotated tag target {release!r} "
                    "cannot be resolved for the tagged-closing protocol"
                )
                return
            check_tagged_closing_identity(
                root,
                path,
                release,
                commit,
                resolved_tag,
                resolved_commit,
                errors,
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
    require_dated_disposition: bool = False,
    require_tagged_closing_commit: bool = False,
    withheld_releases: frozenset[str] = frozenset(),
    hosted_ref_topology: bool = False,
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
        require_dated_disposition,
        require_tagged_closing_commit,
        withheld_releases,
        hosted_ref_topology,
    )


def cycle_version(path: Path) -> tuple[int, ...] | None:
    match = EXECUTION_CYCLE_RE.fullmatch(path.name)
    if match is None:
        return None
    return tuple(int(part) for part in match.group(1).split("."))


def closed_releases(
    execution_files: list[Path],
) -> list[tuple[tuple[int, ...], ClosedRelease]]:
    releases: list[tuple[tuple[int, ...], ClosedRelease]] = []
    for path in execution_files:
        text = path.read_text()
        version = cycle_version(path)
        if (
            version is None
            or UNCHECKED_RE.search(text) is not None
            or text.count(CLOSING_HEADING) != 1
        ):
            continue
        section = text.split(CLOSING_HEADING, 1)[1]
        disposition = DATED_DISPOSITION_RE.search(section)
        if disposition is None:
            disposition = LEGACY_DISPOSITION_RE.search(section)
        # Invariant R12 control site: newest closed release selection.
        if disposition is None or disposition.group(1) != "release":
            continue
        release = RELEASE_RE.search(section)
        commit = RELEASE_COMMIT_RE.search(section)
        tag_objects = list(TAG_OBJECT_RE.finditer(section))
        if release is None or commit is None or len(tag_objects) > 1:
            continue
        releases.append(
            (
                version,
                ClosedRelease(
                    runbook=path,
                    tag=release.group(2),
                    release_commit=commit.group(1),
                    recorded_tag_object=(
                        tag_objects[0].group(1) if tag_objects else None
                    ),
                ),
            )
        )
    return releases


def newest_closed_release(
    execution_files: list[Path],
) -> ClosedRelease | None:
    releases = closed_releases(execution_files)
    if not releases:
        return None
    return max(releases, key=lambda item: item[0])[1]


def check_withheld_release_records(
    state_path: Path,
    state_text: str,
    execution_files: list[Path],
    root: Path,
    errors: list[str],
) -> frozenset[str]:
    """Validate consequential permanent-withholding records in State."""
    candidates = list(WITHHELD_RELEASE_CANDIDATE_RE.finditer(state_text))
    complete = list(WITHHELD_RELEASE_RE.finditer(state_text))
    # Invariant R12 control site: withheld-release record admission.
    if len(complete) != len(candidates):
        errors.append(
            f"{shown(state_path, root)}: every permanently withheld release "
            "record must carry a nonempty reason and the exact "
            "`local-only-never-remote` tag expectation; found "
            f"{len(candidates)} candidate record(s) and {len(complete)} "
            "complete record(s)"
        )

    known_releases = {
        release.tag: release
        for _version, release in (closed_releases(execution_files) or [])
    }
    withheld: set[str] = set()
    for record in complete:
        date = record.group(1)
        tag = record.group(3)
        if not valid_iso_date(date):
            errors.append(
                f"{shown(state_path, root)}: invalid withheld-release "
                f"decision date {date!r} for {tag}"
            )
        if tag in withheld:
            errors.append(
                f"{shown(state_path, root)}: permanently withheld release "
                f"{tag} must have exactly one complete record"
            )
            continue
        release = known_releases.get(tag)
        if release is None:
            errors.append(
                f"{shown(state_path, root)}: permanently withheld release "
                f"{tag} does not name a closed release"
            )
            continue
        if not release.uses_tagged_closing_commit:
            errors.append(
                f"{shown(state_path, root)}: permanently withheld release "
                f"{tag} is not a tagged-closing release"
            )
            continue
        withheld.add(tag)
    return frozenset(withheld)


def check_publication_status(
    root: Path,
    execution_files: list[Path],
    errors: list[str],
    verify_local_tag_refs: bool = True,
    withheld_releases: frozenset[str] = frozenset(),
    hosted_ref_topology: bool = False,
) -> str | None:
    """Reconcile the status header with the newest reachable closed release."""
    release = newest_closed_release(execution_files)
    if release is None:
        return (
            "publication-status: local-tag-reconciliation=not-applicable "
            "bound=no reachable closed release exists, so there is no "
            "release ref to reconcile"
        )
    runbook = release.runbook
    tag = release.tag
    release_commit = release.release_commit
    recorded_object = release.recorded_tag_object
    is_withheld = tag in withheld_releases
    state_path = root / "STATE.md"
    # Invariant R12 control site: publication-family admission gate.
    if not state_path.is_file():
        errors.append(
            f"{shown(state_path, root)}: publication admission file required: "
            "STATE.md is absent or is not a regular file"
        )
        return
    state_text = state_path.read_text()
    header_match = STATE_HEADER_RE.search(state_text)
    if header_match is None:
        leading_match = STATE_LEADING_PARAGRAPH_RE.search(state_text)
        leading = (
            leading_match.group("paragraph")
            if leading_match is not None
            else ""
        )
        if STATE_AS_OF_HEADER_CANDIDATE_RE.search(leading) is not None:
            errors.append(
                f"{shown(state_path, root)}: publication admission header "
                "shape: the leading as-of status header is present but does "
                "not match STATE_HEADER_RE's required '**As of:**' form"
            )
        else:
            errors.append(
                f"{shown(state_path, root)}: publication admission header "
                "required: STATE.md has no '**As of:**' status header"
            )
        return
    header = header_match.group(0)
    tag_independent_error_count = len(errors)

    # This lifecycle gate intentionally does not delegate to
    # version_check.state_version(). That tool independently parses the same
    # header to bind the release version; this function parses publication
    # status. Either hand-written regex can reject text the other accepts, so
    # cycle-check must fail closed at its own family boundary.

    # A mutable ref cannot be truthfully pinned in the immutable commit whose
    # publication moves that same ref. Mutable-ref measurements belong in
    # dated body appends.
    # Invariant R12 control site: origin-main prohibition.
    if ORIGIN_MAIN_LITERAL_RE.search(header) is not None:
        errors.append(
            f"{shown(state_path, root)}: publication status header must not "
            "assert a literal origin/main hash; publishing the asserting "
            "commit moves that ref, so record mutable-ref measurements in a "
            "dated body append"
        )

    # Tagged-closing release-parent identity is derivable entirely from the
    # admitted State header and closed runbook. Evaluate it before either the
    # portable hosted branch or local tag resolution; a tag is not an input.
    if release.uses_tagged_closing_commit:
        check_required_state_ref_assertions(
            state_path,
            root,
            header,
            TAGGED_CLOSING_STATE_REF_ASSERTIONS,
            {"release commit": release_commit},
            errors,
        )
    if is_withheld:
        if WITHHELD_RELEASE_HEADER_RE.search(header) is None:
            errors.append(
                f"{shown(state_path, root)}: permanently withheld release "
                f"{tag} requires the status header to present it as settled"
            )
        # Invariant R12 control site: withheld-pending contradiction.
        if PENDING_PUBLICATION_RE.search(header) is not None:
            errors.append(
                f"{shown(state_path, root)}: permanently withheld release "
                f"{tag} must not be presented as a pending publication"
            )
    tag_independent_verdict = (
        "verified"
        if len(errors) == tag_independent_error_count
        else "failed"
    )

    # Portable hosted verification lacks historical local tag objects. It may
    # skip ref reconciliation only after family admission and every
    # tag-independent assertion have been evaluated; closed-runbook structure
    # remains checked by check_closed_execution().
    if not verify_local_tag_refs:
        return (
            "publication-status: local-tag-reconciliation=not-requested "
            f"tag-independent-assertions={tag_independent_verdict} "
            "bound=portable hosted mode lacks historical local tag objects; "
            "State/header admission, mutable-ref prohibition, applicable "
            "tagged release-parent freshness, and closed-runbook structure "
            "remain enforced"
        )

    measured_object = git_output(root, "rev-parse", tag)
    # Invariant R12 control site: unavailable annotated-tag ref.
    if measured_object is None:
        # Invariant R12 control site: hosted withheld publication admission.
        if is_withheld and hosted_ref_topology:
            return (
                "publication-status: local-tag-reconciliation=withheld-hosted "
                f"tag-independent-assertions={tag_independent_verdict} "
                f"protocol=tagged-closing release={tag} "
                "publication=permanently-withheld "
                "tag-expectation=local-only-never-remote"
            )
        if release.uses_tagged_closing_commit:
            head = git_output(root, "rev-parse", "HEAD")
            # Invariant R12 control site: tagged-closing pre-tag publication gate.
            if head == release_commit:
                return (
                    "publication-status: local-tag-reconciliation=pre-tag "
                    f"tag-independent-assertions={tag_independent_verdict} "
                    f"protocol=tagged-closing release={tag} tag=absent "
                    f"release-parent={release_commit}"
                )
        errors.append(
            f"{shown(state_path, root)}: publication verification unavailable: "
            f"annotated tag ref {tag!r} cannot be resolved"
        )
        return
    measured_target = git_output(root, "rev-parse", f"{tag}^{{}}")
    # Invariant R12 control site: unavailable annotated-tag target.
    if measured_target is None:
        errors.append(
            f"{shown(state_path, root)}: publication verification unavailable: "
            f"annotated tag target {tag!r} cannot be resolved"
        )
        return
    if (
        recorded_object is not None
        and measured_object != recorded_object
    ):  # Root cause; mask derived rules.
        errors.append(
            f"{shown(state_path, root)}: publication release-object agreement: "
            f"{tag} resolves to tag object {measured_object}, but "
            f"{shown(runbook, root)} records {recorded_object}"
        )
        return
    if not check_annotated_tag_type(
        root,
        state_path,
        tag,
        measured_object,
        errors,
    ):
        return
    if release.uses_tagged_closing_commit:
        identity_errors: list[str] = []
        check_tagged_closing_identity(
            root,
            runbook,
            tag,
            release_commit,
            measured_object,
            measured_target,
            identity_errors,
        )
        if identity_errors:
            errors.extend(
                error.replace(
                    f"{shown(runbook, root)}:",
                    f"{shown(state_path, root)}:",
                    1,
                )
                for error in identity_errors
            )
            return
    elif measured_target != release_commit:
        errors.append(
            f"{shown(state_path, root)}: publication release-object agreement: "
            f"{tag} peels to {measured_target}, but "
            f"{shown(runbook, root)} records {release_commit}"
        )
        return

    ancestry_status, ancestry_error = git_status(
        root, "merge-base", "--is-ancestor", measured_target, "HEAD"
    )
    # Invariant R12 control site: unavailable publication ancestry.
    if ancestry_status != 0:
        detail = (
            f": {ancestry_error}"
            if ancestry_error
            else f" (git exited {ancestry_status})"
        )
        errors.append(
            f"{shown(state_path, root)}: publication ancestry verification "
            f"unavailable: cannot prove tagged closing commit "
            f"{measured_target} is reachable from HEAD{detail}"
        )
        return

    # Rule 1: a reachable annotated release cannot coexist with a header that
    # still calls its publication pending or outstanding.
    # Invariant R12 control site: pending-publication prohibition.
    if not is_withheld and PENDING_PUBLICATION_RE.search(header) is not None:
        errors.append(
            f"{shown(state_path, root)}: publication disposition agreement: "
            f"newest closed release {tag} in {shown(runbook, root)} is an "
            "annotated tag reachable from HEAD, but the status header asserts "
            "publication is pending or outstanding"
        )

    if is_withheld:
        return (
            "publication-status: local-tag-reconciliation=verified "
            f"protocol=tagged-closing release={tag} "
            "publication=permanently-withheld "
            "tag-expectation=local-only-never-remote"
        )

    # Rule 2: a legacy release header retains both immutable tag hashes. Its
    # assertions remain tag-dependent and therefore run only after successful
    # object and target resolution. Tagged-closing release-parent identity was
    # already checked above because neither local tag value is an input.
    if not release.uses_tagged_closing_commit:
        check_required_state_ref_assertions(
            state_path,
            root,
            header,
            LEGACY_STATE_REF_ASSERTIONS,
            {
                "annotated tag object": measured_object,
                "tag target": measured_target,
            },
            errors,
        )

    if not release.uses_tagged_closing_commit:
        return (
            "publication-status: local-tag-reconciliation=verified "
            f"protocol=legacy release={tag} bound=R-CLOSE post-push records "
            "do not apply to a legacy release"
        )
    head = git_output(root, "rev-parse", "HEAD")
    if head is None:
        errors.append(
            f"{shown(state_path, root)}: publication verification unavailable: "
            "HEAD cannot be resolved"
        )
        return
    # The tagged closing commit is allowed to carry only the already-known
    # release commit. Once HEAD advances, a dated remote-tag absence observation
    # can represent an unpublished local close. Otherwise the post-push record
    # is mandatory and pins the values that came into existence after that
    # commit. The absence observation is necessarily a recorded measurement:
    # no offline Git fact can prove that a remote tag remains absent later.
    # Invariant R12 control site: required and fresh post-push record.
    if head != measured_target:
        records = [
            match
            for match in POST_PUSH_RECORD_RE.finditer(state_text)
            if match.group(3) == tag
        ]
        unpublished_records = [
            match
            for match in UNPUBLISHED_LOCAL_CLOSE_RE.finditer(state_text)
            if match.group(3) == tag
        ]
        # Invariant R12 control site: unpublished local-close observation.
        if not records and len(unpublished_records) == 1:
            observation = unpublished_records[0]
            if not valid_iso_date(observation.group(1)):
                errors.append(
                    f"{shown(state_path, root)}: invalid publication "
                    f"observation date {observation.group(1)!r}"
                )
                return
            if UNPUBLISHED_LOCAL_CLOSE_HEADER_RE.search(header) is None:
                errors.append(
                    f"{shown(state_path, root)}: unpublished local-close "
                    "observation requires the status header to say the "
                    "release is closed locally and unpublished"
                )
                return
            return (
                "publication-status: local-tag-reconciliation=verified "
                f"protocol=tagged-closing release={tag} "
                "publication=unpublished-local-close "
                "bound=dated origin tag-absence observation; offline Git "
                "cannot independently refresh remote absence"
            )
        if len(records) != 1:
            errors.append(
                f"{shown(state_path, root)}: publication post-push record "
                f"required: expected exactly one complete record for {tag}; "
                f"found {len(records)}"
            )
            return
        record = records[0]
        if not valid_iso_date(record.group(1)):
            errors.append(
                f"{shown(state_path, root)}: invalid post-push verification "
                f"date {record.group(1)!r}"
            )
        recorded_post_push_object = record.group(4)
        if recorded_post_push_object != measured_object:
            errors.append(
                f"{shown(state_path, root)}: publication post-push freshness: "
                "annotated tag object records "
                f"{recorded_post_push_object}, but the measured ref is "
                f"{measured_object}"
            )
        recorded_post_push_target = record.group(5)
        if recorded_post_push_target != measured_target:
            errors.append(
                f"{shown(state_path, root)}: publication post-push freshness: "
                f"closing commit records {recorded_post_push_target}, but the "
                f"measured ref is {measured_target}"
            )
    return (
        "publication-status: local-tag-reconciliation=verified "
        f"protocol=tagged-closing release={tag}"
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


SCOPE_HEADING_RE = re.compile(
    r"^## Declared scope(?:[^\n]*)$",
    re.MULTILINE,
)
SCOPE_FORWARD_BOUNDARY = (0, 23)
SCOPE_CLASSES = {
    "scope_version",
    "disposition_intent",
    "allow",
    "release_authority",
    "forbid",
}


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


def step_sort_key(step: str) -> tuple[int, str]:
    match = re.fullmatch(r"([0-9]+)([A-Z]?)", step)
    if match is None:
        raise ValueError(f"invalid step identifier {step!r}")
    number, suffix = match.groups()
    return int(number), suffix


def first_committed_runbook_text(root: Path, path: Path) -> str | None:
    relative = shown(path, root)
    history_path = relative
    staged = git_output(root, "diff", "--cached", "--name-status", "-M", "--")
    if staged:
        for line in staged.splitlines():
            fields = line.split("\t")
            if (
                len(fields) == 3
                and fields[0].startswith("R")
                and fields[2] == relative
            ):
                history_path = fields[1]
                break
    additions = git_output(
        root,
        "log",
        "--follow",
        "--diff-filter=A",
        "--format=%H",
        "--",
        history_path,
    )
    if not additions:
        return None
    first_commit = additions.splitlines()[-1]
    tree = git_output(root, "ls-tree", "-r", "--name-only", first_commit)
    if tree is None:
        return None
    candidates = [
        candidate
        for candidate in tree.splitlines()
        if Path(candidate).name == path.name
    ]
    if len(candidates) != 1:
        return None
    return git_output(root, "show", f"{first_commit}:{candidates[0]}")


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
    for step, label in sorted(
        changed,
        key=lambda item: (*step_sort_key(item[0]), item[1]),
    ):
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


class ScopeDeclaration(NamedTuple):
    version: int
    disposition_intent: str
    allow: tuple[str, ...]
    release_authorities: tuple[str, ...]
    forbid: tuple[str, ...]


def literal_table_cell(cell: str) -> str:
    value = cell.strip()
    if value.startswith("`") and value.endswith("`") and len(value) >= 2:
        return value[1:-1]
    return value


def declared_scope_cycle_version(name: str) -> tuple[int, ...]:
    match = re.fullmatch(r"v([0-9]+(?:\.[0-9]+)*)", name)
    if match is None:
        return ()
    return tuple(int(part) for part in match.group(1).split("."))


def numeric_glob_range(last: int) -> list[str]:
    """Return brace alternatives covering every non-negative integer through last."""
    if last < 0:
        return []
    alternatives: list[str] = []
    decade = 0
    while decade <= last:
        upper = min(decade + 9, last)
        first_digit = 0
        last_digit = upper - decade
        prefix = str(decade // 10) if decade else ""
        if first_digit == last_digit:
            alternatives.append(f"{prefix}{first_digit}")
        elif first_digit == 0 and last_digit == 9:
            alternatives.append(f"{prefix}[0-9]")
        else:
            alternatives.append(f"{prefix}[{first_digit}-{last_digit}]")
        decade += 10
    return alternatives


def expected_review_export_retention_pattern(
    cycle_name: str,
    retained_cycle_paths: set[str],
) -> str:
    """Format the one exclusion pattern from a retained-cycle boundary."""
    version = declared_scope_cycle_version(cycle_name)
    if len(version) < 2:
        raise ValueError(f"cannot derive review retention for {cycle_name!r}")
    runbook_pattern = re.compile(
        r"^docs/cycles/TASKS-(v[0-9]+(?:\.[0-9]+)*)-EXECUTION\.md$"
    )
    retained_versions = sorted(
        declared_scope_cycle_version(match.group(1))
        for path in retained_cycle_paths
        if (match := runbook_pattern.fullmatch(path)) is not None
    )
    if len(retained_versions) != CYCLE_RETENTION_DEPTH:
        raise ValueError(
            f"tracked retained-cycle set for {cycle_name!r} must contain "
            f"{CYCLE_RETENTION_DEPTH} execution runbooks; found "
            f"{len(retained_versions)}"
        )
    if retained_versions[-1] != version:
        raise ValueError(
            f"tracked retained-cycle set does not end at {cycle_name!r}"
        )
    if any(
        retained[:-1] != version[:-1]
        for retained in retained_versions
    ):
        raise ValueError(
            f"tracked retained-cycle set for {cycle_name!r} crosses a "
            "version-family boundary that one exclusion pattern cannot "
            "express"
        )
    first_retained = retained_versions[0][-1]
    last_excluded = first_retained - 1
    alternatives = numeric_glob_range(last_excluded)
    if not alternatives:
        raise ValueError(
            f"cannot retain depth {CYCLE_RETENTION_DEPTH} at {cycle_name!r}"
        )
    prefix = ".".join(str(part) for part in version[:-1])
    return (
        "docs/cycles/{TASKS,PROGRESS}-"
        f"v{prefix}.{{{','.join(alternatives)}}}"
        "{.md,.*.md,-*.md}"
    )


def check_review_export_retention_pattern(
    root: Path,
    cycle_name: str,
    errors: list[str],
) -> None:
    path = root / "repomix.config.json"
    try:
        raw = json.loads(path.read_text())
        custom_patterns = raw["ignore"]["customPatterns"]
        if not isinstance(custom_patterns, list) or not all(
            isinstance(pattern, str) for pattern in custom_patterns
        ):
            raise TypeError("ignore.customPatterns is not a string list")
        retained_cycles = expected_retained_cycle_paths(root)
        expected = expected_review_export_retention_pattern(
            cycle_name,
            retained_cycles,
        )
    except (
        OSError,
        json.JSONDecodeError,
        KeyError,
        TypeError,
        ValueError,
        ExportCheckError,
    ) as error:
        errors.append(
            f"{shown(path, root)}: cannot derive review-export retention "
            f"pattern: {error}"
        )
        return
    prefix = "docs/cycles/{TASKS,PROGRESS}-"
    retention_patterns = [
        pattern for pattern in custom_patterns if pattern.startswith(prefix)
    ]
    # Invariant R12 control site: review-export retention configuration.
    if retention_patterns != [expected]:
        errors.append(
            f"{shown(path, root)}: review-export retention pattern for "
            f"{cycle_name} must be {expected!r} to agree with the tracked "
            f"retained-cycle set; found {retention_patterns!r}"
        )


def scope_pattern_regex(pattern: str) -> re.Pattern[str]:
    if (
        not pattern
        or pattern.startswith("/")
        or any(part == ".." for part in pattern.split("/"))
    ):
        raise ValueError(f"invalid repository-relative scope pattern {pattern!r}")
    translated: list[str] = ["^"]
    index = 0
    while index < len(pattern):
        if pattern.startswith("**/", index):
            translated.append("(?:[^/]+/)*")
            index += 3
        elif pattern.startswith("**", index):
            translated.append(".*")
            index += 2
        elif pattern[index] == "*":
            translated.append("[^/]*")
            index += 1
        elif pattern[index] == "?":
            translated.append("[^/]")
            index += 1
        elif pattern[index] == "[":
            end = pattern.find("]", index + 1)
            if end == -1:
                translated.append(r"\[")
                index += 1
                continue
            character_class = pattern[index + 1 : end]
            if character_class.startswith("!"):
                character_class = "^" + character_class[1:]
            translated.append("[" + character_class.replace("\\", r"\\") + "]")
            index = end + 1
        else:
            translated.append(re.escape(pattern[index]))
            index += 1
    translated.append("$")
    return re.compile("".join(translated))


def scope_pattern_matches(pattern: str, candidate: str) -> bool:
    return scope_pattern_regex(pattern).fullmatch(candidate) is not None


def scope_pattern_population_errors(
    declaration: ScopeDeclaration,
    _candidates: set[str],
) -> list[str]:
    errors: list[str] = []
    # Invariant R12 control site: declared scope pattern population.
    for scope_class, patterns in (
        ("allow", declaration.allow),
        ("release_authority", declaration.release_authorities),
        ("forbid", declaration.forbid),
    ):
        for pattern in patterns:
            if "`" in pattern or re.search(r"\s", pattern) is not None:
                errors.append(
                    f"declared-scope {scope_class} pattern is not a literal "
                    f"repository glob: {pattern!r}"
                )
                continue
    return errors


def parse_declared_scope(
    path: Path,
    text: str,
    root: Path,
    errors: list[str],
) -> ScopeDeclaration | None:
    headings = list(SCOPE_HEADING_RE.finditer(text))
    if len(headings) != 1:
        errors.append(
            f"{shown(path, root)}: v0.23-forward runbook must contain exactly "
            f"one declared-scope heading; found {len(headings)}"
        )
        return None
    section = text[headings[0].end():]
    next_heading = re.search(r"^## ", section, re.MULTILINE)
    if next_heading is not None:
        section = section[: next_heading.start()]
    lines = section.splitlines()
    header_index: int | None = None
    class_index: int | None = None
    value_index: int | None = None
    for index, line in enumerate(lines):
        cells = markdown_table_cells(line)
        normalized = [normalized_table_cell(cell).casefold() for cell in cells]
        if "scope class" not in normalized or "path or value" not in normalized:
            continue
        header_index = index
        class_index = normalized.index("scope class")
        value_index = normalized.index("path or value")
        break
    if header_index is None or class_index is None or value_index is None:
        errors.append(
            f"{shown(path, root)}: declared scope must contain a markdown "
            "table with Scope class and Path or value columns"
        )
        return None

    values: dict[str, list[str]] = {scope_class: [] for scope_class in SCOPE_CLASSES}
    for offset, line in enumerate(lines[header_index + 1 :], header_index + 1):
        cells = markdown_table_cells(line)
        if not cells or max(class_index, value_index) >= len(cells):
            continue
        normalized = [normalized_table_cell(cell) for cell in cells]
        if normalized and all(
            MARKDOWN_TABLE_SEPARATOR_RE.fullmatch(cell) for cell in normalized
        ):
            continue
        scope_class = literal_table_cell(cells[class_index]).casefold()
        value = literal_table_cell(cells[value_index])
        line_number = text[: headings[0].end()].count("\n") + offset + 1
        if scope_class not in SCOPE_CLASSES:
            errors.append(
                f"{shown(path, root)}:{line_number}: unknown declared-scope "
                f"class {scope_class!r}"
            )
            continue
        if not value:
            errors.append(
                f"{shown(path, root)}:{line_number}: declared-scope "
                f"{scope_class!r} value is empty"
            )
            continue
        values[scope_class].append(value)

    if values["scope_version"] != ["1"]:
        errors.append(
            f"{shown(path, root)}: declared scope requires exactly one "
            "scope_version row with value 1"
        )
    if (
        len(values["disposition_intent"]) != 1
        or values["disposition_intent"][0] not in {"release", "no-release"}
    ):
        errors.append(
            f"{shown(path, root)}: declared scope requires exactly one "
            "disposition_intent row with release or no-release"
        )
    patterns_valid = True
    for scope_class in ("allow", "release_authority", "forbid"):
        for pattern in values[scope_class]:
            try:
                scope_pattern_regex(pattern)
            except ValueError as error:
                errors.append(f"{shown(path, root)}: {error}")
                patterns_valid = False
    if errors and (
        values["scope_version"] != ["1"]
        or len(values["disposition_intent"]) != 1
        or values["disposition_intent"][0] not in {"release", "no-release"}
    ):
        return None
    if not values["allow"]:
        errors.append(
            f"{shown(path, root)}: declared scope requires at least one allow row"
        )
    if not patterns_valid:
        return None
    return ScopeDeclaration(
        version=1,
        disposition_intent=values["disposition_intent"][0],
        allow=tuple(values["allow"]),
        release_authorities=tuple(values["release_authority"]),
        forbid=tuple(values["forbid"]),
    )


def release_authority_paths(root: Path) -> tuple[str, ...]:
    manifests = [
        shown(path, root)
        for parent in ("crates", "apps")
        for path in sorted((root / parent).glob("*/Cargo.toml"))
    ]
    return tuple(
        sorted(
            {
                "Cargo.toml",
                "Cargo.lock",
                "README.md",
                "CHANGELOG.md",
                "shell/intel_shell/__init__.py",
                "shell/intel_shell/app.py",
                *manifests,
            }
        )
    )


def report_unpermitted_scope_paths(
    candidates: tuple[str, ...],
    permitted: Callable[[str], bool],
    label: str,
    path: Path,
    root: Path,
    errors: list[str],
) -> None:
    for candidate in candidates:
        # Invariant R12 control site: declared cycle scope.
        if not permitted(candidate):
            errors.append(
                f"{shown(path, root)}: declared scope {label} rejects "
                f"{candidate}"
            )


def scope_changed_path_allowed(
    candidate: str,
    declaration: ScopeDeclaration,
    standing_status_paths: set[str],
) -> bool:
    if candidate in standing_status_paths:
        return True
    if any(
        scope_pattern_matches(pattern, candidate)
        for pattern in declaration.release_authorities
    ):
        return True
    if any(
        scope_pattern_matches(pattern, candidate)
        for pattern in declaration.forbid
    ):
        return False
    return any(
        scope_pattern_matches(pattern, candidate)
        for pattern in declaration.allow
    )


def scope_release_forbid_overlaps(
    declaration: ScopeDeclaration,
    authorities: tuple[str, ...],
) -> tuple[str, ...]:
    return tuple(
        authority
        for authority in authorities
        if any(
            scope_pattern_matches(pattern, authority)
            for pattern in declaration.release_authorities
        )
        and any(
            scope_pattern_matches(pattern, authority)
            for pattern in declaration.forbid
        )
    )


def validate_declared_scope(
    declaration: ScopeDeclaration,
    authorities: tuple[str, ...],
    changed_paths: tuple[str, ...],
    standing_status_paths: set[str],
    recorded_release: bool,
    path: Path,
    root: Path,
    errors: list[str],
) -> None:
    if declaration.disposition_intent == "release" or recorded_release:
        report_unpermitted_scope_paths(
            authorities,
            lambda candidate: any(
                scope_pattern_matches(pattern, candidate)
                for pattern in declaration.release_authorities
            ),
            "release-authority set",
            path,
            root,
            errors,
        )
    report_unpermitted_scope_paths(
        changed_paths,
        lambda candidate: scope_changed_path_allowed(
            candidate,
            declaration,
            standing_status_paths,
        ),
        "diff",
        path,
        root,
        errors,
    )


def activation_anchor(root: Path, path: Path) -> str | None:
    relative = shown(path, root)
    history_path = relative
    staged = git_output(root, "diff", "--cached", "--name-status", "-M", "--")
    if staged:
        for line in staged.splitlines():
            fields = line.split("\t")
            if (
                len(fields) == 3
                and fields[0].startswith("R")
                and fields[2] == relative
            ):
                history_path = fields[1]
                break
    additions = git_output(
        root,
        "log",
        "--follow",
        "--diff-filter=A",
        "--format=%H",
        "--",
        history_path,
    )
    if not additions:
        return None
    return additions.splitlines()[-1]


def check_declared_scope(
    identity,
    path: Path,
    text: str,
    root: Path,
    errors: list[str],
) -> None:
    declaration = parse_declared_scope(path, text, root, errors)
    if declaration is None:
        return
    errors.extend(
        f"{shown(path, root)}: {error}"
        for error in scope_pattern_population_errors(declaration, set())
    )
    recorded_release = any(
        match.group(1) == "release"
        for match in DATED_DISPOSITION_RE.finditer(text)
    )
    changed_paths: tuple[str, ...] = ()
    if (root / ".git").exists():
        anchor = activation_anchor(root, path)
        if anchor is None:
            errors.append(
                f"{shown(path, root)}: cannot resolve activation anchor from "
                "the runbook-add commit"
            )
            return
        changed = git_output(
            root,
            "diff",
            "--name-only",
            f"{anchor}..HEAD",
            "--",
        )
        if changed is None:
            errors.append(
                f"{shown(path, root)}: cannot measure declared-scope diff "
                f"{anchor}..HEAD"
            )
            return
        changed_paths = tuple(
            line for line in changed.splitlines() if line
        )
    standing = {
        "STATE.md",
        shown(identity.progress, root),
        shown(identity.runbook, root),
    }
    validate_declared_scope(
        declaration,
        release_authority_paths(root),
        changed_paths,
        standing,
        recorded_release,
        path,
        root,
        errors,
    )


TRIGGER_FRESHNESS_FORWARD_BOUNDARY = (0, 23)
TRIGGER_IDENTITY_FORWARD_BOUNDARY = (0, 28)
TRIGGER_FLOOR_FORWARD_BOUNDARY = (0, 28)
GOVERNED_EXPORT_FORWARD_BOUNDARY = (0, 30)
ARTIFACT_BYTE_BOUNDARY_FORWARD_BOUNDARY = (0, 32)
STATE_REGION_CONTRACT_FORWARD_BOUNDARY = (0, 33)
FORWARD_BOUNDARY_RELATIONSHIPS = {
    "ARTIFACT_BYTE_BOUNDARY_FORWARD_BOUNDARY": (
        ("TRIGGER_IDENTITY_FORWARD_BOUNDARY",),
        "Artifact byte crossings consume cycle-identified governed trigger "
        "rows and their dated dispositions.",
    ),
    "GOVERNED_EXPORT_FORWARD_BOUNDARY": (
        ("TRIGGER_IDENTITY_FORWARD_BOUNDARY",),
        "The governed export value is a content constraint on the "
        "cycle-identified architecture trigger row.",
    ),
    "SCOPE_FORWARD_BOUNDARY": (
        (),
        "Independent: declared-scope activation does not consume trigger "
        "table state.",
    ),
    "STATE_REGION_CONTRACT_FORWARD_BOUNDARY": (
        ("ARTIFACT_BYTE_BOUNDARY_FORWARD_BOUNDARY",),
        "The State archival-region contract consumes the already-governed "
        "State artifact and adds structural eligibility and reference binding.",
    ),
    "TRIGGER_FRESHNESS_FORWARD_BOUNDARY": (
        (),
        "Independent: trigger freshness is the base trigger-table activation.",
    ),
    "TRIGGER_IDENTITY_FORWARD_BOUNDARY": (
        ("TRIGGER_FRESHNESS_FORWARD_BOUNDARY",),
        "Identity is enforced only inside the trigger-freshness gate.",
    ),
    "TRIGGER_FLOOR_FORWARD_BOUNDARY": (
        ("TRIGGER_FRESHNESS_FORWARD_BOUNDARY",),
        "Population floors consume the rows initialized by trigger freshness.",
    ),
}
DATED_DISPOSITIONS_HEADING = "### Dated operational-residual dispositions"
DEFERRED_COMPLETIONS_HEADING = "## Deferred completions"
ISO_DATE_TOKEN_RE = re.compile(r"\b[0-9]{4}-[0-9]{2}-[0-9]{2}\b")
GOVERNED_EXPORT_SUBJECT_PREFIX = "review-export size and retention bound"
GOVERNED_EXPORT_ROW_MARKER_RE = re.compile(
    r"Governed review-export bytes:\s*`([0-9]+)`"
)
GOVERNED_EXPORT_ROW_PROSE_RE = re.compile(
    r"\bexport of \*\*([0-9][0-9,]*) bytes\b"
)
GOVERNED_EXPORT_MARGIN_SERIES_RE = re.compile(
    r"Review-export margin: kind=`(governed→governed)`; "
    r"prior_progress=`([^`\n]+)`; prior_bytes=`([0-9]+)`; "
    r"current_progress=`([^`\n]+)`; current_bytes=`([0-9]+)`; "
    r"evaluated_progress=`([^`\n]+)`; evaluated_bytes=`([0-9]+)`; "
    r"denominator_bytes_per_cycle=`([0-9]+)`; "
    r"numerator_bytes=`([0-9]+)`; cycles=`([0-9]+\.[0-9]{2})`\."
)
GOVERNED_EXPORT_PROGRESS_PATH_RE = re.compile(
    r"^docs/cycles/PROGRESS-v([0-9]+(?:\.[0-9]+)+)\.md$"
)
GOVERNED_EXPORT_PROGRESS_PREFIX = "- governed review-export measurement:"
GOVERNED_EXPORT_PROGRESS_RE = re.compile(
    r"^- governed review-export measurement: "
    r"tree=`([0-9a-f]{40})`; bytes=`([0-9]+)`$",
    re.MULTILINE,
)
CYCLE_ENDING_EXPORT_AUDIT_PREFIX = "- cycle-ending review-export audit:"
CYCLE_ENDING_EXPORT_AUDIT_RE = re.compile(
    r"^- cycle-ending review-export audit: "
    r"closing_tree=`([0-9a-f]{40})`; bytes=`([0-9]+)`; "
    r"audit_delta=`([+-][0-9]+)`$",
    re.MULTILINE,
)
GOVERNED_ARTIFACT_BOUNDARY_PREFIX = "- governed artifact byte boundary:"
GOVERNED_ARTIFACT_BOUNDARY_RE = re.compile(
    r"^- governed artifact byte boundary: "
    r"path=`([^`\n]+)`; bytes=`([0-9]+)`$",
    re.MULTILINE,
)
TRIGGER_FIRED_DISPOSITION_RE = re.compile(
    r"\btrigger-fired disposition:\s*(?!none(?:\b|$))[^.;|]+",
    re.IGNORECASE,
)
STATE_PERMANENT_TAIL_MARKER = "<!-- STATE_ARCHIVE_PERMANENT_TAIL:START -->"
STATE_NUMBERED_HEADING_RE = re.compile(
    r"^(?P<level>##|###) (?P<section>[1-9][0-9]*[a-z]?)\.",
    re.MULTILINE,
)
STATE_SECTION_REFERENCE_RE = re.compile(
    r"\bSTATE(?:\.md)?\s+§(?P<section>[1-9][0-9]*[a-z]?)\b",
    re.IGNORECASE,
)
GOVERNED_ARTIFACT_ROW_SPECS = {
    "STATE.md": (
        DEFERRED_HEADING,
        "Deferred item",
        "Second STATE.md archival",
        "the export ceiling trigger fires, or STATE.md reaches its governed "
        "artifact byte boundary",
    ),
    "config/protected-artifacts.json": (
        DATED_DISPOSITIONS_HEADING,
        "subject",
        "protected evidence-manifest growth",
        "the manifest reaches its governed artifact byte boundary, or two "
        "consecutive clean ./run verify-artifacts runs each take ≥1.00 s real",
    ),
}


def module_forward_boundaries() -> dict[str, tuple[int, ...]]:
    """Derive tools/cycle_check.py module-global forward boundaries.

    This binding is deliberately module-scoped. A boundary declared in another
    module under tools/ is outside this derived namespace and remains a named
    residual rather than being silently represented as covered here.
    """
    return {
        name: value
        for name, value in globals().items()
        if name.endswith("_FORWARD_BOUNDARY")
    }


def check_trigger_boundary_relationship(errors: list[str]) -> None:
    # Invariant R12 control site: trigger boundary relationship.
    boundaries = module_forward_boundaries()
    registered = set(FORWARD_BOUNDARY_RELATIONSHIPS)
    for boundary_name in sorted(boundaries.keys() - registered):
        errors.append(
            "tools/cycle_check.py module-scoped forward-boundary registry is "
            f"missing {boundary_name}"
        )
    for boundary_name in sorted(registered - boundaries.keys()):
        errors.append(
            "tools/cycle_check.py module-scoped forward-boundary registry "
            f"names absent constant {boundary_name}"
        )

    for boundary_name in sorted(boundaries.keys() & registered):
        dependencies, reason = FORWARD_BOUNDARY_RELATIONSHIPS[boundary_name]
        if not reason.strip():
            errors.append(
                f"{boundary_name} forward-boundary relationship requires a "
                "stated reason"
            )
        if not dependencies and not reason.startswith("Independent:"):
            errors.append(
                f"{boundary_name} has no required relation and must be "
                "registered as Independent with a stated reason"
            )
        if len(dependencies) != len(set(dependencies)):
            errors.append(
                f"{boundary_name} forward-boundary relationship repeats a "
                "dependency"
            )
        for dependency_name in dependencies:
            if dependency_name == boundary_name:
                errors.append(
                    f"{boundary_name} cannot depend on its own forward boundary"
                )
                continue
            dependency_value = boundaries.get(dependency_name)
            if dependency_value is None:
                errors.append(
                    f"{boundary_name} requires unknown forward boundary "
                    f"{dependency_name}"
                )
                continue
            boundary_value = boundaries[boundary_name]
            if boundary_value < dependency_value:
                errors.append(
                    f"{boundary_name} must be greater than or equal to "
                    f"{dependency_name}"
                )


def check_trigger_table(
    path: Path,
    text: str,
    heading: str,
    subject_header: str,
    root: Path,
    errors: list[str],
    required_cycle_name: str | None = None,
) -> int:
    heading_matches = list(
        re.finditer(rf"^{re.escape(heading)}$", text, re.MULTILINE)
    )
    if len(heading_matches) != 1:
        errors.append(
            f"{shown(path, root)}: expected exactly one {heading!r}; "
            f"found {len(heading_matches)}"
        )
        return 0

    heading_level = len(heading) - len(heading.lstrip("#"))
    section_start = heading_matches[0].end()
    section = text[section_start:]
    next_heading = re.search(
        rf"^#{{1,{heading_level}}} ",
        section,
        re.MULTILINE,
    )
    if next_heading is not None:
        section = section[: next_heading.start()]

    lines = section.splitlines()
    header_index: int | None = None
    trigger_index: int | None = None
    measured_index: int | None = None
    expected_subject = subject_header.casefold()
    for index, line in enumerate(lines):
        cells = markdown_table_cells(line)
        normalized = [normalized_table_cell(cell).casefold() for cell in cells]
        if expected_subject not in normalized:
            continue
        header_index = index
        trigger_index = next(
            (
                cell_index
                for cell_index, cell in enumerate(normalized)
                if "trigger" in cell
            ),
            None,
        )
        measured_index = next(
            (
                cell_index
                for cell_index, cell in enumerate(normalized)
                if "measured" in cell
            ),
            None,
        )
        break
    if (
        header_index is None
        or trigger_index is None
        or measured_index is None
    ):
        errors.append(
            f"{shown(path, root)}: {heading!r} must contain a markdown "
            f"table with {subject_header}, trigger, and measured columns"
        )
        return 0

    trigger_rows = 0
    for offset, line in enumerate(lines[header_index + 1 :], header_index + 1):
        cells = markdown_table_cells(line)
        if not cells:
            if trigger_rows:
                break
            continue
        normalized = [normalized_table_cell(cell) for cell in cells]
        if normalized and all(
            MARKDOWN_TABLE_SEPARATOR_RE.fullmatch(cell) for cell in normalized
        ):
            continue
        if max(trigger_index, measured_index) >= len(normalized):
            continue
        trigger = normalized[trigger_index].casefold()
        if trigger in {"", "none", "n/a", "not applicable"}:
            continue
        trigger_rows += 1
        measured = normalized[measured_index]
        valid_dates = [
            raw
            for raw in ISO_DATE_TOKEN_RE.findall(measured)
            if valid_iso_date(raw)
        ]
        line_number = text[:section_start].count("\n") + offset + 1
        # Invariant R12 control site: trigger freshness.
        item = normalized[0] if normalized else "<unnamed>"
        missing_date_error = (
            f"{shown(path, root)}:{line_number}: trigger-bearing row "
            f"{item!r} requires a valid dated measured observation"
        )
        if not valid_dates:
            errors.append(missing_date_error)
        if (
            required_cycle_name is not None
            and required_cycle_name not in CYCLE_LITERAL_RE.findall(measured)
        ):
            errors.append(
                f"{shown(path, root)}:{line_number}: trigger-bearing row "
                f"{item!r} requires a measured observation naming active "
                f"cycle {required_cycle_name!r}"
            )
    return trigger_rows


def check_trigger_freshness(
    path: Path,
    active_text: str,
    root: Path,
    errors: list[str],
) -> tuple[int, int]:
    identity = resolve_cycle(root)
    required_cycle_name = (
        identity.name
        if (
            declared_scope_cycle_version(identity.name)
            >= TRIGGER_IDENTITY_FORWARD_BOUNDARY
        )
        else None
    )
    architecture = root / "ARCHITECTURE.md"
    architecture_text = (
        architecture.read_text() if architecture.is_file() else ""
    )
    architecture_rows = check_trigger_table(
        architecture,
        architecture_text,
        DATED_DISPOSITIONS_HEADING,
        "subject",
        root,
        errors,
        required_cycle_name,
    )
    deferral_rows = check_trigger_table(
        path,
        active_text,
        DEFERRED_HEADING,
        "Deferred item",
        root,
        errors,
        required_cycle_name,
    )
    return architecture_rows, deferral_rows


def governed_trigger_row(
    path: Path,
    text: str,
    heading: str,
    subject_header: str,
    subject_prefix: str,
    root: Path,
    errors: list[str],
) -> tuple[str, str] | None:
    heading_matches = list(
        re.finditer(rf"^{re.escape(heading)}$", text, re.MULTILINE)
    )
    if len(heading_matches) != 1:
        errors.append(
            f"{shown(path, root)}: expected exactly one {heading!r} while "
            f"resolving governed trigger row {subject_prefix!r}; found "
            f"{len(heading_matches)}"
        )
        return None
    heading_level = len(heading) - len(heading.lstrip("#"))
    section = text[heading_matches[0].end():]
    next_heading = re.search(
        rf"^#{{1,{heading_level}}} ",
        section,
        re.MULTILINE,
    )
    if next_heading is not None:
        section = section[: next_heading.start()]

    lines = section.splitlines()
    header_index: int | None = None
    subject_index: int | None = None
    trigger_index: int | None = None
    measured_index: int | None = None
    expected_subject_header = subject_header.casefold()
    for index, line in enumerate(lines):
        cells = markdown_table_cells(line)
        normalized = [normalized_table_cell(cell).casefold() for cell in cells]
        if expected_subject_header not in normalized:
            continue
        header_index = index
        subject_index = normalized.index(expected_subject_header)
        trigger_index = next(
            (
                cell_index
                for cell_index, cell in enumerate(normalized)
                if "trigger" in cell
            ),
            None,
        )
        measured_index = next(
            (
                cell_index
                for cell_index, cell in enumerate(normalized)
                if "measured" in cell
            ),
            None,
        )
        break
    if (
        header_index is None
        or subject_index is None
        or trigger_index is None
        or measured_index is None
    ):
        errors.append(
            f"{shown(path, root)}: {heading!r} must contain a markdown table "
            f"with {subject_header}, trigger, and measured columns while "
            f"resolving governed trigger row {subject_prefix!r}"
        )
        return None

    matches: list[tuple[str, str]] = []
    for line in lines[header_index + 1:]:
        cells = markdown_table_cells(line)
        if not cells:
            if matches:
                break
            continue
        normalized = [normalized_table_cell(cell) for cell in cells]
        if normalized and all(
            MARKDOWN_TABLE_SEPARATOR_RE.fullmatch(cell) for cell in normalized
        ):
            continue
        if max(subject_index, trigger_index, measured_index) >= len(normalized):
            continue
        if normalized[subject_index].casefold().startswith(
            subject_prefix.casefold()
        ):
            matches.append(
                (normalized[trigger_index], normalized[measured_index])
            )
    if len(matches) != 1:
        errors.append(
            f"{shown(path, root)}: expected exactly one governed trigger row "
            f"whose subject starts {subject_prefix!r}; found {len(matches)}"
        )
        return None
    return matches[0]


def checked_tree_label(root: Path) -> str:
    head_tree = git_output(root, "rev-parse", "HEAD^{tree}")
    dirty = git_output(
        root,
        "status",
        "--porcelain=v1",
        "--untracked-files=all",
    )
    if head_tree is None:
        return "unversioned-worktree"
    if dirty == "":
        return f"HEAD-tree:{head_tree}"
    return f"worktree-over-HEAD-tree:{head_tree}"


def check_governed_artifact_byte_boundaries(
    active_path: Path,
    active_text: str,
    root: Path,
    errors: list[str],
    *,
    checked_tree: str | None = None,
) -> tuple[str, list[str]]:
    matches = list(GOVERNED_ARTIFACT_BOUNDARY_RE.finditer(active_text))
    prefix_count = active_text.count(GOVERNED_ARTIFACT_BOUNDARY_PREFIX)
    if prefix_count != len(matches):
        errors.append(
            f"{shown(active_path, root)}: malformed governed artifact byte "
            f"boundary; found {prefix_count} field(s) but parsed "
            f"{len(matches)}"
        )
        return "invalid-authority", []

    boundaries: dict[str, int] = {}
    for match in matches:
        relative, raw_bytes = match.groups()
        if relative in boundaries:
            errors.append(
                f"{shown(active_path, root)}: governed artifact byte boundary "
                f"for {relative!r} is declared more than once"
            )
            continue
        boundaries[relative] = int(raw_bytes)
    required = set(GOVERNED_ARTIFACT_ROW_SPECS)
    if set(boundaries) != required:
        errors.append(
            f"{shown(active_path, root)}: governed artifact byte-boundary "
            f"authority must name exactly {sorted(required)!r}; found "
            f"{sorted(boundaries)!r}"
        )
        return "invalid-authority", []
    if any(value <= 0 for value in boundaries.values()):
        errors.append(
            f"{shown(active_path, root)}: governed artifact byte boundaries "
            "must be positive"
        )
        return "invalid-authority", []

    tree = checked_tree or checked_tree_label(root)
    architecture_path = root / "ARCHITECTURE.md"
    architecture_text = (
        architecture_path.read_text() if architecture_path.is_file() else ""
    )
    states: list[str] = []
    reports: list[str] = []
    for relative, boundary_bytes in boundaries.items():
        heading, subject_header, subject_prefix, expected_trigger = (
            GOVERNED_ARTIFACT_ROW_SPECS[relative]
        )
        row_path = active_path if heading == DEFERRED_HEADING else architecture_path
        row_text = active_text if heading == DEFERRED_HEADING else architecture_text
        row = governed_trigger_row(
            row_path,
            row_text,
            heading,
            subject_header,
            subject_prefix,
            root,
            errors,
        )
        if row is None:
            states.append("invalid-row")
            continue
        trigger, measured = row
        if trigger.casefold() != expected_trigger.casefold():
            errors.append(
                f"{shown(row_path, root)}: governed trigger row "
                f"{subject_prefix!r} must reference its single machine "
                "artifact byte-boundary authority instead of restating it"
            )

        artifact = root / relative
        if not artifact.is_file():
            errors.append(
                f"{shown(artifact, root)}: governed artifact is not a file"
            )
            states.append("missing-artifact")
            continue
        measured_bytes = artifact.stat().st_size
        state = "bound"
        # Invariant R12 control site: governed artifact byte boundary.
        if measured_bytes >= boundary_bytes:
            valid_dates = [
                raw
                for raw in ISO_DATE_TOKEN_RE.findall(measured)
                if valid_iso_date(raw)
            ]
            if (
                not valid_dates
                or TRIGGER_FIRED_DISPOSITION_RE.search(measured) is None
            ):
                errors.append(
                    f"{shown(artifact, root)}: measured {measured_bytes} bytes "
                    f"at checked_tree={tree}, meeting or exceeding governed "
                    f"boundary {boundary_bytes}; row {subject_prefix!r} "
                    "requires a dated 'trigger-fired disposition:'"
                )
                state = "trigger-fired-undisposed"
            else:
                state = "trigger-fired-disposed"
        states.append(state)
        timing = (
            "out-of-scope"
            if relative == "config/protected-artifacts.json"
            else "not-applicable"
        )
        reports.append(
            f"artifact-boundary: path={relative} bytes={measured_bytes} "
            f"boundary={boundary_bytes} state={state} checked_tree={tree} "
            f"timing={timing}"
        )
    overall = (
        "bound"
        if states and all(state == "bound" for state in states)
        else ",".join(states)
    )
    return overall, reports


def state_region_tracked_paths(root: Path) -> list[Path]:
    """Return live tracked files, excluding historical cycle/archive records."""
    listed = git_output(root, "ls-files")
    if listed is None:
        candidates = [path for path in root.rglob("*") if path.is_file()]
    else:
        candidates = [root / relative for relative in listed.splitlines()]
    historical = {
        path.resolve()
        for path in (*task_documents(root), *progress_records(root))
    }
    return [
        path
        for path in candidates
        if (
            path.resolve() not in historical
            and path.name != "STATE.md"
            and "tests" not in path.resolve().relative_to(root.resolve()).parts
            and not path.name.startswith("test_")
        )
        and not (
            len(path.resolve().relative_to(root.resolve()).parts) >= 2
            and path.resolve().relative_to(root.resolve()).parts[:2]
            == ("docs", "state-archive")
        )
    ]


def state_region_reference_inventory(
    root: Path,
) -> list[tuple[str, int, str]]:
    """Derive live external State section references from tracked text."""
    inventory: list[tuple[str, int, str]] = []
    for path in state_region_tracked_paths(root):
        try:
            text = path.read_text()
        except (OSError, UnicodeDecodeError):
            continue
        relative = shown(path, root)
        for match in STATE_SECTION_REFERENCE_RE.finditer(text):
            inventory.append(
                (
                    relative,
                    text.count("\n", 0, match.start()) + 1,
                    match.group("section").casefold(),
                )
            )
    return sorted(inventory)


def state_has_registered_current_restatement(
    root: Path,
    state_text: str,
) -> bool:
    """Delegate the current State restatement decision to version_check."""
    try:
        version_check.offline_msrv_report(
            root,
            text_overrides={"STATE.md": state_text},
        )
    except (OSError, ValueError) as error:
        return (
            "STATE.md: current run-reference correction yielded zero "
            "extracted current restatements"
        ) not in str(error)
    return True


def check_state_archival_region_contract(
    state_path: Path,
    state_text: str,
    root: Path,
    errors: list[str],
) -> str | None:
    """Derive and enforce State's header, movable append, and permanent tail."""
    header = STATE_HEADER_RE.search(state_text)
    if header is None:
        errors.append(
            f"{shown(state_path, root)}: State archival structural admission "
            "requires the status header; semantic current-restatement "
            "membership remains delegated to version-check and was not "
            "evaluated"
        )
        return None
    header_end = header.end()
    if state_text[header_end:].startswith("\n\n"):
        header_end += 2

    headings = list(STATE_NUMBERED_HEADING_RE.finditer(state_text))
    top_headings = [match for match in headings if match.group("level") == "##"]
    marker_matches = list(re.finditer(re.escape(STATE_PERMANENT_TAIL_MARKER), state_text))
    has_restatement = state_has_registered_current_restatement(root, state_text)
    # Invariant R12 control site: State archival permanent-tail boundary.
    if len(marker_matches) != 1:
        errors.append(
            f"{shown(state_path, root)}: State archival structural "
            "permanent-tail marker required exactly once; "
            f"found {len(marker_matches)}; semantic current-restatement "
            f"state={'present' if has_restatement else 'absent'} remains "
            "delegated to version-check"
        )
        return None
    if not marker_matches:
        if not top_headings:
            return None
        tail_start = top_headings[0].start()
        marker_end = tail_start
    else:
        tail_start = marker_matches[0].start()
        marker_end = marker_matches[0].end()

    tail_top_headings = [
        match for match in top_headings if match.start() >= marker_end
    ]
    if not tail_top_headings:
        errors.append(
            f"{shown(state_path, root)}: State permanent tail has no numbered "
            "top-level heading after its marker"
        )
        return None
    first_top = tail_top_headings[0]
    if state_text[marker_end:first_top.start()].strip():
        errors.append(
            f"{shown(state_path, root)}: State permanent-tail marker must "
            "immediately precede its first numbered top-level heading"
        )
        return None
    if any(match.start() < tail_start for match in top_headings):
        errors.append(
            f"{shown(state_path, root)}: numbered State top-level heading "
            "appears in the archival-eligible region"
        )
        return None
    if header_end >= tail_start:
        errors.append(
            f"{shown(state_path, root)}: State archival regions overlap or "
            "leave no eligible dated-append region"
        )
        return None

    anchors = [
        match.group("section").casefold()
        for match in headings
        if match.start() >= marker_end
    ]
    duplicate_anchors = sorted(
        anchor for anchor in set(anchors) if anchors.count(anchor) > 1
    )
    if duplicate_anchors:
        errors.append(
            f"{shown(state_path, root)}: duplicate permanent State section "
            f"anchors: {','.join(duplicate_anchors)}"
        )
        return None
    inventory = state_region_reference_inventory(root)
    missing = [
        f"{path}:{line}=§{section}"
        for path, line, section in inventory
        if section not in anchors
    ]
    if missing:
        errors.append(
            f"{shown(state_path, root)}: external State section references "
            f"do not resolve: {', '.join(missing)}"
        )
        return None

    top_numbers = [int(match.group("section")) for match in tail_top_headings]
    if top_numbers != sorted(set(top_numbers)):
        errors.append(
            f"{shown(state_path, root)}: permanent State top-level section "
            "ordinals must be unique and increasing"
        )
        return None
    numbering_gaps = sorted(
        set(range(top_numbers[0], top_numbers[-1] + 1)) - set(top_numbers)
    )
    referenced = sorted({section for _path, _line, section in inventory})
    referenced_gaps = [
        str(gap) for gap in numbering_gaps if str(gap) in referenced
    ]
    sites = ",".join(
        f"{path}:{line}=§{section}"
        for path, line, section in inventory
    ) or "none"
    return (
        "state-region-contract: "
        "structural=bound "
        f"semantic_current_restatement="
        f"{'present' if has_restatement else 'absent'} "
        "semantic_owner=version-check "
        f"header_bytes={len(state_text[:header_end].encode())} "
        f"eligible_bytes={len(state_text[header_end:tail_start].encode())} "
        f"tail_bytes={len(state_text[tail_start:].encode())} "
        f"top_sections={','.join(str(number) for number in top_numbers)} "
        f"numbering_gaps={','.join(str(gap) for gap in numbering_gaps) or 'none'} "
        f"referenced_sections={','.join(referenced) or 'none'} "
        f"referenced_gaps={','.join(referenced_gaps) or 'none'} "
        f"reference_sites={sites}"
    )


def governed_export_row_value(
    path: Path,
    text: str,
    root: Path,
    errors: list[str],
) -> int | None:
    heading_matches = list(
        re.finditer(
            rf"^{re.escape(DATED_DISPOSITIONS_HEADING)}$",
            text,
            re.MULTILINE,
        )
    )
    if len(heading_matches) != 1:
        return None
    section = text[heading_matches[0].end():]
    next_heading = re.search(r"^#{1,3} ", section, re.MULTILINE)
    if next_heading is not None:
        section = section[: next_heading.start()]

    lines = section.splitlines()
    header_index: int | None = None
    subject_index: int | None = None
    measured_index: int | None = None
    for index, line in enumerate(lines):
        cells = markdown_table_cells(line)
        normalized = [normalized_table_cell(cell).casefold() for cell in cells]
        if "subject" not in normalized:
            continue
        header_index = index
        subject_index = normalized.index("subject")
        measured_index = next(
            (
                cell_index
                for cell_index, cell in enumerate(normalized)
                if "measured" in cell
            ),
            None,
        )
        break
    if (
        header_index is None
        or subject_index is None
        or measured_index is None
    ):
        return None

    matching_cells: list[str] = []
    for line in lines[header_index + 1:]:
        cells = markdown_table_cells(line)
        if not cells:
            if matching_cells:
                break
            continue
        normalized = [normalized_table_cell(cell) for cell in cells]
        if normalized and all(
            MARKDOWN_TABLE_SEPARATOR_RE.fullmatch(cell) for cell in normalized
        ):
            continue
        if max(subject_index, measured_index) >= len(normalized):
            continue
        if normalized[subject_index].casefold().startswith(
            GOVERNED_EXPORT_SUBJECT_PREFIX
        ):
            matching_cells.append(cells[measured_index])

    if len(matching_cells) != 1:
        errors.append(
            f"{shown(path, root)}: expected exactly one governed export row "
            f"whose subject starts {GOVERNED_EXPORT_SUBJECT_PREFIX!r}; "
            f"found {len(matching_cells)}"
        )
        return None

    measured = matching_cells[0]
    marker_matches = GOVERNED_EXPORT_ROW_MARKER_RE.findall(measured)
    prose_matches = GOVERNED_EXPORT_ROW_PROSE_RE.findall(measured)
    if len(marker_matches) != 1 or len(prose_matches) != 1:
        errors.append(
            f"{shown(path, root)}: governed export row requires exactly one "
            "machine byte marker and one visible 'export of **N bytes' value"
        )
        return None
    marker_value = int(marker_matches[0])
    prose_value = int(prose_matches[0].replace(",", ""))
    if marker_value != prose_value:
        errors.append(
            f"{shown(path, root)}: governed export row machine value "
            f"{marker_value} disagrees with visible value {prose_value}"
        )
        return None
    return marker_value


def check_governed_export_margin(
    architecture_path: Path,
    architecture_text: str,
    progress_path: Path,
    progress_text: str,
    cycle_state: str,
    root: Path,
    errors: list[str],
) -> str:
    row_value = governed_export_row_value(
        architecture_path,
        architecture_text,
        root,
        errors,
    )
    measurements = list(GOVERNED_EXPORT_PROGRESS_RE.finditer(progress_text))
    prefix_count = progress_text.count(GOVERNED_EXPORT_PROGRESS_PREFIX)
    if prefix_count != len(measurements):
        errors.append(
            f"{shown(progress_path, root)}: malformed governed review-export "
            f"measurement; found {prefix_count} field(s) but parsed "
            f"{len(measurements)}"
        )
        return "invalid-progress-measurement"
    cycle_ending_audits = list(
        CYCLE_ENDING_EXPORT_AUDIT_RE.finditer(progress_text)
    )
    audit_prefix_count = progress_text.count(CYCLE_ENDING_EXPORT_AUDIT_PREFIX)
    if audit_prefix_count != len(cycle_ending_audits):
        errors.append(
            f"{shown(progress_path, root)}: malformed cycle-ending "
            f"review-export audit; found {audit_prefix_count} field(s) but "
            f"parsed {len(cycle_ending_audits)}"
        )
        return "invalid-cycle-ending-audit"
    if len(cycle_ending_audits) > 1:
        errors.append(
            f"{shown(progress_path, root)}: expected at most one cycle-ending "
            f"review-export audit; found {len(cycle_ending_audits)}"
        )
        return "duplicate-cycle-ending-audit"
    if row_value is None:
        return "invalid-architecture-row"
    # Invariant R12 control site: governed written-figure export ceiling.
    if row_value > MAX_EXPORT_BYTES:
        errors.append(
            f"{shown(architecture_path, root)}: recorded governed "
            f"review-export figure {row_value} exceeds the "
            f"{MAX_EXPORT_BYTES}-byte ceiling; this constrains the written "
            "figure at the checked tree and does not measure an export"
        )
        return "recorded-figure-over-ceiling"

    if cycle_state == "open":
        if cycle_ending_audits:
            errors.append(
                f"{shown(progress_path, root)}: cycle-ending review-export "
                "audit is unavailable while the active cycle is open"
            )
            return "open-cycle-ending-audit"
        if not measurements:
            return "exempt-open-empty-progress"
        return "exempt-open-latest-at-close"
    if cycle_state != "closed":
        return "not-applicable"
    if not measurements:
        errors.append(
            f"{shown(progress_path, root)}: closed cycle has no governed "
            "review-export measurement; the open-cycle empty-progress "
            "exemption is unavailable"
        )
        return "missing-closed-progress-measurement"
    # Invariant R12 control site: cycle-ending review-export audit ordering.
    if (
        cycle_ending_audits
        and cycle_ending_audits[0].start() < measurements[-1].end()
    ):
        errors.append(
            f"{shown(progress_path, root)}: cycle-ending review-export audit "
            "must follow the last governed review-export measurement at the "
            "checked tree"
        )
        return "misordered-cycle-ending-audit"

    latest = measurements[-1]
    latest_tree = latest.group(1)
    latest_value = int(latest.group(2))
    # Invariant R12 control site: governed review-export latest-at-close.
    if row_value != latest_value:
        errors.append(
            f"{shown(architecture_path, root)}: governed review-export row is "
            f"superseded: row={row_value}, latest_progress={latest_value}, "
            f"tree={latest_tree}"
        )
        return "superseded"
    if cycle_ending_audits:
        return "bound-with-cycle-ending-audit"
    return "bound"


def check_governed_export_margin_kind(
    architecture_path: Path,
    architecture_text: str,
    root: Path,
    errors: list[str],
) -> str | None:
    """Bind an evaluated margin to the latest positive same-kind basis."""
    matches = list(GOVERNED_EXPORT_MARGIN_SERIES_RE.finditer(architecture_text))
    if len(matches) != 1:
        errors.append(
            f"{shown(architecture_path, root)}: governed export row requires "
            "exactly one executable Review-export margin series; only "
            "governed→governed is supported because closing and delivered "
            "exports have no common in-repository measurement authority"
        )
        return None

    match = matches[0]
    line_start = architecture_text.rfind("\n", 0, match.start()) + 1
    line_end = architecture_text.find("\n", match.end())
    if line_end < 0:
        line_end = len(architecture_text)
    margin_cells = markdown_table_cells(
        architecture_text[line_start:line_end]
    )
    if (
        not any(
            normalized_table_cell(cell).casefold().startswith(
                GOVERNED_EXPORT_SUBJECT_PREFIX
            )
            for cell in margin_cells
        )
        or not any(
            match.group(0) in cell
            and GOVERNED_EXPORT_ROW_MARKER_RE.search(cell) is not None
            for cell in margin_cells
        )
    ):
        errors.append(
            f"{shown(architecture_path, root)}: executable Review-export "
            "margin series must be in the governed export row's measured cell"
        )
        return None
    prior_relative = Path(match.group(2))
    prior_value = int(match.group(3))
    current_relative = Path(match.group(4))
    current_value = int(match.group(5))
    evaluated_relative = Path(match.group(6))
    evaluated_value = int(match.group(7))
    denominator = int(match.group(8))
    numerator = int(match.group(9))
    displayed_cycles = Decimal(match.group(10))
    relative_paths = (
        prior_relative,
        current_relative,
        evaluated_relative,
    )
    if any(
        path.is_absolute()
        or ".." in path.parts
        or not path.as_posix().startswith("docs/cycles/PROGRESS-v")
        or path.suffix != ".md"
        for path in relative_paths
    ):
        errors.append(
            f"{shown(architecture_path, root)}: governed export margin "
            "progress sources must be safe docs/cycles/PROGRESS-v*.md paths"
        )
        return None
    if prior_relative == current_relative:
        errors.append(
            f"{shown(architecture_path, root)}: governed export margin must "
            "name distinct prior and current progress sources"
        )
        return None

    recorded_values: list[int] = []
    source_versions: list[tuple[int, ...]] = []
    for relative in relative_paths:
        version_match = GOVERNED_EXPORT_PROGRESS_PATH_RE.fullmatch(
            relative.as_posix()
        )
        if version_match is None:
            errors.append(
                f"{shown(architecture_path, root)}: governed export margin "
                f"source {relative.as_posix()} has no parseable cycle version"
            )
            return None
        source_versions.append(
            tuple(int(part) for part in version_match.group(1).split("."))
        )
        source = root / relative
        if not source.is_file():
            errors.append(
                f"{shown(architecture_path, root)}: governed export margin "
                f"source {relative.as_posix()} is not a file"
            )
            return None
        source_text = source.read_text()
        source_measurements = list(
            GOVERNED_EXPORT_PROGRESS_RE.finditer(source_text)
        )
        if (
            source_text.count(GOVERNED_EXPORT_PROGRESS_PREFIX)
            != len(source_measurements)
            or not source_measurements
        ):
            errors.append(
                f"{shown(architecture_path, root)}: governed export margin "
                f"source {relative.as_posix()} has no valid governed "
                "measurement series"
            )
            return None
        recorded_values.append(int(source_measurements[-1].group(2)))

    # Invariant R12 control site: governed review-export same-kind margin.
    if recorded_values != [prior_value, current_value, evaluated_value]:
        errors.append(
            f"{shown(architecture_path, root)}: governed export margin mixes "
            "or misstates measurement series: "
            f"declared={prior_value}→{current_value}@{evaluated_value}, "
            f"recorded={recorded_values[0]}→{recorded_values[1]}"
            f"@{recorded_values[2]}"
        )
        return None

    evaluated_version = source_versions[2]
    if evaluated_version < source_versions[1]:
        errors.append(
            f"{shown(architecture_path, root)}: governed export margin "
            "evaluation cycle precedes its denominator basis"
        )
        return None

    governed_series: dict[tuple[int, ...], tuple[Path, int]] = {}
    for source in sorted((root / "docs" / "cycles").glob("PROGRESS-v*.md")):
        relative = source.relative_to(root)
        version_match = GOVERNED_EXPORT_PROGRESS_PATH_RE.fullmatch(
            relative.as_posix()
        )
        if version_match is None:
            continue
        version = tuple(
            int(part) for part in version_match.group(1).split(".")
        )
        if version > evaluated_version:
            continue
        source_text = source.read_text()
        measurements = list(GOVERNED_EXPORT_PROGRESS_RE.finditer(source_text))
        if measurements:
            governed_series[version] = (
                relative,
                int(measurements[-1].group(2)),
            )
    positive_pairs: list[tuple[tuple[int, ...], Path, Path]] = []
    for version, (relative, value) in governed_series.items():
        if version[-1] == 0:
            continue
        previous_version = (*version[:-1], version[-1] - 1)
        previous = governed_series.get(previous_version)
        if previous is not None and value > previous[1]:
            positive_pairs.append((version, previous[0], relative))
    if not positive_pairs:
        errors.append(
            f"{shown(architecture_path, root)}: governed export margin has "
            "no positive adjacent-cycle governed denominator basis"
        )
        return None
    _latest_version, latest_prior, latest_current = max(positive_pairs)
    # Invariant R12 control site: governed review-export margin basis selection.
    if (prior_relative, current_relative) != (latest_prior, latest_current):
        errors.append(
            f"{shown(architecture_path, root)}: governed export margin must "
            "use the latest positive adjacent-cycle governed pair; "
            f"declared={prior_relative.as_posix()}→"
            f"{current_relative.as_posix()}, latest={latest_prior.as_posix()}→"
            f"{latest_current.as_posix()}"
        )
        return None

    governed_values = GOVERNED_EXPORT_ROW_MARKER_RE.findall(architecture_text)
    if len(governed_values) != 1 or int(governed_values[0]) != evaluated_value:
        errors.append(
            f"{shown(architecture_path, root)}: governed export margin "
            f"evaluated value {evaluated_value} does not equal the governed "
            "row value"
        )
        return None
    expected_denominator = current_value - prior_value
    if expected_denominator <= 0 or denominator != expected_denominator:
        errors.append(
            f"{shown(architecture_path, root)}: governed export margin "
            f"denominator {denominator} disagrees with same-kind delta "
            f"{expected_denominator}"
        )
        return None
    try:
        attention = export_attention_boundary(root)
        attention_measured = governed_export_measured_cell(root)
    except ExportCheckError as error:
        errors.append(f"{shown(architecture_path, root)}: {error}")
        return None
    if attention.denominator_bytes_per_cycle != expected_denominator:
        errors.append(
            f"{shown(architecture_path, root)}: review-export attention "
            f"denominator {attention.denominator_bytes_per_cycle} disagrees "
            f"with latest positive adjacent governed delta "
            f"{expected_denominator}"
        )
        return None
    attention_errors = export_attention_errors(
        evaluated_value,
        attention.boundary_bytes,
        attention_measured,
    )
    if attention_errors:
        errors.extend(
            f"{shown(architecture_path, root)}: recorded governed {error}"
            for error in attention_errors
        )
        return None
    expected_numerator = MAX_EXPORT_BYTES - evaluated_value
    if numerator != expected_numerator:
        errors.append(
            f"{shown(architecture_path, root)}: governed export margin "
            f"numerator {numerator} disagrees with ceiling remainder "
            f"{expected_numerator}"
        )
        return None
    expected_cycles = (
        Decimal(numerator) / Decimal(denominator)
    ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    if displayed_cycles != expected_cycles:
        errors.append(
            f"{shown(architecture_path, root)}: governed export margin cycles "
            f"{displayed_cycles} disagree with same-kind quotient "
            f"{expected_cycles}"
        )
        return None
    return (
        "governed-export-margin-basis: "
        "selected=latest-positive-adjacent-governed-pair "
        f"attention_boundary={attention.boundary_bytes} "
        "representativeness=unbounded(single adjacent pair carries no "
        "representativeness guarantee) "
        "structural_epoch=unobserved(checker cannot detect a basis "
        "predating a structural change)"
    )


def governed_trigger_subjects(
    text: str,
    heading: str,
    subject_header: str,
) -> dict[str, str]:
    heading_matches = list(
        re.finditer(rf"^{re.escape(heading)}$", text, re.MULTILINE)
    )
    if len(heading_matches) != 1:
        return {}
    heading_level = len(heading) - len(heading.lstrip("#"))
    section = text[heading_matches[0].end():]
    next_heading = re.search(
        rf"^#{{1,{heading_level}}} ",
        section,
        re.MULTILINE,
    )
    if next_heading is not None:
        section = section[: next_heading.start()]
    lines = section.splitlines()
    header_index: int | None = None
    subject_index: int | None = None
    trigger_index: int | None = None
    expected_subject = subject_header.casefold()
    for index, line in enumerate(lines):
        cells = markdown_table_cells(line)
        normalized = [normalized_table_cell(cell).casefold() for cell in cells]
        if expected_subject not in normalized:
            continue
        header_index = index
        subject_index = normalized.index(expected_subject)
        trigger_index = next(
            (
                cell_index
                for cell_index, cell in enumerate(normalized)
                if "trigger" in cell
            ),
            None,
        )
        break
    if (
        header_index is None
        or subject_index is None
        or trigger_index is None
    ):
        return {}

    subjects: dict[str, str] = {}
    for line in lines[header_index + 1:]:
        cells = markdown_table_cells(line)
        if not cells:
            if subjects:
                break
            continue
        normalized = [normalized_table_cell(cell) for cell in cells]
        if normalized and all(
            MARKDOWN_TABLE_SEPARATOR_RE.fullmatch(cell) for cell in normalized
        ):
            continue
        if max(subject_index, trigger_index) >= len(normalized):
            continue
        trigger = normalized[trigger_index].casefold()
        if trigger in {"", "none", "n/a", "not applicable"}:
            continue
        subject = normalized[subject_index]
        subjects[subject.casefold()] = subject
    return subjects


def dated_deferred_completions(text: str) -> dict[str, str]:
    heading_matches = list(
        re.finditer(
            rf"^{re.escape(DEFERRED_COMPLETIONS_HEADING)}$",
            text,
            re.MULTILINE,
        )
    )
    if len(heading_matches) != 1:
        return {}
    section = text[heading_matches[0].end():]
    next_heading = re.search(r"^## ", section, re.MULTILINE)
    if next_heading is not None:
        section = section[: next_heading.start()]
    lines = section.splitlines()
    header_index: int | None = None
    subject_index: int | None = None
    completion_index: int | None = None
    for index, line in enumerate(lines):
        cells = markdown_table_cells(line)
        normalized = [normalized_table_cell(cell).casefold() for cell in cells]
        if "deferred item" not in normalized:
            continue
        header_index = index
        subject_index = normalized.index("deferred item")
        completion_index = next(
            (
                cell_index
                for cell_index, cell in enumerate(normalized)
                if "completion" in cell
            ),
            None,
        )
        break
    if (
        header_index is None
        or subject_index is None
        or completion_index is None
    ):
        return {}

    completed: dict[str, str] = {}
    for line in lines[header_index + 1:]:
        cells = markdown_table_cells(line)
        if not cells:
            if completed:
                break
            continue
        normalized = [normalized_table_cell(cell) for cell in cells]
        if normalized and all(
            MARKDOWN_TABLE_SEPARATOR_RE.fullmatch(cell) for cell in normalized
        ):
            continue
        if max(subject_index, completion_index) >= len(normalized):
            continue
        completion = normalized[completion_index]
        if not any(
            valid_iso_date(raw)
            for raw in ISO_DATE_TOKEN_RE.findall(completion)
        ):
            continue
        subject = normalized[subject_index]
        completed[subject.casefold()] = subject
    return completed


def check_deferred_carry_forward(
    active_path: Path,
    active_text: str,
    root: Path,
    errors: list[str],
) -> None:
    active_version = cycle_version(active_path)
    if active_version is None:
        return
    prior_candidates = [
        (version, path)
        for path in execution_runbooks(root)
        if (
            (version := cycle_version(path)) is not None
            and version < active_version
        )
    ]
    if not prior_candidates:
        return
    _, prior_path = max(prior_candidates, key=lambda candidate: candidate[0])
    prior_subjects = governed_trigger_subjects(
        prior_path.read_text(),
        DEFERRED_HEADING,
        "Deferred item",
    )
    active_subjects = governed_trigger_subjects(
        active_text,
        DEFERRED_HEADING,
        "Deferred item",
    )
    completed_subjects = dated_deferred_completions(active_text)
    for key, subject in sorted(prior_subjects.items()):
        # Invariant R12 control site: deferred trigger carry-forward.
        if key not in active_subjects and key not in completed_subjects:
            errors.append(
                f"{shown(active_path, root)}: deferred subject {subject!r} "
                f"from immediately prior {shown(prior_path, root)} is absent "
                "without a valid dated completion"
            )


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
                    f"{', '.join(sorted(referenced_steps, key=step_sort_key))}'s "
                    "recorded/measured quantity; assert the invariant relation "
                    "at the same commit instead"
                )


def run(
    root: Path = ROOT,
    *,
    verify_local_tag_refs: bool = True,
    hosted_ref_topology: bool | None = None,
) -> int:
    root = root.resolve()
    if hosted_ref_topology is None:
        hosted_ref_topology = os.environ.get("GITHUB_ACTIONS") == "true"
    errors: list[str] = []
    try:
        identity = resolve_cycle(root)
    except CycleIdentityError as error:
        print(f"cycle-check: ERROR: {error}", file=sys.stderr)
        return 1
    check_contract_cycle_paths(identity, root, errors)
    check_source_cycle_literals(root, errors)
    check_review_export_retention_pattern(root, identity.name, errors)

    for required in (identity.runbook, identity.progress):
        if not required.is_file():
            errors.append(
                f"{shown(required, root)}: declared {identity.name} target "
                "does not exist"
            )

    execution_files = execution_runbooks(root)
    state_path = root / "STATE.md"
    withheld_releases = check_withheld_release_records(
        state_path,
        state_path.read_text() if state_path.is_file() else "",
        execution_files,
        root,
        errors,
    )
    active_state = "missing"
    governed_export_state = "not-applicable"
    artifact_boundary_state = "not-applicable"
    artifact_boundary_reports: list[str] = []
    state_region_report: str | None = None
    governed_export_basis_report: str | None = None
    if identity.runbook.is_file():
        active_text = identity.runbook.read_text()
        architecture_trigger_rows = 0
        deferral_trigger_rows = 0
        check_trigger_boundary_relationship(errors)
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
        if declared_scope_cycle_version(identity.name) >= SCOPE_FORWARD_BOUNDARY:
            check_declared_scope(
                identity,
                identity.runbook,
                active_text,
                root,
                errors,
            )
        if (
            declared_scope_cycle_version(identity.name)
            >= TRIGGER_FRESHNESS_FORWARD_BOUNDARY
        ):
            architecture_trigger_rows, deferral_trigger_rows = (
                check_trigger_freshness(
                    identity.runbook,
                    active_text,
                    root,
                    errors,
                )
            )
        if (
            declared_scope_cycle_version(identity.name)
            >= TRIGGER_FLOOR_FORWARD_BOUNDARY
        ):
            if architecture_trigger_rows == 0:
                errors.append(
                    f"{shown(root / 'ARCHITECTURE.md', root)}: "
                    f"{DATED_DISPOSITIONS_HEADING!r} must contain at least "
                    "one trigger-bearing row"
                )
            if deferral_trigger_rows == 0:
                errors.append(
                    f"{shown(identity.runbook, root)}: {DEFERRED_HEADING!r} "
                    "must contain at least one trigger-bearing row"
                )
            check_deferred_carry_forward(
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
                verify_local_tag_refs=verify_local_tag_refs,
                require_dated_disposition=True,
                require_tagged_closing_commit=True,
                withheld_releases=withheld_releases,
                hosted_ref_topology=hosted_ref_topology,
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
        if (
            declared_scope_cycle_version(identity.name)
            >= ARTIFACT_BYTE_BOUNDARY_FORWARD_BOUNDARY
        ):
            artifact_boundary_state, artifact_boundary_reports = (
                check_governed_artifact_byte_boundaries(
                    identity.runbook,
                    active_text,
                    root,
                    errors,
                )
            )
        if (
            declared_scope_cycle_version(identity.name)
            >= STATE_REGION_CONTRACT_FORWARD_BOUNDARY
        ):
            state_region_report = check_state_archival_region_contract(
                state_path,
                state_path.read_text() if state_path.is_file() else "",
                root,
                errors,
            )
        if (
            declared_scope_cycle_version(identity.name)
            >= GOVERNED_EXPORT_FORWARD_BOUNDARY
        ):
            architecture_path = root / "ARCHITECTURE.md"
            architecture_text = (
                architecture_path.read_text()
                if architecture_path.is_file()
                else ""
            )
            progress_text = (
                identity.progress.read_text()
                if identity.progress.is_file()
                else ""
            )
            governed_export_state = check_governed_export_margin(
                architecture_path,
                architecture_text,
                identity.progress,
                progress_text,
                active_state,
                root,
                errors,
            )
            governed_export_basis_report = check_governed_export_margin_kind(
                architecture_path,
                architecture_text,
                root,
                errors,
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
            verify_local_tag_refs=verify_local_tag_refs,
            withheld_releases=withheld_releases,
            hosted_ref_topology=hosted_ref_topology,
        )
        check_authority(path, text, root, errors)

    publication_status_report = check_publication_status(
        root,
        execution_files,
        errors,
        verify_local_tag_refs,
        withheld_releases,
        hosted_ref_topology,
    )

    plain_task_files = [
        path
        for path in task_documents(root)
        if not path.name.endswith("-EXECUTION.md")
    ]
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
    expected_deferred = progress_records(root)
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

    for report in artifact_boundary_reports:
        print(f"cycle-check: {report}")
    if state_region_report is not None:
        print(f"cycle-check: {state_region_report}")
    if governed_export_basis_report is not None:
        print(f"cycle-check: {governed_export_basis_report}")
    if publication_status_report is not None:
        print(f"cycle-check: {publication_status_report}")

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
        f"ref_topology={'hosted' if hosted_ref_topology else 'local'}, "
        f"runbook={shown(identity.runbook, root)}, "
        f"progress={shown(identity.progress, root)}, "
        f"artifact_boundaries={artifact_boundary_state}, "
        f"state_regions={'bound' if state_region_report else 'not-measured'}, "
        f"governed_export={governed_export_state}, "
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
