from dash import html, dcc, register_page
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from styles import C, CARD_HIGHLIGHT, FONT

register_page(__name__, path="/methodologie", name="Méthodologie")


def layout():
    return html.Div(
        style={
            "maxWidth": "800px", "margin": "0 auto",
            "padding": "40px 5%", "fontFamily": FONT,
        },
        children=[
            _header(),
            _section_principes(),
            _section_sources_academiques(),
            _section_donnees(),
            _section_calculateur(),
            _section_code(),
            _section_limites(),
        ],
    )


def _header():
    return html.Div(
        style={"marginBottom": "40px"},
        children=[
            html.P("MÉTHODOLOGIE", style={
                "color": C["muted"], "fontSize": "0.85em", "letterSpacing": "3px",
                "fontWeight": "600", "marginBottom": "8px", "fontFamily": FONT,
            }),
            html.H1("Transparence totale", style={
                "color": C["text"], "fontSize": "2.2em", "fontWeight": "700",
                "marginBottom": "12px", "marginTop": "0", "fontFamily": FONT,
            }),
            html.P(
                "Chaque chiffre de ce site est sourcé, vérifiable et reproductible. "
                "Voici comment nous estimons l'impact économique de l'Union européenne pour la France.",
                style={
                    "color": C["text_secondary"], "fontSize": "1.1em",
                    "lineHeight": "1.6", "fontFamily": FONT,
                },
            ),
        ],
    )


def _section_principes():
    return html.Div(
        style={"marginBottom": "40px"},
        children=[
            html.H2("Nos principes", style=_h2_style()),
            html.Div(
                style={"display": "flex", "gap": "16px", "flexWrap": "wrap"},
                children=[
                    _principe_card(
                        "01", "Non-partisan",
                        "Ce site n'est affilié à aucun parti politique. Nous ne disons pas "
                        "que l'UE est « bien » ou « mal ». Nous présentons les données "
                        "et laissons chacun se forger sa propre opinion.",
                    ),
                    _principe_card(
                        "02", "Sourcé",
                        "Chaque estimation est accompagnée de ses sources académiques. "
                        "Toutes les études citées sont publiées dans des revues à comité de lecture "
                        "ou par des institutions reconnues (NBER, CEPII, BCE, Commission européenne).",
                    ),
                    _principe_card(
                        "03", "Reproductible",
                        "Le code source est ouvert et les données sont publiques. "
                        "N'importe qui peut vérifier, critiquer ou améliorer nos estimations.",
                    ),
                ],
            ),
        ],
    )


def _principe_card(num, titre, texte):
    return html.Div(
        style={
            "flex": "1", "minWidth": "220px",
            "borderTop": "3px solid " + C["bleu_france"],
            "padding": "20px", "borderRadius": "2px",
            "border": "1px solid " + C["border"],
            "borderTopWidth": "3px",
            "borderTopColor": C["bleu_france"],
        },
        children=[
            html.Span(num, style={
                "color": C["bleu_france"], "fontSize": "12px",
                "fontWeight": "700", "fontFamily": FONT,
            }),
            html.H3(titre, style={
                "color": C["text"], "fontSize": "1.1em", "fontWeight": "700",
                "margin": "8px 0", "fontFamily": FONT,
            }),
            html.P(texte, style={
                "color": C["text_secondary"], "fontSize": "14px",
                "lineHeight": "1.6", "margin": "0", "fontFamily": FONT,
            }),
        ],
    )


def _section_sources_academiques():
    sources = [
        {
            "auteurs": "Mayer, Vicard & Zignago (2018)",
            "institution": "CEPII",
            "titre": "The Cost of Non-Europe, Revisited",
            "apport": "Modèle de gravité structurel. Le marché unique a doublé les échanges intra-UE. "
                      "Gains de bien-être estimés entre 3 et 7% du PIB.",
        },
        {
            "auteurs": "Fontagné & Yotov (2024)",
            "institution": "PSE / Commission européenne",
            "titre": "Reassessing the Gains from the Single Market",
            "apport": "Réévaluation sectorielle. Seulement 50% du potentiel du marché unique est exploité. "
                      "L'agriculture est le secteur où les effets sont les plus forts.",
        },
        {
            "auteurs": "Bloom, Bunn, Chen, Mizen, Smietanka & Thwaites (2025)",
            "institution": "NBER",
            "titre": "The Economic Impact of Brexit",
            "apport": "Le Brexit a réduit le PIB britannique de 6 à 8%, l'investissement de 12 à 18%, "
                      "l'emploi et la productivité de 3 à 4%.",
        },
        {
            "auteurs": "Bruno, Campos, Estrin & Tian (2016, 2020)",
            "institution": "CEP / LSE",
            "titre": "The FDI Premium of EU Membership",
            "apport": "L'appartenance à l'UE augmente les flux d'IDE entrants de 28 à 60%.",
        },
        {
            "auteurs": "Campos, Coricelli & Moretti (2014)",
            "institution": "CEPR",
            "titre": "Economic Growth and EU Membership",
            "apport": "Méthode de contrôle synthétique. L'adhésion à l'UE augmente le PIB par habitant "
                      "de 12 à 22% pour les membres fondateurs.",
        },
        {
            "auteurs": "BCE (2025)",
            "institution": "Banque centrale européenne",
            "titre": "Untapped Potential of the Single Market",
            "apport": "Le marché unique a augmenté le PIB réel par habitant de 12 à 22% pour les États fondateurs. "
                      "Les barrières restantes dans les services sont considérables.",
        },
        {
            "auteurs": "Mion & Ponattu (2019)",
            "institution": "Bertelsmann Stiftung",
            "titre": "Estimating Economic Benefits of the Single Market",
            "apport": "Gains moyens de bien-être d'environ 840 euros par personne et par an. "
                      "Forte hétérogénéité régionale.",
        },
    ]

    return html.Div(
        style={"marginBottom": "40px"},
        children=[
            html.H2("Sources académiques", style=_h2_style()),
            html.P(
                "Les estimations de ce site s'appuient sur les travaux suivants :",
                style={
                    "color": C["text_secondary"], "fontSize": "15px",
                    "lineHeight": "1.6", "marginBottom": "20px", "fontFamily": FONT,
                },
            ),
            html.Div([_source_card(s) for s in sources]),
        ],
    )


