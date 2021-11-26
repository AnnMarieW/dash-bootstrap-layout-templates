
from dash import Dash, dcc, html, dash_table


import dash_bootstrap_components as dbc


from .util import datatable_make_subheading


about_md = dcc.Markdown("""

### About the "dbc" class

The dbc class is defined in the [dash-bootstrap-templates](https://github.com/AnnMarieW/dash-bootstrap-templates) library.  You can add it to you app like this:
```
dbc_css = ("https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.2/dbc.min.css")
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP, dbc_css])

```

If you would like to modify the css, you can find a more human readable stylesheet here:  "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.2/dbc.css"

This stylesheet is from version V1.0.2. Check the dash-bootstrap-templates library for the latest updates.


Add  `className="dbc"` to the outer container of the app or a component like this:
```
app.layout = dbc.Container(
    [
        ...
    ],
    fluid=True,
    className="dbc"
)
```

That's it!  Now all the Dash Core Components and the DataTable will look better with any of the themes
included in the dash-bootstrap-components library.

Adding `className="dbc"` minimally styles the components with your selected Bootstrap theme:
- Makes the text readable in both light and dark themes.
- Uses the font from the Bootstrap theme's font-family.
- Changes the accent color to he theme's primary color

See more information and community discussion here.  If you improve this sylesheet please share!  Or if you find
and bug, please let us know on the [issue tracker](https://github.com/AnnMarieW/dash-bootstrap-templates/issues)

""",
    className="dbc p-4"
)
