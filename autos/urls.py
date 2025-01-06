from django.urls import path
from autos import views

app_name = 'autos'
urlpatterns = [path('', views.MainView.as_view(), name="main_view"),
               path('makes/', views.MakeView.as_view(), name='make_list'),
               path('makes/create/', views.MakeCreate.as_view(), name='make_create'),
               path('makes/<int:pk>/update/', views.MakeUpdate.as_view(), name='make_update'),
               path('makes/<int:pk>/delete/', views.MakeDelete.as_view(), name='make_delete'),
               path('autos/create/', views.AutoCreate.as_view(), name='auto_create'),
               path('autos/<int:pk>/update/', views.AutoUpdate.as_view(), name='auto_update'),
               path('autos/<int:pk>/delete/', views.AutoDelete.as_view(), name='auto_delete'),
               ]