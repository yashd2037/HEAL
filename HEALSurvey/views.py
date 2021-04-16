from django.shortcuts import render, redirect, get_object_or_404
from .forms import TopicForm, ChoiceForm, UserChoicesForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.views import generic
from .models import Topics, Question, Choice, SummaryStatement, UserChoices, City, CityData, ZipCode, Post


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
    uform = UserChoicesForm(request.POST or None)
    if UserChoices.objects.filter(username=request.user).exists():
        UserChoices.objects.filter(username=request.user).delete()

    if request.method == 'POST':
            firstTopic = request.POST.get('topic')  # Gets submitted topic 1
            secondTopic = request.POST.get('topic2')  # Gets submitted topic 2
            if (firstTopic == 'Housing' and secondTopic == 'Transportation') or (
                    secondTopic == 'Housing' and firstTopic == 'Transportation'):  # Checks which topics were selected
                question = Question.objects.get(id=201)  # Gets question at specified id
                UserChoices.objects.create(username=request.user, u_choice='2').save
            elif (firstTopic == 'Housing' and secondTopic == 'Healthcare') or (
                    secondTopic == 'Housing' and firstTopic == 'Healthcare'):
                question = Question.objects.get(id=301)
                UserChoices.objects.create(username=request.user, u_choice='3').save
            elif (firstTopic == 'Healthy Food' and secondTopic == 'Healthcare') or (
                    secondTopic == 'Healthy Food' and firstTopic == 'Healthcare'):
                question = Question.objects.get(id=401)
                UserChoices.objects.create(username=request.user, u_choice='4').save
            elif (firstTopic == 'Transportation' and secondTopic == 'Healthcare') or (
                    secondTopic == 'Transportation' and firstTopic == 'Healthcare'):
                question = Question.objects.get(id=501)
                UserChoices.objects.create(username=request.user, u_choice='5').save
            elif (firstTopic == 'Employment' and secondTopic == 'Healthcare') or (
                    secondTopic == 'Employment' and firstTopic == 'Healthcare'):
                question = Question.objects.get(id=601)
                UserChoices.objects.create(username=request.user, u_choice='6').save
            elif (firstTopic == 'Employment' and secondTopic == 'Housing') or (
                    secondTopic == 'Employment' and firstTopic == 'Housing'):
                question = Question.objects.get(id=701)
                UserChoices.objects.create(username=request.user, u_choice='7').save
            elif (firstTopic == 'Employment' and secondTopic == 'Transportation') or (
                    secondTopic == 'Employment' and firstTopic == 'Transportation'):
                question = Question.objects.get(id=801)
                UserChoices.objects.create(username=request.user, u_choice='8').save
            elif ((firstTopic == 'Healthy Food' and secondTopic == 'Housing') or (
                    secondTopic == 'Healthy Food' and firstTopic == 'Housing')) or (
                    (firstTopic == 'Healthy Food' and secondTopic == 'Transportation') or (
                        secondTopic == 'Healthy Food' and firstTopic == 'Transportation')):
                question = Question.objects.get(id=101)  # Gets question at id 101, temporary solution for invalid input
                UserChoices.objects.create(username=request.user, u_choice='1').save
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
    base_question = Question.objects.get(id=question_id)  # Gets the question at the current id
    upchoice = UserChoices.objects.get(username=request.user).u_choice
    if request.method == 'POST':
        if base_question.NextIDA == 1:
            return redirect('results')

        if 'choice' in request.POST:  # Checks if there is a choice in the current request
            response = (base_question.choice_set.get(pk=request.POST['choice'])).choice_text  # sets choices text to var
        elif (base_question.choice_set.exists()) and ('choice' not in request.POST):  # Checks choices exist on page
            response = None  # Sets var to null
        else:
            question = Question.objects.get(id=base_question.NextIDA)  # Goes to the next page if no choices
            upchoice = upchoice + 'C'
            UserChoices.objects.filter(username=request.user).update(u_choice=upchoice)
            return render(request, 'Survey.html', {'question': question})  # renders page

        if (response == 'Yes') or (response == 'Agree') or (response == 'Strongly Agree') or (
                response == 'Familiar') or (response == 'Very familiar') or (response == 'True'):
            question = Question.objects.get(id=base_question.NextIDB)  # Gets the question at the next B branch ID
            upchoice = upchoice + 'B'
        elif (response == 'No') or (response == 'Disagree') or (response == 'Strongly Disagree') or (
                response == 'Somewhat') or (response == 'Not at all') or (response == 'False'):
            question = Question.objects.get(id=base_question.NextIDA)  # Gets the question at the next A branch ID
            upchoice = upchoice + 'A'
        else:
            question = base_question  # Gets base question

        UserChoices.objects.filter(username=request.user).update(u_choice=upchoice)
        return render(request, 'Survey.html', {'question': question})  # Renders page with set question
    question = base_question  # Gets base question
    return render(request, 'Survey.html', {'question': question})  # Renders page with set question


