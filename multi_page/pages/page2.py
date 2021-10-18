from dash import dcc
import plotly.express as px
import dash_bootstrap_components as dbc
import layout_templates.layout as tpl
import layout_templates.util as util

df = px.data.tips()
fig = px.scatter(df, x="total_bill", y="tip", opacity=0.65, trendline="ols")

controls = tpl.Form(
    [("My Dropdown", dcc.Dropdown()), ("My Slider", dcc.Slider())],
    header="My control panel"
)

layout = tpl.Layout(
    [
        util.navbar,
        [controls, tpl.Card([dcc.Graph(figure=fig)], width=8)]
    ], title=None
)
