from dash import Dash, dcc, html, Input, Output, State
import plotly.express as px
import dash_bootstrap_components as dbc
from aio.aio_components import ThemeChangerAIO, url_dbc_themes, dbc_dark_themes
import layout_templates.layout as tpl

df = px.data.iris()
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

range_slider = dcc.RangeSlider(
        id="rs",  min=0,  max=2.5, step=0.1, value=[1, 2],
        tooltip={"placement": "bottom", "always_visible": True}
    )
controls = tpl.card([(range_slider, "Select petal width:") ])

app.layout = tpl.layout(
    [tpl.card([dcc.Graph(id="graph")]), controls, ThemeChangerAIO(aio_id="theme")],
    id="layout",
    title="Explore The Iris Dataset"
)



@app.callback(
    Output("graph", "figure"),
    Output("layout", "className"),
    Input("rs", "value"),
    Input(ThemeChangerAIO.ids.radio("theme"), "value"),
)
def update(slider_range, theme):
    a, b = slider_range
    m = (df.petal_width > a) & (df.petal_width < b)

    template = url_dbc_themes[theme].lower()
    class_name = ("dbc-dark" if template in dbc_dark_themes else "dbc-light")

    fig = px.scatter(
        df[m],
        x="sepal_width",
        y="sepal_length",
        color="species",
        size="petal_length",
        hover_data=["petal_width"],
        template=template
    )
    return fig, class_name

if __name__ == "__main__":
    app.run_server(debug=True)









# App without the AIO component

#
# from dash import Dash, dcc, html, Input, Output, State
# import plotly.express as px
# import dash_bootstrap_components as dbc
#
# from dash_bootstrap_templates import load_figure_template
#
# load_figure_template()
# import layout_templates.util as util
#
# df = px.data.iris()
# app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
#
#
# theme_radio = dbc.RadioItems(
#     id="themes",
#     options=[
#         {"label": str(i), "value": util.dbc_themes_url[i]} for i in util.dbc_themes_url
#     ],
#     value=util.dbc_themes_url["BOOTSTRAP"],
# )
# change_theme_btn = dbc.Button("Change Theme", id="change-theme", color="secondary", outline=True, size="sm")
#
#
# change_theme = html.Div(
#     [
#         change_theme_btn,
#         dbc.Offcanvas(
#             [
#                 html.P(
#                     "Dark themes are: CYBORG, DARKLY, SLATE, SOLAR, SUPERHERO",
#                     className="small",
#                 ),
#                 theme_radio,
#             ],
#             id="theme-offcanvas",
#             title="Select a Theme",
#             is_open=False,
#             backdrop=False,
#             style={"width": 235},
#         ),
#         html.Div(id="blank-output"),
#     ]
# )
#
# range_slider = dcc.RangeSlider(
#         id="rs",
#         min=0,
#         max=2.5,
#         step=0.1,
#         tooltip={"placement": "bottom", "always_visible": True},
#         value=[1, 2],
#     )
#
#
# app.layout = dbc.Container(
#     [dcc.Graph(id="graph"), dbc.Label("Petal Width:"), range_slider, change_theme,],
#     id="layout",
# )
#
#
# @app.callback(
#     Output("graph", "figure"),
#     Output("layout", "className"),
#     Input("rs", "value"),
#     Input("themes", "value"),
# )
# def update(slider_range, theme):
#     a, b = slider_range
#     m = (df.petal_width > a) & (df.petal_width < b)
#
#     template = util.url_dbc_themes[theme].lower()
#     fig = px.scatter(
#         df[m],
#         x="sepal_width",
#         y="sepal_length",
#         color="species",
#         size="petal_length",
#         hover_data=["petal_width"],
#         template=template
#     )
#     class_name = ("dbc-dark" if template in ["cyborg", "darkly", "slate", "solar", "superhero"] else "dbc-light")
#     return fig, class_name
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
#     Output("blank-output", "children"),
#     Input("themes", "value"),
# )
#
# if __name__ == "__main__":
#     app.run_server(debug=True)
