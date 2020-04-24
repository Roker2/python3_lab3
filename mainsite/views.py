from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from .models import Artist
from .models import YandexMusic
from .models import mp3Music
from .models import mp3LocalMusic
from .models import Device
from .models import Picture
from .forms import mp3MusicForm
from .forms import mp3LocalMusicForm
from .forms import YandexMusicForm
from .forms import ArtistForm
from .forms import DeviceForm
from .forms import PictureForm


def mainpage(request):
    return render(request, 'mainpage/mainpage.html', {})


def musicpage(request):
    return render(request, 'musicpage/musicpage.html',
                  {'music': YandexMusic.objects.all(),
                   'mp3s': mp3Music.objects.all(),
                   'localmp3s': mp3LocalMusic.objects.all()})


def devicespage(request):
    return render(request, 'devicespage/devicespage.html', {'devices': Device.objects.all()})


def add_mp3(request):
    if request.method == 'POST':
        form = mp3MusicForm(request.POST)
        artistform = ArtistForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect(reverse_lazy('musicpage'))
        if artistform.is_valid():
            artist = artistform.save(commit=False)
            if artist.save():
                return redirect(reverse_lazy('addmp3'))
            else:
                request.method = None
                form = mp3MusicForm()
                return render(request, 'mp3music_crud/mp3music_create_is_exist.html', {'form': form,
                                                                              'artistform': artistform})
    else:
        form = mp3MusicForm()
        artistform = ArtistForm()
        return render(request, 'mp3music_crud/mp3music_create.html', {'form': form,
                                                                      'artistform': artistform})


def add_local_mp3(request):
    if request.method == 'POST':
        form = mp3LocalMusicForm(request.POST)
        artistform = ArtistForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect(reverse_lazy('musicpage'))
        if artistform.is_valid():
            artist = artistform.save(commit=False)
            if artist.save():
                return redirect(reverse_lazy('addlocalmp3'))
            else:
                request.method = None
                form = mp3LocalMusicForm()
                return render(request, 'mp3music_crud/mp3music_create_is_exist.html', {'form': form,
                                                                              'artistform': artistform})
    else:
        form = mp3LocalMusicForm()
        artistform = ArtistForm()
        return render(request, 'mp3music_crud/mp3music_create.html', {'form': form,
                                                                      'artistform': artistform})


def add_yandex_music(request):
    if request.method == 'POST':
        form = YandexMusicForm(request.POST)
        artistform = ArtistForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect(reverse_lazy('musicpage'))
        if artistform.is_valid():
            artist = artistform.save(commit=False)
            if artist.save():
                return redirect(reverse_lazy('addyandex'))
            else:
                request.method = None
                form = YandexMusicForm()
                return render(request, 'yandexmusic_crud/yandexmusic_create_is_exist.html', {'form': form,
                                                                              'artistform': artistform})
    else:
        form = YandexMusicForm()
        artistform = ArtistForm()
        return render(request, 'yandexmusic_crud/yandexmusic_create.html', {'form': form,
                                                                      'artistform': artistform})


def add_device(request):
    if request.method == 'POST':
        deviceform = DeviceForm(request.POST)
        pictureform = PictureForm(request.POST)
        if deviceform.is_valid():
            deviceform.save(commit=True)
            return redirect(reverse_lazy('devicespage'))
        if pictureform.is_valid():
            pictureform.save(commit=True)
            return redirect(reverse_lazy('adddevice'))
    else:
        deviceform = DeviceForm()
        pictureform = PictureForm()
        return render(request, 'device_crud/device_create.html', {'form': deviceform,
                                                                  'pictureform': pictureform})


class ArtistList(ListView):
    model = Artist
    template_name = 'artist_crud/artist_list.html'


class ArtistDetail(DetailView):
    model = Artist
    template_name = 'artist_crud/artist_details.html'


class ArtistCreate(CreateView):
    model = Artist
    template_name = 'artist_crud/artist_form.html'
    fields = ['Name']
    success_url = reverse_lazy('artist_list')


class ArtistUpdate(UpdateView):
    model = Artist
    template_name = 'artist_crud/artist_form.html'
    fields = ['Name']
    success_url = reverse_lazy('artist_list')


class ArtistDelete(DeleteView):
    model = Artist
    template_name = 'artist_crud/artist_confirm_delete.html'
    success_url = reverse_lazy('artist_list')


class UploadPic(CreateView):
    model = Picture
    template_name = 'picture_crud/picture_create.html'
    fields = ['name', 'file']
    reverse_lazy('')

    def set_success_url(self, url):
        self.success_url = reverse_lazy(url)
