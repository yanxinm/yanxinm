#!/usr/bin/env node
/**
 * Bulk compute embeddings for TDAI l1_records without vector embeddings.
 *
 * Reads records from vectors.db l1_records that are missing in l1_vec,
 * calls NVIDIA NIM embedding API in batches, and inserts vectors.
 *
 * Usage:
 *   cd ~/.memory-tencentdb
 *   set -a && source ~/.hermes/.env && set +a
 *   node --experimental-sqlite /path/to/tdai-bulk-embed.mjs
 *
 * Dependencies: Node.js 22+ (built-in node:sqlite)
 * Prerequisites:
 *   - TDAI Gateway NOT running (to avoid SQLite lock contention)
 *   - NVIDIA_API_KEY in environment
 *   - sqlite-vec installed at ~/.memory-tencentdb/node_modules/sqlite-vec-linux-x64/vec0.so
 *   - TDAI embedding provider configured in tdai-gateway.yaml
 *
 * NOTES:
 *   - DatabaseSync has NO transactionSync() method — this script inserts
 *     each vector individually (sqlite-vec handles atomicity per row).
 *   - Must use { allowExtension: true } in DatabaseSync constructor, else
 *     load_extension fails with "not authorized".
 *   - NVIDIA nv-embedqa-e5-v5 requires input_type: "query" and does NOT
 *     accept a dimensions parameter (it outputs fixed 1024d).
 */
'use strict';

const path = require('path');
const os = require('os');
const fs = require('fs');

// ── Config ──────────────────────────────────────────
const TDAI_DIR   = path.join(os.homedir(), '.memory-tencentdb', 'memory-tdai');
const VECTORS_DB = path.join(TDAI_DIR, 'vectors.db');
const VEC_SO     = path.join(os.homedir(), '.memory-tencentdb',
  'node_modules', 'sqlite-vec-linux-x64', 'vec0.so');
const NVIDIA_KEY = (() => {
  try {
    const env = fs.readFileSync(path.join(os.homedir(), '.hermes', '.env'), 'utf8');
    const m = env.match(/^NVIDIA_API_KEY=(.+)$/m);
    return m ? m[1].trim() : null;
  } catch { return null; }
})();

const EMBED_URL   = 'https://integrate.api.nvidia.com/v1/embeddings';
const EMBED_MODEL = 'nvidia/nv-embedqa-e5-v5';
const BATCH_SIZE  = 20;
const DIMS        = 1024;

// ── Setup checks ────────────────────────────────────
if (!NVIDIA_KEY) { console.error('❌ NVIDIA_API_KEY not found in ~/.hermes/.env'); process.exit(1); }
if (!fs.existsSync(VEC_SO)) { console.error('❌ sqlite-vec not found at', VEC_SO); process.exit(1); }

// ── Open DB & load sqlite-vec ───────────────────────
// ⚠️ {allowExtension: true} is REQUIRED — without it load_extension fails
const { DatabaseSync } = require('node:sqlite');
const db = new DatabaseSync(VECTORS_DB, { allowExtension: true });
db.enableLoadExtension(true);

try {
  db.exec(`SELECT load_extension('${VEC_SO}')`);
  console.log('✅ sqlite-vec loaded');
} catch (e) {
  console.error('❌ Failed to load sqlite-vec:', e.message);
  process.exit(1);
}

// ── Find records needing embeddings ─────────────────
const missing = db.prepare(`
  SELECT r.record_id, r.content
  FROM l1_records r LEFT JOIN l1_vec v ON r.record_id = v.record_id
  WHERE v.record_id IS NULL
`).all();

console.log(`📊 ${missing.length} records need embeddings`);

if (missing.length === 0) {
  const total = db.prepare('SELECT COUNT(*) as c FROM l1_vec').get().c;
  console.log(`✅ All ${total} records already have embeddings. Nothing to do.`);
  db.close();
  process.exit(0);
}

// ── Prepare insert statement ────────────────────────
const insertVec = db.prepare(
  'INSERT INTO l1_vec (record_id, embedding, updated_time) VALUES (?, ?, ?)');

// ── Batch process ────────────────────────────────────
// ⚠️ DatabaseSync does NOT have transactionSync(). Each insert is atomic
// via sqlite-vec's vec0 virtual table. No explicit transaction wrapping needed.
let done = 0;
let errors = 0;

for (let i = 0; i < missing.length; i += BATCH_SIZE) {
  const batch = missing.slice(i, i + BATCH_SIZE);
  const texts = batch.map(m => m.content);

  try {
    const resp = await fetch(EMBED_URL, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${NVIDIA_KEY}`,
        'Content-Type': 'application/json',
      },
      // ⚠️ nv-embedqa-e5-v5 requires input_type and does NOT support dimensions param
      body: JSON.stringify({
        input: texts,
        model: EMBED_MODEL,
        encoding_format: 'float',
        input_type: 'query',          // required for asymmetric models
        // NO dimensions param — model rejects it with HTTP 400
      }),
    });

    if (!resp.ok) {
      const err = await resp.text();
      console.error(`❌ Batch ${i/BATCH_SIZE+1}: HTTP ${resp.status} — ${err.substring(0, 120)}`);
      errors++;
      continue;
    }

    const data = await resp.json();

    // Insert each vector individually (no transaction wrapper needed)
    for (let j = 0; j < data.data.length; j++) {
      const vec = new Float32Array(data.data[j].embedding);
      insertVec.run(batch[j].record_id, vec, new Date().toISOString());
    }

    done += batch.length;
    if (done % 100 === 0 || done === missing.length) {
      const pct = ((done / missing.length) * 100).toFixed(1);
      console.log(`  ${done}/${missing.length} (${pct}%)`);
    }

    // Rate-limit breather
    if (i + BATCH_SIZE < missing.length) {
      await new Promise(r => setTimeout(r, 200));
    }
  } catch (e) {
    console.error(`❌ Batch ${i/BATCH_SIZE+1}: ${e.message}`);
    errors++;
    await new Promise(r => setTimeout(r, 2000));
  }
}

// ── Summary ──────────────────────────────────────────
const finalVec  = db.prepare('SELECT COUNT(*) as c FROM l1_vec').get().c;
const finalRec  = db.prepare('SELECT COUNT(*) as c FROM l1_records').get().c;
const stillMiss = db.prepare(`
  SELECT COUNT(*) as c FROM l1_records r
  LEFT JOIN l1_vec v ON r.record_id = v.record_id
  WHERE v.record_id IS NULL
`).get().c;

console.log(`\n📊 Summary:`);
console.log(`  l1_records: ${finalRec}`);
console.log(`  l1_vec:     ${finalVec}`);
console.log(`  remaining:  ${stillMiss}`);
console.log(`  errors:     ${errors}`);
console.log(errors === 0 && stillMiss === 0 ? '✅ Done!' : '⚠️  Partial — check errors above');

db.close();
