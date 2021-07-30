from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('allmeetings/', views.get_meetings),
    path('createmeeting/', views.createmeeting),
    path('changemeeting/', views.changemeeting),
    path('deletemeeting/', views.deletemeeting),
    path('main/', views.mains),
]