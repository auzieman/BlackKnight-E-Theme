#!/bin/sh
# Independent host watchdog; rollback never depends on the preview surviving.
set -eu
helper=$1
theme=$2
log=$3
# Optional existing wallpaper swap: preserve its path/config and restore its bytes.
wallpaper=${4:-}
active_wallpaper=${5:-}
background_armed=0
if [ -n "$wallpaper" ]; then
 [ -n "$active_wallpaper" ] && [ -f "$active_wallpaper" ] && [ -f "$wallpaper" ]
 [ "$wallpaper" != "$active_wallpaper" ]
 cp -p "$active_wallpaper" "$log.background-before.edj"
 sha256sum "$active_wallpaper" > "$log.background-before.sha256"
fi
"$helper" > "$log.before"
# elm_theme_get returns a resolved fallback chain, not the saved setting.
# Decode read-only; Eet -r would REMOVE the config entry.
profile=$(sed -n 's/^PROFILE //p' "$log.before")
case "$profile" in ''|*[!a-zA-Z0-9_-]*) exit 1;; esac
eet -d "$HOME/.elementary/config/$profile/base.cfg" config "$log.config-before"
previous=$(sed -n 's/^ *value "theme" string: "\([^"\\]*\)";$/\1/p' "$log.config-before")
[ -n "$previous" ]
restore() {
 trap - EXIT INT TERM
 if [ "$background_armed" = 1 ]; then
  cp -p "$log.background-before.edj" "$active_wallpaper.bk-restore"
  mv "$active_wallpaper.bk-restore" "$active_wallpaper"
  sha256sum -c "$log.background-before.sha256" >> "$log" 2>&1
 fi
 "$helper" --restore "$previous" >> "$log" 2>&1
 enlightenment_remote -restart >> "$log" 2>&1
 printf '%s\n' 'Desktop restart requested with restored theme' >> "$log"
}
trap restore EXIT INT TERM
if [ -n "$wallpaper" ]; then
 # The host restoration trap is armed before replacing the live wallpaper.
 background_armed=1
 cp "$wallpaper" "$active_wallpaper.bk-trial"
 mv "$active_wallpaper.bk-trial" "$active_wallpaper"
fi
"$helper" "$theme" --previous "$previous" > "$log" 2>&1 &
trial_pid=$!
i=0
while ! grep -q '^TRIAL ' "$log"; do
 if ! kill -0 "$trial_pid" 2>/dev/null; then exit 1; fi
 i=$((i+1)); if [ "$i" -ge 100 ]; then exit 1; fi
 sleep 0.1
done
enlightenment_remote -restart >> "$log" 2>&1
sleep 20
# The watchdog restores independently, even if the native timer process failed.
restore
wait "$trial_pid" || true
