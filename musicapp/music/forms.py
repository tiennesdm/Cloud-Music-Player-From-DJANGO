from django.contrib.auth.models import User
from django.db import models
from django import forms
from .models import Album
from .models import Song
class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields =['username','email','password']
class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ['artist', 'album_title', 'genre', 'album_logo']
class SongForm(forms.ModelForm):



    class Meta:
        model = Song

        fields = ['song_title', 'audio_file']
