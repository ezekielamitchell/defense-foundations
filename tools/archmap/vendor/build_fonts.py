"""Fetch OFL font sources at a recorded revision, instance and subset offline faces."""
import hashlib
import io
import json
from pathlib import Path
import sys
import urllib.request
sys.dont_write_bytecode=True
BASE=Path(__file__).resolve().parent
sys.path.insert(0,str(BASE.parent/'.artifacts/font-tools'))
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools import subset

def fetch(url):
    with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'defense-foundations-archmap'}),timeout=60) as response:return response.read()

target=BASE/'fonts';target.mkdir(parents=True,exist_ok=True)
revision=json.loads(fetch('https://api.github.com/repos/google/fonts/commits/main'))['sha']
families=[('cormorantgaramond','Cormorant Garamond',[500]),('inter','Inter',[400,500,600]),('ibmplexmono','IBM Plex Mono',[400,500]),('notosansjp','endr-brackets',[300])]
manifest={'revision':revision,'fonts':[],'sources':[]}
latin=set(range(0x20,0x7f))|{0xB7,0x2190,0x2192,0x2191,0x2193,0x2260,0x2013,0x2014,0x2018,0x2019,0x201c,0x201d,0x2026,0xD7,0x2318,0x2081,0x2080,0x2265}
for directory,family,weights in families:
    listing=json.loads(fetch(f'https://api.github.com/repos/google/fonts/contents/ofl/{directory}?ref={revision}'))
    files=[f['name'] for f in listing if f['name'].endswith('.ttf') and 'Italic' not in f['name']]
    license=fetch(f'https://raw.githubusercontent.com/google/fonts/{revision}/ofl/{directory}/OFL.txt')
    dest=target/'sources'/directory;dest.mkdir(parents=True,exist_ok=True);(dest/'OFL.txt').write_bytes(license)
    for weight in weights:
        name=next((f for f in files if '[' in f),None)
        if not name:name=next(f for f in files if ('Regular' if weight==400 else 'Medium') in f)
        url=f'https://raw.githubusercontent.com/google/fonts/{revision}/ofl/{directory}/'+urllib.parse.quote(name)
        raw=fetch(url);(dest/name).write_bytes(raw)
        font=TTFont(io.BytesIO(raw))
        if 'fvar' in font:
            axes={axis.axisTag:(weight if axis.axisTag=='wght' else axis.defaultValue) for axis in font['fvar'].axes}
            font=instantiateVariableFont(font,axes,inplace=True)
        opts=subset.Options();opts.flavor='woff2';opts.recalc_timestamp=False;opts.layout_features=['*']
        sub=subset.Subsetter(options=opts);sub.populate(unicodes={0x300c,0x300d} if family=='endr-brackets' else latin);sub.subset(font);font.flavor='woff2'
        out=f'{directory}-{weight}.woff2';font.save(target/out)
        manifest['fonts'].append(dict(family=family,weight=weight,file=out,bytes=(target/out).stat().st_size))
        manifest['sources'].append(dict(file='sources/'+directory+'/'+name,url=url,sha256=hashlib.sha256(raw).hexdigest(),license='sources/'+directory+'/OFL.txt'))
        print(out,(target/out).stat().st_size,flush=True)
(target/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
(target/'OFL.txt').write_text('All embedded typefaces are licensed under the SIL Open Font License 1.1.\nComplete original notices and licenses are preserved under sources/<family>/OFL.txt.\nSee manifest.json for source URLs, revision, and hashes.\n')
total=sum(f['bytes'] for f in manifest['fonts']);assert total<=220*1024,total
print('Combined WOFF2 bytes:',total)
