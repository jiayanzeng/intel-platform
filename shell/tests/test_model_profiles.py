from __future__ import annotations

from pathlib import Path
import subprocess

import pytest

from tools.model_profiles import (
    Action,
    CONTAINER_INVENTORY,
    CONTAINERS,
    ModelProfiles,
    ProfileError,
    build_remote_command,
    classify_profile,
    container_inventory_disposition,
    health_disposition,
    listener_disposition,
    socket_disposition,
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
        CONTAINER_INVENTORY,
        (
            "curl",
            "-sS",
            "--max-time",
            "2",
            "--write-out",
            "\n%{http_code}",
            "http://127.0.0.1:8082/v1/models",
        ),
        ("nvidia-smi",),
        ("ip", "-br", "address"),
        ("git", "status"),
    ):
        assert build_remote_command(command)


def test_transition_never_emits_an_ask_first_command() -> None:
    for profile in ("intel", "athenaeum", "athenaeum-bulk", "stop"):
        script = transition_script(profile)
        for forbidden in (
            "docker run",
            "docker rm",
            "docker rmi",
            "docker pull",
            "/data/models",
            "kill ",
        ):
            assert forbidden not in script


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


def test_container_inventory_accepts_complete_and_refuses_missing() -> None:
    complete = container_inventory_disposition(set(CONTAINERS))
    assert complete.action == Action.PROCEED

    incomplete = container_inventory_disposition(
        set(CONTAINERS) - {"athenaeum-embed-gpu"}
    )
    assert incomplete.action == Action.REFUSE
    assert "athenaeum-embed-gpu" in incomplete.message


def test_listener_gate_reuses_managed_and_refuses_foreign() -> None:
    free = listener_disposition(set(), set())
    assert free.action == Action.PROCEED

    managed = listener_disposition({18080, 18081}, {18080, 18081})
    assert managed.action == Action.REUSE

    foreign = listener_disposition({18080, 28082}, {18080})
    assert foreign.action == Action.REFUSE
    assert "28082" in foreign.message


def test_health_gate_accepts_only_exact_200_ok_and_names_failures() -> None:
    healthy = health_disposition(
        status=200,
        payload={"status": "ok"},
        error=None,
    )
    assert healthy.action == Action.PROCEED

    non_200 = health_disposition(status=503, payload=None, error=None)
    wrong_body = health_disposition(
        status=200,
        payload={"status": "loading"},
        error=None,
    )
    hung = health_disposition(status=None, payload=None, error="timeout")
    dead = health_disposition(
        status=None,
        payload=None,
        error="connection refused",
    )
    for refused in (non_200, wrong_body, hung, dead):
        assert refused.action == Action.REFUSE
    assert "HTTP 503" in non_200.message
    assert "unexpected body" in wrong_body.message
    assert "hung" in hung.message
    assert "dead" in dead.message
    assert hung.message != dead.message


def test_socket_gate_reuses_moves_stale_and_refuses_unreadable() -> None:
    absent = socket_disposition(exists=False, live=False, readable=True)
    live = socket_disposition(exists=True, live=True, readable=True)
    stale = socket_disposition(exists=True, live=False, readable=True)
    unreadable = socket_disposition(exists=True, live=False, readable=False)

    assert absent.action == Action.PROCEED
    assert live.action == Action.REUSE
    assert stale.action == Action.MOVE_ASIDE
    assert unreadable.action == Action.REFUSE


def test_start_tunnel_reuses_managed_listener_without_stopping_it(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    controller = ModelProfiles()
    socket_path = tmp_path / "managed.sock"
    socket_path.touch()
    monkeypatch.setattr(controller, "_control_alive", lambda *args: True)
    monkeypatch.setattr("tools.model_profiles._port_open", lambda port: True)
    monkeypatch.setattr("tools.model_profiles._http_health", lambda port: True)
    monkeypatch.setattr(
        controller,
        "stop_tunnel",
        lambda *args, **kwargs: pytest.fail("managed tunnel was stopped"),
    )
    monkeypatch.setattr(
        controller,
        "ensure_bridge",
        lambda: pytest.fail("managed tunnel was recreated"),
    )

    controller._start_tunnel(
        kind="intel",
        socket_path=socket_path,
        forwards=((18080, 8080), (18081, 8081)),
        required_health_ports=(18080, 18081),
    )
