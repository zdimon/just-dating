from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from backend.cent_client import CentClient
from rest_framework.authtoken.models import Token

from account.models import UserProfile



class Like(models.Model):
    liking_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='liking_user')
    liked_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='liked_user')

    @staticmethod
    def like_user(liking_user,liked_user):
       try:
           c = Like.objects.get(liking_user=liking_user,liked_user=liked_user)
       except:
           c = Like.objects.create( \
               liking_user=liking_user, \
               liked_user=liked_user, \
               
           )
