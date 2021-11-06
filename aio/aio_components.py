
from dash import html, dcc, Input, Output, State, callback, clientside_callback, MATCH
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
            "component": "ThemeChangerAIO",
            "subcomponent": "radio",
            "aio_id": aio_id,
        }
        button = lambda aio_id: {
            "component": "ThemeChangerAIO",
            "subcomponent": "button",
            "aio_id": aio_id,
        }
        offcanvas = lambda aio_id: {
            "component": "ThemeChangerAIO",
            "subcomponent": "offcanvas",
            "aio_id": aio_id,
        }
        dummy_div = lambda aio_id: {
            "component": "ThemeChangerAIO",
            "subcomponent": "dummy_div",
            "aio_id": aio_id,
        }

    ids = ids

    def __init__(
        self,
        radio_props={},
        button_props={},
        offcanvas_props={},
        aio_id=None,
    ):
        """
        todo: write docstring
        :param aio_id:
        """
        from dash_bootstrap_templates import load_figure_template

        load_figure_template(dbc_themes_lowercase)

        if aio_id is None:
            aio_id = str(uuid.uuid4())

        radio_props = radio_props.copy()
        if "value" not in radio_props:
            radio_props["value"] = dbc_themes_url["BOOTSTRAP"]
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


        button_props = button_props.copy()
        if "children" not in button_props:
            button_props["children"] = "Change Theme"
        if "color" not in button_props:
            button_props["color"] = "secondary"
        if "outline" not in button_props:
            button_props["outline"] = True
        if "size" not in button_props:
            button_props["size"] = "sm"

        offcanvas_props = offcanvas_props.copy()
        if "children" not in offcanvas_props:
            offcanvas_props["children"] = [
                dbc.RadioItems(id=self.ids.radio(aio_id), **radio_props),
            ]
        if "title" not in offcanvas_props:
            offcanvas_props["title"] = "Select a Theme"
        if "is_open" not in offcanvas_props:
            offcanvas_props["is_open"] = False
        if "backdrop" not in offcanvas_props:
            offcanvas_props["backdrop"] = False
        if "style" not in offcanvas_props:
            offcanvas_props["style"] = {"width": 235}

        super().__init__(
            [
                dbc.Button(id=self.ids.button(aio_id), **button_props),
                dbc.Offcanvas(id=self.ids.offcanvas(aio_id), **offcanvas_props),
                html.Div(id=self.ids.dummy_div(aio_id)),
            ]
        )

    @callback(
        Output(ids.offcanvas(MATCH), "is_open"),
        Input(ids.button(MATCH), "n_clicks"),
        [State(ids.offcanvas(MATCH), "is_open")],
    )
    def toggle_theme_offcanvas(n1, is_open):
        if n1:
            return not is_open
        return is_open

    # Use 2 style sheet in the app to reduce the flicker when the theme changes
    # example:  app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.themes.CYBORG])
    clientside_callback(
        """
        function(url) {            
            var stylesheets = document.querySelectorAll('link[rel=stylesheet][href^="https://cdn.jsdelivr"]')                  
            stylesheets[stylesheets.length - 1].href = url           
        }
        """,
        Output(ids.dummy_div(MATCH), "children"),
        Input(ids.radio(MATCH), "value"),
    )

    # This callback is used to bundle custom CSS with the AIO component
    # The Input and Output can be any dummy property. The Input is used to trigger the
    # callback when the app starts. The clientside function adds the css to a <style>
    # element and appends it to the <head>.  Dash requires callbacks to have an Output
    # even if there is nothing to update.
    #
    clientside_callback(
        """
        function() {
            var style = document.createElement('style')
            const aio_css = `
              #theme-switch-label-dark {
              background-color: black;
              color: white;
              width: 100px
            }
            
            #theme-switch-label {
              background-color: white;
              color: black;
              width: 100px
            `
            
            style.innerText = aio_css            
            document.head.appendChild(style)
        }
        """,
        Output(ids.dummy_div(MATCH), "role"),
        Input(ids.dummy_div(MATCH), "role")
    )


# ----------  Slide Deck ------------------------------------------------------


class SlideDeckAIO(html.Div):
    # pattern matching callback ids
    class ids:
        pagination = lambda aio_id: {
            "component": "SlideDeckAIO",
            "subcomponent": "pagination",
            "aio_id": aio_id,
        }
        page_content = lambda aio_id: {
            "component": "SlideDeckAIO",
            "subcomponent": "page_content",
            "aio_id": aio_id,
        }
        store = lambda aio_id: {
            "component": "SlideDeckAIO",
            "subcomponent": "store",
            "aio_id": aio_id,
        }

    ids = ids

    # define properties of SlideDeckAIO
    def __init__(
        self, slide_deck={}, pagination_props={}, title=" ", aio_id=None,
    ):
        """
        SlideDeckAIO is an All-in-One component to display page content by page number. It is composed
        of a parent `html.Div` with a dbc.Pagination ('pagination'), html.Div for the page content (`page_content`)
        and a dcc.Store (`store`) for the slide deck dictionary.

        The pagination buttons control which page is displayed.

        - slide_deck:  A dictionary with the key as the page number and the page layout as the value {page_number: page_layout}
        - pagination_props:  A dictionary of properties passed into the dbc.Pagination component. See [](url)
        - title - optional text or components for the SlideDeck template
        - aio_id: The All-in-One component ID used to generate the pagination, content and store component's dictionary IDs.
        """

        # Set default props
        if aio_id is None:
            aio_id = str(uuid.uuid4())
        pagination_props = pagination_props.copy()
        if "fully_expanded" not in pagination_props:
            pagination_props["fully_expanded"] = False
        if "previous_next" not in pagination_props:
            pagination_props["previous_next"] = True
        if "active_page" not in pagination_props:
            pagination_props["active_page"] = 1
        if "size" not in pagination_props:
            pagination_props["size"] = "sm"

        # components used in the SlideDeckAIO layout
        pagination_btns = dbc.Pagination(
            id=self.ids.pagination(aio_id),
            max_value=len(slide_deck),
            **pagination_props,
        )
        slide_deck_controls = dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(title, className="text-white ms-2 h4"),
                        dbc.Col(
                            pagination_btns, width="auto", className="float-end pt-2"
                        ),
                    ],
                    align="center",
                )
            ],
            className="bg-primary text-white mb-4",
            fluid=True,
        )

        # layout
        super().__init__(
            [
                html.Div(slide_deck_controls),
                html.Div(  # slide deck output
                    slide_deck[pagination_props["active_page"]],
                    id=self.ids.page_content(aio_id),
                ),
                dcc.Store(id=self.ids.store(aio_id), data=slide_deck),
            ]
        )

    @callback(
        Output(ids.page_content(MATCH), "children"),
        Input(ids.pagination(MATCH), "active_page"),
        State(ids.store(MATCH), "data"),
    )
    def show_page(active_page, sl_deck):
        return sl_deck[str(active_page)]
