# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-30 06:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0009_auto_20180330_0325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addhour',
            name='Event_ID',
        ),
        migrations.AlterField(
            model_name='addhour',
            name='EmpRecord_Time',
            field=models.DecimalField(decimal_places=2, max_digits=2),
        ),
    ]
