# BlackKnight theme/tutorial kit

Original BlackKnight Storm/Still wallpapers, blue-steel native materials and a desktop reskin toolkit. The accepted work is being prepared for its first release; see [v0.1.0 scope and checks](docs/release-v0.1.0.md).

Read [brief](docs/brief.md), [feature map](docs/feature-map.md), [active task](docs/task.md), [shared design/ownership contract](docs/project-contract.md), [branching](docs/branching.md) and [remote toolchain](docs/toolchain.md).

```text
master/ — shared theme foundation
themes/<name>/ — one folder per theme
build/ — toolchain/build preparation
docs/images/ — screenshots and visual evidence
.agents/skills/ — project workflows
```

Work from development into feature/<topic>; merge accepted features back to development. Validated releases merge to main and receive annotated version tags. Source licensing and reused-asset notices must be established before distribution.

First wallpaper pass: [BlackKnight MVP](themes/blackknight/README.md), [still artwork](themes/blackknight/assets/scene.png), and [source study/tutorial notes](docs/wallpaper-mvp.md). Animated EDJs compile through the lab-edge Swarm pipeline; native preview and protected desktop test evidence are in [local setup testing](docs/setup-test.md).

Deep reference study: [Sci-Fi and Transient-Color mechanisms](docs/theme-mechanisms.md), including active state chains, dormant filters and artwork adaptation boundaries.

Second material pass: [forged-blue chrome study](docs/blue-steel-pass.md), with focused/inactive and shelf concepts.

Current implementation slice: [raster artwork and native Edje assembly](master/blue-steel/README.md). Previous SVG chrome overlay is retired.

[Native compile/runtime evidence](docs/native-skin-test.md): lab-edge Swarm build and laptop test app.

[Desktop integration workflow and upstream references](docs/edje-desktop-workflow.md); project skill: [e-desktop-theme](.agents/skills/e-desktop-theme/SKILL.md).

[Final local theme and production wallpaper build](docs/final-build.md), including package paths and checksums.

Source and donor-distribution notices: [NOTICE.md](NOTICE.md).

Original code: **GPLv3**. Original artwork: **CC BY-SA 4.0**.
See [licensing scope and exceptions](LICENSING.md).
