from django.db import models


class BaseMusic(models.Model):
    class Meta:
        abstract = True

    musicName = models.CharField(max_length=50)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True)

    def fullsinglename(self):
        return str(self)

    def __str__(self):
        return str(self.artist) + ' - ' + str(self.musicName)
