from dash import Dash
import dash_bootstrap_components as dbc
import layout_templates.layout as tpl

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

intro = """
### Overview

This is a demo of the Dash Bootstrap Layout Templates. Using a template makes it easier and faster to create the most 
common app layouts.  

The templates use Dash Bootstrap Components under the hood to create responsive mobile-first apps.  Customize the look 
of your app by choosing one of the 24 Bootstrap themes.  

Use the templates to build your entire app, or include them as a part of a regular Dash app.  Seamlessly transition 
from using a template to creating a fully customized production-ready Dash app.  

Since there are no changes to Dash callbacks and only 4 templates, there is not a lot of "new stuff" to learn. These templates
 are great for beginners, but the template's convenient shorthand will make even experienced Dash developers want to reach for a template. 
   

### Layout Templates

Here are a few guidelines for getting started:  

1. `tpl.Layout`:  is ideal for the main app.layout.
    - A header is added automatically. It's styled based on your selected Bootstrap theme and will include a logo too, if you
     have an image in the assets folder named "logo".  You can update the app title with the `title` prop.  To
     use your own custom header, set `title=None' and put your custom header in the first row.   
    - You can use Markdown in any string.
    - Each item in the layout children is a row. No need to wrap it in a dbc.Row(dbc.Col()) the template does that for you!
    - If the item is a list, it's a multi-column row.  
    

2. `tpl.Card`: is a dbc.Card with optional header and footer. This is a convenient container for any content.
    - The `width` prop is passed to the dbc.Col().  It can be and integer, for example, `width=6` or you can include responsive breakpoints
    by using a dict instead. For example, `width={"width":12, "lg":6}`  will make the card 6 columns on large screens and above, otherwise
    12 columns wide.   

    
3. `tpl.Form` is a dbc.Form wrapped in a dbc.Card.  This is ideal for a control panel with labeled components.
    - the `width` prop is passed to the dbc.Col() and the default is `{"width":12, "md":6, "lg":4}` This means it wil be
    4 columns wide on larger screens and either 6 columns or 12 columns on smaller screens.  
    - each item in `children` is a row.
    - if the row item is a tuple ("component label", component) the label and component will be on two rows and includes bottom margin automatically.  
    
4. `tpl.Tab`: is a dbc.Tab with a shorthand for placing tab content in a card and labeling the tab. This make it faster and 
easier to add tabs to an app. 


### Next Steps

Use this app as a tutorial by stepping through each app in sequence, or use it as 
a handy cheatsheet to go directly to the topic using the dropdown.

See the project on [GitHub](https://github.com/AnnMarieW/dash-bootstrap-layout-templates)
"""


app.layout = tpl.Layout([intro])

if __name__ == "__main__":
    app.run_server(debug=True)
