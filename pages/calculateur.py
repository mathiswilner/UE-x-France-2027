from dash import html, dcc, register_page, callback, Input, Output, State
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from styles import C, CARD, CARD_HIGHLIGHT, CARD_ALERT, CARD_SUCCESS, FONT

register_page(__name__, path="/calculateur", name="Calculateur")

# =====================================================================
# DONNÉES
# =====================================================================

CONTRIBUTION_PAR_REVENU = [
    (1100, 80), (1400, 130), (1600, 190), (1800, 250),
    (2100, 310), (2400, 380), (2800, 460), (3500, 580),
    (5000, 780), (99999, 1300),
]

SECTEURS = {
    "Agriculture": {
        "bas": 0.08, "haut": 0.20,
        "perso_bas": (
            "Sans le marché unique et la PAC, votre revenu agricole serait amputé "
            "d'environ {bas} euros par an. La PAC représente en moyenne 40% du revenu "
            "des exploitations françaises. Sans elle, beaucoup ne seraient pas viables."
        ),
        "perso_haut": (
            "Dans le scénario le plus défavorable, la perte atteindrait {haut} euros par an. "
            "70% des exports agricoles françaises vont vers l'UE sans droits de douane. "
            "Un Frexit imposerait des tarifs douaniers qui rendraient ces exports non compétitifs."
        ),
        "concret": (
            "Concrètement : la PAC verse en moyenne 30 700 euros par exploitation et par an "
            "en France (source : ASP, 2023). Sans l'UE, ces aides disparaîtraient ou devraient "
            "être financées intégralement par le budget national."
        ),
        "source": "ASP (2023), CEPII (2018), Eurostat",
    },
    "Aéronautique et défense": {
        "bas": 0.10, "haut": 0.22,
        "perso_bas": (
            "Votre salaire serait inférieur d'environ {bas} euros par an. "
            "L'aéronautique européenne repose sur la coopération entre pays de l'UE. "
            "Airbus, qui emploie 48 000 personnes en France, n'existerait pas sous sa forme actuelle."
        ),
        "perso_haut": (
            "La perte pourrait atteindre {haut} euros par an. Plus de 70% du chiffre d'affaires "
            "du secteur est réalisé dans l'UE. Des barrières commerciales mettraient en péril "
            "des milliers d'emplois directs et indirects."
        ),
        "concret": (
            "Concrètement : chaque avion Airbus contient des pièces fabriquées en France, "
            "en Allemagne, en Espagne et au Royaume-Uni. Sans le marché unique, chaque pièce "
            "qui traverse une frontière serait soumise à des droits de douane et des contrôles."
        ),
        "source": "Airbus Group, Eurostat, GIFAS",
    },
    "Automobile": {
        "bas": 0.07, "haut": 0.16,
        "perso_bas": (
            "Votre salaire serait inférieur d'environ {bas} euros par an. "
            "L'industrie automobile française est profondément intégrée aux chaînes de production européennes."
        ),
        "perso_haut": (
            "La perte pourrait atteindre {haut} euros par an. Les pièces d'une voiture "
            "traversent en moyenne 3 pays européens avant assemblage. Des droits de douane "
            "à chaque frontière augmenteraient les coûts de production de 5 à 10%."
        ),
        "concret": (
            "Concrètement : une Peugeot 308 contient des pièces fabriquées en Espagne, "
            "en Allemagne et en République tchèque. Si chaque passage de frontière coûtait "
            "3 à 5% de droits de douane, le prix final augmenterait de plusieurs milliers d'euros."
        ),
        "source": "PFA (Plateforme automobile), CCFA, Eurostat",
    },
    "Industrie manufacturière": {
        "bas": 0.06, "haut": 0.14,
        "perso_bas": (
            "Votre salaire serait inférieur d'environ {bas} euros par an. "
            "60% des exports industrielles françaises sont destinées au marché unique."
        ),
        "perso_haut": (
            "La perte pourrait atteindre {haut} euros par an. Sans accès libre au marché "
            "de 450 millions de consommateurs, les entreprises industrielles françaises "
            "perdraient en compétitivité face à la concurrence internationale."
        ),
        "concret": (
            "Concrètement : si votre entreprise exporte vers l'Allemagne ou l'Italie, "
            "un Frexit imposerait des formalités douanières, des délais de livraison "
            "et des coûts supplémentaires sur chaque commande."
        ),
        "source": "INSEE, Eurostat, CEPII (2018)",
    },
    "Finance et assurance": {
        "bas": 0.05, "haut": 0.12,
        "perso_bas": (
            "Votre salaire serait inférieur d'environ {bas} euros par an. "
            "Le passeport européen permet à votre employeur d'opérer dans 27 pays "
            "sans autorisation supplémentaire."
        ),
        "perso_haut": (
            "La perte pourrait atteindre {haut} euros par an. "
            "Sans le passeport, les banques et assureurs français devraient ouvrir "
            "des filiales dans chaque pays, ce qui augmenterait massivement les coûts."
        ),
        "concret": (
            "Concrètement : après le Brexit, les banques britanniques ont dû déplacer "
            "des milliers d'emplois vers Paris, Dublin et Francfort pour conserver "
            "leur accès au marché européen. L'inverse se produirait pour la France."
        ),
        "source": "ACPR, BCE, Financial Times",
    },
    "Tourisme et hôtellerie": {
        "bas": 0.05, "haut": 0.12,
        "perso_bas": (
            "Votre salaire serait inférieur d'environ {bas} euros par an. "
            "Schengen et l'euro facilitent considérablement le tourisme européen en France."
        ),
        "perso_haut": (
            "La perte pourrait atteindre {haut} euros par an. La France accueille "
            "83 millions de visiteurs étrangers par an, dont une majorité d'Européens "
            "qui viennent sans visa ni change de monnaie."
        ),
        "concret": (
            "Concrètement : si un touriste allemand devait changer ses euros en francs "
            "et faire la queue à la frontière, beaucoup choisiraient l'Espagne ou l'Italie "
            "à la place. Moins de touristes = moins de clients dans votre établissement."
        ),
        "source": "Atout France, OMT, Eurostat",
    },
    "Technologie et numérique": {
        "bas": 0.04, "haut": 0.10,
        "perso_bas": (
            "Votre salaire serait inférieur d'environ {bas} euros par an. "
            "Le marché unique numérique vous donne accès à 450 millions d'utilisateurs."
        ),
        "perso_haut": (
            "La perte pourrait atteindre {haut} euros par an. Sans harmonisation "
            "réglementaire (RGPD, DSA), chaque pays aurait ses propres règles, "
            "multipliant les coûts de conformité."
        ),
        "concret": (
            "Concrètement : si votre entreprise vend un logiciel ou un service en ligne, "
            "elle peut le vendre dans 27 pays avec les mêmes règles. "
            "Hors UE, il faudrait adapter le produit à chaque marché national."
        ),
        "source": "Commission européenne (DSM), France Digitale",
    },
    "Services et commerce": {
        "bas": 0.03, "haut": 0.08,
        "perso_bas": (
            "Votre salaire serait inférieur d'environ {bas} euros par an. "
            "Le marché unique des services est encore en construction, mais il génère "
            "déjà des bénéfices significatifs."
        ),
        "perso_haut": (
            "La perte pourrait atteindre {haut} euros par an. "
            "Les services représentent 70% du PIB français. "
            "Même un petit effet du marché unique se traduit par des montants importants."
        ),
        "concret": (
            "Concrètement : si vous travaillez dans la grande distribution, "
            "les produits importés d'autres pays de l'UE (fruits espagnols, fromage italien) "
            "arriveraient plus chers et moins vite, ce qui réduirait les marges et les volumes."
        ),
        "source": "BCE (2025), INSEE",
    },
    "Santé et pharmacie": {
        "bas": 0.03, "haut": 0.08,
        "perso_bas": (
            "Votre salaire serait inférieur d'environ {bas} euros par an. "
            "Les autorisations de mise sur le marché européennes réduisent les coûts réglementaires."
        ),
        "perso_haut": (
            "La perte pourrait atteindre {haut} euros par an. "
            "Sans l'EMA (Agence européenne des médicaments), chaque médicament "
            "devrait être approuvé séparément en France."
        ),
        "concret": (
            "Concrètement : pendant le Covid, l'achat groupé de vaccins par l'UE "
            "a permis à la France d'obtenir des prix 20 à 30% plus bas "
            "que si elle avait négocié seule."
        ),
        "source": "EMA, Commission européenne, LEEM",
    },
    "Éducation et recherche": {
        "bas": 0.03, "haut": 0.08,
        "perso_bas": (
            "Votre salaire serait inférieur d'environ {bas} euros par an. "
            "Les programmes européens financent directement la recherche et la mobilité."
        ),
        "perso_haut": (
            "La perte pourrait atteindre {haut} euros par an. "
            "La France a reçu 7,8 milliards d'Horizon Europe sur 2021-2027 "
            "pour financer ses chercheurs et ses laboratoires."
        ),
        "concret": (
            "Concrètement : si vous êtes chercheur, une part importante de votre financement "
            "vient de l'UE. Si vous êtes enseignant, Erasmus+ finance la mobilité "
            "de 100 000 étudiants et personnels français chaque année."
        ),
        "source": "Commission européenne (Horizon Europe), Erasmus+",
    },
    "Fonction publique": {
        "bas": 0.02, "haut": 0.05,
        "perso_bas": (
            "L'impact direct sur votre salaire serait limité (environ {bas} euros par an). "
            "Mais le bénéfice principal est indirect."
        ),
        "perso_haut": (
            "La perte indirecte pourrait atteindre {haut} euros par an. "
            "L'euro réduit le coût d'emprunt de l'État d'environ 25 milliards par an. "
            "C'est autant de budget disponible pour les services publics et les salaires."
        ),
        "concret": (
            "Concrètement : si l'État devait emprunter à des taux plus élevés (comme avant l'euro), "
            "il faudrait soit augmenter les impôts, soit réduire les dépenses publiques, "
            "y compris les salaires et les effectifs de la fonction publique."
        ),
        "source": "Banque de France, Cour des Comptes",
    },
    "Retraité": {
        "bas": 0.02, "haut": 0.06,
        "perso_bas": (
            "Votre pension serait inférieure d'environ {bas} euros par an. "
            "La croissance économique générée par le marché unique finance le système de retraite."
        ),
        "perso_haut": (
            "La perte pourrait atteindre {haut} euros par an. "
            "Le système de retraite par répartition dépend directement de l'activité économique. "
            "Moins de croissance = moins de cotisations = moins de pensions."
        ),
        "concret": (
            "Concrètement : le Brexit a réduit la croissance britannique de 6 à 8%. "
            "En France, un choc comparable réduirait les recettes de cotisations retraite "
            "de plusieurs milliards, menaçant le niveau des pensions."
        ),
        "source": "COR (Conseil d'Orientation des Retraites), CEPII",
    },
    "Étudiant": {
        "bas": 0.01, "haut": 0.03,
        "perso_bas": (
            "L'impact direct est limité (environ {bas} euros par an). "
            "Mais les bénéfices sont surtout futurs : votre employabilité et votre salaire "
            "d'entrée dépendent de la santé économique du pays."
        ),
        "perso_haut": (
            "La perte future pourrait atteindre {haut} euros par an une fois en poste. "
            "De plus, Erasmus+ (13 000 étudiants français par an) et les programmes de recherche "
            "dépendent directement de l'appartenance à l'UE."
        ),
        "concret": (
            "Concrètement : sans l'UE, les frais d'inscription dans une université européenne "
            "seraient ceux d'un étudiant « étranger » (souvent 3 à 10 fois plus cher). "
            "Et votre diplôme ne serait plus automatiquement reconnu dans 27 pays."
        ),
        "source": "Erasmus+, Commission européenne, EHEA",
    },
    "En recherche d'emploi": {
        "bas": 0.02, "haut": 0.06,
        "perso_bas": (
            "L'impact est indirect mais réel : le marché unique soutient environ "
            "3 à 5 millions d'emplois en France liés aux échanges intra-UE. "
            "Moins de marché unique = moins d'offres d'emploi."
        ),
        "perso_haut": (
            "Le Brexit a réduit l'emploi britannique de 3 à 4%. "
            "Appliqué à la France, cela représenterait 800 000 à 1 100 000 emplois en moins, "
            "ce qui réduirait considérablement vos chances de retrouver un poste."
        ),
        "concret": (
            "Concrètement : le marché unique permet aux entreprises françaises d'exporter "
            "sans barrières, ce qui maintient leur activité et leurs embauches. "
            "Sans cet accès, certaines entreprises délocaliseraient ou réduiraient leurs effectifs."
        ),
        "source": "Bloom et al. (NBER, 2025), INSEE, Eurostat",
    },
    "Autre": {
        "bas": 0.03, "haut": 0.07,
        "perso_bas": (
            "Votre revenu serait inférieur d'environ {bas} euros par an. "
            "Le marché unique génère un bénéfice estimé entre 3 et 7% du PIB français."
        ),
        "perso_haut": (
            "La perte pourrait atteindre {haut} euros par an. "
            "Ce chiffre est une moyenne tous secteurs confondus."
        ),
        "concret": (
            "Concrètement : l'appartenance à l'UE maintient les prix plus bas "
            "(concurrence accrue), les salaires plus hauts (commerce accru) "
            "et les taux d'emprunt plus bas (euro)."
        ),
        "source": "CEPII (Mayer et al., 2018), BCE (2025)",
    },
}

