from .forms import mp3MusicForm
from .forms import mp3LocalMusicForm
from .forms import YandexMusicForm
from .forms import ArtistForm
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View


class AddMp3View(View):
    def post(self, request):
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

    def get(self, request):
        form = mp3MusicForm()
        artistform = ArtistForm()
        return render(request, 'mp3music_crud/mp3music_create.html', {'form': form,
                                                                      'artistform': artistform})


class AllLocalMp3View(View):
    def post(self, request):
        form = mp3LocalMusicForm(request.POST, request.FILES)
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

    def get(self, request):
        form = mp3LocalMusicForm()
        artistform = ArtistForm()
        return render(request, 'mp3music_crud/mp3music_create.html', {'form': form,
                                                                      'artistform': artistform})


class AddYandexMusicView(View):
    def post(self, request):
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

    def get(self, request):
        form = YandexMusicForm()
        artistform = ArtistForm()
        return render(request, 'yandexmusic_crud/yandexmusic_create.html', {'form': form,
                                                                            'artistform': artistform})
