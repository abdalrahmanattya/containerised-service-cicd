# Project journal

This is the current hand-off record for humans and fresh Codex sessions. Keep
it factual and replace stale status rather than accumulating a transcript.

## Current status

- **Project:** 3 — Containerised Service with CI/CD
- **State:** Planning complete; ready for Issue 001
- **Branch:** `main`
- **Environment:** Local macOS repository; Git author configured; no remote
- **Available tools:** Git and Python 3.9.6
- **Missing planned tools:** Python 3.11+, Docker, Ruff, pytest, and Trivy
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

## Decisions

- [ADR-001](decisions/ADR-001-project-working-method.md): repository files and
  Git history are the durable source of project context.
- [ADR-002](decisions/ADR-002-service-and-delivery-stack.md): use FastAPI,
  Uvicorn, pytest, Ruff, Docker, GitHub Actions, and Trivy with no default
  publishing or deployment.
- The root README is the primary user entry point and must contain verified
  step-by-step usage as functionality becomes available.

## Resume here

Begin [Issue 001](issues/001-scaffold-and-health-endpoint.md) on a focused
feature branch:

1. Confirm the exact Python version and dependency pinning approach.
2. Agree on Issue 001's acceptance criteria before installing dependencies.
3. Create only the Python scaffold and `GET /health` with its tests.
4. Do not add the other endpoints, custom logging, Docker, or CI/CD yet.

## Open questions

- Which locally available installation method should provide Python 3.11 or
  newer for Issue 001?
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
