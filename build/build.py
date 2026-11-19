# -*- coding: utf-8 -*-
"""
Générateur statique du site Derapest.
Usage :  python3 build/build.py
Écrit toutes les pages .html, sitemap.xml et robots.txt à la racine du projet.
"""
import json
import os
import sys
from datetime import date
from html import escape
from urllib.parse import quote

sys.path.insert(0, os.path.dirname(__file__))
from data import SITE, SERVICES, PESTS, ZONES, PROMISES
from map_data import MAP  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TODAY = date.today().isoformat()
ALL = SERVICES + PESTS
BY_SLUG = {p["slug"]: p for p in ALL}
WA_URL = f"https://wa.me/{SITE['whatsapp']}?text={quote(SITE['wa_message'])}"
PAGES = []  # (filename, priority) pour le sitemap


def zone_file(z):
    return f"deratisation-{z['slug']}.html"


# ------------------------------------------------------------------ icônes
I = {
    "arrow": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 17 17 7M9 7h8v8"/></svg>',
    "chev": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg>',
    "phone": '<svg class="fill" viewBox="0 0 24 24" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.6a1 1 0 0 1-.25 1z"/></svg>',
    "wa": '<svg class="fill" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm5.2 14.1c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .3-3.5-.7-2.9-1.2-4.8-4.2-4.9-4.4-.1-.2-1.2-1.6-1.2-3 0-1.4.8-2.1 1-2.4.3-.3.6-.3.8-.3h.6c.2 0 .5-.1.7.5l1 2.4c.1.2.1.4 0 .6l-.4.6-.5.5c-.2.2-.3.4-.1.7.2.3.8 1.3 1.7 2.1 1.2 1 2.1 1.4 2.4 1.5.3.1.5.1.7-.1l.9-1.1c.2-.3.4-.2.7-.1l2.2 1.1c.3.1.5.2.6.4 0 .1 0 .7-.3 1.4z"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m4 7 8 6 8-6"/></svg>',
    "doc": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5M9 13h6M9 17h4"/></svg>',
    "shield": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3 4 6v6c0 4.5 3.2 8 8 9 4.8-1 8-4.5 8-9V6z"/><path d="m8.5 12 2.5 2.5 4.5-5"/></svg>',
    "pin": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 21s-7-6.2-7-12a7 7 0 0 1 14 0c0 5.8-7 12-7 12z"/><circle cx="12" cy="9" r="2.5"/></svg>',
    "bolt": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M13 2 4 14h7l-1 8 9-12h-7z"/></svg>',
    "warn": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3 2 20h20z"/><path d="M12 10v4M12 17v.5"/></svg>',
    "eye": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/></svg>',
    "bulb": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 18h6M10 21h4M12 3a6 6 0 0 0-3.5 10.9c.6.4 1 1.1 1 1.8V16h5v-.3c0-.7.4-1.4 1-1.8A6 6 0 0 0 12 3z"/></svg>',
    "building": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 21V5a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v16M16 9h2a2 2 0 0 1 2 2v10M3 21h18M8 7h4M8 11h4M8 15h4"/></svg>',
    "home": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="m3 11 9-7 9 7M5 9.5V20h14V9.5M10 20v-5h4v5"/></svg>',
    # pictos métiers
    "deratisation": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 15c0-4 3-7 8-7 2 0 3-2 5-2s2 2 1 3c2 1 4 3 4 5 0 1-1 2-2 2H7c-2 0-4-.5-4-1z"/><circle cx="17" cy="11.5" r=".6"/><path d="M7 16c-2 1-4 1-5 3"/></svg>',
    "desinsectisation": '<svg viewBox="0 0 24 24" aria-hidden="true"><ellipse cx="12" cy="13.5" rx="4.5" ry="6"/><path d="M12 7.5V5M9.5 5 8 3M14.5 5 16 3M7.5 11 4 9.5M7.5 14H3.5M8 17l-3 2M16.5 11 20 9.5M16.5 14h4M16 17l3 2M8 12.5h8M8.3 15.5h7.4"/></svg>',
    "desinfection": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 9h6v10a2 2 0 0 1-2 2h-2a2 2 0 0 1-2-2zM10 9V6h4v3M14 6h3M12 13v4M10 15h4M6 4l-1-1M5.5 7H4M6 10l-1 1"/></svg>',
    "fumigation": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 20h16M6 20v-5h12v5M8 11c0-2 2-2 2-4s-2-2-2-4M12 11c0-2 2-2 2-4s-2-2-2-4M16 11c0-2 2-2 2-4"/></svg>',
    "punaises-de-lit": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 18v-6h18v6M3 15h18M6 12V9a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v3"/><circle cx="17" cy="8" r="1.6"/></svg>',
    "cafards-blattes": '<svg viewBox="0 0 24 24" aria-hidden="true"><ellipse cx="12" cy="14" rx="4" ry="6.5"/><path d="M12 7.5c0-2-1-3.5-4-5M12 7.5c0-2 1-3.5 4-5M8 12 4 10M8 15H4M8.5 18 5 20M16 12l4-2M16 15h4M15.5 18l3.5 2"/></svg>',
    "guepes-frelons": '<svg viewBox="0 0 24 24" aria-hidden="true"><ellipse cx="12" cy="15" rx="3.5" ry="5"/><circle cx="12" cy="7.5" r="2"/><path d="M8.5 13h7M8.7 16h6.6M12 20v2M10 9 5 6.5c-1.5-.8-2.8 1.4-1 2.2L8.6 11M14 9l5-2.5c1.5-.8 2.8 1.4 1 2.2L15.4 11"/></svg>',
    "fourmis": '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="6" cy="12" r="2.2"/><circle cx="11.5" cy="12" r="1.6"/><ellipse cx="17.5" cy="12" rx="3" ry="2.4"/><path d="M5 10 3.5 6.5M7 10l1-3.5M11 13.5 9 18M12 13.5l2 4.5M11 10.5 9 6M12 10.5l2-4.5M17 14.5 16 18M18.5 14.5l1.5 3.5"/></svg>',
}


