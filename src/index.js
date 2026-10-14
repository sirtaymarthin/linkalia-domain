// Solo pasa por aquí /tutoriales/* (ver run_worker_first en wrangler.toml); el
// resto de la web se sirve directamente como ficheros estáticos.
// Los ficheros estáticos no responden a «Range» y Safari (iPhone, Mac) no
// reproduce un vídeo si no recibe 206: se recorta aquí. Los vídeos pesan
// menos de 1 MB, así que basta con leerlos enteros.
export default {
  async fetch(request, env) {
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
