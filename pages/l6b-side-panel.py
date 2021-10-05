from dash import Dash, dcc, html
import plotly.express as px
import dash_bootstrap_components as dbc
import layout_templates.layout as tpl

df = px.data.tips()
fig = px.scatter(df, x="total_bill", y="tip", opacity=0.65, trendline="ols")

app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB])

controls = tpl.card(
    [(dcc.Dropdown(), "My dropdown"), (dcc.Slider(), "My Slider")],
    title=html.H6("My control panel"),
    # footer="My footer"
)

app.layout = tpl.layout(
    [
        """
        # Hello Dash Templates!
        *** App with a side panel ***
        """,
        [(controls, 4), (dcc.Graph(figure=fig, className="border"), 8)],
    ],
)

if __name__ == "__main__":
    app.run_server(debug=True)
