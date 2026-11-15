import type {Daily} from './types';
import {fmt,numeric} from './utils';

/** Paired date-window counts, never a cross-sensor calibration. */
export default function RawComparison({rows}:{rows:Daily[]}){
 const groups=new Map<string,Daily[]>();
 for(const row of rows){const key=row.date.slice(0,7);groups.set(key,[...(groups.get(key)||[]),row]);}
 const series=[['raw_terra','Terra','#e8ae73'],['raw_aqua','Aqua','#7ed9c6'],['raw_viirs','VIIRS','#ec7d66']] as const;
 const points=[...groups].sort(([a],[b])=>a.localeCompare(b)).map(([date,days])=>({date,values:series.map(([key])=>{const values=days.map(d=>d[key]).filter(numeric);return values.length?values.reduce((a,b)=>a+b,0):null;})}));
 const max=Math.max(1,...points.flatMap(p=>p.values).filter(numeric));
 return <><p className="panel-description">Monthly raw observations on the same selected dates. Detection sensitivity and overpass differences remain; these lines are not equivalent fire counts.</p>
 <svg viewBox="0 0 850 230" role="img" aria-label="Monthly raw Terra, Aqua and VIIRS counts; exact values in table below" style={{width:'100%'}}>
 {series.map(([,name,color],j)=><g key={name}><text x={20+j*220} y={18} fill={color} fontSize="12">{name}</text><polyline fill="none" stroke={color} strokeWidth="2" points={points.map((p,i)=>`${35+i/Math.max(1,points.length-1)*780},${195-(p.values[j]||0)/max*155}`).join(' ')}/></g>)}
 {points.map((p,i)=><text key={p.date} x={35+i/Math.max(1,points.length-1)*780} y="220" fill="#b1c4c8" fontSize="9" textAnchor="middle">{p.date.slice(5)}</text>)}
 </svg><details><summary>Monthly sensor values</summary><div className="table-scroll"><table><thead><tr><th>Month (UTC)</th>{series.map(([,s])=><th key={s}>{s}</th>)}</tr></thead><tbody>{points.map(p=><tr key={p.date}><td>{p.date}</td>{p.values.map((v,i)=><td key={i}>{fmt(v)}</td>)}</tr>)}</tbody></table></div></details></>;
}
