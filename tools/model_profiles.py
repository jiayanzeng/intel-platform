#!/usr/bin/env python3
"""Fail-closed Mac controller for the shared intel/Athenaeum model server."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import shlex
import socket
import subprocess
import sys
import time
from typing import Iterable, Sequence
import urllib.error
import urllib.request


CONTAINERS = frozenset(
    {
        "intel-gen",
        "intel-embed",
        "athenaeum-gen",
        "athenaeum-embed-gpu",
        "athenaeum-embed-cpu",
    }
)

TRANSITIONS = {
    "intel": (
        ("docker", "stop", "athenaeum-gen", "athenaeum-embed-gpu"),
        ("docker", "start", "intel-gen"),
        ("docker", "start", "intel-embed"),
    ),
    "athenaeum": (
        (
            "docker",
            "stop",
            "intel-gen",
            "intel-embed",
            "athenaeum-embed-gpu",
        ),
        ("docker", "start", "athenaeum-gen"),
        ("docker", "start", "athenaeum-embed-cpu"),
    ),
    "athenaeum-bulk": (
        ("docker", "stop", "intel-gen", "intel-embed", "athenaeum-gen"),
        ("docker", "start", "athenaeum-embed-cpu"),
        ("docker", "start", "athenaeum-embed-gpu"),
    ),
    "stop": (
        (
            "docker",
            "stop",
            "intel-gen",
            "intel-embed",
            "athenaeum-gen",
            "athenaeum-embed-gpu",
            "athenaeum-embed-cpu",
        ),
    ),
}

CONTAINER_INVENTORY = (
    "docker",
    "ps",
    "-a",
    "--filter",
    "name=athenaeum-",
    "--filter",
    "name=intel-",
    "--format",
    "{{.Names}}\\t{{.State}}\\t{{.Status}}",
)
REMOTE_HEALTH_URL = re.compile(
    r"http://127\.0\.0\.1:(?:8080|8081|8082)/(?:health|v1/models)"
)


class ProfileError(RuntimeError):
    """An operating gate refused to proceed."""


def build_remote_command(command: Sequence[str]) -> str:
    """Validate one structured command against the L1 remote allowlist."""
    parts = tuple(command)
    docker_lifecycle = (
        len(parts) >= 3
        and parts[:1] == ("docker",)
        and parts[1] in {"start", "stop", "restart"}
        and set(parts[2:]) <= CONTAINERS
    )
    docker_inventory = parts in {
        ("docker", "ps"),
        ("docker", "ps", "-a"),
        CONTAINER_INVENTORY,
    }
    health_query = (
        len(parts) == 5
        and parts[:4] == ("curl", "-fsS", "--max-time", "2")
        and REMOTE_HEALTH_URL.fullmatch(parts[4]) is not None
    )
    exact_read_only = parts in {
        ("nvidia-smi",),
        ("ip", "-br", "address"),
        ("git", "status"),
    }
    if not (
        docker_lifecycle
        or docker_inventory
        or health_query
        or exact_read_only
    ):
        rendered = shlex.join(parts) if parts else "<empty>"
        raise ProfileError(
            f"remote command is outside the compiled L1 allowlist: {rendered}"
        )
    return shlex.join(parts)


def classify_profile(running: set[str]) -> str:
    """Classify the server without treating an overlapping profile as valid."""
    intel_pair = {"intel-gen", "intel-embed"}
    gpu_roles = {
        "intel-gen",
        "intel-embed",
        "athenaeum-gen",
        "athenaeum-embed-gpu",
    }
    active_gpu_roles = running & gpu_roles

    if intel_pair <= running and not (
        running & {"athenaeum-gen", "athenaeum-embed-gpu"}
    ):
        return "intel"
    if (
        {"athenaeum-gen", "athenaeum-embed-cpu"} <= running
        and not (running & {"intel-gen", "intel-embed", "athenaeum-embed-gpu"})
    ):
        return "athenaeum"
    if (
        {"athenaeum-embed-gpu", "athenaeum-embed-cpu"} <= running
        and not (running & {"intel-gen", "intel-embed", "athenaeum-gen"})
    ):
        return "athenaeum-bulk"
    if not active_gpu_roles:
        return "idle-cpu" if "athenaeum-embed-cpu" in running else "stopped"
    return "INVALID"


def transition_commands(profile: str) -> tuple[tuple[str, ...], ...]:
    try:
        commands = TRANSITIONS[profile]
    except KeyError as exc:
        raise ProfileError(f"unknown model profile: {profile}") from exc
    for command in commands:
        build_remote_command(command)
    return commands


def transition_script(profile: str) -> str:
    """Render the validated transition for documentation and absence tests."""
    return "\n".join(
        build_remote_command(command)
        for command in transition_commands(profile)
    )


def _run(
    command: Sequence[str],
    *,
    check: bool = True,
    quiet: bool = False,
) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(
        list(command),
        text=True,
        capture_output=True,
        check=False,
    )
    if check and result.returncode != 0:
        detail = result.stderr.strip() or result.stdout.strip() or "no output"
        raise ProfileError(f"command failed ({result.returncode}): {detail}")
    if not quiet:
        if result.stdout:
            print(result.stdout, end="")
        if result.stderr:
            print(result.stderr, end="", file=sys.stderr)
    return result


def _port_open(port: int) -> bool:
    try:
        with socket.create_connection(("127.0.0.1", port), timeout=0.25):
            return True
    except OSError:
        return False


def _http_health(port: int) -> bool:
    try:
        with urllib.request.urlopen(
            f"http://127.0.0.1:{port}/health", timeout=2
        ) as response:
            payload = json.loads(response.read())
            return response.status == 200 and payload == {"status": "ok"}
    except (OSError, ValueError, urllib.error.URLError):
        return False


def _wait_until(predicate: object, *, timeout: float, label: str) -> None:
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        if callable(predicate) and predicate():
            return
        time.sleep(1)
    raise ProfileError(f"timed out waiting for {label}")


class ModelProfiles:
    def __init__(self) -> None:
        self.server_host = os.environ.get("MODEL_SERVER_HOST", "192.168.0.192")
        self.server_user = os.environ.get("MODEL_SERVER_USER", "jia")
        self.bridge_port = int(os.environ.get("MODEL_BRIDGE_PORT", "2222"))
        profile_tmpdir = Path(os.environ.get("TMPDIR", "/tmp"))
        self.bridge_socket = profile_tmpdir / "athenaeum-server-ssh.sock"
        self.intel_socket = profile_tmpdir / "intel-llama-tunnel.sock"
        self.athenaeum_socket = profile_tmpdir / "athenaeum-codex-model.sock"

    @property
    def server_target(self) -> str:
        return f"{self.server_user}@{self.server_host}"

    @property
    def bridge_target(self) -> str:
        return f"{self.server_user}@127.0.0.1"

    def _direct_ssh(self, *remote: str) -> list[str]:
        return [
            "ssh",
            "-o",
            "BatchMode=yes",
            "-o",
            "ConnectTimeout=8",
            self.server_target,
            *remote,
        ]

    def _bridge_ssh(self, *remote: str) -> list[str]:
        return [
            "ssh",
            "-p",
            str(self.bridge_port),
            "-o",
            "BatchMode=yes",
            "-o",
            "ConnectTimeout=8",
            self.bridge_target,
            *remote,
        ]

    def bridge_alive(self) -> bool:
        probe = build_remote_command(("ip", "-br", "address"))
        return _run(
            self._bridge_ssh(probe), check=False, quiet=True
        ).returncode == 0

    def direct_alive(self) -> bool:
        probe = build_remote_command(("ip", "-br", "address"))
        return _run(
            self._direct_ssh(probe), check=False, quiet=True
        ).returncode == 0

    def _move_stale_socket(self, path: Path) -> None:
        if not path.exists():
            return
        stamp = time.strftime("%Y%m%dT%H%M%S")
        destination = path.with_name(f"{path.name}.stale-{stamp}")
        path.rename(destination)
        print(f"moved stale control socket to {destination}")

    def ensure_bridge(self) -> None:
        if self.bridge_alive():
            print(f"shared SSH bridge: reuse localhost:{self.bridge_port}")
            return
        if _port_open(self.bridge_port):
            raise ProfileError(
                f"localhost:{self.bridge_port} is occupied but is not the model-server bridge"
            )
        if not self.direct_alive():
            raise ProfileError(
                "the server is unreachable from this shell. Run the command in "
                "Terminal.app, which has the Mac LAN route, or create the documented "
                f"localhost:{self.bridge_port} bridge there first"
            )
        self._move_stale_socket(self.bridge_socket)
        _run(
            [
                "ssh",
                "-f",
                "-N",
                "-M",
                "-S",
                str(self.bridge_socket),
                "-o",
                "ExitOnForwardFailure=yes",
                "-o",
                "ServerAliveInterval=30",
                "-o",
                "ServerAliveCountMax=3",
                "-L",
                f"{self.bridge_port}:127.0.0.1:22",
                self.server_target,
            ],
            quiet=True,
        )
        _wait_until(
            self.bridge_alive,
            timeout=10,
            label=f"shared SSH bridge on localhost:{self.bridge_port}",
        )
        print(f"shared SSH bridge: started localhost:{self.bridge_port}")

    def _remote(
        self,
        command: Sequence[str],
        *,
        check: bool = True,
        quiet: bool = False,
    ) -> subprocess.CompletedProcess[str]:
        rendered = build_remote_command(command)
        if self.bridge_alive():
            return _run(
                self._bridge_ssh(rendered), check=check, quiet=quiet
            )
        if self.direct_alive():
            return _run(
                self._direct_ssh(rendered), check=check, quiet=quiet
            )
        raise ProfileError("no working direct or bridged SSH route to the model server")

    def _container_rows(self) -> list[tuple[str, bool, str]]:
        result = self._remote(CONTAINER_INVENTORY, quiet=True)
        rows: list[tuple[str, bool, str]] = []
        for line in result.stdout.splitlines():
            fields = line.split("\t", 2)
            if len(fields) != 3:
                raise ProfileError(
                    "malformed container inventory row from model server: "
                    + repr(line)
                )
            name, state, status = fields
            rows.append((name, state == "running", status))
        return rows

    def _require_containers(self) -> None:
        found = {name for name, _, _ in self._container_rows()}
        missing = sorted(CONTAINERS - found)
        if missing:
            raise ProfileError(
                "named containers are missing; routine switching never recreates them: "
                + ", ".join(missing)
            )

    def _running(self) -> set[str]:
        return {name for name, running, _ in self._container_rows() if running}

    def _remote_health(self, port: int) -> bool:
        result = self._remote(
            (
                "curl",
                "-fsS",
                "--max-time",
                "2",
                f"http://127.0.0.1:{port}/health",
            ),
            check=False,
            quiet=True,
        )
        if result.returncode != 0:
            return False
        try:
            return json.loads(result.stdout) == {"status": "ok"}
        except ValueError:
            return False

    def _wait_remote_health(self, port: int, role: str) -> None:
        _wait_until(
            lambda: self._remote_health(port),
            timeout=120,
            label=f"{role} health on server port {port}",
        )
        print(f"{role}: server port {port} healthy")

    def _expect_remote_down(self, port: int, role: str) -> None:
        if self._remote_health(port):
            raise ProfileError(f"{role} unexpectedly remains healthy on server port {port}")
        print(f"{role}: server port {port} down as required")

    def _control_commands(
        self, kind: str, socket_path: Path, operation: str
    ) -> list[list[str]]:
        if kind == "bridge":
            return [
                [
                    "ssh",
                    "-S",
                    str(socket_path),
                    "-O",
                    operation,
                    self.server_target,
                ]
            ]
        bridge_command = [
            "ssh",
            "-p",
            str(self.bridge_port),
            "-S",
            str(socket_path),
            "-O",
            operation,
            self.bridge_target,
        ]
        if kind == "intel":
            direct_command = [
                "ssh",
                "-S",
                str(socket_path),
                "-O",
                operation,
                self.server_target,
            ]
            return [bridge_command, direct_command]
        return [bridge_command]

    def _control_alive(self, kind: str, socket_path: Path) -> bool:
        if not socket_path.exists():
            return False
        return any(
            _run(command, check=False, quiet=True).returncode == 0
            for command in self._control_commands(kind, socket_path, "check")
        )

    def _listener_detail(self, ports: Iterable[int]) -> str:
        command = ["lsof", "-nP"]
        for port in ports:
            command.extend(["-iTCP:" + str(port)])
        command.extend(["-sTCP:LISTEN"])
        result = _run(command, check=False, quiet=True)
        return result.stdout.strip() or "listener owner unavailable"

    def _require_ports_free(self, ports: Sequence[int]) -> None:
        occupied = [port for port in ports if _port_open(port)]
        if occupied:
            raise ProfileError(
                f"local model ports are occupied: {occupied}\n"
                + self._listener_detail(occupied)
            )

    def stop_tunnel(self, kind: str, socket_path: Path, ports: Sequence[int]) -> None:
        if self._control_alive(kind, socket_path):
            for command in self._control_commands(kind, socket_path, "exit"):
                if _run(command, check=False, quiet=True).returncode == 0:
                    break
            _wait_until(
                lambda: not any(_port_open(port) for port in ports),
                timeout=10,
                label=f"{kind} tunnel ports to close",
            )
            print(f"{kind} model tunnel: stopped")
            return
        if socket_path.exists():
            self._move_stale_socket(socket_path)
        self._require_ports_free(ports)

    def _start_tunnel(
        self,
        *,
        kind: str,
        socket_path: Path,
        forwards: Sequence[tuple[int, int]],
        required_health_ports: Sequence[int],
    ) -> None:
        ports = [local for local, _ in forwards]
        self.stop_tunnel(kind, socket_path, ports)
        self.ensure_bridge()
        command = [
            "ssh",
            "-4",
            "-p",
            str(self.bridge_port),
            "-f",
            "-N",
            "-M",
            "-S",
            str(socket_path),
            "-o",
            "ExitOnForwardFailure=yes",
            "-o",
            "ServerAliveInterval=30",
            "-o",
            "ServerAliveCountMax=3",
        ]
        for local, remote in forwards:
            command.extend(["-L", f"{local}:127.0.0.1:{remote}"])
        command.append(self.bridge_target)
        _run(command, quiet=True)
        _wait_until(
            lambda: all(_port_open(port) for port in ports),
            timeout=10,
            label=f"{kind} local tunnel listeners",
        )
        for port in required_health_ports:
            _wait_until(
                lambda port=port: _http_health(port),
                timeout=30,
                label=f"{kind} tunneled health on localhost:{port}",
            )
            print(f"{kind}: localhost:{port} healthy")

    def _start_profile_tunnel(self, profile: str) -> None:
        if profile == "intel":
            self._start_tunnel(
                kind="intel",
                socket_path=self.intel_socket,
                forwards=((18080, 8080), (18081, 8081)),
                required_health_ports=(18080, 18081),
            )
            return
        required = (28080, 28082) if profile == "athenaeum" else (28081, 28082)
        self._start_tunnel(
            kind="athenaeum",
            socket_path=self.athenaeum_socket,
            forwards=((28080, 8080), (28081, 8081), (28082, 8082)),
            required_health_ports=required,
        )

    def status(self) -> str:
        rows = self._container_rows()
        running = {name for name, active, _ in rows if active}
        profile = classify_profile(running)
        print(f"server profile: {profile}")
        for name, active, status in sorted(rows):
            marker = "running" if active else "stopped"
            print(f"  {name}: {marker} ({status})")
        print(
            "local controls: "
            f"bridge={'up' if self.bridge_alive() else 'down'}, "
            f"intel-tunnel={'up' if self._control_alive('intel', self.intel_socket) else 'down'}, "
            "athenaeum-tunnel="
            f"{'up' if self._control_alive('athenaeum', self.athenaeum_socket) else 'down'}"
        )
        return profile

    def switch(self, profile: str) -> None:
        self.ensure_bridge()
        self._require_containers()
        entering = classify_profile(self._running())
        print(f"entering server profile: {entering}")
        if entering == "INVALID":
            raise ProfileError(
                "server is in a partial or overlapping GPU state; inspect it before switching"
            )
        self.stop_tunnel("intel", self.intel_socket, (18080, 18081))
        self.stop_tunnel(
            "athenaeum", self.athenaeum_socket, (28080, 28081, 28082)
        )
        for command in transition_commands(profile):
            self._remote(
                command,
                check=command[1] != "stop",
                quiet=True,
            )

        if profile == "intel":
            self._wait_remote_health(8080, "intel generation")
            self._wait_remote_health(8081, "intel embedding")
        elif profile == "athenaeum":
            self._wait_remote_health(8080, "Athenaeum generation")
            self._wait_remote_health(8082, "Athenaeum query embedding")
            self._expect_remote_down(8081, "Athenaeum bulk embedding")
        else:
            self._wait_remote_health(8081, "Athenaeum bulk embedding")
            self._wait_remote_health(8082, "Athenaeum query embedding")
            self._expect_remote_down(8080, "Athenaeum generation")

        measured = classify_profile(self._running())
        if measured != profile:
            raise ProfileError(
                f"profile transition requested {profile}, measured {measured}"
            )
        self._start_profile_tunnel(profile)
        self.status()

    def _stop_bridge(self) -> None:
        if not self._control_alive("bridge", self.bridge_socket):
            if _port_open(self.bridge_port):
                print(
                    f"shared SSH bridge left running: localhost:{self.bridge_port} "
                    "is not owned by the documented control socket"
                )
            return
        command = self._control_commands("bridge", self.bridge_socket, "exit")[0]
        _run(command, quiet=True)
        _wait_until(
            lambda: not _port_open(self.bridge_port),
            timeout=10,
            label="shared SSH bridge to close",
        )
        print("shared SSH bridge: stopped")

    def stop_all(self) -> None:
        self.ensure_bridge()
        self._require_containers()
        self.stop_tunnel("intel", self.intel_socket, (18080, 18081))
        self.stop_tunnel(
            "athenaeum", self.athenaeum_socket, (28080, 28081, 28082)
        )
        for command in transition_commands("stop"):
            self._remote(command, check=False, quiet=True)
        measured = classify_profile(self._running())
        if measured != "stopped":
            raise ProfileError(f"all-stop requested, measured server profile {measured}")
        print("server profile: stopped")
        self._stop_bridge()


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Switch or stop the shared intel/Athenaeum model profiles."
    )
    parser.add_argument(
        "profile",
        choices=("status", "intel", "athenaeum", "athenaeum-bulk", "stop"),
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    controller = ModelProfiles()
    try:
        if args.profile == "status":
            controller.status()
        elif args.profile == "stop":
            controller.stop_all()
        else:
            controller.switch(args.profile)
    except ProfileError as exc:
        print(f"model-profiles: REFUSED: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
