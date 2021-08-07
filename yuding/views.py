from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from yuding.models import meetings
from django.shortcuts import render, get_object_or_404
from .forms import RegistrationForm, LoginForm, ProfileForm, PwdChangeForm
from .models import UserProfile
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def index(request):
    dic = {
        'title':'会议室预定系统',
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
    qs_change = meetings.objects.filter(createname=True)
    return render(request, 'huiyiyuding/core/changemeeting.html', {'name': qs_change})


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


# # 登录相关
# def login(request):
#     if request.method == 'GET':
#         #1, 首先检查session，判断用户是否第一次登录，如果不是，则直接重定向到首页
#         if 'username' in request.session:
#             return HttpResponseRedirect('/')
#         #2, 然后检查cookie，是否保存了用户登录信息
#         if 'username' in request.COOKIES:
#             #若存在则赋值回session，并重定向到首页
#             request.session['username'] = request.COOKIES['username']
#             return  HttpResponseRedirect('/')
#             #不存在则重定向登录页，让用户登录
#         return render(request, 'huiyiyuding/login/index.html')
#
#     elif request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         message = '请检查填写的内容！'
#         if not username or not password:
#             message = '用户名或密码错误'
#             return render(request, 'huiyiyuding/login/index.html', locals())
#         users = models.Userinfo.objects.filter(username=username, password=password)
#         if not users:
#             message = '用户不存在或者密码错误'
#             return render(request, 'huiyiyuding/login/index.html', locals())
#         users = users[0]
#
#     return render(request, 'huiyiyuding/core/admin.html')
#
#
#
#
#
# def logout(request):
#     return redirect('/')
#
#

@login_required
def profile(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'huiyiyuding/core/users/profile.html', {'user': user})


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


def register(request):
    if request.method == 'POST':

        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password2']

            # 使用内置User自带create_user方法创建用户，不需要使用save()
            user = User.objects.create_user(username=username, password=password, email=email)

            # 如果直接使用objects.create()方法后不需要使用save()
            user_profile = UserProfile(user=user)
            user_profile.save()

            return HttpResponseRedirect("/login/")
    else:
        form = RegistrationForm()
    return render(request, 'huiyiyuding/core/users/registration.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(username=username, password=password)

            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect('/main/')
            else:
                # 登录失败
                return render(request, 'huiyiyuding/login/index.html',
                              {'form': form, 'message': 'Wrong password Please Try agagin'})
    else:
        form = LoginForm()

    return render(request, 'huiyiyuding/login/index.html', {'form': form})


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/login/")


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
