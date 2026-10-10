# Basic BlackKnight desktop trial

This private local adaptation compiles the full editable Sci-Fi source with the approved forged-blue raster plate bound to the visible default titlebar. Window geometry, existing buttons, focus effects and alternative border styles remain inherited. Shelf/menu artwork and wallpaper animation are follow-up slices.

Stage into a **new** output directory:

```sh
python3 stage.py /path/to/E20-Scifi-theme /path/to/new-staging-directory
```

The BKC lab-edge compiler payload contains that staged directory as `desktop/`, `compiler.sh`, `theme-trial.c`, the verified public package key, and `source-revision.txt`. Builds use the existing `e-skin-swarm-build` pipeline. Upstream licensing must be established before redistribution; upstream files are not vendored here.

The native helper prints the current profile/theme when invoked without arguments. `theme-trial THEME_EDJ` validates the desktop border group, arms a 20-second timer **before** changing the theme, broadcasts the candidate, and restores the captured theme. `--restore THEME` is a separate restore operation for the independent watchdog.

Run `trial.sh HELPER THEME_EDJ LOG` on the host through `nohup`. It records the original theme, restarts Enlightenment into the trial, then independently restores the original and restarts back after 20 seconds. The helper and watchdog are separate processes. Applications remain running across the desktop restarts. Back up both Enlightenment and Elementary settings first. Do not turn this trial into a permanent application without user authorization.

This is a render trial, not proof of complete desktop compatibility or animation performance. Retain before/trial/restored screenshots and the log with the artifact hashes.
