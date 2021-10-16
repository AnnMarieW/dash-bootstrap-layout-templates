from dash import Dash, dcc, html
import plotly.express as px
import dash_bootstrap_components as dbc
import layout_templates.layout as tpl

df = px.data.tips()
fig = px.scatter(df, x="total_bill", y="tip", opacity=0.65, trendline="ols")

app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB])

controls = tpl.card(
    [(dcc.Dropdown(), "My dropdown"), (dcc.Slider(), "My Slider")],
    header="My control panel"
)

app.layout = tpl.layout(
    [
        [dbc.Col(controls, width=4), dbc.Col(tpl.card([dcc.Graph(figure=fig)]), width=8)],
    ],
)

if __name__ == "__main__":
    app.run_server(debug=True)



# --------------------------------------------------------
# Same app without the templates:
#     Layout:                 31 lines
#     Layout with templates:  13 lines
# --------------------------------------------------------
#
# from dash import Dash, dcc, html
# import plotly.express as px
# import dash_bootstrap_components as dbc
#
#
# df = px.data.tips()
# fig = px.scatter(df, x="total_bill", y="tip", opacity=0.65, trendline="ols")
#
# app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB])
#
#
# controls = dbc.Card(
#     [
#         dbc.CardHeader("My Control Panel"),
#         dbc.CardBody(
#             [
#                 html.Div([dbc.Label("Dropdown"), dcc.Dropdown(),], className="mb-3",),
#                 html.Div([dbc.Label("Slider"), dcc.Slider(),], className="mb-3",),
#             ]
#         ),
#     ],
# )
#
#
# app.layout = dbc.Container(
#     [
#         html.H4("Layout Templates Demo", className="bg-primary text-white p-3"),
#         dcc.Markdown(
#             """
#             # Hello Dash Templates!
#             *** App with a side panel ***
#             """,
#             className="my-3",
#         ),
#         dbc.Row(
#             [
#                 dbc.Col(controls, width=4),
#                 dbc.Col(dcc.Graph(figure=fig, className="border"), width=8),
#             ]
#         ),
#     ],
#     fluid=True,
# )
#
# if __name__ == "__main__":
#     app.run_server(debug=True)
