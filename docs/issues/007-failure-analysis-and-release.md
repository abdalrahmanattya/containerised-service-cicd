# Issue 007: Diagnose a failed pipeline and prepare release v0.1.0

## Outcome

Complete an evidence-led failure analysis, then document and tag the
first finished local release.

## Acceptance criteria

- One controlled CI failure is introduced on a focused branch.
- The maintainer identifies the failed stage and cites its evidence before any
  repair is proposed.
- The repair is limited to the diagnosed cause and all gates pass afterward.
- The changelog and README describe the completed `v0.1.0` behaviour.
- A reviewed local Git tag `v0.1.0` identifies the release commit.
- Any image export or publication occurs only if separately configured and
  explicitly approved.

## Out of scope

Production deployment and automatic registry publication.

## Result

The CI failure was traced to FastAPI `0.116.1` constraining vulnerable
Starlette `0.47.3`. FastAPI `0.141.1` and Starlette `1.3.1` were selected as the
focused repair. The full local gates then passed: 14 tests, image build,
non-root verification, and a Trivy scan with zero HIGH or CRITICAL findings.
