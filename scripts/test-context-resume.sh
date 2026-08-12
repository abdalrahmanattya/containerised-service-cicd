#!/bin/sh

set -eu

repository_root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
cd "$repository_root"

checks_run=0

pass() {
  checks_run=$((checks_run + 1))
  printf 'ok %s - %s\n' "$checks_run" "$1"
}

fail() {
  checks_run=$((checks_run + 1))
  printf 'not ok %s - %s\n' "$checks_run" "$1" >&2
  exit 1
}

require_file() {
  description=$1
  path=$2

  if [ -f "$path" ]; then
    pass "$description"
  else
    fail "$description (missing $path)"
  fi
}

require_text() {
  description=$1
  path=$2
  expected_text=$3

  if grep -Fq "$expected_text" "$path"; then
    pass "$description"
  else
    fail "$description (expected text not found in $path)"
  fi
}

printf 'TAP version 13\n'

if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  pass 'running inside a Git working tree'
else
  fail 'running inside a Git working tree'
fi

require_file 'repository purpose is documented' 'README.md'
require_file 'complete learning roadmap exists' 'docs/learning-roadmap.md'
require_file 'license exists' 'LICENSE'
require_file 'Project 3 requirements exist' 'docs/requirements.md'
require_file 'working-method decision exists' \
  'docs/decisions/ADR-001-project-working-method.md'
require_file 'service stack decision exists' \
  'docs/decisions/ADR-002-service-and-delivery-stack.md'
require_file 'first implementation issue exists' \
  'docs/issues/001-scaffold-and-health-endpoint.md'
require_file 'restart exercise is documented' 'docs/development.md'

require_text 'README identifies Project 3' 'README.md' \
  '# Containerised Service with CI/CD'
require_text 'requirements define the health endpoint' 'docs/requirements.md' \
  '### `GET /health`'
require_text 'roadmap includes the capstone destination' \
  'docs/learning-roadmap.md' \
  '## Project 7 — Capstone: Self-Service Cloud Environment Platform'
require_text 'working-method decision is accepted' \
  'docs/decisions/ADR-001-project-working-method.md' '**Status:** Accepted'
require_text 'service stack decision is accepted' \
  'docs/decisions/ADR-002-service-and-delivery-stack.md' '**Status:** Accepted'
require_text 'manual terminal restart test is available' 'docs/development.md' \
  '## Terminal restart context test'

printf '1..%s\n' "$checks_run"
printf 'Public repository context is ready. Local orchestration notes remain outside Git.\n'
