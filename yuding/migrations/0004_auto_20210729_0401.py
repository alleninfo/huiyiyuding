# Generated by Django 3.2.5 on 2021-07-29 04:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yuding', '0003_auto_20210729_0358'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='meetings',
            options={'ordering': ['name'], 'verbose_name': '会议室信息', 'verbose_name_plural': '会议室信息'},
        ),
        migrations.AlterModelOptions(
            name='userinfo',
            options={'ordering': ['truename'], 'verbose_name': '员工信息', 'verbose_name_plural': '员工信息'},
        ),
    ]