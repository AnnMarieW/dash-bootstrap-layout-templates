import dash
import dash_bootstrap_components as dbc
from dash import html, Input, Output, State
from dash_bootstrap_templates import ThemeChangerAIO

import dcc_theme_explorer as dcc_te



#dbc_css = ("https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.2/dbc.min.css")
#dbc_css = ("https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css")
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.css"
app = dash.Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP, dbc_css]
)


def make_dcc_card(content):
    """ This makes a comparison between with className=dbc and default"""
    # content = html.Div(
    #     [
    #         dcc_te.table,
    #         # dcc_te.dcc_date_picker_single, dcc_te.dcc_date_picker_range, dcc_te.dcc_dropdowns,
    #         # dcc_te.dcc_slider, dcc_te.dcc_range_slider, dcc_te.dcc_tabs
    #
    #     ]
    # )
    return dbc.Row([
        dbc.Col(
            dbc.Card(
                [
                    dbc.CardHeader(' Styled with ClassName="dbc"',
                                   className="card-title h3 overflow-auto text-nowrap"),
                    dbc.CardBody(content)
                ],
                outline=True, color="primary"
            ),
            className="dbc"),
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


heading = html.H1("Styling the DataTable", className="text-white bg-primary p-4")

app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(ThemeChangerAIO(), width=2),
                dbc.Col([heading, make_dcc_card(dcc_te.datatable), dcc_te.datatable_md, dcc_te.about_md], width=10)
            ], className="mt-4"
        ),
    ],
    fluid=True,


)

if __name__ == "__main__":
    app.run_server(debug=True)
