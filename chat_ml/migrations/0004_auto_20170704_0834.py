# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-04 08:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_ml', '0003_auto_20170704_0825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userquery',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 4, 8, 33, 58, 583402)),
        ),
    ]