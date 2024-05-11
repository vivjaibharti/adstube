from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from core.models import Video,Comment
from channel.models import Channel
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    video=Video.objects.filter(visibility="public")
    context={
        "video":video
    }
    #return HttpResponse("Hello world")
    return render(request,"index.html",context)


#Function for video-detail.html 
def videoDetail(request,pk):
    video=Video.objects.get(id=pk)

    video.views=video.views + 1
    video.save()
    
    #Getting all comments related to this video
    comment=Comment.objects.filter(active=True, video=video.id).order_by("-date")

    context={
        "video":video,
        "comment":comment,
    }
    return render(request,"video-detail.html",context)


#Saving Comment
def ajax_save_comment(request):

    if request.method=="POST":
        pk=request.POST.get("id")

        comment=request.POST.get("comment")
        video=Video.objects.get(id=pk)
        user=request.user

        new_comment=Comment.objects.create(comment=comment,user=user,video=video)
        new_comment.save()

        comments_count=Comment.objects.filter(video=video).count()
        new_comment_id=new_comment.id

        # comments_count=int(comments_count)

        response="Comment Posted"

        return JsonResponse({'comments_count':comments_count,'new_comment_id':new_comment_id})


#Deleting Comment
@csrf_exempt
def ajax_delete_comment(request):
    if request.method=="POST":
        id=request.POST.get("cid")
        comment=Comment.objects.get(id=id)
        #Deriving video_id through the comment object
        video_id=comment.video
        #Deleting the comment from db
        comment.delete()

        #Counting the no. of. comments
        comments_count=Comment.objects.filter(video=video_id).count()

        return JsonResponse({"status":1,"comments_count":comments_count})

    else:
        return JsonResponse({"status":0})
    

#Adding-Removing Subscribers
def axios_add_remove_subscribers(request,channel_id):
    user=request.user
    channel=Channel.objects.get(id=channel_id)

    if user in channel.subscribers.all():
        channel.subscribers.remove(user)
        response="Unsubscribe"
        count_subscribers=channel.subscribers.all().count()
        return JsonResponse({'status':0,'response':response,'count_subscribers':count_subscribers})
    else:
        channel.subscribers.add(user)
        response="Unsubscribe"
        count_subscribers=channel.subscribers.count()      
        return JsonResponse({'status':1,'response':response,'count_subscribers':count_subscribers})

#Like Video
def axios_like_video(request,video_id):
    user=request.user
    video=Video.objects.get(id=video_id)

    if user in video.likes.all():
        video.likes.remove(user)
        count_likes=video.likes.count()
        status=0
        return JsonResponse({'status':status,'count_likes':count_likes})
    else:
        video.likes.add(user)
        count_likes=video.likes.count()
        status=1
        return JsonResponse({'status':status,'count_likes':count_likes})        










def homepage(request):
    return render(request, "test_temp/index.html")

def aboutpage(request):
    return render(request,"test_temp/about.html")

def contactpage(request):
    return render(request,"test_temp/contact.html")