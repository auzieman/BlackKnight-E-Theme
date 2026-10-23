#!/usr/bin/env python3
"""Create isolated Frosty/Minty sources from the verified, extracted Ice baseline."""
import argparse, hashlib, json, re, shutil
from pathlib import Path
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('baseline',type=Path);p.add_argument('output',type=Path)
a=p.parse_args()
assets=Path(__file__).resolve().parents[1]/'assets'
if a.output.exists():p.error('Output must be new')

def replace_once(text,old,new):
    if text.count(old)!=1:raise ValueError('Unexpected baseline: '+old[:100])
    return text.replace(old,new,1)

def hide_decoration(text, name):
    # Retain the part and its geometry: other parts may anchor to it.
    start=text.index('      part { name: "'+name+'";')
    opening=text.index('{',start)
    depth=1; end=opening+1
    while depth:
        if text[end]=='{':depth+=1
        elif text[end]=='}':depth-=1
        end+=1
    block=text[start:end]
    block=re.sub(r'(description \{ state: [^;]+;)',r'\1 visible: 0;',block)
    return text[:start]+block+text[end:]

for name in ['Frosty','Minty']:
    out=a.output/name
    shutil.copytree(a.baseline,out)
    for f in assets.glob('*.svg'):
        text=f.read_text()
        if name=='Minty':
            colors={'#e2ebf0':'#e1eee8','#c4d2dd':'#c2d8cd','#e5edf1':'#e5f0ea',
                    '#8ca2b1':'#87a99a','#9cb0bd':'#99b8aa','#617786':'#5d7e70',
                    '#d8e3ea':'#d4e8dc','#b8cbd7':'#b5d2c2','#8fa8b8':'#8aaf9c','#5a7285':'#587a68'}
            for old,new in colors.items():text=text.replace(old,new)
        (out/('frost-'+f.name)).write_text(text)
    border=(out/'edc-dm/border.edc').read_text()
    border=replace_once(border,'group { name: "e/widgets/border/default/border";',
        'group { name: "e/widgets/border/default/border";\n   images.image: "frost-rail.svg" COMP;\n   images.image: "frost-cap.svg" COMP;')
    start=border.index('      part { name: "top";')
    end=border.index('      part { name: "bevel";',start)
    block=border[start:end]
    block=block.replace('"vgrad_med_lighter.png"','"frost-rail.svg"').replace('"vgrad_med_dark_color.png"','"frost-rail.svg"')
    block=block.replace('TILED_HORIZ(120)','image.border: 14 14 6 6;').replace('fill.smooth: 0;','fill.smooth: 1;')
    border=border[:start]+block+border[end:]
    # Keep native event rectangles, icon swallow and glyph state programs intact.
    caps=''
    for key in ['icon','close','maximize','minimize']:
        caps+='''      part { name: "frost.cap.%s"; mouse_events: 0;
         description { state: "default" 0.0;
            image.normal: "frost-cap.svg";
            rel1.to: "e.event.%s"; rel2.to: "e.event.%s";
            rel1.offset: 1 0; rel2.offset: -2 -1;
         }
      }
'''%(key,key,key)
    border=replace_once(border,'      part { name: "e.swallow.icon"; type: SWALLOW;',caps+'      part { name: "e.swallow.icon"; type: SWALLOW;')
    # Light glass requires dark glyphs in both focus states.
    for symbol in ['close','up','down']:
        border=border.replace('image.normal: "sym_'+symbol+'_light_', 'image.normal: "sym_'+symbol+'_dark_')
    # Give the material and its controls room without changing resize/input logic.
    for title in ['e.text.title','title2']:
        start=border.index('      part { name: "'+title+'";')
        end=border.index('      part {',start+12)
        block=border[start:end].replace('text { font: FNBD; size: 10;', 'min: 0 28;\n            text { font: FNBD; size: 12;')
        block=block.replace('align: 0.5 0.0;\n               min:', 'align: 0.5 0.5;\n               min:')
        border=border[:start]+block+border[end:]
    # Ice's rectangular bevel crosses the transparent, cut-away rail corners.
    border=hide_decoration(border,'bevel')
    (out/'edc-dm/border.edc').write_text(border)
    shelf=(out/'edc-dm/shelf.edc').read_text()
    shelf=replace_once(shelf,'group { name: "e/shelf/default/base"; nomouse;',
        'group { name: "e/shelf/default/base"; nomouse;\n   images.image: "frost-rail.svg" COMP;\n   images.image: "frost-rail-vertical.svg" COMP;')
    rail=(out/'frost-rail.svg').read_text()
    rail=rail.replace('width="256" height="64" viewBox="0 0 256 64"','width="64" height="256" viewBox="0 0 64 256"')
    rail=rail.replace('</defs>','</defs><g transform="translate(64 0) rotate(90)">').replace('</svg>','</g></svg>')
    (out/'frost-rail-vertical.svg').write_text(rail)
    start=shelf.index('      part { name: "bg";');end=shelf.index('      part { name: "bevel";',start)
    block=shelf[start:end].replace('"vgrad_med.png"','"frost-rail.svg"').replace('"vgrad_tall.png"','"frost-rail-vertical.svg"')
    block=block.replace('TILED_HORIZ(120)','image.border: 14 14 6 6;').replace('TILED_HORIZ(40)','image.border: 6 6 14 14;').replace('fill.smooth: 0;','fill.smooth: 1;')
    shelf=shelf[:start]+block+shelf[end:]
    # The SVG already supplies its own shaped rim and highlight.
    for decoration in ['bevel','dots_start','dots_end','shine']:
        shelf=hide_decoration(shelf,decoration)
    shelf=replace_once(shelf,'//      item: "shaped" "1";', '      item: "shaped" "1";')
    (out/'edc-dm/shelf.edc').write_text(shelf)
    colors=(out/'colorclasses-dm.edc').read_text()
    colors=replace_once(colors,'name: "border_title_active";\n      color: FN_COL_HIGHLIGHT_SELECTED;',
                       'name: "border_title_active";\n      color: 35 55 65 255;')
    colors=replace_once(colors,'name: "border_frame";\n      color: WIN_DEFAULT_BASIC;',
                       'name: "border_frame";\n      color: 225 230 233 255;')
    (out/'colorclasses-dm.edc').write_text(colors)
    if name=='Minty':
        for f in [out/'fonts-dm.edc',out/'colorclasses-dm.edc']:
            f.write_text(f.read_text().replace('28 68 99','31 83 65'))
    manifest={str(f.relative_to(out)):hashlib.sha256(f.read_bytes()).hexdigest() for f in sorted(out.rglob('*')) if f.is_file()}
    (out/'frost-source.json').write_text(json.dumps({'variant':name,'files':manifest},indent=2)+'\n')
print('Prepared Frosty and Minty; preserved native window/shelf programs and content swallows.')
