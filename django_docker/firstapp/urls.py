from django.urls import path
from . import views

urlpatterns = [
    # create a path object that defines the URL pattern to the index view
    path(route='', view=views.index, name='index'),
    # create a path object that defines the URL using '\date' prefix
    path(route='date', view=views.get_date, name='date'),
]

