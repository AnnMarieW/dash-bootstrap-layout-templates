

import dash_bootstrap_components.themes as themes
from dash import Dash, dcc, html, Input, Output
from pages import page1, page2



app = Dash(__name__,
                suppress_callback_exceptions=True,
                external_stylesheets=[themes.BOOTSTRAP]
                )

server = app.server

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/pages/page1':
        return page1.layout
    elif pathname == '/pages/page2':
        return page2.layout
    elif pathname == '/':
        return page1.layout
    else:
        "404"

if __name__ == '__main__':
    app.run_server(debug=True)