# pictos du bandeau défilant (un par nuisible)
I.update({
    "m_rat": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M2.5 15.5c0-3.6 3-6.5 7.5-6.5 1.6 0 2.6-1.8 4.4-1.8 1.7 0 1.9 1.7 1 2.7 1.9.9 3.6 2.6 3.6 4.4 0 .9-.8 1.7-1.7 1.7H6.5c-1.8 0-4-.3-4-.5z"/><circle cx="16.2" cy="12" r=".7" fill="currentColor"/><path d="M6.5 16.2c-1.8 1-3.6 1.3-4.5 3.3M19.5 13.8l2 .4"/></svg>',
    "m_mouse": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 16c0-3.3 2.7-6 6.5-6 2.4 0 4.3.8 5.5 2.2l3 .8c.6.2.7 1 .2 1.4L17 16H4z"/><circle cx="12" cy="8.5" r="2.2"/><circle cx="15" cy="13" r=".6" fill="currentColor"/><path d="M4 16c-1.2.5-2 1.5-2 3"/></svg>',
    "m_roach": '<svg viewBox="0 0 24 24" aria-hidden="true"><ellipse cx="12" cy="14" rx="4" ry="6.5"/><path d="M12 7.5v13M12 7.5c0-2-1-3.5-4-5M12 7.5c0-2 1-3.5 4-5M8 12 4 10M8 15H4M8.5 18 5 20M16 12l4-2M16 15h4M15.5 18l3.5 2"/></svg>',
    "m_bedbug": '<svg viewBox="0 0 24 24" aria-hidden="true"><ellipse cx="12" cy="14" rx="5.5" ry="6"/><circle cx="12" cy="6.5" r="2"/><path d="M7 11.5h10M6.8 14.5h10.4M7.8 17.5h8.4M6.8 11 3.5 9M6.5 14.5H3M7.5 18l-3 2M17.2 11l3.3-2M17.5 14.5H21M16.5 18l3 2M11 4.8 10 3M13 4.8 14 3"/></svg>',
    "m_flea": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 13c0-4 3-7 7-7 3 0 5 2 5 4.5 0 4-3.5 7.5-8 7.5-2.5 0-4-2-4-5z"/><circle cx="16" cy="9.5" r=".6" fill="currentColor"/><path d="M18 9l3-1M9 17l-2 4M12 17.5l1.5 3.5M15 15.5l4 5.5 2-1"/></svg>',
    "m_ant": '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="6" cy="12" r="2.2"/><circle cx="11.5" cy="12" r="1.6"/><ellipse cx="17.5" cy="12" rx="3" ry="2.4"/><path d="M5 10 3.5 6.5M7 10l1-3.5M11 13.5 9 18M12 13.5l2 4.5M11 10.5 9 6M12 10.5l2-4.5M17 14.5 16 18M18.5 14.5l1.5 3.5"/></svg>',
    "m_moth": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 7v12M12 9C9 4 3 4 3 8c0 3 3 5 9 5M12 9c3-5 9-5 9-1 0 3-3 5-9 5M12 13c-3 0-6 1.5-6 4 0 2 3 2 6-2M12 13c3 0 6 1.5 6 4 0 2-3 2-6-2M11 7 9.5 4M13 7l1.5-3"/></svg>',
    "m_mosquito": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 9.5v8M12 9.5 4 5M12 9.5l8-4.5M12 9.5 9.5 7.5M12 9.5 4 3.5M10.5 12 5 15l-1 4M13.5 12 19 15l1 4M11 15l-3 4M13 15l3 4M12 9.5l-4.5 3"/><circle cx="12" cy="8.5" r="1.4"/></svg>',
    "m_wasp": '<svg viewBox="0 0 24 24" aria-hidden="true"><ellipse cx="12" cy="15" rx="3.5" ry="5"/><circle cx="12" cy="7.5" r="2"/><path d="M8.5 13h7M8.7 16h6.6M12 20v2M10 9 5 6.5c-1.5-.8-2.8 1.4-1 2.2L8.6 11M14 9l5-2.5c1.5-.8 2.8 1.4 1 2.2L15.4 11"/></svg>',
    "m_hornet": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 9.5c-2.4 0-4 2.4-4 6s1.6 6 4 6 4-2.4 4-6-1.6-6-4-6z"/><circle cx="12" cy="7" r="2.4"/><path d="M8.2 14h7.6M8.2 17.5h7.6M10.5 9.5 3 5.5c-1.6-.8-2.6 1.6-.8 2.3L8.5 11M13.5 9.5l7.5-4c1.6-.8 2.6 1.6.8 2.3L15.5 11M10.8 4.8 9.5 2.5M13.2 4.8l1.3-2.3"/></svg>',
    "m_termite": '<svg viewBox="0 0 24 24" aria-hidden="true"><ellipse cx="12" cy="15.5" rx="3" ry="5"/><rect x="9.8" y="7.5" width="4.4" height="4" rx="2"/><path d="M10.5 7.5 9 4.5M13.5 7.5l1.5-3M9.3 13 5.5 11M9 16H5M9.5 19l-3 2M14.7 13l3.8-2M15 16h4M14.5 19l3 2"/></svg>',
})

MARQUEE = [("Rats", "rat"), ("Souris", "mouse"), ("Cafards", "roach"), ("Punaises de lit", "bedbug"), ("Puces", "flea"), ("Fourmis", "ant"), ("Mites", "moth"), ("Moustiques", "mosquito"), ("Guêpes", "wasp"), ("Frelons", "hornet"), ("Termites", "termite")]

# ------------------------------------------------------------------ fragments


def btn(href, label, variant="dark", extra="", attrs=""):
    return f'<a class="btn btn--{variant} {extra}" href="{href}"{attrs}>{label} <span class="btn__arrow">{I["arrow"]}</span></a>'


def tel_btn(variant="green", extra=""):
    return f'<a class="btn-ic btn-ic--{variant} {extra}" href="tel:{SITE["phone_intl"]}">{I["phone"]}<span><small>Appel direct</small>{SITE["phone_display"]}</span></a>'


def wa_btn(extra=""):
    return f'<a class="btn-ic btn-ic--wa {extra}" href="{WA_URL}" target="_blank" rel="noopener">{I["wa"]}<span><small>Réponse rapide</small>WhatsApp</span></a>'


def eyebrow(text, dark=False):
    return f'<p class="eyebrow{" eyebrow--onDark" if dark else ""}"><i></i>{text}</p>'


def nav_html(active):
    services = "".join(f'<a href="{s["slug"]}.html"><span class="dd__ic">{I[s["slug"]]}</span><span><strong>{s["nav"]}</strong><small>{s["short"]}</small></span></a>' for s in SERVICES)
    pests = "".join(f'<a href="{p["slug"]}.html"><span class="dd__ic">{I[p["slug"]]}</span><span><strong>{p["nav"]}</strong></span></a>' for p in PESTS)
    zones = "".join(f'<a href="{zone_file(z)}"><b>{z["num"]}</b>{z["name"]}</a>' for z in ZONES)

    def cls(key):
        return ' class="is-active"' if active == key else ""

    return f'''<nav class="nav" id="nav" aria-label="Navigation principale">
    <a href="index.html"{cls("home")}>Accueil</a>
    <div class="nav__dd{" is-current" if active == "prestations" else ""}">
      <button type="button" class="nav__toggle" aria-expanded="false">Prestations {I["chev"]}</button>
      <div class="dd dd--wide">
        <div class="dd__col"><p class="dd__title">Nos métiers</p>{services}</div>
        <div class="dd__col"><p class="dd__title">Nuisibles</p>{pests}
          <a class="dd__cta" href="contact.html">Demander un devis gratuit {I["arrow"]}</a></div>
      </div>
    </div>
    <div class="nav__dd{" is-current" if active == "zones" else ""}">
      <button type="button" class="nav__toggle" aria-expanded="false">Zones {I["chev"]}</button>
      <div class="dd dd--zones">
        <p class="dd__title">Île-de-France &amp; Oise</p>
        <div class="dd__zones">{zones}</div>
        <a class="dd__all" href="zones-intervention.html">Toutes nos zones d'intervention {I["arrow"]}</a>
      </div>
    </div>
    <a href="professionnels.html"{cls("pro")}>Professionnels</a>
    <a href="contact.html"{cls("contact")}>Contact</a>
    <div class="nav__mobile-cta">
      <a class="btn btn--green btn--block" href="tel:{SITE["phone_intl"]}">Appeler le {SITE["phone_display"]} <span class="btn__arrow">{I["phone"]}</span></a>
    </div>
  </nav>'''


def topbar():
    items = "".join(f'<li>{I[ic]}{t}</li>' for t, ic in PROMISES)
    return f'<div class="topbar" id="topbar"><ul class="topbar__list">{items}</ul></div>'


def header(active):
    return f'''{topbar()}
<header class="header" id="header">
  <a class="header__logo" href="index.html" aria-label="Derapest — accueil">
    <img src="assets/img/logo-sm.png" alt="Derapest Anti-Nuisibles" width="420" height="178">
  </a>
  {nav_html(active)}
  <div class="header__actions">
    <a class="header__tel" href="tel:{SITE["phone_intl"]}">{I["phone"]}<span>{SITE["phone_display"]}</span></a>
    {btn("contact.html", "Devis gratuit", "light", "btn--sm header__cta")}
    <button class="burger" id="burger" aria-label="Ouvrir le menu" aria-expanded="false" aria-controls="nav"><span></span><span></span></button>
  </div>
</header>'''


PRELOADER = '''<div class="preloader" id="preloader" aria-hidden="true">
  <div class="preloader__inner">
    <div class="preloader__logo"><img src="assets/img/logo-sm.png" alt="" width="420" height="178"><span class="preloader__scan"></span></div>
    <div class="preloader__bar"><span id="preloaderBar"></span></div>
    <div class="preloader__meta"><span>Sécurisation des lieux</span><span class="preloader__count"><em id="preloaderCount">0</em>%</span></div>
  </div>
</div>'''


