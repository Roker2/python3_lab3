from django.shortcuts import render
from .models import Device
from .models import YandexMusic
from .models import mp3Music


def mainpage(request):
    devices = Device.objects.all()
    return render(request, 'mainpage/mainpage.html', {'devices': devices})


def musicpage(request):
    return render(request, 'musicpage/musicpage.html', {'music': YandexMusic.objects.all(), 'mp3s': mp3Music.objects.all() })
