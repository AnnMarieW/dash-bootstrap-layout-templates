
from dash import Dash, dcc, html, dash_table, Input, Output, State
import plotly.express as px
import dash_bootstrap_components as dbc

import layout_templates.layout as tpl
from aio.aio_components import ThemeChangerAIO, dbc_dark_themes, url_dbc_themes
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
dcc_dropdown = html.Div([
    dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='MTL'
    )
])
multi_dropdown = html.Div([
    dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        multi=True,
        value="MTL"
    )
])
dcc_slider = html.Div([
    dcc.Slider(
        min=0,
        max=9,
        marks={i: 'Label {}'.format(i) for i in range(10)},
        value=5,
    )
])
range_slider  = html.Div([
    dcc.RangeSlider(
        marks={i: 'Label {}'.format(i) for i in range(-5, 7)},
        min=-5,
        max=6,
        value=[-3, 4]
    )
])
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
        dcc.Tab(label='Tab one', value='tab-1'),
        dcc.Tab(label='Tab two', value='tab-2'),
    ]),
    html.Div(id='tabs-content')
])
theme_sample = tpl.Card([html.Div(
    [
        dbc.Button("Primary", color="primary", className="mr-1"),
        dbc.Button("Secondary", color="secondary", className="mr-1"),
        dbc.Button("Success", color="success", className="mr-1"),
        dbc.Button("Warning", color="warning", className="mr-1"),
        dbc.Button("Danger", color="danger", className="mr-1"),
        dbc.Button("Info", color="info", className="mr-1"),
        dbc.Button("Light", color="light", className="mr-1"),
        dbc.Button("Dark", color="dark", className="mr-1"),
        dbc.Button("Link", color="link"),
    ]
)], header="Bootstrap Color Sample")

dcc_sampler = [
    "## This is a Sample of Dash Core Components",
    theme_sample,
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




# todo - change this to Dash shorthand sytnax in Dash 2.1
slider = util.make_range_slider(df.year.unique(), id="years")
checklist = util.make_checklist(df.continent.unique(), id="continents")
dropdown = util.make_dropdown(["gdpPercap", "lifeExp", "pop"], id="indicator")
#table = util.make_datatable(df, id="table")

controls = html.Div(
    [
        tpl.Card(
            [
                (dropdown, "Select indicator (y-axis)"),
                (checklist, "Select Continents"),
                (slider, "Select Years"),
            ],
        ),
        ThemeChangerAIO(aio_id="theme"),
    ]
)

tabs = dbc.Tabs(
    [
        tpl.Tab([dcc.Graph(id="line-chart")], label="Graph"),
        tpl.Tab([table], label="Table"),
        tpl.Tab(dcc_sampler, label="dcc components", className="dbc")
    ]
)

app.layout = tpl.Layout([
    [dbc.Col(controls, width=4), dbc.Col(tabs, width=8)]
], className="dbc")


@app.callback(
    Output("line-chart", "figure"),
    Output("table", "data"),
    Input("indicator", "value"),
    Input("continents", "value"),
    Input("years", "value"),
    Input(ThemeChangerAIO.ids.radio("theme"), "value"),
)
def update_line_chart(indicator, continents, years, theme):
    if continents == [] or indicator is None:
        return {}, []

    template = url_dbc_themes[theme].lower()

    dff = df[df.year.between(years[0], years[1])]
    dff = dff[dff.continent.isin(continents)]
    data = dff.to_dict("records")

    fig = px.line(dff, x="year", y=indicator, color="continent", line_group="country", template=template)
    fig.update_layout(margin=dict(l=75, r=20, t=10, b=20))

    return fig, data


if __name__ == "__main__":
    app.run_server(debug=True)




