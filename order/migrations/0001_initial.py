# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-11-25 16:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=180, verbose_name='商品名称')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='商品价格')),
                ('count', models.IntegerField(default=0, null=True, verbose_name='数量')),
            ],
            options={
                'verbose_name': '订单商品',
                'verbose_name_plural': '订单商品',
                'db_table': 'order_goods',
            },
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='订单ID')),
                ('addr_id', models.IntegerField(verbose_name='收货地址ID')),
                ('total_count', models.IntegerField(verbose_name='订单商品总数')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='订单总价')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='订单创建时间')),
                ('status', models.IntegerField(choices=[(0, '未付款'), (1, '等待发货'), (2, '配送中'), (3, '已完成'), (4, '支付失败'), (5, '已取消'), (6, '订单关闭')], default=0, verbose_name='订单状态')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.UserInfo')),
            ],
            options={
                'verbose_name': '订单信息',
                'verbose_name_plural': '订单信息',
                'db_table': 'order_info',
            },
        ),
        migrations.AddField(
            model_name='ordergoods',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.OrderInfo'),
        ),
    ]
