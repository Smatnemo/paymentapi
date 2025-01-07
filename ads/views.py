from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q
from django.views import View
from django.contrib.humanize.templatetags.humanize import naturaltime

from ads.owner import LoginRequiredMixin, OwnerListView, OwnerDetailView, OwnerDeleteView
from ads.models import Ad, Comment, Fav

from ads.forms import CreateForm, CommentForm

# Create your views here.
class AdListView(OwnerListView):
    model = Ad
    template_name = 'ads/ad_list.html'

    def get(self, request):
        ad_list = Ad.objects.all().order_by('-updated_at')[:10]
        favorites = list()
        # For search
        strval = request.GET.get("search", False)
        if strval:
            # Simple title-only search
            # __icontains for case-insensitive search
            query = Q(title__icontains=strval)
            query.add(Q(text__icontains=strval), Q.OR)
            query.add(Q(tags__name__in=[strval]), Q.OR)

            ad_list = Ad.objects.filter(query).select_related().distinct().order_by('-updated_at')[:10]

        # Augment the ad_list
        for obj in ad_list:
            obj.natural_updated = naturaltime(obj.updated_at)

        if request.user.is_authenticated:
            # Return a list(QuerySet) of dictionaries showing all the ads that the current user likes
            # rows = [{'ad_id':1},{'ad_id':2}]
            rows = request.user.favorite_ads.values('id')
            # Convert from a querySet to an actual list of only ids
            # favorites = [1, 2]
            favorites = [row['id'] for row in rows]
        ctx = {'ad_list':ad_list, 'favorites': favorites, 'search':strval }
        return render(request, self.template_name, ctx)

class AdDetailView(OwnerDetailView):
    model = Ad
    template_name = 'ads/ad_detail.html'

    def get(self, request, pk):
        # inherited method retrieves the ad with pk
        x = get_object_or_404(Ad, id=pk)
        # Use ad to filter comments related to current ad
        comments = Comment.objects.filter(ad=x).order_by('-updated_at')
        comment_form = CommentForm()
        context = {'ad':x, 'comments': comments, 'comment_form': comment_form}
        return render(request, self.template_name, context)

class AdCreateView(LoginRequiredMixin, View):
    template_name = 'ads/ad_form.html'
    success_url = reverse_lazy('ads:all')

    def get(self, request, pk=None):
        form = CreateForm()
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        form = CreateForm(request.POST, request.FILES or None)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        # Add owner to the model before saving
        ad = form.save(commit=False)
        ad.owner = self.request.user
        ad.save()

        # https://django-taggit.readthedocs.io/en/latest/forms.html#commit-false
        form.save_m2m()

        return redirect(self.success_url)

class AdUpdateView(LoginRequiredMixin, View):
    template_name = 'ads/ad_form.html'
    success_url = reverse_lazy('ads:all')

    def get(self, request, pk):
        ad = get_object_or_404(Ad, id=pk, owner=self.request.user)
        form = CreateForm(instance=ad)
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk):
        ad = get_object_or_404(Ad, id=pk, owner=self.request.user)
        form = CreateForm(request.POST, request.FILES or None, instance=ad)

        if not form.is_valid():
            ctx = {'form':form}
            return render(request, self.template_name, ctx)

        ad = form.save(commit=False)
        ad.save()

        return redirect(self.success_url)

class AdDeleteView(OwnerDeleteView):
    model = Ad
    success_url = reverse_lazy('ads:all')

class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, pk):
        a = get_object_or_404(Ad, id=pk)
        comment = Comment(text=request.POST['comment'], owner=request.user, ad=a)
        comment.save()
        return redirect(reverse('ads:ad_detail', args=[pk]))

class CommentDeleteView(OwnerDeleteView):
    model = Comment

    def get_success_url(self):
        ad = self.object.ad
        return reverse('ads:ad_detail', args=[ad.id])

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db.utils import IntegrityError

# Views for adding and removing favorites
@method_decorator(csrf_exempt, name="dispatch")
class AddFavoriteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        print("Add PK", pk)
        a = get_object_or_404(Ad, id=pk)
        fav = Fav(user=request.user, ad=a)
        try:
            fav.save()
        except IntegrityError:
            # Because (ad, user) have a unique combination,
            # integrity error will occur when you try to add
            # a second record to Fav which already exists before
            pass
        return HttpResponse()

@method_decorator(csrf_exempt, name="dispatch")
class DeleteFavoriteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        print("Delete PK", pk)
        a = get_object_or_404(Ad, id=pk)
        try:
            Fav.objects.get(user=request.user, ad=a).delete()
        except Fav.DoesNotExist:
            pass
        return HttpResponse()

def stream_file(request, pk):
    ad = get_object_or_404(Ad, id=pk)
    response = HttpResponse()
    response['Content-Type'] = ad.content_type
    response['Content-Length'] = len(ad.picture)
    response.write(ad.picture)
    return response