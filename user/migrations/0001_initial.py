# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-11-25 16:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReceiverInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiver', models.CharField(max_length=32, verbose_name='收货人')),
                ('address', models.CharField(max_length=648, verbose_name='收货地址')),
                ('receiver_phone', models.CharField(max_length=11, verbose_name='收货人电话')),
                ('is_default', models.BooleanField(default=False, verbose_name='是否默认')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '收件人信息',
                'verbose_name_plural': '收件人信息',
                'db_table': 'receiver_info',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('username', models.CharField(max_length=32, primary_key=True, serialize=False, verbose_name='用户名')),
                ('password', models.CharField(max_length=32, verbose_name='密码')),
                ('nickname', models.CharField(max_length=32, verbose_name='昵称')),
                ('email', models.EmailField(default='', max_length=255, verbose_name='邮箱')),
                ('telephone', models.CharField(max_length=11, verbose_name='手机号码')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('login_time', models.DateTimeField(auto_now_add=True, verbose_name='登录时间')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
                'db_table': 'user_info',
            },
        ),
        migrations.AddField(
            model_name='receiverinfo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.UserInfo', verbose_name='所属用户'),
        ),
    ]
