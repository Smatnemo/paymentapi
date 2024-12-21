from django.urls import path
from .views import Validate, success

urlpatterns = [
        path('validate/', Validate.as_view(), name='validate'),
        path('form/success/', success, name='success'),
    ]