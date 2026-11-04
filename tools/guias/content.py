# Textos de las guías. Cada artículo ataca un problema concreto; datos de la app comprobados en el código (2026-11-04).

EXISTING = {
    "es": {"path": "/apps-guardar-enlaces", "short": "Apps para guardar enlaces en Android (y alternativas a Pocket)",
           "summary": "Raindrop.io, Link, Gatherly, Files de Google y Linkalia comparadas."},
    "en": {"path": "/en/link-saver-apps", "short": "Link saver apps for Android (and Pocket alternatives)",
           "summary": "Raindrop.io, Link, Gatherly, Files by Google and Linkalia compared."},
}

HUB = {
    "es": {"title": "Guías para organizar enlaces y documentos en el móvil · Linkalia",
           "h1": "Guías para no perder nada en el móvil",
           "desc": "Guías prácticas para guardar y ordenar enlaces, PDF, recetas, viajes y documentos en Android: WhatsApp, Instagram, TikTok, marcadores y más.",
           "lede": "Cada guía parte de un problema real —el PDF que se pierde en el chat, la receta que guardaste y no encuentras, el viaje con veinte enlaces sueltos— y explica cómo resolverlo paso a paso."},
    "en": {"title": "Guides to organise links and documents on your phone · Linkalia",
           "h1": "Guides to stop losing things on your phone",
           "desc": "Practical guides to save and organise links, PDFs, recipes, trips and documents on Android: WhatsApp, Instagram, TikTok, bookmarks and more.",
           "lede": "Each guide starts from a real problem — the PDF lost in a chat, the recipe you saved and can't find, the trip with twenty loose links — and shows how to fix it step by step."},
}

