
from dash import Dash, dcc, html, dash_table


import dash_bootstrap_components as dbc


from .util import datatable_make_subheading


about_md = dcc.Markdown("""

### About the "dbc" class

Add the dbc external stylesheet to your app like this:
```
dbc_css = ("https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.2/dbc.min.css")
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP, dbc_css])

```

If you would like to modify the css or add a local copy to your assets folder, you can find a more
human readable stylesheet here:  "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.2/dbc.css"

Check the dash-bootstrap-templates library for the latest updates!


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

See more infomation and comminity discussion here.  If you improve this sylesheet please share!  Or if you find
and bug, please open an issue at 

""",
    className="dbc p-4"
)
