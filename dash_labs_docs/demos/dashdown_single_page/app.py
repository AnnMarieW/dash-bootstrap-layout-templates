from dash import Dash, html
import dash_bootstrap_components as dbc
from dash_labs import dashdown

# hljs = "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.3.1/styles/github-dark-dimmed.min.css"
hljs = "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.4.0/styles/base16/equilibrium-gray-light.min.css"

app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB, hljs])

app.layout = dbc.Container(
    [
        html.H2(["dashdown demo"], className="p-2 mb-4 bg-primary text-white"),
        dbc.Row(
            dashdown(
                # "notebook.md",
                "/home/amward/PycharmProjects/dash-labs/docs/demos/dashdown_multi_page/pages/dashdown/README.md",
                #  "https://github.com/thedirtyfew/dash-extensions/blob/master/README.md",
                scope={"app": app},
                # side_by_side=False,
                # exec_code=False
                scope_creep=True,
            ),
            className="mb-4",
        ),
    ],
    fluid=True,
)

# app.layout = html.Div(dashdown("https://raw.githubusercontent.com/thedirtyfew/dash-extensions/master/README.md", scope={"app": app}, ))


if __name__ == "__main__":
    app.run_server(debug=True)
