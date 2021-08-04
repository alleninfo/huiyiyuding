# Generated by Django 3.2.5 on 2021-08-04 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yuding', '0008_auto_20210804_0149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetings',
            name='name',
            field=models.CharField(max_length=200, null=True, verbose_name='会议室名称'),
        ),
        migrations.AlterField(
            model_name='meetings',
            name='people',
            field=models.CharField(max_length=100, null=True, verbose_name='容纳人数'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='email',
            field=models.CharField(max_length=200, null=True, verbose_name='邮箱'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='password',
            field=models.CharField(max_length=200, null=True, verbose_name='密码'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='truename',
            field=models.CharField(max_length=200, null=True, verbose_name='真实姓名'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='username',
            field=models.CharField(max_length=200, null=True, verbose_name='用户名'),
        ),
    ]