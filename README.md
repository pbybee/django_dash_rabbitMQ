# django_dash_rabbitMQ

This app uses [Plotly Dash](https://plot.ly/products/dash/) and Django to plot sensor data (simulated with random data in this project).

Using a drop down box multiple (up to 5) sensor plots can be shown in the browser.

![Dash Plots Gif](https://github.com/pbybee/django_dash_rabbitMQ/blob/master/sensorVizExample.gif)

KNOWN ISSUES:
Removing the sensors in any order other than the order you added causes dash to fail. This seems to be a known Dash Issue.

TO DO:
1. Make a require file for easy environment setup
2. Add a Postgresql database to store sensor data
3. Use RabbitMQ to handle passing sensor data
4. Try performing some manipulations to the sensor data or add another app to do computational work
5. Add Celery to handle multiple users doing multiple task requests



Props to the people who figured out how to integrate Dash into Django. I found the example here:
https://github.com/ned2/dash-django-example
