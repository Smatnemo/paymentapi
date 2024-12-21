from django import forms
from django.core import validators

class BasicForm(forms.Form):
    title = forms.CharField(validators=[
        validators.MinLengthValidator(2, "Please enter 2 or more characters")
        ])
    mileage = forms.IntegerField()
    purchase_date = forms.DateField()