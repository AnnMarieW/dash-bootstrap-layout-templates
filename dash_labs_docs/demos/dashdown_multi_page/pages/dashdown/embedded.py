from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
from dash_labs import dashdown
import dash

dash.register_page(__name__)


def layout():
    return dbc.Container(
        [
            dbc.Row(
                dbc.Col(
                    [
                        dcc.Markdown(
                            """
                    #### `dashdown` can be used within a regular Dash layout.  
                    In this example, the `sample.md` is displayed in a dbc.Collapse:
                    
                    ```python                    
                    app.layout = dbc.Container(
                        [
                            # other elements
                            
                            dbc.Collapse(
                                dbc.Card(dashdown("sample.md")),
                                id="collapse",
                                is_open=False,
                            ), 
                            
                            # other elements
                            
                        ], fluid=True
                    )
                                     
                    ```
                    click the "More Info" button to see the content.
                    
                    """,
                            className="mb-4",
                        ),
                        dbc.Button(
                            "More Info",
                            id="collapse-btn",
                            color="info",
                            className="m-4",
                            n_clicks=0,
                        ),
                        dbc.Collapse(
                            dbc.Card(dashdown("sample.md")),
                            id="collapse",
                            is_open=False,
                        ),
                    ]
                )
            )
        ],
        fluid=True,
    )


@callback(
    Output("collapse", "is_open"),
    Input("collapse-btn", "n_clicks"),
    State("collapse", "is_open"),
)
def toggle(n, is_open):
    if n:
        return not is_open
    return is_open
