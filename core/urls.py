from django.urls import path
from core import views

urlpatterns = [
    path("",views.index,name="index"),
    path("watch/<int:pk>/",views.videoDetail,name="video-detail"),
    
    #Saving comment to db
    path("ajax-save-comment/",views.ajax_save_comment,name='save-comment'),
    #Deleting comment from db
    path("ajax-delete-comment/",views.ajax_delete_comment,name='delete-comment'),
    #Subscribing and Unsubscribing Channel
    path("subs-unsubs/<int:channel_id>/",views.axios_add_remove_subscribers,name="add-remove-subscribers"),
    #Like Video
    path("like/<int:video_id>/",views.axios_like_video,name="like-video"),
    #Save Video
    path("save-video/<int:video_id>/",views.axios_save_video,name="save-video"),


    
    path("home/",views.homepage),
    path("about/",views.aboutpage,name="about"),
    path("contact/",views.contactpage),

]



