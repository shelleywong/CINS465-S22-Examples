from django.urls import path

from . import views

urlpatterns = [
    # path(route='', view='')
    path('', views.index),
]