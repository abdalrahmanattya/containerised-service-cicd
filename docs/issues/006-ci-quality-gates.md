# Issue 006: Add CI quality and security gates

## Outcome

Define a GitHub Actions workflow that runs formatting/linting, tests, container
build, and image vulnerability scanning as distinct understandable gates.

## Acceptance criteria

- The workflow uses pinned action revisions and least-required permissions.
- Each gate runs the same core command documented for local use.
- Dependency caching does not bypass installation or verification.
- A failed gate prevents dependent later work.
- The vulnerability threshold and exception process are documented.
- The workflow does not publish, deploy, or require repository secrets.
- If no remote is configured, workflow execution is inspected locally without
  claiming that GitHub executed it.

## Out of scope

Registry credentials, image publication, deployment, and environment promotion.
