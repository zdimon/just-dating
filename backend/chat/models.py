from django.db import models
from account.models import UserProfile
import uuid 
from backend.celery import app
# channels
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from rest_framework.authtoken.models import Token

class ChatRoom(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    token = models.CharField(max_length=250,  default='', db_index=True)
    search_key = models.CharField(max_length=250, db_index=True)

    def get_participants(self):
        out = []
        c2us = ChatRoom2User.objects.filter(room=self) 
        for c2u in c2us:
            out.append(c2u.user)
        return out

    @staticmethod
    def get_or_create(user_one, user_two):
        #search_key = '%s-%s|%s-%s' % (user_one.id, user_two.id, user_two.id, user_one.id)
        search_key = '%s-%s' % (user_one.id, user_two.id)
        try:
            room = ChatRoom.objects.get(search_key__contains = search_key)
        except:
            search_key = '%s-%s|%s-%s' % (user_one.id, user_two.id, user_two.id, user_one.id)
            room = ChatRoom()
            room.search_key = search_key
            room.token = uuid.uuid1()
            room.save()
            r2u = ChatRoom2User()
            r2u.user = user_one
            r2u.room = room
            r2u.save()
            r2u = ChatRoom2User()
            r2u.user = user_two
            r2u.room = room
            r2u.save()
        return room

class ChatRoom2User(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)

class ChatMessage(models.Model):
    token = models.CharField(max_length=250,  default='', db_index=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    message =  models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_readed = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.pk:
           self.token = self.room.token
        super(ChatMessage, self).save(*args, **kwargs)
        self.send_chat_message(self.pk)

    @app.task
    def send_chat_message(id):
        print('Sending message %s' % id)
        from chat.serializers.message import ChatRoomMessageSerializer
        channel_layer = get_channel_layer()
        message  = ChatMessage.objects.get(pk=id)
        room = message.room
        for user in room.get_participants():
            token, created = Token.objects.get_or_create(user=user)
            async_to_sync(channel_layer.group_send)( \
                token.key, \
                { \
                    'type': 'chat_message', \
                    'message': ChatRoomMessageSerializer(message).data \
                })        