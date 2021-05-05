from django.contrib import admin

from .models import Question, Choice, City, ZipCode, ZipCodeData, SummaryStatement, UserChoices, Post


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 0


class SummaryStatementInline(admin.StackedInline):
    model = SummaryStatement
    extra = 0


class QuestionAdmin(admin.ModelAdmin):
    inlines = [SummaryStatementInline, ChoiceInline]
    search_fields = ['QuestionText']


class CityAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


class ZipCodeAdmin(admin.ModelAdmin):
    list_display = ['city', 'zipcode']
    search_fields = ['zipcode']


class ZipCodeDataAdmin(admin.ModelAdmin):
    list_display = ['city', 'zipcode']


admin.site.register(Question, QuestionAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(ZipCode, ZipCodeAdmin)
admin.site.register(ZipCodeData, ZipCodeDataAdmin)


# admin.site.register(SummaryStatement)
# admin.site.register(UserChoices)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
