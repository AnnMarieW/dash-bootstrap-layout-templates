from dash import Dash, dcc, html
import plotly.express as px
import dash_bootstrap_components as dbc
import layout_templates.layout as tpl

df = px.data.tips()
fig = px.scatter(df, x="total_bill", y="tip", opacity=0.65, trendline="ols")

app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB])

card_content = tpl.make_labeled_components(
    [(dcc.Dropdown(), "My dropdown"), (dcc.Slider(), "My Slider")],
)
controls = dbc.Card(card_content, body=True, className="bg-black text-white")

app.layout = tpl.layout(
    [
        html.H3("My Custom Header", className="text-center bg-black text-white p-2"),
        [(controls, 4), (dcc.Graph(figure=fig, className="border"), 8)],
    ],
    title=None,
)

if __name__ == "__main__":
    app.run_server(debug=True)
