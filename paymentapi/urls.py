"""
URL configuration for paymentapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os.path as osp
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve
from .settings import BASE_DIR
from home.views import TemplateView

SITE_ROOT = osp.join(BASE_DIR, 'site')

urlpatterns = [
    path("", TemplateView.as_view(template_name='home/main.html')),
    path("accounts/", include('django.contrib.auth.urls')),
    path("autos/", include('autos.urls')),
    path("admin/", admin.site.urls),
    path("hello/", include("hello.urls")),
    path("polls/", include("polls.urls")),
    path("forms/", include("forms.urls")),
    re_path(r'^site/(?P<path>.*)$', serve,
        {'document_root': SITE_ROOT, 'show_indexes': True},
        name='site_path'
    ),
]
