from django.contrib import admin
from django.urls import path, include
from HEALSurvey import views

urlpatterns = [
    path('surveys/', include('surveys.urls')),
    path('admin/', admin.site.urls),
    path('home/', views.home, name="home"),
    path('topic/', views.topic, name='topic'),
    path('survey/', views.survey, name='survey'),
    path('team/', views.team, name='team')
]
