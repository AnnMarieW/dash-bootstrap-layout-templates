from dash import Dash, dash_table
import dash_bootstrap_components as dbc
import plotly.express as px

df=px.data.tips()

app = Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

app.layout = dbc.Container(
    dash_table.DataTable(
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
        page_size=10,
        style_data_conditional=[
            {
                'if': {
                    'column_id': 'tip',
                },
                'backgroundColor': 'dodgerblue',
                'color': 'yellow',
                'fontWeight': 1000,
            },

        ]
    ),
    className="mycss"
)

if __name__ == "__main__":
    app.run_server(debug=True)