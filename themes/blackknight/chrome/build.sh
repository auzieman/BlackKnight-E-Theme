#!/bin/sh
# Run through the approved remote BKC build route.
set -eu
echo "SVG-derived overlay retired. Build master/blue-steel/material.edc for the raster demonstration." >&2
exit 1
if [ "$#" -ne 2 ]; then
  echo "Usage: sh build.sh EDITABLE_SCIFI_TREE NEW_OUTPUT_DIRECTORY" >&2
  exit 2
fi
base=$(cd "$1" && pwd)
script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
out=$2
[ -f "$base/default.edc" ] || { echo "Missing default.edc" >&2; exit 1; }
[ ! -e "$out" ] || { echo "Output directory must be new" >&2; exit 1; }
command -v edje_cc >/dev/null || { echo "Missing approved edje_cc toolchain" >&2; exit 1; }
mkdir -p "$out"
out=$(cd "$out" && pwd)
mkdir "$out/source"
cp -R "$base/." "$out/source/"
# Artwork overlay contains no EDC; existing state machines remain intact.
cp -R "$script_dir/overrides/wrk/." "$out/source/wrk/"
(cd "$out/source" && edje_cc -id . -fd . default.edc -o "$out/blackknight-scifi.edj")
sha256sum "$out/blackknight-scifi.edj" > "$out/blackknight-scifi.edj.sha256"
