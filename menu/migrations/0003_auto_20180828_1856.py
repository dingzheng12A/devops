# Generated by Django 2.0.7 on 2018-08-28 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20180725_0059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='span_id',
        ),
        migrations.AlterModelTable(
            name='menu',
            table='sys_menu',
        ),
    ]