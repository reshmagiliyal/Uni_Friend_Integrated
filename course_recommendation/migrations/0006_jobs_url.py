# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-01 08:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_recommendation', '0005_remove_jobs_description2'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='url',
            field=models.URLField(max_length=100, null=True),
        ),
    ]
