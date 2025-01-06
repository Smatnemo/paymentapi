from django.urls import reverse_lazy
from myarts.models import Article
from myarts.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView


# Create your views here.
class ArticleListView(OwnerListView):
    model = Article

class ArticleDetailView(OwnerDetailView):
    model = Article

class ArticleCreateView(OwnerCreateView):
    model = Article
    fields = ['title', 'text']
    success_url = reverse_lazy('myarts:main_view')

class ArticleUpdateView(OwnerUpdateView):
    model = Article
    fields = ['title', 'text']
    success_url = reverse_lazy('myarts:main_view')

class ArticleDeleteView(OwnerDeleteView):
    model = Article
    success_url = reverse_lazy('myarts:main_view')