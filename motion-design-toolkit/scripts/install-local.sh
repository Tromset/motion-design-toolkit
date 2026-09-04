#!/usr/bin/env bash
# Back-compat wrapper: the repo root is the installable plugin.
set -euo pipefail
exec "$(cd "$(dirname "$0")/../.." && pwd)/scripts/install-local.sh" "$@"
