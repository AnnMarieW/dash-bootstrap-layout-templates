
"""
Alternate method of registering pages.
All pages registered here and imported into app.py

"""
import dash
from dash_labs import dashdown

# ----------------- Register homepage  md  ---------------------------
dash.register_page("home", path="/", layout=dashdown("pages/home.md"))

# ----------------- Register dashdown  md  ---------------------------
dash.register_page(
    "dashdown-overview",
    name="Overview",
    order=0,
    layout=dashdown(
        "pages/dashdown/overview.md",
        side_by_side=True,
    ),
)

dash.register_page(
    "dashdown-reference",
    name="Reference",
    order=1,
    layout=dashdown(
        "pages/dashdown/reference.md",
        exec_code=False,
    ),
)

dash.register_page(
    "dashdown-display_options",
    name="Display Options",
    order=2,
    layout=dashdown(
        "pages/dashdown/display_options.md",
    ),
)

#
# dash.register_page(
#     "dashdown-README",
#     name="README.md",
#     order=3,
#     layout=dashdown(
#         "pages/dashdown/README.md",
#         scope={"app": app},
#         side_by_side=True,
#     ),
#)

# ----------------- Register Multi-page md  ---------------------------

dash.register_page(
    "Multi-Page-Overview",
    name="Overview",
    order=1,
    layout=dashdown(
        "pages/multi_page_apps/overview.md",
        exec_code=False,
    ),
)


dash.register_page(
    "Multi-Page-Reference",
    name="Reference",
    order=1,
    layout=dashdown(
        "pages/multi_page_apps/reference.md",
        exec_code=False,
    ),
)


dash.register_page(
    "Multi-Page-Nested-Folders",
    name="Nested Folders",
    order=2,
    layout=dashdown(
        "pages/multi_page_apps/nested_folders.md",
        exec_code=False,
        #  code_card_style={"margin": "25px 50px"}
    ),
)


dash.register_page(
    "Multi-Page-Meta-Tags",
    name="Meta Tags",
    order=3,
    layout=dashdown(
        "pages/multi_page_apps/meta_tags.md",
        exec_code=False,
        #  code_card_style={"margin": "25px 50px"}
    ),
)


dash.register_page(
    "Multi-Page-Layout-Functions",
    name="Sub Menus",
    order=4,
    layout=dashdown(
        "pages/multi_page_apps/sub_menus.md",
        exec_code=False,
        #   code_card_style={"margin": "25px 50px"}
    ),
)
