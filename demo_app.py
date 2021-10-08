from importlib import import_module
from inspect import getsource
import os

from dash import Dash, dcc, html, Input, Output, State, no_update, callback_context
import dash_bootstrap_components as dbc
import layout_templates.layout as tpl

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
print(apps)
source_codes = {p: preprocess(getsource(m)) for p, m in modules.items()}

app_page = {app: page + 1 for page, app in enumerate(apps)}
page_app = {page + 1: app for page, app in enumerate(apps)}

app_dropdown = dcc.Dropdown(
    id="app-choice",
    placeholder="Please select an app...",
    options=[{"label": x, "value": x} for x in apps],
    value=list(apps.keys())[0],
)

app_pagination = dbc.Pagination(
    id="pages",
    max_value=len(apps),
    fully_expanded=False,
    previous_next=True,
)

card = tpl.card([
    (app_dropdown, "Please select an app"),
    (app_pagination, "Or for a tutorial, step through the apps in sequence"),
], header= "Welcome to the Dash Layout Templates Demo", className='m-4')


landing_page = tpl.layout([
    [dbc.Col(card, width=12, lg=4)],
    html.Iframe(id="iframe", className=("vw-100 vh-100"))
], title=None)

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

@app.callback(
    Output("app-choice","value"),
    Output("pages", "active_page"),
    Input("app-choice","value"),
    Input("pages", "active_page"),
)
def sync(app, page):
    ctx = callback_context
    trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]
    page = app_page[app] if trigger_id == "app-choice" else page
    app = page_app[page] if trigger_id == 'pages' else app
    return app, page




if __name__ == "__main__":
    app.run_server(debug=True)
