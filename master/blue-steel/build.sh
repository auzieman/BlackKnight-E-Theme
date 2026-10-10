#!/bin/sh
set -eu
[ "$#" -eq 1 ] || { echo "Usage: sh build.sh NEW_OUTPUT_DIRECTORY" >&2; exit 2; }
command -v edje_cc >/dev/null || { echo "Missing approved remote edje_cc" >&2; exit 1; }
[ ! -e "$1" ] || { echo "Output must be new" >&2; exit 1; }
base=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
mkdir -p "$1"
out=$(cd "$1" && pwd)
edje_cc -id "$base/assets" "$base/material.edc" -o "$out/blackknight-material.edj"
sha256sum "$out/blackknight-material.edj" > "$out/blackknight-material.edj.sha256"
