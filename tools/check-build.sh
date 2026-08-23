#!/usr/bin/env bash
# Post-build checks. Run by CI and locally:  ./tools/check-build.sh _site
set -uo pipefail
SITE="${1:-_site}"
[ -d "$SITE" ] || { echo "check-build: '$SITE' not found" >&2; exit 1; }
python3 "$(dirname "${BASH_SOURCE[0]}")/check_build.py" "$SITE"
