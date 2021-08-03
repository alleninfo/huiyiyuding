import datetime

from django.db import models


class Userinfo(models.Model):
    username = models.CharField(max_length=200, verbose_name=u'用户名')
    password = models.CharField(max_length=200, verbose_name=u'密码')
    email = models.CharField(max_length=200, verbose_name=u'邮箱')
    truename = models.CharField(max_length=200, verbose_name=u'真实姓名')
    men = 'men'
    women = 'women'
    tech = 'tech'
    xingzheng = 'xingzheng'
    GENDER_CHOICES = [
        ('men', '男'),
        ('women', '女'),
    ]
    gender = models.CharField(
        choices= GENDER_CHOICES,
        max_length=300,
    )

    DEPARTIMENT_CHOICES = [
        ('tech', '技术部'),
        ('xingzheng', '行政部'),
    ]
    department = models.CharField(
        choices=DEPARTIMENT_CHOICES,
        max_length=300,
    )
    lastlogin = datetime.datetime.now()
    class Meta:
        ordering = ['truename']
        verbose_name = u"员工信息"
        verbose_name_plural = verbose_name
    def __str__(self):
        return 'username:%s email:%s truename:%s department:%s gender:%s' %(self.username, self.truename, self.email, self.gender, self.department)


class meetings(models.Model):
    name = models.CharField(max_length=200, verbose_name=u'会议室名称')
    people = models.CharField(max_length=100, verbose_name=u'容纳人数')
    starttime = models.CharField(max_length=200, null=True, verbose_name=u'开始时间')
    endtime = models.CharField(max_length=200,  null=True,  verbose_name=u'结束时间')
    createname = models.CharField(max_length=200, null=True, verbose_name=u'预约人')
    pretime = models.CharField(max_length=100,  null=True,verbose_name=u'会议持续时间')


    class Meta:
        ordering = ['name']
        verbose_name = u"会议室信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return 'name:%s pretime:%s createname:%s' % (self.name, self.pretime, self.createname)
