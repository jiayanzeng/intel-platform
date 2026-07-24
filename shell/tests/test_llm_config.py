"""Model configuration and loopback proxy guards.

The wrong legacy endpoint and proxy-enabled loopback client are deliberate
negative controls: these tests fail if role/profile selection or the proxy guard
is removed.
"""

from __future__ import annotations

import pytest

from intel_shell import core_client, llm


LLM_ENV_KEYS = (
    "LLM_CHAT_PROFILE",
    "LLM_LAN_BASE_URL",
    "LLM_LAN_API_KEY",
    "LLM_LAN_CHAT_MODEL",
    "LLM_ONLINE_BASE_URL",
    "LLM_ONLINE_API_KEY",
    "LLM_ONLINE_CHAT_MODEL",
    "LLM_CHAT_BASE_URL",
    "LLM_CHAT_API_KEY",
    "LLM_CHAT_MODEL",
    "LLM_EMBED_BASE_URL",
    "LLM_EMBED_API_KEY",
    "LLM_EMBED_MODEL",
    "LLM_CHAT_TIMEOUT_SECONDS",
    "LLM_EMBED_TIMEOUT_SECONDS",
    "LLM_CHAT_TRANSPORT_BASE_URL",
    "LLM_EMBED_TRANSPORT_BASE_URL",
    "LLM_TIMEOUT_SECONDS",
    "LLM_BASE_URL",
    "LLM_API_KEY",
    "LLM_MODEL",
)


def _clear_llm_env(monkeypatch: pytest.MonkeyPatch) -> None:
    for key in LLM_ENV_KEYS:
        monkeypatch.delenv(key, raising=False)


@pytest.mark.parametrize(
    ("profile", "expected_base", "expected_key", "expected_model"),
    [
        ("lan", "http://lan.test/v1", "lan-secret", "lan-chat"),
        ("online", "https://online.test/v1", "online-secret", "online-chat"),
    ],
)
def test_chat_profile_and_independent_embeddings_override_wrong_legacy(
    monkeypatch: pytest.MonkeyPatch,
    profile: str,
    expected_base: str,
    expected_key: str,
    expected_model: str,
) -> None:
    _clear_llm_env(monkeypatch)
    monkeypatch.setenv("LLM_BASE_URL", "https://wrong-legacy.test/v1")
    monkeypatch.setenv("LLM_API_KEY", "wrong-legacy-secret")
    monkeypatch.setenv("LLM_MODEL", "wrong-legacy-model")

    monkeypatch.setenv("LLM_CHAT_PROFILE", profile)
    monkeypatch.setenv("LLM_LAN_BASE_URL", "http://lan.test/v1")
    monkeypatch.setenv("LLM_LAN_API_KEY", "lan-secret")
    monkeypatch.setenv("LLM_LAN_CHAT_MODEL", "lan-chat")
    monkeypatch.setenv("LLM_ONLINE_BASE_URL", "https://online.test/v1")
    monkeypatch.setenv("LLM_ONLINE_API_KEY", "online-secret")
    monkeypatch.setenv("LLM_ONLINE_CHAT_MODEL", "online-chat")

    monkeypatch.setenv("LLM_EMBED_BASE_URL", "https://embed.test/v1")
    monkeypatch.setenv("LLM_EMBED_API_KEY", "embed-secret")
    monkeypatch.setenv("LLM_EMBED_MODEL", "embed-model")

    chat = llm.chat_from_env()
    embed = llm.embed_from_env()

    assert chat is not None
    assert embed is not None
    assert chat.base_url == expected_base
    assert chat.model == expected_model
    assert chat._c.headers["Authorization"] == f"Bearer {expected_key}"
    assert embed.base_url == "https://embed.test/v1"
    assert embed.model == "embed-model"
    assert embed._c.headers["Authorization"] == "Bearer embed-secret"


