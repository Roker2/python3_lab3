from django.urls import path
from . import views
from . import artist_views
from . import picture_views
from . import music_views

urlpatterns = [
    path('', views.MainPageView.as_view(), name='mainpage'),
    path('favoritemusic', views.MusicPageView.as_view(), name='musicpage'),
    path('devices', views.DevicePageView.as_view(), name='devicespage'),
    path('artist', artist_views.ArtistList.as_view(), name='artist_list'),
    path('artist/<int:pk>', artist_views.ArtistDetail.as_view(), name='artist_detail'),
    path('create', artist_views.ArtistCreate.as_view(), name='artist_create'),
    path('edit/<int:pk>', artist_views.ArtistUpdate.as_view(), name='artist_edit'),
    path('delete/<int:pk>', artist_views.ArtistDelete.as_view(), name='artist_delete'),
    path('uploadpic', picture_views.UploadPic.as_view(), name="uploadpic"),
    path('piclist', picture_views.PicturesList.as_view(), name='piclist'),
    path('pic_delete/<int:pk>', picture_views.PicturesDelete.as_view(), name='pic_delete'),
    path('adddevice', views.add_device, name='adddevice'),
    path('addyandex', music_views.AddYandexMusicView.as_view(), name='addyandex'),
    path('addmp3', music_views.AddMp3View.as_view(), name='addmp3'),
    path('addlocalmp3', music_views.AllLocalMp3View.as_view(), name='addlocalmp3'),
]
