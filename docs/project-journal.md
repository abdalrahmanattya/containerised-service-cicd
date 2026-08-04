# Project journal

This is the current hand-off record for humans and fresh Codex sessions. Keep
it factual and replace stale status rather than accumulating a transcript.

## Current status

- **Project:** 3 — Containerised Service with CI/CD
- **State:** Issue 001 complete; ready for Issue 002
- **Branch:** `main`
- **Environment:** Local macOS repository; Git author configured; no remote
- **Available tools:** Git, Python 3.9.6, and Python 3.13
- **Missing planned tools:** Docker, Hadolint, and Trivy
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

## Decisions

- [ADR-001](decisions/ADR-001-project-working-method.md): repository files and
  Git history are the durable source of project context.
- [ADR-002](decisions/ADR-002-service-and-delivery-stack.md): use FastAPI,
  Uvicorn, pytest, Ruff, Docker, GitHub Actions, and Trivy with no default
  publishing or deployment.
- The root README is the primary user entry point and must contain verified
  step-by-step usage as functionality becomes available.

## Resume here

Begin [Issue 002](issues/002-version-endpoint.md) on a branch named
`feature/002-version-endpoint`:

1. Use the package version in `pyproject.toml` as the single version source.
2. Add only `GET /version` and its tests.
3. Update the verified README and development commands if behaviour changes.
4. Do not add configuration, custom logging, Docker, or CI/CD yet.

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
