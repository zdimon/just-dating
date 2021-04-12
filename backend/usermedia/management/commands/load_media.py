from django.core.management.base import BaseCommand, CommandError
from backend.settings import FIXTURES_PATH
import json
from django.core.files import File
from account.models import UserProfile
from usermedia.models import UserMedia
import requests
from backend.settings import API_URL
from rest_framework.authtoken.models import Token
import os
from usermedia.views.add_image import AddImageView
from django.test import RequestFactory
from rest_framework.test import APIRequestFactory
factory = APIRequestFactory()
from rest_framework.test import force_authenticate
from rest_framework.test import APITestCase, APIClient
from django.core.files.uploadedfile import SimpleUploadedFile
client = APIClient()


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
                    # token = get_user_token(user['username'])
                    u = UserProfile.objects.get(username=user['username'])
                    for image in user['images']:
                        filepath = os.path.join(FIXTURES_PATH, 'images', '%s.jpg' % user['username'])
                        file = File(open(filepath, 'rb'))
                        uploaded_file = SimpleUploadedFile(image['image'], file.read(),content_type='multipart/form-data')
                        #files = {'image': open(filepath,'rb')}
                        image["image"] = uploaded_file
                        #print(dir(uploaded_file))
                        files = {'image': file}
                        # request = client.post(API_URL+'usermedia/add_image', files = files, data=image, format='multipart')
                        request = factory.post( \
                            API_URL+'usermedia/add_image', \
                            image, \
                            format='multipart')
                        #client.force_authenticate(request,user=u)
                        force_authenticate(request, user=u)
                        rez = AddImageView.as_view()(request)
                        # import pdb; pdb.set_trace()
                        print(rez.status_code)
                        rez.render()
                        print(rez.content)
                        if rez.status_code == 200:
                            print(json.loads(rez.text))
                        else:
                            print('Error!')
                            rez.rendered_content
                            #print(rez.text)

           