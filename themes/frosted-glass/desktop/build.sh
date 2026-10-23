#!/bin/sh
# Invoked by BKC inside the pinned native compiler container.
# /work/themes/{Frosty,Minty} comes from prepare.py; no host installation.
set -eu
mkdir -p /work/build/out /usr/share/fonts/frost-preview
# Test fixture fonts are not embedded into the resulting theme.
cp /work/fonts/*.ttf /usr/share/fonts/frost-preview/
cc -Wall -Wextra /work/render.c -o /work/build/out/render $(pkg-config --cflags --libs ecore-evas edje)
for name in Frosty Minty; do
    cd /work/themes/$name
    edje_cc -id . -fd . source.edc /work/build/out/$name.edj > /work/build/out/$name.log 2>&1
    timeout 30 /work/build/out/render /work/build/out/$name.edj /work/build/out/$name.png > /work/build/out/$name-render.log 2>&1
    cp frost-source.json /work/build/out/$name-source.json
done
cd /work/build/out
sha256sum *.edj *.png render > SHA256SUMS
