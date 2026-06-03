from dash import html, dcc, register_page
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from styles import C, CARD, CARD_HIGHLIGHT, CARD_ALERT, GC, FONT
from data.estimates import CONTRIBUTION_NETTE, BENEFICE_TOTAL, RATIO, GAIN_PIB

register_page(__name__, path="/", name="Accueil")

SECTION_TITLE = {
    "color": C["text"], "marginTop": "60px", "marginBottom": "16px",
    "fontSize": "1.6em", "fontWeight": "700", "fontFamily": FONT,
}
NOTE = {
    "color": C["text_secondary"], "lineHeight": "1.8",
    "margin": "0", "fontSize": "15px", "fontFamily": FONT,
}


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
        ],
    )


def _hero():
    return html.Div(
        style={"textAlign": "center", "paddingTop": "40px", "paddingBottom": "40px"},
        children=[
            # Le chiffre que tout le monde connaît
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
                "Tout le monde connaît ce chiffre. Personne ne connaît celui-ci :",
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
        {"label": "Contribution nette", "value": "-" + str(CONTRIBUTION_NETTE) + " Mds€/an",
         "detail": "Versée au budget de l'UE", "color": C["rouge_marianne"]},
        {"label": "Bénéfices économiques", "value": "+" + str(int(BENEFICE_TOTAL)) + " Mds€/an",
         "detail": "Marché unique, IDE, euro, PAC, recherche", "color": C["vert"]},
        {"label": "Ratio bénéfice / coût", "value": "×" + str(int(RATIO)),
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
        style={"textAlign": "center", "marginTop": "20px", "marginBottom": "40px"},
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
                        html.Div("Calculez votre bénéfice personnel →", style={
                            "backgroundColor": C["bleu_france"], "color": C["text_light"],
                            "padding": "14px 28px", "borderRadius": "2px",
                            "fontSize": "1em", "fontWeight": "600",
                            "fontFamily": FONT, "display": "inline-block",
                        }),
                        href="/calculateur",
                        style={"textDecoration": "none"},
                    ),
                    dcc.Link(
                        html.Div("Voir les idées reçues →", style={
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