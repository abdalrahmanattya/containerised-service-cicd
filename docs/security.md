# CI security policy

Issue 006 scans the locally built image with Trivy before any future release
workflow could publish it. The scan fails for fixed `HIGH` or `CRITICAL`
vulnerabilities. Unfixed findings are reported separately by the scanner but
do not fail this gate because there may not yet be a vendor remediation.

There is no blanket ignore list. A proposed exception must be recorded in a
reviewed issue or ADR with the CVE, affected component, reason, compensating
control, owner, and expiry date. The exception must be narrowly scoped and
removed when the dependency or base image is updated. Changing the workflow's
threshold or adding an ignore requires the learner's review.

The workflow has no registry credentials, publish step, deployment step, or
secret requirement. It builds and scans only the local CI image.
