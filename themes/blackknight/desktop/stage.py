#!/usr/bin/env python3
"""Copy the donor and optionally remap geometry-matched PNGs; never rewrite EDC."""
import argparse
import hashlib
import json
import shutil
import struct
from pathlib import Path

SLOTS = (
    "default_top_left_corner", "default_top_titlebar", "default_top_right_corner",
    "default_left_border_mid", "default_left_border_top", "default_right_border",
    "default_bottom_right_corner", "default_bottom_right", "default_bottom_mid",
    "default_bottom_left", "default_bottom_left_corner", "e17_mini_button",
    "e17_shelf_bg2_h", "e17_shelf_bg2_v", "e17_shelf_bg3_v", "shelf_bar", "shelf_bottom", "shelf_top", "shelf_bottom_left", "shelf_bottom_right", "shelf_top_left", "shelf_top_right", "shelf_mid_left", "shelf_mid_right", "shelf_ibar_bg",
)

def dimensions(path):
    data = path.read_bytes()
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError(f"Not a PNG: {path}")
    return struct.unpack(">II", data[16:24])

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("base", type=Path)
parser.add_argument("output", type=Path)
parser.add_argument("--assets", type=Path, help="Replacement PNGs named exactly like donor wrk/ images")
a = parser.parse_args()
if a.output.exists():
    parser.error("Output must be new")
changes = []
if a.assets:
    supplied = sorted(a.assets.glob("*.png"))
    if not supplied:
        parser.error("No replacement PNGs supplied")
    for replacement in supplied:
        if replacement.stem not in SLOTS:
            parser.error(f"Outside the current frame reskin: {replacement.name}")
        original = a.base / "wrk" / replacement.name
        expected=dimensions(original); supplied_size=dimensions(replacement)
        center_strip=replacement.stem=="default_top_titlebar" and supplied_size[1]==expected[1]
        if supplied_size != expected and not center_strip:
            parser.error(f"Size mismatch for {replacement.name}: expected {dimensions(original)}")
        changes.append({"image": "wrk/" + replacement.name,
                        "size": supplied_size, "original_sha256": digest(original),
                        "replacement_sha256": digest(replacement)})
shutil.copytree(a.base, a.output, ignore=shutil.ignore_patterns("*.edj", ".git"))
for change in changes:
    shutil.copy2(a.assets / Path(change["image"]).name, a.output / change["image"])
# Record and verify the essential invariant: all donor EDC remains byte-identical.
edc = {}
for original in a.base.rglob("*.edc"):
    relative = original.relative_to(a.base)
    assert digest(original) == digest(a.output / relative), relative
    edc[str(relative)] = digest(original)
manifest = {"scope": "donor frame image remapping only", "images": changes,
            "unchanged_edc_sha256": edc, "build_recipe": (a.base / "build.sh").read_text()}
(a.output / "blackknight-source.json").write_text(json.dumps(manifest, indent=2) + "\n")
print(f"Staged {len(changes)} image replacements; {len(edc)} EDC files unchanged")
