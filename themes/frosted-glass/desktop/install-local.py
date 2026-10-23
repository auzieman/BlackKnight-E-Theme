#!/usr/bin/env python3
"""Stage dated candidates in the user theme picker; never select a theme."""
from pathlib import Path
import argparse,hashlib,re
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('source',type=Path)
parser.add_argument('--revision',default='20261023')
args=parser.parse_args()
if not re.fullmatch(r'[a-zA-Z0-9-]+',args.revision):parser.error('Invalid revision')
source=args.source;target=Path.home()/'.elementary/themes'
target.mkdir(parents=True,exist_ok=True)
for name in ['Frosty','Minty']:
 data=(source/(name+'.edj')).read_bytes()
 dest=target/(name+'-'+args.revision+'.edj')
 if dest.exists() and dest.read_bytes()!=data:
  raise SystemExit('Refusing to replace a different candidate: '+str(dest))
 dest.write_bytes(data);dest.chmod(0o644)
 print(hashlib.sha256(data).hexdigest(),dest)
print('Theme selection unchanged.')
