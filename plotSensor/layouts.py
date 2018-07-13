import dash_core_components as dcc
import dash_html_components as html


def index():
    ''' '''
    return 'Welcome to index page'


def fig1():
    ''' '''
    return html.Div([
        html.Div([html.H2('Select a number of sensors from the dropdown')]),
        dcc.Dropdown(
            id='sensor-dropdown',
            options=[{'label': 'sensor '+str(x) , 'value': str(x)}
                     for x in range(5)],
            value=['0',],
            multi=True
        ),
        html.Br(),
        html.Div(children=html.Div(id='graphs'), className='row'),
        dcc.Interval(
                id='sensor-interval',
                interval=1000
            ),
    ], className='container')
