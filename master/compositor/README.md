# Restrained compositor demo pass

The inspected E27.1 setup already enables VSync, smooth windows and fades. The donor theme supplies default focus glow and visibility effects. Its rotate/flip frame styles rotate unfocused content through 180 degrees, so this pass avoids them.

`prepare.py INPUT_DECODE OUTPUT_DECODE` adds `visibility/vertical` to existing application popup-menu override rules (types 9 and 10), then appends a non-borderless, non-fullscreen ordinary-window rule after the existing fullscreen rule. The E27.1 compositor loads effect groups as `e/comp/effects/<effect>` and the donor contains `e/comp/effects/visibility/vertical`. Existing renderer and global settings remain unchanged. This targets show/hide/minimize/restore; it does not add a Super+Tab animation or change internal Enlightenment menu rules.

The candidate is encoded into a copy of the existing Eet archive, then decoded to verify the three new fields. `trial.sh ACTIVE_CFG CANDIDATE_CFG LOG` backs up the active file, arms a host trap before replacement, restarts E, and restores the original bytes after 20 seconds. The candidate survived the trial restart; restoration passed the original SHA256 after the second restart. Artifacts/logs remain in `build/out/compositor-*`.

Visual effect acceptance is pending user review. No permanent application was performed. Leave the user's windows open during trials and retain the rollback preference.

`focus-opacity.py` is a separate temporary X11 preview: it caps inactive ordinary windows at 92% for 20 seconds, preserves original opacity for the active window and excludes dialogs/menus/fullscreen. It restores original properties on completion or SIGINT/SIGTERM; it is not a persistent service. First runtime completed restoration for 12 windows. Visual acceptance/performance remain pending user review.
