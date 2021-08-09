from django.contrib.auth import authenticate, login,logout

from yuding.models import meetings
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProfileForm, PwdChangeForm
from accounts.models import MyUser as User
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse
from django.contrib.auth.decorators import login_required


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

@login_required
def profile(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'huiyiyuding/core/users/profile.html', {'user': user})


def login(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
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
    return redirect(request, '/index/')

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
