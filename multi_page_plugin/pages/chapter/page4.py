import dash

dash.register_page(__name__)

from dash import dcc, html, Input, Output, callback
import plotly.express as px
import layout_templates.layout as tpl
from aio.aio_components import ThemeChangerAIO, url_dbc_themes

df = px.data.tips()

layout = tpl.Layout([html.Div(id="sunburst"),], title=None,)


@callback(
    Output("sunburst", "children"), Input(ThemeChangerAIO.ids.store("theme"), "data"),
)
def update(theme):
    return dcc.Graph(
        figure=px.sunburst(
            df, path=["day", "time"], values="total_bill", template=theme
        )
    )
