# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-13 13:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0008_suggestions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suggestions',
            name='email',
        ),
        migrations.AddField(
            model_name='suggestions',
            name='phone',
            field=models.IntegerField(default=0),
        ),
    ]