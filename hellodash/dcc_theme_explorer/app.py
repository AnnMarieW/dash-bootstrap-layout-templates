import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, State

from alert import alerts

dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.css"
app = dash.Dash(
    external_stylesheets=[dbc.themes.CYBORG, dbc.icons.BOOTSTRAP, dbc_css]
)

app.layout = dbc.Container(
    [
        alerts,

        dbc.Row(
            [
                dbc.Col([form, input_group], xs=12, md=6),
                dbc.Col([input_], xs=12, md=6),
            ]
        ),
        dbc.Row(
            [
                dbc.Col([checklist_items], xs=12, md=6),
                dbc.Col([radio_items], xs=12, md=6),
            ]
        ),

    ],
    fluid=True,
    className="px-4 dbc",
)

if __name__ == "__main__":
    app.run_server(debug=True)




from dash import Dash, dcc, html, dash_table, Input, Output, State
import plotly.express as px
import dash_bootstrap_components as dbc

import layout_templates.layout as tpl
from aio import ThemeChangerAIO, url_dbc_themes
import layout_templates.util as util

from collections import OrderedDict
import pandas as pd

df = px.data.gapminder()
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.themes.CYBORG])

table = dash_table.DataTable(
    id="table",
    columns=[{"name": i, "id": i, "deletable": True} for i in df.columns],
    data=df.to_dict("records"),
    page_size=10,
    editable=True,
    cell_selectable=True,
    filter_action="native",
    sort_action="native",
    style_table={"overflowX": "auto"},
    #style_header={"backgroundColor": "yellow"},
    style_data_conditional=[
        {
            'if': {
                'state': 'active'  # 'active' | 'selected'
            },
            'backgroundColor': 'rgba(var(--bs-primary-rgb), 0.2)',
            'border': '1px solid rgb(0, 116, 217)'
        }

    ],
)

# ---- DCC Sampler -----------------------------------------------

input = html.Div([
    dcc.Input(
        placeholder='This is a dash dcc input...',
        type='text',
        value='',
        className='mt-4 mb-2'
    ),
    dcc.Input(
        placeholder='This is a dash dcc input with className="form-control" ...',
        type='text',
        value='',
        className='form-control'
    ),
    dbc.Input(
        placeholder='This is a dbc input...',
        type='text',
        value='',
        className='my-2'
    )
])
textarea = html.Div([
    dcc.Textarea(
        placeholder='Enter a value...',
        value='This is a TextArea component',
        style={'width': '100%'}
    )
])
checkboxes = html.Div([
    dcc.Checklist(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value=['MTL', 'SF']
    )
])
dcc_checklist = dcc.Checklist(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value=['MTL', 'SF'],
        labelStyle={'display': 'inline-block'}

)
radioitems = html.Div([
    dcc.RadioItems(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='MTL'
    )
])
from datetime import date
datepicker_single = html.Div([
    dcc.DatePickerSingle(
        id='date-picker-single',
        date=date(1997, 5, 10)
    )
])
datepicker_range =html.Div([
    dcc.DatePickerRange(
        id='date-picker-range',
        start_date=date(1997, 5, 3),
        end_date_placeholder_text='Select a date!'
    )
])
dcc_tabs = html.Div([
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='Tab one', value='tab-1', children="Tab 1 content"),
        dcc.Tab(label='Tab two', value='tab-2', children="Tab 2 Content"),
    ]),
    html.Div(id='tabs-content')
])
theme_colors = tpl.Card([html.Div(
    [
        dbc.Button("Primary", color="primary"),
        dbc.Button("Secondary", color="secondary"),
        dbc.Button("Success", color="success"),
        dbc.Button("Warning", color="warning"),
        dbc.Button("Danger", color="danger"),
        dbc.Button("Info", color="info"),
        dbc.Button("Light", color="light"),
        dbc.Button("Dark", color="dark"),
        dbc.Button("Link", color="link"),
    ]
)], header="Bootstrap Color Sample")

dcc_sampler = [
    "## This is a Sample of Dash Core Components",
    theme_colors,
    tpl.Card(
        [
            datepicker_single,
            datepicker_range,
            dcc_dropdown, multi_dropdown,
            dcc_slider, range_slider,
            input, textarea,
            dcc_tabs
        ]
    )
]


# ----- End Dcc Sampler-----------------------------------------------------------





