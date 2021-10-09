from dash import Dash, html, dcc, dash_table, Input, Output, State, callback_context
import dash_bootstrap_components as dbc
import plotly.express as px
import layout_templates.layout as tpl

df = px.data.tips()

app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.SPACELAB],
    suppress_callback_exceptions=True,
)


checklist = dbc.Checklist(
    id="slide-checklist",
    options=[{"label": d, "value": d} for d in ["Thur", "Fri", "Sat", "Sun"]],
    value=["Sun"],
)

checklist_card = tpl.card([(checklist, "Select day:")])

slide_content = tpl.layout([
        [
            dbc.Col(checklist_card, width=3),
            dbc.Col(dcc.Graph(id="slide-graph"), width=9),
        ],
    ],
    title=None,
)


slide_deck = {
    1: tpl.card([
        """
        ### Hey team - Check out these slides for our next planning meeting!

        -----------
        Use Dash templates to quickly make an interactive slide deck. This entire app has fewer than 100 lines of code!
        """
    ]),
    2: tpl.card([
        (
            dcc.Graph(figure=px.bar(df, x="day", y="total_bill")),
            "Maybe we should close on the weekend?  Thursday was higher than normal but still doesn't cover overhead",
        )
    ]),
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
        )
    ]),
    3: tpl.card([
        (
            dcc.Graph(
                figure=px.sunburst(df, path=["day", "time"], values="total_bill")
            ),
            "This shows the success of Thursday's lunch event!",
        )
    ]),
    4: tpl.card([(slide_content, "Here is some data on tips",)]),
}

pagination = dbc.Pagination(
    id="presentation-page",
    max_value=len(slide_deck),
    fully_expanded=False,
    previous_next=True,
    active_page=1,
)

app.layout = tpl.layout(
    [tpl.card([(pagination, "Select a slide")]), html.Div(id="presentation")],
    title="Interactive Presentation",
)


@app.callback(
    Output("presentation", "children"), Input("presentation-page", "active_page")
)
def show_page(active_page):
    return slide_deck[active_page]


@app.callback(Output("slide-graph", "figure"), Input("slide-checklist", "value"))
def update_slide(days):
    dff = df[df.day.isin(days)]
    return px.histogram(dff, x="total_bill", y="tip", color="sex", marginal="rug")


if __name__ == "__main__":
    app.run_server(debug=True)
