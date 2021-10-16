
from dash import  html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import layout_templates.layout as tpl

df = px.data.tips()

checklist = dbc.Checklist(
    id="slide-checklist",
    options=[{"label": d, "value": d} for d in ["Thur", "Fri", "Sat", "Sun"]],
    value=["Sun"],
)
checklist_card = tpl.card([(checklist, "Select day:")])

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Page 1", href='/pages/page1')),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("More pages", header=True),
                dbc.DropdownMenuItem("Page 2", href='/pages/page2'),
                dbc.DropdownMenuItem("Page 3", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="More",
        ),
    ],
    brand="NavbarSimple",
    brand_href="#",
    color="primary",
    dark=True,
)


# def layout():
#     return tpl.layout(
layout = tpl.layout(
    [
        navbar,
        [
            dbc.Col(checklist_card, width=3),
            dbc.Col(dcc.Graph(id="slide-graph"), width=9),
        ],
    ],
    title=None,
)


@callback(Output("slide-graph", "figure"), Input("slide-checklist", "value"))
def update_slide(days):
    dff = df[df.day.isin(days)]
    return px.histogram(dff, x="total_bill", y="tip", color="sex", marginal="rug")