REGIONS = {
    "Île-de-France":                {"fonds_total": 4.8, "pop": 12.3},
    "Auvergne-Rhône-Alpes":         {"fonds_total": 5.2, "pop": 8.1},
    "Nouvelle-Aquitaine":           {"fonds_total": 5.8, "pop": 6.0},
    "Occitanie":                    {"fonds_total": 6.2, "pop": 5.9},
    "Hauts-de-France":              {"fonds_total": 5.5, "pop": 6.0},
    "Grand Est":                    {"fonds_total": 4.8, "pop": 5.6},
    "Provence-Alpes-Côte d'Azur":   {"fonds_total": 3.8, "pop": 5.1},
    "Bretagne":                     {"fonds_total": 4.2, "pop": 3.4},
    "Pays de la Loire":             {"fonds_total": 3.6, "pop": 3.8},
    "Normandie":                    {"fonds_total": 3.8, "pop": 3.3},
    "Bourgogne-Franche-Comté":      {"fonds_total": 3.8, "pop": 2.8},
    "Centre-Val de Loire":          {"fonds_total": 3.2, "pop": 2.6},
    "Corse":                        {"fonds_total": 0.8, "pop": 0.34},
    "Outre-mer":                    {"fonds_total": 5.8, "pop": 2.2},
}


