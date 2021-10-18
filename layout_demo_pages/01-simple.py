from dash import Dash
import dash_bootstrap_components as dbc

import layout_templates.layout as tpl

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = tpl.Layout(
    [
        """
        # Hello Dash Templates!
        *** Make your first app in less than 2 minutes! ***  
        
        You can use Markdown with any text string
        """
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
