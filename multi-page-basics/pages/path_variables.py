import dash

dash.register_page(__name__, path="/my_page/<my_id>")


def layout(my_id="", **other_unknown_variables):
    return dash.dcc.Textarea(id=my_id, value=f"The id of this component is {my_id}")

