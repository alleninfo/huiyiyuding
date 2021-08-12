from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from accounts.models import MyUser as User
from yuding.models import meetings
from . import forms
from .forms import ProfileForm, PwdChangeForm, applymeeting
from . import models





def index(request):
    dic = {
        'title': '会议室预定系统',
        'copyright': '某某有限公司 版权所有©2016-2021',

    }

    return render(request, 'huiyiyuding/login/index.html', dic)


def mains(request):
    qs_all = meetings.objects.values()
    return render(request, 'huiyiyuding/core/list.html', {'name': qs_all})



def createmeeting(request):
    qs_creates = meetings.objects.filter(starttime__isnull=True)
    return render(request, 'huiyiyuding/core/newmeeting.html', {'name': qs_creates})

def changemeeting(request):
    show_qs = meetings.objects.filter()
    return render(request, 'huiyiyuding/core/changemeeting.html', {'name': show_qs})


def deletemeeting(request):
    qs_creat = meetings.objects.values()
    delete = qs_creat.filter()
    return render(request, 'huiyiyuding/core/deletemeeting.html', {'name': delete})


def mycreate(request):
    qs = meetings.objects.filter(username=username)
    return render(request, 'huiyiyuding/core/mycreate.html', {'name':qs})


def list_all(request):
    qs_all = meetings.objects.values()
    return render(request, 'huiyiyuding/core/list.html', {'name': qs_all})

@login_required
def profile(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'huiyiyuding/core/users/profile.html', {'user': user})


def login(request):
    if request.method == 'POST':
        user = request.POST.get('username')
        pwd = request.POST.get('password')
        # if 验证成功返回 user 对象，否则返回None
        user = auth.authenticate(username=user, password=pwd)

        if user:
            # request.user ： 当前登录对象
            auth.login(request, user)
            # return HttpResponse("OK")
            return redirect('/main/')

    return render(request, 'huiyiyuding/core/admin.html')

def logout(request):
    auth.logout(request)
    return render(request, 'huiyiyuding/login/index.html')

@login_required
def profile_update(request, pk):
    user = get_object_or_404(User, pk=pk)
    user_profile = get_object_or_404(User, user=user)

    if request.method == 'POST':
        form = ProfileForm(request.POST)

        if form.is_valid():
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()

            user_profile.org = form.cleaned_data['org']
            user_profile.telephone = form.cleaned_data['telephone']
            user_profile.save()

            return HttpResponseRedirect(reverse('users:profile', args=[user.id]))
    else:
        default_data = {'first_name': user.first_name, 'last_name': user.last_name,
                        'org': user_profile.org, 'telephone': user_profile.telephone, }
        form = ProfileForm(default_data)

    return render(request, 'huiyiyuding/core/users/profile_update.html', {'form': form, 'user': user})

@login_required
def pwd_change(request, pk):
    user = get_object_or_404(User, pk=pk)

    if request.method == "POST":
        form = PwdChangeForm(request.POST)

        if form.is_valid():
            password = form.cleaned_data['old_password']
            username = user.username

            user = auth.authenticate(username=username, password=password)

            if user is not None and user.is_active:
                new_password = form.cleaned_data['password2']
                user.set_password(new_password)
                user.save()
                return HttpResponseRedirect('/login/')

            else:
                return render(request, 'huiyiyuding/core/users/pwd_change.html', {'form': form,
                                                                 'user': user,
                                                                 'message': 'Old password is wrong Try again'})
    else:
        form = PwdChangeForm()

    return render(request, 'huiyiyuding/core/users/pwd_change.html', {'form': form, 'user': user})

def bookmeet(request):
    if request.method =='POST':
            apply_name = request.POST.get('applyname')
            meetingname = request.POST.get('meeting')
            stime = request.POST.get('stime')
            etime = request.POST.get('etime')
            _update_meeting = meetings.objects.get(name=meetingname)
            _update_meeting.name=meetingname
            _update_meeting.starttime=stime
            _update_meeting.endtime=etime
            _update_meeting.createname=apply_name
            _update_meeting.save()
            show_qs = meetings.objects.filter(createname=apply_name)
            return redirect('/mycreate/')
    return render(request, 'huiyiyuding/core/list.html', locals())
