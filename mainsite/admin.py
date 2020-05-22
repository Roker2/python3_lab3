import datetime
import logging

from django.contrib import admin

from .models import Picture
from .models import Device
from .models import YandexMusic
from .models import mp3Music
from .models import Artist
from .models import mp3LocalMusic
from .models import Profile
from .utils import send_mail_from_template

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
        # logging
        logging.debug(profile.__class__)
        logging.debug(profile.user.email)

        if not profile.verified:
            send_mail_from_template('Verification', {'username': profile.user.username, 'url': VERIFY_URL + str(profile.code),
                                               'time': datetime.datetime.now().strftime('%H:%M:%S'),
                                               'user_mail': profile.user.email},
                                    'mainsite/templates/mails/verification.txt', [profile.user.email])


send_verify_mail.short_description = 'Sending mails'


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'verified']
    ordering = ['user']
    actions = [send_verify_mail]


admin.site.register(Profile, ProfileAdmin)
