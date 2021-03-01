from django.shortcuts import render, redirect, get_object_or_404
from .forms import TopicForm
from .models import Topics
from django.http import HttpResponse
from .models import Question


def home(request):  # Renders home page
    return render(request, 'IntroPage.html')


def topic(request):  # Checks the validity of the form and saves if valid, otherwise it renders the topic page
    form = TopicForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('survey')
    context = {'form': form}
    return render(request, 'TopicPage.html', context)


def survey(request):  # renders survey page
    return render(request, 'Survey.html')


def team(request):  # renders team page
    return render(request, 'Team.html')


def index(request):  # renders a list of all questions in the database on index page
    question_list = Question.objects.all()
    context = {'question_list': question_list}
    return render(request, 'index.html', context)


def detail(request, question_id):  # renders detail page with selected question object from database
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'detail.html', {'question': question})


def results(request, question_id):  # returns http response for the results
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):  # returns http response for the vote information
    return HttpResponse("You're voting on question %s." % question_id)

def video(request):  # renders video page
    return render(request, 'Video.html')
