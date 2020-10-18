from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from backend.cent_client import CentClient
from rest_framework.authtoken.models import Token

from account.models import UserProfile
from chat.models import ChatRoom
from likeuser.models import Like

class Sympathy(models.Model):
    user1 = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user_one')
    user2 = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user_two')
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    @staticmethod
    def add_sympathy(user_one,user_two):
       
       try:
           c = Sympathy.objects.get(user1=user_one,user2=user_two)
       except:
           c = Sympathy.objects.create( \
               user1=user_one, \
               user2=user_two, \
               room = ChatRoom.get_or_create(user_two,user_two) \
           )


""" 
@receiver(post_save, sender=Contact)
def send_contact_message_created(sender, instance, created, **kwargs):
    from contact.serializers.contact import ContactSerializer
    if created:
        cent_client = CentClient()
        token, created = Token.objects.get_or_create(user=instance.owner)
        payload =  { \
                    'type': 'contact_created_message', \
                    'message': ContactSerializer(instance).data \
                    }
        try:    
            cent_client.send(token.key, payload)
        except:
            pass 
        
"""