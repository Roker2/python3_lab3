from django.contrib import admin
from .models import Device
from .models import YandexMusic
from .models import mp3Music

# Register your models here.

admin.site.register(Device)
admin.site.register(YandexMusic)
admin.site.register(mp3Music)