import {spawnSync} from 'node:child_process';
import {cpSync, mkdirSync, rmSync, readdirSync, readFileSync} from 'node:fs';
import {fileURLToPath} from 'node:url';
import path from 'node:path';
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
await import('./prepare-map.mjs');
// Invoke Node entrypoints directly so Windows does not need shell command quoting.
for (const [entry, args] of [
  ['typescript/bin/tsc', ['--noEmit']],
  ['vite/bin/vite.js', ['build']],
]) {
  const result = spawnSync(process.execPath, [path.join(root, 'web/node_modules', entry), ...args],
    {cwd: path.join(root, 'web'), stdio: 'inherit'});
  if (result.status !== 0) process.exit(result.status || 1);
}
const target = path.resolve(root, 'dist');
if (path.dirname(target) !== root || path.basename(target) !== 'dist') throw new Error('Invalid build output path');
rmSync(target, {recursive:true, force:true});
mkdirSync(target, {recursive: true});
cpSync(path.join(root, 'web/dist'), target, {recursive: true});
// Ship only files reachable from the active catalog; scientific archives stay in source.
const dataDir=path.join(target,'data');
const index=JSON.parse(readFileSync(path.join(dataDir,'index.json'),'utf8'));
const keep=new Set(['index.json','globe.json','globe-raw.json','sea-pilot.json','world-land.json','world-outline.json']);
for(const region of index.regions){
  keep.add(region.file);
  const payload=JSON.parse(readFileSync(path.join(dataDir,region.file),'utf8'));
  for(const cell of payload.cells||[])if(cell.file)keep.add(cell.file);
}
function prune(dir,prefix=''){
  for(const entry of readdirSync(dir,{withFileTypes:true})){
    const rel=prefix+entry.name, full=path.join(dir,entry.name);
    if(entry.isDirectory())prune(full,rel+'/');
    else if(!keep.has(rel))rmSync(full);
  }
}
prune(dataDir);
console.log('Static deployment assets prepared; inactive country/rhythm payloads excluded from dist/.');
