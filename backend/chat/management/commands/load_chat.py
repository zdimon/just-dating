from django.core.management.base import BaseCommand, CommandError
from backend.settings import FIXTURES_PATH
import json
from account.models import UserProfile
import requests
from backend.settings import API_URL
import os
from chat.models import ChatMessage, ChatRoom
from rest_framework.authtoken.models import Token

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
                    rez = requests.get(API_URL+'chat/get_room/%s' % male_user.id, headers=headers)
                    room_out = json.loads(rez.text)
                    print('chat room %s was created' % room_out['id'])
                    data = {"room": room_out['id'], "message": "Hello from %s" % female_user.username}
                    rez = requests.post(API_URL+'chat/create_message/', json=data, headers=headers)
                    message_out = json.loads(rez.text)
                    print('Message: %s' % message_out['message'])