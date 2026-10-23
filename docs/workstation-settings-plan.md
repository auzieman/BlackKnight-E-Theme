# Workstation settings and frosted-glass preparation

Prepared 2026-10-14 for review. Planning and editable shape reference only;
no settings shell implementation, native theme build or desktop application.

## Product direction

Provide one native EFL workstation control centre. Enlightenment already owns
many settings; the shell improves discovery, grouping and continuity rather
than duplicating every module. Use everyday labels and show current state.
A stable sidebar owns primary navigation; small tabs own genuine subsections.
Search finds settings and synonyms, then opens the relevant control.

| Category | First useful pages |
| --- | --- |
| Appearance | Theme, wallpaper, shelves, window behaviour |
| Displays & Input | Monitors, text size/scaling, keyboard, mouse, shortcuts |
| Audio | Output, microphone, per-application volumes |
| Network | Connections, Wi-Fi, Bluetooth, VPN |
| Accounts & Security | Users, authentication, locking |
| Software & Updates | Enaptic handoff, repositories, update preferences |
| Storage & Devices | Disks, mounts, removable media, printers |
| System | Power, date/time, startup, host information |
| Services | Service status, startup policy, logs |

A page presents current status, everyday controls, then expandable advanced
options. Clearly label read-only/unavailable controls. Show immediate versus
Apply behaviour, authentication and restart/logout needs at the actual action.
Keep navigation in the same window; focused tasks can use dialogs. Keyboard
navigation, focus visibility, readable text, scaling and reduced motion belong
in the initial design. Never rely solely on colour or decorative shape.

Services are a secondary workstation capability, with a proper sidebar home.
Explain a service's purpose and current state before showing technical details.
No bulk service changes or privileged executor are implied by this preparation.

## Ownership and integration study

Theme-kit owns material/chrome and the shared shape reference. A settings shell
would be a separate application/project, with its own state and provider layer.
E-Jamz remains independently owned; this work does not modify the player.

Before implementation, inventory the installed E version's settings registry,
module entrypoints and supported APIs. Classify each page as native embedding,
public API adapter, or an explicitly labelled external-tool handoff. Existing
module availability does not establish embeddability. Research boundaries for
Pulse/PipeWire, network, OpenRC, storage and authentication against this host.
Reuse Enaptic's authenticated-action experience where appropriate; do not copy
its package helper into a general host-management privilege boundary.

## Selected workflows

- [e-visual-layout](../.agents/skills/e-visual-layout/SKILL.md): structure,
  material, readability and representative visual previews. The user's new
  frosted direction applies to this variant; accepted blue-metal assets stay
  intact in their own theme.
- [e-desktop-theme](../.agents/skills/e-desktop-theme/SKILL.md): source/group
  tracing, preservation of E actions, BKC native builds and scoped trials.
- Enaptic's project-owned backend/authentication workflows are references for
  a later provider/security pass, after scope and host interfaces are known.
  No new skill is needed merely to produce this design plan.
- Image generation is unnecessary for this geometric preparation. Native
  EDC/vector geometry is the appropriate first reference; choose raster work
  later only if the frosted material benefits from original textures.

## Review sequence

1. Agree on truncated-triangle silhouette, orientation and title-rail treatment.
2. Preview Displays, Audio and Services with the same sidebar/page structure.
   Include a normal page, unavailable control, focused control and confirmation.
3. Map representative controls to real host/module interfaces before wiring.
4. Build a standalone native preview through BKC; measure static/visible and
   hidden cost on the i3. Compare contrast over light, dark and busy backgrounds.
5. Consider a selected desktop group override only after native visual review.
   Desktop application follows the existing authorized timed-trial workflow;
   this plan does not change the installed theme or compositor.

Prefer static translucent layers and bounded cached assets. A frosted visual
appearance does not require live background blur. Treat real compositor blur
as a separately measured enhancement with an opaque/readable fallback.

Acceptance: people can find text size, output device and service status without
knowing module names; three page types remain coherent; controls retain full
rectangular hit targets; no continuous decorative redraw; unavailable features
are honest; default material remains readable across backgrounds.

Rollback for preparation: remove the new plan/reference files and their links.
Existing theme work and uncommitted task history are retained.
