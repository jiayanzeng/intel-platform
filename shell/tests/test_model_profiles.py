from __future__ import annotations

import subprocess

import pytest

from tools.model_profiles import (
    ModelProfiles,
    ProfileError,
    build_remote_command,
    classify_profile,
    transition_commands,
    transition_script,
)


def test_profile_classifier_accepts_only_complete_mutually_exclusive_states() -> None:
    assert classify_profile({"intel-gen", "intel-embed"}) == "intel"
    assert (
        classify_profile(
            {"intel-gen", "intel-embed", "athenaeum-embed-cpu"}
        )
        == "intel"
    )
    assert (
        classify_profile({"athenaeum-gen", "athenaeum-embed-cpu"})
        == "athenaeum"
    )
    assert (
        classify_profile({"athenaeum-embed-gpu", "athenaeum-embed-cpu"})
        == "athenaeum-bulk"
    )
    assert classify_profile(set()) == "stopped"
    assert classify_profile({"athenaeum-embed-cpu"}) == "idle-cpu"


@pytest.mark.parametrize(
    "running",
    [
        {"intel-gen"},
        {"intel-gen", "intel-embed", "athenaeum-gen"},
        {"athenaeum-gen"},
        {"athenaeum-embed-gpu"},
        {"athenaeum-gen", "athenaeum-embed-gpu", "athenaeum-embed-cpu"},
    ],
)
def test_profile_classifier_refuses_partial_or_overlapping_gpu_states(
    running: set[str],
) -> None:
    assert classify_profile(running) == "INVALID"


def test_transition_scripts_stop_conflicting_gpu_roles_before_starting() -> None:
    intel = transition_script("intel")
    assert intel.index("docker stop athenaeum-gen athenaeum-embed-gpu") < intel.index(
        "docker start intel-gen"
    )

    serving = transition_script("athenaeum")
    assert serving.index(
        "docker stop intel-gen intel-embed athenaeum-embed-gpu"
    ) < serving.index("docker start athenaeum-gen")

    bulk = transition_script("athenaeum-bulk")
    assert bulk.index(
        "docker stop intel-gen intel-embed athenaeum-gen"
    ) < bulk.index("docker start athenaeum-embed-gpu")

    for profile in ("intel", "athenaeum", "athenaeum-bulk", "stop"):
        for command in transition_commands(profile):
            assert build_remote_command(command)
    for command in (
        ("docker", "ps"),
        ("docker", "ps", "-a"),
        (
            "curl",
            "-fsS",
            "--max-time",
            "2",
            "http://127.0.0.1:8082/v1/models",
        ),
        ("nvidia-smi",),
        ("ip", "-br", "address"),
        ("git", "status"),
    ):
        assert build_remote_command(command)


def test_transition_never_recreates_a_named_container() -> None:
    for profile in ("intel", "athenaeum", "athenaeum-bulk", "stop"):
        script = transition_script(profile)
        assert "docker run" not in script
        assert "docker rm" not in script


def test_unknown_commands_and_malformed_inventory_are_refused(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    with pytest.raises(ProfileError, match="unknown model profile"):
        transition_script("other")

    planted = (
        ("docker", "rm", "intel-gen"),
        ("docker", "run", "intel-gen"),
        ("rm", "-rf", "/data/models"),
        ("docker", "start", "sixth-container"),
    )
    for command in planted:
        with pytest.raises(ProfileError, match="compiled L1 allowlist"):
            build_remote_command(command)

    controller = ModelProfiles()
    malformed = subprocess.CompletedProcess(
        args=[],
        returncode=0,
        stdout="intel-gen running Up 2 hours\n",
        stderr="",
    )
    monkeypatch.setattr(
        controller,
        "_remote",
        lambda *args, **kwargs: malformed,
    )
    with pytest.raises(ProfileError, match="malformed container inventory row"):
        controller._container_rows()
