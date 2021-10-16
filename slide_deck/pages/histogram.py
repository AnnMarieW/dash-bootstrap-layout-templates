from dash import  dcc, Input, Output, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import layout_templates.layout as tpl

df = px.data.tips()

checklist = dbc.Checklist(
    id="slide-checklist",
    options=[{"label": d, "value": d} for d in ["Thur", "Fri", "Sat", "Sun"]],
    value=["Sun"],
)
checklist_card = tpl.card([(checklist, "Select day:")])
slide_content = tpl.layout(
    [
        [
            dbc.Col(checklist_card, width=3),
            dbc.Col(dcc.Graph(id="slide-graph"), width=9),
        ],
    ],
    title=None,
)

layout = tpl.card([(slide_content, "Here is some data on tips",)]),


@callback(Output("slide-graph", "figure"), Input("slide-checklist", "value"))
def update_slide(days):
    dff = df[df.day.isin(days)]
    return px.histogram(dff, x="total_bill", y="tip", color="sex", marginal="rug")

