from django.urls import path
from core import views

urlpatterns = [
    path("",views.index,name="index"),
    path("watch/<int:pk>/",views.videoDetail,name="video-detail"),
    
    #Saving comment to db
    path("ajax-save-comment/",views.ajax_save_comment,name='save-comment'),
    #Deleting comment from db
    path("ajax-delete-comment/",views.ajax_delete_comment,name='delete-comment'),


    
    path("home/",views.homepage),
    path("about/",views.aboutpage,name="about"),
    path("contact/",views.contactpage),

]



