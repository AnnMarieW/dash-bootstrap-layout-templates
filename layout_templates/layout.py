#
from dash import html, dcc
import dash_bootstrap_components as dbc


def make_markdown(content):
    """ Wrap text in dcc.Markdown() """
    return [dcc.Markdown(c) if isinstance(c, str) else c for c in content]


def make_header(title):
    """ Default header bar """
    header = html.H4(title, className="bg-primary bg-gradient rounded text-white p-3")
    return header if title else None


def labeled(component, label):
    return html.Div([dbc.Label(dcc.Markdown(label)), component,], className="mb-2")


def make_labeled_components(content):
    row = []
    for c in content:
        label_text = None
        # handle label  if given
        if len(c) == 2:
            c, label_text = c

        # wrap string in markdown
        if isinstance(c, str):
            c = dcc.Markdown(c)
        row.append(html.Div([dbc.Label(label_text), c], className="mb-4"))
    return row


def card(content, title=None, footer=None):
    header = dbc.CardHeader(title) if title else None
    content = make_labeled_components(content)
    footer = dbc.CardFooter(footer) if footer else None
    return dbc.Card([header, dbc.CardBody(content), footer])


def _make_multi_column(content):
    """
    Creates the columns for a multi column row.
    Input: list:  [(children, width)]
           children: either string or a component.
           width: number of columns (optional)
    returns a list: [dbc.Col(children, width=width)]
    """
    multi_col = []
    for c in content:
        width = None
        # handle width if given
        if len(c) == 2:
            c, width = c

        # wrap string in markdown
        if isinstance(c, str):
            c = dbc.Col(dcc.Markdown(c), width=width)
        else:
            c = dbc.Col(c, width=width)
        multi_col.append(c)
    return multi_col


def make_rows(content):
    """ makes a single or multi column dbc.Row from a list of components"""
    content = make_markdown(content)
    row = []
    for c in content:
        if isinstance(c, list):
            row.append(dbc.Row(_make_multi_column(c), className="mb-2"))
        elif isinstance(c, dbc.Row):
            row.append(c)
        else:
            row.append(dbc.Row(dbc.Col(c), className="mb-2"))
    return row


def layout(content, title="My Cool Dash App", className=None, id=""):
    return dbc.Container(
        [make_header(title)] + make_rows(content), fluid=True, className=className, id=id
    )


def tab(content, label=None, tab_id="", className=""):
    return dbc.Tab(
        dbc.Card(make_rows(content), body=True, className="mt-3 " + className),
        label=label,
        tab_id=tab_id
    )

