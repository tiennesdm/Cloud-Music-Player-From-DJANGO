# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib import admin
from music.models import Album,Song
# Register your models here.
admin.site.register(Album),
admin.site.register(Song)
