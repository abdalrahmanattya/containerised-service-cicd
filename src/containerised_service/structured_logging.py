"""JSON logging utilities for the service and its HTTP middleware."""

import json
import logging
import sys
from datetime import datetime, timezone
from logging import LogRecord

from containerised_service.config import Settings


class JsonFormatter(logging.Formatter):
    """Render approved log fields as one JSON object per output line."""

    def __init__(self, service_name: str) -> None:
        super().__init__()
        self.service_name = service_name

    def format(self, record: LogRecord) -> str:
        """Build a stable, non-sensitive JSON representation of a log record."""

        payload: dict[str, object] = {
            "timestamp": datetime.now(timezone.utc).isoformat(timespec="milliseconds"),
            "level": record.levelname,
            "service": self.service_name,
            "event": record.getMessage(),
        }

        # Copy only known request fields; arbitrary record extras could leak data.
        for field in ("method", "path", "status_code", "duration_ms"):
            value = getattr(record, field, None)
            if value is not None:
                payload[field] = value

        return json.dumps(payload, sort_keys=True)


def configure_logging(settings: Settings) -> logging.Logger:
    """Configure and return the service logger using validated settings."""

    logger = logging.getLogger("containerised_service")
    logger.setLevel(getattr(logging, settings.log_level))
    logger.propagate = False

    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(JsonFormatter(settings.service_name))
        logger.addHandler(handler)

    return logger
