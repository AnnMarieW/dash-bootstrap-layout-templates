
from dash import Dash, dcc, html, dash_table
import plotly.express as px

import dash_bootstrap_components as dbc


from util import make_subheading


df = px.data.tips()

table = dash_table.DataTable(
    columns=[{"name": i, "id": i, "deletable": True} for i in df.columns],
    data=df.to_dict("records"),
    page_size=5,
    editable=True,
    cell_selectable=True,
    filter_action="native",
    sort_action="native",
    style_table={"overflowX": "auto"},
)


DataTable = html.Div(
    [make_subheading("DataTable", "datatable"), dbc.Row(table)],
    className="mb-4",
)
