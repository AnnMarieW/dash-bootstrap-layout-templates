from dash import Dash, dcc
import dash_bootstrap_components as dbc
import layout_templates.layout as tpl

app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB])

controls = tpl.Form([("My dropdown", dcc.Dropdown()), ("My Slider", dcc.Slider())],header=" #### My Controls")
card2 = tpl.Card(["__This card has a header__"],header= "# Card Header", width=4)
card3 = tpl.Card(["__This card has a header and footer__"], header="Card Header", footer="Card Footer", width=4)

app.layout = tpl.Layout(
    [
        " *** Card may have an optional header and footer *** ",
        [controls, card2, card3]
    ],
)

if __name__ == "__main__":
    app.run_server(debug=True)
