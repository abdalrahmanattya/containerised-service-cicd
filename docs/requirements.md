# Project 3 requirements

## Outcome

Build a small internal HTTP service and a reviewable delivery pipeline. The
service must be understandable enough that the learner can explain every
endpoint and every pipeline stage, while still demonstrating realistic
configuration, logging, testing, container, and security practices.

## Functional requirements

### `GET /health`

- Return HTTP `200` while the application is running and responsive.
- Return JSON with the exact shape `{"status":"healthy"}`.
- Perform no external network, database, or cloud checks.

This is a liveness-style endpoint: it proves that this process can answer a
request, not that unrelated external systems are available.

### `GET /version`

- Return HTTP `200`.
- Return JSON containing one non-empty `version` string.
- Use one application version source so API output, release notes, and the
  container artifact can be kept consistent.

### `GET /config-summary`

- Return HTTP `200` when startup configuration is valid.
- Return only `service_name`, `environment`, and `log_level`.
- Never return the full process environment or fields not explicitly listed.
- Reflect validated runtime configuration rather than rereading untrusted input
  independently for each request.

## Configuration contract

| Environment variable | Default | Accepted values |
| --- | --- | --- |
| `SERVICE_NAME` | `containerised-service` | Non-empty text suitable for logs |
| `APP_ENV` | `development` | `development`, `test`, `staging`, or `production` |
| `LOG_LEVEL` | `INFO` | `DEBUG`, `INFO`, `WARNING`, `ERROR`, or `CRITICAL` |

Values must be normalized only where documented; invalid values must stop
startup with a clear, non-secret error. Tests must cover defaults, overrides,
and invalid configuration.

Surrounding whitespace is stripped from all three values. `SERVICE_NAME` must be
1–100 characters and may contain only letters, numbers, dots, underscores, and
hyphens. `APP_ENV` and `LOG_LEVEL` retain the case shown in the accepted-values
table after whitespace is stripped.

`SERVICE_VERSION` is not read by the initial implementation. The package
metadata version remains the single source used by `GET /version` and future
release artifacts.

## Logging requirements

- Application and request logs must be emitted as one JSON object per line.
- Each entry must include a timestamp, severity level, service name, and event.
- Request-completion logs must include method, path, status code, and duration.
- Logs must not include secrets, the complete environment, or request bodies.
- Tests should verify stable required fields without depending on timestamps or
  exact timing values.

## Container requirements

- The image must build from a reviewed Dockerfile and pinned dependency input.
- The runtime must use a non-root user.
- The final image must exclude source-control metadata, local environments,
  tests, caches, credentials, and unnecessary build tools.
- The service must listen on the documented container port and accept runtime
  configuration through environment variables.
- A local smoke test must exercise all three endpoints from the running image.

## CI/CD requirements

The pipeline must have understandable stages for:

1. formatting and linting;
2. automated tests;
3. container image build; and
4. container vulnerability scanning.

Stages must fail when their corresponding check fails. The learner will
diagnose one deliberately failed CI run from evidence before making a repair.
Publishing or exporting a versioned image is optional and occurs only after an
explicit destination and authentication decision.

## Acceptance criteria

- Endpoint, configuration, and error-path tests pass.
- Local formatting and linting pass.
- The container image builds reproducibly and runs using documented commands.
- The running container returns the documented endpoint responses.
- The image passes the agreed vulnerability policy or documents reviewed
  exceptions.
- Pipeline stages, dependencies, and failure conditions are documented.
- The README contains verified setup, local-run, test, container, and endpoint
  instructions.
- No secret, credential, image registry, deployment, or cloud resource is
  required.

## Non-goals

- A database, persistent storage, or business-domain API
- User authentication or authorization
- Cloud-provider integration
- Kubernetes manifests or deployment
- Production availability, scaling, or disaster recovery
- Automatic publication to a container registry
- Returning arbitrary environment variables or secret values