# =====================================================================
# CALCULS
# =====================================================================

def _contribution(revenu_mensuel):
    for seuil, montant in CONTRIBUTION_PAR_REVENU:
        if revenu_mensuel <= seuil:
            return montant
    return 1300


def _benefice_marche_unique(revenu_annuel, secteur):
    data = SECTEURS.get(secteur, SECTEURS["Autre"])
    bas = int(round(revenu_annuel * data["bas"], -1))
    haut = int(round(revenu_annuel * data["haut"], -1))
    texte_bas = data["perso_bas"].format(bas=str(bas))
    texte_haut = data["perso_haut"].format(haut=str(haut))
    return bas, haut, texte_bas, texte_haut, data["concret"], data["source"]


def _benefice_euro_credit(proprio):
    if proprio != "credit":
        return 0, 0, "Vous n'avez pas de crédit immobilier en cours.", ""
    bas = 900
    haut = 2700
    detail = (
        "Votre crédit immobilier vous coûterait entre " + str(int(round(bas/12, 0)))
        + " et " + str(int(round(haut/12, 0))) + " euros de plus par mois. "
        "L'euro permet à la France d'emprunter à des taux plus bas qu'avec une monnaie nationale. "
        "Le différentiel est estimé entre 0,5 et 1,5 point (source : BCE, Banque de France). "
        "Sur un crédit moyen de 180 000 euros (source : Observatoire Crédit Logement), "
        "cela représente entre 900 et 2 700 euros d'économie par an."
    )
    return bas, haut, detail, "BCE, Banque de France, Observatoire Crédit Logement"


