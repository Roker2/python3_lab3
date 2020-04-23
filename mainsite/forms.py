from django.forms import ModelForm
from .models import mp3Music
from .models import Artist


class mp3MusicForm(ModelForm):
    class Meta:
        model = mp3Music
        fields = ['artist', 'musicName', 'musicUrl']


class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        fields = ['Name']
