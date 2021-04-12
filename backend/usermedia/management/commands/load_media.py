from django.core.management.base import BaseCommand, CommandError
from backend.settings import FIXTURES_PATH
import json
from account.models import UserProfile
from usermedia.models import UserMedia
import requests
from backend.settings import API_URL
from rest_framework.authtoken.models import Token
import os


def get_user_token(username):
    user = UserProfile.objects.get(username=username)
    token = Token.objects.get_or_create(user=user)
    return token

class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Loading images')
        usertypes = ['male', 'female']
        user_file = os.path.join(FIXTURES_PATH, 'users.json')
        with open(user_file,'r') as f:
            jdata = json.loads(f.read())
            UserMedia.objects.all().delete()
            for type in usertypes:
                for user in jdata[type]:
                    token = get_user_token(user['username'])
                    for image in user['images']:
                        filepath = os.path.join(FIXTURES_PATH, 'images', '%s.jpg' % user['username'])
                        files = {'image': open(filepath,'rb')}
                        print(image)
                        rez = requests.post( \
                            API_URL+'usermedia/add_image', \
                            data=image, \
                            files=files, \
                            headers={'Authorization': 'Token %s' % token[0].key})
                        if rez.status_code == 200:
                            print(json.loads(rez.text))
                        else:
                            print('Error!')
                            print(rez.text)

           