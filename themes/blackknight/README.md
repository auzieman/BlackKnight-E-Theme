# BlackKnight wallpaper MVP
Selected base: assets/scene-v2.png, original knight landscape with distant left castle. scene.png remains the first candidate.
wallpaper.edc builds e/desktop/background as still or animated EDJ. Run sh build.sh through BKC's remote build path with verified EFL/edje_cc and SVG-loader support.
BK-003 cycle: 12 seconds quiet -> 18 seconds clouds cover moon/dim scene -> 0.08 second large branching strike/glow -> 0.9 second fade -> 22 seconds clouds clear -> invisible cloud-position reset. Approximately 53 seconds per cycle. All animated parts return to baseline; actual seam/render behaviour awaits E validation.
The glow is an MVP translucent illumination overlay, not physical per-object relighting. Existing painted clouds remain part of the base image; the moving cloud-shadow layer obscures them. True layered parallax is later work.
Still variant contains no animation parts/programs. Slow transitions may still redraw at display rate; laptop CPU/memory and hidden-desktop pause must be measured. bk,pause resets overlays; bk,resume restarts after the quiet interval. Host signal integration is not proved.
No EDJs compiled, desktop applied or performance acceptance claimed. Native 16:9 layout; other aspect-ratio policy pending.

Blue-metal-palette.json and ../../docs/images/blue-metal-preview.svg propose a bluer static metal treatment. Existing Transient-Color artwork is the candidate base, not yet altered. Preserve dimensions/stretch regions and source notices during adaptation.
