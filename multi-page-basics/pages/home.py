import dash
from dash import html


dash.register_page(
    __name__,
    path="/",
    name="Analytic Apps",
    description="Welcome to my app",
    order=0,
    redirect_from=["/old-home-page", "/v2"],
    extra_template_stuff="yup",
)

layout = html.Div(
    [
        "Home Page",
        dash.dcc.Dropdown(
                id='auction_dropdown2',
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
