"""HTTP application entry point for the containerised service."""

from fastapi import FastAPI

app = FastAPI(title="Containerised Service")


@app.get("/health")
def health() -> dict[str, str]:
    """Return the process liveness response."""

    return {"status": "healthy"}
