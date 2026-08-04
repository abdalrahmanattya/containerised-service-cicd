"""HTTP application entry point for the containerised service."""

from importlib.metadata import PackageNotFoundError
from importlib.metadata import version as distribution_version

from fastapi import FastAPI


def application_version() -> str:
    """Return the installed package version used as the service version source."""

    try:
        return distribution_version("containerised-service")
    except PackageNotFoundError as exc:
        raise RuntimeError(
            "containerised-service must be installed before the service starts"
        ) from exc


app = FastAPI(title="Containerised Service", version=application_version())


@app.get("/health")
def health() -> dict[str, str]:
    """Return the process liveness response."""

    return {"status": "healthy"}


@app.get("/version")
def version() -> dict[str, str]:
    """Return the version recorded in the installed package metadata."""

    return {"version": application_version()}
