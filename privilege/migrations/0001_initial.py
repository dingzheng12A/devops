# Generated by Django 2.1.3 on 2019-02-13 15:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Privilege',
            fields=[
                ('id', models.AutoField(default=1, max_length=11, primary_key=True, serialize=False)),
                ('pid', models.IntegerField(validators=[django.core.validators.MinValueValidator(10)])),
                ('privilege_name', models.CharField(max_length=200)),
                ('request_method', models.CharField(max_length=10)),
                ('request_url', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'sys_privilege',
            },
        ),
    ]
