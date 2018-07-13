import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input, Event
from plotly import graph_objs as go
from .server import app

#need to import router here
#It seems like a weakness that in order for Django Dash integration to work, import statements need to be called. Could probably be done differently
from . import router
from .sensor import Sensor

#startup the sensors
sensors = [Sensor(float('0.'+str(x+1))) for x in range(5)]


app.layout = html.Div(children=[
    dcc.Location(id='url', refresh=False),
    dcc.Link('Index', href='/'),
    ', ',
    dcc.Link('Figure 1', href='{}fig1'.format(app.url_base_pathname)),
    ', ',
    html.Br(),
    html.Br(),
    html.Div(id='content')
])

@app.callback(Output('graphs', 'children'),
              [Input('sensor-dropdown', 'value')],
              events=[Event('sensor-interval', 'interval')])
def graphLayout(sensorList):

    graphs = []
    datas = []
    red = 0
    blue = 0
    green = 0
    if sensorList is None:
        sensorList = ['0']
    for sensor in sensorList:
        sensorNum = int(sensor)
        if (sensorNum == 1):
            red = 255
        elif (sensorNum == 2):
            red = 0
            blue = 255
        elif (sensorNum == 3):
            red = 0
            blue = 0
            green = 255
        elif (sensorNum == 4):
            red = 80
            blue = 0
            green = 80
        xVals =  sensors[sensorNum].getSensorValues()['x']
        yVals = sensors[sensorNum].getSensorValues()['y']
        data=go.Scatter(
            x=xVals,
            y=yVals,
            mode='line',
            line=go.Line(color='rgb({}, {}, {})'.format(red,blue,green))
        )
        # datas.append(data)
        graphs.append(html.Div(dcc.Graph(
                id=sensor,
                animate=True,
                figure={
                    'data': [data],
                    'layout': go.Layout(xaxis=dict(range=[min(xVals), max(xVals)]),
                                        yaxis=dict(range=[0, 10]),
                                        title='Sensor'+sensor)
                }
            )
        )
    )
    return graphs