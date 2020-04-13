from django.db import models


# Create your models here.
class Device(models.Model):
    name = models.TextField()
    picture = models.ImageField()
    url = models.TextField()


def __str__(self):
    return self.name
