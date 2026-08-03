# Issue 002: Add the version endpoint

## Outcome

Establish one application version source and expose it through `GET /version`.

## Acceptance criteria

- `GET /version` returns HTTP `200` with one non-empty `version` string.
- Tests prove the endpoint uses the chosen application version source.
- Version retrieval does not depend on Git being installed in the runtime image.
- Packaging and README documentation identify the same versioning approach.

## Out of scope

Configuration summaries, logging changes, containers, and pipeline work.
