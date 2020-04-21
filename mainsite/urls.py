from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('favoritemusic', views.musicpage, name='musicpage'),
    path('devices', views.devicespage, name='devicespage'),
    path('artist', views.ArtistList.as_view(), name='artist_list'),
    path('artist/<int:pk>', views.ArtistDetail.as_view(), name='artist_detail'),
    path('create', views.ArtistCreate.as_view(), name='artist_create'),
    path('edit/<int:pk>', views.ArtistUpdate.as_view(), name='artist_edit'),
    path('delete/<int:pk>', views.ArtistDelete.as_view(), name='artist_delete'),
]