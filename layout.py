from dash import dcc, html
from styles import C, CARD, KPI, GC
from data_estimates import (
    budget_data, pib_data, ide_data, benefices, scenarios, brexit,
    CONTRIBUTION_NETTE, BENEFICE_TOTAL, RATIO, GAIN_PIB,
)
from figures_all import (
    make_fig_benefices, make_fig_pie, make_fig_budget,
    make_fig_pib, make_fig_ide, make_fig_scenarios, make_fig_brexit,
)

fig_ben = make_fig_benefices(benefices, CONTRIBUTION_NETTE)
fig_pie = make_fig_pie(benefices)
fig_bud = make_fig_budget(budget_data)
fig_pib = make_fig_pib(pib_data)
fig_ide = make_fig_ide(ide_data)
fig_sc = make_fig_scenarios(scenarios)
fig_brx = make_fig_brexit(brexit)

NOTE = {"color": C["text_secondary"], "lineHeight": "1.8", "margin": "0", "fontSize": "15px"}
ST = {"color": C["text"], "marginTop": "40px", "marginBottom": "16px", "fontSize": "1.5em", "fontWeight": "600"}


def build_layout():
    return html.Div(
        className="page-container",
        style={
            "backgroundColor": C["bg"],
            "minHeight": "100vh",
            "padding": "40px 8%",
            "fontFamily": "'Source Sans Pro', 'Segoe UI', 'Helvetica Neue', sans-serif",
            "color": C["text"],
            "maxWidth": "1400px",
            "margin": "0 auto",
        },
        children=[
            _header(),
            _kpis(),
            _section_overview(),
            _section_budget(),
            _section_pib(),
            _section_ide(),
            _section_scenarios(),
            _section_brexit(),
            _footer(),
        ],
    )


def _header():
    return html.Div(
        style={"textAlign": "center", "marginBottom": "40px", "paddingTop": "20px"},
        children=[
            html.Span("OBSERVATOIRE", style={
                "fontSize": "0.85em", "letterSpacing": "3px",
                "color": C["muted"], "fontWeight": "600",
                "display": "block", "marginBottom": "8px",
            }),
            html.H1("Ce que l'Europe rapporte à la France", className="main-title", style={
                "color": C["text"], "fontSize": "2.4em", "marginBottom": "12px",
                "marginTop": "0", "fontWeight": "700", "lineHeight": "1.2",
            }),
            html.P(
                "Au-delà de la contribution nette : une analyse économique "
                "des bénéfices de l'appartenance à l'Union européenne",
                style={
                    "color": C["text_secondary"], "fontSize": "1.15em",
                    "maxWidth": "700px", "margin": "0 auto 16px auto", "lineHeight": "1.6",
                },
            ),
            html.Div(style={
                "display": "inline-block", "backgroundColor": C["card_alt"],
                "border": "1px solid " + C["border"], "borderRadius": "4px", "padding": "6px 16px",
            }, children=[
                html.Span("Données estimées — version de travail",
                           style={"color": C["muted"], "fontSize": "0.85em"}),
            ]),
        ],
    )


def _kpi_card(label, value, sublabel, color):
    return html.Div(style={
        "flex": "1", "minWidth": "200px", "padding": "16px 20px",
        "borderLeft": "3px solid " + color,
    }, children=[
        html.P(label, style={"color": C["muted"], "margin": "0 0 4px 0", "fontSize": "13px", "fontWeight": "500"}),
        html.P(value, className="kpi-value", style={"color": color, "margin": "0 0 4px 0", "fontSize": "1.5em", "fontWeight": "700"}),
        html.P(sublabel, style={"color": C["muted"], "margin": "0", "fontSize": "12px"}),
    ])


def _kpis():
    return html.Div(className="kpi-row", style={
        "display": "flex", "gap": "16px", "flexWrap": "wrap", "marginBottom": "40px",
        "paddingTop": "10px", "paddingBottom": "10px",
        "borderTop": "1px solid " + C["border"], "borderBottom": "1px solid " + C["border"],
    }, children=[
        _kpi_card("Contribution nette",
                  "-" + str(CONTRIBUTION_NETTE) + " Mds EUR/an",
                  "Versée au budget UE", C["red"]),
        _kpi_card("Bénéfices économiques estimés",
                  "+" + str(int(BENEFICE_TOTAL)) + " Mds EUR/an",
                  "Commerce, IDE, euro, PAC, recherche", C["green"]),
        _kpi_card("Ratio bénéfice / coût",
                  "1 EUR versé = " + str(int(RATIO)) + " EUR de retour",
                  "Pour chaque euro de contribution nette", C["blue"]),
        _kpi_card("Gain cumulé de PIB",
                  "+" + str(round(GAIN_PIB, 1)) + "%",
                  "Par rapport à un scénario hors UE (2000-2025)", C["blue"]),
    ])


