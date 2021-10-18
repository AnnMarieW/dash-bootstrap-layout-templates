"""
Configure the slide_deck app:
  1) Put your logo in the assets folder (optional)
  2) Customize the `make_slide_deck_nav()` to change the format of header (optional)

To create a new presentation:
 1) Put content in pages folder
 2) Update the three lines in the "Change presentation section
    - Import the pages to include in the presentation
    - Update the `slide_deck` dict  {page_number, page_content}
    - Update the `title`
"""


from dash import Dash, dcc, html, Output, Input
import dash_bootstrap_components as dbc
import os

# Change  presentation ----_----
from pages import agenda, histogram, bar_graph
slide_deck = {1: agenda.layout, 2: histogram.layout, 3: bar_graph.layout}
title = "My Presentation"
# -------------------------------


def get_logo():
    """ get the logo from /assets,  if there is one"""
    assets = os.listdir(os.getcwd()+'/assets/')
    split_assets = [x.split('.')[0] for x in assets]
    for i,x in enumerate(split_assets):
        if x=='logo':
            return html.Img(src='assets/'+assets[i],style=dict(height='40px'))
    return None


def make_slide_deck_nav():
    # make layout of the slide deck hav
    presentation_title = " " if title is None else title
    logo = get_logo()
    pagination_btns = dbc.Pagination(
                id="pagination",
                max_value=len(slide_deck),
                fully_expanded=False,
                previous_next=True,
               # size="sm",
                active_page=1,
            )
    slide_deck_nav = dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(get_logo(), className='me-auto'),
                    dbc.Col(presentation_title, className="text-white ms-2 h3"),
                    dbc.Col(
                        pagination_btns, width="auto", className="float-end pt-2"
                    ),
                ],
                align="center",
            )
        ],
        className="bg-primary text-white mb-4",
        fluid=True,
    )
    return slide_deck_nav


app = Dash(__name__,
           suppress_callback_exceptions=True,
           external_stylesheets=[dbc.themes.SPACELAB]
           )

app.layout = dbc.Container([
    dcc.Location(id='url', refresh=False),
    make_slide_deck_nav(),
    html.Div(id='page-content')
], fluid=True)

@app.callback(
    Output("page-content", "children"),
    Input("pagination", "active_page"),
)
def show_page(active_page):
    return slide_deck[active_page]


if __name__ == '__main__':
    app.run_server(debug=True)