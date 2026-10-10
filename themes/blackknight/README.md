# BlackKnight wallpaper

The accepted base is `assets/scene-v2.png`: the original knight landscape with a distant left castle. The painted composition remains intact.

`wallpaper.edc` builds the native `e/desktop/background` group as a still or animated EDJ. Compile through the existing BKC CLI Swarm pipeline using `desktop/griffin-storm-compiler.sh`.

The animated version adds two raster cloud depths. Faint distant clouds cross the upper sky over 90 seconds. A larger, darker foreground bank covers the moon on a separate approximately 53-second storm cycle: 12 seconds quiet, 18 seconds cover and ambient dimming, a 0.08-second strike, 0.9-second flash decay, then 22 seconds clearing. Lightning brightens the whole scene with a translucent illumination layer. This is stylized lighting, not physical per-object relighting.

Each cloud layer fades to zero before its position resets, allowing the two loops to overlap without a visible jump. `bk,pause` stops both chains and restores the static baseline; `bk,resume` restarts them. The still variant excludes all animated parts. The moving clouds and bolt are original generated PNGs recorded in `assets/provenance.json`.

`wallpaper-preview.c` provides a small native test window: Space pauses/resumes, Escape closes, and a 130-second timer closes automatically. `BK_PREVIEW` accelerates the storm to about 15 seconds and distant clouds to 24 seconds. Compilation, observed rendering, desktop installation and performance acceptance are separate checks; see `../../docs/task.md` for actual evidence.
