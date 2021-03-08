from django.contrib import admin
from django.urls import path, include
from HEALSurvey import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('topic/', views.topic, name='topic'),
    path('team/', views.team, name='team'),
    path('index/', views.index, name='index'),
    path('<int:question_id>/', views.survey, name='survey'),
    path('video/', views.video, name='video')
]
