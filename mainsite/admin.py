from django.contrib import admin
from .models import Picture
from .models import Device
from .models import YandexMusic
from .models import mp3Music
from .models import Artist
from .models import mp3LocalMusic
from .models import Profile

# Register your models here.

admin.site.register(Picture)
admin.site.register(Device)
admin.site.register(YandexMusic)
admin.site.register(mp3Music)
admin.site.register(Artist)
admin.site.register(mp3LocalMusic)
admin.site.register(Profile)
