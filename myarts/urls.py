from django.urls import path
from myarts import views

app_name='myarts'
urlpatterns = [
    path('', views.ArticleListView.as_view(), name='main_view'),
    path('article/<int:pk>', views.ArticleDetailView.as_view(), name='article_details'),
    path('article/create', views.ArticleCreateView.as_view(), name='create_article'),
    path('article/<int:pk>/update', views.ArticleUpdateView.as_view(), name='update_article'),
    path('article/<int:pk/delete', views.ArticleDeleteView.as_view(), name='delete_article'),
    ]