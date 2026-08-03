# Repository instructions for Codex

## Mission

Help the learner practise a safe, reviewable, AI-assisted cloud engineering
workflow. Prefer teaching and small verified changes over generating a large
solution at once.

## Start every new session by orienting

Before proposing or making changes:

1. Read `README.md`.
2. Read `docs/learning-roadmap.md` for the current phase and its completion gate.
3. Read `docs/project-journal.md`, especially **Resume here**.
4. Read relevant files in `docs/decisions/` and `docs/architecture.md`.
5. Inspect `git status --short --branch` and the recent Git log.
6. Summarize the current state, intended next task, and any uncommitted work.

Do not assume that a previous terminal conversation is available. Repository
files and Git history are the durable source of context.

## Working rules

- Agree on a small outcome and acceptance criteria before implementation.
- Follow the current stage in `docs/learning-roadmap.md`; do not skip its
  completion gate or begin a later project without the learner's agreement.
- Keep changes narrow and explain unfamiliar terms in plain language.
- Preserve user changes; never discard or overwrite them without permission.
- Show and review the diff before committing.
- Run the smallest relevant verification after each change.
- Keep commits focused. Do not mix refactoring, features, and documentation.
- Update `docs/project-journal.md` when the current state or next step changes.
- Add an ADR for a durable decision with meaningful trade-offs.
- Update `CHANGELOG.md` for notable user-visible changes.

## Safety boundaries

- Never add secrets, tokens, passwords, private keys, or real credentials.
- Do not run cloud-changing commands (`apply`, deploy, delete, or equivalent)
  without the learner explicitly approving the exact action and target.
- Do not configure a remote, create an online repository, or push code unless
  explicitly requested and authentication has been verified.
- Prefer read-only checks and local validation.
- Pause before destructive or difficult-to-reverse operations.

## Verification

For the Phase 0 starter, run:

```sh
./scripts/test-context-resume.sh
git status --short --branch
git log --oneline --decorate -5
```

When future projects add tools, record their exact format, lint, test, and
security commands in `docs/development.md`.
