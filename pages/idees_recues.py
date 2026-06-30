from dash import html, dcc, register_page
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from styles import C, CARD, CARD_HIGHLIGHT, CARD_ALERT, CARD_SUCCESS, FONT

register_page(__name__, path="/idees-recues", name="Idées reçues")


IDEES = [
    {
        "id": "cout",
        "num": "01",
        "affirmation": "L'Europe nous coûte 10 milliards par an",
        "verdict": "C'est vrai. Mais c'est une fraction de l'équation.",
        "contenu": [
            {
                "type": "texte",
                "text": (
                    "La France verse environ 10 milliards d'euros nets au budget de l'UE chaque année. "
                    "Ce chiffre est exact et personne ne le conteste."
                ),
            },
            {
                "type": "alerte",
                "text": (
                    "Mais les bénéfices économiques liés au marché unique, aux investissements étrangers, "
                    "à l'euro et aux programmes européens sont estimés à 151 milliards d'euros par an. "
                    "Soit un ratio de 1 pour 15."
                ),
            },
            {
                "type": "analogie",
                "text": (
                    "C'est comme juger le coût de votre connexion internet (30 euros/mois) sans compter tout ce qu'elle vous permet de faire : travailler, étudier, communiquer, vous divertir."
                ),
            },
            {
                "type": "source",
                "text": "Sources : Commission européenne, CEPII (Mayer, Vicard & Zignago, 2018), BCE (2025)",
            },
        ],
    },
    {
        "id": "euro",
        "num": "02",
        "affirmation": "L'euro nous a appauvris",
        "verdict": "79% des Français soutiennent l'euro. C'est un record.",
        "contenu": [
            {
                "type": "texte",
                "text": (
                    "L'euro permet à la France d'emprunter à des taux 0,5 à 2 points plus bas "
                    "que si elle avait sa propre monnaie. C'est un avantage considérable."
                ),
            },
            {
                "type": "chiffre",
                "label": "Sur un crédit immobilier de 200 000 euros sur 20 ans",
                "value": "20 000 à 80 000 euros d'économie",
                "color": C["vert"],
            },
            {
                "type": "chiffre",
                "label": "Économie annuelle pour l'État sur les intérêts de la dette",
                "value": "~25 milliards d'euros",
                "color": C["vert"],
            },
            {
                "type": "texte",
                "text": (
                    "Sans l'euro, la France serait exposée aux crises de change, à la spéculation "
                    "sur sa monnaie et à des taux d'intérêt bien plus élevés."
                ),
            },
            {
                "type": "source",
                "text": "Sources : Eurobaromètre (2025), BCE, Banque de France",
            },
        ],
    },
    {
        "id": "seule",
        "num": "03",
        "affirmation": "La France s'en sortirait mieux seule",
        "verdict": "Les Britanniques pensaient la même chose.",
        "contenu": [
            {
                "type": "texte",
                "text": (
                    "Le 23 juin 2016, les Britanniques ont voté pour quitter l'Union européenne. "
                    "Neuf ans plus tard, le bilan est sans appel."
                ),
            },
            {
                "type": "chiffre",
                "label": "Impact du Brexit sur le PIB britannique",
                "value": "-6 à 8%",
                "color": C["rouge_marianne"],
            },
            {
                "type": "chiffre",
                "label": "Impact sur l'investissement",
                "value": "-12 à 18%",
                "color": C["rouge_marianne"],
            },
            {
                "type": "alerte",
                "text": (
                    "Et le Royaume-Uni n'était ni dans l'euro, ni dans Schengen. "
                    "La France y est. Un Frexit serait donc encore plus disruptif. "
                    "Coût estimé : entre 750 et 2 650 euros de perte par ménage et par an."
                ),
            },
            {
                "type": "source",
                "text": "Sources : Bloom et al. (NBER, 2025), OBR, UK in a Changing Europe",
            },
        ],
    },
    {
        "id": "immigration",
        "num": "04",
        "affirmation": "L'Europe, c'est de l'immigration incontrôlée",
        "verdict": "L'immigration extra-européenne reste une compétence nationale.",
        "contenu": [
            {
                "type": "texte",
                "text": (
                    "La libre circulation intra-UE concerne principalement des actifs qualifiés "
                    "qui contribuent à l'économie française : médecins, ingénieurs, saisonniers agricoles, "
                    "chercheurs."
                ),
            },
            {
                "type": "texte",
                "text": (
                    "L'immigration extra-européenne (hors UE) reste une compétence nationale. "
                    "Chaque pays contrôle ses propres frontières extérieures et délivre ses propres visas."
                ),
            },
            {
                "type": "alerte",
                "text": (
                    "D'ailleurs, 77% des Français souhaitent une politique commune de migration "
                    "au niveau européen, soit plus d'Europe sur ce sujet, pas moins."
                ),
            },
            {
                "type": "source",
                "text": "Sources : Eurobaromètre (2025), Eurostat, Ministère de l'Intérieur",
            },
        ],
    },
    {
        "id": "pouvoir",
        "num": "05",
        "affirmation": "On n'a aucun pouvoir de décision dans l'UE",
        "verdict": "La France est le 2e pays le plus influent de l'Union.",
        "contenu": [
            {
                "type": "texte",
                "text": (
                    "La France dispose d'un arsenal d'influence considérable dans les institutions européennes."
                ),
            },
            {
                "type": "liste",
                "items": [
                    "Droit de veto au Conseil sur les sujets clés (fiscalité, défense, traités)",
                    "79 eurodéputés sur 720 au Parlement européen",
                    "Un Commissaire européen dans le collège",
                    "Co-fondatrice de l'UE, poids historique et symbolique",
                    "Seul pays de l'UE avec un siège permanent au Conseil de sécurité de l'ONU",
                ],
            },
            {
                "type": "alerte",
                "text": (
                    "Quitter l'UE ne rend pas de souveraineté. Le Royaume-Uni doit désormais "
                    "accepter les normes européennes pour exporter vers l'UE, sans avoir voix au chapitre."
                ),
            },
            {
                "type": "source",
                "text": "Sources : Traité de Lisbonne, Parlement européen, Conseil de l'UE",
            },
        ],
    },
]


