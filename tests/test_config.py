"""Tests for application configuration."""

import pytest

from tech_intel.config import Settings


def test_loads_default_settings(monkeypatch):
    """Settings should load sensible defaults."""
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.delenv("LOG_LEVEL", raising=False)
    monkeypatch.setattr("tech_intel.config.load_dotenv", lambda: None)

    settings = Settings.from_environment()

    assert settings.openai_api_key is None
    assert settings.log_level == "INFO"


def test_loads_api_key_from_environment(monkeypatch):
    """Settings should read the API key from the environment."""
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    monkeypatch.setenv("LOG_LEVEL", "DEBUG")

    settings = Settings.from_environment()

    assert settings.openai_api_key == "test-key"
    assert settings.log_level == "DEBUG"


def test_rejects_invalid_log_level(monkeypatch):
    """Invalid log levels should raise an error."""
    monkeypatch.setenv("LOG_LEVEL", "INVALID")

    with pytest.raises(ValueError, match="Invalid LOG_LEVEL"):
        Settings.from_environment()