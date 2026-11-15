import pandas as pd
from pipeline.sea_pilot import summarize


def test_sea_raw_keeps_streams_and_excludes_low_unknown_type_and_duplicates():
    base=dict(latitude=-1,longitude=110,acq_date='2019-09-01',acq_time='1200',type=0)
    frame=pd.DataFrame([{**base,'satellite':s,'confidence':c,'type':t} for s,c,t in
                        [('T','80',0),('A','80',0),('N','n',0),('N','n',0),('N','l',0),('A','80',-1)]])
    result=summarize(frame)
    assert result['totals']==dict(Terra=1,Aqua=1,VIIRS=1)
    assert result['retained_rows']==3
    assert result['daily'][0]['date']=='2019-09-01'
    assert sum(c['VIIRS'] for c in result['cells'])==1


def test_sea_pilot_rejects_invalid_date_time_and_coordinates():
    rows=[dict(latitude=0,longitude=110,acq_date='bad',acq_time='1200',satellite='A',confidence=90,type=0),
          dict(latitude=100,longitude=110,acq_date='2019-01-01',acq_time='1200',satellite='A',confidence=90,type=0),
          dict(latitude=0,longitude=110,acq_date='2019-01-01',acq_time='2460',satellite='A',confidence=90,type=0)]
    assert summarize(pd.DataFrame(rows))['retained_rows']==0