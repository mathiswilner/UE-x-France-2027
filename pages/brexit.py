from dash import html, register_page
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from styles import C, CARD, CARD_HIGHLIGHT, CARD_ALERT, GC, FONT

register_page(__name__, path="/brexit", name="Brexit")


def layout():
    return html.Div(
        style={
            "maxWidth": "900px", "margin": "0 auto",
            "padding": "40px 5%", "fontFamily": FONT,
        },
        children=[
            _header(),
            _compteur(),
            _indicateurs(),
            _promesses_vs_realite(),
            _et_la_france(),
            _citation(),
        ],
    )


def _header():
    return html.Div(
        style={"marginBottom": "40px"},
        children=[
            html.P("LE MIROIR DU BREXIT", style={
                "color": C["muted"], "fontSize": "0.85em", "letterSpacing": "3px",
                "fontWeight": "600", "marginBottom": "8px", "fontFamily": FONT,
            }),
            html.H1("Ils ont essayé.", style={
                "color": C["text"], "fontSize": "2.4em", "fontWeight": "700",
                "marginBottom": "12px", "marginTop": "0", "fontFamily": FONT,
            }),
            html.P(
                "Le 23 juin 2016, les Britanniques ont voté pour quitter l'Union européenne. "
                "Neuf ans plus tard, voici le bilan.",
                style={
                    "color": C["text_secondary"], "fontSize": "1.1em",
                    "lineHeight": "1.6", "fontFamily": FONT,
                },
            ),
        ],
    )


def _compteur():
    return html.Div(
        style={
            "textAlign": "center",
            "padding": "40px 24px",
            "marginBottom": "40px",
            "borderTop": "2px solid " + C["rouge_marianne"],
            "borderBottom": "1px solid " + C["border"],
            "backgroundColor": C["bg"],
        },
        children=[
            html.P(
                "Depuis le Brexit, l'économie britannique a perdu l'équivalent de :",
                style={
                    "color": C["text_secondary"], "fontSize": "1em",
                    "marginBottom": "8px", "fontFamily": FONT,
                },
            ),
            html.P(
                "140 milliards de livres par an",
                style={
                    "color": C["rouge_marianne"], "fontSize": "2.8em",
                    "fontWeight": "800", "margin": "0 0 8px 0",
                    "lineHeight": "1.1", "fontFamily": FONT,
                },
            ),
            html.P(
                "soit environ 4 000 livres par ménage et par an",
                style={
                    "color": C["text"], "fontSize": "1.2em",
                    "fontWeight": "600", "marginBottom": "12px", "fontFamily": FONT,
                },
            ),
            html.P(
                "Estimation basée sur un PIB inférieur de 6 à 8% à ce qu'il aurait été sans Brexit "
                "(Bloom et al., NBER, 2025).",
                style={
                    "color": C["muted"], "fontSize": "0.85em", "fontFamily": FONT,
                },
            ),
        ],
    )


def _indicateurs():
    indicateurs = [
        {"label": "PIB par habitant", "value": "-6 à 8%", "remaining": "93%", "detail": "Bien au-delà des prévisions initiales de -4%"},
        {"label": "Investissement", "value": "-12 à 18%", "remaining": "85%", "detail": "Les entreprises ont gelé leurs projets"},
        {"label": "Commerce avec l'UE", "value": "-15 à 25%", "remaining": "80%", "detail": "Nouvelles barrières douanières et réglementaires"},
        {"label": "Productivité", "value": "-3 à 4%", "remaining": "96%", "detail": "Perte d'accès aux talents et aux chaînes de valeur"},
        {"label": "Emploi", "value": "-3 à 4%", "remaining": "96%", "detail": "Pénuries de main-d'oeuvre dans plusieurs secteurs"},
    ]

    return html.Div([
        html.H2("Les cinq indicateurs clés", style={
            "color": C["text"], "fontSize": "1.4em", "fontWeight": "700",
            "marginTop": "40px", "marginBottom": "24px", "fontFamily": FONT,
        }),
        html.Div(
            style={
                "border": "1px solid " + C["border"],
                "borderRadius": "2px",
                "padding": "24px",
                "marginBottom": "16px",
                "backgroundColor": C["bg"],
            },
            children=[
                html.P(
                    "Impact observé du Brexit sur l'économie britannique (2025)",
                    style={
                        "color": C["text"], "fontSize": "14px", "fontWeight": "700",
                        "marginBottom": "24px", "fontFamily": FONT,
                    },
                ),
                html.Div([_indicateur_bar(ind) for ind in indicateurs]),
            ],
        ),
        html.P(
            "Sources : Bloom, Bunn, Chen, Mizen, Smietanka & Thwaites (NBER, 2025), "
            "OBR, UK in a Changing Europe",
            style={"color": C["muted"], "fontSize": "12px", "fontFamily": FONT},
        ),
    ])


