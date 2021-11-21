
from dash import Dash, dcc, html, dash_table
import plotly.express as px

import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeChangerAIO

from datepickers import dcc_date_picker_range, dcc_date_picker_single
from dropdowns import dcc_dropdowns
from input import input, checklist, radioitems
from table import table
from tabs import tabs
from theme_colors import theme_colors


#dbc_css = ("https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.2/dbc.min.css")
dbc_css = ("https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css")
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP,
                                          dbc_css
                                           ])


def make_card(title,content):
    return dbc.Card(
        [
            dbc.CardHeader(title, className="card-title h1"),
            dbc.CardBody(content)
        ]
    )

content = html.Div(
    [
        table,dcc_date_picker_single, dcc_date_picker_range, dcc_dropdowns

    ]
)

app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(ThemeChangerAIO(), width=2),
                dbc.Col(theme_colors)
            ]
        ),
        dbc.Row([
            dbc.Col([
                make_card('Styled with ClassName="dbc"', content)


            ], width={"size":5, "offset":2}, className="dbc"),
            dbc.Col([
                make_card('Default style', content)

            ],width=5)
        ], )
    ],fluid=True
)

if __name__ == "__main__":
    app.run_server(debug=True)
