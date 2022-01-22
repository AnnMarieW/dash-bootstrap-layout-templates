import dash
from dash import Dash, html
import dash_bootstrap_components as dbc
from dash_labs import dashdown
import dash_labs as dl

"""
Select code highlight style:  https://highlightjs.org/static/demo/
get url: https://cdnjs.com/libraries/highlight.js
Add url to external_stylesheets or to assets/
"""

# light
hljs = "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.3.1/styles/foundation.min.css"
# dark
# hljs = "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.3.1/styles/github-dark-dimmed.min.css"

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 90,
    "left": 0,
    "bottom": 0,
    "width": "12rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
    "overflow": "auto",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "12rem",
    "margin-right": "2rem",
    "padding": "2rem 2rem",
}

app = Dash(
    __name__,
    plugins=[dl.plugins.pages],
    external_stylesheets=[dbc.themes.SPACELAB, hljs],
    suppress_callback_exceptions=True,
)

topbar = html.H2("Dash Labs Docs & Demo", className="p-4 bg-primary text-white sticky-top")

sidebar = dbc.Card(
    [
        dbc.NavLink(
            [
                html.Div("home", className="ms-2"),
            ],
            href=dash.page_registry["pages.home"]["path"],
            active="exact",
        ),
        html.H6("Multi-Page Apps", className="mt-2"),
        dbc.Nav(
            [
                dbc.NavLink(
                    [
                        html.Div(page["name"], className="ms-2"),
                    ],
                    href=page["path"],
                    active="exact",
                )
                for page in dash.page_registry.values()
                if page["path"].startswith("/multi-page")
            ],
            vertical=True,
        ),
        html.H6("Dashdown", className="mt-2"),
        dbc.Nav(
            [
                dbc.NavLink(
                    [
                        html.Div(page["name"], className="ms-2"),
                    ],
                    href=page["path"],
                    active="exact",
                )
                for page in dash.page_registry.values()
                if page["path"].startswith("/dashdown")
            ],
            vertical=True,
        ),
    ],
    className="overflow-auto",
    style=SIDEBAR_STYLE,
)

app.layout = html.Div(
    [topbar, sidebar, html.Div(dl.plugins.page_container, style=CONTENT_STYLE)]
)



if __name__ == "__main__":
    app.run_server(debug=True)
