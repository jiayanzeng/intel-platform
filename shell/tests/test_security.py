"""Tests for the shell's security primitives (no Rust, no network)."""

from __future__ import annotations

from intel_shell import security


def test_hash_is_deterministic_and_hex():
    h1 = security.hash_token("ak_acme_7f3d9c", pepper="")
    h2 = security.hash_token("ak_acme_7f3d9c", pepper="")
    assert h1 == h2
    assert len(h1) == 64 and all(c in "0123456789abcdef" for c in h1)


def test_pepper_changes_the_digest():
    plain = security.hash_token("secret", pepper="")
    peppered = security.hash_token("secret", pepper="server-pepper")
    assert plain != peppered


def test_token_matches_constant_time_helper():
    h = security.hash_token("right-key", pepper="")
    assert security.token_matches("right-key", h, pepper="")
    assert not security.token_matches("wrong-key", h, pepper="")


def test_webhook_signature_roundtrip():
    secret = "whsec_123"
    body = b'{"type":"subscription.updated","data":{}}'
    import hashlib
    import hmac

    sig = hmac.new(secret.encode(), body, hashlib.sha256).hexdigest()
    assert security.verify_webhook_signature(secret, body, sig)
    assert security.verify_webhook_signature(secret, body, f"sha256={sig}")
    assert not security.verify_webhook_signature(secret, body, "deadbeef")
    assert not security.verify_webhook_signature(secret, body, None)
    assert not security.verify_webhook_signature(secret, b"tampered", sig)
