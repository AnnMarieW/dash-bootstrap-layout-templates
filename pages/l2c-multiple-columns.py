from dash import Dash, dcc, dash_table
import plotly.express as px
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import layout_templates.layout as tpl

df = px.data.tips()

fig = px.scatter(df, x="total_bill", y="tip", opacity=0.65, trendline="ols")
fig2= go.Figure(go.Indicator(mode="number+delta",value = 450, delta={"reference":90}, title={"text":"Sales"}))
fig2.update_layout(margin=dict(l=20, r=20, t=50, b=20))

gauge = dbc.Card(dcc.Graph(figure=fig2, style={"height":150}))
graph = dbc.Card(dcc.Graph(figure=fig, ))


app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB])

app.layout = tpl.layout(
    [
        """
        # Hello Dash Templates!
        *** Use a list to make multiple columns ***
        """,

        [(gauge, 4), (gauge, 4), (gauge, 4)],
        graph

    ],
)

if __name__ == "__main__":
    app.run_server(debug=True)
