
from django.urls import re_path, include
from . import views

urlpatterns = [
    re_path(r'^$', views.ShowVideos, name='show_videos_url'),
    re_path(r'^get/(?P<video_id>\d+)/$', views.ShowVideo, name='show_vid_url'), #регулярное выражение
    re_path(r'^AddLike/(?P<video_id>\d+)/$', views.AddLike),
    re_path(r'^AddComment/(?P<video_id>\d+)/$', views.AddCom),
    re_path(r'^AddLike/ajax/$', views.ajax),
]
