
from django.urls import re_path, include
from . import views

urlpatterns = [
    re_path(r'^$', views.ShowVideos),
    re_path(r'^get/(?P<video_id>\d+)/$', views.ShowVideo), #регулярное выражение
    re_path(r'^AddLike/(?P<video_id>\d+)/$', views.AddLike),
    re_path(r'^AddComment/(?P<video_id>\d+)/$', views.AddCom),
    re_path(r'^AddLike/ajax/$', views.ajax)
]
