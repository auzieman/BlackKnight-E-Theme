# Edje desktop integration references

Use upstream documentation for mechanisms, matching local headers/source for exact installed APIs, and render evidence for acceptance. The laptop currently runs Enlightenment 0.27.1 with EFL 1.28.1-r2; re-check these versions when the target changes.

## Official documentation

- [Enlightenment documentation entry point](https://www.enlightenment.org/docs/start)
- [Getting started with themes and Edje](https://www.enlightenment.org/docs/themes/start): desktop and application theme foundations.
- [Edje programming guide](https://www.enlightenment.org/develop/legacy/program_guide/edje_pg): positioning, scaling, swallowed content and layout signals.
- [EDC language reference](https://www.enlightenment.org/_legacy_embed/edcref.html): precise syntax; check availability against the selected compiler.
- [Edje blocks](https://www.enlightenment.org/develop/legacy/program_guide/edje/edje_blocks): image declarations, compiler image directories and scaled borders.
- [Part blocks](https://www.enlightenment.org/develop/legacy/program_guide/edje/part_block): relative geometry, descriptions, image borders, tweens and clipping.
- [Programs](https://www.enlightenment.org/develop/legacy/program_guide/edje/program): signals, sources, transitions and program chains.
- [Elementary themes](https://www.enlightenment.org/_legacy_embed/group__Elm__Theme.html): application theme composition; desktop application still requires its own integration contract.

## Verified source lessons from BK-013

Sci-Fi's default border `title_bar` is alpha zero in both descriptions. The visible center strip is `top_titlebar`. The adaptation drives its added active description from the existing focus programs; the existing control and glint contracts remain inherited. This first slice does not replace all frame caps or shelf/menu textures.

The user confirms that the running Sci-Fi EDJ was built from the reference source. The original `build.sh` runs `edje_cc $@ -id . -fd . default.edc -o E20-Scifi-theme.edj` from the source root. Reproduce that baseline with its actual toolchain and any supplied arguments before changing includes, search paths or entrypoints. The earlier staged builds changed these inputs without first reproducing the original build; their failures do not establish a defect in the user's source.

Earlier attempts found include, image-path and state errors in altered build inputs. Those remain diagnostic history in the active task, not an approved set of source repairs. Check preprocessed/selected source and asset lookup before patching anything.

Matching local source was found under `local-untracked/auzix-stale-outs/out-20260823T175720Z/package-slices/`, in the `desktop-enlightenment-session/source-guidebook/source/e17-0.27.1` and `desktop-efl-session/source-guidebook/source/efl-1.28.1` trees. Those are study references, not runtime dependencies. Preserve their provenance if offloading the old tree.

The 0.27.1 theme settings dialog calls `elm_theme_set`, `elm_config_all_flush`, `elm_config_save`, then the restart action. EFL's `elm_theme_set(NULL, ...)` updates the default config theme; `elm_config_all_flush` also saves config. The standalone trial uses this mechanism and a host watchdog around the two desktop restarts. See [the trial source and procedure](../themes/blackknight/desktop/README.md). Until executed and confirmed, this is a prepared rollback mechanism, not a runtime PASS. For serialized settings inspection, Eet -d decodes and -x extracts; -r removes an entry. Prefer the native theme APIs for application.

## Current evidence

[Material test](native-skin-test.md) proves the original standalone raster groups compiled and ran. [Active task](task.md) records the full-theme build attempts and local-trial status. [Theme mechanisms](theme-mechanisms.md) records the deeper Sci-Fi/Transient-Color study. Do not conflate these evidence levels.

The basic trial now uses an Edje desktop-border override followed by the captured installed theme in Elementary’s colon-separated search order. An altered full-tree build encountered shelf state errors; an unchanged baseline has not yet been reproduced. Earlier whole-tree compatibility patches are unaccepted study history; they are removed from the active border staging script. Use the installed working theme for all unselected groups.

## Donor verification and image-only pass

The installed Sci-Fi EDJ was extracted into ignored build storage. All 139 EDC files match the donor byte-for-byte, confirming the user's stated source provenance. The unchanged build on current EFL 1.28.1 reports an include lookup mismatch for border_shaped.edc. This is build-path evidence, not grounds to repair states or restructure the theme. The active staging script now leaves all EDC identical and accepts only selected, dimension-matched frame images. See [source proof](../themes/blackknight/desktop/donor-source-proof.json) and [slot mapping](blue-steel-pass.md).
