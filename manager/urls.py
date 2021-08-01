from django.urls import path
from manager import sign, meetings


urlpatterns =[
    path('signin', sign.signin),
    path('signout', sign.signout),
    path('meetings', meetings.listmeeting),
]