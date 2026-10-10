# Sci-Fi and Transient-Color: mechanism study

BK-005, 2026-10-10. This is a source inspection, not an E27 compatibility or performance result. No upstream artwork, compiled theme or desktop setting was changed.

## Evidence and reproducibility

- Enlightenment-Themes checkout: `1d9c308ae3a028b8951ba0fb137ee1a6498e6b2d`, branch `Archived/transient-color-old`.
- Current Transient-Color source inspected through Git: `origin/Transient-Color`, revision `04b14c8cb922d43c835e3bb11dbfcdb0451ff3ee`. Use `git show <revision>:<path>` rather than assuming the archived checkout is current.
- Installed reference: `/home/auzieman/.e/e/themes/E20-Scifi-theme.edj`; SHA-256 `99536074e913dedc79d9fc88e59cc4263fe8c87d1fd08e742aef85c119f89e7e`.
- Animated-background reference: `E23-scifi-good-FULL-anim.edj`, repository revision `f6ea447ad74c719b1d2ac3dee942e477b8384143`; SHA-256 `56ff64ce21d1fe80e99bf765cab916ce60541a8a6393534800b4e7866ba43a6b`.

The Sci-Fi EDJs contain compressed embedded source. A bounded Python zlib scan recovered source text at byte offsets 21786560 (E20, 2,480,916 decompressed bytes) and 14745480 (E23, 18,178 bytes). Inspection files are `/tmp/bk-theme-study/E20-Scifi-theme-21786560.txt` and `E23-scifi-good-FULL-anim-14745480.txt`. They include EET serialization metadata and NUL separators: they are searchable evidence, not clean compiler inputs. This was not an `edje_decc` extraction or a successful rebuild. Temporary paths may disappear; original EDJ hashes identify the evidence.

## Sci-Fi window chrome

The recovered E20 group `e/widgets/border/default/border` begins around inspection line 47336. It uses separate title, shadows, text, buttons and glints. The depth comes from coordinating these parts with focus and pointer events.

| Mechanism | Source evidence | BlackKnight adaptation |
| --- | --- | --- |
| Staged focus lighting | Around line 49126, `go_active_pre` responds to `e,state,focused`, resets parts, then chains icon activation, title activation over 2 seconds, and shadow activation over 0.5 seconds. | Preserve the sequence; make the underlying metal colder and highlights ice blue. |
| Layered glints | Around line 48268, `title_glint_clip` clips image overlays to the titlebar. `title_glint_1/2/3` use `wrk/e17_titlebar_glint1/2/3.png`; an active tint is `(0,111,222,255)`. Focus chains trigger glint state changes. | Retain separate transparent highlight assets rather than baking every highlight into one plate. |
| State versus execution | `active2` descriptions exist, but the inspected active chain does not prove they execute. A `go_active4` section is commented; `go_active4b` and `go_active5b` are chained together. | Trace each state target before claiming a travelling sweep. Inspect overlapping programs on target before changing timing. |
| Unfocus | `go_passive_pre` responds to `e,state,unfocused`; subsequent programs reset shadows, icons and title in stages. | Keep inactive readable and visually quieter. Test rapid focus changes; source inspection does not establish cancellation correctness. |
| Hover/pressed controls | Around line 49250, close-button hover enters a short state transition and a self-chained program; mouse-out sets another state. Mouse-down emits `e,action,close`. Maximize/minimize have related programs. | Preserve action signals and hit areas. Verify that hover loops stop when leaving or hiding the window; the inspected excerpt does not show an explicit stop. |
| Shelf geometry | `e/shelf/default/base` uses shaped metadata, `shelf_bar.png` with `image.border: 100 100 0 0`, orientation descriptions and a vertical image variant. | Preserve scalable edges, fill/origin settings and orientation variants. Do not stretch one horizontal metal texture into every shelf orientation. |

The bundled source also contains Embryo message handlers, timers/cancellation, custom states, dragging and mapped clock hands. Those demonstrate the wider theme's capabilities, but are not evidence that the titlebar uses all of them.

## Sci-Fi animated background

The E20 `e/desktop/background` group (around line 38777) and the smaller E23 embedded source expose actual animation plumbing:

- Three image layers enable `map.on` and rotate around the Z axis, with alternating directions. A `LINEAR 30` transition chains through reset back to rotation. These are native mapped parts, not a video player.
- Two image sequences declare frames `wrk/d/0.png` through `85.png` and `wrk/g/0.png` through `85.png`. Image tweening supplies more complex artwork changes than position/opacity alone.
- The E23 source contains logo pointer interaction and chained `anim-d` / `anim-g` transitions over 12 seconds.

Frame names do not identify their visual content. The recovered text does not establish which pixels depict clouds or lightning; extracting and previewing those images remains necessary before making that claim. Rotation and tween mechanisms are verified in source, but their appearance, runtime cost and E27 behaviour are not.

For BlackKnight, the current quiet → cloud cover → strike → fade → clear sequence remains a separate original implementation. Study mapped layers for modest cloud/fog depth; do not automatically import continuous rotating layers or 172 frame declarations into a laptop wallpaper. Textures, frame dimensions and continuously active programs all need a measured budget.

## Transient-Color: current versus archived

Inspect `enlightenment-elementary/edc/border.edc` at the current revision. The group `e/widgets/border/volume` (roughly lines 115–218) is a particularly good compact interaction example:

