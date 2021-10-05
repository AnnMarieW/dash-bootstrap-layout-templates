# Overview
Dash Bootstrap Layout Templates is a project for developing:
- layout templates to help create beautiful Dash quickly and with less code. 
- A collection of Dash "all-in-one" components to provide low code solutions for common app functionality.
- Custom CSS classes to enhance the style of Dash Core Components and the Dash DataTable when used in Bootstrap light 
or dark themed apps.


## Layout Templates Design Goals    
   - Simplify app development
   - Reduce the learning curve for new users
   - Build apps with standard layouts faster
   - Integrate templates seamlessly with a fully customizable Dash App
   - No changes to callbacks
   

## Layout Templates

Provides layout templates for the most common App layouts:
1. `tpl.layout`: Is a `dbc.Container` with optional header and footer. This is ideal for the main app.layout.
It also provides  a shorthand syntax for adding rows and columns using the Bootstrap grid system to create responsive moble-first apps.

2. `tpl.card`: Is a dbc.Card with optional header and footer.  It includes a shorthand for adding labeled components to a card
which is ideal for creating an app control panel.
3. `tpl.tab`: Is a dbc.Tab with a shorthand for placing tab content in a card and labeling the tab.

With these three simple layout templates and shorthands, it's possible to create standard app layouts such as
control panels on the top, side or bottom  very quickly with less code.  The tabs and cards can be placed anywhere
in the flexable Bootstrap grid layout.

 ## "All in One" Components
The All-in-One Dash components bundle components and callbacks to provide a low code solution for commonly used app functionality. 
Currently, this project has a button that enables the user to change the app theme to any of the 22 themes in the `dash-bootstrap-components`
library. This functionality can be added to any Dash app with 2 lines of code!

## CSS for light and dark themes

In the `assets` folder you will find  `dbc.css` that defines two classes to help style Dash Core Components and the 
Dash DataTable to make them more compatible with Bootstrap light and dark themes.  Simply add `className="dbc-light"` or
`className="dbc-dark"` to the outer container of your app. 

## Installation

This library is unpublished and is intended for development only.  There are will be frequent and unannounced 
breaking changes.  With that being said, I encourage you to clone or fork this repo and take all the new features
for a test drive!  Feedback and/or pull requests are welcome.  Please feel free to open an issue here.
 
## Demo Apps

After cloning this repo:
- Run `demo_app.py` to see the code and the app for each of the 14 examples in the docs. This app is also  a handy
cheatsheet for the new templates!
- Run the `theme-switch1.py` and/or `theme-switch2.py` to demo the new ThemeChangerAIO component.


## Documentation
The documentation, like the entire project, is a work in progress.  See the `docs` folder for more detailed
examples.


Here's a quick preview - see the docs or run the demo apps to see 16 other examples!