from django.contrib import admin

# Register your models here.

from .models import Userinfo, meetings


admin.site.register([Userinfo, meetings])
