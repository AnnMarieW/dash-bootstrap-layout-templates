# Layout templates

To see all the layout template examples  run `demo_app.py` in the root directory.  This makes a handy template 
cheetsheet too!

## Quickstart

This first example is a quickstart app for a new user.


![image](https://user-images.githubusercontent.com/72614349/136036149-b40be367-36c8-49de-b0e4-5784015e0628.png)


The `tpl.layout` is a `dbc.Container` with optional header and footer. This is ideal for the main app.layout.
It also provides  a shorthand syntax for adding rows and columns using the Bootstrap grid system to create responsive 
moble-first apps. More on that topic later.

The content of the `tpl.layout` may contain strings, components or lists.  If it contains a string like in this example, 
then under-the-covers it wraps the string in a `dcc.Markdown` component - so Markdown syntax can be used.  

Here is the code to create this app without the template:




```python

from dash import Dash, dcc, html
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
    [
        html.H4(
            "My Cool Dash App",
            className="bg-primary bg-gradient rounded text-white p-3",
        ),
        dbc.Row(
            dbc.Col(
                dcc.Markdown(
                    """
                    # Hello Dash Templates!
                    *** Make your first app in less than 5 minutes! ***
                    """
                )
            )
        ),
    ],
    fluid=True,
)

if __name__ == "__main__":
    app.run_server(debug=True)

```
