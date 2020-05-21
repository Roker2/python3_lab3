from django.urls import path, include
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
    path('adddevice', views.AddDeviceView.as_view(), name='adddevice'),
    path('addyandex', music_views.AddYandexMusicView.as_view(), name='addyandex'),
    path('addmp3', music_views.AddMp3View.as_view(), name='addmp3'),
    path('addlocalmp3', music_views.AllLocalMp3View.as_view(), name='addlocalmp3'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/verify/', views.VerifyProfile.as_view(), name='verify'),
]

"""
accounts/login/ [name='login']
accounts/logout/ [name='logout']
accounts/password_change/ [name='password_change']
accounts/password_change/done/ [name='password_change_done']
accounts/password_reset/ [name='password_reset']
accounts/password_reset/done/ [name='password_reset_done']
accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
accounts/reset/done/ [name='password_reset_complete']
"""
"""
path('registration/login/$', 'django.contrib.auth.views.login', name='login'),
path('registration/logout/$', 'django.contrib.auth.views.logout', name='logout'),
path('registration/logout-then-login/$', 'django.contrib.auth.views.logout_then_login', name='logout_then_login'),
"""