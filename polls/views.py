from django.http import HttpResponse, HttpResponseRedirect
from django.views import View, generic
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Question, Choice


# Create your views here.
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions"""
        return Question.objects.order_by("-question_text")[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

def owner(request):
    return HttpResponse("Hello, world. 9fed52a6 is the polls index.")

def cookie(request):
    resp = HttpResponse("C is for cookie and that is good enough for me")
    resp.set_cookie("zap", 42)
    resp.set_cookie("sakaicar", 42, max_age=1000)
    return resp

# Use Class based views here.
class QuestionView(View):
    def get(self, request, guess):
        x = { 'num' : int(guess) }
        return render(request, "polls/main.html", x)