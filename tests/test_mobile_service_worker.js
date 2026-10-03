const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const test = require('node:test');
const vm = require('node:vm');

function worker() {
  const listeners = new Map();
  const fetched = [];
  const stored = [];
  const cached = new Map();
  const origin = 'https://example.test';
  const cache = {
    async put(request, response) { stored.push(request.url); cached.set(request.url, response); },
    async addAll() {},
  };
  const context = {
    URL, Response,
    self: { location: { origin }, addEventListener: (kind, listener) => listeners.set(kind, listener) },
    caches: { async open() { return cache; }, async match(request) { return cached.get(request.url); } },
    async fetch(request) { fetched.push(request.url); return new Response('current network content'); },
  };
  vm.runInNewContext(fs.readFileSync(path.join(__dirname, '../mobile/sw.js'), 'utf8'), context);
  function request(url, method = 'GET') {
    let response;
    listeners.get('fetch')({ request: { url, method }, respondWith(value) { response = value; } });
    return response;
  }
  return { request, fetched, stored, cached, context, origin };
}

test('extension and foreign requests are left to the browser without cache writes', () => {
  const w = worker();
  for (const url of ['chrome-extension://extension/content.js', 'moz-extension://extension/content.js',
    'file:///mobile/app.js', 'https://foreign.test/mobile/app.js', 'http://example.test/mobile/app.js']) {
    assert.equal(w.request(url), undefined, url);
  }
  assert.equal(w.request(`${w.origin}/mobile/app.js`, 'POST'), undefined);
  assert.deepEqual(w.fetched, []);
  assert.deepEqual(w.stored, []);
});

test('same-origin shell remains cache first and projection remains network first', async () => {
  const w = worker();
  const shell = `${w.origin}/defense-foundations/mobile/app.js`;
  const projection = `${w.origin}/defense-foundations/docs/aegis-phase0-projection.json`;
  w.cached.set(shell, new Response('cached shell'));
  w.cached.set(projection, new Response('older projection'));
  assert.equal(await (await w.request(shell)).text(), 'cached shell');
  assert.equal(await (await w.request(projection)).text(), 'current network content');
  assert.deepEqual(w.fetched, [projection]);
  assert.deepEqual(w.stored, [projection]);
});

test('same-origin projection can use its cached copy when offline', async () => {
  const w = worker();
  const projection = `${w.origin}/docs/aegis-phase0-projection.json`;
  w.cached.set(projection, new Response('cached educational projection'));
  w.context.fetch = async () => { throw new Error('offline'); };
  assert.equal(await (await w.request(projection)).text(), 'cached educational projection');
  assert.deepEqual(w.stored, []);
});