def footer():
    srv = "".join(f'<a href="{s["slug"]}.html">{s["nav"]}</a>' for s in SERVICES)
    pst = "".join(f'<a href="{p["slug"]}.html">{p["nav"]}</a>' for p in PESTS)
    zns = "".join(f'<a href="{zone_file(z)}">Dératisation {z["name"]} ({z["num"]})</a>' for z in ZONES)
    return f'''<footer class="footer">
  <div class="container footer__top">
    <div>
      <p class="footer__claim">Un nuisible ? <em>On s'en occupe.</em></p>
      <p class="footer__sub">Devis gratuit, en Île-de-France et dans l'Oise.</p>
    </div>
    <div class="footer__ctas">{tel_btn("green")}{wa_btn()}</div>
  </div>
  <div class="container footer__grid">
    <div class="footer__brand">
      <img src="assets/img/logo-sm.png" alt="Derapest Anti-Nuisibles" width="420" height="178" loading="lazy">
      <p>Dératisation, désinsectisation, désinfection et fumigation pour particuliers et professionnels en Île-de-France et dans l'Oise.</p>
    </div>
    <div><h4>Prestations</h4>{srv}<a href="professionnels.html">Professionnels</a></div>
    <div><h4>Nuisibles</h4>{pst}<a href="contact.html">Devis gratuit</a></div>
    <div class="footer__zones"><h4>Zones d'intervention</h4>{zns}</div>
  </div>
  <div class="container footer__bottom">
    <span>© {date.today().year} {SITE["full_name"]}. Tous droits réservés.</span>
    <span><a href="mentions-legales.html">Mentions légales</a> · <a href="zones-intervention.html">Zones d'intervention</a> · <a href="contact.html">Contact</a></span>
  </div>
</footer>
<a class="wa" href="{WA_URL}" target="_blank" rel="noopener" aria-label="Nous écrire sur WhatsApp">
  <span class="wa__label">Besoin d'aide ? Écrivez-nous</span>
  <span class="wa__btn">{I["wa"]}</span>
</a>
<nav class="mbar" aria-label="Contact rapide">
  <a href="contact.html#devis" class="mbar__quote">{I["doc"]}Devis</a>
  <a href="{WA_URL}" target="_blank" rel="noopener" class="mbar__wa">{I["wa"]}WhatsApp</a>
  <a href="tel:{SITE["phone_intl"]}" class="mbar__call">{I["phone"]}Appeler</a>
</nav>'''


def local_business():
    return {
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "additionalType": "https://www.wikidata.org/wiki/Q2306047",
        "@id": f"{SITE['url']}/#entreprise",
        "name": SITE["full_name"],
        "url": f"{SITE['url']}/",
        "logo": f"{SITE['url']}/assets/img/logo.png",
        "image": f"{SITE['url']}/assets/img/logo-full.jpg",
        "telephone": SITE["phone_intl"],
        "email": SITE["email"],
        "description": "Dératisation, désinsectisation, désinfection et fumigation en Île-de-France et dans l'Oise.",
        "areaServed": [{"@type": "AdministrativeArea", "name": f"{z['name']} ({z['num']})"} for z in ZONES],
        "knowsAbout": [s["nav"] for s in ALL],
    }


def breadcrumb_ld(items):
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": f"{SITE['url']}/{u}"}
            for i, (n, u) in enumerate(items)
        ],
    }


def faq_ld(faq):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq
        ],
    }


def breadcrumb_html(items):
    parts = []
    for i, (n, u) in enumerate(items):
        if i == len(items) - 1:
            parts.append(f'<span aria-current="page">{n}</span>')
        else:
            parts.append(f'<a href="{u or "index.html"}">{n}</a>')
    return '<nav class="crumbs" aria-label="Fil d\'Ariane">' + "<i>/</i>".join(parts) + "</nav>"


def page(filename, *, title, desc, body, active="", schemas=(), priority="0.7", robots="index, follow", og_image="assets/img/logo-full.jpg", preload_img=None):
    canonical = f"{SITE['url']}/" if filename == "index.html" else f"{SITE['url']}/{filename}"
    ld = "\n".join(
        f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>'
        for s in [local_business(), *schemas]
    )
    preload = f'<link rel="preload" as="image" href="assets/img/{preload_img}">' if preload_img else ""
    html = f'''<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title>
<meta name="description" content="{escape(desc)}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{canonical}">
<meta name="theme-color" content="#0a0c0a">
<link rel="icon" type="image/png" href="assets/img/favicon.png">
<link rel="apple-touch-icon" href="assets/img/favicon.png">
<meta property="og:type" content="website">
<meta property="og:locale" content="fr_FR">
<meta property="og:site_name" content="{SITE["full_name"]}">
<meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE["url"]}/{og_image}">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Exo:ital,wght@0,400;0,500;0,600;0,700;0,800;1,600;1,700;1,800&display=swap" rel="stylesheet">
<link rel="preload" as="image" href="assets/img/logo-sm.png">
{preload}
<link rel="stylesheet" href="assets/css/style.css">
<script>try{{if(sessionStorage.getItem('dp-seen'))document.documentElement.classList.add('pl-skip')}}catch(e){{}}</script>
{ld}
</head>
<body class="is-loading" data-wa="{SITE["whatsapp"]}">
{PRELOADER}
{header(active)}
<main id="top">
{body}
</main>
{footer()}
<script src="assets/js/main.js" defer></script>
</body>
</html>
'''
    with open(os.path.join(ROOT, filename), "w", encoding="utf-8") as f:
        f.write(html)
    if not robots.startswith("noindex"):
        PAGES.append((filename, priority))


# ------------------------------------------------------------------ sections partagées


def page_hero(crumbs, kicker, h1, lead, img, img_alt, chips=None, cta_label="Obtenir mon devis gratuit"):
    chips = chips or ["Devis gratuit et sans engagement", "Techniciens habilités", "Île-de-France &amp; Oise"]
    chips_html = "".join(f"<li>{I['shield']}{c}</li>" for c in chips)
    return f'''<section class="phero">
  <div class="phero__glow" aria-hidden="true"></div>
  <div class="container phero__grid">
    <div class="phero__text">
      {breadcrumb_html(crumbs)}
      <p class="eyebrow eyebrow--glass"><i></i>{kicker}</p>
      <h1 class="phero__title">{h1}</h1>
      <p class="phero__lead">{lead}</p>
      <div class="phero__ctas">
        {btn("#devis", cta_label, "green")}
        <a class="phero__tel" href="tel:{SITE["phone_intl"]}"><span>{I["phone"]}</span><span><small>Une urgence ? Appelez</small>{SITE["phone_display"]}</span></a>
      </div>
      <ul class="phero__chips">{chips_html}</ul>
    </div>
    <div class="phero__media">
      <img src="assets/img/{img}" alt="{escape(img_alt)}" width="500" height="400">
      <div class="phero__badge"><strong>Devis gratuit</strong><span>Réponse rapide par téléphone ou WhatsApp</span></div>
    </div>
  </div>
</section>'''


def cta_band(title, text, kicker="Besoin d'une intervention ?"):
    return f'''<section class="ctaband">
  <div class="container ctaband__inner reveal">
    <div class="ctaband__text">
      {eyebrow(kicker, True)}
      <h2 class="ctaband__title">{title}</h2>
      <p>{text}</p>
    </div>
    <div class="ctaband__actions">
      {tel_btn("green")}
      {wa_btn()}
      <a class="ctaband__link" href="#devis">ou demander un devis écrit {I["arrow"]}</a>
    </div>
  </div>
</section>'''


def steps_section(steps, title='De votre appel<br><em>au dernier contrôle.</em>', kicker="Notre méthode", cta=True):
    items = "".join(
        f'<li class="step reveal"><span class="step__num"><em>{i + 1}</em></span><h3>{t}</h3><p>{d}</p></li>'
        for i, (t, d) in enumerate(steps)
    )
    cta_html = f'<div class="steps__cta reveal">{btn("#devis", "Planifier mon intervention", "green")}<span>Diagnostic sur place avant tout traitement.</span></div>' if cta else ""
    return f'''<section class="section section--dark">
  <div class="container">
    <div class="section__head reveal">{eyebrow(kicker, True)}<h2 class="h2">{title}</h2></div>
    <ol class="steps">{items}</ol>
    {cta_html}
  </div>
</section>'''


