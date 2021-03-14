from django import forms
from .models import Topics, Question


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topics
        fields = '__all__'


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
