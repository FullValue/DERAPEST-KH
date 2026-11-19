# -*- coding: utf-8 -*-
"""
DERAPEST — contenu du site.
Modifiez ce fichier puis relancez :  python3 build/build.py
"""

# ------------------------------------------------------------------
# COORDONNÉES — à remplacer par les vraies avant la mise en ligne
# ------------------------------------------------------------------
SITE = {
    "url": "https://www.derapest.fr",        # domaine définitif (canonical, sitemap, schema)
    "name": "Derapest",
    "full_name": "Derapest Anti-Nuisibles",
    "phone_display": "07 62 75 75 72",
    "phone_intl": "+33762757572",
    "whatsapp": "33762757572",               # format international, sans + ni espaces
    "email": "contact@derapest.com",
    "wa_message": "Bonjour Derapest, j'ai un problème de nuisibles et je souhaite un devis.",
}

# ------------------------------------------------------------------
# LES 3 PROMESSES affichées tout en haut de chaque page.
# N'écrivez que ce que vous pouvez tenir. Exemples si c'est vrai :
#   ("Intervention 24h/24 – 7j/7", "bolt"), ("Traitement garanti", "shield")
# Icônes disponibles : "bolt", "shield", "doc", "phone", "pin"
# ------------------------------------------------------------------
PROMISES = [
    ("Intervention 24h/24 – 7j/7", "bolt"),
    ("Traitement garanti", "shield"),
    ("Devis gratuit et rapide", "doc"),
]

