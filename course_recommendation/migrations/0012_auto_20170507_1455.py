# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-07 21:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_recommendation', '0011_auto_20170507_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='description',
            field=models.CharField(max_length=2000, null=True),
        ),
    ]