"""Genera los artículos ES/EN de linkalia.org (uno por problema), el índice de guías y el sitemap.
Uso: python gen.py <carpeta public de linkalia-domain>"""
import html, json, os, sys
from content import ARTICLES, EXISTING, HUB
from content_groups import GROUPS, GROUPS_HUB

PUBLIC = sys.argv[1]
DATE = "2026-11-04"
SITE = "https://linkalia.org"
PLAY = "https://play.google.com/store/apps/details?id=com.linkalia"

UI = {
    "es": {"home": "← Inicio", "updated": "Actualizado el 4 de noviembre de 2026 · Escrito por el equipo de Linkalia",
           "top": "<strong>Linkalia</strong> · Gratis para Android, sin registro y sin anuncios",
           "top_btn": "Abrir en Google Play", "cta_btn": "Descargar en Google Play",
           "related": "Más guías", "faq": "Preguntas frecuentes",
           "foot": [("/", "Inicio"), ("/guias", "Guías"), ("/tutoriales", "Tutoriales"), ("/privacidad", "Política de privacidad")],
           "og": "/img/og-es.jpg", "locale": "es_ES", "hub": "/guias", "all": "Ver todas las guías",
           "modes_h": "Canal o Colaborativa: cuál usar", "channel": "Canal", "collab": "Colaborativa",
           "channel_sub": "uno publica, los demás ven", "collab_sub": "todos añaden y editan",
           "setup_h": "Cómo montarlo en cinco minutos",
           "setup": ["Instala Linkalia y crea una colección con el nombre del grupo.",
                     "Crea las categorías. Por ejemplo: {cats}.",
                     "Añade el material con <strong>Compartir</strong> desde cualquier app: PDF, Word, fotos, vídeos de YouTube, enlaces o ubicaciones de Google Maps.",
                     "Toca el nombre de la colección para abrir <strong>Info de la colección</strong> y, en <strong>Acceso</strong>, elige <strong>Canal</strong> o <strong>Colaborativa</strong>.",
                     "En el menú ⋮, toca <strong>Compartir enlace de invitación</strong>: mándalo al grupo de WhatsApp o enseña el <strong>código QR</strong>."],
           "setup_after": "Quien no tenga la app llega a la página para descargarla gratis; no hace falta registrarse ni dar el correo. Como administrador ves quién está en la colección y puedes expulsar (y readmitir) a quien quieras.",
           "demo": "<strong>Míralo en la app:</strong> Linkalia trae de ejemplo la colección «{name}». Al instalarla la tienes en tu biblioteca para ver cómo queda antes de crear la tuya."},
    "en": {"home": "← Home", "updated": "Updated 4 November 2026 · Written by the Linkalia team",
           "top": "<strong>Linkalia</strong> · Free for Android, no sign-up and no ads",
           "top_btn": "Open in Google Play", "cta_btn": "Get it on Google Play",
           "related": "More guides", "faq": "Frequently asked questions",
           "foot": [("/en/", "Home"), ("/en/guides", "Guides"), ("/en/tutorials", "Tutorials"), ("/en/privacy", "Privacy Policy")],
           "og": "/img/og-en.jpg", "locale": "en_US", "hub": "/en/guides", "all": "See all guides",
           "modes_h": "Channel or Collaborative: which to use", "channel": "Channel", "collab": "Collaborative",
           "channel_sub": "one person publishes, the rest view", "collab_sub": "everyone adds and edits",
           "setup_h": "How to set it up in five minutes",
           "setup": ["Install Linkalia and create a collection named after the group.",
                     "Create the categories. For example: {cats}.",
                     "Add material with <strong>Share</strong> from any app: PDFs, Word files, photos, YouTube videos, links or Google Maps locations.",
                     "Tap the collection's name to open <strong>Collection info</strong> and, under <strong>Access</strong>, pick <strong>Channel</strong> or <strong>Collaborative</strong>.",
                     "In the ⋮ menu, tap <strong>Share invite link</strong>: send it to the WhatsApp group or show the <strong>QR code</strong>."],
           "setup_after": "Anyone without the app lands on the page to download it for free; no sign-up or email needed. As admin you see who's in the collection and can remove (and readmit) anyone.",
           "demo": "<strong>See it in the app:</strong> Linkalia comes with the example collection “{name}”. Once installed it's in your library, so you can see how it looks before creating your own."},
}

