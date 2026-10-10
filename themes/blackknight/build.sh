#!/bin/sh
set -eu
base=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
output=${BK_OUTPUT_DIR:-"$base/../../build/out/blackknight"}
command -v edje_cc >/dev/null
mkdir -p "$output"
edje_cc -id "$base/assets" "$base/wallpaper.edc" "$output/blackknight-still.edj"
edje_cc -DANIMATED=1 -id "$base/assets" "$base/wallpaper.edc" "$output/blackknight-animated.edj"
