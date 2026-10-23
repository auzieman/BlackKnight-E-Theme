# Frosty / Minty desktop candidates

These are full Enlightenment/Elementary archives built from the installed Ice
baseline, with original Frosty window and shelf materials. Minty changes those
materials and text accents to a pale green. Other widgets initially inherit Ice;
this is a first desktop candidate, not complete visual acceptance or a release.

The generator preserves the base window programs, event rectangles, title and
client/icon swallows, inherited border styles and shelf orientation programs.
New cap artwork is passive: native event rectangles continue to own input.
No compositor blur, animation loop, root access or desktop restart is needed to
render these candidates. No desktop configuration is changed by the build.

## Reproduce

1. Extract `/usr/share/elementary/themes/Ice.edj` with `edje_decc`, using
   `-main-out source.edc`. The emitted build.sh refers to an old entrypoint;
   compile `source.edc` with `-id . -fd .` in the extracted directory.
2. Supply the missing `Megrim.ttf` from the `Ice` branch of the local
   Enlightenment-Themes source. Its font is already embedded in the installed
   archive, but edje_decc did not emit it. Do not substitute another font.
3. Rebuild the unchanged baseline first. Baseline BKC run:
   `3c23ec4d-5151-4cbb-9b4c-f4fbb5231f23` (successful).
4. `python3 prepare.py EXTRACTED_BASELINE NEW_OUTPUT_DIRECTORY`
5. Stage the generated Frosty/Minty trees and render.c in the existing BKC native
   build pipeline, pinned compiler image and resource limits. Compile each
   source.edc, then render the native border/shelf groups using render.c.
6. Review rendered images before a protected live trial. Use the project desktop
   theme skill for the independent 20-second rollback. Do not apply directly.

The source manifest records hashes for every staged input. Builds run on edge
with 2 CPUs and a 2 GiB memory limit, not on the laptop.

## Provenance and distribution

Installed base SHA256:
`652b6e9630f7e1322897fb058563ae6869d7ad6c027f95afd4cc05ec7e344093`.
Font source: Enlightenment-Themes `Ice` commit
`707e6fa2a0e13f73b2319b4537c1429eaef5a8ec`.
Original Frosty SVG provenance is in ../assets/provenance.json (CC BY-SA 4.0).
Our generator and renderer are GPLv3 under the project source license.
Inherited Ice source/assets retain their upstream licensing; the source tree's
COPYING distinguishes BSD/LGPL theme code and asset-specific notices. Retain and
audit those notices, including the embedded Megrim font, before public packaging.
A copy of the upstream notices is retained in ../upstream-notices. The upstream
image-license file appears to describe gesture icons rather than the full Ice
asset set; verify the actual image permissions before distributing full EDJs.
Local experimental candidates do not establish distribution readiness.

## Checked candidates

BKC run `38747e6a-08e3-4a9f-a580-e851409fa140` built both variants and rendered
native focused/inactive borders and horizontal/vertical shelves with font
fixtures present. Artifact SHA256 verification passed. Installed, without
selection, into `~/.elementary/themes/` as `Frosty-20261023.edj` and
`Minty-20261023.edj`.

- Frosty: `81c9c336aba7c638a01ea5136e383aff0cf08668e6c078eff56a9f5f6a4a1696`
- Minty: `b4d33ed4f6acac861aa07707f04121de1aebc672e2b9ad7eb9d014166f8af204`

Native buffer renders:
[Frosty](../../../docs/images/frosty-desktop-candidate-20261023.png),
[Minty](../../../docs/images/minty-desktop-candidate-20261023.png).
The plain client rectangles are preview fixtures, not a depiction of all app
widgets. These are native renders, not screenshots of an applied desktop theme.

Original Ice min/max arrow glyphs remain; final action glyph styling, inherited
border variants and full widget/menu contrast are still visual review items.

The corner-corrected BKC run `146eb2f2-9917-4c39-950d-9b3decc442c4`
produced the locally staged `Frosty-20261023-corners` and
`Minty-20261023-corners` files. User screenshots show these on the live desktop;
full widget and interaction coverage remains under review.
