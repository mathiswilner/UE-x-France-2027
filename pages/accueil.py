from dash import html, dcc, register_page
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from styles import C, CARD, CARD_HIGHLIGHT, CARD_ALERT, GC, FONT
from data.estimates import CONTRIBUTION_NETTE, BENEFICE_TOTAL, RATIO, GAIN_PIB

register_page(__name__, path="/", name="Accueil")


def layout():
    return html.Div(
        style={
            "maxWidth": "900px", "margin": "0 auto",
            "padding": "40px 5%", "fontFamily": FONT,
        },
        children=[
            _hero(),
            _kpis(),
            _call_to_action(),
            _pourquoi_ce_site(),
            _quatre_sections(),
            _chiffre_final(),
        ],
    )


def _hero():
    return html.Div(
        style={"textAlign": "center", "paddingTop": "40px", "paddingBottom": "40px"},
        children=[
            html.P(
                "Chaque année, la France verse à l'Union européenne :",
                style={"color": C["text_secondary"], "fontSize": "1.1em", "marginBottom": "8px", "fontFamily": FONT},
            ),
            html.H1(
                "10 milliards d'euros.",
                style={
                    "color": C["rouge_marianne"], "fontSize": "3.5em",
                    "fontWeight": "800", "margin": "0 0 24px 0",
                    "lineHeight": "1.1", "fontFamily": FONT,
                },
            ),
            html.P(
                "Beaucoup connaissent ce chiffre. Personne ne connaît celui-ci :",
                style={"color": C["text_secondary"], "fontSize": "1.1em", "marginBottom": "8px", "fontFamily": FONT},
            ),
            html.H1(
                "151 milliards d'euros.",
                style={
                    "color": C["bleu_france"], "fontSize": "3.5em",
                    "fontWeight": "800", "margin": "0 0 24px 0",
                    "lineHeight": "1.1", "fontFamily": FONT,
                },
            ),
            html.P(
                "C'est ce que l'Union européenne rapporte à la France. Chaque année.",
                style={
                    "color": C["text"], "fontSize": "1.2em",
                    "fontWeight": "600", "marginBottom": "16px", "fontFamily": FONT,
                },
            ),
            html.Div(
                style={
                    "display": "inline-block", "backgroundColor": C["highlight"],
                    "border": "1px solid " + C["bleu_france"], "borderRadius": "2px",
                    "padding": "12px 24px", "marginTop": "8px",
                },
                children=[
                    html.Span(
                        "Pour 1 euro versé, la France récupère 15 euros en bénéfices économiques.",
                        style={"color": C["bleu_france"], "fontSize": "1em", "fontWeight": "600", "fontFamily": FONT},
                    ),
                ],
            ),
        ],
    )


def _kpis():
    kpis = [
        {"label": "Contribution nette", "value": "-" + str(CONTRIBUTION_NETTE) + " Mds euros/an",
         "detail": "Versée au budget de l'UE", "color": C["rouge_marianne"]},
        {"label": "Bénéfices économiques", "value": "+" + str(int(BENEFICE_TOTAL)) + " Mds euros/an",
         "detail": "Marché unique, IDE, euro, PAC, recherche", "color": C["vert"]},
        {"label": "Ratio bénéfice / coût", "value": "x" + str(int(RATIO)),
         "detail": "Pour chaque euro de contribution nette", "color": C["bleu_france"]},
        {"label": "Gain cumulé de PIB", "value": "+" + str(round(GAIN_PIB, 1)) + "%",
         "detail": "Par rapport à un scénario hors UE (2000-2025)", "color": C["bleu_france"]},
    ]
    return html.Div(
        style={
            "display": "flex", "gap": "0", "flexWrap": "wrap",
            "marginTop": "40px", "marginBottom": "40px",
            "borderTop": "2px solid " + C["bleu_france"],
            "borderBottom": "1px solid " + C["border"],
            "borderLeft": "1px solid " + C["border"],
        },
        children=[
            html.Div(
                style={
                    "flex": "1", "minWidth": "180px", "padding": "20px 16px",
                    "borderRight": "1px solid " + C["border"],
                },
                children=[
                    html.P(kpi["label"], style={
                        "color": C["muted"], "margin": "0 0 4px 0",
                        "fontSize": "12px", "fontWeight": "600",
                        "textTransform": "uppercase", "letterSpacing": "0.5px",
                        "fontFamily": FONT,
                    }),
                    html.P(kpi["value"], style={
                        "color": kpi["color"], "margin": "0 0 4px 0",
                        "fontSize": "1.6em", "fontWeight": "800", "fontFamily": FONT,
                    }),
                    html.P(kpi["detail"], style={
                        "color": C["text_secondary"], "margin": "0",
                        "fontSize": "12px", "fontFamily": FONT,
                    }),
                ],
            )
            for kpi in kpis
        ],
    )


