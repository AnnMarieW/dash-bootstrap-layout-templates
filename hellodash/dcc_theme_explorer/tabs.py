
from dash import Dash, dcc, html, dash_table
import plotly.express as px

import dash_bootstrap_components as dbc


from util import dcc_make_subheading




dcc_content= dcc.Markdown(
    """
Note that the dcc.Tabs are easy to customizable with inline styles or css.  
See the Dash documentation [here](https://dash.plotly.com/dash-core-components/tab).
    """
)

dbc_content = dcc.Markdown(
    """    
Rather than using dcc.Tabs, These tabs are from the dash-bootstrap-components library. 
They are automatically styled according to the theme

    """
)


tabs = html.Div([
    dcc.Tabs( value='tab-1', children=[
        dcc.Tab(label='Tab one', value='tab-1', children=html.P(dcc_content, className="p-4")),
        dcc.Tab(label='Tab two', value='tab-2', children=html.P("Tab 2 Content",className="p-4")),
    ]),
])


dcc_tabs = html.Div(
    [dcc_make_subheading("dcc.Tabs", "tabs"), dbc.Row(tabs)],
    className="mb-4",
)


dbc_tabs = html.Div(
    [
        dcc_make_subheading("dbc.Tabs", "tabs"),
        dbc.Tabs(
            [
                dbc.Tab(html.P(dbc_content, className="p-3"), label="Tab 1"),
                dbc.Tab(html.P("This is tab 2", className="p-3"), label="Tab 2"),
            ]
        ),
    ],
    className="mb-4",
)

