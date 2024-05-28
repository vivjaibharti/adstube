from django.db import models
from taggit.managers import TaggableManager

from django.conf import settings
from core.models import user_directory_path

# Create your models here.

User=settings.AUTH_USER_MODEL

STATUS=(
    ("active","Active"),
    ("unactive","Unactive"),
)

class Channel(models.Model):
    image=models.ImageField(upload_to=user_directory_path,null=True,blank=True)
    full_name=models.CharField(max_length=200)
    channel_name=models.CharField(max_length=200)
    description=models.TextField(null=True,blank=True)
    keywords=TaggableManager()
    joined=models.DateTimeField(auto_now_add=True)
    status=models.CharField(choices=STATUS,max_length=100,default="active")
    user=models.OneToOneField(User,on_delete=models.SET_NULL,null=True,related_name="channel")
    subscribers=models.ManyToManyField(User,related_name="user_subs")
    verified=models.BooleanField(default=False)

    total_views = models.IntegerField(default=0)
    
    business_email = models.EmailField(null=True, blank=True)
    make_business_email_public = models.BooleanField(default=False)

    business_location = models.CharField(null=True, blank=True, max_length=500)
    make_business_location_public = models.BooleanField(default=False)

    website = models.URLField(default="https://my-website.com/")
    instagram = models.URLField(default="https://isntagram.com/")
    facebook = models.URLField(default="https://facebook.com/")
    twitter = models.URLField(default="https://twitter.com/")

    def __str__(self):
        return self.channel_name

def user_directory_path(instance,filename):
    return "user_{0}/{1}".format(instance.channel.user.id,filename)


class Community(models.Model):
    channel= models.ForeignKey(Channel,on_delete=models.CASCADE)
    image=models.ImageField(upload_to=user_directory_path,null=True,blank=True)
    content=models.TextField(null=True,blank=True)
    date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=100,choices=STATUS,default="active")
    likes=models.ManyToManyField(User)

    def __str__(self):
        return self.channel.channel_name
    
    class Meta:
        verbose_name="Community"
        verbose_name_plural="Community Posts"