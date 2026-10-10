#!/bin/sh
# Independent host watchdog; rollback never depends on the preview surviving.
set -eu
helper=$1
theme=$2
log=$3
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
 "$helper" --restore "$previous" >> "$log" 2>&1
 enlightenment_remote -restart >> "$log" 2>&1
 printf '%s\n' 'Desktop restart requested with restored theme' >> "$log"
}
trap restore EXIT INT TERM
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
