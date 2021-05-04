from django.contrib import admin
from django.urls import path, include
from HEALSurvey import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('topic/', views.topic, name='topic'),
    path('team/', views.team, name='team'),
    path('{<int:question_id>,<int:xid>}/', views.survey, name='survey'),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('register/', views.register_view, name="register"),
    path('results<int:xid>/', views.results, name="results"),
    path('del_results<int:xid>/', views.del_results, name="del_results"),
    path('delete_rep<int:xid>', views.delete_rep, name="delete_rep"),
    path('info/', views.info, name='info'),
    path('blog/', views.PostList.as_view(), name='blog'),
    path('zipcode/', views.zipcode_details, name='zipcode'),
    path('account_page/', views.account_page, name='account_page'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail')


]
