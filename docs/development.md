# Development guide

Run commands from the repository root unless a step says otherwise. This file
distinguishes commands that work now from tools planned for later issues.

## Current prerequisites

- A POSIX-compatible shell
- Git

The current machine has Git, Python 3.9.6, and `/opt/homebrew/bin/python3.13`.
Issue 001 targets Python 3.13. Docker, Hadolint, and Trivy are not available;
Ruff and pytest are installed into the project virtual environment rather than
globally.

No remote repository, registry, cloud account, or credentials are required.

## Begin a work session

1. Inspect `git status --short --branch`.
2. Read `AGENTS.md` and the journal's **Resume here** section.
3. Read recent history with `git log --oneline --decorate -5`.
4. Read the current issue and state its small outcome and acceptance criteria.
5. Inspect unexpected changes before doing anything else.

## Current verification

Run the durable-context and whitespace checks at every hand-off:

```sh
./scripts/test-context-resume.sh
git diff --check
git status --short --branch
```

## Issues 001 and 002 application commands

Run these from the repository root:

```sh
/opt/homebrew/bin/python3.13 -m venv .venv
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -e '.[dev]'
.venv/bin/ruff format --check src tests
.venv/bin/ruff check src tests
.venv/bin/pytest
.venv/bin/uvicorn containerised_service.main:app --reload
```

The server listens on `http://127.0.0.1:8000` until stopped with `Ctrl-C`.
In another terminal, verify the endpoint with:

```sh
curl http://127.0.0.1:8000/health
curl http://127.0.0.1:8000/version
```

Issue 003 will add configuration commands and tests. Issue 005 will add Docker
commands. Issue 006 will document the matching CI and vulnerability-scan
commands.

## Review and commit loop

```sh
git diff
git diff --check
git add path/to/intended/file
git diff --staged
git commit -m "type: focused outcome"
```

Stage explicit paths so unrelated work cannot enter a commit. A feature branch
should contain one endpoint or one delivery concern, not a mixture. Name it
`feature/<issue-number>-<short-outcome>`, such as
`feature/001-service-scaffold-health`, so Git history explains its purpose.

When an issue is complete, the hand-off must state what changed, link the
important files, list the exact format/lint/test/build/security commands that
were run, and show the expected or observed result. Functions should carry
concise explanatory docstrings where their purpose is not obvious; comments
before non-trivial loops should explain the loop's purpose or invariant.

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