def test_legacy_shared_provider_still_configures_both_roles(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _clear_llm_env(monkeypatch)
    monkeypatch.setenv("LLM_BASE_URL", "https://shared.test/v1")
    monkeypatch.setenv("LLM_API_KEY", "shared-secret")
    monkeypatch.setenv("LLM_MODEL", "shared-model")

    chat = llm.chat_from_env()
    embed = llm.embed_from_env()

    assert chat is not None
    assert embed is not None
    assert chat.base_url == embed.base_url == "https://shared.test/v1"
    assert chat.model == embed.model == "shared-model"
    assert chat._c.headers["Authorization"] == "Bearer shared-secret"
    assert embed._c.headers["Authorization"] == "Bearer shared-secret"


def test_loopback_core_client_cannot_inherit_proxy_environment(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    calls: list[dict] = []

    def proxy_sensitive_client(**kwargs):
        calls.append(kwargs)
        base_url = kwargs["base_url"]
        is_loopback = "127.0.0.1" in base_url or "localhost" in base_url
        if is_loopback and kwargs.get("trust_env") is not False:
            raise AssertionError("loopback CoreClient attempted proxy inheritance")
        return object()

    monkeypatch.setattr(core_client.httpx, "Client", proxy_sensitive_client)

    core_client.CoreClient("http://127.0.0.1:8788")
    core_client.CoreClient("http://localhost:8788")
    core_client.CoreClient("https://remote-core.test")

    assert [call["trust_env"] for call in calls] == [False, False, True]


def test_role_timeouts_override_wrong_shared_timeout(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _clear_llm_env(monkeypatch)
    monkeypatch.setenv("LLM_CHAT_BASE_URL", "https://chat.test/v1")
    monkeypatch.setenv("LLM_EMBED_BASE_URL", "https://embed.test/v1")
    monkeypatch.setenv("LLM_TIMEOUT_SECONDS", "999")
    monkeypatch.setenv("LLM_CHAT_TIMEOUT_SECONDS", "7.5")
    monkeypatch.setenv("LLM_EMBED_TIMEOUT_SECONDS", "8.5")
    calls: list[dict] = []

    def capture_client(**kwargs):
        calls.append(kwargs)
        return object()

    monkeypatch.setattr(llm.httpx, "Client", capture_client)

    chat = llm.chat_from_env()
    embed = llm.embed_from_env()

    assert chat is not None
    assert embed is not None
    assert [call["timeout"] for call in calls] == [7.5, 8.5]
    assert chat.timeout_seconds == 7.5
    assert embed.timeout_seconds == 8.5


def test_legacy_shared_timeout_configures_both_roles(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _clear_llm_env(monkeypatch)
    monkeypatch.setenv("LLM_BASE_URL", "https://shared.test/v1")
    monkeypatch.setenv("LLM_TIMEOUT_SECONDS", "9")
    calls: list[dict] = []

    def capture_client(**kwargs):
        calls.append(kwargs)
        return object()

    monkeypatch.setattr(llm.httpx, "Client", capture_client)

    assert llm.chat_from_env() is not None
    assert llm.embed_from_env() is not None
    assert [call["timeout"] for call in calls] == [9.0, 9.0]


def test_transport_overrides_route_only_after_role_identity_resolution(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _clear_llm_env(monkeypatch)
    monkeypatch.setenv("LLM_CHAT_PROFILE", "lan")
    monkeypatch.setenv("LLM_LAN_BASE_URL", "http://lan.test/v1")
    monkeypatch.setenv("LLM_LAN_API_KEY", "lan-secret")
    monkeypatch.setenv("LLM_LAN_CHAT_MODEL", "lan-chat")
    monkeypatch.setenv("LLM_EMBED_BASE_URL", "https://embed.test/v1")
    monkeypatch.setenv("LLM_EMBED_API_KEY", "embed-secret")
    monkeypatch.setenv("LLM_EMBED_MODEL", "embed-model")
    monkeypatch.setenv(
        "LLM_CHAT_TRANSPORT_BASE_URL",
        "http://127.0.0.1:18080/v1",
    )
    monkeypatch.setenv(
        "LLM_EMBED_TRANSPORT_BASE_URL",
        "http://127.0.0.1:18081/v1",
    )
    calls: list[dict] = []

    def capture_client(**kwargs):
        calls.append(kwargs)
        return object()

    monkeypatch.setattr(llm.httpx, "Client", capture_client)

    chat = llm.chat_from_env()
    embed = llm.embed_from_env()

    assert chat is not None
    assert embed is not None
    assert chat.provider_base_url == "http://lan.test/v1"
    assert chat.base_url == "http://127.0.0.1:18080/v1"
    assert chat.model == "lan-chat"
    assert embed.provider_base_url == "https://embed.test/v1"
    assert embed.base_url == "http://127.0.0.1:18081/v1"
    assert embed.model == "embed-model"
    assert [call["trust_env"] for call in calls] == [False, False]


@pytest.mark.parametrize("bad_timeout", ["0", "-1", "not-a-number"])
def test_invalid_model_timeout_is_refused(
    monkeypatch: pytest.MonkeyPatch,
    bad_timeout: str,
) -> None:
    _clear_llm_env(monkeypatch)
    monkeypatch.setenv("LLM_CHAT_BASE_URL", "https://chat.test/v1")
    monkeypatch.setenv("LLM_CHAT_TIMEOUT_SECONDS", bad_timeout)

    with pytest.raises(llm.LlmError, match="LLM_CHAT_TIMEOUT_SECONDS"):
        llm.chat_from_env()
