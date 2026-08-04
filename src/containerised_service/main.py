"""HTTP application entry point for the containerised service."""

import time
from collections.abc import Awaitable, Callable
from importlib.metadata import PackageNotFoundError
from importlib.metadata import version as distribution_version

from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import Response

from containerised_service.config import Settings, load_settings
from containerised_service.structured_logging import configure_logging


def application_version() -> str:
    """Return the installed package version used as the service version source."""

    try:
        return distribution_version("containerised-service")
    except PackageNotFoundError as exc:
        raise RuntimeError(
            "containerised-service must be installed before the service starts"
        ) from exc


settings: Settings = load_settings()
service_logger = configure_logging(settings)
service_logger.info("application.configured")
app = FastAPI(title="Containerised Service", version=application_version())


@app.middleware("http")
async def log_requests(
    request: Request, call_next: Callable[[Request], Awaitable[Response]]
) -> Response:
    """Log request completion metadata without reading or recording its body."""

    started_at = time.perf_counter()
    status_code = 500

    try:
        response = await call_next(request)
        status_code = response.status_code
        return response
    finally:
        duration_ms = round((time.perf_counter() - started_at) * 1000, 3)
        service_logger.info(
            "request.completed",
            extra={
                "method": request.method,
                "path": request.url.path,
                "status_code": status_code,
                "duration_ms": duration_ms,
            },
        )


@app.get("/health")
def health() -> dict[str, str]:
    """Return the process liveness response."""

    return {"status": "healthy"}


@app.get("/version")
def version() -> dict[str, str]:
    """Return the version recorded in the installed package metadata."""

    return {"version": application_version()}


@app.get("/config-summary")
def config_summary() -> dict[str, str]:
    """Return the startup-validated, allow-listed configuration summary."""

    return settings.summary()
