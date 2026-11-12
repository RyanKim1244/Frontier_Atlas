// Phone-width check: node widemath.mjs <site-dir> <id,id,...> [mathjax node_modules dir]
// Opens each concept page at 390px and lists formulas wider than their column. CDN requests are served from local node_modules.
import { createRequire } from 'module'; import http from 'http'; import fs from 'fs'; import path from 'path';
const require = createRequire(import.meta.url); const { chromium } = require('playwright');
const [dir, ids, nm] = process.argv.slice(2);
const srv = http.createServer((q, r) => { let p = path.join(dir, decodeURIComponent(q.url.split('?')[0])); if (p.endsWith('/')) p += 'index.html';
  fs.readFile(p, (e, d) => { if (e) { r.statusCode = 404; r.end(); return; } r.setHeader('content-type', p.endsWith('.html') ? 'text/html' : p.endsWith('.js') ? 'text/javascript' : p.endsWith('.svg') ? 'image/svg+xml' : 'application/json'); r.end(d); }); }).listen(0);
const port = srv.address().port; const b = await chromium.launch(); const pg = await b.newPage({ viewport: { width: 390, height: 844 } });
await pg.route(/cdn\.jsdelivr\.net\/npm\//, async rt => { const u = new URL(rt.request().url()); const m = u.pathname.match(/^\/npm\/((?:@[^/]+\/)?[^@/]+)(?:@[^/]+)?\/(.*)$/);
  const f = m && path.join(nm, m[1], m[2]); if (f && fs.existsSync(f)) rt.fulfill({ body: fs.readFileSync(f), contentType: f.endsWith('.js') ? 'text/javascript' : 'application/octet-stream' }); else rt.abort(); });
await pg.route(/supabase\.co/, rt => rt.abort());
let bad = 0;
for (const id of ids.split(',')) {
  await pg.goto(`http://localhost:${port}/#concept-${id}`); await pg.waitForTimeout(1500);
  await pg.evaluate(async () => { for (const d of document.querySelectorAll('details')) d.open = true; if (window.MathJax?.typesetPromise) await MathJax.typesetPromise(); });
  await pg.waitForTimeout(800);
  const r = await pg.evaluate(() => { const out = []; const n = document.querySelectorAll('mjx-container').length;
    for (const m of document.querySelectorAll('mjx-container')) { const w = m.getBoundingClientRect().width; let p = m.parentElement; while (p && getComputedStyle(p).display === 'inline') p = p.parentElement;
      const cw = p ? p.clientWidth : 390; if (w > cw + 1) out.push({ w: Math.round(w), cw, tex: (m.querySelector('mjx-assistive-mml, math')?.textContent || m.textContent).slice(0, 120) }); }
    return { n, out, docw: document.documentElement.scrollWidth }; });
  bad += r.out.length; console.log(id, 'formulas', r.n, 'too wide', r.out.length, 'page width', r.docw); for (const o of r.out) console.log('  ', o.w, '>', o.cw, o.tex);
}
await b.close(); srv.close(); process.exit(0);
