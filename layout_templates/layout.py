#
from dash import html, dcc
import dash_bootstrap_components as dbc


def make_markdown(content):
    """ Wrap text in dcc.Markdown() """
    if isinstance(content, list):
        return [dcc.Markdown(c, className="mb-0") if isinstance(c, str) else c for c in content]
    else:
        return dcc.Markdown(content, className="mb-0") if isinstance(content, str) else content


def make_header(title):
    """ Default header bar """
    header = html.H4(title, className="bg-primary text-white p-3")
    return header if title else None

def labeled(component, label):
    return html.Div([dbc.Label(dcc.Markdown(label, className="mb-0")), component,], className="mb-2")


def make_labeled_components(content):
    """ cards may have an optional header and footer"""
    """ to-do: Allow columns.  This currently puts everything in rows (no columns, no lists)"""
    row = []
    for c in content:

        label = " "
        # handle label  if given
        if len(c) == 2:
            c, label = c
            if isinstance(label, str):
                label = dcc.Markdown(label, className="mb-0")

        # wrap string in markdown if component is a string
        if isinstance(c, str):
            c = dcc.Markdown(c, className="mb-0")
        row.append(html.Div([label, c], className="mb-4"))
    return row


def card(content, header=None, footer=None, className=None):
    header = dbc.CardHeader(header) if header else None
    content = make_labeled_components(content) if content else None
    footer = dbc.CardFooter(footer) if footer else None
    return dbc.Card([header, dbc.CardBody(content), footer], className=className)


def make_rows(content):
    """ makes a single or multi column dbc.Row from a list of components"""
    # to-do check if content of the col is a string and wrap with markdown?
    content = make_markdown(content)
    row = []
    for c in content:
        if isinstance(c, (dbc.Col, list)):
            row.append(dbc.Row(make_markdown(c), className="mb-2"))
        elif isinstance(c, dbc.Row):
            row.append(c)
        else:
            row.append(dbc.Row(dbc.Col(c), className="mb-2"))
    return row


def layout(content, title="Layout Templates Demo", className=None, id=""):
    return dbc.Container(
        [make_header(title)] + make_rows(content),
        fluid=True,
        className=className,
        id=id,
    )


def tab(content, label=None, tab_id="", className=""):
    return dbc.Tab(
        dbc.Card(make_rows(content), body=True, className="mt-3 " + className),
        label=label,
        tab_id=tab_id,
    )
