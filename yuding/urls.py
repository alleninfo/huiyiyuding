from django.urls import path

from . import views

app_name = 'yuding'
urlpatterns = [
    path('', views.index, name='index'),
    path('createmeeting/', views.createmeeting, name='createmeeting'),
    path('mycreate/', views.mycreate, name='mycreate'),
    path('list/', views.list_all, name='list'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('user/profile/', views.profile, name='profile'),
    path('bookmeeting/', views.bookmeet, name='bookmeet'),
    path('update_meeting/', views.get_json, name='getdate'),
    path('delete_page/',views.delete_page),
    path("update_page/",views.update_page)
]

