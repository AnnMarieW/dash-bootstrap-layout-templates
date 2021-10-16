from dash import dcc

import plotly.express as px
import layout_templates.layout as tpl


df = px.data.tips()

layout= tpl.card(
    [
        (
            dcc.Graph(figure=px.bar(df, x="day", y="total_bill")),
            "Maybe we should close on the weekend?  Thursday was higher than normal but still doesn't cover overhead",
        )
    ], className='vh-100 vw-100'
)