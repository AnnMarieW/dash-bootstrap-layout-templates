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

tab1 = tpl.tab([" ## This is my Graph ", dcc.Graph(figure=fig)], label="Graph")
tab2 = tpl.tab([" ## This is my Table ", table], label="Table")
tab3 = tpl.tab([" ## More Info Here"], label="More Info")

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


#
# --------------------------------------------------------
# Same app without the templates:
#     Layout:                 35 lines
#     Layout with templates:  12 lines
# --------------------------------------------------------
#
# from dash import Dash, dcc, html, dash_table
# import plotly.express as px
# import dash_bootstrap_components as dbc
#
#
# df = px.data.tips()
# fig = px.scatter(df, x="total_bill", y="tip", opacity=0.65, trendline="ols")
#
# table = dash_table.DataTable(
#     data=df.to_dict("records"),
#     columns=[{"id": c, "name": c} for c in df.columns],
#     page_size=10,
#     style_table={"overflowX": "auto"},
# )
# app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB])
#
#
# tab1 = dbc.Tab(
#     dbc.Card(
#         dbc.CardBody(
#             [
#                 dcc.Markdown("## This is my Graph", className="mb-3",),
#                 dcc.Graph(figure=fig),
#             ]
#         ),
#     ),
#     label="Graph",
# )
#
# tab2 = dbc.Tab(
#     dbc.Card(
#         dbc.CardBody([dcc.Markdown("## This is my Table", className="mb-3",), table]),
#     ),
#     label="Table",
# )
#
# tab3 = dbc.Tab(dbc.Card(dbc.CardBody(html.Div("More Info"))), label="More Info")
#
#
# app.layout = dbc.Container(
#     [
#         html.H4("Layout Templates Demo", className="bg-primary text-white p-3"),
#         dcc.Markdown(
#             """
#             # Hello Dash Templates
#             *** Use tpl.tab for tab content ***
#             """,
#             className="my-3",
#         ),
#         dbc.Tabs([tab1, tab2, tab3]),
#     ],
#     fluid=True,
# )
#
# if __name__ == "__main__":
#     app.run_server(debug=True)
