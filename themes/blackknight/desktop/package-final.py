#!/usr/bin/env python3
"""Assemble verified native artifacts without modifying desktop selection."""
import argparse, hashlib, json, shutil, subprocess
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('artifacts',type=Path);p.add_argument('output',type=Path);p.add_argument('--run-id',required=True);p.add_argument('--payload-sha256',required=True);a=p.parse_args()
subprocess.run(['sha256sum','-c','SHA256SUMS'],cwd=a.artifacts,check=True)
repo=Path(__file__).resolve().parents[3]
if a.output.exists():raise SystemExit('Output exists; choose a new package directory.')
a.output.mkdir(parents=True)
files={'BlackKnight-BlueSteel.edj':a.artifacts/'BlackKnight-BlueSteel.edj','BlackKnight-Storm.edj':a.artifacts/'blackknight-animated.edj','BlackKnight-Still.edj':a.artifacts/'blackknight-still.edj','BlackKnight Ice.eet':repo/'master/terminal/BlackKnight Ice.eet','remap-verification.txt':a.artifacts/'remap-verification.txt'}
files['wallpaper-provenance.json']=repo/'themes/blackknight/assets/provenance.json'
files['griffin-provenance.json']=repo/'themes/blackknight/desktop/assets/griffin-v3/provenance.json'
if (a.artifacts.parent/'packages.txt').exists():files['packages.txt']=a.artifacts.parent/'packages.txt'
for name,src in files.items():shutil.copy2(src,a.output/name)
source=(a.artifacts/'source-revision.txt').read_text().strip()
manifest={'source_revision':source,'bkc_run_id':a.run_id,'payload_sha256':a.payload_sha256,'artifacts':{name:hashlib.sha256((a.output/name).read_bytes()).hexdigest() for name in files},'wallpaper':{'storm_cycle_seconds':52.98,'distant_cloud_cycle_seconds':90,'accelerated_preview':False},'validation':'Native image-only donor remap; checksums verified. Desktop selections are separate from packaging.'}
(a.output/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
(a.output/'README.txt').write_text('BlackKnight final local build\n\nBlackKnight-BlueSteel.edj: blue-steel donor reskin with AuzieTek griffin emblem.\nBlackKnight-Storm.edj: production parallax wallpaper (53-second storm, 90-second distant clouds).\nBlackKnight-Still.edj: no-animation alternative.\nBlackKnight Ice.eet: optional Terminology palette candidate.\n\nSelect the installed theme in Enlightenment Settings > Look > Theme and the wallpaper in Wallpaper settings. The palette is available in Terminology color-scheme settings. Selections are not changed by packaging.\n\nDonor EDC, geometry, interaction and programs are preserved. The scene and moving cloud/lightning overlays are original generated artwork. This local build is not a tagged/public release; upstream theme distribution notices remain a release prerequisite.\n\nSee manifest.json and remap-verification.txt for build identity and verification.\n')
(a.output/'SHA256SUMS').write_text(''.join(f'{hashlib.sha256(f.read_bytes()).hexdigest()}  {f.name}\n' for f in sorted(a.output.iterdir()) if f.is_file()))
print(a.output)
