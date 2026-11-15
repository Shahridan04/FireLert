import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import ts from 'typescript';

const source=readFileSync(new URL('../src/calendarColors.ts',import.meta.url),'utf8');
const output=ts.transpileModule(source,{compilerOptions:{target:ts.ScriptTarget.ES2021,module:ts.ModuleKind.ES2022}}).outputText;
const {calendarColor,CALENDAR_COLORS}=await import('data:text/javascript;base64,'+Buffer.from(output).toString('base64'));
assert.equal(calendarColor(null,101399),undefined);
assert.equal(calendarColor(undefined,101399),undefined);
assert.equal(calendarColor(NaN,101399),undefined);
assert.equal(calendarColor(0,101399),CALENDAR_COLORS[0]);
assert.equal(calendarColor(101399,101399),CALENDAR_COLORS.at(-1));
let prior=0;
for(const value of [1,10,100,1000,13048,101399]){
  const red=parseInt(calendarColor(value,101399).slice(1,3),16);
  assert.ok(red>=prior);
  prior=red;
}
// Decode the actual release, including its lossless numeric dictionaries.
const data=JSON.parse(readFileSync(new URL('../public/data/Indonesia.json',import.meta.url),'utf8'));
const compact=data.daily_compact;
const weeks=new Map();
for(const row of compact.rows){
  const record=Object.fromEntries(compact.columns.map((key,i)=>[key,compact.dictionaries?.[key]?compact.dictionaries[key][row[i]]:row[i]]));
  const date=new Date(record.date),year=date.getUTCFullYear();
  const week=Math.floor((date-Date.UTC(year,0,1))/86400000/7)+1;
  const key=`${year}-${week}`,total=weeks.get(key)||{raw:0,harmonized:0};
  for(const mode of ['raw','harmonized'])if(typeof record[mode]==='number')total[mode]+=record[mode];
  weeks.set(key,total);
}
const maximum=Math.max(...[...weeks.values()].flatMap(w=>[w.raw,w.harmonized]));
const positive=[...weeks.values()].filter(w=>w.harmonized>0);
assert.equal(weeks.size,1166);
assert.equal(positive.length,1163);
assert.ok(new Set(positive.map(w=>calendarColor(w.harmonized,maximum))).size>=4);
const reds=positive.map(w=>parseInt(calendarColor(w.harmonized,maximum).slice(1,3),16));
assert.ok(reds.filter(red=>red>=215).length<positive.length*.1,'bright orange must remain exceptional');
assert.ok(reds.filter(red=>red<120).length>positive.length*.5,'most weeks should remain subdued');
console.log('PASS: softened shared calendar scale preserves missing values and reserves highlights for higher activity.');