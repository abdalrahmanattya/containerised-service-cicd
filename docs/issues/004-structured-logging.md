# Issue 004: Emit structured logs

## Outcome

Produce one-line JSON application and request logs suitable for collection from
standard output.

## Acceptance criteria

- Required log fields match `docs/requirements.md`.
- Request completion records method, path, status code, and duration.
- Tests verify stable fields without asserting exact timestamps or durations.
- Tests demonstrate that request bodies and unrelated environment values are
  not logged.
- Logging behaviour and example output are documented.

## Out of scope

External log services, tracing platforms, metrics backends, and dashboards.
