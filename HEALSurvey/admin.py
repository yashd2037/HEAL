from django.contrib import admin

from .models import Question, Choice, City, ZipCode, CityData, SummaryStatement


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 4


# class SummaryStatementInline(admin.StackedInline):
#     model = SummaryStatement
#     extra = 2


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(City)
admin.site.register(ZipCode)
admin.site.register(CityData)
admin.site.register(SummaryStatement)