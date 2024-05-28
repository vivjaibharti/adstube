from django.urls import path
from channel import views

urlpatterns=[
    #channel profile
    path("<int:channel_id>/",views.channel_profile,name="channel-profile"),
    #channel videos
    path("channel-videos/<int:channel_id>/",views.channel_videos,name="channel-videos"),
    #channel about
    path("channel-about/<int:channel_id>/",views.channel_about,name="channel-about"),
    #channel community
    path("channel_community/<str:channel_name>/",views.channel_community,name="channel-community")
]