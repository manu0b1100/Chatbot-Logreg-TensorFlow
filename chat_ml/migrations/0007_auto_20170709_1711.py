# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-09 17:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_ml', '0006_userquery_backend'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userquery',
            name='pclass',
            field=models.CharField(default='about', max_length=255),
        ),
    ]
