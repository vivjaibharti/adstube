from django.db import models
from django.contrib.auth.models import AbstractUser
from core.models import Video
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class User(AbstractUser):
    email=models.EmailField(unique=True,null=True)
    username=models.CharField(max_length=100)

    USERNAME_FIELD="email"
    REQUIRED_FIELDS=["username"]

    def __str__(self):
        return self.username

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    saved_videos=models.ManyToManyField(Video, blank=True)

    def __str__(self):
        return self.user.username
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()
    else:
        pass