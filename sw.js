// Service worker: maakt de fotoapp installeerbaar en laat hem openen bij slecht bereik.
// Altijd eerst het netwerk (zodat updates direct doorkomen), anders de opgeslagen versie.
// Uploads en de fotomuur (Google) gaan hier nooit doorheen.
const CACHE = 'feest40-v13';
const SHELL = ['./', './index.html', './qr.png', './tijn-martijn.jpg', './icon-192.png', './icon-512.png', './manifest.webmanifest', './manifest-tv.webmanifest'];

self.addEventListener('install', (e) => {
  e.waitUntil(caches.open(CACHE).then((c) => c.addAll(SHELL)).then(() => self.skipWaiting()));
});

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (e) => {
  const req = e.request;
  if (req.method !== 'GET') return;
  if (new URL(req.url).origin !== self.location.origin) return;
  e.respondWith(
    fetch(req)
      .then((res) => {
        if (res.ok) { const copy = res.clone(); caches.open(CACHE).then((c) => c.put(req, copy)); }
        return res;
      })
      .catch(() => caches.match(req, { ignoreSearch: true }).then((m) => m || caches.match('./')))
  );
});
