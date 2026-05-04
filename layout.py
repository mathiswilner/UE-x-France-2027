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
SECTION_TITLE = {"color": C["text"], "marginTop": "40px", "marginBottom": "16px", "fontSize": "1.5em", "fontWeight": "600"}


def build_layout():
    return html.Div(
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
            html.Span(
                "OBSERVATOIRE",
                style={
                    "fontSize": "0.85em",
                    "letterSpacing": "3px",
                    "color": C["muted"],
                    "fontWeight": "600",
                    "display": "block",
                    "marginBottom": "8px",
                },
            ),
            html.H1(
                "Ce que l'Europe rapporte a la France",
                style={
                    "color": C["text"],
                    "fontSize": "2.4em",
                    "marginBottom": "12px",
                    "marginTop": "0",
                    "fontWeight": "700",
                    "lineHeight": "1.2",
                },
            ),
            html.P(
                "Au-dela de la contribution nette : une analyse economique des benefices "
                "de l'appartenance a l'Union europeenne",
                style={
                    "color": C["text_secondary"],
                    "fontSize": "1.15em",
                    "maxWidth": "700px",
                    "margin": "0 auto 16px auto",
                    "lineHeight": "1.6",
                },
            ),
            html.Div(
                style={
                    "display": "inline-block",
                    "backgroundColor": C["card_alt"],
                    "border": "1px solid " + C["border"],
                    "borderRadius": "4px",
                    "padding": "6px 16px",
                },
                children=[
                    html.Span(
                        "Donnees estimees - version de travail",
                        style={"color": C["muted"], "fontSize": "0.85em"},
                    ),
                ],
            ),
        ],
    )


def _kpi_card(label, value, sublabel, color):
    return html.Div(
        style={
            "flex": "1",
            "minWidth": "200px",
            "padding": "16px 20px",
            "borderLeft": "3px solid " + color,
        },
        children=[
            html.P(label, style={"color": C["muted"], "margin": "0 0 4px 0", "fontSize": "13px", "fontWeight": "500"}),
            html.P(value, style={"color": color, "margin": "0 0 4px 0", "fontSize": "1.5em", "fontWeight": "700"}),
            html.P(sublabel, style={"color": C["muted"], "margin": "0", "fontSize": "12px"}),
        ],
    )


def _kpis():
    return html.Div(
        style={
            "display": "flex",
            "gap": "16px",
            "flexWrap": "wrap",
            "marginBottom": "40px",
            "paddingTop": "10px",
            "paddingBottom": "10px",
            "borderTop": "1px solid " + C["border"],
            "borderBottom": "1px solid " + C["border"],
        },
        children=[
            _kpi_card(
                "Contribution nette",
                "-" + str(CONTRIBUTION_NETTE) + " Mds EUR/an",
                "Versee au budget UE",
                C["red"],
            ),
            _kpi_card(
                "Benefices economiques estimes",
                "+" + str(int(BENEFICE_TOTAL)) + " Mds EUR/an",
                "Commerce, IDE, euro, PAC, recherche",
                C["green"],
            ),
            _kpi_card(
                "Ratio benefice / cout",
                "1 EUR verse = " + str(int(RATIO)) + " EUR de retour",
                "Pour chaque euro de contribution nette",
                C["blue"],
            ),
            _kpi_card(
                "Gain cumule de PIB",
                "+" + str(round(GAIN_PIB, 1)) + "%",
                "Par rapport a un scenario hors UE (2000-2025)",
                C["blue"],
            ),
        ],
    )


