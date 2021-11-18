import dash

dash.register_page(__name__, path="/my_page2/<my_id>/<other_id>")


def layout(my_id="", other_id="", **other_unknown_variables):
    return dash.html.Div(
        [
            dash.dcc.Textarea(
                id=my_id,
                value=f"variables from pathname:  my_id: {my_id} other_id: {other_id}",
                style={"width": 400},
            ),
            dash.dcc.Dropdown(
                id='auction_dropdown',
                options=[{'label': auction, 'value': auction}
                         for auction in
                         ['AAAW', 'FAAO', 'SVAA', 'MAA', 'BWAE', 'GCAA', 'PXAA', 'DFWA', 'BCAA', 'GOAA']],
                value=['AAAW', 'FAAO', 'SVAA', 'MAA', 'BWAE', 'GCAA', 'PXAA', 'DFWA', 'BCAA', 'GOAA'],
                # Default value to show
                persistence=True,
                multi=True,
                searchable=False
            ),
        ]
    )