def _call_to_action():
    return html.Div(
        style={"textAlign": "center", "marginTop": "20px", "marginBottom": "48px"},
        children=[
            html.P(
                "44% des Français pensent que l'UE existe à leurs dépens.",
                style={"color": C["text_secondary"], "fontSize": "1em", "marginBottom": "4px", "fontFamily": FONT},
            ),
            html.P(
                "Les données montrent le contraire.",
                style={"color": C["text"], "fontSize": "1em", "fontWeight": "600", "marginBottom": "24px", "fontFamily": FONT},
            ),
            html.Div(
                style={"display": "flex", "gap": "16px", "justifyContent": "center", "flexWrap": "wrap"},
                children=[
                    dcc.Link(
                        html.Div("Calculez votre bénéfice personnel \u2192", style={
                            "backgroundColor": C["bleu_france"], "color": C["text_light"],
                            "padding": "14px 28px", "borderRadius": "2px",
                            "fontSize": "1em", "fontWeight": "600",
                            "fontFamily": FONT, "display": "inline-block",
                        }),
                        href="/calculateur",
                        style={"textDecoration": "none"},
                    ),
                    dcc.Link(
                        html.Div("Voir les idées reçues \u2192", style={
                            "backgroundColor": C["bg"], "color": C["bleu_france"],
                            "padding": "14px 28px", "borderRadius": "2px",
                            "border": "1px solid " + C["bleu_france"],
                            "fontSize": "1em", "fontWeight": "600",
                            "fontFamily": FONT, "display": "inline-block",
                        }),
                        href="/idees-recues",
                        style={"textDecoration": "none"},
                    ),
                ],
            ),
        ],
    )


def _pourquoi_ce_site():
    return html.Div(
        style={"marginBottom": "48px"},
        children=[
            html.H2("Pourquoi ce site", style={
                "color": C["text"], "fontSize": "1.5em", "fontWeight": "700",
                "marginBottom": "16px", "fontFamily": FONT,
                "paddingBottom": "8px", "borderBottom": "2px solid " + C["bleu_france"],
            }),
            html.Div(
                style={"display": "flex", "gap": "24px", "flexWrap": "wrap"},
                children=[
                    _stat_card(
                        "44%",
                        "des Français estiment que l'UE « existe aux dépens de la France ».",
                        "Eurobaromètre, 2025",
                    ),
                    _stat_card(
                        "30%",
                        "des Français seulement ont une bonne image de l'Union européenne. "
                        "C'est le taux le plus bas d'Europe.",
                        "Eurobaromètre, 2025",
                    ),
                    _stat_card(
                        "61%",
                        "des Français reconnaissent pourtant que la France a bénéficié "
                        "de son appartenance à l'UE.",
                        "Eurobaromètre, 2025",
                    ),
                ],
            ),
            html.Div(
                style={**CARD_HIGHLIGHT, "marginTop": "24px"},
                children=[
                    html.P(
                        "Les Français sentent que l'UE est utile, mais ne voient pas pourquoi. "
                        "Ce site rend visible ce qui est invisible : les bénéfices concrets, "
                        "chiffrés et vérifiables de l'appartenance à l'Union européenne.",
                        style={
                            "color": C["text"], "fontSize": "15px", "lineHeight": "1.8",
                            "margin": "0", "fontWeight": "500", "fontFamily": FONT,
                        },
                    ),
                ],
            ),
        ],
    )


def _stat_card(chiffre, texte, source):
    return html.Div(
        style={
            "flex": "1", "minWidth": "220px",
            "borderTop": "3px solid " + C["bleu_france"],
            "padding": "20px",
            "border": "1px solid " + C["border"],
            "borderTopWidth": "3px",
            "borderTopColor": C["bleu_france"],
            "borderRadius": "2px",
        },
        children=[
            html.P(chiffre, style={
                "color": C["bleu_france"], "fontSize": "2em",
                "fontWeight": "800", "margin": "0 0 8px 0",
                "fontFamily": FONT,
            }),
            html.P(texte, style={
                "color": C["text_secondary"], "fontSize": "14px",
                "lineHeight": "1.6", "margin": "0 0 8px 0",
                "fontFamily": FONT,
            }),
            html.P(source, style={
                "color": C["muted"], "fontSize": "11px",
                "margin": "0", "fontFamily": FONT,
            }),
        ],
    )


