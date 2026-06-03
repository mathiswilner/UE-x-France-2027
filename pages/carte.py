from dash import html, register_page
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from styles import C, CARD_HIGHLIGHT, FONT

register_page(__name__, path="/carte", name="Carte de France")


def layout():
    return html.Div(
        style={
            "maxWidth": "800px", "margin": "0 auto",
            "padding": "40px 5%", "fontFamily": FONT,
        },
        children=[
            html.Div(
                style={"marginBottom": "40px"},
                children=[
                    html.P("CARTE DE FRANCE", style={
                        "color": C["muted"], "fontSize": "0.85em", "letterSpacing": "3px",
                        "fontWeight": "600", "marginBottom": "8px", "fontFamily": FONT,
                    }),
                    html.H1("L'Europe près de chez vous", style={
                        "color": C["text"], "fontSize": "2.2em", "fontWeight": "700",
                        "marginBottom": "12px", "marginTop": "0", "fontFamily": FONT,
                    }),
                    html.P(
                        "Découvrez ce que l'Union européenne finance dans votre région, "
                        "combien elle y rapporte, et ce que vous perdriez en cas de sortie.",
                        style={
                            "color": C["text_secondary"], "fontSize": "1.1em",
                            "lineHeight": "1.6", "fontFamily": FONT,
                        },
                    ),
                ],
            ),

            html.Div(
                style=CARD_HIGHLIGHT,
                children=[
                    html.P("Section en cours de développement", style={
                        "color": C["bleu_france"], "fontSize": "14px",
                        "fontWeight": "700", "marginBottom": "8px", "fontFamily": FONT,
                    }),
                    html.P(
                        "Cette carte interactive est en cours de construction. "
                        "Elle présentera, région par région : les fonds européens reçus "
                        "(PAC, FEDER, FSE, Horizon Europe), les emplois dépendant du marché unique, "
                        "les secteurs clés liés à l'UE et la perte estimée en cas de Frexit.",
                        style={
                            "color": C["text_secondary"], "fontSize": "15px",
                            "lineHeight": "1.8", "margin": "0", "fontFamily": FONT,
                        },
                    ),
                ],
            ),

            html.Div(
                style={
                    "marginTop": "32px",
                    "border": "1px solid " + C["border"],
                    "borderRadius": "2px",
                    "padding": "24px",
                },
                children=[
                    html.P("Données déjà disponibles pour chaque région :", style={
                        "color": C["text"], "fontSize": "14px", "fontWeight": "700",
                        "marginBottom": "16px", "fontFamily": FONT,
                    }),
                    _region_table(),
                ],
            ),

            html.P(
                "Sources : Commission européenne, préfectures de région, INSEE. "
                "Données estimées, à confirmer par les chiffres officiels.",
                style={
                    "color": C["muted"], "fontSize": "12px",
                    "marginTop": "16px", "fontFamily": FONT,
                },
            ),
        ],
    )


def _region_table():
    regions = [
        ("Île-de-France", "3,2 Mds", "12,3 M", "~37 euros"),
        ("Auvergne-Rhône-Alpes", "2,8 Mds", "8,1 M", "~49 euros"),
        ("Nouvelle-Aquitaine", "3,1 Mds", "6,0 M", "~74 euros"),
        ("Occitanie", "3,5 Mds", "5,9 M", "~85 euros"),
        ("Hauts-de-France", "3,8 Mds", "6,0 M", "~91 euros"),
        ("Grand Est", "2,9 Mds", "5,6 M", "~74 euros"),
        ("Provence-Alpes-Côte d'Azur", "2,4 Mds", "5,1 M", "~67 euros"),
        ("Bretagne", "2,6 Mds", "3,4 M", "~109 euros"),
        ("Pays de la Loire", "2,1 Mds", "3,8 M", "~79 euros"),
        ("Normandie", "2,3 Mds", "3,3 M", "~100 euros"),
        ("Bourgogne-Franche-Comté", "2,7 Mds", "2,8 M", "~138 euros"),
        ("Centre-Val de Loire", "2,2 Mds", "2,6 M", "~121 euros"),
        ("Corse", "0,6 Mds", "0,34 M", "~252 euros"),
        ("Outre-mer", "4,2 Mds", "2,2 M", "~273 euros"),
    ]

    header_style = {
        "color": C["text"], "fontSize": "12px", "fontWeight": "700",
        "padding": "10px 12px", "textAlign": "left",
        "borderBottom": "2px solid " + C["bleu_france"],
        "fontFamily": FONT,
    }
    cell_style = {
        "color": C["text_secondary"], "fontSize": "13px",
        "padding": "8px 12px", "borderBottom": "1px solid " + C["border"],
        "fontFamily": FONT,
    }
    cell_strong = {
        **cell_style,
        "color": C["text"], "fontWeight": "600",
    }

    return html.Table(
        style={"width": "100%", "borderCollapse": "collapse"},
        children=[
            html.Thead(
                html.Tr([
                    html.Th("Région", style=header_style),
                    html.Th("Fonds UE (2021-2027)", style=header_style),
                    html.Th("Population", style=header_style),
                    html.Th("Par habitant/an", style=header_style),
                ]),
            ),
            html.Tbody([
                html.Tr([
                    html.Td(r[0], style=cell_strong),
                    html.Td(r[1], style=cell_style),
                    html.Td(r[2], style=cell_style),
                    html.Td(r[3], style={**cell_style, "color": C["bleu_france"], "fontWeight": "700"}),
                ])
                for r in regions
            ]),
        ],
    )