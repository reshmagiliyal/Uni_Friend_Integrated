# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-01 07:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course_recommendation', '0004_auto_20170430_1822'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobs',
            name='description2',
        ),
    ]
