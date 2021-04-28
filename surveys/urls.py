from django.urls import path

from . import views

app_name = 'surveys'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /surveys/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /surveys/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /surveys/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]