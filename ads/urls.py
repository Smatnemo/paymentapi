from django.urls import path
from ads import views

app_name='ads'
urlpatterns = [path('', views.AdListView.as_view(), name='all'),
               path('ad/<int:pk>', views.AdDetailView.as_view(), name='ad_detail'),
               path('ad/create', views.AdCreateView.as_view(), name='create_ad'),
               path('ad/<int:pk>/update', views.AdUpdateView.as_view(), name='update_ad'),
               path('ad/<int:pk>/delete', views.AdDeleteView.as_view(), name='delete_ad'),
               path('ad/ad_picture/<int:pk>', views.stream_file, name='ad_picture'),
               path('ad/<int:pk>/comment', views.CommentCreateView.as_view(), name='create_ad_comment'),
               path('comment/<int:pk>/delete', views.CommentDeleteView.as_view(), name='delete_ad_comment'),
               path('ad/<int:pk>/favorite', views.AddFavoriteView.as_view(), name="ad_favorite"),
               path('ad/<int:pk>/unfavorite', views.DeleteFavoriteView.as_view(), name='ad_unfavorite'),
            ]