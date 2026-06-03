from dash import html, dcc, register_page, callback, Input, Output, State
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from styles import C, CARD, CARD_HIGHLIGHT, CARD_ALERT, CARD_SUCCESS, FONT

register_page(__name__, path="/calculateur", name="Calculateur")

# =====================================================================
# DONNÉES DE RÉFÉRENCE
# =====================================================================

# Contribution UE par décile de revenu mensuel net (euros/an)
# Basé sur : contribution nette 10 Mds / 30M ménages = 333 euros moyen
# Ajusté par la progressivité fiscale (IR + TVA)
CONTRIBUTION_PAR_REVENU = [
    (1100, 100),
    (1400, 150),
    (1600, 200),
    (1800, 250),
    (2100, 300),
    (2400, 350),
    (2800, 420),
    (3500, 520),
    (5000, 700),
    (99999, 1200),
]

# Taux de bénéfice du marché unique par secteur (% du revenu annuel)
# Estimation basée sur l'exposition sectorielle au commerce intra-UE
# Sources : CEPII, INSEE, Eurostat
SECTEURS = {
    "Agriculture": {
        "taux": 0.17,
        "detail": "La PAC représente environ 40% du revenu agricole moyen. "
                  "Les exports agricoles françaises vers l'UE dépassent 30 milliards d'euros par an.",
    },
    "Aéronautique et défense": {
        "taux": 0.18,
        "detail": "Airbus est le symbole de la coopération européenne. "
                  "Plus de 70% du chiffre d'affaires du secteur est réalisé dans l'UE.",
    },
    "Automobile": {
        "taux": 0.14,
        "detail": "Les chaînes de production sont intégrées à l'échelle européenne : "
                  "pièces, assemblage et distribution traversent plusieurs pays de l'UE.",
    },
    "Industrie manufacturière": {
        "taux": 0.12,
        "detail": "60% des exports industrielles françaises sont destinées au marché unique, "
                  "sans droits de douane ni barrières réglementaires.",
    },
    "Finance et assurance": {
        "taux": 0.10,
        "detail": "Le passeport européen permet aux banques et assureurs français d'opérer "
                  "dans les 27 pays de l'UE sans autorisation supplémentaire.",
    },
    "Tourisme et hôtellerie": {
        "taux": 0.10,
        "detail": "Schengen et l'euro facilitent le tourisme. La France accueille 83 millions "
                  "de visiteurs étrangers par an, dont une majorité d'Européens.",
    },
    "Technologie et numérique": {
        "taux": 0.08,
        "detail": "Le marché unique numérique et les programmes Horizon Europe financent "
                  "l'innovation et offrent un accès direct à 450 millions de consommateurs.",
    },
    "Services et commerce": {
        "taux": 0.06,
        "detail": "Le marché unique des services reste en construction mais génère déjà "
                  "des gains significatifs, notamment dans la distribution et le conseil.",
    },
    "Santé et pharmacie": {
        "taux": 0.07,
        "detail": "Les autorisations de mise sur le marché européennes simplifient l'accès "
                  "à 450 millions de patients et réduisent les coûts réglementaires.",
    },
    "Éducation et recherche": {
        "taux": 0.06,
        "detail": "Erasmus+ (4,2 Mds euros) et Horizon Europe (7,8 Mds euros pour la France) "
                  "financent la mobilité étudiante et la recherche.",
    },
    "Fonction publique": {
        "taux": 0.04,
        "detail": "Le bénéfice est principalement indirect : l'euro réduit le coût d'emprunt de l'État, "
                  "ce qui libère du budget pour les services publics.",
    },
    "Autre / ne sait pas": {
        "taux": 0.06,
        "detail": "En moyenne, l'appartenance au marché unique génère un bénéfice économique "
                  "estimé entre 3 et 7% du PIB (CEPII, 2018).",
    },
}

