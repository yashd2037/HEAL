from django.shortcuts import render, redirect, get_object_or_404
from .forms import TopicForm, QuestionForm
from django.http import HttpResponse
from .models import Topics, Question


def home(request):  # Renders home page
    return render(request, 'IntroPage.html')


def topic(request):  # Checks the validity of the form and saves if valid, otherwise it renders the topic page
    form = TopicForm(request.POST or None)
    question = Question.objects.get(id=1)  # Gets question at id 1, temporary solution
    if form.is_valid():  # Checks is form received proper input
        form.save()
        return render(request, 'Survey.html', {'question': question})  # Renders survey with current question
    return render(request, 'TopicPage.html', {'form': form})  # Re-renders the current page


def team(request):  # renders team page
    return render(request, 'Team.html')


def index(request):  # renders a list of all questions in the database on index page
    question_list = Question.objects.all()
    context = {'question_list': question_list}
    return render(request, 'index.html', context)


def survey(request, question_id):  # renders initial survey page with selected question object from database
    baseQuestion = Question.objects.get(id=question_id)  # Gets the question at the current id
    if request.method == 'POST':
        question = Question.objects.get(id=baseQuestion.NextIDA)  # Gets the question at the next A branch ID
        return render(request, 'Survey.html', {'question': question})
    question = baseQuestion
    return render(request, 'Survey.html', {'question': question})


def video(request):  # renders video page
    return render(request, 'Video.html')