ARTICLES = [
# ───────────────────────────── 1. WhatsApp ─────────────────────────────
{
"campaign": "whatsapp",
"es": {
"path": "/guardar-enlaces-whatsapp",
"title": "Cómo guardar enlaces y PDF de WhatsApp para que no se pierdan en el chat",
"h1": "Cómo guardar enlaces y PDF de WhatsApp para que no se pierdan en el chat",
"short": "Guardar enlaces y PDF de WhatsApp sin que se pierdan",
"summary": "El enlace o el PDF que te mandan hoy queda enterrado mañana. Cómo sacarlo del chat en dos toques.",
"desc": "Te mandan enlaces, sitios y PDF por WhatsApp y a los dos días no hay forma de encontrarlos. Cómo guardarlos fuera del chat, ordenados por temas, en Android.",
"lede": "Alguien manda al grupo el enlace del hotel, el PDF con el horario o el vídeo que «tienes que ver». Dos días y trescientos mensajes después, ya no está. Hacer scroll hacia arriba no es un sistema: aquí tienes cómo sacarlo del chat en el momento y tenerlo a mano cuando lo necesites.",
"body": """
  <h2>Por qué en WhatsApp se pierde todo</h2>
  <p>WhatsApp está pensado para conversar, no para archivar. Lo importante llega mezclado con audios, memes y «ok 👍», y cada chat guarda lo suyo por separado. Además:</p>
  <ul>
    <li>El buscador solo sirve si recuerdas una palabra exacta del mensaje.</li>
    <li>Los <strong>mensajes destacados</strong> siguen dentro de cada chat y no se pueden ordenar por temas.</li>
    <li>Si vacías el chat o liberas espacio, los PDF y las fotos pueden desaparecer.</li>
    <li>El truco de «enviármelo a mí mismo» acaba siendo otro chat infinito.</li>
  </ul>

  <h2>La solución: guardarlo fuera del chat en cuanto llega</h2>
  <p>La clave es no dejarlo para luego. Con una app para guardar enlaces y archivos, desde el propio chat lo mandas a una carpeta con nombre («Viaje a Lisboa», «Cole de los niños», «Trabajo») y te olvidas.</p>
  <p>Con <strong>Linkalia</strong> son estos pasos:</p>
  <ol>
    <li>En WhatsApp, <strong>mantén pulsado</strong> el mensaje con el enlace, el PDF o la foto.</li>
    <li>Toca <strong>Compartir</strong> (el icono de la flecha arriba; si no lo ves, en ⋮ › Compartir).</li>
    <li>Elige <strong>Linkalia</strong> en la lista de apps.</li>
    <li>Elige la colección y pulsa <strong>«Guardar aquí»</strong>. El título y la imagen aparecen solos.</li>
  </ol>
  <p>Puedes seleccionar varias fotos o documentos a la vez y guardarlos de una tacada.</p>

  <h2>Se ordena solo</h2>
  <p>Linkalia reconoce qué le mandas y lo coloca en su categoría: un vídeo de YouTube o TikTok va a <strong>Ver</strong>, un PDF o un billete de Renfe a <strong>Documentos</strong>, un enlace de Google Maps, Booking o Airbnb a <strong>Lugares</strong>, una canción de Spotify a <strong>Escuchar</strong>. Si prefieres elegir tú la categoría cada vez, se desactiva en Ajustes.</p>
  <p>Después lo encuentras con el buscador, que mira el título, la descripción, tus notas, el nombre del archivo y la web de origen. Y lo que usas a menudo lo puedes <strong>fijar arriba</strong>.</p>

  <div class="note"><p><strong>¿Lo que te mandan es para todo el grupo?</strong> En vez de reenviar mensajes, comparte la colección como <em>Colaborativa</em>: todos guardáis ahí y los cambios llegan a todos al momento. Lo explicamos en <a href="/organizar-viaje-en-grupo">cómo organizar un viaje en grupo</a>.</p></div>

  <h2>¿Y si uso Telegram, Gmail o Chrome?</h2>
  <p>Funciona igual: cualquier app con botón <strong>Compartir</strong> puede mandar a Linkalia. WhatsApp es solo el caso más habitual.</p>
""",
"howto": {"name": "Guardar un enlace o un PDF de WhatsApp en Linkalia",
          "steps": ["Mantén pulsado el mensaje con el enlace, el PDF o la foto.", "Toca Compartir.",
                    "Elige Linkalia en la lista de apps.", "Elige la colección y pulsa «Guardar aquí»."]},
"faq": [("¿Se guarda el PDF o solo el enlace?", "Se guarda el archivo: el PDF, la foto o el documento quedan dentro de Linkalia en tu móvil, aunque después borres el chat."),
        ("¿Necesito crear una cuenta?", "No. Linkalia funciona sin registro y sin dar tu correo. Lo que guardas en colecciones privadas se queda en tu móvil."),
        ("¿Funciona con WhatsApp Business?", "Sí. Cualquier app que tenga el botón Compartir puede enviar enlaces y archivos a Linkalia.")],
"cta": "<strong>Que no se te vuelva a perder nada en el chat.</strong> Linkalia es gratis, sin registro y sin anuncios.",
},
"en": {
"path": "/en/save-whatsapp-links",
"title": "How to save WhatsApp links and PDFs so they don't get lost in the chat",
"h1": "How to save WhatsApp links and PDFs so they don't get lost in the chat",
"short": "Save WhatsApp links and PDFs before they get buried",
"summary": "The link or PDF you get today is buried tomorrow. How to get it out of the chat in two taps.",
"desc": "People send you links, places and PDFs on WhatsApp and two days later you can't find them. How to save them outside the chat, organised by topic, on Android.",
"lede": "Someone posts the hotel link, the timetable PDF or the video you “have to watch” in the group. Two days and three hundred messages later, it's gone. Scrolling up is not a system: here's how to get it out of the chat right away and have it at hand when you need it.",
"body": """
  <h2>Why everything gets lost on WhatsApp</h2>
  <p>WhatsApp is built for chatting, not for keeping things. The important stuff arrives mixed in with voice notes, memes and “ok 👍”, and every chat keeps its own pile. On top of that:</p>
  <ul>
    <li>Search only helps if you remember an exact word from the message.</li>
    <li><strong>Starred messages</strong> stay inside each chat and can't be sorted by topic.</li>
    <li>If you clear the chat or free up space, PDFs and photos can disappear.</li>
    <li>The “message myself” trick just becomes another endless chat.</li>
  </ul>

  <h2>The fix: save it outside the chat as soon as it arrives</h2>
  <p>The key is not leaving it for later. With an app for saving links and files, you send it from the chat itself to a named folder (“Lisbon trip”, “Kids' school”, “Work”) and forget about it.</p>
  <p>With <strong>Linkalia</strong> it takes these steps:</p>
  <ol>
    <li>In WhatsApp, <strong>long-press</strong> the message with the link, PDF or photo.</li>
    <li>Tap <strong>Share</strong> (the arrow icon at the top; if you don't see it, ⋮ › Share).</li>
    <li>Pick <strong>Linkalia</strong> from the list of apps.</li>
    <li>Choose the collection and tap <strong>“Save here”</strong>. The title and image appear on their own.</li>
  </ol>
  <p>You can select several photos or documents at once and save them in one go.</p>

  <h2>It sorts itself</h2>
  <p>Linkalia recognises what you send it and puts it in its category: a YouTube or TikTok video goes to <strong>Watch</strong>, a PDF or a train ticket to <strong>Documents</strong>, a Google Maps, Booking or Airbnb link to <strong>Places</strong>, a Spotify song to <strong>Listen</strong>. If you'd rather choose the category yourself each time, turn it off in Settings.</p>
  <p>Later you find it with search, which looks at the title, description, your notes, the file name and the website it came from. And anything you use often can be <strong>pinned to the top</strong>.</p>

  <div class="note"><p><strong>Is it meant for the whole group?</strong> Instead of forwarding messages, share the collection as a <em>Collaborative</em> one: everyone saves there and changes reach everyone straight away. See <a href="/en/plan-group-trip">how to plan a group trip</a>.</p></div>

  <h2>What if I use Telegram, Gmail or Chrome?</h2>
  <p>Same thing: any app with a <strong>Share</strong> button can send to Linkalia. WhatsApp is just the most common case.</p>
""",
"howto": {"name": "Save a WhatsApp link or PDF to Linkalia",
          "steps": ["Long-press the message with the link, PDF or photo.", "Tap Share.",
                    "Pick Linkalia from the list of apps.", "Choose the collection and tap “Save here”."]},
"faq": [("Does it save the PDF or just the link?", "It saves the file: the PDF, photo or document stays inside Linkalia on your phone, even if you later delete the chat."),
        ("Do I need to create an account?", "No. Linkalia works without signing up or giving your email. What you keep in private collections stays on your phone."),
        ("Does it work with WhatsApp Business?", "Yes. Any app with a Share button can send links and files to Linkalia.")],
"cta": "<strong>Never lose anything in a chat again.</strong> Linkalia is free, with no sign-up and no ads.",
},
},
# ───────────────────────────── 2. Guardados de redes ─────────────────────────────
{
"campaign": "social_saves",
"es": {
"path": "/organizar-guardados-instagram-tiktok-youtube",
"title": "Cómo organizar tus guardados de Instagram, TikTok y YouTube en un solo sitio",
"h1": "Cómo organizar tus guardados de Instagram, TikTok y YouTube en un solo sitio",
"short": "Tus guardados de Instagram, TikTok y YouTube, en un solo sitio",
"summary": "Cada red guarda lo suyo y nunca lo vuelves a ver. Cómo juntarlo todo y ordenarlo por temas.",
"desc": "Guardas posts en Instagram, vídeos en TikTok y en «Ver más tarde» de YouTube, y nunca los vuelves a abrir. Cómo juntarlos en un solo sitio y ordenarlos por temas en Android.",
"lede": "Un post de Instagram con ideas para el salón, un TikTok con un truco de Excel, un vídeo de YouTube para el finde. Los guardas para luego… y luego nunca llega, porque cada uno vive en una app distinta y en una lista sin orden. Así se juntan en un solo sitio.",
"body": """
  <h2>El problema de los «guardados» de cada red</h2>
  <ul>
    <li><strong>Están repartidos:</strong> Instagram tiene sus Guardados, TikTok sus Favoritos, YouTube «Ver más tarde». Para encontrar algo tienes que acordarte de dónde lo viste.</li>
    <li><strong>No se ordenan por temas</strong> que mezclen redes: no puedes tener «Ideas para el salón» con un post de Instagram, un TikTok y un vídeo de YouTube juntos.</li>
    <li><strong>Te quedas sin ellos</strong> si borran el post, si la cuenta pasa a privada o si dejas la red.</li>
    <li><strong>No se pueden compartir</strong> como lista con alguien que no use esa red.</li>
  </ul>

  <h2>Guárdalo con el botón Compartir, no con el de guardar</h2>
  <p>El cambio es pequeño: en lugar de tocar «Guardar» dentro de la red, tocas <strong>Compartir</strong> y lo mandas a tu app de enlaces. Así queda fuera de la red, con su título e imagen, en la colección que tú elijas.</p>
  <h3>En Instagram</h3>
  <p>Toca el <strong>avión de papel</strong> debajo del post o reel, desliza la fila de abajo hasta el final y elige <strong>Compartir</strong> (o «Compartir en…»). Elige Linkalia.</p>
  <h3>En TikTok</h3>
  <p>Toca la <strong>flecha de compartir</strong> a la derecha del vídeo, desliza la fila de apps hasta <strong>Más</strong> y elige Linkalia.</p>
  <h3>En YouTube</h3>
  <p>Toca <strong>Compartir</strong> debajo del vídeo (o en ⋮ › Compartir en un Short) y elige Linkalia.</p>
  <p>En Linkalia pulsa <strong>«Guardar aquí»</strong> en la colección que quieras. Los vídeos van solos a la categoría <strong>Ver</strong>; la música y los pódcast de Spotify, a <strong>Escuchar</strong>.</p>

  <h2>Ordénalo por lo que te importa, no por la red</h2>
  <p>Crea colecciones por tema —«Casa», «Recetas», «Ejercicio», «Ideas de regalo»— y dentro, las categorías que quieras. Un mismo tema puede tener un reel, un TikTok, un vídeo de YouTube, un PDF y una web, todo junto. Con el buscador lo encuentras por título, descripción, tus notas o el nombre de la web.</p>
  <div class="note"><p><strong>¿Guardas sobre todo recetas?</strong> Linkalia detecta los reels de cocina aunque no digan «receta». Lo contamos en <a href="/guardar-recetas-instagram-tiktok">cómo guardar recetas de Instagram y TikTok</a>.</p></div>

  <h2>Y compártelo con quien no tenga esa red</h2>
  <p>Una colección se puede compartir como <strong>Canal</strong> (los demás solo la ven) o como <strong>Colaborativa</strong> (todos añaden). Tu pareja no necesita TikTok para ver las ideas que habéis ido guardando: le llega el enlace o el código QR y lo ve todo en Linkalia.</p>
""",
"faq": [("¿Puedo pasar a Linkalia los guardados que ya tengo en Instagram?", "Instagram no permite exportarlos de golpe. Lo práctico es abrir tus Guardados y compartir a Linkalia los que quieras conservar; a partir de ahí, guarda lo nuevo directamente con Compartir."),
        ("¿Qué pasa si borran el post original?", "En Linkalia te queda el enlace con su título, imagen y tus notas, así que al menos sabrás qué era y de quién. El vídeo en sí está en la red y, si se borra, ya no se puede ver."),
        ("¿Linkalia es gratis?", "Sí, es gratis, sin registro y sin anuncios. Hay un plan Pro opcional para quien necesite más espacio o más colecciones compartidas.")],
"cta": "<strong>Todo lo que guardas en las redes, en un solo sitio.</strong> Descarga Linkalia gratis.",
},
"en": {
"path": "/en/organize-instagram-tiktok-youtube-saves",
"title": "How to organise your Instagram, TikTok and YouTube saves in one place",
"h1": "How to organise your Instagram, TikTok and YouTube saves in one place",
"short": "Your Instagram, TikTok and YouTube saves, in one place",
"summary": "Each network keeps its own list and you never look at it again. How to bring it all together by topic.",
"desc": "You save posts on Instagram, videos on TikTok and in YouTube's Watch Later, and never open them again. How to gather them in one place and organise them by topic on Android.",
"lede": "An Instagram post with living-room ideas, a TikTok with an Excel trick, a YouTube video for the weekend. You save them for later… and later never comes, because each one lives in a different app, in a list with no order. Here's how to bring them together.",
"body": """
  <h2>The problem with each network's “saved” list</h2>
  <ul>
    <li><strong>They're scattered:</strong> Instagram has Saved, TikTok has Favourites, YouTube has Watch Later. To find something you have to remember where you saw it.</li>
    <li><strong>You can't sort them by topic</strong> across networks: no “Living room ideas” with an Instagram post, a TikTok and a YouTube video side by side.</li>
    <li><strong>You lose them</strong> if the post is deleted, the account goes private or you leave the network.</li>
    <li><strong>You can't share them</strong> as a list with someone who doesn't use that network.</li>
  </ul>

  <h2>Save with the Share button, not the save button</h2>
  <p>It's a small change: instead of tapping “Save” inside the network, tap <strong>Share</strong> and send it to your link app. It's kept outside the network, with its title and image, in the collection you choose.</p>
  <h3>On Instagram</h3>
  <p>Tap the <strong>paper plane</strong> under the post or reel, swipe the bottom row to the end and pick <strong>Share</strong> (or “Share to…”). Choose Linkalia.</p>
  <h3>On TikTok</h3>
  <p>Tap the <strong>share arrow</strong> on the right of the video, swipe the row of apps to <strong>More</strong> and choose Linkalia.</p>
  <h3>On YouTube</h3>
  <p>Tap <strong>Share</strong> under the video (or ⋮ › Share on a Short) and choose Linkalia.</p>
  <p>In Linkalia, tap <strong>“Save here”</strong> in the collection you want. Videos go to the <strong>Watch</strong> category on their own; Spotify music and podcasts go to <strong>Listen</strong>.</p>

  <h2>Organise by what matters to you, not by network</h2>
  <p>Create collections by topic — “Home”, “Recipes”, “Workouts”, “Gift ideas” — with whatever categories you like inside. One topic can hold a reel, a TikTok, a YouTube video, a PDF and a web page, all together. Search finds them by title, description, your notes or the website name.</p>
  <div class="note"><p><strong>Mostly saving recipes?</strong> Linkalia spots cooking reels even when they don't say “recipe”. See <a href="/en/save-recipes-instagram-tiktok">how to save recipes from Instagram and TikTok</a>.</p></div>

  <h2>And share it with people who aren't on that network</h2>
  <p>A collection can be shared as a <strong>Channel</strong> (others can only view) or as a <strong>Collaborative</strong> one (everyone adds). Your partner doesn't need TikTok to see the ideas you've been saving: they get the link or QR code and see everything in Linkalia.</p>
""",
"faq": [("Can I move the saves I already have on Instagram to Linkalia?", "Instagram doesn't let you export them all at once. The practical way is to open your Saved list and share the ones you want to keep to Linkalia; from then on, save new things straight away with Share."),
        ("What happens if the original post is deleted?", "Linkalia keeps the link with its title, image and your notes, so at least you'll know what it was and who posted it. The video itself lives on the network and can't be watched once it's deleted."),
        ("Is Linkalia free?", "Yes, it's free, with no sign-up and no ads. There's an optional Pro plan for people who need more space or more shared collections.")],
"cta": "<strong>Everything you save on social media, in one place.</strong> Get Linkalia for free.",
},
},
# ───────────────────────────── 3. Recetas ─────────────────────────────
{
"campaign": "recipes",
"es": {
"path": "/guardar-recetas-instagram-tiktok",
"title": "Cómo guardar recetas de Instagram y TikTok (y encontrarlas cuando vas a cocinar)",
"h1": "Cómo guardar recetas de Instagram y TikTok y encontrarlas cuando vas a cocinar",
"short": "Guardar recetas de Instagram y TikTok y encontrarlas al cocinar",
"summary": "Tu recetario está repartido entre reels, TikToks y webs. Cómo juntarlo en uno que se ordena solo.",
"desc": "Guardas reels de recetas en Instagram y TikTok y cuando vas a cocinar no los encuentras. Cómo montar un recetario en el móvil que se ordena solo, con webs, vídeos y PDF.",
"lede": "Ves un reel de lasaña en diez minutos, le das a guardar y el sábado, con la sartén en la mano, no aparece entre cientos de guardados. Si tu recetario está repartido entre Instagram, TikTok, YouTube y capturas de pantalla, esta guía es para ti.",
"body": """
  <h2>Por qué las recetas guardadas no se encuentran</h2>
  <ul>
    <li>Los guardados de Instagram y TikTok mezclan recetas con todo lo demás y no se pueden buscar por ingrediente.</li>
    <li>Las recetas de webs acaban en marcadores del navegador o en pestañas abiertas.</li>
    <li>Las que te pasa tu madre por WhatsApp se pierden en el chat.</li>
    <li>Las capturas de pantalla se pierden en la galería entre fotos de todo tipo.</li>
  </ul>

  <h2>Un recetario en el móvil que se ordena solo</h2>
  <p>En Linkalia crea una colección y añádele una categoría llamada <strong>Recetas</strong> (o <strong>Cocina</strong>). A partir de ahí, cuando compartas un reel o un TikTok de cocina, Linkalia lee el título y la descripción y, si habla de una receta, <strong>lo coloca en Recetas solo</strong>, aunque el vídeo no diga la palabra «receta»: le basta con que aparezcan ingredientes o vocabulario de cocina.</p>
  <p>Las webs de recetas conocidas (Directo al Paladar, Recetas Gratis, Cookpad, Bon Viveur, Cookidoo, Thermorecetas…) también van directas a Recetas.</p>

  <h2>Cómo guardar cada receta</h2>
  <ol>
    <li>En Instagram, TikTok, YouTube o el navegador, toca <strong>Compartir</strong>.</li>
    <li>Elige <strong>Linkalia</strong>.</li>
    <li>Pulsa <strong>«Guardar aquí»</strong> en tu colección de cocina.</li>
  </ol>
  <p>Funciona también con la receta en PDF que te mandan por WhatsApp o con la foto de la receta de la abuela: se guardan como documentos en la misma colección.</p>

  <h2>Trucos para encontrarlas al cocinar</h2>
  <ul>
    <li><strong>Añade una nota</strong> con los ingredientes clave («pollo, curry, 30 min»). El buscador mira también tus notas, así que podrás buscar por ingrediente.</li>
    <li>Crea categorías propias: «Cenas rápidas», «Postres», «Para invitados», «Batch cooking».</li>
    <li><strong>Fija arriba</strong> las que repites cada semana.</li>
    <li>Funciona sin conexión: tu lista de recetas está aunque en la cocina no llegue bien el wifi. (Para ver el vídeo, eso sí, hace falta internet.)</li>
  </ul>

  <h2>Un recetario familiar compartido</h2>
  <p>Comparte la colección como <strong>Colaborativa</strong> y que cada uno añada sus recetas: tu pareja, tus hermanos o tus compañeros de piso. O como <strong>Canal</strong>, si eres tú quien publica y los demás solo miran.</p>
""",
"howto": {"name": "Montar un recetario que se ordena solo en Linkalia",
          "steps": ["Crea una colección y añade una categoría llamada Recetas.", "En Instagram, TikTok o el navegador toca Compartir y elige Linkalia.",
                    "Pulsa «Guardar aquí»: las recetas van solas a la categoría Recetas.", "Añade una nota con los ingredientes clave para buscarlas después."]},
"faq": [("¿Cómo sabe Linkalia que un reel es una receta?", "Lee el título y la descripción del enlace. Si aparece una palabra inequívoca como «receta» o «ingredientes», o dos términos de cocina distintos, lo coloca en Recetas. Solo lo hace con lo que tú no has movido a mano."),
        ("¿Se guarda el vídeo?", "Se guarda el enlace con su título, imagen y descripción. El vídeo se reproduce desde Instagram, TikTok o YouTube."),
        ("¿Puedo guardar recetas de webs?", "Sí. Desde el navegador toca Compartir y elige Linkalia; las webs de recetas más conocidas van directas a la categoría Recetas.")],
"cta": "<strong>Tu recetario, ordenado y a mano cuando vas a cocinar.</strong> Linkalia es gratis.",
},
"en": {
"path": "/en/save-recipes-instagram-tiktok",
"title": "How to save recipes from Instagram and TikTok (and find them when you cook)",
"h1": "How to save recipes from Instagram and TikTok and find them when you cook",
"short": "Save recipes from Instagram and TikTok and find them when you cook",
"summary": "Your recipe book is spread across reels, TikToks and websites. How to gather it into one that sorts itself.",
"desc": "You save recipe reels on Instagram and TikTok and can't find them when it's time to cook. How to build a recipe book on your phone that sorts itself, with websites, videos and PDFs.",
"lede": "You see a ten-minute lasagne reel, hit save, and on Saturday, pan in hand, it's nowhere among hundreds of saves. If your recipes are spread across Instagram, TikTok, YouTube and screenshots, this guide is for you.",
"body": """
  <h2>Why saved recipes are so hard to find</h2>
  <ul>
    <li>Instagram and TikTok saves mix recipes with everything else, and you can't search them by ingredient.</li>
    <li>Recipes from websites end up as browser bookmarks or open tabs.</li>
    <li>The ones family send you on WhatsApp get lost in the chat.</li>
    <li>Screenshots get lost in the gallery among every other photo.</li>
  </ul>

  <h2>A recipe book on your phone that sorts itself</h2>
  <p>In Linkalia, create a collection and add a category called <strong>Recipes</strong> (or <strong>Cooking</strong>). From then on, when you share a cooking reel or TikTok, Linkalia reads the title and description and, if it's about a recipe, <strong>puts it in Recipes on its own</strong> — even if the video never says “recipe”: ingredients or cooking words are enough.</p>
  <p>Well-known recipe sites (Allrecipes, NYT Cooking, Cookpad, Cookidoo…) also go straight to Recipes.</p>

  <h2>How to save each recipe</h2>
  <ol>
    <li>On Instagram, TikTok, YouTube or your browser, tap <strong>Share</strong>.</li>
    <li>Choose <strong>Linkalia</strong>.</li>
    <li>Tap <strong>“Save here”</strong> in your cooking collection.</li>
  </ol>
  <p>It also works with the recipe PDF someone sends you on WhatsApp or the photo of grandma's handwritten recipe: they're saved as documents in the same collection.</p>

  <h2>Tips to find them when you cook</h2>
  <ul>
    <li><strong>Add a note</strong> with the key ingredients (“chicken, curry, 30 min”). Search also looks at your notes, so you can search by ingredient.</li>
    <li>Make your own categories: “Quick dinners”, “Desserts”, “For guests”, “Batch cooking”.</li>
    <li><strong>Pin to the top</strong> the ones you make every week.</li>
    <li>It works offline: your recipe list is there even if the Wi-Fi is weak in the kitchen. (Playing the video still needs internet.)</li>
  </ul>

  <h2>A shared family recipe book</h2>
  <p>Share the collection as a <strong>Collaborative</strong> one and let everyone add their recipes: your partner, siblings or flatmates. Or as a <strong>Channel</strong>, if you're the one publishing and the rest just browse.</p>
""",
"howto": {"name": "Build a self-sorting recipe book in Linkalia",
          "steps": ["Create a collection and add a category called Recipes.", "On Instagram, TikTok or your browser tap Share and choose Linkalia.",
                    "Tap “Save here”: recipes go to the Recipes category on their own.", "Add a note with the key ingredients to search for them later."]},
"faq": [("How does Linkalia know a reel is a recipe?", "It reads the link's title and description. If there's a clear word like “recipe” or “ingredients”, or two different cooking terms, it files it under Recipes. It only does this for items you haven't moved by hand."),
        ("Is the video saved?", "The link is saved with its title, image and description. The video plays from Instagram, TikTok or YouTube."),
        ("Can I save recipes from websites?", "Yes. In your browser tap Share and choose Linkalia; the best-known recipe sites go straight to the Recipes category.")],
"cta": "<strong>Your recipes, organised and at hand when you cook.</strong> Linkalia is free.",
},
},
# ───────────────────────────── 4. Viaje en grupo ─────────────────────────────
{
"campaign": "group_trip",
"es": {
"path": "/organizar-viaje-en-grupo",
"title": "Cómo organizar un viaje en grupo sin perder enlaces, reservas ni billetes",
"h1": "Cómo organizar un viaje en grupo sin perder enlaces, reservas ni billetes",
"short": "Organizar un viaje en grupo sin perder reservas ni billetes",
"summary": "Alojamientos, restaurantes y billetes repartidos en un grupo de WhatsApp. Cómo tenerlo todo en un sitio compartido.",
"desc": "Alojamientos de Airbnb y Booking, restaurantes, sitios en Google Maps y billetes en PDF repartidos por el grupo de WhatsApp. Cómo reunirlo todo en una colección compartida.",
"lede": "Seis amigos, un viaje y un grupo de WhatsApp que echa humo: tres opciones de Airbnb, cinco restaurantes, el enlace del museo, los billetes de tren en PDF… Cuando hay que decidir o enseñar la reserva en el hotel, nadie encuentra nada. Así se organiza todo en un único sitio que veis y editáis todos.",
"body": """
  <h2>El caos de siempre</h2>
  <ul>
    <li>Las propuestas de alojamiento quedan enterradas entre mensajes.</li>
    <li>Cada uno guarda los sitios en su propia lista de Google Maps.</li>
    <li>Los billetes y las reservas están en el correo de quien los compró.</li>
    <li>El que se une tarde al grupo no ve nada de lo anterior.</li>
  </ul>

  <h2>Una colección Colaborativa para el viaje</h2>
  <p>En Linkalia una colección <strong>Colaborativa</strong> es una carpeta compartida en la que <strong>todos añaden y editan</strong>, y los cambios llegan a todos al momento. Así se monta:</p>
  <ol>
    <li>Crea una colección: «Lisboa — mayo».</li>
    <li>Toca su nombre para abrir <strong>Info de la colección</strong> y, en <strong>Acceso</strong>, elige <strong>Colaborativa</strong>.</li>
    <li>En el menú ⋮ de arriba, toca <strong>Compartir enlace de invitación</strong> y mándalo al grupo, o enseña el <strong>código QR</strong> si estáis juntos. Quien no tenga la app llega a la página para descargarla.</li>
  </ol>

  <h2>Cada cosa en su sitio, sin pensar</h2>
  <p>Cuando alguien comparte algo a la colección, Linkalia lo ordena solo:</p>
  <ul>
    <li>Enlaces de <strong>Google Maps, Booking, Airbnb, TripAdvisor o TheFork</strong> → <strong>Lugares</strong>.</li>
    <li>Billetes de <strong>Renfe, Iberia, Vueling, Ryanair o ALSA</strong>, entradas y PDF → <strong>Documentos</strong>.</li>
    <li>Vídeos de YouTube o TikTok con ideas de qué ver → <strong>Ver</strong>.</li>
  </ul>
  <p>Podéis crear más categorías («Alojamiento», «Comer», «Día 1», «Día 2») y <strong>fijar arriba</strong> lo imprescindible: la reserva del hotel y los billetes de vuelta.</p>

  <h2>Durante el viaje</h2>
  <ul>
    <li>Activa <strong>Descargar documentos automáticamente</strong> en la colección: los billetes y reservas se bajan al móvil de cada uno y <strong>se abren sin conexión</strong>, en el avión o en un sitio sin cobertura.</li>
    <li>El buscador encuentra «museo» o «cena viernes» al momento, en vez de hacer scroll en el chat.</li>
    <li>Si alguien borra algo por error, hay <strong>papelera</strong> y deshacer.</li>
  </ul>

  <div class="note"><p><strong>Y a la vuelta</strong>, la colección queda como recuerdo con todos los sitios a los que fuisteis. Si algún día alguien te pide recomendaciones de Lisboa, se la compartes.</p></div>
""",
"howto": {"name": "Organizar un viaje en grupo con una colección Colaborativa de Linkalia",
          "steps": ["Crea una colección con el nombre del viaje.", "Toca su nombre y, en Acceso, elige Colaborativa.",
                    "Comparte el enlace de invitación o el código QR con el grupo.", "Cada uno guarda en ella alojamientos, sitios y billetes con el botón Compartir."]},
"faq": [("¿Todos necesitan tener la app?", "Para añadir y editar, sí: cada persona entra con el enlace de invitación o el QR y, si no tiene Linkalia, llega a la página para descargarla gratis."),
        ("¿Cuántas personas pueden unirse?", "El plan gratuito permite un grupo pequeño en cada Colaborativa; con Pro caben más personas y más colecciones compartidas."),
        ("¿Se pueden ver los billetes sin internet?", "Sí, una vez descargados. Con «Descargar documentos automáticamente» activado en la colección, se bajan solos al móvil y se abren sin conexión.")],
"cta": "<strong>El viaje, organizado en un solo sitio para todo el grupo.</strong> Descarga Linkalia gratis.",
},
"en": {
"path": "/en/plan-group-trip",
"title": "How to plan a group trip without losing links, bookings or tickets",
"h1": "How to plan a group trip without losing links, bookings or tickets",
"short": "Plan a group trip without losing bookings or tickets",
"summary": "Stays, restaurants and tickets scattered across a WhatsApp group. How to keep it all in one shared place.",
"desc": "Airbnb and Booking stays, restaurants, Google Maps places and PDF tickets scattered across the group chat. How to gather them in one shared collection.",
"lede": "Six friends, one trip and a group chat on fire: three Airbnb options, five restaurants, the museum link, the train tickets as PDFs… When it's time to decide or show the booking at the hotel, nobody can find anything. Here's how to keep it all in one place everyone can see and edit.",
"body": """
  <h2>The usual mess</h2>
  <ul>
    <li>Accommodation options get buried between messages.</li>
    <li>Everyone keeps places in their own Google Maps list.</li>
    <li>Tickets and bookings sit in the inbox of whoever paid.</li>
    <li>Whoever joins the group late can't see any of it.</li>
  </ul>

  <h2>A Collaborative collection for the trip</h2>
  <p>In Linkalia a <strong>Collaborative</strong> collection is a shared folder where <strong>everyone adds and edits</strong>, and changes reach everyone straight away. Here's how to set it up:</p>
  <ol>
    <li>Create a collection: “Lisbon — May”.</li>
    <li>Tap its name to open <strong>Collection info</strong> and, under <strong>Access</strong>, pick <strong>Collaborative</strong>.</li>
    <li>In the ⋮ menu at the top, tap <strong>Share invite link</strong> and send it to the group, or show the <strong>QR code</strong> if you're together. Anyone without the app lands on the page to download it.</li>
  </ol>

  <h2>Everything in its place, automatically</h2>
  <p>When someone shares something to the collection, Linkalia sorts it:</p>
  <ul>
    <li><strong>Google Maps, Booking, Airbnb, Tripadvisor or TheFork</strong> links → <strong>Places</strong>.</li>
    <li>Airline and train tickets, event tickets and PDFs → <strong>Documents</strong>.</li>
    <li>YouTube or TikTok videos with things to see → <strong>Watch</strong>.</li>
  </ul>
  <p>You can add more categories (“Stay”, “Food”, “Day 1”, “Day 2”) and <strong>pin to the top</strong> what matters most: the hotel booking and the return tickets.</p>

  <h2>During the trip</h2>
  <ul>
    <li>Turn on <strong>Download documents automatically</strong> in the collection: tickets and bookings are saved to everyone's phone and <strong>open offline</strong>, on the plane or somewhere without signal.</li>
    <li>Search finds “museum” or “Friday dinner” instantly, instead of scrolling the chat.</li>
    <li>If someone deletes something by mistake, there's a <strong>trash</strong> and undo.</li>
  </ul>

  <div class="note"><p><strong>And when you're back</strong>, the collection stays as a keepsake with every place you went to. If someone ever asks you for Lisbon tips, just share it.</p></div>
""",
"howto": {"name": "Plan a group trip with a Linkalia Collaborative collection",
          "steps": ["Create a collection named after the trip.", "Tap its name and, under Access, pick Collaborative.",
                    "Share the invite link or QR code with the group.", "Everyone saves stays, places and tickets to it with the Share button."]},
"faq": [("Does everyone need the app?", "To add and edit, yes: each person joins with the invite link or QR code and, if they don't have Linkalia, lands on the page to download it for free."),
        ("How many people can join?", "The free plan allows a small group in each Collaborative collection; Pro allows more people and more shared collections."),
        ("Can I see tickets without internet?", "Yes, once downloaded. With “Download documents automatically” turned on in the collection, they're saved to your phone and open offline.")],
"cta": "<strong>The whole trip, organised in one place for the whole group.</strong> Get Linkalia for free.",
},
},
# ───────────────────────────── 5. Material para alumnos o clientes ─────────────────────────────
{
"campaign": "channel",
"es": {
"path": "/compartir-material-alumnos-clientes",
"title": "Cómo compartir enlaces y documentos con alumnos o clientes sin que se pierdan",
"h1": "Cómo compartir enlaces y documentos con alumnos o clientes sin que se pierdan",
"short": "Compartir material con alumnos o clientes sin que se pierda",
"summary": "Profesores, entrenadores, academias o inmobiliarias: un único enlace con todo el material, siempre al día.",
"desc": "Profesores, academias, entrenadores o inmobiliarias: cómo dar a tus alumnos o clientes un único enlace con todos tus vídeos, PDF y enlaces, siempre actualizado y fácil de consultar.",
"lede": "Mandas el temario por WhatsApp, el vídeo por correo, el PDF actualizado otra vez por WhatsApp… y aun así te preguntan «¿dónde estaba lo de la semana pasada?». Si das clase, entrenas a un grupo o enseñas viviendas a clientes, un único sitio con todo tu material te ahorra esas preguntas.",
"body": """
  <h2>Lo que falla al mandar el material suelto</h2>
  <ul>
    <li>Cada archivo llega por un canal distinto y se pierde entre mensajes.</li>
    <li>Cuando actualizas un PDF, conviven la versión vieja y la nueva.</li>
    <li>El que entra a mitad de curso no tiene lo anterior.</li>
    <li>Las carpetas de Drive piden cuenta, permisos y no se ven bien en el móvil.</li>
  </ul>

  <h2>Un Canal: tú publicas, ellos lo tienen siempre al día</h2>
  <p>En Linkalia, una colección compartida como <strong>Canal</strong> funciona así: <strong>solo tú editas</strong> y quienes la siguen la ven en su móvil, ordenada por categorías y siempre actualizada. Cada vez que añades algo, les llega al momento.</p>
  <p>Algunos ejemplos que vienen en la propia app:</p>
  <ul>
    <li><strong>Academia u oposiciones:</strong> temario en PDF, vídeos explicativos y exámenes de otros años por temas.</li>
    <li><strong>Autoescuela:</strong> test, vídeos de maniobras y documentos para el examen teórico.</li>
    <li><strong>Entrenador o club de running:</strong> planes de entrenamiento, rutas de Strava o Wikiloc y vídeos de técnica.</li>
    <li><strong>Inmobiliaria:</strong> fichas de pisos, fotos, planos y la ubicación en Maps para cada cliente.</li>
    <li><strong>Curso online:</strong> lecciones, lecturas y recursos de cada módulo.</li>
  </ul>

  <h2>Cómo crear tu Canal</h2>
  <ol>
    <li>Crea una colección y organiza las categorías («Tema 1», «Vídeos», «Exámenes»).</li>
    <li>Añade el material desde cualquier app con <strong>Compartir</strong>: PDF, vídeos de YouTube, documentos de Word, fotos, enlaces.</li>
    <li>Toca su nombre para abrir <strong>Info de la colección</strong> y, en <strong>Acceso</strong>, elige <strong>Canal</strong>.</li>
    <li>En el menú ⋮, toca <strong>Compartir enlace de invitación</strong>: manda el enlace o proyecta el <strong>código QR</strong> en clase. Quien no tenga la app llega a la página para descargarla.</li>
  </ol>
  <p>Tú decides quién sigue el Canal: puedes ver la lista de seguidores y quitar a quien ya no deba tener acceso.</p>

  <h2>¿Y quien no quiere instalar nada?</h2>
  <p>Con <strong>Pro</strong> puedes exportar una colección entera como <strong>página web</strong> (HTML), que se abre en cualquier navegador, con buscador incluido. En el plan gratuito puedes exportar así categorías sueltas de tus colecciones privadas.</p>

  <div class="note"><p><strong>Consejo:</strong> fija arriba lo que necesitan esta semana. Así, al abrir el Canal, lo primero que ven es lo importante.</p></div>
""",
"howto": {"name": "Crear un Canal de Linkalia para alumnos o clientes",
          "steps": ["Crea una colección y organiza las categorías.", "Añade el material con el botón Compartir desde cualquier app.",
                    "Toca su nombre y, en Acceso, elige Canal.", "Comparte el enlace o el código QR con tus alumnos o clientes."]},
"faq": [("¿Mis alumnos pueden modificar el material?", "No. En un Canal solo edita el propietario; los seguidores solo ven. Si quieres que todos añadan, usa una colección Colaborativa."),
        ("¿Cuántos seguidores puede tener un Canal?", "El plan gratuito admite un grupo reducido de seguidores por Canal; con Pro caben muchos más, con más espacio para documentos."),
        ("¿Necesitan crear una cuenta?", "No. Instalan Linkalia, abren tu enlace o escanean el QR y ya lo ven. Sin registro ni correo.")],
"cta": "<strong>Todo tu material en un solo enlace, siempre al día.</strong> Crea tu Canal gratis con Linkalia.",
},
"en": {
"path": "/en/share-material-students-clients",
"title": "How to share links and documents with students or clients without them getting lost",
"h1": "How to share links and documents with students or clients without them getting lost",
"short": "Share material with students or clients without it getting lost",
"summary": "Teachers, coaches, academies or estate agents: one link with all your material, always up to date.",
"desc": "Teachers, academies, coaches or estate agents: how to give your students or clients a single link with all your videos, PDFs and links, always up to date and easy to browse.",
"lede": "You send the syllabus on WhatsApp, the video by email, the updated PDF on WhatsApp again… and people still ask “where was last week's thing?”. If you teach, coach a group or show homes to clients, one place with all your material saves you those questions.",
"body": """
  <h2>What goes wrong when you send material piecemeal</h2>
  <ul>
    <li>Each file arrives through a different channel and gets lost between messages.</li>
    <li>When you update a PDF, the old and new versions live side by side.</li>
    <li>Whoever joins mid-course doesn't have what came before.</li>
    <li>Drive folders ask for accounts and permissions and aren't great on a phone.</li>
  </ul>

  <h2>A Channel: you publish, they're always up to date</h2>
  <p>In Linkalia, a collection shared as a <strong>Channel</strong> works like this: <strong>only you edit</strong>, and followers see it on their phone, sorted into categories and always current. Whenever you add something, it reaches them straight away.</p>
  <p>Some examples that come with the app:</p>
  <ul>
    <li><strong>Academy or exam prep:</strong> PDF notes, explainer videos and past papers by topic.</li>
    <li><strong>Driving school:</strong> practice tests, manoeuvre videos and documents for the theory test.</li>
    <li><strong>Coach or running club:</strong> training plans, Strava or AllTrails routes and technique videos.</li>
    <li><strong>Estate agent:</strong> property sheets, photos, floor plans and the Maps location for each client.</li>
    <li><strong>Online course:</strong> lessons, readings and resources for each module.</li>
  </ul>

  <h2>How to create your Channel</h2>
  <ol>
    <li>Create a collection and set up categories (“Unit 1”, “Videos”, “Past papers”).</li>
    <li>Add material from any app with <strong>Share</strong>: PDFs, YouTube videos, Word documents, photos, links.</li>
    <li>Tap its name to open <strong>Collection info</strong> and, under <strong>Access</strong>, pick <strong>Channel</strong>.</li>
    <li>In the ⋮ menu, tap <strong>Share invite link</strong>: send the link or put the <strong>QR code</strong> on the screen in class. Anyone without the app lands on the page to download it.</li>
  </ol>
  <p>You decide who follows the Channel: you can see the list of followers and remove anyone who should no longer have access.</p>

  <h2>What about people who don't want to install anything?</h2>
  <p>With <strong>Pro</strong> you can export a whole collection as a <strong>web page</strong> (HTML) that opens in any browser, search included. On the free plan you can export single categories of your private collections that way.</p>

  <div class="note"><p><strong>Tip:</strong> pin this week's material to the top. That way, the first thing they see when they open the Channel is what matters.</p></div>
""",
"howto": {"name": "Create a Linkalia Channel for students or clients",
          "steps": ["Create a collection and set up categories.", "Add material with the Share button from any app.",
                    "Tap its name and, under Access, pick Channel.", "Share the link or QR code with your students or clients."]},
"faq": [("Can my students change the material?", "No. In a Channel only the owner edits; followers can only view. If you want everyone to add things, use a Collaborative collection."),
        ("How many followers can a Channel have?", "The free plan allows a small group of followers per Channel; Pro allows many more, with more space for documents."),
        ("Do they need to create an account?", "No. They install Linkalia, open your link or scan the QR code, and they're in. No sign-up, no email.")],
"cta": "<strong>All your material in one link, always up to date.</strong> Create your Channel for free with Linkalia.",
},
},
# ───────────────────────────── 6. Marcadores ─────────────────────────────
{
"campaign": "bookmarks",
"es": {
"path": "/pasar-marcadores-chrome-al-movil",
"title": "Cómo pasar tus marcadores de Chrome al móvil y tenerlos por fin ordenados",
"h1": "Cómo pasar tus marcadores de Chrome al móvil y tenerlos por fin ordenados",
"short": "Pasar tus marcadores de Chrome al móvil, ordenados",
"summary": "Años de marcadores en el ordenador que nunca usas en el móvil. Cómo importarlos con sus carpetas.",
"desc": "Tienes cientos de marcadores en Chrome, Edge o Firefox que en el móvil no usas. Cómo exportarlos e importarlos en Android con sus carpetas como categorías, sin cuenta de Google.",
"lede": "Años guardando marcadores en el ordenador: la web del banco, tutoriales, tiendas, recetas, artículos para leer «cuando tenga tiempo». En el móvil, donde pasas la mayor parte del día, no los usas porque están enterrados en un menú del navegador. Así se pasan al móvil con su orden.",
"body": """
  <h2>Por qué los marcadores no funcionan en el móvil</h2>
  <ul>
    <li>En el navegador del móvil los marcadores están escondidos en un menú y son incómodos de recorrer.</li>
    <li>Sincronizarlos obliga a iniciar sesión con la misma cuenta en todos los navegadores.</li>
    <li>Solo guardan enlaces: el PDF o el vídeo relacionados están en otro sitio.</li>
    <li>Con los años se acumulan carpetas sin orden y enlaces que ya no funcionan.</li>
  </ul>

  <h2>Paso 1: exporta los marcadores en el ordenador</h2>
  <h3>Chrome</h3>
  <ol>
    <li>Pulsa <strong>Ctrl + Mayús + O</strong> para abrir el Gestor de marcadores.</li>
    <li>Pulsa <strong>⋮</strong> (arriba a la derecha) › <strong>Exportar marcadores</strong>. Se guarda un archivo <code>.html</code>.</li>
  </ol>
  <h3>Edge, Firefox o Safari</h3>
  <p>Todos tienen la opción en su gestor de marcadores: en Edge, «Exportar favoritos»; en Firefox, Biblioteca › Importar y respaldar › «Exportar marcadores a HTML»; en Safari, Archivo › «Exportar marcadores». En todos sale el mismo tipo de archivo <code>.html</code>.</p>

  <h2>Paso 2: pásalo al móvil</h2>
  <p>Envíatelo como prefieras: por correo, por Drive o por WhatsApp. Basta con que el archivo llegue al móvil.</p>

  <h2>Paso 3: impórtalo en Linkalia</h2>
  <ol>
    <li>En Linkalia, crea una colección nueva y elige <strong>Importar marcadores del navegador</strong>.</li>
    <li>Elige el archivo <code>.html</code>.</li>
    <li>Listo: <strong>cada carpeta de marcadores se convierte en una categoría</strong>, con sus enlaces dentro.</li>
  </ol>
  <p>No hace falta cuenta de Google ni de nada: el archivo se lee en el móvil y los marcadores se quedan en tu móvil.</p>

  <h2>Paso 4: aprovecha para ordenarlos</h2>
  <ul>
    <li>Mueve a <strong>papelera</strong> lo que ya no sirve (se puede deshacer).</li>
    <li><strong>Fija arriba</strong> los que usas a diario.</li>
    <li>Junta en la misma colección los enlaces con sus PDF, vídeos y documentos.</li>
    <li>Usa el buscador: encuentra por título, nota o dominio.</li>
  </ul>

  <div class="note"><p><strong>Límite del plan gratuito:</strong> las colecciones privadas admiten 200 elementos en total. Si tu archivo trae más, Linkalia importa hasta ese número y te avisa; con Pro no hay límite.</p></div>
""",
"howto": {"name": "Importar los marcadores de Chrome en Linkalia",
          "steps": ["En Chrome pulsa Ctrl + Mayús + O para abrir el Gestor de marcadores.", "Pulsa ⋮ › Exportar marcadores para guardar un archivo .html.",
                    "Pasa el archivo al móvil por correo, Drive o WhatsApp.", "En Linkalia crea una colección y elige Importar marcadores del navegador."]},
"faq": [("¿Se mantienen las carpetas?", "Sí. Cada carpeta de marcadores se convierte en una categoría de la colección, con sus enlaces dentro."),
        ("¿Funciona con Edge, Firefox y Safari?", "Sí. Todos exportan los marcadores al mismo formato .html, que Linkalia sabe importar."),
        ("¿Se sincroniza con el navegador después?", "No: es una importación. A partir de ahí, guarda lo nuevo en Linkalia con el botón Compartir del navegador del móvil.")],
"cta": "<strong>Tus marcadores, en el móvil y ordenados.</strong> Descarga Linkalia gratis e impórtalos en un minuto.",
},
"en": {
"path": "/en/chrome-bookmarks-to-android",
"title": "How to move your Chrome bookmarks to your Android phone and finally organise them",
"h1": "How to move your Chrome bookmarks to your phone and finally organise them",
"short": "Move your Chrome bookmarks to your phone, organised",
"summary": "Years of bookmarks on your computer you never use on your phone. How to import them with their folders.",
"desc": "You have hundreds of bookmarks in Chrome, Edge or Firefox you never use on your phone. How to export them and import them on Android with their folders as categories, no Google account needed.",
"lede": "Years of saving bookmarks on your computer: the bank's website, tutorials, shops, recipes, articles to read “when I have time”. On your phone, where you spend most of the day, you don't use them because they're buried in a browser menu. Here's how to move them to your phone, in order.",
"body": """
  <h2>Why bookmarks don't work on a phone</h2>
  <ul>
    <li>In a mobile browser, bookmarks are hidden in a menu and awkward to browse.</li>
    <li>Syncing them means signing in with the same account in every browser.</li>
    <li>They only store links: the related PDF or video lives somewhere else.</li>
    <li>Over the years, folders pile up with no order and links that no longer work.</li>
  </ul>

  <h2>Step 1: export your bookmarks on the computer</h2>
  <h3>Chrome</h3>
  <ol>
    <li>Press <strong>Ctrl + Shift + O</strong> to open the Bookmark manager.</li>
    <li>Click <strong>⋮</strong> (top right) › <strong>Export bookmarks</strong>. A <code>.html</code> file is saved.</li>
  </ol>
  <h3>Edge, Firefox or Safari</h3>
  <p>They all have the option in their bookmark manager: in Edge, “Export favorites”; in Firefox, Library › Import and Backup › “Export Bookmarks to HTML”; in Safari, File › “Export Bookmarks”. They all produce the same kind of <code>.html</code> file.</p>

  <h2>Step 2: get it onto your phone</h2>
  <p>Send it however you like: by email, Drive or WhatsApp. The file just needs to reach your phone.</p>

  <h2>Step 3: import it into Linkalia</h2>
  <ol>
    <li>In Linkalia, create a new collection and choose <strong>Import browser bookmarks</strong>.</li>
    <li>Pick the <code>.html</code> file.</li>
    <li>Done: <strong>each bookmark folder becomes a category</strong>, with its links inside.</li>
  </ol>
  <p>No Google account or any other account needed: the file is read on your phone and the bookmarks stay on your phone.</p>

  <h2>Step 4: use the chance to tidy up</h2>
  <ul>
    <li>Move what's no longer useful to the <strong>trash</strong> (you can undo).</li>
    <li><strong>Pin to the top</strong> the ones you use every day.</li>
    <li>Keep links together with their PDFs, videos and documents in the same collection.</li>
    <li>Use search: it finds by title, note or domain.</li>
  </ul>

  <div class="note"><p><strong>Free plan limit:</strong> private collections hold 200 items in total. If your file has more, Linkalia imports up to that number and tells you; with Pro there's no limit.</p></div>
""",
"howto": {"name": "Import Chrome bookmarks into Linkalia",
          "steps": ["In Chrome press Ctrl + Shift + O to open the Bookmark manager.", "Click ⋮ › Export bookmarks to save a .html file.",
                    "Send the file to your phone by email, Drive or WhatsApp.", "In Linkalia create a collection and choose Import browser bookmarks."]},
"faq": [("Are the folders kept?", "Yes. Each bookmark folder becomes a category in the collection, with its links inside."),
        ("Does it work with Edge, Firefox and Safari?", "Yes. They all export bookmarks to the same .html format, which Linkalia can import."),
        ("Does it stay in sync with the browser afterwards?", "No, it's a one-off import. From then on, save new things to Linkalia with your mobile browser's Share button.")],
"cta": "<strong>Your bookmarks, on your phone and organised.</strong> Get Linkalia for free and import them in a minute.",
},
},
# ───────────────────────────── 7. Documentos importantes ─────────────────────────────
{
"campaign": "documents",
"es": {
"path": "/guardar-documentos-importantes-movil",
"title": "Dónde guardar los documentos importantes en el móvil: a mano, ordenados y sin conexión",
"h1": "Dónde guardar los documentos importantes en el móvil para tenerlos siempre a mano",
"short": "Documentos importantes en el móvil, ordenados y sin conexión",
"summary": "La póliza del seguro, la tarjeta sanitaria o el contrato, cuando los necesitas y sin cobertura.",
"desc": "Póliza del seguro, tarjeta sanitaria, contrato de alquiler, garantías o el informe médico: cómo tenerlos ordenados en el móvil, sin conexión, sin cuenta y con copia de seguridad.",
"lede": "En urgencias te piden el informe anterior; en el taller, la póliza del seguro; en el aeropuerto, la tarjeta de embarque; en la tienda, la garantía. Están en algún correo, en una foto de la galería o en una carpeta de Descargas con nombres como «doc_2024 (3).pdf». Así se tienen ordenados y a mano.",
"body": """
  <h2>Dónde suelen acabar (y por qué falla)</h2>
  <ul>
    <li><strong>En la galería:</strong> la foto del DNI o del ticket se mezcla con miles de fotos.</li>
    <li><strong>En el correo:</strong> hay que acordarse de quién lo mandó y buscar con cobertura.</li>
    <li><strong>En Descargas:</strong> nombres imposibles y sin carpetas.</li>
    <li><strong>En la nube:</strong> sin conexión no se abre, y no a todo el mundo le gusta subir ahí papeles personales.</li>
  </ul>

  <h2>Una colección privada para tus papeles</h2>
  <p>En Linkalia las colecciones <strong>privadas</strong> se guardan <strong>solo en tu móvil</strong>: no hace falta cuenta, no se suben a ningún servidor y se abren <strong>sin conexión</strong>. Monta una así:</p>
  <ol>
    <li>Crea una colección «Papeles» y las categorías que te encajen: «Salud», «Coche», «Casa», «Seguros», «Garantías», «Viajes».</li>
    <li>Guarda cada documento con <strong>Compartir</strong> desde donde esté: el adjunto del correo, el PDF de WhatsApp, el archivo de Descargas o una foto de la galería.</li>
    <li>Añade una <strong>nota</strong> con lo que te pedirán: número de póliza, fecha de caducidad, teléfono de asistencia.</li>
  </ol>
  <p>Admite PDF, fotos, documentos de Word, hojas de cálculo y más. Y el buscador encuentra por nombre de archivo y por tus notas, así que «póliza» o «ITV» lo saca al momento.</p>

  <h2>Que no se pierdan si cambias de móvil</h2>
  <ul>
    <li><strong>Copia automática en una carpeta</strong> del móvil o de tu almacenamiento, gratis.</li>
    <li><strong>Copia en la nube</strong> diaria, con Pro, para recuperarlo todo en un móvil nuevo.</li>
    <li><strong>Papelera</strong> por si borras algo sin querer.</li>
  </ul>

  <h2>Y cuando tengas que compartirlo</h2>
  <p>Si tu pareja también necesita los papeles de casa o del coche, puedes hacer de esa colección (o de otra con solo esos documentos) una <strong>Colaborativa</strong> y la tendréis los dos. Lo privado sigue siendo privado: tú decides qué se comparte y con quién.</p>

  <div class="note"><p><strong>Seguridad:</strong> lo que guardas en una colección privada está protegido por el bloqueo de pantalla de tu móvil. Si guardas documentos sensibles, asegúrate de tener un PIN, patrón o huella activados.</p></div>
""",
"howto": {"name": "Guardar documentos importantes en una colección privada de Linkalia",
          "steps": ["Crea una colección privada con categorías como Salud, Coche, Casa o Seguros.", "Guarda cada documento con el botón Compartir desde el correo, WhatsApp o Descargas.",
                    "Añade una nota con el número de póliza o la fecha de caducidad.", "Activa la copia automática en Ajustes."]},
"faq": [("¿Mis documentos se suben a internet?", "No, si están en una colección privada: se guardan solo en tu móvil. Solo se suben si activas la copia en la nube (Pro) o si compartes esa colección."),
        ("¿Puedo abrirlos sin cobertura?", "Sí. Las colecciones privadas funcionan sin conexión."),
        ("¿Qué pasa si cambio de móvil?", "Con la copia automática en una carpeta puedes importarla en el móvil nuevo; con Pro, la copia en la nube te deja recuperarlo todo directamente.")],
"cta": "<strong>Tus papeles importantes, ordenados y a mano aunque no haya cobertura.</strong> Descarga Linkalia gratis.",
},
"en": {
"path": "/en/store-important-documents-phone",
"title": "Where to keep important documents on your phone: at hand, organised and offline",
"h1": "Where to keep important documents on your phone so they're always at hand",
"short": "Important documents on your phone, organised and offline",
"summary": "Your insurance policy, health card or lease, right when you need them, even without signal.",
"desc": "Insurance policy, health card, lease, warranties or medical reports: how to keep them organised on your phone, offline, with no account and with a backup.",
"lede": "At A&amp;E they ask for your last report; at the garage, your insurance policy; at the airport, your boarding pass; at the shop, the warranty. They're in some email, a photo in your gallery or a Downloads folder full of names like “doc_2024 (3).pdf”. Here's how to keep them organised and at hand.",
"body": """
  <h2>Where they usually end up (and why it fails)</h2>
  <ul>
    <li><strong>In the gallery:</strong> the photo of your ID or receipt is mixed in with thousands of photos.</li>
    <li><strong>In email:</strong> you have to remember who sent it and search with signal.</li>
    <li><strong>In Downloads:</strong> impossible names and no folders.</li>
    <li><strong>In the cloud:</strong> it won't open offline, and not everyone likes uploading personal papers there.</li>
  </ul>

  <h2>A private collection for your paperwork</h2>
  <p>In Linkalia, <strong>private</strong> collections are stored <strong>only on your phone</strong>: no account needed, nothing uploaded to any server, and they open <strong>offline</strong>. Set one up like this:</p>
  <ol>
    <li>Create a “Paperwork” collection and the categories that suit you: “Health”, “Car”, “Home”, “Insurance”, “Warranties”, “Travel”.</li>
    <li>Save each document with <strong>Share</strong> from wherever it is: the email attachment, the WhatsApp PDF, the file in Downloads or a photo in your gallery.</li>
    <li>Add a <strong>note</strong> with what you'll be asked for: policy number, expiry date, helpline number.</li>
  </ol>
  <p>It takes PDFs, photos, Word documents, spreadsheets and more. Search finds by file name and by your notes, so “policy” or “MOT” brings it up instantly.</p>

  <h2>Don't lose them when you change phones</h2>
  <ul>
    <li><strong>Automatic backup to a folder</strong> on your phone or storage, free.</li>
    <li>Daily <strong>cloud backup</strong>, with Pro, to restore everything on a new phone.</li>
    <li>A <strong>trash</strong> in case you delete something by mistake.</li>
  </ul>

  <h2>And when you need to share them</h2>
  <p>If your partner also needs the house or car papers, you can make that collection (or another with just those documents) a <strong>Collaborative</strong> one and you'll both have it. Private stays private: you decide what's shared and with whom.</p>

  <div class="note"><p><strong>Security:</strong> what you keep in a private collection is protected by your phone's screen lock. If you store sensitive documents, make sure you have a PIN, pattern or fingerprint set up.</p></div>
""",
"howto": {"name": "Keep important documents in a private Linkalia collection",
          "steps": ["Create a private collection with categories such as Health, Car, Home or Insurance.", "Save each document with the Share button from email, WhatsApp or Downloads.",
                    "Add a note with the policy number or expiry date.", "Turn on automatic backup in Settings."]},
"faq": [("Are my documents uploaded to the internet?", "Not if they're in a private collection: they're stored only on your phone. They're only uploaded if you turn on cloud backup (Pro) or share that collection."),
        ("Can I open them without signal?", "Yes. Private collections work offline."),
        ("What happens if I change phones?", "With the automatic folder backup you can import it on the new phone; with Pro, the cloud backup lets you restore everything directly.")],
"cta": "<strong>Your important papers, organised and at hand even without signal.</strong> Get Linkalia for free.",
},
},
]
