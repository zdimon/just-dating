from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from backend.cent_client import CentClient
from rest_framework.authtoken.models import Token

from account.models import UserProfile



class Favourite(models.Model):
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='favourite_owner')
    favourite_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='favourite_user')
    created_at = models.DateTimeField(auto_now_add=True)
    
    @staticmethod
    def add_favourite(owner,favourite):
       try:
           c = Favourite.objects.get(owner=owner,favourite_user=favourite)
       except:
           c = Favourite.objects.create( \
               owner=owner, \
               favourite_user=favourite, \
               
           )
