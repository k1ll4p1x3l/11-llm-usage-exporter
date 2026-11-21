#!/usr/bin/env bash

set -euo pipefail

export GOCACHE="${GOCACHE:-$HOME/.cache/llm-usage-exporter/go-build}"
export GOMODCACHE="${GOMODCACHE:-$HOME/.cache/llm-usage-exporter/go-mod-cache}"

mkdir -p "$GOCACHE" "$GOMODCACHE"

echo "[check] gofmt"
if [[ -n "$(find . \
  -path './.codex' -prune -o \
  -path './.git' -prune -o \
  -path './dist' -prune -o \
  -path './vendor' -prune -o \
  -name '*.go' -type f -print0 | xargs -0 gofmt -l)" ]]; then
  echo "Go files are not formatted." >&2
  exit 1
fi

echo "[check] go test"
go test ./...

echo "[check] go race"
go test -race ./...

echo "[check] go vet"
go vet ./...

echo "[check] govulncheck"
govulncheck ./...

echo "[check] actionlint"
actionlint

echo "[check] gitleaks"
gitleaks detect --source . --no-banner --redact --exit-code 1

echo "[check] agent core metadata"
python3 scripts/verify_agent_core.py

echo "[check] public repository safety"
python3 scripts/public_repo_sanity_check.py

echo "[check] automation and artifact contract tests"
python3 -m unittest discover -s tests -p 'test_*.py' -v

echo "[check] goreleaser"
goreleaser healthcheck
goreleaser check
goreleaser release --snapshot --clean --skip=publish
git diff --exit-code -- go.mod go.sum
python3 scripts/verify_release_artifacts.py --dist dist

echo "[check] ok"
