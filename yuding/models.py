from django.db import models
from django.contrib.auth.models import AbstractUser

class meetings(models.Model):
    name = models.CharField(max_length=200,null=True, verbose_name=u'会议室名称')
    people = models.CharField(max_length=100, null=True,verbose_name=u'容纳人数')
    starttime = models.DateTimeField(null=True, blank=True,verbose_name=u'开始时间')
    endtime = models.DateTimeField(null=True, blank=True,verbose_name=u'结束时间')
    createname = models.CharField(max_length=200, null=True,  blank=True, verbose_name=u'预约人')

    class Meta:
        ordering = ['name']
        verbose_name = u"会议室信息"
        verbose_name_plural = verbose_name

    def __str__(self):
         return self.name

