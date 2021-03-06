#
"""
A collection of layout templates and utilities for AnnMarieW app components
todo- maybe make this two files? 1) user templates, 2) other utilities
"""

from dash import html, dcc, dash_table
import dash_bootstrap_components as dbc


navbar = dbc.NavbarSimple(
    children=[
         dbc.NavItem(dbc.NavLink("Templates", href="templates")),

        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("More pages", header=True),
                dbc.DropdownMenuItem("Templates", href="/templates"),
                dbc.DropdownMenuItem("Theme Switcher", href="/theme_switch"),
                dbc.DropdownMenuItem("GitHub", href="https://github.com/AnnMarieW/dash-bootstrap-layout-templates"),
            ],
            nav=True,
            in_navbar=True,
            label="More",
        ),
    ],
    brand="Dash Layout Templates Demo",
    brand_href="#",
    color="black",
    dark=True,
)




def make_dropdown(option_list, id=id, option_val=0):
    return dcc.Dropdown(
        id=id,
        options=[{"label": str(i), "value": i} for i in option_list],
        value=option_list[option_val],
        clearable=False,
        persistence_type="local",
    )


def make_radio_items(option_list, id=id, option_val=0):
    return dbc.RadioItems(
        id=id,
        options=[{"label": i, "value": i} for i in option_list],
        inline=True,
        value=option_list[option_val],
        persistence_type="local",
        className="mt-2",
    )


def make_checklist(option_list, id=id):
    return dbc.Checklist(
        id=id,
        options=[{"label": i, "value": i} for i in option_list],
        value=option_list[2:],
        inline=True,
        persistence_type="local",
    )


def make_range_slider(slider_list, id=id, step=1):
    return dcc.RangeSlider(
        id=id,
        min=slider_list[0],
        max=slider_list[-1],
        step=step,
        # marks={int(i): str(i) for i in slider_list},
        # marks={
        #     int(i): {"label": str(i), "style": {"transform": "rotate(90deg)"}}
        #     for i in slider_list
        # },
        tooltip={"placement": "bottom", "always_visible": True},
        value=[slider_list[2], slider_list[-2]],
        persistence_type="local",
    )


def make_datatable(dff, id=id):
    return dash_table.DataTable(
        id=id,
        columns=[{"name": i, "id": i, "deletable": True} for i in dff.columns],
        data=dff.to_dict("records"),
        page_size=10,
        editable=True,
        cell_selectable=True,
        filter_action="native",
        sort_action="native",
        style_table={"overflowX": "auto"},
        # style_data_conditional=[
        #     {
        #         "if": {"state": "active"},
        #         "border": "1px solid var(--bs-primary)",
        #         "opacity": 0.75,
        #     },
        #     {"if": {"state": "selected"}, "border": "1px solid", "opacity": 0.75,},
        #     {
        #         'if': {
        #             'column_id': 'pop',
        #         },
        #         'backgroundColor': 'dodgerblue',
        #         'color': 'yellow',
        #         'fontWeight': 1000,
        #     },
        #
        # ],
    )



light_themes = [
    "BOOTSTRAP",
    "CERULEAN",
    "COSMO",
    "FLATLY",
    "JOURNAL",
    "LITERA",
    "LUMEN",
    "LUX",
    "MATERIA",
    "MINTY",
    "PULSE",
    "SANDSTONE",
    "SIMPLEX",
    "SKETCHY",
    "SPACELAB",
    "UNITED",
    "YETI",
]
dark_themes = [
    "CYBORG",
    "DARKLY",
    "SLATE",
    "SOLAR",
    "SUPERHERO",
]

# the template themes are lower case to be consistent with the plotly naming convention
dbc_lower_case = [t.lower() for t in light_themes + dark_themes]
from dash_bootstrap_templates import load_figure_template
load_figure_template(dbc_lower_case)


dbc_themes_url = {
    item: getattr(dbc.themes, item)
    for item in dir(dbc.themes)
    if not item.startswith(("_", "GRID", "VAPOR", "QUARTZ", "MORPH", "ZEPHYR"))
    # todo - when new templates are available in dash-bootstrap-templates, change
    #  line above to:
    # if not item.startswith(("_", "GRID"))
}
url_dbc_themes = dict(map(reversed, dbc_themes_url.items()))
