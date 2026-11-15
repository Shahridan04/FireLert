import assert from 'node:assert/strict';
import {test} from 'node:test';
import {readFileSync} from 'node:fs';
import ts from 'typescript';

const source=readFileSync(new URL('../src/globeCells.ts',import.meta.url),'utf8');
const output=ts.transpileModule(source,{compilerOptions:{target:ts.ScriptTarget.ES2021,module:ts.ModuleKind.ES2022}}).outputText;
const {visibleGlobeCells}=await import('data:text/javascript;base64,'+Buffer.from(output).toString('base64'));
const globe=JSON.parse(readFileSync(new URL('../public/data/globe.json',import.meta.url),'utf8'));
const yearIndex=globe.years.indexOf(2024);
assert.ok(yearIndex>=0);
test('renderer passes all countries to the annual geometry resolver',()=>{
  const renderer=readFileSync(new URL('../src/Globe.tsx',import.meta.url),'utf8');
  assert.match(renderer,/visibleGlobeCells\(data\.cells,yearIndex,regionId\)/);
  for(const region of globe.coverage_regions){
    const visible=visibleGlobeCells(globe.cells,yearIndex,region.id);
    assert.deepEqual([...new Set(visible.map(c=>c.region))].sort(),globe.coverage_regions.map(r=>r.id).sort());
  }
});
// Fixed border fixture: renderer behavior must not depend on release membership.
const pair=['Bangladesh','India'].map((region,i)=>({id:`${region}:23:92`,region,lat:23.125,lon:92.375,values:globe.years.map(()=>i+1)}));

test('actual Bangladesh/India border square follows selected country without summation',()=>{
  assert.deepEqual(pair.map(c=>c.region).sort(),['Bangladesh','India']);
  for(const region of ['Bangladesh','India']){
    const expected=pair.find(c=>c.region===region);
    for(const input of [pair,[...pair].reverse()]){
      const visible=visibleGlobeCells(input,yearIndex,region);
      assert.equal(visible.length,1);
      assert.equal(visible[0],expected);
      assert.equal(visible[0].values[yearIndex],expected.values[yearIndex]);
    }
  }
});

test('foreign border fallback uses stable country ordering regardless of input order',()=>{
  assert.equal(visibleGlobeCells(pair,yearIndex,'Australia')[0].region,'Bangladesh');
  assert.equal(visibleGlobeCells([...pair].reverse(),yearIndex,'Australia')[0].region,'Bangladesh');
});

test('all published annual geometry has unique centers and retains original records',()=>{
  const original=new Set(globe.cells);
  const index=JSON.parse(readFileSync(new URL('../public/data/index.json',import.meta.url),'utf8'));
  const published=new Set(index.regions.map(r=>r.id));
  assert.ok(globe.cells.every(c=>published.has(c.region)),'globe cannot retain removed countries');
  assert.ok(!globe.coverage_regions.some(r=>['Nepal','Bangladesh'].includes(r.id)));
  for(const region of globe.coverage_regions.map(r=>r.id)){
    const visible=visibleGlobeCells(globe.cells,yearIndex,region);
    assert.equal(new Set(visible.map(c=>`${c.lat}:${c.lon}`)).size,visible.length);
    assert.ok(visible.every(c=>original.has(c)),'no new combined or fabricated records');
  }
});

test('selected-country unknown stays unknown and recorded zero stays visible',()=>{
  const foreign={id:'A:0:0',region:'A',lat:0.125,lon:0.125,values:[9,9,9]};
  const selected={id:'B:0:0',region:'B',lat:0.125,lon:0.125,values:[null,0,NaN]};
  const cells=Object.freeze([Object.freeze(foreign),Object.freeze(selected)]);
  assert.deepEqual(visibleGlobeCells(cells,0,'B'),[]);
  assert.deepEqual(visibleGlobeCells(cells,1,'B'),[selected]);
  assert.deepEqual(visibleGlobeCells(cells,2,'B'),[]);
  assert.deepEqual(visibleGlobeCells(cells,3,'B'),[]);
  assert.deepEqual(visibleGlobeCells(cells,0,'A'),[foreign]);
});
