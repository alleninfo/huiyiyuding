from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from yuding.models import meetings
from . import models


def index(request):
    context = {
        'title': '会议室预定系统',
        'copyright': '某某有限公司 版权所有©2016-2021',
    }
    return render(request, 'huiyiyuding/login/index.html', context)


def mains(request):
    qs_all = meetings.objects.values()
    return render(request, 'huiyiyuding/core/list.html', {'name': qs_all})


def createmeeting(request):
    qs_create = meetings.objects.values()
    creates = qs_create.filter(pretime__isnull=True)
    print(creates)
    return render(request, 'huiyiyuding/core/createmeeting.html', {'name': creates})


def changemeeting(request):
    qs_change = meetings.objects.values()
    changes = qs_change.filter()
    return render(request, 'huiyiyuding/core/changemeeting.html', {'name': changes})


def deletemeeting(request):
    qs_creat = meetings.objects.values()
    delete = qs_creat.filter()
    return render(request, 'huiyiyuding/core/deletemeeting.html', {'name': delete})


def mycreate(request):
    qs_my = meetings.objects.values()
    my_create = qs_my.filter()
    return render(request, 'huiyiyuding/core/mycreate.html', {'name': my_create})


def list_all(request):
    qs_all = meetings.objects.values()
    return render(request, 'huiyiyuding/core/list.html', {'name': qs_all})


# 登录相关
def login(request):
    if request.method == 'GET':
        #1, 首先检查session，判断用户是否第一次登录，如果不是，则直接重定向到首页
        if 'username' in request.session:
            return HttpResponseRedirect('/index/')
        #2, 然后检查cookie，是否保存了用户登录信息
        if 'username' in request.COOKIES:
            #若存在则赋值回session，并重定向到首页
            request.session['username'] = request.COOKIES['username']
            return  HttpResponseRedirect('/index/')
            #不存在则重定向登录页，让用户登录
        return render(request, 'huiyiyuding/login/index.html')

    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        message = '请检查填写的内容！'
        if not username or not password:
            message = '用户名或密码错误'
            return render(request, 'huiyiyuding/login/index.html', locals())
        users = models.Userinfo.objects.filter(username=username, password=password)
        if not users:
            message = '用户不存在或者密码错误'
            return render(request, 'huiyiyuding/login/index.html', locals())
        users = users[0]

    return render(request, 'huiyiyuding/core/admin.html')


def logout(request):
    return redirect('/index/')


# 创建会议室相关

def newmeeting(request):
    return render(request, 'huiyiyuding/core/newmeeting.html')

