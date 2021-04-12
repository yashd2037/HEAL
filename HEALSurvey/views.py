from django.shortcuts import render, redirect, get_object_or_404
from .forms import TopicForm, ChoiceForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.views import generic
from .models import Topics, Question, Choice, Post


def home(request):  # Renders home page
    return render(request, 'IntroPage.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'Login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'Register.html', {'form': form})


def topic(request):  # Checks the validity of the form and saves if valid, otherwise it renders the topic page
    form = TopicForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():  # Checks if form received is proper input
            #  form.save()  #this may only be needed after user login is implemented
            firstTopic = request.POST.get('topic')  # Gets submitted topic 1
            secondTopic = request.POST.get('topic2')  # Gets submitted topic 2
            if (firstTopic == 'Housing' and secondTopic == 'Transportation') or (
                    secondTopic == 'Housing' and firstTopic == 'Transportation'):  # Checks which topics were selected
                question = Question.objects.get(id=201)  # Gets question at specified id
            elif (firstTopic == 'Housing' and secondTopic == 'Healthcare') or (
                    secondTopic == 'Housing' and firstTopic == 'Healthcare'):
                question = Question.objects.get(id=301)
            elif (firstTopic == 'Healthy Food' and secondTopic == 'Healthcare') or (
                    secondTopic == 'Healthy Food' and firstTopic == 'Healthcare'):
                question = Question.objects.get(id=401)
            elif (firstTopic == 'Transportation' and secondTopic == 'Healthcare') or (
                    secondTopic == 'Transportation' and firstTopic == 'Healthcare'):
                question = Question.objects.get(id=501)
            elif (firstTopic == 'Employment' and secondTopic == 'Healthcare') or (
                    secondTopic == 'Employment' and firstTopic == 'Healthcare'):
                question = Question.objects.get(id=601)
            elif (firstTopic == 'Employment' and secondTopic == 'Housing') or (
                    secondTopic == 'Employment' and firstTopic == 'Housing'):
                question = Question.objects.get(id=701)
            elif (firstTopic == 'Employment' and secondTopic == 'Transportation') or (
                    secondTopic == 'Employment' and firstTopic == 'Transportation'):
                question = Question.objects.get(id=801)
            elif ((firstTopic == 'Healthy Food' and secondTopic == 'Housing') or (
                    secondTopic == 'Healthy Food' and firstTopic == 'Housing')) or (
                    (firstTopic == 'Healthy Food' and secondTopic == 'Transportation') or (
                        secondTopic == 'Healthy Food' and firstTopic == 'Transportation')):
                question = Question.objects.get(id=101)  # Gets question at id 101, temporary solution for invalid input
            else:
                return render(request, 'TopicPage.html', {'form': form})  # Re-renders the current page

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
        if 'choice' in request.POST:  # Checks if there is a choice in the current request
            response = (baseQuestion.choice_set.get(pk=request.POST['choice'])).choice_text  # sets choices text to var
        elif (baseQuestion.choice_set.exists()) and ('choice' not in request.POST):  # Checks choices exist on page
            response = None  # Sets var to null
        else:
            question = Question.objects.get(id=baseQuestion.NextIDA)  # Goes to the next page if no choices
            return render(request, 'Survey.html', {'question': question})  # renders page

        if (response == 'Yes') or (response == 'Agree') or (response == 'Strongly Agree') or (
                response == 'Familiar') or (response == 'Very familiar') or (response == 'True'):
            question = Question.objects.get(id=baseQuestion.NextIDB)  # Gets the question at the next positive branch ID
        elif (response == 'No') or (response == 'Disagree') or (response == 'Strongly Disagree') or (
                response == 'Somewhat') or (response == 'Not at all') or (response == 'False'):
            question = Question.objects.get(id=baseQuestion.NextIDA)  # Gets the question at the next negative branch ID
        else:
            question = baseQuestion  # Gets base question

        return render(request, 'Survey.html', {'question': question})  # Renders page with set question
    question = baseQuestion  # Gets base question
    return render(request, 'Survey.html', {'question': question})  # Renders page with set question


def video(request):  # renders video page
    return render(request, 'Video.html')

def info(request): # renders info page
    return render(request, 'info.html')

def results(request): # renders info page
    return render(request, 'Results.html')

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'