def results(request):
    upchoice = UserChoices.objects.get(username=request.user).u_choice  # Gets choices for current user
    response_list = []  # creates a list for storing summary statements
    x = 1
    if upchoice[0] == '1':
        q_id = 101
        while q_id < 199:
            question = Question.objects.get(id=q_id)
            if upchoice[x] == 'A':
                if question.summarystatement_set.exists():
                    response_list.append(question.summarystatement_set.get().summary_text_a)
                q_id = question.NextIDA
            else:
                if question.summarystatement_set.exists():
                    response_list.append(question.summarystatement_set.get().summary_text_b)
                q_id = question.NextIDB
            x = x + 1

    elif upchoice[0] == '2':
        q_id = 201
        while q_id < 299:
            question = Question.objects.get(id=q_id)
            if upchoice[x] == 'A':
                if question.summarystatement_set.exists():
                    response_list.append(question.summarystatement_set.get().summary_text_a)
                q_id = question.NextIDA
            elif upchoice[x] == 'B':
                if question.summarystatement_set.exists():
                    response_list.append(question.summarystatement_set.get().summary_text_b)
                q_id = question.NextIDB
            else:
                q_id = question.NextIDB
            x = x + 1

    elif upchoice[0] == '3':
        q_id = 301
        while q_id < 399:
            question = Question.objects.get(id=q_id)
            if upchoice[x] == 'A':
                if question.summarystatement_set.exists():
                    response_list.append(question.summarystatement_set.get().summary_text_a)
                q_id = question.NextIDA
            elif upchoice[x] == 'B':
                if question.summarystatement_set.exists():
                    response_list.append(question.summarystatement_set.get().summary_text_b)
                q_id = question.NextIDB
            else:
                q_id = question.NextIDB
            x = x + 1

    elif upchoice[0] == '4':
        q_id = 401
        while q_id < 499:
            question = Question.objects.get(id=q_id)
            if upchoice[x] == 'A':
                if question.summarystatement_set.exists():
                    response_list.append(question.summarystatement_set.get().summary_text_a)
                q_id = question.NextIDA
            elif upchoice[x] == 'B':
                if question.summarystatement_set.exists():
                    response_list.append(question.summarystatement_set.get().summary_text_b)
                q_id = question.NextIDB
            else:
                q_id = question.NextIDB
            x = x + 1

    elif upchoice[0] == '5':
        q_id = 501
        while q_id < 599:
            question = Question.objects.get(id=q_id)
            if upchoice[x] == 'A':
                if question.summarystatement_set.exists():
                    response_list.append(question.summarystatement_set.get().summary_text_a)
                q_id = question.NextIDA
            elif upchoice[x] == 'B':
                if question.summarystatement_set.exists():
                    response_list.append(question.summarystatement_set.get().summary_text_b)
                q_id = question.NextIDB
            else:
                q_id = question.NextIDB
            x = x + 1

    elif upchoice[0] == '6':
        q_id = 601
        while q_id < 699:
            question = Question.objects.get(id=q_id)
            if upchoice[x] == 'A':
                if question.summarystatement_set.exists():
                    response_list.append(question.summarystatement_set.get().summary_text_a)
                q_id = question.NextIDA
            elif upchoice[x] == 'B':
                if question.summarystatement_set.exists():
                    response_list.append(question.summarystatement_set.get().summary_text_b)
                q_id = question.NextIDB
            else:
                q_id = question.NextIDB
            x = x + 1

    elif upchoice[0] == '7':
        q_id = 701
        while q_id < 799:
            question = Question.objects.get(id=q_id)
            if upchoice[x] == 'A':
                if question.summarystatement_set.exists():
                    response_list.append(question.summarystatement_set.get().summary_text_a)
                q_id = question.NextIDA
            elif upchoice[x] == 'B':
                if question.summarystatement_set.exists():
                    response_list.append(question.summarystatement_set.get().summary_text_b)
                q_id = question.NextIDB
            else:
                q_id = question.NextIDB
            x = x + 1

    else:
        q_id = 801
        while q_id < 899:
            question = Question.objects.get(id=q_id)
            if upchoice[x] == 'A':
                if question.summarystatement_set.exists():
                    response_list.append(question.summarystatement_set.get().summary_text_a)
                q_id = question.NextIDA
            elif upchoice[x] == 'B':
                if question.summarystatement_set.exists():
                    response_list.append(question.summarystatement_set.get().summary_text_b)
                q_id = question.NextIDB
            else:
                q_id = question.NextIDB
            x = x + 1

    return render(request, 'Results.html', {'response_list': response_list, 'upchoice': upchoice})


def info(request):  # renders info page
    return render(request, 'info.html')

class CityDataListView(ListView):
    model = CityData
    context_object_name = 'city data'


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'