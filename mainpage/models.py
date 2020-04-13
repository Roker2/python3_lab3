from django.db import models


# Create your models here.
class Device(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField()
    url = models.TextField()


def publish(self):
    self.save()


def __str__(self):
    return self.name
