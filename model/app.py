
from dash import Dash, dcc, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import layout_templates.layout as tpl


class Model:
    def __init__(self):
        self.df = px.data.gapminder()
        self.ylist = [int(i) for i in self.df["year"].unique()]
        self.yearStart = self.ylist[0]
        self.yearEnd = self.ylist[-1]
        self.yearStep = self.ylist[1] - self.ylist[0]

    def chart(self, year):
        return px.scatter(
            self.df[self.df["year"] == year],
            x="lifeExp",
            y="gdpPercap",
            title=f"Year: {year}",
            color="continent",
            size="pop",
        )

    header = "Global Statistics from Gapminder"
    description = """
      See how life expectancy changes over time 
      and in relation to GDP.
      Move the slider to change the year to display.
    """
    sliderCaption = "Select the year for the chart"


def view(model):
    slider = dcc.Slider(
        id="slider",
        min=model.yearStart,
        max=model.yearEnd,
        step=model.yearStep,
        value=model.yearStart,
        tooltip={"placement": "bottom", "always_visible": True},
    )
    left = tpl.Form([model.description, (model.sliderCaption, slider)])
    right = tpl.Card([dcc.Graph(id="graph")], width=8)
    return  tpl.Layout([[left, right]], title=model.header)


app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB])
model=Model()
app.layout = view(model)


@app.callback(Output("graph", "figure"), Input("slider", "value"))
def update(year):
    return model.chart(year)


if __name__ == "__main__":
    app.run_server(debug=True)

