import dash

dash.register_page(
    __name__,
    path_template="/news/<section>/<topic>",
    title="Plotly Times - World News",
    description="The Plotly Times.  All the data that's fit to plot.  World news topic 1",
    path="/news/world/1",
)


def layout(section=None, topic=None, **other_unknown_query_strings):
    return dash.html.Div(f"variables from pathname:  section: {section} topic: {topic}")
