from django.shortcuts import render, redirect, get_object_or_404
from .forms import TopicForm, ChoiceForm, UserChoicesForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.views import generic
from .models import Topics, Question, Choice, SummaryStatement, UserChoices, City, CityData, ZipCodeData, ZipCode, Post


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
    xid = 1

    if request.user.is_authenticated:
        for xid in range(1, 11):
            if UserChoices.objects.filter(username=request.user, u_id=xid).exists():  # checks choices at username + id
                if 'D' in UserChoices.objects.get(username=request.user, u_id=xid).u_choice:
                    xid = xid + 1  # goes to next id
                else:
                    UserChoices.objects.filter(username=request.user, u_id=xid).delete()
                    break
            else:  # if it doesnt exist
                break
            if xid == 11:
                return redirect('account_page')

    if request.method == 'POST':
        firstTopic = request.POST.get('topic')  # Gets submitted topic 1
        secondTopic = request.POST.get('topic2')  # Gets submitted topic 2
        if (firstTopic == 'Housing' and secondTopic == 'Transportation') or (
                secondTopic == 'Housing' and firstTopic == 'Transportation'):  # Checks which topics were selected
            question = Question.objects.get(id=201)  # Gets question at specified id
            if request.user.is_authenticated:  #checks if the current user is logged in
                UserChoices.objects.create(username=request.user, u_choice='2', u_id=xid).save  # creates uchoices
        elif (firstTopic == 'Housing' and secondTopic == 'Healthcare') or (
                secondTopic == 'Housing' and firstTopic == 'Healthcare'):
            question = Question.objects.get(id=301)
            if request.user.is_authenticated:
                UserChoices.objects.create(username=request.user, u_choice='3', u_id=xid).save
        elif (firstTopic == 'Healthy Food' and secondTopic == 'Healthcare') or (
                secondTopic == 'Healthy Food' and firstTopic == 'Healthcare'):
            question = Question.objects.get(id=401)
            if request.user.is_authenticated:
                UserChoices.objects.create(username=request.user, u_choice='4', u_id=xid).save
        elif (firstTopic == 'Transportation' and secondTopic == 'Healthcare') or (
                secondTopic == 'Transportation' and firstTopic == 'Healthcare'):
            question = Question.objects.get(id=501)
            if request.user.is_authenticated:
                UserChoices.objects.create(username=request.user, u_choice='5', u_id=xid).save
        elif (firstTopic == 'Employment' and secondTopic == 'Healthcare') or (
                secondTopic == 'Employment' and firstTopic == 'Healthcare'):
            question = Question.objects.get(id=601)
            if request.user.is_authenticated:
                UserChoices.objects.create(username=request.user, u_choice='6', u_id=xid).save
        elif (firstTopic == 'Employment' and secondTopic == 'Housing') or (
                secondTopic == 'Employment' and firstTopic == 'Housing'):
            question = Question.objects.get(id=701)
            if request.user.is_authenticated:
                UserChoices.objects.create(username=request.user, u_choice='7', u_id=xid).save
        elif (firstTopic == 'Employment' and secondTopic == 'Transportation') or (
                secondTopic == 'Employment' and firstTopic == 'Transportation'):
            question = Question.objects.get(id=801)
            if request.user.is_authenticated:
                UserChoices.objects.create(username=request.user, u_choice='8', u_id=xid).save
        elif ((firstTopic == 'Healthy Food' and secondTopic == 'Housing') or (
                secondTopic == 'Healthy Food' and firstTopic == 'Housing')) or (
                (firstTopic == 'Healthy Food' and secondTopic == 'Transportation') or (
                    secondTopic == 'Healthy Food' and firstTopic == 'Transportation')):
            question = Question.objects.get(id=101)  # Gets question at id 101, temporary solution for invalid input
            if request.user.is_authenticated:
                UserChoices.objects.create(username=request.user, u_choice='1', u_id=xid).save
        else:  # if the topic chosen is invalid
            messages.warning(request, "No survey for chosen topics. Please choose different topics")
            return render(request, 'TopicPage.html', {'form': form})  # Re-renders the current page
            # need this to display an error message telling user topic is invalid
        return render(request, 'Survey.html', {'question': question, 'xid': xid})  # Renders survey with current question
    return render(request, 'TopicPage.html', {'form': form})  # Re-renders the current page


def team(request):  # renders team page
    return render(request, 'Team.html')


def index(request):  # renders a list of all questions in the database on index page
    question_list = Question.objects.all()
    context = {'question_list': question_list}
    return render(request, 'index.html', context)


