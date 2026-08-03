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
require_file 'Codex instructions exist' 'AGENTS.md'
require_file 'current hand-off exists' 'docs/project-journal.md'
require_file 'complete learning roadmap exists' 'docs/learning-roadmap.md'
require_file 'working-method decision exists' \
  'docs/decisions/ADR-001-project-working-method.md'
require_file 'restart exercise is documented' 'docs/development.md'

require_text 'Codex has fresh-session orientation instructions' 'AGENTS.md' \
  'Start every new session by orienting'
require_text 'journal contains a precise resume section' \
  'docs/project-journal.md' '## Resume here'
require_text 'roadmap identifies the next practical project' \
  'docs/learning-roadmap.md' '## Project 1 — Cloud Configuration Validator'
require_text 'roadmap includes the capstone destination' \
  'docs/learning-roadmap.md' \
  '## Project 7 — Capstone: Self-Service Cloud Environment Platform'
require_text 'working-method decision is accepted' \
  'docs/decisions/ADR-001-project-working-method.md' '**Status:** Accepted'
require_text 'manual terminal restart test is available' 'docs/development.md' \
  '## Terminal restart context test'

printf '1..%s\n' "$checks_run"
printf 'Durable context is ready. Follow the journal Resume here section next.\n'
