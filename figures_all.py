import plotly.graph_objects as go
import plotly.express as px
from styles import C

LAYOUT_BASE = dict(
    plot_bgcolor="#FFFFFF",
    paper_bgcolor="#FFFFFF",
    font=dict(color=C["text"], family="Source Sans Pro, Segoe UI, Helvetica Neue, sans-serif", size=14),
    margin=dict(l=20, r=40, t=60, b=40),
)

AXIS_STYLE = dict(
    gridcolor="#EAEAEA",
    linecolor=C["border"],
    linewidth=1,
    zeroline=False,
)


def make_fig_benefices(benefices, contribution_nette):
    sorted_data = benefices.sort_values("Mds", ascending=True)

    fig = go.Figure()

    fig.add_trace(go.Bar(
        y=sorted_data["Canal"],
        x=sorted_data["Mds"],
        orientation="h",
        marker_color=C["blue"],
        marker_line=dict(width=0),
        text=[str(round(v, 1)) + " Mds" for v in sorted_data["Mds"]],
        textposition="outside",
        textfont=dict(color=C["text"], size=13),
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
        text="Contribution nette : " + str(contribution_nette) + " Mds",
        showarrow=False,
        font=dict(color=C["red"], size=13, family="Source Sans Pro, sans-serif"),
        xanchor="left",
        xshift=8,
        yshift=16,
    )

    fig.update_layout(
        plot_bgcolor="#FFFFFF",
        paper_bgcolor="#FFFFFF",
        font=dict(color=C["text"], family="Source Sans Pro, Segoe UI, Helvetica Neue, sans-serif", size=14),
        title=dict(
            text="Benefices annuels de l'UE pour la France (Mds EUR/an)",
            font=dict(size=18, color=C["text"]),
            x=0,
            xanchor="left",
        ),
        xaxis=dict(
            title="Milliards EUR / an",
            **AXIS_STYLE,
            range=[0, max(benefices["Mds"]) * 1.15],
        ),
        yaxis=dict(**AXIS_STYLE, tickfont=dict(size=13)),
        height=480,
        margin=dict(l=20, r=80, t=70, b=50),
        showlegend=False,
    )
    return fig


def make_fig_pie(benefices):
    fig = px.pie(
        benefices, values="Mds", names="Categorie",
        color_discrete_sequence=[C["blue"], C["gold"], C["green"], C["purple"], C["blue_light"]],
        hole=0.55,
    )
    fig.update_traces(
        textinfo="label+percent",
        textfont=dict(size=13, color=C["text"]),
        marker=dict(line=dict(color="#FFFFFF", width=2)),
    )
    fig.update_layout(
        **LAYOUT_BASE,
        title=dict(
            text="Repartition par categorie",
            font=dict(size=16, color=C["text"]),
            x=0, xanchor="left",
        ),
        height=400,
        showlegend=True,
        legend=dict(font=dict(size=12)),
    )
    return fig


def make_fig_budget(budget_data):
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=budget_data["Annee"], y=budget_data["Contribution brute"],
        name="Contribution brute",
        marker_color=C["red"],
        opacity=0.75,
        marker_line=dict(width=0),
    ))
    fig.add_trace(go.Bar(
        x=budget_data["Annee"], y=budget_data["Retours directs"],
        name="Retours directs (PAC, fonds, recherche)",
        marker_color=C["green"],
        opacity=0.75,
        marker_line=dict(width=0),
    ))
    fig.add_trace(go.Scatter(
        x=budget_data["Annee"], y=budget_data["Contribution nette"],
        name="Contribution nette",
        line=dict(color=C["text"], width=2.5),
        mode="lines+markers",
        marker=dict(size=5),
    ))
    fig.update_layout(
        **LAYOUT_BASE,
        title=dict(
            text="Budget UE : contributions et retours de la France (Mds EUR)",
            font=dict(size=18, color=C["text"]),
            x=0, xanchor="left",
        ),
        barmode="group",
        yaxis=dict(title="Milliards EUR", **AXIS_STYLE),
        xaxis=dict(**AXIS_STYLE),
        legend=dict(orientation="h", y=-0.18, font=dict(size=12)),
        height=450,
    )
    return fig


