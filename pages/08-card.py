from dash import Dash, dcc
import plotly.express as px
import dash_bootstrap_components as dbc
import layout_templates.layout as tpl

app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB])

controls = tpl.card([(dcc.Dropdown(), "My dropdown"), (dcc.Slider(), "My Slider")])
card2 = tpl.card(["__This card has a header__"],header= " # Card Header")
card3 = tpl.card(["__This card has a header and footer__"], header=" # Card Header", footer="Card Footer")

app.layout = tpl.layout(
    [
        """
        # Hello Dash Templates!
        *** Card may have an optional header and footer ***
        """,
        [dbc.Col(controls,width=4), dbc.Col(card2, width=4), dbc.Col(card3, width=4)]
    ],
)

if __name__ == "__main__":
    app.run_server(debug=True)
