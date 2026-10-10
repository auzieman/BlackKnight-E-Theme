#!/bin/sh
# Independent host process restores the byte-exact compositor file after 20s.
set -eu
active=$1
candidate=$2
log=$3
cp -p "$active" "$log.before.cfg"
sha256sum "$active" > "$log.before.sha256"
restore() {
 trap - EXIT INT TERM
 cp -p "$log.before.cfg" "$active.bk-restore"
 mv "$active.bk-restore" "$active"
 enlightenment_remote -restart >> "$log" 2>&1
 sha256sum -c "$log.before.sha256" >> "$log" 2>&1
 printf '%s\n' RESTORED >> "$log"
}
trap restore EXIT INT TERM
cp "$candidate" "$active.bk-trial"
mv "$active.bk-trial" "$active"
printf '%s\n' 'TRIAL restrained visibility effects; rollback 20 seconds' > "$log"
enlightenment_remote -restart >> "$log" 2>&1
sleep 20
restore
