import dash_bootstrap_components as dbc
from dash import html

DCC_DOCS = (
    "https://dash.plotly.com/dash-core-components/"
)


def make_subheading(label, link):
    slug = label.replace(" ", "")

    heading = html.H2(
        html.Span(
            [
                label,
                html.A(
                    html.I(className="bi bi-book h4 ms-2"),
                    href=f"{DCC_DOCS}{link}",
                    target="_blank",
                   # id=f"tooltip_target_{slug}",
                ),
            ],
        ),
    )

    return html.Div(
        [
            heading,
            # dbc.Tooltip(
            #     f"See {label} documentation", target=f"tooltip_target_{slug}"
            # ),
        ],
        className="mt-3",
    )
