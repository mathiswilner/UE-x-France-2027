import dash
from dash import html, dcc
from components.navbar import create_navbar
from components.footer import create_footer
from styles import C, FONT

app = dash.Dash(
    __name__,
    use_pages=True,
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"},
        # Open Graph (Facebook, LinkedIn, WhatsApp)
        {"property": "og:title", "content": "Le prix du Frexit"},
        {"property": "og:description", "content": "Pour 1 euro versé à l'UE, la France en récupère 15. Découvrez ce que l'Europe vous rapporte et ce que vous perdriez en cas de Frexit."},
        {"property": "og:type", "content": "website"},
        {"property": "og:url", "content": "https://ue-france-dashboard.onrender.com"},
        {"property": "og:image", "content": "https://ue-france-dashboard.onrender.com/assets/og-image.png"},
        {"property": "og:locale", "content": "fr_FR"},
        {"property": "og:site_name", "content": "Le prix du Frexit"},
        # Twitter/X
        {"name": "twitter:card", "content": "summary_large_image"},
        {"name": "twitter:title", "content": "Le prix du Frexit"},
        {"name": "twitter:description", "content": "Pour 1 euro versé à l'UE, la France en récupère 15. Découvrez ce que l'Europe vous rapporte."},
        {"name": "twitter:image", "content": "https://ue-france-dashboard.onrender.com/assets/og-image.png"},
        # SEO
        {"name": "description", "content": "Le prix du Frexit : observatoire citoyen de l'impact économique de l'UE pour la France. Calculateur personnel, idées reçues, bilan du Brexit."},
        {"name": "author", "content": "Mathis Wilner-Huet"},
    ],
    suppress_callback_exceptions=True,
)
server = app.server
app.title = "Le prix du Frexit"

app.layout = html.Div(
    style={"backgroundColor": C["bg"], "minHeight": "100vh", "fontFamily": FONT},
    children=[
        create_navbar(),
        html.Div(
            dash.page_container,
            style={"minHeight": "calc(100vh - 200px)"},
        ),
        create_footer(),
    ],
)

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=8050)