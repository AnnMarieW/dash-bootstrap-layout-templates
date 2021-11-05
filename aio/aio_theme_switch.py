

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


class ThemeSwitchAIO(html.Div):
    class ids:
        switch = lambda aio_id: {
            "component": "ThemeSwitchAIO",
            "subcomponent": "switch",
            "aio_id": aio_id,
        }
        store = lambda aio_id: {
            "component": "ThemeSwitchAIO",
            "subcomponent": "store",
            "aio_id": aio_id,
        }
        dummy_div = lambda aio_id: {
            "component": "ThemeSwitchAIO",
            "subcomponent": "dummy_div",
            "aio_id": aio_id,
        }
    ids = ids

    def __init__(
        self,
        themes = [dbc.themes.BOOTSTRAP, dbc.themes.CYBORG],
        switch_props={},
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

        switch_props = switch_props.copy()
        # if "value" not in switch_props:
        #     switch_props["value"] = True

        super().__init__(
            [
                html.Div(
                    [
                        dbc.Label(className="fa fa-moon"),
                        dbc.Switch(value=True, id=self.ids.switch(aio_id), className="d-inline-block"),
                        dbc.Label(className="fa fa-sun"),
                    ],

                ),
                html.Div(id=self.ids.dummy_div(aio_id)),
                dcc.Store(id=self.ids.store(aio_id), data=themes),
            ]
        )

    clientside_callback(
        """
        function(theme_switch, url) {
            console.log('URL',url);
            const stylesheet = document.querySelector('link[rel=stylesheet][href^="https://cdn.jsdelivr"]')        
            var themeLink = theme_switch ? url[0] : url[1];
            stylesheet.href = themeLink
        }
        """,
        Output(ids.dummy_div(MATCH), "children"),
        Input(ids.switch(MATCH), "value"),
        Input(ids.store(MATCH), "data"),
    )
