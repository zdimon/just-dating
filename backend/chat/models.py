from django.db import models
from account.models import UserProfile
import uuid 

class ChatRoom(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    token = models.CharField(max_length=250,  default='')
    search_key = models.CharField(max_length=250, db_index=True)
    
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