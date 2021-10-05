from dash import Dash
import dash_bootstrap_components as dbc

import layout_templates.layout as tpl

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = tpl.layout(
    [
        """
        # Hello Dash Templates!
        *** Make your first app in less than 5 minutes! ***
        """
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