def _source_card(source):
    return html.Div(
        style={
            "padding": "16px", "marginBottom": "8px",
            "borderLeft": "3px solid " + C["bleu_france"],
            "backgroundColor": C["bg_alt"], "borderRadius": "2px",
        },
        children=[
            html.P(
                source["auteurs"] + " (" + source["institution"] + ")",
                style={
                    "color": C["bleu_france"], "fontSize": "14px",
                    "fontWeight": "700", "margin": "0 0 4px 0", "fontFamily": FONT,
                },
            ),
            html.P(source["titre"], style={
                "color": C["text"], "fontSize": "14px", "fontStyle": "italic",
                "margin": "0 0 8px 0", "fontFamily": FONT,
            }),
            html.P(source["apport"], style={
                "color": C["text_secondary"], "fontSize": "13px",
                "lineHeight": "1.6", "margin": "0", "fontFamily": FONT,
            }),
        ],
    )


def _section_donnees():
    return html.Div(
        style={"marginBottom": "40px"},
        children=[
            html.H2("Sources de données", style=_h2_style()),
            html.Div(
                style={
                    "border": "1px solid " + C["border"],
                    "borderRadius": "2px", "overflow": "hidden",
                },
                children=[
                    _donnee_ligne("Eurostat", "Commerce, PIB, emploi, prix", "ec.europa.eu/eurostat", True),
                    _donnee_ligne("CEPII (BACI)", "Commerce bilatéral détaillé (HS6)", "cepii.fr", False),
                    _donnee_ligne("Banque de France / BCE", "Taux d'intérêt, IDE, balance des paiements", "banque-france.fr", True),
                    _donnee_ligne("Commission européenne", "Budget UE, fonds par pays et par région", "commission.europa.eu", False),
                    _donnee_ligne("INSEE", "Données nationales et régionales françaises", "insee.fr", True),
                    _donnee_ligne("OCDE (TiVA)", "Valeur ajoutée dans le commerce international", "oecd.org", False),
                ],
            ),
        ],
    )


def _donnee_ligne(nom, description, url, alt_bg):
    bg = C["bg_alt"] if alt_bg else C["bg"]
    return html.Div(
        style={
            "display": "flex", "justifyContent": "space-between",
            "padding": "12px 16px", "backgroundColor": bg,
            "alignItems": "center",
        },
        children=[
            html.Div([
                html.Span(nom, style={
                    "color": C["text"], "fontSize": "14px",
                    "fontWeight": "600", "fontFamily": FONT,
                }),
                html.Span(" : " + description, style={
                    "color": C["text_secondary"], "fontSize": "13px", "fontFamily": FONT,
                }),
            ]),
            html.Span(url, style={
                "color": C["bleu_france"], "fontSize": "12px", "fontFamily": FONT,
            }),
        ],
    )


