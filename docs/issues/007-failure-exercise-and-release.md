# Issue 007: Diagnose a failed pipeline and prepare release v0.1.0

## Outcome

Complete the roadmap's evidence-led failure exercise, then document and tag the
first finished local release.

## Acceptance criteria

- One controlled CI failure is introduced on a focused branch.
- The learner identifies the failed stage and cites its evidence before any
  repair is proposed.
- The repair is limited to the diagnosed cause and all gates pass afterward.
- The changelog and README describe the completed `v0.1.0` behaviour.
- A reviewed local Git tag `v0.1.0` identifies the release commit.
- Any image export or publication occurs only if separately configured and
  explicitly approved.

## Out of scope

Production deployment and automatic registry publication.
