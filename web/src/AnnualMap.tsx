import {useEffect,useMemo,useRef,useState} from 'react';
import {fmt,geoCoordinate,numeric} from './utils';
import './annual-map.css';

interface Cell {id:string;region:string;lat:number;lon:number;values:(number|null)[]}
interface Layer {years:number[];cell_size:number;reference:string;cells:Cell[];coverage_regions:{id:string;name:string}[]}
interface Outline {coordinates:number[][][]}
let cached:Promise<[Layer,Outline]>|undefined;
function load(){
  if(!cached)cached=Promise.all(['globe.json','world-outline.json'].map(async file=>{
    const response=await fetch(`${import.meta.env.BASE_URL}data/${file}`);
    if(!response.ok)throw new Error('Map data unavailable');
    return response.json();
  })) as Promise<[Layer,Outline]>;
  return cached;
}

export default function AnnualMap({regionId,regionName,initialYear,availableCells,onCell}:{regionId:string;regionName:string;initialYear:number;availableCells:string[];onCell:(id:string)=>void}){
  const canvas=useRef<HTMLCanvasElement>(null);
  const [data,setData]=useState<Layer|null>(null),[outline,setOutline]=useState<Outline|null>(null),[error,setError]=useState(false);
  const [year,setYear]=useState(initialYear),[world,setWorld]=useState(false),[selected,setSelected]=useState<Cell|null>(null);
  useEffect(()=>{let active=true;load().then(([layer,borders])=>{if(active){setData(layer);setOutline(borders);}}).catch(()=>{cached=undefined;if(active)setError(true);});return()=>{active=false;};},[]);
  useEffect(()=>{setYear(initialYear);setSelected(null);setWorld(false);},[regionId,initialYear]);
  const index=data?.years.indexOf(year)??-1;
  const regionCells=useMemo(()=>data?.cells.filter(c=>c.region===regionId)||[],[data,regionId]);
  const bounds=useMemo(()=>{
    if(world||!regionCells.length)return [-180,180,-70,85];
    const lons=regionCells.map(c=>c.lon),lats=regionCells.map(c=>c.lat);
    const left=Math.min(...lons),right=Math.max(...lons),bottom=Math.min(...lats),top=Math.max(...lats);
    const pad=Math.max(2,(right-left)*.1,(top-bottom)*.1);
    return [Math.max(-180,left-pad),Math.min(180,right+pad),Math.max(-85,bottom-pad),Math.min(85,top+pad)];
  },[world,regionCells]);
  const maximum=useMemo(()=>data?.cells.reduce((m,c)=>c.values.reduce<number>((a,v)=>numeric(v)?Math.max(a,v):a,m),1)||1,[data]);
  const projection=useMemo(()=>{
    const [left,right,bottom,top]=bounds,scale=Math.min(960/(right-left),440/(top-bottom));
    return {scale,x:(lon:number)=>480+(lon-(left+right)/2)*scale,y:(lat:number)=>220-(lat-(bottom+top)/2)*scale};
  },[bounds]);
  const visible=useMemo(()=>data?.cells.filter(c=>numeric(c.values[index])&&c.lon>=bounds[0]&&c.lon<=bounds[1]&&c.lat>=bounds[2]&&c.lat<=bounds[3])||[],[data,index,bounds]);
  useEffect(()=>{
    const context=canvas.current?.getContext('2d');if(!context||!data)return;
    context.fillStyle='#10232d';context.fillRect(0,0,960,440);
    context.strokeStyle='#29414a';context.lineWidth=.5;
    for(let lon=-180;lon<=180;lon+=10){context.beginPath();context.moveTo(projection.x(lon),0);context.lineTo(projection.x(lon),440);context.stroke();}
    for(let lat=-80;lat<=80;lat+=10){context.beginPath();context.moveTo(0,projection.y(lat));context.lineTo(960,projection.y(lat));context.stroke();}
    context.strokeStyle='#8aaba7';context.lineWidth=.8;
    for(const line of outline?.coordinates||[]){context.beginPath();line.forEach(([lon,lat],i)=>{if(!i||Math.abs(lon-line[i-1][0])>180)context.moveTo(projection.x(lon),projection.y(lat));else context.lineTo(projection.x(lon),projection.y(lat));});context.stroke();}
    // Draw selected-country records last so border overlap never sums countries.
    const ordered=[...visible.filter(c=>c.region!==regionId),...visible.filter(c=>c.region===regionId)];
    const size=Math.max(.8,data.cell_size*projection.scale);
    for(const c of ordered){const value=c.values[index]!;const t=Math.log1p(Math.max(0,value))/Math.log1p(maximum);context.fillStyle=value===0?'#52666a':`hsl(${36*(1-t)} 78% ${24+45*t}%)`;context.fillRect(projection.x(c.lon)-size/2,projection.y(c.lat)-size/2,size,size);}
    if(selected&&numeric(selected.values[index])){context.strokeStyle='#ffffff';context.lineWidth=2;context.strokeRect(projection.x(selected.lon)-size/2-2,projection.y(selected.lat)-size/2-2,size+4,size+4);}
  },[data,outline,visible,projection,index,maximum,selected,regionId]);
  const ranked=useMemo(()=>[...regionCells].filter(c=>numeric(c.values[index])).sort((a,b)=>b.values[index]!-a.values[index]!).slice(0,20),[regionCells,index]);
  const dailyId=selected?.id.startsWith(regionId+':')?selected.id.slice(regionId.length+1):selected?.id;
  if(error)return <div className="annual-map"><p role="alert">Annual map unavailable. The calendar and optional Earth view remain available.</p><button className="text-button" onClick={()=>{setError(false);load().then(([layer,borders])=>{setData(layer);setOutline(borders);}).catch(()=>{cached=undefined;setError(true);});}}>Retry map</button></div>;
  if(!data)return <div className="annual-map" role="status">Loading annual geographic activity…</div>;
  return <section className="annual-map" aria-labelledby="annual-map-title">
    <div className="annual-map-heading"><div><span className="eyebrow">WHERE ACTIVITY WAS RECORDED</span><h3 id="annual-map-title">Annual activity map</h3></div><div className="annual-map-controls"><label>Map year <select value={index<0?'':year} onChange={e=>{setYear(Number(e.target.value));setSelected(null);}}><option value="" disabled>Select year</option>{data.years.map(y=><option key={y}>{y}</option>)}</select></label><button className="chart-scale-button" aria-pressed={world} onClick={()=>setWorld(v=>!v)}>{world?`Focus ${regionName}`:'World overview'}</button></div></div>
    <p className="chart-note">Full-year Aqua-reference activity, independent of the calendar date range and scale switch. Showing {year}; choose another map year above.</p>
    <canvas ref={canvas} width={960} height={440} role="img" aria-label={`Annual processed activity map for ${year}. Click a grid square to inspect it, or use the accessible cell list below.`} onClick={event=>{
      const rect=event.currentTarget.getBoundingClientRect(),x=(event.clientX-rect.left)/rect.width*960,y=(event.clientY-rect.top)/rect.height*440;
      const tolerance=Math.max(data.cell_size*projection.scale/2,3);
      const hits=visible.filter(c=>Math.abs(projection.x(c.lon)-x)<=tolerance&&Math.abs(projection.y(c.lat)-y)<=tolerance);
      hits.sort((a,b)=>Number(b.region===regionId)-Number(a.region===regionId)||Math.hypot(projection.x(a.lon)-x,projection.y(a.lat)-y)-Math.hypot(projection.x(b.lon)-x,projection.y(b.lat)-y));setSelected(hits[0]||null);
    }}/>
    <div className="annual-map-legend"><span>LOW</span><i/><span>HIGH</span><span>Fixed all-year log scale · {data.cell_size}° grid · gray = recorded zero</span></div>
    <div className="annual-map-inspection" aria-live="polite">{selected?<><strong>{data.coverage_regions.find(r=>r.id===selected.region)?.name||selected.region} · {geoCoordinate(selected.lat,'lat')}, {geoCoordinate(selected.lon,'lon')}</strong><span>{fmt(selected.values[index],1)} {data.reference} in {year}</span>{selected.region===regionId&&dailyId&&availableCells.includes(dailyId)?<button className="button subtle" onClick={()=>onCell(dailyId)}>Explore daily cell record</button>:<span>Annual summary only; daily detail is available for selected cells.</span>}</>:<span>Click a colored grid square to inspect its annual activity.</span>}</div>
    <details><summary>Accessible cell list: 20 highest-activity cells in {regionName}, {year}</summary><div className="annual-map-cell-list">{ranked.length?ranked.map(c=><button key={c.id} className="text-button" onClick={()=>setSelected(c)}>{geoCoordinate(c.lat,'lat')}, {geoCoordinate(c.lon,'lon')} · {fmt(c.values[index],1)}</button>):<p>No processed annual values available.</p>}</div></details>
    <p className="chart-note">Processed regions only—not worldwide coverage. Uncolored areas are not evidence of no fire. Detections are not distinct fires or burned area. Geographic context: Natural Earth.</p>
  </section>;
}