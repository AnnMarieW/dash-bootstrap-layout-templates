from dash import Dash, dcc, dash_table
import plotly.express as px
import dash_bootstrap_components as dbc
import layout_templates.layout as tpl

df = px.data.tips()
fig = px.scatter(df, x="total_bill", y="tip", opacity=0.65, trendline="ols")

table = dash_table.DataTable(
    data=df.to_dict("records"),
    columns=[{"id": c, "name": c} for c in df.columns],
    page_size=10,
    style_table={"overflowX": "auto", "border":"1px solid"},
)
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = tpl.layout(
    [
        """
        # Hello Dash Templates!    
        *** Example of custom row ***
        """,

        dcc.Graph(figure=fig),

        dbc.Row(dbc.Col(table, width=7), justify="center"),
    ],
)

if __name__ == "__main__":
    app.run_server(debug=True)
