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

    @staticmethod
    def add_contact(owner,contact):
       try:
           c = Contact.objects.get(owner=owner,contact_user=contact)
       except:
           c = Contact.objects.create( \
               owner=owner, \
               contact_user=contact, \
               room = ChatRoom.get_or_create(owner,contact) \
           )

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

class ContactRequest(models.Model):
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='cr_owner')
    contact_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='cr_contact_user')
    is_accepted = models.BooleanField(default=False)
    is_refused = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)