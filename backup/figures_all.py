import plotly.graph_objects as go
import plotly.express as px
from styles import C

AXIS_STYLE = dict(
    gridcolor="#EAEAEA",
    linecolor=C["border"],
    linewidth=1,
    zeroline=False,
)

LAYOUT_COMMON = dict(
    plot_bgcolor="#FFFFFF",
    paper_bgcolor="#FFFFFF",
    font=dict(
        color=C["text"],
        family="Source Sans Pro, Segoe UI, Helvetica Neue, sans-serif",
        size=14,
    ),
)


def make_fig_benefices(benefices, contribution_nette):
    sorted_data = benefices.sort_values("Mds", ascending=True)

    short_labels = {
        "Marché unique (commerce)": "Marché unique",
        "PAC (retours agricoles)": "PAC",
        "Fonds structurels": "Fonds structurels",
        "Recherche et innovation": "Recherche",
        "IDE additionnels": "IDE",
        "Économie coûts d'emprunt (euro)": "Éco. emprunt (euro)",
        "Négociations commerciales": "Négoce collectif",
        "Erasmus+ et mobilité": "Erasmus+",
    }
    labels = [short_labels.get(c, c) for c in sorted_data["Canal"]]

    fig = go.Figure()
    fig.add_trace(go.Bar(
        y=labels,
        x=sorted_data["Mds"],
        orientation="h",
        marker_color=C["blue"],
        marker_line=dict(width=0),
        text=[str(round(v, 1)) for v in sorted_data["Mds"]],
        textposition="outside",
        textfont=dict(color=C["text"], size=12),
    ))

    fig.add_shape(
        type="line",
        x0=contribution_nette, x1=contribution_nette,
        y0=-0.5, y1=len(sorted_data) - 0.5,
        line=dict(color=C["red"], width=3, dash="solid"),
    )

    fig.add_annotation(
        x=contribution_nette,
        y=len(sorted_data) - 0.5,
        text="▼ Contribution nette : " + str(contribution_nette) + " Mds",
        showarrow=False,
        font=dict(color=C["red"], size=13),
        xanchor="left",
        yanchor="bottom",
        yshift=10,
        xshift=6,
        bgcolor="white",
        bordercolor=C["red"],
        borderwidth=1,
        borderpad=4,
    )

    fig.update_layout(
        **LAYOUT_COMMON,
        title=dict(
            text="Bénéfices annuels de l'UE<br>pour la France (Mds EUR/an)",
            font=dict(size=16, color=C["text"]),
            x=0, xanchor="left",
        ),
        xaxis=dict(
            title="Mds EUR / an",
            **AXIS_STYLE,
            range=[0, max(benefices["Mds"]) * 1.15],
        ),
        yaxis=dict(**AXIS_STYLE, tickfont=dict(size=12)),
        height=500,
        margin=dict(l=120, r=60, t=80, b=50),
        showlegend=False,
    )
    return fig


def make_fig_pie(benefices):
    color_map = {
        "Commerce": C["blue"],
        "Financier": C["gold"],
        "Budget direct": C["green"],
        "Investissement": C["purple"],
        "Capital humain": "#5BA4E6",
    }
    fig = px.pie(
        benefices, values="Mds", names="Catégorie",
        color="Catégorie",
        color_discrete_map=color_map,
        hole=0.45,
    )
    fig.update_traces(
        textinfo="label+percent",
        textposition="outside",
        textfont=dict(size=12, color=C["text"]),
        marker=dict(line=dict(color="#FFFFFF", width=2)),
    )
    fig.update_layout(
        **LAYOUT_COMMON,
        title=dict(
            text="Répartition par catégorie",
            font=dict(size=16, color=C["text"]),
            x=0, xanchor="left",
        ),
        height=500,
        margin=dict(l=80, r=80, t=60, b=40),
        showlegend=False,
    )
    return fig


def make_fig_budget(budget_data):
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=budget_data["Année"], y=budget_data["Contribution brute"],
        name="Contribution brute",
        marker_color=C["red"], opacity=0.75, marker_line=dict(width=0),
    ))
    fig.add_trace(go.Bar(
        x=budget_data["Année"], y=budget_data["Retours directs"],
        name="Retours directs",
        marker_color=C["green"], opacity=0.75, marker_line=dict(width=0),
    ))
    fig.add_trace(go.Scatter(
        x=budget_data["Année"], y=budget_data["Contribution nette"],
        name="Contribution nette",
        line=dict(color=C["text"], width=2.5), mode="lines+markers",
        marker=dict(size=4),
    ))
    fig.update_layout(
        **LAYOUT_COMMON,
        title=dict(
            text="Budget UE : contributions et<br>retours de la France (Mds EUR)",
            font=dict(size=16, color=C["text"]),
            x=0, xanchor="left",
        ),
        barmode="group",
        yaxis=dict(title="Mds EUR", **AXIS_STYLE),
        xaxis=dict(**AXIS_STYLE, dtick=5),
        legend=dict(orientation="h", y=-0.2, font=dict(size=11)),
        height=450,
        margin=dict(l=50, r=20, t=70, b=80),
    )
    return fig


