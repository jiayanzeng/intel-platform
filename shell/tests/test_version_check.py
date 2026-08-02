from __future__ import annotations

from pathlib import Path

import pytest

from tools import version_check


ROOT = Path(__file__).resolve().parents[2]


def _replace_extracted_version(
    spec: version_check.RustVersionSpec,
    text: str,
    replacement: str,
) -> str:
    match = spec.pattern.search(text)
    assert match is not None
    return (
        text[: match.start("version")]
        + replacement
        + text[match.end("version") :]
    )


def test_offline_msrv_binds_exact_authorities_and_current_restatements() -> None:
    report = version_check.offline_msrv_report(ROOT)

    assert {pin.raw for pin in report.pins} == {"1.78.0"}
    assert {pin.normalized for pin in report.pins} == {report.derived}
    assert report.derived == "1.78"
    assert len(report.pins) == 3
    assert len(report.restatements) == len(
        version_check.OFFLINE_MSRV_RESTATEMENTS
    )
    assert {
        restatement.normalized for restatement in report.restatements
    } == {report.derived}


@pytest.mark.parametrize("authority", version_check.OFFLINE_MSRV_AUTHORITIES)
def test_offline_msrv_rejects_an_authority_with_zero_extracted_pins(
    authority: version_check.RustVersionSpec,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            rf"{authority.path}: {authority.label} yielded zero extracted "
            r"executable pins"
        ),
    ):
        version_check.offline_msrv_report(
            ROOT,
            text_overrides={authority.path: ""},
        )


def test_offline_msrv_rejects_disagreeing_normalized_pins() -> None:
    authority = version_check.OFFLINE_MSRV_AUTHORITIES[1]
    original = (ROOT / authority.path).read_text()
    stale = _replace_extracted_version(authority, original, "1.79")

    with pytest.raises(
        ValueError,
        match="offline MSRV executable pins disagree after normalization",
    ):
        version_check.offline_msrv_report(
            ROOT,
            text_overrides={authority.path: stale},
        )


def test_offline_msrv_rejects_a_stale_current_restatement() -> None:
    restatement = next(
        spec
        for spec in version_check.OFFLINE_MSRV_RESTATEMENTS
        if spec.path == "README.md"
    )
    original = (ROOT / restatement.path).read_text()
    stale = _replace_extracted_version(restatement, original, "1.77")

    with pytest.raises(
        ValueError,
        match=(
            r"README\.md: offline toolchain table states 1\.77->1\.77, "
            r"but executable offline MSRV pins derive 1\.78"
        ),
    ):
        version_check.offline_msrv_report(
            ROOT,
            text_overrides={restatement.path: stale},
        )


def test_rust_floor_partition_classifies_every_tracked_literal_file() -> None:
    report = version_check.rust_floor_partition_report(ROOT)

    assert report.files
    assert all(item.memberships for item in report.files)
    assert all(
        item.selected == item.memberships[0]
        for item in report.files
    )
    assert "1.75" in report.context_versions
    assert report.context_only_occurrences > 0
    assert report.context_classification_decisions == 0


def test_rust_floor_context_registry_does_not_enumerate_wrong_values() -> None:
    patterns = b"\n".join(
        context.pattern.pattern
        for context in version_check.RUST_FLOOR_CONTEXTS
    )

    assert b"1.75" not in patterns
    assert b"1.77" not in patterns


def test_rust_floor_partition_rejects_a_wrong_context_value() -> None:
    path = "tools/export_check.py"
    original = (ROOT / path).read_text()

    with pytest.raises(
        ValueError,
        match=(
            r"tools/export_check\.py: floor-shaped context value\(s\) "
            r"\['1\.75'\] yielded zero file-level classifications"
        ),
    ):
        version_check.rust_floor_partition_report(
            ROOT,
            text_overrides={
                path: original + "\n# offline needs >= 1.75\n",
            },
        )


def test_non_floor_version_context_stays_outside_value_closure() -> None:
    path = "tools/export_check.py"
    original = (ROOT / path).read_text()
    report = version_check.rust_floor_partition_report(
        ROOT,
        text_overrides={
            path: original + "\n# release version 1.75\n",
        },
    )

    assert all(item.path != path for item in report.files)


def test_release_version_restatements_agree_with_canonical() -> None:
    canonical = version_check.state_version()
    report = version_check.release_version_restatement_report(canonical)

    assert report.canonical == canonical
    assert len(report.restatements) == len(
        version_check.RELEASE_VERSION_RESTATEMENTS
    )
    assert {item.version for item in report.restatements} == {canonical}


def test_release_version_restatement_rejects_readme_disagreement() -> None:
    canonical = version_check.state_version()
    restatement = version_check.RELEASE_VERSION_RESTATEMENTS[0]
    original = (ROOT / restatement.path).read_text()
    stale = _replace_extracted_version(restatement, original, "9.9.9")

    with pytest.raises(
        ValueError,
        match=(
            r"README\.md: project heading states 9\.9\.9, but executable "
            r"release authorities derive 0\.17\.1"
        ),
    ):
        version_check.release_version_restatement_report(
            canonical,
            text_overrides={restatement.path: stale},
        )


def test_release_version_restatement_reader_rejects_zero_extraction() -> None:
    canonical = version_check.state_version()

    with pytest.raises(
        ValueError,
        match=(
            r"README\.md: project heading yielded 0 current release-version "
            r"restatements; expected exactly one"
        ),
    ):
        version_check.release_version_restatement_report(
            canonical,
            text_overrides={"README.md": "# no current release identity\n"},
        )


def test_rust_floor_partition_rejects_an_unclassified_file() -> None:
    path = "tools/export_check.py"
    original = (ROOT / path).read_text()
    derived = version_check.offline_msrv_report(ROOT).derived

    with pytest.raises(
        ValueError,
        match=(
            r"tools/export_check\.py: Rust floor literal\(s\) yielded zero "
            r"file-level classifications"
        ),
    ):
        version_check.rust_floor_partition_report(
            ROOT,
            text_overrides={
                path: original + f"\n# planted Rust floor {derived}\n",
            },
        )
