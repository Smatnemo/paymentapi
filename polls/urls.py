from django.urls import path
from . import views

# Used to set the application namespace
app_name = 'polls'
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("owner/", views.owner, name="owner"),
    path("cookie/", views.cookie, name="cookie"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("main/<slug:guess>/", views.QuestionView.as_view(), name="question")
]