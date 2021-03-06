# Generated by Django 3.2.5 on 2021-08-09 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='meetings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True, verbose_name='会议室名称')),
                ('people', models.CharField(max_length=100, null=True, verbose_name='容纳人数')),
                ('starttime', models.DateTimeField(auto_now=True, null=True, verbose_name='开始时间')),
                ('endtime', models.DateTimeField(auto_now=True, null=True, verbose_name='结束时间')),
                ('createname', models.DateTimeField(null=True, verbose_name='预约人')),
                ('pretime', models.DateTimeField(auto_now=True, null=True, verbose_name='会议持续时间')),
            ],
            options={
                'verbose_name': '会议室信息',
                'verbose_name_plural': '会议室信息',
                'ordering': ['name'],
            },
        ),
    ]
