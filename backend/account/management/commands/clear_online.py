from django.core.management.base import BaseCommand, CommandError
import json
from account.models import UserProfile
from online.models import SocketConnection

import os


class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Clear Online users')
        SocketConnection.objects.all().delete()
        for user in UserProfile.objects.all():
            user.is_online = False
            user.save()
