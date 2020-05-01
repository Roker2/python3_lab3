from django.db import models
from django.conf import settings
import os


# For saving memory
class Picture(models.Model):
    name = models.CharField(max_length=50)
    file = models.ImageField()

    def delete(self, using=None, keep_parents=False):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.file.name))
        super(Picture, self).delete(using, keep_parents)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name


class Device(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ForeignKey(Picture, on_delete=models.CASCADE, null=True)
    url = models.URLField()

    def publish(self):
        self.save()

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


class YandexMusic(models.Model):
    musicName = models.CharField(max_length=50)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True)
    trackInt = models.IntegerField(default=0)
    albumInt = models.IntegerField(default=0)
    artistInt = models.IntegerField(default=0)

    def musicUrlWithGrid(self) -> str:
        return 'https://music.yandex.ru/iframe/#track/' + str(self.trackInt) + '/' + str(self.albumInt)

    def musicUrl(self) -> str:
        return 'https://music.yandex.ru/album/' + str(self.albumInt) + '/track/' + str(self.trackInt)

    def artistUrl(self) -> str:
        return 'https://music.yandex.ru/artist/' + str(self.albumInt)

    def publish(self):
        self.save()

    def __str__(self):
        return str(self.artist) + ' - ' + str(self.musicName)


class mp3Music(models.Model):
    musicUrl = models.URLField()
    musicName = models.CharField(max_length=50)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True)

    def publish(self):
        self.save()

    def fullsinglename(self):
        return str(self)

    def __str__(self):
        return str(self.artist) + ' - ' + str(self.musicName)


class mp3LocalMusic(models.Model):
    musicFile = models.FileField()
    musicName = models.CharField(max_length=50)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True)

    def delete(self, using=None, keep_parents=False):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.musicFile.name))
        super(mp3LocalMusic, self).delete(using, keep_parents)

    def publish(self):
        self.save()

    def fullsinglename(self):
        return str(self)

    def __str__(self):
        return str(self.artist) + ' - ' + str(self.musicName)