def _benefice_regional(region):
    data = REGIONS.get(region, {"fonds_total": 4.0, "pop": 5.0})
    par_hab_an = int(round((data["fonds_total"] * 1000) / data["pop"] / 7, -1))
    detail = (
        "Votre région reçoit " + str(data["fonds_total"])
        + " milliards d'euros de l'UE sur 2021-2027 (PAC, FEDER, FSE+, Horizon Europe). "
        "Cela représente environ " + str(par_hab_an) + " euros par habitant et par an. "
        "Ces fonds financent des routes, des formations, des aides agricoles "
        "et des projets de recherche dans votre territoire."
    )
    return par_hab_an, detail


def _perte_frexit(revenu_annuel, scenario):
    taux = {
        "norvege": (0.015, 0.025),
        "suisse": (0.035, 0.055),
        "omc": (0.055, 0.085),
    }
    bas_t, haut_t = taux.get(scenario, (0.035, 0.055))
    return int(round(revenu_annuel * bas_t, -1)), int(round(revenu_annuel * haut_t, -1))


# =====================================================================
# LAYOUT
# =====================================================================

def layout():
    return html.Div(
        style={"maxWidth": "800px", "margin": "0 auto", "padding": "40px 5%", "fontFamily": FONT},
        children=[
            _header(),
            _formulaire(),
            html.Div(id="resultat-calculateur"),
        ],
    )