def _section_overview():
    return html.Div([
        html.H2("Les bénéfices de l'UE pour la France", className="section-title", style=ST),
        html.P(
            "Chaque barre représente un canal de bénéfice économique lié à l'appartenance "
            "à l'Union européenne. La ligne rouge matérialise la contribution nette annuelle "
            "de la France au budget européen.",
            style={"color": C["text_secondary"], "marginBottom": "20px", "fontSize": "15px", "lineHeight": "1.6"},
        ),
        html.Div(style=CARD, children=[
            dcc.Graph(figure=fig_ben, config=GC, responsive=True),
        ]),
        html.Div(className="flex-row", style={"display": "flex", "gap": "20px", "flexWrap": "wrap"}, children=[
            html.Div(className="graph-card", style={**CARD, "flex": "1", "minWidth": "300px"}, children=[
                dcc.Graph(figure=fig_pie, config=GC, responsive=True),
            ]),
            html.Div(className="graph-card", style={
                **CARD, "flex": "1", "minWidth": "300px", "display": "flex", "alignItems": "center",
            }, children=[
                html.Div([
                    html.H3("L'essentiel", style={"color": C["text"], "marginTop": "0", "marginBottom": "12px"}),
                    html.P(
                        "La contribution nette de la France au budget européen s'élève à environ "
                        + str(CONTRIBUTION_NETTE) + " milliards d'euros par an. "
                        "Les bénéfices économiques liés au marché unique, aux investissements, "
                        "à la monnaie commune et aux programmes européens sont estimés à "
                        + str(int(BENEFICE_TOTAL)) + " milliards d'euros par an.",
                        style={"color": C["text_secondary"], "lineHeight": "1.8", "fontSize": "15px", "marginBottom": "12px"},
                    ),
                    html.P(
                        "Se focaliser uniquement sur la contribution nette revient à ne regarder "
                        "qu'une seule ligne d'un bilan comptable.",
                        style={"color": C["text"], "lineHeight": "1.8", "fontSize": "15px", "fontWeight": "500"},
                    ),
                ]),
            ]),
        ]),
    ])


def _section_budget():
    return html.Div([
        html.H2("Budget européen : contributions et retours", className="section-title", style=ST),
        html.Div(style=CARD, children=[
            dcc.Graph(figure=fig_bud, config=GC, responsive=True),
        ]),
        html.Div(style={**CARD, "borderLeft": "4px solid " + C["blue"]}, children=[
            html.P(
                "La contribution nette (~10 Mds/an) représente environ 0,35% du PIB français. "
                "C'est le prix d'accès à un marché intégré de 450 millions de consommateurs, "
                "sans barrières douanières ni réglementaires. Les retours directs incluent la PAC "
                "(~9 Mds), les fonds structurels (~3,5 Mds) et les programmes de recherche (~2,8 Mds).",
                style=NOTE,
            ),
        ]),
    ])


def _section_pib():
    return html.Div([
        html.H2("Trajectoire du PIB : France dans l'UE vs contrefactuel", className="section-title", style=ST),
        html.Div(style=CARD, children=[
            dcc.Graph(figure=fig_pib, config=GC, responsive=True),
        ]),
        html.Div(style={**CARD, "borderLeft": "4px solid " + C["blue"]}, children=[
            html.P(
                "Sur la période 2000-2025, l'appartenance à l'UE aurait généré un gain cumulé de +"
                + str(round(GAIN_PIB, 1)) + "% de PIB par rapport à un scénario où la France "
                "serait restée en dehors du marché unique. Cette estimation repose sur un différentiel "
                "de croissance de ~0,25 point de pourcentage par an, cohérent avec la littérature "
                "(Campos et al., 2014 ; Mayer, Vicard & Zignago, 2018).",
                style=NOTE,
            ),
        ]),
    ])


def _section_ide():
    return html.Div([
        html.H2("Investissements directs étrangers", className="section-title", style=ST),
        html.Div(style=CARD, children=[
            dcc.Graph(figure=fig_ide, config=GC, responsive=True),
        ]),
        html.Div(style={**CARD, "borderLeft": "4px solid " + C["green"]}, children=[
            html.P(
                "L'appartenance à l'UE augmente les flux d'IDE entrants de 28 à 60% selon "
                "les estimations (Bruno et al., 2016, 2020). La zone bleue représente les IDE "
                "réellement reçus par la France ; la zone rouge représente le contrefactuel estimé "
                "en l'absence de l'effet attractif du marché unique.",
                style=NOTE,
            ),
        ]),
    ])


