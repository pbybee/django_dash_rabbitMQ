from .server import app, server
from . import layouts
from dash.dependencies import Output, Input


pages = (
    ('', layouts.index),
    ('fig1', layouts.fig1),
)

routes = {"{}{}".format(app.url_base_pathname, path): layout for path, layout in pages}

@app.callback(Output('content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    ''' '''
    if pathname is None:
        return ''

    page = routes.get(pathname, 'Unknown link')

    if callable(page):
        # can add arguments to layout functions if needed
        layout = page()
    else:
        layout = page

    return layout