def _section_overview():
    return html.Div([
        html.H2("Les benefices de l'UE pour la France", style=SECTION_TITLE),
        html.P(
            "Chaque barre represente un canal de benefice economique lie a l'appartenance "
            "a l'Union europeenne. La ligne rouge materialise la contribution nette annuelle "
            "de la France au budget europeen.",
            style={"color": C["text_secondary"], "marginBottom": "20px", "fontSize": "15px", "lineHeight": "1.6"},
        ),
        html.Div(style=CARD, children=[dcc.Graph(figure=fig_ben, config=GC)]),
        html.Div(
            style={"display": "flex", "gap": "20px", "flexWrap": "wrap"},
            children=[
                html.Div(
                    style={**CARD, "flex": "1", "minWidth": "300px"},
                    children=[dcc.Graph(figure=fig_pie, config=GC)],
                ),
                html.Div(
                    style={**CARD, "flex": "1", "minWidth": "300px", "display": "flex", "alignItems": "center"},
                    children=[
                        html.Div([
                            html.H3("L'essentiel", style={"color": C["text"], "marginTop": "0", "marginBottom": "12px"}),
                            html.P(
                                "La contribution nette de la France au budget europeen s'eleve a environ "
                                + str(CONTRIBUTION_NETTE) + " milliards d'euros par an. "
                                "Les benefices economiques lies au marche unique, aux investissements, "
                                "a la monnaie commune et aux programmes europeens sont estimes a "
                                + str(int(BENEFICE_TOTAL)) + " milliards d'euros par an.",
                                style={"color": C["text_secondary"], "lineHeight": "1.8", "fontSize": "15px", "marginBottom": "12px"},
                            ),
                            html.P(
                                "Se focaliser uniquement sur la contribution nette revient a ne regarder "
                                "qu'une seule ligne d'un bilan comptable.",
                                style={"color": C["text"], "lineHeight": "1.8", "fontSize": "15px", "fontWeight": "500"},
                            ),
                        ]),
                    ],
                ),
            ],
        ),
    ])


def _section_budget():
    return html.Div([
        html.H2("Budget europeen : contributions et retours", style=SECTION_TITLE),
        html.Div(style=CARD, children=[dcc.Graph(figure=fig_bud, config=GC)]),
        html.Div(
            style={**CARD, "borderLeft": "4px solid " + C["blue"]},
            children=[
                html.P(
                    "La contribution nette (~10 Mds/an) represente environ 0.35% du PIB francais. "
                    "C'est le prix d'acces a un marche integre de 450 millions de consommateurs, "
                    "sans barrieres douanieres ni reglementaires. Les retours directs incluent la PAC "
                    "(~9 Mds), les fonds structurels (~3.5 Mds) et les programmes de recherche (~2.8 Mds).",
                    style=NOTE,
                ),
            ],
        ),
    ])


def _section_pib():
    return html.Div([
        html.H2("Trajectoire du PIB : France dans l'UE vs contrefactuel", style=SECTION_TITLE),
        html.Div(style=CARD, children=[dcc.Graph(figure=fig_pib, config=GC)]),
        html.Div(
            style={**CARD, "borderLeft": "4px solid " + C["blue"]},
            children=[
                html.P(
                    "Sur la periode 2000-2025, l'appartenance a l'UE aurait genere un gain cumule de +"
                    + str(round(GAIN_PIB, 1)) + "% de PIB par rapport a un scenario ou la France "
                    "serait restee en dehors du marche unique. Cette estimation repose sur un differentiel "
                    "de croissance de ~0.25 point de pourcentage par an, coherent avec la litterature "
                    "(Campos et al., 2014 ; Mayer, Vicard & Zignago, 2018).",
                    style=NOTE,
                ),
            ],
        ),
    ])


def _section_ide():
    return html.Div([
        html.H2("Investissements directs etrangers", style=SECTION_TITLE),
        html.Div(style=CARD, children=[dcc.Graph(figure=fig_ide, config=GC)]),
        html.Div(
            style={**CARD, "borderLeft": "4px solid " + C["green"]},
            children=[
                html.P(
                    "L'appartenance a l'UE augmente les flux d'IDE entrants de 28 a 60% selon "
                    "les estimations (Bruno et al., 2016, 2020). La zone bleue represente les IDE "
                    "reellement recus par la France ; la zone rouge represente le contrefactuel estime "
                    "en l'absence de l'effet attractif du marche unique.",
                    style=NOTE,
                ),
            ],
        ),
    ])


