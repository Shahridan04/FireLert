export const CALENDAR_COLORS = ['#26353b','#4e4b3d','#786040','#a86c3d','#d77945','#f89965','#ffd4ad'];

/** Shared softened log scale: reserve warm highlights for higher activity. */
export function calendarColor(value:number|null|undefined,maximum:number):string|undefined {
  if(typeof value!=='number'||!Number.isFinite(value))return undefined;
  if(value<=0)return CALENDAR_COLORS[0];
  const ratio=Math.pow(Math.min(1,Math.log1p(value)/Math.log1p(Math.max(1,maximum))),2.5);
  const position=ratio*(CALENDAR_COLORS.length-1);
  const lower=Math.floor(position),upper=Math.min(lower+1,CALENDAR_COLORS.length-1);
  const mix=position-lower;
  const channels=(hex:string)=>[1,3,5].map(offset=>parseInt(hex.slice(offset,offset+2),16));
  const a=channels(CALENDAR_COLORS[lower]),b=channels(CALENDAR_COLORS[upper]);
  return '#'+a.map((channel,i)=>Math.round(channel+(b[i]-channel)*mix).toString(16).padStart(2,'0')).join('');
}