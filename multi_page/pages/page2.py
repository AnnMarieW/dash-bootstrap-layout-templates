from dash import dcc
import plotly.express as px
import dash_bootstrap_components as dbc
import layout_templates.layout as tpl

df = px.data.tips()
fig = px.scatter(df, x="total_bill", y="tip", opacity=0.65, trendline="ols")

controls = tpl.card(
    [(dcc.Dropdown(), "My dropdown"), (dcc.Slider(), "My Slider")],
    header="My control panel"
)


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
        [dbc.Col(controls, width=4), dbc.Col(tpl.card([dcc.Graph(figure=fig)]), width=8)],
    ], title=None
)
