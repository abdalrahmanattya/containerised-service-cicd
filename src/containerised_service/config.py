"""Validated runtime configuration for the containerised service."""

import os
import re
from collections.abc import Mapping
from dataclasses import dataclass


class ConfigurationError(ValueError):
    """Raised when an environment value cannot form valid service settings."""


@dataclass(frozen=True, slots=True)
class Settings:
    """Immutable, validated settings captured when the application starts."""

    service_name: str
    environment: str
    log_level: str

    def summary(self) -> dict[str, str]:
        """Return the explicit non-sensitive fields allowed in API responses."""

        return {
            "service_name": self.service_name,
            "environment": self.environment,
            "log_level": self.log_level,
        }


def _read_choice(
    values: Mapping[str, str], name: str, default: str, allowed: frozenset[str]
) -> str:
    """Read and validate a whitespace-trimmed value from an allowed set."""

    value = values.get(name, default).strip()
    if value not in allowed:
        choices = ", ".join(sorted(allowed))
        raise ConfigurationError(f"{name} must be one of: {choices}")
    return value


def _read_service_name(values: Mapping[str, str]) -> str:
    """Read a short log-safe service name without accepting arbitrary text."""

    value = values.get("SERVICE_NAME", "containerised-service").strip()
    if not value or len(value) > 100:
        raise ConfigurationError(
            "SERVICE_NAME must contain 1 to 100 non-whitespace characters"
        )
    if re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]*", value) is None:
        raise ConfigurationError(
            "SERVICE_NAME may contain only letters, numbers, dots, underscores, "
            "and hyphens"
        )
    return value


def load_settings(environment: Mapping[str, str] | None = None) -> Settings:
    """Load and validate startup settings from a supplied or real environment."""

    values = os.environ if environment is None else environment
    return Settings(
        service_name=_read_service_name(values),
        environment=_read_choice(
            values,
            "APP_ENV",
            "development",
            frozenset({"development", "production", "staging", "test"}),
        ),
        log_level=_read_choice(
            values,
            "LOG_LEVEL",
            "INFO",
            frozenset({"CRITICAL", "DEBUG", "ERROR", "INFO", "WARNING"}),
        ),
    )
