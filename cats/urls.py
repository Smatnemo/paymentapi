from django.urls import path
from cats import views

app_name = 'cats'
urlpatterns = [path('', views.CatList.as_view(), name='cat_list'),
               path('main/create/', views.CatCreate.as_view(), name='cat_create'),
               path('main/<int:pk>/update/', views.CatUpdate.as_view(), name='cat_update'),
               path('main/<int:pk>/delete/', views.CatDelete.as_view(), name='cat_delete'),
               path('breeds/', views.BreedList.as_view(), name='breed_list'),
               path('breed/create/', views.BreedCreate.as_view(), name='create_breed'),
               path('breed/<int:pk>/update/', views.BreedUpdate.as_view(), name='update_breed'),
               path('breed/<int:pk>/delete/', views.BreedDelete.as_view(), name='delete_breed')]