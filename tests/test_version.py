"""Tests for the service version endpoint."""

from importlib.metadata import version as distribution_version

from fastapi.testclient import TestClient

from containerised_service.main import app, application_version

client = TestClient(app)


def test_version_comes_from_package_metadata() -> None:
    """Verify the endpoint and helper use the package's declared version."""

    response = client.get("/version")
    expected_version = distribution_version("containerised-service")

    assert response.status_code == 200
    assert response.json() == {"version": expected_version}
    assert application_version() == expected_version
