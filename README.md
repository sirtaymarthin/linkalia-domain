# Linkalia

**Organizador de enlaces y archivos para Android** · **Link and file organizer for Android**

🌐 Web / Website: **https://linkalia.org** · 🇬🇧 English: **https://linkalia.org/en/**

📥 Descarga directa (APK) / Direct download (APK): [linkalia_v2_0_1.apk](https://github.com/sirtaymarthin/linkalia-domain/releases/download/v2.0.1/linkalia_v2_0_1.apk)

---

## Español

Linkalia organiza tus enlaces y archivos por categorías, los clasifica solo y te deja compartir colecciones enteras con quien quieras. Una librería personal que no se pierde entre pestañas.

- Categorías automáticas
- Colecciones colaborativas
- Exportación a HTML
- Gratis

### Instalación

1. Descarga el APK desde [la última versión](https://github.com/sirtaymarthin/linkalia-domain/releases/latest) o desde [linkalia.org](https://linkalia.org).
2. Ábrelo en tu móvil Android y permite la instalación desde esta fuente si te lo pide.

> Android puede avisar de "archivo dañino" o "fuente desconocida" simplemente porque el APK no viene de Google Play. Es un aviso genérico del sistema.

### Contacto

info@linkalia.org

---

## English

Linkalia organizes your links and files into categories, sorts them on its own, and lets you share whole collections with anyone. A personal library that never gets lost between tabs.

- Automatic categories
- Collaborative collections
- HTML export
- Free

### Installation

1. Download the APK from [the latest release](https://github.com/sirtaymarthin/linkalia-domain/releases/latest) or from [linkalia.org/en](https://linkalia.org/en/).
2. Open it on your Android phone and allow installation from this source if prompted.

> Android may warn about a "harmful file" or "unknown source" simply because the APK is not from Google Play. It is a generic system warning.

### Contact

info@linkalia.org

---

## Sitio web / Website (este repositorio / this repository)

Este repositorio contiene la web estática de [linkalia.org](https://linkalia.org) y aloja las versiones del APK en [Releases](https://github.com/sirtaymarthin/linkalia-domain/releases).

This repository contains the static website for [linkalia.org](https://linkalia.org) and hosts the APK builds under [Releases](https://github.com/sirtaymarthin/linkalia-domain/releases).

```
public/
├── index.html        # Español (https://linkalia.org/)
├── en/index.html     # English (https://linkalia.org/en/)
├── sitemap.xml
├── robots.txt
└── favicons e iconos / icons
wrangler.toml         # Cloudflare (dominio + carpeta public/)
```

Despliegue / Deploy:

```bash
npx wrangler deploy
```
