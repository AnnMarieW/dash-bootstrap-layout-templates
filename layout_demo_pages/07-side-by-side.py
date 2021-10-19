from dash import Dash, dcc
import plotly.express as px
import dash_bootstrap_components as dbc
import layout_templates.layout as tpl

df = px.data.tips()
fig = px.scatter(df, x="total_bill", y="tip", opacity=0.65, trendline="ols")
graph = tpl.Card([dcc.Graph(figure=fig)], width={"width":12, "lg":6})

app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB])

app.layout = tpl.Layout(
    [
        """        
        *** Two graphs side by side. One of the most popular question on the Dash Community Forum with >65K views. ***  
        ________    
        To make a multi-column row, simply put the items in a list!
        """,
        [graph, graph],
        " ### Wow - that was so easy! ##",
    ],
)

if __name__ == "__main__":
    app.run_server(debug=True)
