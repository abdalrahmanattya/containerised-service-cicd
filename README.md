# Containerised Service with CI/CD

This repository is Project 3 of the AI-assisted cloud engineering learning
roadmap. It will contain a small Python HTTP service and the automated delivery
checks around it. The application is deliberately simple so the project can
focus on how code becomes a tested, secure, versioned container image.

The project is currently **planned but not implemented**. Commands shown under
**Planned usage** describe the intended finished workflow and will be replaced
with verified commands as each issue is completed.

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

## Planned usage

When implementation is complete, another engineer will be able to:

1. Create an isolated Python environment and install the declared dependencies.
2. Run formatting, linting, and automated tests.
3. Start the service locally with optional environment-variable overrides.
4. Call the endpoints with a browser or `curl`.
5. Build and run the same service as a local Docker container.
6. Run or inspect the CI/CD stages before producing a versioned artifact.

The eventual endpoint checks will resemble:

```sh
curl http://localhost:8000/health
curl http://localhost:8000/version
curl http://localhost:8000/config-summary
```

These commands do not work yet because no application code exists. Exact,
copy-and-paste setup and container commands will be added only after they have
been implemented and verified.

## Scope and safety boundaries

The initial project does not include a database, authentication, a cloud API,
Kubernetes, or a production deployment. It must not store or reveal secrets.
The configuration summary will expose only explicitly approved fields.

Building and running a container will be local. Configuring a Git remote,
publishing an image, adding credentials, or deploying the service are separate
actions and require explicit learner approval.

## Technology plan

The accepted technology direction is:

- Python 3.11 or newer;
- FastAPI served by Uvicorn;
- pytest for automated tests;
- Ruff for formatting and linting;
- Docker for the runtime image;
- GitHub Actions for the pipeline definition; and
- Trivy for container vulnerability scanning.

The reasoning and trade-offs are recorded in
[`ADR-002`](docs/decisions/ADR-002-service-and-delivery-stack.md). No dependency
or tool has been installed as part of planning.

## Repository map

| Path | Purpose |
| --- | --- |
| `AGENTS.md` | Safety and collaboration instructions for Codex |
| `docs/requirements.md` | Agreed behaviour, acceptance criteria, and non-goals |
| `docs/architecture.md` | Components, data flow, and trust boundaries |
| `docs/development.md` | Current and eventual local workflows |
| `docs/issues/` | Ordered, bounded implementation issues |
| `docs/decisions/` | Durable decisions and their trade-offs |
| `docs/project-journal.md` | Current state and exact resume point |
| `docs/learning-roadmap.md` | The complete multi-project learning programme |
| `CHANGELOG.md` | Notable user-visible changes |

## Current status and next step

Planning is complete when these documents pass the durable-context check and
the learner reviews the diff. Implementation then begins with
[`Issue 001`](docs/issues/001-scaffold-and-health-endpoint.md): establish the
minimal Python package and implement only `GET /health` with tests.
