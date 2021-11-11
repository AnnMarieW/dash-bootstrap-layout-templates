from dash import dcc, html, Input, Output, callback
import plotly.express as px
import layout_templates.layout as tpl
from aio.aio_slide_deck import ThemeChangerAIO
import dash

dash.register_page(__name__)

df = px.data.tips()

layout = tpl.Layout([html.Div(id="parallel")], title=None,)


@callback(
    Output("parallel", "children"), Input(ThemeChangerAIO.ids.store("theme"), "data"),
)
def update(theme):
    return dcc.Graph(figure=px.parallel_categories(df, color="size", template=theme))
