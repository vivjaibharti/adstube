from django.shortcuts import render,get_object_or_404
from channel.models import Channel,Community
from core.models import Video


# Create your views here.

def channel_profile(request,channel_id):
    channel=get_object_or_404(Channel,id=channel_id)
    video=Video.objects.filter(user=channel.user,visibility="public").order_by("-views")
    try:
        feature_video=video.get(featured=True)
    except:
        pass
    context={
        'channel':channel,
        'video':video,
        'featured_video':feature_video
    }
    return render(request,"channel/channel.html",context)

def channel_videos(request,channel_id):
    channel=get_object_or_404(Channel,id=channel_id)
    video=Video.objects.filter(user=channel.user,visibility="public").order_by("-date")
    context={
        'channel':channel,
        'video':video
    }

    return render(request,"channel/channel-videos.html",context)


def channel_about(request,channel_id):
    channel=get_object_or_404(Channel,id=channel_id)
    # video=Video.objects.filter(user=channel.user,visibility="public")
    context={
        'channel':channel
    }
    return render(request,'channel/channel-about.html',context)

def channel_community(request, channel_name):
    channel=get_object_or_404(Channel,channel_name=channel_name)
    community=Community.objects.filter(channel=channel, status="active").order_by("-date")
    context={
        "community":community,
        'channel':channel
    }
    return render(request, "channel/channel-community.html", context)