GENERIC_STEPS = [
    ("Prise de contact", "Vous décrivez la situation par téléphone, WhatsApp ou formulaire : type de nuisible, lieu, ampleur."),
    ("Diagnostic sur place", "Identification de l'espèce, des points d'entrée et du niveau d'infestation. Aucun traitement sans inspection."),
    ("Traitement adapté", "Technique et produits homologués choisis selon le nuisible, les lieux et leurs occupants."),
    ("Compte rendu & suivi", "Rapport d'intervention par e-mail, conseils de prévention et contrôle jusqu'à éradication."),
]

GENERIC_FAQ = [
    ("Le devis est-il gratuit ?", "Oui. Le devis est gratuit et sans engagement. Décrivez votre situation par téléphone, WhatsApp ou via le formulaire."),
    ("Les produits sont-ils dangereux pour ma famille ou mes animaux ?", "Nous utilisons uniquement des produits agréés et homologués, appliqués par des techniciens formés. Les appâts rodenticides sont placés dans des postes sécurisés fermés à clé, et le technicien vous indique les précautions à respecter."),
    ("Intervenez-vous pour les professionnels ?", "Oui : restaurants, commerces alimentaires, entrepôts, copropriétés, établissements recevant du public. Interventions ponctuelles ou contrats de suivi avec rapport à chaque passage."),
]


def faq_section(faq, title='Vos questions,<br><em>nos réponses.</em>'):
    items = "".join(
        f'<details{" open" if i == 0 else ""}><summary>{q}<span></span></summary><p>{a}</p></details>'
        for i, (q, a) in enumerate(faq)
    )
    return f'''<section class="section" id="faq">
  <div class="container faqwrap">
    <div class="faqwrap__aside reveal">
      {eyebrow("FAQ")}
      <h2 class="h2">{title}</h2>
      <p class="muted">Vous ne trouvez pas votre réponse ? Un technicien vous répond directement.</p>
      <div class="faqwrap__ctas">{tel_btn("dark")}{wa_btn()}</div>
    </div>
    <div class="faq reveal">{items}</div>
  </div>
</section>'''


def zones_strip(prefix_text, title):
    chips = "".join(f'<a class="zchip" href="{zone_file(z)}"><b>{z["num"]}</b>{z["name"]}</a>' for z in ZONES)
    return f'''<section class="section section--grey section--tight">
  <div class="container zstrip reveal">
    <div>{eyebrow("Zones d'intervention")}<h2 class="h3">{title}</h2><p class="muted">{prefix_text}</p></div>
    <div class="zchips">{chips}</div>
  </div>
</section>'''


def related_section(slugs, title="Nos autres prestations"):
    cards = "".join(card(BY_SLUG[s]) for s in slugs)
    return f'''<section class="section section--tight">
  <div class="container">
    <div class="section__head section__head--row reveal">
      <div>{eyebrow("À découvrir")}<h2 class="h2">{title}</h2></div>
      {btn("zones-intervention.html", "Voir nos zones", "outline")}
    </div>
    <div class="cards">{cards}</div>
  </div>
</section>'''


def card(p):
    return f'''<a class="scard reveal" href="{p["slug"]}.html">
  <div class="scard__media"><img src="assets/img/{p["img"]}" alt="{escape(p["img_alt"])}" loading="lazy" width="500" height="400"><span class="scard__ic">{I[p["slug"]]}</span></div>
  <div class="scard__body"><small>{p["kicker"]}</small><h3>{p["nav"]}</h3><p>{p["short"]}</p><span class="scard__more">En savoir plus {I["arrow"]}</span></div>
</a>'''


def contact_section(selected="", title='Un nuisible ?<br><em>On s\'en occupe.</em>'):
    opts = "".join(
        f'<option{" selected" if s["nav"] == selected else ""}>{s["nav"]}</option>' for s in ALL
    ) + '<option>Désinfection après sinistre</option><option>Contrat professionnel</option><option>Je ne sais pas</option>'
    zones_opts = "".join(f'<option>{z["name"]} ({z["num"]})</option>' for z in ZONES)
    return f'''<section class="contact" id="devis">
  <div class="contact__bg"><img src="assets/img/hero.webp" alt="" loading="lazy"></div>
  <div class="container contact__grid">
    <div class="contact__intro reveal">
      {eyebrow("Devis gratuit", True)}
      <h2 class="h2">{title}</h2>
      <p class="lead">Décrivez votre situation : nous revenons vers vous rapidement avec une date d'intervention et un devis clair.</p>
      <ul class="contact__list">
        <li><a href="tel:{SITE["phone_intl"]}"><span>{I["phone"]}</span><div><small>Téléphone</small><strong>{SITE["phone_display"]}</strong></div></a></li>
        <li><a href="{WA_URL}" target="_blank" rel="noopener"><span>{I["wa"]}</span><div><small>WhatsApp</small><strong>Écrire sur WhatsApp</strong></div></a></li>
        <li><a href="mailto:{SITE["email"]}"><span>{I["mail"]}</span><div><small>E-mail</small><strong>{SITE["email"]}</strong></div></a></li>
      </ul>
    </div>
    <form class="form reveal" id="quoteForm" novalidate>
      <h3>Demande de devis</h3>
      <p class="form__hint">Gratuit et sans engagement. Votre demande s'ouvre dans WhatsApp, prête à être envoyée.</p>
      <div class="form__row">
        <label>Nom<input type="text" name="nom" autocomplete="name" required></label>
        <label>Téléphone<input type="tel" name="tel" autocomplete="tel" required></label>
      </div>
      <div class="form__row">
        <label>Prestation<select name="prestation" id="prestationSelect">{opts}</select></label>
        <label>Département<select name="zone"><option value="">Choisir…</option>{zones_opts}</select></label>
      </div>
      <div class="form__row">
        <label>Vous êtes<select name="profil"><option>Particulier</option><option>Professionnel</option><option>Syndic / bailleur</option></select></label>
        <label>Ville<input type="text" name="ville" autocomplete="address-level2"></label>
      </div>
      <label>Votre situation<textarea name="message" rows="3" placeholder="Ex. : bruits dans les combles la nuit, crottes dans la cuisine…"></textarea></label>
      <p class="form__error" id="formError" role="alert" hidden>Merci d'indiquer votre nom et votre téléphone.</p>
      <button class="btn btn--green btn--block" type="submit">Envoyer ma demande <span class="btn__arrow">{I["arrow"]}</span></button>
      <p class="form__legal">Vos informations servent uniquement à traiter votre demande.</p>
    </form>
  </div>
</section>'''


# ------------------------------------------------------------------ pages prestations / nuisibles


