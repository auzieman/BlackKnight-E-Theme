#!/bin/sh
set -eu
trap 'code=$?; printf "%s\n" "$code" > /outputs/exit-code' EXIT
cp /work/package-key.rsa.pub /etc/apk/keys/-6aaf02a2.rsa.pub
printf '%s\n' 'https://auzix.auzietek.com/alpine/repo/v3.24' >> /etc/apk/repositories
apk add --no-cache build-base pkgconf efl=1.28.1-r2 efl-dev=1.28.1-r2
apk info -v > /outputs/packages.txt
mkdir -p /outputs/result /tmp/desktop
cp -a /work/desktop/. /tmp/desktop/
cd /tmp/desktop
# Retain the donor's original entrypoint, layout and build recipe.
sh ./build.sh
cp E20-Scifi-theme.edj /outputs/result/BlackKnight-BlueSteel.edj
cp blackknight-source.json /outputs/result/
cp /work/source-revision.txt /outputs/result/
cd /outputs/result
sha256sum BlackKnight-BlueSteel.edj > SHA256SUMS

cc -std=gnu99 -Wall -Wextra $(pkg-config --cflags elementary) /work/theme-trial.c -o /outputs/result/theme-trial $(pkg-config --libs elementary)
cd /outputs/result
sha256sum theme-trial >> SHA256SUMS
