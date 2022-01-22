import dash


def register_paths():
    dash.register_page(
        "path_variables_path1",
        path_template="/news/<section>/<topic>",
        title="Plotly Times - Sports",
        description="The Plotly Times.  All the data that's fit to plot.  Sports news topic 1",
        path="/news/sports/1",
        layout=dash.page_registry["pages.path_variables"]["layout"],
    )

    dash.register_page(
        "path_variables_path2",
        path_template="/news/<section>/<topic>",
        title="Plotly Times - Sports",
        description="The Plotly Times.  All the data that's fit to plot.  Sports news topic 2",
        path="/news/sports/2",
        layout=dash.page_registry["pages.path_variables"]["layout"],
    )
