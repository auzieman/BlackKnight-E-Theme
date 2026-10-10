# Basic BlackKnight desktop trial

This private adaptation remaps selected Sci-Fi frame PNGs with geometry-matched blue-steel artwork. The donor EDC, layout, controls, states and animations remain byte-identical. The full donor is built with its original `build.sh` and `default.edc`; the earlier reduced entrypoint and compatibility patches are retired.

## Image-only working-EDJ pass

For the current trial, `remap-images.c` patches a copy of the known-working EDJ, using the existing image IDs. It writes only the selected `edje/images/*` payloads with lossless encoding, then verifies all other decoded archive entries are byte-identical to the donor. No Edje Edit save/regeneration or EDC compilation is used for this path. The donor remains untouched. `remap-compiler.sh` builds the native tools and performs the verified remap through the existing BKC Swarm job.

`slice-frame.sh DONOR_SOURCE MATERIAL_DIR OUTPUT_DIR` creates the measured replacements from the approved plate/button PNGs. The donor's alpha is retained exactly; original glyphs, shadows and glints remain. Source coordinates and transforms are recorded in this script, with checksums in `assets/frame-v1-provenance.json`. See [the comparison preview](../../../docs/images/frame-remap-v1-comparison.png).

The source-build path below remains available for later toolchain investigation; it is not required for the image-only EDJ trial.

Stage an unchanged baseline into a **new** output directory:

```sh
python3 stage.py /path/to/E20-Scifi-theme /path/to/new-staging-directory
```

After its original build is reproduced, supply prepared replacement PNGs using the same filenames and dimensions as the donor's `wrk/` slots:

```sh
python3 stage.py /path/to/E20-Scifi-theme /path/to/new-reskin-directory --assets /path/to/frame-replacements
```

The script validates the selected slot names and image dimensions before copying. It verifies all donor EDC hashes afterward and records the image mapping in `blackknight-source.json`. The existing large plate/button PNGs are material sources; they are not geometry-matched replacements yet. See [the measured comparison](../../../docs/blue-steel-pass.md).

The BKC lab-edge compiler payload contains that staged directory as `desktop/`, `compiler.sh`, `theme-trial.c`, the verified public package key, and `source-revision.txt`. Builds use the existing `e-skin-swarm-build` pipeline. Upstream licensing must be established before redistribution; upstream files are not vendored here.

The watchdog reads the exact saved theme from the Eet configuration with read-only decoding and passes it to both restoration paths. The resolved Elementary fallback list is not the saved value.

The native helper prints the current profile/theme when invoked without arguments. `theme-trial THEME_EDJ` validates the desktop border group, arms a 20-second timer **before** changing the theme, broadcasts the candidate followed by the original theme as fallback, and restores the captured theme. `--restore THEME` is a separate restore operation for the independent watchdog.

Run `trial.sh HELPER THEME_EDJ LOG` on the host through `nohup`. It records the original theme, restarts Enlightenment into the trial, then independently restores the original and restarts back after 20 seconds. The helper and watchdog are separate processes. Applications remain running across the desktop restarts. Back up both Enlightenment and Elementary settings first. Do not turn this trial into a permanent application without user authorization.

This is a render trial, not proof of complete desktop compatibility or animation performance. Retain before/trial/restored screenshots and the log with the artifact hashes.