def _section_calculateur():
    return html.Div(
        style={"marginBottom": "40px"},
        children=[
            html.H2("Méthodologie du calculateur", style=_h2_style()),
            html.P(
                "Le calculateur personnel estime votre bénéfice via quatre canaux indépendants :",
                style={
                    "color": C["text_secondary"], "fontSize": "15px",
                    "lineHeight": "1.6", "marginBottom": "16px", "fontFamily": FONT,
                },
            ),
            _methode_card(
                "Canal 1 : Marché unique",
                "Le bénéfice est estimé comme un pourcentage du revenu annuel, variable selon le secteur d'activité. "
                "Les taux sont dérivés de l'exposition sectorielle au commerce intra-UE "
                "(part des exports vers l'UE, intégration des chaînes de valeur). "
                "Sources : CEPII, INSEE, Eurostat.",
            ),
            _methode_card(
                "Canal 2 : Effet prix",
                "Le marché unique augmente la concurrence et réduit les prix à la consommation. "
                "L'effet est estimé à 1,5% de la consommation annuelle du ménage "
                "(environ 80% du revenu net). Sources : Commission européenne, BCE.",
            ),
            _methode_card(
                "Canal 3 : Fonds européens régionaux",
                "Les fonds européens (PAC, FEDER, FSE, Horizon Europe) reçus par chaque région "
                "sont divisés par la population régionale pour obtenir un montant par habitant et par an. "
                "Sources : Commission européenne, préfectures de région.",
            ),
            _methode_card(
                "Canal 4 : Euro et taux d'intérêt",
                "L'appartenance à la zone euro réduit les taux d'emprunt d'environ 1 point de pourcentage. "
                "Pour les propriétaires avec un crédit en cours, l'économie annuelle est calculée sur la base "
                "d'un crédit estimé à 5 ans de revenu net. Sources : BCE, Banque de France.",
            ),
            _methode_card(
                "Contribution individuelle",
                "La contribution nette de la France (environ 10 milliards d'euros par an) est répartie "
                "entre les ménages de manière progressive, en tenant compte de la structure fiscale "
                "(impôt sur le revenu, TVA). Les ménages les plus modestes contribuent moins, "
                "les plus aisés davantage. Source : DGFiP, INSEE.",
            ),
        ],
    )


def _methode_card(titre, texte):
    return html.Div(
        style={
            "padding": "16px 20px", "marginBottom": "8px",
            "border": "1px solid " + C["border"],
            "borderRadius": "2px",
        },
        children=[
            html.P(titre, style={
                "color": C["text"], "fontSize": "14px",
                "fontWeight": "700", "margin": "0 0 8px 0", "fontFamily": FONT,
            }),
            html.P(texte, style={
                "color": C["text_secondary"], "fontSize": "14px",
                "lineHeight": "1.6", "margin": "0", "fontFamily": FONT,
            }),
        ],
    )


def _section_code():
    return html.Div(
        style={"marginBottom": "40px"},
        children=[
            html.H2("Code source", style=_h2_style()),
            html.Div(
                style=CARD_HIGHLIGHT,
                children=[
                    html.P(
                        "L'intégralité du code source de ce site est disponible sur GitHub :",
                        style={
                            "color": C["text"], "fontSize": "15px",
                            "marginBottom": "8px", "fontFamily": FONT,
                        },
                    ),
                    html.A(
                        "github.com/mathiswilner/UE-x-France-2027",
                        href="https://github.com/mathiswilner/UE-x-France-2027",
                        target="_blank",
                        style={
                            "color": C["bleu_france"], "fontSize": "15px",
                            "fontWeight": "600", "fontFamily": FONT,
                        },
                    ),
                    html.P(
                        "Vous pouvez consulter, vérifier, critiquer ou contribuer au projet.",
                        style={
                            "color": C["text_secondary"], "fontSize": "14px",
                            "marginTop": "8px", "fontFamily": FONT,
                        },
                    ),
                ],
            ),
        ],
    )


def _section_limites():
    return html.Div(
        style={"marginBottom": "40px"},
        children=[
            html.H2("Limites et avertissements", style=_h2_style()),
            html.Div(
                style={
                    "border": "1px solid " + C["border"],
                    "borderLeft": "4px solid " + C["or"],
                    "borderRadius": "2px",
                    "padding": "24px",
                },
                children=[
                    html.Ul(
                        style={"paddingLeft": "20px", "margin": "0"},
                        children=[
                            _limite("Les estimations sectorielles et régionales reposent sur des moyennes. "
                                    "La réalité est plus nuancée et varie selon les entreprises et les territoires."),
                            _limite("Les scénarios de Frexit sont des projections basées sur des modèles économiques. "
                                    "L'issue réelle dépendrait des accords négociés et des politiques mises en place."),
                            _limite("Le calculateur personnel fournit des ordres de grandeur, pas des chiffres exacts. "
                                    "Il vise à illustrer les mécanismes économiques, pas à prédire un montant précis."),
                            _limite("Les données régionales sur les fonds européens sont des estimations qui seront "
                                    "affinées avec les données officielles de la Commission européenne."),
                            _limite("Ce site est un projet de recherche en cours. Les méthodes et données seront "
                                    "actualisées au fur et à mesure de l'avancement des travaux."),
                        ],
                    ),
                ],
            ),
        ],
    )


def _limite(texte):
    return html.Li(texte, style={
        "color": C["text_secondary"], "fontSize": "14px",
        "lineHeight": "1.7", "marginBottom": "8px", "fontFamily": FONT,
    })


def _h2_style():
    return {
        "color": C["text"], "fontSize": "1.4em", "fontWeight": "700",
        "marginBottom": "16px", "fontFamily": FONT,
        "paddingBottom": "8px", "borderBottom": "2px solid " + C["bleu_france"],
    }