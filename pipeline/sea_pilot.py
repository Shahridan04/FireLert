"""Build a raw UTC observation pilot, never a calibrated historical release."""
import argparse
import datetime as dt
import json
from pathlib import Path
import shutil

import pandas as pd

from pipeline.download import download, _inspect
from pipeline.sea_scope import PILOT_COUNTRIES

ROOT = Path(__file__).resolve().parents[1]


def summarize(frame):
    """Keep independent streams, nominal/high confidence, and explicit type 0."""
    required = {'latitude', 'longitude', 'acq_date', 'acq_time', 'satellite', 'confidence', 'type'}
    if not required.issubset(frame):
        raise ValueError(f'Missing columns: {sorted(required-set(frame))}')
    f = frame.copy()
    sat = f.satellite.astype(str).str.upper()
    f['stream'] = sat.map({'T': 'Terra', 'A': 'Aqua', 'N': 'VIIRS', 'TERRA': 'Terra', 'AQUA': 'Aqua', 'SUOMI-NPP': 'VIIRS'})
    conf = f.confidence.astype(str).str.lower().str.strip()
    confidence_ok = ((f.stream == 'VIIRS') & conf.isin(['n','h','nominal','high'])) | (f.stream.isin(['Terra','Aqua']) & (pd.to_numeric(conf,errors='coerce') >= 30))
    dates = pd.to_datetime(f.acq_date,format='%Y-%m-%d',errors='coerce')
    lat, lon = pd.to_numeric(f.latitude,errors='coerce'), pd.to_numeric(f.longitude,errors='coerce')
    clock = f.acq_time.astype(str).str.zfill(4)
    valid_time = clock.str.fullmatch(r'\d{4}') & (pd.to_numeric(clock.str[:2],errors='coerce') < 24) & (pd.to_numeric(clock.str[2:],errors='coerce') < 60)
    keep = confidence_ok & (pd.to_numeric(f.type,errors='coerce') == 0) & dates.notna() & lat.between(-90,90) & lon.between(-180,180) & valid_time
    f = f[keep].copy()
    f['date'] = dates[keep].dt.strftime('%Y-%m-%d')
    f['latitude'],f['longitude'] = lat[keep],lon[keep]
    f = f.drop_duplicates(['stream','latitude','longitude','date','acq_time'])
    daily = [{'date': date, **{s: int(g.stream.eq(s).sum()) for s in ['Terra','Aqua','VIIRS']}}
             for date,g in f.groupby('date',sort=True)]
    f['lat'] = (f.latitude // .5 * .5 + .25).round(2)
    f['lon'] = (f.longitude // .5 * .5 + .25).round(2)
    cells = [{'lat':float(lat),'lon':float(lon), **{s:int(g.stream.eq(s).sum()) for s in ['Terra','Aqua','VIIRS']}}
             for (lat,lon),g in f.groupby(['lat','lon'],sort=True)]
    # Exploratory selection by this snapshot's activity, not training-selected cells.
    ranks = f.groupby(['lat','lon']).size().sort_values(ascending=False).head(12)
    detailed = []
    for lat, lon in ranks.index:
        group = f[(f.lat == lat) & (f.lon == lon)]
        series = [{'date': date, **{s: int(g.stream.eq(s).sum()) for s in ['Terra','Aqua','VIIRS']}}
                  for date, g in group.groupby('date', sort=True)]
        detailed.append({'id': f'{lat:.2f}:{lon:.2f}', 'lat': float(lat), 'lon': float(lon), 'daily': series})
    return {'detailed_cells': detailed,'daily':daily,'cells':cells,'totals':{s:int(f.stream.eq(s).sum()) for s in ['Terra','Aqua','VIIRS']},
            'input_rows':len(frame),'retained_rows':len(f),'excluded_or_duplicate_rows':len(frame)-len(f)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=ROOT/'work/sea-pilot')
    parser.add_argument('--year',type=int,default=2019)
    args = parser.parse_args()
    if shutil.disk_usage(ROOT).free < 2*1024**3:
        parser.error('Pilot requires at least 2 GiB free space; no download started.')
    manifest = download(PILOT_COUNTRIES,[args.year],data_dir=args.output/'archives',workers=2)
    files = manifest['files']
    if len(files) != len(PILOT_COUNTRIES)*2 or not all(r.get('complete') for r in files):
        raise RuntimeError('Incomplete pilot inputs; no public output written')
    regions=[]
    for country in PILOT_COUNTRIES:
        frames=[]
        for row in files:
            if row['country'] != country:
                continue
            path=Path(row['path'])
            count,digest=_inspect(path)
            if digest != row['sha256'] or count != row['rows']:
                raise ValueError('Archive integrity mismatch')
            frames.append(pd.read_csv(path,low_memory=False))
        regions.append({'id':country,'name':country,**summarize(pd.concat(frames,ignore_index=True))})
    payload={'status':'raw_observation_pilot','year':args.year,'time_convention':'UTC acquisition dates; not local civil dates',
             'generated_at':dt.datetime.now(dt.timezone.utc).isoformat(),'regions':regions,
             'sources':[{k:r[k] for k in ['country','sensor','url','sha256','rows','bytes']} for r in files],
             'limitations':['No calibration or historical anomaly is published for this pilot.',
                            'Missing detections do not establish no fire or complete observation coverage.',
                            'Annual source files may be revised by NASA. This snapshot is identified by hashes.',
                            'The map aggregates the selected year into 0.5-degree cells; degrees are not equal area.']}
    out=ROOT/'web/public/data/sea-pilot.json'
    out.write_text(json.dumps(payload,separators=(',',':')),encoding='utf-8')
    (args.output/'PILOT.json').write_text(json.dumps(payload,indent=2),encoding='utf-8')
    print(json.dumps({r['id']:r['totals'] for r in regions},indent=2))


if __name__ == '__main__':
    main()