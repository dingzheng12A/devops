# Generated by Django 2.1.3 on 2019-03-11 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20190311_2137'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mygroup',
            old_name='department',
            new_name='description',
        ),
        migrations.AlterModelTable(
            name='mygroup',
            table='groups',
        ),
    ]