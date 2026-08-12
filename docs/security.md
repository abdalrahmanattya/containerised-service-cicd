# CI security policy

The pull-request and release workflows scan the locally built image with Trivy
before a versioned image can be published. The scan fails for fixed `HIGH` or
`CRITICAL` vulnerabilities. Unfixed findings are reported separately by the
scanner but do not fail this gate because there may not yet be a vendor
remediation. The CI scanner uses the immutable Docker Hub multi-platform index
for `aquasec/trivy:0.58.1`:

```text
aquasec/trivy@sha256:ab70a02200597efa04748f210f793936eb647cbcdb0ea69cc30b226d6f5a22c7
```

There is no blanket ignore list. A proposed exception must be recorded in a
reviewed issue or ADR with the CVE, affected component, reason, compensating
control, owner, and expiry date. The exception must be narrowly scoped and
removed when the dependency or base image is updated. Changing the workflow's
threshold or adding an ignore requires maintainer review.

The pull-request validation workflow has no registry credentials, publish step,
or deployment step. The release workflow uses only the short-lived
`GITHUB_TOKEN` with scoped package and attestation permissions after the same
quality, runtime, and vulnerability gates pass.
