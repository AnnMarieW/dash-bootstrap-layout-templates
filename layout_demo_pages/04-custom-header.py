from dash import Dash, html
import dash_bootstrap_components as dbc

import layout_templates.layout as tpl

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Page 1", href="#")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("More layout_demo_pages", header=True),
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

app.layout = tpl.Layout(
    [
        navbar,

        """
        # Hello Dash Templates!        
        *** This app has a custom header.***  
        
        Make this the default header by adding it to the config file.
        """,
    ],
    title=None,
)

if __name__ == "__main__":
    app.run_server(debug=True)
