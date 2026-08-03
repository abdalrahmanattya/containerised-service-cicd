# Issue 001: Establish the service scaffold and health endpoint

## Outcome

Create the smallest maintainable Python application that serves
`GET /health`, with its dependency metadata and automated test.

## In scope

- Choose and document the exact supported Python version and dependency pins.
- Add the minimal application package and FastAPI entry point.
- Implement only `GET /health`.
- Add pytest configuration and endpoint tests.
- Add Ruff configuration and relevant Python ignore rules.
- Replace the README's planned local setup and test placeholders with verified
  commands for this issue.

## Out of scope

- `/version` and `/config-summary`
- Custom structured logging
- Dockerfiles and container commands
- CI/CD workflows, scanners, registries, and deployment

## Acceptance criteria

- `GET /health` returns HTTP `200` and exactly `{"status":"healthy"}`.
- An unsupported method or unknown path retains framework-standard behaviour.
- Tests pass using the documented isolated environment.
- Ruff formatting and lint checks pass.
- Runtime dependencies are separate from development-only dependencies.
- The README commands have been executed successfully on this machine.

## Verification

Record the exact environment creation, dependency installation, format, lint,
test, and local-run commands in `docs/development.md`, then run them. Review
`git diff` and `git diff --check` before committing.
