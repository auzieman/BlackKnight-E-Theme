# BlackKnight local test setup

The lab-edge BKC/Swarm build installed these candidates on the laptop:

- Theme: `~/.elementary/themes/BlackKnight-BlueSteel.edj` — accepted frame/shelf artwork plus the AuzieTek griffin start emblem.
- Wallpaper: `~/.e/e/backgrounds/BlackKnight-Storm.edj` — slow production parallax and storm loop.
- Wallpaper: `~/.e/e/backgrounds/BlackKnight-Storm-Test.edj` — accelerated test loop.
- Wallpaper: `~/.e/e/backgrounds/BlackKnight-Still.edj` — still alternative.
- Terminology color scheme: `~/.config/terminology/colorschemes/BlackKnight Ice.eet` — candidate palette; current selection unchanged.

`themes/blackknight/desktop/install-local.sh ARTIFACT_DIRECTORY` stages the candidates after verifying build hashes. `desktop/trial.sh HELPER THEME LOG [TEST_WALLPAPER ACTIVE_WALLPAPER]` performs the 20-second theme trial. If wallpaper arguments are supplied, it backs up the active wallpaper, arms a host restoration trap, atomically swaps its bytes without editing desktop configuration, then restores and verifies the original file. Do not pass an unrelated active file; identify the saved desktop background first. The production wallpaper is a selectable candidate, not permanently activated by this test.

Build run: `0d0e6c0f-7d8b-4a55-9767-6d2b681a8343`; payload SHA256 `347667d6eb82e991472ce6abb16929be9e76211eb5e2a2a06dc2b9acce21b519`. All seven returned artifact checksums passed. Native remap verification reports 64 changed image entries and 4,595 unchanged archive entries. Donor layout/program entries remain untouched.

The native parallax preview logged cover, strike, reset and a second strike before the user closed it. [Native wallpaper view](images/parallax-v5-native.png). Pause/resume and idle resource measurements remain unverified for this revision. No performance acceptance is implied.

The combined desktop trial rendered the griffin on the [blue-steel shelf](images/griffin-shelf-v5-trial.png). Both native timer and independent host watchdog restored `E20-Scifi-theme`; the saved original wallpaper hash passed after restoration. Full logs and EDJs are under `build/out/parallax-v5/`. This is local testing, with no release/tag or remote publication.
