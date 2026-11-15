"""Promote reviewed SEA history, retaining other countries and a reversible backup."""
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT/'work/sea-history-v1/public/data'
PUBLIC = ROOT/'web/public/data'
COUNTRIES = {'Indonesia','Malaysia'}


def promote():
    status=json.loads((SOURCE.parents[1]/'STATUS.json').read_text())
    if status['stage']!='ready_for_review':
        raise ValueError('History is not ready for review')
    index=json.loads((PUBLIC/'index.json').read_text())
    incoming=json.loads((SOURCE/'index.json').read_text())
    globe=json.loads((PUBLIC/'globe.json').read_text())
    addition=json.loads((SOURCE/'globe.json').read_text())
    if globe['years']!=addition['years'] or globe['cell_size']!=addition['cell_size']:
        raise ValueError('Incompatible globe grid or years')
    backup=ROOT/'work/pre-history-public'
    if not backup.exists():
        shutil.copytree(PUBLIC,backup)
    for entry in incoming['regions']:
        if entry['id'] not in COUNTRIES:
            raise ValueError('Unexpected incoming scope')
        payload=json.loads((SOURCE/entry['file']).read_text())
        if payload['meta']['period_start']!='2003-01-01' or payload['meta']['period_end']!='2024-12-31':
            raise ValueError('Incomplete history')
        payload['meta']['centroid']=[118,-2] if entry['id']=='Indonesia' else [109,4]
        for cell in payload['cells']:
            target=PUBLIC/cell['file'];target.parent.mkdir(parents=True,exist_ok=True)
            shutil.copy2(SOURCE/cell['file'],target)
        (PUBLIC/entry['file']).write_text(json.dumps(payload,separators=(',',':')),encoding='utf-8')
    index['regions']=incoming['regions']+[e for e in index['regions'] if e['id'] not in COUNTRIES|{'Nepal','Bangladesh','India'}]
    index['generated_at']=incoming['generated_at']
    index['model_scopes']={'firelert-sea-v1':sorted(COUNTRIES),'seven-country-v1':'Retained five countries use their original fitted model; no refit implied.'}
    # Do not attach a single old source fingerprint to a composite release.
    for key in ['archive_manifest_fingerprint','model_revision']:
        index.pop(key,None)
        globe.pop(key,None)
    globe['cells']=[c for c in globe['cells'] if c['region'] not in COUNTRIES]+addition['cells']
    globe['coverage_regions']=[r for r in globe['coverage_regions'] if r['id'] not in COUNTRIES]+addition['coverage_regions']
    globe['model_scopes']=index['model_scopes']
    globe['coverage_note']='Aqua-reference-equivalent activity; separate documented calibration scopes. National accuracy does not establish cell accuracy.'
    (PUBLIC/'globe.json').write_text(json.dumps(globe,separators=(',',':')),encoding='utf-8')
    (PUBLIC/'index.json').write_text(json.dumps(index,indent=2),encoding='utf-8')
    reports=ROOT/'reports/firelert-sea-v1'
    if not reports.exists():
        shutil.copytree(SOURCE.parents[1]/'reports',reports)
    print('Promoted Indonesia/Malaysia 2003–2024. Backup:',backup)


if __name__=='__main__':
    promote()
