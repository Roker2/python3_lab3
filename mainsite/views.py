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
from .forms import ArtistForm


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
            artistform.save(commit=True)
            return redirect(reverse_lazy('addmp3'))
    else:
        form = mp3MusicForm()
        artistform = ArtistForm()
        return render(request, 'mp3music_crud/mp3music_create.html', {'form': form,
                                                                      'artistform': artistform})


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


class AddDevice(CreateView):
    model = Device
    template_name = 'device_crud/device_create.html'
    fields = ['name', 'picture', 'url']


class AddYandexMusic(CreateView):
    model = YandexMusic
    template_name = 'yandexmusic_crud/yandexmusic_create.html'
    fields = ['musicName', 'artist', 'trackInt', 'albumInt', 'artistInt']


class Addmp3LocalMusic(CreateView):
    model = mp3LocalMusic
    template_name = 'base_form/base_form.html'
    fields = ['artist', 'musicName', 'musicFile']