def survey(request, question_id, xid):  # renders initial survey page with selected question object from database
    base_question = Question.objects.get(id=question_id)  # Gets the question at the current id
    if request.user.is_authenticated:
        upchoice = UserChoices.objects.get(username=request.user, u_id=xid).u_choice
    if request.method == 'POST':
        if base_question.NextIDA == 1:
            return results(request, xid)

        if 'choice' in request.POST:  # Checks if there is a choice in the current request
            response = (base_question.choice_set.get(pk=request.POST['choice'])).choice_text  # sets choices text to var
        elif (base_question.choice_set.exists()) and ('choice' not in request.POST):  # Checks choices exist on page
            response = None  # Sets var to null
        else:
            question = Question.objects.get(id=base_question.NextIDA)  # Goes to the next page if no choices
            if request.user.is_authenticated:
                upchoice = upchoice + 'C'  # Updates user choices with a blank choice if authenticated
                UserChoices.objects.filter(username=request.user, u_id=xid).update(u_choice=upchoice)
            return render(request, 'Survey.html', {'question': question, 'xid': xid})  # renders page

        if (response == 'Yes') or (response == 'Agree') or (response == 'Strongly Agree') or (
                response == 'Familiar') or (response == 'Very familiar') or (response == 'True'):
            question = Question.objects.get(id=base_question.NextIDB)  # Gets the question at the next B branch ID
            if request.user.is_authenticated:
                upchoice = upchoice + 'B'  # Updates user choices with a positive choice if authenticated
        elif (response == 'No') or (response == 'Disagree') or (response == 'Strongly Disagree') or (
                response == 'Somewhat') or (response == 'Not at all') or (response == 'False'):
            question = Question.objects.get(id=base_question.NextIDA)  # Gets the question at the next A branch ID
            if request.user.is_authenticated:
                upchoice = upchoice + 'A'  # Updates user choices with a blank choice if authenticated
        else:
            question = base_question  # Gets base question

        if request.user.is_authenticated:
            UserChoices.objects.filter(username=request.user, u_id=xid).update(u_choice=upchoice)
        return render(request, 'Survey.html', {'question': question, 'xid': xid})  # Renders page with set question
    question = base_question  # Gets base question
    return render(request, 'Survey.html', {'question': question, 'xid': xid})  # Renders page with set question


def results(request, xid):
    response_list = []  # creates a list for storing summary statements
    if request.user.is_authenticated:  # checks if user is logged in or not
        upchoice = UserChoices.objects.get(username=request.user, u_id=xid).u_choice  # Gets choices for current user
        x = 1  # sets iterable variable x to 1
        if upchoice[0] == '1':  # check if user choices are on path 1
            q_id = 101  # sets temporary question id to 1
            while q_id < 199:  # until end of path 1 questions
                question = Question.objects.get(id=q_id)  # gets question at current id
                if upchoice[x] == 'A':  # if negative choice
                    if question.summarystatement_set.exists():  # checks if there is a summary statement
                        response_list.append(question.summarystatement_set.get().summary_text_a)  # appends to array
                    q_id = question.NextIDA  # goes to next question
                else:
                    if question.summarystatement_set.exists():  # checks if there is a summary statement
                        response_list.append(question.summarystatement_set.get().summary_text_b)  # appends to array
                    q_id = question.NextIDB  # goes to next question
                x = x + 1  # add 1 to x

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

        upchoice = upchoice + 'D'  # Adds a D to user choices to signify that choices are complete
        UserChoices.objects.filter(username=request.user, u_id=xid).update(u_choice=upchoice)  # updates upchoice

    else:  #If user is not logged in
        upchoice = 'x'  # sets user choice string to arbitrary x
        response_list.append("Thank you for taking the survey")  # simply thanks user for taking survey

    return render(request, 'Results.html', {'response_list': response_list, 'upchoice': upchoice})


def del_results(request, xid):
    response_list = []  # creates a list for storing summary statements
    upchoice = UserChoices.objects.get(username=request.user, u_id=xid).u_choice  # Gets choices for current user
    x = 1  # sets iterable variable x to 1
    if upchoice[0] == '1':  # check if user choices are on path 1
        q_id = 101  # sets temporary question id to 1
        while q_id < 199:  # until end of path 1 questions
            question = Question.objects.get(id=q_id)  # gets question at current id
            if upchoice[x] == 'A':  # if negative choice
                if question.summarystatement_set.exists():  # checks if there is a summary statement
                    response_list.append(question.summarystatement_set.get().summary_text_a)  # appends to array
                q_id = question.NextIDA  # goes to next question
            else:
                if question.summarystatement_set.exists():  # checks if there is a summary statement
                    response_list.append(question.summarystatement_set.get().summary_text_b)  # appends to array
                q_id = question.NextIDB  # goes to next question
            x = x + 1  # add 1 to x

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

    return render(request, 'DelResults.html', {'response_list': response_list, 'upchoice': upchoice, 'xid': xid})

def delete_rep(request, xid):
    UserChoices.objects.filter(username=request.user, u_id=xid).delete()
    x = 1
    for x in range(1, 11):
        if UserChoices.objects.filter(username=request.user, u_id=x).exists():  # checks choices at username + id
            if x > xid:
                UserChoices.objects.filter(username=request.user, u_id=x).update(u_id=x-1)  # updates upchoice
        x = x + 1
    return redirect('account_page')


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


def zipcode_details(request):
    result = ZipCodeData.objects.all()
    city_list = City.objects.all()
    return render(request, 'ZipCode_Data.html', {"ZipCodeData": result, "City": city_list})


def account_page(request):
    user_choice_list = []
    xid = 1
    for xid in range(1, 11):
        if UserChoices.objects.filter(username=request.user, u_id=xid).exists():
            if 'D' in UserChoices.objects.get(username=request.user, u_id=xid).u_choice:
                user_choice_list.append(UserChoices.objects.get(username=request.user, u_id=xid).u_choice)
            else:
                UserChoices.objects.filter(username=request.user, u_id=xid).delete()
        xid = xid + 1

    return render(request, 'UserAccount.html', {'user_choice_list': user_choice_list})