CSS = """:root{--ink:#150B10;--ink-2:#1F1017;--paper:#F6EEF1;--brand:#C22A5F;--brand-mid:#DC7A9C;--brand-light:#EFB5C9;--line:rgba(246,238,241,.12)}
*{margin:0;padding:0;box-sizing:border-box}
body{background:var(--ink);color:var(--paper);font-family:'Inter',sans-serif;min-height:100vh;line-height:1.65}
a{color:var(--brand-light);text-underline-offset:3px}
.lang-switch{position:fixed;top:1.25rem;right:1.25rem;z-index:3;display:flex;gap:.4rem;background:rgba(21,11,16,.7);border:1px solid var(--line);border-radius:999px;padding:.3rem;backdrop-filter:blur(6px)}
.lang-switch a{font-size:.82rem;font-weight:500;color:rgba(246,238,241,.55);border-radius:999px;padding:.35rem .8rem;text-decoration:none}
.lang-switch a.active{background:var(--brand);color:var(--paper)}
.back{position:fixed;top:1.25rem;left:1.25rem;z-index:3;font-size:.85rem;color:rgba(246,238,241,.7);text-decoration:none;background:rgba(21,11,16,.7);border:1px solid var(--line);border-radius:999px;padding:.45rem .9rem}
article,.hub{max-width:720px;margin:0 auto;padding:5.5rem 16px 3rem}
h1{font-family:'Fraunces',serif;font-weight:500;font-size:clamp(1.9rem,5vw,2.8rem);line-height:1.15}
.meta{margin-top:.6rem;font-size:.85rem;color:rgba(246,238,241,.5)}
.lede{margin-top:1.2rem;font-size:1.1rem;color:rgba(246,238,241,.85)}
h2{font-family:'Fraunces',serif;font-weight:500;font-size:1.5rem;margin:2.6rem 0 .8rem;color:var(--brand-light)}
h3{font-size:1.1rem;font-weight:600;margin:1.8rem 0 .4rem}
p,ul,ol{margin-top:.8rem;color:rgba(246,238,241,.82)}
ul,ol{padding-left:1.3rem}
li{margin-top:.35rem}
strong{color:var(--paper);font-weight:600}
.play-top{display:flex;align-items:center;justify-content:space-between;gap:.8rem;flex-wrap:wrap;margin-top:1.4rem;padding:.8rem 1rem;background:var(--ink-2);border:1px solid var(--line);border-radius:14px;font-size:.92rem;color:rgba(246,238,241,.82)}
.play-top a{flex:none;background:var(--brand);color:var(--paper);text-decoration:none;font-weight:600;border-radius:999px;padding:.5rem 1rem;font-size:.88rem}
.note{margin-top:1rem;padding:.9rem 1rem;border-left:3px solid var(--brand);background:rgba(194,42,95,.08);border-radius:0 10px 10px 0}
.note p{margin-top:0}
.cta{margin-top:2.6rem;padding:1.4rem;background:var(--ink-2);border:1px solid var(--line);border-radius:18px;text-align:center}
.cta p{margin-top:0}
.cta a.btn{display:inline-block;margin-top:1rem;background:var(--brand);color:var(--paper);text-decoration:none;font-weight:600;border-radius:999px;padding:.75rem 1.4rem}
.related{margin-top:2.6rem}
.related ul{list-style:none;padding:0}
.related li{margin-top:.5rem}
.cards{list-style:none;padding:0;margin-top:1.6rem}
.cards li{margin-top:.8rem}
.cards a{display:block;padding:1rem 1.1rem;background:var(--ink-2);border:1px solid var(--line);border-radius:14px;text-decoration:none;color:var(--paper)}
.cards a span{display:block;margin-top:.3rem;font-size:.9rem;color:rgba(246,238,241,.65)}
.modes{display:grid;grid-template-columns:1fr 1fr;gap:.8rem;margin-top:1rem}
@media (max-width:620px){.modes{grid-template-columns:1fr}}
.mode{padding:1rem 1.1rem;background:var(--ink-2);border:1px solid var(--line);border-radius:14px}
.mode h3{margin:0;font-family:'Fraunces',serif;font-weight:500;font-size:1.25rem;color:var(--brand-light)}
.mode .sub{margin-top:.1rem;font-size:.85rem;color:rgba(246,238,241,.55)}
.mode .who{margin-top:.6rem;font-weight:600;color:var(--paper)}
.mode ul{margin-top:.3rem}
.hub h2{margin-top:2.4rem}
footer{text-align:center;padding:1.5rem 1rem 2rem;font-size:.82rem;color:rgba(246,238,241,.4)}
footer a{color:inherit;opacity:.7}"""

