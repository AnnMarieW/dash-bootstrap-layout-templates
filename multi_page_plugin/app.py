# from dash import Dash, html
# import dash_bootstrap_components as dbc
# import pages_plugin
#
# app = Dash(
#     __name__,
#     plugins=[pages_plugin],
#     suppress_callback_exceptions=True,
#     external_stylesheets=[dbc.themes.BOOTSTRAP],
# )
#
#
# navbar = dbc.NavbarSimple(
#     children=[
#         dbc.NavItem(dbc.NavLink("Page 1", href="/pages/page1")),
#         dbc.DropdownMenu(
#             children=[
#                 dbc.DropdownMenuItem("More pages", header=True),
#                 dbc.DropdownMenuItem("Page 2", href="/pages/page2"),
#                 dbc.DropdownMenuItem("Page 3", href="#"),
#             ],
#             nav=True,
#             in_navbar=True,
#             label="More",
#         ),
#     ],
#     brand="Multi Page App Plugin Demo",
#     brand_href="#",
#     color="primary",
#     dark=True,
# )
#
#
# app.layout = dbc.Container([navbar, pages_plugin.page_container], fluid=True)
#
#
# if __name__ == "__main__":
#     app.run_server(debug=True)

# ---------------------------------------------------
# from dash import Dash, html, dcc
# import dash
# import pages_plugin
# import dash_bootstrap_components as dbc
#
# app = Dash(__name__, plugins=[pages_plugin],
#             suppress_callback_exceptions=True,
#         external_stylesheets=[dbc.themes.BOOTSTRAP],
#
#            )
#
# app.layout = html.Div([
#     html.H1('App Frame'),
#
#     html.Div(
#         dcc.Link('Go back home', href=dash.page_registry['pages.home']['path'])
#     ),
#
#     html.Div([
#         html.Div(dcc.Link(
#             f"{page['name']} - {page['path']}",
#             href=page['path']
#         ))
#         for page in dash.page_registry.values()
#         if page['module'] != 'pages.not_found_404'
#     ]),
#
#     pages_plugin.page_container
#
# ])
#
# dash.register_page('another_page', layout='Another page', path='/another-page')
# dash.register_page('and_again', layout='And again!', path='/and-again')
#
# if __name__ == '__main__':
#     app.run_server(debug=True)

#
#
# import dash
# import pages_plugin
# from dash import Dash, html, dcc
# import dash_bootstrap_components as dbc
# from aio.aio_slide_deck import ThemeChangerAIO
#
# app = Dash(__name__, plugins=[pages_plugin], external_stylesheets=[dbc.themes.BOOTSTRAP])
#
# print(dash.page_registry)
# navbar = dbc.NavbarSimple(
#     dbc.DropdownMenu(
#         [
#             dbc.DropdownMenuItem(page["name"], href=page["path"])
#             for page in dash.page_registry.values()
#             if page["module"] != "pages.not_found_404"
#         ],
#         nav=True,
#         label="More Pages",
#     ),
#     brand="Multi Page App Plugin Demo",
#     color="primary",
#     dark=True,
#     className="mb-2",
# )
#
# app.layout = dbc.Container(
#     [navbar, pages_plugin.page_container, ThemeChangerAIO(aio_id="theme"),],
#     className="dbc",
#     fluid=True,
# )
#
# if __name__ == "__main__":
#     app.run_server(debug=True)



import dash
#import pages_plugin
import dash_labs as dl
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
#from aio.aio_slide_deck import ThemeChangerAIO
from dash_bootstrap_templates import ThemeChangerAIO

app = Dash(__name__, plugins=[dl.plugins.pages], external_stylesheets=[dbc.themes.BOOTSTRAP])



print(dash.page_registry)
navbar = dbc.NavbarSimple(
    dbc.DropdownMenu(
        [
            dbc.DropdownMenuItem(page["name"], href=page["path"])
            for page in dash.page_registry.values()
            if page["module"] != "pages.not_found_404"
        ],
        nav=True,
        label="More Pages",
    ),
    brand="Multi Page App Plugin Demo",
    color="primary",
    dark=True,
    className="mb-2",
)

app.layout = dbc.Container(
    [navbar, dl.plugins.page_container, ThemeChangerAIO(aio_id="theme"),],
    className="dbc",
    fluid=True,
)

if __name__ == "__main__":
    app.run_server(debug=True)
