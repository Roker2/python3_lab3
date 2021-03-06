from django.forms import ModelForm
from django.forms import Form
from django.forms import CharField
from .models import mp3Music
from .models import mp3LocalMusic
from .models import YandexMusic
from .models import Artist
from .models import Device
from .models import Picture


class mp3MusicForm(ModelForm):
    class Meta:
        model = mp3Music
        fields = ['artist', 'musicName', 'musicUrl']


class mp3LocalMusicForm(ModelForm):
    class Meta:
        model = mp3LocalMusic
        fields = ['artist', 'musicName', 'musicFile']


class YandexMusicForm(ModelForm):
    class Meta:
        model = YandexMusic
        fields = ['artist', 'musicName', 'trackInt', 'albumInt', 'artistInt']


class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        fields = ['Name']


class DeviceForm(ModelForm):
    class Meta:
        model = Device
        fields = ['name', 'picture', 'url']


class PictureForm(ModelForm):
    class Meta:
        model = Picture
        fields = ['name', 'file']


class VerifyForm(Form):
    code = CharField(label='Code', max_length=5)
