from dash import html, dcc

C_BLEU = "#000091"
C_WHITE = "#FFFFFF"
C_BORDER = "#DDDDDD"

LINKS = [
    {"label": "Accueil", "href": "/"},
    {"label": "Calculateur", "href": "/calculateur"},
    {"label": "Idées reçues", "href": "/idees-recues"},
    {"label": "Brexit", "href": "/brexit"},
    {"label": "Carte de France", "href": "/carte"},
    {"label": "Méthodologie", "href": "/methodologie"},
]


def create_navbar():
    return html.Nav(
        style={
            "backgroundColor": C_BLEU,
            "padding": "0 5%",
            "position": "sticky",
            "top": "0",
            "zIndex": "1000",
            "borderBottom": "4px solid #E1000F",
        },
        children=[
            html.Div(
                style={
                    "maxWidth": "1200px",
                    "margin": "0 auto",
                    "display": "flex",
                    "alignItems": "center",
                    "justifyContent": "space-between",
                    "height": "64px",
                },
                children=[
                    # Logo / Nom du site
                    dcc.Link(
                        html.Div([
                            html.Span("LE PRIX DU ", style={
                                "color": C_WHITE,
                                "fontSize": "1.1em",
                                "fontWeight": "700",
                                "letterSpacing": "1px",
                                "fontFamily": "'Source Sans 3', sans-serif",
                            }),
                            html.Span("FREXIT", style={
                                "color": "#E1000F",
                                "fontSize": "1.1em",
                                "fontWeight": "700",
                                "letterSpacing": "1px",
                                "fontFamily": "'Source Sans 3', sans-serif",
                            }),
                        ]),
                        href="/",
                        style={"textDecoration": "none"},
                    ),

                    # Liens desktop
                    html.Div(
                        className="nav-links-desktop",
                        style={
                            "display": "flex",
                            "gap": "8px",
                            "alignItems": "center",
                        },
                        children=[
                            dcc.Link(
                                link["label"],
                                href=link["href"],
                                style={
                                    "color": C_WHITE,
                                    "textDecoration": "none",
                                    "padding": "8px 14px",
                                    "fontSize": "0.9em",
                                    "fontWeight": "500",
                                    "borderRadius": "2px",
                                    "fontFamily": "'Source Sans 3', sans-serif",
                                },
                            )
                            for link in LINKS
                        ],
                    ),
                ],
            ),
        ],
    )