
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











# from dash import Dash, dcc, html, Input, Output, State
# import plotly.express as px
# import dash_bootstrap_components as dbc
#
# import layout_templates.layout as tpl
# import layout_templates.util as util
#
# from dash_bootstrap_templates import load_figure_template
# load_figure_template()
#
# df = px.data.gapminder()
#
# app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
#
#
# theme_radio = dbc.RadioItems(
#     id="themes",
#     options=[{"label": str(i), "value": util.dbc_themes_url[i], "label_id": i} for i in util.dbc_themes_url],
#     value=util.dbc_themes_url["BOOTSTRAP"],
# )
#
# change_theme = html.Div(
#     [
#         dbc.Button(
#             "Change Theme", id="change-theme", n_clicks=0, color="secondary",outline=True, size="sm"
#         ),
#         dbc.Offcanvas(
#             [html.P("Dark themes are: CYBORG, DARKLY, SLATE, SOLAR, SUPERHERO", className="small"), theme_radio],
#             id="theme-offcanvas",
#             title="Select a Theme",
#             is_open=False,
#             backdrop=False,
#             style={"width":200}
#         ),
#     ]
# )
#
# # todo - change this to Dash shorthand sytnax in Dash 2.1
# slider = util.make_range_slider(df.year.unique(), id="years")
# checklist = util.make_checklist(df.continent.unique(), id="continents")
# dropdown = util.make_dropdown(["gdpPercap", "lifeExp", "pop"], id="indicator")
# table = util.make_datatable(df, id="table")
#
# controls = tpl.card(
#     [
#         (dropdown, "Select indicator (y-axis)"),
#         (checklist, "Select Continents"),
#         (slider, "Select Years"),
#         html.Div(id="blank_output"),
#     ],
# )
#
# tabs = dbc.Tabs(
#     [
#         tpl.tab([dcc.Graph(id="line-chart")], label="Graph"),
#         tpl.tab([table], label="Table")
#     ]
# ),
#
# app.layout = tpl.layout([[(controls, 4), (tabs, 8)], change_theme], id="layout")
#
#
# @app.callback(
#     Output("line-chart", "figure"),
#     Output("table", "data"),
#     Output("layout", "className"),
#     Input("indicator", "value"),
#     Input("continents", "value"),
#     Input("years", "value"),
#     Input("themes", "value"),
# )
# def update_line_chart(indicator, continents, years, theme):
#     if continents == [] or indicator is None:
#         return {}, [], None
#
#     template = util.url_dbc_themes[theme].lower()
#     class_name = "dbc-dark" if template in ["cyborg", "darkly", "slate", "solar", "superhero"] else "dbc-light"
#
#     dff = df[df.year.between(years[0], years[1])]
#     dff = dff[dff.continent.isin(continents)]
#     data = dff.to_dict("records")
#
#     fig = px.line(dff, x="year", y=indicator, color="continent", line_group="country", template=template)
#     fig.update_layout(margin=dict(l=75, r=20, t=10, b=20))
#
#     return fig, data, class_name
#
#
#
# @app.callback(
#     Output("theme-offcanvas", "is_open"),
#     Input("change-theme", "n_clicks"),
#     [State("theme-offcanvas", "is_open")],
# )
# def toggle_theme_offcanvas(n1, is_open):
#     if n1:
#         return not is_open
#     return is_open
#
#
# # Using 2 stylesheets with the delay reduces the  flicker when the theme changes
# app.clientside_callback(
#     """
#     function(url) {
#         // Select the stylesheets.
#         var stylesheets = document.querySelectorAll('link[rel=stylesheet][href^="https://cdn.jsdelivr"]')
#         // Update the url of the main stylesheet.
#         stylesheets[stylesheets.length - 1].href = url
#         // Delay update of the url of the buffer stylesheet.
#         setTimeout(function() {stylesheets[0].href = url;}, 100);
#     }
#     """,
#     Output("blank_output", "children"),
#     Input("themes", "value"),
# )
#
# if __name__ == "__main__":
#     app.run_server(debug=True)
