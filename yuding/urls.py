from django.urls import re_path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'yuding'
urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^createmeeting/', views.createmeeting, name='createmeeting'),
    re_path(r'^changemeeting/', views.changemeeting, name='changemeeting'),
    re_path(r'^deletemeeting/', views.deletemeeting, name='deletemeeting'),
    re_path(r'^mycreate/', views.mycreate, name='mycreate'),
    re_path(r'^list/', views.list_all, name='list'),
    re_path(r'^login/$', views.login, name='login'),
    re_path(r'^logout/$', views.logout, name='logout'),
    re_path(r'^user/profile/$', views.profile, name='profile'),
    re_path(r'^bookmeeting/', views.bookmeet, name='bookmeet'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

