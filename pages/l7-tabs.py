from dash import Dash, html, dcc, dash_table
import dash_bootstrap_components as dbc
import plotly.express as px

import layout_templates.layout as tpl

df = px.data.tips()
fig = px.scatter(df, x="total_bill", y="tip", opacity=0.65, trendline="ols")

table = dash_table.DataTable(
    data=df.to_dict("records"),
    columns=[{"id": c, "name": c} for c in df.columns],
    page_size=10,
    style_table={"overflowX": "auto"},
)

app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB])

tab1 = tpl.tab([""" ## This is my Graph """, dcc.Graph(figure=fig)], label="Graph")
tab2 = tpl.tab([table], label="Table")
tab3 = tpl.tab(["More App info"], label="More Info")

app.layout = tpl.layout(
    [
        """
        # Hello Dash Templates
        *** Use tpl.tab for tab content ***
        """,
        dbc.Tabs([tab1, tab2, tab3]),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
