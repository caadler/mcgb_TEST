# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-29 03:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0006_auto_20180310_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='Event_Postal',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='organization',
            name='Org_Phone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='organization',
            name='Org_Postal',
            field=models.IntegerField(),
        ),
    ]
