# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-25 07:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0010_auto_20170525_1506'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='VirusUrl',
            new_name='VirusString',
        ),
        migrations.RenameField(
            model_name='virusdatabase',
            old_name='url',
            new_name='string',
        ),
        migrations.RenameField(
            model_name='virusstring',
            old_name='url',
            new_name='string',
        ),
    ]