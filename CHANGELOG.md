# Changelog

All notable changes to this learning repository will be documented here. The
format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and
versions follow [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Project 3 requirements, architecture, service and delivery stack decision,
  and seven-issue implementation plan.
- A self-contained project introduction covering purpose, behaviour,
  usefulness, intended usage, and safety boundaries.
- Issue 001's Python package scaffold, FastAPI health endpoint, tests, and
  pinned development dependencies.
- Durable feature hand-off and code-commenting rules for upcoming issues.
- Issue 002's package-metadata version source and `GET /version` endpoint.
- Issue 003's validated environment settings and safe `/config-summary`
  endpoint.
- Issue 004's JSON application and request logging with body and extra-field
  exclusion tests.
- Issue 005's digest-pinned, non-root Docker image and local endpoint smoke-test
  workflow.
- Issue 006's pinned-action CI quality gates, non-root image check, and Trivy
  vulnerability-scan policy without publishing or deployment.
- Issue 002's reviewed, semantic-tag GHCR publication workflow with
  short-lived-token authentication, immutable digest reporting, provenance,
  and SBOM generation.

### Changed

- Replaced the reusable starter hand-off with Project 3 status and Issue 001 as
  the exact next implementation step.
- Made the root README the required primary user entry point for future work.
- Documented the verified Python 3.13 local development workflow.
- Documented the matching local commands for the CI workflow and security
  exception process.

## [0.1.0] - 2026-08-04

### Added

- Reusable Phase 0 repository structure and beginner quick start.
- Durable Codex instructions in `AGENTS.md`.
- Architecture, development, journal, and ADR documentation.
- Automated structural check and manual terminal-restart context exercise.
- Pull request review template and cloud-focused safety checklist.
- Project 3's FastAPI service with health, version, and configuration-summary
  endpoints.
- Validated configuration, structured JSON request logging, and a digest-pinned
  non-root Docker image.
- GitHub Actions quality gates for formatting, linting, tests, image building,
  and Trivy vulnerability scanning.
- Remediated the Trivy findings by upgrading FastAPI to `0.141.1` and Starlette
  to `1.3.1`; the release image scan reports zero HIGH or CRITICAL findings.
