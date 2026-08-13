# ADR-003: Publish images for the supported local CPU architectures

- **Status:** Accepted
- **Date:** 2026-08-06
- **Decision owners:** Service maintainers

## Context

The companion GitOps deployment runs on Docker Desktop Kubernetes. The local
control-plane node is
`arm64`, while the published `v0.1.2` image index contains only `linux/amd64`.
Kubernetes therefore cannot pull the reviewed image on the local target.

## Decision

The versioned GHCR publication workflow will build and publish both
`linux/amd64` and `linux/arm64` manifests for each new release. The companion
GitOps deployment will continue to reference the resulting top-level immutable
digest.

## Consequences

- The same release can run on common Intel/AMD and Apple Silicon local nodes.
- Build time and registry storage increase because two platform images are
  produced.
- The platform list is explicit and reviewable rather than relying on a
  runner's default architecture.
- The companion GitOps deployment must update its digest after each
  multi-architecture release.

## Alternatives considered

### Publish amd64 only

Rejected because it cannot run on the current arm64 Docker Desktop target.

### Use a moving tag or local image

Rejected because GitOps desired state must retain an immutable, reviewable
artifact reference.