# ------------------------------------------------------------------
# PRESTATIONS (métiers) et NUISIBLES (pages ciblées)
# ------------------------------------------------------------------
SERVICES = [
    {
        "slug": "deratisation",
        "kind": "service",
        "nav": "Dératisation",
        "short": "Rats, souris, mulots : on localise, on traite, on suit jusqu'à disparition.",
        "title": "Dératisation Île-de-France & Oise : rats et souris | Derapest",
        "desc": "Rats ou souris chez vous ? Dératisation en Île-de-France et dans l'Oise : diagnostic, postes d'appâtage sécurisés, rebouchage et suivi. Devis gratuit.",
        "kicker": "Rongeurs",
        "h1": "Des rats ou des souris chez vous ?<br><em>On s'en occupe, pour de bon.</em>",
        "lead": "Grattements la nuit, crottes, câbles rongés : un rongeur n'est jamais seul bien longtemps. Nos techniciens localisent les passages, traitent avec des postes sécurisés et suivent l'infestation jusqu'à sa disparition complète.",
        "img": "photos/deratisation.webp",
        "img_alt": "Rat posé sur une planche de bois",
        "signs_title": "Les signes qui ne trompent pas",
        "signs": [
            ("Crottes et urine", "Petites crottes noires le long des murs, dans les placards ou derrière l'électroménager, avec une odeur d'ammoniaque persistante."),
            ("Bruits nocturnes", "Grattements et trottinements dans les combles, les cloisons ou les faux plafonds, surtout la nuit."),
            ("Dégâts visibles", "Emballages percés, câbles, gaines et isolants rongés, traces de passage grasses sur les plinthes."),
        ],
        "risks_title": "Pourquoi il ne faut pas attendre",
        "risks_text": "Une souris peut avoir jusqu'à une dizaine de portées par an. Au-delà de la gêne, les rongeurs contaminent les denrées et dégradent le bâti.",
        "risks": [
            "Transmission de maladies (leptospirose, salmonellose) par l'urine et les déjections",
            "Câbles électriques rongés : risque de court-circuit et d'incendie",
            "Isolants, boiseries et canalisations dégradés",
            "Denrées et stocks souillés, à jeter",
        ],
        "steps": [
            ("Diagnostic", "Identification de l'espèce, des points d'entrée, des zones de nidification et du niveau d'infestation."),
            ("Traitement", "Pose de postes d'appâtage sécurisés fermés à clé et/ou de pièges mécaniques, placés sur les axes de passage."),
            ("Rebouchage", "Conseils et, si besoin, obturation des accès : gaines, trous, bas de portes, aérations."),
            ("Suivi", "Contrôle des consommations, rotation des molécules et compte rendu écrit envoyé par e-mail."),
        ],
        "solutions_title": "Nos techniques de dératisation",
        "solutions": [
            "Postes d'appâtage en PVC fermés à clé, sans danger pour les enfants et animaux",
            "Pièges mécaniques pour les zones sensibles (cuisines, crèches, commerces)",
            "Répulsifs à base d'huiles essentielles en complément",
            "Rotation des molécules pour éviter les résistances",
            "Contrats de suivi pour les professionnels et les copropriétés",
        ],
        "tips": [
            "Stockez les aliments (y compris croquettes) dans des boîtes hermétiques",
            "Sortez les poubelles régulièrement et fermez les bacs",
            "Bouchez les trous de plus de 6 mm autour des gaines et canalisations",
            "Désencombrez caves, garages et combles",
        ],
        "faq": [
            ("Combien de passages faut-il pour une dératisation ?", "En général deux à trois passages : la pose, un ou deux contrôles pour vérifier la consommation des appâts et réajuster. Le nombre exact est annoncé après le diagnostic."),
            ("Les appâts sont-ils dangereux pour mon chien ou mon chat ?", "Les appâts sont placés dans des postes sécurisés fermés à clé, inaccessibles aux animaux domestiques et aux enfants. Dans les zones sensibles, nous privilégions les pièges mécaniques."),
            ("Rat ou souris : comment faire la différence ?", "La crotte de souris mesure 3 à 6 mm, celle du rat 1 à 2 cm. Le rat fréquente plutôt caves, égouts et rez-de-chaussée ; la souris grimpe partout, jusque dans les étages."),
            ("Le propriétaire ou le locataire doit-il payer la dératisation ?", "Cela dépend de l'origine de l'infestation et du bail. Pour une copropriété, les parties communes relèvent du syndic. Nous établissons un rapport d'intervention qui facilite ces démarches."),
        ],
        "related": ["desinfection", "punaises-de-lit", "cafards-blattes"],
    },
    {
        "slug": "desinsectisation",
        "kind": "service",
        "nav": "Désinsectisation",
        "short": "Cafards, punaises, puces, fourmis, mites : un traitement par espèce.",
        "title": "Désinsectisation Île-de-France & Oise : traitement insectes | Derapest",
        "desc": "Cafards, punaises de lit, puces, fourmis, mites, guêpes : désinsectisation professionnelle en Île-de-France et dans l'Oise. Produits homologués, devis gratuit.",
        "kicker": "Insectes",
        "h1": "Des insectes qui s'installent ?<br><em>On cible, on traite, on prévient.</em>",
        "lead": "Chaque insecte a son mode de vie, donc son traitement. Pulvérisation, nébulisation, gel, appâts ou fumigation : nous choisissons la technique la plus efficace selon l'espèce, les lieux et leurs occupants.",
        "img": "photos/desinsectisation.webp",
        "img_alt": "Technicien pulvérisant un traitement insecticide",
        "signs_title": "Quand faut-il faire appel à un professionnel ?",
        "signs": [
            ("Ils reviennent", "Les bombes et pièges du commerce n'ont qu'un effet temporaire : les insectes réapparaissent quelques jours plus tard."),
            ("Ils se multiplient", "Vous en voyez en plein jour, dans plusieurs pièces : c'est le signe d'une colonie bien installée."),
            ("Ils piquent", "Piqûres alignées au réveil, démangeaisons, réactions cutanées : punaises ou puces sont probablement en cause."),
        ],
        "risks_title": "Des nuisances qui vont au-delà de la gêne",
        "risks_text": "Les insectes prolifèrent dans les endroits chauds et humides. Une infestation qui s'étend devient plus longue et plus coûteuse à traiter.",
        "risks": [
            "Blattes et fourmis contaminent les aliments et les zones de rangement",
            "Mouches : vecteurs d'agents pathogènes vers les denrées",
            "Punaises, puces, moustiques, guêpes : piqûres, allergies, démangeaisons",
            "Termites et insectes du bois : dégâts sur les charpentes et boiseries",
        ],
        "steps": [
            ("Identification", "Le technicien identifie l'espèce et localise les foyers : c'est ce qui conditionne le choix du traitement."),
            ("Préparation", "Nous vous indiquons comment préparer les lieux (linge, accès, animaux) pour un traitement efficace."),
            ("Traitement ciblé", "Pulvérisation, nébulisation, gel, appâts ou fumigation, selon l'insecte et la configuration."),
            ("Contrôle", "Second passage si nécessaire, conseils de prévention et compte rendu d'intervention."),
        ],
        "solutions_title": "Insectes traités",
        "solutions": [
            "Blattes et cafards (blatte germanique, orientale, américaine)",
            "Punaises de lit et puces",
            "Fourmis, mites alimentaires et textiles",
            "Moustiques, mouches, guêpes et frelons",
            "Insectes du bois : termites, capricornes, vrillettes",
        ],
        "tips": [
            "Ne multipliez pas les insecticides du commerce : ils dispersent souvent l'infestation",
            "Limitez l'humidité (fuites, siphons, ventilation)",
            "Contrôlez les meubles et vêtements d'occasion avant de les rentrer",
            "Nettoyez les miettes et graisses derrière l'électroménager",
        ],
        "faq": [
            ("Faut-il quitter le logement pendant le traitement ?", "Pour la plupart des traitements, il faut quitter les pièces traitées pendant quelques heures, avec vos animaux. Le technicien vous indique la durée exacte et les consignes d'aération."),
            ("Le traitement est-il efficace en une seule fois ?", "Contre les cafards ou les fourmis, un passage bien ciblé suffit souvent. Contre les punaises de lit ou les puces, deux passages sont généralement nécessaires pour toucher les œufs qui éclosent après le premier traitement."),
            ("Les produits sont-ils sans danger ?", "Nous utilisons des produits biocides homologués, appliqués par des techniciens formés, à des doses maîtrisées. Les consignes de sécurité vous sont remises avant et après l'intervention."),
        ],
        "related": ["cafards-blattes", "punaises-de-lit", "guepes-frelons"],
    },
    {
        "slug": "desinfection",
        "kind": "service",
        "nav": "Désinfection",
        "short": "Assainir surfaces et volumes après infestation, sinistre ou en prévention.",
        "title": "Désinfection de locaux et logements en Île-de-France & Oise | Derapest",
        "desc": "Désinfection de logements, locaux professionnels, cuisines et parties communes en Île-de-France et dans l'Oise. Biocides homologués, intervention rapide, devis gratuit.",
        "kicker": "Hygiène",
        "h1": "Retrouvez un lieu sain,<br><em>désinfecté en profondeur.</em>",
        "lead": "Après une infestation, un logement insalubre ou en prévention dans un local recevant du public, la désinfection élimine bactéries, virus et germes sur les surfaces comme dans l'air ambiant.",
        "img": "photos/desinfection.webp",
        "img_alt": "Technicien en combinaison réalisant une nébulisation désinfectante",
        "signs_title": "Dans quels cas désinfecter ?",
        "signs": [
            ("Après une infestation", "Rongeurs, blattes ou pigeons laissent déjections et germes : une désinfection complète le traitement."),
            ("Logement insalubre", "Avant une remise en location, après un décès, un syndrome de Diogène ou un dégât des eaux."),
            ("Locaux professionnels", "Cuisines, commerces alimentaires, vestiaires, parties communes : une exigence d'hygiène continue."),
        ],
        "risks_title": "Une hygiène qui protège les occupants",
        "risks_text": "Les nuisibles sont des vecteurs de maladies : ils transportent germes et bactéries sur les surfaces et les denrées. Traiter les nuisibles sans assainir laisse ce risque en place.",
        "risks": [
            "Germes et bactéries laissés par les déjections et cadavres",
            "Odeurs persistantes dans les logements et les locaux",
            "Risque sanitaire pour les personnes fragiles (enfants, seniors)",
            "Non-conformité lors des contrôles d'hygiène pour les professionnels",
        ],
        "steps": [
            ("Évaluation", "Visite des lieux, identification des zones à risque et choix du protocole."),
            ("Nettoyage", "Retrait des souillures et déjections : un préalable indispensable à une désinfection efficace."),
            ("Désinfection", "Pulvérisation ou nébulisation de biocides homologués sur les surfaces et dans les volumes."),
            ("Restitution", "Temps d'action respecté, aération, puis remise des lieux avec un compte rendu."),
        ],
        "solutions_title": "Nos interventions de désinfection",
        "solutions": [
            "Désinfection de logements après infestation ou sinistre",
            "Cuisines professionnelles, restaurants, commerces alimentaires",
            "Parties communes, locaux poubelles, caves de copropriété",
            "Véhicules, entrepôts et zones de stockage",
            "Nébulisation pour traiter l'air et les volumes difficiles d'accès",
        ],
        "tips": [
            "Aérez quotidiennement pour limiter l'humidité",
            "Nettoyez régulièrement les locaux poubelles et les siphons",
            "Faites désinfecter après tout traitement contre les rongeurs ou les pigeons",
            "Planifiez des passages réguliers dans les locaux recevant du public",
        ],
        "faq": [
            ("Quelle différence entre nettoyage et désinfection ?", "Le nettoyage retire les salissures visibles ; la désinfection détruit les micro-organismes (bactéries, virus, champignons) grâce à des produits biocides et un temps d'action précis."),
            ("Combien de temps faut-il attendre avant de réintégrer les lieux ?", "En général quelques heures, le temps d'action et d'aération. Le technicien vous indique le délai exact selon le produit utilisé."),
            ("Intervenez-vous après un décès ou un logement très encombré ?", "Oui, nous intervenons pour la désinfection de logements insalubres. Pour un débarras complet, nous pouvons vous orienter vers des partenaires."),
        ],
        "related": ["deratisation", "desinsectisation", "fumigation"],
    },
    {
        "slug": "fumigation",
        "kind": "service",
        "nav": "Fumigation",
        "short": "Traitement par gaz des marchandises et volumes que rien d'autre n'atteint.",
        "title": "Fumigation de marchandises et locaux en Île-de-France & Oise | Derapest",
        "desc": "Fumigation (traitement par gaz) des marchandises, denrées stockées, conteneurs et locaux en Île-de-France et dans l'Oise. Protocole sécurisé, devis gratuit.",
        "kicker": "Gazage",
        "h1": "Quand les traitements classiques échouent,<br><em>la fumigation va plus loin.</em>",
        "lead": "Pulvérisations et insecticides sont parfois inadaptés, notamment dans les environnements délicats ou pour des marchandises. Le traitement par gaz pénètre au cœur des matières et atteint les parasites là où rien d'autre ne passe.",
        "img": "photos/fumigation.webp",
        "img_alt": "Entrepôt de stockage avec palettes et rayonnages",
        "signs_title": "Les situations qui demandent une fumigation",
        "signs": [
            ("Denrées stockées", "Céréales, farines, fruits secs, cacao ou tabac infestés par des insectes des denrées."),
            ("Marchandises et emballages", "Palettes, bois d'emballage, conteneurs et lots à traiter avant expédition ou stockage."),
            ("Volumes inaccessibles", "Infestations au cœur des matériaux, mobilier ancien, œuvres ou archives."),
        ],
        "risks_title": "Pourquoi choisir la fumigation",
        "risks_text": "Le gaz diffuse dans l'ensemble du volume traité, y compris à l'intérieur des produits et des matériaux, et atteint tous les stades de développement des insectes.",
        "risks": [
            "Action en profondeur, à cœur des produits",
            "Tous les stades touchés : œufs, larves, adultes",
            "Pas de manipulation de la marchandise",
            "Adapté aux environnements où la pulvérisation est exclue",
        ],
        "steps": [
            ("Étude", "Analyse du volume, de la marchandise, de l'espèce ciblée et des contraintes du site."),
            ("Confinement", "Mise sous bâche ou étanchéification du local, balisage et sécurisation de la zone."),
            ("Gazage", "Application du fumigant et maintien de la concentration pendant le temps d'exposition."),
            ("Dégazage", "Aération contrôlée, mesures de sécurité, puis restitution avec compte rendu."),
        ],
        "solutions_title": "Ce que nous traitons par fumigation",
        "solutions": [
            "Denrées alimentaires stockées et matières premières",
            "Conteneurs, palettes et bois d'emballage",
            "Silos, entrepôts et zones de stockage",
            "Mobilier, archives et objets infestés",
            "Locaux fortement infestés, en dernier recours",
        ],
        "tips": [
            "Contrôlez les lots à réception et isolez ceux qui sont suspects",
            "Respectez la rotation des stocks (premier entré, premier sorti)",
            "Nettoyez les résidus de produits dans les zones de stockage",
            "Mettez en place un monitoring par pièges à phéromones",
        ],
        "faq": [
            ("La fumigation laisse-t-elle des résidus sur les produits ?", "Le fumigant est un gaz : après la phase de dégazage, il est évacué. La marchandise peut être remise en circulation une fois les mesures de contrôle réalisées."),
            ("Combien de temps dure une fumigation ?", "De quelques heures à plusieurs jours selon le volume, la température, la marchandise et le produit utilisé. La durée est fixée lors de l'étude préalable."),
            ("Est-ce dangereux ?", "Les fumigants sont des produits très encadrés : la zone est confinée, balisée et interdite d'accès pendant toute l'opération, réalisée exclusivement par des techniciens habilités."),
        ],
        "related": ["desinsectisation", "desinfection", "deratisation"],
    },
]

