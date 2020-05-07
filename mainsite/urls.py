from django.urls import path
from . import views
from . import artist_views

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('favoritemusic', views.musicpage, name='musicpage'),
    path('devices', views.devicespage, name='devicespage'),
    path('artist', artist_views.ArtistList.as_view(), name='artist_list'),
    path('artist/<int:pk>', artist_views.ArtistDetail.as_view(), name='artist_detail'),
    path('create', artist_views.ArtistCreate.as_view(), name='artist_create'),
    path('edit/<int:pk>', artist_views.ArtistUpdate.as_view(), name='artist_edit'),
    path('delete/<int:pk>', artist_views.ArtistDelete.as_view(), name='artist_delete'),
    path('uploadpic', views.UploadPic.as_view(), name="uploadpic"),
    path('piclist', views.PicturesList.as_view(), name='piclist'),
    path('pic_delete/<int:pk>', views.PicturesDelete.as_view(), name='pic_delete'),
    path('adddevice', views.add_device, name='adddevice'),
    path('addyandex', views.add_yandex_music, name='addyandex'),
    path('addmp3', views.add_mp3, name='addmp3'),
    path('addlocalmp3', views.add_local_mp3, name='addlocalmp3'),
]
