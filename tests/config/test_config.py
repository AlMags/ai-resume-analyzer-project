import pytest

import app.config as config


def test_gemini_api_key_is_loaded(monkeypatch):
    monkeypatch.setenv(
        "GEMINI_API_KEY",
        "test-api-key",
    )

    assert config.get_gemini_api_key() == "test-api-key"

def test_gemini_api_key_loading_failed(monkeypatch):
    monkeypatch.delenv(
        "GEMINI_API_KEY",
        raising=False,
    )

    with pytest.raises(
        RuntimeError,
        match="GEMINI_API_KEY environment variable is required."
    ):
        config.get_gemini_api_key()