"""The calendar and calibrated globe must never advertise conflicting scope."""
import json
from pathlib import Path


def test_globe_excludes_removed_and_raw_only_countries():
    public = Path(__file__).resolve().parents[1] / 'web/public/data'
    index = json.loads((public / 'index.json').read_text(encoding='utf-8'))
    globe = json.loads((public / 'globe.json').read_text(encoding='utf-8'))
    ids = {r['id'] for r in index['regions']}
    assert 'Indonesia' in ids and 'Malaysia' in ids
    assert not ids.intersection({'Nepal', 'Bangladesh', 'India'})
    calibrated = set()
    for entry in index['regions']:
        payload = json.loads((public / entry['file']).read_text(encoding='utf-8'))
        if not payload['meta'].get('raw_only'):
            calibrated.add(entry['id'])
    assert {r['id'] for r in globe['coverage_regions']} == calibrated
    assert {c['region'] for c in globe['cells']} <= calibrated


def test_historical_spatial_detail_and_globe_reconcile():
    public = Path(__file__).resolve().parents[1] / 'web/public/data'
    globe = json.loads((public/'globe.json').read_text(encoding='utf-8'))
    def decode(payload):
        if 'daily' in payload:
            return payload['daily']
        p=payload.get('daily_compact',payload)
        return [dict(zip(p['columns'],[p.get('dictionaries',{}).get(k,[v])[v] if k in p.get('dictionaries',{}) else v for k,v in zip(p['columns'],row)])) for row in p['rows']]
    for country in ['Indonesia','Malaysia']:
        data=json.loads((public/f'{country}.json').read_text(encoding='utf-8'))
        assert data['meta']['period_start']=='2003-01-01'
        assert data['meta']['period_end']=='2024-12-31'
        assert data['meta']['model_revision']=='firelert-sea-v1'
        assert not data['meta'].get('raw_only')
        assert len(data['cells'])==12
        daily=decode(data)
        assert len(daily)==8036
        for year in [2003,2013,2024]:
            total=sum(d['harmonized'] or 0 for d in daily if d['date'].startswith(str(year)))
            annual=sum(c['values'][globe['years'].index(year)] or 0 for c in globe['cells'] if c['region']==country)
            assert abs(total-annual)<.1
        for cell in data['cells']:
            rows=decode(json.loads((public/cell['file']).read_text(encoding='utf-8')))
            assert len(rows)==8036


def test_build_omits_removed_country_and_obsolete_rhythm_payloads():
    dist = Path(__file__).resolve().parents[1] / 'dist/data'
    if not dist.exists():
        return
    assert not (dist/'Nepal.json').exists()
    assert not (dist/'Bangladesh.json').exists()
    assert not (dist/'rhythm.json').exists()
    assert not list((dist/'cells').glob('Nepal*'))
    assert not list((dist/'cells').glob('Bangladesh*'))