def layout():
    return html.Div(
        style={
            "maxWidth": "800px", "margin": "0 auto",
            "padding": "40px 5%", "fontFamily": FONT,
        },
        children=[
            _header(),
            html.Div([_idee_card(idee) for idee in IDEES]),
        ],
    )


def _header():
    return html.Div(
        style={"marginBottom": "40px"},
        children=[
            html.P("IDÉES REÇUES", style={
                "color": C["muted"], "fontSize": "0.85em", "letterSpacing": "3px",
                "fontWeight": "600", "marginBottom": "8px", "fontFamily": FONT,
            }),
            html.H1("On vous dit que...", style={
                "color": C["text"], "fontSize": "2.4em", "fontWeight": "700",
                "marginBottom": "12px", "marginTop": "0", "fontFamily": FONT,
            }),
            html.P(
                "Cinq affirmations sur l'Europe, passées au crible des données. "
                "Pas d'opinion. Des faits.",
                style={
                    "color": C["text_secondary"], "fontSize": "1.1em",
                    "lineHeight": "1.6", "fontFamily": FONT,
                },
            ),
        ],
    )


def _idee_card(idee):
    return html.Details(
        style={
            "marginBottom": "16px",
            "border": "1px solid " + C["border"],
            "borderLeft": "4px solid " + C["bleu_france"],
            "borderRadius": "2px",
            "overflow": "hidden",
            "backgroundColor": C["bg"],
        },
        children=[
            html.Summary(
                style={
                    "padding": "20px 24px",
                    "cursor": "pointer",
                    "listStyle": "none",
                    "display": "flex",
                    "alignItems": "center",
                    "gap": "16px",
                    "userSelect": "none",
                },
                children=[
                    html.Span(idee["num"], style={
                        "backgroundColor": C["bleu_france"],
                        "color": C["text_light"],
                        "width": "36px", "height": "36px",
                        "borderRadius": "50%",
                        "display": "flex", "alignItems": "center", "justifyContent": "center",
                        "fontSize": "14px", "fontWeight": "700",
                        "flexShrink": "0", "fontFamily": FONT,
                    }),
                    html.Div(
                        style={"flex": "1"},
                        children=[
                            html.P(idee["affirmation"], style={
                                "color": C["text"], "fontSize": "1.15em", "fontWeight": "700",
                                "margin": "0 0 4px 0", "fontFamily": FONT,
                            }),
                            html.P(idee["verdict"], style={
                                "color": C["bleu_france"], "fontSize": "0.9em",
                                "fontWeight": "600", "margin": "0", "fontFamily": FONT,
                            }),
                        ],
                    ),
                    html.Span("+", style={
                        "color": C["bleu_france"], "fontSize": "1.5em",
                        "fontWeight": "300", "flexShrink": "0",
                    }),
                ],
            ),
            html.Div(
                style={
                    "padding": "0 24px 24px 76px",
                    "borderTop": "1px solid " + C["border"],
                    "paddingTop": "20px",
                },
                children=[_render_bloc(bloc) for bloc in idee["contenu"]],
            ),
        ],
    )


