
from dash import dcc
import plotly.express as px
import layout_templates.layout as tpl
from dash_bootstrap_templates import load_figure_template
load_figure_template("cyborg")
import dash
dash.register_page(__name__)

df = px.data.tips()

layout = tpl.Layout(
    [dcc.Graph(figure=px.sunburst(df, path=["day", "time"], values="total_bill")),],
    title=None,
)
