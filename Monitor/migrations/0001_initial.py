# Generated by Django 2.0.7 on 2018-08-15 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('memory_used', models.FloatField(default=0, verbose_name='内存MB')),
                ('cpu_used', models.FloatField(default=0, verbose_name='统计当前cpu使用率')),
                ('disk_used', models.FloatField(default=0, verbose_name='统计磁盘使用情况')),
                ('createtime', models.DateTimeField(auto_now=True, verbose_name='生成时间')),
            ],
            options={
                'db_table': 'resource_monitor',
            },
        ),
    ]