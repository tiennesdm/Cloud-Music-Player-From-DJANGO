# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-24 09:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_auto_20180324_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='audio_file',
            field=models.FileField(default='', max_length=200, upload_to='mp3/'),
        ),
    ]
