from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from backend.cent_client import CentClient
from rest_framework.authtoken.models import Token

from account.models import UserProfile



class BlackList(models.Model):
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='blacklist_owner')
    blocked_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='blocked_user')
    created_at = models.DateTimeField(auto_now_add=True)
    
    @staticmethod
    def block_user(owner,blocked):
       try:
           c = BlackList.objects.get(owner=owner,blocked_user=blocked_user)
       except:
           c = BlackList.objects.create( \
               owner=owner, \
               blocked_user=blocked_user, \
               
           )
