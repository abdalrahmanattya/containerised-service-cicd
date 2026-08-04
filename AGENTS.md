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
- Name feature branches `feature/<issue-number>-<short-outcome>` so the branch
  communicates the work, for example `feature/001-service-scaffold-health`.
- Update `docs/project-journal.md` when the current state or next step changes.
- Add an ADR for a durable decision with meaningful trade-offs.
- Update `CHANGELOG.md` for notable user-visible changes.
- At the end of every completed feature, explain what was accomplished and give
  the exact commands needed to test it, including the expected result.
- Add concise docstrings or comments to functions when their purpose or a
  non-obvious decision needs explanation. Add a comment before a non-trivial
  loop to explain its purpose or invariant; do not narrate obvious syntax.
- Keep the root `README.md` as the primary user entry point. It must explain
  what the project is, what it does, why it is useful, prerequisites, exact
  step-by-step local usage, inputs and outputs, safety boundaries, and
  non-goals. Update it whenever behaviour or the verified workflow changes.

## Safety boundaries

- Never add secrets, tokens, passwords, private keys, or real credentials.
- Do not run cloud-changing commands (`apply`, deploy, delete, or equivalent)
  without the learner explicitly approving the exact action and target.
- Do not configure a remote, create an online repository, or push code unless
  explicitly requested and authentication has been verified.
- Prefer read-only checks and local validation.
- Pause before destructive or difficult-to-reverse operations.
- Do not publish a container image, configure registry credentials, or deploy
  the service without explicit approval of the destination and version.
- Never return arbitrary environment variables from `/config-summary`; expose
  only the fields explicitly allowed by `docs/requirements.md`.

## Verification

Until application tooling is added, run:

```sh
./scripts/test-context-resume.sh
git status --short --branch
git log --oneline --decorate -5
```

As application tools are added, record their exact format, lint, test, build,
and security commands in `docs/development.md` and keep them verified.
