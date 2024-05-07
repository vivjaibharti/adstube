from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from core.models import Video,Comment

# Create your views here.

def index(request):
    video=Video.objects.filter(visibility="public")
    context={
        "video":video
    }
    #return HttpResponse("Hello world")
    return render(request,"index.html",context)

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
        # comments_count=int(comments_count)

        response="Comment Posted"

        return JsonResponse({'comments_count':comments_count})

#Deleting Comment
def ajax_delete_comment(request):
    if request.method=="POST":
        id=request.POST.get("cid")
        comment=Comment.objects.get(id=id)
        #Deriving video_id through the comment object
        video_id=comment.video
        comment.delete()

        comments_count=Comment.objects.filter(video=video_id).count()

        return JsonResponse({"status":1,"comments_count":comments_count})

    else:
        return JsonResponse({"status":0})








def homepage(request):
    return render(request, "test_temp/index.html")

def aboutpage(request):
    return render(request,"test_temp/about.html")

def contactpage(request):
    return render(request,"test_temp/contact.html")