def build_service(p):
    is_pest = p["kind"] == "pest"
    crumbs = [("Accueil", "index.html"), (p["nav"], f'{p["slug"]}.html')]
    signs = "".join(
        f'<article class="sign reveal"><span class="sign__ic">{I[["eye", "warn", "bolt"][i % 3]]}</span><h3>{t}</h3><p>{d}</p></article>'
        for i, (t, d) in enumerate(p["signs"])
    )
    risks = "".join(f"<li>{r}</li>" for r in p["risks"])
    sols = "".join(f"<li>{s}</li>" for s in p["solutions"])
    tips = "".join(f"<li>{t}</li>" for t in p["tips"])
    faq = p["faq"] + [GENERIC_FAQ[0]]

    body = f'''{page_hero(crumbs, p["kicker"] + " · Île-de-France &amp; Oise", p["h1"], p["lead"], p["img"], p["img_alt"])}

<section class="section">
  <div class="container">
    <div class="section__head reveal">{eyebrow("Diagnostic")}<h2 class="h2">{p["signs_title"]}</h2></div>
    <div class="signs">{signs}</div>
  </div>
</section>

<section class="section section--grey">
  <div class="container split reveal">
    <div class="split__media"><img src="assets/img/{p["img"]}" alt="{escape(p["img_alt"])}" loading="lazy" width="500" height="400"></div>
    <div class="split__body">
      {eyebrow("Les risques")}
      <h2 class="h2">{p["risks_title"]}</h2>
      <p class="lead">{p["risks_text"]}</p>
      <ul class="warns">{risks}</ul>
    </div>
  </div>
</section>

{cta_band("Vous reconnaissez ces signes ?<br><em>Ne laissez pas l'infestation s'étendre.</em>", "Un technicien évalue votre situation au téléphone et vous propose une date d'intervention.", "Agir vite")}

{steps_section(p["steps"], f'Notre protocole<br><em>{p["nav"].lower()}.</em>', "Comment nous intervenons")}

<section class="section">
  <div class="container duo">
    <div class="duo__main reveal">
      {eyebrow("Nos solutions")}
      <h2 class="h2">{p["solutions_title"]}</h2>
      <ul class="ticks">{sols}</ul>
      {btn("#devis", "Demander un devis " + p["nav"].lower(), "dark")}
    </div>
    <aside class="tipcard reveal">
      <span class="tipcard__ic">{I["bulb"]}</span>
      <h3>Nos conseils de prévention</h3>
      <ul>{tips}</ul>
    </aside>
  </div>
</section>

{zones_strip(f"Nos techniciens interviennent pour la {p['nav'].lower()} chez les particuliers et les professionnels, dans les 8 départements d'Île-de-France et dans l'Oise." if not is_pest else f"Nous traitons les {p['nav'].lower()} dans toute l'Île-de-France et dans l'Oise, en logement comme en local professionnel.", f"{p['nav']} en Île-de-France et dans l'Oise")}

{faq_section(faq, f'{p["nav"]} :<br><em>vos questions.</em>')}

{related_section(p["related"])}

{contact_section(p["nav"])}'''

    service_ld = {
        "@context": "https://schema.org",
        "@type": "Service",
        "serviceType": p["nav"],
        "name": p["title"].split(" | ")[0],
        "description": p["desc"],
        "provider": {"@id": f"{SITE['url']}/#entreprise"},
        "areaServed": [{"@type": "AdministrativeArea", "name": z["name"]} for z in ZONES],
        "url": f"{SITE['url']}/{p['slug']}.html",
    }
    page(
        f'{p["slug"]}.html', title=p["title"], desc=p["desc"], body=body, active="prestations",
        schemas=[service_ld, breadcrumb_ld(crumbs), faq_ld(faq)], priority="0.9" if not is_pest else "0.8",
        og_image=f"assets/img/{p['img']}", preload_img=p["img"],
    )


# ------------------------------------------------------------------ pages zones


def build_zone(z):
    fname = zone_file(z)
    crumbs = [("Accueil", "index.html"), ("Zones d'intervention", "zones-intervention.html"), (f"{z['name']} ({z['num']})", fname)]
    focus = [BY_SLUG[s] for s in z["focus"]]
    ordered = focus + [p for p in ALL if p["slug"] not in z["focus"]]
    cards = "".join(card(p) for p in ordered[:6])
    cities = "".join(f"<li>{I['pin']}{c}</li>" for c in z["cities"])
    ctx = "".join(f"<p>{c}</p>" for c in z["context"])
    others = "".join(f'<a class="zchip" href="{zone_file(o)}"><b>{o["num"]}</b>{o["name"]}</a>' for o in ZONES if o is not z)
    faq = z["faq"] + GENERIC_FAQ[:2]
    title = f"Dératisation & désinsectisation {z['name']} ({z['num']}) | Derapest"
    desc = f"Dératisation, désinsectisation et désinfection {z['prep']} ({z['num']}) : rats, souris, punaises de lit, cafards, guêpes. Techniciens habilités, devis gratuit."
    h1 = f"Dératisation et désinsectisation<br><em>{z['prep']} ({z['num']})</em>"

    body = f'''{page_hero(crumbs, f"{z['region']} · {z['name']} ({z['num']})", h1, z["intro"], focus[0]["img"], focus[0]["img_alt"], ["Devis gratuit et sans engagement", "Particuliers &amp; professionnels", f"Tout le département ({z['num']})"])}

<section class="section">
  <div class="container">
    <div class="section__head section__head--row reveal">
      <div>{eyebrow(f"Nos interventions {z['prep']}")}<h2 class="h2">Les nuisibles que nous traitons<br><em>{z['prep']}.</em></h2></div>
      {btn("#devis", "Devis gratuit", "dark")}
    </div>
    <div class="cards">{cards}</div>
  </div>
</section>

<section class="section section--grey">
  <div class="container duo">
    <div class="duo__main prose reveal">
      {eyebrow("Le contexte local")}
      <h2 class="h2">Pourquoi les nuisibles<br><em>s'installent {z['prep']}.</em></h2>
      {ctx}
      <p>Quel que soit le cas, nous commençons par un diagnostic sur place, puis choisissons le traitement adapté au nuisible, aux lieux et à leurs occupants, avec des produits homologués et un compte rendu écrit.</p>
    </div>
    <aside class="citycard reveal">
      <h3>{I["pin"]} Villes desservies</h3>
      <ul class="cities">{cities}</ul>
      <p>Votre commune n'apparaît pas ? Nous couvrons tout le département.</p>
      {btn(f"tel:{SITE['phone_intl']}", "Vérifier ma commune", "green", "btn--block")}
    </aside>
  </div>
</section>

{cta_band(f"Une intervention {z['prep']} ?<br><em>Appelez, on organise tout.</em>", "Décrivez votre problème : nous vous proposons une date d'intervention et un devis gratuit.")}

{steps_section(GENERIC_STEPS)}

{faq_section(faq, f'Nuisibles {z["prep"]} :<br><em>vos questions.</em>')}

<section class="section section--grey section--tight">
  <div class="container zstrip reveal">
    <div>{eyebrow("Autres départements")}<h2 class="h3">Nous intervenons aussi en Île-de-France et dans l'Oise</h2></div>
    <div class="zchips">{others}</div>
  </div>
</section>

{contact_section()}'''

    service_ld = {
        "@context": "https://schema.org",
        "@type": "Service",
        "serviceType": "Dératisation, désinsectisation et désinfection",
        "name": f"Dératisation et désinsectisation {z['prep']} ({z['num']})",
        "provider": {"@id": f"{SITE['url']}/#entreprise"},
        "areaServed": {"@type": "AdministrativeArea", "name": f"{z['name']} ({z['num']})"},
        "url": f"{SITE['url']}/{fname}",
    }
    page(fname, title=title, desc=desc, body=body, active="zones",
         schemas=[service_ld, breadcrumb_ld(crumbs), faq_ld(faq)], priority="0.8",
         og_image=f"assets/img/{focus[0]['img']}", preload_img=focus[0]["img"])


def build_zones_hub():
    crumbs = [("Accueil", "index.html"), ("Zones d'intervention", "zones-intervention.html")]
    idf = [z for z in ZONES if z["region"] == "Île-de-France"]
    oise = [z for z in ZONES if z["region"] != "Île-de-France"]

    def zcards(lst):
        return "".join(
            f'''<a class="zcard reveal" href="{zone_file(z)}"><span class="zcard__num">{z["num"]}</span><h3>{z["name"]}</h3><p>{", ".join(z["cities"][:4])}…</p><span class="zcard__more">Dératisation {z["name"]} {I["arrow"]}</span></a>'''
            for z in lst
        )

    body = f'''{page_hero(crumbs, "Île-de-France &amp; Oise", "Nos zones d'intervention :<br><em>Île-de-France et Oise.</em>", "Nos techniciens interviennent dans les huit départements franciliens et dans l'Oise, chez les particuliers comme chez les professionnels. Choisissez votre département pour en savoir plus.", "hero.webp", "Technicien Derapest en intervention", ["9 départements couverts", "Particuliers &amp; professionnels", "Devis gratuit"], "Demander un devis")}

<section class="section">
  <div class="container">
    <div class="section__head reveal">{eyebrow("Île-de-France")}<h2 class="h2">Les 8 départements<br><em>d'Île-de-France.</em></h2></div>
    <div class="zcards">{zcards(idf)}</div>
    <div class="section__head reveal" style="margin-top:72px">{eyebrow("Hauts-de-France")}<h2 class="h2">Et tout le département<br><em>de l'Oise.</em></h2></div>
    <div class="zcards">{zcards(oise)}</div>
  </div>
</section>

{cta_band("Vous ne savez pas si nous couvrons votre commune ?<br><em>Posez-nous la question.</em>", "Un appel ou un message WhatsApp suffit : nous vous répondons rapidement.")}

{contact_section()}'''
    page("zones-intervention.html", title="Zones d'intervention : Île-de-France et Oise | Derapest",
         desc="Derapest intervient pour la dératisation, la désinsectisation et la désinfection à Paris, dans les 77, 78, 91, 92, 93, 94, 95 et dans l'Oise (60). Devis gratuit.",
         body=body, active="zones", schemas=[breadcrumb_ld(crumbs)], priority="0.8")