# Fonds européens par région (milliards d'euros sur 2021-2027, et population en millions)
# Sources : Commission européenne, préfectures de région
REGIONS = {
    "Île-de-France": {"fonds": 3.2, "pop": 12.3},
    "Auvergne-Rhône-Alpes": {"fonds": 2.8, "pop": 8.1},
    "Nouvelle-Aquitaine": {"fonds": 3.1, "pop": 6.0},
    "Occitanie": {"fonds": 3.5, "pop": 5.9},
    "Hauts-de-France": {"fonds": 3.8, "pop": 6.0},
    "Grand Est": {"fonds": 2.9, "pop": 5.6},
    "Provence-Alpes-Côte d'Azur": {"fonds": 2.4, "pop": 5.1},
    "Bretagne": {"fonds": 2.6, "pop": 3.4},
    "Pays de la Loire": {"fonds": 2.1, "pop": 3.8},
    "Normandie": {"fonds": 2.3, "pop": 3.3},
    "Bourgogne-Franche-Comté": {"fonds": 2.7, "pop": 2.8},
    "Centre-Val de Loire": {"fonds": 2.2, "pop": 2.6},
    "Corse": {"fonds": 0.6, "pop": 0.34},
    "Outre-mer": {"fonds": 4.2, "pop": 2.2},
}


# =====================================================================
# FONCTIONS DE CALCUL
# =====================================================================

def _calculer_contribution(revenu_mensuel):
    """Contribution UE estimée selon le décile de revenu."""
    for seuil, contribution in CONTRIBUTION_PAR_REVENU:
        if revenu_mensuel <= seuil:
            return contribution
    return 1200


def _calculer_benefice_marche_unique(revenu_annuel, secteur):
    """Bénéfice lié au marché unique selon le secteur."""
    data = SECTEURS.get(secteur, SECTEURS["Autre / ne sait pas"])
    return int(revenu_annuel * data["taux"]), data["detail"]


def _calculer_benefice_euro_credit(revenu_mensuel, proprio):
    """Économie sur le crédit immobilier grâce aux taux bas de l'euro."""
    if proprio != "credit":
        return 0, ""

    # Estimation : crédit moyen = 5 ans de revenu net
    # Différentiel de taux estimé = 1 point de pourcentage
    credit_estime = revenu_mensuel * 12 * 5
    economie_annuelle = int(credit_estime * 0.01)

    # Plafond réaliste
    economie_annuelle = min(economie_annuelle, 3000)
    economie_annuelle = max(economie_annuelle, 400)

    detail = (
        "Crédit estimé : ~" + str(int(credit_estime / 1000)) + " 000 euros. "
        "Différentiel de taux estimé : ~1 point grâce à la zone euro. "
        "Économie annuelle sur les intérêts : ~" + str(economie_annuelle) + " euros."
    )
    return economie_annuelle, detail


def _calculer_effet_prix(revenu_mensuel):
    """Baisse des prix grâce à la concurrence du marché unique (1 à 2%)."""
    consommation_annuelle = revenu_mensuel * 12 * 0.80
    economie = int(consommation_annuelle * 0.015)
    detail = (
        "Le marché unique augmente la concurrence et réduit les prix. "
        "Effet estimé : 1,5% sur votre consommation annuelle (~"
        + str(int(consommation_annuelle / 1000)) + " 000 euros)."
    )
    return economie, detail


def _calculer_benefice_regional(region):
    """Fonds européens par habitant dans votre région."""
    data = REGIONS.get(region, {"fonds": 2.5, "pop": 5.0})
    # Fonds sur 7 ans, divisé par population, par an
    par_habitant_par_an = int((data["fonds"] * 1000) / data["pop"] / 7)
    detail = (
        "Votre région reçoit " + str(data["fonds"]) + " milliards d'euros de fonds européens "
        "sur 2021-2027 (PAC, FEDER, FSE, Horizon Europe), "
        "soit environ " + str(par_habitant_par_an) + " euros par habitant et par an."
    )
    return par_habitant_par_an, detail


def _calculer_perte_frexit(revenu_annuel, scenario):
    """Perte estimée en cas de Frexit selon le scénario."""
    taux = {"norvege": 0.02, "suisse": 0.045, "omc": 0.07}
    t = taux.get(scenario, 0.045)
    return int(revenu_annuel * t)


# =====================================================================
# LAYOUT
# =====================================================================

def layout():
    return html.Div(
        style={
            "maxWidth": "800px", "margin": "0 auto",
            "padding": "40px 5%", "fontFamily": FONT,
        },
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
                "En 30 secondes, découvrez ce que vous gagnez grâce à l'Union européenne "
                "et ce que vous perdriez en cas de Frexit.",
                style={
                    "color": C["text_secondary"], "fontSize": "1.1em",
                    "lineHeight": "1.6", "fontFamily": FONT,
                },
            ),
        ],
    )


