from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


from cats.models import Cat, Breed
from cats.forms import CatForm

# Create your views here.
class CatList(LoginRequiredMixin, View):
    template = 'cats/cat_list.html'
    def get(self, request):
        cl = Cat.objects.all()
        bc = Breed.objects.count()

        ctx = {'cat_list':cl, 'breed_count':bc}
        return render(request, self.template, ctx)

class CatCreate(LoginRequiredMixin, View):
    template = 'cats/cat_form.html'
    success_url = reverse_lazy('cats:cat_list')

    def get(self, request):
        form = CatForm()
        ctx = {'form':form}
        return render(request, self.template, ctx)

    def post(self, request):
        form = CatForm(request.POST)
        if not form.is_valid():
            ctx = {'form':form}
            return render(request, self.template, ctx)
        form.save()
        return redirect(self.success_url)

class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:cat_list')

class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:cat_list')

class BreedList(LoginRequiredMixin, View):
    template = 'cats/breed_list.html'
    def get(self, request):
        bl = Breed.objects.all()
        ctx = {'breed_list':bl}
        return render(request, self.template, ctx)

class BreedCreate(LoginRequiredMixin, CreateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:cat_list')

class BreedUpdate(LoginRequiredMixin, UpdateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:breed_list')

class BreedDelete(LoginRequiredMixin, DeleteView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:breed_list')
