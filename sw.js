// Serves the site from cache so it works offline, and refreshes the cache in the background.
const CACHE = "faculty-directory-v1";
const FILES = ["./", "index.html", "styles.css", "app.js", "faculty.json"];

self.addEventListener("install", (event) => {
  event.waitUntil(caches.open(CACHE).then((cache) => cache.addAll(FILES)).then(() => self.skipWaiting()));
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener("fetch", (event) => {
  if (event.request.method !== "GET" || new URL(event.request.url).origin !== location.origin) return;
  event.respondWith(
    caches.open(CACHE).then(async (cache) => {
      const key = event.request.mode === "navigate" ? "./" : event.request;
      const cached = await cache.match(key, { ignoreSearch: true });
      const fresh = fetch(event.request).then((response) => {
        if (response.ok) cache.put(key, response.clone());
        return response;
      });
      if (cached) {
        fresh.catch(() => {});
        return cached;
      }
      return fresh;
    })
  );
});