def _formulaire():
    label_style = {
        "color": C["text"], "fontSize": "14px", "fontWeight": "600",
        "marginBottom": "6px", "display": "block", "fontFamily": FONT,
    }

    return html.Div(
        style={
            "border": "1px solid " + C["border"],
            "borderTop": "3px solid " + C["bleu_france"],
            "borderRadius": "2px",
            "padding": "32px",
            "marginBottom": "32px",
            "backgroundColor": C["bg"],
        },
        children=[
            html.P("Vos informations", style={
                "color": C["bleu_france"], "fontSize": "1.1em", "fontWeight": "700",
                "marginBottom": "24px", "marginTop": "0", "fontFamily": FONT,
            }),

            html.Label("Votre secteur d'activité :", style=label_style),
            dcc.Dropdown(
                id="calc-secteur",
                options=[{"label": s, "value": s} for s in SECTEURS.keys()],
                placeholder="Sélectionnez votre secteur",
                style={"marginBottom": "20px"},
            ),

            html.Label("Votre région :", style=label_style),
            dcc.Dropdown(
                id="calc-region",
                options=[{"label": r, "value": r} for r in REGIONS.keys()],
                placeholder="Sélectionnez votre région",
                style={"marginBottom": "20px"},
            ),

            html.Label("Vous êtes propriétaire avec un crédit en cours ?", style=label_style),
            dcc.Dropdown(
                id="calc-proprio",
                options=[
                    {"label": "Oui, avec un crédit immobilier en cours", "value": "credit"},
                    {"label": "Oui, sans crédit en cours", "value": "proprio"},
                    {"label": "Non, locataire", "value": "locataire"},
                ],
                placeholder="Sélectionnez votre situation",
                style={"marginBottom": "20px"},
            ),

            html.Label("Votre revenu mensuel net (en euros) :", style=label_style),
            dcc.Slider(
                id="calc-revenu",
                min=800,
                max=10000,
                step=100,
                value=2500,
                marks={
                    800: "800",
                    1500: "1 500",
                    2500: "2 500",
                    4000: "4 000",
                    6000: "6 000",
                    8000: "8 000",
                    10000: "10 000",
                },
                tooltip={"placement": "top", "always_visible": True},
            ),
            html.Div(style={"height": "24px"}),

            html.Label("Scénario de sortie de l'UE :", style=label_style),
            dcc.Dropdown(
                id="calc-scenario",
                options=[
                    {"label": "Accord type Norvège (EEE) : accès au marché maintenu", "value": "norvege"},
                    {"label": "Accord type Suisse : accès partiel, secteur par secteur", "value": "suisse"},
                    {"label": "Sortie complète (règles OMC) : barrières maximales", "value": "omc"},
                ],
                value="suisse",
                style={"marginBottom": "24px"},
            ),

            html.Button(
                "Calculer mon bilan Europe",
                id="calc-button",
                n_clicks=0,
                style={
                    "backgroundColor": C["bleu_france"],
                    "color": C["text_light"],
                    "border": "none",
                    "padding": "14px 32px",
                    "fontSize": "1em",
                    "fontWeight": "700",
                    "borderRadius": "2px",
                    "cursor": "pointer",
                    "width": "100%",
                    "fontFamily": FONT,
                },
            ),
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
        return html.Div(
            style=CARD_ALERT,
            children=[
                html.P(
                    "Veuillez remplir tous les champs pour obtenir votre résultat.",
                    style={"color": C["rouge_marianne"], "margin": "0", "fontFamily": FONT},
                ),
            ],
        )

    revenu_annuel = revenu * 12

    # Canal 1 : Contribution
    contribution = _calculer_contribution(revenu)

    # Canal 2 : Marché unique
    ben_marche, detail_marche = _calculer_benefice_marche_unique(revenu_annuel, secteur)

    # Canal 3 : Euro / crédit
    ben_credit, detail_credit = _calculer_benefice_euro_credit(revenu, proprio)

    # Canal 4 : Effet prix
    ben_prix, detail_prix = _calculer_effet_prix(revenu)

    # Canal 5 : Fonds régionaux
    ben_region, detail_region = _calculer_benefice_regional(region)

    # Totaux
    benefice_total = ben_marche + ben_credit + ben_prix + ben_region
    ratio = round(benefice_total / contribution, 1) if contribution > 0 else 0
    benefice_mensuel = round(benefice_total / 12)
    contribution_mensuelle = round(contribution / 12)

    # Perte Frexit
    perte_frexit = _calculer_perte_frexit(revenu_annuel, scenario)
    mois_courses = round(perte_frexit / 350, 1)
    pleins_essence = int(round(perte_frexit / 80, 0))

    scenario_labels = {
        "norvege": "EEE (type Norvège)",
        "suisse": "Accord bilatéral (type Suisse)",
        "omc": "Sortie complète (règles OMC)",
    }

    return html.Div([
        # Titre
        html.Div(
            style={
                "textAlign": "center", "padding": "24px 0",
                "borderTop": "3px solid " + C["bleu_france"],
                "marginBottom": "24px",
            },
            children=[
                html.P("VOTRE BILAN EUROPE", style={
                    "color": C["muted"], "fontSize": "0.85em", "letterSpacing": "3px",
                    "fontWeight": "600", "marginBottom": "0", "fontFamily": FONT,
                }),
            ],
        ),

        # Coût vs Bénéfice
        html.Div(
            style={"display": "flex", "gap": "16px", "flexWrap": "wrap", "marginBottom": "24px"},
            children=[
                _result_card(
                    "Ce que l'UE vous coûte",
                    str(contribution) + " euros/an",
                    "soit ~" + str(contribution_mensuelle) + " euros/mois (votre part de la contribution nette)",
                    C["rouge_marianne"], "#FEF4F4",
                ),
                _result_card(
                    "Ce que l'UE vous rapporte",
                    "~" + str(benefice_total) + " euros/an",
                    "soit ~" + str(benefice_mensuel) + " euros/mois (somme des 4 canaux ci-dessous)",
                    C["vert"], "#F5FBF8",
                ),
            ],
        ),

        # Ratio
        html.Div(
            style={
                "textAlign": "center", "padding": "20px",
                "backgroundColor": C["highlight"],
                "border": "1px solid " + C["bleu_france"],
                "borderRadius": "2px", "marginBottom": "24px",
            },
            children=[
                html.P(
                    "Pour 1 euro que vous versez, vous en récupérez environ " + str(ratio) + ".",
                    style={
                        "color": C["bleu_france"], "fontSize": "1.1em",
                        "fontWeight": "700", "margin": "0", "fontFamily": FONT,
                    },
                ),
            ],
        ),

        # Détail des 4 canaux
        html.Div(
            style={
                "border": "1px solid " + C["border"], "borderRadius": "2px",
                "padding": "24px", "marginBottom": "24px",
            },
            children=[
                html.P("Détail des bénéfices par canal", style={
                    "color": C["text"], "fontSize": "14px", "fontWeight": "700",
                    "marginBottom": "16px", "fontFamily": FONT,
                }),
                _canal_ligne(
                    "Marché unique (" + secteur + ")",
                    str(ben_marche) + " euros/an",
                    detail_marche,
                ),
                _canal_ligne(
                    "Effet prix (concurrence européenne)",
                    str(ben_prix) + " euros/an",
                    detail_prix,
                ),
                _canal_ligne(
                    "Fonds européens (" + region + ")",
                    str(ben_region) + " euros/an",
                    detail_region,
                ),
                _canal_ligne(
                    "Économie sur votre crédit (euro)",
                    str(ben_credit) + " euros/an",
                    detail_credit if detail_credit else "Non applicable (pas de crédit immobilier en cours).",
                ),
            ],
        ),

        # Perte Frexit
        html.Div(
            style=CARD_ALERT,
            children=[
                html.P(
                    "EN CAS DE FREXIT : " + scenario_labels.get(scenario, ""),
                    style={
                        "color": C["rouge_marianne"], "fontSize": "11px", "fontWeight": "700",
                        "letterSpacing": "0.5px", "margin": "0 0 8px 0", "fontFamily": FONT,
                    },
                ),
                html.P(
                    "Vous perdriez environ " + str(perte_frexit) + " euros par an.",
                    style={
                        "color": C["text"], "fontSize": "1.3em",
                        "fontWeight": "700", "marginBottom": "8px", "fontFamily": FONT,
                    },
                ),
                html.P(
                    "C'est l'équivalent de " + str(mois_courses) + " mois de courses alimentaires "
                    "ou " + str(pleins_essence) + " pleins d'essence.",
                    style={
                        "color": C["text_secondary"], "fontSize": "14px",
                        "lineHeight": "1.6", "margin": "0", "fontFamily": FONT,
                    },
                ),
            ],
        ),

        # Partage
        html.Div(
            style={"textAlign": "center", "marginTop": "32px"},
            children=[
                html.P("Partagez votre résultat", style={
                    "color": C["muted"], "fontSize": "13px", "marginBottom": "12px", "fontFamily": FONT,
                }),
                html.Div(
                    style={"display": "flex", "gap": "12px", "justifyContent": "center", "flexWrap": "wrap"},
                    children=[
                        _share_button(
                            "Partager sur X", C["text"],
                            "https://twitter.com/intent/tweet?text=L'Europe me rapporte environ "
                            + str(benefice_total) + " euros par an, soit "
                            + str(ratio) + " fois ce qu'elle me coute."
                            + " Calculez votre bilan :&url=https://leprixdufrexit.fr/calculateur",
                        ),
                        _share_button(
                            "Partager sur LinkedIn", "#0A66C2",
                            "https://www.linkedin.com/sharing/share-offsite/?url=https://leprixdufrexit.fr/calculateur",
                        ),
                        _share_button(
                            "Envoyer par WhatsApp", "#25D366",
                            "https://wa.me/?text=L'Europe me rapporte environ "
                            + str(benefice_total) + " euros par an. Calculez votre bilan : https://leprixdufrexit.fr/calculateur",
                        ),
                    ],
                ),
            ],
        ),

        # Avertissement méthodologique
        html.Div(
            style={
                "marginTop": "32px", "padding": "16px",
                "borderTop": "1px solid " + C["border"],
            },
            children=[
                html.P(
                    "Ces estimations sont indicatives et reposent sur des moyennes sectorielles et régionales. "
                    "La contribution individuelle est estimée à partir de la progressivité fiscale. "
                    "Les bénéfices sont calculés via quatre canaux : marché unique, effet prix, "
                    "fonds européens et taux d'emprunt. Sources : CEPII, BCE, Commission européenne, INSEE.",
                    style={
                        "color": C["muted"], "fontSize": "12px",
                        "lineHeight": "1.6", "fontFamily": FONT,
                    },
                ),
            ],
        ),
    ])


# =====================================================================
# COMPOSANTS RÉUTILISABLES
# =====================================================================

def _result_card(titre, valeur, detail, couleur, bg):
    return html.Div(
        style={
            "flex": "1", "minWidth": "200px", "padding": "20px",
            "borderLeft": "4px solid " + couleur,
            "backgroundColor": bg, "borderRadius": "2px",
        },
        children=[
            html.P(titre, style={
                "color": C["muted"], "fontSize": "12px", "fontWeight": "600",
                "textTransform": "uppercase", "letterSpacing": "0.5px",
                "margin": "0 0 4px 0", "fontFamily": FONT,
            }),
            html.P(valeur, style={
                "color": couleur, "fontSize": "1.8em",
                "fontWeight": "800", "margin": "0 0 4px 0", "fontFamily": FONT,
            }),
            html.P(detail, style={
                "color": C["text_secondary"], "fontSize": "12px", "margin": "0", "fontFamily": FONT,
            }),
        ],
    )


def _canal_ligne(label, value, detail):
    return html.Div(
        style={
            "padding": "12px 0",
            "borderBottom": "1px solid " + C["border"],
        },
        children=[
            html.Div(
                style={"display": "flex", "justifyContent": "space-between", "marginBottom": "4px"},
                children=[
                    html.Span(label, style={
                        "color": C["text"], "fontSize": "14px",
                        "fontWeight": "600", "fontFamily": FONT,
                    }),
                    html.Span(value, style={
                        "color": C["vert"], "fontSize": "14px",
                        "fontWeight": "700", "fontFamily": FONT,
                    }),
                ],
            ),
            html.P(detail, style={
                "color": C["text_secondary"], "fontSize": "12px",
                "margin": "0", "lineHeight": "1.5", "fontFamily": FONT,
            }),
        ],
    )


def _share_button(label, color, href):
    return html.A(
        html.Div(label, style={
            "backgroundColor": color, "color": C["text_light"],
            "padding": "10px 20px", "borderRadius": "2px",
            "fontSize": "14px", "fontWeight": "600", "fontFamily": FONT,
        }),
        href=href,
        target="_blank",
        style={"textDecoration": "none"},
    )