from django.contrib import admin
from django.urls import path, include
from HEALSurvey import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('topic/', views.topic, name='topic'),
    path('survey/', views.survey, name='survey'),
    path('team/', views.team, name='team'),
    # ex: /index/
    path('index/', views.index, name='index'),
    # ex: /surveys/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /surveys/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /surveys/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('video/', views.video, name='video')
]
