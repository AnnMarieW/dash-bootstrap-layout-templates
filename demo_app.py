from importlib import import_module
from inspect import getsource
import os

from dash import Dash, dcc, html, Input, Output, State, no_update
import dash_bootstrap_components as dbc


def preprocess(source):
    # source = source.replace(
    #     '\nif __name__ == "__main__":\n    app.run_server(debug=True)',
    #     "app.run_server(debug=True)",
    # )
    # source = source.replace("\n\n\n", "\n\n")
    return source


def prepend_recursive(component, prefix: str) -> None:
    """in-place modifications"""
    if hasattr(component, "id"):
        component.id = prefix + component.id

    if hasattr(component, "children") and component.children is not None:
        for child in component.children:
            prepend_recursive(child, prefix)


app = Dash(
    __name__,
    suppress_callback_exceptions=True,
    assets_folder="pages",
    external_stylesheets=[dbc.themes.SPACELAB],
)


pages = sorted([p.replace(".py", "") for p in os.listdir("./pages") if ".py" in p])
modules = {p: import_module(f"pages.{p}") for p in pages}
apps = {p: m.app for p, m in modules.items()}
source_codes = {p: preprocess(getsource(m)) for p, m in modules.items()}


landing_page = [
    dbc.Container(
        [
            dbc.Row(
                dbc.Col(
                    [
                        html.H5(
                            "Dash Bootstrap Layout Templates Demo.  Please select an app:"
                        ),
                        dcc.Dropdown(
                            id="app-choice",
                            placeholder="Please select an app...",
                            options=[{"label": x, "value": x} for x in apps],
                            value=list(apps.keys())[0],
                        ),
                    ],
                    width=12,
                    lg=5,
                ),
                className="mb-4",
            ),
            dbc.Row(dbc.Col(html.Iframe(id="iframe", className=("vw-100 vh-100")),)),
        ],
        fluid=True,
    ),
]

app.layout = html.Div([dcc.Location(id="url", refresh=False), html.Div(id="display"),])

for k in apps:
    # Prepend to layout IDs recursively in-place
    prepend_recursive(apps[k].layout, prefix=k + "-")

    app.callback_map.update(apps[k].callback_map)
    app._callback_list.extend(apps[k]._callback_list)


@app.callback(
    Output("iframe", "src"), [Input("app-choice", "value")], [State("url", "pathname")]
)
def update_iframe(app, pathname):
    if app is None:
        return no_update
    return pathname + app


@app.callback(Output("display", "children"), [Input("url", "pathname")])
def display_content(pathname):
    if "/" in pathname:
        selected = pathname.split("/")[-1]
        if selected in apps:
            return dbc.Container(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                dcc.Markdown(
                                    f"```python\n{source_codes[selected]}\n```"
                                ),
                                width=12,
                                lg=5,
                                className="border",
                            ),
                            dbc.Col(
                                apps[selected].layout,
                                width=12,
                                lg=7,
                                className="border",
                            ),
                        ]
                    )
                ],
                fluid=True,
            )
    return landing_page


if __name__ == "__main__":
    app.run_server(debug=True)
