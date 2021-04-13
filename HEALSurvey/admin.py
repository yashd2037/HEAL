from django.contrib import admin

from .models import Question, Choice, City, ZipCode, CityData, SummaryStatement, UserChoices, Post


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(City)
admin.site.register(ZipCode)
admin.site.register(CityData)
admin.site.register(SummaryStatement)
admin.site.register(UserChoices)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)

