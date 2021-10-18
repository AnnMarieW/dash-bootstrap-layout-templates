from dash import Dash, dcc
import plotly.express as px
import dash_bootstrap_components as dbc
import layout_templates.layout as tpl

df = px.data.tips()
fig = px.scatter(df, x="total_bill", y="tip", opacity=0.65, trendline="ols")

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = tpl.Layout(
    [
        """
        # Hello Dash Templates!    
        *** Each item in the layout is a row ***
        """,

        dcc.Graph(figure=fig),

        """  ### This is a really cool graph! """,
    ],
)

if __name__ == "__main__":
    app.run_server(debug=True)
