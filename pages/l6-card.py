from dash import Dash, dcc
import plotly.express as px
import dash_bootstrap_components as dbc
import layout_templates.layout as tpl

app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB])

controls = tpl.card([(dcc.Dropdown(), "My dropdown"), (dcc.Slider(), "My Slider")])

app.layout = tpl.layout(
    [
        """
        # Hello Dash Templates!
        *** Make a control panel with labeled components using the `tpl.card` template ***
        """,
        controls,
    ],
)

if __name__ == "__main__":
    app.run_server(debug=True)
