"""Add restrained E27 visibility rules to an exported compositor config."""
from pathlib import Path
import re,sys
src,out=map(Path,sys.argv[1:]);s=src.read_text()
# Match the existing override menu rules; preserve all other matching fields.
for typ in (9,10):
 pattern=r'(group "Comp_Match" struct \{\s*value "primary_type" int: '+str(typ)+r';.*?value "shadow_style" string: "menu";)'
 s,n=re.subn(pattern,r'\1\n            value "visibility_effect" string: "visibility/vertical";',s,count=1,flags=re.S)
 assert n==1,typ
start=s.index('    group "match.borders" list {');end=s.index('    group "match.popups" list {',start)
block=s[start:end];assert block.endswith('    }\n')
rule='''        group "Comp_Match" struct {
            value "primary_type" int: 0;
            value "borderless" char: -1;
            value "fullscreen" char: -1;
            value "shadow_style" string: "default";
            value "visibility_effect" string: "visibility/vertical";
        }
'''
s=s[:start]+block[:-6]+rule+'    }\n'+s[end:]
assert s.count('value "visibility_effect"')==3
out.write_text(s)
