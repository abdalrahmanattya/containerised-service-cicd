# Development guide

This guide turns the working method into repeatable steps. Run commands from
the repository root unless a step says otherwise.

## Prerequisites

- macOS Terminal or another POSIX-compatible shell
- Git
- Codex for the interactive resume exercise

No package manager, cloud command-line tool, remote repository, or credentials
are required in Phase 0.

## Begin a work session

1. Move into the repository.
2. Inspect `git status --short --branch`.
3. Read `AGENTS.md` and the **Resume here** section of the journal.
4. Read recent history with `git log --oneline --decorate -5`.
5. State one small outcome and how you will verify it.

If Git reports an unexpected change, inspect it before doing anything else.
It may belong to you or to another unfinished task.

## Make and review a change

```sh
# See unstaged changes
git diff

# Stage only the intended paths
git add path/to/file

# Review exactly what the commit would contain
git diff --staged

# Commit after verification
git commit -m "docs: describe the small outcome"
```

`git add .` is convenient, but explicit paths are easier to audit while
learning. A commit should answer one question: "What single outcome did this
change produce?"

## Local verification

Run the structural context check:

```sh
./scripts/test-context-resume.sh
```

Also check formatting errors and repository state:

```sh
git diff --check
git status --short --branch
```

The script is intentionally simple. It confirms that the durable files and key
resume instructions exist. It cannot judge whether Codex understood them, so
the manual exercise below completes the test.

## Terminal restart context test

This is a safe test of context recovery. It changes no cloud or remote system.

### Prepare

1. Finish or deliberately record any in-progress work.
2. Update `docs/project-journal.md` with a precise **Resume here** action.
3. Commit the relevant documentation.
4. Run `./scripts/test-context-resume.sh` and `git status`.

### Restart

1. Close the terminal window and the active Codex session.
2. Open a new terminal window.
3. Move back into this repository.
4. Start a new Codex session from the repository root.
5. Give Codex this read-only request:

> Orient yourself in this repository using its durable context. Do not modify
> files. Tell me the project's purpose, working rules, current status, exact
> next step, and whether the Git working tree contains changes. Cite the files
> you used.

### Expected evidence

Codex should read `AGENTS.md` without relying on the old chat, inspect Git, and
report all of the following:

- this is an AI-assisted cloud engineering learning starter;
- work should be small, reviewed, verified, and safely scoped;
- the current state and next action match `docs/project-journal.md`;
- ADR-001 makes repository files and Git the durable source of context; and
- the reported working-tree state agrees with `git status`.

The test passes when those facts are correct. If anything is missing, improve
the relevant durable document, commit the fix, close the session, and repeat.

## Optional remote work comes later

Before adding or using a remote, first inspect:

```sh
git remote -v
```

An empty result is expected in Phase 0. Adding a GitHub repository, choosing
visibility, authenticating, and pushing are separate actions that require an
explicit decision; this starter does not perform them automatically.

## Troubleshooting

### Git says "Author identity unknown"

Configure the identity you want stored in this repository's future commits:

```sh
git config --local user.name "Your Name"
git config --local user.email "you@example.com"
```

### A file appears unexpectedly in `git status`

Do not delete it immediately. Inspect its path and diff, decide whether it is
work to keep, and either include it in an appropriate commit or leave it alone.

### The context test is not executable

Run it through the shell once:

```sh
sh scripts/test-context-resume.sh
```

Then verify that Git records executable mode after the repository setup commit.
