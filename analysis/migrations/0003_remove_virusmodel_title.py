# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-19 10:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0002_auto_20170519_1722'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='virusmodel',
            name='title',
        ),
    ]
