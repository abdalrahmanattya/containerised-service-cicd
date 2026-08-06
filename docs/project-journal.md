# Project journal

This is the current hand-off record for humans and fresh Codex sessions. Keep
it factual and replace stale status rather than accumulating a transcript.

## Current status

- **Project:** 3 — Containerised Service with CI/CD
- **State:** Issue 007 follow-up in progress; preparing multi-architecture
  release `v0.1.3` for Project 5's arm64 local cluster
- **Branch:** `feature/007-multiarch-release`
- **Environment:** Local macOS repository; Git author configured; GitHub remote
  configured as `origin`
- **Available tools:** Git, Python 3.9.6, Python 3.13, and Docker Desktop 29.6.2
- **Missing planned tools:** Hadolint; Trivy is available through its pinned
  Docker image for the CI scan
- **Safety:** No credentials were added. The new image has not been published
  yet; publication remains limited to the approved semantic tag workflow.

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
- Diagnosed the Trivy failure as FastAPI `0.116.1` constraining vulnerable
  Starlette `0.47.3`; upgraded to FastAPI `0.141.1` and Starlette `1.3.1`.
- Re-ran the full checks successfully: 14 tests passed, the image ran as a
  non-root user, and Trivy reported zero HIGH or CRITICAL findings.
- Documented the completed `v0.1.0` release and prepared its local Git tag.
- Added a SHA-pinned GHCR publication workflow triggered only by semantic
  version tags, using `GITHUB_TOKEN`, BuildKit provenance, and an SBOM.
- The first `v0.1.1` publication attempt reached the build step but failed
  because the default Docker Buildx driver does not support attestations.
- Added the SHA-pinned Docker Buildx container builder required by the
  provenance and SBOM settings; the failed tag is not being reused.
- Bumped the single package version source and active release documentation to
  `0.1.2`; the historical `v0.1.0` release remains unchanged.
- Diagnosed Project 5's local image pull failure: the `v0.1.2` image index has
  only a linux/amd64 manifest while Docker Desktop Kubernetes is arm64.

## Decisions

- [ADR-001](decisions/ADR-001-project-working-method.md): repository files and
  Git history are the durable source of project context.
- [ADR-002](decisions/ADR-002-service-and-delivery-stack.md): use FastAPI,
  Uvicorn, pytest, Ruff, Docker, GitHub Actions, and Trivy with no default
  publishing or deployment.
- The root README is the primary user entry point and must contain verified
  step-by-step usage as functionality becomes available.

## Resume here

Finish the multi-architecture `v0.1.3` release after reviewing the exact GHCR
publication:

1. Review and merge this workflow and package-version change.
2. Confirm the package remains public and that `GITHUB_TOKEN` may receive
   `packages: write`, `attestations: write`, and `id-token: write`.
3. Push tag `v0.1.3` through the reviewed workflow, then record the resulting
   multi-architecture digest in Project 5.

## Open questions

- Will the optional final image be exported locally or published to a registry?

The last two questions are intentionally deferred and do not block local
implementation.

## Session hand-off checklist

- [x] Current state is accurate.
- [x] The next action is concrete and small.
- [x] Planning diff has been reviewed and committed.
- [x] Project-specific context verification has passed.
- [x] No secret, credential, remote, or external artifact was added.