def _render_bloc(bloc):
    if bloc["type"] == "texte":
        return html.P(
            bloc["text"],
            style={
                "color": C["text_secondary"], "fontSize": "15px",
                "lineHeight": "1.8", "marginBottom": "16px", "fontFamily": FONT,
            },
        )

    elif bloc["type"] == "alerte":
        return html.Div(
            style=CARD_HIGHLIGHT,
            children=[
                html.P(bloc["text"], style={
                    "color": C["text"], "fontSize": "15px", "lineHeight": "1.8",
                    "margin": "0", "fontWeight": "500", "fontFamily": FONT,
                }),
            ],
        )

    elif bloc["type"] == "analogie":
        return html.Div(
            style={
                "backgroundColor": C["bg_alt"], "padding": "20px 24px",
                "borderRadius": "2px", "marginBottom": "16px",
                "borderLeft": "4px solid " + C["or"],
            },
            children=[
                html.P("ANALOGIE", style={
                    "color": C["or"], "fontWeight": "700",
                    "fontSize": "11px", "margin": "0 0 8px 0",
                    "letterSpacing": "1px", "fontFamily": FONT,
                }),
                html.P(bloc["text"], style={
                    "color": C["text"], "fontSize": "15px", "lineHeight": "1.8",
                    "margin": "0", "fontStyle": "italic", "fontFamily": FONT,
                }),
            ],
        )

    elif bloc["type"] == "chiffre":
        return html.Div(
            style={
                "display": "flex", "alignItems": "center", "gap": "16px",
                "marginBottom": "12px", "padding": "12px 16px",
                "backgroundColor": C["bg_alt"], "borderRadius": "2px",
            },
            children=[
                html.Span(bloc["value"], style={
                    "color": bloc["color"], "fontSize": "1.3em",
                    "fontWeight": "800", "whiteSpace": "nowrap", "fontFamily": FONT,
                }),
                html.Span(bloc["label"], style={
                    "color": C["text_secondary"], "fontSize": "14px", "fontFamily": FONT,
                }),
            ],
        )

    elif bloc["type"] == "liste":
        return html.Ul(
            style={"marginBottom": "16px", "paddingLeft": "20px"},
            children=[
                html.Li(item, style={
                    "color": C["text_secondary"], "fontSize": "15px",
                    "lineHeight": "1.8", "marginBottom": "4px", "fontFamily": FONT,
                })
                for item in bloc["items"]
            ],
        )

    elif bloc["type"] == "source":
        return html.P(
            bloc["text"],
            style={
                "color": C["muted"], "fontSize": "12px",
                "marginTop": "16px", "marginBottom": "0",
                "borderTop": "1px solid " + C["border"],
                "paddingTop": "12px", "fontFamily": FONT,
            },
        )

    return html.Div()