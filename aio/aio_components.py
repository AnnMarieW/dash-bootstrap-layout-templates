#
from dash import html, Input, Output, State, callback, clientside_callback, MATCH
import dash_bootstrap_components as dbc
import uuid

dbc_themes_url = {
            item: getattr(dbc.themes, item)
            for item in dir(dbc.themes)
            if not item.startswith(("_", "GRID", "VAPOR", "QUARTZ", "MORPH", "ZEPHYR"))
        }
url_dbc_themes = dict(map(reversed, dbc_themes_url.items()))
dbc_themes_lowercase = [t.lower() for t in dbc_themes_url.keys()]
dbc_dark_themes = ["cyborg", "darkly", "slate", "solar", "superhero"]

class ThemeChangerAIO(html.Div):
    class ids:
        radio = lambda aio_id: {
            'component': 'ThemeChangerAIO',
            'subcomponent': 'radio',
            'aio_id': aio_id
        }
        button = lambda aio_id: {
            'component': 'ThemeChangerAIO',
            'subcomponent': 'button',
            'aio_id': aio_id
        }
        offcanvas = lambda aio_id: {
            'component': 'ThemeChangerAIO',
            'subcomponent': 'offcanvas',
            'aio_id': aio_id
        }
        dummy_div = lambda aio_id: {
            'component': 'ThemeChangerAIO',
            'subcomponent': 'dummy_div',
            'aio_id': aio_id
        }

    ids=ids

    def __init__(
            self,
            radio_props = {},
            button_props = {},
            offcanvas_props = {},
            dummy_div_props = {},
            aio_id=None
    ):
        """

        :param aio_id:
        """
        from dash_bootstrap_templates import load_figure_template
        load_figure_template(dbc_themes_lowercase)

        if aio_id is None:
            aio_id = str(uuid.uuid4())

        if "options" not in radio_props:
            radio_props["options"] = [
                {
                    "label": str(i),
                    "label_id": "theme-switch-label",
                    "value": dbc_themes_url[i],
                }
                for i in dbc_themes_url
            ]
            # assign id to dark themes in order to apply css
            for option in radio_props["options"]:
                if option["label"].lower() in dbc_dark_themes:
                    option["label_id"] = "theme-switch-label-dark"

            radio_props["value"] = dbc_themes_url["BOOTSTRAP"]

        button_props = button_props.copy()
        if 'children' not in button_props:
            button_props['children']= "Change Theme"
        if 'color' not in button_props:
            button_props['color'] = "secondary"
        if 'outline' not in button_props:
            button_props['outline'] = True
        if 'size' not in button_props:
            button_props['size'] = "sm"

        offcanvas_props = offcanvas_props.copy()
        if 'children' not in offcanvas_props:
            offcanvas_props['children'] = [
                dbc.RadioItems(id=self.ids.radio(aio_id), **radio_props),
            ]
        if 'title' not in offcanvas_props:
            offcanvas_props['title']="Select a Theme"
        if 'is_open' not in offcanvas_props:
            offcanvas_props['is_open']=False
        if 'backdrop' not in offcanvas_props:
            offcanvas_props['backdrop'] = False
        if 'style' not in offcanvas_props:
            offcanvas_props['style']= {"width": 235}

        dummy_div_props['children'] = None

        super().__init__([
            dbc.Button(id=self.ids.button(aio_id), **button_props),
            dbc.Offcanvas(id=self.ids.offcanvas(aio_id), **offcanvas_props),
            html.Div(id=self.ids.dummy_div(aio_id), **dummy_div_props)
        ])


    @callback(
        Output(ids.offcanvas(MATCH), "is_open"),
        Input(ids.button(MATCH), "n_clicks"),
        [State(ids.offcanvas(MATCH), "is_open")],
    )
    def toggle_theme_offcanvas(n1, is_open):
        if n1:
            return not is_open
        return is_open


    # Using 2 stylesheets with the delay reduces the  flicker when the theme changes
    clientside_callback(
        """
        function(url) {
            // Select the stylesheets.
            var stylesheets = document.querySelectorAll('link[rel=stylesheet][href^="https://cdn.jsdelivr"]')
            // Update the url of the main stylesheet.
            stylesheets[stylesheets.length - 1].href = url
            // Delay update of the url of the buffer stylesheet.
            setTimeout(function() {stylesheets[0].href = url;}, 100);
        }
        """,
        Output(ids.dummy_div(MATCH), "children"),
        Input(ids.radio(MATCH), "value"),
    )