# ------------------------------------------------------------------ autres pages


def build_pro():
    crumbs = [("Accueil", "index.html"), ("Professionnels", "professionnels.html")]
    sectors = [
        ("Restauration", "Restaurants, cuisines centrales, traiteurs : un plan de lutte suivi, intégré à votre plan de maîtrise sanitaire.", "cafards-blattes"),
        ("Commerces alimentaires", "Boulangeries, supérettes, primeurs, boucheries : interventions hors heures d'ouverture.", "deratisation"),
        ("Copropriétés & bailleurs", "Parties communes, caves, locaux poubelles, colonnes : traitements coordonnés et rapports par logement.", "punaises-de-lit"),
        ("Entrepôts & logistique", "Postes d'appâtage cartographiés, monitoring, fumigation des marchandises.", "fumigation"),
        ("Industrie agroalimentaire", "Plans de lutte conformes aux exigences d'audit, traçabilité complète.", "desinsectisation"),
        ("Établissements recevant du public", "Hôtels, écoles, crèches, résidences seniors, bureaux : discrétion et produits adaptés.", "desinfection"),
    ]
    sec_html = "".join(
        f'<article class="sector reveal"><span class="sector__ic">{I[ic]}</span><h3>{t}</h3><p>{d}</p></article>' for t, d, ic in sectors
    )
    perks = [
        ("Plan de lutte sur mesure", "Nombre de passages, emplacements des postes et produits définis selon votre activité et vos contraintes."),
        ("Traçabilité complète", "Plan d'implantation des postes, fiches produits, rapport écrit après chaque passage : tout ce qu'attend un auditeur."),
        ("Interventions discrètes", "Passages tôt le matin, en soirée ou le week-end, pour ne jamais perturber votre activité."),
        ("Réactivité", "En cas d'activité anormale entre deux passages, nous intervenons en priorité."),
    ]
    perks_html = "".join(f'<li class="perk reveal"><span>{I["shield"]}</span><div><h3>{t}</h3><p>{d}</p></div></li>' for t, d in perks)
    faq = [
        ("Un plan de lutte contre les nuisibles est-il obligatoire ?", "Pour les établissements manipulant des denrées alimentaires, la réglementation hygiène (Paquet hygiène, démarche HACCP) impose de maîtriser le risque nuisibles et d'en conserver la trace. Un contrat avec un professionnel est le moyen le plus simple de le démontrer."),
        ("Combien de passages par an ?", "Cela dépend de l'activité et du niveau de risque : souvent entre 4 et 12 passages par an. Nous le définissons ensemble après une visite initiale."),
        ("Recevez-vous un rapport après chaque visite ?", "Oui, un compte rendu écrit est envoyé par e-mail après chaque passage : postes contrôlés, consommations, produits utilisés, recommandations."),
        GENERIC_FAQ[0],
    ]
    body = f'''{page_hero(crumbs, "Contrats professionnels", "Professionnels :<br><em>un plan anti-nuisibles qui tient l'audit.</em>", "Restaurants, commerces, copropriétés, entrepôts, industrie : nous mettons en place un plan de lutte suivi, traçable et discret, en Île-de-France et dans l'Oise.", "s3.webp", "Infestation de blattes en cuisine", ["Rapport après chaque passage", "Interventions hors horaires", "Île-de-France &amp; Oise"], "Demander une visite gratuite")}

<section class="section">
  <div class="container">
    <div class="section__head reveal">{eyebrow("Secteurs")}<h2 class="h2">Une réponse adaptée<br><em>à chaque activité.</em></h2></div>
    <div class="sectors">{sec_html}</div>
  </div>
</section>

<section class="section section--grey">
  <div class="container duo">
    <div class="duo__main reveal">
      {eyebrow("Contrat de suivi")}
      <h2 class="h2">Ce que comprend<br><em>votre contrat.</em></h2>
      <ul class="perks">{perks_html}</ul>
    </div>
    <aside class="tipcard tipcard--dark reveal">
      <span class="tipcard__ic">{I["doc"]}</span>
      <h3>Visite initiale gratuite</h3>
      <p>Un technicien visite votre site, évalue les risques et vous remet une proposition de contrat détaillée, sans engagement.</p>
      {btn("#devis", "Planifier la visite", "green", "btn--block")}
      <a class="tipcard__tel" href="tel:{SITE["phone_intl"]}">{I["phone"]} {SITE["phone_display"]}</a>
    </aside>
  </div>
</section>

{steps_section(GENERIC_STEPS, 'Un suivi régulier,<br><em>sans surprise.</em>', "Fonctionnement")}

{faq_section(faq, 'Professionnels :<br><em>vos questions.</em>')}

{contact_section("Contrat professionnel", 'Parlons de<br><em>votre établissement.</em>')}'''
    page("professionnels.html", title="Dératisation et désinsectisation pour professionnels IDF & Oise | Derapest",
         desc="Contrats anti-nuisibles pour restaurants, commerces, copropriétés, entrepôts et industrie en Île-de-France et dans l'Oise. Traçabilité, rapports, visite gratuite.",
         body=body, active="pro", schemas=[breadcrumb_ld(crumbs), faq_ld(faq)], priority="0.8",
         og_image="assets/img/s3.webp", preload_img="s3.webp")


def build_contact():
    crumbs = [("Accueil", "index.html"), ("Contact", "contact.html")]
    body = f'''<section class="phero phero--compact">
  <div class="phero__glow" aria-hidden="true"></div>
  <div class="container">
    {breadcrumb_html(crumbs)}
    <p class="eyebrow eyebrow--glass"><i></i>Contact &amp; devis gratuit</p>
    <h1 class="phero__title">Parlons de<br><em>votre problème de nuisibles.</em></h1>
    <p class="phero__lead">Le moyen le plus rapide : un appel ou un message WhatsApp. Vous pouvez aussi remplir le formulaire ci-dessous.</p>
    <div class="quick">
      <a class="quick__card" href="tel:{SITE["phone_intl"]}"><span>{I["phone"]}</span><small>Appel direct</small><strong>{SITE["phone_display"]}</strong></a>
      <a class="quick__card" href="{WA_URL}" target="_blank" rel="noopener"><span>{I["wa"]}</span><small>WhatsApp</small><strong>Écrire maintenant</strong></a>
      <a class="quick__card" href="mailto:{SITE["email"]}"><span>{I["mail"]}</span><small>E-mail</small><strong>{SITE["email"]}</strong></a>
    </div>
  </div>
</section>
{contact_section("", 'Votre devis<br><em>gratuit.</em>')}
{zones_strip("Nous intervenons dans les 8 départements d'Île-de-France et dans l'Oise.", "Où intervenons-nous ?")}'''
    page("contact.html", title="Contact et devis gratuit | Derapest Anti-Nuisibles",
         desc="Contactez Derapest pour un devis gratuit : dératisation, désinsectisation, désinfection en Île-de-France et dans l'Oise. Téléphone, WhatsApp ou formulaire.",
         body=body, active="contact", schemas=[breadcrumb_ld(crumbs)], priority="0.7")


