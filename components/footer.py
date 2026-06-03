from dash import html

C_BLEU = "#000091"
C_MUTED = "#929292"
C_BORDER = "#DDDDDD"


def create_footer():
    return html.Footer(
        style={
            "borderTop": "2px solid " + C_BLEU,
            "marginTop": "80px",
            "paddingTop": "40px",
            "paddingBottom": "40px",
            "textAlign": "center",
        },
        children=[
            html.P(
                "Le prix du Frexit — Observatoire citoyen de l'impact économique de l'UE pour la France",
                style={"color": C_BLEU, "fontSize": "14px", "fontWeight": "600", "marginBottom": "12px"},
            ),
            html.P(
                "Ce site n'est affilié à aucun parti politique. Les données sont publiques, "
                "le code source est ouvert, les méthodes sont transparentes.",
                style={"color": C_MUTED, "fontSize": "13px", "marginBottom": "8px", "maxWidth": "600px", "margin": "0 auto 8px auto"},
            ),
            html.P(
                "Projet de recherche — Mathis Wilner-Huet — 2026",
                style={"color": C_MUTED, "fontSize": "13px", "marginBottom": "8px"},
            ),
            html.P(
                "Sources : CEPII, Eurostat, BCE, NBER, CER, Bertelsmann Stiftung",
                style={"color": C_BORDER, "fontSize": "12px"},
            ),
        ],
    )