GA = """<script async src="https://www.googletagmanager.com/gtag/js?id=G-9EYV2RXZZ9"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','G-9EYV2RXZZ9');
document.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('a[data-play]');if(a)gtag('event','play_click',{article:a.getAttribute('data-play'),place:a.getAttribute('data-place')});});</script>"""

FONTS = """<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">"""

e = lambda s: html.escape(s, quote=True)


def play_url(campaign):
    # El referrer llega a Play Console (Adquisición de usuarios) y dice qué artículo trae instalaciones.
    return f"{PLAY}&amp;referrer=utm_source%3Dlinkalia.org%26utm_medium%3Darticle%26utm_campaign%3D{campaign}"


def head(lang, title, desc, path, alt_es, alt_en, ld, og_type="article"):
    u = UI[lang]
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{SITE}{path}">
<link rel="alternate" hreflang="es" href="{SITE}{alt_es}">
<link rel="alternate" hreflang="en" href="{SITE}{alt_en}">
<link rel="alternate" hreflang="x-default" href="{SITE}{alt_en}">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta property="og:type" content="{og_type}">
<meta property="og:url" content="{SITE}{path}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:locale" content="{u['locale']}">
<meta property="og:image" content="{SITE}{u['og']}">
<meta name="twitter:card" content="summary_large_image">
<script type="application/ld+json">
{json.dumps(ld, ensure_ascii=False, indent=1)}
</script>
{FONTS}
<style>
{CSS}
</style>
{GA}
</head>
<body>
<a class="back" href="{u['foot'][0][0]}">{u['home']}</a>
<nav class="lang-switch" aria-label="Idioma / Language">
  <a href="{alt_es}" hreflang="es" lang="es"{' class="active" aria-current="true"' if lang == 'es' else ''}>ES</a>
  <a href="{alt_en}" hreflang="en" lang="en"{' class="active" aria-current="true"' if lang == 'en' else ''}>EN</a>
</nav>
"""


def footer(lang):
    links = " &nbsp;·&nbsp; ".join(f'<a href="{h}">{t}</a>' for h, t in UI[lang]["foot"])
    return f"<footer>Linkalia &nbsp;·&nbsp; {links}</footer>\n</body>\n</html>\n"


def all_guides(lang):
    """(ruta, título corto, resumen) de todas las guías, la comparativa primero."""
    out = [(EXISTING[lang]["path"], EXISTING[lang]["short"], EXISTING[lang]["summary"])]
    out += [(a[lang]["path"], a[lang]["short"], a[lang]["summary"]) for a in ARTICLES + GROUPS]
    return out


GROUP_PATHS = {g[l]["path"] for g in GROUPS for l in ("es", "en")}


def group_block(a, lang):
    c, u = a[lang], UI[lang]

    def card(kind, sub, data):
        li = "".join(f"<li>{x}</li>" for x in data["items"])
        return f'<div class="mode"><h3>{kind}</h3><p class="sub">{sub}</p><p class="who">{data["who"]}</p><ul>{li}</ul></div>'
    steps = "".join(f"    <li>{st.format(cats=c['cats'])}</li>\n" for st in u["setup"])
    out = f"""  <h2>{u['modes_h']}</h2>
  <div class="modes">
    {card(u['channel'], u['channel_sub'], c['channel'])}
    {card(u['collab'], u['collab_sub'], c['collab'])}
  </div>

  <h2>{u['setup_h']}</h2>
  <ol>
{steps}  </ol>
  <p>{u['setup_after']}</p>
