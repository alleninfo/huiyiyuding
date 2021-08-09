from django.urls import  re_path
from . import views

app_name = 'yuding'
urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^createmeeting/', views.createmeeting, name='createmeeting'),
    re_path(r'^changemeeting/', views.changemeeting, name='changemeeting'),
    re_path(r'^deletemeeting/', views.deletemeeting, name='deletemeeting'),
    re_path(r'^main/', views.mains, name='main'),
    re_path(r'^mycreate/', views.mycreate, name='mycreate'),
    re_path(r'^list/', views.list_all, name='list'),
    re_path(r'^login/$', views.login, name='login'),
    re_path(r'^logout/$', views.logout, name='logout'),
    re_path(r'^user/(?P<pk>\d+)/profile/$', views.profile, name='profile'),
    re_path(r'^user/(?P<pk>\d+)/profile/update/$', views.profile_update, name='profile_update'),
    re_path(r'^user/(?P<pk>\d+)/pwd_change/$', views.pwd_change, name='pwd_change'),
]
