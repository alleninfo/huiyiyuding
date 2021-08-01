from django.shortcuts import render
from yuding.models import meetings

def index(request):

    context ={
        'title': '会议室预定系统',
        'copyright': '某某有限公司 版权所有©2016-2021',
    }
    return render(request, 'huiyiyuding/index.html', context)

def mains(request):
    qs = meetings.objects.values()
    return render(request, 'huiyiyuding/core/admin.html', {'name': qs})

def createmeeting(request):
        qs = meetings.objects.values()
        creates = qs.filter(pretime__isnull=True)
        return render(request, 'huiyiyuding/core/createmeeting.html', {'name': creates})

def changemeeting(request):
        qs = meetings.objects.values()
        changes = qs.filter(createname)
        return render(request, 'huiyiyuding/core/changemeeting.html', {'name': changes})

def deletemeeting(request):
        qs = meetings.objects.values()
        delete = qs.filter(createname)
        return render(request, 'huiyiyuding/core/deletemeeting.html', {'name': delete})


