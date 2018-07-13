# django_dash_rabbitMQ

This app uses [Plotly Dash](https://plot.ly/products/dash/) and Django to plot sensor data (simulated with random data in this project).

Using a drop down box multiple (up to 5) sensor plots can be shown in the browser.

![Dash Plots Gif](https://github.com/pbybee/django_dash_rabbitMQ/blob/master/sensorVizExample.gif)

KNOWN ISSUES:
Removing the sensors in any order other than the order you added causes dash to fail. This seems to be a known Dash Issue.

Future steps will be to use RabbitMQ to handle passing sensor data to get more familiar with message brokers and distributed systems.



Props to the people who figured out how to integrate Dash into Django. I found the example here:
https://github.com/ned2/dash-django-example
