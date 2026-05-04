import dash
from layout import build_layout

app = dash.Dash(
    __name__,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)
server = app.server
app.title = "Ce que l'Europe rapporte a la France"
app.layout = build_layout()

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=8050)