def build_legal():
    crumbs = [("Accueil", "index.html"), ("Mentions légales", "mentions-legales.html")]
    todo = '<mark>[à compléter]</mark>'
    body = f'''<section class="phero phero--compact">
  <div class="phero__glow" aria-hidden="true"></div>
  <div class="container">{breadcrumb_html(crumbs)}<h1 class="phero__title">Mentions <em>légales.</em></h1></div>
</section>
<section class="section"><div class="container container--narrow prose legal">
  <h2>Éditeur du site</h2>
  <p>{SITE["full_name"]} — raison sociale {todo}<br>Forme juridique et capital {todo}<br>SIRET {todo}<br>Adresse du siège {todo}<br>Téléphone : {SITE["phone_display"]} — E-mail : {SITE["email"]}<br>Directeur de la publication {todo}</p>
  <h2>Certifications</h2>
  <p>Numéro de certificat Certibiocide (application de produits biocides) {todo}</p>
  <h2>Hébergement</h2>
  <p>Hébergeur, adresse et téléphone {todo}</p>
  <h2>Données personnelles</h2>
  <p>Les informations transmises via le formulaire ou WhatsApp sont utilisées uniquement pour répondre à votre demande et établir un devis. Elles ne sont ni cédées ni revendues. Conformément au RGPD, vous disposez d'un droit d'accès, de rectification et de suppression de vos données en écrivant à {SITE["email"]}.</p>
  <h2>Propriété intellectuelle</h2>
  <p>Les contenus de ce site (textes, logo, visuels) sont la propriété de {SITE["full_name"]} ou de leurs auteurs respectifs. Toute reproduction sans autorisation est interdite.</p>
</div></section>'''
    page("mentions-legales.html", title="Mentions légales | Derapest", desc="Mentions légales du site Derapest Anti-Nuisibles.",
         body=body, robots="noindex, follow")


def build_404():
    body = f'''<section class="phero phero--compact phero--center">
  <div class="phero__glow" aria-hidden="true"></div>
  <div class="container">
    <p class="eyebrow eyebrow--glass"><i></i>Erreur 404</p>
    <h1 class="phero__title">Cette page<br><em>a été éradiquée.</em></h1>
    <p class="phero__lead">La page demandée n'existe pas ou a été déplacée.</p>
    <div class="phero__ctas">{btn("index.html", "Retour à l'accueil", "green")}{btn("contact.html", "Demander un devis", "light")}</div>
  </div>
</section>'''
    page("404.html", title="Page introuvable | Derapest", desc="Cette page n'existe pas.", body=body, robots="noindex, follow")



# ------------------------------------------------------------------ carte 3D des zones


def zone_map():
    M = MAP
    zbyn = {z["num"]: z for z in ZONES}
    small = {"75", "92", "93", "94"}
    land = "".join(f'<path d="{d["d"]}"/>' for d in M["main"].values())
    nei = "".join(f'<path d="{d}"/>' for d in M["nei"].values())
    layers = "".join(f'<use href="#zm-land" y="{i}" style="--i:{i}"/>' for i in range(14, 0, -1))
    deps = "".join(
        f'<a href="{zone_file(zbyn[c])}" class="zmap__dep" aria-label="{escape(zbyn[c]["name"])} ({c})"><path d="{d["d"]}"/></a>'
        for c, d in M["main"].items()
    )
    labels = ""
    for c, d in M["main"].items():
        x, y = d["c"]
        r, fs = (12, 10.5) if c in small else (18, 14)
        labels += f'<g class="zmap__lbl{" zmap__lbl--s" if c in small else ""}" transform="translate({x} {y})"><circle r="{r}"/><text dy=".36em" font-size="{fs}">{c}</text></g>'
    left = {"Cergy"}
    below = {"Versailles"}
    pins = "".join(
        f'<g class="zmap__pin" transform="translate({x} {y})"><circle class="zmap__pulse" r="4"/><circle r="3.4"/>'
        + (f'<text y="15" dy=".35em" text-anchor="middle">{n}</text></g>' if n in below else f'<text x="{-8 if n in left else 8}" dy=".35em" text-anchor="{"end" if n in left else "start"}">{n}</text></g>')
        for n, x, y in M["cities"] if n != "Paris"
    )
    F = M["france"]
    chips = "".join(f'<a class="zmap__chip" href="{zone_file(z)}"><b>{z["num"]}</b>{z["name"]}</a>' for z in ZONES)
    return f"""<section class="zmap" id="zones">
  <div class="zmap__bg" aria-hidden="true"></div>
  <div class="container zmap__grid">
    <div class="zmap__text reveal">
      <p class="eyebrow zmap__eyebrow"><i></i>Zones d'intervention</p>
      <h2 class="h2">Toute l'Île-de-France<br><em>et l'Oise.</em></h2>
      <p class="zmap__lead">Paris, petite et grande couronne, et tout le département de l'Oise : nos techniciens interviennent chez vous, en logement comme en local professionnel.</p>
      <div class="zmap__chips">{chips}</div>
      <div class="zmap__ctas">{btn("#devis", "Devis gratuit", "green")}<a class="zmap__tel" href="tel:{SITE["phone_intl"]}">{I["phone"]}{SITE["phone_display"]}</a></div>
    </div>
    <div class="zmap__stage reveal" id="zmapStage">
      <div class="zmap__shadow" aria-hidden="true"></div>
      <div class="zmap__tilt" id="zmapTilt">
        <svg class="zmap__svg" viewBox="0 0 {M["W"]} {M["H"]}" role="img" aria-label="Carte des zones d'intervention : Île-de-France et Oise">
          <defs><linearGradient id="zm-grad" x1="0" y1="0" x2=".35" y2="1"><stop offset="0" stop-color="#5fd21f"/><stop offset="1" stop-color="#2f9410"/></linearGradient><g id="zm-land">{land}</g></defs>
          <g class="zmap__nei">{nei}</g>
          <g class="zmap__ext">{layers}</g>
          <g class="zmap__deps">{deps}</g>
          <g class="zmap__pins">{pins}</g>
          <g class="zmap__lbls">{labels}</g>
        </svg>
      </div>
      <div class="zmap__inset">
        <svg viewBox="-6 -6 {F["W"] + 12} {F["H"] + 12}" aria-hidden="true"><path class="zmap__fr" d="{F["d"]}"/><path class="zmap__frhl" d="{F["hl"]}"/></svg>
        <span><b>9</b> départements<br>couverts</span>
      </div>
      <div class="zmap__badge">{I["bolt"]}<span><b>24h/24 – 7j/7</b>Intervention rapide</span></div>
    </div>
  </div>
</section>"""


# ------------------------------------------------------------------ accueil


