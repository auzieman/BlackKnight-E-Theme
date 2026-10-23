# Theme track — Frosty for Enlightenment

Confirmed 2026-10-15 as independent from control-centre application development.
Owner: theme-kit. Application behaviour/providers live in ../control-centre.
The current standalone native material preview is a reference, not an installed
E theme. See desktop-contracts.md for the integration boundary.

## Delivery sequence

1. Trace and render real E border and shelf groups with Frosty's small triangle
   cap, matching edge treatment, clear action glyphs and usable hit areas.
2. Cover focused/inactive, maximized, shaded and urgent windows; shelf orientations,
   constrained sizes and common widgets, menus and dialogs.
3. Keep neutral Frost, Glacier Blue and Mint as coordinated material/accent choices.
   Preserve text contrast, focus and disabled states across all hues.
4. Build through BKC, inspect native renders, then use the established protected
   desktop trial for a selected candidate. Application of a theme remains distinct
   from compiling a candidate. Package only what has traceable source/notices.

Acceptance: correct E client/content swallow and actions, matching window/shelf
edges, readable widget states, sensible resizing/scaling and measured host cost.
Real-time compositor blur is optional and separate; retain a readable static
frosted fallback. Do not replace accepted blue-steel materials or disturb that theme.

The settings app should be a useful native application under Frosty or another E
theme. The theme must not require the settings app to run to style the desktop.

Rollback: retain the current working desktop theme and immutable candidate files;
follow e-desktop-theme for any actual desktop trial. Current work changes no
saved desktop theme or compositor settings.
