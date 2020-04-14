from django.shortcuts import render
from .models import YandexMusic
from .models import mp3Music


def mainpage(request):
    return render(request, 'mainpage/mainpage.html', {})


def musicpage(request):
    return render(request, 'musicpage/musicpage.html', {'music': YandexMusic.objects.all(), 'mp3s': mp3Music.objects.all() })
