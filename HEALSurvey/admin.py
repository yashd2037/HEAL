from django.contrib import admin

from .models import Question, Choice, SummaryStatement


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)

admin.site.register(SummaryStatement)

