# Generated by Django 3.2.5 on 2021-07-28 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('truename', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('men', '男'), ('women', '女')], max_length=300)),
                ('department', models.CharField(choices=[('tech', '技术部'), ('xingzheng', '行政部')], max_length=300)),
            ],
        ),
    ]
