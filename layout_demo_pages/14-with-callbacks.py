
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc
import layout_templates.layout as tpl

df = px.data.gapminder()

app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB])

# This will be changed to the new shorthand in the next release of Dash
import layout_templates.util as util
slider = util.make_range_slider(df.year.unique(), id="years")
checklist = util.make_checklist(df.continent.unique(), id="checklist")
dropdown = util.make_dropdown(["gdpPercap", "lifeExp", "pop"], id="indicator")
table = util.make_datatable(df, id="table")


controls = tpl.Form(
    [
        ("Select indicator (y-axis)", dropdown),
        ("Select Continents", checklist),
        ("Select Years", slider),
    ],
)

app.layout = tpl.Layout([[controls, tpl.Card([dcc.Graph(id="line_chart")], width=8)]])


@app.callback(
    Output("line_chart", "figure"),
    Input("indicator", "value"),
    Input("checklist", "value"),
    Input("years", "value"),
)
def update_line_chart(indicator, continents, years):
    if continents == [] or indicator is None:
        return {}

    dff = df[df.year.between(years[0], years[1])]
    dff = dff[dff.continent.isin(continents)]

    fig = px.line(dff, x="year", y=indicator, color="continent", line_group="country")
    fig.update_layout(margin=dict(l=75, r=20, t=10, b=20))
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
