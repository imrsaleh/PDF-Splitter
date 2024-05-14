// service-worker.js
self.addEventListener('fetch', function(event) {
  if (event.request.url.includes('hls.m3u8')) {
    const newHeaders = new Headers(event.request.headers);
    newHeaders.set('Referrer', 'https://app.restream.io/');

    const modRequest = new Request(event.request, {
      headers: newHeaders
    });

    event.respondWith((async () => {
      return fetch(modRequest);
    })());
  }
});
