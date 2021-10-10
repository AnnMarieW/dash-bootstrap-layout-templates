from dash import Dash, dcc
import plotly.express as px
import dash_bootstrap_components as dbc
import layout_templates.layout as tpl

df = px.data.tips()
fig = px.scatter(df, x="total_bill", y="tip", opacity=0.65, trendline="ols")

app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB])

app.layout = tpl.layout(
    [
        """
        # Hello Dash Templates!
        *** Two graphs side by side. One of the most popular question on the 
        Dash Community Forum with >65K views***
        """,
        [dbc.Col(dcc.Graph(figure=fig), width= 12, md=6), dbc.Col(dcc.Graph(figure=fig), width=12, md=6)],
        " ### Wow - that was so easy! ##",
    ],
)

if __name__ == "__main__":
    app.run_server(debug=True)