def _indicateur_bar(ind):
    return html.Div(
        style={"marginBottom": "20px"},
        children=[
            html.Div(
                style={"display": "flex", "justifyContent": "space-between", "marginBottom": "6px"},
                children=[
                    html.Span(ind["label"], style={
                        "color": C["text"], "fontSize": "14px",
                        "fontWeight": "600", "fontFamily": FONT,
                    }),
                    html.Span(ind["value"], style={
                        "color": C["rouge_marianne"], "fontSize": "14px",
                        "fontWeight": "800", "fontFamily": FONT,
                    }),
                ],
            ),
            html.Div(
                style={
                    "backgroundColor": C["rouge_marianne"],
                    "borderRadius": "2px",
                    "height": "28px",
                    "width": "100%",
                    "overflow": "hidden",
                    "opacity": "0.15",
                    "position": "relative",
                },
            ),
            html.Div(
                style={
                    "backgroundColor": C["bleu_france"],
                    "borderRadius": "2px",
                    "height": "28px",
                    "width": ind["remaining"],
                    "marginTop": "-28px",
                    "position": "relative",
                    "transition": "width 0.6s ease",
                },
            ),
            html.P(ind["detail"], style={
                "color": C["text_secondary"], "fontSize": "12px",
                "marginTop": "4px", "marginBottom": "0", "fontFamily": FONT,
            }),
        ],
    )


def _promesses_vs_realite():
    comparaisons = [
        {
            "promesse": "350 millions de livres par semaine pour le NHS",
            "realite": "Le NHS traverse sa pire crise historique. Les listes d'attente ont explosé.",
        },
        {
            "promesse": "Des accords commerciaux fantastiques avec le monde entier",
            "realite": "Les accords signés représentent +0,5% de PIB, contre un coût de -6 à 8%.",
        },
        {
            "promesse": "Reprendre le contrôle de l'immigration",
            "realite": "L'immigration nette a augmenté après le Brexit, atteignant un record en 2023.",
        },
        {
            "promesse": "L'économie va prospérer hors de l'UE",
            "realite": "Le Royaume-Uni est passé derrière la France en PIB nominal.",
        },
        {
            "promesse": "L'impact sera limité, entre -1 et -2% du PIB",
            "realite": "Impact réel : -6 à 8%, et les effets continuent de s'aggraver.",
        },
    ]

    return html.Div([
        html.H2("Ce qu'on leur avait promis, et la réalité", style={
            "color": C["text"], "fontSize": "1.4em", "fontWeight": "700",
            "marginTop": "48px", "marginBottom": "24px", "fontFamily": FONT,
        }),
        html.Div([
            html.Div(
                style={
                    "display": "flex", "gap": "0",
                    "marginBottom": "2px",
                    "border": "1px solid " + C["border"],
                },
                children=[
                    html.Div(
                        style={
                            "flex": "1", "padding": "16px 20px",
                            "backgroundColor": C["bg_alt"],
                            "borderRight": "1px solid " + C["border"],
                        },
                        children=[
                            html.P("PROMESSE (2016)", style={
                                "color": C["muted"], "fontSize": "10px", "fontWeight": "700",
                                "letterSpacing": "1px", "margin": "0 0 6px 0", "fontFamily": FONT,
                            }) if idx == 0 else html.Span(),
                            html.P(c["promesse"], style={
                                "color": C["text_secondary"], "fontSize": "14px",
                                "lineHeight": "1.6", "margin": "0", "fontFamily": FONT,
                            }),
                        ],
                    ),
                    html.Div(
                        style={
                            "flex": "1", "padding": "16px 20px",
                            "backgroundColor": "#FEF4F4",
                        },
                        children=[
                            html.P("RÉALITÉ (2025)", style={
                                "color": C["rouge_marianne"], "fontSize": "10px", "fontWeight": "700",
                                "letterSpacing": "1px", "margin": "0 0 6px 0", "fontFamily": FONT,
                            }) if idx == 0 else html.Span(),
                            html.P(c["realite"], style={
                                "color": C["text"], "fontSize": "14px", "fontWeight": "500",
                                "lineHeight": "1.6", "margin": "0", "fontFamily": FONT,
                            }),
                        ],
                    ),
                ],
            )
            for idx, c in enumerate(comparaisons)
        ]),
        html.P(
            "Sources : BBC, Financial Times, ONS, OBR, Full Fact",
            style={"color": C["muted"], "fontSize": "12px", "marginTop": "12px", "fontFamily": FONT},
        ),
    ])


