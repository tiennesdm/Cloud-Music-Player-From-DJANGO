# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-21 15:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_song_audio_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.FileField(default='', upload_to=''),
        ),
    ]
