# Architecture

## Purpose and scope

Project 3 is a small Python HTTP service surrounded by tests, a container build,
and CI/CD validation. Its runtime behaviour is intentionally narrow; most of
the learning value is in creating a predictable path from source to a reviewed
container artifact.

## Planned system context

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
  +--> export or publish only after explicit configuration and approval
```

There is no database, downstream service, cloud API, or secret store in the
initial architecture.

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
a terminal, Docker, and a future container platform. Logging must not expose
the entire environment, request bodies, or secrets.

### Tests

Exercise the application in process without opening a real network port where
possible. Unit tests cover configuration; API tests cover status codes and JSON
contracts; later container smoke tests verify the packaged runtime boundary.

### Container image

Packages the application and runtime dependencies using a pinned Python base
image, a non-root runtime user, and a small build context. Docker is a delivery
boundary, not a place for environment-specific configuration.

### CI/CD pipeline

Runs independent quality gates in an understandable order. It validates and
builds artifacts but does not deploy or publish by default.

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

## Evolution constraints

Do not add a database, authentication, cloud integration, Kubernetes, registry
publishing, or deployment merely to make the example appear production-like.
Each would require separate requirements, threat and cost review, and learner
approval.
