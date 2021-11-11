from dash import Dash, html, dcc, dash_table, Input, Output, State, callback_context
import dash_bootstrap_components as dbc
import plotly.express as px
import layout_templates.layout as tpl
from aio.aio_slide_deck import SlideDeckAIO

df = px.data.tips()

app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.SPACELAB],
    suppress_callback_exceptions=True,
)

#----- used in slide 4 layout  --------------
checklist = dbc.Checklist(
    id="checklist",
    options=[{"label": d, "value": d} for d in ["Thur", "Fri", "Sat", "Sun"]],
    value=["Sun"],
)
controls = tpl.Form([("Select day:", checklist)])
slide_content = tpl.Layout(
    [
        [
            controls,
            tpl.Card([dcc.Graph(id="slide-graph")], width=8),
        ],
    ],
    title=None,
)
# --------------------------------

# slide_deck is a dict where the key is page number and the value is the layout for each page.
# This is passed to the SlideDeckAIO component
slide_deck = {
    1: tpl.Card(
        [
            """
            ### Hey team - Check out these slides for our next planning meeting!
    
            -----------
            Use Dash templates to quickly make an interactive slide deck. This entire app has about 70 lines of code!
            """
        ],
    ),
    2: tpl.Card([
        (
            "Maybe we should close on the weekend?  Thursday was higher than normal but still doesn't cover overhead",
            dcc.Graph(figure=px.bar(df, x="day", y="total_bill")),
        )],
    ),
    5: tpl.Card([
        (
            "This graph is cool, but I have no idea what it means.  Can someone explain?",
            dcc.Graph(
                figure=px.parallel_categories(
                    df,
                    color="size",
                    color_continuous_scale=px.colors.sequential.Inferno,
                )
            ),

        )]
    ),
    3: tpl.Card([
        (
            "This shows the success of Thursday's lunch event!",
            dcc.Graph(
                figure=px.sunburst(df, path=["day", "time"], values="total_bill")
            ),
        )]
    ),
    4: tpl.Card(["Here is some data on tips", slide_content]),
}

# Slide deck navigation is handled in the SlideDeckAIO component
app.layout = tpl.Layout([SlideDeckAIO(slide_deck=slide_deck, title="Interactive Presentation")], title=None)


# slide 4 callback
@app.callback(Output("slide-graph", "figure"), Input("checklist", "value"))
def update_slide(days):
    dff = df[df.day.isin(days)]
    return px.histogram(dff, x="total_bill", y="tip", color="sex", marginal="rug")


if __name__ == "__main__":
    app.run_server(debug=True)
