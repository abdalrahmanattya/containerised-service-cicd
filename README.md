# AI-Assisted Cloud Engineering Starter

This repository is the reusable Phase 0 starting point for learning how to lead
an AI-assisted cloud engineering workflow. It is deliberately small: the goal
is to practise context, review, Git, documentation, and safe collaboration
before adding cloud resources.

## Phase 0 outcomes

By completing this phase, you will be able to:

- explain the difference between Git, a local repository, and GitHub;
- inspect changes before accepting or committing them;
- make small commits with a clear purpose;
- give Codex durable project instructions in `AGENTS.md`;
- record decisions and a reliable resume point in project documentation; and
- restart the terminal without losing the project's working context.

No cloud account, GitHub account, credentials, or paid service is required.

## Programme roadmap

The complete learning path is stored in `docs/learning-roadmap.md`. It defines
Phase 0, Projects 1–7, the workflow used for every task, increasing Codex
autonomy, safety rules, and the assessment after each project. This repository
therefore remains sufficient context when work moves primarily to Terminal.

## Repository map

| Path | Purpose |
| --- | --- |
| `AGENTS.md` | Instructions Codex should follow in this repository |
| `CHANGELOG.md` | Human-readable record of notable changes |
| `docs/architecture.md` | System boundaries and architectural overview |
| `docs/development.md` | Repeatable local workflow and tests |
| `docs/learning-roadmap.md` | Phase 0 and the seven-project learning path |
| `docs/project-journal.md` | Current state, recent work, and next step |
| `docs/decisions/` | Architecture Decision Records (ADRs) |
| `.github/pull_request_template.md` | Review checklist for future pull requests |
| `scripts/test-context-resume.sh` | Checks that durable restart context exists |

## First local checks

Open Terminal, move to this repository, and run:

```sh
git --version
git status
git log --oneline --decorate --graph
git remote -v
```

What these commands tell you:

- `git --version` confirms that Git is available.
- `git status` shows the current branch and uncommitted changes.
- `git log` shows the small commits that built this starter.
- `git remote -v` shows where code would be sent. No output is expected because
  Phase 0 intentionally has no remote.

### Set your real author identity before sharing

This repository starts with local-only training metadata so commits can be
created without assuming your identity:

```sh
git config --local --get user.name
git config --local --get user.email
```

Before publishing the repository, replace it with the name and email you want
recorded in future commits:

```sh
git config --local user.name "Your Name"
git config --local user.email "you@example.com"
```

These settings are commit metadata, not login credentials. Authentication to a
hosting service is a separate step and is intentionally outside Phase 0.

## The safe AI-assisted Git loop

Use this loop for every small task:

1. **Orient:** Ask Codex to read `AGENTS.md`, the journal, and Git status.
2. **Plan:** Agree on one small outcome and its acceptance checks.
3. **Change:** Let Codex edit only the files needed for that outcome.
4. **Inspect:** Run `git diff` and read the change yourself.
5. **Verify:** Run the relevant test or documentation check.
6. **Record:** Update the journal or decision record if context changed.
7. **Commit:** Stage deliberately and use a focused commit message.

Useful inspection commands:

```sh
git status --short
git diff
git diff --staged
```

Never commit secrets, private keys, state files, or real credentials. If an AI
suggests a destructive command or a cloud-changing operation, stop and verify
the target and consequences first.

## Context restart exercise

The main Phase 0 exercise proves that project context lives in the repository,
not only in one terminal conversation. Follow the test in
[`docs/development.md`](docs/development.md#terminal-restart-context-test).

## Definition of done

Phase 0 is complete when:

- the context-resume check passes;
- `git status` reports a clean working tree;
- `git log --oneline` shows several focused commits;
- you can explain what each repository document is for; and
- you know that no remote or cloud credentials were configured for you.
