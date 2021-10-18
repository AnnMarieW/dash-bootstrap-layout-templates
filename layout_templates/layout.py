#
"""
Design Objectives:

- easy to go from shorthand to full customization

- tpl.Layout
  - is a dbc.Container with optional header and footer
  - each item is a wrapped in a dbc.Row
  - if the item is a list, then it's a multi col row.  items in the list may be any of type:
      - tpl.Card - the width parameter is passed to dbc.Col
      - tpl.Form - the width parameter is passed to dbc.Col
      - dbc.Col  - full customization of a column - good if you don't want the content in a card.

  -  tpl.Card
        - wrapped in dbc.Col()
        - has a width prop.  Width accepts int or dict.  Dict includes the dbc.Column props for width and breakpoints

  -  tpl.Form
          - wrapped in a dbc.Col(dbc.Card())
          - default width is set for control pannel with responsive breakpoints:
             width={"width":12, "md":6, "xl":4}
         - if children include tuples ("label", component), then it adds bottom margin

  - Header
        - adds a logo if one
        - use custom headers for multi-page apps

  todo - in dcc.Markdwon, un-formatted text is wrapped in a <p> with 1rm mb which does not look good in labels
        and in card headers.  How to remove this in tpl.Form and tpl.Card headers, footers and labels?

"""
from dash import html, dcc
import dash_bootstrap_components as dbc
from layout_templates.util import get_logo


def make_markdown(content):
    """ Wrap text in dcc.Markdown() """
    if isinstance(content, list):
        return [dcc.Markdown(c, className="mb-0") if isinstance(c, str) else c for c in content]
    else:
        return dcc.Markdown(content, className="mb-0") if isinstance(content, str) else content


def Header(title):
    """ Default single page header bar """
    header = html.H4([get_logo(), title], className="bg-primary text-white hstack gap-3 p-3")
    return header if title else None


def Form(content, width={"width":12, "md":6, "lg":4}, header=None, floating_form=False ):
    """ returns a dbc.Col(dbc.Card(dbc.Form()))"""
    form = []
    for c in content:
        label = " "
        # handle label  if given
        if len(c) == 2:
            label, c = c
        form.append(html.Div([make_markdown(label), make_markdown(c)], className="mb-4"))
    return Card(form, width=width, header=header)


def make_col(content, width):
    """ wraps content in a dbc.Col
        :param width: int or a dict with breakpoint "xs", "sm", "md", "lg" "xl", "xxl"

    """
    if isinstance(width, int):
        return dbc.Col(content, width=width)
    if isinstance(width, dict):
        if "width" in width and len(width) == 1:
            return dbc.Col(content, width=width['width'])
    return dbc.Col(content, **width )


def Card(content, header=None, footer=None, className=None, width=12):
    """ creates a dbc.Col(dbc.Card() ) """
    header = dbc.CardHeader(make_markdown(header)) if header else None
    content = Grid(content) if content else None
    footer = dbc.CardFooter(make_markdown(footer)) if footer else None
    card = dbc.Card([header, dbc.CardBody(content), footer], className=className)
    return make_col(card, width)


def Grid(content):
    """ makes a single or multi column dbc.Row from a list of components"""
    # to-do check if content of the col is a string and wrap with markdown?
    content = make_markdown(content)
    row = []
    for c in content:
        if isinstance(c, (dbc.Col, list)):
            row.append(dbc.Row(c, className="mb-2"))
        elif isinstance(c, dbc.Row):
            row.append(c)
        else:
            row.append(dbc.Row(dbc.Col(c), className="mb-2"))
    return row


def Layout(content, title="Layout Templates Demo", className=None, id=""):
    return dbc.Container(
        [Header(title)] + Grid(content),
        fluid=True,
        className=className,
        id=id,
    )


def Tab(content, label=None, tab_id="", className=""):
    return dbc.Tab(
        dbc.Card(Grid(content), body=True, className="mt-3 " + className),
        label=label,
        tab_id=tab_id,
    )
