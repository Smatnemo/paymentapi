from django.contrib import admin
from .models import Question, Choice

# Create your models here.
admin.site.register(Question)
admin.site.register(Choice)