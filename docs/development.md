# Development guide

Run commands from the repository root unless a step says otherwise. This file
distinguishes commands that work now from tools planned for later issues.

## Current prerequisites

- A POSIX-compatible shell
- Git

The current machine has Git and Python 3.9.6. Project application development
will target Python 3.11 or newer. Docker, Ruff, pytest, `uv`, Hadolint, and Trivy
were not available when planning was recorded. Do not treat those tools as
installed and do not install them without reviewing Issue 001 or the relevant
delivery issue first.

No remote repository, registry, cloud account, or credentials are required.

## Begin a work session

1. Inspect `git status --short --branch`.
2. Read `AGENTS.md` and the journal's **Resume here** section.
3. Read recent history with `git log --oneline --decorate -5`.
4. Read the current issue and state its small outcome and acceptance criteria.
5. Inspect unexpected changes before doing anything else.

## Current verification

Only documentation and planning checks are available before Issue 001:

```sh
./scripts/test-context-resume.sh
git diff --check
git status --short --branch
```

## Planned application commands

Issue 001 will add and verify exact commands for:

- creating an isolated Python 3.11-or-newer environment;
- installing pinned runtime and development dependencies;
- formatting and linting with Ruff;
- running tests with pytest; and
- starting the FastAPI application with Uvicorn.

Issue 005 will add verified Docker build, run, inspection, and smoke-test
commands. Issue 006 will document the matching CI and vulnerability-scan
commands. Until those issues are complete, README examples are expected
behaviour rather than executable instructions.

## Review and commit loop

```sh
git diff
git diff --check
git add path/to/intended/file
git diff --staged
git commit -m "type: focused outcome"
```

Stage explicit paths so unrelated work cannot enter a commit. A feature branch
should contain one endpoint or one delivery concern, not a mixture.

## Terminal restart context test

1. Ensure the journal contains an accurate **Resume here** action.
2. Run `./scripts/test-context-resume.sh`.
3. Commit the reviewed change or clearly record why work is uncommitted.
4. Start a fresh Codex session in this repository.
5. Ask Codex to explain the project's purpose, rules, state, next action, and
   working-tree status using repository evidence.

The exercise passes when the answer identifies Project 3, its three endpoints,
its safety boundaries, the current issue, and the actual Git state without
depending on the previous conversation.

## External actions

Inspect `git remote -v` before discussing remote execution. Configuring a
remote, authenticating, publishing an image, or deploying are separate actions.
They require an explicit destination, version, credential strategy, and learner
approval; none is part of the default local workflow.
