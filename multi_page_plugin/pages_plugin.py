from dash import callback, Output, Input, html, dcc
import dash
import os
import importlib
from collections import OrderedDict

if not os.path.exists('pages'):
    raise Exception('A folder called `pages` does not exist.')

_ID_CONTENT = '_pages_plugin_content'
_ID_LOCATION = '_pages_plugin_location'

page_container = html.Div([
    dcc.Location(id=_ID_LOCATION),
    html.Div(id=_ID_CONTENT),
])


def register_page(
        module,
        path=None,
        name=None,
        title=None,
        description=None,
        description_image=None,
        order=None,
        layout=None,
        **kwargs
):
    """
    Assigns the variables to `dash.page_registry` as an `OrderedDict`
    (ordered by `order`).

    `dash.page_registry` is used by `pages_plugin` to set up the layouts as
    a multi-page Dash app. This includes the URL routing callbacks
    (using `dcc.Location`) and the HTML templates to include title,
    meta description, and the meta description image.

    `dash.page_registry` can also be used by Dash developers to create the
    page navigation links or by template authors.

    module:
        The module path where this page's `layout` is defined. Often `__name__`.

    path:
        URL Path, e.g. `/` or `/home-page`.
        If not supplied, will be inferred by module,
        e.g. `pages.weekly_analytics` to `/weekly-analytics`

    name:
        The name of the link.
        If not supplied, will be inferred by module,
        e.g. `pages.weekly_analytics` to `Weekly analytics`

    title:
        The name of the page <title>. That is, what appears in the browser title.
        If not supplied, will use the supplied `name` or will be inferred by module,
        e.g. `pages.weekly_analytics` to `Weekly analytics`

    description:
        The <meta type="description"></meta>.
        If not supplied, then nothing is supplied.

    description_image:
        The meta description image used by social media platforms.
        If not supplied, then it looks for the following images in `assets/`:
        - A page specific image: `assets/<title>.png` is used, e.g. `assets/weekly_analytics.png`
        - A generic app image at `assets/meta-description-image.png`
        - A logo at `assets/logo.png`

    order:
        The order of the pages in `page_registry`.
        If not supplied, then the filename is used and the page with path `/` has
        order `0`

    layout:
        The layout function or component for this page.
        If not supplied, then looks for `layout` from within the supplied `module`.

    **kwargs:
        Arbitrary keyword arguments

    ***

    `page_registry` stores the original property that was passed in under
    `supplied_<property>` and the coerced property under `<property>`.
    For example, if this was called:
    ```
    register_page(
        'pages.historical_outlook',
        name='Our historical view',
        custom_key='custom value'
    )
    ```
    Then this will appear in `page_registry`:
    ```
    OrderedDict([
        (
            'pages.historical_outlook',
            dict(
                module='pages.historical_outlook',

                supplied_path=None,
                path='/historical-outlook',

                supplied_name='Our historical view',
                name='Our historical view',

                supplied_title=None,
                title='Our historical view'

                supplied_description=None,
                description='Our historical view',

                supplied_order=None,
                order=1,

                supplied_layout=None,
                layout=<function pages.historical_outlook.layout>,

                custom_key='custom value'
            )
        ),
    ])
    ```

    """
    # COERCE
    # - Set the order
    # - Inferred paths
    page = dict(
        module=module,

        supplied_path=path,
        path=(path if path is not None else _filename_to_path(module)),

        supplied_name=name,
        name=(name if name is not None else _filename_to_name(module)),
    )
    page.update(
        supplied_title=title,
        title=(title if title is not None else page['name']),
    )
    page.update(
        supplied_description=description,
        description=(description if description is not None else page['title']),

        supplied_order=order,

        supplied_layout=layout,
        **kwargs
    )

    dash.page_registry[module] = page

    if layout is not None:
        # Override the layout found in the file set during `plug`
        dash.page_registry[module]['layout'] = layout

    # Reset order
    order = []
    for page_module in dash.page_registry:
        if page['supplied_path'] == '/':
            order.append((0, page_module))
            page['order'] = 0

    page_registry_list = sorted(
        dash.page_registry.values(),
        key=lambda i: str(i.get('order', i['module']))
    )
    dash.page_registry = OrderedDict([
        (p['module'], p) for p in page_registry_list
    ])


dash.register_page = register_page


def _filename_to_name(filename):
    return filename.split('.')[-1].replace('_', ' ').capitalize()


def _filename_to_path(filename):
    return '/' + filename.split('.')[-1].replace('_', '-').lower()


def plug(app):
    # Import the pages so that the user doesn't have to.
    # TODO - Do validate_layout in here too
    dash.page_registry = OrderedDict()

    for page_filename in os.listdir('pages'):
        if page_filename.startswith('_') or not page_filename.endswith('.py'):
            continue
        page_filename = page_filename.replace('.py', '')
        page_module = importlib.import_module(f'pages.{page_filename}')

        if f'pages.{page_filename}' in dash.page_registry:
            dash.page_registry[f'pages.{page_filename}']['layout'] = getattr(page_module, 'layout')

    @app.server.before_first_request
    def router():

        for page_module in dash.page_registry:
            page = dash.page_registry[page_module]

            if 'supplied_layout' in page:
                layout = page['supplied_layout']
            else:
                layout = importlib.import_module(f'pages.{page_filename}').layout

        @callback(
            Output(_ID_CONTENT, 'children'),
            Input(_ID_LOCATION, 'pathname'),
            prevent_initial_call=True
        )
        def update(pathname):
            path_id = app.strip_relative_path(pathname)
            layout = None
            for module in dash.page_registry:
                page = dash.page_registry[module]
                if path_id == app.strip_relative_path(page['path']):
                    layout = page['layout']

            if layout is None:
                layout = dash.page_registry.get('pages.not_found_404', html.H1('404'))

            if callable(layout):
                return layout()
            else:
                return layout