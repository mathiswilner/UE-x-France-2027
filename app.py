import dash
from dash import html, dcc
from components.navbar import create_navbar
from components.footer import create_footer
from styles import C, FONT

app = dash.Dash(
    __name__,
    use_pages=True,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
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