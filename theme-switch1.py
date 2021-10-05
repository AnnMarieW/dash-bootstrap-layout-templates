
from dash import Dash, dcc, html, Input, Output, State
import plotly.express as px
import dash_bootstrap_components as dbc

import layout_templates.layout as tpl
from aio.aio_components import ThemeChangerAIO, dbc_dark_themes, url_dbc_themes
import layout_templates.util as util

df = px.data.gapminder()
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


# todo - change this to Dash shorthand sytnax in Dash 2.1
slider = util.make_range_slider(df.year.unique(), id="years")
checklist = util.make_checklist(df.continent.unique(), id="continents")
dropdown = util.make_dropdown(["gdpPercap", "lifeExp", "pop"], id="indicator")
table = util.make_datatable(df, id="table")

controls = tpl.card(
    [
        (dropdown, "Select indicator (y-axis)"),
        (checklist, "Select Continents"),
        (slider, "Select Years"),
    ],
)

tabs = dbc.Tabs(
    [
        tpl.tab([dcc.Graph(id="line-chart")], label="Graph"),
        tpl.tab([table], label="Table")
    ]
),

app.layout = tpl.layout([[(controls, 4), (tabs, 8)], ThemeChangerAIO(aio_id="theme")], id="layout")


@app.callback(
    Output("line-chart", "figure"),
    Output("table", "data"),
    Output("layout", "className"),
    Input("indicator", "value"),
    Input("continents", "value"),
    Input("years", "value"),
    Input(ThemeChangerAIO.ids.radio("theme"), "value"),
)
def update_line_chart(indicator, continents, years, theme):
    if continents == [] or indicator is None:
        return {}, [], None

    template = url_dbc_themes[theme].lower()
    class_name = "dbc-dark" if template in dbc_dark_themes else "dbc-light"

    dff = df[df.year.between(years[0], years[1])]
    dff = dff[dff.continent.isin(continents)]
    data = dff.to_dict("records")

    fig = px.line(dff, x="year", y=indicator, color="continent", line_group="country", template=template)
    fig.update_layout(margin=dict(l=75, r=20, t=10, b=20))

    return fig, data, class_name


if __name__ == "__main__":
    app.run_server(debug=True)