def make_fig_pib(pib_data):
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=list(pib_data["Année"]) + list(pib_data["Année"][::-1]),
        y=list(pib_data["PIB réel"]) + list(pib_data["PIB sans UE"][::-1]),
        fill="toself", fillcolor="rgba(0,51,153,0.08)",
        line=dict(width=0), showlegend=False, hoverinfo="skip",
    ))

    fig.add_trace(go.Scatter(
        x=pib_data["Année"], y=pib_data["PIB réel"],
        name="France (dans l'UE)",
        line=dict(color=C["blue"], width=3), mode="lines",
    ))

    fig.add_trace(go.Scatter(
        x=pib_data["Année"], y=pib_data["PIB sans UE"],
        name="Contrefactuel (hors UE)",
        line=dict(color=C["red"], width=2.5, dash="dash"), mode="lines",
    ))

    last_reel = pib_data["PIB réel"].iloc[-1]
    last_sans = pib_data["PIB sans UE"].iloc[-1]
    gain = round((last_reel / last_sans - 1) * 100, 1)

    fig.add_annotation(
        x=pib_data["Année"].iloc[-1],
        y=(last_reel + last_sans) / 2,
        text="Écart : +" + str(gain) + "%",
        showarrow=True, arrowhead=0, arrowcolor=C["blue"],
        font=dict(size=13, color=C["blue"]),
        bgcolor="white", bordercolor=C["blue"], borderwidth=1, borderpad=4,
    )

    fig.update_layout(
        **LAYOUT_COMMON,
        title=dict(
            text="PIB France : trajectoire réelle vs<br>contrefactuel hors UE (base 100)",
            font=dict(size=16, color=C["text"]),
            x=0, xanchor="left",
        ),
        yaxis=dict(title="Indice (base 100)", **AXIS_STYLE),
        xaxis=dict(**AXIS_STYLE, dtick=5),
        legend=dict(orientation="h", y=-0.2, font=dict(size=11)),
        height=450,
        margin=dict(l=50, r=20, t=70, b=80),
    )
    return fig


def make_fig_ide(ide_data):
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=ide_data["Année"], y=ide_data["IDE totaux"],
        name="IDE réels", fill="tozeroy",
        fillcolor="rgba(0,51,153,0.1)",
        line=dict(color=C["blue"], width=2), mode="lines",
    ))

    fig.add_trace(go.Scatter(
        x=ide_data["Année"], y=ide_data["IDE sans UE"],
        name="IDE estimés hors UE", fill="tozeroy",
        fillcolor="rgba(192,57,43,0.08)",
        line=dict(color=C["red"], width=2, dash="dash"), mode="lines",
    ))

    fig.update_layout(
        **LAYOUT_COMMON,
        title=dict(
            text="IDE entrants en France :<br>réel vs contrefactuel hors UE (Mds EUR)",
            font=dict(size=16, color=C["text"]),
            x=0, xanchor="left",
        ),
        yaxis=dict(title="Mds EUR", **AXIS_STYLE),
        xaxis=dict(**AXIS_STYLE, dtick=5),
        legend=dict(orientation="h", y=-0.2, font=dict(size=11)),
        height=450,
        margin=dict(l=50, r=20, t=70, b=80),
    )
    return fig


def make_fig_scenarios(scenarios):
    fig = go.Figure()
    colors_sc = [C["green"], C["yellow"], C["red"]]

    short_names = {
        "EEE (Norvège)": "EEE\n(Norvège)",
        "Accord bilatéral (Suisse/CETA)": "Bilatéral\n(Suisse)",
        "Sortie complète (OMC)": "Sortie\n(OMC)",
    }

    for i, row in scenarios.iterrows():
        label = short_names.get(row["Scénario"], row["Scénario"])
        fig.add_trace(go.Bar(
            x=[label],
            y=[abs(row["PIB mds"])],
            name=row["Scénario"],
            marker_color=colors_sc[i],
            marker_line=dict(width=0),
            text=(str(row["PIB pct"]) + "% PIB\n"
                  + str(row["Coût ménage"]) + " EUR\n/ménage/an"),
            textposition="inside",
            textfont=dict(color="white", size=11),
        ))

    fig.update_layout(
        **LAYOUT_COMMON,
        title=dict(
            text="Coût estimé d'un Frexit<br>(impact cumulé sur 10 ans)",
            font=dict(size=16, color=C["text"]),
            x=0, xanchor="left",
        ),
        yaxis=dict(title="Perte PIB (Mds EUR)", **AXIS_STYLE),
        xaxis=dict(**AXIS_STYLE, tickfont=dict(size=11)),
        showlegend=False,
        height=450,
        margin=dict(l=50, r=20, t=70, b=50),
    )
    return fig


def make_fig_brexit(brexit):
    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=brexit["Indicateur"], y=brexit["UK observé"],
        name="Royaume-Uni (observé)",
        marker_color=C["purple"], marker_line=dict(width=0),
    ))

    fig.add_trace(go.Bar(
        x=brexit["Indicateur"], y=brexit["France projection"],
        name="France (projection Frexit)",
        marker_color=C["red"], marker_line=dict(width=0),
    ))

    fig.update_layout(
        **LAYOUT_COMMON,
        title=dict(
            text="Le miroir du Brexit :<br>UK observé vs France projection (%)",
            font=dict(size=16, color=C["text"]),
            x=0, xanchor="left",
        ),
        barmode="group",
        yaxis=dict(title="Impact (%)", **AXIS_STYLE),
        xaxis=dict(**AXIS_STYLE, tickfont=dict(size=12)),
        legend=dict(orientation="h", y=-0.2, font=dict(size=11)),
        height=450,
        margin=dict(l=50, r=20, t=70, b=80),
    )
    return fig
