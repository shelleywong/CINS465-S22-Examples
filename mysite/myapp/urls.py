from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    # path(route='', view='')
    path('', views.index, name="index"),
    path('<int:page>/', views.index, name="index"),
    path('questions/', views.questions, name="questions"),
    path('likes/', views.likes, name="likes"),
    path('login/', auth_views.LoginView.as_view()),
    path('register/', views.register, name="register"),
]