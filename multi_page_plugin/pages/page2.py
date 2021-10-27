import dash
dash.register_page(__name__)
from dash import dcc, html, Input, Output, callback
import plotly.express as px
import layout_templates.layout as tpl
from aio.aio_components import ThemeChangerAIO


df = px.data.tips()

slider1 = dcc.Slider(id="slider", min=0, max=10)

controls = tpl.Form(
    [("My Dropdown", dcc.Dropdown()), ("Page 2 Slider", slider1)],
    header="My control panel",
)
layout = tpl.Layout(
    [[controls, tpl.Card([html.Div(id="scatter")], width=8)]], title=None
)


@callback(
    Output("scatter", "children"), Input(ThemeChangerAIO.ids.store("theme"), "data"), Input("slider","value")
)
def update(theme, slider):
    return dcc.Graph(
        figure=px.scatter(
            df, x="total_bill", y="tip", opacity=0.65, trendline="ols", template=theme,
        )
    )
