# Architecture

## Purpose and scope

This project is a small Python HTTP service surrounded by tests, a container
build, and CI/CD validation. It provides operational endpoints and produces a
versioned image for the companion GitOps repository.

## System context

![Containerised service delivery architecture](diagrams/containerised-service-delivery.svg)

Source for the rendered diagram is
[`diagrams/containerised-service-delivery.mmd`](diagrams/containerised-service-delivery.mmd).
The drawing uses explicit boundaries and directional flow so it can be updated
alongside the workflows.

```text
caller
  |
  | HTTP GET
  v
FastAPI application --------------------> JSON logs on stdout
  |       |       |
  |       |       +--> /config-summary
  |       +----------> /version
  +------------------> /health
  |
  v
validated environment configuration

source + tests + dependency metadata
  |
  v
CI: format/lint -> test -> image build -> vulnerability scan
  |
  v
local image artifact
  |
  +--> tag-triggered GHCR publication (release workflow only)
  |
  +--> immutable digest consumed by the companion GitOps repository
```

There is no database, downstream service, cloud API, or secret store in the
current architecture.

## Component responsibilities

### Application entry point

Creates the FastAPI application, connects routes, initializes validated
configuration, and establishes logging. It must remain thin; endpoint-specific
behaviour belongs in focused modules only when separation improves clarity.

### Configuration

Reads the documented environment variables once, applies defaults, validates
accepted values, and exposes a typed application configuration. It creates the
allow-listed response for `/config-summary`; callers cannot query arbitrary
environment keys.

### Endpoints

- `/health` reports process responsiveness without external dependency checks.
- `/version` reports the single application version.
- `/config-summary` reports only the approved operational configuration.

### Logging

Writes structured JSON to standard output so the same logging contract works in
a terminal, Docker, and a container platform. Logging must not expose
the entire environment, request bodies, or secrets.

### Tests

Run the application in process without opening a real network port where
possible. Unit tests cover configuration; API tests cover status codes and JSON
contracts; the CI workflow also verifies the packaged runtime boundary.

### Container image

Packages the application and runtime dependencies using a pinned Python base
image, a non-root runtime user, and a small build context. Docker is a delivery
boundary, not a place for environment-specific configuration.

### CI/CD pipeline

The CI workflow runs quality gates, builds an image, and scans it without
publishing or deploying. The separate tag-triggered release workflow repeats
those gates and publishes the versioned image to GHCR.

## Data and request flow

1. Environment variables enter at process startup.
2. The configuration component validates them or terminates startup clearly.
3. A caller sends an HTTP request to one of the three read-only endpoints.
4. The endpoint returns a fixed or allow-listed JSON representation.
5. Request metadata and the result are logged as structured JSON to stdout.

The service stores no application data between requests.

## Trust boundaries

- HTTP input is untrusted even though the service is described as internal.
- Environment variables are deployment input and must be validated.
- `/config-summary` crosses an information-disclosure boundary and therefore
  uses an explicit allow-list.
- The Docker build context must exclude local credentials and generated files.
- Third-party packages and the base image are supply-chain inputs checked by
  dependency pinning and image scanning.
- A registry or deployment platform is outside the initial boundary.

## Quality attributes

- **Clarity:** another engineer can explain the endpoints and pipeline stages.
- **Testability:** behaviour can be verified without cloud services.
- **Reproducibility:** declared dependencies and the base image produce a
  repeatable container build.
- **Security:** least-privileged runtime, no secret exposure, and image scanning.
- **Operability:** health, version, safe configuration, and structured logs aid
  diagnosis.
- **Auditability:** work proceeds through bounded issues and focused commits.

## Current boundaries and future changes

Do not add a database, authentication, cloud integration, Kubernetes, registry
publishing, or deployment merely to make the example appear production-like.
Each would require separate requirements, threat and cost review, and
maintainer approval.
