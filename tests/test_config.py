"""Tests for startup configuration and the safe configuration endpoint."""

import os
import subprocess
import sys

import pytest
from fastapi.testclient import TestClient

from containerised_service.config import ConfigurationError, load_settings
from containerised_service.main import app

client = TestClient(app)


def test_defaults_are_applied() -> None:
    """Use the documented defaults when no configuration values are supplied."""

    settings = load_settings({})

    assert settings.summary() == {
        "service_name": "containerised-service",
        "environment": "development",
        "log_level": "INFO",
    }


def test_valid_overrides_are_trimmed_and_retained() -> None:
    """Accept valid deployment overrides while preserving their meaning."""

    settings = load_settings(
        {
            "SERVICE_NAME": " payments-api ",
            "APP_ENV": "staging",
            "LOG_LEVEL": "DEBUG",
        }
    )

    assert settings.summary() == {
        "service_name": "payments-api",
        "environment": "staging",
        "log_level": "DEBUG",
    }


@pytest.mark.parametrize(
    ("name", "value"),
    [
        ("SERVICE_NAME", "bad name"),
        ("SERVICE_NAME", ""),
        ("APP_ENV", "qa"),
        ("LOG_LEVEL", "TRACE"),
    ],
)
def test_invalid_values_raise_configuration_error(name: str, value: str) -> None:
    """Reject each invalid-value class with a clear configuration exception."""

    with pytest.raises(ConfigurationError, match=name):
        load_settings({name: value})


def test_invalid_environment_stops_application_startup() -> None:
    """Prove an invalid process environment prevents application import."""

    environment = os.environ.copy()
    environment["APP_ENV"] = "qa"
    result = subprocess.run(
        [sys.executable, "-c", "import containerised_service.main"],
        env=environment,
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode != 0
    assert "APP_ENV" in result.stderr


def test_config_summary_has_only_allow_listed_fields(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Ensure secrets and unrelated environment values never enter the response."""

    monkeypatch.setenv("SECRET_TOKEN", "do-not-return")
    response = client.get("/config-summary")

    assert response.status_code == 200
    assert set(response.json()) == {"service_name", "environment", "log_level"}
    assert "SECRET_TOKEN" not in response.json()
