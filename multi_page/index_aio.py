from app import app
from apps import app1, app2
from aio.aio_components import MultiPageAIO

app.layout = MultiPageAIO(layouts={"/apps/app1": app1.layout, "/apps/app2": app2.layout, "/": app1.layout})


if __name__ == "__main__":
    app.run_server(debug=True)
