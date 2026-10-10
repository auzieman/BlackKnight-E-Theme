# BlackKnight theme/tutorial kit

Independent theme/tutorial project with original wallpaper artwork, a compiled native raster-material test, and a full desktop adaptation under validation. No release has been tagged.

Read [brief](docs/brief.md), [feature map](docs/feature-map.md), [active task](docs/task.md), [shared design/ownership contract](docs/project-contract.md), [branching](docs/branching.md) and [remote toolchain](docs/toolchain.md).

```text
master/ — shared theme foundation
themes/<name>/ — one folder per theme
build/ — toolchain/build preparation
docs/images/ — screenshots and visual evidence
.agents/skills/ — project workflows
```

Work from development into feature/<topic>; merge accepted features back to development. Validated releases merge to main and receive annotated version tags. Source licensing and reused-asset notices must be established before distribution.

First wallpaper pass: [BlackKnight MVP](themes/blackknight/README.md), [still artwork](themes/blackknight/assets/scene.png), and [source study/tutorial notes](docs/wallpaper-mvp.md). Animated EDJ compilation/runtime validation remains pending.

Deep reference study: [Sci-Fi and Transient-Color mechanisms](docs/theme-mechanisms.md), including active state chains, dormant filters and artwork adaptation boundaries.

Second material pass: [forged-blue chrome study](docs/blue-steel-pass.md), with focused/inactive and shelf concepts.

Current implementation slice: [raster artwork and native Edje assembly](master/blue-steel/README.md). Previous SVG chrome overlay is retired.

[Native compile/runtime evidence](docs/native-skin-test.md): lab-edge Swarm build and laptop test app.

[Desktop integration workflow and upstream references](docs/edje-desktop-workflow.md); project skill: [e-desktop-theme](.agents/skills/e-desktop-theme/SKILL.md).
