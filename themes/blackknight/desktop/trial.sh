#!/bin/sh
# Independent host watchdog; rollback never depends on the preview surviving.
set -eu
helper=$1
theme=$2
log=$3
"$helper" > "$log.before"
previous=$(sed -n 's/^THEME //p' "$log.before")
[ -n "$previous" ]
restore() {
 trap - EXIT INT TERM
 "$helper" --restore "$previous" >> "$log" 2>&1
 enlightenment_remote -restart >> "$log" 2>&1
 printf '%s\n' 'Desktop restart requested with restored theme' >> "$log"
}
trap restore EXIT INT TERM
"$helper" "$theme" > "$log" 2>&1 &
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
