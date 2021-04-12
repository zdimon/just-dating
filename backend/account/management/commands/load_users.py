from django.core.management.base import BaseCommand, CommandError
from backend.settings import FIXTURES_PATH
import json
from account.models import UserProfile
import requests
from backend.settings import API_URL
import os
from django.test import RequestFactory
factory = RequestFactory()
from account.views.registration import RegistrationView

class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Loading users')
        user_file = os.path.join(FIXTURES_PATH, 'users.json')
        with open(user_file,'r') as f:
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
                request = factory.post(API_URL+'account/registration', data=user, content_type='application/json')
                rez = RegistrationView.as_view()(request)
                print(json.loads(rez.rendered_content)['message'])

            for user in jdata['male']:
                request = factory.post(API_URL+'account/registration', data=user, content_type='application/json')
                rez = RegistrationView.as_view()(request)
                print(json.loads(rez.rendered_content)['message'])