def _header():
    return html.Div(
        style={"marginBottom": "40px"},
        children=[
            html.P("CALCULATEUR", style={
                "color": C["muted"], "fontSize": "0.85em", "letterSpacing": "3px",
                "fontWeight": "600", "marginBottom": "8px", "fontFamily": FONT,
            }),
            html.H1("Et vous, combien l'Europe vous rapporte ?", style={
                "color": C["text"], "fontSize": "2.2em", "fontWeight": "700",
                "marginBottom": "12px", "marginTop": "0", "fontFamily": FONT,
            }),
            html.P(
                "Découvrez une estimation de ce que vous gagnez grâce à l'Union européenne "
                "et de ce que vous perdriez en cas de Frexit. Les résultats sont des ordres "
                "de grandeur accompagnés de leurs sources.",
                style={"color": C["text_secondary"], "fontSize": "1.1em", "lineHeight": "1.6", "fontFamily": FONT},
            ),
        ],
    )


def _formulaire():
    ls = {"color": C["text"], "fontSize": "14px", "fontWeight": "600",
          "marginBottom": "6px", "display": "block", "fontFamily": FONT}

    return html.Div(
        style={
            "border": "1px solid " + C["border"], "borderTop": "3px solid " + C["bleu_france"],
            "borderRadius": "2px", "padding": "32px", "marginBottom": "32px",
        },
        children=[
            html.P("Vos informations", style={
                "color": C["bleu_france"], "fontSize": "1.1em", "fontWeight": "700",
                "marginBottom": "24px", "marginTop": "0", "fontFamily": FONT,
            }),
            html.Label("Votre situation :", style=ls),
            dcc.Dropdown(
                id="calc-secteur",
                options=[{"label": s, "value": s} for s in SECTEURS.keys()],
                placeholder="Sélectionnez votre situation ou secteur",
                style={"marginBottom": "20px"},
            ),
            html.Label("Votre région :", style=ls),
            dcc.Dropdown(
                id="calc-region",
                options=[{"label": r, "value": r} for r in REGIONS.keys()],
                placeholder="Sélectionnez votre région",
                style={"marginBottom": "20px"},
            ),
            html.Label("Avez-vous un crédit immobilier en cours ?", style=ls),
            dcc.Dropdown(
                id="calc-proprio",
                options=[{"label": "Oui", "value": "credit"}, {"label": "Non", "value": "non"}],
                placeholder="Sélectionnez",
                style={"marginBottom": "20px"},
            ),
            html.Label("Votre revenu mensuel net (en euros) :", style=ls),
            dcc.Slider(
                id="calc-revenu", min=800, max=10000, step=100, value=2500,
                marks={800:"800", 1500:"1 500", 2500:"2 500", 4000:"4 000",
                       6000:"6 000", 8000:"8 000", 10000:"10 000"},
                tooltip={"placement": "top", "always_visible": True},
            ),
            html.Div(style={"height": "24px"}),
            html.Label("Scénario de sortie de l'UE :", style=ls),
            dcc.Dropdown(
                id="calc-scenario",
                options=[
                    {"label": "Accord type Norvège (EEE) : accès au marché maintenu", "value": "norvege"},
                    {"label": "Accord type Suisse : accès partiel", "value": "suisse"},
                    {"label": "Sortie complète (règles OMC)", "value": "omc"},
                ],
                value="suisse",
                style={"marginBottom": "24px"},
            ),
            html.Button("Estimer mon bilan Europe", id="calc-button", n_clicks=0, style={
                "backgroundColor": C["bleu_france"], "color": C["text_light"],
                "border": "none", "padding": "14px 32px", "fontSize": "1em",
                "fontWeight": "700", "borderRadius": "2px", "cursor": "pointer",
                "width": "100%", "fontFamily": FONT,
            }),
        ],
    )