1. A `SWALLOW` holds the volume control; a RECT clip hides or reveals it.
2. `mouse,in` stops both hide programs, expands the event region, then changes the clip with `SIN 0.25`.
3. `mouse,out` stops both show programs, hides the clip with the same easing, then contracts the event region.

This combines presentation, hit-area management and cancellation. Preserve that discipline for retracting controls: geometry and event coverage need to follow the animation together.

The default border has shaped metadata, title/button active states, resize/titlebar event areas, and an `e,version,22` script setting pointer modes. These are behavioural contracts, not decorative pixels. Artwork substitutions must retain named parts, swallowed content, emitted action signals, pointer modes and resize coverage.

Both branches contain snapshot/filter-related material, but **current `enlightenment-elementary/filters.edc` wraps its filter definitions in a block comment**, explicitly saying the theme does not use filters. Archived definitions also rename the high-performance blur to disable it and warn about performance. A SNAPSHOT/filter reference is not proof of functioning live blur. Do not enable blur merely because the declaration looks useful; compiler and runtime evidence must settle compatibility and cost first.

## Artwork pass boundary

The next visual slice should retain Sci-Fi's existing geometry and programs while changing a small, representative border/shelf asset set:

- Forged blue steel with dark cut edges, layered bevels and controlled texture, closer to the wallpaper armour than the flat SVG study.
- Separate ice-blue glints and emissive seams, triggered by focus/hover, with quieter inactive states.
- Preserve alpha, image borders, content padding, clipping, sizing, orientation and pointer/action contracts.
- Preview focused, unfocused, hovered and pressed states at compact and wide window sizes before expanding to menus and toolbars.

The SVG palette preview is a colour study only; it does not represent the existing theme's material depth or animation. No final base-theme selection or asset replacement is made by this report.

Before shipping an adapted EDJ: identify upstream author/license and per-asset provenance; obtain proper editable extraction, compile through the approved remote toolchain, and test on the actual E version. Check rapid hover/focus reversal, resize, shelf orientation, hidden/minimized behaviour, idle activity and still/low-motion alternatives. These are pending acceptance checks, not reasons to redesign the whole theme.

## Additional wallpaper references named by the user

The installed wallpaper folder `/home/auzieman/.e/e/backgrounds` contains `E23-scifi-good-FULL-anim.edj`, `background-oh-V1.edj`, `background-oh-V1 (1).edj` and `blackhole-pclos-bt2.edj`. The last is a candidate for the user's “Black” reference; that identity is not established. These are wallpaper packages separate from the installed theme folder. Sci-Fi also embeds an `e/desktop/background` group in its full theme, as described above.

Oh-v1 has directly editable source at `Animated-background/background-oh-V1/background.edc` in the studied repository revision. Its `e/desktop/background` group layers `bg.png`, `cloud2.png` and `cloud1.png`. The cloud parts disable mouse events. Each cloud's `drift` state shifts its image fill origin by one declared texture width: 1.47083 for cloud2 and 1.86667 for cloud1. `show` starts LINEAR transitions lasting 65 and 55 seconds respectively; each `after` chain resets to default and starts again. Different speeds provide layered motion without a frame sequence.

A texture-origin reset by exactly one tile width is a useful seamless-loop technique, but the texture edges must actually tile. No rendered seam or performance test has been performed here. The source also declares `nappe-cloud.png` and `stars.png` (stars twice); those files are absent from the source folder, and the inspected parts do not use them. Treat this as a source cleanup/build-input issue rather than assuming the source will compile unchanged. Blackhole package animation and the installed Oh-v1 variants' correspondence to this source remain unverified.

## Actual branch checkout inspection — BK-009

Switched the existing Simotek checkout through current Transient-Color (`04b14c8cb922d43c835e3bb11dbfcdb0451ff3ee`), Fireball2 (`2d7f06ad81b26d7eb80d4db17f7ac49c9904a312`) and Ice (`707e6fa2a0e13f73b2319b4537c1429eaef5a8ec`). Left it on local study/transient-color, tracking origin/Transient-Color. Existing untracked helper scripts/artifacts were preserved; their visibility varies with branch ignore rules.

Transient-Color: visually inspected img-manual/border_full.png and e_surface.png, both small transparent contour layers, and img/glow_round_corners_small.png, a separate blue segmented spinner. border.edc uses border_full with 8-pixel image borders and a maximized variant. The busy indicator maps and rotates its separate glow layer around the knob. The EDC part roles are essential context for interpreting these small PNGs.

Fireball2: visually inspected img-manual/shelf_background_top.png, a dimensional rounded dark plate; orientation-specific shelf images also exist. edc/background.edc references e_fireball_wallpaper.png and e_fireball_wallpaper1.png, with SINUSOIDAL 0.5 transitions. Full signal-chain and frame-content inspection remains pending.

Ice: border.edc references vgrad_med_lighter.png, vgrad_med_dark_color.png, bevel_out.png with 1-pixel image borders, and separate light/dark normal/selected button symbols. These source bindings show a different assembly from the whole-border approach; Ice pixels were not visually inspected in this pass.

The Simotek build-darkmod.sh uses ImageMagick modulation/brightness/alpha operations and compiles with manual, colour-converted and unchanged image search directories. Therefore raw source PNG colours may differ from build inputs. Inspect colours.conf, selected manual image directory and generated assets before presenting a branch's final palette. The build script was read, not executed.

Lesson for BlackKnight: start from approved raster material and measure its actual EDC placement/stretch regions. Inspect base, overlay, converted build input and composed render separately. The previous SVG-derived replacement set remains an unaccepted experiment and should not be treated as the approved forged-metal implementation.
