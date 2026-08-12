# Containerised Service with CI/CD

This repository contains a small Python HTTP service and the automated delivery
checks around it. The service is deliberately narrow: it demonstrates how
source code becomes a tested, secure, versioned container image that can be
consumed by a separate GitOps deployment repository.

Issues 001–007 are implemented. The repository contains the service, its
container image, CI quality gates, and the documented release workflow.

## What the service does

The service exposes three JSON endpoints:

| Endpoint | Purpose |
| --- | --- |
| `GET /health` | Confirm that the process is running and able to respond |
| `GET /version` | Identify the application version currently running |
| `GET /config-summary` | Show an allow-listed, non-sensitive configuration summary |

It reads configuration from environment variables, rejects invalid
configuration with a useful error, and emits structured JSON logs. Automated
tests cover endpoint responses, configuration behaviour, and error paths. The
same application runs locally and inside a Docker container.

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

The delivery path is:

```text
Python source
    -> formatting and linting
    -> automated tests
    -> container image build
    -> container security scan
    -> explicitly exported or published versioned artifact
```

This project is the application-delivery half of the companion
[Secure Container Delivery & GitOps case study](https://github.com/abdalrahmanattya/containerised-service-gitops).
It produces the immutable image consumed by the separate Kubernetes desired-
state repository.

## Architecture at a glance

The diagram shows the boundaries between the Python process, its container
runtime, and the GitHub Actions delivery path. The GitOps repository consumes
the published digest; it is not changed by this repository's CI workflow.

![Containerised service delivery architecture](docs/diagrams/containerised-service-delivery.svg)

The maintainable diagram source is
[`docs/diagrams/containerised-service-delivery.mmd`](docs/diagrams/containerised-service-delivery.mmd).
The runtime has no database, cloud API, or secret store. Configuration enters
only at startup, and logs leave through standard output.

## API contract

Example successful responses are intentionally small and predictable:

```json
{"status":"healthy"}
```

```json
{"version":"0.1.3"}
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

## Local development

Use Python 3.13 and run these commands from the repository root:

```sh
python3.13 -m venv .venv
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

The responses include `{"status":"healthy"}`, `{"version":"0.1.3"}`, and
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

## Local container usage

Build the image from the repository root:

```sh
docker build --tag containerised-service:0.1.3 .
```

Run it with the same configuration contract:

```sh
docker run --rm --name containerised-service \
  --publish 8000:8000 \
  --env SERVICE_NAME=containerised-service \
  --env APP_ENV=development \
  --env LOG_LEVEL=INFO \
  containerised-service:0.1.3
```

In another terminal, verify all endpoints:

```sh
curl http://127.0.0.1:8000/health
curl http://127.0.0.1:8000/version
curl http://127.0.0.1:8000/config-summary
```

The image runs as the non-root `app` user. Stop the foreground container with
`Ctrl-C`, or use `docker stop containerised-service` from another terminal.

## CI quality and security gates

The workflow in [`.github/workflows/ci.yml`](.github/workflows/ci.yml) runs on
pull requests and pushes to `main`. It installs the package and development
dependencies, checks Ruff formatting and lint, runs pytest, builds the Docker
image, verifies its non-root runtime, and scans the image with Trivy.

The scan fails on fixed `HIGH` or `CRITICAL` vulnerabilities and ignores only
unfixed findings. The exception process and required review details are in
[`docs/security.md`](docs/security.md). This validation workflow does not
publish or deploy; the separate release workflow repeats the quality and
security gates before publication.

## Versioned GHCR image publication

The separate [`publish-image.yml`](.github/workflows/publish-image.yml)
workflow publishes only when a semantic-version Git tag such as `v0.1.3` is
pushed. It uses the short-lived GitHub Actions token and the minimum package
write permission; no personal registry token is required.

The current release image is:

```text
ghcr.io/abdalrahmanattya/containerised-service:0.1.3
```

The published v0.1.3 multi-architecture image is identified by this immutable
top-level digest:

```text
sha256:6a9075b289a699692f60f6936b84590c8ad487071145a909ae7c3de98025f3b2
```

The workflow records the immutable image digest in the run summary and enables
BuildKit provenance and SBOM attestations. The companion
[GitOps repository](https://github.com/abdalrahmanattya/containerised-service-gitops)
references this digest rather than a moving tag. Before publishing another
release, confirm the tag, repository ownership, package visibility, and
workflow permissions.

Publishing is intentionally not performed from a local terminal. It occurs
only through the reviewed tag workflow after explicit approval.

## Scope and safety boundaries

The current service does not include a database, authentication, a cloud API,
Kubernetes, or a production deployment. It must not store or reveal secrets.
The configuration summary exposes only explicitly approved fields.

Building and running a container is local. Configuring a Git remote,
publishing an image, adding credentials, or deploying the service are separate
actions and require explicit maintainer approval.

## Technology

The current technology stack is:

- Python 3.13 for the current implementation;
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
| `docs/requirements.md` | Agreed behaviour, acceptance criteria, and non-goals |
| `docs/architecture.md` | Components, data flow, and trust boundaries |
| `docs/development.md` | Local development, CI, and release workflows |
| `docs/issues/` | Ordered, bounded implementation issues |
| `docs/decisions/` | Durable decisions and their trade-offs |
| `src/containerised_service/` | Python application package |
| `tests/` | Automated tests |
| `pyproject.toml` | Package metadata, dependency pins, and tool configuration |
| `CHANGELOG.md` | Notable user-visible changes |
| `LICENSE` | MIT license for the repository |

## Current status and next step

Project 3 release `v0.1.3` contains the documented service, non-root image,
quality gates, vulnerability-scan policy, and linux/amd64 plus linux/arm64
image manifests. Its published digest is recorded above and is consumed by
Project 5's Docker Desktop Kubernetes target.
