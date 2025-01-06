from django import forms
from cats.models import Cat

class CatForm(forms.ModelForm):
    class Meta:
        model = Cat
        fields = '__all__'