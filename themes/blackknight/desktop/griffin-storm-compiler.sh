#!/bin/sh
set -eu
trap 'code=$?; printf "%s\n" "$code" > /outputs/exit-code' EXIT
cp /work/package-key.rsa.pub /etc/apk/keys/-6aaf02a2.rsa.pub
printf '%s\n' 'https://auzix.auzietek.com/alpine/repo/v3.24' >> /etc/apk/repositories
apk add --no-cache build-base pkgconf efl=1.28.1-r2 efl-dev=1.28.1-r2
apk info -v > /outputs/packages.txt
mkdir -p /outputs/result
cc -std=gnu99 -Wall -Wextra $(pkg-config --cflags ecore-evas edje eet) /work/remap-images.c -o /outputs/result/remap-images $(pkg-config --libs ecore-evas edje eet)
cc -std=gnu99 -Wall -Wextra $(pkg-config --cflags elementary) /work/theme-trial.c -o /outputs/result/theme-trial $(pkg-config --libs elementary)
cp /work/donor.edj /outputs/result/BlackKnight-BlueSteel.edj
/outputs/result/remap-images /work/donor.edj /outputs/result/BlackKnight-BlueSteel.edj /work/assets > /outputs/result/remap-verification.txt
cp /work/source-revision.txt /outputs/result/
cd /outputs/result
sha256sum BlackKnight-BlueSteel.edj remap-images theme-trial > SHA256SUMS

edje_cc -id /work/wallpaper/assets /work/wallpaper/wallpaper.edc /outputs/result/blackknight-still.edj
edje_cc -DANIMATED=1 -id /work/wallpaper/assets /work/wallpaper/wallpaper.edc /outputs/result/blackknight-animated.edj
edje_cc -DANIMATED=1 -DBK_PREVIEW=1 -id /work/wallpaper/assets /work/wallpaper/wallpaper.edc /outputs/result/blackknight-storm-preview.edj
cc -std=gnu99 -Wall -Wextra $(pkg-config --cflags elementary) /work/wallpaper/wallpaper-preview.c -o /outputs/result/wallpaper-preview $(pkg-config --libs elementary)
cd /outputs/result
sha256sum blackknight-still.edj blackknight-animated.edj blackknight-storm-preview.edj wallpaper-preview >> SHA256SUMS
