import dash

dash.register_page(__name__, path="/")
from dash import html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import layout_templates.layout as tpl
from aio.aio_components import ThemeChangerAIO

df = px.data.tips()

checklist = dbc.Checklist(
    id="slide-checklist",
    options=[{"label": d, "value": d} for d in ["Thur", "Fri", "Sat", "Sun"]],
    value=["Sun"],
)
slider = dcc.Slider(id="slider",min=10, max=100)
controls = tpl.Form([("Select day:", checklist), ("Page 1 Slider", slider)])

layout = tpl.Layout(
    [[controls, tpl.Card([html.Div(id="slide-graph")], width=8)],], title=None,
)


@callback(
    Output("slide-graph", "children"),
    Input("slide-checklist", "value"),
    Input("slider", "value"),
    Input(ThemeChangerAIO.ids.store("theme"), "data"),
)
def update_slide(days, slider, theme):
    print("page1", slider)
    dff = df[df.day.isin(days)]
    return dcc.Graph(
        figure=px.histogram(
            dff, x="total_bill", y="tip", color="sex", marginal="rug", template=theme
        )
    )
