
from dash import Dash, dcc, html, dash_table
import plotly.express as px

import dash_bootstrap_components as dbc


from util import make_subheading


content= dcc.Markdown(
    """
This is the default style when using the dbc class.  However, the dcc.Tabs are
very customizable with inline styles or css.  See the Dash documentation [here](https://dash.plotly.com/dash-core-components/tab)

If you customize according the the examples in the Dash documentation, you can make them work with
any theme by using the Bootstrap variable names instead of a hard coded color.  For example, instead of:

```
tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#119DFF',
    'color': 'white',
    'padding': '6px'
}
```
You could do something like this:

```
tab_selected_style = {
    'borderTop': '1px solid var(--bs-primary)',
    'borderBottom': '1px solid var(--bs-primary)',
    'backgroundColor': 'var(--bs-body-bg)',
    'color': 'var(--bs-body-color)',
    'padding': '6px'
}
```
    """
)


tabs = html.Div([
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='Tab one', value='tab-1', children=content),
        dcc.Tab(label='Tab two', value='tab-2', children="Tab 2 Content"),
    ]),
    html.Div(id='tabs-content')
])


dcc_tabs = html.Div(
    [make_subheading("Tabs", "tabs"), dbc.Row(tabs)],
    className="mb-4",
)
