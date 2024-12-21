from . import views
from django.urls import path



urlpatterns = [
    path('', views.myView, name='hello_world'),
]
