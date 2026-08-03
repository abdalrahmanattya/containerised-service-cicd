# ADR-002: Use FastAPI with a local-first container delivery pipeline

- **Status:** Accepted
- **Date:** 2026-08-03
- **Decision owners:** Learner and project maintainer

## Context

Project 3 needs a small HTTP service whose application behaviour is easy to
test while providing realistic dependency, container, logging, and pipeline
work. The repository currently has Python 3.9.6 available, but Docker, Ruff,
pytest, and `uv` are not installed. Planning must not silently install tools or
let the current machine dictate an obsolete runtime target.

## Decision

Use the following stack:

- Python 3.11 or newer as the supported runtime;
- FastAPI for routing, response models, and in-process API testing;
- Uvicorn as the ASGI server;
- pytest for configuration and endpoint tests;
- Ruff for formatting and linting;
- the Python standard logging library with a small JSON formatter;
- Docker with a pinned Python base-image reference and a non-root runtime user;
- GitHub Actions as the versioned CI/CD definition; and
- Trivy for container image vulnerability scanning.

Use standard `venv` and pip-compatible dependency metadata initially. Exact
dependency versions and the reproducible lock strategy will be added and
reviewed in Issue 001 before installation.

The pipeline will validate locally reproducible commands. It will not publish
or deploy by default, and a remote repository is not assumed.

## Consequences

### Benefits

- FastAPI provides concise typed HTTP contracts without needing a custom web
  layer.
- In-process tests keep the feedback loop fast and independent of a live port.
- Ruff combines two basic quality concerns behind one tool.
- JSON stdout logs and a non-root container match common platform conventions.
- GitHub Actions and Trivy expose realistic pipeline and security concepts
  while keeping publication optional.

### Costs and risks

- The local Python installation is older than the selected minimum, so a newer
  interpreter must be installed or supplied by Docker before application tests
  can run.
- Docker and scanning tools add setup time and are currently unavailable.
- FastAPI and its test client add third-party dependencies for a very small API.
- GitHub Actions cannot execute remotely until the learner explicitly chooses
  and configures a remote repository.
- Vulnerability results can require judgement; a scanner result is evidence,
  not proof that an image is secure.

## Alternatives considered

### Python standard library HTTP server

Rejected because it would minimize dependencies but shift attention to custom
routing and response plumbing instead of API and delivery practices.

### Flask

Viable and simpler in some respects, but not selected because FastAPI's typed
contracts and in-process testing align better with the planned exercises.

### Run only in Docker

Rejected because requiring a container for every test would slow feedback and
make application failures harder to separate from packaging failures.

### Publish images automatically

Rejected for the initial pipeline because it requires an external registry,
credentials, and an explicit release policy. A later approved issue may add it.

## Verification

The decision is satisfied when the exact commands recorded in
`docs/development.md` pass locally, the image runs as a non-root user, the four
pipeline gates are understandable, and no publish or deployment action occurs
without explicit approval.
