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

You can build an app with the templates --  or you can use them as part of a regular Dash app.  Seamlessly transition 
from using a template to creating a fully customized production-ready Dash app.  

Since there are no changes to Dash callbacks and only 3 templates, there is not a lot of "new stuff" to learn. These templates
 are great for beginners, but since they are so easy to use, even experienced Dash developers are likely to reach for a template 
   

### Layout Templates

The following three layout templates makes it easy to create standard app layouts such as
control panels on the top, side or bottom  very quickly with less code.  

1. `tpl.layout`: Is a `dbc.Container` with optional header and footer. This is ideal for the main app.layout.
It also provides  a shorthand syntax for adding rows and columns using the Bootstrap grid system to create responsive apps.

2. `tpl.card`: Is a dbc.Card with optional header and footer.  It includes a shorthand for adding labeled components to a card
which is ideal for creating an app control panel.  It's also a convenient container for any app content.

3. `tpl.tab`: Is a dbc.Tab with a shorthand for placing tab content in a card and labeling the tab. This make it faster and 
easier to add tabs to an app. 

*** Note that you can use Markdown in the text content in any of the three templates! ***

### Next Steps

Use this app as a tutorial by stepping through each app in sequence, or use it as 
a handy cheatsheet to go directly to the topic using the dropdown.

See the project on [GitHub](https://github.com/AnnMarieW/dash-bootstrap-layout-templates)
"""


app.layout = tpl.layout([intro])

if __name__ == "__main__":
    app.run_server(debug=True)