def _section_scenarios():
    return html.Div([
        html.H2("Scenarios de sortie : quel cout pour la France ?", style=SECTION_TITLE),
        html.P(
            "Trois scenarios de sortie de l'UE sont envisages, du moins au plus disruptif. "
            "Les estimations s'appuient sur les travaux du CEPII, du CEP (LSE) et sur "
            "l'observation des effets du Brexit.",
            style={"color": C["text_secondary"], "marginBottom": "20px", "fontSize": "15px", "lineHeight": "1.6"},
        ),
        html.Div(style=CARD, children=[dcc.Graph(figure=fig_sc, config=GC)]),
        html.Div(
            style={"display": "flex", "gap": "16px", "flexWrap": "wrap"},
            children=[
                html.Div(
                    style={**CARD, "flex": "1", "borderLeft": "4px solid " + C["green"]},
                    children=[
                        html.H4("Scenario EEE (type Norvege)", style={"color": C["green"], "margin": "0 0 8px 0"}),
                        html.P(
                            "Acces au marche unique maintenu, mais sans participation aux decisions. "
                            "Contribution financiere preservee. Perte estimee : -2% du PIB, soit "
                            "environ -750 EUR par menage et par an.",
                            style={"color": C["text_secondary"], "margin": "0", "fontSize": "14px", "lineHeight": "1.6"},
                        ),
                    ],
                ),
                html.Div(
                    style={**CARD, "flex": "1", "borderLeft": "4px solid " + C["yellow"]},
                    children=[
                        html.H4("Scenario accord bilateral (type Suisse)", style={"color": C["yellow"], "margin": "0 0 8px 0"}),
                        html.P(
                            "Acces partiel et sectoriel au marche unique. Barrieres non-tarifaires "
                            "significatives. Perte estimee : -4.5% du PIB, soit environ "
                            "-1 700 EUR par menage et par an.",
                            style={"color": C["text_secondary"], "margin": "0", "fontSize": "14px", "lineHeight": "1.6"},
                        ),
                    ],
                ),
                html.Div(
                    style={**CARD, "flex": "1", "borderLeft": "4px solid " + C["red"]},
                    children=[
                        html.H4("Scenario sortie complete (regles OMC)", style={"color": C["red"], "margin": "0 0 8px 0"}),
                        html.P(
                            "Application des droits de douane et barrieres maximales. Perte de poids "
                            "dans les negociations commerciales. Perte estimee : -7% du PIB, soit "
                            "environ -2 650 EUR par menage et par an.",
                            style={"color": C["text_secondary"], "margin": "0", "fontSize": "14px", "lineHeight": "1.6"},
                        ),
                    ],
                ),
            ],
        ),
    ])


def _section_brexit():
    return html.Div([
        html.H2("Le miroir du Brexit", style=SECTION_TITLE),
        html.Div(style=CARD, children=[dcc.Graph(figure=fig_brx, config=GC)]),
        html.Div(
            style={**CARD, "borderLeft": "4px solid " + C["purple"]},
            children=[
                html.P(
                    "Le Brexit constitue un contrefactuel empirique precieux. En 2025, le PIB "
                    "britannique est estime inferieur de 6.5% a ce qu'il aurait ete en l'absence "
                    "de sortie (Bloom et al., 2025, NBER). Les projections pour un Frexit sont "
                    "comparables, voire superieures, compte tenu de l'integration plus profonde "
                    "de la France dans la zone euro.",
                    style=NOTE,
                ),
            ],
        ),
    ])


def _footer():
    return html.Div(
        style={
            "textAlign": "center",
            "marginTop": "60px",
            "paddingTop": "30px",
            "borderTop": "1px solid " + C["border"],
        },
        children=[
            html.P(
                "Les donnees presentees sont des estimations a des fins de demonstration. "
                "Elles seront remplacees par des resultats econometriques.",
                style={"color": C["muted"], "fontSize": "13px", "marginBottom": "8px"},
            ),
            html.P(
                "Projet de memoire HEC — Mathis Wilner-Huet — 2026",
                style={"color": C["muted"], "fontSize": "13px", "marginBottom": "8px"},
            ),
            html.P(
                "Sources : CEPII, Eurostat, BCE, NBER, CER, Bertelsmann Stiftung",
                style={"color": C["border"], "fontSize": "12px"},
            ),
        ],
    )
