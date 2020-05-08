from django.db import models
from django.conf import settings
from . import base_models
import os


YANDEX_MUSIC_URL = 'https://music.yandex.ru'


# For saving memory
class Picture(models.Model):
    name = models.CharField(max_length=50)
    file = models.ImageField()

    def delete(self, using=None, keep_parents=False):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.file.name))
        super(Picture, self).delete(using, keep_parents)

    def __str__(self):
        return self.name


class Device(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ForeignKey(Picture, on_delete=models.CASCADE, null=True)
    url = models.URLField()

    def __str__(self):
        return self.name


class Artist(models.Model):
    Name = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        ArtistList = Artist.objects.filter(Name=self.Name)
        print(len(ArtistList))
        if len(ArtistList) != 0:
            return 0
        super(Artist, self).save(*args, **kwargs)
        return 1

    def __str__(self):
        return self.Name


class YandexMusic(base_models.BaseMusic):
    trackInt = models.IntegerField(default=0)
    albumInt = models.IntegerField(default=0)
    artistInt = models.IntegerField(default=0)

    def musicUrlWithGrid(self) -> str:
        return YANDEX_MUSIC_URL + '/iframe/#track/' + str(self.trackInt) + '/' + str(self.albumInt)

    def musicUrl(self) -> str:
        return YANDEX_MUSIC_URL + '/album/' + str(self.albumInt) + '/track/' + str(self.trackInt)

    def artistUrl(self) -> str:
        return YANDEX_MUSIC_URL + '/artist/' + str(self.albumInt)


class mp3Music(base_models.BaseMusic):
    musicUrl = models.URLField(default="https://")


class mp3LocalMusic(base_models.BaseMusic):
    musicFile = models.FileField()

    def delete(self, using=None, keep_parents=False):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.musicFile.name))
        super(mp3LocalMusic, self).delete(using, keep_parents)
