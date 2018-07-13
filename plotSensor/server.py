from flask import Flask
from dash import Dash


# should start and end with a '/'
URL_BASE_PATHNAME = '/plot/'

server = Flask(__name__)

app = Dash(
    server=server,
    url_base_pathname=URL_BASE_PATHNAME,
    csrf_protect=False,
)

app.config['suppress_callback_exceptions'] = True