def build_home():
    srv_cards = "".join(card(s) for s in SERVICES)
    pests = "".join(
        f'<a class="pest" href="{p["slug"]}.html"><img src="assets/img/{p["img"]}" alt="{escape(p["img_alt"])}" loading="lazy"><div class="pest__body"><small>{p["kicker"]}</small><h3>{p["nav"]}</h3><p>{p["short"]}</p><span class="pest__more">Voir le traitement {I["arrow"]}</span></div></a>'
        for p in PESTS
    ) + f'<a class="pest" href="deratisation.html"><img src="assets/img/s9.webp" alt="Fouine sortant d\'une souche" loading="lazy"><div class="pest__body"><small>Rongeurs</small><h3>Rats, souris &amp; mulots</h3><p>Combles, caves, cuisines : on traite et on rebouche.</p><span class="pest__more">Voir le traitement {I["arrow"]}</span></div></a>'
    zcards = "".join(
        f'<a class="zcard reveal" href="{zone_file(z)}"><span class="zcard__num">{z["num"]}</span><h3>{z["name"]}</h3><p>{", ".join(z["cities"][:3])}…</p><span class="zcard__more">Voir {I["arrow"]}</span></a>'
        for z in ZONES
    )
    choices = "".join(
        f'<a class="choice" href="{s["slug"]}.html"><span class="choice__icon">{I[s["slug"]]}</span><span><strong>{lbl}</strong><small>{s["nav"]}</small></span></a>'
        for s, lbl in zip(SERVICES, ["Rats &amp; souris", "Insectes", "Assainir un lieu", "Marchandises"])
    )
    depts = "".join(f'<a href="{zone_file(z)}" title="{escape(z["name"])}">{z["num"]}<small>{z["name"]}</small></a>' for z in ZONES)
    faq = GENERIC_FAQ + [
        ("Dans quels départements intervenez-vous ?", "Dans les 8 départements d'Île-de-France (Paris, Seine-et-Marne, Yvelines, Essonne, Hauts-de-Seine, Seine-Saint-Denis, Val-de-Marne, Val-d'Oise) et dans l'Oise."),
        ("Combien de passages faut-il pour venir à bout d'une infestation ?", "Cela dépend du nuisible et de l'ampleur du problème. Certains traitements se règlent en une intervention, d'autres (punaises de lit, rongeurs installés) demandent plusieurs passages. Le nombre est annoncé après le diagnostic."),
    ]
    body = f'''<section class="hero">
  <div class="hero__bg"><img src="assets/img/hero.webp" alt="Technicien Derapest en combinaison effectuant un traitement" fetchpriority="high"></div>
  <div class="hero__content">
    <p class="eyebrow eyebrow--glass"><i></i>Dératisation · Désinsectisation · Désinfection</p>
    <h1 class="hero__title">
      <span class="line"><span>Intervention rapide</span></span>
      <span class="line"><span>à Paris et en Île-de-France</span></span>
      <span class="line"><span><em>et dans l'Oise.</em></span></span>
    </h1>
    <p class="hero__lead">Rats, souris, cafards, punaises de lit, guêpes : des techniciens habilités interviennent chez vous avec des produits homologués et un traitement adapté à chaque situation.</p>
    <div class="hero__ctas">
      {btn("#devis", "Devis gratuit", "green")}
      <a class="hero__tel" href="tel:{SITE["phone_intl"]}">{I["phone"]}<span>{SITE["phone_display"]}</span></a>
    </div>
    <nav class="hero__depts" aria-label="Départements desservis"><span>{I["pin"]}Départements :</span>{depts}</nav>
  </div>
  <div class="hero__panel">
    <div class="hero__panel-head"><h2>Quel est votre problème ?</h2><p>Choisissez, on vous oriente immédiatement.</p></div>
    <div class="hero__choices">{choices}</div>
  </div>
</section>

<div class="marquee" aria-hidden="true"><div class="marquee__track">{"".join(f'<b class="marquee__item"><i class="marquee__ic">{I["m_" + ic]}</i><span>{w}</span></b>' for w, ic in MARQUEE * 2)}</div></div>

<section class="section section--grey" id="engagements">
  <div class="container">
    <div class="about reveal">
      <div class="about__media">
        <img src="assets/img/hero.webp" alt="Traitement anti-nuisibles par pulvérisation" loading="lazy">
        <span class="about__badge">{I["shield"]}Techniciens habilités</span>
        <div class="about__caption"><strong>Derapest Anti-Nuisibles</strong><span>Île-de-France · Oise</span></div>
      </div>
      <div class="about__body">
        {eyebrow("Notre engagement")}
        <h2 class="h2">Un regard expert.<br><em>À vos côtés.</em></h2>
        <p class="lead">Une infestation ne se règle pas avec une bombe du commerce. Elle se règle avec un diagnostic, la bonne méthode et un vrai suivi.</p>
        <p class="muted">Chaque intervention est réalisée par des techniciens habilités et diplômés. Le traitement est choisi en tenant compte de la sécurité des personnes, des animaux, des biens et de l'environnement, avec des produits agréés et homologués, dans le respect strict de la réglementation.</p>
        <div class="stats">
          <div class="stat"><small>Départements</small><strong><em>9</em></strong><span>les 8 d'Île-de-France et l'Oise</span></div>
          <div class="stat"><small>Nos métiers</small><strong><em>4</em></strong><span>dératisation, désinsectisation, désinfection, fumigation</span></div>
        </div>
        <div class="about__cta">{btn("#prestations", "Découvrir nos prestations", "dark")}{btn("#devis", "Devis gratuit", "outline")}</div>
      </div>
    </div>
    <div class="pillars">
      <article class="pillar reveal"><span class="pillar__num">01</span><h3>Interventions</h3><p>Réalisées uniquement par des techniciens habilités et diplômés.</p></article>
      <article class="pillar reveal"><span class="pillar__num">02</span><h3>Sécurité</h3><p>Respect strict de la législation, produits agréés et homologués, formations régulières.</p></article>
      <article class="pillar reveal"><span class="pillar__num">03</span><h3>Maîtrise</h3><p>Un traitement choisi pour protéger les personnes, les animaux, les biens et l'environnement.</p></article>
      <article class="pillar reveal"><span class="pillar__num">04</span><h3>Suivi</h3><p>Rotation des molécules et compte rendu de chaque intervention envoyé par e-mail.</p></article>
    </div>
  </div>
</section>

<section class="section" id="prestations">
  <div class="container">
    <div class="section__head section__head--row reveal">
      <div>{eyebrow("Nos prestations")}<h2 class="h2">Quatre métiers,<br><em>une seule exigence.</em></h2></div>
      {btn("professionnels.html", "Offre professionnels", "outline")}
    </div>
    <div class="cards cards--4">{srv_cards}</div>
  </div>
</section>

{cta_band("Un nuisible chez vous ?<br><em>Chaque jour compte.</em>", "Rongeurs, punaises, cafards : plus on attend, plus l'infestation s'étend. Appelez-nous, on vous propose une date d'intervention.", "Intervention rapide")}

<section class="section section--grey" id="nuisibles">
  <div class="container">
    <div class="section__head section__head--row reveal">
      <div>{eyebrow("Nuisibles traités")}<h2 class="h2">Chaque nuisible<br><em>a son point faible.</em></h2></div>
      <div class="slider-nav">
        <button type="button" id="pestPrev" aria-label="Précédent"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M15 6l-6 6 6 6"/></svg></button>
        <button type="button" id="pestNext" aria-label="Suivant"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 6l6 6-6 6"/></svg></button>
      </div>
    </div>
  </div>
  <div class="pests" id="pests">{pests}</div>
</section>

{steps_section(GENERIC_STEPS)}

{zone_map()}

<section class="section section--grey section--tight">
  <div class="container audience">
    <a class="audience__card reveal" href="#devis"><small>Particuliers</small><h3>Maison, appartement, cave, jardin</h3><p>Une intervention discrète, expliquée clairement, sans danger pour votre famille ni vos animaux.</p><span class="audience__more">Demander un devis {I["arrow"]}</span></a>
    <a class="audience__card audience__card--dark reveal" href="professionnels.html"><small>Professionnels</small><h3>Restaurants, commerces, entrepôts, copropriétés</h3><p>Contrats de suivi, rapports à chaque passage, interventions hors horaires.</p><span class="audience__more">Voir l'offre pro {I["arrow"]}</span></a>
  </div>
</section>

{faq_section(faq, 'Tout ce que vous<br><em>vous demandez.</em>')}

{contact_section()}'''
    page("index.html",
         title="Dératisation Paris, Île-de-France & Oise : intervention rapide | Derapest",
         desc="Intervention rapide à Paris, en Île-de-France et dans l'Oise : dératisation, désinsectisation, désinfection, fumigation. Techniciens habilités, devis gratuit.",
         body=body, active="home", schemas=[faq_ld(faq)], priority="1.0", preload_img="hero.webp")


# ------------------------------------------------------------------ sitemap / robots


def build_seo_files():
    urls = "\n".join(
        f"  <url><loc>{SITE['url']}/{'' if f == 'index.html' else f}</loc><lastmod>{TODAY}</lastmod><priority>{p}</priority></url>"
        for f, p in sorted(PAGES, key=lambda x: -float(x[1]))
    )
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n')
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(f"User-agent: *\nAllow: /\nDisallow: /build/\n\nSitemap: {SITE['url']}/sitemap.xml\n")


if __name__ == "__main__":
    build_home()
    for p in ALL:
        build_service(p)
    for z in ZONES:
        build_zone(z)
    build_zones_hub()
    build_pro()
    build_contact()
    build_legal()
    build_404()
    build_seo_files()
    print(f"{len(PAGES)} pages indexables + mentions légales + 404 générées dans {ROOT}")
