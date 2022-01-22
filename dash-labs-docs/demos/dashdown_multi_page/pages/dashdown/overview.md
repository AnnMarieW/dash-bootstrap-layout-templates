---
dash.register_page(
    __name__,
    name="Overview",
    order=0,
    layout=dashdown(
        "pages/dashdown/overview.md",
        side_by_side=True,
    ),
)
---



## Welcome to `dashdown`! - _Markdown that runs code_
--------------

### Background

`dashdown` creates a page layout from a markdown file.  It will display the Markdown text and has options to run
and/or display the embedded code blocks.  
  
`dashdown` is compatible with the `pages/` api.  The documentation you are now viewing uses `pages/` to create a multi-page app.  Each page is
created from a from a Markdown file. You can find it [here --todo add link]().
 
### `dashdown` is ideal for:  

 - __Reports__  
 - __Presentations__
 - __Documentation__ 
 - __Tutorials__
   



------------

### Quickstart

This is how to create a single page app from a Markdown file using `dashdown`. It's live!  Try interacting with the slider.


```python exec-code-false
from dash import Dash
from dash_labs import dashdown

app.layout = dashdown("path_to_my_mardown_file.md", side_by_side=True)

if __name__ == "__main__":
    app.run_server()
    
    
```
----------
----------

```python

from dash import Dash, dcc, html, Output, Input, callback
import plotly.express as px


df = px.data.iris()
fig = px.scatter(
        df, x="sepal_width", y="sepal_length",
        color="species", size='petal_length',
        hover_data=['petal_width'])
        
app = Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id="scatter-plot"),
    html.P("Petal Width:"),
    dcc.RangeSlider(
        id='range-slider',
        min=0, max=2.5, step=0.1,
        marks={0: '0', 2.5: '2.5'},
        value=[0.5, 2]
    ),
])

@callback(
    Output("scatter-plot", "figure"),
    Input("range-slider", "value"))
def update_bar_chart(slider_range):
    low, high = slider_range
    mask = (df['petal_width'] > low) & (df['petal_width'] < high)
    fig = px.scatter(
        df[mask], x="sepal_width", y="sepal_length",
        color="species", size='petal_length',
        hover_data=['petal_width'])
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)

```


