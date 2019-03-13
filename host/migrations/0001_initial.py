# Generated by Django 2.1.3 on 2019-03-11 16:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='实例名称')),
                ('region', models.CharField(default='', max_length=20, verbose_name='数据中心')),
                ('az', models.CharField(default='', max_length=20, verbose_name='可用区')),
                ('mem', models.IntegerField(default=0, verbose_name='内存')),
                ('cpu', models.IntegerField(default=0, verbose_name='CPU')),
                ('status', models.CharField(default='', max_length=10, verbose_name='状态')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('expire', models.DateTimeField(auto_now=True, verbose_name='过期时间')),
                ('instance_type', models.CharField(default='', max_length=20, verbose_name='实例类型')),
                ('instance_name', models.CharField(default='', max_length=50, verbose_name='实例名称')),
                ('hostname', models.CharField(default='', max_length=50, verbose_name='主机名')),
                ('internet_ip', models.GenericIPAddressField(default='0.0.0.0', verbose_name='公网IP')),
                ('internet_charge', models.CharField(default='', max_length=100, verbose_name='流量支付模式')),
                ('internal_ip', models.GenericIPAddressField(default='0.0.0.0', verbose_name='内网IP')),
                ('elastic_ip', models.GenericIPAddressField(default='0.0.0.0', verbose_name='弹性IP')),
                ('charge_type', models.CharField(default='', max_length=20, verbose_name='支付方式')),
                ('desc', models.CharField(default='', max_length=100, verbose_name='备注')),
                ('os_type', models.CharField(max_length=30, verbose_name='操作系统类型')),
                ('tags', models.CharField(max_length=100, verbose_name='实例标签')),
            ],
        ),
        migrations.CreateModel(
            name='Metric',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('cpu_avg', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='cpu平均值')),
                ('cpu_max', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='cpu峰值')),
                ('mem_avg', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='mem平均值')),
                ('mem_max', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='mem峰值')),
                ('iops_avg', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='iops平均值')),
                ('iops_max', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='iosp峰值')),
                ('writeiops_avg', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='写操作iops平均值')),
                ('writeiops_max', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='写操作iops峰值')),
                ('network_avg', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='网卡流量平均值')),
                ('network_max', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='网卡流量峰值')),
                ('load_avg', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='系统负载均值')),
                ('load_max', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='系统负载峰值')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='生成时间')),
            ],
        ),
    ]