# =====================================================================
# CALLBACK
# =====================================================================

@callback(
    Output("resultat-calculateur", "children"),
    Input("calc-button", "n_clicks"),
    State("calc-secteur", "value"),
    State("calc-region", "value"),
    State("calc-proprio", "value"),
    State("calc-revenu", "value"),
    State("calc-scenario", "value"),
    prevent_initial_call=True,
)
def calculer(n_clicks, secteur, region, proprio, revenu, scenario):
    if not all([secteur, region, proprio, revenu, scenario]):
        return html.Div(style=CARD_ALERT, children=[
            html.P("Veuillez remplir tous les champs.", style={"color": C["rouge_marianne"], "margin": "0", "fontFamily": FONT}),
        ])

    revenu_annuel = revenu * 12
    contribution = _contribution(revenu)
    contribution_mois = int(round(contribution / 12, 0))

    mu_bas, mu_haut, mu_texte_bas, mu_texte_haut, mu_concret, mu_source = _benefice_marche_unique(revenu_annuel, secteur)
    cr_bas, cr_haut, cr_detail, cr_source = _benefice_euro_credit(proprio)
    reg_montant, reg_detail = _benefice_regional(region)

    total_bas = mu_bas + cr_bas + reg_montant
    total_haut = mu_haut + cr_haut + reg_montant
    total_bas_mois = int(round(total_bas / 12, 0))
    total_haut_mois = int(round(total_haut / 12, 0))
    ratio_bas = int(round(total_bas / contribution, 0)) if contribution > 0 else 0
    ratio_haut = int(round(total_haut / contribution, 0)) if contribution > 0 else 0

    frexit_bas, frexit_haut = _perte_frexit(revenu_annuel, scenario)
    frexit_bas_mois = int(round(frexit_bas / 12, 0))
    frexit_haut_mois = int(round(frexit_haut / 12, 0))
    courses_bas = round(frexit_bas / 350, 1)
    courses_haut = round(frexit_haut / 350, 1)

    scenario_labels = {
        "norvege": "EEE (type Norvège)",
        "suisse": "Accord bilatéral (type Suisse)",
        "omc": "Sortie complète (règles OMC)",
    }

    return html.Div([
        # Titre
        html.Div(style={"textAlign": "center", "padding": "24px 0",
                         "borderTop": "3px solid " + C["bleu_france"], "marginBottom": "24px"}, children=[
            html.P("VOTRE ESTIMATION", style={
                "color": C["muted"], "fontSize": "0.85em", "letterSpacing": "3px",
                "fontWeight": "600", "marginBottom": "4px", "fontFamily": FONT,
            }),
        ]),

        # Coût vs Bénéfice
        html.Div(style={"display": "flex", "gap": "16px", "flexWrap": "wrap", "marginBottom": "24px"}, children=[
            _result_card("Ce que l'UE vous coûte",
                         "~" + str(contribution_mois) + " euros/mois",
                         "soit ~" + str(contribution) + " euros/an (votre part de la contribution nette)",
                         C["rouge_marianne"], "#FEF4F4"),
            _result_card("Ce que l'UE vous rapporte",
                         str(total_bas_mois) + " à " + str(total_haut_mois) + " euros/mois",
                         "soit " + str(total_bas) + " à " + str(total_haut) + " euros/an",
                         C["vert"], "#F5FBF8"),
        ]),

        # Ratio
        html.Div(style={"textAlign": "center", "padding": "20px", "backgroundColor": C["highlight"],
                         "border": "1px solid " + C["bleu_france"], "borderRadius": "2px", "marginBottom": "32px"}, children=[
            html.P("Pour 1 euro versé, vous en récupérez entre " + str(ratio_bas) + " et " + str(ratio_haut) + ".",
                   style={"color": C["bleu_france"], "fontSize": "1.1em", "fontWeight": "700", "margin": "0", "fontFamily": FONT}),
        ]),

        # Canal 1 : Marché unique (détaillé)
        html.Div(style={"marginBottom": "24px", "border": "1px solid " + C["border"],
                         "borderRadius": "2px", "overflow": "hidden"}, children=[
            html.Div(style={"padding": "16px 20px", "backgroundColor": C["bg_alt"],
                             "borderBottom": "1px solid " + C["border"]}, children=[
                html.Div(style={"display": "flex", "justifyContent": "space-between"}, children=[
                    html.Span("Marché unique et activité économique", style={
                        "color": C["text"], "fontSize": "15px", "fontWeight": "700", "fontFamily": FONT}),
                    html.Span(str(mu_bas) + " à " + str(mu_haut) + " euros/an", style={
                        "color": C["vert"], "fontSize": "15px", "fontWeight": "700", "fontFamily": FONT}),
                ]),
            ]),
            html.Div(style={"padding": "20px"}, children=[
                html.P(mu_texte_bas, style={"color": C["text_secondary"], "fontSize": "14px",
                                             "lineHeight": "1.7", "marginBottom": "12px", "fontFamily": FONT}),
                html.P(mu_texte_haut, style={"color": C["text_secondary"], "fontSize": "14px",
                                              "lineHeight": "1.7", "marginBottom": "16px", "fontFamily": FONT}),
                html.Div(style={"backgroundColor": C["bg_alt"], "padding": "16px", "borderRadius": "2px",
                                 "borderLeft": "4px solid " + C["bleu_france"], "marginBottom": "12px"}, children=[
                    html.P(mu_concret, style={"color": C["text"], "fontSize": "14px",
                                               "lineHeight": "1.7", "margin": "0", "fontFamily": FONT}),
                ]),
                html.P("Source : " + mu_source, style={"color": C["muted"], "fontSize": "11px", "margin": "0", "fontFamily": FONT}),
            ]),
        ]),

        # Canal 2 : Fonds régionaux
        _canal_simple("Fonds européens dans votre région",
                      "~" + str(reg_montant) + " euros/an",
                      reg_detail,
                      "cohesiondata.ec.europa.eu, europe-en-france.gouv.fr"),

        # Canal 3 : Euro / crédit
        _canal_simple("Économie sur votre crédit immobilier",
                      str(cr_bas) + " à " + str(cr_haut) + " euros/an" if cr_bas > 0 else "Non applicable",
                      cr_detail,
                      cr_source),

        # Perte Frexit
        html.Div(style={**CARD_ALERT, "marginTop": "32px"}, children=[
            html.P("EN CAS DE FREXIT : " + scenario_labels.get(scenario, ""), style={
                "color": C["rouge_marianne"], "fontSize": "11px", "fontWeight": "700",
                "letterSpacing": "0.5px", "margin": "0 0 8px 0", "fontFamily": FONT,
            }),
            html.P("Vous perdriez entre " + str(frexit_bas_mois) + " et " + str(frexit_haut_mois) + " euros par mois.",
                   style={"color": C["text"], "fontSize": "1.3em", "fontWeight": "700", "marginBottom": "4px", "fontFamily": FONT}),
            html.P("Soit entre " + str(frexit_bas) + " et " + str(frexit_haut) + " euros par an.",
                   style={"color": C["text"], "fontSize": "1em", "marginBottom": "8px", "fontFamily": FONT}),
            html.P("C'est l'équivalent de " + str(courses_bas) + " à " + str(courses_haut) + " mois de courses alimentaires.",
                   style={"color": C["text_secondary"], "fontSize": "14px", "lineHeight": "1.6", "margin": "0 0 8px 0", "fontFamily": FONT}),
            html.P("Sources : CEPII (2018), Bloom et al. (NBER, 2025), BCE",
                   style={"color": C["muted"], "fontSize": "11px", "margin": "0", "fontFamily": FONT}),
        ]),

        # Partage
        html.Div(style={"textAlign": "center", "marginTop": "32px"}, children=[
            html.P("Partagez votre résultat", style={"color": C["muted"], "fontSize": "13px", "marginBottom": "12px", "fontFamily": FONT}),
            html.Div(style={"display": "flex", "gap": "12px", "justifyContent": "center", "flexWrap": "wrap"}, children=[
                _share_button("Partager sur X", C["text"],
                    "https://twitter.com/intent/tweet?text=L'Europe me rapporte entre "
                    + str(total_bas_mois) + " et " + str(total_haut_mois)
                    + " euros par mois. Calculez votre bilan :&url=https://leprixdufrexit.fr/calculateur"),
                _share_button("Partager sur LinkedIn", "#0A66C2",
                    "https://www.linkedin.com/sharing/share-offsite/?url=https://leprixdufrexit.fr/calculateur"),
                _share_button("Envoyer par WhatsApp", "#25D366",
                    "https://wa.me/?text=L'Europe me rapporte entre "
                    + str(total_bas_mois) + " et " + str(total_haut_mois)
                    + " euros par mois. Calculez votre bilan : https://leprixdufrexit.fr/calculateur"),
            ]),
        ]),

        # Note méthodologique
        html.Div(style={"marginTop": "32px", "padding": "16px 20px",
                         "borderTop": "1px solid " + C["border"], "borderLeft": "4px solid " + C["or"]}, children=[
            html.P("Note méthodologique", style={"color": C["text"], "fontSize": "13px", "fontWeight": "700",
                                                   "marginBottom": "8px", "fontFamily": FONT}),
            html.P("Ces estimations sont des ordres de grandeur. Les fourchettes reflètent l'incertitude. "
                   "La contribution est estimée via la progressivité fiscale. Les bénéfices sont calculés "
                   "via trois canaux : marché unique (CEPII, 2018), fonds européens (Commission européenne) "
                   "et taux d'emprunt (BCE). Consultez la page Méthodologie pour le détail complet.",
                   style={"color": C["text_secondary"], "fontSize": "12px", "lineHeight": "1.6", "margin": "0", "fontFamily": FONT}),
        ]),
    ])


