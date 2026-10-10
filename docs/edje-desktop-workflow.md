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

The reference's `edc/border.edc` includes four alternate border files located at the source root. Staging makes their paths explicitly `../border_*.edc`. This EFL compiler rejects `-I`; inspect its help rather than assuming C compiler flags apply. `edc/time.edc` refers to clock-hand PNGs by basename; existing files reside in `clock/`, so compilation needs `-id clock` in addition to `-id .`. Missing files in unused or commented source are different from selected compiler dependencies.

Matching local source was found under `local-untracked/auzix-stale-outs/out-20260823T175720Z/package-slices/`, in the `desktop-enlightenment-session/source-guidebook/source/e17-0.27.1` and `desktop-efl-session/source-guidebook/source/efl-1.28.1` trees. Those are study references, not runtime dependencies. Preserve their provenance if offloading the old tree.

The 0.27.1 theme settings dialog calls `elm_theme_set`, `elm_config_all_flush`, `elm_config_save`, then the restart action. EFL's `elm_theme_set(NULL, ...)` updates the default config theme; `elm_config_all_flush` also saves config. The standalone trial uses this mechanism and a host watchdog around the two desktop restarts. See [the trial source and procedure](../themes/blackknight/desktop/README.md). Until executed and confirmed, this is a prepared rollback mechanism, not a runtime PASS.

## Current evidence

[Material test](native-skin-test.md) proves the original standalone raster groups compiled and ran. [Active task](task.md) records the full-theme build attempts and local-trial status. [Theme mechanisms](theme-mechanisms.md) records the deeper Sci-Fi/Transient-Color study. Do not conflate these evidence levels.
