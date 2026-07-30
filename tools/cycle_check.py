#!/usr/bin/env python3
"""Verify that cycle identity, runbook lifecycle, and tool targets agree."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import subprocess
import sys
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
from tools.export_check import CYCLE_RETENTION_DEPTH
from tools.progress_check import default_progress_path


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
    )


def cycle_version(path: Path) -> tuple[int, ...] | None:
    match = EXECUTION_CYCLE_RE.fullmatch(path.name)
    if match is None:
        return None
    return tuple(int(part) for part in match.group(1).split("."))


def newest_closed_release(
    execution_files: list[Path],
) -> ClosedRelease | None:
    closed: list[tuple[tuple[int, ...], Path, str]] = []
    for path in execution_files:
        text = path.read_text()
        version = cycle_version(path)
        if (
            version is None
            or UNCHECKED_RE.search(text) is not None
            or text.count(CLOSING_HEADING) != 1
        ):
            continue
        closed.append(
            (version, path, text.split(CLOSING_HEADING, 1)[1])
        )
    if not closed:
        return None
    _, path, section = max(closed, key=lambda item: item[0])
    disposition = DATED_DISPOSITION_RE.search(section)
    if disposition is None:
        disposition = LEGACY_DISPOSITION_RE.search(section)
    if disposition is None or disposition.group(1) != "release":
        return None
    release = RELEASE_RE.search(section)
    commit = RELEASE_COMMIT_RE.search(section)
    tag_objects = list(TAG_OBJECT_RE.finditer(section))
    if release is None or commit is None or len(tag_objects) > 1:
        return None
    return ClosedRelease(
        runbook=path,
        tag=release.group(2),
        release_commit=commit.group(1),
        recorded_tag_object=(
            tag_objects[0].group(1) if tag_objects else None
        ),
    )


def check_publication_status(
    root: Path,
    execution_files: list[Path],
    errors: list[str],
) -> None:
    """Reconcile the status header with the newest reachable closed release."""
    release = newest_closed_release(execution_files)
    if release is None:
        return
    runbook = release.runbook
    tag = release.tag
    release_commit = release.release_commit
    recorded_object = release.recorded_tag_object
    state_path = root / "STATE.md"
    if not state_path.is_file():
        return
    state_text = state_path.read_text()
    header_match = STATE_HEADER_RE.search(state_text)
    if header_match is None:
        return
    header = header_match.group(0)

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

    measured_object = git_output(root, "rev-parse", tag)
    # Invariant R12 control site: unavailable annotated-tag ref.
    if measured_object is None:
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
    if PENDING_PUBLICATION_RE.search(header) is not None:
        errors.append(
            f"{shown(state_path, root)}: publication disposition agreement: "
            f"newest closed release {tag} in {shown(runbook, root)} is an "
            "annotated tag reachable from HEAD, but the status header asserts "
            "publication is pending or outstanding"
        )

    # Rule 2: a legacy release header retains both immutable tag hashes. A
    # tagged-closing release instead asserts the already-known release commit;
    # its tag object and closing target cannot exist until after that tree is
    # committed and therefore belong to the dated post-push record below.
    if release.uses_tagged_closing_commit:
        assertions_to_check = TAGGED_CLOSING_STATE_REF_ASSERTIONS
        expected = {"release commit": release_commit}
    else:
        assertions_to_check = LEGACY_STATE_REF_ASSERTIONS
        expected = {
            "annotated tag object": measured_object,
            "tag target": measured_target,
        }
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

    if not release.uses_tagged_closing_commit:
        return
    head = git_output(root, "rev-parse", "HEAD")
    if head is None:
        errors.append(
            f"{shown(state_path, root)}: publication verification unavailable: "
            "HEAD cannot be resolved"
        )
        return
    # The tagged closing commit is allowed to carry only the already-known
    # release commit. Once HEAD advances, the dated forward record is mandatory
    # and pins the values that came into existence after that commit.
    # Invariant R12 control site: required and fresh post-push record.
    if head != measured_target:
        records = [
            match
            for match in POST_PUSH_RECORD_RE.finditer(state_text)
            if match.group(3) == tag
        ]
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


def expected_review_export_retention_pattern(cycle_name: str) -> str:
    """Derive the one Repomix exclusion pattern from cycle identity and depth."""
    version = declared_scope_cycle_version(cycle_name)
    if len(version) < 2:
        raise ValueError(f"cannot derive review retention for {cycle_name!r}")
    last_excluded = version[-1] - CYCLE_RETENTION_DEPTH
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
        expected = expected_review_export_retention_pattern(cycle_name)
    except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError) as error:
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
            f"{cycle_name} must be {expected!r}; found {retention_patterns!r}"
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
DATED_DISPOSITIONS_HEADING = "### Dated operational-residual dispositions"
DEFERRED_COMPLETIONS_HEADING = "## Deferred completions"
ISO_DATE_TOKEN_RE = re.compile(r"\b[0-9]{4}-[0-9]{2}-[0-9]{2}\b")


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
        if required_cycle_name is None and not valid_dates:
            errors.append(missing_date_error)
        if required_cycle_name is not None and not valid_dates:
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
    check_review_export_retention_pattern(root, identity.name, errors)

    for required in (identity.runbook, identity.progress):
        if not required.is_file():
            errors.append(
                f"{shown(required, root)}: declared {identity.name} target "
                "does not exist"
            )

    execution_files = execution_runbooks(root)
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
                verify_local_tag_refs,
                require_dated_disposition=True,
                require_tagged_closing_commit=True,
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

    check_publication_status(root, execution_files, errors)

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
