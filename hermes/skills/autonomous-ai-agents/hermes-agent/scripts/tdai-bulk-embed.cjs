#!/usr/bin/env node
/* TDAI bulk embedding: compute vectors for l1_records missing from l1_vec.
 * Uses NVIDIA NIM via node:sqlite + sqlite-vec.
 * 
 * Usage:
 *   cd ~/.memory-tencentdb
 *   source ~/.hermes/.env && export NVIDIA_API_KEY
 *   node --experimental-sqlite /path/to/tdai-bulk-embed.mjs
 * 
 * Requirements: node:sqlite (Node 22+), sqlite-vec
 */
const path = require('path');
const os = require('os');
const fs = require('fs');
const { DatabaseSync } = require('node:sqlite');

const DB_PATH = path.join(os.homedir(), '.memory-tencentdb', 'memory-tdai', 'vectors.db');
const VEC_SO = path.join(os.homedir(), '.memory-tencentdb', 'node_modules', 'sqlite-vec-linux-x64', 'vec0.so');
const NVIDIA_KEY = process.env.NVIDIA_API_KEY || (() => {
  try {
    const env = fs.readFileSync(os.homedir() + '/.hermes/.env', 'utf8');
    const m = env.match(/^NVIDIA_API_KEY=(.+)$/m);
    return m ? m[1].trim() : '';
  } catch(e) { return ''; }
})();

if (!NVIDIA_KEY) { console.error('FAIL: No NVIDIA_API_KEY'); process.exit(1); }

const db = new DatabaseSync(DB_PATH, { allowExtension: true });
db.enableLoadExtension(true);
db.loadExtension(VEC_SO);
console.log('sqlite-vec loaded OK');

const missing = db.prepare(`
  SELECT r.record_id, r.content FROM l1_records r
  LEFT JOIN l1_vec v ON r.record_id = v.record_id
  WHERE v.record_id IS NULL
`).all();
console.log('Records needing embeddings:', missing.length);
if (!missing.length) { console.log('All done!'); db.close(); process.exit(0); }

const insertVec = db.prepare('INSERT INTO l1_vec (record_id, embedding, updated_time) VALUES (?, ?, ?)');
const https = require('https');
const BATCH_SIZE = 20;

function embed(texts) {
  return new Promise((resolve, reject) => {
    const pld = JSON.stringify({
      input: texts,
      model: 'nvidia/nv-embedqa-e5-v5',
      encoding_format: 'float',
      input_type: 'query'  // asymmetric model requires this
    });
    const u = new URL('https://integrate.api.nvidia.com/v1/embeddings');
    const opts = {
      hostname: u.hostname, path: u.pathname, method: 'POST',
      headers: { 'Authorization': `Bearer ${NVIDIA_KEY}`, 'Content-Type': 'application/json', 'Content-Length': Buffer.byteLength(pld) },
      timeout: 30000
    };
    const r = https.request(opts, res => {
      let d = '';
      res.on('data', c => d += c);
      res.on('end', () => { try { resolve(JSON.parse(d)); } catch(e) { reject(d.substring(0,200)); } });
    });
    r.on('error', reject);
    r.on('timeout', () => { r.destroy(); reject('timeout'); });
    r.write(pld); r.end();
  });
}

async function main() {
  const total = missing.length;
  let done = 0, errors = 0;
  for (let i = 0; i < total; i += BATCH_SIZE) {
    const batch = missing.slice(i, i + BATCH_SIZE);
    try {
      const data = await embed(batch.map(m => m.content));
      if (data.data && data.data.length > 0) {
        for (let j = 0; j < data.data.length; j++) {
          insertVec.run(batch[j].record_id, new Float32Array(data.data[j].embedding), new Date().toISOString());
        }
        done += batch.length;
      }
    } catch(e) { errors++; }
    if (done % 400 === 0 && done > 0) console.log('Progress:', done, '/', total);
    if (i + BATCH_SIZE < total) await new Promise(r => setTimeout(r, 50));
  }
  const c = db.prepare('SELECT COUNT(*) as cnt FROM l1_vec').get().cnt;
  const r = db.prepare('SELECT COUNT(*) as cnt FROM l1_records').get().cnt;
  console.log(`Done: l1_vec=${c} / l1_records=${r} (errors: ${errors})`);
  db.close();
}
main().catch(e => { console.error('Fatal:', e.message); process.exit(1); });
