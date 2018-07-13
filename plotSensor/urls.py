from django.urls import re_path
from . import views

#startup the app
from . import dashapp

urlpatterns = [
    re_path('^_dash-', views.dash_ajax),
    re_path('^', views.dash_index),
]