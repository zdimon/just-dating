from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from backend.cent_client import CentClient
from rest_framework.authtoken.models import Token
from usermedia.models import UserMedia
from account.models import UserProfile



class LikeMedia(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='liker')
    media = models.ForeignKey(UserMedia, on_delete=models.CASCADE, related_name='user_media')
    created_at = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def get(user,image):
       try:
           c = LikeMedia.objects.get(user=user,media=image)
       except:
           c = LikeMedia.objects.create( \
               user=user, \
               media=image, \
               
           )
