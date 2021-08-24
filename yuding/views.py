from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from accounts.models import MyUser as User
from yuding.models import meetings
from django.utils import timezone
from .forms import UploadFileForm



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
    meetings.objects.filter(createname=user1).update(starttime=None, endtime=None, createname=None)

    # _delete_meeting = meetings.objects.get(createname=user1)
    # _delete_meeting.starttime = None
    # _delete_meeting.endtime = None
    # _delete_meeting.createname = None
    # _delete_meeting.save()
    return render(request, 'huiyiyuding/core/list.html')


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

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')

    else:
        form = UploadFileForm()
    return render(request,'huiyiyuding/core/users/upload.html',{'form':form})

def handle_uploaded_file(f):
    with open('huiyiyuding/upload/images/title.jpg', 'wb+') as destination:
        for chunk in f.chunk():
            destination.write(chunk)

@login_required
def profile_update(request):
    user = get_object_or_404(User)
    user_profile = get_object_or_404(User, user=user)

    if request.method == 'POST':
        if user.is_valid():
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
def pwd_change(request):
    user = get_object_or_404(User)

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

def password_reset(request):
    return render(request, 'huiyiyuding/core/users/password_reset_form.html')

def password_reset_done(request):
    return render(request, 'huiyiyuding/core/users/password_reset_done.html')

def password_reset_confirm(request):
    return render(request, 'huiyiyuding/core/users/password_reset_confirm.html')

def password_reset_complete(request):
    return render(request, 'huiyiyuding/core/users/password_reset_complete.html')

















def bookmeet(request):
    if request.method =='POST':
            apply_name = request.POST.get('applyname')
            meetingname = request.POST.get('meeting')
            stime = request.POST.get('stime')
            etime = request.POST.get('etime')
            meetings.objects.filter(name=meetingname).update(name=meetingname,starttime=stime,
                                                             endtime=etime, createname=apply_name)
            show_qs = meetings.objects.filter(createname=apply_name)
            return render(request, 'huiyiyuding/core/mycreate.html', locals())
    else:
        return HttpResponse('预定失败，没有可用的会议室')


def a_delete_meetings(request):
    now = timezone.now()
    meetings.objects.filter(endtime__lte=now).update(starttime=None, endtime=None, createname=None)
    return render(request, 'huiyiyuding/core/list.html')
