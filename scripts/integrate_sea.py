"""Integrate verified regional observations into the existing explorer catalog."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / 'web/public/data'


def integrate(public=PUBLIC):
    for country in ['Indonesia','Malaysia']:
        existing=public/f'{country}.json'
        if existing.exists() and json.loads(existing.read_text(encoding='utf-8'))['meta'].get('model_revision')=='firelert-sea-v1':
            raise ValueError('Historical release already promoted; refusing to overwrite it with the raw pilot.')
    pilot = json.loads((public / 'sea-pilot.json').read_text(encoding='utf-8'))
    index_path = public / 'index.json'
    index = json.loads(index_path.read_text(encoding='utf-8'))
    def daily_rows(rows, cell='ALL'):
        return [dict(date=d['date'], cell_id=cell, raw_terra=d['Terra'], raw_aqua=d['Aqua'],
                     raw_viirs=d['VIIRS'], raw=d['VIIRS'], harmonized=None, lo=None, hi=None,
                     coverage='Observation coverage unknown; UTC archive dates',
                     source='observed VIIRS; UTC raw pilot', model='Not calibrated') for d in rows]
    entries = []
    for r in pilot['regions']:
        country = r['id']
        daily = daily_rows(r['daily'])
        detail = [dict(id=c['id'],lat=c['lat'],lon=c['lon'],daily=daily_rows(c['daily'],c['id'])) for c in r.get('detailed_cells',[])]
        payload = dict(meta=dict(region=country, name=r['name'], label='REAL FIRMS DATA · RAW',
                     period_start=f"{pilot['year']}-01-01", period_end=f"{pilot['year']}-12-31",
                     reference='Separate raw sensor counts', model='Not calibrated', raw_only=True,
                     coverage_note='2019 UTC observations only. No regional calibration or multi-year anomaly has been validated. Missing records do not establish zero burning.',
                     sources=[dict(name=s['sensor'], url=s['url']) for s in pilot['sources'] if s['country']==country],
                     centroid=[118,-2] if country=='Indonesia' else [109,4],
                     cell_scope='12 activity-ranked 0.5-degree cells from 2019; exploratory selection, not training-selected. National totals use all cells.'),
                     daily=daily, cells=detail, eval=[], rhythm=None, anomalies=[], weekly_climatology=[], critical_periods=[])
        (public / f'{country}.json').write_text(json.dumps(payload, separators=(',',':')),encoding='utf-8')
        entries.append(dict(id=country,name=r['name'],file=f'{country}.json'))
    excluded={'Nepal','Bangladesh',*(r['id'] for r in pilot['regions'])}
    index['regions']=entries+[r for r in index['regions'] if r['id'] not in excluded]
    index_path.write_text(json.dumps(index,indent=2),encoding='utf-8')
    # The globe has its own catalog: remove countries no longer in the explorer.
    # Raw SEA counts must not be inserted into this calibrated layer.
    globe_path = public / 'globe.json'
    if globe_path.exists():
        globe = json.loads(globe_path.read_text(encoding='utf-8'))
        calibrated = {r['id'] for r in index['regions']} - {r['id'] for r in pilot['regions']}
        globe['coverage_regions'] = [r for r in globe['coverage_regions'] if r['id'] in calibrated]
        globe['cells'] = [c for c in globe['cells'] if c['region'] in calibrated]
        globe_path.write_text(json.dumps(globe,separators=(',',':')),encoding='utf-8')

    raw_globe = dict(years=[pilot['year']], cell_size=.5, label='REAL FIRMS DATA ? RAW VIIRS',
                     reference='Raw VIIRS detections (uncalibrated)',
                     coverage_regions=[dict(id=r['id'],name=r['name'],sources=['observed VIIRS; UTC']) for r in pilot['regions']],
                     cells=[dict(id=f"{r['id']}:{c['lat']:.2f}:{c['lon']:.2f}",region=r['id'],lat=c['lat'],lon=c['lon'],values=[c['VIIRS']])
                            for r in pilot['regions'] for c in r['cells'] if c['VIIRS'] > 0])
    (public/'globe-raw.json').write_text(json.dumps(raw_globe,separators=(',',':')),encoding='utf-8')


if __name__=='__main__':
    integrate()

