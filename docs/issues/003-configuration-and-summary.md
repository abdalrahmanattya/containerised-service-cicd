# Issue 003: Validate configuration and expose a safe summary

## Outcome

Read the documented environment variables once at startup, validate them, and
implement `GET /config-summary` using an explicit allow-list.

## Acceptance criteria

- Defaults and valid overrides match `docs/requirements.md`.
- Invalid configuration stops startup with a clear, non-secret error.
- `GET /config-summary` returns exactly the three approved fields.
- Tests cover defaults, overrides, each invalid-value class, and an unrelated
  environment variable that must not appear in the response.
- README configuration and usage instructions are verified and current.

## Out of scope

Secret management, arbitrary environment inspection, Docker, and CI/CD.
