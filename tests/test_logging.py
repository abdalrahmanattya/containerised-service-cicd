"""Tests for structured application and request logs."""

import json
import logging
from io import StringIO

from fastapi.testclient import TestClient

from containerised_service.main import app, service_logger
from containerised_service.structured_logging import JsonFormatter

client = TestClient(app)


def test_formatter_includes_required_application_fields() -> None:
    """Keep the stable fields needed by log collectors and operators."""

    record = logging.LogRecord(
        name="containerised_service",
        level=logging.INFO,
        pathname=__file__,
        lineno=1,
        msg="application.configured",
        args=(),
        exc_info=None,
    )

    payload = json.loads(JsonFormatter("payments-api").format(record))

    assert payload["level"] == "INFO"
    assert payload["service"] == "payments-api"
    assert payload["event"] == "application.configured"
    assert isinstance(payload["timestamp"], str)


def test_request_log_includes_metadata_without_body() -> None:
    """Record request metadata while excluding a submitted secret body."""

    stream = StringIO()
    handler = logging.StreamHandler(stream)
    handler.setFormatter(JsonFormatter("containerised-service"))
    service_logger.addHandler(handler)

    try:
        response = client.post("/does-not-exist", content="SECRET_TOKEN=do-not-log")
    finally:
        service_logger.removeHandler(handler)
        handler.close()

    assert response.status_code == 404
    records = [json.loads(line) for line in stream.getvalue().splitlines()]
    request_record = next(
        record for record in records if record["event"] == "request.completed"
    )

    assert request_record["method"] == "POST"
    assert request_record["path"] == "/does-not-exist"
    assert request_record["status_code"] == 404
    assert isinstance(request_record["duration_ms"], float)
    assert "SECRET_TOKEN" not in stream.getvalue()
    assert "body" not in request_record
