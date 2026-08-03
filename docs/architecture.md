# Architecture

## Purpose and scope

This repository is a learning scaffold, not a deployed system. Its architecture
is the working method: durable context, small Git changes, local verification,
and deliberate human review. Phase 0 has no runtime, cloud resources, network
dependency, or secrets.

## Context model

```text
Learner intent
    |
    v
README + AGENTS.md ---------> Codex session rules
    |                              |
    v                              v
Journal + ADRs <------------ reviewed changes
    |                              |
    +----------> Git history <-----+
                      |
                      v
              fresh-session resume
```

The repository is the durable source of truth. A chat or terminal session is
temporary and may disappear. The files have distinct jobs:

- `README.md` explains purpose and entry points.
- `AGENTS.md` tells Codex how to work safely in the repository.
- `docs/project-journal.md` records time-sensitive state and the next action.
- ADRs record durable decisions and their trade-offs.
- Git history records what changed in reviewable increments.

## Boundaries

### Inside Phase 0

- Local documentation and a local Git repository
- A shell-based structural verification test
- Review conventions for future work

### Outside Phase 0

- GitHub or another remote hosting service
- CI/CD execution
- Cloud providers and deployed infrastructure
- Real credentials, secrets, cost, or production data

Those capabilities may be added in later projects only when their requirements,
safety controls, and verification approach are explicit.

## Quality attributes

- **Recoverability:** a fresh session can reconstruct context from versioned
  files and history.
- **Auditability:** each commit has one understandable purpose.
- **Safety:** default actions are local and read-only; external changes require
  explicit approval.
- **Clarity:** instructions and commands are understandable to a beginner.
- **Reusability:** future projects can copy this structure and replace the
  project-specific content.

## Evolution rule

When a future project gains actual components, update this document with the
component responsibilities, data flow, trust boundaries, dependencies, and
deployment model. Do not let the diagram become a substitute for the written
assumptions and decisions.
