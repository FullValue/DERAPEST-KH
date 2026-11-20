# Audit SEO, GEO et performance : derapest.fr

Audit réalisé le 20/11/2026 sur les 23 pages du site (21 indexables).

## 1. Constat de départ

| Domaine | État avant | Gravité |
|---|---|---|
| Titres `<title>` | 17 pages sur 23 dépassaient 60 caractères (coupés dans Google) | Moyenne |
| Meta descriptions | 6 pages au-delà de 158 caractères | Faible |
| Images | 2,1 Mo de photos (jusqu'à 325 Ko par photo), 8 images sans dimensions sur l'accueil (décalages de mise en page) | Forte |
| Polices | Google Fonts chargé depuis un serveur externe, bloquant l'affichage | Moyenne |
| Préloader | Bloquait l'affichage au moins 1,8 s, jusqu'à 6,5 s → LCP mobile mesuré à 3,7 s | Forte |
| Lien « Accueil » | Pointait vers `index.html` (doublon de `/`) | Faible |
| Données structurées | LocalBusiness minimal, pas de schéma WebSite | Moyenne |
| Moteurs IA (GEO) | Pas de `llms.txt`, aucun signal pour les robots IA | Moyenne |
| Cache et sécurité | Aucun en-tête de cache ni de sécurité | Moyenne |
| Base saine | 1 H1 par page, aucun doublon de titre ou description, FAQPage + BreadcrumbList + Service, sitemap, canonical, maillage interne complet, ~1 000 mots par page | ✓ |

## 2. Ce qui a été corrigé

### Vitesse
- **Polices hébergées sur le site** (Exo, 2 fichiers variables de 22 Ko, préchargés). Plus aucun appel à Google Fonts.
- **Photos recompressées et redimensionnées** : 2,1 Mo → 0,8 Mo, versions de 560 px pour les cartes et de 900 px pour le hero mobile, servies via `srcset`.
- **Logo en WebP** : 90 Ko → 14 Ko.
- **Dimensions ajoutées automatiquement** sur toutes les images, ce qui supprime les décalages de mise en page.
- **Image principale préchargée en priorité** sur chaque page (`fetchpriority="high"`), décodage asynchrone pour les autres.
- **Préloader raccourci** : 900 ms au minimum, 3 s au maximum, toujours affiché une seule fois par visite.
- **Texte principal et titres visibles dès le premier affichage** : l'animation de glissement est gardée, le fondu est retiré. Le LCP n'attend plus la fin des animations.
- **Cache long sur les fichiers statiques** (polices, CSS et JS versionnés pendant 1 an, images pendant 30 jours) et en-têtes de sécurité.

Mesures en mobile (412 px), première visite avec préloader, réseau non compris :

| Indicateur | Avant | Après |
|---|---|---|
| LCP accueil | 3,7 s | ~0,1 s |
| LCP page prestation | n/m | ~0,1 s |
| CLS | 0,046 | 0,022 |
| Poids au premier affichage (hors HTML) | 443 Ko | ≈ 200 Ko |

### SEO technique
- **Titres réécrits** sur 17 pages : mot-clé en tête, ≤ 60 caractères. Exemple : « Dératisation Seine-et-Marne (77) : rats, insectes | Derapest ».
- **Descriptions ramenées sous 158 caractères**, avec la mention des 30 ans d'expérience sur l'accueil et les pages départements.
- **LocalBusiness enrichi** : description, horaires 24h/24 et 7j/7, point de contact, catalogue des 8 prestations, slogan.
- **Schéma WebSite** sur l'accueil.
- **Balises Open Graph et Twitter complétées** (image, alt, titre, description).
- **Liens « Accueil » vers l'URL canonique `/`**, et redirection 301 de `/index.html` vers `/`.
- **Domaines** : derapest.fr, derapest.com et www.derapest.com redirigent en 301 vers www.derapest.fr.

### GEO (ChatGPT, Perplexity, Claude, Google AI Overviews)
- **`/llms.txt`** : fiche synthétique de l'entreprise (métier, zones, expérience, contact, prestations, nuisibles, FAQ), régénérée à chaque build.
- **`robots.txt`** : autorisation explicite de GPTBot, OAI-SearchBot, ClaudeBot, PerplexityBot, Google-Extended, Applebot-Extended, etc.
- **Faits clés répétés de façon cohérente** (30 ans d'expérience, 9 départements, 4 métiers) dans le contenu, le schéma et `llms.txt`. C'est ce que les IA citent.

## 3. Plan d'action : ce qui reste à faire (de ton côté)

### Priorité 1 : cette semaine (impact fort)
1. **Google Search Console** : ajoute la propriété `derapest.fr` (validation DNS chez IONOS), puis soumets `https://www.derapest.fr/sitemap.xml`. Sans ça, Google mettra plusieurs semaines à découvrir le site.
2. **Fiche Google Business Profile** : c'est le facteur n°1 pour apparaître dans le « pack local » (la carte). Pour une entreprise sans boutique, crée-la en mode « zone desservie » avec les 9 départements, la catégorie principale « Service d'extermination et de lutte contre les nuisibles », le téléphone, le site et des photos réelles.
3. **Mentions légales** : 5 champs sont encore « [à compléter] » (forme juridique, SIRET, siège, directeur de publication, hébergeur). C'est une obligation légale (LCEN), et un signal de confiance pour Google et les IA. Hébergeur : déjà rempli (Vercel Inc.).
4. **Bing Webmaster Tools** : importe la propriété depuis Search Console en un clic. ChatGPT et Copilot s'appuient sur l'index Bing.

### Priorité 2 : ce mois-ci
5. **Avis Google** : demande un avis à chaque client satisfait (lien direct depuis la fiche). Viser 20 avis ou plus avec réponse systématique.
6. **Annuaires (citations NAP)** : PagesJaunes, Yelp, Hoodspot, Mappy, 118712, Cylex, Apple Plans, Bing Places, avec exactement le même nom, téléphone et site partout.
7. **Preuves d'expertise** : numéro de certificat **Certibiocide**, assurance RC pro, éventuelle adhésion à la **CS3D** (chambre syndicale du secteur). À afficher sur le site : je peux les intégrer dès que tu me donnes les infos.
8. **Vraies photos** de l'équipe et des interventions, en remplacement des photos de banque d'images. Fort impact sur la conversion et sur la fiche Google.

### Priorité 3 : dans les 3 mois (croissance)
9. **Pages villes** pour les grandes communes (Boulogne-Billancourt, Saint-Denis, Versailles, Argenteuil, Montreuil, Beauvais…), uniquement avec un contenu réellement local.
10. **Guides pratiques** (blog) qui répondent aux questions que les gens posent aux IA : « comment savoir si j'ai des punaises de lit », « que faire face à un nid de frelons asiatiques », « dératisation : à la charge du propriétaire ou du locataire ? ».
11. **Fourchettes de prix indicatives** par prestation : très demandées par les internautes et fortement reprises par les IA.
12. **Suivi** : contrôle mensuel des positions dans Search Console sur « dératisation + département » et « punaises de lit + ville ».

## 4. Pour garder le site optimisé
- Les contenus se modifient dans `build/data.py`, puis on lance `python3 build/build.py`. Les dimensions d'images, le `srcset`, le sitemap, `robots.txt` et `llms.txt` sont régénérés automatiquement.
- Pour une nouvelle photo, exporte-la en WebP de 900 px de large et ajoute une version `-560.webp` : le site l'utilisera tout seul.
