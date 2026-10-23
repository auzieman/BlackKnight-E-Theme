# Frosted-glass shape preparation

Working direction: off-white glass, frosted grey structure, restrained icy
accents and softly blunted triangle details. User reference is the original
`~/.e/e/shots/shot-2026-10-12_16-54-13.jpg`, inspected on 2026-10-14.
The screenshot is a source of intent, not a precision geometry specification.

See [workstation settings plan](../../docs/workstation-settings-plan.md) and
[editable silhouette sheet](shape-study.svg). Original SVG generated from
symmetrical edge cuts on an equilateral triangle; no third-party art reused.
Original artwork follows the repository's CC BY-SA 4.0 licensing.

Each silhouette has six sides, alternating long and short when cut fraction
is below one third. Threefold symmetry is retained. Cuts parallel to the
opposite edge yield 120-degree interior angles. A stretched variant can be a
useful visual design, but does not retain those angles in general.

Use the motif for corner accents, selected navigation markers and title/action
caps. Keep content panels broadly rectangular, labels readable and hit regions
large enough to use. Shape alone must not identify Close versus Minimize.
Hover can change tint or outline without moving the target or resizing chrome.
Focus and inactive states must be explicit; optional animation is deferred.

The SVG is a geometric study, not proof of frosted rendering or E compatibility.
No live blur, desktop theme installation or running settings centre is included.

## Native first assembly — Frosty

The user selected the name/direction **Frosty**. The independent
[control-centre preview](../../../control-centre/README.md) consumes a versioned
copy of the original [SVG components](assets/): a slim glass rail, a small
truncated-triangle cap and a quiet content plate. Window and shelf studies share
the rail/end treatment; glyphs remain live Edje text.

Neutral Frost, Glacier Blue and Mint are app-local preview palettes. See
[desktop integration boundary](desktop-contracts.md) for the work required to
turn these materials into actual E border/shelf/widget groups. The first app
preview does not change or install a desktop theme.

Independent delivery scope: [Frosty theme track](track.md). Functional settings pages are owned by the [application roadmap](../../../control-centre/docs/application-roadmap.md).

## Desktop candidates — 2026-10-23

[Frosty and Minty desktop integration](desktop/README.md) now generates full
candidate EDJs from a successfully rebuilt Ice baseline. Original glass rails
and compact triangle caps decorate real window and shelf groups. Common widgets
still inherit Ice. This supersedes the app-only boundary above; full desktop
interaction and all inherited border styles still need a protected live trial.
