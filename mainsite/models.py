from django.db import models
from django.conf import settings
import os


YANDEX_MUSIC_URL = 'https://music.yandex.ru'


class BaseModelWithName(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# For saving memory
class Picture(BaseModelWithName):
    file = models.ImageField()

    def delete(self, using=None, keep_parents=False):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.file.name))
        super(Picture, self).delete(using, keep_parents)


class Device(BaseModelWithName):
    picture = models.ForeignKey(Picture, on_delete=models.CASCADE, null=True)
    url = models.URLField()


class Artist(models.Model):
    Name = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        artist_list = Artist.objects.filter(Name=self.Name)
        print(len(artist_list))
        if len(artist_list) != 0:
            return 0
        super(Artist, self).save(*args, **kwargs)
        return 1

    def __str__(self):
        return self.Name


class BaseMusic(models.Model):
    class Meta:
        abstract = True

    musicName = models.CharField(max_length=50)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True)

    def full_single_name(self):
        return str(self)

    def __str__(self):
        return str(self.artist) + ' - ' + str(self.musicName)


class YandexMusic(BaseMusic):
    trackInt = models.IntegerField(default=0)
    albumInt = models.IntegerField(default=0)
    artistInt = models.IntegerField(default=0)

    def musicUrlWithGrid(self) -> str:
        return YANDEX_MUSIC_URL + '/iframe/#track/' + str(self.trackInt) + '/' + str(self.albumInt)

    def musicUrl(self) -> str:
        return YANDEX_MUSIC_URL + '/album/' + str(self.albumInt) + '/track/' + str(self.trackInt)

    def artistUrl(self) -> str:
        return YANDEX_MUSIC_URL + '/artist/' + str(self.albumInt)


class mp3Music(BaseMusic):
    musicUrl = models.URLField(default="https://")


class mp3LocalMusic(BaseMusic):
    musicFile = models.FileField()

    def delete(self, using=None, keep_parents=False):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.musicFile.name))
        super(mp3LocalMusic, self).delete(using, keep_parents)
