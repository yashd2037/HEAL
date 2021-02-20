from django.shortcuts import render, redirect
from .forms import TopicForm
from .models import Topics

def home(request):
    return render(request, 'IntroPage.html')

def topic(request):
    form = TopicForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('survey')
    context = {'form': form}
    return render(request, 'TopicPage.html', context)

def survey(request):
    return render(request, 'Survey.html')

