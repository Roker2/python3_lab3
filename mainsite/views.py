from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Artist
from .models import YandexMusic
from .models import mp3Music
from .models import mp3LocalMusic
from .models import Device


def mainpage(request):
    return render(request, 'mainpage/mainpage.html', {})


def musicpage(request):
    return render(request, 'musicpage/musicpage.html',
                  {'music': YandexMusic.objects.all(),
                   'mp3s': mp3Music.objects.all(),
                   'localmp3s': mp3LocalMusic.objects.all()})


def devicespage(request):
    return render(request, 'devicespage/devicespage.html', {'devices': Device.objects.all()})


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
