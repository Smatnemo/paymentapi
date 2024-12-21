from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .forms import BasicForm

# Create your views here.
class Validate(View):
    def get(self, request):
        old_data = {
            'title': 'SakaiCar',
            'mileage': 42,
            'purchase_date': '2024-12-18'
            }
        form = BasicForm(initial=old_data)
        ctx = {'form': form}
        return render(request, 'form/form.html', ctx)

    def post(self, request):
        form = BasicForm(request.POST)
        if not form.is_valid():
            ctx = {'form' : form}
            return render(request, 'form/form.html', ctx)
        # save the Data
        return redirect('/form/success')

def success(request):
    return HttpResponse('Thank you!')