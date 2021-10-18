
from dash import  html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import layout_templates.layout as tpl
import layout_templates.util as util

df = px.data.tips()

checklist = dbc.Checklist(
    id="slide-checklist",
    options=[{"label": d, "value": d} for d in ["Thur", "Fri", "Sat", "Sun"]],
    value=["Sun"],
)
controls = tpl.Form([("Select day:", checklist)])

layout = tpl.Layout(
    [
        util.navbar,
        [controls, tpl.Card([dcc.Graph(id="slide-graph")], width=8)],
    ],
    title=None,
)


@callback(Output("slide-graph", "figure"), Input("slide-checklist", "value"))
def update_slide(days):
    dff = df[df.day.isin(days)]
    return px.histogram(dff, x="total_bill", y="tip", color="sex", marginal="rug")

