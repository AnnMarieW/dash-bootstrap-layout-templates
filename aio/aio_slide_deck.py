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
