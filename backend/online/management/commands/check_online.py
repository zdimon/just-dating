from django.core.management.base import BaseCommand, CommandError
import json
from account.models import UserProfile
from online.models import SocketConnection
from backend.cent_client import CentClient
import os


class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Checking online users')
        cent_client = CentClient()
        channels = cent_client.getChannels()
        print(channels)