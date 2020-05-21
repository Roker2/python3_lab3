import logging

from django.contrib import admin
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings

from .models import Picture
from .models import Device
from .models import YandexMusic
from .models import mp3Music
from .models import Artist
from .models import mp3LocalMusic
from .models import Profile

VERIFY_URL = 'http://127.0.0.1:8000/accounts/verify/?code='

# Register your models here.

admin.site.register(Picture)
admin.site.register(Device)
admin.site.register(YandexMusic)
admin.site.register(mp3Music)
admin.site.register(Artist)
admin.site.register(mp3LocalMusic)


def send_verify_mail(modeladmin, request, queryset):
    for profile in queryset:
        logging.debug(profile.__class__)
        logging.debug(profile.user.email)
        if not profile.verified:
            send_mail(
                'Verification',
                'Hi! You need verify your account. Go to the ' + VERIFY_URL + str(profile.code),
                settings.EMAIL_HOST_USER,
                [profile.user.email],
                fail_silently=False,
            )


send_verify_mail.short_description = 'Sending mails'


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'verified']
    ordering = ['user']
    actions = [send_verify_mail]


admin.site.register(Profile, ProfileAdmin)
