from django.contrib import admin
from django.urls import path
from HEALSurvey import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('topic/', views.topic, name='topic'),
    path('survey/', views.survey, name='survey'),
    path('team/', views.team, name='team')
]