PESTS = [
    {
        "slug": "punaises-de-lit",
        "kind": "pest",
        "nav": "Punaises de lit",
        "short": "Piqûres au réveil ? Traitement en deux passages, préparation guidée.",
        "title": "Punaises de lit : traitement Île-de-France & Oise | Derapest",
        "desc": "Traitement des punaises de lit en Île-de-France et dans l'Oise : diagnostic, traitement en deux passages, préparation guidée. Intervention rapide, devis gratuit.",
        "kicker": "Insectes piqueurs",
        "h1": "Des punaises de lit ?<br><em>Réagissez vite, on vous guide.</em>",
        "lead": "Une infestation de punaises se règle vite ou devient incontrôlable. Nous intervenons rapidement, avec un protocole en deux passages et une préparation expliquée pas à pas.",
        "img": "photos/punaises-de-lit.webp",
        "img_alt": "Punaise de lit en gros plan",
        "signs_title": "Comment reconnaître des punaises de lit",
        "signs": [
            ("Piqûres alignées", "Plusieurs piqûres en ligne ou en grappe, découvertes au réveil, sur les bras, le cou ou les jambes."),
            ("Taches sur la literie", "Petits points noirs (déjections) sur le matelas et les coutures, traces de sang sur les draps."),
            ("Insectes visibles", "Insectes bruns et plats de 4 à 7 mm, mues et œufs blancs dans les coutures et le sommier."),
        ],
        "risks_title": "Pourquoi agir sans attendre",
        "risks_text": "Une femelle pond plusieurs œufs par jour. Les punaises se cachent dans les plinthes, prises et meubles, et voyagent d'un logement à l'autre via les bagages et les vêtements.",
        "risks": [
            "Troubles du sommeil, anxiété et fatigue",
            "Démangeaisons et réactions cutanées",
            "Propagation aux pièces et aux logements voisins",
            "Mobilier et literie parfois à jeter si l'on tarde",
        ],
        "steps": [
            ("Diagnostic", "Inspection de la literie, du mobilier et des pièces voisines pour délimiter l'infestation."),
            ("Préparation", "Nous vous remettons une fiche : lavage du linge à 60 °C, ensachage, dégagement des zones."),
            ("1er traitement", "Traitement ciblé des couchages, meubles, plinthes et cachettes."),
            ("2e passage", "Environ deux semaines plus tard, pour éliminer les punaises issues des œufs."),
        ],
        "solutions_title": "Notre protocole punaises de lit",
        "solutions": [
            "Inspection minutieuse avant traitement",
            "Traitement insecticide ciblé, produits homologués",
            "Deux passages systématiques pour couvrir le cycle des œufs",
            "Fiche de préparation et consignes post-traitement",
            "Interventions en logement, hôtel, résidence et transport",
        ],
        "tips": [
            "En voyage, posez la valise sur un support, jamais sur le lit",
            "Au retour, lavez les vêtements à 60 °C ou passez-les au sèche-linge",
            "Inspectez tout meuble ou matelas d'occasion",
            "N'utilisez pas de fumigènes du commerce : ils dispersent les punaises",
        ],
        "faq": [
            ("Faut-il jeter son matelas ?", "Rarement. Un matelas traité puis protégé par une housse anti-punaises peut généralement être conservé. Le technicien vous conseille selon l'état de la literie."),
            ("Pourquoi deux passages ?", "Les œufs de punaises résistent à la plupart des traitements. Le second passage élimine les jeunes punaises écloses entre-temps, avant qu'elles ne pondent à leur tour."),
            ("Les punaises de lit sont-elles liées à un manque d'hygiène ?", "Non. Elles se nourrissent de sang, pas de saleté : on les trouve aussi bien dans les hôtels de luxe que dans les logements impeccables. Elles voyagent avec les bagages."),
        ],
        "related": ["desinsectisation", "cafards-blattes", "desinfection"],
    },
    {
        "slug": "cafards-blattes",
        "kind": "pest",
        "nav": "Cafards & blattes",
        "short": "Cuisine, restaurant, local : traitement par gel ciblé et suivi.",
        "title": "Cafards et blattes : désinsectisation Île-de-France & Oise | Derapest",
        "desc": "Cafards ou blattes dans votre cuisine, restaurant ou immeuble ? Traitement par gel et pulvérisation ciblée en Île-de-France et dans l'Oise. Devis gratuit.",
        "kicker": "Insectes rampants",
        "h1": "Des cafards dans la cuisine ?<br><em>On les élimine à la source.</em>",
        "lead": "Les blattes vivent cachées et ne sortent qu'à la nuit tombée. Si vous en voyez, la colonie est déjà installée. Nous traitons les foyers avec un gel ciblé et prévenons la réinfestation.",
        "img": "photos/cafards-blattes.webp",
        "img_alt": "Cafard en gros plan sur une surface",
        "signs_title": "Les signes d'une infestation de blattes",
        "signs": [
            ("Sorties nocturnes", "Insectes qui fuient à l'allumage de la lumière, dans la cuisine ou la salle de bains."),
            ("Déjections", "Petits points noirs ressemblant à du poivre dans les placards, tiroirs et derrière les appareils."),
            ("Odeur et oothèques", "Odeur âcre et capsules d'œufs brunes dans les recoins chauds et humides."),
        ],
        "risks_title": "Un risque sanitaire réel",
        "risks_text": "Les blattes ont une préférence pour les lieux de stockage alimentaire. Elles passent des canalisations aux plans de travail et transportent germes et allergènes.",
        "risks": [
            "Contamination des aliments et des surfaces de préparation",
            "Allergènes pouvant aggraver l'asthme",
            "Propagation par les gaines et colonnes d'immeubles",
            "Non-conformité et risque de fermeture pour les restaurants",
        ],
        "steps": [
            ("Repérage", "Localisation des foyers : moteurs d'appareils, gaines, siphons, faux plafonds."),
            ("Gel ciblé", "Application de gel insecticide dans les fissures et cachettes, sans vider vos placards."),
            ("Pulvérisation", "Complément par pulvérisation ou nébulisation si l'infestation est importante."),
            ("Contrôle", "Passage de contrôle et conseils pour éviter le retour des blattes."),
        ],
        "solutions_title": "Notre traitement anti-cafards",
        "solutions": [
            "Gel insecticide appliqué au plus près des cachettes",
            "Pulvérisation ou nébulisation en cas de forte infestation",
            "Traitement des colonnes et parties communes en copropriété",
            "Contrats de suivi pour restaurants et commerces alimentaires",
        ],
        "tips": [
            "Ne laissez ni vaisselle sale ni nourriture à l'air libre la nuit",
            "Réparez les fuites et asséchez les zones humides",
            "Calfeutrez les passages de gaines et canalisations",
            "Évitez de stocker cartons et sacs en papier en cuisine",
        ],
        "faq": [
            ("Faut-il vider les placards avant le traitement ?", "Avec le traitement par gel, ce n'est généralement pas nécessaire : le gel est appliqué en points discrets dans les fissures. Le technicien vous indique les préparatifs selon la méthode retenue."),
            ("En combien de temps les cafards disparaissent-ils ?", "Une nette diminution est visible en quelques jours ; l'élimination complète prend environ deux à trois semaines, le temps que le gel agisse sur toute la colonie."),
            ("Intervenez-vous dans les restaurants ?", "Oui, avec des produits adaptés aux zones alimentaires, des interventions en dehors des heures de service et un rapport pour votre plan de maîtrise sanitaire."),
        ],
        "related": ["desinsectisation", "punaises-de-lit", "desinfection"],
    },
    {
        "slug": "guepes-frelons",
        "kind": "pest",
        "nav": "Guêpes & frelons",
        "short": "Destruction de nids en sécurité, en hauteur comme en cavité.",
        "title": "Destruction de nids de guêpes et frelons Île-de-France & Oise | Derapest",
        "desc": "Nid de guêpes ou de frelons asiatiques ? Destruction en sécurité en Île-de-France et dans l'Oise, en hauteur ou en cavité. Intervention rapide, devis gratuit.",
        "kicker": "Insectes volants",
        "h1": "Un nid de guêpes ou de frelons ?<br><em>N'y touchez pas, on intervient.</em>",
        "lead": "Toiture, cheminée, haie, cabanon : un nid à proximité de la maison représente un vrai danger. Nos techniciens équipés le neutralisent en sécurité, quel que soit son emplacement.",
        "img": "photos/guepes-frelons.webp",
        "img_alt": "Guêpes construisant un nid sous un toit",
        "signs_title": "Comment repérer un nid",
        "signs": [
            ("Va-et-vient", "Allées et venues régulières d'insectes au même endroit : rebord de toit, trou de mur, sol."),
            ("Bourdonnement", "Bruit sourd dans un mur, un coffre de volet roulant ou des combles."),
            ("Nid visible", "Boule grise papyracée sous un avant-toit, dans un arbre ou une haie."),
        ],
        "risks_title": "Un danger à ne pas sous-estimer",
        "risks_text": "Un nid peut abriter plusieurs milliers d'individus en fin d'été. Les frelons asiatiques sont particulièrement agressifs à l'approche de leur nid.",
        "risks": [
            "Piqûres multiples, risque de choc allergique",
            "Danger accru pour les enfants et les animaux",
            "Chutes lors de tentatives de destruction en hauteur",
            "Frelon asiatique : menace pour les ruchers voisins",
        ],
        "steps": [
            ("Localisation", "Identification de l'espèce (guêpe, frelon européen ou asiatique) et du nid."),
            ("Sécurisation", "Périmètre de sécurité, équipement de protection, matériel adapté à la hauteur."),
            ("Destruction", "Injection d'insecticide au cœur du nid, à la perche si nécessaire."),
            ("Vérification", "Contrôle de l'activité et retrait du nid lorsqu'il est accessible."),
        ],
        "solutions_title": "Nos interventions",
        "solutions": [
            "Nids de guêpes sous toiture, dans les murs et au sol",
            "Nids de frelons européens et asiatiques",
            "Interventions en hauteur à la perche télescopique",
            "Coffres de volets roulants, cheminées, combles",
        ],
        "tips": [
            "Ne bouchez jamais l'entrée d'un nid : les insectes chercheront une autre sortie, parfois vers l'intérieur",
            "N'aspergez pas le nid vous-même",
            "Éloignez enfants et animaux de la zone",
            "Inspectez avant-toits et abris de jardin au printemps, quand les nids sont petits",
        ],
        "faq": [
            ("Les pompiers détruisent-ils les nids de guêpes ?", "Dans la plupart des cas, non : les sapeurs-pompiers n'interviennent plus que s'il y a un danger immédiat sur la voie publique. La destruction relève d'une entreprise spécialisée."),
            ("Quand faut-il détruire un nid ?", "Le plus tôt possible : au printemps, le nid est petit et l'intervention plus simple. Les nids sont aussi plus actifs et plus dangereux en fin d'été."),
            ("Le nid sera-t-il retiré ?", "Lorsqu'il est accessible sans risque, oui. Un nid traité dans une cavité inaccessible n'est plus actif et ne sera pas réoccupé l'année suivante."),
        ],
        "related": ["desinsectisation", "fourmis", "cafards-blattes"],
    },
    {
        "slug": "fourmis",
        "kind": "pest",
        "nav": "Fourmis",
        "short": "On localise le nid, on traite à la source, on coupe les accès.",
        "title": "Traitement contre les fourmis Île-de-France & Oise | Derapest",
        "desc": "Fourmis dans la maison ou le local ? Traitement à la source par appâts et gel en Île-de-France et dans l'Oise. Produits homologués, devis gratuit.",
        "kicker": "Insectes rampants",
        "h1": "Une colonie de fourmis ?<br><em>On remonte jusqu'au nid.</em>",
        "lead": "Écraser les fourmis visibles ne sert à rien : l'essentiel de la colonie et ses reines restent au nid. Nous traitons à la source pour une élimination durable.",
        "img": "photos/fourmis.webp",
        "img_alt": "Colonie de fourmis le long d'un mur",
        "signs_title": "Les signes d'une colonie installée",
        "signs": [
            ("Pistes", "Files de fourmis le long des plinthes, du plan de travail ou des encadrements."),
            ("Petits tas de terre", "Sciure ou terre fine près des murs, des dalles ou des boiseries."),
            ("Fourmis ailées", "Essaimage au printemps ou en été : signe d'une colonie mature à proximité."),
        ],
        "risks_title": "Plus qu'une simple gêne",
        "risks_text": "Les fourmis peuvent contaminer les aliments, mais certaines espèces dégradent aussi le bois et les matériaux isolants.",
        "risks": [
            "Denrées contaminées dans les cuisines et réserves",
            "Bois et isolants dégradés par certaines espèces",
            "Infestations récurrentes chaque printemps",
            "Nuisance dans les commerces et les restaurants",
        ],
        "steps": [
            ("Identification", "Espèce, pistes et localisation du nid, à l'intérieur ou à l'extérieur."),
            ("Appâts", "Pose d'appâts ou de gel que les ouvrières rapportent au nid, jusqu'aux reines."),
            ("Barrière", "Traitement des points d'entrée et du périmètre extérieur si besoin."),
            ("Suivi", "Contrôle de l'activité et conseils pour éviter le retour."),
        ],
        "solutions_title": "Notre traitement",
        "solutions": [
            "Appâts et gels à action différée, rapportés jusqu'au nid",
            "Traitement direct du nid quand il est accessible",
            "Barrière insecticide autour du bâtiment",
            "Intervention en logement, commerce et industrie agroalimentaire",
        ],
        "tips": [
            "Ne laissez pas traîner de sucre, miettes ou gamelles",
            "Rangez les aliments dans des boîtes hermétiques",
            "Colmatez les fissures en bas des murs et autour des fenêtres",
            "Éloignez les pots de fleurs et tas de bois des façades",
        ],
        "faq": [
            ("Pourquoi les fourmis reviennent-elles chaque année ?", "Parce que le nid n'a pas été détruit : seules les ouvrières visibles ont été éliminées. Le traitement par appât agit sur la colonie entière, reines comprises."),
            ("Combien de temps avant de voir un résultat ?", "L'activité diminue en quelques jours ; il faut parfois une à deux semaines pour que l'appât atteigne toute la colonie. Il ne faut pas nettoyer les pistes pendant ce temps."),
        ],
        "related": ["desinsectisation", "cafards-blattes", "guepes-frelons"],
    },
]

