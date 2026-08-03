# ADR-001: Use repository files and Git as durable project context

- **Status:** Accepted
- **Date:** 2026-08-01
- **Decision owners:** Learner and project maintainer

## Context

AI conversations and terminal sessions are temporary. A new Codex session may
not have the previous conversation, and undocumented decisions can be forgotten
or reinterpreted. Cloud engineering also benefits from changes that can be
reviewed, audited, and recovered.

We need a working method that is useful with Codex but remains understandable
and controllable by a human.

## Decision

Use versioned repository files and Git history as the durable source of project
context:

- `AGENTS.md` defines how Codex should operate.
- `README.md` defines the project purpose and entry points.
- `docs/project-journal.md` gives the current state and exact resume action.
- ADRs preserve important decisions and trade-offs.
- Small commits preserve a reviewable history of completed outcomes.

At the beginning of a session, Codex must read those sources and inspect Git
before making changes. At the end of meaningful work, the journal must contain
an accurate hand-off.

## Consequences

### Benefits

- Work can resume after a terminal restart without relying on chat memory.
- Humans can review the same context the AI uses.
- Decisions and changes are auditable and portable between tools.
- Small commits make mistakes easier to understand and correct.

### Costs

- Documentation and the journal require regular maintenance.
- Stale instructions can mislead a fresh session.
- The team must spend time reviewing changes rather than accepting AI output
  automatically.

## Alternatives considered

### Rely on conversation history

Rejected because access to earlier chats is not guaranteed and the context is
not naturally reviewed with the code.

### Keep one large notes file outside Git

Rejected because it lacks version history, is easy to lose, and separates the
working context from the repository it describes.

### Commit all generated work in large batches

Rejected because mixed changes are difficult to review, test, explain, and
revert safely.

## Verification

The terminal restart exercise in `docs/development.md` demonstrates the
decision. A fresh Codex session must reconstruct project purpose, rules,
current state, next step, and working-tree status from repository evidence.
