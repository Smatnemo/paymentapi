from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView


class OwnerListView(LoginRequiredMixin, ListView):
    """"""

class OwnerDetailView(LoginRequiredMixin, DetailView):
    """"""

class OwnerCreateView(LoginRequiredMixin, CreateView):
    """"""
    def form_valid(self, form):
        object = form.save(commit=False)
        print(type(object))
        object.owner = self.request.user
        object.save()
        return super(OwnerCreateView, self).form_valid(form)

class OwnerUpdateView(LoginRequiredMixin, UpdateView):
    """
    Sub-class the UpdateView to pass the request to the form and limit the
    queryset to the requesting user.
    """
    def get_queryset(self):
        qs = super(OwnerUpdateView, self).get_queryset()
        return qs.filter(owner=self.request.user)

class OwnerDeleteView(LoginRequiredMixin, DeleteView):
    """"""
    def get_queryset(self):
        qs = super(OwnerDeleteView, self).get_queryset()
        return qs.filter(owner=self.request.user)