from django import forms
from .models import Topics, Choice


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topics
        fields = '__all__'


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = '__all__'
