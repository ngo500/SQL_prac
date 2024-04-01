from django.urls import path
from . import views

url patterns = [
    # create a path object that defines the URL pattern to the index view
    path(route='', view=views.index, name='index'),
]
