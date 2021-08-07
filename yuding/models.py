from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    username = models.CharField(max_length=200,null=True,verbose_name=u'用户名')
    password = models.CharField(max_length=200, null=True,verbose_name=u'密码')
    email = models.CharField(max_length=200, null=True,verbose_name=u'邮箱')
    realname = models.CharField(max_length=200, db_index=True,verbose_name=u'真实姓名')
    lastlogintime = models.DateTimeField(auto_now=True, verbose_name=u'上次登录时间')
    mod_data =models.DateTimeField(u'最近修改时间', auto_now=True)
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
    REQUIRED_FIELDS = ['usertype', 'realname']
    class Meta:

        # ordering = ['username']
         verbose_name = u"员工信息"
        # verbose_name_plural = verbose_name
    def __str__(self):
        return '{}'.format(self.user.__str__())

class meetings(models.Model):
    name = models.CharField(max_length=200,null=True, verbose_name=u'会议室名称')
    people = models.CharField(max_length=100, null=True,verbose_name=u'容纳人数')
    starttime = models.DateTimeField(auto_now=True,null=True, verbose_name=u'开始时间')
    endtime = models.DateTimeField(auto_now=True,null=True,  verbose_name=u'结束时间')
    createname = models.DateTimeField(null=True, verbose_name=u'预约人')
    pretime = models.DateTimeField(auto_now=True,null=True,verbose_name=u'会议持续时间')


    class Meta:
        ordering = ['name']
        verbose_name = u"会议室信息"
        verbose_name_plural = verbose_name

    def __str__(self):
         return self.name