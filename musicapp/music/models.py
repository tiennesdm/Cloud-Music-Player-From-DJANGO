# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import Permission, User
from django.core.urlresolvers import reverse, reverse_lazy, resolve
from django.db import models


# Create your models here.
class Album(models.Model):
    user = models.ForeignKey(User,default=1)
    artist=models.CharField(max_length=250)
    album_title=models.CharField(max_length=500)
    genre=models.CharField(max_length=150)
    album_logo=models.ImageField(default='' )

    def __str__(self):
        return self.artist + "---" +self.album_title

class Song(models.Model):
    album=models.ForeignKey(Album,on_delete=models.CASCADE)
    file_type=models.CharField(max_length=10)
    song_title=models.CharField(max_length=250)
    audio_file = models.FileField(default='',upload_to = u'mp3/',max_length=200)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title
