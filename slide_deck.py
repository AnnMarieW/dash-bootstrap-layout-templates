from dash import Dash, html
import dash_bootstrap_components as dbc
from aio.aio_components import SlideDeckAIO

app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB])

slide_deck = {i: html.Div(f"slide {i}") for i in range(9)}

app.layout = SlideDeckAIO(
    slide_deck=slide_deck,
    title="My presentation"
)

if __name__ == "__main__":
    app.run_server(debug=True)






