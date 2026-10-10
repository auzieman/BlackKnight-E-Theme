# Forged-blue raster material / native Edje demonstration

BK-010 supersedes the SVG-derived chrome experiment. The material is actual generated PNG artwork: textured plate with corner hardware, blank control tile and separate emitted-light sprite. Live titles and symbols are EDC TEXT parts; transparent event rectangles own input. No new desktop theme has been installed.

`material.edc` exposes `bk/material/titlebar` and `bk/material/control`. It uses lossless raster images, image borders and `border_scale_by` for supersampled corners. The plate's generated bottom padding is accommodated by an extended image part clipped to the titlebar. Those measurements need target render proof; source inspection cannot guarantee a clean seam or final compact proportions.

Build remotely through the BKC route: `sh build.sh /outputs/new-material-run`. An approved EFL compiler is required. On the graphical test host, build preview.c with `cc preview.c $(pkg-config --cflags --libs elementary) -o preview` and run `./preview /outputs/new-material-run/blackknight-material.edj`. The preview logs requested actions rather than controlling playback or a desktop window. Neither source has been compiled yet.

## Presentation contract

| Host input | Source | Effect |
| --- | --- | --- |
| bk,state,active | host | Brighter plate/title and one glint sweep |
| bk,state,inactive | host | Cancel sweep and restore quieter plate/title |
| bk,state,hidden | host | Cancel/reset glint |
| bk,control,disabled / enabled | close, maximize, minimize, or activate | Disable/enable the named event area and material state |

Outputs: `bk,action,close`, `bk,action,maximize`, `bk,action,minimize` from titlebar controls; `bk,action,activate` from generic control. Sources identify the control. Hosts must map these requests to desktop or player operations and enforce disabled state for keyboard invocation too.

Set `title` through edje_object_part_text_set. Generic control label is `label.activate`; E-Jamz can set play/pause/stop glyphs without baking text into textures. The layout owns visible hover/pressed/disabled feedback, while the player owns playback state. No timers or perpetual animation chains: focus fires one 0.75-second sweep with 0.15-second fade, and button state changes are immediate to avoid conflicting transition chains.

## Pending acceptance

Compile EDC and C on the approved toolchain. Render at 480/800/1200 widths and actual UI scale. Verify transparent padding, corner scaling, title ellipsis, button text readability, rapid focus reversal, hover/press/release and disable/re-enable. Minimize must cancel optional effects. Measure idle/redraw cost separately from playback. The material sheet approval does not validate these generated assets or their assembly.

Mechanism reference: https://www.enlightenment.org/develop/legacy/program_guide/edje/part_block (image borders, scaling, image fill and live text). This demonstration is independent original EDC; adapting it into Sci-Fi's production border groups remains a later step with the existing desktop signal/hit-area contract intact.