def _quatre_sections():
    sections = [
        {
            "num": "01",
            "titre": "Calculez votre bénéfice personnel",
            "texte": "En 30 secondes, découvrez combien l'Europe vous rapporte "
                     "et combien vous perdriez en cas de Frexit.",
            "lien": "/calculateur",
            "bouton": "Accéder au calculateur",
        },
        {
            "num": "02",
            "titre": "Idées reçues sur l'Europe",
            "texte": "« L'Europe nous coûte trop cher », « L'euro nous a appauvris », "
                     "« La France s'en sortirait mieux seule ». Cinq affirmations passées au crible.",
            "lien": "/idees-recues",
            "bouton": "Voir les idées reçues",
        },
        {
            "num": "03",
            "titre": "Le miroir du Brexit",
            "texte": "Les Britanniques ont voté pour quitter l'UE en 2016. "
                     "Neuf ans plus tard, le bilan est sans appel : entre 6 et 8% de PIB perdu.",
            "lien": "/brexit",
            "bouton": "Voir le bilan du Brexit",
        },
        {
            "num": "04",
            "titre": "L'Europe près de chez vous",
            "texte": "Combien votre région reçoit de fonds européens ? "
                     "Quels sont les secteurs locaux qui dépendent du marché unique ?",
            "lien": "/carte",
            "bouton": "Explorer la carte",
        },
    ]

    return html.Div(
        style={"marginBottom": "48px"},
        children=[
            html.H2("Explorer le site", style={
                "color": C["text"], "fontSize": "1.5em", "fontWeight": "700",
                "marginBottom": "24px", "fontFamily": FONT,
                "paddingBottom": "8px", "borderBottom": "2px solid " + C["bleu_france"],
            }),
            html.Div([_section_card(s) for s in sections]),
        ],
    )


def _section_card(section):
    return html.Div(
        style={
            "display": "flex", "gap": "20px", "alignItems": "flex-start",
            "padding": "24px 0",
            "borderBottom": "1px solid " + C["border"],
        },
        children=[
            html.Span(section["num"], style={
                "backgroundColor": C["bleu_france"],
                "color": C["text_light"],
                "width": "40px", "height": "40px",
                "borderRadius": "50%",
                "display": "flex", "alignItems": "center", "justifyContent": "center",
                "fontSize": "14px", "fontWeight": "700",
                "flexShrink": "0", "fontFamily": FONT,
            }),
            html.Div(
                style={"flex": "1"},
                children=[
                    html.H3(section["titre"], style={
                        "color": C["text"], "fontSize": "1.1em", "fontWeight": "700",
                        "margin": "0 0 8px 0", "fontFamily": FONT,
                    }),
                    html.P(section["texte"], style={
                        "color": C["text_secondary"], "fontSize": "14px",
                        "lineHeight": "1.6", "margin": "0 0 12px 0",
                        "fontFamily": FONT,
                    }),
                    dcc.Link(
                        section["bouton"] + " \u2192",
                        href=section["lien"],
                        style={
                            "color": C["bleu_france"], "fontSize": "14px",
                            "fontWeight": "600", "textDecoration": "none",
                            "fontFamily": FONT,
                        },
                    ),
                ],
            ),
        ],
    )


def _chiffre_final():
    return html.Div(
        style={
            "textAlign": "center",
            "padding": "40px 24px",
            "marginBottom": "20px",
            "borderTop": "2px solid " + C["bleu_france"],
        },
        children=[
            html.P(
                "Ce site est un projet de recherche indépendant et non partisan.",
                style={"color": C["text_secondary"], "fontSize": "14px", "marginBottom": "8px", "fontFamily": FONT},
            ),
            html.P(
                "Les données sont publiques, le code est ouvert, les méthodes sont transparentes.",
                style={"color": C["text_secondary"], "fontSize": "14px", "marginBottom": "16px", "fontFamily": FONT},
            ),
            dcc.Link(
                "Consulter la méthodologie \u2192",
                href="/methodologie",
                style={
                    "color": C["bleu_france"], "fontSize": "14px",
                    "fontWeight": "600", "textDecoration": "none",
                    "fontFamily": FONT,
                },
            ),
        ],
    )