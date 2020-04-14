from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('favoritemusic', views.musicpage, name='musicpage'),
    path('devices', views.devicespage, name='devicespage'),
]