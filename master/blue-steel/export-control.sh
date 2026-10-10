#!/bin/sh
set -eu
[ "$#" -eq 1 ] || { echo "Usage: sh export-control.sh NEW_EXPORT_DIRECTORY" >&2; exit 2; }
[ ! -e "$1" ] || { echo "Export destination must be new" >&2; exit 1; }
base=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
mkdir -p "$1/assets"
cp "$base/assets/button.png" "$1/assets/button.png"
cp "$base/control-group.edc" "$1/control-group.edc"
cat > "$1/control.edc" <<'EDC'
images { image: "button.png" COMP; }
collections {
#include "control-group.edc"
}
EDC
