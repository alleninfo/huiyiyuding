import json

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.utils import timezone

from accounts.models import MyUser as User
from yuding.models import meetings


def index(request):
    title = '会议室预定系统',
    copyright1 = '某某有限公司 版权所有©2021',

    return render(request, 'huiyiyuding/login/index.html', locals())


def createmeeting(request):
    qs_creates = meetings.objects.filter(starttime__isnull=True)
    return render(request, 'huiyiyuding/core/newmeeting.html', {'name': qs_creates})


def mycreate(request):
    user1 = request.user
    qs = meetings.objects.filter(createname=user1)
    return render(request, 'huiyiyuding/core/mycreate.html', {'name': qs})



def get_json(request):
        user1= request.user
        data = meetings.objects.filter(createname=user1)
        dataCount = data.count()

        list = []
        # dic1 = dict()
        for item in data:
            dic = {"id":item.id,"name":item.name, "people":item.people,"starttime":item.starttime
                   ,"endtime":item.endtime,"createname":item.createname}
            list.append(dic)
        dic1 = {"code": 0, "msg": "ok", "DataCount": dataCount, "data": list}
        return JsonResponse(dic1)

def delete_page(request):
    get_id = request.GET.get("id")
    meetings.objects.filter(id=get_id).update(starttime=None, endtime=None, createname=None)
    return render(request,"index.html")

def update_page(request):
    get_id = request.GET.get("id")
    get_name = request.GET.get("name")
    get_people = request.GET.get("people")
    get_starttime = request.GET.get("starttime")
    get_endtime = request.GET.get("endtime")
    get_createname = request.GET.get("createname")

    obj = meetings.objects.get(id=get_id)
    obj.name = get_name
    obj.people = get_people
    obj.starttime = get_starttime
    obj.endtime = get_endtime
    obj.createname = get_createname
    obj.save()
    return render(request,"index.html")



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
    if request.method == 'POST':
        apply_name = request.POST.get('applyname')
        meetingname = request.POST.get('meeting')
        stime = request.POST.get('stime')
        etime = request.POST.get('etime')
        meetings.objects.filter(name=meetingname).update(name=meetingname, starttime=stime,
                                                         endtime=etime, createname=apply_name)
        # show_qs = meetings.objects.filter(createname=apply_name)
    return render(request, 'huiyiyuding/core/mycreate.html', locals())
