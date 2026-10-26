#!/usr/bin/env python3
"""Run after exporting a new QStoryMap site; place beside its manifest.json."""
import json,os,shutil,sys
from pathlib import Path
folder=Path(__file__).resolve().parent
manifest=folder/'manifest.json'
story=folder/'story.json'
if not manifest.exists():
    sys.exit('ERROR: manifest.json was not found here. Move install_story.py and story.json into the QStoryMap export folder (next to index.html and manifest.json), then run again.')
if not story.exists():
    sys.exit('ERROR: story.json missing. Extract both files into the export folder.')
try:
    st=json.loads(story.read_text(encoding='utf-8'))
    assert len(st.get('sections',[]))==10
    m=json.loads(manifest.read_text(encoding='utf-8'))
    assert isinstance(m.get('layers'),list), 'No map layers in manifest'
except Exception as e: sys.exit(f'ERROR: Invalid story or manifest: {e}')
shutil.copy2(manifest,manifest.with_suffix('.json.backup'))
m['story']='story.json'
manifest.write_text(json.dumps(m,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print('Success: 10 corrected story sections installed. Existing map layers preserved. You can now test index.html on a local HTTP server.')
