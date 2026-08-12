# Development guide

Run commands from the repository root unless a step says otherwise. This file
documents commands that work with the current v0.1.3 service and delivery
workflows.

## Current prerequisites

- A POSIX-compatible shell
- Git
- Python 3.13
- Docker (for image build and scan commands)

The application targets Python 3.13. Trivy runs through its pinned Docker
image; Ruff and pytest are installed into the project virtual environment.

The GitHub remote is configured for CI execution. No registry, cloud account,
or credentials are required.

## Inspect the repository

1. Inspect `git status --short --branch`.
2. Read the README and relevant architecture or requirements pages.
3. Read recent history with `git log --oneline --decorate -5`.
4. Inspect unexpected changes before doing anything else.

## Current verification

Run the whitespace and repository-state checks when reviewing a change:

```sh
git diff --check
git status --short --branch
```

## Application commands

Run these from the repository root:

```sh
python3.13 -m venv .venv
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
curl http://127.0.0.1:8000/config-summary
```

For a configuration override smoke test, start a separate process with:

```sh
SERVICE_NAME=payments-api APP_ENV=staging LOG_LEVEL=DEBUG \
  .venv/bin/uvicorn containerised_service.main:app --reload
```

The server writes structured JSON logs to standard output. Run these Docker
commands from the repository root:

```sh
docker build --tag containerised-service:0.1.3 .
docker run --rm --name containerised-service \
  --publish 8000:8000 \
  --env SERVICE_NAME=containerised-service \
  --env APP_ENV=development \
  --env LOG_LEVEL=INFO \
  containerised-service:0.1.3
```

In another terminal, call the three endpoints with `curl`. Confirm the image
user with `docker exec <container> id` while it is running. Issue 006 runs the
same core checks in GitHub Actions. Locally, inspect the workflow file and run:

```sh
.venv/bin/ruff format --check src tests
.venv/bin/ruff check src tests
.venv/bin/pytest
docker build --tag containerised-service:ci .
docker run --rm --entrypoint id containerised-service:ci -u
docker run --rm --volume /var/run/docker.sock:/var/run/docker.sock \
  aquasec/trivy:0.58.1 image --exit-code 1 \
  --severity HIGH,CRITICAL --ignore-unfixed --no-progress \
  containerised-service:ci
```

The Trivy command requires Docker network access to download its pinned scanner
image and vulnerability database. A scan fails for fixed high or critical
findings; see [`security.md`](security.md) before proposing an exception.

The CI workflow validates source and a local image; it does not log in to a
registry, push an image, or deploy. The separate release workflow publishes a
multi-architecture image only for semantic-version tags.

## Versioned image publication

The reviewed release workflow is `.github/workflows/publish-image.yml`. Inspect
its tag filter and permissions before creating a release tag:

```sh
sed -n '1,220p' .github/workflows/publish-image.yml
git diff --check
```

The workflow publishes `vMAJOR.MINOR.PATCH` tags to
`ghcr.io/abdalrahmanattya/containerised-service` using `GITHUB_TOKEN`, and
prints the resulting top-level digest in the GitHub Actions summary. Each
release builds `linux/amd64` and `linux/arm64` manifests so the image can run
on the Project 5 Docker Desktop target. BuildKit provenance and SBOM
attestations are enabled. Do not push a release tag until the exact
destination, version, package visibility, and permissions have been reviewed
and explicitly approved.

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

## External actions

Inspect `git remote -v` before discussing remote execution. Configuring a
remote, authenticating, publishing an image, or deploying are separate actions.
They require an explicit destination, version, credential strategy, and
maintainer approval; none is part of the default local workflow.
