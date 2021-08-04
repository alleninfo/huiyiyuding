from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('createmeeting/', views.createmeeting),
    path('changemeeting/', views.changemeeting),
    path('deletemeeting/', views.deletemeeting),
    path('main/', views.mains),
    path('mycreate/', views.mycreate),
    path('list/', views.list_all),
    path('login/', views.login),
    path('logout/', views.logout),
    path('userinfo/', views.nuserinfo),
]
