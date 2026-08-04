# Containerised Service with CI/CD

This repository is Project 3 of the AI-assisted cloud engineering learning
roadmap. It contains a small Python HTTP service and the automated delivery
checks around it. The application is deliberately simple so the project can
focus on how code becomes a tested, secure, versioned container image.

Issues 001–007 are implemented. The repository contains the service, its
container image, CI quality gates, and the documented release workflow.

## What the service will do

The service will expose three JSON endpoints:

| Endpoint | Purpose |
| --- | --- |
| `GET /health` | Confirm that the process is running and able to respond |
| `GET /version` | Identify the application version currently running |
| `GET /config-summary` | Show an allow-listed, non-sensitive configuration summary |

It will read configuration from environment variables, reject invalid
configuration with a useful error, and emit structured JSON logs. Automated
tests will cover endpoint responses, configuration behaviour, and error paths.
The same application will run locally and inside a Docker container.

## Why this is useful

These are common production-service patterns:

- Health endpoints let monitoring and container platforms determine whether a
  process is responding.
- Version endpoints help operators identify the deployed release.
- Environment variables let one immutable image run with different settings.
- An allow-listed configuration summary supports diagnosis without exposing
  secrets or dumping the process environment.
- Structured logs can be searched and analysed by log-processing systems.
- Containers provide a consistent application and dependency boundary.
- CI/CD checks detect defects, packaging errors, and known image vulnerabilities
  before an artifact is released.

The larger learning outcome is understanding this delivery path:

```text
Python source
    -> formatting and linting
    -> automated tests
    -> container image build
    -> container security scan
    -> explicitly exported or published versioned artifact
```

This project bridges the Terraform module in Project 2 and the Kubernetes
deployment work planned for Project 5.

## Planned behaviour

Example successful responses are intentionally small and predictable:

```json
{"status":"healthy"}
```

```json
{"version":"0.1.0"}
```

```json
{
  "environment": "development",
  "log_level": "INFO",
  "service_name": "containerised-service"
}
```

The exact contract, defaults, and failure behaviour are defined in
[`docs/requirements.md`](docs/requirements.md).

## Local usage for Issues 001–004

Use Python 3.13 and run these commands from the repository root:

```sh
/opt/homebrew/bin/python3.13 -m venv .venv
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -e '.[dev]'
.venv/bin/ruff format --check src tests
.venv/bin/ruff check src tests
.venv/bin/pytest
```

Start the local development server with:

```sh
.venv/bin/uvicorn containerised_service.main:app --reload
```

Then check the implemented endpoint:

```sh
curl http://localhost:8000/health
curl http://localhost:8000/version
curl http://localhost:8000/config-summary
```

The responses include `{"status":"healthy"}`, `{"version":"0.1.0"}`, and
the allow-listed configuration fields. The version comes from the package
metadata in `pyproject.toml`; it is not read from Git at runtime.

To run with valid overrides, set only the documented variables before startup:

```sh
SERVICE_NAME=payments-api APP_ENV=staging LOG_LEVEL=DEBUG \
  .venv/bin/uvicorn containerised_service.main:app --reload
```

Invalid values stop startup with a clear error. The service never returns the
complete process environment or secret-like variables.

The service also writes one JSON object per log line to standard output. A
request-completion record contains the method, path, status code, and duration;
request bodies and arbitrary environment variables are excluded.

## Local container usage for Issue 005

Build the image from the repository root:

```sh
docker build --tag containerised-service:0.1.0 .
```

Run it with the same configuration contract:

```sh
docker run --rm --name containerised-service \
  --publish 8000:8000 \
  --env SERVICE_NAME=containerised-service \
  --env APP_ENV=development \
  --env LOG_LEVEL=INFO \
  containerised-service:0.1.0
```

In another terminal, verify all endpoints:

```sh
curl http://127.0.0.1:8000/health
curl http://127.0.0.1:8000/version
curl http://127.0.0.1:8000/config-summary
```

The image runs as the non-root `app` user. Stop the foreground container with
`Ctrl-C`, or use `docker stop containerised-service` from another terminal.

## CI quality and security gates for Issue 006

The workflow in [`.github/workflows/ci.yml`](.github/workflows/ci.yml) runs on
pull requests and pushes to `main`. It installs the package and development
dependencies, checks Ruff formatting and lint, runs pytest, builds the Docker
image, verifies its non-root runtime, and scans the image with Trivy.

The scan fails on fixed `HIGH` or `CRITICAL` vulnerabilities and ignores only
unfixed findings. The exception process and required review details are in
[`docs/security.md`](docs/security.md). The workflow does not publish, deploy,
or require secrets.

## Scope and safety boundaries

The initial project does not include a database, authentication, a cloud API,
Kubernetes, or a production deployment. It must not store or reveal secrets.
The configuration summary will expose only explicitly approved fields.

Building and running a container will be local. Configuring a Git remote,
publishing an image, adding credentials, or deploying the service are separate
actions and require explicit learner approval.

## Technology plan

The accepted technology direction is:

- Python 3.13 for the current implementation (the ADR permits Python 3.11 or
  newer, but this machine provides Python 3.13);
- FastAPI served by Uvicorn;
- pytest for automated tests;
- Ruff for formatting and linting;
- Docker for the runtime image;
- GitHub Actions for the pipeline definition; and
- Trivy for container vulnerability scanning.

The reasoning and trade-offs are recorded in
[`ADR-002`](docs/decisions/ADR-002-service-and-delivery-stack.md). Issues 001–007
use the reviewed dependency pins and package version in `pyproject.toml`.

## Repository map

| Path | Purpose |
| --- | --- |
| `AGENTS.md` | Safety and collaboration instructions for Codex |
| `docs/requirements.md` | Agreed behaviour, acceptance criteria, and non-goals |
| `docs/architecture.md` | Components, data flow, and trust boundaries |
| `docs/development.md` | Current and eventual local workflows |
| `docs/issues/` | Ordered, bounded implementation issues |
| `docs/decisions/` | Durable decisions and their trade-offs |
| `src/containerised_service/` | Python application package |
| `tests/` | Automated tests |
| `pyproject.toml` | Package metadata, dependency pins, and tool configuration |
| `docs/project-journal.md` | Current state and exact resume point |
| `docs/learning-roadmap.md` | The complete multi-project learning programme |
| `CHANGELOG.md` | Notable user-visible changes |

## Current status and next step

Project 3 release `v0.1.0` contains the documented service, non-root image,
quality gates, and vulnerability-scan policy. The next task is Project 4 in the
learning roadmap.
