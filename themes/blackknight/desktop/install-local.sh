#!/bin/sh
# Stage candidates only; theme/wallpaper selection is a separate timed trial.
set -eu
artifacts=$1
repo=$(CDPATH= cd -- "$(dirname -- "$0")/../../.." && pwd)
(cd "$artifacts" && sha256sum -c SHA256SUMS)
mkdir -p "$HOME/.elementary/themes" "$HOME/.e/e/backgrounds" "${XDG_CONFIG_HOME:-$HOME/.config}/terminology/colorschemes"
install -m 644 "$artifacts/BlackKnight-BlueSteel.edj" "$HOME/.elementary/themes/BlackKnight-BlueSteel.edj"
install -m 644 "$artifacts/blackknight-animated.edj" "$HOME/.e/e/backgrounds/BlackKnight-Storm.edj"
install -m 644 "$artifacts/blackknight-storm-preview.edj" "$HOME/.e/e/backgrounds/BlackKnight-Storm-Test.edj"
install -m 644 "$artifacts/blackknight-still.edj" "$HOME/.e/e/backgrounds/BlackKnight-Still.edj"
install -m 644 "$repo/master/terminal/BlackKnight Ice.eet" "${XDG_CONFIG_HOME:-$HOME/.config}/terminology/colorschemes/BlackKnight Ice.eet"
printf '%s\n' 'Staged blue-steel/griffin theme, storm/still wallpapers and BlackKnight Ice terminal palette; selections unchanged.'
