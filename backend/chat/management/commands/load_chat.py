from django.core.management.base import BaseCommand, CommandError
from backend.settings import FIXTURES_PATH
import json
from account.models import UserProfile
import requests
from backend.settings import API_URL
import os
from chat.models import ChatMessage, ChatRoom
from rest_framework.authtoken.models import Token
from rest_framework.test import APIRequestFactory
factory = APIRequestFactory()
from rest_framework.test import force_authenticate
from chat.views.room import GetRoomView
from chat.views.message import CreateRoomMessageView

class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Loading chat rooms')
        user_file = os.path.join(FIXTURES_PATH, 'users.json')
        with open(user_file,'r') as f:
            jdata = json.loads(f.read())
            ChatRoom.objects.all().delete()
            ChatMessage.objects.all().delete()
            for female_user in jdata['female']:
                female_user = UserProfile.objects.get(username=female_user['username'])
                token, created = Token.objects.get_or_create(user=female_user)
                headers = {'Authorization': 'Token %s' % token.key}
                
                for male_user in jdata['male']:
                    male_user = UserProfile.objects.get(username=male_user['username'])
                    url = API_URL+'chat/get_room/%s' % male_user.id
                    print(url)
                    request = factory.get(url)
                    force_authenticate(request, user=female_user)
                    rez = GetRoomView.as_view()(request, user_id=male_user.id)
                    rez.render()

                    room_out = json.loads(rez.content)
                    print('chat room %s was created' % room_out['id'])
                    data = {"room": room_out['id'], "token": room_out['token'], "message": "Hello from %s" % female_user.username}
                    
                    url = API_URL+'chat/create_message/'
                    request = factory.post(url,data)
                    force_authenticate(request, user=female_user)
                    rez = CreateRoomMessageView.as_view()(request)
                    rez.render()
                    message_out = json.loads(rez.content)
                    print('Message: %s' % message_out['message'])


            for female_user in jdata['male']:
                female_user = UserProfile.objects.get(username=female_user['username'])
                token, created = Token.objects.get_or_create(user=female_user)
                headers = {'Authorization': 'Token %s' % token.key}
                
                for male_user in jdata['female']:
                    male_user = UserProfile.objects.get(username=male_user['username'])
                    url = API_URL+'chat/get_room/%s' % male_user.id
                    print(url)
                    request = factory.get(url)
                    force_authenticate(request, user=female_user)
                    rez = GetRoomView.as_view()(request, user_id=male_user.id)
                    rez.render()

                    room_out = json.loads(rez.content)
                    print('chat room %s was created' % room_out['id'])
                    data = {"room": room_out['id'], "token": room_out['token'], "message": "Hello from %s" % female_user.username}
                    
                    url = API_URL+'chat/create_message/'
                    request = factory.post(url,data)
                    force_authenticate(request, user=female_user)
                    rez = CreateRoomMessageView.as_view()(request)
                    rez.render()
                    message_out = json.loads(rez.content)
                    print('Message: %s' % message_out['message'])
                    

       