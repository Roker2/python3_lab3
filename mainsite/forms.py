from django.forms import ModelForm
from .models import mp3Music
from .models import mp3LocalMusic
from .models import Artist


class mp3MusicForm(ModelForm):
    class Meta:
        model = mp3Music
        fields = ['artist', 'musicName', 'musicUrl']


class mp3LocalMusicForm(ModelForm):
    class Meta:
        model = mp3LocalMusic
        fields = ['artist', 'musicName', 'musicFile']


class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        fields = ['Name']