# ------------------------------------------------------------------
# ZONES D'INTERVENTION — Île-de-France + Oise
# ------------------------------------------------------------------
ZONES = [
    {
        "slug": "paris", "name": "Paris", "num": "75", "prep": "à Paris", "region": "Île-de-France",
        "cities": ["Paris 1er à 4e", "Paris 5e", "Paris 6e", "Paris 7e", "Paris 8e", "Paris 9e", "Paris 10e", "Paris 11e", "Paris 12e", "Paris 13e", "Paris 14e", "Paris 15e", "Paris 16e", "Paris 17e", "Paris 18e", "Paris 19e", "Paris 20e"],
        "intro": "Immeubles anciens, caves reliées, réseau d'égouts, densité de commerces et de restaurants : Paris concentre tout ce qui favorise les nuisibles. Rats, souris, cafards et punaises de lit y circulent d'un logement à l'autre.",
        "context": [
            "Dans les immeubles parisiens, les infestations se propagent par les gaines techniques, les colonnes d'eau et les caves communes. Traiter un seul appartement ne suffit pas toujours : nous travaillons avec les syndics et gestionnaires pour traiter les parties communes et éviter la réinfestation.",
            "Restaurants, commerces de bouche, hôtels et bureaux font l'objet de contrôles d'hygiène réguliers. Nous proposons des interventions ponctuelles comme des contrats de suivi, avec un rapport écrit après chaque passage.",
        ],
        "focus": ["deratisation", "punaises-de-lit", "cafards-blattes"],
        "faq": [
            ("Intervenez-vous dans tous les arrondissements ?", "Oui, nous intervenons dans les vingt arrondissements de Paris, en logement comme en local professionnel."),
            ("Qui doit payer la dératisation dans un immeuble parisien ?", "Les parties communes (caves, locaux poubelles, cours) relèvent du syndic de copropriété. À l'intérieur d'un logement, cela dépend de l'origine de l'infestation et du bail."),
        ],
    },
    {
        "slug": "seine-et-marne", "name": "Seine-et-Marne", "num": "77", "prep": "en Seine-et-Marne", "region": "Île-de-France",
        "cities": ["Meaux", "Chelles", "Melun", "Pontault-Combault", "Savigny-le-Temple", "Bussy-Saint-Georges", "Champs-sur-Marne", "Torcy", "Lagny-sur-Marne", "Villeparisis", "Fontainebleau", "Provins"],
        "intro": "Pavillons, corps de ferme, zones d'activité et lisières de forêt : en Seine-et-Marne, les rongeurs trouvent refuge dans les combles et dépendances, et les nids de guêpes et frelons se multiplient dès le printemps.",
        "context": [
            "Le département alterne zones urbaines denses autour de Marne-la-Vallée et Meaux, et secteurs ruraux autour de Provins ou Fontainebleau. Les maisons individuelles avec jardin, garage et grenier sont particulièrement exposées aux rats, souris et mulots à l'automne.",
            "Les exploitations agricoles, silos et entrepôts logistiques demandent des plans de dératisation suivis et, pour les denrées stockées, parfois une fumigation.",
        ],
        "focus": ["deratisation", "guepes-frelons", "fumigation"],
        "faq": [
            ("Intervenez-vous dans les communes rurales du 77 ?", "Oui, nous couvrons l'ensemble de la Seine-et-Marne, des villes nouvelles aux communes rurales."),
            ("Traitez-vous les exploitations agricoles ?", "Oui : dératisation de bâtiments agricoles, silos et hangars, avec postes sécurisés et suivi régulier."),
        ],
    },
    {
        "slug": "yvelines", "name": "Yvelines", "num": "78", "prep": "dans les Yvelines", "region": "Île-de-France",
        "cities": ["Versailles", "Saint-Germain-en-Laye", "Poissy", "Mantes-la-Jolie", "Sartrouville", "Montigny-le-Bretonneux", "Les Mureaux", "Houilles", "Chatou", "Plaisir", "Trappes", "Rambouillet"],
        "intro": "Maisons anciennes, demeures en pierre, forêts et bords de Seine : les Yvelines offrent aux nuisibles de nombreux abris, des combles aux caves voûtées.",
        "context": [
            "Les maisons de caractère et les bâtiments anciens sont exposés aux insectes du bois et aux rongeurs qui circulent dans les doubles cloisons. Nous intervenons avec discrétion, y compris dans les résidences et les copropriétés de standing.",
            "Les communes en bord de forêt et de Seine connaissent aussi une forte activité de guêpes et frelons asiatiques à la belle saison.",
        ],
        "focus": ["deratisation", "guepes-frelons", "desinsectisation"],
        "faq": [
            ("Intervenez-vous à Versailles et Saint-Germain-en-Laye ?", "Oui, ainsi que dans l'ensemble des Yvelines, de Mantes-la-Jolie à Rambouillet."),
            ("Pouvez-vous intervenir discrètement ?", "Oui, nous adaptons nos interventions aux résidences et commerces qui souhaitent rester discrets."),
        ],
    },
    {
        "slug": "essonne", "name": "Essonne", "num": "91", "prep": "en Essonne", "region": "Île-de-France",
        "cities": ["Évry-Courcouronnes", "Corbeil-Essonnes", "Massy", "Savigny-sur-Orge", "Sainte-Geneviève-des-Bois", "Palaiseau", "Viry-Châtillon", "Athis-Mons", "Draveil", "Brétigny-sur-Orge", "Les Ulis", "Étampes"],
        "intro": "Entre zones pavillonnaires, grands ensembles et plateaux agricoles, l'Essonne présente des situations très variées : rongeurs en sous-sol, blattes en immeuble, guêpes en jardin.",
        "context": [
            "Dans les grands ensembles, les blattes et les punaises de lit se propagent par les colonnes techniques. Nous intervenons auprès des bailleurs et des syndics pour des traitements coordonnés, logement par logement et en parties communes.",
            "Dans les secteurs pavillonnaires et ruraux du sud du département, les rongeurs s'installent dans les garages, les vides sanitaires et les abris de jardin.",
        ],
        "focus": ["cafards-blattes", "deratisation", "punaises-de-lit"],
        "faq": [
            ("Travaillez-vous avec les bailleurs sociaux ?", "Oui, nous intervenons pour les bailleurs et syndics, avec des rapports d'intervention par logement."),
            ("Couvrez-vous le sud de l'Essonne ?", "Oui, jusqu'à Étampes et les communes rurales du département."),
        ],
    },
    {
        "slug": "hauts-de-seine", "name": "Hauts-de-Seine", "num": "92", "prep": "dans les Hauts-de-Seine", "region": "Île-de-France",
        "cities": ["Boulogne-Billancourt", "Nanterre", "Courbevoie", "Colombes", "Asnières-sur-Seine", "Rueil-Malmaison", "Issy-les-Moulineaux", "Levallois-Perret", "Neuilly-sur-Seine", "Antony", "Clichy", "Puteaux"],
        "intro": "Tours de bureaux, restaurants d'entreprise, résidences et copropriétés : dans les Hauts-de-Seine, la densité urbaine et les sous-sols étendus favorisent rongeurs et blattes.",
        "context": [
            "Autour de La Défense et des pôles d'affaires, les restaurants d'entreprise, cuisines centrales et locaux techniques ont besoin d'un suivi régulier et traçable. Nous proposons des contrats adaptés, avec des passages en dehors des heures d'activité.",
            "Dans les copropriétés, parkings souterrains et locaux poubelles sont des points sensibles que nous traitons en coordination avec les syndics.",
        ],
        "focus": ["deratisation", "cafards-blattes", "desinfection"],
        "faq": [
            ("Intervenez-vous en dehors des heures de bureau ?", "Oui, pour les entreprises et restaurants, nous planifions les passages tôt le matin, en soirée ou le week-end."),
            ("Proposez-vous des contrats annuels ?", "Oui, avec un nombre de passages adapté à votre activité et un rapport après chaque visite."),
        ],
    },
    {
        "slug": "seine-saint-denis", "name": "Seine-Saint-Denis", "num": "93", "prep": "en Seine-Saint-Denis", "region": "Île-de-France",
        "cities": ["Saint-Denis", "Montreuil", "Aubervilliers", "Aulnay-sous-Bois", "Drancy", "Noisy-le-Grand", "Pantin", "Bondy", "Épinay-sur-Seine", "Sevran", "Le Blanc-Mesnil", "Bobigny"],
        "intro": "Habitat collectif dense, entrepôts, marchés et commerces alimentaires : en Seine-Saint-Denis, rats, cafards et punaises de lit sont des problèmes fréquents que nous traitons au quotidien.",
        "context": [
            "Dans l'habitat collectif, une infestation non traitée gagne rapidement les logements voisins. Nous coordonnons les traitements avec les bailleurs, syndics et locataires pour agir sur l'ensemble du bâtiment.",
            "Zones logistiques, commerces de gros et marchés nécessitent un plan de dératisation suivi : postes sécurisés, relevés réguliers et compte rendu écrit.",
        ],
        "focus": ["deratisation", "cafards-blattes", "punaises-de-lit"],
        "faq": [
            ("Intervenez-vous rapidement dans le 93 ?", "Oui, nous fixons une date d'intervention dès votre appel, en priorisant les situations urgentes."),
            ("Traitez-vous les entrepôts et commerces de gros ?", "Oui, avec des plans de dératisation et de désinsectisation adaptés aux grandes surfaces de stockage."),
        ],
    },
    {
        "slug": "val-de-marne", "name": "Val-de-Marne", "num": "94", "prep": "dans le Val-de-Marne", "region": "Île-de-France",
        "cities": ["Créteil", "Vitry-sur-Seine", "Champigny-sur-Marne", "Saint-Maur-des-Fossés", "Ivry-sur-Seine", "Maisons-Alfort", "Fontenay-sous-Bois", "Villejuif", "Vincennes", "Alfortville", "Choisy-le-Roi", "Nogent-sur-Marne"],
        "intro": "Bords de Marne et de Seine, pavillons, grands ensembles et le marché de Rungis à proximité : le Val-de-Marne concentre des enjeux variés, de la maison individuelle au site agroalimentaire.",
        "context": [
            "Les communes riveraines de la Marne et de la Seine voient les rongeurs remonter vers les habitations, notamment en période de crue ou de travaux. Caves, sous-sols et jardins sont les premières zones touchées.",
            "Pour les professionnels de l'alimentation, nous mettons en place des plans de lutte conformes aux exigences d'hygiène, avec traçabilité complète.",
        ],
        "focus": ["deratisation", "desinsectisation", "desinfection"],
        "faq": [
            ("Intervenez-vous pour les professionnels de l'agroalimentaire ?", "Oui, avec des plans de lutte contre les nuisibles et une traçabilité adaptée à vos audits."),
            ("Les rats viennent-ils des bords de Marne ?", "Les berges et réseaux d'assainissement sont des zones de vie des rats, qui peuvent remonter vers les habitations. Le rebouchage des accès est alors essentiel."),
        ],
    },
    {
        "slug": "val-d-oise", "name": "Val-d'Oise", "num": "95", "prep": "dans le Val-d'Oise", "region": "Île-de-France",
        "cities": ["Argenteuil", "Cergy", "Sarcelles", "Garges-lès-Gonesse", "Franconville", "Pontoise", "Bezons", "Ermont", "Goussainville", "Villiers-le-Bel", "Gonesse", "Taverny"],
        "intro": "Villes nouvelles, zones aéroportuaires, Vexin rural : le Val-d'Oise mêle habitat collectif, zones d'activité et maisons de campagne, chacun avec ses nuisibles.",
        "context": [
            "Autour de Roissy et des zones logistiques, les entrepôts et plateformes doivent maîtriser rongeurs et insectes des denrées. Nous intervenons avec des plans suivis et, si besoin, des traitements par fumigation.",
            "Dans le Vexin et les communes rurales, les rongeurs et les nids de guêpes et frelons sont les demandes les plus fréquentes.",
        ],
        "focus": ["deratisation", "fumigation", "guepes-frelons"],
        "faq": [
            ("Intervenez-vous dans le Vexin ?", "Oui, nous couvrons tout le Val-d'Oise, y compris le Vexin français et ses communes rurales."),
            ("Traitez-vous les sites logistiques ?", "Oui : dératisation, désinsectisation et fumigation de marchandises pour les entrepôts et plateformes."),
        ],
    },
    {
        "slug": "oise", "name": "Oise", "num": "60", "prep": "dans l'Oise", "region": "Hauts-de-France",
        "cities": ["Beauvais", "Compiègne", "Creil", "Nogent-sur-Oise", "Senlis", "Chantilly", "Noyon", "Crépy-en-Valois", "Méru", "Pont-Sainte-Maxence", "Clermont", "Montataire"],
        "intro": "Corps de ferme, maisons individuelles, forêts de Compiègne et de Chantilly, zones industrielles du bassin creillois : l'Oise combine milieu rural et sites d'activité, avec des besoins très différents.",
        "context": [
            "Dans les communes rurales, granges, greniers et dépendances attirent rats, souris et mulots, surtout à l'arrivée du froid. Les nids de guêpes et de frelons asiatiques sont aussi nombreux en lisière de forêt.",
            "Exploitations agricoles, silos, industries agroalimentaires et entrepôts nécessitent un plan de lutte suivi. Nous intervenons sur l'ensemble du département, de Beauvais à Compiègne.",
        ],
        "focus": ["deratisation", "guepes-frelons", "fumigation"],
        "faq": [
            ("Intervenez-vous dans tout le département de l'Oise ?", "Oui, de Beauvais à Compiègne, en passant par Creil, Senlis, Chantilly et les communes rurales."),
            ("Traitez-vous les silos et bâtiments agricoles ?", "Oui : dératisation suivie, désinsectisation et fumigation des denrées stockées."),
        ],
    },
]
