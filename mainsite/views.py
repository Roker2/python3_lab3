from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views import View
from .models import YandexMusic
from .models import mp3Music
from .models import mp3LocalMusic
from .models import Device
from .forms import DeviceForm
from .forms import PictureForm


class MainPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'mainpage/mainpage.html', {})


class MusicPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'musicpage/musicpage.html',
                      {'music': YandexMusic.objects.all(),
                       'mp3s': mp3Music.objects.all(),
                       'localmp3s': mp3LocalMusic.objects.all()})


class DevicePageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'devicespage/devicespage.html', {'devices': Device.objects.all()})


def add_device(request):
    if request.method == 'POST':
        print(request.FILES)
        deviceform = DeviceForm(request.POST)
        pictureform = PictureForm(request.POST, request.FILES)
        if deviceform.is_valid():
            deviceform.save(commit=True)
            return redirect(reverse_lazy('devicespage'))
        if pictureform.is_valid():
            pictureform.save()
            return redirect(reverse_lazy('adddevice'))
    else:
        pictureform = PictureForm()
    deviceform = DeviceForm()
    return render(request, 'device_crud/device_create.html', {'form': deviceform,
                                                              'pictureform': pictureform})

