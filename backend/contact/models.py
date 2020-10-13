from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from backend.cent_client import CentClient
from rest_framework.authtoken.models import Token

from account.models import UserProfile
from chat.models import ChatRoom


class Contact(models.Model):
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='owner')
    contact_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='contact_user')
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)

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
        cent_client.send(token.key, payload)