def _et_la_france():
    return html.Div([
        html.H2("Et pour la France ?", style={
            "color": C["text"], "fontSize": "1.4em", "fontWeight": "700",
            "marginTop": "48px", "marginBottom": "16px", "fontFamily": FONT,
        }),
        html.P(
            "La France est plus intégrée à l'UE que ne l'était le Royaume-Uni au moment du Brexit.",
            style={
                "color": C["text_secondary"], "fontSize": "15px",
                "lineHeight": "1.8", "marginBottom": "20px", "fontFamily": FONT,
            },
        ),
        # Trois cartes de comparaison
        html.Div(
            style={"display": "flex", "gap": "16px", "flexWrap": "wrap", "marginBottom": "24px"},
            children=[
                _france_card(
                    "Zone euro",
                    "La France est dans la zone euro. Le Royaume-Uni ne l'était pas.",
                    "Un Frexit impliquerait un changement de monnaie, avec des conséquences majeures sur "
                    "l'épargne, les emprunts et les prix.",
                ),
                _france_card(
                    "Espace Schengen",
                    "La France est dans Schengen. Le Royaume-Uni ne l'était pas.",
                    "La sortie entraînerait le rétablissement de contrôles aux frontières avec tous "
                    "les pays voisins.",
                ),
                _france_card(
                    "Commerce intra-UE",
                    "60% des exports françaises vont vers l'UE, contre 45% pour le Royaume-Uni avant le Brexit.",
                    "L'économie française est plus dépendante du marché unique que ne l'était l'économie "
                    "britannique.",
                ),
            ],
        ),
        html.Div(
            style=CARD_ALERT,
            children=[
                html.P(
                    "Un Frexit serait au moins aussi coûteux que le Brexit, probablement davantage. "
                    "Selon les scénarios, la perte se situerait entre 54 et 189 milliards d'euros sur 10 ans, "
                    "soit entre 750 et 2 650 euros par ménage et par an.",
                    style={
                        "color": C["text"], "fontSize": "15px", "lineHeight": "1.8",
                        "margin": "0", "fontWeight": "500", "fontFamily": FONT,
                    },
                ),
            ],
        ),
    ])


def _france_card(titre, sous_titre, detail):
    return html.Div(
        style={
            "flex": "1", "minWidth": "240px",
            "border": "1px solid " + C["border"],
            "borderTop": "3px solid " + C["bleu_france"],
            "borderRadius": "2px",
            "padding": "20px",
            "backgroundColor": C["bg"],
        },
        children=[
            html.H3(titre, style={
                "color": C["bleu_france"], "fontSize": "1em", "fontWeight": "700",
                "margin": "0 0 8px 0", "fontFamily": FONT,
            }),
            html.P(sous_titre, style={
                "color": C["text"], "fontSize": "14px", "fontWeight": "600",
                "lineHeight": "1.6", "marginBottom": "8px", "fontFamily": FONT,
            }),
            html.P(detail, style={
                "color": C["text_secondary"], "fontSize": "13px",
                "lineHeight": "1.6", "margin": "0", "fontFamily": FONT,
            }),
        ],
    )


def _citation():
    return html.Div(
        style={
            "marginTop": "48px", "marginBottom": "40px",
            "padding": "32px",
            "backgroundColor": C["bg_alt"],
            "borderLeft": "4px solid " + C["bleu_france"],
            "borderRadius": "2px",
        },
        children=[
            html.P(
                "« Les économistes avaient globalement raison sur la direction et l'ordre de grandeur "
                "de l'impact à long terme, mais ils ont sous-estimé à quel point le processus serait "
                "prolongé et les coûts d'ajustement persistants. »",
                style={
                    "color": C["text"], "fontSize": "16px", "lineHeight": "1.8",
                    "fontStyle": "italic", "marginBottom": "12px", "fontFamily": FONT,
                },
            ),
            html.P(
                "Bloom, Bunn, Mizen, Smietanka & Thwaites, NBER, 2025",
                style={
                    "color": C["muted"], "fontSize": "13px",
                    "margin": "0", "fontFamily": FONT,
                },
            ),
        ],
    )