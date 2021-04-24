from django import forms
from .models import Topics, Choice, UserChoices


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topics
        fields = '__all__'


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = '__all__'


class UserChoicesForm(forms.ModelForm):
    class Meta:
        model = UserChoices
        fields = '__all__'
