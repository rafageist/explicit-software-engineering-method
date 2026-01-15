#!/usr/bin/env sh
set -eu
SCRIPT_DIR="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
exec mmdc -p "$SCRIPT_DIR/puppeteer.json" "$@"
