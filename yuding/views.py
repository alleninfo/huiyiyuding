from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from accounts.models import MyUser as User
from yuding.models import meetings
from django.utils import timezone



def index(request):
        title = '会议室预定系统',
        copyright1 = '某某有限公司 版权所有©2021',

        return render(request, 'huiyiyuding/login/index.html', locals())


def createmeeting(request):
    qs_creates = meetings.objects.filter(starttime__isnull=True)
    return render(request, 'huiyiyuding/core/newmeeting.html', {'name': qs_creates})

def changemeeting(request):
    user1 = request.user
    qs = meetings.objects.filter(createname=user1)
    return render(request, 'huiyiyuding/core/changemeeting.html', {'name': qs})


def deletemeeting(request):
    user1 = request.user
    qs = meetings.objects.filter(createname=user1)
    qs.createname = None
    qs.starttime = None
    qs.endtime = None
    qs.update()
    return render(request, 'huiyiyuding/core/mycreate.html')


def mycreate(request):
    user1 = request.user
    qs = meetings.objects.filter(createname=user1)
    return render(request, 'huiyiyuding/core/mycreate.html', {'name':qs})


def list_all(request):
    qs_all = meetings.objects.values()
    return render(request, 'huiyiyuding/core/list.html', {'name': qs_all})


def login(request):
    if request.method == 'POST':
        user = request.POST.get('username')
        pwd = request.POST.get('password')
        # if 验证成功返回 user 对象，否则返回None
        user = auth.authenticate(username=user, password=pwd)

        if user:
            # request.user ： 当前登录对象
            auth.login(request, user)
            return redirect('/list/')
        else:
            return HttpResponse('用户名或密码错误')

    return render(request, 'huiyiyuding/core/list.html')

def logout(request):
    auth.logout(request)
    return render(request, 'huiyiyuding/login/index.html')

@login_required
def profile(request):
    user1 = request.user
    qs = User.objects.filter(username=user1)
    return render(request, 'huiyiyuding/core/users/profile.html', {'user': qs})



def bookmeet(request):
    if request.method =='POST':
            apply_name = request.POST.get('applyname')
            meetingname = request.POST.get('meeting')
            stime = request.POST.get('stime')
            etime = request.POST.get('etime')
            meetings.objects.filter(name=meetingname).update(name=meetingname,starttime=stime,
                                                             endtime=etime, createname=apply_name)
            # show_qs = meetings.objects.filter(createname=apply_name)
    return render(request, 'huiyiyuding/core/mycreate.html', locals())


def a_delete_meetings(request):
    now = timezone.now()
    meetings.objects.filter(endtime__lte=now).update(starttime=None, endtime=None, createname=None)
    return render(request, 'huiyiyuding/core/list.html')
