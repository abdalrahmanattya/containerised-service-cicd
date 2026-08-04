# Project journal

This is the current hand-off record for humans and fresh Codex sessions. Keep
it factual and replace stale status rather than accumulating a transcript.

## Current status

- **Project:** 3 — Containerised Service with CI/CD
- **State:** Issue 006 complete; ready for Issue 007
- **Branch:** `main`
- **Environment:** Local macOS repository; Git author configured; no remote
- **Available tools:** Git, Python 3.9.6, Python 3.13, and Docker Desktop 29.6.2
- **Missing planned tools:** Hadolint; Trivy is available through its pinned
  Docker image for the CI scan
- **Safety:** No credentials, registry, cloud resources, deployment, or image
  publication are configured

## Completed

- Created this separate sibling repository from the reusable Phase 0 starter.
- Preserved the complete learning roadmap and durable working method.
- Defined Project 3's purpose, usefulness, intended usage, requirements,
  architecture, non-goals, and safety boundaries.
- Selected the Python service and local-first delivery stack in ADR-002.
- Split implementation into seven ordered, bounded issues.
- Designated Issue 001 as the first implementation outcome.
- Added the Python package scaffold, pinned Issue 001 dependencies, and the
  tested `GET /health` endpoint.
- Verified formatting, linting, three automated tests, and a localhost smoke
  request returning `{"status":"healthy"}`.
- Added `GET /version`, backed by the package metadata version, and verified
  its endpoint and source consistency.
- Added startup-validated environment settings and the allow-listed
  `/config-summary` endpoint, including invalid-startup and non-disclosure
  tests.
- Added JSON application and request logging with required fields and tests
  proving request bodies and arbitrary extras are excluded.
- Added a digest-pinned Python image, non-root runtime user, Docker build
  context exclusions, and verified container endpoint smoke tests.
- Added pinned-revision GitHub Actions quality gates for formatting, linting,
  tests, container build, non-root verification, and Trivy scanning. Documented
  the high/critical threshold and time-bounded vulnerability exception process.
- The local Trivy run correctly failed on three fixed HIGH Starlette findings
  inherited from the current FastAPI dependency pin; Issue 007 will diagnose
  this controlled failure before any dependency repair is proposed.

## Decisions

- [ADR-001](decisions/ADR-001-project-working-method.md): repository files and
  Git history are the durable source of project context.
- [ADR-002](decisions/ADR-002-service-and-delivery-stack.md): use FastAPI,
  Uvicorn, pytest, Ruff, Docker, GitHub Actions, and Trivy with no default
  publishing or deployment.
- The root README is the primary user entry point and must contain verified
  step-by-step usage as functionality becomes available.

## Resume here

Begin [Issue 007](issues/007-failure-exercise-and-release.md) on a branch named
`feature/007-failure-exercise-release`:

1. Define the versioned artifact hand-off without publishing or deploying it.
2. Keep registry credentials and external services out of the default workflow.
3. Diagnose a deliberately failed gate before repairing it.

## Open questions

- Will a remote repository be added later for an actual GitHub Actions run?
- Will the optional final image be exported locally or published to a registry?

The last two questions are intentionally deferred and do not block local
implementation.

## Session hand-off checklist

- [x] Current state is accurate.
- [x] The next action is concrete and small.
- [x] Planning diff has been reviewed and committed.
- [x] Project-specific context verification has passed.
- [x] No secret, credential, remote, or external artifact was added.
