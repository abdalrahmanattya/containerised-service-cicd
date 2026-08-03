# Issue 005: Package and run the service as a container

## Outcome

Build a reproducible Docker image that runs the service as a non-root user and
accepts the documented runtime configuration.

## Acceptance criteria

- The Dockerfile uses a pinned Python base-image reference.
- Dependency installation is reproducible and cache-friendly.
- The final process runs as a non-root user.
- `.dockerignore` excludes unnecessary and sensitive local content.
- The documented build and run commands work locally.
- A smoke test calls all three endpoints on the running container.

## Out of scope

Registry publication, orchestration, cloud deployment, and Kubernetes.
