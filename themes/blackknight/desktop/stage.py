#!/usr/bin/env python3
"""Stage a private Sci-Fi adaptation; preserve the reference source tree."""
import argparse, hashlib, json, shutil
from pathlib import Path
parser=argparse.ArgumentParser()
parser.add_argument("base",type=Path);parser.add_argument("output",type=Path)
a=parser.parse_args()
if a.output.exists(): raise SystemExit("Output must be new")
root=Path(__file__).resolve().parents[3]
shutil.copytree(a.base,a.output,ignore=shutil.ignore_patterns("*.edj",".git"))
p=a.output/"edc/border.edc";original=p.read_text()
text=original.replace('image: "wrk/default_top_titlebar.png" COMP;', 'image: "wrk/default_top_titlebar.png" COMP;\n   image: "wrk/bk-blue-plate.png" COMP;')
start=text.index('name:          "top_titlebar";')
end=text.index('\n\t\t//////////////////////////////////////////////////////////////////////////////////////////',start)
part=text[start:end]
assert part.count('normal: "wrk/default_top_titlebar.png";')==1
part=part.replace('normal: "wrk/default_top_titlebar.png";', 'normal: "wrk/bk-blue-plate.png";\n                    border: 280 280 48 240; border_scale: 1; border_scale_by: 0.04;')
part=part.replace('smooth: 0;', 'smooth: 1;')
# Add inherited active state immediately after the default description.
pos=part.rfind('\n\t\t}')
assert pos>=0
part=part[:pos].rstrip()+'\n            description { state: "active" 0.0; inherit: "default" 0.0; color: 255 255 255 255; }'+part[pos:]
part=part.replace('state:    "default" 0.0;', 'state:    "default" 0.0;\n                color: 145 171 201 255;',1)
text=text[:start]+part+text[end:]
# Existing state chains now also drive the visible plate.
text=text.replace('target:  "title_bar";', 'target:  "title_bar";\n        target:  "top_titlebar";')
for name in ["border_shaped.edc","border_noresize.edc","border_dialog.edc","border_noresize_dialog.edc"]:
 assert (a.output/name).is_file()
 text=text.replace('#include "'+name+'"', '#include "../'+name+'"')
p.write_text(text)
shutil.copy2(root/"master/blue-steel/assets/plate.png",a.output/"wrk/bk-blue-plate.png")
manifest={"base_border_sha256":hashlib.sha256(original.encode()).hexdigest(),"adapted_border_sha256":hashlib.sha256(text.encode()).hexdigest(),"plate_sha256":hashlib.sha256((a.output/"wrk/bk-blue-plate.png").read_bytes()).hexdigest(),"scope":"default window titlebar material; upstream geometry/actions/effects retained","distribution":"private local study; upstream licensing not established"}
(a.output/"blackknight-source.json").write_text(json.dumps(manifest,indent=2)+"\n")