"""
    if a.get("demo"):
        out += f'  <div class="note"><p>{u["demo"].format(name=e(a["demo"][lang]))}</p></div>\n'
    return out


def article(a, lang):
    c, u = a[lang], UI[lang]
    path = c["path"]
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "Article", "headline": c["title"], "inLanguage": lang, "datePublished": DATE, "dateModified": DATE,
         "author": {"@type": "Organization", "name": "Linkalia", "url": SITE + "/"},
         "publisher": {"@type": "Organization", "name": "Linkalia", "url": SITE + "/"},
         "image": SITE + u["og"], "mainEntityOfPage": SITE + path},
        {"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": ans}} for q, ans in c["faq"]]}]}
    if c.get("howto"):
        ld["@graph"].append({"@type": "HowTo", "name": c["howto"]["name"], "inLanguage": lang,
                             "step": [{"@type": "HowToStep", "text": s} for s in c["howto"]["steps"]]})
    camp = a["campaign"]
    pool = GROUPS if a in GROUPS else ARTICLES
    rel = [(x[lang]["path"], x[lang]["short"], "") for x in pool if x[lang]["path"] != path]
    if a not in GROUPS:
        rel.insert(0, (EXISTING[lang]["path"], EXISTING[lang]["short"], ""))
    rel.append((u["hub"], u["all"], ""))
    out = head(lang, c["title"], c["desc"], path, a["es"]["path"], a["en"]["path"], ld)
    out += f"""<article>
  <h1>{e(c['h1'])}</h1>
  <p class="meta">{u['updated']}</p>
  <p class="lede">{c['lede']}</p>
  <div class="play-top"><span>{u['top']}</span><a href="{play_url(camp)}" rel="noopener" data-play="{camp}" data-place="top">{u['top_btn']}</a></div>
{c['body']}
{group_block(a, lang) if 'channel' in c else ''}
  <h2>{u['faq']}</h2>
"""
    for q, ans in c["faq"]:
        out += f"  <h3>{e(q)}</h3>\n  <p>{e(ans)}</p>\n"
    out += f"""
  <div class="cta">
    <p>{c['cta']}</p>
    <a class="btn" href="{play_url(camp)}" rel="noopener" data-play="{camp}" data-place="bottom">{u['cta_btn']}</a>
  </div>

  <nav class="related" aria-label="{u['related']}">
    <h2>{u['related']}</h2>
    <ul>
"""
    out += "".join(f'      <li><a href="{p}">{e(t)}</a></li>\n' for p, t, _ in rel)
    out += "    </ul>\n  </nav>\n</article>\n" + footer(lang)
    return out


def hub(lang):
    h, u = HUB[lang], UI[lang]
    ld = {"@context": "https://schema.org", "@type": "CollectionPage", "name": h["title"], "inLanguage": lang,
          "url": SITE + u["hub"],
          "hasPart": [{"@type": "Article", "headline": t, "url": SITE + p} for p, t, _ in all_guides(lang)]}
    out = head(lang, h["title"], h["desc"], u["hub"], "/guias", "/en/guides", ld, og_type="website")
    out += f"""<main class="hub">
  <h1>{e(h['h1'])}</h1>
  <p class="lede">{h['lede']}</p>
  <div class="play-top"><span>{u['top']}</span><a href="{play_url('guides')}" rel="noopener" data-play="guides" data-place="top">{u['top_btn']}</a></div>
  <h2>{GROUPS_HUB[lang]['problems']}</h2>
  <ul class="cards">
"""
    out += "".join(f'    <li><a href="{p}">{e(t)}<span>{e(s)}</span></a></li>\n' for p, t, s in all_guides(lang) if p not in GROUP_PATHS)
    gh = GROUPS_HUB[lang]
    out += f'  </ul>\n  <h2>{gh["groups"]}</h2>\n  <p>{gh["groups_lede"]}</p>\n  <ul class="cards">\n'
    out += "".join(f'    <li><a href="{g[lang]["path"]}">{e(g[lang]["short"])}<span>{e(g[lang]["summary"])}</span></a></li>\n' for g in GROUPS)
    out += "  </ul>\n</main>\n" + footer(lang)
    return out


def write(path, text):
    full = os.path.join(PUBLIC, path.lstrip("/").replace("/", os.sep) + ".html")
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print("escrito", full)


for a in ARTICLES + GROUPS:
    for lang in ("es", "en"):
        write(a[lang]["path"], article(a, lang))
for lang in ("es", "en"):
    write(UI[lang]["hub"], hub(lang))

# Sitemap: lo existente + guías + artículos.
urls = [("/", "2026-11-04"), ("/en/", "2026-11-04"), ("/tutoriales", "2026-10-14"), ("/en/tutorials", "2026-10-14"),
        ("/guias", DATE), ("/en/guides", DATE),
        (EXISTING["es"]["path"], DATE), (EXISTING["en"]["path"], DATE)]
for a in ARTICLES + GROUPS:
    urls += [(a["es"]["path"], DATE), (a["en"]["path"], DATE)]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
sm += "".join(f"  <url>\n    <loc>{SITE}{p}</loc>\n    <lastmod>{d}</lastmod>\n  </url>\n" for p, d in urls)
sm += "</urlset>\n"
open(os.path.join(PUBLIC, "sitemap.xml"), "w", encoding="utf-8", newline="\n").write(sm)
print("sitemap", len(urls), "URL")
