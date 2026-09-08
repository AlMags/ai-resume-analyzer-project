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
        match="GEMINI_API_KEY environment variable is missing."
    ):
        config.get_gemini_api_key()

def test_mongodb_uri_is_loaded(monkeypatch):
    monkeypatch.setenv(
        "MONGODB_URI",
        "test-uri",
    )

    assert config.get_mongodb_uri() == "test-uri"

def test_mongodb_uri_loading_failed(monkeypatch):
    monkeypatch.delenv(
        "MONGODB_URI",
        raising=False
    )

    with pytest.raises(
        RuntimeError,
        match="MONGODB_URI environment variable is missing."
    ):
        config.get_mongodb_uri()

def test_mongodb_database_is_loaded(monkeypatch):
    monkeypatch.setenv(
        "MONGODB_DATABASE",
        "test-database-name",
    )

    assert config.get_mongodb_database() == "test-database-name"

def test_mongodb_database_loading_failed(monkeypatch):
    monkeypatch.delenv(
        "MONGODB_DATABASE",
        raising=False
    )

    with pytest.raises(
        RuntimeError,
        match="MONGODB_DATABASE environment variable is missing.",
    ):
        config.get_mongodb_database()