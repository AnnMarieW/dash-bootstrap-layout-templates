import dash
import dash_bootstrap_components as dbc
from dash import html, Input, Output, State
from dash_bootstrap_templates import ThemeChangerAIO

import dcc_theme_explorer as dcc_te
import dbc_theme_explorer as dbc_te
from theme_explorer_multipage import layout as sample_app_layout


#dbc_css = ("https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.2/dbc.min.css")
#dbc_css = ("https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css")
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.css"
app = dash.Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP, dbc_css]
)


def make_dcc_gallery():
    content = html.Div(
        [
            dcc_te.intro,
            dcc_te.datatable,
            dcc_te.dcc_date_picker_single, dcc_te.dcc_date_picker_range, dcc_te.dcc_dropdowns,
            dcc_te.dcc_markdown,
            dcc_te.dcc_slider, dcc_te.dcc_range_slider, dcc_te.dcc_tabs,
            dcc_te.about_md

        ]
    )
    return dbc.Row([
        dbc.Col(
            dbc.Card(
                [
                    dbc.CardHeader('Dash Core Components and DataTable Styled with ClassName="dbc"',
                                   className="card-title h2"),
                    dbc.CardBody(content)
                ],
                outline=True, color="primary"
            ),
             className="dbc"),

    ])


def make_dcc_card():
    """ This makes a comparison between with className=dbc and default"""
    content = html.Div(
        [
            dcc_te.table, dcc_te.dcc_date_picker_single, dcc_te.dcc_date_picker_range, dcc_te.dcc_dropdowns,
            dcc_te.dcc_slider, dcc_te.dcc_range_slider, dcc_te.dcc_tabs

        ]
    )
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


heading = html.H2("Component Gallery", className="text-white bg-primary p-2 mt-4")

dbc_gallery = html.Div(
    [
        dbc_te.alerts,
        dbc_te.badges,
        dbc_te.buttons,
        dbc_te.cards,
        dbc_te.collapse,
        dbc_te.fade,
        dbc.Row(
            [
                dbc.Col([dbc_te.form, dbc_te.input_group], xs=12, md=6),
                dbc.Col([dbc_te.input_], xs=12, md=6),
            ]
        ),
        dbc.Row(
            [
                dbc.Col([dbc_te.checklist_items], xs=12, md=6),
                dbc.Col([dbc_te.radio_items], xs=12, md=6),
            ]
        ),
        dbc_te.list_group,
        dbc_te.modal,
        dbc_te.navbar,
        dbc_te.popover,
        dbc_te.progress,
        dbc_te.spinner,
        dbc_te.table,
        dbc_te.tabs,
        dbc_te.toast,
        dbc_te.tooltip,

    ]
)

app.layout = dbc.Container(
    [

        dbc.Row(
            [
                dbc.Col(ThemeChangerAIO(aio_id="theme"), width=2),
                dbc.Col([sample_app_layout, heading, dbc_gallery, make_dcc_gallery()], width=10)
            ], className="mt-4"
        ),

    ],
    fluid=True,

)


@app.callback(
    Output("collapse", "is_open"),
    [Input("collapse-button", "n_clicks")],
    [State("collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


@app.callback(
    Output("fade", "is_in"),
    [Input("fade-button", "n_clicks")],
    [State("fade", "is_in")],
)
def toggle_fade(n, is_in):
    if n:
        return not is_in
    return is_in


@app.callback(
    Output("popover", "is_open"),
    [Input("popover-target", "n_clicks")],
    [State("popover", "is_open")],
)
def toggle_popover(n, is_open):
    if n:
        return not is_open
    return is_open


@app.callback(
    Output("modal", "is_open"),
    [Input("button", "n_clicks")],
    [State("modal", "is_open")],
)
def toggle_modal(n, is_open):
    if n:
        return not is_open
    return is_open


@app.callback(
    Output("auto-toast", "is_open"), [Input("auto-toast-toggle", "n_clicks")]
)
def open_toast(_):
    return True


if __name__ == "__main__":
    app.run_server(debug=True)
