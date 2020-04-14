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
    musicUrlWithGrid = models.URLField()
    musicUrl = models.URLField()
    musicName = models.CharField(max_length=50)
    artistUrl = models.URLField()
    artistName = models.CharField(max_length=50)

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

    def __str__(self):
        return self.artistName + ' - ' + self.musicName