def _section_scenarios():
    return html.Div([
        html.H2("Scénarios de sortie : quel coût pour la France ?", className="section-title", style=ST),
        html.P(
            "Trois scénarios de sortie de l'UE sont envisagés, du moins au plus disruptif. "
            "Les estimations s'appuient sur les travaux du CEPII, du CEP (LSE) et sur "
            "l'observation des effets du Brexit.",
            style={"color": C["text_secondary"], "marginBottom": "20px", "fontSize": "15px", "lineHeight": "1.6"},
        ),
        html.Div(style=CARD, children=[
            dcc.Graph(figure=fig_sc, config=GC, responsive=True),
        ]),
        html.Div(className="scenario-cards", style={"display": "flex", "gap": "16px", "flexWrap": "wrap"}, children=[
            html.Div(style={**CARD, "flex": "1", "minWidth": "250px", "borderLeft": "4px solid " + C["green"]}, children=[
                html.H4("Scénario EEE (type Norvège)", style={"color": C["green"], "margin": "0 0 8px 0"}),
                html.P(
                    "Accès au marché unique maintenu, mais sans participation aux décisions. "
                    "Contribution financière préservée. Perte estimée : -2% du PIB, soit "
                    "environ -750 EUR par ménage et par an.",
                    style={"color": C["text_secondary"], "margin": "0", "fontSize": "14px", "lineHeight": "1.6"},
                ),
            ]),
            html.Div(style={**CARD, "flex": "1", "minWidth": "250px", "borderLeft": "4px solid " + C["yellow"]}, children=[
                html.H4("Scénario accord bilatéral (type Suisse)", style={"color": C["yellow"], "margin": "0 0 8px 0"}),
                html.P(
                    "Accès partiel et sectoriel au marché unique. Barrières non-tarifaires "
                    "significatives. Perte estimée : -4,5% du PIB, soit environ "
                    "-1 700 EUR par ménage et par an.",
                    style={"color": C["text_secondary"], "margin": "0", "fontSize": "14px", "lineHeight": "1.6"},
                ),
            ]),
            html.Div(style={**CARD, "flex": "1", "minWidth": "250px", "borderLeft": "4px solid " + C["red"]}, children=[
                html.H4("Scénario sortie complète (règles OMC)", style={"color": C["red"], "margin": "0 0 8px 0"}),
                html.P(
                    "Application des droits de douane et barrières maximales. Perte de poids "
                    "dans les négociations commerciales. Perte estimée : -7% du PIB, soit "
                    "environ -2 650 EUR par ménage et par an.",
                    style={"color": C["text_secondary"], "margin": "0", "fontSize": "14px", "lineHeight": "1.6"},
                ),
            ]),
        ]),
    ])


def _section_brexit():
    return html.Div([
        html.H2("Le miroir du Brexit", className="section-title", style=ST),
        html.Div(style=CARD, children=[
            dcc.Graph(figure=fig_brx, config=GC, responsive=True),
        ]),
        html.Div(style={**CARD, "borderLeft": "4px solid " + C["purple"]}, children=[
            html.P(
                "Le Brexit constitue un contrefactuel empirique précieux. En 2025, le PIB "
                "britannique est estimé inférieur de 6,5% à ce qu'il aurait été en l'absence "
                "de sortie (Bloom et al., 2025, NBER). Les projections pour un Frexit sont "
                "comparables, voire supérieures, compte tenu de l'intégration plus profonde "
                "de la France dans la zone euro.",
                style=NOTE,
            ),
        ]),
    ])


def _footer():
    return html.Div(style={
        "textAlign": "center", "marginTop": "60px", "paddingTop": "30px",
        "borderTop": "1px solid " + C["border"],
    }, children=[
        html.P(
            "Les données présentées sont des estimations à des fins de démonstration. "
            "Elles seront remplacées par des résultats économétriques.",
            style={"color": C["muted"], "fontSize": "13px", "marginBottom": "8px"},
        ),
        html.P(
            "Projet de mémoire HEC — Mathis Wilner-Huet — 2026",
            style={"color": C["muted"], "fontSize": "13px", "marginBottom": "8px"},
        ),
        html.P(
            "Sources : CEPII, Eurostat, BCE, NBER, CER, Bertelsmann Stiftung",
            style={"color": C["border"], "fontSize": "12px"},
        ),
    ])
