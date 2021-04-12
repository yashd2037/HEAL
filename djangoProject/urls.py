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
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('register/', views.register_view, name="register"),
    path('results/', views.results, name="results"),
    path('info/', views.info, name='info')

]
