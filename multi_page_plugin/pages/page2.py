
from dash import dcc
import plotly.express as px
import layout_templates.layout as tpl
from dash_bootstrap_templates import load_figure_template
load_figure_template("cyborg")
import dash

dash.register_page(__name__)

df = px.data.tips()
fig = px.scatter(df, x="total_bill", y="tip", opacity=0.65, trendline="ols")

controls = tpl.Form(
    [("My Dropdown", dcc.Dropdown()), ("My Slider", dcc.Slider())],
    header="My control panel",
)

layout = tpl.Layout(
    [[controls, tpl.Card([dcc.Graph(figure=fig)], width=8)]], title=None
)