def make_fig_pib(pib_data):
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=list(pib_data["Annee"]) + list(pib_data["Annee"][::-1]),
        y=list(pib_data["PIB reel"]) + list(pib_data["PIB sans UE"][::-1]),
        fill="toself",
        fillcolor="rgba(0,51,153,0.08)",
        line=dict(width=0),
        showlegend=False,
        hoverinfo="skip",
    ))

    fig.add_trace(go.Scatter(
        x=pib_data["Annee"], y=pib_data["PIB reel"],
        name="France (dans l'UE)",
        line=dict(color=C["blue"], width=3),
        mode="lines",
    ))

    fig.add_trace(go.Scatter(
        x=pib_data["Annee"], y=pib_data["PIB sans UE"],
        name="Contrefactuel (hors UE)",
        line=dict(color=C["red"], width=2.5, dash="dash"),
        mode="lines",
    ))

    last_year = pib_data["Annee"].iloc[-1]
    last_reel = pib_data["PIB reel"].iloc[-1]
    last_sans = pib_data["PIB sans UE"].iloc[-1]
    gain = round((last_reel / last_sans - 1) * 100, 1)

    fig.add_annotation(
        x=last_year, y=(last_reel + last_sans) / 2,
        text="Ecart : +" + str(gain) + "%",
        showarrow=True,
        arrowhead=0,
        arrowcolor=C["blue"],
        font=dict(size=14, color=C["blue"]),
        bgcolor="white",
        bordercolor=C["blue"],
        borderwidth=1,
        borderpad=6,
    )

    fig.update_layout(
        **LAYOUT_BASE,
        title=dict(
            text="PIB France : trajectoire reelle vs contrefactuel hors UE (base 100 = 2000)",
            font=dict(size=18, color=C["text"]),
            x=0, xanchor="left",
        ),
        yaxis=dict(title="Indice (base 100 en 2000)", **AXIS_STYLE),
        xaxis=dict(**AXIS_STYLE),
        legend=dict(orientation="h", y=-0.15, font=dict(size=12)),
        height=450,
    )
    return fig


def make_fig_ide(ide_data):
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=ide_data["Annee"], y=ide_data["IDE totaux"],
        name="IDE reels",
        fill="tozeroy",
        fillcolor="rgba(0,51,153,0.1)",
        line=dict(color=C["blue"], width=2),
        mode="lines",
    ))

    fig.add_trace(go.Scatter(
        x=ide_data["Annee"], y=ide_data["IDE sans UE"],
        name="IDE estimes hors UE",
        fill="tozeroy",
        fillcolor="rgba(192,57,43,0.08)",
        line=dict(color=C["red"], width=2, dash="dash"),
        mode="lines",
    ))

    fig.update_layout(
        **LAYOUT_BASE,
        title=dict(
            text="IDE entrants en France : reel vs contrefactuel hors UE (Mds EUR)",
            font=dict(size=18, color=C["text"]),
            x=0, xanchor="left",
        ),
        yaxis=dict(title="Milliards EUR", **AXIS_STYLE),
        xaxis=dict(**AXIS_STYLE),
        legend=dict(orientation="h", y=-0.15, font=dict(size=12)),
        height=450,
    )
    return fig


def make_fig_scenarios(scenarios):
    fig = go.Figure()
    colors_sc = [C["green"], C["yellow"], C["red"]]

    for i, row in scenarios.iterrows():
        fig.add_trace(go.Bar(
            x=[row["Scenario"]],
            y=[abs(row["PIB mds"])],
            name=row["Scenario"],
            marker_color=colors_sc[i],
            marker_line=dict(width=0),
            text=(str(row["PIB pct"]) + "% du PIB\n"
                  + str(row["Cout menage"]) + " EUR/menage/an"),
            textposition="inside",
            textfont=dict(color="white", size=13),
        ))

    fig.update_layout(
        **LAYOUT_BASE,
        title=dict(
            text="Cout estime d'un Frexit selon 3 scenarios (impact cumule sur 10 ans)",
            font=dict(size=18, color=C["text"]),
            x=0, xanchor="left",
        ),
        yaxis=dict(title="Perte de PIB (Mds EUR)", **AXIS_STYLE),
        xaxis=dict(**AXIS_STYLE, tickfont=dict(size=12)),
        showlegend=False,
        height=450,
    )
    return fig


def make_fig_brexit(brexit):
    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=brexit["Indicateur"], y=brexit["UK observe"],
        name="Royaume-Uni (observe, 2025)",
        marker_color=C["purple"],
        marker_line=dict(width=0),
    ))

    fig.add_trace(go.Bar(
        x=brexit["Indicateur"], y=brexit["France projection"],
        name="France (projection Frexit, scenario OMC)",
        marker_color=C["red"],
        marker_line=dict(width=0),
    ))

    fig.update_layout(
        **LAYOUT_BASE,
        title=dict(
            text="Le miroir du Brexit : impact observe (UK) vs projections (France)",
            font=dict(size=18, color=C["text"]),
            x=0, xanchor="left",
        ),
        barmode="group",
        yaxis=dict(title="Impact (%)", **AXIS_STYLE),
        xaxis=dict(**AXIS_STYLE),
        legend=dict(orientation="h", y=-0.18, font=dict(size=12)),
        height=450,
    )
    return fig
