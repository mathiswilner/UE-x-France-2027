from dash import html, dcc, callback, Input, Output, State

C_BLEU = "#000091"
C_WHITE = "#FFFFFF"
C_RED = "#E1000F"
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
            "borderBottom": "4px solid " + C_RED,
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
                    # Logo
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
                                "color": C_RED,
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

                    # Bouton hamburger (mobile)
                    html.Button(
                        id="hamburger-btn",
                        n_clicks=0,
                        className="hamburger-btn",
                        style={
                            "display": "none",
                            "background": "none",
                            "border": "none",
                            "cursor": "pointer",
                            "padding": "8px",
                            "flexDirection": "column",
                            "gap": "5px",
                        },
                        children=[
                            html.Span(style={
                                "display": "block", "width": "24px", "height": "2px",
                                "backgroundColor": C_WHITE, "borderRadius": "1px",
                            }),
                            html.Span(style={
                                "display": "block", "width": "24px", "height": "2px",
                                "backgroundColor": C_WHITE, "borderRadius": "1px",
                            }),
                            html.Span(style={
                                "display": "block", "width": "24px", "height": "2px",
                                "backgroundColor": C_WHITE, "borderRadius": "1px",
                            }),
                        ],
                    ),
                ],
            ),

            # Menu mobile (caché par défaut)
            html.Div(
                id="mobile-menu",
                style={"display": "none"},
                children=[
                    html.Div(
                        style={
                            "display": "flex",
                            "flexDirection": "column",
                            "paddingBottom": "16px",
                        },
                        children=[
                            dcc.Link(
                                link["label"],
                                href=link["href"],
                                style={
                                    "color": C_WHITE,
                                    "textDecoration": "none",
                                    "padding": "12px 0",
                                    "fontSize": "1em",
                                    "fontWeight": "500",
                                    "borderBottom": "1px solid rgba(255,255,255,0.1)",
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


@callback(
    Output("mobile-menu", "style"),
    Input("hamburger-btn", "n_clicks"),
    State("mobile-menu", "style"),
    prevent_initial_call=True,
)
def toggle_mobile_menu(n_clicks, current_style):
    if current_style.get("display") == "none":
        return {"display": "block"}
    return {"display": "none"}