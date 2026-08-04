"""Tests for the service liveness endpoint."""

from fastapi.testclient import TestClient

from containerised_service.main import app

client = TestClient(app)


def test_health_returns_healthy_status() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_health_rejects_unsupported_method() -> None:
    response = client.post("/health")

    assert response.status_code == 405


def test_unknown_path_returns_not_found() -> None:
    response = client.get("/does-not-exist")

    assert response.status_code == 404
