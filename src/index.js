// Solo pasan por aquí la portada (/), /tutoriales/* y /play-status (ver
// run_worker_first en wrangler.toml); el resto de la web se sirve directamente
// como ficheros estáticos.
// Los ficheros estáticos no responden a «Range» y Safari (iPhone, Mac) no
// reproduce un vídeo si no recibe 206: se recorta aquí. Los vídeos pesan
// menos de 1 MB, así que basta con leerlos enteros.
const PLAY_URL = "https://play.google.com/store/apps/details?id=com.linkalia";

// GET /play-status → {"available": true|false}. La portada lo consulta para
// cambiar «Próximamente en Google Play» por el botón de descarga en cuanto la
// app salga a producción, sin tocar la web: mientras no es pública, Play
// responde 404 a su ficha. Se guarda en caché (1 h si ya está, 15 min si no)
// para no preguntar a Play en cada visita.
async function playStatus(request, ctx) {
  const cache = caches.default;
  const key = new Request(new URL("/play-status", request.url).toString());
  const hit = await cache.match(key);
  if (hit) return hit;
  let available = false;
  try {
    const res = await fetch(PLAY_URL + "&hl=es", { method: "GET", redirect: "follow" });
    available = res.status === 200;
  } catch { /* Play no contesta: se sigue mostrando «Próximamente» */ }
  const res = new Response(JSON.stringify({ available, url: PLAY_URL }), {
    headers: {
      "Content-Type": "application/json",
      "Cache-Control": `public, max-age=${available ? 3600 : 900}`,
    },
  });
  ctx.waitUntil(cache.put(key, res.clone()));
  return res;
}

// Portada: en inglés salvo que el navegador esté en español. La elección del
// selector ES/EN (cookie «lang», la pone la propia página) manda sobre el
// idioma del navegador. A los buscadores no se les redirige, para que indexen
// las dos versiones (están enlazadas con hreflang).
const BOTS = /bot|crawl|spider|slurp|facebookexternalhit|whatsapp|telegram|preview/i;

async function home(request, env) {
  const cookie = /(?:^|;\s*)lang=(es|en)/.exec(request.headers.get("Cookie") || "");
  const first = (request.headers.get("Accept-Language") || "").split(",")[0].trim().toLowerCase();
  const isBot = BOTS.test(request.headers.get("User-Agent") || "");
  const lang = cookie ? cookie[1] : (isBot || first.startsWith("es")) ? "es" : "en";
  if (lang === "en") {
    const url = new URL("/en/", request.url);
    url.search = new URL(request.url).search;
    return new Response(null, {
      status: 302,
      headers: { Location: url.toString(), "Cache-Control": "private, no-store", Vary: "Accept-Language, Cookie" },
    });
  }
  const res = await env.ASSETS.fetch(request);
  const headers = new Headers(res.headers);
  headers.set("Cache-Control", "private, no-cache");
  headers.set("Vary", "Accept-Language, Cookie");
  return new Response(res.body, { status: res.status, headers });
}

export default {
  async fetch(request, env, ctx) {
    const path = new URL(request.url).pathname;
    if (path === "/play-status") return playStatus(request, ctx);
    if (path === "/" || path === "/index.html") return home(request, env);
    const res = await env.ASSETS.fetch(request);
    const range = request.headers.get("Range");
    const m = range && /^bytes=(\d*)-(\d*)$/.exec(range.trim());
    if (!m || res.status !== 200 || (!m[1] && !m[2])) return res;
    const body = await res.arrayBuffer();
    const size = body.byteLength;
    let start, end;
    if (m[1]) { start = +m[1]; end = m[2] ? Math.min(+m[2], size - 1) : size - 1; }
    else { start = Math.max(0, size - +m[2]); end = size - 1; }
    if (start >= size || start > end) {
      return new Response(null, { status: 416, headers: { "Content-Range": `bytes */${size}` } });
    }
    const headers = new Headers(res.headers);
    headers.set("Content-Range", `bytes ${start}-${end}/${size}`);
    headers.set("Content-Length", String(end - start + 1));
    headers.set("Accept-Ranges", "bytes");
    return new Response(body.slice(start, end + 1), { status: 206, headers });
  },
};
