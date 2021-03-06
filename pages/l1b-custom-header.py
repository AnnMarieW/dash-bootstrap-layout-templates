from dash import Dash, html
import dash_bootstrap_components as dbc

import layout_templates.layout as tpl

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Page 1", href="#")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("More pages", header=True),
                dbc.DropdownMenuItem("Page 2", href="#"),
                dbc.DropdownMenuItem("Page 3", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="More",
        ),
    ],
    brand="My Custom Header",
    brand_href="#",
    color="black",
    dark=True,
)

app.layout = tpl.layout(
    [
        navbar,

        """
        # Hello Dash Templates!        
        *** This app has a custom header.***
        """,
    ],
    title=None,
)

if __name__ == "__main__":
    app.run_server(debug=True)
