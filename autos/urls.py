from django.urls import path
from autos import views

app_name = 'autos'
urlpatterns = [path('', views.MainView.as_view(), name='all'),]