from django import forms
from .models import Topics


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topics
        fields = '__all__'


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Topics
        fields = '__all__'
