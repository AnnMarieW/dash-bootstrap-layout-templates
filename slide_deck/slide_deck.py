import dash_bootstrap_components as dbc
from app import app
from apps import page1, page2, page3
from aio.aio_components import SlideDeckAIO

slide_deck = {1 : page1.layout, 2 :page2.layout, 3: page3.layout }

app.layout = dbc.Container(SlideDeckAIO(slide_deck=slide_deck, title="My Presentation"), fluid=True)


if __name__ == '__main__':
    app.run_server(debug=True)