# =====================================================================
# COMPOSANTS
# =====================================================================

def _result_card(titre, valeur, detail, couleur, bg):
    return html.Div(style={
        "flex": "1", "minWidth": "200px", "padding": "20px",
        "borderLeft": "4px solid " + couleur, "backgroundColor": bg, "borderRadius": "2px",
    }, children=[
        html.P(titre, style={"color": C["muted"], "fontSize": "12px", "fontWeight": "600",
                              "textTransform": "uppercase", "letterSpacing": "0.5px",
                              "margin": "0 0 4px 0", "fontFamily": FONT}),
        html.P(valeur, style={"color": couleur, "fontSize": "1.6em", "fontWeight": "800",
                               "margin": "0 0 4px 0", "fontFamily": FONT}),
        html.P(detail, style={"color": C["text_secondary"], "fontSize": "12px", "margin": "0", "fontFamily": FONT}),
    ])


def _canal_simple(titre, valeur, detail, source):
    return html.Div(style={"marginBottom": "16px", "border": "1px solid " + C["border"],
                             "borderRadius": "2px", "overflow": "hidden"}, children=[
        html.Div(style={"padding": "16px 20px", "backgroundColor": C["bg_alt"],
                         "borderBottom": "1px solid " + C["border"]}, children=[
            html.Div(style={"display": "flex", "justifyContent": "space-between"}, children=[
                html.Span(titre, style={"color": C["text"], "fontSize": "15px", "fontWeight": "700", "fontFamily": FONT}),
                html.Span(valeur, style={"color": C["vert"], "fontSize": "15px", "fontWeight": "700", "fontFamily": FONT}),
            ]),
        ]),
        html.Div(style={"padding": "16px 20px"}, children=[
            html.P(detail, style={"color": C["text_secondary"], "fontSize": "14px",
                                   "lineHeight": "1.7", "margin": "0 0 8px 0", "fontFamily": FONT}),
            html.P("Source : " + source, style={"color": C["muted"], "fontSize": "11px", "margin": "0", "fontFamily": FONT}) if source else html.Div(),
        ]),
    ])


def _share_button(label, color, href):
    return html.A(
        html.Div(label, style={"backgroundColor": color, "color": C["text_light"],
                                "padding": "10px 20px", "borderRadius": "2px",
                                "fontSize": "14px", "fontWeight": "600", "fontFamily": FONT}),
        href=href, target="_blank", style={"textDecoration": "none"},
    )