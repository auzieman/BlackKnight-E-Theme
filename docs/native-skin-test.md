# Native skin compile and runtime test — 2026-10-10

Compiled EDJ and minimal EFL app successfully in lab-edge Swarm through BKC CLI/core, run `16a7df81-61d3-4da4-8fae-2983fe0c899a`, source `f1fd16d`. One CPU, 1 GiB limit, pinned Alpine 3.24.2 and signed EFL 1.28.1-r2 matching the laptop. The first run exposed C-dialect and callback-signature mistakes; both were corrected before the successful retry. The temporary compiler service was removed and existing services were untouched.

![Actual native Edje render](images/native-skin-active.png)

![Compact native render](images/native-skin-compact.png)

The test app runs on the laptop's existing EFL libraries; software_x11 was requested. Native focus reversal, live title changes, disabled/enabled clicks and hide/show were exercised using keys and window-targeted XTest input. Disabled click produced no action; enabled click emitted `bk,action,activate`. The 480-pixel titlebar kept control clearance, with current ellipsis retaining the title's trailing text.

A 3.001-second visible idle sample recorded zero CPU ticks and 53,932 KiB RSS (about 52.7 MiB). This is a short observation, not sustained performance acceptance. One nonfatal Evas layout-hint diagnostic appeared at startup; no crash was observed. Native proportions, diagnostic cause and preferred ellipsis direction remain follow-ups. This is not a full Sci-Fi theme integration or a working media engine.

Artifacts and complete logs are in `build/out/swarm-16a7df81/`. Relaunch on the laptop with `ELM_ENGINE=software_x11 ELM_ACCEL=none build/out/swarm-16a7df81/result/skin-test build/out/swarm-16a7df81/result/blackknight-material.edj`. The app is left open at 800 pixels; F1–F6 exercise state and sizing, Escape exits. [Machine-readable evidence](native-skin-test.json) records source/artifact hashes and limits.


## Donor image remap desktop trials — 2026-10-10

The first desktop trial replaced 12 window-frame image entries in a copy of the running Sci-Fi EDJ; 4,647 other archive entries were byte-identical. The user judged it close, requested refinement, and noted that the bar still used original artwork.

The second pass adds 13 shelf images and supplies a 1024-pixel-wide titlebar center strip to reduce excessive horizontal texture stretching. BKC run `48adbdda-4241-4861-ae0b-3fb480815a85` passed native compilation and archive verification: 25 image entries replaced; 4,634 other entries unchanged. Donor EDC, controls, glints, scripts and group geometry were retained. Frame and shelf alpha masks were verified against the donor at target resolution.

The native timer and independent host watchdog both restored after the approximately 20-second trial. The watchdog now reads the exact saved Eet theme setting and passes it to the timer; saving the resolved fallback chain had expanded duplicate names in the first trial. That first saved value was corrected before the second trial. After the second trial, both the serialized setting (`E20-Scifi-theme`) and resolved list matched the pretrial state. User applications were left running.

![Shelf during the second trial](images/shelf-remap-v2-trial.png)

![Shelf after automatic restoration](images/shelf-remap-v2-restored.png)

[Frame screenshot](images/frame-remap-v2-trial.png) is partly obscured by overlapping sample windows after the desktop restart. The shelf render confirms its material changed. Generic application toolbar artwork remains original; this is a frame-and-shelf image pass. Detailed artifact hashes and runtime proof are in [frame-and-shelf-test.json](frame-and-shelf-test.json). The EDJ and native tools are retained under `build/out/frame-and-shelf-v2/result/`. No permanent theme application or final visual acceptance is claimed.
