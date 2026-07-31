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


def test_offline_msrv_normalizes_and_binds_current_restatements() -> None:
    report = version_check.offline_msrv_report(ROOT)

    assert {pin.raw for pin in report.pins} == {"1.78", "1.78.0"}
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
