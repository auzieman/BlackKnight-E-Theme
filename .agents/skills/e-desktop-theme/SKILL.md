---
name: e-desktop-theme
description: Adapt and test Enlightenment desktop themes and Edje wallpapers using real EDC parts, raster materials, existing theme contracts, remote compilation, and timed local trials.
---
Read the project's AGENTS.md and active task. Use [e-visual-layout](../e-visual-layout/SKILL.md) for artwork/layout decisions; this skill owns desktop integration and its render trial, not media playback or provider logic.

Consult [the official references and local integration notes](../../../docs/edje-desktop-workflow.md) for the selected mechanism. Verify APIs against the installed version's headers/source. Separate documentation capability, source implementation, successful compilation, and observed rendering.

Trace the actual group, visible part, clipping, image border, state colors, signals and program targets before choosing an artwork binding. A named titlebar can be completely transparent. Preserve swallowed parts, hit areas, window actions and alternate styles unless the requested slice deliberately changes them. Keep approved raster detail; assemble it with EDC rather than replacing it with flat vector approximations.

For a selected group override, consider the documented Elementary theme search chain with the working installed theme as fallback. A standalone material demo is not a desktop border group; an actual border override plus the base chain is a valid scoped desktop trial. Avoid expanding a titlebar task into unrelated legacy widget/shelf repairs.

Stage adaptations outside the reference tree. Resolve includes relative to their containing EDC; image/font search paths are separate compiler inputs. Check the selected compiler's supported flags. Inspect failures for source/asset errors before increasing resources. Do not invent replacement assets or remove live groups just to make compilation pass.

Use the project's existing BKC CLI/core pipeline for lab compilation. Record immutable source, payload hash, signed matching packages, constrained Swarm job and returned artifact hashes. Compilation alone does not authorize application or prove desktop compatibility.

For an authorized desktop trial, capture the current theme and back up relevant settings. Honour the requested trial duration (currently about 20 seconds). Arm an independent host rollback before changing the theme; restore the captured original even if the preview exits. Verify whether the installed desktop needs a restart. Do not apply until the helper, original identity and rollback path are ready. A settings backup by itself is not automatic rollback.

Use the user's sample windows and a controlled native test window; leave their applications open. Record trial/restored logs and screenshots in docs/images. Confirm the original theme after rollback. Keep shelf/menu, wallpaper animation and permanent installation as separate requested/accepted slices when outside the current objective.

Improve these instructions from demonstrated failures and verified examples; keep detailed theme-specific evidence in the linked document rather than accumulating universal restrictions here.
