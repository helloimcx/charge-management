# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-21 12:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_auto_20170921_1825'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usersuggestions',
            old_name='_id',
            new_name='id',
        ),
    ]