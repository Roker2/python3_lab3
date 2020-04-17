from django.db import models


# Create your models here.
class Device(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField()
    url = models.URLField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.name


class YandexMusic(models.Model):
    artistName = models.CharField(max_length=50)
    musicName = models.CharField(max_length=50)
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
        return self.artistName + ' - ' + self.musicName


class mp3Music(models.Model):
    musicUrl = models.URLField()
    musicName = models.CharField(max_length=50)
    artistName = models.CharField(max_length=50)

    def publish(self):
        self.save()

    def fullsinglename(self):
        return str(self)

    def __str__(self):
        return self.artistName + ' - ' + self.musicName
