from django.core.management.base import BaseCommand, CommandError
from backend.settings import FIXTURES_PATH
import json
from account.models import UserProfile
import requests
from backend.settings import API_URL


class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Loading users')
        with open(FIXTURES_PATH,'r') as f:
            jdata = json.loads(f.read())
            UserProfile.objects.all().delete()
            for user in jdata['administratiors']:
                profile = UserProfile()
                profile.username = user['username']
                profile.set_password(user['password'])
                profile.publicname = user['username']
                profile.is_staff = True
                profile.is_superuser = True
                profile.is_superuser = True
                profile.save()
                print('Creating ... %s' % user['username'])

            for user in jdata['female']:
                rez = requests.post(API_URL+'account/registration', json=user)
                print(json.loads(rez.text)['message'])

            for user in jdata['male']:
                rez = requests.post(API_URL+'account/registration', json=user)
                print(json.loads(rez.text)['message'])