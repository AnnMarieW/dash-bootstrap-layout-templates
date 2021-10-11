from dash import Dash, html, dcc, dash_table, Input, Output, State, callback_context
import dash_bootstrap_components as dbc
import plotly.express as px
import layout_templates.layout as tpl
from aio.aio_components import SlideDeckAIO

df = px.data.tips()

app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.SPACELAB],
    suppress_callback_exceptions=True,
)

#----- slide 4 content --------------
checklist = dbc.Checklist(
    id="slide-checklist",
    options=[{"label": d, "value": d} for d in ["Thur", "Fri", "Sat", "Sun"]],
    value=["Sun"],
)
checklist_card = tpl.card([(checklist, "Select day:")])
slide_content = tpl.layout(
    [
        [
            dbc.Col(checklist_card, width=3),
            dbc.Col(dcc.Graph(id="slide-graph"), width=9),
        ],
    ],
    title=None,
)
# --------------------------------

slide_deck = {
    1: tpl.card(
        [
            """
            ### Hey team - Check out these slides for our next planning meeting!
    
            -----------
            Use Dash templates to quickly make an interactive slide deck. This entire app has about 70 lines of code!
            """
        ], className='vh-100 vw-100'
    ),
    2: tpl.card([
        (
            dcc.Graph(figure=px.bar(df, x="day", y="total_bill")),
            "Maybe we should close on the weekend?  Thursday was higher than normal but still doesn't cover overhead",
        )], className='vh-100 vw-100'
    ),
    5: tpl.card([
        (
            dcc.Graph(
                figure=px.parallel_categories(
                    df,
                    color="size",
                    color_continuous_scale=px.colors.sequential.Inferno,
                )
            ),
            "This graph is cool, but I have no idea what it means.  Can someone explain?",
        )]
    ),
    3: tpl.card([
        (
            dcc.Graph(
                figure=px.sunburst(df, path=["day", "time"], values="total_bill")
            ),
            "This shows the success of Thursday's lunch event!",
        )]
    ),
    4: tpl.card([(slide_content, "Here is some data on tips",)]),
}

app.layout = dbc.Container(SlideDeckAIO(slide_deck=slide_deck, title="Interactive Presentation"), fluid=True)


@app.callback(Output("slide-graph", "figure"), Input("slide-checklist", "value"))
def update_slide(days):
    dff = df[df.day.isin(days)]
    return px.histogram(dff, x="total_bill", y="tip", color="sex", marginal="rug")


if __name__ == "__main__":
    app.run_server(debug=True)
