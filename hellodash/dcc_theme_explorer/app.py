
from dash import Dash, dcc, html


import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeChangerAIO

from datepickers import dcc_date_picker_range, dcc_date_picker_single
from dropdowns import dcc_dropdowns
from input import input, checklist, radioitems
from table import table
from tabs import dcc_tabs, dbc_tabs
from sliders import dcc_slider, dcc_range_slider
from theme_colors import theme_colors
from intro import intro


#dbc_css = ("https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.2/dbc.min.css")
#dbc_css = ("https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css")
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP,
             #                             dbc_css
                                           ])


def make_card(content):
    return dbc.Row([
        dbc.Col(
            dbc.Card(
                [
                    dbc.CardHeader('Styled with ClassName="dbc"',
                                   className="card-title h3 overflow-auto text-nowrap"),
                    dbc.CardBody(content)
                ],
                outline=True, color="primary"
            ),
            width={"size":5, "offset":2}, className="dbc"),
        dbc.Col(
            dbc.Card(
                [
                    dbc.CardHeader('Default style',
                                   className="card-title h3 overflow-auto text-nowrap"),
                    dbc.CardBody(content)
                ]
            ),
            width=5
        )
    ])


content = html.Div(
    [
        table,dcc_date_picker_single, dcc_date_picker_range, dcc_dropdowns,
        dcc_slider, dcc_range_slider, dcc_tabs, dbc_tabs


    ]
)

app.layout = dbc.Container(
    [
        dbc.Row(dbc.Col(intro, width={"offset":2})),
        dbc.Row(
            [
                dbc.Col(ThemeChangerAIO(), width=2),
                dbc.Col([html.Span("Sample theme colors: "), theme_colors], width=5)
            ], className="mt-4"
        ),
        dbc.Row([
            make_card(content),
            #make_card(html.Div([dcc_date_picker_single, dcc_date_picker_range]))
        ], )
    ],fluid=True
)

if __name__ == "__main__":
    app.run_server(debug=True)
